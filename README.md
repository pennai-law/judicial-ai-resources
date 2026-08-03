# Judicial AI Portal

A plain-language resource on AI for federal judges and their chambers — what these tools
actually are, what they're safe for today, what they aren't, and how to build confidence
without taking on risk.

- **Live:** https://judges.pennai.law/
- **Status:** 🚧 **Draft, for panel review.** Publicly reachable but `noindex` and unannounced,
  with a visible draft banner. Do not circulate beyond the panel.

## Where this came from

Polk Wagner is presenting on the AI plenary at the **2026 Judicial Conference of the Sixth
Circuit** (Traverse City, Thursday, August 27). On the panel's July 13 planning call, the
group agreed to build a joint web portal for judges — matching **use cases to the best
tools, plus best practices**. Polk took the action item to build the first draft and
circulate it.

**The panel:**

| Role | Person |
|---|---|
| Moderator, presiding | Hon. John B. Nalbandian, U.S. Circuit Judge, Sixth Circuit |
| Panel organizer | Hon. Robert Jonker, U.S. District Judge, W.D. Michigan |
| Panelist | Hon. Maritza Dominguez Braswell, U.S. Magistrate Judge, D. Colorado |
| Panelist | R. Polk Wagner, Penn Carey Law |

A project of the **Penn Carey Law AI Teaching Lab** (`github.com/ai-teaching-lab`).

## The argument the site is built on

AI tools are **fundamentally different** from the legal research tools judges already trust.
Westlaw and Lexis **retrieve**. Large language models **process**. They are not better search
engines.

That distinction is the whole point, because it's what makes **hallucination and bias legible
as built-in features of how the tool works, not bugs to be patched out**. A judge who
understands this stops asking "when will they fix it?" and starts asking "what is this
actually safe for?" — and that question is what tells them how to limit risk.

## Known gaps in this draft

The site visibly marks what it doesn't know rather than inventing filler. Do not fill these
in with plausible guesses — it's going to federal judges.

- **Use Cases** — the core tab — carries only the two examples the panel actually discussed.
  It is waiting on **Judge Dominguez Braswell's running list of real judge use cases**.
- The **use-case → tool matching matrix** can't be built until that list arrives.
- **Disclosure** is marked an open question, not given a manufactured answer.

## Deploy

**No build step.** Static HTML, served by GitHub Pages ("Deploy from a branch," `main`, root
`/`). Push to `main` → live in a minute or two. The custom domain comes from the root `CNAME`
file; don't delete it.

⚠️ **Before launch:** remove the `noindex` meta tag and the draft banner from `index.html`.

## Structure

- `index.html` — the whole portal. Five tabs (Start Here · How These Tools Work · Use Cases ·
  Guardrails · Tools), inline CSS/JS, Cmd+K search. Self-contained. Tab ids are stable for
  deep links: `#start`, `#how-it-works`, `#use-cases`, `#guardrails`, `#tools`.
- `license.html` — CC BY 4.0 content, Apache 2.0 code.
- `assets/` — favicons and tool logos.

## Design

**"The Slip Opinion."** Warm ivory ground (`#FCFAF5`), near-black warm ink (`#1A1815`),
oxblood accent (`#6E2639`), brass hairline rules (`#9A7B33`). Serif throughout — Libre
Baskerville for display, Source Serif 4 for body. Google Fonts is the only external
dependency.

The look is deliberately **not** the faculty portal's, and deliberately not Penn's brand. The
audience is federal judges; the register is a published opinion, not a web app. Restraint over
ornament: hairline rules, no drop shadows, no gradients, no pills, no emoji.

## Rules

- **Never fabricate.** No invented statistics, studies, cases, quotes, or standing orders.
  This is read by federal judges; a plausible-sounding fiction is worse than a visible gap.
- **Names go through `NAMES.md` in the `ai-teaching-lab/judiciary` repo first.** Two have
  already been gotten wrong on this project. "Dominguez" is spelled with a **g**.
- The **AO has interim guidance in effect** and its authorized-tool list is limited. That much
  is established. Do not characterize its specific contents.
- Sensitive source material lives in Box (`AI Teaching Lab/Judiciary/sixth-circuit-2026/`),
  never in this repo — which is **public**.

## Related

- `ai-teaching-lab/judiciary` (private) — the workstream, the talk, the source material.
- `ai-teaching-lab/penn-law-ai-resources` (public) — the faculty portal this was adapted from.
