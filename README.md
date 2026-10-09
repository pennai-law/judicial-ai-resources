# Judicial AI Portal

A practical, plain-language resource for federal judges and chambers staff: use cases, failure modes, guardrails, tools, court developments, and source notes.

- **Live:** https://judges.pennai.law/
- **Deployment:** GitHub Pages from `main`, repository root
- **Build:** None

## Structure

- **Start Here** — low-risk personal learning, the capability evidence (the 2023-to-2026 trajectory and the Penn exam study), and the two objections.
- **How These Tools Work** — retrieval, generation, bias, grounding, and AI agents (three modes, checkpoints, strengths and risks).
- **Use Cases** — observed testbed practice sorted by risk; proposals; recommendations for appellate work, fenced off from observed practice; the three-question test.
- **Guardrails** — authorization, confidentiality, supervision, verification, five controls for AI agents, and a printable chambers assessment.
- **Tools** — capabilities and dated product examples, including agent products; listing is not authorization.
- **What Courts See** — professional adoption, what the research shows about AI detectors, and Penn Carey Law's tools and teaching.
- **Sources** — what each source supports and its principal limitation.

Fragments work for panes (`#use-cases`) and for targets inside a pane (`#agents`, `#agent-controls`, `#agent-products`, `#appellate`, `#detectors`, `#capability`, `#exam-study`, `#first-screen`); `portal.js` opens the pane that holds the target.

The argument remains load-bearing: retrieval systems retrieve existing material; an AI model generates. Many legal products combine both. That distinction explains why source boundaries and independent verification still matter.

## Files

- `index.html` — semantic content.
- `assets/portal.css` — screen, responsive, and print presentation.
- `assets/portal.js` — tab navigation (click, arrow keys, fragments), search, and assessment printing.
- `assets/fonts/` — self-hosted Oswald and Source Sans 3 (SIL OFL 1.1; see `NOTICE.txt`). No external requests.
- `license.html` — licensing and attribution.
- `scripts/verify_portal.py` — evidence and editorial checks.
- `tests/test_verify_portal.py` — verifier tests.

## Making changes

`main` is the live site: a merge is in front of judges within a minute or two. So changes go through a pull request.

1. Branch from an up-to-date `main` (`git fetch origin`, then branch from `origin/main`).
2. Make the change and run the checks under **Verify** below.
3. Open a pull request. The `verify` workflow runs the same checks.
4. Another collaborator reviews and approves; then merge. Read the page on judges.pennai.law after it deploys.

Follow the editorial rules below and the fuller guidance in `CLAUDE.md`, which Claude Code reads automatically when you work in this repository.

## Verify

```bash
python3 -m unittest tests/test_verify_portal.py -v
node --check assets/portal.js
python3 scripts/verify_portal.py index.html license.html
git diff --check
```

## Editorial rules

- Never fabricate a statistic, study, case, quotation, standing order, or institution.
- Keep testbed material de-identified. Private sources never enter this public repository.
- Separate observed practice, survey findings, published guidance, recommendations, and proposals.
- State denominators, populations, periods, and limitations when they affect interpretation.
- Do not call a task universally safe. On AI detectors, state only what the cited studies show, and never present a detector score as proof of authorship.
- Trace public AO claims to the October 21, 2025 letter from AO Director Robert J. Conrad Jr.
- Check names against `NAMES.md` in the private judiciary repository.

## Design

Navy frame, light reading body, matching Polk Wagner's slide theme. Navy `#05225B` for the header, hero, tab bar, feature bands, diagram panels, and footer. Gold `#F2C100` is the one accent: the current tab, key rules, and payoff lines on navy. It is never text on a light ground (1.7:1); there it is a rule only. Light blue `#82AFD3` is for labels on navy. Body text is near-black on white or very light warm grey. Oswald (400) for headings, Source Sans 3 for text.

The eight inline diagrams come from the deck at `judiciary/talk/fjc-appeals-2026/slides/diagrams/` (generated there by `build.py`). They are pasted into `index.html` with per-figure marker ids, a `<title>`, and a `<desc>`. If the deck's diagrams change, re-inline them; there is no build step here. On narrow screens each diagram scrolls sideways inside its own panel; in print the diagrams are redrawn in black outline by the print stylesheet.

`CLAUDE.md` and `AGENTS.md` carry the current design and content rules.
