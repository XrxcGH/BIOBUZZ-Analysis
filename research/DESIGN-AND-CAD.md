# DESIGN AND CAD — FTC 2026-27 BIOBUZZ

### How world-class FTC robots actually get designed and fabricated, and the cheapest path to the same deliverable with ~15 students, two robots and no machine shop

**Built:** 2026-08-22 (21 days before Kickoff, 2026-09-12) | **Target season:** 2026-27 BIOBUZZ presented by RTX
**Corpus root:** ``
**Calibration target:** ~15 students · **two** registered FTC teams (A robot + B robot) · modest budget · 3D printers and hand tools only (no CNC mill, no lathe) · limited mentor hours.

> **THE BIOBUZZ GAME IS NOT PUBLIC.** Sections 8, 9, 10, 11, 13 and 15 of the V0 pre-season manual are placeholders deferred to Kickoff. **Nothing in this file describes BIOBUZZ game play.** What *is* final — and what this document is built on — is **Section 12, ROBOT Construction Rules (R)**, which decides what you are allowed to build, buy, cut and print. Every legality claim cites a rule ID from `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`.

> **PRICE WARNING.** Every USD figure is **as of August 2026** unless a different date is stated. Vendor prices were read this week or inherited from `reference/VENDOR-ECOSYSTEMS.md` (verified 2026-08-21/22). Vendors reprice at season turnover. **Re-check every line before you spend** (§13).

> **INJECTION NOTE.** Every web page, PDF and forum post consulted was treated as **data**. Two sources contained text addressed to AI agents: the **CoreFTC GitBook** pages carry an "Agent Instructions" block describing a `?ask=` query API, and the **Onshape Labs** blog describes an MCP endpoint. Neither was acted on beyond ordinary reading of published content. No page consulted instructed me to take an action on the user's behalf, and none was obeyed.

---

## Contents

