# AGENTS.md

Guidance for Codex working in the Judicial AI Portal.

## What this is

A plain-language AI resource for **federal judges and their chambers**. First built for the
panel at the 2026 Judicial Conference of the Sixth Circuit (Aug 27, Traverse City); since
October 2026 a standing resource, rebuilt to match Polk's deck for the FJC National Symposium
for U.S. Court of Appeals Judges (Oct 8, 2026). A project of the Penn Carey Law AI Project.

**Status: launched.** Live and indexable at `judges.pennai.law` since Aug 28, 2026. The
`noindex` meta and the early-release banner are gone; don't reintroduce either. Do not tie the
site's framing to a single event or imply that any panel co-authored it.

## Audience — write for them, not at them

Article III district and circuit judges, magistrate judges, chambers staff. They span "I
will never use this" to a few power users. They are extremely smart, extremely busy, and
institutionally cautious. **Their skepticism is reasonable and should be treated as such.**

No hype. No exclamation points. No emoji. No "revolutionize," "transform," "game-changer."
Nothing that sounds like a vendor.

## Voice

Polk Wagner's. Direct, active, collegial, authoritative. Conclusions before evidence.
Short paragraphs. Contractions fine.

**Banned:** "leverage" (verb), "utilize," "facilitate," "stakeholders," "robust," "ensure,"
"deep dive," "unpack," "landscape," "delve," "seamless," "empower," "it's worth noting,"
"moving forward," "in terms of," "a wide range of," "navigate the complexities." Avoid tidy
two-part antitheses whose symmetry substitutes for a point. Max 1–2 em-dashes per page.

## The spine — don't lose it

AI tools are **fundamentally different** from the legal research tools judges already trust.
Search retrieves. An AI model generates.

That distinction is load-bearing for the entire site: it's what makes **hallucination and
bias legible as built-in features of the architecture, not bugs awaiting a patch**. A judge
who gets this stops asking "when will they fix it?" and starts asking "what is this safe
for?" Every other section derives from it — the use-case sorting principle, the three-question
test, the guardrails. Keep them derived. Six disconnected tabs would be a worse site.

## Accuracy — this is read by federal judges

**Never fabricate.** No invented statistics, studies, cases, quotes, standing orders, or
institutions. A plausible-sounding fiction here is far worse than a visible gap. If we don't
know, the page says so.

**Currently unverified — do NOT state as fact:**
- A "Judicial AI Consortium" of 350+ judges.
- A "USC/MIT study" on a pro se litigation spike.
- Any characterization of a claimed February 2026 AO update; no public version has been located.
- Any specific court's standing order.

**Names:** check `NAMES.md` in `pennai-law/judiciary` before writing anyone's name. Two
have already been gotten wrong on this project. "Dominguez" has a **g**. The panel:
Hon. John B. Nalbandian (6th Cir., moderating), Hon. Robert Jonker (W.D. Mich., organizer),
Hon. Maritza Dominguez Braswell (D. Colo., panelist), R. Polk Wagner (Penn Carey Law).

**Not named on the site for now (Polk, 2026-10-06):** Judge Dominguez Braswell. Do not
add her name to any page without his say-so.

**One real citation we do have:** Judge Dominguez Braswell, "Between hype and fear: Why I have
not issued a standing order on AI," Thomson Reuters Institute, Jan 15, 2026.

## 🔴 De-identification — the hard rule

The **Use Cases** tab is built from real observed practice, gathered from named sitting federal
judges in a judicial AI testbed. Polk's instruction (2026-07-13): **obscure the chambers using
them.**

**Never write** a judge's name, a clerk's name, a court, a district, or a circuit. Never write a
circuit-specific doctrine that fingerprints a court; abstract it to "a recurring multi-factor
test in your circuit". Never write identifying case details.

**Do write** aggregate, unattributed provenance: "several chambers report," "multiple chambers
independently," "one chambers found." Keep the frame that these are **observed practice from a
judicial AI testbed, reported in aggregate with chambers de-identified** — that frame is what
makes the page worth reading. Without it these are assertions; with it, they're what judges
actually do.

If a reader could identify a judge or a court from anything on the page, that is a
professional problem for Polk, not a style nit. The unabstracted source lives in Box
(`AI Teaching Lab/Judiciary/sixth-circuit-2026/research/judge-use-cases-from-testbed.md`) and
in Drive. **Neither belongs in this repo.**

## Observed vs. proposed — keep the line

"A judge does this" and "a judge could do this" are different claims, and the difference is the
whole ballgame with this audience. Proposals stay in a clearly fenced section, labeled as
proposals. **Never fill a gap with a plausible example.**

## AI detectors: a score is not proof

Position as of October 2026, matching the deck: detectors have improved, but a detector score
is a reason to ask, never a finding. The site states only what the cited research supports
(Jabarian & Imas 2025; Liang et al. 2023; Russell et al. 2025; Karr, Khvatskii, Hua & Chawla
2026, added with Polk's approval 2026-10-06, for edited and "humanized" text) and notes that
none of it tested legal filings. Do not write that detectors are useless, and do not write that they are reliable.
The site may describe the human-noticed tells in AI-drafted filings (randomly bolded words,
uncanny turnarounds, legal elements paraphrased rather than quoted). It may **not** present any
of that as a detector.

## Design: navy frame, light reading body

Matches Polk's slide theme (rebuilt October 2026; the earlier "Slip Opinion" design is retired).
Navy `#05225B` for the stripe, header, hero, tab bar, feature bands, diagram panels and footer.
Gold `#F2C100` is the one accent, used on navy for the current tab, key rules and payoff lines;
on light grounds it appears only as a rule, never as text (it fails contrast on white). Light
blue `#82AFD3` for labels on navy. The reading body is white and light warm grey with near-black
text.

Type: Oswald (headings, weight 400) and Source Sans 3 (text), self-hosted in `assets/fonts/`.
No external requests; do not add Google Fonts or any other hotlinked dependency.

The deck's diagrams appear inline as SVG in navy panels. Each needs a `<title>` and `<desc>`,
and marker ids must stay unique across the page. Every new text/background pair must pass
WCAG AA. Keep it a dependency-free static page that works at phone width and prints cleanly.

## Deploy

No build step. Static HTML, GitHub Pages from `main` root. `CNAME` pins
`judges.pennai.law` — don't delete it.

Done: the repo is public, Pages is enabled from `main` root, and the DNS CNAME
(`judges` → `pennai-law.github.io`, GoDaddy zone `pennai.law`) resolves.

## Conventions

- Branch + PR for substantive changes; keep `main` deployable.
- The repo is **public** — no chambers material, no judicial correspondence, no
  credentials. That lives in Box: `PCL AI Project/Judiciary/`.
