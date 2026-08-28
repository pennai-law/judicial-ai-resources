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

    def test_public_release_and_evidence_sections(self):
        root = Path(__file__).resolve().parents[1]
        index = (root / "index.html").read_text(encoding="utf-8")
        license_page = (root / "license.html").read_text(encoding="utf-8")
        combined = (index + license_page).lower()
        self.assertNotIn("noindex", combined)
        self.assertNotIn("early release", combined)
        self.assertIn('id="chambers-assessment"', index)
        self.assertIn('id="sources"', index)
        self.assertIn("112 of 502", index)
        self.assertIn("22.3%", index)
        self.assertIn("october 21, 2025", index.lower())
        self.assertIn("working paper", index.lower())
        self.assertNotIn("a2j", index.lower())


if __name__ == "__main__":
    unittest.main()
