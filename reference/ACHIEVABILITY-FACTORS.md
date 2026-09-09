# ACHIEVABILITY FACTORS — Ranking Model for BIOBUZZ Design & Scoring Strategies

**Status:** Game-agnostic scaffolding. Written 2026-08-21, **22 days before BIOBUZZ Kickoff (2026-09-12)**.
The BIOBUZZ game is not public. Nothing here assumes a game task. Every anchor is expressed as an
*observable property of a mechanism or strategy*, so it can be applied to whatever drops on Kickoff day.

**Purpose:** when the AI review harness proposes design and scoring strategies from the real manual, this
document is the rubric that RANKS them for *this specific program*, and hands the ranked list off to the
award-pairing and BOM stages.

**Calibration target (design everything around this):**

| Attribute | Value |
|---|---|
| Students | ~15 total |
| Registered teams | 2 (A team + B team), **two robots** |
| Budget | Modest — 2× `$350` registration + events + 2 robots |
| Fabrication | COTS kits, 3D printing, hand tools. **No CNC mill, no lathe, no in-house waterjet** |
| Mentor hours | Limited — cannot supervise two independent design programs |
| Practice field | Assume partial (tiles + some elements), not a full dedicated field |

---

## 0. How to read this document

| Section | Contents |
|---|---|
| [1](#1-labeling-and-evidence-base) | Labeling conventions + evidence base |
| [2](#2-the-factor-set-at-a-glance) | Factor set at a glance (16 factors, weights) |
| [3](#3-hard-gates-checked-before-scoring) | Hard gates — checked *before* scoring |
| [4](#4-factor-definitions-anchors-and-evidence) | The 16 factors in full: definition, prediction, 1–5 anchors, evidence |
| [5](#5-pre-registered-exemplars-calibrate-the-scale-before-kickoff) | Pre-registered exemplars (calibrate the scale before seeing the game) |
| [6](#6-weighting-scheme-and-justification) | Weighting scheme + per-weight justification |
| [7](#7-what-a-different-team-should-change) | What a *different* team should change |
| [8](#8-anti-flatness-protocol-avoiding-the-everything-scores-3-rubric) | Anti-flatness protocol + worked example |
| [9](#9-scoring-math-and-output-format) | Scoring math and output format |
| [10](#10-handoff-factor-profile--award-targets) | Handoff: factor profile → award targets |
| [11](#11-kickoff-day-instantiation-checklist) | Kickoff-day instantiation checklist |
| [12](#12-machine-readable-factor-set) | Machine-readable factor set (YAML) |

**Polarity is uniform: 5 is always favorable to this program. 1 is always unfavorable.**
Factors that name a *cost* (fabrication complexity, tuning burden, BOM cost) are therefore **inverted** —
5 means *little* of that cost. Each factor block restates its polarity so a scorer cannot get it backwards.

---

## 1. Labeling and evidence base

Per the rigor rules, every factual claim below carries one of:

| Label | Meaning |
|---|---|
| **CONFIRMED-BIOBUZZ** | Read directly from the 2026-27 BIOBUZZ V0 Competition Manual text held locally. Section 3 (I), 4, 5 (E), 6 (A) and 12 (R) are **final** for BIOBUZZ. |
| **CONFIRMED-PRESEASON** | Published by FIRST for 2026-27 *outside* the V0 manual (blogs, product pages, cost pages), verified by direct fetch on 2026-08-21. |
| **HISTORICAL** | Prior-season fact (INTO THE DEEP 2024-25, DECODE 2025-26) or cross-program (FRC). Never a BIOBUZZ fact. |
| **JUDGMENT** | My synthesis. Not a rule, not a measured number. |

### 1.1 BIOBUZZ constraints that are already final (all CONFIRMED-BIOBUZZ)

These are the design envelope. They exist *now* and do not change at Kickoff.

| Rule | Constraint | Why it matters to achievability |
|---|---|---|
| **R102** §12.1 | STARTING CONFIGURATION limited to an 18-inch cube | Fixes the packaging problem before the game is known |
| **R104** §12.1 | **No ROBOT weight limit** in BIOBUZZ | Heavy, over-built, bolt-together steel/aluminum construction is legal — favors low-skill fabrication over lightweighting |
| **R105** §12.1 | ROBOT must stay one assembly; **"Sizing Constraints and more details will be released at Kickoff"** | The single largest *known unknown* in Section 12. Any extension-dependent strategy is exposed — see F16 |
| **R301** §12.3 | COTS MAJOR MECHANISMS purpose-built for a game task are **prohibited**. Exceptions: **(A) COTS drive CHASSIS**, **(B) COTS MAJOR MECHANISMS that are part of the official FIRST Tech Challenge StarterBots** | You may buy your drivetrain and you may buy/build the StarterBot mechanism. You may not buy a finished game solution |
| **R302** §12.3 | Legal COTS parts and raw materials may be drilled, cut, painted | Hand-tool modification of kit parts is explicitly legal |
| **R303** §12.3 | COTS COMPONENTS/MECHANISMS must not exceed **single DoF**; exceptions include holonomic wheels and **dead-wheel odometry kits** | Odometry pods are legal COTS — cheap localization without custom machining |
| **R304** §12.3 | **Custom software, designs, and parts can be reused year-to-year** | Anything you build now compounds. Directly rewards duplicable, reusable subsystems |
| **R304** (2nd sentence) §12.3 | ROBOT software, designs, and FABRICATED ITEMS created **before Kickoff** are permitted | Pre-kickoff drivetrain/intake work is legal to bring to competition. *(NB: this clause is R304, not R305. **R305** is "SCORING ELEMENTS are not allowed for ROBOT construction" — current-season SCORING ELEMENTS or replicas may not be used as part of the ROBOT.)* |
| **R501/R502** §12.5 | Closed motor list; servos capped by mechanical output power and stall current at 6V | No exotic actuators. Cost and spares are predictable |
| **R503** §12.5 | **8 motors and 8 servos maximum**, summed across *all* configurations | Hard budget on mechanism count. Two mechanisms at 3 motors each + 4-motor drivetrain already breaks it |
| **R601** §12.6 | Exactly **1** approved 12V NiMH main battery | No adding power capacity for a hungry mechanism |
| **R801** §12.8 | **No pneumatic actuators**, no generated pressure/vacuum, no high-speed airflow devices (flywheels/rollers are *not* airflow devices) | Removes an entire class of "cheap fast actuation." Everything is motors and servos |
| **I302** §3.3.1 | Electronics limits apply across **all** configurations, whether simultaneously used or not | You cannot dodge R503 with swappable mechanisms |
| **I303** §3.3.2 | Re-inspection **not** generally required for: (D) code revision, (E) replacing a COMPONENT with an **identical** COMPONENT, (F) replacing a MECHANISM with an **identical** MECHANISM (size, weight, material), (G) reconfiguring with an already-inspected subset | **The rulebook itself rewards duplicability.** An identical spare mechanism is a drop-in at an event; a hand-fitted one-off is not |
| **§2** | Team Updates post **every Thursday** from Kickoff until two weeks before FIRST Championship | The nerf channel. See F16 |
| **§2** | Game Q&A opens **2026-09-28, 12:00 p.m. ET**; answers do not supersede the manual; REFEREES/INSPECTORS are final authority | You cannot resolve a strategy's legality by Q&A alone |
| **§2** | Season kicks off September, runs through March; capstone events April–July | Sets the calendar the time factors are anchored to |

### 1.2 BIOBUZZ facts published outside the manual (all CONFIRMED-PRESEASON, verified 2026-08-21)

| Fact | Source | Consequence |
|---|---|---|
| BIOBUZZ SCORING ELEMENT is **POLLEN** — plastic balls **approx. 3 in. diameter**, characteristics similar to DECODE ARTIFACTS. Purchasable from AndyMark **now** | FIRST community *Game Preview 2027: StarterBots, Skill Builders, Field Elements* | The manipulated object is a small sphere. Intake/hopper/roller geometry can be prototyped **before Kickoff**. Scoring *tasks* remain unknown |
| **StarterBot Base** = a drivetrain **and an intake**. Instructions published by **AndyMark, goBILDA, REV Robotics, Studica**. Full StarterBot designs release **at Kickoff** | same | Combined with **R301.B**, an official StarterBot mechanism is a legal COTS major mechanism. This is the single cheapest path to two working robots |
| **Skill Builders** — 7 free mini-games (precision driving, intake/outtake design, scoring cycles, autonomous routines) at `training.firstinspires.org` | FIRST community *Introducing FIRST Tech Challenge Skill Builders* | Free, structured pre-season driver and auto practice. Feeds F11 and, via A201, the portfolio |
| FTC 2026-27 registration **`$350`/season**. Recommended supporting materials **`~$1,500` estimated**: Driver Kit `$295`, REV Control Hub `$350`, Build Kit `$660` | firstinspires.org *Cost & Registration* | Two-team floor before any game mechanism: `2 × $350` + `2 ×` control/driver hardware + events |
| goBILDA **FTC Starter Kit (2026-2027 Season)** — **`$899.99`**; does **not** include a REV Hub control system | gobilda.com product page | Reference price for a per-robot structural + motor package |
| goBILDA **Strafer Chassis Kit V5** — `$599.99`, discontinued/sold out; replaced by **Strafer Chassis Kit V6 (96mm wheels)** at **`$624.99`** | gobilda.com product page | Reference price for a legal COTS drive CHASSIS under R301.A |

> **Note on availability:** prices and stock verified 2026-08-21 and will drift. Re-verify before committing a BOM.
> Anything not listed above with a dollar figure is **UNVERIFIED** and must be priced at BOM time.

### 1.3 Community and reference evidence used

| Source | Label | What it supports |
|---|---|---|
| **Game Manual 0** (gm0.org) — Design Strategy, 3D Printing, Drivetrains | HISTORICAL / reference | Scope discipline, execution-over-design, spare-part doctrine, drivetrain selection |
| **Chief Delphi** FTC 23511 *Seattle Solvers — DECODE OA thread* (t/506155) | HISTORICAL (FTC) | First launcher prototypes were "very inconsistent"; flexible (gecko) wheels worse than rigid (rhino); swerve plates machined by a college mentor, other plates outsourced to a service |
| **Chief Delphi** t/406178 *Thoughts on teams with multiple teams with the same robot* | HISTORICAL (FRC) | Mentors of a two-team program reported they lacked bandwidth to supervise two separate designs; the "SCREAM / SCREAM Jr" pattern — B team builds a **simplified variant of the same architecture** |
| **Chief Delphi** t/519884 *Was building a shooter an overscope for most teams?* | HISTORICAL (FRC 2026 REBUILT) | 50th-pct EPA 37.2 / 75th-pct 71.3; a "0 bps box on wheels" reached EPA 38.3 and qualified on points; **but** a single opposing robot can shut down a feed-the-human-player strategy |
| **BIOBUZZ V0** + **ITD 2024-25** + **DECODE 2025-26** manuals & Team Updates (local) | CONFIRMED-BIOBUZZ / HISTORICAL | Rule text, scoring tables, Team Update nerf history |

> **r/FTC was not reachable** from this environment (reddit.com is blocked to the search/fetch agent). No
> r/FTC evidence is cited. Where community consensus is asserted without a fetched source, it is labeled **JUDGMENT**.

---

## 2. The factor set at a glance

16 factors, four clusters, weights sum to **100**.

| # | Factor | Cluster | Polarity | **Weight** | One-line prediction |
|---|---|---|---|---|---|
| **F1** | Fabrication Complexity | A. Build feasibility | inverted | **9** | Can 15 students with hand tools + a printer actually make the parts? |
| **F2** | **Duplicability (A/B robot)** | A | direct | **9** | Does robot #2 cost the same as robot #1, or 3× the pain? |
| **F3** | BOM + Season Spares Cost | A | inverted | **5** | Can we afford it twice, *and* afford to break it? |
| **F4** | Time-to-First-Working-Prototype | A | inverted | **4** | How long until we know it can work at all? |
| **F5** | Time-to-Reliable | A | inverted | **4** | How long from "works once" to "works in 10 straight matches"? |
| **F6** | Iteration Cost (week-6 reversibility) | A | inverted | **3** | What does it cost to change our mind in December? |
| **F7** | Programming Burden | B. Operational reliability | inverted | **5** | How much *code* does this need before it does anything? |
| **F8** | **Tuning Burden** | B | inverted | **7** | How many empirical constants must be found, and do they drift? |
| **F9** | Sensor & Vision Dependence | B | inverted | **4** | How much does it depend on the field looking the way we expect? |
| **F10** | **Match Reliability & Failure Consequence** | B | direct | **8** | When it breaks mid-match, do we lose a cycle or the match? |
| **F11** | Driver Skill Ceiling & Practice Demand | B | inverted | **4** | How many practice hours before it out-scores the simple option? |
| **F12** | **Scoring Ceiling & Points-Per-Second** | C. Competitive payoff | direct | **12** | Why attempt it at all? |
| **F13** | Defense Resistance | C | direct | **5** | What happens when a robot parks on us? |
| **F14** | Alliance Value (incl. B-team synergy) | C | direct | **5** | Does it get us picked — and can A and B play together? |
| **F15** | **Award-Generation Potential** | C | direct | **8** | Does building it manufacture the evidence judges reward? |
| **F16** | Rule-Change Exposure | D. Strategic risk | inverted | **8** | How badly does a Thursday Team Update hurt? |

**Cluster totals:** A Build feasibility **34** · B Operational reliability **28** · C Competitive payoff **30** · D Strategic risk **8**.

---

## 3. Hard gates (checked *before* scoring)

Gates are **not** weights. A strategy that trips a gate is rejected or rewritten regardless of how well it
scores everywhere else. This prevents the classic rubric failure where a beautiful-on-paper strategy survives
because four 5s outvote one fatal 1.

| Gate | Trip condition | Action |
|---|---|---|
| **G1 — Legality** | Violates any final BIOBUZZ rule in Section 3 (I), 5 (E), or 12 (R) | **Reject.** Not a scoring matter |
| **G2 — Actuator budget** | Total motors > 8 **or** servos > 8 across all configurations for *one* robot (**R503**, reinforced by **I302**) | **Reject or re-scope.** Count the drivetrain first (4 motors is typical), then what remains |
| **G3 — Fabrication floor** | Requires a process the program does not own and cannot reliably buy: CNC milling/turning of structural parts, welding, waterjet, custom gears | **Reject** unless a named, priced, lead-time-verified outsourcing vendor is in the plan. Score F1 = 1 |
| **G4 — Two-robot feasibility** | Cannot be built twice within budget **and** mentor hours | **Reject** unless the plan explicitly de-scopes the B robot to a *different, simpler* architecture (the SCREAM Jr pattern) — and that de-scoped variant is then ranked as its own candidate |
| **G5 — Cash ceiling** | BOM + spares for **two** robots exceeds the program's stated cash ceiling | **Reject or re-scope.** Price both robots, never one |
| **G6 — Pneumatics/airflow** | Uses pneumatic actuation, generated pressure/vacuum, or a high-speed airflow device (**R801**) | **Reject.** Flywheels and rollers are fine; fans and blowers are not |
| **FLAG-1 — Deferred rule** | Depends on the still-unpublished **R105** sizing constraints, or on any Section 8–11 / 13 / 15 text | **Do not reject — flag.** Score, then re-score after Team Update 01 and 02 |

---

## 4. Factor definitions, anchors, and evidence

Each anchor is stated as an **observable**: a count, an hour, a dollar figure, a named process. If a scorer
cannot point at the observable, the factor is scored **U (unknown)** and the strategy goes on the prototype
list — see §8.

---

### F1 — Fabrication Complexity · Weight 9 · **inverted (5 = easiest to build)**

**Definition.** The manufacturing processes and skill required to produce every non-COTS part, from raw
stock to installed part, using only capability the program actually owns or has already paid for.

**Why it predicts.** A design the team cannot *make* is not a design, it is a wish. FTC's rules explicitly
carve out the two escapes that a low-fabrication team needs — **R301.A** (buy your drive chassis) and
**R301.B** (the official StarterBot mechanisms are legal COTS major mechanisms) — and **R302** legalises
drilling/cutting/painting stock kit parts. **R104** (no weight limit) removes the pressure to lightweight,
which is the pressure that pushes teams toward pocketed machined plate. A team with hand tools can therefore
build a competitive robot entirely out of bolt-together extrusion, plate, and printed parts, but only if the
design is *chosen* to be that.

**Observable to measure.** Count, for the whole strategy: (a) parts requiring subtractive machining beyond
drill/cut-off/file; (b) parts requiring a print > 6 h or > the print bed; (c) parts requiring press fits,
reaming, or hand-fitting to work; (d) processes not owned in-house.

| Score | Anchor (observable) |
|---|---|
| **1** | Requires ≥1 CNC-milled/turned/waterjet structural part, welding, or custom gears. No named vendor, price, and lead time in the plan |
| **2** | Requires outsourced flat-plate cutting (laser/waterjet service) for ≥2 load-bearing parts; team can order it but has never done so, and revisions cost a full lead-time cycle |
| **3** | Bolt-together kit structure, but ≥3 printed parts are load-bearing in multiple directions, or ≥2 parts need hand-fitting to work |
| **4** | Kit extrusion + plate + printed brackets. Every printed part is loaded in one orientation. Longest print < 4 h. Drill press, hacksaw, files, taps only |
| **5** | COTS chassis (R301.A) or StarterBot mechanism (R301.B) plus bolt-on kit parts. Printed parts are non-structural (guides, spacers, funnels). No part needs hand-fitting |

**Evidence.**
- **CONFIRMED-BIOBUZZ** — R301.A/B, R302, R104 as above. R104's removal of a weight limit is the specific
  reason a hand-tool team is not forced into machined parts: over-building is legal.
- **HISTORICAL (FTC)** — Chief Delphi FTC 23511 (DECODE OA thread): even a strong team outsourced flat plates
  to a cutting service and had a *college mentor* machine the complex swerve-module parts. That capability is
  not a hand-tool capability, and the team itself noted the parts "should work as 3D printed" only in a
  later, weight-driven revision. Treat "a mentor can machine it" as an outsourcing dependency, not a capability.
- **HISTORICAL (GM0, 3D Printing)** — printed parts are weaker than aluminium and should be **loaded in one
  orientation only**; side loads delaminate them. PLA is brittle under shock; PETG absorbs impact better.
  A design whose printed parts see multi-axis match loads is a 2, not a 4, however easy it is to print.

**Scoring traps.** (i) "We can print it" is not a 5 if the print is structural. (ii) A mentor's garage lathe
is a 1-or-2 dependency, not in-house capability — it does not scale to two robots and it disappears when
the mentor is busy. (iii) Do not score the *prototype* — score the competition part.

---

### F2 — Duplicability (A robot / B robot) · Weight 9 · **direct (5 = second copy nearly free)**

> **This is the factor generic FTC advice omits, and it is first-class for this program.**

**Definition.** The marginal cost — in dollars, mentor hours, and *tacit knowledge* — of producing a second
working instance of the design for the B team, at the same reliability as the first.

**Why it predicts.** This program is two registered teams sharing one shop, one parts stock, and one mentor
pool. Duplicability determines whether the program fields **two competitive robots** or **one robot and one
box on wheels**. That is not a robot question, it is an *advancement and awards* question:

- Each registered team has its own award eligibility. **A215** (CONFIRMED-BIOBUZZ) — a team may win or be
  runner-up for a **single** judged award at an event. Two teams therefore address **two** award slots.
- **§4.1 Table 4-1** (CONFIRMED-BIOBUZZ) — Inspire 1st Place is **60 advancement points**, more than winning
  the event (40). Any other 1st Place award is 12 points, comparable to the ~16 points of the top qualification
  seed. A second functioning team is a second 60-point lottery ticket, not a nicety.
- **I303.F** (CONFIRMED-BIOBUZZ) — replacing a MECHANISM with an **identical** MECHANISM (size, weight,
  material) does **not** generally require re-inspection. Identical A/B mechanisms are also each other's
  competition spares, legally droppable in. A hand-fitted one-off is not.
- **R304** (CONFIRMED-BIOBUZZ) — custom designs and parts persist year to year, so duplicable subsystems
  compound across seasons and non-duplicable ones do not.

**Observable to measure.** For the second copy: (a) fraction of parts that are catalogue-orderable; (b) number
of parts requiring individual fitting/shimming/matching; (c) whether the CAD/print files fully define the part
(is there tacit knowledge in one student's hands?); (d) marginal mentor-hours for copy #2 ÷ mentor-hours for copy #1.

| Score | Anchor (observable) |
|---|---|
| **1** | Copy #2 needs the same one student and the same 40+ mentor hours. Parts are hand-fitted, undocumented, or one-off machined. Marginal effort ≥ 0.8× original |
| **2** | Copy #2 is orderable but expensive (> 60% of original BOM) *and* needs meaningful re-tuning; no CAD/print files exist yet |
| **3** | Reproducible from files, but 2–4 parts need per-robot fitting and each robot needs its own tuning pass |
| **4** | 100% catalogue + print-file defined; copy #2 assembles from a printed BOM by a student who did not build copy #1; one short tuning pass per robot |
| **5** | COTS chassis / StarterBot mechanism, or a design whose entire parts list is a shopping cart. Copy #2 is a purchase order plus an assembly session. Mechanisms are interchangeable between A and B (I303.F drop-in spares) |

**Evidence.**
- **HISTORICAL (FRC, CD t/406178)** — the mentors of a well-known two-team program stated they **did not have
  the mentor bandwidth to supervise two separate designs**. That is exactly this program's constraint, stated
  by people who ran the experiment.
- **HISTORICAL (FRC, CD t/406178)** — the "SCREAM / SCREAM Jr" pattern: the second team built a
  **simplified variant of the same architecture** (score from one fixed spot; lower-tier endgame) rather than
  a different robot. That is the correct fallback when F2 scores 2–3, and it is why **G4** offers re-scoping
  instead of rejection.
- **HISTORICAL (FRC, CD t/406178)** — the counter-argument, worth recording honestly: with two teams, more
  students get hands-on design time, and some mentors argue for two *different* robots on pedagogical grounds.
  For a **~15-student** program that argument loses to the mentor-bandwidth one; for a 40-student program it wins.
- **HISTORICAL (GM0, 3D Printing)** — print **one full set of every printed part as spares** for competition;
  if you run out at an event you are out of luck. For a two-robot program that means **three** sets minimum
  (A, B, spares) — a design with 25 printed parts implies 75 prints. Printed-part count is a duplicability cost,
  not just a fabrication cost.

**Scoring traps.** (i) Scoring the *design* as duplicable when the *tuning* is not — a design where each robot
needs its own bespoke constants is a 3 at best, no matter how identical the hardware. (ii) Forgetting that the
B robot needs its own control hub, driver station, and battery set. (iii) Counting "we'll build the second one
later" as duplicability — later never arrives; check the calendar in F4/F5.

---

### F3 — BOM + Season Spares Cost · Weight 5 · **inverted (5 = cheapest)**

**Definition.** Total cash for **two** robots, plus the consumables and spares needed to survive a season of
collisions, plus event costs already committed.

**Why it predicts.** The fixed floor is large and known. **CONFIRMED-PRESEASON**: registration is `$350`
per team per season — `$700` for this program before a single bolt — and FIRST estimates `~$1,500` of
recommended supporting materials per team (Driver Kit `$295`, REV Control Hub `$350`, Build Kit `$660`).
Reference mechanism/structure packages: goBILDA FTC Starter Kit (2026-2027) `$899.99`; a legal COTS drive
chassis (R301.A) around `$599.99–$624.99`. Every dollar the game mechanism costs is a dollar times two, and
the spares budget is the one teams cut first and regret at the event.

**Observable to measure.** (a) Marginal BOM of the game mechanism, ×2; (b) count of *wear/impact* parts and
their unit price; (c) cost of one full spare set of every printed part ×3 sets; (d) whether any single part
failure has a >2-week lead time.

| Score | Anchor (observable) |
|---|---|
| **1** | Marginal mechanism BOM > `$800`/robot, or any single-source part with > 2-week lead time and no spare budgeted |
| **2** | `$500–$800`/robot marginal, spares unbudgeted |
| **3** | `$250–$500`/robot marginal, with a partial spares kit |
| **4** | `$100–$250`/robot marginal; full spare set of printed parts and all wear items budgeted and in the pit bin |
| **5** | < `$100`/robot marginal — reuses parts already owned under **R304**, or is a StarterBot/COTS-chassis derivative already paid for. Spares are literally the other robot's identical parts (**I303.F**) |

**Evidence.**
- **CONFIRMED-PRESEASON** — the registration, kit, and chassis figures above (verified 2026-08-21; re-verify at BOM time).
- **CONFIRMED-BIOBUZZ** — **R304** makes last season's parts and pre-Kickoff fabrication legal, so
  inventory is real budget. **R601** allows exactly one main battery per robot: budget spare *batteries*
  (legal to own, one installed) as a reliability item, not an optional.
- **HISTORICAL (GM0, 3D Printing)** — a full spare set of printed parts is doctrine, not luxury.

**Scoring traps.** (i) Pricing one robot. (ii) Omitting the second control system. (iii) Treating filament as
free — 75 prints of a 200 g part is `~15 kg` of filament. (iv) Ignoring event registration, which is set
regionally and is often the largest line item after the robots.

---

### F4 — Time-to-First-Working-Prototype · Weight 4 · **inverted (5 = fastest)**

**Definition.** Calendar days from Kickoff (2026-09-12) to a rough mechanism that completes the game task
**once**, on the real POLLEN element, off the competition robot.

**Why it predicts.** It is the *risk-retirement clock*. A strategy that cannot be proven in a few weeks
consumes the schedule you need for reliability and driving. Season structure (**CONFIRMED-BIOBUZZ §2**):
kicks off September, runs through March, capstone events April–July — but a team's *first* event is typically
far earlier than March, so the usable build window is short.

| Score | Anchor (observable) |
|---|---|
| **1** | > 6 weeks to first successful attempt, or requires a part with a lead time that lands after your first event |
| **2** | 4–6 weeks — most of the pre-first-event window is consumed proving it can work at all |
| **3** | 2–4 weeks |
| **4** | 1–2 weeks, using materials already in the shop |
| **5** | ≤ 1 week, or **already proven before Kickoff** — POLLEN is purchasable now and the StarterBot Base (drivetrain + intake) is published now (**CONFIRMED-PRESEASON**), so intake/ball-handling concepts can be at "works once" on Kickoff morning |

**Evidence.**
- **CONFIRMED-PRESEASON** — POLLEN available pre-Kickoff; StarterBot Base published by AndyMark, goBILDA, REV,
  Studica; Skill Builders provide structured pre-season intake/outtake and cycle exercises. **R304** makes
  pre-Kickoff fabrication competition-legal. A team that arrives at Kickoff with a working ball intake has
  bought itself weeks.
- **HISTORICAL (FTC, CD 23511)** — that team's *first* launcher prototypes were reported as very inconsistent,
  and the difference between flexible and rigid contact wheels was discovered empirically. First prototypes
  answer "can it work", never "does it work".

**Scoring trap.** Scoring the *CAD* completion date. The clock stops when the physical thing succeeds once.

---

### F5 — Time-to-Reliable · Weight 4 · **inverted (5 = fastest)**

**Definition.** Additional calendar time from "works once" to "works 9 times out of 10, on a battery that is
half-drained, after being hit."

**Why it predicts.** This is where seasons are actually lost, and it is *not* correlated with F4. A flywheel
launcher is quick to build and slow to make repeatable; a bolt-on hook is slow to design and instantly
repeatable. Splitting F4 and F5 is what stops the model from rewarding "we had something moving in week 2."

| Score | Anchor (observable) |
|---|---|
| **1** | Reliability is still improving at the first event; success rate < 60% in practice |
| **2** | Needs > 6 weeks past first prototype; success rate plateaus around 70% |
| **3** | 3–6 weeks; ~80% success, sensitive to battery state or field position |
| **4** | 1–3 weeks; ≥ 90% success across battery states and starting positions |
| **5** | Reliable on first assembly — success is a geometric/mechanical property, not a tuned one (e.g. a passive funnel, a hook, a fixed-height deposit) |

**Evidence.**
- **HISTORICAL (GM0, Design Strategy)** — a robot that does one thing consistently beats a robot that does
  everything inconsistently; build for the worst case, not the best case; consistency matters more than peak
  scoring because top teams pick *reliable* partners.
- **CONFIRMED-BIOBUZZ** — the award criteria encode this directly: Innovate §6.3.6 requires the creative design
  be **stable and reliable** and help reach game goals **most of the time**; Design §6.3.8 encourages that the
  design **works consistently**; Control §6.3.7 encourages the control solution work consistently during **most
  MATCHES**. Unreliable = unjudgeable, not just unscoreable.

**Scoring trap.** Confusing "it worked in the last 3 tries" with a measured success rate. Require a logged
n ≥ 20 trial count before scoring 4 or 5.

---

### F6 — Iteration Cost (week-6 reversibility) · Weight 3 · **inverted (5 = cheapest to change)**

**Definition.** The cost — parts, hours, and destroyed work — of substantially changing this mechanism's
geometry or concept **six weeks in**, when you have learned what the game actually rewards.

**Why it predicts.** Every team is wrong about the game in week 1. What separates programs is whether being
wrong is survivable. Modular, bolted, catalogue-parts designs let you change your mind; welded/machined/
integrated designs punish it. For a ~15-student, low-mentor-hour program, an unrecoverable week-6 decision is
functionally a season-ending decision.

**Observable to measure.** (a) Fraction of the mechanism that must be discarded to change one design parameter;
(b) number of fasteners vs. permanent joints; (c) whether mounting is on a slotted/gridded structure; (d) lead
time for the replacement parts.

| Score | Anchor (observable) |
|---|---|
| **1** | Change requires re-ordering outsourced plates (multi-week) or scrapping the chassis. Cost > 50% of original build |
| **2** | Change scraps the mechanism but not the chassis; 2+ weeks and > 30% of BOM |
| **3** | Change means re-printing several parts and re-drilling structure; ~1 week |
| **4** | Change is re-printing 1–2 brackets and moving bolts on existing extrusion; < 3 days |
| **5** | Change is repositioning on a slotted/gridded structure with existing hardware; hours. Mechanism attaches at a defined interface so the whole subsystem can be swapped |

**Evidence.**
- **HISTORICAL (GM0, Design Strategy)** — a mid-season rebuild is realistic only for experienced teams and is
  described as a 50–100+ hour undertaking; rookies and small teams should iterate the design they have rather
  than restart. So for this program, iteration cost must be *designed in* up front.
- **CONFIRMED-BIOBUZZ** — **I303.G** — reconfiguring the ROBOT with a *subset of already-inspected MECHANISMS*
  generally needs no re-inspection. Designing to a clean subsystem interface therefore buys in-event flexibility too.
- **HISTORICAL (FTC, CD 23511)** — mounting intake rollers on separate "daughter plates" so they can be adjusted
  independently of the main frame plates is the concrete pattern that turns a 2 into a 4.

**Scoring trap.** Rating a design 5 because it *is* bolted, when in practice the bolt pattern is unique to one
geometry. Ask: "what physically changes if we need 2 inches more reach?"

---

### F7 — Programming Burden · Weight 5 · **inverted (5 = least code)**

**Definition.** The volume and difficulty of *software* the strategy requires before the mechanism does its job —
distinct from tuning. Measured in subsystems, state machines, and control loops, not lines.

**Why it predicts.** This program has ~15 students across two teams; realistically one to three of them write
code, and they must support **two** robots. Programming burden is one of the few costs that does **not**
duplicate cheaply *if* the two robots differ — and duplicates nearly free if they are the same architecture,
which is another reason F2 and F7 interact.

| Score | Anchor (observable) |
|---|---|
| **1** | Needs motion profiling, path following, a multi-state coordinated sequence, and a custom control loop before scoring at all |
| **2** | Needs closed-loop position/velocity control on ≥2 subsystems plus a state machine |
| **3** | Needs encoder-based positioning with PID on one subsystem, plus a simple sequence |
| **4** | Needs run-to-position on a motor and a couple of servo presets; stock SDK features throughout |
| **5** | Direct operator control of a motor/servo. Auto is drive-forward-and-deposit. Works with what the SDK gives you |

**Evidence.**
- **CONFIRMED-BIOBUZZ** — **R503** caps actuators at 8 motors / 8 servos, which bounds how much there is to
  coordinate; **R303** legalises COTS **dead-wheel odometry kits**, which is the cheapest legal route to
  decent localization without custom hardware.
- **CONFIRMED-BIOBUZZ** — **I303.D**: revising ROBOT code does **not** require re-inspection. Software is the
  cheapest thing to change at an event; hardware is not. That asymmetry argues for *pushing* complexity into
  software when the alternative is a hardware change — but only up to the tuning limit (F8).
- **HISTORICAL (GM0, Design Strategy)** — partial automation is recommended specifically to reduce driver error
  and cognitive load, i.e. some programming burden *buys down* F11.

**Scoring trap.** Scoring the burden for the A team's best programmer. Score it for whoever will maintain the
**B robot's** code in February.

---

### F8 — Tuning Burden · Weight 7 · **inverted (5 = fewest constants)**

> Deliberately separate from F7. **A shooter is easy to build and brutal to tune.**

**Definition.** The number of empirically-determined constants the mechanism needs, how strongly performance
depends on them, and how much they **drift** with battery voltage, wear, temperature, humidity, static, and venue.

**Why it predicts.** Tuning cost is paid in *field time with the real element*, which is the scarcest resource
a modest program has — and it is paid **once per robot**, so it is the hidden multiplier on F2. Worse, tuning
constants that drift must be re-found at the venue, on the morning of, with no practice field.

**Observable to measure.** (a) Count of empirical constants; (b) sensitivity — does a ±5% change visibly hurt?
(c) drift sources — voltage, wear, surface, humidity/static; (d) whether the constants transfer between robot A and B.

| Score | Anchor (observable) |
|---|---|
| **1** | > 10 empirical constants; performance is a function of robot pose and battery voltage; constants do **not** transfer between the two robots and must be re-found at each venue |
| **2** | 6–10 constants with real drift (velocity-controlled launch, variable-distance aiming) |
| **3** | 3–5 constants, mildly drift-sensitive (a PID'd arm, a timed sequence tuned to a surface) |
| **4** | 1–2 constants, stable across batteries and venues (a hold power, a servo preset) |
| **5** | Zero empirical constants — geometry does the work. Hard stops, funnels, gravity, a fixed hook |

**Evidence.**
- **HISTORICAL (FTC, CD 23511 DECODE)** — that team's first single-wheel launcher prototypes were reported as
  **very inconsistent**, with a strong dependence on ball–wheel contact time and on wheel compliance (flexible
  "gecko" wheels performed worse than rigid "rhino" wheels). Nothing about that is a *build* problem; it is
  entirely a tuning/consistency problem, discovered empirically.
- **HISTORICAL (FTC, CD community, DECODE)** — teams reported tuning dual launcher motors to matched velocity
  and adding RPM/velocity-based control to improve consistency, and that this only partially solved it; static
  electricity was reported as an additional inconsistency source. Label **HISTORICAL/JUDGMENT** — reported in
  season threads, not measured here.
- **CONFIRMED-BIOBUZZ** — **R601**: exactly one 12V NiMH battery. You cannot engineer around voltage sag with
  more capacity, so voltage-dependent mechanisms carry unavoidable drift. This is the rule-level reason
  velocity-critical launchers score low on F8.
- **CONFIRMED-PRESEASON** — POLLEN is a ~3 in. plastic ball similar to DECODE's ARTIFACTS, so DECODE's
  ball-handling tuning experience is the most transferable historical evidence available for BIOBUZZ. It is
  still **HISTORICAL**, not a BIOBUZZ fact.

**Scoring trap.** The single most common ranking error in FTC. Teams score a launcher 4 on F1 (easy to build —
correct) and then let that halo it to a 4 on F8 (wrong). **Score F1 and F8 in separate passes, column-wise.**

---

### F9 — Sensor & Vision Dependence · Weight 4 · **inverted (5 = least dependent)**

**Definition.** How much the strategy's *scoring* (not its polish) depends on sensors, AprilTags/vision, or
field-relative localization behaving as expected under real venue lighting and real collisions.

**Why it predicts.** Sensors add capability and add a failure mode that is invisible in the pit and fatal on
the field. Vision in particular fails on venue lighting, on a bumped camera mount, and on an occluded tag —
none of which reproduce in your shop.

**Note the tension with awards:** the **Control Award (§6.3.7, CONFIRMED-BIOBUZZ)** *requires* one or more
hardware/software solutions that use **external feedback**. So F9 = 5 (no sensors) forfeits Control eligibility.
This is a genuine trade the ranking must surface rather than hide — see §10.

| Score | Anchor (observable) |
|---|---|
| **1** | Primary scoring path fails without vision/tag localization. No non-vision fallback |
| **2** | Vision-dependent for high-value scoring; a manual fallback exists but is much slower |
| **3** | Uses vision/odometry for auto only; teleop scoring is fully manual |
| **4** | Uses only robust proprioceptive sensors — encoders, limit switches, IMU. Failures are detectable and recoverable in-match |
| **5** | No sensor is required to score. Sensors, if present, are convenience only |

**Evidence.**
- **CONFIRMED-BIOBUZZ** — **R303** permits COTS dead-wheel odometry kits (robust, cheap localization);
  §6.3.7 Control Award criteria require external feedback and encourage the team to *explain how reliable*
  the solution is and how it could be improved — i.e. FIRST rewards honest reliability analysis, not sensor count.
- **CONFIRMED-BIOBUZZ** — **R702**: teams may not alter coprocessor software unless explicitly allowed, and
  **R701**: a single ROBOT CONTROLLER. Vision architecture options are bounded; verify any camera/coprocessor
  plan against §12.7 before committing.
- **JUDGMENT** — the correct pattern for this program is *sensor-assisted, not sensor-dependent*: encoders and
  an IMU for a repeatable auto (Control evidence, low risk), manual teleop scoring (low risk), and vision only
  where a clean fallback exists.

**Scoring trap.** Scoring 4 because "we'll add sensors later." Score what the strategy *requires* to hit its
claimed F12 score.

---

### F10 — Match Reliability & Failure Consequence · Weight 8 · **direct (5 = safest)**

**Definition.** Two things multiplied: probability of failure during a 2.5-minute match, and **severity** —
does the failure cost one cycle, all remaining cycles, or the match (immobilised robot, foul, or damage).

**Why it predicts.** Severity is what teams under-weight. A jam you can clear in 5 seconds is cheap; a jam
that immobilises the drivetrain is a zero. Severity is also a *rules* question: **R201** requires robots be
designed not to damage the ARENA or make a mess, and **R203** requires the robot be removable from the FIELD
quickly **without power** — a failure mode that violates either is far worse than a lost cycle.

**Observable to measure.** (a) Number of single-point-of-failure elements between input and score; (b) whether
a failure is *recoverable by the driver* mid-match; (c) whether failure risks a foul or damage; (d) whether an
identical spare exists that is a legal drop-in under **I303.E/F**.

| Score | Anchor (observable) |
|---|---|
| **1** | A likely failure immobilises the robot, drops a SCORING ELEMENT where it causes a foul, or risks ARENA damage (**R201**) or a robot that cannot be removed unpowered (**R203**) |
| **2** | Failure ends all scoring for the match; not driver-recoverable; no spare |
| **3** | Failure ends scoring for the match but robot still drives and can play defense/park |
| **4** | Failure costs 1–2 cycles and the driver can clear it (reverse the intake, re-home the arm) |
| **5** | No plausible in-match failure removes scoring. Degrades gracefully. Identical spare mechanism exists and is a legal drop-in between matches under **I303.F** |

**Evidence.**
- **CONFIRMED-BIOBUZZ** — R201, R203, I303.E/F as above. **R104** (no weight limit) means over-building for
  impact costs nothing but battery and is the cheapest reliability purchase available to a hand-tool team.
- **HISTORICAL (GM0, Design Strategy)** — build for the worst case; design redundancy; account for collision
  forces; simpler mechanisms have fewer failure points.
- **HISTORICAL (FRC, CD t/519884)** — a team lost a launcher at the World Championship when one motor failed
  while its partner idled, stripping a pinion — **and they had no replacement pinion**. The failure was cheap;
  the missing spare was not. Spares are part of this factor, not just F3.
- **HISTORICAL (GM0, 3D Printing)** — out of printed spares at a competition means out of luck.

**Scoring trap.** Scoring probability and ignoring severity. Force the scorer to write the sentence:
*"When this fails mid-match, we lose ___."* If the blank is "the match", the ceiling is 2.

---

### F11 — Driver Skill Ceiling & Practice Demand · Weight 4 · **inverted (5 = least practice needed)**

**Definition.** How many hours of driver practice separate a novice's output from the strategy's claimed
scoring rate, and how steep the learning curve is.

**Why it predicts.** A strategy that only pays off with an expert driver is a strategy the B team cannot run,
and with ~15 students across two teams, driver depth is thin and turnover is annual. High practice demand also
competes directly with build and portfolio time, which are the same evenings.

| Score | Anchor (observable) |
|---|---|
| **1** | Requires precise positioning at speed under defense; claimed rate needs > 40 h practice; a novice gets < 40% of it |
| **2** | Requires consistent alignment; 20–40 h to reach claimed rate |
| **3** | 10–20 h; novice reaches ~70% of claimed rate |
| **4** | < 10 h; forgiving alignment tolerance (funnels, wide capture, driver-assist presets) |
| **5** | Near-zero skill floor. Novice matches expert output within a session. Both A and B drive teams can run it in week 1 |

**Evidence.**
- **CONFIRMED-PRESEASON** — **Skill Builders**: 7 free mini-games explicitly covering precision driving, intake/
  outtake, scoring cycles and autonomous routines, free at `training.firstinspires.org`, usable **now**. This is
  the cheapest way to move a strategy's effective F11 up before Kickoff, and it is portfolio-eligible under
  **A201.E** (content from 2026-01-01 onward).
- **HISTORICAL (GM0, Design Strategy)** — driver practice must be continuous, not crammed before competition;
  partial automation reduces driver error and cognitive load.
- **HISTORICAL (CD, driver-practice threads)** — some programs report 10+ h/week of practice from early season.
  Treat that as the *high-resource* end of the distribution, not a target for a ~15-student program.

**Scoring trap.** Scoring for your best driver. Score for the **B team's rookie driver**, because that is the
median driver this program will field across two teams and two seasons.

---

### F12 — Scoring Ceiling & Points-Per-Second · Weight 12 · **direct (5 = highest)**

> **The largest single weight. Without it, the model ranks "do nothing" first.**

**Definition.** Realistically achievable points per match at *this program's* execution level — expressed as
points-per-second of match time consumed, including travel, acquire, align, score, and reset — plus the
strategy's ceiling if everything goes right.

**Why it predicts.** It is the entire reason to attempt anything. Achievability without payoff produces a
robot that is trivially achievable and worth nothing. PPS rather than raw points is the right unit because
match time is the binding constraint and a high-value action that consumes 20 seconds may be worth less than
a low-value action that consumes 4.

**Observable to measure.** (a) Points per successful action; (b) measured seconds per full cycle at *your*
driver skill; (c) realistic success rate (from F5) applied as a multiplier; (d) whether the action is
repeatable or a once-per-match endgame; (e) whether the alliance partner competes for the same scoring resource.

| Score | Anchor (observable) |
|---|---|
| **1** | Contributes < 10% of a typical winning score at realistic success rate |
| **2** | 10–20% — a parking/support role |
| **3** | 20–35% — a credible third robot |
| **4** | 35–55% — a solid second pick; a strong once-per-match endgame counts here if the point value is high |
| **5** | > 55% of a typical winning score at *realistic* rate, or is the single highest-PPS action available to a robot of this class |

**Evidence — how to instantiate this on Kickoff day.**
- **HISTORICAL (ITD 2024-25, §10.5.4 Table 10-3)** — point values were: PARK 3 · SAMPLE in NET ZONE 2 ·
  LOW BASKET 4 · HIGH BASKET 8 · LOW CHAMBER 6 · **HIGH CHAMBER 10** · ASCENT LEVEL 1 = 3 · **LEVEL 2 = 15** ·
  **LEVEL 3 = 30**. Two lessons transfer: (a) the highest-value repeatable action (HIGH CHAMBER, 10) was
  reachable with a *short* mechanism, while the 8-point action needed a tall extension — value did not track
  difficulty; (b) a single endgame action worth **30** rivalled several minutes of cycling, so a one-shot
  mechanism can be an F12 = 4 despite a cycle count of one.
- **HISTORICAL (FRC 2026 REBUILT, CD t/519884)** — a program that fielded a **non-scoring** driveable robot
  finished at roughly the field's median performance rating and still qualified onward on points. Useful
  calibration for F12 = 2: a reliable box on wheels is *not* worthless. Cross-program, so **HISTORICAL** only.
- **CONFIRMED-BIOBUZZ** — **§4.1 Table 4-1**: qualification-phase performance is worth 2–16 advancement points.
  That is the true competitive value of F12 for *advancement* purposes, and it is smaller than one Inspire
  Award. F12 gets the biggest weight because it is the reason to build, not because it is the biggest
  advancement lever — see §6.

**Scoring trap.** Scoring the *theoretical* cycle time from CAD. Multiply by the F5 success rate and by a
driver-skill factor from F11 before scoring. A 5-second cycle at 60% success is an 8.3-second cycle.

---

### F13 — Defense Resistance · Weight 5 · **direct (5 = hardest to stop)**

**Definition.** How much of the strategy survives an opponent whose entire plan is to stop you — by blocking a
location, by contact, or by denying a resource.

**Why it predicts.** Any strategy that funnels through **one location** or **one narrow corridor** is
shut down by one opponent robot that simply parks there — and that opponent needs no mechanism at all, which
means even weak opponents can execute it. This is the specific failure mode of "low-fabrication" strategies
that avoid building a mechanism by relying on a fixed delivery point.

| Score | Anchor (observable) |
|---|---|
| **1** | Requires occupying one specific spot, or depends on a resource an opponent can deny outright. One parked robot zeroes you |
| **2** | Single scoring location; a defender halves the rate; no alternate scoring path |
| **3** | Scoring location is contestable but there is a slower fallback |
| **4** | Multiple scoring positions or scoring on the move; defense costs cycles, not the strategy |
| **5** | Scoring is position-independent, or occurs where opponents may not legally be, or is an endgame action defense cannot reach |

**Evidence.**
- **HISTORICAL (FRC 2026 REBUILT, CD t/519884)** — the central argument against the low-tech "collect and feed
  the human players" strategy was precisely this: an opponent robot with no mechanism at all can park in the
  delivery corner and shut it down completely, and once teams notice, it works maybe once or twice at an event.
  The cheapest strategy to *build* was the cheapest strategy to *defend*.
- **HISTORICAL (rules pattern, ITD + DECODE)** — every recent game has protected-zone rules that shape defense
  (ITD **G410** limited control to 1 SAMPLE/SPECIMEN; DECODE **G408** capped simultaneous control at 3 ARTIFACTS,
  **G416** restricted LAUNCHING to LAUNCH ZONES, and multiple G-rules created protected zones). BIOBUZZ's
  Section 11 G-rules are **deferred to Kickoff**, so F13 cannot be scored properly until Kickoff — score it
  provisionally and mark **FLAG-1**.
- **CONFIRMED-BIOBUZZ** — **R104** (no weight limit) cuts both ways: opponents may build heavy defenders, and
  so may you. A heavier robot is a cheap defense-resistance purchase for a hand-tool team.

**Scoring trap.** Assuming opponents will not bother. Assume the *lowest-capability* opponent at the event
plays defense against you, because that is who has nothing better to do.

---

### F14 — Alliance Value (including B-team synergy) · Weight 5 · **direct (5 = most desirable partner)**

**Definition.** How much the strategy raises your value to an alliance captain — plus, uniquely for this
program, whether the A and B robots **complement** each other rather than compete for the same field resource.

**Why it predicts.** Advancement is not purely individual. **§4.1 Table 4-1 (CONFIRMED-BIOBUZZ)** awards
`21 − draft position` for accepting a draft slot (18 points for the 3rd draft acceptance) and `21 − alliance
lead number` for leading, plus 40/20/10/5 for Winning-Alliance finish. Being *pickable* is worth roughly as
much as being individually good.

The two-team dimension is real: if A and B build identical robots that both compete for the same scoring
resource, an alliance that fields both gets less than the sum. If B is a de-scoped complement (defense,
feeding, a different scoring path, or a reliable endgame), the pair is worth more.

| Score | Anchor (observable) |
|---|---|
| **1** | Actively harms alliance value — hogs a shared resource, causes fouls, or is unpredictable to plan around |
| **2** | Neutral filler; picked late if at all |
| **3** | Reliable driveable partner: parks, plays clean defense, does not cause fouls |
| **4** | Adds a capability captains actively want and can plan around; A and B do not contend for the same resource |
| **5** | Captain-grade or first-pick-grade contribution, **and** the A/B pair is deliberately complementary so both robots are individually pickable |

**Evidence.**
- **CONFIRMED-BIOBUZZ** — §4.1 Table 4-1 draft/lead/playoff point structure as above.
- **HISTORICAL (FRC, CD t/406178)** — the SCREAM Jr pattern again: the second team ran a *simplified* version
  of the same architecture and served as the program's development squad, and observers rated the arrangement
  positively. The pattern that works is **shared architecture, differentiated role** — which is also the pattern
  that maximises F2.
- **HISTORICAL (FRC, CD t/519884)** — alliance composition in a recent game settled into 2 offense + 1 defense
  even at the top level; a robot that is a reliable *defender* is a real pick, and defense is the lowest-
  fabrication role available. That is the natural B-robot role when F2 forces de-scoping.
- **HISTORICAL (GM0)** — top teams prioritise *reliable* partners at alliance selection, which links F14 to F5/F10.

**Scoring trap.** Scoring alliance value from a mechanism list rather than from a captain's point of view.
Ask: "what does the captain write next to our number on their pick list?"

---

### F15 — Award-Generation Potential · Weight 8 · **direct (5 = richest evidence)**

**Definition.** How much *judgeable evidence* the act of designing and building this strategy naturally
produces — and how directly that evidence maps onto specific BIOBUZZ award criteria.

**Why it predicts.** For a modest program, awards are the highest-yield advancement currency available, and
they are the currency where a ~15-student team competes on equal terms with a powerhouse.
**§4.1 Table 4-1 (CONFIRMED-BIOBUZZ)** is unambiguous:

| Achievement | Advancement points |
|---|---|
| **Inspire Award 1st Place** | **60** |
| Winning Alliance (1st Place) | 40 |
| Inspire 2nd / 3rd | 30 / 15 |
| Finalist Alliance (2nd Place) | 20 |
| **Any other 1st Place judged award** | **12** |
| Top qualification seed (approx. max) | 16 |
| Any other 2nd / 3rd Place judged award | 6 / 3 |

One Inspire win outweighs winning the event outright. Two registered teams = two independent shots at that,
because **A215 (CONFIRMED-BIOBUZZ)** limits each team to a single judged award *per event* but says nothing
about sibling teams.

**The BIOBUZZ award catalog is final now (Section 6, CONFIRMED-BIOBUZZ):** Inspire; **Think**; TA awards
**Connect / Reach / Sustain**; MCI awards **Design / Innovate (sponsored by RTX) / Control**; Judges' Choice.
Note the Motivate Award **does not exist** in this catalog — HISTORICAL DECODE Team Update 00 recorded its
retirement and replacement by Reach and Sustain. Do not cite Motivate.

**Which criteria a *design choice* can satisfy** (all CONFIRMED-BIOBUZZ, §6.3):

| Award | Portfolio required? | What the design must produce |
|---|---|---|
| **Think** §6.3.2 | **Yes** | Evidence of the engineering process; lessons learned applied to the ROBOT; **comparing choices** (alternatives considered and why one won); **math choices** (math used to make a robot/software decision) |
| **Innovate** §6.3.6 | No | Engineering work showing how the design was developed; the ROBOT or a MECHANISM is creative/unique; the creative design is **stable and reliable** and helps reach game goals **most of the time**; encouraged: explain how design **risks were reduced** |
| **Control** §6.3.7 | **Yes** | Portfolio summary of hardware/software control COMPONENTS, the challenge each solves, and its function; **one or more solutions using external feedback**; encouraged: consistent across most MATCHES, and a reliability explanation |
| **Design** §6.3.8 | No | ROBOT is **elegant, efficient (simple to build and operate), and/or practical to maintain**; the **whole** ROBOT or the detailed process, not one component; encouraged: distinctive appearance + function, articulated reasoning, **works consistently and aligns with the game plan** |
| **Inspire** §6.3.1 | **Yes** | Strong contender in **at least one MCI award AND one TA award AND Think** |
| **Connect / Reach / Sustain** §6.3.3–5 | No | Team-attribute awards — not generated by a design choice. Tracked separately |

| Score | Anchor (observable) |
|---|---|
| **1** | Produces no distinctive artifact: no alternatives compared, no math, no measurable reliability story, no sensor/feedback story. Nothing to write in the 15 pages |
| **2** | Supports one award weakly — e.g. a generic control claim with no external feedback |
| **3** | Cleanly supports **one** MCI award with real evidence (documented alternatives + a decision, or a genuine feedback loop) |
| **4** | Supports **two** MCI awards — e.g. Design (simple to build/maintain, whole-robot coherence) *and* Think (documented comparison + math), with reliability data to back the "works consistently" criteria |
| **5** | Supports an MCI award **and** produces the Think evidence **and** the build story feeds a TA narrative — i.e. it puts the team on the **Inspire** path per §6.3.1, with a sensor/feedback element that also opens Control |

**Evidence and mechanics.**
- **CONFIRMED-BIOBUZZ, A201** — the PORTFOLIO is capped at **1 cover page + 15 pages of content**, US Letter or
  A4, < 15 MB digital, and may **only** contain progress from **2026-01-01 onward**. Judges will **not** click
  links or videos, and cannot take extra papers from an interview. Everything must be *in* the 15 pages.
  → **Consequence for ranking:** page budget is a scarce resource. A strategy that generates 40 pages of evidence
  is not better than one that generates 12 crisp pages. Score the *density* of judgeable evidence, not the volume.
- **CONFIRMED-BIOBUZZ, A201** — FIRST explicitly permits AI and research aids for composing portfolios,
  provided IP rights are respected and a footnote/endnote credit is included (the manual's own example credit
  format is "Portfolio created by Team XXXXX and ChatGPT"). This harness's outputs are usable in the portfolio
  **with attribution**.
- **CONFIRMED-BIOBUZZ, A203/A204/A205** — every team must participate in an Initial Interview to be eligible for
  any judged award; all teams get equal interview time; A204 covers what to bring. A design nobody can *explain*
  scores 1 here regardless of how good it is.
- **CONFIRMED-BIOBUZZ, A211 Table 6-1** — the number of awards scales with event size, and only listed awards
  are points-eligible for advancement. At a small event (4–10 teams) only one TA award and one MCI award are
  given; at 21–40 teams the set is wider. → **Score F15 against the event you are actually attending.**
- **CONFIRMED-BIOBUZZ, A213/A214** — Inspire eligibility is limited to your own region, and a team may win 1st
  place Inspire only once per season from Qualifying/League Tournaments.
- **HISTORICAL (GM0, Awards)** — judging is subjective and varies regionally; the portfolio is the central
  artifact; teams should document *how* decisions were made, not just what was built.

**Scoring trap.** Assuming award potential is a property of the *portfolio writer*. It is a property of the
**design process**: if you never built two prototypes and measured them, there is no "comparing choices"
evidence to write, and Think criterion 1C is simply unavailable to you in February.

---

### F16 — Rule-Change Exposure · Weight 8 · **inverted (5 = least exposed)**

**Definition.** How much of the strategy's value depends on rule text that could be changed, clarified, or
tightened by a Thursday Team Update — or on Section 8–11 / 13 / 15 text that does not exist yet.

**Why it predicts.** **CONFIRMED-BIOBUZZ (§2):** Team Updates post **every Thursday from Kickoff** until two
weeks before FIRST Championship; additions are highlighted yellow and deletions struck through; updates
published after an event's driver's meeting do not apply at that event. The **Game Q&A opens 2026-09-28,
12:00 p.m. ET** with moderators answering Monday through Thursday 5:00 p.m. ET — and Q&A answers do **not**
supersede the manual; REFEREES and INSPECTORS are the final authority. So you cannot pre-clear a clever
strategy; you can only choose one that has little to lose.

**The DECODE case study — why this weight is 8, not 3.** In DECODE (2025-26), the two most obvious
*low-fabrication* strategies were both constrained within **12 days of Kickoff** (all **HISTORICAL**, read from
the local combined Team Updates PDF):

| When | Update | What changed | Who it hurt |
|---|---|---|---|
| Kickoff (2025-09-06) | **TU00** | Evergreen changes: Motivate Award retired → replaced by Reach + Sustain; max servos reduced to 10; expansion limits reinstated (R105) | Anyone who planned around the old award set or a 12-servo design |
| Kickoff + 5 days (2025-09-11) | **TU01** | **G419 retitled from "ROBOTS only score into their own GOAL" to "ROBOTS only LAUNCH into their own GOAL"**, and rewritten to prohibit intentionally **placing** or launching ARTIFACTS onto the team's own RAMP. G418 tightened so robots may not contact ARTIFACTS on **any** RAMP | Killed the cheap "gently place the ball rather than build a launcher" plan |
| Kickoff + 12 days (2025-09-18) | **TU02** | **G433** — human DRIVE TEAM members may only enter ARTIFACTS **without LAUNCHING or rolling**, only during TELEOP, only via the LOADING ZONE. **G434** — an ALLIANCE may not store more than 6 ARTIFACTS off the FIELD | Constrained the "robot feeds human players who score" plan — the other classic no-mechanism strategy |

Both of the strategies a low-fabrication team would naturally pick were narrowed almost immediately. Meanwhile
the strategies built on *core scoring as written* were untouched.

**Additional BIOBUZZ-specific exposure right now:** **R105 (CONFIRMED-BIOBUZZ)** states outright that sizing
constraints and further detail are **released at Kickoff**. Any strategy relying on a large extension is
carrying an unpriced risk today. HISTORICAL precedent: DECODE's R105 constrained horizontal expansion to a
fixed 18 in. × 18 in. footprint and vertical expansion to 18 in. (or 38 in. under conditions), and required
compliance **mechanically, not in software**, demonstrated at inspection. Assume something comparable and
verify on Kickoff day.

| Score | Anchor (observable) |
|---|---|
| **1** | Value depends on an unstated interaction, a loophole, an ambiguity, or an "it doesn't say we can't". Historically the first thing a Team Update closes |
| **2** | Depends on a specific edge of one rule, or on a rule with a known history of tightening (protected zones, human-player actions, descoring, expansion) |
| **3** | Depends on a normal reading of one G-rule that could plausibly be clarified against you |
| **4** | Depends only on core scoring as written; a nerf would cost efficiency, not the strategy |
| **5** | Depends on the game's central scoring loop, which cannot be nerfed without redesigning the game. Or: uses only Section 12 (R) rules, which are **already final** for BIOBUZZ |

**Mitigation the harness must attach to any score ≤ 3.** (a) Name the exact rule the strategy leans on;
(b) name the plausible tightening; (c) state the fallback and its cost in F6 terms; (d) schedule a re-score
after **TU01 (expected Thursday 2026-09-17)** and **TU02 (2026-09-24)**; (e) note that updates published after
an event's driver's meeting do not apply at that event (**CONFIRMED-BIOBUZZ §2**).

---

## 5. Pre-registered exemplars (calibrate the scale *before* Kickoff)

Score these **now**, before the game is known, so the scale is anchored before motivated reasoning arrives.
When the BIOBUZZ candidates are scored on Kickoff day, each score must be defensible *relative to these*.
All are **HISTORICAL** archetypes; none is a BIOBUZZ prediction.

| ID | Archetype (season) | F1 fab | F2 dup | F5 t-to-rel | F8 tune | F10 rel | F12 score | F15 award | Why it anchors |
|---|---|---|---|---|---|---|---|---|
| **E1** | COTS mecanum chassis, park only (any season) | 5 | 5 | 5 | 5 | 5 | **2** | 1 | The floor for payoff, the ceiling for buildability. Defines what a 5 on the build factors and a 2 on F12 look like |
| **E2** | ITD short-arm specimen scorer — slide + 1-motor arm + printed claw, HIGH CHAMBER (10 pts) | 4 | 4 | 4 | 4 | 4 | 4 | 3 | The "boring and correct" answer. Most BIOBUZZ candidates should be scored against this |
| **E3** | ITD tall two-stage vertical extension + bucket, HIGH BASKET (8 pts) | 2 | 2 | 2 | 3 | 3 | 4 | 4 | Higher fabrication and duplicability cost for *less* per-action value than E2 — the standing proof that difficulty ≠ value |
| **E4** | ITD endgame-only ascent specialist — winch + hooks, LEVEL 3 (30 pts) | 4 | 5 | 4 | 5 | 3 | 4 | 2 | One action, one mechanism, huge points. Anchors "high F12 with low F7/F8" |
| **E5** | DECODE full launcher — flywheel + hopper + turret + vision auto-aim | 2 | 1 | 1 | **1** | 2 | 5 | 5 | The **F8 = 1** anchor. Buildable-ish, tunable barely, duplicable not at all |
| **E6** | DECODE fixed-angle single-flywheel launcher from one fixed spot | 4 | 3 | 2 | 2 | 3 | 3 | 3 | The middle of the launcher family. Anchors why F1 and F8 must be scored separately |
| **E7** | DECODE intake + hopper, no launcher (feed the human players) | 5 | 5 | 4 | 4 | 4 | 2 | 2 | The **F13 = 1** anchor: one parked opponent zeroes it. Also the **F16 = 2** anchor (TU02 G433/G434) |
| **E8** | Custom swerve drivetrain, machined/outsourced plates | **1** | **1** | 1 | 2 | 3 | 4 | 4 | The **G3 gate** anchor. Excellent robot, wrong program |

---

## 6. Weighting scheme and justification

Weights sum to **100**. A weight is an assertion about *what kills this program's seasons*, and each one below
states that assertion explicitly.

| Factor | Weight | Justification for a ~15-student, two-robot, hand-tool program |
|---|---|---|
| **F12 Scoring Ceiling / PPS** | **12** | Largest single weight, deliberately. An achievability model with no payoff term ranks "park" first every time. F12 must outweigh any single build-cost factor so that a hard-but-valuable strategy can still win the ranking — but it must not outweigh the *cluster* (build feasibility totals 34), because this program's historical failure mode is over-scoping, not under-scoping |
| **F1 Fabrication Complexity** | **9** | The binding physical constraint. With no CNC, F1 is not a preference, it is a wall. Weighted equal to F2 because a design that fails F1 fails for **both** robots simultaneously |
| **F2 Duplicability** | **9** | The program-defining factor and the one generic advice omits. Failing here converts a two-team program into a one-team program, forfeiting a second independent shot at a 60-point Inspire (§4.1) and a second A215 award slot. Backed by rule text: **I303.F** makes identical mechanisms legal drop-in replacements, and **R304** makes duplicable work compound across seasons |
| **F10 Match Reliability & Failure Consequence** | **8** | Consistency beats peak (GM0). It is also an *award* precondition, not just a scoring one — Innovate §6.3.6, Design §6.3.8 and Control §6.3.7 all condition on the solution working most of the time. Weighted above F5 because *severity* of failure, not frequency, is what teams systematically under-price |
| **F15 Award-Generation Potential** | **8** | Awards are this program's highest-yield advancement currency: Inspire 1st = **60** advancement points vs. **40** for winning the event, and one non-Inspire 1st place award (12) is comparable to the top qualification seed (~16) — **§4.1 Table 4-1**. Not weighted higher because judged awards are subjective and partly team-attribute-driven (Connect/Reach/Sustain), which no design choice controls |
| **F16 Rule-Change Exposure** | **8** | Weighted equal to reliability because the DECODE evidence is stark: both classic low-fabrication strategies were narrowed by **TU01 and TU02 within 12 days of Kickoff**. A small program cannot absorb a week-2 pivot; GM0 puts a mid-season rebuild at 50–100+ hours, which this program does not have. Additionally **R105's** sizing constraints are still unpublished for BIOBUZZ |
| **F8 Tuning Burden** | **7** | Broken out from F7 and weighted higher than it, because tuning is paid in *field time with the real element*, per robot, and it drifts — and **R601** (one battery, no capacity headroom) means voltage-driven drift cannot be engineered away. This is the factor that turns "we built it in week 3" into "it still doesn't work in February" |
| **F3 BOM + Spares Cost** | **5** | Real but not decisive: the known floor (`2 × $350` registration, `~$1,500`/team of recommended materials) dominates, and marginal mechanism cost is usually a few hundred dollars. Weighted below F1/F2 because *capability* limits this program harder than *cash*, and because F2 already prices the second robot |
| **F7 Programming Burden** | **5** | Meaningful with 1–3 programmers supporting two robots, but capped by **R503** (8 motors / 8 servos) and largely mitigated when F2 is high, since identical robots share code. **I303.D** also makes code the cheapest thing to change at an event |
| **F13 Defense Resistance** | **5** | Directly evidenced (CD t/519884): a strategy funnelling through one location is zeroed by one opponent with no mechanism. Not higher because BIOBUZZ's G-rules and protected zones are **deferred to Kickoff**, so pre-Kickoff scores here are provisional (FLAG-1) |
| **F14 Alliance Value** | **5** | Advancement rewards being pickable (`21 − draft position`, plus 40/20/10/5 for playoff finish, §4.1). Also carries the A/B complementarity question — but it is downstream of F10 and F12, so it should not be double-counted at a higher weight |
| **F4 Time-to-First-Prototype** | **4** | Matters, but is partly buyable *now*: POLLEN, StarterBot Bases and Skill Builders are all available pre-Kickoff (**CONFIRMED-PRESEASON**), and **R304** makes pre-Kickoff fabrication legal. A program that uses August–September well reduces this factor's bite |
| **F5 Time-to-Reliable** | **4** | Split from F4 so a fast prototype cannot halo into a false reliability score. Weighted lower than F10 only because F10 already captures the *consequence*; F5 captures the schedule |
| **F9 Sensor & Vision Dependence** | **4** | A real risk, but deliberately not higher, because **Control §6.3.7 requires external feedback** — over-weighting sensor avoidance would rank the team out of an entire MCI award. The model wants *sensor-assisted, not sensor-dependent* |
| **F11 Driver Skill Ceiling** | **4** | Scarce practice time across two drive teams, but partially bought down by free **Skill Builders** and by partial automation (GM0). Lower than F8 because driver skill improves monotonically with practice whereas tuning drift does not |
| **F6 Iteration Cost** | **3** | Lowest weight, and that is a deliberate claim: for this program the *first* decision matters more than the ability to reverse it, because there are not enough mentor hours to execute a reversal anyway. Kept in the model because it is a cheap design property to buy (bolt-on interfaces, slotted structure) and it interacts with F16 as the mitigation term |

**Sanity checks built into the weighting.**
1. Build feasibility (34) > payoff (30). If this inverts, the model will recommend robots this program cannot build.
2. F12 (12) < the F1+F2 pair (18). No single payoff number can outvote "we can't make two of them."
3. F15 (8) ≈ F10 (8). Award chasing never outranks a working robot — and the award criteria themselves require one.
4. F16 (8) is large enough that a loophole strategy cannot win on payoff alone.

---

## 7. What a *different* team should change

The weights above are **calibrated to one program**. Any other team must re-weight, and the model should refuse
to be used unweighted. Deltas below are suggestions, expressed as changes from the baseline.

| Team archetype | Raise | Lower | Reasoning |
|---|---|---|---|
| **Single team, one robot** | F12 +4, F6 +2, F5 +1 | **F2 −7** (or drop it entirely), F14 −1 | Duplicability is nearly irrelevant with one robot; the freed weight belongs to payoff and to the ability to iterate, since one robot means all eggs in one design |
| **Powerhouse: 30+ students, CNC mill, deep mentor bench** | F12 +6, F13 +3, F8 +2 | F1 −6, F3 −3, F4 −2 | Fabrication ceases to be a wall. Their binding constraints become tuning time, defense from peer teams, and raw scoring rate |
| **Rookie team, season 1** | F4 +3, F7 +3, F11 +2, F10 +2 | F12 −5, F15 −3, F13 −2 | Their goal is a working robot and a completed season, not advancement. Getting *anything* on the field is the win |
| **Team optimizing purely for advancement/Inspire** | **F15 +6**, F10 +2 | F12 −5, F13 −3 | §4.1 makes Inspire (60) worth more than winning (40). A robot that works reliably and is well-documented beats a robot that scores more and is not |
| **Team optimizing purely for Winning Alliance** | F12 +5, F13 +3, F14 +3 | F15 −6, F3 −3, F6 −2 | Playoff finish is 40/20/10/5; awards become secondary |
| **League-play-only team (no Qualifying Tournament)** | F5 +3, F6 +3, F11 +2 | F16 −4, F4 −2, F14 −2 | League Meets spread the season out, giving real iteration windows between matches. **CONFIRMED-BIOBUZZ §6.1: no awards are presented at League Meets**, so award pressure shifts entirely to the League Tournament |
| **Team with a strong programmer, weak builders** | F1 +3, F2 +2 | F7 −3, F9 −2 | Push complexity into software (**I303.D**: code changes need no re-inspection) and out of the machine shop |
| **Team with a machine shop but 6 students** | F11 +3, F7 +3, F5 +2 | F1 −4, F6 −2, F3 −2 | Labour, not capability, is the wall. Anything requiring many parallel hands is out |
| **Two teams with *independent* mentor pools and shops** | F12 +3, F6 +2, F14 +2 | **F2 −5** | The mentor-bandwidth argument (CD t/406178) no longer binds; two different designs become the better pedagogical choice |

**Rule for re-weighting:** change weights **before** scoring any candidate, write down why, and keep the total
at 100. Re-weighting after seeing the scores is how a rubric becomes a rationalisation — and, incidentally,
the *record* of having pre-registered weights is exactly the "comparing choices" evidence Think §6.3.2 asks for.

---

## 8. Anti-flatness protocol: avoiding the "everything scores 3" rubric

The predictable failure of any 1–5 rubric is regression to 3: every option looks moderately good, the weighted
totals land within 4 points of each other, and the rubric ratifies whatever the loudest person already wanted.
Eight mechanisms, in order of importance:

| # | Mechanism | How it works |
|---|---|---|
| **1** | **Score column-wise, never row-wise** | Score **all** candidates on F1, then all on F2, and so on. Never score one strategy across all 16 factors before moving on. Row-wise scoring produces halo effects (a strategy you like gets 4s everywhere); column-wise scoring forces comparison, which forces spread |
| **2** | **Forced-spread check per factor** | After each column, check the spread. If every candidate got the same score on a factor, **the anchors were not concrete enough** — re-anchor with a sharper observable and re-score that column. If after re-anchoring the factor still does not discriminate for this game, set its weight to 0 and redistribute (recording why) |
| **3** | **3 must be earned in writing** | A 3 requires a one-sentence written justification citing the specific observable. If the scorer cannot write it, the score is not 3 — it is **U** |
| **4** | **"U" is a legal score and it costs you** | Unknown ⇒ the strategy goes on the **prototype list** and is ranked **twice**: optimistic (U→4) and pessimistic (U→2). If the two rankings disagree on the top choice, **you are not ready to decide** — prototype first. This converts ignorance into a scheduled experiment instead of a comfortable 3 |
| **5** | **Every anchor is a countable** | Anchors are dollars, hours, part counts, constant counts, success percentages, named processes. Banned words in anchors: "moderate", "reasonable", "somewhat", "fairly". If an anchor contains one, rewrite it |
| **6** | **Pre-registered exemplars (§5)** | The E1–E8 table was scored *before* the game was known. Every live score must be defensible as "harder than E2, easier than E5". Relative judgments are far more reliable than absolute ones |
| **7** | **Two independent scorers** | One student, one mentor, scored blind to each other. Any factor where they differ by ≥ 2 gets discussed and the *reasoning* recorded. That disagreement log is directly usable as Think §6.3.2 "comparing choices" evidence and Innovate §6.3.6 criterion 4 "how risks were reduced" |
| **8** | **Gates are not scores (§3)** | A fatal flaw must not be averageable. Gates run first and reject outright, so four 5s cannot outvote one 1 on fabrication |

### 8.1 Worked example — the flat rubric and the fix

**Setup (HISTORICAL, INTO THE DEEP 2024-25).** Three candidates:
**S1** short-arm specimen scorer (HIGH CHAMBER, 10 pts) · **S2** tall extension + bucket (HIGH BASKET, 8 pts)
· **S3** endgame ascent specialist (LEVEL 3, 30 pts).

**The flat version — scored row-wise, with vague anchors:**

| | F1 | F2 | F8 | F10 | F12 | F15 | Weighted /100 |
|---|---|---|---|---|---|---|---|
| S1 | 3 | 3 | 3 | 3 | 4 | 3 | **62** |
| S2 | 3 | 3 | 3 | 3 | 4 | 4 | **64** |
| S3 | 4 | 3 | 3 | 3 | 3 | 3 | **62** |

Spread: **2 points across three fundamentally different robots.** The rubric has said nothing. Worse, S2 leads
— on the strength of one soft "feels more impressive to judges" 4.

**The fix, applied.**

*Mechanism 1+5 — score column-wise against countable anchors.*
**F1 (fabrication):** S1 = COTS slide + one motor + printed claw, longest print 2 h, no structural prints → **4**.
S2 = a two-stage vertical extension: multi-stage slide alignment, structural printed mounts loaded in bending,
a rigid tall tower on a hand-tool budget → **2**. S3 = winch drum + hooks, one motor, bolt-on → **4**.
Spread achieved: 4 / 2 / 4.

*Mechanism 2 — forced-spread check on F2.* All three initially got 3. Re-anchor on the observable "parts
requiring per-robot fitting": S1 = 0 (catalogue + print files) → **4**. S2 = the two-stage slide needs per-robot
alignment shimming and its own tuning pass → **2**. S3 = 0, and the two robots' winches are interchangeable
spares under **I303.F** → **5**. Now the factor discriminates.

*Mechanism 3 — no free 3s on F8.* S1: arm hold-power + 2 preset positions, stable across batteries → 2 constants → **4**.
S2: extension height presets + tip-over-sensitive drive speed limits + a bucket release timing, all
voltage-sensitive on one battery (**R601**) → ~6 constants → **2**. S3: winch to hard stop, zero empirical
constants → **5**.

*Mechanism 6 — check against pre-registered exemplars.* S2 is the E3 archetype exactly; E3 was pre-scored
F1 = 2, F2 = 2. Consistent. S3 is E4 (F2 = 5, F8 = 5). Consistent. The scale held.

*Mechanism 3 again, on F15.* The original S2 = 4 was the soft judgment that produced the wrong ranking.
Written justification required: which criterion? Design §6.3.8 asks for **elegant, efficient — explicitly
"simple to build and operate" — and practical to maintain**. A tall two-stage tower is the *opposite* of that
text. S2's real strength is Innovate §6.3.6 (creative/unique) — but Innovate criterion 3 requires the design be
**stable and reliable most of the time**, which given F10 = 3 is not yet demonstrated. S2 → **3**.
S1: documented alternatives + arm-geometry math (Think 1C and 1D) *and* Design's "simple to build and operate" →
**4**. S3: one mechanism, thin evidence base → **2**.

**Re-scored:**

| | F1 (w9) | F2 (w9) | F8 (w7) | F10 (w8) | F12 (w12) | F15 (w8) | Weighted /100 |
|---|---|---|---|---|---|---|---|
| **S1** | 4 | 4 | 4 | 4 | 4 | 4 | **80** |
| **S2** | 2 | 2 | 2 | 3 | 4 | 3 | **54** |
| **S3** | 4 | 5 | 5 | 3 | 4 | 2 | **74** |

*(Weighted values shown for the six factors displayed, normalised over their 53 points of weight; the full run
uses all 16.)*

Spread is now **26 points**, the ranking is decisive, and — critically — the ranking **changed**: S2 went from
first to last. The flat rubric had ratified the most impressive-looking robot. The anchored rubric identified
the one this program can build twice.

**The tell that you have the flat version:** if the gap between your best and worst candidate is under ~10
points on a 100-point scale, you have not scored anything. Re-run mechanisms 1, 2 and 5.

---

## 9. Scoring math and output format

**Weighted score** (0–100):

```
score = ( Σ over i of  weight_i × rating_i ) / 5
```
with `Σ weight_i = 100` and `rating_i ∈ {1,2,3,4,5}`. Dividing by 5 puts an all-5s strategy at 100.

**Always report five numbers, not one:**

| Output | Meaning | Why |
|---|---|---|
| `score` | Weighted 0–100 | The headline rank |
| `min_factor` | Lowest single rating + which factor | A strategy with an 80 and a 1 somewhere is not an 80 |
| `gates` | Pass / trip list from §3 | Fatal flaws are not averageable |
| `flags` | FLAG-1 items and unknowns (`U`) | What must be re-scored after Kickoff / TU01 / TU02 |
| `spread` | Range of `score` across all candidates | If < 10, the rubric failed — see §8 |

**Decision rule.** Rank by `score`, but a strategy is **not recommendable** if it trips any gate, or if
`min_factor = 1` on F1, F2, F3, or F10, or if the optimistic and pessimistic `U`-substituted rankings disagree
on the top pick (§8 mechanism 4).

**Required per-strategy record** (this is also the raw material for the portfolio under Think §6.3.2):
strategy name · one-line description · gate results · the 16 ratings, each with its one-line observable
justification · weighted score · min factor · flags · the 2 recommended awards (from §10) · the two-robot BOM.

---

## 10. Handoff: factor profile → award targets

The downstream stage pairs each ranked strategy with **~2 awards**. This table is the mapping rule; the
detailed criteria live in §4/F15 and in the BIOBUZZ Section 6 text. All award criteria are **CONFIRMED-BIOBUZZ**.

| Factor profile | Primary award target | Secondary | Why |
|---|---|---|---|
| High **F1** + high **F10** + coherent whole robot | **Design** §6.3.8 | **Think** §6.3.2 | Design's own words are "elegant, efficient (simple to build and operate), and/or practical to maintain" and it judges the **entire** ROBOT — the exact profile a COTS-heavy, hand-tool, high-reliability robot has. It rewards the constraint instead of apologising for it |
| Distinctive geometry + documented risk reduction + **F10 ≥ 4** | **Innovate** §6.3.6 (sponsored by RTX) | **Think** | Innovate needs creative/unique **and** stable/reliable **most of the time**, and encourages explaining how design risks were reduced. Never pair Innovate with a strategy scoring F10 ≤ 2 — criterion 3 will fail |
| **F9 ≤ 3** (genuine external feedback) + measurable consistency | **Control** §6.3.7 | **Think** | Control *requires* external feedback and a portfolio summary of components, the challenge each solves, and its function. This is the one award where sensor dependence is an asset — and the reason F9 is weighted only 4 |
| Multiple prototypes compared + math used in a decision | **Think** §6.3.2 | best available MCI | Think criterion 1C ("comparing choices") and 1D ("math choices") are generated by the *process*, not the robot. A high-**F6** design that was actually iterated produces this evidence naturally |
| High **F2** + high **F10** + a de-scoped complementary B robot | **Design** (A team) | **Think** (B team) | Two teams, two A215 award slots. Deliberately split targets so the sibling teams are not competing for the same award at the same event |
| **F15 = 5** across MCI + Think, plus a real TA story | **Inspire** §6.3.1 | its strongest MCI | Inspire requires being a strong contender in **an MCI award AND a TA award AND Think**. Only pursue when the TA side (Connect/Reach/Sustain) is genuinely in hand — it is not produced by any design choice |

**Constraints the pairing stage must respect** (all **CONFIRMED-BIOBUZZ**):
**A215** one judged award (or runner-up) per team per event · **A211 Table 6-1** the award set shrinks at small
events, and only listed awards are points-eligible · **A201** 15 content pages + 1 cover page, content from
2026-01-01 only, judges will not click links, AI use permitted **with a footnote/endnote credit** ·
**A203** an Initial Interview is mandatory for any judged award · **A213/A214** Inspire is region-limited and
1st place Inspire is once per season from Qualifying/League Tournaments · **§6.1** no awards at League Meets.

---

## 11. Kickoff-day instantiation checklist

What to do on **2026-09-12** to turn this model from scaffolding into a ranking. Estimated 3–4 hours.

| # | Step | Output |
|---|---|---|
| 1 | Read Sections 8–11, 13 and 15 (the deferred ones — note §14 League Play is NOT a placeholder). Extract the **scoring table** and every **G-rule** that constrains control, zones, or scoring | Points-per-action list; zone/control constraint list |
| 2 | Read **R105's** now-published sizing constraints. Re-check every candidate against them | FLAG-1 items resolved or re-scored |
| 3 | Download the full **StarterBot** designs (released at Kickoff) and read them against **R301.B** | Baseline candidate E1′ — the legal-COTS floor for both robots |
| 4 | Time a human doing each scoring action on the real field. Convert to seconds/cycle | The denominator for **F12** |
| 5 | Instantiate F12 anchors: compute "typical winning score" from the scoring table × plausible cycle counts | F12 anchor bands, numeric |
| 6 | Instantiate F13 anchors from the actual protected-zone and defense G-rules | F13 anchor bands |
| 7 | Score column-wise per §8. Two scorers. Log disagreements | The 16 × N rating matrix |
| 8 | Run gates (§3), compute scores (§9), check spread ≥ 10 | Ranked list |
| 9 | Pair awards (§10); build the two-robot BOM for the top 2–3 | Deliverable |
| 10 | **Re-score after TU01 (expected Thu 2026-09-17) and TU02 (2026-09-24)** — the DECODE precedent says the nerfs land here | Revised ranking |
| 11 | Log Q&A questions from 2026-09-28 12:00 p.m. ET; remember answers do not supersede the manual | Open-questions list |

---

## 12. Machine-readable factor set

For the ranking harness. Weights sum to 100; `polarity: inverted` means a high real-world cost maps to a
**low** rating, so 5 is always favorable.

```yaml
model: BIOBUZZ-ACHIEVABILITY
version: 1.0
authored: 2026-08-21
calibrated_for:
  students: 15
  robots: 2
  fabrication: [cots, 3d_printing, hand_tools]
  excluded_fabrication: [cnc_mill, lathe, waterjet, welding]
  budget: modest
  mentor_hours: limited
scale: {min: 1, max: 5, unknown: U, direction: "5 is always favorable"}
score_formula: "sum(weight_i * rating_i) / 5"
gates: [G1_legality, G2_actuator_budget_R503, G3_fabrication_floor, G4_two_robot_feasibility,
        G5_cash_ceiling, G6_pneumatics_R801]
flags: [FLAG1_deferred_rule_R105_and_sections_8_11]
reject_if: ["any gate tripped", "min_factor==1 on F1|F2|F3|F10",
            "optimistic and pessimistic U-substitution disagree on rank 1"]
spread_warning_threshold: 10
factors:
  - {id: F1,  name: fabrication_complexity,      cluster: build,       polarity: inverted, weight: 9}
  - {id: F2,  name: duplicability_A_B,           cluster: build,       polarity: direct,   weight: 9}
  - {id: F3,  name: bom_and_spares_cost,         cluster: build,       polarity: inverted, weight: 5}
  - {id: F4,  name: time_to_first_prototype,     cluster: build,       polarity: inverted, weight: 4}
  - {id: F5,  name: time_to_reliable,            cluster: build,       polarity: inverted, weight: 4}
  - {id: F6,  name: iteration_cost,              cluster: build,       polarity: inverted, weight: 3}
  - {id: F7,  name: programming_burden,          cluster: reliability, polarity: inverted, weight: 5}
  - {id: F8,  name: tuning_burden,               cluster: reliability, polarity: inverted, weight: 7}
  - {id: F9,  name: sensor_vision_dependence,    cluster: reliability, polarity: inverted, weight: 4}
  - {id: F10, name: match_reliability_and_consequence, cluster: reliability, polarity: direct, weight: 8}
  - {id: F11, name: driver_skill_and_practice,   cluster: reliability, polarity: inverted, weight: 4}
  - {id: F12, name: scoring_ceiling_pps,         cluster: payoff,      polarity: direct,   weight: 12}
  - {id: F13, name: defense_resistance,          cluster: payoff,      polarity: direct,   weight: 5}
  - {id: F14, name: alliance_value,              cluster: payoff,      polarity: direct,   weight: 5}
  - {id: F15, name: award_generation_potential,  cluster: payoff,      polarity: direct,   weight: 8}
  - {id: F16, name: rule_change_exposure,        cluster: risk,        polarity: inverted, weight: 8}
cluster_weights: {build: 34, reliability: 28, payoff: 30, risk: 8}
award_catalog_biobuzz:   # CONFIRMED-BIOBUZZ, Section 6. Motivate does NOT exist.
  inspire: {portfolio_required: true,  section: "6.3.1"}
  think:   {portfolio_required: true,  section: "6.3.2", category: think}
  connect: {portfolio_required: false, section: "6.3.3", category: TA}
  reach:   {portfolio_required: false, section: "6.3.4", category: TA}
  sustain: {portfolio_required: false, section: "6.3.5", category: TA}
  innovate:{portfolio_required: false, section: "6.3.6", category: MCI, sponsor: RTX}
  control: {portfolio_required: true,  section: "6.3.7", category: MCI}
  design:  {portfolio_required: false, section: "6.3.8", category: MCI}
  judges_choice: {section: "6.3.9", optional: true}
advancement_points:      # CONFIRMED-BIOBUZZ, Section 4.1 Table 4-1
  inspire: {first: 60, second: 30, third: 15}
  other_judged_award: {first: 12, second: 6, third: 3}
  winning_alliance: {first: 40, second: 20, third: 10, fourth: 5}
  qualification_performance: {min: 2, max: 16}
  alliance_lead: "21 - alliance_lead_number"
  draft_acceptance: "21 - draft_order_acceptance_number"
```

---

## 13. Known gaps and unverified items

| Item | Status |
|---|---|
| BIOBUZZ scoring values, field layout, G-rules, AUTO/TELEOP structure | **Deferred to Kickoff** (V0 Sections 8–11, 13 and 15 are placeholders). F12 and F13 anchors are *shapes*, not numbers, until 2026-09-12 |
| **R105** sizing/expansion constraints for BIOBUZZ | **Deferred to Kickoff.** DECODE's version is HISTORICAL context only |
| r/FTC community evidence | **Not gathered** — reddit.com is inaccessible from this environment. All community evidence is Chief Delphi |
| Marginal mechanism BOM prices in F3 anchors | **JUDGMENT bands**, not vendor quotes. Only the registration, FIRST materials estimate, goBILDA Starter Kit and Strafer Chassis figures in §1.2 are verified prices |
| Practice-hour figures in F11 anchors | **JUDGMENT**, calibrated against community reports; no measured FTC dataset was located |
| Exact **R502** servo stall-current limit | Text extraction was lossy on the numeric cell. Rule cited by ID only; **read the number off the PDF before using it in a BOM** |
| DECODE tuning anecdotes (matched flywheel velocities, static electricity) | **HISTORICAL / JUDGMENT** — reported in season threads; not independently measured here |
| Whether BIOBUZZ retains DECODE-style RANKING POINTS | **Unknown.** Affects F14 materially; resolve at Kickoff |
