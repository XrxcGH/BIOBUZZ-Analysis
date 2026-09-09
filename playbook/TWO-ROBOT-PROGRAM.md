# TWO-ROBOT PROGRAM — the operating model for an A team and a B team with ~15 students

**Scope.** One organization, two registered FTC teams, two robots, ~15 students total (≈8 / 7), modest
budget, limited fabrication, limited mentor hours. BIOBUZZ 2026-27, presented by RTX.

**What this file is.** The *operating model*: who is on which team, whether the two robots share a design,
what the B team is for, how you sequence two builds, how you ration a shared shop, how you run two pits at
one event, how you split the awards, and what the second robot actually costs.

**What this file is not.** It is not the rules reference and not the award reference. Those exist:

| Question | Go here |
|---|---|
| "Is *X* legal for two teams from one org?" | `research/TWO-TEAM-PROGRAM-RULES.md` — every rule, every citation |
| "Which award does this robot argue for?" | `reference/AWARD-ALIGNMENT-MATRIX.md` — the design → award → materials grid |
| "What are the award criteria?" | `reference/AWARD-CATALOG-BIOBUZZ.md` |
| "How achievable is this design for us?" | `reference/ACHIEVABILITY-FACTORS.md` — especially **F2 Duplicability** |
| "Which archetype?" | `reference/ROBOT-ARCHETYPE-LIBRARY.md` |
| "What does it cost?" | `research/SMALL-TEAM-ECONOMICS.md` |
| "What week is it?" | `research/SEASON-CADENCE.md` |
| "How do we scout?" | `research/SCOUTING-AND-AWARDS.md` |

**This file does not re-derive rules already derived elsewhere.** Where a rule matters operationally it is
cited inline; where the full derivation matters, the cross-reference points at it.

---

## Evidence labels

| Label | Meaning |
|---|---|
| **[C]** CONFIRMED-BIOBUZZ | Quoted or paraphrased from BIOBUZZ V0 (2026-07-31), from a section **already final** for BIOBUZZ: §3 (I), §4, §5 (E), §6 (A), §12 (R) |
| **[O-FTC]** | Official FIRST publication scoped to FTC, outside the Competition Manual |
| **[O-FRC]** | Official FIRST publication scoped to **FRC**. Persuasive, **not binding on FTC** |
| **[H]** HISTORICAL | Prior-season FTC manual (DECODE 2025-26 / INTO THE DEEP 2024-25). **Not a BIOBUZZ fact** |
| **[COMM]** | Named person on a public forum. Opinion, not rule |
| **[J]** JUDGMENT | Inference from cited facts. Flagged as inference |
| **UNVERIFIED** | Not confirmable from the corpus or the open web |

> **Standing caveat.** BIOBUZZ V0 §§8-11, 13, 15 are **placeholders deferred to Kickoff (2026-09-12)**. **§14 League Play is final text, not a placeholder.**
> Anything in this file about DRIVE TEAM composition, match counts, or alliance selection is **[H]** and must
> be re-verified against the Kickoff manual. Everything about registration, inspection, event conduct,
> awards and robot construction is **[C]** and will not move.

> **Rule-ID correction, carried forward.** `pdftotext -layout` mis-aligns the rule-ID margin column in
> several V0 sections. Two corrections used throughout this file, both re-derived from PDF text coordinates
> (p.71 and p.50):
> - **R304\*** is *"Custom software, designs, and parts can be reused year-to-year. ROBOT software, designs,
>   and FABRICATED ITEMS created before Kickoff are permitted."* — **both** clauses are R304. **R305\*** is
>   the SCORING-ELEMENTS-not-for-construction rule. `reference/ROBOT-ARCHETYPE-LIBRARY.md` §5.1 splits these
>   across R304/R305; prefer the reading here.
> - **A208\*** is *"One adult silent observer is welcome"*; A206 is the timer rule and A207 is the
>   uninterrupted-5-minutes rule.

---

# 1. Student allocation

## 1.1 The roster math, stated honestly

| Fact | Value | Label |
|---|---|---|
| Competition Manual roster cap | **none — V0 is silent** | [C] |
| FIRST's published cap | "up to 15 team members, grades 7-12" | [O-FTC] `ftc-docs` |
| FIRST's published typical band | "Many teams include 8-12 students" | [O-FTC] get-started |
| Your split | **8 / 7** | — |
| Where that lands you | **Both teams below FIRST's own typical floor of 8** | [J] |

**[J] Say this out loud at the start of the season.** Splitting 15 students produces two under-strength
teams, not two normal teams. Every structural decision in this file — shared design, shared scouting,
staggered meetings, B-first build order — exists to buy back the capability that the split gives away. A
program that splits *and* runs both teams as if they were full-size will field two mediocre robots and two
thin portfolios.

**The counterweight, which is real:** two teams means two award slots (**A215\*** caps *each team* at one
judged award — the cap is per team, and no anti-sweep rule exists in §6) [C]; two independent advancement
point totals (§4, no organizational cap) [C]; two judge-feedback forms per event (**A212\***) [C]; and
roughly twice the hands-on hours per student, which is the argument every multi-team program makes and the
one the community consistently endorses [COMM] — see `research/TWO-TEAM-PROGRAM-RULES.md` §9.2.

## 1.2 Roles that MUST exist on each team, separately

These cannot be covered once for the organization. Each is per-team by rule.

| # | Role | Minimum count | Why it cannot be shared | Label |
|---|---|:---:|---|---|
| 1 | **Lead Coach 1 + Lead Coach 2** (adults, YPP-screened) | 2 per team | **I101.A.iii** requires two screened adults in those Dashboard slots for each registered team | [C] |
| 2 | **Responsible adult present the whole event** | ≥1, "preferably 2" | **I103\*** — read per team; two teams at one event ⇒ ≥2 adults, realistically 4 | [C] |
| 3 | **Check-in adult + ≥1 student at the venue** | 1 adult + 1 student | **I102** — no later than 45 min before qualification matches, *per team*, in the same window | [C] |
| 4 | **≥2 STUDENT interview representatives** | 2 per team | **A204.A** — "no fewer than 2 STUDENT representatives for teams of 2 STUDENTS and larger" | [C] |
| 5 | **Adult silent observer at judging** (optional but wanted) | 1 per session | **A208\*** — "One adult may attend the judging session." One *per session*; concurrent slots need two adults | [C] |
| 6 | **Students who present the ROBOT at inspection** | ≥1 per team | §3.3.1 — student team members present their ROBOT; **E115\*** each robot needs its own complete inspection pass | [C] |
| 7 | **Builders of each MAJOR MECHANISM** | per team | **R101\*** — the ROBOT and its MAJOR MECHANISMS must be built by the team that registered and intends to use it | [C] |
| 8 | **DRIVE TEAM** (drivers + human player + drive coach) | up to 4, ≤1 non-student | **[H]** DECODE §10.2 — "a set of up to 4 people from the same FIRST Tech Challenge team". BIOBUZZ §10 is a placeholder | [H] |
| 9 | **Student rep at ALLIANCE selection** | 1 per team | **[H]** DECODE T701 — no rep ⇒ ineligible for playoffs. BIOBUZZ §13 is a placeholder | [H] |

## 1.3 What CAN be shared across the two teams

