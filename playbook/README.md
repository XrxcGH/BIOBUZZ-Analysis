# PLAYBOOK — how this team actually runs its season

### The operating track: how championship teams work, how a small team matches them, and where AI plugs in.

The other tracks answer *"what does the manual say"* (`../reference/`) and *"what did we find out"*
(`../research/`). **This one answers "what do we do on Tuesday."**

Calibrated throughout for **~15 students across two registered teams, two robots, modest budget,
hand tools plus 3D printing, limited mentor hours.** Where a recommendation only works with money or
labor you do not have, it says so instead of pretending.

---

## Start here

**If you are a student:** read `SMALL-TEAM-SEASON-PLAYBOOK.md` §1 (ten bullets), then the prompt file
for your job in `../tools/ai/` — `PROMPTS-programming.md`, `PROMPTS-design.md`, `PROMPTS-portfolio.md`
or `PROMPTS-scouting.md`. That is enough to be useful this week.

**If you are a mentor:** read `SMALL-TEAM-SEASON-PLAYBOOK.md` end to end, then `TWO-ROBOT-PROGRAM.md`
(the A/B decision is yours and it is the highest-leverage call of the pre-season), then
`../research/AI-IN-FTC-POLICY.md` before anyone touches AI for a judged deliverable.

**If you have twenty minutes:** `SMALL-TEAM-SEASON-PLAYBOOK.md` executive summary + the
"deliverables parity" table. That is the whole argument in two pages.

---

## Files in this directory

| File | What it is |
|---|---|
| **`SMALL-TEAM-SEASON-PLAYBOOK.md`** | **The capstone.** Week-by-week season plan from now to championship, the elite-vs-lean gap analysis, the deliverables-parity table, role chart, weekly time budget before and after AI, and the top 10 mistakes that sink small teams |
| `TWO-ROBOT-PROGRAM.md` | Running an A team and a B team on ~15 students: rosters, shared-vs-divergent design, build sequencing, sharing one practice field and one printer, the deliberate award split, and the anti-patterns that hollow out a B team |
| `BUILD-AND-FABRICATION.md` | Prototyping fast and cheap, the fabrication tiers and what each unlocks, COTS-first doctrine, and design-for-reliability |
| `AI-FOR-PROGRAMMING.md` | AI across the software workstream, with a ready-to-use `CLAUDE.md` for an FTC robot repo, worked prompts, and a blunt danger list about untested AI-written robot code |
| `AI-FOR-DESIGN-AND-ANALYSIS.md` | AI for game analysis, design trade studies, scouting data, documentation and team ops — including what AI is genuinely bad at here |
| `AI-TOOLKIT-SETUP.md` | Step-by-step setup, file conventions that make agents effective, and a 30-minute student onboarding |

## Working files in `../tools/ai/`

| File | Use |
|---|---|
| `CLAUDE.md.template` | Drop into your robot repo. Hardware map, subsystem conventions, SDK pinning, and the safety rules an agent must never violate |
| `PROMPTS-programming/design/strategy/portfolio/scouting.md` | Copy-paste prompt libraries, one per job |
| `decision-log.template.md` | One entry per engineering decision. **This is what makes the portfolio write itself** — see the capture cadence in `AWARD-ALIGNMENT-MATRIX.md` |
| `meeting-notes.template.md` | Standing agenda that doubles as portfolio input |
| `inspection-checklist.template.md` | Pre-event self-inspection against the V0 I-rules and Section 12 R-rules |
| `match-day-runbook.template.md` | Printable pit operations sheet for a small team |
| `scouting/fetch_events.py` | Working scouting tool, standard library only. Start with `dossier` — it needs no credentials |
| `verify-setup.ps1` | Checks your machine has what the toolkit needs |

## Related research (`../research/`)

`ELITE-TEAM-PRACTICES.md` · `SEASON-CADENCE.md` · `DESIGN-AND-CAD.md` · `PROGRAMMING-PRACTICE.md` ·
`TESTING-AND-TUNING.md` · `SCOUTING-AND-AWARDS.md` · `SMALL-TEAM-ECONOMICS.md` · `AI-IN-FTC-POLICY.md`

