# Judicial AI Portal

A practical, plain-language resource for federal judges and chambers staff: use cases, failure modes, guardrails, tools, court developments, and source notes.

- **Live:** https://judges.pennai.law/
- **Deployment:** GitHub Pages from `main`, repository root
- **Build:** None

## Structure

- **Start Here** — low-risk personal learning and the three-question test.
- **How These Tools Work** — retrieval, generation, context limits, and bias.
- **Use Cases** — observed practice sorted by risk.
- **Guardrails** — authorization, confidentiality, supervision, verification, and a printable chambers assessment.
- **Tools** — capabilities and dated product examples; listing is not authorization.
- **What Courts See** — AI-assisted filings, professional adoption, and effects reaching chambers.
- **Sources** — what each source supports and its principal limitation.

The argument remains load-bearing: retrieval systems retrieve existing material; an AI model generates. Many legal products combine both. That distinction explains why source boundaries and independent verification still matter.

## Files

- `index.html` — semantic content.
- `assets/portal.css` — screen, responsive, and print presentation.
- `assets/portal.js` — tab navigation, search, legacy fragments, and assessment printing.
- `license.html` — licensing and attribution.
- `scripts/verify_portal.py` — evidence and editorial checks.
- `tests/test_verify_portal.py` — verifier tests.

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
- Do not call a task universally safe or claim reliable detection of AI-generated writing.
- Trace public AO claims to the October 21, 2025 letter from AO Director Robert J. Conrad Jr.
- Check names against `NAMES.md` in the private judiciary repository.

## Design

The visual register is “The Slip Opinion”: ivory, warm ink, oxblood, brass rules, and serif typography. It should read like a published judicial resource, not a software dashboard.