| Shared item | Legal? | Authority |
|---|---|---|
| Mentors / Lead Coaches (same humans in both teams' slots) | **Yes** — I101.A.iii does not require distinct people | [C]; **UNVERIFIED** whether the FIRST Dashboard permits one person in a Lead Coach slot twice — confirm before registering |
| CAD files, drawings, design concepts | **Yes** | [C] **R101\*** note: "developing game strategy" |
| Software, autonomous code, the whole repo | **Yes, named explicitly** | [C] **R101\*** note: "writing software" |
| Fabrication labour — A prints/cuts parts for B | **Yes, named explicitly** | [C] **R101\*** note: "fabricating elements, supporting construction" |
| Individual COMPONENTS and sub-MECHANISMS | **Yes, named explicitly** | [C] **R101\*** note: "contributing COMPONENTS, and/or MECHANISMS" |
| A gearbox assembly | **Yes — explicitly *not* a MAJOR MECHANISM** | [C] R101 exclusion list, item A |
| COTS parts, COTS drive chassis | **Yes** | [C] **R301\***, R101 exclusion list item C |
| Tools, spares stock, carts, pit kit | **Yes** — nothing restricts it | [C] no prohibiting rule; **E107.B\*** covers cross-pit work |
| Scouting data collection and the scouting database | **Yes** | [O-FRC] sibling guidance: "Sharing scouts or having Sibling Teams help each other at the event is still allowed" |
| Outreach *events* | **Yes — but each team writes its own role in it** | [C] A201 sets format limits only; [O-FTC] Judging Process Guide trains judges to probe duplicate outreach claims |
| Year-to-year reuse and pre-Kickoff fabrication | **Yes** | [C] **R304\*** — reuse year-to-year **and** FABRICATED ITEMS created before Kickoff |

## 1.4 What CANNOT be shared

| Cannot share | Why | Authority |
|---|---|---|
| The physical ROBOT | Each team inspects and plays with **1 ROBOT**; that robot must have been built by the registering team | [C] **E117\*** + **R101\*** + **I301\***; full derivation in `research/TWO-TEAM-PROGRAM-RULES.md` §3 |
| A whole **MAJOR MECHANISM** built by the other team | R101's load-bearing clause | [C] **R101\*** |
| The students who speak to judges | ≥2 student reps **per team**; a judge who sees the same faces twice sees one team with two numbers | [C] **A204.A**; [O-FRC] "students speaking to judges must be distinguished for each event" |
| The electronics allowance | Each team's total across **all** configurations must independently meet §12 caps — a shared parts pool does **not** create a shared allowance | [C] **I302\*** + **R503\*** (8 motors, 8 servos per ROBOT) |
| An inspection pass | Practice-field access requires *that* robot to have passed a complete inspection | [C] **E115\*** |
| A recording of one team's interview to prep the other | No photo/video/audio during the Initial Interview | [C] **A210\***, **E116\*** |
| The portfolio text | No rule forbids it; it is simply the fastest way to lose both awards | [C] A201 (format limits only); [O-FTC] judges assess each sibling team "individually" |

## 1.5 The recommended rosters

Two teams, no dual-rostering. **[J] Do not dual-roster in a 15-student program.** V0 is silent and FIRST's
sibling guidance permits it [O-FRC], but the only thing it buys you is a body, and it costs you the one thing
you cannot buy back: a clean answer to the judges' sibling probe. See §4.3.

### A team — 8 students

| # | Primary role | Secondary role | Event-day job |
|---|---|---|---|
| A1 | **Driver 1** | Software 2 / sensors | Driver 1 |
| A2 | **Driver 2 / Human Player** | Spares runner | Driver 2 / HP |
| A3 | **Drive Coach / Strategist** | Alliance list owner | Drive coach; alliance-selection rep |
| A4 | **Software lead** (auto + teleop) | Control-award narrative owner | Pit software; interview rep |
| A5 | **CAD lead** | BOM + cut list | Pit mechanical; interview rep |
| A6 | **Build lead** | Inspection owner | Pit mechanical; inspection presenter |
| A7 | **Documentation / portfolio lead** | Interview lead | Interview rep; portfolio hand-off (A202) |
| A8 | **Scouting lead** | Logistics (batteries, pit kit) | Match scouting (see §7.3) |

### B team — 7 students

| # | Primary role | Secondary role | Event-day job |
|---|---|---|---|
| B1 | **Driver 1** | Build 2 | Driver 1 |
| B2 | **Driver 2 / Human Player** | Scouting collector | Driver 2 / HP |
| B3 | **Drive Coach / Strategist** | Logistics | Drive coach; alliance-selection rep |
| B4 | **Software lead** | Sensors | Pit software; interview rep |
| B5 | **CAD + Build lead** *(merged)* | Inspection owner | Pit mechanical; inspection presenter |
| B6 | **Documentation / portfolio lead** | Interview lead | Interview rep; portfolio hand-off |
| B7 | **Scouting lead** | Spares | Match scouting |

**Rules that make these rosters survive contact with reality:**

1. **Every role names a backup on Kickoff Sunday.** No exceptions, CAD least of all — see
   `research/SEASON-CADENCE.md` §8.6. Assume 80% attendance; some meetings will be three people.
2. **Minimum crew = 3.** Below three, the meeting converts to a documented solo task, not a cancellation.
3. **Two drivers plus one trained backup per team.** An illness the morning of a qualifier must not cost the
   season.
4. **The interview roster is fixed and separate.** Name the ≥2 A-team reps and the ≥2 B-team reps in
   September, and never cross them. **A204.A** [C].

## 1.6 Staffing when only a few students can program or CAD

This is the real constraint, and the honest answer is that **the scarce skill gets shared and the scarce
*explanation* does not.**

| Scarce skill | What R101 lets you share | What each team must own itself | Staffing pattern |
|---|---|---|---|
| **Programming** | The entire codebase. R101's note names "writing software" as permitted assistance [C] | A student on **that team** who can explain the control system to judges. **Table 6-8 R1** (Control Award) asks the team to identify its control components, the challenge each solves, and its function [C] | One **shared software architect** (rostered on one team only) writes the library. Each team has a **software owner** who configures, tunes, and can narrate it. The owner writes the team's own Control/portfolio pages |
| **CAD** | The master model, the drawings, the print files [C] R101 note, R304\* | The cut list and the assembly for *its own* MAJOR MECHANISMS [C] R101 | One CAD lead total is survivable **only if the chassis is shared**. Each team supplies a "model reader" who can open the assembly and produce its own BOM. Divergent mechanisms need a second CAD-capable student — this is a hard gate on §2's divergent model |
| **Vision / sensors** | Camera mount geometry, pipeline code [C] R101 note | Its own calibration data and its own failure log | Standardize the camera pose across both robots. Written once, deployed twice — see `reference/ROBOT-ARCHETYPE-LIBRARY.md` §5.3 rule 2 |
| **Driving** | Nothing useful | Its own drivers, always | **[H]** DRIVE TEAM is "from the same team" (DECODE §10.2). Do **not** parachute A's driver onto B's controls |

**[J] The share-the-pattern-not-the-part rule, applied to people.** A team's student may sit with B's student
and teach them to write the tuning loop. A team's student may not write B's tuning loop while B's students
watch. The first produces a B student who can answer *"How did you decide who did what?"*; the second
produces a B student who cannot. That question is on the published list judges are told to ask sibling teams
[O-FTC].

**Apprenticeship pattern that works with three programmers across two teams:**

| Weeks | A-team software | B-team software |
|---|---|---|
| Pre-season → W2 | Architect + A owner build the shared library together | B owner sits in, pair-programs, owns the hardware map |
| W3 → W5 | A owner extends for A's mechanism | B owner ports the library to B's chassis **alone**, architect on call |
| W6 → event | A owner tunes A | B owner tunes B, writes B's Control pages |
| Between events | Architect does not touch B's repo without B asking | B owner owns the regression list |

---

# 2. Same design or different designs?

## 2.1 The three models

| | **M1 — Shared design** | **M2 — Divergent design** | **M3 — Hybrid (recommended)** |
|---|---|---|---|
| Drivetrain | Identical | Different | **Identical** |
| Control system + wiring layout | Identical | Different | **Identical** |
| AUTO codebase | Identical | Separate | **Identical, different paths** |
| Intake / acquisition | Identical | Different | Shared CAD, tuned per robot |
| **Scoring / delivery mechanism** | **Identical** | **Different** | **Different** |
| Endgame | Identical | Different | A attempts; B parks |
| Legality | [C] Nothing forbids twin robots; [O-FRC] "Teams may design multiple copies of the same ROBOT... but each team must have their own unique physical ROBOT" | [C] Legal | [C] Legal |

## 2.2 The honest trade-off table

| Dimension | M1 Shared | M2 Divergent | M3 Hybrid |
|---|---|---|---|
| **Mentor-hours** (the binding constraint) | Lowest — one engineering effort | **Highest — two full efforts** | Low-moderate: one drivetrain effort + two mechanism efforts |
| **Cost per unit of learning** | Best | Worst | Good |
| **Spares interchange** | **Total.** **I303.E/F** — identical COMPONENT and identical MECHANISM swaps need **no re-inspection** [C] | **None.** Every spare is single-purpose | **Partial** — drivetrain, electronics, wheels interchange; scoring mechanisms do not |
| **Tuning transfer** | One tuning effort covers both | Two tuning efforts | Drivetrain/auto tuning transfers; mechanism tuning does not |
| **Correlated failure** | **Both teams fail the same way.** A wrong archetype ends both seasons | Hedged — one design being wrong costs one team | **Hedged where it matters.** A wrong drivetrain is rare; a wrong scoring strategy is common |
| **B-team original engineering** | **Weakest.** B assembles a design it did not choose | Strongest | Adequate — B owns a real MAJOR MECHANISM end to end |
| **Judging exposure** | **Highest risk.** [O-FTC] judges are told to expect "multiple teams have a similar design for their robot" and to probe it | Lowest | Low — the two teams' Innovate/Design claims are about different mechanisms |
| **Distinct award stories** | Hard — both teams argue the same machine | Easy | Easy — see §8 |
| **Duplicability score** (`ACHIEVABILITY-FACTORS.md` F2, weight 9) | 5 | 1-2 | 3-4 |
| **Second-robot BOM** | Cheapest (identical order, volume pricing) | Most expensive | Moderate |

## 2.3 The recommendation

> ### **Default to M3 — Hybrid: shared drivetrain, shared control system, shared AUTO codebase, divergent scoring mechanism.**

**Why, in one paragraph.** The mentor-hour cost of a two-team program is concentrated almost entirely in
*chassis integration, wiring, and getting a robot to drive and run an auto* — work that is identical between
the two robots and produces no distinct award story on either. The *pedagogical* and *judging* value is
concentrated almost entirely in choosing, prototyping, and defending a scoring mechanism. M3 shares the first
and splits the second. It is the only model that does not force you to choose between mentor bandwidth and
the B team's legitimacy.

**Five supporting facts:**

1. **[C] R101\* explicitly blesses the shared half.** "Fabricating elements, supporting construction, writing
   software, developing game strategy, contributing COMPONENTS, and/or MECHANISMS" are all named as *not*
   prohibited. Only MAJOR MECHANISMS must be built by the team that uses them. M3 draws the line exactly where
   R101 draws it.
2. **[C] R304\*** — designs and pre-Kickoff FABRICATED ITEMS carry over. A shared drivetrain built in
   pre-season is legal, reusable next season, and amortized across two robots.
3. **[C] I303.E / I303.F** — identical COMPONENT and identical MECHANISM replacements need no re-inspection.
   A shared drivetrain means A's spare gearbox is legally droppable into B's robot mid-event. A shared scoring
   mechanism would extend that, but see §4 for why you do not want that dependency.
4. **[O-FTC]** the judges' sibling script asks *"Were there any specific roles or tasks that each team member
   took ownership of?"* — asked explicitly about "coming up with a robot design used by Sibling Teams." Under
   M3, both teams have a truthful, specific answer about the mechanism they own.
5. **[COMM]** the practitioner pattern. `saatb`: "4766 opts to build a more simple bot and 4522 goes all
   out. this year **4766 beat 4522** at both of their regionals that they shared!" `AndrewFRC135` runs
   "distinctly different" strategy and design goals as *program policy*, not a FIRST rule. Meanwhile the
   mentors in CD t/406178 state plainly that they **did not have the bandwidth to supervise two separate
   designs** — which is the M2 objection, stated by people who tried it.

**What M3 looks like concretely** (game-agnostic; instantiate on 2026-09-12):

| Subsystem | A team | B team | Shared? |
|---|---|---|---|
| Chassis footprint, motor ports, camera pose | Standard | **Identical** | ✅ Same CAD, same cut list |
| Drivetrain | Standard | **Identical** | ✅ Each team assembles its own copy (R101) |
| Control Hub / Driver Hub / wiring layout | Standard | **Identical** | ✅ Same harness drawing |
| AUTO codebase | Full path + vision branch | Same codebase, shorter path | ✅ One repo, two configs |
| Intake / acquisition | Shared CAD, tuned for A's delivery | Shared CAD, tuned for B's delivery | ✅ Same files, separate builds |
| **Scoring / delivery** | The season's **highest-value repeatable task** | The season's **cheapest repeatable task** | ❌ **Divergent — this is the point** |
| Endgame | Attempt if worth ≥5 cycles | Park only | ❌ |

## 2.4 When to switch models

Write these triggers on the whiteboard on Kickoff Sunday. Check them at gate **G3 (mechanism selection, Sun
Oct 4)** and **G4 (design freeze, Sun Oct 18)** — dates from `research/SEASON-CADENCE.md` §2.2.

### Switch DOWN to M1 (fully shared) if any of these is true at G3

| Trigger | Reason |
|---|---|
| Fewer than two mentors available on a typical build night | M3's second mechanism has no supervisor |
| The B team has ≥4 students with no prior build season | They cannot carry an independent mechanism to G4 |
| B's mechanism concept is still unresolved at G3 (Oct 4) | It will not be reliable by the first event; a copy of A's proven mechanism will be |
| Only one CAD-capable student exists | M3 needs a second model author |
| B's mechanism scores **F2 Duplicability ≤ 2** or **F1 Fabrication ≥ 4** in `ACHIEVABILITY-FACTORS.md` | You are building the hard thing twice |

**If you switch to M1, pay the judging tax deliberately:** B claims the *whole-robot Design* case or the
*Think* process case, never the same creative mechanism A claims. See §8.4.

### Switch UP to M2 (fully divergent) only if ALL of these are true at G3

| Trigger | Reason |
|---|---|
| The BIOBUZZ scoring table has **two genuinely separable value paths** at very different cost | Otherwise M2 is two solutions to one problem |
| ≥3 mentor-nights per week are actually staffed | M2 doubles the supervision load |
| B team has ≥3 returning students including a build lead and a CAD-capable student | M2 needs B to be self-sufficient |
| Both drivetrains are still *identical* in practice | A truly divergent drivetrain buys nothing and costs a whole spares inventory |

**[J] In practice M2 is rarely correct for 15 students.** It is the right answer for a 40-student program.
Record it as considered-and-rejected in both portfolios — that is a Think R1.C decision-matrix artifact for
free (`reference/AWARD-ALIGNMENT-MATRIX.md` M4).

### Never do this

| Anti-model | Why |
|---|---|
| **Both teams build the same complex mechanism** (tall stacker, tuned launcher, multi-stage lift) | `ACHIEVABILITY-FACTORS.md` scores the stacker at Duplicability 2, Cost 5, Complexity 5. You will finish one and abandon the other |
| **Divergent drivetrains** | Doubles the spares inventory, kills I303.E/F interchange, and buys no award story — Design R2 grades "the entire ROBOT," not the chassis |
| **B copies A one design revision behind** | B is then permanently unfinished. If you copy, copy the *frozen* design and finish **first** (§5.3) |

---

# 3. What the B team is for

> ## The B team is a competitive FTC team. It is not a parts donor, a farm team, a driver-development program, or a waiting room.

## 3.1 The rules-grounded case

| Fact | Consequence for the B team | Label |
|---|---|---|
| **A215\*** caps *each team* at one judged award; the cap is per team, and §6 contains no anti-sweep rule | The B team is a second, fully independent award slot | [C] |
| §4 advancement is a per-team point ranking with no organizational cap | The B team can out-advance the A team, and sometimes does | [C] |
| **A213\* / A214\*** (Inspire home-region limit; 1st-place Inspire once per season from a QT/LT) are per team | An A-team Inspire win does **not** touch the B team's eligibility | [C] |
| §6.1.1 — judges "cannot consider information from outside of what they have seen or heard at the current event"; explicitly disallowed inputs include "Past performance" and "**Personal knowledge of a team**" | **This protects the B team from being marked down as new — and means it gets zero credit for anything it does not say itself** | [C] |
| **A212\*** every team gets a judging feedback form | Two teams ⇒ two feedback forms per event. Almost nobody uses these | [C] |
| §6.3.4 Reach Required 2 — "successful recruitment of new teams, coaches, mentors, or volunteers who have not previously participated"; §6.3.5 Sustain Required 3 — "clearly defined team roles and an intentional process for preparing future student leaders" | **A well-run A/B structure is literally on-criteria for both awards**, from both sides | [C] |

**[J] The single most important sentence in the awards section, for a two-team org:** §6.1.1 means the
program's overall excellence does not rub off on the B team. There is no mechanism by which it can. Whatever
the B team cannot say in its own ten minutes and its own fifteen pages does not exist.

## 3.2 The anti-patterns that destroy B teams

Each is a real failure mode with a named countermeasure. None of these is a rule violation — that is precisely
why they happen.

| # | Anti-pattern | What it looks like | Countermeasure | Anchor |
|---|---|---|---|---|
| **AP1** | **Mid-event cannibalization** | A's mechanism breaks; B's identical spare goes onto A's robot; B plays the rest of the event crippled | **Written no-strip rule.** Spares belong to the *program's spares box*, not to the B robot. If the box is empty, A plays broken. Post the rule in both pits | Legal per [C] **I303.E/F**, but [C] §6.1.1 means B is judged only on what it can show. `TWO-TEAM-PROGRAM-RULES.md` X4 |
| **AP2** | **Season-long parts donor** | Every scarce motor, every good battery, every printed part routes to A first | **Parity procurement.** Both robots' BOMs are ordered in the same purchase order, in the same quantities, and B's parts are bagged and labelled *before* A's build starts | [J]; **R601\*** each robot needs its own single main battery |
| **AP3** | **The waiting-room narrative** | "B team is where the freshmen go until they're ready" — said by adults, absorbed by students | **Name the B team's competitive goal on day one** and put it on the whiteboard next to A's: a target award, a target ranking, a target auto success rate. Never describe B in terms of A | [COMM] `geekygirlsarah`: teams whose "vibe is always that FTC doesn't really matter"; `ElectraLucky5413`: "the 'middle child'" |
| **AP4** | **B builds nothing it chose** | B assembles A's design, from A's CAD, on A's schedule | **B owns one MAJOR MECHANISM end to end** — concept, prototype, test data, build, tuning. This is the M3 model in §2 and it is also **R101\*** compliance | [C] **R101\***; [O-FTC] judges' probe: "Were there any specific roles or tasks that each team member took ownership of?" |
| **AP5** | **B is always second on the field** | Practice-field time is allocated by whoever asks; A always asks first | **Written field schedule, published before the season** (§6.2). B gets the *earlier* slot whenever B's robot is less finished — field time is worth more to an untuned robot | [J]; nothing regulates your home field, so this is pure program policy |
| **AP6** | **B's robot is finished last** | B copies A's frozen design, so B starts three weeks behind and never drives | **Build the B robot first** (§5.3). The B robot is the de-risking build | [J]; `ROBOT-ARCHETYPE-LIBRARY.md` §5.3 rule 3 |
| **AP7** | **B gets no mentor** | Both teams meet the same night; the one mentor floats between them and serves neither | **Stagger meeting nights.** Never split one mentor across two simultaneous teams | [COMM] `NatsirtD`: "Meetings are generally on alternating days"; `Mr.Dave6327`: same night ⇒ "less available time for the mentors to support both teams" |
| **AP8** | **One student writes both portfolios** | The documentation lead is good, so they do it twice | **Two documentation leads, one per team, who do not read each other's drafts before submission.** Same facts, separate authorship (§8.5) | [C] A201 permits it; [O-FTC] judges assess each team "individually" and probe duplicated claims |
| **AP9** | **A's students speak in B's interview** | The confident presenters get borrowed | **Fixed, disjoint interview rosters named in September.** Add a visible team-number badge to the shared org shirt | [C] **A204.A**; [O-FRC] "students specify to the judges which team they are talking on behalf of" |
| **AP10** | **B is staffed as A's pit crew at events** | B's students spend the day fetching for A | **Both pits are staffed independently at all times.** B's scouting assignment (§7.3) is B's *own* competitive work, not a favour to A | [C] **I103\***, **E702\*** (≥1 rep per team observing ceremonies) |
| **AP11** | **B's award target is A's leftovers** | "A is going for Control, so B can try Design I guess" | **Assign primaries in September and hold them** (§8) | [C] **A211** Table 6-1 — at a 4-10 team event only *one* MCI award exists at all |
| **AP12** | **B is entered at fewer events to save money** | B plays one qualifier, A plays three | **Each team's advancement window is its own first three chronological entry-level events** [C] §4. Cutting B's schedule cuts B's season, not A's cost — and event fees are the *smallest* line in §9's delta table |

## 3.3 The B team's own success criteria

**[J] Write these on the board in September. They must not reference the A team.**

| Criterion | Target |
|---|---|
| Robot drives, scores, and finishes every match | 6 consecutive full matches with no failure at gate G6 |
| Owns one MAJOR MECHANISM it chose, prototyped, tested and built | Test data table exists by G3 (Oct 4) |
| AUTO scores repeatably | ≥8/10 at gate G6 |
| Its own portfolio, its own interview, its own students | Fixed roster of ≥2 interview reps (A204.A) |
| A named primary award target and a hedge | See §8 |
| Scouting output the program actually uses | Its match-scouting stream feeds the shared alliance list (§7.3) |
| Is a team another team wants to pick | See `research/SCOUTING-AND-AWARDS.md` §6.3 |

---

# 4. Judging with two teams — the three questions

[O-FTC] The FTC **Judging Process Guide** (Rev. 25-26.3) has a section *"Judging Teams with Close Affiliations
(Sibling Teams)"* that tells judges sibling teams "are considered separately for all awards," warns that
"multiple teams have a similar design for their robot or claim the same outreach activities," and gives judges
three clarifying questions. Full quotation and sourcing: `research/TWO-TEAM-PROGRAM-RULES.md` §8.2.

| Judge's question | A bad answer | A good answer |
|---|---|---|
| **"How did you decide who did what?"** / "Were there any specific roles or tasks that each team member took ownership of?" | "The A team came up with it." | "We share a drivetrain because we only have one CAD lead. I own our deposit chute — I built three versions and picked the one that jammed least." |
| **"Who contacted ___ to coordinate your outreach activity?"** | "Our coach set it up for both teams." | "I emailed the library. The A team ran the morning session and we ran the afternoon one; here's our attendance count." |
| **"How did you ensure the outreach activity, or robot design, aligned with your team plan?"** | "It's the same plan." | "Our plan is a reliable low-cycle robot, so we did the elementary demo with the simplest mechanism — we could actually let kids drive it." |

**[J] Drill these until every student on both teams can answer for their own team, cold, in 20 seconds.** This
is a 15-minute agenda item, three times a season. It is the highest-value non-build activity in the two-team
program, because it is the exact failure the judges are trained to look for.

**Two supporting practices:**

- **Badges.** Matching org shirts make sibling teams indistinguishable to judges. Add a visible team-number
  badge or a differently-coloured accessory. [O-FRC] "If the Sibling Teams share apparel, it is recommended
  that the students specify to the judges which team they are talking on behalf of."
- **Two adults on judging day, minimum.** **A208\*** permits one adult silent observer *per session*, and
  slots may collide. [C]

---

# 5. Build sequencing across two robots

## 5.1 The controlling calendar

From `research/SEASON-CADENCE.md` §2. Weeks numbered from Kickoff; **W0 = Sep 12-13, 2026**.

| Gate | Date | Two-robot meaning |
|---|---|---|
| **G0 Pre-season ready** | Sep 11 | **Both** chassis drive a figure-8. This is the single most important two-robot deadline |
| **G1 Archetype chosen** | Sun Sep 13 | Two paragraphs, not one: A's identity and B's identity, each with a "does not do" list |
| **G2 Strategy frozen** | Sun Sep 20 | Two ranked scoring-task lists; the shared/divergent boundary written down |
| **G3 Mechanisms selected** | Sun Oct 4 | **Model-switch checkpoint** (§2.4). Each team's chosen mechanism has one page of test numbers |
| **G4 DESIGN FREEZE** | Sun Oct 18 | **Both** BOMs ordered in one purchase order. Nothing new after this date |
| **G5 Robot alive** | Sun Nov 1 | **B robot alive by Oct 25** — one week early. See §5.3 |
| **G6 Competition ready** | Sun Nov 8 | Both: auto ≥8/10, 6 consecutive failure-free matches |
| **G7 Dress rehearsal** | Thu Nov 12 | One rehearsal, run as a two-team event: two check-ins, two inspections, two interviews |

**Hard external dates** [O-FTC] `2026-27_BIOBUZZ_ImportantSeasonDates.pdf` V26-27.1:
Kickoff **Sep 12**; Q&A opens **Sep 28, 12:00 p.m. ET**; earliest League Meet / Qualifying Tournament
**Oct 15**; AndyMark game sets start shipping **Sep 14** (the Aug 7 pre-order wave has passed — assume you
have no official game elements in September).

## 5.2 The shared-vs-duplicated BOM

**The organizing principle: duplicate what plugs into a robot; share what sits on a bench.**

### Must be duplicated (one per robot)

| Item | Qty for two robots | Rule / reason | Label |
|---|---|---|---|
| ROBOT CONTROLLER — REV Control Hub (REV-31-1595) | **2** | **R701\*** — 1 programmable ROBOT CONTROLLER per robot | [C] |
| OPERATOR CONSOLE — REV Driver Hub (REV-31-1596) or Android device + gamepads | **2 sets** | **R901\*** | [C] |
| Main battery, installed | **1 per robot**, minimum **2-3 per robot** in rotation | **R601\*** — "1 and only 1 approved 12V NiMH main battery," from the Table 12-4 list | [C] |
| Drivetrain motors + wheels | 2 sets | Each robot is a separate ROBOT under **R503\*** (8 motors / 8 servos each) | [C] |
| Mechanism motors and servos | 2 sets | **I302\*** — each team's electronics total across **all** configurations must independently meet §12 caps. A shared pool does **not** create a shared allowance | [C] |
| ROBOT SIGNS | ≥2 per robot | **R401\*** — ≥2 signs, ≥90° apart, ≥6.5" × 2.5", robust material | [C] |
| Printed portfolio | **2** | **A202\*** — default is 1 printed copy per team at the Initial Interview | [C] |

### Should be shared (buy once)

| Item | Why it does not double |
|---|---|
| Practice field — DIY perimeter + soft tiles | One field, time-sliced (§6.2). The **only** major line that does not scale with team count |
| Game set / scoring elements | One set serves both robots |
| 3D printer + filament | One printer, queued (§6.3) |
| Hand tools, benchtop tools, drill press, saw | One shop. Duplicate only the "hot" tools (§6.4) |
| CAD seat, code repo, scouting spreadsheet | Free tier for both — `SMALL-TEAM-ECONOMICS.md` §1.7 |
| Bulk stock: extrusion, plate, fasteners, belt, chain | Buy one bulk order, split it |

### Deliberately over-ordered (the two-robot multiplier)

| Item | Rule of thumb | Source |
|---|---|---|
| **Printed parts** | **Three full sets: A, B, and spares.** GM0's rule is "print one full set of every printed part as spares"; with two robots that is three sets. A 25-part design implies **75 prints** | `ACHIEVABILITY-FACTORS.md` F2 evidence |
| **Batteries** | 5-6 across the program, 3 chargers. **E511\*** caps chargers at "3-amp average channel current," so a single charger cannot turn a pack around at a two-robot event | [C] **E511\***; `SMALL-TEAM-ECONOMICS.md` §1.3 |
| **Motors / servos** | +1 spare of each *family*. **Standardize on one motor family and one servo family across both robots** — the saving is inventory, not unit price | `SMALL-TEAM-ECONOMICS.md` §1.4 |
| **Gamepads** | +1 spare. A dead gamepad at an event is a lost match | [J] |

**[J] The single highest-leverage BOM decision: standardize the chassis footprint, motor ports and camera
pose across both robots.** Every hour spent on this is repaid in shared AUTO code, shared spares, and I303.F
drop-in mechanism swaps.

## 5.3 The sequencing trick: build the simpler robot first

> **Build the B robot first. Finish it early. Use it to de-risk the A robot.**

| Why | Detail |
|---|---|
| **It de-risks the shared half at low cost** | Every problem in the shared drivetrain, wiring harness and AUTO codebase surfaces on the cheap robot first, where fixing it costs a simple build, not a complex one |
| **It produces a driveable robot early** | A robot that can be driven in October is worth more than a robot that will be excellent in December. Driver practice starts on the B robot |
| **It gives the B team the earlier field slot legitimately** | AP5's countermeasure stops being a fairness rule and becomes a schedule fact |
| **It gives the program a working robot at the first event no matter what** | If A's mechanism is not ready, B still plays. Two teams, one working robot, is a survivable November; two teams, zero working robots, is not |
| **It resolves the model-switch question with evidence** | By G3 (Oct 4) you know from the B build whether the shared architecture actually works |
| **It is what the archetype library already recommends** | "The B robot is a *derivative*, and it should be finished earlier than the A robot, not later" — `ROBOT-ARCHETYPE-LIBRARY.md` §5.3 rule 1 |

### The staggered build calendar

| Week | B team (simpler) | A team (harder) | Shared |
|---|---|---|---|
| Pre-season (Aug 21 - Sep 11) | Assemble chassis #2 | Assemble chassis #1 | Drivetrain CAD; SDK setup; **R304\*** permits all of this before Kickoff |
| W0 (Sep 12-13) | Archetype B chosen | Archetype A chosen | Scoring model; mock elements |
| W1-W2 | Prototype B's mechanism (simple) | Prototype A's mechanism (complex) | Strategy freeze G2 |
| W3 | **B mechanism selected** — it is simpler, it converges first | A still iterating | **G3 model-switch check (Oct 4)** |
| W4-W5 | **Build B's mechanism.** B robot integrates | A CAD; A's parts ordered in the same PO | **G4 design freeze (Oct 18); one purchase order** |
| W6 | **B ROBOT ALIVE (Oct 25).** B starts driver practice | A builds; A borrows every lesson from B's integration | B's harness drawing becomes A's harness drawing |
| W7 | B tunes; B runs auto | **A ROBOT ALIVE (Nov 1) — G5** | AUTO codebase proven on B, ported to A |
| W8 | B: 6 consecutive failure-free matches | A: tune and integrate | **G6 (Nov 8)** |
| W9 | Both: dress rehearsal, two check-ins, two inspections, two interviews | | **G7 (Nov 12)**; first event **Nov 14** |

**[J] The rule that makes this work: the B design freezes at G3, not G4.** B gets an extra two weeks of build
time precisely because its design is simpler and converges sooner. If B is still choosing a mechanism at G4,
you have already failed — switch to M1 and copy A's proven mechanism (§2.4).

## 5.4 Ordering and lead times

| Category | Order by | Note |
|---|---|---|
| Registrations (×2) | **Before Kickoff** | $350/team [O-FTC]. Set up the organization's **financial guarantor by EIN** so both can be purchased together |
| Control systems (×2), driver kits (×2), build kits (×2) | **Pre-season** | The FIRST Storefront Build Kit is **limit 1 per team per season** [O-FTC] — **two registered teams means two allocations of team-priced kits.** This is a genuine two-team purchasing advantage |
| Structure, motion, bulk stock | **One PO at G4 (Oct 18)** | Both BOMs in one order. Volume pricing; one shipping charge; parity procurement defuses AP2 |
| Game elements | **Already late** | The AndyMark pre-order wave closed **Aug 7, 2026**; sets ship from **Sep 14**. Plan September around the $5.50 Pollen preview pack and printed substitutes. Phone AndyMark for a real ship date |
| Batteries and chargers | **Pre-season** | Do not wait. These are the cheapest thing that loses matches |
| Filament | **Pre-season, in bulk** | Three print sets (§5.2) is a lot of filament |
| Portfolio printing (×2) | **G6 week** | **A202\*** — 1 printed copy per team at the Initial Interview unless the ED says otherwise |

---

# 6. Sharing the shop

## 6.1 The concrete weekly schedule

**Assumptions:** one shared space; one half-field (DIY perimeter + 18 tiles); one 3D printer; 2-3 mentors,
not all available every night. Adapt the days, keep the structure.

| Day | Who | Hours | Mentors | Field | Printer | Purpose |
|---|---|---|---|---|---|---|
| **Mon** | **B team only** | 3 h | M1 + M2 | **B — full block** | B's queue | B build night. B has the shop and the mentors to itself |
| **Tue** | **A team only** | 3 h | M1 + M3 | **A — full block** | A's queue | A build night |
| **Wed** | *dark* | — | — | — | **Overnight long prints** | Documentation and portfolio written async; printer runs unattended |
| **Thu** | **Both teams** | 3 h | M1 + M2 + M3 | **Time-sliced 45/45** | either | **RULES NIGHT + shared block.** First 20 min: both teams together for the Team Update diff. Then split |
| **Fri** | *dark* | — | — | — | Overnight prints | Recovery. Do not schedule here |
| **Sat** | **Both teams** | 7 h | all available | **4 × 90-min blocks, alternating** | continuous | Integration day. Full-team demo at the end (both teams present to each other) |
| **Sun** | *dark* | — | — | — | Overnight prints | |

**Standing agenda for a weekday meeting** and the Saturday session structure are in
`research/SEASON-CADENCE.md` §8.2-§8.3 — do not re-invent them. Two two-team-specific additions:

1. **Thursday's first 20 minutes are joint.** [C] Team Updates post every Thursday from Kickoff until two
   weeks before FIRST Championship; additions are highlighted yellow and deletions struck through; updates
   published after an event's driver's meeting do not apply at that event. Both teams need the same diff, and
   reading it once for both is the cheapest shared hour in the program. One student owns Rules Night; the
   other team's software owner asks the one question: *"does anything here change our robot, our auto, or our
   math?"*
2. **Saturday ends with a joint demo.** Each workstream on each team shows the other team what it built. This
   is the only reliable defence against two students building incompatible things for three weeks — and with
   two robots the failure mode is twice as likely.

## 6.2 Practice field time-slicing

The field is the one resource that does not double. Nothing in the rules governs your home field, so this is
pure program policy — which means it must be written down or it will be decided by whoever shouts.

| Rule | Statement |
|---|---|
| **F1 — Written schedule, published before the season** | Ad-hoc allocation is how the B team learns it is second in line (AP5) |
| **F2 — The less-finished robot gets the earlier slot** | Field time is worth more to an untuned robot than to a tuned one. Early season this is B (§5.3); late season it may be A |
| **F3 — The field is never idle** | If the scheduled team's robot is down, the slot transfers immediately to the other team. Announce it, do not negotiate it |
| **F4 — Saturday is four 90-minute blocks, alternating, starting with B** | Predictable, auditable, and B goes first |
| **F5 — The robot touches the field every meeting a robot exists** | Even if it is broken. From `SEASON-CADENCE.md` §8.2 — this is the rule small teams break first |
| **F6 — Driver practice is scheduled, not leftover** | From W6, each team's Saturday block C is driver practice, non-negotiable |

**At the event, none of this applies** — event practice fields are regulated: **E105\*** (registered teams
only — a B-team student cannot "help" on the practice field if B is not registered for that event),
**E115\*** (each robot needs its own complete inspection pass; B's robot cannot ride on A's inspection),
**E106\*** (practice only in your pit, the designated practice areas, or a Practice MATCH — you may not set
up a shared practice rig in the aisle between your two pits). [C]

## 6.3 The 3D printer queue

**[J] The printer is the second-most contended resource and the one that generates the most resentment,
because a print failure is invisible until morning.**

| Rule | Statement |
|---|---|
| **P1 — One written queue, FIFO by submission time** | A shared text file or whiteboard. Job name, team, owner, duration, submitted-at |
| **P2 — During contention, one job per team per day** | Prevents one team's 40-part batch from blocking the other for a week |
| **P3 — Overnight slots go to the longest job** | Wed/Fri/Sun nights are the long-print slots (§6.1) |
| **P4 — When the design is shared, B's copy prints first** | B is the de-risking build (§5.3). Also: it is the visible proof that AP2 is not happening |
| **P5 — Three sets, always: A, B, spares** | `ACHIEVABILITY-FACTORS.md` F2. Print the spare set *before* the first event, not after the first breakage |
| **P6 — A failed print is the owner's to re-queue at the back** | Removes the argument |
| **P7 — Printed-part count is a design constraint** | A 25-part mechanism means 75 prints for a two-robot program. Count prints at G3, not at G5 |

**[C] R101\*** makes cross-team printing explicitly legal — "fabricating elements" is named in the rule's own
note. A team may print B's parts. **[J] But B must assemble its own MAJOR MECHANISMS** — share the pattern,
not the part.

## 6.4 Mentor hours

**[J] The binding constraint is simultaneity, not total hours.** Two teams meeting on the same night with one
mentor is strictly worse than two teams meeting on alternate nights with the same mentor — the mentor is
context-switching, and neither team gets a decision made. [COMM] `Mr.Dave6327` reports exactly this from a
two-team program: same-event convenience buys "less available time for the mentors to support both teams."

| Rule | Statement | Source |
|---|---|---|
| **M1 — Never split one mentor across two simultaneous teams** | Stagger the nights (§6.1 Mon/Tue) | [COMM] `NatsirtD`, `Mr.Dave6327` |
| **M2 — Each team has a *named* primary mentor** | Not "the mentors support both teams." A named adult who knows B's mechanism is the difference between B being real and B being supervised | [J] |
| **M3 — The shared nights (Thu/Sat) are for cross-cutting work only** | Rules diff, integration, demos, field time — not for one team's mechanism debugging | [J] |
| **M4 — Experienced students are mentors for the second team** | [COMM] `EricH`: "you can also get experienced students as mentors for the second team." **Constraint:** they teach, they do not build B's MAJOR MECHANISMS (**R101\***) | [COMM] + [C] |
| **M5 — Four screened adults, if you can get them** | **I101.A.iii** needs 2 Lead Coaches per team; **I103\*** wants "preferably 2" responsible adults per team at the event; **A208\*** allows 1 silent observer *per session* and slots collide | [C] |
| **M6 — Mentor-hours are a G3 gate input** | If M1 cannot be staffed, switch to model M1-shared (§2.4) | [J] |

## 6.5 Tools

| Category | Policy |
|---|---|
| **"Hot" tools** — the hex drivers, nut drivers, and wrenches in the two or three sizes you touch every ten minutes | **Duplicate.** These are cheap and they are the ones that go missing. One set per team, colour-coded |
| **Bench tools** — drill press, band saw, sander, vise | **Share.** One of each, first-come |
| **Measurement** — calipers, square, scale | **Duplicate the calipers.** One of everything else |
| **Pit kits** | **One deep kit + two hot kits** (§7.2) |
| **Consumables** — zip ties, tape, thread-locker, fasteners | **Share from one stock, but bag each robot's fastener BOM separately at G4** (parity procurement, AP2) |

---

# 7. Competition day with two teams

## 7.1 The per-team obligations that double

| Obligation | Rule | Two-team consequence |
|---|---|---|
| Check-in, ≤45 min before qualification matches, adult + ≥1 student at the venue | **I102** [C] | Two check-ins in the same 45-minute window ⇒ **two adults** |
| Responsible adult present the whole event | **I103\*** [C] | ≥2 adults, "preferably 2" each ⇒ 4 |
| Complete inspection, per robot | **I301\***, **E115\*** [C] | Two inspection queues. B's robot cannot ride on A's pass |
| Initial Interview, ≥2 student reps, ≥10 min | **A203\***, **A204.A**, **A205\*** [C] | Two interviews, possibly concurrent; disjoint student rosters |
| Prepared 5-minute uninterrupted presentation | **A207\*** [C] | **Two presentations to write**, not one |
| One adult silent observer per session | **A208\*** [C] | Concurrent slots ⇒ two available adults |
| Printed portfolio at the interview (default) | **A202\*** [C] | Two printed portfolios |
| ≥1 team rep observing ceremonies; ≤5 in the pit during ceremonies | **E702\*** [C] | Per team. With ~7 students each, you need coverage of both pits and both teams in the stands |
| Student rep at ALLIANCE selection | **[H]** DECODE T701 | Per team. A missing rep costs the playoffs |

## 7.2 Pit logistics

| Item | Rule | Practice |
|---|---|---|
| **Adjacent pits** | **E502.B/C\*** — teams may not "swap team pits with other teams if pits have assigned team numbers" or "move themselves to empty team pits without Event Director approval" [C] | **Email the ED before every event** asking for adjacent assignment. It is their call, not yours. [COMM] `Marlinvx`: "they put both teams together and we have mega-pit!" |
| **Cross-pit work** | **E107.B\*** — FABRICATED ITEMS may be produced "in another team's pit area **with permission from that team**" [C] | **Print a standing-permission card and tape it inside each pit.** Your two teams grant each other that permission in writing. This legally gives you a two-pit workshop without violating E502 |
| **Self-containment** | **E502\*** — "Pit set ups should be self-contained within the space assigned"; no power or internet lines run to any other area [C] | Two teams' worth of totes is the classic **E503\*** aisle violation. One deep kit under one bench, two hot kits |
| **Pit machinery** | **E505\*** — small benchtop machinery only [C] | Same limit whether you have one pit or two |
| **Battery charging** | **E511\*** — safe rate, **no charger exceeding 3-amp average channel current**, polarized connectors only, never alligator clips [C]; §5.5 notes "Power may not be available overnight for a multi-day event" | Two robots ⇒ double the charge load on a 3A-limited charger. **3 chargers, 5-6 batteries.** Arrive fully charged |
| **Pit kit split** | — | **One deep kit** (spare hub, spare motors, full fastener stock, soldering) shared; **two hot kits** (hex drivers, zip ties, tape, spare gamepad, battery, laptop cable) so neither team is ever blocked waiting on the other |

## 7.3 Can the two teams help each other? Yes — here is exactly how far

| Action | Legal? | Rule | Note |
|---|---|---|---|
| Work in each other's pit | **Yes, with permission** | [C] **E107.B\*** | Grant standing permission in writing |
| Lend tools, spares, a cart | **Yes** | [C] no prohibiting rule; helping other teams is encouraged | |
| Hand over a **spare identical COMPONENT** mid-event | **Yes, no re-inspection** | [C] **I303.E** | |
| Hand over a **spare identical MECHANISM** (size, weight, material) | **Yes, no re-inspection** | [C] **I303.F** | The M3 shared drivetrain makes this real for chassis parts |
| Hand over a **non-identical** mechanism never inspected on the receiving robot | **Re-inspection required** | [C] **I301\***, **I303\*** | |
| Reconfigure using a subset of already-inspected mechanisms | **Yes, no re-inspection** | [C] **I303.G** | |
| Share a parts pool to exceed electronics caps | **No** | [C] **I302\*** — each team's total across all configurations must independently comply | |
| Use re-inspection to get around a rule | **No** | [C] **I304\*** | |
| **Strip the B robot to keep A running** | *Legal, and the thing you must not do* | [C] I303.E/F permit it; [C] §6.1.1 means B is judged only on what it can show | **AP1.** Written no-strip rule |
| Run one physical robot under two team numbers | **No** | [C] **E117\***, **R101\***, **I301\***, **R403\***; §1.5.1 Competition Integrity Contract | **I303.C** permits sign swaps without re-inspection — that is the loophole, and the CIC closes it. `TWO-TEAM-PROGRAM-RULES.md` X1/X2 |
| Share scouts and scouting data | **Yes** | [O-FRC] "Sharing scouts or having Sibling Teams help each other at the event is still allowed" | §7.4 |
| Let an unregistered team's students use the event practice field | **No** | [C] **E105\***, **E115\*** | |

## 7.4 Scouting — the genuine two-team advantage

**[J] This is the one place where the two-team structure produces a real, compounding competitive edge, and
most two-team programs waste it.**

**The arithmetic** [H] — DECODE §13.6.1: "All event types will schedule either 5 or 6 Qualification MATCHES
per team as determined by the Event Director." BIOBUZZ §13 is a placeholder; re-verify at Kickoff.

| | One team | **Two teams** |
|---|---|---|
| Matches with your robot on the field | 5-6 | **10-12** |
| Matches where students are free to scout | all others | all others, **plus every match the sibling plays** |
| Pit-scouting crews | 1 | **2** |
| Pit-scouting time for a 30-team field @ 90 s | ~45 min for one crew | **~22 min each** — split the field by team number |
| Judge-feedback forms per event (**A212\***) | 1 | **2** |

**The operating pattern:**

| Rule | Statement |
|---|---|
| **S1 — One shared spreadsheet, two collectors** | Both teams write into the same match-scouting sheet. Two data streams, one database |
| **S2 — The team not playing scouts the team that is** | B's free students scout A's matches and vice versa. Nobody has to sit out to collect data |
| **S3 — Split pit scouting by team number** | Odd/even or low/high half. Halves the wall-clock cost of the most information-dense scouting activity |
| **S4 — One alliance list, two drive coaches read it** | Build it as **tiers, not a ranking** — `SCOUTING-AND-AWARDS.md` §6.1. Maintain a DNP list with a **written reason** per entry |
| **S5 — Reconcile before selection, not during** | Ten minutes before alliance selection, the two drive coaches agree on the tier list and on the sibling policy (§7.5) |
| **S6 — The award narrative is written separately** | Sharing the *data* is legal and encouraged [O-FRC]. But §6.1.1 means each team gets credit only for what *it* says. Each team writes its own account of what it collected and how it used it. A published scouting database also counts as a "Provided Published Resource" under FIRST's outreach definitions — `SCOUTING-AND-AWARDS.md` §5.6 |

**Sample-size warning [H] + [J]:** five or six qualification matches is one-half to one-third of an FRC
sample. Every statistic is noisy — `SCOUTING-AND-AWARDS.md` §3.5 measures roughly ±2.4 places of rank churn
from noise alone. Human observation is proportionally *more* valuable in FTC, not less, which is exactly why a
second team's worth of eyes matters.

## 7.5 Alliance selection with both teams at one event

**All of this is [H] — DECODE T701-T703 and §13.7.1. BIOBUZZ Section 13 is a V0 placeholder. Re-verify on
2026-09-12.**

| Mechanic | [H] Text (abridged) | Two-team consequence |
|---|---|---|
| Alliance size | **2 teams** per alliance; **1 pick** per lead | There is nowhere to hide a gap. Your single pick must be both high-ceiling and reliable |
| **T701** | Each team must send a STUDENT rep; no rep ⇒ ineligible for playoffs | **Two reps, two chairs.** This is a checklist item, not a formality |
| **T702** | A lead that declines an invitation may still invite, but may not be invited | **Declining is a one-way door.** Both drive coaches must know this before the table |
| **T703** | No backup teams in playoffs; "consider reliability when selecting partners" | The manual itself tells you to weight reliability |
| §13.7.1 promotion | If a lead accepts another lead's invitation, all lower leads promote one spot and the highest unselected team becomes a new lead | The *effective* cutoff for becoming a lead is deeper than the nominal alliance count |

### The sibling policy — write it down before the event

**[J] The worst possible outcome is a public family argument at the selection table.** Decide these in
advance, in writing, and brief both drive coaches:

| Scenario | Policy |
|---|---|
| **A is a lead; B is available** | **Pick B only if B is in your top-2 on the tier list you would apply to any other team.** Write the reason down either way. Picking a sibling who is not the best available costs you the playoff; refusing a sibling who *is* the best available costs you the playoff *and* the goodwill |
| **Both are leads** | One may invite the other. Run the **Table 4-1** advancement arithmetic for both branches *before* the event: ALLIANCE Selection Results contribute `21 − lead/draft number`, playoff advancement contributes 40/20/10/5 (per `TWO-TEAM-PROGRAM-RULES.md` §7). **UNVERIFIED**: the exact draft-number assignment when a lead accepts another lead's invitation — confirm against BIOBUZZ §4 and §13 at Kickoff |
| **B is a lead; A is available** | Same test, run by B's drive coach. **B's drive coach decides.** If the adults override this, you have just taught the B team that it is a satellite (AP3) |
| **Either is invited by a third team** | **Say yes fast.** T702 makes a decline irreversible and hesitation reads as reluctance |
| **Both are available, neither is a lead** | Both teams pitch separately. Go introduce yourselves to the top-6 pits with a 20-second description and a card. Two teams means two pitches, not one pitch delivered twice |

**[J] Do not coordinate a decline.** Two teams agreeing to decline invitations so they can pair with each
other is (a) irreversible under T702, (b) an obvious loss of expected advancement points, and (c) exactly the
behaviour that earns a two-team program the "pay-to-win" reputation the community already worries about
[COMM] — see `TWO-TEAM-PROGRAM-RULES.md` §8.3.

**Advancement note [C]:** both teams advance or not entirely independently. §4 has no organizational cap;
each team's advancement window is **its own first three chronological entry-level events**; the local Program
Delivery Partner determines the slot count per tournament. Ask your PDP for that number — it, not any rule,
decides whether both of your teams can advance from one event.

**[COMM] The conversation to have before the first qualifier, not after:** decide and announce what happens
if only one team advances. Source thread in `TWO-TEAM-PROGRAM-RULES.md` D17.

---

# 8. The award split

Full grid, materials packages and pairing cards: **`reference/AWARD-ALIGNMENT-MATRIX.md`** — especially §2.3
(top-2 per archetype), §3 (the six materials packages M1-M6), and §6 (two-team split guidance). This section
covers only what is specific to running the split across two teams.

## 8.1 The controlling rules

| Rule | Effect | Label |
|---|---|---|
| **A215\*** | Each team may win or be runner-up for **one** team judged award at the event. **Per team** — no anti-sweep rule exists in §6 | [C] |
| **A211\* / Table 6-1** | **The award pool scales with event size.** This is the real constraint on the split | [C] |
| **A213\* / A214\*** | Inspire only in your HOME REGION; 1st-place Inspire once per season from any QT/LT (2nd/3rd still available; Regional Championship Inspire still available). **Both per team** | [C] |
| §6.1 categories | **MCI** = Innovate (RTX), Control, Design · **TA** = Connect, Reach, Sustain · **Documentation** = Think · plus Inspire and Judges' Choice | [C] |
| §6.1.1 | Judges use only what they see and hear from *that team* at *that event* | [C] |

## 8.2 The split is conditional on event size — this is the part everyone gets wrong

**Table 6-1** [C] (verbatim reconstruction in `research/SCOUTING-AND-AWARDS.md` §7.3):

| Award | 4-10 teams | 11-20 teams | 21-40 teams | 41-64 teams |
|---|---|---|---|---|
| **Inspire** | 1st | 1st, 2nd | 1st, 2nd, 3rd | 1st, 2nd, 3rd |
| **Think** (Documentation) | 1st | 1st | 1st, 2nd | 1st, 2nd, (3rd\*) |
| **Connect / Reach / Sustain** (TA) | 1st — ***only one of the three is given*** | 1st each | 1st, (2nd\*) each | 1st, 2nd, (3rd\*) each |
| **Design / Innovate / Control** (MCI) | 1st — ***only one of the three is given*** | 1st each | 1st, (2nd\*) each | 1st, 2nd, (3rd\*) each |
| **Judges' Choice** | Optional\* | Optional\* | Optional\* | Optional\* |

### The split, by event size

| Event size | Judged slots available | **A team primary** | **B team primary** | Why |
|---|---|---|---|---|
| **4-10 teams** | ~4: Inspire, Think, **one** TA, **one** MCI | **MCI** (whichever of Innovate/Control/Design the A robot argues for) | **Think** | **Only one MCI award exists at all.** Two teams in the MCI pool means one of them is guaranteed to lose to the other. Think is a separate category with its own 1st place |
| **11-20 teams** | 9: Inspire ×2, Think, 3 TA, 3 MCI | **Control** *(sensor-led build)* or **Innovate (RTX)** *(mechanism-led build)* | **Design** | Three distinct MCI slots exist, so both teams can sit in MCI **provided they target different awards** |
| **21-40 teams** *(the modal qualifier)* | 11-17 | **Control** or **Innovate (RTX)** | **Design** or **Think** | 2nd places appear; the deepest pool. `SCOUTING-AND-AWARDS.md` §7.3: roughly one team in two or three leaves with a judged award |
| **41-64 teams** | deepest | as above | as above | — |

**[J] The rule in one line: never let both teams walk into the same event arguing the same award — and at a
4-10 team event, never let both teams argue MCI at all.**

## 8.3 The standing assignment

Assign primaries in September and hold them. Rationale and evidence in `AWARD-ALIGNMENT-MATRIX.md` §6.2, which
this table matches.

| | **A team** | **B team** |
|---|---|---|
| Robot identity | Specialist in the season's **highest-value repeatable task** | Specialist in the season's **cheapest repeatable task** |
| **Primary award** | **Control** (6.3.7) if sensor-led · **Innovate sponsored by RTX** (6.3.6) if mechanism-led | **Design** (6.3.8) · or **Think** (6.3.2) at a ≤10-team event |
| **Hedge** | Innovate or Design (whichever is not primary) | Think or Design (whichever is not primary) |
| Materials packages | **M3** or **M2**, + M4 + M5 + M6 | **M1** or **M4**, + M5 + M6 |
| Portfolio emphasis | Control block diagram; Table 6-8 component table; development path | Engineering-journey narrative; decision matrix; math page; readability (Table 6-3 E2) |
| Portfolio required? | **Control requires a portfolio**; Innovate does not | **Think requires a portfolio**; Design does not |
| Why | Puts the robot-heavy team where the machine criteria live | Puts the developing team where fabrication capability is irrelevant, and where the BIOBUZZ rewrite **lowered** the bar (Think now needs only one of four options) |

**The TA awards are the two-team org's natural double-dip [C] + [J]:**

- **§6.3.5 Sustain** Required 3 asks for "leadership development competency through **clearly defined team
  roles and an intentional process for preparing future student leaders**." Required 1 asks for
  organizational sustainability; Encouraged 4 asks for risk management — "identifying organizational
  constraints, implementing mitigation strategies, and adapting plans."
- **§6.3.4 Reach** Required 2 asks for "successful recruitment of new teams, coaches, mentors, or volunteers
  who have not previously participated in the FIRST community."
- **[J] A well-run A/B structure is literally all of those things.** The A team tells it as *"we built the
  pipeline"*; the B team tells it as *"we are what the pipeline produced."* **Same truth, two genuinely
  distinct narratives** — which is exactly what the judges' sibling probe rewards (§4).
- **A215\*** still caps each team at one judged award, so treat Sustain/Reach as the *hedge* that a team pivots
  to when the MCI/Documentation pool is thin, not as a third target.

## 8.4 If you are running model M1 (fully shared design)

The award split gets harder, and you must plan for it rather than discover it:

| Constraint | Handling |
|---|---|
| Both robots are the same machine | **Only one team may claim the shared mechanism as its creative/innovative mechanism.** The other claims a different mechanism, or claims the *whole-robot* Design case, or moves to Think |
| **Innovate (6.3.6)** is scoped to "the whole ROBOT **or one MECHANISM**" | Assign the mechanism to one team, in writing, in September |
| **Design (6.3.8) R2** requires "the design of the **entire** ROBOT, or the detailed process used to create it — not just one COMPONENT" | The whole-robot argument is available to *both* teams only if each robot genuinely differs somewhere. Under M1 it does not — so one team takes Design and the other takes Think or an MCI award it can argue independently |
| **Control (6.3.7)** grades software and a reliability log | Under M1 the *code* is shared but the *tuning data and failure log* are per robot. Control is the most survivable MCI award for a shared design, and the cheapest MCI path for a program without a mill (`AWARD-ALIGNMENT-MATRIX.md` S3) |

## 8.5 Keeping the two stories distinct

| Rule | Practice | Anchor |
|---|---|---|
| **Different primary awards, always** | Assigned in September, held all season | [C] A211 Table 6-1, A215\* |
| **Same fact, different side of it** | The A/B pipeline story, told from each end | [C] §6.3.4 R2, §6.3.5 R3 |
| **Different mechanisms in the Innovate/Design claim** | One team per mechanism, assigned in writing | [C] R304\*/R101\* make sharing legal; the *claim* is what must be unique |
| **Different students speaking** | Disjoint interview rosters, fixed in September, badges on the shirts | [C] **A204.A**; [O-FRC] |
| **Shared engineering, separate authorship** | Share the CAD, the repo, the chassis. Never share portfolio pages verbatim. Two documentation leads who do not read each other's drafts before submission | [C] A201; [O-FTC] judges assess each team individually |
| **AI credit in both portfolios** | [C] **A201**: "Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a footnote or endnote credit." The manual's own example format is *"Portfolio created by Team XXXXX and ChatGPT."* **Both** portfolios need the footnote if AI touched either | [C] **A201** |
| **Content window** | [C] **A201.E** — content must be from **on or after January 1, 2026**; §6.1.1 confirms "the current season begins on January 1, 2026" | [C] |
| **Read both A212 feedback forms after every event** | Standing agenda item. Each team picks one weak area and fixes it before the next event. Two teams = two forms = twice the signal, and almost nobody uses even one | [C] **A212\*** |

---

# 9. Budget: what the second robot actually costs

**All figures USD, Aug 2026, from `research/SMALL-TEAM-ECONOMICS.md` §1-§2 unless noted. Labels are that
document's: [FACT] = sourced price; [JUDGMENT] = my arithmetic on top of them.**

## 9.1 The delta table

**The question is not "what does a robot cost" but "what does the *second* one cost, given you already have
the first."**

| Line | Doubles? | Second-team cost | Note | Label |
|---|:---:|---:|---|---|
| FIRST season registration | **Yes** | **$350** | Per team, per season | [FACT] |
| Event fees | **Yes** | **$100 – $800** | Set by your PDP; a ~5× regional spread (NJ $100 flat ⟷ Chesapeake $500 for two qualifiers). **Get yours in writing before committing** | [FACT] |
| Storefront **Electronics Kit** (Control Hub + servo + sensors + cables) | **Yes** | **$350** | **R701\*** — one ROBOT CONTROLLER per robot. The kit contains a $375 Hub plus six other parts; buying the Hub retail is strictly worse | [FACT] |
| Storefront **Driver Kit** (Driver Hub + 2 gamepads + webcam) | **Yes** | **$295** | **R901\*** | [FACT] |
| Storefront **Build Kit** (REV FTC Competition Set V3.1) | **Yes** | **$660** | **Limit 1 per team per season — so a second registered team unlocks a second team-priced allocation** | [FACT] |
| Batteries + charger | **Yes** | **$146** | 2 × REV Slim Battery @ $55 + 1 charger @ $36.50. **R601\*** one installed battery per robot; **E511\*** 3A charger cap makes a second charger necessary at a two-robot event | [FACT] |
| Extra motors / servos / mechanism parts | **Yes** | **$150 – $300** | Depends on the B archetype's motor count | [JUDGMENT] |
| Portfolio print, shirts, badges | **Yes** | **$60 – $100** | **A202\*** one printed copy per team | [JUDGMENT] |
| Shipping + sales tax (~10% of goods) | Yes | **~$165** | | [JUDGMENT] |
| **Practice field** (perimeter + tiles) | **No** | **$0** | One field, time-sliced (§6.2) | |
| **Game set / scoring elements** | **No** | **$0** | | |
| **3D printer** | **No** | **$0** (filament scales) | | |
| **Tools** | **No** | **~$50** | Duplicate only the hot tools (§6.5) | [JUDGMENT] |
| **CAD / repo / scouting software** | **No** | **$0** | Free tier, identical for both teams | [FACT] |
| **Travel** | **No** | **$0** if same event | Same weekend, same carpool. This is the argument for co-locating both teams at one event | [JUDGMENT] |
| | | | | |
| **TOTAL — second team, first year** | | **≈ $2,300 – $2,900** | | **[JUDGMENT]** |

**[JUDGMENT] The headline number: the second team costs roughly $2,400-2,800 all-in, against ≈$7,240 for a
Tier B first team — about one-third.** Everything that does not scale (field, tools, printer, game set,
software, travel) is already paid for by team one. The delta is almost entirely registration + a control
system + a build kit + an event fee.

**Two comparisons for context** [FACT]:

- FIRST's own start-a-team figure is "around $1,800, which includes the yearly registration fee and initial
  robotics set investment" — and explicitly excludes event participation.
- `SMALL-TEAM-ECONOMICS.md` Tier A (bare minimum, one team, all-in) is **≈$2,620**. **The second team costs
  about what a whole Tier A team costs — because it *is* a Tier A team, standing on team one's infrastructure.**

**The line that is not in the table [FACT]:** FIRST Championship is **$3,000 per team in entry fee alone**,
plus ~$6,000-9,000 travel. **If both teams qualify, that doubles.** Do not carry it in the baseline; plan the
fundraiser in November when advancement allocations publish (Nov 19).

## 9.2 Where the B robot can legitimately be cheaper

| # | Saving | Amount | Why it is legitimate |
|---|---|---:|---|
| 1 | **Skip the second goBILDA Starter Kit** — the Storefront Build Kit covers B's structure | **~$675** | B's design is simpler by construction (§2.3). This is the largest single legitimate saving |
| 2 | **Fewer motors ⇒ no second Expansion Hub** | **$275** | **R701.C\*** permits at most one additional Expansion Hub; you only need it if you exceed the Control Hub's port budget. 4 drive + 1-2 mechanism motors fits. **Choosing a 2-motor mechanism over a 3-motor one can save $275 of electronics, not just a motor** |
| 3 | **B's structure from A's offcuts and last season's parts** | varies | **R304\*** — "Custom software, designs, and parts can be reused year-to-year" |
| 4 | **Shallower mechanism-specific spares** | ~$100 | The *shared* subsystems (drivetrain, electronics) already have spares that serve both robots under **I303.E/F** |
| 5 | **No second field, printer, tool set, or game set** | ~$1,000+ | Already counted in §9.1 |
| 6 | **Fewer printed parts by design** | filament | A simpler mechanism is fewer of the 3× print sets (§6.3 P5/P7) |

## 9.3 Where the B robot must NOT be cheaper

**[JUDGMENT] These are the false economies. Each one costs more than it saves.**

| Do not cut | Why |
|---|---|
| **Batteries and chargers** | The cheapest thing that loses matches. **R601\*** one installed pack; **E511\*** a single 3A-limited charger cannot turn packs around at a two-robot event |
| **The Control Hub** — do not put B on the phone-based path | **R701.B\*** makes it legal, but the manual itself warns in writing: "the REV Control Hub is the only officially supported ROBOT CONTROLLER device. Teams choosing to use any other unsupported device (e.g., smartphones) are responsible for testing and verifying its compatibility." You would own the entire Android compatibility surface with **no support from REV, the forums, or the FTA at your event**. A small team's scarcest resource is debugging hours |
| **The Driver Hub / gamepads** | **R901\***. A dead gamepad loses a match; a spare is $30 |
| **The event fee** | Cutting B's schedule cuts B's season (AP12). Each team's advancement window is its own first three chronological entry-level events [C] §4 |
| **Portfolio printing and interview prep** | **A202\*** default is one printed copy at the interview; **A204.B** wants a copy for reference during it. This is a $30 line that gates a 12- to 60-point award |
| **The second registration** | Without it there is no second team, no second award slot, and no second advancement total |

---

# 10. Kickoff-day and pre-season checklist

## 10.1 Before Kickoff (now → Sep 11, 2026)

| # | Action | Anchor |
|---|---|---|
| 1 | Register **both** teams: 2 registrations, 2 fees, 4 Lead Coach slots with YPP screening, every student on the roster they actually work on | [C] **I101.A.i-v** |
| 2 | Set up the organization's **financial guarantor by EIN** so both registrations purchase together | [O-FTC] 2026-27 registration changes |
| 3 | Confirm with FIRST Support whether FTC treats the second team as a **rookie or a new-veteran** team — it affects grant eligibility | **UNVERIFIED for FTC**; `TWO-TEAM-PROGRAM-RULES.md` Q2 |
| 4 | Confirm the FIRST Dashboard permits one person in a Lead Coach slot on two teams | **UNVERIFIED**; Q3 |
| 5 | Confirm both team numbers show the **same HOME REGION** on FTC-Events | [C] §4 |
| 6 | Ask your PDP for the **per-event fee** and the **advancement slot count** per qualifier | [C] §4 — "The local Program Delivery Partner determines the advancement numbers" |
| 7 | **Build both chassis.** Both drive a figure-8 by Sep 11 (G0) | [C] **R304\*** permits pre-Kickoff FABRICATED ITEMS |
| 8 | Publish the **written weekly schedule** (§6.1) and the **field-time policy** (§6.2) | [J] |
| 9 | Name the **primary mentor per team** and the **interview roster per team** | [C] **A204.A** |
| 10 | Order batteries, chargers, filament in bulk | [C] **E511\*** |

## 10.2 Kickoff weekend (Sep 12-13)

| # | Action |
|---|---|
| 1 | **Two archetype paragraphs, not one** (G1). A's identity and B's identity, each with an explicit "does not do" list |
| 2 | Write the **shared/divergent boundary** on the whiteboard: what both robots share, what diverges |
| 3 | Write the **G3 model-switch triggers** (§2.4) next to it, with the Oct 4 date |
| 4 | Assign **award primaries** for both teams (§8.3), conditional on your first event's size |
| 5 | Assign the **shared mechanism claim** in writing (§8.4) if any mechanism is shared |
| 6 | Draft the Game Q&A question: *"May two teams from the same organization present the same physical ROBOT for inspection at different events?"* — Q&A opens **Sep 28, 12:00 p.m. ET**. Note [C] Q&A answers do **not** supersede manual text; REFEREES and INSPECTORS are the final authority |
| 7 | Re-verify the **[H]** items in this file against the Kickoff manual: DRIVE TEAM size (§10), qualification match count and alliance-selection rules (§13) |
| 8 | Re-download the **Judging Process Guide** and confirm the Sibling Teams section is unchanged |

## 10.3 Open items

| # | Question | Where | Why it matters here |
|---|---|---|---|
| U1 | BIOBUZZ **DRIVE TEAM** size and composition | Kickoff manual §10 | §1.2 role 8 and the whole 7-student roster math |
| U2 | BIOBUZZ **qualification match count** per team | Kickoff manual §13 | §7.4's scouting arithmetic |
| U3 | BIOBUZZ **alliance-selection rules** (T701-T703 equivalents) | Kickoff manual §13 | §7.5 in its entirety |
| U4 | Exact **draft-number assignment** when one alliance lead accepts another lead's invitation | Kickoff manual §4 + §13 | §7.5's both-are-leads branch |
| U5 | Whether one person may hold a **Lead Coach slot on two teams** in the Dashboard | FIRST Support | Whether you need 2 screened adults or 4 |
| U6 | Whether FTC classifies the second team as **rookie or new-veteran** | `customerservice@firstinspires.org` | Rookie grant eligibility |
| U7 | Your PDP's **per-event fee** and **advancement slots** | Local PDP | §9.1's largest uncontrolled variable |
| U8 | Whether the ED will assign **adjacent pits** | Event Director, per event | [C] **E502.B/C\*** makes it their call |

---

# 11. The one-page version

| Question | Answer |
|---|---|
| **Rosters** | 8 / 7. No dual-rostering. Every role has a named backup; minimum crew 3 |
| **Same or different design?** | **Hybrid.** Shared drivetrain, control system and AUTO codebase; **divergent scoring mechanism** |
| **When to switch** | Down to fully-shared if mentors, CAD capacity or B's mechanism concept fail at **G3 (Oct 4)**. Up to fully-divergent only if the game has two separable value paths *and* ≥3 staffed mentor-nights *and* B is self-sufficient |
| **What is the B team?** | A competitive team with its own award target, its own MAJOR MECHANISM, its own portfolio, its own students. **Not a parts donor.** Written no-strip rule |
| **Build order** | **B first.** B alive by Oct 25, A by Nov 1. B de-risks the shared architecture |
| **BOM** | Duplicate what plugs into a robot; share what sits on a bench. **Three print sets: A, B, spares** |
| **Shop** | Mon = B, Tue = A, Thu = both (rules night), Sat = both (integration). Never split one mentor across two simultaneous teams |
| **Field** | Written schedule. Less-finished robot gets the earlier slot. The field is never idle |
| **Event day** | Two pits, ask the ED for adjacency (**E502\***). Standing cross-pit permission (**E107.B\***). Two adults minimum, four preferred |
| **Mutual aid** | Everything except: one robot under two numbers, a MAJOR MECHANISM built by the wrong team, a shared electronics allowance, and stripping the B robot |
| **Scouting** | One spreadsheet, two collectors, split pit scouting. **The real two-team advantage.** Separate award narratives |
| **Awards** | A → **Control** or **Innovate (RTX)**. B → **Design**, or **Think** at a ≤10-team event. Never both in the same pool. **A211 Table 6-1 conditions everything** |
| **Budget** | Second team ≈ **$2,400-2,800** all-in, ~⅓ of a Tier B season. Cheaper on structure and motor count; **never** on batteries, Control Hub, event fee or portfolio |
| **The three questions** | *"How did you decide who did what?"* · *"Who contacted ___?"* · *"How did you ensure it aligned with your team plan?"* Drill them. This is where two-team programs are won and lost |

---

# 12. Sources

**Sibling documents in this workspace** (read these for the underlying derivations):
`research/TWO-TEAM-PROGRAM-RULES.md` · `research/SMALL-TEAM-ECONOMICS.md` · `research/SEASON-CADENCE.md` ·
`research/SCOUTING-AND-AWARDS.md` · `reference/AWARD-ALIGNMENT-MATRIX.md` ·
`reference/AWARD-CATALOG-BIOBUZZ.md` · `reference/ACHIEVABILITY-FACTORS.md` ·
`reference/ROBOT-ARCHETYPE-LIBRARY.md` · `reference/CONSTRUCTION-RULES-R.md`

**Primary [C] source.** BIOBUZZ V0 Competition Manual, 2026-07-31, 93 pp —
`manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` and the pre-split section files in
`manuals/2026-27_BIOBUZZ/sections/`. Rules cited: §1.5.1 Competition Integrity Contract · §3 (I101, I102,
I103, I301, I302, I303, I304) · §3.3.1-3.3.2 · §4 Advancement (Tables 4-1, 4-2) · §5 (E105, E106, E107, E115,
E116, E117, E501-E505, E511, E701, E702) · §6 (§6.1, §6.1.1, A201-A215, Table 6-1, §6.3.1-6.3.9, Tables
6-2…6-9) · §12 (R101, R301, R304, R305, R401, R403, R503, R601, R602, R701, R901). **R304/R305 and
A206/A207/A208 verified against PDF pages 71 and 50 directly** — the `-layout` text extraction misaligns those
rule IDs.

**[H] source.** DECODE 2025-26 Competition Manual TU32 —
`manuals/_reference_prior_seasons/` — §10.2 DRIVE TEAM, §13.6.1 match counts, §13.7.1 alliance promotion,
T701-T703. **Prior-season only; BIOBUZZ §§10 and 13 are placeholders.**

**[O-FTC] / [O-FRC] web sources** (accessed 2026-08-21; full URLs in `TWO-TEAM-PROGRAM-RULES.md` §12):
FTC Judging Process Guide Rev. 25-26.3 (Sibling Teams section) · FIRST Guidelines for Sibling Teams Rev. June
2026 (FRC-scoped) · ftc-docs program overview (team size) · FIRST Get Started · FIRST Cost & Registration ·
FIRST Storefront registration changes · `2026-27_BIOBUZZ_ImportantSeasonDates.pdf` V26-27.1.

**[COMM] sources.** Chief Delphi threads, quoted with usernames in `TWO-TEAM-PROGRAM-RULES.md` §9 and §8.3:
*1 or 2 teams?* · *Rethinking our FTC team(s)* · *One school with multiple teams requirements* · *Thoughts on
teams with multiple teams with the same robot* · *[FRC Blog] Sibling Teams and an Expanded District* · *[FTC]
Two-Teams, One Qualified for Regionals, One Did Not*. **Opinion, not rule.**

**AI attribution.** This document was drafted with AI assistance from the sources above. If any of its content
reaches a team PORTFOLIO, **A201** requires a footnote or endnote credit in that portfolio — the manual's own
example format is *"Portfolio created by Team XXXXX and ChatGPT."*