---

## Four things worth knowing before you read anything else

**The portfolio is the cheapest thing on the board.** V0 Table 4-1: **Inspire 1st = 60 advancement
points; winning the entire tournament = 40.** Judged-award points are the first tiebreaker. The
portfolio is capped at 15 pages (A201), costs $0, and judges will not click links. **But do not read
that as "the robot doesn't matter":** across 156 real 2025-26 qualifiers the median Inspire 1st winner
sat at the **14.5th percentile of qual rank** and 67% were in the event's top quartile
(`../research/SCOUTING-AND-AWARDS.md`). The portfolio is the cheapest *additional* points on the board,
not a substitute for a competitive robot — see `../research/SMALL-TEAM-ECONOMICS.md`.

**Only three awards respond to what you build.** Innovate, Control and Design. Connect, Reach and
Sustain are won by how the team *operates*, and Inspire requires being a contender in an MCI award
**and** a Team Attributes award **and** Think, simultaneously. Plan the Team Attributes leg separately;
it is not optional. Details in `../reference/AWARD-ALIGNMENT-MATRIX.md`.

**AI is explicitly allowed, with credit.** BIOBUZZ Section 6 permits AI and research aids for
portfolios *"provided they respect intellectual property rights and include a footnote or endnote
credit."* The binding constraint is not policy — it is that judged awards assess **student** work, and
a student who cannot explain their own code or design fails the interview regardless. Use AI as tutor,
reviewer and drafter; students remain authors and explainers. Read `../research/AI-IN-FTC-POLICY.md`.

**Duplicability is a design factor, not an afterthought.** Every mechanism gets built twice. COTS-heavy
designs scale to a second robot nearly free; custom-machined or individually hand-tuned ones do not.
This is weighted explicitly in `../reference/ACHIEVABILITY-RUBRIC.md` and it will reorder your
strategy shortlist relative to generic FTC advice.

---

## This week

Kickoff is **12 September 2026** — the game is not public yet, but Sections 3, 4, 5, 6 and 12 already
are, and FIRST's Game Preview (3 May 2026) has already named the scoring element: **POLLEN**. Its
dimensions — **2.8 in ± 0.1 in yellow sphere, 0.055 lb** — come from the AndyMark listing
(`am-5851_preview`, $5.50 / 3, currently back-ordered), a vendor page rather than a FIRST primary
source; FIRST's own wording is the looser *"approximately 3 in."* Treat the precise figure as
provisional until the Kickoff manual confirms it.

**Read the two halves of that separately — they point opposite ways.** FIRST says Pollen has
*"similar characteristics to the Artifacts used in… DECODE."*

- **Geometry does NOT transfer.** A DECODE ARTIFACT is ~5 in nominal; Pollen is ~2.8 in — barely half
  the diameter. Any intake throat, hopper spacing, indexer pitch or ball-count sensor gap carried over
  from last season is **mis-sized** and must be re-dimensioned.
- **Material behaviour probably DOES transfer.** "Similar characteristics" is FIRST telling you the
  compliance, grip and bounce are comparable — so DECODE intake *principles* (roller durometer,
  compliant-wheel choice, how aggressively it needs to be squeezed) are a reasonable starting point.

So prototype the geometry fresh, but keep last season's material choices as your first guess. And note
all four previewed tasks are **acquisition-side** — nothing about scoring is public, so do not commit
to a launcher on the preview alone.

So the pre-season sprint is real work, not waiting. Run the 21-day plan in
`SMALL-TEAM-SEASON-PLAYBOOK.md`: build the drivetrain and control system (R-rules are final), stand up
the software skeleton, set up the practice space, order long-lead parts before the kickoff stockout,
and prototype a 2.8 in sphere intake. **R304** — not R305 — permits fabrication before Kickoff.

---

*Front door for the playbook track. Manual analysis: the `../reference/` track, indexed in the workspace `../README.md`.
Written 2026-08-22. Produced with AI assistance — per BIOBUZZ A201, anything reaching a PORTFOLIO carries the credit.*
