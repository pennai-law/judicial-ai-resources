# CLAUDE.md

Guidance for Claude Code working in the Judicial AI Portal.

## What this is

A plain-language AI resource for **federal judges and their chambers**, built for the panel
at the 2026 Judicial Conference of the Sixth Circuit (Aug 27, Traverse City). A project of
the Penn Carey Law AI Teaching Lab.

**Status: draft, for panel review.** Publicly reachable at `judges.pennai.law`, but `noindex`
and unannounced, with a visible draft banner.

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

Still outstanding: **Judge Dominguez Braswell's running list of use cases.** The catalogue grows
when it lands.

## Do not claim AI can detect AI-generated writing

One testbed office reported that it can. That is almost certainly wrong and it contradicts Polk's
own published position — *"There are no reliable tools to detect AI-generated writing. None."*
The site may describe the human-noticed tells in AI-drafted filings (randomly bolded words,
uncanny turnarounds, legal elements paraphrased rather than quoted). It may **not** present any
of that as a detector.

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
`judges.pennai.law` — don't delete it.

Done: the repo is public, Pages is enabled from `main` root, and the DNS CNAME
(`judges` → `pennai-law.github.io`, GoDaddy zone `pennai.law`) resolves.

**Still to do before launch:** remove the `noindex` meta and the draft banner.

## Conventions

- Branch + PR for substantive changes; keep `main` deployable.
- The repo is **public** (or will be) — no chambers material, no judicial correspondence, no
  credentials. That lives in Box: `AI Teaching Lab/Judiciary/sixth-circuit-2026/`.
