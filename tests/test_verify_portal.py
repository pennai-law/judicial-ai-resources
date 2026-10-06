from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.verify_portal import verify_files


VALID = """<!doctype html><html><body>
<article data-use-case="summarize-briefs" data-risk="lower-risk"
 data-provenance="observed-testbed" data-source-refs="sedona-survey"
 data-reviewed="2026-08-28">
 <p data-field="failure-mode">May omit a material point.</p>
 <p data-field="human-check">Compare the summary with the briefs.</p>
 <p data-field="authorization">Use an authorized tool and account.</p>
</article>
<article data-source="sedona-survey" data-source-type="survey"
 data-reviewed="2026-08-28">
 <p data-field="limitation">112 of 502 sampled judges responded.</p>
</article></body></html>"""


class VerifyPortalTests(unittest.TestCase):
    def verify(self, html: str, stale_days: int = 365) -> list[str]:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "index.html"
            path.write_text(html, encoding="utf-8")
            return verify_files([path], stale_days=stale_days)

    def test_valid_portal_has_no_errors(self):
        self.assertEqual([], self.verify(VALID))

    def test_missing_provenance_is_reported(self):
        html = VALID.replace(' data-provenance="observed-testbed"', "")
        self.assertTrue(any("data-provenance" in error for error in self.verify(html)))

    def test_unknown_source_is_reported(self):
        html = VALID.replace('data-source-refs="sedona-survey"',
                             'data-source-refs="unknown-source"')
        self.assertTrue(any("unknown-source" in error for error in self.verify(html)))

    def test_duplicate_source_is_reported(self):
        source = """<article data-source="sedona-survey" data-source-type="survey"
        data-reviewed="2026-08-28"><p data-field="limitation">Limit.</p></article>"""
        self.assertTrue(any("duplicate" in error.lower()
                            for error in self.verify(VALID.replace("</body>", source + "</body>"))))

    def test_missing_required_field_is_reported(self):
        html = VALID.replace('<p data-field="human-check">Compare the summary with the briefs.</p>', "")
        self.assertTrue(any("human-check" in error for error in self.verify(html)))

    def test_forbidden_markers_are_reported(self):
        for marker in ("[VERIFY]", "Early release", "noindex", "safe and effective today",
                       "is not yet in hand"):
            with self.subTest(marker=marker):
                self.assertTrue(any("forbidden" in error.lower()
                                    for error in self.verify(VALID.replace("</body>", marker + "</body>"))))

    def test_stale_date_is_reported(self):
        html = VALID.replace("2026-08-28", "2020-01-01")
        self.assertTrue(any("stale" in error.lower() for error in self.verify(html, stale_days=365)))

    def test_presentation_and_script_are_external(self):
        root = Path(__file__).resolve().parents[1]
        index = (root / "index.html").read_text(encoding="utf-8")
        license_page = (root / "license.html").read_text(encoding="utf-8")
        self.assertNotIn("<style>", index)
        self.assertNotIn("<style>", license_page)
        self.assertIn('href="assets/portal.css"', index)
        self.assertIn('href="assets/portal.css"', license_page)
        self.assertIn('type="module" src="assets/portal.js"', index)
        css = (root / "assets/portal.css").read_text(encoding="utf-8")
        script = (root / "assets/portal.js").read_text(encoding="utf-8")
        self.assertIn(".js .tab-pane", css)
        self.assertIn("classList.add('js')", script)

    def test_public_release_and_evidence_sections(self):
        root = Path(__file__).resolve().parents[1]
        index = (root / "index.html").read_text(encoding="utf-8")
        license_page = (root / "license.html").read_text(encoding="utf-8")
        combined = (index + license_page).lower()
        self.assertNotIn("noindex", combined)
        self.assertNotIn("early release", combined)
        self.assertIn('id="chambers-assessment"', index)
        self.assertIn('id="sources"', index)
        self.assertIn("Evaluate a task", index)
        self.assertIn("Set guardrails", index)
        self.assertIn("112 of 502", index)
        self.assertIn("22.3%", index)
        self.assertIn("october 21, 2025", index.lower())
        self.assertIn("working paper", index.lower())
        self.assertNotIn("a2j", index.lower())

    def test_rebuild_is_self_hosted_and_synced_to_the_deck(self):
        import re
        root = Path(__file__).resolve().parents[1]
        index = (root / "index.html").read_text(encoding="utf-8")
        license_page = (root / "license.html").read_text(encoding="utf-8")
        css = (root / "assets/portal.css").read_text(encoding="utf-8")
        # Fonts are served from this site; nothing is hotlinked.
        for text in (index, license_page, css):
            self.assertNotIn("fonts.googleapis.com", text)
            self.assertNotIn("fonts.gstatic.com", text)
        for font in ("oswald.woff2", "source-sans-3-roman.woff2", "source-sans-3-italic.woff2"):
            self.assertIn(font, css)
            self.assertTrue((root / "assets/fonts" / font).is_file())
        # Retired names, retired styling, and superseded testbed figures stay out.
        lowered = (index + license_page).lower()
        for retired in ("teaching lab", "law lab", "eighteen", "at least five",
                        "prepared with the ai panel", "libre baskerville", "source serif"):
            self.assertNotIn(retired, lowered)
        self.assertIn("20+ chambers as of September 2026", index)
        self.assertIn("reported by <strong>three chambers</strong>", index)
        self.assertIn("Last updated October 2026", index)
        # Every id is unique, including the marker ids inside the inline diagrams.
        ids = re.findall(r'\sid="([^"]+)"', index)
        self.assertEqual(sorted(ids), sorted(set(ids)))
        # Each inline diagram carries a title and a description, and its markers resolve.
        figures = re.findall(r'<figure class="diagram".*?</figure>', index, flags=re.S)
        self.assertEqual(8, len(figures))
        for figure in figures:
            self.assertRegex(figure, r'<svg[^>]*role="img"[^>]*aria-labelledby="[^"]+"')
            self.assertIn("<title id=", figure)
            self.assertIn("<desc id=", figure)
            for ref in re.findall(r'url\(#([^)]+)\)', figure):
                self.assertIn(f'id="{ref}"', figure)
        # In-page links point at something that exists.
        for target in re.findall(r'href="#([^"]+)"', index):
            self.assertIn(target, ids)


if __name__ == "__main__":
    unittest.main()
