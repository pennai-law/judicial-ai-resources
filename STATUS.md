# Judicial AI Portal

**Updated:** 2026-10-06

**Live site:** judges.pennai.law still serves `main` as launched on August 28, 2026. Nothing described below is deployed.

**In progress, on a local branch only:** `rebuild/fjc-2026` (worktree `../judicial-ai-resources-rebuild`, branched from `origin/main`) rebuilds the portal to agree with Polk's deck for the FJC National Symposium for U.S. Court of Appeals Judges on October 8, 2026, whose closing slide points to this site. The branch has not been pushed, has no PR, and has not been reviewed by Polk. Merging to `main` deploys the public site and needs his explicit go-ahead.

What the branch changes:

- **Look.** Navy frame with a light reading body, Oswald and Source Sans 3 self-hosted, eight deck diagrams inline. The "Slip Opinion" styling and the Google Fonts dependency are gone.
- **Framing.** A standing resource, not tied to one conference. The "prepared with the AI panel" wording that two reviewers read as co-authorship is removed from the license page, the last place it appeared.
- **Testbed facts.** "20+ chambers as of September 2026"; the invented-quotation failure is "reported by three chambers."
- **New content from the deck.** Capability evidence, AI agents, agent product examples, five agent controls, appellate recommendations, AI-detector research, and Penn Carey Law's fall 2026 tools and teaching. New sources are in the Sources tab.

**Open before merge:**

- Polk's review of the branch, including the items the rebuild report lists as declined or uncertain.
- `CLAUDE.md` and `AGENTS.md` still describe the old design and say there are no reliable AI detectors. The deck now says detectors have improved but a score is not proof, and the branch follows the deck. The instruction files need Polk's revision.
- The Tools tab's use-case-to-tool matrix is still a placeholder. The branch dropped the sentence tying it to the Sixth Circuit panel and to Judge Dominguez Braswell's list; confirm that is right.
- The retired-name logo files in `assets/` (`ai-law-lab-logo.png`, `ai-teaching-lab-stacked.svg`) are not referenced by any page. They were left in place; delete them if nothing else needs them.

**Still true from before:** the portal is the base for the judiciary testbed training program, whose plan lives in the restricted Box judiciary folder, not here. The unverified items in `CLAUDE.md` stay unverified.
