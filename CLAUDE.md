# CLAUDE.md

Guidance for Claude Code working in the Judicial AI Portal.

## What this is

A plain-language AI resource for **federal judges and their chambers**, built for the panel
at the 2026 Judicial Conference of the Sixth Circuit (Aug 27, Traverse City). A project of
the Penn Carey Law AI Teaching Lab.

**Status: draft, for panel review.** Not published, `noindex`, visible draft banner.

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
Westlaw and Lexis **retrieve**. Large language models **process**.

That distinction is load-bearing for the entire site: it's what makes **hallucination and
bias legible as built-in features of the architecture, not bugs awaiting a patch**. A judge
who gets this stops asking "when will they fix it?" and starts asking "what is this safe
for?" Every other section derives from it — the use-case sorting principle, the three-question
test, the guardrails. Keep them derived. Five disconnected tabs would be a worse site.

## Accuracy — this is read by federal judges

**Never fabricate.** No invented statistics, studies, cases, quotes, standing orders, or
institutions. A plausible-sounding fiction here is far worse than a visible gap. If we don't
know, the page says so.

**Currently unverified — do NOT state as fact:**
- A "Judicial AI Consortium" of 350+ judges.
- A "USC/MIT study" on a pro se litigation spike.
- The specific contents of the AO interim guidance. (That guidance **exists** and is in
  effect, and the authorized-tool list **is** limited — that much is established. Its
  contents are not.)
- Any specific court's standing order.

**Names:** check `NAMES.md` in `ai-teaching-lab/judiciary` before writing anyone's name. Two
have already been gotten wrong on this project. "Dominguez" has a **g**. The panel:
Hon. John B. Nalbandian (6th Cir., moderating), Hon. Robert Jonker (W.D. Mich., organizer),
Hon. Maritza Dominguez Braswell (D. Colo., panelist), R. Polk Wagner (Penn Carey Law).

**One real citation we do have:** Judge Dominguez Braswell, "Between hype and fear: Why I have
not issued a standing order on AI," Thomson Reuters Institute, Jan 15, 2026.

## Known gaps — leave them visible

The **Use Cases** tab is the core of the site and is deliberately thin. It's waiting on Judge
Dominguez Braswell's running list of real judge use cases. Until that lands, it carries only
what the panel actually discussed, plus a clearly fenced set of *proposals* — labeled as
proposals, not as reports of judicial practice. **Do not fill the gap with plausible
examples.** The distinction between "a judge does this" and "a judge could do this" is the
whole ballgame with this audience.

## Design — "The Slip Opinion"

Ivory `#FCFAF5`, warm ink `#1A1815`, oxblood `#6E2639` (sole accent), brass `#9A7B33`
(hairlines and ornament only — never a fill, never text). Serif throughout: Libre Baskerville
(display), Source Serif 4 (body). Google Fonts is the only external dependency.

Restraint over ornament. Hairline rules, not colored boxes. Flat — no shadows, no gradients,
no pills, no rounded cards. Active tab = oxblood underline. Letterspaced small-caps for
eyebrow labels. It should read like a published opinion, not a web app.

**This is deliberately NOT the faculty portal's look and NOT Penn's brand.** Don't drift back
toward it. If you see `#011F5B` or `#990000`, something has gone wrong.

## Deploy

No build step. Static HTML, GitHub Pages from `main` root. `CNAME` pins
`judicial-ai.ai-teaching-lab.org` — don't delete it.

**Before going live:** remove the `noindex` meta and the draft banner, flip the repo public,
and confirm the DNS CNAME record exists.

## Conventions

- Branch + PR for substantive changes; keep `main` deployable.
- The repo is **public** (or will be) — no chambers material, no judicial correspondence, no
  credentials. That lives in Box: `AI Teaching Lab/Judiciary/sixth-circuit-2026/`.