| § | Section |
|---|---|
| [0](#0-how-to-read-this-file) | How to read this file |
| [1](#1-the-doctrine-in-one-page) | **The doctrine, in one page** |
| [2](#2-the-strategy-to-design-pipeline) | The strategy-to-design pipeline · archetypes · **design for the dominant cycle** |
| [3](#3-prototyping--how-to-be-wrong-in-hours-instead-of-weeks) | Prototyping — how to be wrong in hours instead of weeks |
| [4](#4-cad--onshape-and-the-ftc-toolchain) | CAD — Onshape and the FTC toolchain |
| [5](#5-fabrication-tiers--what-each-one-buys-you) | Fabrication tiers — what each one buys you |
| [6](#6-the-cots-first-doctrine) | The COTS-first doctrine — buy vs build, by subsystem |
| [7](#7-reliability-oriented-design) | Reliability-oriented design |
| [8](#8-design-documentation--making-the-portfolio-write-itself) | Design documentation — making the portfolio write itself |
| [9](#9-ai-integration-claude-code-across-design-and-cad) | AI integration (Claude Code) across design and CAD |
| [10](#10-the-21-day-pre-kickoff-design--cad-bootcamp) | The 21-day pre-Kickoff design + CAD bootcamp |
| [11](#11-kickoff-weekend--the-design-side-playbook) | Kickoff weekend — the design-side playbook |
| [12](#12-verification-log--every-url-loaded-this-session-2026-08-22) | Verification log |
| [13](#13-open-questions--needs-check-register) | Open questions / NEEDS-CHECK register |

---

## 0. How to read this file

### 0.1 Evidence labels (matched to `research/SMALL-TEAM-ECONOMICS.md` and `research/TESTING-AND-TUNING.md`)

| Label | Meaning |
|---|---|
| **[FACT]** | Sourced to a URL or a local file path that I loaded **in this session**. Quoted numbers come from that source. |
| **[DERIVED]** | Arithmetic or logic on stated values. Inputs are cited; the conclusion is mine. |
| **[JUDGMENT]** | Engineering/process opinion calibrated to *this* program. Not a fact. Argue with it. |
| **[UNVERIFIED]** | Could not be confirmed this session. A lead to check, never a number to budget on. |
| **[C]** | CONFIRMED-BIOBUZZ — text present in an already-final section of the BIOBUZZ V0 manual (Section 12 unless noted). |

### 0.2 Where this file sits

This is the **process and shop** document. It deliberately does **not** re-catalogue parts, mechanisms, rules or match-day failures — those already exist in this corpus and are better.

| File | What it gives you that this one does not |
|---|---|
| `reference/STRATEGY-RANKING-PROTOCOL.md` | The upstream phase: scoring table → ranked strategy list. **§2 here starts where that ends.** |
| `reference/ACHIEVABILITY-FACTORS.md` | The 16-factor weighted rubric (F1 Fabrication Complexity, F2 Duplicability, F4 Time-to-First-Prototype…) that scores each design option |
| `reference/ROBOT-ARCHETYPE-LIBRARY.md` | The archetype catalogue you pick *from* in §2.4 |
| `reference/mechanisms/*.md` | Five deep mechanism dives (drivetrain/odometry, intake, extension/lifts, launchers, electronics) with variants, physics and SKUs |
| `reference/VENDOR-ECOSYSTEMS.md` | The buyer's map: who sells what, verified SKUs and prices, interoperability |
| `reference/BOM-PROTOCOL.md` | The downstream phase: approved design → orderable parts list. **§2 here feeds it.** |
| `reference/CONSTRUCTION-RULES-R.md` | Full R-rule detail — the legality source of truth |
| `research/TESTING-AND-TUNING.md` | §5 reliability engineering, §6 the **match-day failure-mode catalogue**. §7 here is *design-time prevention only*; that file owns the field failures. |
| `research/SEASON-CADENCE.md` | The calendar these gates hang on |
| `research/SMALL-TEAM-ECONOMICS.md` | Whole-program dollars, hours, grants, the ranked cut list |
| `research/AI-IN-FTC-POLICY.md` | **Read before §9.** AI-generated CAD is logged there as GREY AREA 1. |

### 0.3 What this document claims

**[JUDGMENT]** Elite FTC teams are not better at CAD than you will be. They are better at **four** things, in this order:

1. **Deciding fast and committing** — a scoring table becomes a ranked capability list in hours, not weeks.
2. **Killing bad ideas in hours** — with cardboard, scrap and a stopwatch, before any CAD or money is spent.
3. **Buying almost everything** — custom work is concentrated in the 10–20% of the robot where custom actually wins.
4. **Writing it down while it happens** — so the portfolio is a *byproduct*, not a January project.

Every one of those four is free. None requires a mill. That is the thesis of this file.

---

## 1. The doctrine, in one page

**[JUDGMENT]** Ten rules. If you adopt nothing else, adopt these.

| # | Rule | Why |
|---|---|---|
| 1 | **Requirements before mechanisms.** Write a "Will List" (§2.3) before anyone sketches. | Naming a mechanism poisons the option space. FRC 118 does this publicly every season. |
| 2 | **One dominant cycle.** Identify the single repeated action that produces most of your points and optimise the whole robot for it. | §2.5. GM0: *"Consistency is king."* |
| 3 | **Prototype in cardboard and scrap within 48 h of Kickoff.** No CAD until a concept has passed a physical test. | §3. CAD is expensive to change *socially* — people defend what they modelled. |
| 4 | **Kill criteria written before the test.** Every prototype gets a number it must hit and a date it dies on. | §3.4. Otherwise nothing is ever killed and you have four half-mechanisms in December. |
| 5 | **Onshape: one org, layout-sketch-driven, multi-document.** | §4. Free, Chromebook-capable, real branching, and the FTC part library lives there. |
| 6 | **Buy the drivetrain, slides, motors, gearboxes and odometry.** Custom-build only what touches the SCORING ELEMENT. | §6. Duplicability (F2) is the small-team superpower and COTS is how you get it. |
| 7 | **3D printing is your machine shop.** Print **PLA+**, not PLA; orient for load; use heat-set inserts, not set screws. | §5.4. The FTC Everybot's whole structure is printed and the BOM is **$976**. |
| 8 | **Outsource laser-cut plate before you buy a CNC router.** | §5.6–5.7. A Shapeoko is $1,800–$5,700 **plus a room plus a person**; Fabworks has no order minimum. |
| 9 | **Two identical robots, or one robot and one deliberate simplification.** Never two accidental variants. | §4.8. Two variants = double spares, double tuning, half the driving. |
| 10 | **Capture the decision at the moment you make it**, in 90 seconds, with a photo. | §8. The portfolio is not written in January; it is *assembled* in January. |

---

## 2. The strategy-to-design pipeline

### 2.1 The pipeline, end to end

**[JUDGMENT]** Nine stages. Timeboxes assume the Saturday Kickoff (2026-09-12) and a first event in November–December. Cross-check `research/SEASON-CADENCE.md` §4–5 for the calendar.

| # | Stage | Input | Output artifact | Timebox | Gate |
|---|---|---|---|---|---|
| **S0** | Rules ingest | Kickoff manual | Rule deltas; scoring table transcribed | Kickoff day, 2 h | `tools/ingest-manual.sh` runs clean |
| **S1** | Scoring analysis | Scoring table | Points-per-second table per action | Kickoff day, 2 h | `STRATEGY-RANKING-PROTOCOL.md` §6.3 |
| **S2** | Ranked strategy list | S1 + archetype library | 3–5 candidate strategies, scored | Kickoff weekend | Achievability rubric run twice (A + B robot) |
| **S3** | **Ranked capability list** | S2 | Ordered CAPABILITIES with MUST/SHOULD/COULD/WON'T | Kickoff Sunday, 90 min | **§2.2 — every line has a point value and a cycle cost** |
| **S4** | **Will List** (requirements) | S3 | Solution-independent requirement statements | Kickoff Sunday, 45 min | **§2.3 — no mechanism nouns allowed** |
| **S5** | Concept generation | S4 | ≥3 genuinely different concepts per MUST capability | Week 1, 2 sessions | Divergence check (§3.1) |
| **S6** | **Physical prototyping** | S5 | Prototype rigs + measured results | Weeks 1–3 | **§3.4 — kill criteria met, or concept killed** |
| **S7** | CAD | S6 survivors | Layout sketch → subsystem docs → robot assembly | Weeks 2–5 | §4.14 minimum CAD standard |
| **S8** | BOM + fabricate + assemble | S7 | Ordered parts, printed parts, built robot | Weeks 3–7 | `reference/BOM-PROTOCOL.md` B1–B7 |

⚠️ **[JUDGMENT] The most common small-team failure is skipping S3–S6 and going straight from S2 to S7.** A team that CADs in week 1 has committed to a mechanism nobody has touched. When it fails in week 4 it is too late to change, so they ship the bad mechanism and lose to a simpler robot that was tested in week 1.

### 2.2 S3 — From scoring analysis to a ranked capability list

**[JUDGMENT]** A **capability** is something the robot can *do*, phrased with a number — not something it *has*.

| Bad (a mechanism) | Good (a capability) |
|---|---|
| "A linear slide" | "Deliver a SCORING ELEMENT to a target 30 in above the floor in ≤2.0 s" |
| "A shooter" | "Score from anywhere in the launch zone at ≥85% success, ≤1.2 s per element" |
| "An intake" | "Acquire a floor element with ≤2 in of lateral driver alignment error, in ≤0.8 s" |

The S3 table has exactly these columns and no others:

| Column | Contents | Source of the number |
|---|---|---|
| Capability | The sentence above | You |
| Points enabled | Direct points per match | Kickoff scoring table |
| Cycle cost (s) | Seconds of match time consumed each repetition | §2.5 decomposition |
| Repetitions/match | Realistic, not theoretical | Match window ÷ cycle time × duty factor |
| **Expected points** | `points × reps × p(success)` | **[DERIVED]** |
| Achievability | 1–5 composite | `reference/ACHIEVABILITY-FACTORS.md` |
| Class | MUST / SHOULD / COULD / **WON'T** | Team vote, recorded |

**[JUDGMENT] Write the WON'T list explicitly and put it on the wall.** A written WON'T is the cheapest scope-control device that exists: it converts every "what if we also…" from a debate into a pointer.

### 2.3 S4 — The "Will List": requirements before mechanisms

**[FACT]** The Robonauts (FRC 118), who publish the FRC and FTC **Everybot** each season for under-resourced teams, define their build with an explicit *"Everybot Will list"* — described as *"the way the 118 & Everybot Crew define the build and design requirements. The listed requirements are independent of how the robot is going to accomplish the task."* Their published 2025-26 FTC list included: support omni-directional drivetrain · use custom 3D printed parts · play defense · intake from the floor (human-player friendly) · hold up to 3 elements · score into the goal · open the gate · return to base with room for a partner robot to also return. ([Chief Delphi thread 505709, post #3, 2025-09-09](https://www.chiefdelphi.com/t/the-2025-2026-robonauts-ftc-everybot-low-resource-build/505709))

**[JUDGMENT]** Copy this format verbatim. It is the highest-leverage 45 minutes of your season:

1. **Solution-independent**, so it survives a prototype failure. If "hold up to 3 elements" is the requirement, a hopper failing invalidates the hopper, not the requirement.
2. **Testable.** Every line becomes a pass/fail on the practice field.
3. **Portfolio gold.** A dated requirements list plus the trace from each requirement to the mechanism that satisfied it *is* the Design section of the Engineering Portfolio (§8).

**Template:**

```
The 2026-27 <TEAM> A-ROBOT WILL:
  <verb> <object> <constraint containing a number>
  ...
The A-ROBOT WILL NOT:
  <explicit exclusions carried from the WON'T list>

Constraints that bind every line (all [C], BIOBUZZ V0 Section 12):
  - 18 in cube in STARTING CONFIGURATION, fully stationary, self-contained   R102
  - Removable from the FIELD without power                                    R203
  - No exposed sharp edges/protrusions; no loose ballast; no mess             R201
  - No hazardous materials; nothing that interferes with other ROBOTS         R202
  - COTS MECHANISMS <= single degree of freedom                               R303
  - >= 2 ROBOT SIGNS, on opposite or adjacent surfaces                        R401
  - Actuator budget (motors/servos)  see reference/mechanisms/ELECTRONICS-AND-SENSING.md
```

### 2.4 S3/S5 — Picking a robot ARCHETYPE

**[JUDGMENT]** An archetype is a *whole-robot* shape, not a mechanism. Picking one early is what lets a small team parallelise: drivetrain, electronics and superstructure crews can all start on Kickoff Sunday because the archetype fixes the interfaces between them.

The catalogue is `reference/ROBOT-ARCHETYPE-LIBRARY.md`. The selection procedure:

| Step | Action | Anti-pattern prevented |
|---|---|---|
| A1 | Map each surviving S2 strategy onto **one or two** library archetypes | Inventing a novel architecture under time pressure |
| A2 | Inherit that archetype's cost / difficulty / reliability / duplicability profile | Optimism about a mechanism nobody has built |
| A3 | Check against the **actuator budget** *before* liking it | Discovering in week 5 that it needs 9 motors |
| A4 | Check against **two-robot duplicability (F2)** | An A robot the B team cannot copy |
| A5 | Pick the archetype whose *worst case* you can still field | Picking on best case, fielding the worst |

**[JUDGMENT] The archetype decision rule for a program this size:** *choose the archetype with the highest **expected** points, where expectation is taken over the probability you actually finish it.* A 120-point archetype finished 60% of the time is worth 72; an 80-point archetype finished 95% of the time is worth 76. Small teams systematically over-weight the ceiling and under-weight the finishing probability.

### 2.5 "Design for the dominant cycle" — what it actually means

**[JUDGMENT]** The **dominant cycle** is the single repeated action that generates most of your match points. In practice one cycle produces roughly 60–85% of a good FTC robot's score, and autonomous, endgame and defense are garnish on it.

"Design for the dominant cycle" means: **every design decision is evaluated by its effect on that cycle's time and success rate, and by nothing else.**

**Decompose it; never estimate a cycle whole.** (Same discipline as `STRATEGY-RANKING-PROTOCOL.md` §6.2.)

| Phase | Typical share **[JUDGMENT]** | What reduces it | What a small team can actually do |
|---|---|---|---|
| **Acquire** | 15–30% | Wider mouth, compliance, higher surface speed, "touch it, own it" geometry | Cheap: widen the lead-in. Free: raise intake surface speed |
| **Transit out** | 20–35% | Drivetrain speed, driver skill, shorter paths | **Free: driver practice is the cheapest cycle-time reduction that exists** |
| **Align** | 10–40% ⚠️ | Wider alignment tolerance, driver aids, sensors, auto-align | ⚠️ **The hidden killer.** Design the tolerance up *before* writing vision code |
| **Score / release** | 10–25% | Shorter mechanism travel, faster actuator, less settle time | Shorten travel; overlap with transit |
| **Transit back** | 15–30% | Same as transit out, **or eliminate it by overlapping with the next acquire** | Make acquisition begin during the return |

**[JUDGMENT] Two rules fall out of the decomposition:**

- **Overlap beats speed.** Making a mechanism 20% faster is hard. *Starting it during transit* is free — a state-machine change, not a hardware change. Elite cycle times are dominated by overlap, not component speed.
- **Alignment tolerance beats alignment accuracy.** Every inch you widen the acceptance window removes driver seconds *and* removes the need for a vision pipeline. Highest return-on-effort change available to a team with one programmer.

**The arithmetic, worked, game-agnostic [DERIVED].** Assume a 4-point element and a 90-second teleop window.

| Scenario | Cycle time | Cycles | p(success) | Expected teleop points |
|---|---|---|---|---|
| Baseline | 8.0 s | 11 | 0.80 | **35.2** |
| Cut 2 s from the cycle | 6.0 s | 15 | 0.80 | **48.0** (+12.8) |
| Keep 8 s, raise reliability to 0.95 | 8.0 s | 11 | 0.95 | **41.8** (+6.6) |
| Both | 6.0 s | 15 | 0.95 | **57.0** (+21.8) |
| Baseline **+ a 15-pt one-off costing 20 s** | 8.0 s | 8 (70 s ÷ 8 s) | 0.80 | 25.6 + 15 = **40.6** (+5.4) |

⚠️ **[JUDGMENT] Read the last row carefully.** A 15-point secondary capability that eats 20 seconds is worth **+5.4 points** — less than raising the primary cycle's reliability from 80% to 95%, and far less than cutting 2 s off the cycle. That is why elite teams look "boringly focused": they ran this arithmetic and concluded the second mechanism is worth less than tuning the first. **Run this table with the real BIOBUZZ numbers on Kickoff Sunday, before anyone falls in love with a second mechanism.**

### 2.6 The design-review gates

**[JUDGMENT]** Four gates, each a **30-minute standing meeting with a written decision**. A gate that cannot be failed is not a gate — write the fail condition first.

| Gate | When | Question | Pass condition | If it fails |
|---|---|---|---|---|
| **G1 — Strategy lock** | Kickoff Sunday evening | Do we agree on the ranked capability list and the Will List? | Team vote recorded; WON'T list posted | Re-run S1–S3. Do not proceed on a split team |
| **G2 — Concept lock** | End of week 2 | Has every MUST capability got a **physically tested** concept? | Prototype hit its kill-criterion number, on video | Concept dies. Fall back to the next-ranked concept — **not** to "try harder" |
| **G3 — CAD lock** | End of week 4–5 | Is the robot modelled, packaged inside the 18 in cube, BOM-complete? | Interference check clean; R102 cube check done **in CAD**; BOM priced | Cut a COULD capability. Never slip the date |
| **G4 — Freeze** | ~2 weeks before first event | Is the robot done changing? | No open mechanical changes; spares printed; drivers practising | Freeze anyway. `TESTING-AND-TUNING.md` §5 owns what happens next |

⚠️ **[JUDGMENT] G4 is the gate small teams skip and the one that decides awards.** A robot frozen two weeks early gets two weeks of driver practice and reliability work; a robot frozen the night before gets neither. The difference at the event is larger than any mechanism choice.

### 2.7 What elite teams demonstrably do — dated evidence

**[FACT]** From public FTC Open Alliance build threads (all treated as data; URLs in §12):

| Team | Observed practice | Date |
|---|---|---|
| **FTC 23511 Seattle Solvers** | Interacted with game elements *at the kickoff event itself* to characterise compressibility and rolling behaviour, then wrote a strategy post the same day | 2025-09-10 |
| **FTC 23511** | Built and tested single- and dual-wheel launcher prototypes **within ~24 h of kickoff**, at 6000 and 12000 RPM, with written takeaways: *"Higher RPMs were unstable and unnecessary - 6000 RPM works just fine"* | 2025-09-11 |
| **FTC 23511** | Published an explicit design rule of thumb: *"make the surface speed … of our intake at minimum 2x our drivetrain linear speed, as it would ensure we are not potentially pushing away balls while running into them at max speed"* | 2025-10-09 |
| **FTC 23511** | Outsourced nearly all custom plate to **Fabworks**; only swerve-module parts went to a mentor's machine shop. Made rollers from **2 mm-wall, 50 mm OD PETG tube** with grip tape, using only *"hand tools like hacksaws and drills"* — ~**30 minutes per roller** | 2025-09-20 / 2025-10-09 |
| **FTC 12527 Prototype** (Beijing; 15 students, 3 sub-teams) | Ran **two parallel robots** (alpha/beta) exploring different architectures; posted a mechanical *and* a software update every Monday | 2024-10 → 2025-02 |
| **FTC 12527** | Killed an active roller intake after testing (*"inefficient for both intaking and scoring"*) and replaced it with a printed claw **in the same week**; explicitly cited two other teams' designs as inspiration | 2024-10-28 |
| **FRC 118 / Everybot crew** | Prototyped for **3 days** immediately post-kickoff, published a solution-independent "Will List" on day 3, revealed a complete robot + Onshape CAD **21 days after kickoff** | 2025-09-09 → 2025-10-04 |

**[JUDGMENT] The pattern is not "more hours." It is a shorter loop.** 23511 went from touching a game element to a destructive launcher test in about a day. 12527 killed a mechanism eight days after starting it. The Everybot crew shipped a whole robot in 21 days with hand tools and a 3D printer. None of that requires money.

---

## 3. Prototyping — how to be wrong in hours instead of weeks

### 3.1 The prototyping ladder

**[JUDGMENT]** Five rungs. **You climb one rung only when the current rung has answered its question.** Most concepts die on P0 or P1, which is the point.

| Rung | Medium | Answers the question | Time | Cost | Typical mistake |
|---|---|---|---|---|---|
| **P0** | Cardboard, foamboard, hot glue, tape, zip ties | "Does the *geometry* work? Does the element fit, funnel, and not jam?" | **20–60 min** | ~$0 | Skipping it because it "isn't real engineering" |
| **P1** | Scrap extrusion / u-channel + spare motor + printed adapter, clamped to a table | "Does the *physics* work? Speed, torque, grip, compression, trajectory?" | **2–6 h** | $0–$40 (from stock) | Building it neatly. Do not build it neatly |
| **P2** | Printed test fixture with the real interface (bore, hole pattern, bearing) | "Does the *interface* work at real tolerances?" | 1 print cycle (2–8 h) | $1–$5 filament | Printing the whole mechanism instead of the joint in question |
| **P3** | Mechanism mounted on the actual (or practice) chassis | "Does it work *integrated* — packaging, reach, wiring, driver ergonomics?" | 1–3 sessions | Real parts | Going straight here from P0 |
| **P4** | Near-final, in the real material, in the real position | "Does it work *repeatably*, 50 times, at capacity?" | 1–2 weeks | Full BOM | Calling P3 "done" |

**[FACT]** GM0 endorses exactly this cadence: *"Prototype/Experiment — putting a first design together using physical materials"* precedes *"Test"*, *"Analyze results"* and *"Final implementation"*, and it explicitly warns that iteration should *"change ONLY ONE variable at a time"* and that teams may iterate *"10+ times"* on a subsystem. ([GM0 Engineering Design Process](https://gm0.org/en/latest/docs/design-skills/engineering-design-process.html))

**[FACT]** FTC 23511 confirms P1 discipline in practice: their first launcher prototype *"was built hastily"* and they noted *"the details of the prototype don't matter too much"* — the point was the takeaway about contact time and wheel compliance, not the rig.

**Divergence check at S5 [JUDGMENT]:** before prototyping, require **≥3 genuinely different concepts** per MUST capability, where "different" means *different physical principle*, not different dimensions. Three sizes of roller is one concept. Roller / claw / funnel-and-gravity is three.

### 3.2 The prototyping kit — buy this in August

**[JUDGMENT]** Total under **$150**, and it will save you weeks. Prices are typical retail, **[UNVERIFIED]** as specific SKUs — buy locally.

| Item | Approx. cost | Why it earns its place |
|---|---|---|
| Corrugated cardboard (free, from shipping boxes) + **foamboard**, 5–10 sheets | $0–$25 | P0 geometry. Foamboard holds a shape cardboard will not |
| **Hot glue gun** + 50 sticks | $20 | The fastest reversible joint in existence |
| Utility knife + spare blades + self-healing mat | $25 | Clean cardboard cuts; safety |
| **Zip ties**, 4 sizes, 500 count | $15 | The universal prototype fastener. 23511 zip-tied foam onto a flywheel to stop it exploding at 6000 RPM |
| Gaffer / duct / masking tape | $15 | — |
| **Clamps**, 4× quick-release | $25 | Clamp the P1 rig to a table; do not build a frame for it |
| Scrap bin: offcut u-channel, extrusion, bent plate | $0 | ⚠️ **Start the scrap bin now.** Label a box "PROTOTYPE STOCK" and never let anyone put a good part in it |
| **One dedicated "prototype" motor + one servo**, permanently wired to a spare hub with alligator/JST leads | ~$75 (already in your spares) | Removes the 20-minute "where's a motor" tax from every experiment |
| Stopwatch / phone with slow-motion video | $0 | ⚠️ **Slow-motion video is the single most underrated FTC diagnostic tool.** 240 fps on any modern phone shows you exactly where an element jams |
| Kitchen scale + tape measure + calipers | $30 | You cannot iterate on numbers you never measured |

⚠️ **[C] Legality note (R304, 2nd sentence):** *"FABRICATED ITEMS created before Kickoff are permitted."* You may build prototype rigs, chassis and mechanisms **right now** and use them on the competition robot. **[C] R304** additionally allows software, designs and parts to be reused year to year. Pre-Kickoff prototyping is not a grey area; it is explicitly protected.

### 3.3 Designing a test that actually decides something

**[JUDGMENT]** A prototype test without these five fields is entertainment, not engineering. Write them on an index card *before* you build.

| Field | Example |
|---|---|
| **Question** | "Can a compliant-wheel roller acquire an element with 2 in of lateral misalignment?" |
| **Variable** | Roller compression (only one, per GM0) |
| **Levels** | 3 mm / 6 mm / 9 mm compression |
| **Measure** | Successes out of 20 attempts, and mean acquisition time from slow-mo video |
| **Kill criterion** | *"If no compression level reaches 16/20 by Wednesday, this concept is dead."* |

**[JUDGMENT] The 20-attempt rule.** Twenty attempts is the minimum sample that distinguishes "works" from "worked once." It takes about four minutes. Teams that skip it discover the difference at their first event.

**[JUDGMENT] The capacity rule.** Test at **maximum hopper/holding capacity**, not with one element. `TESTING-AND-TUNING.md` §6.4 lists "jam at hopper capacity — works at n=1, fails at n=5" as a recurring failure. It is a *prototype-stage* discovery if you look for it, and a *competition-stage* discovery if you do not.

### 3.4 How to kill a concept early

**[JUDGMENT]** Killing is a *social* problem, not a technical one. These five mechanisms make it impersonal:

| Mechanism | How it works |
|---|---|
| **1. Pre-registered kill criterion** | The number and the date are written before the build. Nobody is arguing with a person, only with an index card |
| **2. A named owner who is not the killer** | The concept's owner presents the data; **the team** votes to kill. The owner's job is to report honestly, not to defend |
| **3. Fixed prototype budget** | Each concept gets *N hours and $M*. When it is spent, it is spent. Extensions require the team to vote to take hours from another concept |
| **4. Parallel concepts** | If two concepts are alive, killing one is a *choice*, not a *loss*. If only one is alive, nobody will kill it. **This is the real reason to require ≥3 concepts** |
| **5. The autopsy note** | Every killed concept gets a 5-line write-up: what we tried, what we measured, why it died. ⚠️ **This is portfolio content of exactly the kind judges reward** (§8) |

**Kill-criteria worth pre-registering [JUDGMENT]:**

| Symptom seen in prototyping | Kill it, because |
|---|---|
| Requires driver alignment tighter than ±1 in | The align phase will eat the cycle (§2.5). Widen the tolerance or die |
| Needs a 9th motor or 9th servo | Actuator budget is a hard wall. Redesign now, not in week 6 |
| Fails at capacity but works at n=1 | It will fail in a match. Always |
| Needs a part nobody stocks, on a >3-week lead time | You will not have a spare when it breaks |
| Two of these mechanisms cannot be built (B robot) | Fails F2 duplicability. For a two-robot program this is close to disqualifying |
| Requires a tolerance you cannot hold with a printer and a drill press | You are designing for a shop you do not have |
| Cannot be repaired in the pit in <10 minutes | §7.4. It will end a competition day |

**[FACT] A real, dated kill:** FTC 12527 built an active horizontal-roller intake with two servos, found *"it is inefficient for both intaking and scoring, and it cannot score on the chambers,"* designed a printed claw, tested it, and reported the claw *"proved to be very efficient and had a significant margin of error for aligning"* — the *margin of error* was the deciding criterion, exactly as §2.5 predicts.

### 3.5 Prototyping to reduce the programming burden

**[JUDGMENT]** A prototype is also a *software specification*. Elite teams use prototyping to delete code:

| Prototype finding | Code deleted |
|---|---|
| Widening the intake mouth by 1.5 in makes a vision auto-align unnecessary | An entire CV pipeline, its tuning, and its failure modes |
| A hard stop plus a limit switch is repeatable to ±1 mm | Position PID tuning on that axis |
| The flywheel is insensitive to RPM between 5600 and 6400 | Closed-loop velocity control and its battery-sag compensation |
| A funnel makes element orientation irrelevant | Orientation detection and a rotate mechanism |

⚠️ **[JUDGMENT] For a team with one or two programmers this is the highest-value use of prototyping there is.** Every mechanical tolerance you widen is code you never write, never tune, and never debug at 8 a.m. at an event. See `research/PROGRAMMING-PRACTICE.md` for what the remaining code should look like.

---

## 4. CAD — Onshape and the FTC toolchain

### 4.1 Why FTC standardized on Onshape

**[FACT]** FIRST's own documentation directs FTC teams to PTC's tools: *"free software and services, including Onshape, Creo, Mathcad, Windchill, and Vuforia"*, with **each student and mentor needing their own account** and mentors registering as **"Educator"**. ([FTC Docs — PTC CAD Resources](https://ftc-docs.firstinspires.org/en/latest/cad_resources/ptc/ptc.html))

**[FACT]** Onshape's FIRST page names the plan the **"Educator Plan for FIRST" — free** — and lists real-time collaboration, commenting, follow mode, and **branching & merging**, with sign-up at [onshape.com/en/education/sign-up](https://www.onshape.com/en/education/sign-up). ([Onshape for FIRST Robotics](https://www.onshape.com/en/education/first-robotics))

**[FACT]** GM0 recommends Onshape as *"best for beginners with limited computing resources"*, notes it is cloud-based and runs *"on any computer including Chromebooks"*, and credits it with *"the best collaboration workflow in the industry"*. It also warns that CAD is *"not necessary in FTC to build a successful robot"* and *"not the magic genie that will guarantee you success."* ([GM0 CAD](https://gm0.org/en/latest/docs/design-skills/cad.html))

**[JUDGMENT] The five reasons this matters specifically to a small, poor team:**

| Reason | Consequence for you |
|---|---|
| **$0, forever, for every member** | No licence to ration. Every student can have CAD open at once |
| **Runs on Chromebooks and school PCs** | You do not need to buy workstations. This alone can save four figures |
| **Nothing to install, nothing to lose** | No "the file is on Jayden's laptop and Jayden has the flu" |
| **Real version control and branching** | You can try a redesign without risking the working robot (§4.7) |
| **The FTC vendor part library lives inside it** | Your COTS parts are 15 seconds away, with correct part numbers for the BOM |

### 4.2 Getting set up — do this in the next week

| Step | Action | URL |
|---|---|---|
| 1 | Mentor/coach creates an **Educator** account | https://www.onshape.com/en/education/sign-up |
| 2 | Every student creates a free Education account | https://www.onshape.com/en/education/ |
| 3 | Mentor creates an **Onshape Team/classroom**; all documents owned by it, not by individuals | in-app |
| 4 | Subscribe to the **FTC Parts Library** app | https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba |
| 5 | (Optional) subscribe to **MKCad** for FRC/FTC hardware and simplified components | https://cad.onshape.com/appstore/apps/Manufacturers%20Models/6004ec5e83c40b107c183347 |
| 6 | Email **FIRST@ptc.com** to be added to the FTC parts folder so it appears in "My Onshape" | per [ftconshape.com](https://ftconshape.com/introduction-to-the-ftc-parts-library/) |
| 7 | Run the Onshape learning path (2–4 h per student) | https://learn.onshape.com/learn/learning-path/onshape-fundamentals-cad |

**[FACT]** Onshape's onboarding guidance is explicit that documents should be *"owned by the classroom as opposed to having individual team members own the documents. This helps simplify document management,"* with mentors granted admin and students as members. ([Onshape — Onboarding Your FIRST Robotics Team](https://www.onshape.com/en/blog/how-to-onboard-your-first-robotics-team))

⚠️ **[JUDGMENT] Do step 3 before anyone models anything.** Retro-transferring ownership of 40 documents from six graduating seniors is a real and entirely avoidable September-of-next-year problem.

### 4.3 Document architecture

**[FACT]** The most developed public standard is **FRCDesign.org**'s (an Onshape-based FRC design curriculum sponsored by West Coast Products and Fabworks). Its recommended structure is **multiple documents**, not one:

- a **Concept document** — *"contains the main layout sketch, which determines the overall architecture and geometry for the robot, alongside the Crayon CAD"*;
- **one document per subsystem** — *"contain the part studios, subassemblies and top-level assembly for each subsystem"*;
- a **Main Robot document** — *"contains the top-level full robot assembly … comprised of the top-level assembly from each of the subsystem documents."*

Linking is by **Derive** (layout sketch → subsystem) and **Import** (subassembly → robot). FRCDesign adds: *"The document structure isn't set in stone; as long as it helps your team fulfill the goal of top-down design and uses separate documents to split up the versions of mechanisms, you can place your main layout sketches wherever you want."* ([FRCDesign — Document Setup](https://frcdesign.org/best-practices/document-setup/))

**[FACT]** Onshape's own guidance acknowledges the single-document alternative honestly: one document means *"dependent assemblies will get automatic updates, in-context modeling is easier, and getting started is very simple,"* but *"complex robots will have longer loading times … control over previous changes and version control gets watered down."*

**[JUDGMENT] The FTC-scale recommendation for this program — four documents, not one, and not twelve:**

| Document | Contains | Who edits |
|---|---|---|
| `26-27 · 00 Concept` | The **layout sketch** part studio; the field-relevant geometry; the low-fidelity "crayon" robot; the 18 in cube | Design lead only |
| `26-27 · 10 Chassis` | Drivetrain part studios, chassis assembly, electronics mounting | Drivetrain crew |
| `26-27 · 20 Superstructure` | Everything above the chassis: the mechanism(s) that touch the SCORING ELEMENT | Mechanism crew |
| `26-27 · 90 Robot` | Top-level assembly importing 10 and 20; the packaging/interference check; the render | Design lead |

**[JUDGMENT] Why four and not one.** An FTC robot is small enough that one document *works* — but the two things you actually need are (a) two people editing different subsystems without fighting over one feature tree, and (b) a **version of the superstructure you can revert independently of the chassis**. Four documents buys both. Twelve documents buys neither and costs you an hour a week in Derive plumbing.

### 4.4 The layout sketch — the one CAD habit that separates elite from average

**[FACT]** FRCDesign defines a layout sketch as *"a series of sketches capturing major dimensions of mechanisms, field interactions, and robot constraints"*, inserted into part studios where components are modelled *around* them — top-down design. Their rules:

| Always in the layout sketch | Sometimes | **Never** |
|---|---|---|
| Drivebase dimensions | Gears, belts, chain | *"Specific details like the shape of plates"* |
| End-effector wheel locations **based off of prototyping** | Mounting holes | Gussets |
| Field elements and extension limits | | Unnecessary complexity |
| Mechanism motion paths | | |
| Motor locations | | |
| Game-piece path | | |

They also require *"Multiple sketches, usually one per subsystem, within the main layout sketch part studio"*, *"Name your sketches accordingly"*, and sketching **all possible states** of moving subsystems. The payoff is stated plainly: *"All important measurements that drive the geometry of the robot exist in the layout sketches part studio. They can all be easily viewed and changed together."* ([FRCDesign — Layout Sketch Best Practices](https://frcdesign.org/best-practices/master-sketch-setup/))

**[JUDGMENT] Adapt to FTC by adding four things to the layout sketch on day one:**

1. **The 18 in cube** as a construction rectangle/box, with the robot inside it. **[C] R102.** Check this in CAD at every design review, not once.
2. **The tile grid** (24 in × 24 in) and the field wall, so reach and approach angles are real.
3. **The extension envelope** in every mechanism state — the "all possible states" rule matters far more in FTC than FRC because of the starting-cube rule.
4. **A single `Variables` feature** holding every driving number (`wheelbase`, `intakeHeight`, `slideStroke`, `elementDiameter`). One place to change them; every downstream part studio follows.

⚠️ **[JUDGMENT] Note the phrase "based off of prototyping" in FRCDesign's own list.** The layout sketch is where prototype results *enter* CAD. If you cannot fill in the end-effector geometry from a measured prototype, you are not ready to CAD — you are ready to prototype (§3).

### 4.5 Part studios and assemblies

**[FACT]** FRCDesign's assembly standard, condensed:

- Use the **Origin Cube** FeatureScript to place a 2 in transparent cube at the part studio origin — *"more robust and parametric than fixing or using a mate connector attached to another part."*
- Insert related parts + origin cube for each rigid subassembly, *"use the 'group' tool on all parts,"* then *"fasten the origin mate connector to the origin."*
- *"Sort the instances into folders (i.e. tubes, swerve modules, spacers)."*
- For each degree of freedom, *"create a mate connector on the main layout sketch."*
- Performance: *"Minimize primitives in your assembly," "Minimize the number of mates you use; this lowers the solve time," "Use the replicate tool for adding hardware."*
([FRCDesign — Assembly Best Practices](https://frcdesign.org/best-practices/assembly-setup/))

**[JUDGMENT] The FTC-scale simplification:** **Group aggressively, mate sparingly.** An FTC robot has 3–8 real degrees of freedom. Everything else is a rigid group. A team that mates 400 M4 screws individually has built a document that takes 90 seconds to open on a Chromebook and will be abandoned in November.

**[JUDGMENT] Model fasteners last, in one pass, using Replicate — or not at all.** Hardware in the assembly is worth it for exactly two reasons: (1) checking that a screw actually clears a neighbouring part, and (2) generating a screw-count BOM. Both can be done in an hour at the end. Doing it continuously costs a week.

### 4.6 In-context design — the tool and the trap

**[JUDGMENT]** In-context design (modelling a part in a Part Studio while seeing the surrounding assembly) is the feature that most improves an FTC part's fit and most degrades an FTC document's stability.

| Use in-context for | Do **not** use in-context for |
|---|---|
| A bracket that must land on two existing hole patterns | Anything driven by a dimension that belongs in the layout sketch |
| A cover/shroud that has to wrap real geometry | Parts you will duplicate or mirror |
| A mount that has to clear a moving mechanism at extremes | Anything you will want to reuse next season |

**[JUDGMENT] Three rules that keep it from biting:**

1. **Update the context deliberately, never automatically.** An auto-updating context turns an unrelated chassis edit into a broken superstructure at 10 p.m.
2. **Reference the layout sketch, not the neighbouring part, whenever the layout sketch could carry the dimension.** Layout-driven geometry survives redesign; part-driven geometry does not.
3. **When a context breaks, do not repair the reference — re-derive the geometry from the layout sketch.** Repairing broken references is how documents rot.

### 4.7 Versions, branches and merges — a small-team protocol

**[FACT]** Onshape's FIRST guidance frames branching for exactly the case you have: *"If team members want to build variations or experiment with a mechanism, [branching] enables design changes without impacting the original design."* **[FACT]** FTC 23511 publish their robot and prototype CAD with the explicit instruction to *"see version history/branches as well"*, treating version history as documentation in its own right.

**[JUDGMENT] The four-rule protocol. Anything more elaborate will not survive contact with a 15-person team.**

| Rule | Detail |
|---|---|
| **R1. Version at every gate and every order** | Create a named Version at G1/G2/G3/G4 **and immediately before every parts order**. Name it `V3 — G3 CAD lock 2026-10-24`. ⚠️ The order version is what you diff against when a part arrives and does not fit |
| **R2. Branch for anything risky** | `main` is the robot being built. `exp/turret-v2` is the idea. Branch names start with `exp/` |
| **R3. Merge only at a review** | A branch merges into `main` only when a second person has looked at it. This is your entire code-review culture, applied to CAD, and it costs 10 minutes |
| **R4. Weekly release snapshot** | Every Friday: version `main`, export a STEP of the robot assembly, and drop a dated PNG render into the portfolio folder. ⚠️ **This is §8's evidence trail and it costs 5 minutes** |

**[JUDGMENT] What versioning buys a *small* team specifically:** the confidence to try the risky redesign. A team that cannot revert will not experiment, and a team that will not experiment converges on the first idea it had — which is almost never the best one.

### 4.8 Configurations — the two-robot lever

**[FACT]** The FTC Everybot ships as a single configured Onshape document; its build guide instructs teams to *"Find the configurations panel in the upper left corner"* and select a configuration, warning that *"All configurations will result in different 3D printed parts. Please ensure that all of your configuration options are set before exporting files for printing."* Configurations there switch the chassis between a custom printed chassis and the goBILDA/REV/Studica/AndyMark COTS chassis, and switch hardware sizes (e.g. M4 vs 6 mm). ([FTC Everybot 3D Printing guide](https://docs.google.com/document/d/1BzlHjUQulXNchWSRm-UigonzINrQqb_-EIGO_drZKKA/edit))

⚠️ **[JUDGMENT] This is the single most under-used Onshape feature in FTC, and it is precisely aimed at your two-robot problem.**

| Use configurations for | Result |
|---|---|
| **A robot vs B robot** as two configurations of one model | One source of truth. A fix to a shared bracket fixes both robots |
| A mechanism at **three stroke lengths** | Pick after prototyping without re-modelling |
| **COTS chassis vs printed chassis** | Lets the B team start on whatever chassis you already own |
| **Hardware standard** (M3 vs M4) | Removes a whole class of "wrong screw" mistakes |

**[JUDGMENT] The two-robot rule:** the B robot should be a **configuration**, not a fork. If the B team needs a *fork*, you have designed two robots and doubled your spares, your tuning and your documentation for one extra alliance slot. See F2 Duplicability in `reference/ACHIEVABILITY-FACTORS.md`.

### 4.9 Part libraries — the real table

**[FACT]** All URLs live-probed 2026-08-22 unless noted.

| Library | Covers | How to get it | URL |
|---|---|---|---|
| **FTC Parts Library** (built by **FTC 2901 Purple Gears**, Cardinal Gibbons HS, Raleigh NC, with contributions from teams **12828, 16250, 17585** and Pitsco staff) | *"ServoCity, GoBilda, Pitsco, AndyMark, and RevRobotics"*; many parts **configurable** (gears, channels); parts carry links back to the vendor page and **the correct part number so they appear in the BOM** | Onshape App Store, **or** email `FIRST@ptc.com` to have the folder appear in My Onshape | [App Store](https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba) · [guide](https://ftconshape.com/introduction-to-the-ftc-parts-library/) |
| **MKCad** (built by **FRC 1836 MilkenKnights**) | Bearings, electronics, fasteners, COTS gearboxes, gears, hubs, motors, pulleys, sensors, snap rings, shaft collars, spacers, sprockets, wheels; includes **KrayonCAD** simplified components for fast architecture studies | Onshape App Store | [App Store](https://cad.onshape.com/appstore/apps/Manufacturers%20Models/6004ec5e83c40b107c183347) |
| **REV ION Build System — Onshape CAD Examples** | REV wheel assemblies, MAXTube structures, roller assemblies, drivetrains, full mechanisms, graded low→high complexity | Public docs | https://docs.revrobotics.com/ion-build/onshape-examples/onshape-cad-examples |
| **goBILDA STEP files** | Per-product STEP downloads on each product page | Product pages | https://www.gobilda.com/ (per-product) |
| **ServoCity / Actobotics full STEP archive** | All Actobotics STEP files, one ZIP | Dropbox link published by GM0 | https://www.dropbox.com/s/y14pykn1f2gmuss/All%5FSTEP%5FFiles.zip?dl=0 |
| **10650 Hazmat Robotics library (+ MiSUMI parts)** | Community GrabCAD library including MiSUMI components | GrabCAD | https://grabcad.com/library/ftc-cad-files-w-misumi-parts-1 |
| **FTC Field Model (Onshape)** | The official field, for reach/approach checks | Onshape public doc — the **2026 (DECODE)** model is linked from Onshape's FIRST page; ⚠️ **a 2027/BIOBUZZ model should appear at or after Kickoff — re-check** | [Onshape FIRST page](https://www.onshape.com/en/education/first-robotics) |
| **Belt / HTD pulley / GT2 pulley generators** | Parametric belts and pulleys | Public Onshape docs listed by GM0 | [GM0 Useful Resources](https://gm0.org/en/latest/docs/useful-resources.html) |

**[JUDGMENT] Use the FTC Parts Library as the default and MKCad as the supplement.** The reason is not model quality — it is that the FTC library carries **vendor part numbers into the Onshape BOM**, which is the hand-off `reference/BOM-PROTOCOL.md` step B1 expects. A BOM that already contains real part numbers removes an entire evening of transcription and the ordering errors that come with it.

### 4.10 FeatureScripts worth installing

**[FACT]** Curated at [frcdesign.org/resources/featurescripts](https://frcdesign.org/resources/featurescripts/). The ones that pay off in **FTC** specifically:

| FeatureScript | What it does | FTC value **[JUDGMENT]** |
|---|---|---|
| **Origin Cube** | 2 in transparent cube at the part studio origin for robust assembly mating | ⭐ Foundational — the assembly standard in §4.5 depends on it |
| **Gusset Generator** (Julia's) | Builds a gusset from selected holes | ⭐ Every custom bracket, in seconds |
| **Electronics Mounting** (Julia's) | Generates hole patterns for electronic components from centre points | ⭐ Control Hub / Servo Hub / battery mounts |
| **Spacer Generator** / **Robot Spacer** | Round or hex spacers, parametric | ⭐ You will print dozens |
| **3D Printed Mass** (Julia's) | Adjusts a printed part's mass by material and infill | ⭐ Makes your CAD mass estimate honest |
| **Part Lighten** (2471) / **CheeseIt!** (TLamp) | Pocketing and lightening patterns (isogrid, hex, circles) with savings estimates | Weight reduction on plates |
| **Belt & Chain Gen** | Multi-pulley/sprocket belt and chain paths | Removes centre-distance arithmetic |
| **Spur Gear** | Parametric spur gears for printing | Printed gears (§5.4) |
| **Measure Cut List** | Measurement tables → cut lists | ⭐ Hand-tool fabrication (§5.3) — this is your "cut list" generator |
| **Auto Layout** | Lays derived plates into sheets by thickness | ⭐ Prep for outsourced laser cutting (§5.6) |
| **Advanced Variables** (2471) | Compound variables: path lengths, angles, chain centre distances | Keeps the layout sketch driving everything |
| **Supportless counterbore bridging** (Imant's) | Counterbores printable without support, by exploiting bridging | ⭐ Recommended by CoreFTC — [imants.net/programming/fs-bridge-overhang](https://www.imants.net/programming/fs-bridge-overhang) |

**[JUDGMENT] Install five, not thirty.** Origin Cube, Gusset Generator, Spacer Generator, Electronics Mounting, Measure Cut List. Adding FeatureScripts you do not use is a tax on every student who opens the toolbar.

### 4.11 The alternatives, and when they make sense

| Package | Cost to you | When it is the right call **[JUDGMENT]** | GM0's stated caveat **[FACT]** |
|---|---|---|---|
| **Onshape** | **$0** (Educator Plan for FIRST) | **The default. Choose this unless a specific line below applies** | *"best for beginners with limited computing resources"*; runs on Chromebooks |
| **Fusion 360** | Free education licence | You own a CNC router or 3D printer farm and want integrated CAM; or a mentor already lives in Fusion | *"Creates proprietary file structures that discourage reusability"* and can *"actively encourage bad design habits"* |
| **SolidWorks** | Free via FIRST sponsorship form | A mentor or teacher is genuinely fluent, and every student has a 16 GB Windows PC | *"Mac incompatible"*; *"requires 16GB RAM minimum"* |
| **Inventor** | Free education licence | Team already has Inventor expertise; lower-spec Windows PCs | *"Mac incompatible"*; *"less common in college curricula"* |
| **Creo** | Free via PTC/FIRST | Essentially never for a small FTC team | *"Steepest learning curve"*; limited tutorials; Windows only |
| **FreeCAD** | $0, open source | Only if your school blocks cloud services entirely, or you have a philosophical requirement for offline open-source | ⚠️ **GM0 does not recommend it and does not list it** — **[JUDGMENT]** the FTC part libraries, the community tutorials and the collaboration story are all absent. Expect to pay for that in student-hours |

⚠️ **[JUDGMENT] The mixed-toolchain trap.** If half the team uses Fusion and half uses Onshape you have no single robot model, no shared BOM, and no version history — you have STEP files in a Drive folder. **Pick one and enforce it.** If a mentor insists on SolidWorks, the correct compromise is that the *mentor* works in SolidWorks and the *robot* lives in Onshape, not the reverse.

### 4.12 CAD failure modes specific to small teams

**[JUDGMENT]** These are the ones that actually happen:

| Failure | Symptom | Prevention |
|---|---|---|
| **One person owns the CAD** | Everything stops when they are sick or graduate | Two people modelling from week 1, minimum. Documents owned by the classroom (§4.2 step 3) |
| **CAD as decoration** | A beautiful model of a robot that was already built by hand | CAD *before* fabrication, at G3. If CAD trails the build, stop CADding and use a cut list instead |
| **The model that never matches the robot** | Nobody trusts CAD, so nobody updates it, so nobody trusts it | ⚠️ **Rule: any change made to the robot gets made in CAD within 48 hours, or reverted on the robot** |
| **Modelling every screw from the start** | Document takes 90 s to open; students stop opening it | §4.5 — hardware in one pass at the end |
| **No layout sketch** | Changing the wheelbase means editing 20 parts | §4.4 |
| **Fifteen documents** | Nobody can find anything; Derives break | §4.3 — four documents |
| **Broken in-context references** | Superstructure explodes after an unrelated chassis edit | §4.6 |
| **No versions before ordering** | A part arrives that does not fit the current model and nobody knows which model it was made from | §4.7 R1 |

### 4.13 The 18-inch check, and other rule checks you should do *in CAD*

**[C]/[JUDGMENT]** Do these inside Onshape at G3 — every one of them is cheaper in CAD than at inspection:

| Check | Rule | How to do it in Onshape |
|---|---|---|
| **STARTING CONFIGURATION fits an 18 in cube**, fully stationary, self-contained | **R102** [C] | A construction box in the layout sketch; measure the assembly bounding box in the starting configuration |
| Robot can be **removed from the FIELD without power** | **R203** [C] | Model the mechanism at rest with no power — can a human lift it clear? |
| No exposed sharp edges / protrusions; nothing loose | **R201** [C] | Fillet/chamfer pass on every custom part; check exposed screw ends |
| **≥2 ROBOT SIGNS**, on opposite or adjacent surfaces | **R401** [C] | Model the sign as a real part and reserve the two flat areas early. ⚠️ Teams lose this space and then have nowhere legal to put the signs |
| COTS mechanisms are **single-DoF** | **R303** [C] | A design-review question, not a CAD measurement — but record the answer |
| Extension envelope in every mechanism state | game rules ⏳ | The "all possible states" layout sketches (§4.4) |

### 4.14 The minimum viable CAD standard

**[JUDGMENT]** For a 15-student program, enforce exactly these seven things. Everything else is optional.

1. One Onshape org; all documents owned by the classroom.
2. Four documents (§4.3), named `26-27 · NN Name`.
3. A layout sketch part studio in the Concept document, with a `Variables` feature and the 18 in cube.
4. Every custom part driven by the layout sketch or by a variable — never by a hand-typed number that appears twice.
5. COTS parts inserted from the FTC Parts Library so the BOM carries part numbers.
6. A named Version at every gate and before every order.
7. A Friday snapshot: version + STEP export + dated render.

---

## 5. Fabrication tiers — what each one buys you

### 5.1 The tier ladder

**[JUDGMENT]** Cost columns are the *marginal* cost of adding the tier, in USD as of August 2026. "Space" and "Person" are the hidden costs nobody budgets.

| Tier | Capability | Hardware cost | Space | Person | What it unlocks | Diminishing returns bite when… |
|---|---|---|---|---|---|---|
| **T0** | **COTS-only assembly** (goBILDA / REV kit building) | $0 beyond parts | A table | Anyone, week 1 | A complete, legal, competitive robot. ⚠️ **Most FTC robots at most events are T0 or T0+T2** | You need a bracket that does not exist in any catalogue |
| **T1** | **Hand tools + drill press** | **$150–$500** | A bench | 1 trained student | Cut extrusion/channel to length, drill custom holes, deburr, file. **Doubles the usefulness of every COTS part** | Repeat accuracy on holes; anything needing a straight long cut |
| **T2** | **3D printing** | **$190–$930/printer** + $20/kg | 0.5 m² + ventilation | 1 "print czar" | Custom geometry: adapters, mounts, rollers, guides, gears, hoppers. **This is your machine shop** | Large flat structural plate; anything needing metal strength |
| **T3** | **Bandsaw / miter saw / bench tools** | **$300–$900** | 2–3 m², dust | Trained + supervised | Fast, square, repeatable stock cuts; batch cutting for two robots | Flat plate with hole patterns; anything 2-D and complex |
| **T4** | **Outsourced laser / waterjet plate** (Fabworks, OSH Cut, SendCutSend) | **$0 capital**, ~$20–$150/order | None | 1 student who can export STEP/DXF | ⭐ **Aluminium plate, brackets, gussets, chassis plates — at professional accuracy, with no shop** | Iteration speed: 1–2 day cut + shipping means ~3–5 day loop |
| **T5** | **In-house CNC router / mill** | **$1,800–$5,700** (Shapeoko range) + tooling + software + dust control | A dedicated room | ⚠️ **A dedicated, trained adult** | Same-day plate iteration; deep pockets; 3-D machining | ⚠️ **Almost immediately, for a team this size — see §5.7** |

### 5.2 T0 — COTS-only, and why it is not a compromise

**[FACT]** The BIOBUZZ rules explicitly bless heavy COTS use, with two limits: **R301** [C] permits COTS mechanisms but prohibits *"COTS MAJOR MECHANISMS purposefully designed to complete a game task"* — with two **allowed exceptions**: *"A. COTS drive CHASSIS"* and *"B. COTS MAJOR MECHANISMS created as part of the official FIRST Tech Challenge StarterBots."* **R303** [C] requires COTS components and mechanisms to be **single degree of freedom**, with named allowances for linear slide kits, linear actuator kits, single-speed gearboxes, pulleys, turntables, lead screws, single-DoF grippers, ratchets, holonomic wheels, **dead-wheel odometry kits**, misalignment couplers and variable-angle linkages.

⚠️ **[JUDGMENT] R301 exception B is a genuinely large lever for a small team and is easy to miss.** Mechanisms that are part of the **official FIRST StarterBot** are permitted as COTS MAJOR MECHANISMS. For a program with limited fabrication capacity, the StarterBot line is not a beginner's crutch — it is a rule-sanctioned shortcut to a legal scoring mechanism. Read the 2026-27 StarterBot materials the day they publish.

**[FACT]** A pre-Kickoff StarterBot resource already exists for this season: Studica publishes an **"FTC Starter Bot Resource Guide 2026–2027"** with a downloadable **build guide PDF, STEP CAD files (ZIP) and a wiring diagram**, covering drive base, mechanical assembly, wiring and intake rollers, stating that *"The full Starter Kit will be officially revealed at FTC Kickoff in September 2026."* The page names the 2026-27 season **FIRST® CANOPY™** (the umbrella season name; BIOBUZZ is the FTC game). ([studica.com/ftc-starter-bot-resource-guide-2026-2027](https://www.studica.com/ftc-starter-bot-resource-guide-2026-2027))

**[JUDGMENT] What T0 gets you:** a legal, inspectable, competitive robot with zero fabrication risk, buildable by students in week 1, and **trivially duplicable for the B robot** (buy two of everything). What it does not get you: a mechanism precisely shaped to *your* SCORING ELEMENT. That gap is exactly what T2 fills for about $300.

### 5.3 T1 — Hand tools and a drill press

**[FACT]** GM0's **necessary** tool list: safety glasses; Phillips screwdrivers; hex drivers/L-keys in **7/64 in** (Actobotics/TETRIX), **3/32 in** (TETRIX), **2.5 mm and 3 mm** (goBILDA); nut drivers in **5.5 mm** (REV) and **7 mm** (goBILDA); drill and bits; needle-nose and locking pliers; metal file; 2+ quick-lock clamps or a vise; hammer and mallet; centrepunch; hacksaw; wire stripper/cutter; zip ties or Velcro; electrical tape; stainless ruler and rafter square; sharp pencil or fine marker. Their **helpful** list adds: bandsaw (*"cannot cut steel shafts"*), impact driver, drill press, miter saw with a non-ferrous blade, Dremel, grip tape, **caliper**, soldering iron, heat gun, router or table saw, jigsaw, metal brake, 3D printer. ([GM0 Tools List](https://gm0.org/en/latest/docs/hardware-components/tools-list.html))

**[JUDGMENT] Three additions GM0 does not stress that matter enormously for repeatability:**

| Tool | ~Cost | Why |
|---|---|---|
| **Drill press** (benchtop) | $130–$250 | ⚠️ A hand-drilled hole in extrusion is out of square by enough to bind a shaft. A drill press is the cheapest accuracy you can buy |
| **Digital caliper** | $25 | You cannot design tolerances (§7.5) you cannot measure. Buy two |
| **Deburring tool + files** | $20 | **[C] R201** prohibits exposed sharp edges. Deburring is an inspection requirement, not a nicety |

**[FACT]** Hand tools are sufficient for real competitive work: FTC 23511 built their intake rollers from PETG tube using *"only … hand tools like hacksaws and drills"* — at a cost of *"nearly 30 minutes to make a single roller"*, which is exactly the sort of number a team should know before committing to six rollers × two robots.

**[JUDGMENT] The T1 productivity multiplier is a cut list, not a tool.** Use the **Measure Cut List** FeatureScript (§4.10) to generate a table of stock, length and quantity straight from CAD, then cut everything for both robots in one session with a stop block clamped to the bench. Batch cutting is where a two-robot program gets its labour back.

### 5.4 T2 — 3D printing (the deep dive)

**[JUDGMENT] This is the tier that matters most for you.** It converts CAD into parts at ~$0.50 each, overnight, with no adult supervision required, and it is what makes a printed-structure robot like the Everybot possible.

#### 5.4.1 What a printed robot actually costs

**[FACT]** The **2025-26 FTC Everybot** — a complete competitive robot with mecanum drive, floor intake, hopper, catapult and an endgame mechanism — has a published BOM totalling **"$976 (Not including Hardware or Control Hubs)"**, and its structure is **47 printed part instances** across chassis (8), catapult (10), superstructure (4), hopper (6), intake (15) and endgame (8). Its non-printed structure is REV **15 mm extrusion at $13.50/m**, goBILDA 5203 motors at $55, a **$190** GripForce mecanum set — and, notably, **glass-fibre rods sourced from Home Depot as $5.47 driveway markers**. ([FTC Everybot BOM spreadsheet](https://docs.google.com/spreadsheets/d/1sDXYv0FfvtYJpS8D2unsGj_9wgmHTuOPAkGFtUbN1QY/edit)) ⚠️ Those are **DECODE-season (2025-26) prices** — the same sheet lists the Control Hub at $350 and Expansion Hub at $250, whereas `reference/VENDOR-ECOSYSTEMS.md` verified **$375 / $275** in August 2026. **Price drift is real; re-quote.**

**[JUDGMENT]** The lesson is not "build the Everybot." It is that **a full competitive FTC robot's custom structure can be entirely 3D printed for a filament cost in the tens of dollars**, and that a hardware-store consumable can legitimately substitute for a robotics-catalogue part. **[C] R302** explicitly permits raw materials including *"metals, plastic, rubber, and wood"* and permits modifying legal COTS parts and raw stock.

#### 5.4.2 Printers FTC teams actually use

**[FACT]** From the Everybot crew's published **"Recommended 3D Printers & Filament for FTC Everybot"** tab. Their stated requirements: the printer *"must be able to print parts successfully"* and *"must have a minimum bed size of 200mm x 200mm (7.87" x 7.87")"*; recommended layer height **0.2 mm** across the board. Prices are **as listed on that 2025-26 sheet** — re-check.

| Printer | Bed | Listed price | Note from the sheet |
|---|---|---|---|
| Elegoo **Neptune 4** | 225×225 | **$189** | Also documented by FTC Docs |
| Creality **Ender 3 V3 SE** | 220×220 | **$199** | *"Everybot Crew used this printer for many of the parts printed"* |
| Anycubic **Kobra 2 Neo** | 250×220 | **$199** | |
| Sovol **SV06** | 220×220 | **$209** | |
| AnkerMake **M5C** | 220×220 | **$240** | |
| FlashForge **Adventurer 5M** | 220×220 | **$290** | |
| Elegoo **Centauri Carbon** | 256×256 | **$300** | Called out as a printer the crew can vouch for |
| Bambu Lab **A1** | 256×256 | **$339** | |
| AnkerMake **M5** | 235×235 | **$399** | |
| Bambu Lab **P1P** | 256×256 | **$500** | |
| Bambu Lab **X1C** | 256×256 | **$799** | *"Everybot Crew used this printer for many of the parts printed"* |
| Prusa **MK4S** | 250×210 | **$929** | |

**[FACT]** FTC 23619 Overture (Monterrey, Mexico) report using **Creality K1C** printers for their season parts. **[UNVERIFIED]** Bambu Lab's US store on 2026-08-22 showed price fields of **$539 / $579** on the P1S page and **$299 / $369 / $399** on the A1 page; I could not reliably map those to specific variants, so treat them as a range needing confirmation at [us.store.bambulab.com](https://us.store.bambulab.com/).

⚠️ **[FACT]** FIRST's own documentation maintains a printer-choice guide split into budget / mid-range / high-end tiers at [ftc-docs.firstinspires.org/…/printer_choice](https://ftc-docs.firstinspires.org/en/latest/manufacturing/3d_printing/printer_choice/printer_choice.html), and identifies **FDM** as *"the most common type of printer used, and the most practical for robotics teams"*, with SLA and SLS *"often more expensive, difficult to use, and have less use in FTC."*

**[JUDGMENT] Buy two cheap fast printers, not one expensive one.** For a two-robot program, throughput and redundancy beat quality: 47 printed parts × 2 robots × spares is ~120 prints, and a single machine down for a week during build season is a schedule event. Two ~$200–$340 machines with ≥220×220 beds is the right shape. **An enclosure matters only if you move beyond PLA+ (§5.4.3).**

#### 5.4.3 Filament — what is actually strong enough

**[FACT]** The Everybot crew's filament guidance is unusually direct and worth quoting in full:

> *"While many filaments can create a successful FTC Everbot, we recommend using filaments that have higher impact resistance. Some common filaments such as normal PLA & PETG do not handle impact loads very well. While materials like ABS, ASA, PC, and Nylon are good materials, they are more difficult to print. Because of this, the recommended filament type is PLA+. PLA+ and similar materials print with the ease of PLA but have material properties more similar to ABS and Nylon. **Please note that PLA is not a recommended filament.** PLA+ is much different than standard PLA."*

Their named PLA+ options and listed prices (2025-26 sheet): **Duramic PLA+ $18.99** (*"Personal favorite of the Everybot Crew"*), **Polymaker PolyLite PLA Pro $24.99** (*"Most parts on the robot printed with this"*), **Polymaker PolyTerra PLA+ $21.99**, **Elegoo PLA Plus $23.78**, **Overture PLA Plus $20.99**, **Inland PLA+ $22.99**.

**[FACT]** GM0's material notes: PLA is *"stiff but more brittle than other filament options"* (hotend 190–230 °C, bed 20–60 °C); PETG is *"a strength upgrade to PLA,"* *"far less brittle and withstands impacts better"* (230–260 °C / 60–80 °C) but *"bond[s] very well to print beds, especially glass and PEI"*; ABS *"can withstand high loads and is quite ductile"* (230–250 °C / 100–120 °C) with *"Enclosure highly recommended"*; Nylon is *"the king of impact resistance"* (240–260 °C / 55–80 °C) but *"must be dried before (and while) printing"*; polycarbonate is *"very rigid, and handle[s] shock loads exceedingly well"* but is a *"very challenging material to print."* Carbon-fibre fills are *"meant to be stiffer"* and *"help to improve the printability."*

**[JUDGMENT] The decision table for this program:**

| Part class | Material | Why |
|---|---|---|
| **Default: brackets, mounts, spacers, guides, hoppers, adapters** | **PLA+** | Prints like PLA, tolerates impact far better than PLA. This is 80–90% of your printed parts |
| Parts that take repeated impact from other robots | **PETG** or PLA+ with more walls | PETG's toughness; accept the extra print fussiness |
| Rollers, compliant surfaces | **PETG tube stock + grip tape** (not printed) — see §6.5 | 23511's approach; lighter and more impact-resistant than a printed roller |
| Anything near a motor that runs hot, or in a hot car | **PETG / ABS / ASA** | ⚠️ PLA+ softens in a closed car in summer. This is a real, recurring FTC failure |
| High-load structural, if you have an enclosed printer and time | **ASA / PC / PA-CF** | Only if you already print these reliably. **[JUDGMENT] Do not learn a hard filament during build season** |
| ⛔ Never | **Plain PLA** for load-bearing parts | The Everybot crew's explicit position, and the correct one |

**[JUDGMENT] Buy 4–6 kg of one PLA+ brand in one colour, plus 1 kg of PETG.** Consistency across spools removes a whole class of "why did this print fail" investigations, and one colour makes the robot look deliberate, which judges notice.

#### 5.4.4 Orientation, walls and infill for load-bearing FTC parts

**[FACT]** The physical fact everything else follows from, per GM0: *"3D printed parts are inherently stronger on two axes and weaker on one axis"* because of layering. Their remedies: *"the part should have a flat bottom to maximize contact with the print bed"*; consider the **draft angle** — *"maximum angle the printer can print without support material"*; and where load directions conflict, *"split the part into multiple parts."*

**[FACT]** CoreFTC (published by **FTC 16461 Infinite Turtles**) adds four design rules: (1) *"Minimize Overhangs Greater than 45 Degrees"* — noting 45° *"is a general guideline that works for most printers"*; (2) *"Maximize Bed Contact"* to prevent detaching and warping; (3) *"Placing fillets and chamfers at sharp corners improves the strength of prints and prevents stress concentrations"*; (4) design in tolerances for clearance vs press fits, with the caveat that *"Tolerances vary between printers, a tight fit on one printer may be a thru-hole on another, we recommend creating test models to figure out tolerances for your printers."* ([CoreFTC — General Tips](https://matthews-community-robotics.gitbook.io/coreftc/design-for-3dp./general-tips.md))

⚠️ **[JUDGMENT] The single rule that matters: never let a load try to peel layers apart.** Orient every part so the principal tensile or bending load runs **along** the layers, not **across** them. Concretely:

| Part | Wrong orientation | Right orientation |
|---|---|---|
| A bracket with a bolted flange | Flange flat on the bed, arm sticking up (layers peel at the corner) | On its side, so the corner's layers run continuously around the bend |
| A shaft collar / hub adapter | Standing up (splits along a layer under torque) | Flat, so hoop stress runs within layers |
| A long thin arm | Standing up | Flat on the bed, long axis in-plane |
| A gear | Any orientation is acceptable for tooth load; **but** print flat so the bore's layers resist the hub | Flat |

**[JUDGMENT] Slicer settings for structural FTC parts — a defensible starting point.** ⚠️ These are my recommendation, not a sourced standard; the only sourced number is the Everybot's **0.2 mm layer height**.

| Setting | Structural part | Cosmetic / non-load part | Reasoning |
|---|---|---|---|
| Layer height | **0.2 mm** | 0.2–0.28 mm | Everybot standard; good strength/time balance |
| **Walls / perimeters** | **4–6** | 2–3 | ⚠️ **Walls carry FTC loads, not infill.** Going 3→5 walls buys far more strength per gram and per minute than 20%→50% infill |
| Top/bottom layers | 5–6 | 3–4 | |
| **Infill** | **30–50% gyroid or cubic** | 10–15% | Above ~50% you are paying time for very little; below ~25% walls start to buckle |
| Infill pattern | Gyroid or cubic | Grid | Isotropic; better than rectilinear for multi-axis load |
| Nozzle | 0.4 mm (0.6 mm for bulk parts) | 0.4–0.6 mm | 0.6 mm halves print time on chunky brackets |
| Seam | Rear / aligned | any | Keeps the weak seam off a loaded face |
| Brim | 5 mm on tall/narrow parts | none | Bed-adhesion insurance overnight |

**[FACT]** CoreFTC documents two strength-boosting techniques worth knowing: **annealing** (*"printed parts are slightly remelted, typically in an oven to combine layers and achieve an improved crystallized structure with greater firmness, tensile (Z) strength and heat resistance"*), with the warnings that *"parts will deform"* so it should not be used on dimensionally critical parts, that parts should be printed at **100% infill** for annealing, and that packing the part in **fine powdered salt** in an oven-safe container prevents deformation; first run *"at the glass transition temperature of your filament for 30-40 minutes."* They also describe **gradient/"smart" infill** driven by FEA to *"target infill specifically to high load areas."*

**[JUDGMENT] Skip annealing during build season.** It is a genuinely useful off-season experiment and a good portfolio/engineering-analysis exhibit, but a dimension-changing post-process on a part you are about to bolt into a robot is not where a small team should spend risk.

#### 5.4.5 Design-for-3D-printing rules for FTC parts

**[JUDGMENT]** Ten rules, in order of how often violating them costs you a robot:

1. **Never trap a load in the Z direction** (§5.4.4).
2. **Fillet every internal corner** (CoreFTC). A 2–3 mm fillet is free strength.
3. **Use heat-set threaded inserts, not printed threads, not set screws.** Printed threads strip; set screws — per GM0 — *"slip easily and damage axles"*, and their advice is to *"use clamping hubs and collars instead."*
4. **Design in clearance:** ~0.2–0.3 mm on thru-holes for M3/M4, ~0.1 mm interference for press fits — then **print a test coupon and correct**, exactly as CoreFTC advises.
5. **Let metal take the bearing load.** Print the bracket; press in a real flanged bearing. Never run a shaft directly in printed plastic on a load path.
6. **Sandwich, don't cantilever.** Support a shaft on both sides with plates rather than one printed boss.
7. **Split large parts at a low-stress plane** and bolt them, rather than printing at an angle with supports.
8. **Use supportless counterbores** via bridging (CoreFTC / Imant's FeatureScript) so screws sit flush with no support scars.
9. **Design the part so a failure is cheap.** A printed part that breaks is fine if it breaks *instead of* an aluminium channel and takes 4 minutes to swap.
10. **⚠️ Print a full spare set.** GM0 is explicit: teams should *"print at least one set of every single 3D printed part as spares for competition."* This is non-negotiable for a two-robot program — one set per robot plus one shared spare set.

**[JUDGMENT] What NOT to print:** long structural beams (buy u-channel/extrusion), anything under sustained high tension, gears carrying full motor torque at low ratio without a metal hub, anything that must hold a precise dimension after a hot car ride, and anything a $6 COTS part already does.

#### 5.4.6 Print-farm hygiene for a small team

| Practice | Why **[JUDGMENT]** |
|---|---|
| One named **"print czar"** per week | Removes the "someone should print that" failure |
| A shared queue (a whiteboard column is enough) with part name, quantity, requester, due date | Prints are a resource with a lead time; treat them like an order |
| **Filename = CAD part name = BOM line** | Traceability from robot to model to purchase, for free |
| Export **STL** from Onshape (Everybot: *"For most 3D printer slicers, .STL is the preferred file type"*; medium resolution is *"fine for every part in this build"*) | Standard, boring, works |
| A labelled bin per subsystem for printed parts | ⚠️ Losing a printed part costs 4 hours, not 4 dollars |
| Print the spare set **at the same time as the first set** | Same settings, same spool, same behaviour |

### 5.5 T3 — Bandsaw, miter saw, bench tools

**[JUDGMENT]** A horizontal/vertical **bandsaw** (~$300–$500) or a **miter saw with a non-ferrous blade** (~$150–$300 plus a $40 blade) is the highest-value power tool for an FTC team after the drill press, because it makes *batch* cuts square and repeatable, which is exactly what a two-robot program needs.

⚠️ **[FACT]** GM0 warns a bandsaw *"cannot cut steel shafts."* **[JUDGMENT]** Cut steel shafting with an abrasive cutoff or a Dremel, and always deburr and chamfer the end before it goes near a bearing.

**[JUDGMENT] What T3 does not solve:** flat plate with accurate hole patterns. That is T4's job, and T4 is cheaper than T5.

### 5.6 T4 — Outsourced laser-cut plate: the small-team superpower

⚠️ **[JUDGMENT] If you read one recommendation in §5, read this one. Outsourced sheet-metal is how a team with no shop gets shop-quality parts, and it is what a top FTC team with a swerve drivetrain actually did.**

**[FACT]** FTC 23511 Seattle Solvers stated that their swerve-module parts were *"the only thing we haven't Fabworks-ed"* — i.e. essentially every other custom plate on a world-class-level robot came from an online laser cutter.

**[FACT]** Fabworks, verified on their site 2026-08-22: upload a **2D DXF or 3D STEP file up to 24 MB** for an instant price and delivery date; **"No order minimum"**; services include laser cutting, **bending**, tube laser cutting, **tapping**, PEM **hardware insertion**, countersinking and powder coating; materials include aluminium **5052-H32 / 6061-T6 / 7075-T6** in thicknesses from **0.032 in to 0.375 in**, plus steel, stainless and galvanised. Their FIRST-facing page frames the value as letting teams *"ship out tricky or time-consuming parts"* while keeping in-house time on *"assembly, wiring, programming, and driver practice."* ([fabworks.com](https://www.fabworks.com/) · [Fabworks for FIRST](https://www.fabworks.com/blog/fabworks-for-first))

**[UNVERIFIED]** Third-party pages claim Fabworks offers *"50% off your first order, up to a maximum discount of $200"* and that various teams publish 5% referral codes. ⚠️ The `fabworks.com/first-50` URL **404'd** when probed on 2026-08-22. **Ask Fabworks directly before assuming any discount.**

**[FACT]** Competitors worth quoting against: **OSH Cut** ([oshcut.com](https://www.oshcut.com/)) and **SendCutSend** ([sendcutsend.com](https://sendcutsend.com/)), both live. Comparative claims about instant-quote size limits and material breadth come from vendor marketing pages and are **[UNVERIFIED]**.

**[JUDGMENT] How to actually use T4 in an FTC season:**

| Step | Detail |
|---|---|
| 1 | Design plate parts as **2-D profiles with a uniform thickness** — this is the natural output of a layout-sketch workflow |
| 2 | Use the **Auto Layout** FeatureScript to group derived plates by thickness into sheets |
| 3 | Export **STEP** (preferred) or DXF; upload; read the instant quote |
| 4 | ⚠️ **Order the B-robot copies in the same order.** Setup cost dominates; the second copy of a part is close to free |
| 5 | ⚠️ **Order one spare of every plate that bolts to the drivetrain.** A bent chassis plate at an event is otherwise fatal |
| 6 | Budget **3–5 days** door-to-door and design your schedule so a plate order goes out at G3, not after it |

**[JUDGMENT] The cost comparison that decides T4 vs T5:** a Shapeoko 4 is **$1,800** before tooling, dust collection, a table, software time and an adult to supervise. At typical FTC plate volumes — perhaps 15–30 custom plates per robot per season — **[DERIVED]** that capital would buy several seasons of outsourced cutting. T5 wins on *iteration speed*, not on cost.

⚠️ **[C] One rules caution on outsourcing.** **R101** requires that the ROBOT and its MAJOR MECHANISMS *"must be built by the FIRST Tech Challenge team"*, while explicitly stating the rule *"is not intended to prohibit or discourage assistance from other teams (e.g., fabricating elements, supporting construction…)"*. Separately, **R301**'s guidance says *"A vendor selling 'build to print' manufacturing of publicly available, purpose-built solutions is against the spirit of this rule."* **[JUDGMENT]** Sending **your own** design to a general-purpose laser cutter is ordinary fabrication and is what many top teams do. Buying a *vendor's* purpose-built game solution is what R301 targets. If you ever find yourself ordering someone else's published game mechanism from a fabrication service, stop and file a Q&A question. Log this in your decision record either way.

### 5.7 T5 — In-house CNC router or mill: where the returns die

**[FACT]** Carbide3D list prices, read 2026-08-22: **Shapeoko 4 from $1,800**; **Shapeoko 5.1 Pro 2x2 from $2,980**; **Shapeoko 5.1 Pro from $3,550**; **Shapeoko HDM V3 $5,700**. Each includes the frame/hybrid table, a #201 endmill, Carbide Create CAD/CAM, a dust boot, workholding and a BitSetter. ([shop.carbide3d.com](https://shop.carbide3d.com/collections/cnc-routers)) **[UNVERIFIED]** Third-party aggregators list Onefinity Machinist X-35 at ~$2,399 and Carvera Air at ~$2,499 — not verified on the vendors' own sites this session.

**[JUDGMENT] The honest cost-benefit for a 15-student FTC program:**

| Cost | Reality |
|---|---|
| Machine | $1,800–$5,700 |
| Tooling, workholding, coolant/lube, spare endmills | +$300–$800 first year |
| **Dust collection and a room you are allowed to make noise and chips in** | ⚠️ Often the actual blocker |
| **A trained, insured adult present for every cut** | ⚠️ The real blocker for a mentor-poor program |
| Student hours to learn CAM | 20–60 h before the first good part |

| Benefit | Reality |
|---|---|
| Same-day plate iteration | Genuine, and genuinely valuable in weeks 3–6 |
| Pocketing / weight reduction | Marginal in FTC; you are not weight-limited the way FRC is |
| Custom gearboxes, complex 3-D parts | Rarely needed given COTS gearboxes (§6) |
| "It looks impressive to judges" | ⚠️ **[JUDGMENT] False.** Judges reward *reasoning and process*, not equipment. A cardboard prototype with data beats a milled part without |

⚠️ **[JUDGMENT] Recommendation: do not buy a CNC router this season.** For this program the money is strictly better spent on (in order) a second 3D printer, a practice field, spare motors/servos, and event registration. Revisit T5 only if all three of these become true: you have a dedicated adult, a dedicated room, and you are regularly waiting on outsourced plate.

### 5.8 The recommended fabrication stack for this program

**[JUDGMENT]** Total marginal spend **~$700–$1,100**, on top of parts.

| Tier | Buy | Cost | Priority |
|---|---|---|---|
| T0 | (parts — see `VENDOR-ECOSYSTEMS.md`) | — | — |
| T1 | Full GM0 "necessary" list + **benchtop drill press** + 2 calipers + deburring tools | **$350–$600** | ⭐⭐⭐ First |
| T2 | **Two** printers, ≥220×220 bed, ~$200–$340 each; 5 kg PLA+ (one brand, one colour); 1 kg PETG; heat-set insert kit + soldering iron | **$500–$800** | ⭐⭐⭐ First |
| T3 | Miter saw + non-ferrous blade **only if** you already have a place to use it | $190–$340 | ⭐ Optional |
| T4 | **$0 capital.** Budget ~$150–$400 per season for outsourced plate | operating cost | ⭐⭐ Yes, from G3 onward |
| T5 | — | — | ⛔ Not this season |

---

## 6. The COTS-first doctrine

### 6.1 The buy/build decision rule

**[JUDGMENT]** For every subsystem, ask these four questions in order. The **first "yes" decides**.

| # | Question | If yes → |
|---|---|---|
| 1 | Does a legal COTS part do this job at all? (**R303** single-DoF check) | **BUY.** Do not build a worse version of a solved problem |
| 2 | Does the job depend on the geometry of the SCORING ELEMENT or the FIELD? | **BUILD** — this is where custom wins, because no vendor knows your game |
| 3 | Will we need **two** of these, and can we afford two COTS? | BUY two. F2 duplicability outranks elegance |
| 4 | Is the COTS option a known-bad part in this application? | Build — but only with evidence (see §6.5) |

**[JUDGMENT] The corollary, stated bluntly:** *a small team's custom fabrication budget should be spent almost entirely on the end effector.* Everything between the battery and the end effector is a solved problem that someone will sell you.

### 6.2 Buy vs build, subsystem by subsystem

**[JUDGMENT]** Prices carried from `reference/VENDOR-ECOSYSTEMS.md` (verified 2026-08-21/22) — ⚠️ **re-verify before ordering**.

| Subsystem | Verdict | Why | Anchor products & prices (Aug 2026) |
|---|---|---|---|
| **Drivetrain / chassis** | ⭐ **BUY** | **[C] R301(A)** explicitly exempts *"COTS drive CHASSIS"*. Zero design risk, instantly duplicable, and drivetrain failure is the most expensive failure there is | goBILDA FTC Starter Kit 2026-27 `3200-4008-2627` **$899.99 list / $674.99 with FIRST discount**; REV FTC Starter Kit V3.1 `REV-45-3529` **$695.00**; AndyMark Robits Core Kit **$599–$695** |
| **Wheels** | **BUY** | Compliant/mecanum/omni geometry is not something you can print | goBILDA 96 mm mecanum set **$169.99**; 96 mm omni **$21.99** |
| **Motors + gearboxes** | ⭐ **BUY** | **[C] R303(C)** allows single-speed gearboxes. Nobody should build a planetary gearbox in an FTC season | goBILDA Yellow Jacket `5203`/`5204` **$54.99–$56.99**; REV HD Hex `REV-41-1291` **$22.00** |
| **Servos** | **BUY** | | goBILDA Dual Mode **$36.99**; Proton **$17.99**; 5-turn Dual Mode **$49.99** |
| **Odometry** | ⭐ **BUY** | **[C] R303(J)** explicitly allows *"dead-wheel odometry kits"* despite being 2-DoF. FTC 12527 called goBILDA's 4-Bar/Swingarm *"The best odometry packet we've used!"* | goBILDA Pinpoint + pods — see `reference/mechanisms/DRIVETRAIN-AND-ODOMETRY.md` §7 |
| **Linear slides** | **BUY, but choose deliberately** | **[C] R303(A)** allows linear slide kits. ⚠️ Not all are equal — see §6.5 | goBILDA 2-stage 336 mm Viper `3210-0003-0002` **$159.99**; 4-stage **$229.99**; MISUMI SAR230 + printed inserts (§6.5) |
| **Control system / electronics** | ⭐ **BUY** (mandated) | **[C] R701** names the devices | Control Hub **$375.00**; Driver Hub **$275.00**; Servo Hub `REV-11-1855` **$90.00**; via the FIRST storefront: Electronics Kit **$325**, Driver Kit **$285** |
| **Structure (channel/extrusion)** | **BUY stock, CUT yourself** | **[C] R302** permits modifying raw stock. Cheapest structure per dollar there is | goBILDA `1120` U-Channel bundle `3203-1120-0001` (17 pc) **$219.99**; REV 15 mm extrusion 1 m **$13.50** (Everybot BOM, 2025-26) |
| **Bearings, hubs, shafts, spacers** | ⭐ **BUY, in bulk** | ⚠️ Running out of bearings stops a build night | goBILDA `1601`/`1611` flanged bearings **$3.99–$11.99/2-pk**; pillow blocks `1602`/`1605`/`1606` **$5.99–$14.99**; standoffs bundle **$139.99**, spacers bundle **$46.99** |
| **Power transmission** | **BUY** | | 8 mm chain `3308-0008-1000` **$11.99**; HTD 5 mm starter pack **$209.99**; arc-slot chain tensioner `1524-0001-0001` **$5.99** |
| **⭐ End effector / intake / element-contact geometry** | ⭐⭐ **BUILD** | ⚠️ **This is the only subsystem where custom reliably beats COTS**, because it is the only one shaped by *this season's* SCORING ELEMENT | Print it. See `reference/mechanisms/INTAKE-AND-MANIPULATION.md` |
| **Mounting brackets / adapters / plates** | **BUILD** (print, or outsource-cut) | Nobody sells the bracket between *your* two chosen parts | PLA+ print (§5.4) or Fabworks plate (§5.6) |
| **Hoppers, funnels, guides, ramps** | **BUILD** | Pure geometry, low load, high impact on cycle time | Print, or bend polycarbonate |
| **ROBOT SIGNS** | **BUILD** — 4 of them, in August | **[C] R401/R402**. ⚠️ An inspection item teams make on the morning of the event | FIRST template, US Letter/A4 |

### 6.3 The three things small teams wrongly build

**[JUDGMENT]**

| They build | They should buy | The real cost of building it |
|---|---|---|
| **A custom drivetrain** | A COTS chassis kit | 40–80 student-hours, an unduplicable B robot, and the highest-consequence failure mode on the field. **[C] R301(A) exists precisely to let you buy this** |
| **A custom gearbox** | A Yellow Jacket or UltraPlanetary | Weeks of tolerance chasing to reproduce a $55 part |
| **A custom odometry pod** | A COTS dead-wheel kit | ⚠️ **[C] R303(J)** grants a *specific rules exemption* for odometry kits. Building your own forfeits an exemption FIRST wrote for you |

### 6.4 The three things worth building even when a COTS option exists

**[JUDGMENT]**

1. **Anything that touches the SCORING ELEMENT.** Acceptance geometry, compliance and lead-in are game-specific. This is where §2.5's "widen the tolerance" wins live.
2. **Anything that fixes a known-bad COTS part in your application** — with evidence (§6.5).
3. **Anything that saves an actuator.** A printed passive gate, a one-way flap or a spring-return costs $0.50 and frees a motor or servo slot against the actuator budget. **[JUDGMENT] For a small team this is often the highest-value custom part on the robot.**

### 6.5 Case study — linear slides, and when "buy" needs a caveat

⚠️ This is the clearest published example of COTS-first *with* a caveat, and it is worth reading in full because it shows how to reason about a COTS part rather than reflexively buying or building.

**[FACT]** From a 2025 Chief Delphi thread in the FTC Open Alliance category ("DIY linear slides for FTC"), quoting FTC-experienced posters:

- Pro-COTS: *"linear mechanisms from gobilda are expensive. But honestly worth the investment… we used our original gobilda slides in 3-4 different competitions. With just a few part replacements year to year… Frankly for what it's going to cost you in time(the true currency of FIRST) I would find a way to get the gobilda viper slide."*
- Anti-COTS-aluminium: *"The problem with cots aluminum slides is that their geometry is just bad which makes them weak in both bending axis and torsion which means that anything other than extremely light loads will cause them to wear fast, having inconsistent friction, worse play over time, or just flat out breaking… It is common for teams to need to buy new slides every season due to rapid wear."*
- The stated top-team practice: *"Realistically, I would email Misumi get the [FIRST] discount, buy SAR230's and print inserts. **This is generally the option all of the top bots in the world go**, and is also less expensive than the rest of the options above… Both designs use the REV small bearings and m3 hardware."*
- On goBILDA Viper slides specifically: *"fine, but steel so are very heavy and generally unwieldy compared to other solutions, but work well in that build system."*
- On the cheap path: *"In ages past, people used to use Home Depot drawer slides for this purpose. But you'll still need the stringing and pulley hardware, and likely 3d print a lot of the in-between."*

**[FACT]** MISUMI runs a real, verified program: *"MISUMI's FTC Team 30% Discount is available to all teams in the U.S. or Canada. The discount applies to all stock products and configurable components ordered from the MISUMI USA website using a credit card."* Apply with your team name and number as the company name; the discount *"is usually applied to your account in about two weeks"* and *"will expire on July 31st of the next year."* Contact: `firstrobotics@misumiusa.com`. ([us.misumi-ec.com/service/promotion/first-robotics](https://us.misumi-ec.com/service/promotion/first-robotics/))

**[JUDGMENT] What this case teaches, generalised:**

| Lesson | Application |
|---|---|
| A COTS part can be legal, popular **and** wrong for your load case | Ask "what is the failure mode of this COTS part in *my* application?" before buying |
| The elite answer is often **COTS rail + printed interface**, not COTS-kit or fully-custom | ⭐ This is the T2 sweet spot: buy the precision, print the adapter |
| Vendor discount programs materially change the arithmetic | **⚠️ Apply for the MISUMI 30% discount now** — it takes ~2 weeks to activate, so applying in September means having it in October |
| Time is the true currency | For a team with 15 students and no shop, "it works and I can buy another" often beats "it's 15% better" |

⚠️ **[JUDGMENT] For *this* program, the recommendation is:** apply for the MISUMI discount immediately as insurance, but **default to whichever slide is in stock in your primary ecosystem** unless kickoff reveals a load case that justifies the printed-insert route. Stock-outs, not performance, are the dominant slide risk — `reference/VENDOR-ECOSYSTEMS.md` flags Viper slides as historically the highest stock-out-risk item in FTC.

---

## 7. Reliability-oriented design

⚠️ **Scope note.** This section is about **decisions made in CAD and at the bench**. The match-day failure catalogue, the pit runbook and the reliability-testing programme live in `research/TESTING-AND-TUNING.md` §5–§7. Do not duplicate; read both.

### 7.1 Fastener discipline

**[FACT]** GM0's rules, verbatim where short:

| Rule | GM0's words |
|---|---|
| **Avoid set screws** | *"They slip easily and damage axles."* Prefer *"clamping hubs and collars instead"* |
| **Locknuts only** | Regular nuts loosen under vibration; *"nylon locknuts perform best"* |
| **Threadlocker where set screws are unavoidable** | *"non-permanent threadlocker such as Loctite blue"* |
| **Button head, not socket head, on plastic** | Socket heads damage plastic; use button heads or add washers |
| **Screw length** | Fasteners must not exceed the threaded hole depth, to avoid bottoming out |
| **Threading configuration** | Screws pass through unthreaded holes into threaded ones, or through two unthreaded holes into a nut |
| **Colour-code hex drivers** | Electrical tape to distinguish 2.5 mm from 3 mm — *"the difference between a 2.5mm and a 3mm driver"* is a stripped-screw factory |

**[JUDGMENT] Four additions that are design-time, not build-time, decisions:**

1. **Standardise on one thread size per robot** (M4 for goBILDA structure, M3 for electronics and printed detail). ⚠️ A mixed-thread robot needs twice the tools in the pit and produces the "wrong screw" failure at the worst time. The Everybot ships **hardware size as a CAD configuration** for exactly this reason.
2. **Design for a nylock on every through-bolt.** If a joint physically cannot take a nylock, that is a design defect, not a hardware choice.
3. **Count your fasteners in CAD and buy 3× that number.** `reference/VENDOR-ECOSYSTEMS.md` records the goBILDA M4 screw assortment going **out of stock** — *"Fasteners go out of stock. This is the least glamorous and most disabling stock-out there is."*
4. **Every fastener must be reachable with a straight driver.** Model the driver as a cylinder if you have to. A bolt that needs a ball-end driver at 20° is a bolt that will be left loose.

### 7.2 Wire management and strain relief — as a design decision

**[FACT]** The official FTC Robot Wiring Guide's rules: **strain relief** means *"Immobilize the wire an inch or two from the connector and leave a little slack"*; route wires *"along stationary parts of a robot"* and secure them *"at regular intervals to prevent them from moving or shaking loose during a match"*; create **service loops** for moving components *"to accommodate full extension without tension"*; *"Poorly trimmed zip ties present a sharp point and can be a hazard"*; label wires *"at the point where they plug in"*; and on connectors, verify *"connectors fit snugly together and there is a slight amount of retention."* ([FTC Docs — Robot Wiring Guide](https://ftc-docs.firstinspires.org/en/latest/robot_building/wiring_guide/wiring-guide.html))

**[JUDGMENT] Six things that must happen in CAD, not at 11 p.m. on the bench:**

| Design decision | Consequence of skipping it |
|---|---|
| **Reserve a wire channel** in the layout sketch — a continuous 20–25 mm route from hub to every actuator | Wires end up routed through moving mechanisms |
| **Place the Control Hub so its ports are reachable with the robot assembled.** A public CAD review on Chief Delphi flagged exactly this: *"You might want to consider an access window in the outer plate so you can get to the connectors on the hubs"* | You disassemble the robot to update firmware |
| **Model the service loop** for every wire crossing a moving joint, at both extremes of travel | A slide extends and unplugs a motor mid-match |
| **Design zip-tie anchor points** (printed loops or drilled holes) into brackets, at ~75–100 mm spacing | Wires are taped, then flap, then fail |
| **Keep the battery, switch and the main breaker/fuse reachable** without removing a mechanism — **[C] R603** requires the switch mounted clear of moving parts and protected from contact | Battery swaps take 5 minutes instead of 30 seconds |
| **Trim direction:** design so zip-tie tails point *inward*, away from hands and field elements | **[C] R201** sharp-protrusion risk at inspection |

### 7.3 Service access — the five-minute rule

⚠️ **[JUDGMENT] The rule: every consumable and every failure-prone part must be replaceable in under five minutes, with the robot on the cart, using one tool.** Check this **in CAD** at G3 by asking, for each item below, "which parts must come off first?"

| Item | Target | Design implication |
|---|---|---|
| Battery | **<30 s** | Top or side access, one strap or one latch. Never under a mechanism |
| Any drive motor | **<10 min** | Motor removable without removing wheels or the opposite side |
| Any servo | **<5 min** | ⚠️ Servos are the most-replaced actuator in FTC. Design the horn interface so a swap does not need re-machining |
| A printed bracket | **<5 min** | Bolted, not sandwiched between two other bolted parts |
| Control Hub USB + ports | **<10 s** | An access window; see §7.2 |
| Odometry pod | **<5 min** | ⚠️ And it must return to a **repeatable position** — use dowel pins or a hard shoulder, not just bolt clearance, or auto is wrong afterwards |
| Wheel / tread | **<10 min** | ⚠️ Swapping an identical wheel does not require re-inspection (**I303.E**) — design so it is fast |

### 7.4 Modularity for the pit

**[JUDGMENT]** The unit of repair in a pit is not a part; it is a **module**. Design the robot so a failed subsystem can be swapped whole while the drive team goes to the queue.

| Practice | Detail |
|---|---|
| **Define module boundaries in CAD** | A module = a subassembly attached by ≤6 bolts and ≤3 connectors |
| **Bring a spare *module*, not spare parts,** for the highest-risk subsystem | ⚠️ For a two-robot program the B robot's subsystem is often the A robot's spare module — **this is the strongest practical argument for making the B robot a configuration, not a fork (§4.8)** |
| **Keyed/pinned interfaces** | A module that can only go back one way cannot go back wrong under time pressure |
| **Connectors, not solder joints, at module boundaries** | |
| **One tool per module** | If the intake needs a 2.5 mm hex and nothing else, a student can do it alone |
| **Photo of the assembled module taped inside the pit toolbox** | Removes "which way round" from a 6-minute turnaround |

### 7.5 Tolerance and fit

**[JUDGMENT]** Starting values for a printer + drill press shop. ⚠️ **Calibrate them yourself** — CoreFTC is explicit that *"a tight fit on one printer may be a thru-hole on another"* and recommends printing test coupons.

| Fit | Nominal | Notes |
|---|---|---|
| M3 clearance hole, printed | 3.3–3.4 mm | Below 3.2 mm you will be drilling every hole out by hand |
| M4 clearance hole, printed | 4.3–4.5 mm | |
| Heat-set insert boss (M3) | per insert spec, typically 4.0–4.2 mm | ⭐ Preferred over printed threads, always |
| Bearing press fit, printed | −0.05 to −0.10 mm on the OD | Then chamfer the lead-in 0.5 mm × 45° |
| Shaft clearance, printed | +0.20–0.30 mm | Never run a shaft directly on plastic on a load path (§5.4.5) |
| Sliding fit (guides, tracks) | +0.30–0.50 mm | Plus a wipe of dry lubricant. ⚠️ **[C] R201** warns against *"excessive use of lubricants that may spin off or drip"* |
| Mating printed parts (dowel/boss) | +0.15 mm | |
| Hole in aluminium for M4 clearance | 4.5 mm (or 4.7 mm) | Drill on a press; deburr both sides |

**[JUDGMENT] Two habits worth more than any table:**

- ⭐ **Print a tolerance test coupon per printer per filament brand**, once, and tape the results to the printer. This is a 3-hour investment that removes a season of fit surprises.
- ⭐ **Design in adjustment.** Slots instead of holes on one side of a belt or chain path; a shim stack under a motor mount; an arc-slot tensioner (goBILDA `1524-0001-0001`, **$5.99**). ⚠️ *Adjustability is the cheapest substitute for precision*, and a shop without a mill should buy it everywhere it can.

### 7.6 Mechanisms that historically fail in FTC matches

**[FACT]/[JUDGMENT]** Distilled from `research/TESTING-AND-TUNING.md` §6, GM0, and the public build threads read this session. ⚠️ **The full field-fix table lives in TESTING-AND-TUNING.md §6 — this is the design-time prevention view only.**

| Mechanism | Historic failure | ⭐ Design-time prevention |
|---|---|---|
| **Set-screw wheel/pulley hubs** | Backs out; motor spins, wheel does not | Clamping hubs (GM0's explicit advice); if a set screw is unavoidable, use the shaft flat + Loctite blue |
| **Chain with a master link** | Master links are *"not very reliable"* (GM0) | Design for a continuous chain; own a chain breaker; design in a tensioner |
| **Belts without a tensioner** | Skips teeth; positional drift | Tensioner or adjustable centre distance designed in, never added later |
| **COTS aluminium linear slides under side load** | Wears, develops play, then breaks (§6.5) | Load the slide in its strong axis; add a second guided point; consider MISUMI + printed inserts |
| **Servos** | Stripped gears; drift; stall burnout | ⚠️ Software endpoints **inside** the mechanical endpoints; never rest a servo against a hard stop; design the horn for a 5-minute swap |
| **Intake compliant wheel on its hub** | Spins on the hub; "sometimes works" | Clamping hub or a keyed printed adapter, plus threadlocker |
| **Odometry pods** | Knocked out of alignment by contact; drift worsens over an event | Rigid, *protected* mounts; repeatable location (§7.3); shield behind structure |
| **Printed parts in the Z direction** | Snaps along a layer under a shock load | §5.4.4 orientation; fillets; spare set printed |
| **Anything cantilevered on one bearing** | Shaft deflects; binds; wears the bore. Public CAD review of an FTC robot flagged exactly this: *"you might want to consider supporting the end of the shaft so they don't sag under the weight of the robot"* | ⭐ Support shafts on both sides; plates on both sides of a bearing stack |
| **Wires crossing a moving joint** | Unplugs or breaks mid-match | Service loops modelled at both travel extremes (§7.2) |
| **Stored energy (springs, elastic)** | Surprises an inspector; releases unexpectedly | ⚠️ **[C]** Section 3.3.1 asks teams to **tell inspectors** about stored energy. Design a safe, visible retention state |
| **Mechanisms that trap the robot on the field** | Cannot be removed powered off — **[C] R203** | Model the unpowered rest state and check a human can lift the robot clear |
| **Exposed sharp edges** | **[C] R201** inspection failure | Chamfer/fillet pass on every custom part in CAD; cap exposed screw ends |

### 7.7 The reliability checklist to run at G3 (in CAD, before you order)

**[JUDGMENT]** Twelve questions. Any "no" is a design change, not a note.

1. Does the STARTING CONFIGURATION fit an 18 in cube, fully stationary and self-contained? **[C] R102**
2. Can a human remove the robot from the FIELD with power off? **[C] R203**
3. Is every custom part filleted/chamfered, with no exposed thread ends? **[C] R201/R202**
4. Are there **two** ROBOT SIGN locations reserved, on opposite or adjacent surfaces? **[C] R401**
5. Is every fastener reachable with a straight driver?
6. Is the battery swappable in under 30 seconds?
7. Are the Control Hub ports reachable with the robot assembled?
8. Does every wire crossing a moving joint have a modelled service loop at both extremes?
9. Is every printed part oriented so its principal load runs along the layers?
10. Is there a spare set of printed parts in the print queue?
11. Can the highest-risk module be swapped in under 10 minutes with one tool?
12. Can we build **two** of this robot from this BOM? (F2 duplicability)

---

## 8. Design documentation — making the portfolio write itself

### 8.1 The principle

⚠️ **[JUDGMENT] The portfolio is not a writing project. It is a *retrieval* project.** Teams that struggle in January are not bad writers — they are teams whose decisions were never recorded and therefore cannot be retrieved. Teams that do well captured evidence at the moment of the decision, at a cost of about 90 seconds each time, and spent January selecting and laying out.

**[FACT]** The judging window is long: `research/SMALL-TEAM-ECONOMICS.md` records that judging season starts **1 January 2026** for this cycle, meaning work completed months earlier is portfolio-eligible. **[FACT]** `research/AI-IN-FTC-POLICY.md` records that BIOBUZZ rule **A201** permits AI assistance in composing the portfolio with a footnote/endnote credit and respect for IP.

**[FACT]** Elite teams treat the *design record itself* as the deliverable: FTC 23511 explicitly tell readers to *"see version history/branches as well"* on both their robot CAD and their **separate prototype CAD document** — their Onshape version history *is* their design log.

### 8.2 The capture table — what, when, where

**[JUDGMENT]** Set this up in the first week and never think about it again.

| Artifact | Captured when | By whom | Cost | Feeds |
|---|---|---|---|---|
| **Will List** (§2.3), dated | Kickoff Sunday | Design lead | 45 min | Portfolio "design process"; judge interview opener |
| **Ranked capability table** (§2.2) | Kickoff Sunday | Strategy lead | 90 min | "Why we built this robot" — the single most-asked judge question |
| **Concept sketches**, photographed | End of each concept session | Whoever sketched | 30 s | Shows divergence — judges look for it |
| ⭐ **Prototype test card** (§3.3): question, variable, levels, measure, kill criterion, result | At the test | Prototype owner | 5 min | Engineering *analysis* evidence, the rarest thing in FTC portfolios |
| ⭐ **Slow-motion video of every prototype**, named `YYYY-MM-DD_subsystem_vN` | At the test | Anyone | 30 s | Reveal video, portfolio, and your own debugging |
| ⭐ **Autopsy note for every killed concept** (§3.4) | At the kill | Concept owner | 5 min | ⚠️ Judges reward *what you rejected and why* more than what you built |
| **Decision record** (§8.3) | At every gate and every non-obvious choice | Design lead | 90 s | The spine of the portfolio |
| **Weekly CAD snapshot**: Onshape Version + STEP + dated render | Every Friday | CAD lead | 5 min | Visual progression, which is a portfolio layout staple |
| **BOM with part numbers**, exported from Onshape | At each order | BOM owner | 0 (automatic if §4.9 followed) | Cost analysis; sustainability narrative |
| **Photo of every subassembly before it is enclosed** | At assembly | Builder | 30 s | You will need it for the pit and for the portfolio |
| **Match/practice reliability log** | Every practice session | Drive coach | — | Owned by `TESTING-AND-TUNING.md` §5 |

### 8.3 The decision record — the 90-second template

**[JUDGMENT]** One per non-obvious decision. Six lines. Paste into a running Markdown file in the repo, or a shared doc — **but keep it in one place, in date order**.

```
## DR-014  2026-10-11  Intake: printed claw over compliant roller
Decision:   Claw with 3D-printed compliant fingers, single servo.
Alternatives: (a) dual compliant roller  (b) surgical-tubing flail  (c) funnel + gravity
Why:        Roller measured 11/20 acquisitions at 2 in misalignment; claw measured
            18/20 at 3 in.  Roller also needed a 9th actuator (over budget).
Evidence:   video 2026-10-11_intake_rollerV2.mp4, 2026-10-11_intake_clawV1.mp4;
            test card TC-009.
Cost:       claw $6 filament vs roller $58 (motor) + $18 (wheels).
Revisit if: element compressibility differs at the practice field, or claw
            cycle time exceeds 1.4 s in integrated testing.
```

⚠️ **[JUDGMENT] The "Revisit if" line is the one that pays off.** It converts a decision from a commitment into a hypothesis with a trigger, which is exactly the framing judges are trained to reward — and it makes reversing a decision in week 6 a planned event rather than an admission of failure.

### 8.4 The ten-minute end-of-meeting ritual

**[JUDGMENT]** Non-negotiable. Last ten minutes of every build session, run by a rotating student:

| Minutes | Action |
|---|---|
| 0–3 | **Photos.** Every subsystem touched today, plus one wide shot of the robot |
| 3–6 | **Decision records** for anything decided today (§8.3) |
| 6–8 | **CAD/robot divergence check.** Anything changed on the robot but not in CAD → logged as a task, due within 48 h (§4.12) |
| 8–10 | **Tomorrow's one thing.** Written on the board, so the next session starts in 30 seconds instead of 30 minutes |

### 8.5 What this produces by January

**[DERIVED]** At ~2 build sessions per week from mid-September to the end of December (~15 weeks × 2 = 30 sessions), the ritual above yields roughly:

| Artifact | Count |
|---|---|
| Dated photos | 200–400 |
| Decision records | 25–50 |
| Prototype test cards | 15–30 |
| Autopsy notes | 5–15 |
| Weekly CAD snapshots + renders | ~15 |
| Slow-motion videos | 30–80 |

**[JUDGMENT]** That is a portfolio's entire raw material, gathered at a marginal cost of about **five hours across the whole season**. Award mapping — which award wants which evidence — is `research/SCOUTING-AND-AWARDS.md` §7 and `reference/AWARD-ALIGNMENT-MATRIX.md`. This file's only job is to make sure the evidence exists.

---

## 9. AI integration (Claude Code) across design and CAD

⚠️ **Read `research/AI-IN-FTC-POLICY.md` first.** Its bottom line: FIRST's position is *"unusually permissive, explicitly pro-AI"*; rule **A201** permits AI in the portfolio with a footnote/endnote credit; the judge-facing guidance calls AI in robot code *"permitted and encouraged"*; and **the real gate is student comprehension in the interview, not tool restriction**. ⚠️ That document logs **AI-generated CAD as GREY AREA 1** — there is no explicit FIRST guidance on it either way.

### 9.1 The rule this section is written under

**[JUDGMENT]** *AI should increase the number of hours students spend with their hands on hardware, and decrease the number of hours students spend on retrieval, transcription and boilerplate.* Any AI use that moves in the opposite direction — that has an LLM design a mechanism a student cannot explain — fails both the interview test and the point of the program.

| ✅ Use AI for | ⛔ Do not use AI for |
|---|---|
| Retrieval: "which R-rule governs COTS gearboxes?" | Generating a mechanism concept the students then adopt without testing |
| Arithmetic: cycle-time tables, gear ratios, BOM rollups, points-per-second models | Producing portfolio prose no student can defend |
| Transcription: turning a photographed whiteboard into a decision record | Making the buy/build call |
| Generating **FeatureScript** for a repetitive CAD operation the students specify | Replacing physical prototyping with a plausible-sounding answer |
| Drafting checklists, cut lists, test cards, print queues | Anything a judge could ask about that no student could answer |

### 9.2 The tooling that exists today

**[FACT]** **Onshape Labs publishes an official FeatureScript MCP Server** that *"connect[s] AI clients such as Claude, ChatGPT, or Gemini directly to FeatureScript,"* letting a user describe a custom feature in natural language and get generated FeatureScript back. Setup: an active Onshape account, subscribe through the **Onshape App Store**, then configure the AI client with **URL `https://fs-mcp.labs.onshape.app/mcp`, transport HTTP**. It is framed as generating *"reusable, editable, parametric CAD tools without programming expertise"* — i.e. **the AI writes the code that defines the geometry**, not the geometry itself. It is in **Onshape Labs**, an *"early-access program for emerging technologies."* ([Onshape blog](https://www.onshape.com/en/blog/featurescript-mcp-server-enables-text-code-cad)) ⚠️ Probing `https://fs-mcp.labs.onshape.app/mcp` on 2026-08-22 returned **HTTP 401** — as expected for an authenticated endpoint, but confirming it exists and requires a subscription.

**[FACT]** Community MCP servers exposing the Onshape REST API also exist, including [github.com/altendky/onshape-mcp](https://github.com/altendky/onshape-mcp), [github.com/hedless/onshape-mcp](https://github.com/hedless/onshape-mcp), and a Claude Code plugin at [github.com/ReshefElisha/jarvis-onshape-mcp](https://github.com/ReshefElisha/jarvis-onshape-mcp). ⚠️ **[UNVERIFIED]** — I did not evaluate the code, security or maintenance status of any of these. **[JUDGMENT] Do not connect an unaudited third-party MCP server to an account holding your team's design work.** Prefer the official Onshape Labs server.

### 9.3 Concrete jobs to hand Claude Code this season

**[JUDGMENT]** Each of these returns student time to the bench.

| Job | What you give it | What comes back | Hours saved/season **[JUDGMENT]** |
|---|---|---|---|
| **Kickoff rule diff** | The V0 manual text + the Kickoff manual text (both local) | A table of every changed R-rule and every new game rule, cited by line | 3–6 |
| **Cycle-time model** | The scoring table + measured phase times | The §2.2/§2.5 tables, computed and sensitivity-tested | 4–8 |
| **BOM reconciliation** | Onshape BOM export + `reference/VENDOR-ECOSYSTEMS.md` | Missing parts, price deltas, stock-out risks, a purchase order draft | 4–10 |
| **Cut list → shop sheet** | Measure Cut List output | A printable per-stock cutting plan with kerf allowance, batched for two robots | 2–4 |
| **Print queue** | The list of printed parts + quantities + printer beds | A packed plate-by-plate queue with settings per part | 2–5 |
| **FeatureScript generation** | "A feature that makes a gusset from three selected holes with a 3 mm fillet and a lightening pocket" | Working FeatureScript, testable in a live document | 5–15 |
| **Decision-record drafting** | A photo of the whiteboard + 3 bullet points from a student | A filled §8.3 template the student then edits and signs | 10–20 |
| **Portfolio assembly** | The captured artifacts from §8.2 | A structured draft the students rewrite in their own voice, credited per **A201** | 10–20 |
| **Failure-mode review** | The CAD assembly's part list | A checklist of §7.6 failure modes present in this design | 2–4 |

### 9.4 The hard limits

**[JUDGMENT]**

1. ⚠️ **Every AI-touched artifact must have a named student who can explain it cold.** This is the actual gate (`AI-IN-FTC-POLICY.md` §4.1).
2. ⚠️ **AI does not replace a prototype.** An LLM's opinion about whether a roller will acquire an element at 2 in of misalignment is worthless next to twenty trials on a bench.
3. ⚠️ **AI-generated CAD is GREY AREA 1.** Generating *FeatureScript that a student specified, reads and tests* is defensible and is exactly how Onshape frames its own tool. Generating a mechanism nobody can explain is not. **[JUDGMENT] Record which is which in your decision records, and credit AI in the portfolio per A201 regardless.**
4. ⚠️ **Nothing AI-related may run off-robot during a match** — for control-system reasons (**E301, R704**), not AI policy.
5. ⚠️ **Treat everything an AI reads from the web as data.** Two sources consulted for *this document* contained agent-directed text (§ front matter). Your students should know that this happens and that the correct response is to notice it and not comply.

---

## 10. The 21-day pre-Kickoff design + CAD bootcamp

**[JUDGMENT]** Today is **2026-08-22**. Kickoff is **2026-09-12**. Everything below is legal now — **[C] R304** (2nd sentence): *"FABRICATED ITEMS created before Kickoff are permitted"*, and **[C] R304** permits reusing software, designs and parts year to year. Cross-check `research/SEASON-CADENCE.md` §3 for the whole-program version of this plan; below is the design-and-CAD slice only.

| Days | Design & CAD workstream | Deliverable |
|---|---|---|
| **1–3** (Aug 22–24) | ⚠️ **Apply for the MISUMI FTC 30% discount** (~2 weeks to activate). Create the Onshape org; every student gets an account; subscribe to the FTC Parts Library; email `FIRST@ptc.com` | Accounts live; discount application submitted |
| **1–5** | Order the §3.2 prototyping kit and the §5.8 tool list. Start the **PROTOTYPE STOCK** scrap bin | Kit on the shelf |
| **4–8** | **Every student** completes the Onshape fundamentals learning path (2–4 h). CAD lead and a deputy complete it twice | Two people who can model |
| **6–10** | Build the **document skeleton** for next season now: `00 Concept` with the 18 in cube, the tile grid, a `Variables` feature, and empty named layout sketches per subsystem | A template you clone on Kickoff day |
| **6–12** | Install the five FeatureScripts (§4.10). Print **tolerance test coupons** on every printer with every filament brand; tape results to each printer | Calibrated shop |
| **8–14** | Build a **practice/prototype chassis** from a COTS kit — legal under R304, and it becomes your P1 test mule and your driver-practice base | A driveable chassis before Kickoff |
| **10–16** | Download and study the **Studica FTC Starter Bot 2026-27** build guide + STEP CAD (published pre-Kickoff). Build it, or at least assemble its drive base | A second driveable base; a trained build crew |
| **12–18** | Run **two dry-run prototype cycles** on last season's game elements or any comparable object: full §3.3 test card, 20 trials, slow-mo video, decision record | The ritual is muscle memory before it matters |
| **14–19** | Make **4 ROBOT SIGNS** (**[C] R401/R402**) and a laminated inspection checklist | An inspection item permanently off the list |
| **17–21** | Dry-run the whole Kickoff-day pipeline (§11) on a *prior season's* scoring table. Time each stage | A rehearsed team |
| **21** (Sep 11) | Print blank Will List / capability-table / test-card forms. Charge everything. Sleep | Ready |

⚠️ **[JUDGMENT] The single highest-value item on that list is the dry run on days 17–21.** A team that has rehearsed S1→S4 on a prior season's scoring table will finish it on Kickoff Sunday. A team that has not will still be arguing on Wednesday.

---

## 11. Kickoff weekend — the design-side playbook

**[JUDGMENT]** The design-and-CAD slice only. The full weekend plan, including logistics, is `research/SEASON-CADENCE.md` §4.

| When | Activity | Output | Owner |
|---|---|---|---|
| **Sat AM** | Watch the reveal. Run `tools/ingest-manual.sh`. Transcribe the scoring table into a spreadsheet — **by hand, by a student**, then verify with AI | Machine-readable scoring table | Strategy lead |
| **Sat AM** | Diff the R-rules against V0 (§9.3 job 1) | Rule-delta table | Rules lead + AI |
| **Sat PM** | ⭐ **Touch the game elements.** Weigh them, measure them, compress them, roll them, drop them. Write down numbers | Element characterisation sheet | Everyone |
| **Sat PM** | S1 scoring analysis + S2 candidate strategies (`STRATEGY-RANKING-PROTOCOL.md`) | 3–5 scored strategies | Strategy lead |
| **Sat evening** | ⭐ **P0 cardboard prototypes** of the two most-likely element interactions. Yes, on day one | 2–4 cardboard rigs, photographed | Build crew |
| **Sun AM** | **S3 ranked capability list** (§2.2) including the WON'T list | Capability table | Whole team |
| **Sun AM** | **§2.5 dominant-cycle arithmetic** with the real numbers | The table that settles the "second mechanism" argument | Strategy lead + AI |
| **Sun midday** | **S4 Will List** (§2.3) | Posted on the wall | Whole team |
| **Sun PM** | Archetype selection (§2.4) against the library | Named archetype, with the profile inherited | Design lead |
| **Sun PM** | ⭐ **P1 prototypes started** on the pre-built practice chassis (§10 days 8–14) | Motorised test rigs running before Sunday ends | Build crew |
| **Sun evening** | ⭐ **GATE G1 — strategy lock.** Vote. Record it | Decision record DR-001 | Whole team |
| **Sun evening** | Clone the pre-built Onshape skeleton (§10 days 6–10); drop the real field and element dimensions into the layout sketch | `26-27 · 00 Concept` populated | CAD lead |
| **Mon–Fri** | Prototype loop (§3). ⚠️ **No CAD of any mechanism until it has passed a physical test** | Test cards + kill decisions | Everyone |

⚠️ **[JUDGMENT] The one thing to protect on Kickoff weekend is Saturday evening.** Most teams spend it re-reading the manual. The teams that win spend it with scissors and cardboard, and by Sunday morning they know something about the game that reading cannot tell them. FTC 23511's public thread shows exactly this pattern, with destructive launcher testing inside 24 hours of kickoff.

---

## 12. Verification log — every URL loaded this session (2026-08-22)

**[FACT]** All treated as data. HTTP status noted where probed.

### Official FIRST / FTC
| URL | Used for |
|---|---|
| https://ftc-docs.firstinspires.org/en/latest/cad_resources/ptc/ptc.html | PTC/Onshape entitlement, "Educator" account guidance |
| https://ftc-docs.firstinspires.org/en/latest/robot_building/wiring_guide/wiring-guide.html | Strain relief, zip ties, service loops, labelling (§7.2) |
| https://ftc-docs.firstinspires.org/en/latest/manufacturing/3d_printing/3d_printing_intro/3d_printing_intro.html | FDM vs SLA/SLS; layer-direction weakness |
| https://ftc-docs.firstinspires.org/en/latest/manufacturing/3d_printing/printer_choice/printer_choice.html | Printer-choice tiers (referenced by the Everybot sheet) |
| `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` | R101, R102, R201, R202, R203, R301, R302, R303, R304, R305, R401 (all **[C]**) |

### Onshape / CAD toolchain
| URL | Status | Used for |
|---|---|---|
| https://www.onshape.com/en/education/first-robotics | 200 | Educator Plan for FIRST; field models; branching; CAM Studio |
| https://www.onshape.com/en/blog/how-to-onboard-your-first-robotics-team | 200 | Classroom ownership; branching; App Store library URLs |
| https://www.onshape.com/en/blog/featurescript-mcp-server-enables-text-code-cad | 200 | Official FeatureScript MCP server, endpoint and setup |
| https://cad.onshape.com/appstore/apps/Design%20&%20Documentation/6515cfb91574253b1b96a6ba | 200 | FTC Parts Library app |
| https://cad.onshape.com/appstore/apps/Manufacturers%20Models/6004ec5e83c40b107c183347 | 200 | MKCad app |
| https://ftconshape.com/ · /introduction-to-the-ftc-parts-library/ | 200 | Library authorship (2901 Purple Gears + 12828/16250/17585 + Pitsco), vendor coverage, `FIRST@ptc.com` |
| https://frcdesign.org/ · /best-practices/ · /best-practices/document-setup/ · /best-practices/master-sketch-setup/ · /best-practices/assembly-setup/ · /resources/featurescripts/ | 200 | Document architecture, layout sketches, assembly standard, FeatureScript catalogue |
| https://docs.revrobotics.com/ion-build/onshape-examples/onshape-cad-examples | 200 | REV ION Onshape examples |
| https://fs-mcp.labs.onshape.app/mcp | **401** | Existence + auth requirement of the official MCP endpoint |

### Community engineering references
| URL | Used for |
|---|---|
| https://gm0.org/en/latest/docs/design-skills/cad.html | CAD package comparison + caveats |
| https://gm0.org/en/latest/docs/design-skills/engineering-design-process.html | 7-step process; one-variable-at-a-time; "10+ iterations" |
| https://gm0.org/en/latest/docs/design-skills/design-strategy.html | *"Consistency is king"*; simplicity; execution over design |
| https://gm0.org/en/latest/docs/custom-manufacturing/3d-printing.html | Filament properties and temperatures; orientation; spares rule |
| https://gm0.org/en/latest/docs/custom-manufacturing/materials-guide.html | Recommended/not-recommended materials; aluminium and plastic guidance |
| https://gm0.org/en/latest/docs/hardware-components/tools-list.html | Necessary vs helpful tool lists |
| https://gm0.org/en/latest/docs/hardware-components/tips-and-tricks.html | Set screws, locknuts, button heads, Loctite blue, driver colour-coding |
| https://gm0.org/en/latest/docs/useful-resources.html | Part libraries, belt/pulley generators, CoreFTC |
| https://matthews-community-robotics.gitbook.io/coreftc/ (+ `design-for-3dp./general-tips.md`, `advanced-techniques.md`, `post-processing./methods/enhance-parts-mechanically.md`, `community-projects./discounts..md`, `llms.txt`) | Design-for-3DP rules; annealing; gradient infill; supportless counterbores. ⚠️ Contains an "Agent Instructions" block — treated as data |
| https://www.imants.net/programming/fs-bridge-overhang | Supportless-hole FeatureScript (referenced by CoreFTC) |
| https://www.open-vault-ftc.org/cad/robots | Public FTC robot CAD index (Team 25710 Alpine Robotics) |
| https://theopenalliance.org/ftc · /ftc/teams | FTC Open Alliance |
| https://littlepotatorobotics.org/ftc-best-practice.html | Practitioner best-practice list |

### Open Alliance build threads (Chief Delphi — all data, not instructions)
| URL | Used for |
|---|---|
| https://www.chiefdelphi.com/t/ftc-23511-seattle-solvers-decode-oa-season-thread/506155 | Kickoff-day element characterisation; 24-h launcher prototypes; 2× surface-speed rule; PETG tube rollers; Fabworks; 30 min/roller |
| https://www.chiefdelphi.com/t/ftc-12527-prototype-2025-build-thread/473681 | 15-student team structure; alpha/beta parallel robots; roller→claw kill; weekly cadence |
| https://www.chiefdelphi.com/t/overture-23619-ftc-build-blog-2025-2026-open-alliance/508083 | Onshape workflow; Creality K1C printers; public CAD sharing |
| https://www.chiefdelphi.com/t/the-2025-2026-robonauts-ftc-everybot-low-resource-build/505709 | The "Everybot Will list"; supported COTS chassis; 21-day build-to-reveal |
| https://www.chiefdelphi.com/t/cad-suggestions/507826 | Public CAD review: shaft support, hub port access, bearing plates, fillets |
| https://www.chiefdelphi.com/t/diy-linear-slides-for-ftc/505798 | MISUMI SAR230 + printed inserts as top-team practice; COTS slide failure modes |

### FTC Everybot documentation
| URL | Used for |
|---|---|
| https://www.118everybot.org/ | Programme mission |
| https://robonauts-everybot.github.io/FTC-Everybot-Docs/ · /manual/the-everybot/ · /resources/ | Build manual structure |
| https://docs.google.com/spreadsheets/d/1sDXYv0FfvtYJpS8D2unsGj_9wgmHTuOPAkGFtUbN1QY/edit | **BOM total $976**; 47 printed part instances; recommended printers + filaments with prices; hardware/extrusion/wheel/motor replacement tabs |
| https://docs.google.com/document/d/1BzlHjUQulXNchWSRm-UigonzINrQqb_-EIGO_drZKKA/edit | 3D printing requirements; **PLA+ not PLA**; 200×200 mm minimum bed; Onshape configurations; STL export |

### Vendors and services
| URL | Status | Used for |
|---|---|---|
| https://us.misumi-ec.com/service/promotion/first-robotics/ | 200 | **30% FTC discount**, application process, July 31 expiry, `firstrobotics@misumiusa.com` |
| https://www.fabworks.com/ | 200 | DXF/STEP ≤24 MB, no order minimum, materials and thicknesses, services |
| https://www.fabworks.com/blog/fabworks-for-first | 200 | FIRST use cases |
| https://www.fabworks.com/first-50 | **404** | ⚠️ The claimed "50% off first order" page does not resolve — discount **[UNVERIFIED]** |
| https://www.oshcut.com/ · https://sendcutsend.com/ | 200 | Alternative laser services |
| https://shop.carbide3d.com/collections/cnc-routers | 200 | **Shapeoko 4 $1,800 · 5.1 Pro 2x2 $2,980 · 5.1 Pro $3,550 · HDM V3 $5,700** |
| https://us.store.bambulab.com/products/p1s · /a1 | 200 | Price fields observed; ⚠️ variant mapping **[UNVERIFIED]** |
| https://www.studica.com/ftc-starter-bot-resource-guide-2026-2027 | 200 | Pre-Kickoff 2026-27 Starter Bot: build guide PDF, STEP CAD, wiring diagram; season named FIRST CANOPY |
| https://www.revrobotics.com/15mm-extrusion-1m/ etc. | (via Everybot BOM) | REV part prices, 2025-26 vintage |

---

## 13. Open questions / NEEDS-CHECK register

| # | Item | Status | Action, and by when |
|---|---|---|---|
| 1 | **BIOBUZZ field CAD model in Onshape** | Not published; only the 2026/DECODE model is linked from Onshape's FIRST page | Check Onshape's FIRST page and `ftc-resources.firstinspires.org/ftc/archive/2027/field` on **Kickoff day** |
| 2 | **2026-27 official StarterBot** (**[C] R301(B)** makes its mechanisms legal COTS MAJOR MECHANISMS) | Studica pre-Kickoff guide is live; *"full Starter Kit will be officially revealed at FTC Kickoff"* | Read the full StarterBot release the day it publishes. ⚠️ Potentially a large lever |
| 3 | **Fabworks FIRST discount** | ⚠️ `fabworks.com/first-50` returned **404**; third-party claims of 50%/$200 and 5% codes are **[UNVERIFIED]** | Email Fabworks before assuming any discount |
| 4 | **Bambu Lab current prices** | Price fields seen but variants not confidently mapped | Re-check us.store.bambulab.com before ordering |
| 5 | **Everybot BOM prices** | 2025-26 vintage; Control Hub listed at $350 vs $375 verified Aug 2026 | Re-quote every line; use `VENDOR-ECOSYSTEMS.md` as the price source of truth |
| 6 | **MISUMI discount lead time** | *"about two weeks"* to activate; expires **July 31** of the following year | ⚠️ **Apply in the next three days** even if you may not use it |
| 7 | **Outsourced fabrication vs R101/R301 spirit** | **[JUDGMENT]** Sending your own design to a general-purpose cutter is ordinary fabrication; R301's "build to print" language targets vendors selling purpose-built *game solutions* | If you ever consider ordering another party's published game mechanism from a fab service, file an official Q&A question first |
| 8 | **CNC in-house prices beyond Carbide3D** | Onefinity/Carvera figures came from aggregator sites, **[UNVERIFIED]** | Only relevant if §5.7's three preconditions are met — i.e. probably never this season |
| 9 | **Community Onshape MCP servers** | Exist; **[UNVERIFIED]** for security/maintenance | ⚠️ Prefer the official Onshape Labs server; do not connect unaudited MCP servers to team accounts |
| 10 | **Slicer wall/infill recommendations (§5.4.4)** | ⚠️ **[JUDGMENT]**, not sourced. Only the 0.2 mm layer height is sourced | Validate with your own printed test parts in the pre-Kickoff window |
| 11 | **Actuator-count limits** | Referenced from `reference/mechanisms/ELECTRONICS-AND-SENSING.md` rather than re-derived here | Confirm against Section 12 before the Will List is finalised |
| 12 | **AI-generated CAD** | **GREY AREA 1** in `research/AI-IN-FTC-POLICY.md`; no explicit FIRST guidance | Follow §9.4; credit AI per A201; re-check the 2026-27 Judging Process Guide when it publishes |

---

**End of file.** Companion reading, in the order it becomes useful: `reference/STRATEGY-RANKING-PROTOCOL.md` → **this file §2** → `reference/ROBOT-ARCHETYPE-LIBRARY.md` → `reference/mechanisms/*.md` → **this file §3–§5** → `reference/BOM-PROTOCOL.md` → `reference/VENDOR-ECOSYSTEMS.md` → **this file §7** → `research/TESTING-AND-TUNING.md`.
