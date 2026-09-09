# TESTING AND TUNING — Turning a Built Robot Into a Winning One
### FTC 2026-27 BIOBUZZ presented by RTX · small-team edition
**Written 2026-08-21 · kickoff is 2026-09-12 · you have 22 days before the game is public**

---

## How to read this document

| Label | Meaning |
|---|---|
| **[FACT — LOCAL]** | Taken from a file in this workspace. Path given. |
| **[FACT — WEB]** | Taken from a cited URL, accessed 2026-08-21. |
| **[JUDGMENT]** | My recommendation. Argued, not sourced. Disagree freely. |
| **[UNVERIFIED]** | I could not confirm it. Do not spend money or schedule on it until you do. |
| ⚠️ | A trap that costs teams matches or inspection passes. |

**Every price is "as of August 2026" and must be re-checked before you order.** Vendors change prices mid-season, and the 2026-27 pre-order window at AndyMark already closed on 7 August 2026.

**Scope boundary.** This document covers *the loop between "the robot exists" and "the robot wins"*: practice surfaces, drive practice, measurement, reliability, failure modes, and event-day operations. Sibling documents in this workspace cover adjacent ground and are not repeated here:

| For… | Read |
|---|---|
| Control-loop tuning, PIDF, localization, logging code, Dashboard/Panels legality | `research/PROGRAMMING-PRACTICE.md` §6, §7.7 |
| Budget tiers, what to buy, grants | `research/SMALL-TEAM-ECONOMICS.md` §1.3, §1.5 |
| Week-by-week season plan, meeting cadence, dress rehearsal | `research/SEASON-CADENCE.md` §8 |
| Match scouting, alliance selection, award strategy | `research/SCOUTING-AND-AWARDS.md` |
| Rule taxonomy, R-rule detail, penalties | `reference/CONSTRUCTION-RULES-R.md`, `reference/PENALTY-AND-ENFORCEMENT.md` |

---

## Contents

1. [Executive summary — the twelve things that actually matter](#1-executive-summary--the-twelve-things-that-actually-matter)
2. [The practice field problem](#2-the-practice-field-problem)
3. [Drive practice](#3-drive-practice)
4. [Data-driven tuning: measuring what you are actually bad at](#4-data-driven-tuning-measuring-what-you-are-actually-bad-at)
5. [Reliability engineering](#5-reliability-engineering)
6. [Failure-mode catalogue](#6-failure-mode-catalogue)
7. [Competition-day operations for a small team](#7-competition-day-operations-for-a-small-team)
8. [PRINTABLE — the weekly testing protocol](#8-printable--the-weekly-testing-protocol)
9. [PRINTABLE — the match-day runbook](#9-printable--the-match-day-runbook)
10. [PRINTABLE — BIOBUZZ self-inspection checklist](#10-printable--biobuzz-self-inspection-checklist-v0-rule-numbers)
11. [Where Claude Code earns its keep here](#11-where-claude-code-earns-its-keep-here)
12. [Sources and known gaps](#12-sources-and-known-gaps)

---

## 1. Executive summary — the twelve things that actually matter

**[JUDGMENT]** Ordered by points-per-dollar-per-hour for a team with fewer than ten students.

| # | Claim | Why | Where |
|---|---|---|---|
| 1 | **You do not need a full field. You need 18 tiles, a wall on two sides, and the one scoring structure.** Full official field = **$1,665**; the useful 80% = **~$700**. | ~90% of useful reps are "acquire → travel 4–8 ft → score". That fits in 12 ft × 6 ft. | [§2](#2-the-practice-field-problem) |
| 2 | **Buy tiles first, perimeter last.** Tiles change how the robot drives; walls only matter for wall-hugging, corner extraction and pinning. | Tile friction, seams, and 5/8 in foam compliance change wheel behaviour more than anything else you can buy. | [§2.3](#23-what-each-practice-activity-actually-needs) |
| 3 | **Drive practice is the cheapest performance you will ever buy, and small teams systematically under-buy it.** 2 h/week minimum, scheduled and defended, from week 3. | The driver is the bottleneck in most matches. Motor power almost never is. | [§3](#3-drive-practice) |
| 4 | **Measure cycle time with a phone stopwatch and a tally sheet before you measure anything with code.** | A 30-second timed drill, logged weekly, exposes regressions that telemetry hides. | [§4.2](#42-the-cheapest-possible-measurement-rig) |
| 5 | **Three batteries and two chargers, or you are testing a different robot every hour.** A sagging pack wrecks autonomous repeatability more than any gain you will ever retune. | NiMH internal resistance rises with age; goBILDA publishes explicit retire-at IR thresholds. | [§5.1](#51-battery-management--the-single-highest-leverage-reliability-investment) |
| 6 | **Log battery voltage on every run and put it on the driver station.** Then never debug an autonomous without checking it first. | Half of "the auto is inconsistent" is "the pack was at 12.1 V instead of 13.4 V". | [§4.4](#44-logging--what-to-capture-and-what-to-do-with-it) |
| 7 | **Self-inspect against BIOBUZZ V0 R-rules, not last year's checklist.** ⚠️ The numbers moved *and* two limits changed. | DECODE allowed **8 motors / 10 servos**; BIOBUZZ **R503 allows 8 motors / 8 servos**. Operator console depth grew from 1 ft 2 in to 1 ft 6 in. | [§7.1](#71-inspection--pass-it-on-the-first-try), [§10](#10-printable--biobuzz-self-inspection-checklist-v0-rule-numbers) |
| 8 | **R105 — how far the robot may expand after the match starts — is NOT published yet.** Do not commit to an extension geometry before 12 Sep 2026. | V0 says literally: *"Sizing Constraints and more details will be released at Kickoff"*. | [§7.1](#71-inspection--pass-it-on-the-first-try) |
| 9 | **Nylon locknuts everywhere, threadlocker on every set screw, and a full fastener lap before every event.** | Vibration loosening is the top mechanical DNF cause and takes 20 minutes to prevent. | [§5.2](#52-fastener-discipline) |
| 10 | **Connectors fail far more often than wires. Strain-relieve every USB and every XT30.** | GM0 is blunt: XT30 is "prone to breaking"; battery Tamiya connectors go unreliable after repeated cycles. | [§5.3](#53-wiring-and-connector-failure-modes) |
| 11 | **A five-person team can run a pit — if roles are assigned on paper before load-in and nobody improvises.** | The failure mode is not "too few people", it is "everyone doing the same thing at once, and nobody watching the queue". | [§7.3](#73-role-assignment-for-4-10-students) |
| 12 | **Video-review your own matches at 0.25× the same night.** Free. Almost nobody does it. It finds driver hesitation and intake misalignment that no sensor sees. | Every FTC event page on ftc-events.firstinspires.org links its Twitch/YouTube archive. | [§4.5](#45-video-review-of-your-own-matches) |

---

## 2. The practice field problem

### 2.1 What the official field actually costs

**[FACT — WEB]** Vendor product pages, accessed 2026-08-21.

| Component | Part number | Price (USD) | Notes | Source |
|---|---|---|---|---|
| **Field Soft Tiles**, 36-tile pack | `am-2499` | **$293.00** | 24 in × 24 in × ⅝ in EVA foam, 1.3 lb each, grey, textured one side. Also 1-pk $9.70, 4-pk $38, 18-pk $147. **A full field is 36 tiles in a 6×6 grid.** | [AndyMark](https://andymark.com/products/first-tech-challenge-field-soft-tiles) |
| **FTC Perimeter Kit** | `am-0481b` | **$740.00** | Interior 11 ft 9 in square, walls 12.3 in tall, **80 lb** total, ships as two 52×14×8 in boxes at 40 lb each. Tool-free hinged corners + quick-release pins. Contains 4 corner assemblies (`am-2600b`), 4 panels (`am-2160b`), 2 straps (`am-2270a`), 16 rail links (`am-2580a`), 32 pins (`am-2579`). Assembly guide and STEP CAD published. | [AndyMark](https://andymark.com/products/first-tech-challenge-perimeter-kit) |
| **BIOBUZZ Full Game Set** | pre-order | **$599.00** | Excludes perimeter and tiles. | [AndyMark](https://andymark.com/products/ftc-2026-27-preorders) |
| **BIOBUZZ Partial Game Set** (Red *or* Blue) | pre-order | **$399.00** each | One alliance's half of the field elements. | same |
| **BIOBUZZ Tape Set** | `am-5850_tape` | **$33.00** | 1× red + 1× blue gaffers tape, 1 in × 165 ft each (`am-4952`, `am-4953`). | [AndyMark](https://andymark.com/products/ftc-2026-27-tape-set) |
| **BIOBUZZ POLLEN Game Preview Pack** | `am-5851_preview` | **$5.50** | 3 scoring elements. Yellow, **2.8 in ± 0.1 in diameter, 0.055 lb each** (≈ $1.83/ball). | [AndyMark](https://andymark.com/products/ftc-2026-27-game-preview-pack) |

**Full official field delivered to your build space: 293 + 740 + 599 + 33 = $1,665**, before shipping (the perimeter alone is 80 lb in two long boxes) and before tax.

> ⚠️ **[FACT — WEB] The pre-order window has closed.** AndyMark states: *"Orders received by 7-August-2026 will begin shipping after kickoff, beginning Monday, 14-September, 2026."* No second wave is published. **[JUDGMENT]** Phone or email AndyMark (`sales@andymark.com`) **this week** and ask (a) what an order placed today would actually ship, and (b) whether the FIRST Storefront will carry game sets in September — AndyMark's page notes grant dollars **cannot** be used on their site and directs teams to the FIRST Storefront instead. Plan your first month assuming you will not have official game elements in hand.

### 2.2 The cost ladder — every cheaper path, priced

**[FACT — WEB / LOCAL]** for costs; **[JUDGMENT]** for what each tier buys.

| Tier | What it is | Cost | Space needed | What it lets you practise | What it cannot do |
|---|---|---|---|---|---|
| **0. Tape on the floor** | Painter's tape marking a 12 ft square plus key distances, on a gym or classroom floor. | **~$10** | 12×12 ft | Autonomous path shapes, distance calibration, driver spatial awareness, setup-ritual rehearsal. | Anything involving tile friction, walls, or scoring. The floor is wrong — see §2.6. |
| **1. Tile square, no walls** | 18 tiles (12×6 ft) or 36 tiles (12×12 ft). | **$147** / **$293** | 12×6 / 12×12 ft | Everything about drivetrain behaviour: acceleration, wheel slip, odometry tuning, mecanum strafe drift, turn scrub, autonomous repeatability. | Wall alignment, pinning, ball rebound. |
| **2. Tiles + DIY PVC/hardboard perimeter** | FIRST's own published low-cost design. | **+ ~$160** (2020 material prices; expect more) | 12×12 ft | Tier 1 plus wall alignment, corner extraction, approximate ball rebound. | Exact wall bounce/friction — ⅛ in hardboard is not polycarbonate on extrusion. |
| **3. Tiles + partial official game set** | One alliance's scoring structure. | **+$399** | 12×6 ft is often enough | The actual scoring interaction — the thing that sets your cycle time. | Opponent-side play, full-field autonomous travel. |
| **4. Half field, official-ish** ⭐ | 18 tiles + DIY walls on two sides + one partial game set. | **≈ $706** | 12×6 ft + 3 ft aisle | ~85% of all useful practice reps. | Full-field auto, defence, alliance coordination. |
| **5. Full official field** | Everything in §2.1. | **$1,665** | 12×12 ft + ≥3 ft all round ⇒ ~18×18 ft room | Everything. | — |
| **6. Full field on a riser** | Commercial 12×12 ft riser platform. | **+$2,495–3,195** (+$395 cart) | 18×18 ft, 9 ft ceiling | Everything, plus ~300 ft³ of storage underneath. | Nothing extra competitively. This is a **space** purchase, not a **performance** purchase. |

Tier-2 source: [FIRST Low-Cost Field Perimeter Guide](https://ftc-resources.firstinspires.org/ftc/archive/2025/game/diy-perimeter) (Rev 1, 7/11/2023; material costs stamped 10/6/2020). Tier-6 source: [Robosource Field Risers](https://www.robosource.net/field-risers-ftc) — Classroom 12×12 ft **$2,495**, Portable **$2,995**, Gen 2 Portable **$3,195**, cart & storage **$395**, folding desk **$95**, shelf **$85**.

> **[JUDGMENT] For a small team the answer is Tier 4, then beg time on a real field.** ~$706 buys ~85% of the practice value of a $1,665 field, in half the floor area, and it fits in a classroom. The two things a half field genuinely cannot teach — full-field autonomous travel and defence — are exactly the two things a borrowed session fixes fastest (§2.7).

### 2.3 What each practice activity actually needs

**[JUDGMENT]** This is the table that saves the most money. Read it before buying anything.

| Practice activity | Minimum surface | Why |
|---|---|---|
| Drivetrain sanity check, motor direction, gamepad mapping | **Hallway, hard floor, 10 ft** | You are testing wiring and code, not dynamics. |
| Loop-time profiling, bulk-read verification, telemetry layout | **Bench, robot on blocks** | No floor required at all. |
| Mechanism range of motion, hard stops, servo endpoints | **Bench, robot on blocks** | Wheels off the ground is safer and faster. |
| Intake pickup from a flat surface | **4 tiles (4×4 ft) + a handful of Pollen** | Only the ball and the floor matter. |
| Intake pickup from a wall or corner | **4 tiles + 2 wall segments in an L** | Corners are where intakes fail. DIY walls are fine. |
| Scoring accuracy and repeatability | **Scoring structure + 8 ft of run-up** | This is why the $399 partial game set beats the $740 perimeter. |
| Cycle-time drilling (acquire → travel → score → return) | **18 tiles + scoring structure** | A real cycle is rarely longer than half a field. |
| Odometry / dead-wheel tuning, drift measurement | **36 tiles, flat and level** | You need the longest straight and largest square you can get; seams matter. |
| Autonomous path development and repeatability | **36 tiles + accurate tape lines** | Path geometry is absolute; tape gives the reference. |
| Autonomous ending in a wall/structure interaction | **36 tiles + perimeter + elements** | The auto ends by touching something. |
| Full match simulation, alliance coordination, defence | **Full field, two robots** | Borrow this. |
| Driver muscle memory under time pressure | **Whatever you have + a timer** | The timer is the essential part, not the field. |
| Human-player practice (loading / feeding) | **A wall segment + a bucket of Pollen** | Costs almost nothing and is almost never practised. |
| Setup ritual and pre-match checklist rehearsal | **Tape square on any floor** | Free. Do it weekly (§9). |

> **[JUDGMENT] The most common small-team mistake is buying the perimeter before the tiles.** The perimeter is the most expensive item ($740) and improves the fewest rows in that table. Tiles ($293) improve *every* row.

### 2.4 Building it yourself

#### 2.4.1 FIRST's own low-cost perimeter — full bill of materials

**[FACT — WEB]** Reproduced from the [FIRST Low-Cost Field Perimeter Guide](https://ftc-resources.firstinspires.org/ftc/archive/2025/game/diy-perimeter), Rev 1 dated 7/11/2023, with material costs the document stamps **"Costs updated 10/6/2020"**.

| # | Item | Qty required | Home Depot SKU* | Qty to buy | Unit | Total |
|---|---|---|---|---|---|---|
| 1 | PVC tee joint | 32 | 187917 | 32 | $0.82 | **$26.24** |
| 2 | PVC 90° elbow joint | 8 | 187976 | 8 | $0.79 | **$6.32** |
| 3 | 43.5 in long ½ in PVC pipe | 24 | 193712 (10 ft sticks) | 12 sticks | $6.29 | **$75.48** |
| 4 | 9.3 in long ½ in PVC pipe | 16 | (same sticks) | — | — | — |
| 5 | 1.75 in long ½ in PVC pipe | 16 | (same sticks) | — | — | — |
| 6 | 47.75 × 11.5 × 0.115 in hardboard panels | 12 | 832777 (4×8 ft × 0.125 in sheet) | 2 sheets | $13.98 | **$27.96** |
| 7 | #8 × ½ in wood screws | 120 | 251364 (100/pkg) | 2 pkgs | $7.97 | **$15.94** |
| 8 | 8 oz PVC cement | as needed | 187100 | 1 can | $7.96 | **$7.96** |
| | | | | | **Est. cost before tax** | **$159.90** |

\* The guide notes Home Depot is *"given as a convenient reference"*; materials are widely available and prices vary.

**Construction summary [FACT — WEB]:** each wall assembly is two outer panels plus one centre panel; the outer panels' PVC is cemented and **the centre panel's PVC is left unglued** so the field can be knocked down and rebuilt. Five screws evenly spaced along the top and bottom edge of each board, pre-drilled through wood *and* PVC with a bit slightly smaller than the screw. Eight corner pieces, cemented. Each 4×8 ft hardboard sheet yields 8 panels.

> **[JUDGMENT] Build two or three walls, not four.** Nearly every rep that needs a wall needs *one* wall — the one behind the scoring structure, or the one you extract balls from. Two adjacent walls in an L costs roughly **$55** in materials and covers corner extraction, which is where intakes actually fail. Add the rest later if you ever need a closed field.

#### 2.4.2 Building field elements from official CAD

**[FACT — LOCAL]** FIRST publishes **full-field STEP CAD** for FTC. This workspace already holds the DECODE example: `manuals/archive/supplemental/2025-26_DECODE_FieldCAD_STEP.zip` → a single 13.2 MB STEP assembly of the entire field (`DECODE… Full Field - am-5700_Full.step`). Expect the BIOBUZZ equivalent under `ftc-resources.firstinspires.org/ftc/2027/field` at or shortly after kickoff.

**[FACT — LOCAL]** FIRST also publishes two step-by-step assembly documents per season, both usable as fabrication references:

| Document | What it gives you | Local copy |
|---|---|---|
| **Initial FIELD Element Assembly Guide** | How each element is built from its constituent panels, with a parts list that explicitly distinguishes **"Full"** vs **"Partial"** quantities (DECODE example: 12 green + 24 purple ARTIFACTs full, 6 + 12 partial). | `manuals/archive/supplemental/2025-26_DECODE_InitialFieldElementAssemblyGuide.pdf` |
| **Event FIELD Setup Guide** | Tile coordinates and cutting, perimeter assembly, tape installation, element placement, plus a disassembly-for-storage procedure. | `manuals/archive/supplemental/2025-26_DECODE_EventFieldSetupGuide.pdf` |

**[FACT — WEB]** FIRST is formalising a tiered practice-element programme, explicitly distinguishing **testing** (validating a single function) from **practising** (simulating match conditions), and publishing four resource classes: *Team Test Elements* (CAD + build instructions, hardware-store materials), *Event Test Elements* (CAD + drawing package, newly public), *Team Practice Elements* (CAD only), and a *Wood Practice Perimeter* (CAD only). Medium-fidelity options assume access to a **4×8 ft CNC router**. Game-specific resources release **after kickoff**. ([FIRST community: Practice Field & Team Element Changes](https://community.firstinspires.org/2026-practice-field-team-element-changes)) ⚠️ **[UNVERIFIED]** — the post as retrieved reads FRC-framed. Confirm the FTC-side equivalents on `ftc-resources.firstinspires.org` at kickoff before planning a build around it.

> **[JUDGMENT] The realistic small-team play with CAD is not to reproduce the structure.** Reproduce **only the interface surface your mechanism touches** — the goal aperture, the ramp lip, the loading slot — at correct dimensions and correct height, on plywood or printed brackets bolted to a 2×4 frame. That is a $30–60, one-Saturday build, and it is worth more practice value than the other 90% of the structure combined. Take the dimensions from the STEP file, not from a photo.

#### 2.4.3 Scoring elements: the BIOBUZZ-specific win

**[FACT — WEB]** BIOBUZZ Pollen: **2.8 in ± 0.1 in diameter, 0.055 lb, yellow**, $5.50 per 3.

**[JUDGMENT]** At $1.83/ball this is the cheapest high-fidelity practice asset in the sport. **Buy 24–36 of them ($44–66) the moment they are in stock.** Reasons:

1. A ball game punishes practising with the wrong ball. Diameter, mass and surface finish all change intake compliance, hopper packing, and — if BIOBUZZ involves a launcher — exit velocity and spin.
2. Balls disappear. Under furniture, into bags, home in pockets. Budget ~20% loss per season.
3. With enough balls you can practise a **full hopper cycle** rather than a single pickup. Jams live at capacity, not at n=1.
4. A community 3D print of the Pollen exists on MakerWorld (`makerworld.com/en/models/2755231-ftc-2026-2027-biobuzz-pollen-game-element`) — **[UNVERIFIED]**, the page returned HTTP 403 to this workspace, and printed balls will not match 0.055 lb or the official surface. Use printed balls for **volume** tests ("does the hopper jam at 12?"), official balls for **tuning**.

### 2.5 Sharing, borrowing, and the "someone else's field" strategy

**[JUDGMENT]** For a team that cannot afford a field, access is a relationship problem, not a money problem. Ranked by effort-to-payoff:

| Path | How to get it | Realistic access | Cost | Catch |
|---|---|---|---|---|
| **Your own school/host org already owns one** | Ask the FLL coordinator, the tech-ed teacher, the makerspace lead. Many schools have tiles in a closet from a prior season. | Weekly | $0 | Setup/teardown time — see §2.6. |
| **A nearby team with a full field** | Offer something they need: 3D printing, CAD help, portfolio proofreading, or simply a scrimmage partner (they need one too). | 1–2×/month | $0 + travel | Scheduling. Start asking in **September**, not January. |
| **Regional / PDP scrimmage or practice day** | Watch your region's calendar. Many regions run pre-season and mid-season scrimmages on real fields. | 2–4×/season | $0–25 | Usually one day; very high value per day. |
| **Host team's field at an event** | See E105 below. | Event days only | $0 | You must be registered for that event. |
| **Split a field with 2–3 teams** | Co-purchase, rotate storage annually, or split by component (you buy tiles, they buy perimeter). | Depends | $250–550 each | Write down who owns what **before** money changes hands. |
| **University / library / community makerspace** | FIRST-affiliated universities frequently host. | Varies | $0 | Often needs an adult present and insurance paperwork. |

⚠️ **[FACT — LOCAL] Three practice rules that constrain event-day practice.** From `manuals/2026-27_BIOBUZZ/sections/05_EventRules_E_p33-42.txt`:

- **E105** — *"Only teams registered for an event may use that event's competition FIELD, practice FIELD, and inspection unless pre-approved… Host teams supplying practice FIELD elements and/or machine shop resources may use them; however, teams registered for that event must be granted priority."*
- **E106** — *"Teams may only practice with their ROBOT in their pit space, in the designated event practice areas, or while in a Practice MATCH."* Plus the orange-box note that teams **may not set up their own practice equipment outside their pit**. (Demonstrating functionality to guests or JUDGES is explicitly **not** "practice".)
- **E116** — *"A team may only use a practice FIELD with a ROBOT that has passed an initial, complete inspection. This rule only applies to events not using scheduled inspection times."*

> **[JUDGMENT] E116 is a scheduling weapon.** At any event that does not use assigned inspection slots, **inspection is the gate on practice-field access**. Being first through inspection converts directly into extra practice-field minutes that most teams never get. See §7.1 and §9.

### 2.6 Surface, space, and setup-time engineering

**[FACT — LOCAL]** From the DECODE *Event FIELD Setup Guide* §5.1 (guidance is game-independent):

> *"While every FIELD uses TILES, ROBOTS will perform differently depending on the surface under the FIELD. We recommend that wherever possible, TILES are placed on top of a hard, level, and uniform surface… whatever the surface conditions are for the FIELDS in the ARENA, similar conditions are available at any practice FIELDS… Consistency is most important. (If you must have carpet under practice FIELDS, consider putting carpet under the FIELDS in the ARENA, and vice versa.)"*

**[JUDGMENT] Translation: tiles on carpet ≠ tiles on a gym floor.** A compliant substrate absorbs energy, changes effective wheel friction, and lets tile seams open under a heavy robot. Tune odometry on carpet-backed tiles and compete on hardwood and your autonomous will be systematically wrong in a direction you will not diagnose on the day. Practical rules:

1. Put tiles on the hardest, flattest surface available.
2. If you cannot, **write down what your practice substrate is** and treat autonomous distances as needing a calibration lap at every event (§9, step 6).
3. Never mix substrates under one field — half on carpet, half on tile edge is the worst case.

**[FACT — WEB/LOCAL] Two setup details that cost an hour if unknown:**

- **Tile dimensional variance is real and expected.** AndyMark warns tiles measure **24¼ in to 24⅜ in** and recommends assembling the full 6×6 grid *inside* the perimeter before trimming any tabs. The setup guide's procedure is to cut **16 edge tiles** (material removed from one edge) and **4 corner tiles** (two adjacent edges), keeping cuts symmetric so the grid stays centred.
- **Fastener guidance:** *"There are no specifications for torquing the various fasteners used on the FIRST Tech Challenge FIELD… all fasteners should be fully tightened."* Threadforming screws until no threads are visible; nylock nuts until no threads show between head and nut.

**Space arithmetic [JUDGMENT]:**

| Configuration | Field footprint | Usable room needed | Fits in |
|---|---|---|---|
| Tape square only | 12×12 ft | 12×12 ft | Any gym, cafeteria, hallway intersection |
| 18-tile half field, no walls | 12×6 ft | 15×9 ft | Classroom with desks pushed back |
| 18-tile half field + L walls + partial game set | 12×6 ft | 16×10 ft | Large classroom, two-car garage |
| Full field, no riser | 12×12 ft | ~18×18 ft (3 ft aisle all round) | Gym stage, shop, double classroom |
| Full field on 24 in riser | 12×12 ft | ~18×18 ft, 9 ft ceiling | Dedicated room only |

**Setup-time engineering [JUDGMENT].** If the field must be torn down every session you will practise less — that is simply true, and it is the hidden cost of shared space. Mitigations, cheapest first:

1. **Tape the tile-grid outline onto the floor once.** Re-laying 18 tiles onto a marked outline takes ~4 minutes instead of ~15 with an alignment argument.
2. **Number every tile on the underside** (A1…F6, per the setup guide's coordinate convention). Rebuild becomes mechanical, not judgement-based.
3. **Bundle tiles in stacks of six with a cam strap.** Two students move a half field in three trips.
4. **Build walls as three-panel modules that stay assembled** — the FIRST DIY design already supports this, since only the centre PVC is unglued.
5. **Keep the scoring structure permanently assembled on a dolly** if at all possible. It is the slowest thing to rebuild and the most valuable thing to have standing.
6. **Time your own setup once and write the number on the wall.** If it is over 15 minutes, fix it; you are paying that tax every single session.

### 2.7 The borrowed-field session: extracting maximum value

**[JUDGMENT]** You will get a handful of full-field sessions per season. Do not waste them on anything a half field can do. Arrive with this list printed:

| Priority | Do on a full field | Time |
|---|---|---|
| 1 | **Run your autonomous 10× consecutively, logging every result.** Not three times. Ten. Record start pose, end-pose error (measure it with a tape), and battery voltage each run. | 30 min |
| 2 | **Full-field cycle timing** — the real travel distance, not your compressed practice distance. | 20 min |
| 3 | **Defence drills** — have the host team push you. You cannot simulate this alone. | 20 min |
| 4 | **Alliance-partner coordination** — two robots in one space; learn what "get out of the way" looks like. | 20 min |
| 5 | **Endgame timing** — rehearse the last 20 seconds against a clock, whatever BIOBUZZ's endgame turns out to be. | 15 min |
| 6 | **Video** — GoPro on a tripod behind the driver station, one full match, for later review. | continuous |
| 7 | Anything you could have done at home | **never** |

**[FACT — LOCAL]** Recording on the robot is legal: BIOBUZZ V0 permits self-contained recorders (GoPro or similar) *"used only for non-functional post-MATCH viewing"* with wireless capability disabled (margin-labelled R709/R710 in the V0 extraction). Recording *people* at an event requires their consent per the V0 rule adjacent to E116.

---

## 3. Drive practice

### 3.1 How much, and when

**[FACT — WEB]** Reported practice loads vary enormously and are mostly self-reported. On Chief Delphi, teams describe schedules from *"Tuesday and Thursday 2 hours in the evening and Saturday for 4 hours for most of the fall semester"* up to *"10+ hours per week of driver practice"*, and one recurring theme is that teams *"have been more successful with less functionality purely because they've gotten more stick time"* ([How to run Drive Practice?](https://www.chiefdelphi.com/t/how-to-run-drive-practice/514296), [Looking for Driver Practice Advice](https://www.chiefdelphi.com/t/looking-for-driver-practice-advice/512706)). ⚠️ These are FRC-heavy forums; treat the hour counts as directional, not as an FTC benchmark.

**[JUDGMENT] The small-team prescription:**

| Phase | Driver hours/week | Notes |
|---|---|---|
| Pre-kickoff (now → 11 Sep) | **1 h** | Drive last year's or a StarterBot chassis. Build controller familiarity, not game skill. |
| Kickoff → week 3 | **0–1 h** | The robot is being built. Do not fake it. Instead: drivers do setup-ritual rehearsal and study game rules. |
| Week 4 → first event | **2 h minimum, 3–4 h ideal** | Non-negotiable, scheduled, defended against build panic. |
| Between events | **3 h** | This is when driver skill compounds fastest, because the robot is stable. |
| Championship prep | **4 h+** | Plus at least two full-field sessions. |

**[JUDGMENT] The rule that makes this survive contact with reality: drive practice happens *while* builders build.** It is not a separate meeting. The moment drive practice competes with build time for the same hour, it loses, every time. Put the practice surface in the same room as the workbench and run them concurrently.

**⚠️ The trap:** a small team's robot is *never* "done enough to practise". You will always be able to justify one more mechanism change. **Set a weekly hard cut — e.g. Thursday 18:00 the robot is frozen for 90 minutes** — and enforce it with a timer, not a discussion.

### 3.2 Driver selection

**[JUDGMENT]** Most small teams pick drivers by seniority or by who built the thing. Both are wrong often enough to cost matches.

**A defensible selection process that takes one meeting:**

| Step | What | Why |
|---|---|---|
| 1 | **Everybody drives.** Every student gets 10 minutes on the same drill, same robot, same battery state. | You cannot select from a pool of one. |
| 2 | **Score objectively.** Run a fixed 90-second timed drill (§3.4, Drill A). Record cycles completed and penalties/collisions. Run it twice per candidate, take the second score. | Removes "who seems confident". |
| 3 | **Score learning rate, not peak.** Run the same drill again a week later. **Improvement matters more than the first number.** | The season is 6 months long. The fast learner passes the natural in November. |
| 4 | **Check the soft factors deliberately** — attendance reliability, calm under a referee's voice, willingness to be corrected mid-match. | These decide playoffs. |
| 5 | **Name a primary and a backup for every seat, in writing.** | Illness and college visits are certainties, not risks. |
| 6 | **Re-run the selection once, in January.** | Locking a drive team in October and never revisiting it is a small-team classic. |

**[FACT — LOCAL, prior season]** DRIVE TEAM composition in DECODE (`2025-26_DECODE_Competition_Manual_TU32.html` §10.2): *"A DRIVE TEAM is a set of up to 4 people from the same FIRST Tech Challenge team… no more than 1 member of the DRIVE TEAM is allowed to be a non-STUDENT."* Roles:

| Role | Description | Max per drive team | Criteria |
|---|---|---|---|
| **DRIVE COACH** | "a guide or advisor" | 1 | any team member, **may be an adult**, must wear the DRIVE COACH badge |
| **DRIVER** | "an operator and controller of the ROBOT" | 3 | STUDENT, must wear a DRIVE TEAM badge |
| **HUMAN PLAYER** | "a SCORING ELEMENT manager" | (within the 4 total) | STUDENT |

⚠️ **BIOBUZZ's own DRIVE TEAM section is Section 10, which is a placeholder in V0** — *"This section will be updated with the Kickoff Competition Manual release on September 12, 2026"*. Plan on the DECODE structure; re-verify on kickoff morning.

### 3.3 The drive coach — the role small teams waste

**[JUDGMENT]** With 4–8 students, the drive coach is usually "the mentor who happens to be standing there". That is a wasted slot. The drive coach is the only person on the alliance wall whose job is *information*, and information is what decides close matches.

**What a drive coach should actually do, in order:**

| Time | Coach's job | What they must NOT do |
|---|---|---|
| T−20 min (queue) | Confirm the alliance strategy in one sentence with both partners. Write it on a wrist card. | Renegotiate strategy at the field. |
| T−5 min (field setup) | Watch the *checklist runner*, not the robot. Confirm battery swapped, signs on, init pose correct. | Touch the robot (that is the technician's job). |
| AUTO | Watch the **opponents**, not your own robot. Your robot is running code; nothing you say changes it. | Narrate your own auto. |
| TELEOP first 30 s | Call the field state: "two balls left in the corner", "they're going for the goal". | Call button presses. Drivers own the controls. |
| TELEOP middle | Call **one** thing at a time. Count down to endgame at 40 s, 30 s, 20 s. | Stack three instructions in one breath. |
| Endgame | Own the clock. "Twelve seconds — go now." | Panic-narrate. |
| Post-match | Say one specific positive thing and record one specific fix. | Debrief on the field; wait for the pit. |

**[JUDGMENT] Practise the coach.** The coach should run the drills in §3.4 *as coach* — talking over them, with a real clock — not just watch. A coach who has never rehearsed will say twelve words in the first ten seconds of a real match and then go silent.

### 3.4 The drill catalogue

**[JUDGMENT]** All of these fit on 18 tiles unless marked. Each has a **number** you write down. A drill without a recorded number is a warm-up, not practice.

| ID | Drill | Setup | How | Metric | Target progression |
|---|---|---|---|---|---|
| **A** | **Timed cycle count** | Scoring structure + 8 ft run-up + 10 balls | 90 s on a clock. Count completed score events. | Cycles per 90 s | Log weekly. Expect +30–50% over 6 weeks, then a plateau. |
| **B** | **Cold-start cycle** | Same | Driver takes the controller having not touched it for 10 min, and immediately runs Drill A. | Cycles per 90 s, cold | Should approach warm score within 3 weeks. **This is the real match condition.** |
| **C** | **First-cycle latency** | Same | Stopwatch from "GO" to first score. Ten reps. | Median, and worst of 10 | The worst-of-10 is the number that matters. |
| **D** | **Corner extraction** | 2 walls in an L + 5 balls jammed into the corner | Retrieve all 5. | Seconds, and failures | Most intakes fail here. Find out in October. |
| **E** | **Precision approach** | Tape a target box the size of your scoring tolerance | Drive from 8 ft, stop inside the box, no correction. 10 reps. | Hits / 10 | 8/10 before you trust any alignment macro. |
| **F** | **Blind drive** | Tape square, no game elements | Drive a set path with the driver facing away from the field, watching only the driver station screen. | Path completion | Tests your telemetry design more than the driver. |
| **G** | **Sag drill** | Deliberately half-charged battery | Run Drill A on a pack at ~11.5 V resting. | Cycles per 90 s | Drivers must have felt a sagging robot **before** match 9 of a qualifier. |
| **H** | **Failure injection** | Any | Mentor silently disables a mechanism (unplug a servo, kill a macro). Driver must notice and switch to manual. | Seconds to recognise | Under 5 s. This one saves matches. |
| **I** | **Handoff drill** | Any | Primary and backup driver swap seats mid-drill. | Cycles lost in transition | Makes the backup real. |
| **J** | **Setup ritual** | Tape square | Full pre-match placement from cart to hands-off, against a 90-second clock. | Seconds, errors | Under 60 s, zero errors, every time. See §9. |
| **K** | **Endgame rehearsal** | Whatever the endgame requires | Start a 30-second clock mid-cycle; the driver must abandon the cycle and execute endgame. | Success rate | The abandon decision is the skill. |
| **L** | **Defence survival** *(full field)* | Two robots | Partner robot actively obstructs. | Cycles per 90 s under pressure | Compare to Drill A. The delta is your defence vulnerability. |
| **M** | **Human-player feed** | Wall + balls | Human player feeds under time pressure; driver receives. | Balls delivered per 30 s | Free points nobody practises. |

**[JUDGMENT] A 60-minute drive practice that actually works:**

```
0:00–0:05  Setup ritual drill (J) — cold, timed, no coaching
0:05–0:10  Free drive / warm-up
0:10–0:20  Drill A ×3, logged
0:20–0:30  Skill of the week (D, E, K or M)
0:30–0:40  Drill B (cold start) ×2 — driver leaves the room in between
0:40–0:50  Drill H (failure injection) ×3
0:50–0:55  Backup driver runs Drill A ×1, logged
0:55–1:00  Log the numbers on the wall chart. Name ONE fix for next week.
```

### 3.5 Running practice matches with a very small team

**[JUDGMENT]** A "practice match" needs: a clock, a scorer, a field reset, and consequences. It does **not** need six robots or an opposing alliance.

| Team size | How to run a practice match |
|---|---|
| **2 students** | One drives, one runs clock + resets + scores on paper. Swap every match. Use a phone timer with the real period lengths. |
| **3–4** | Driver, coach, field reset/scorer, plus one person doing pit-triage rehearsal on a deliberately "broken" spare part. |
| **5–8** | Full drive team (2 drivers + coach + human player) plus a scorer and a pit crew of 1–2. This is a real match rehearsal. |
| **Two teams together** | Run true alliance matches. This is the single highest-value use of an inter-team relationship. |

**Match structure to rehearse [FACT — LOCAL, prior season].** DECODE ran **30 s AUTO + 8 s transition + 2:00 TELEOP**, with field cycle time of **5–12 minutes per field** including pre-match setup and post-match reset. ⚠️ BIOBUZZ match periods are in Section 10, a **placeholder** in V0. Rehearse to DECODE timing and re-verify at kickoff.

**[JUDGMENT] Make practice matches have consequences.** Keep a season-long practice-match record on a whiteboard: date, cycles, score, one failure observed, one fix applied. Two effects: it produces a real trend line, and it becomes engineering-portfolio evidence of an iterative test process — which is exactly what judges look for and what most small teams cannot show.

### 3.6 Scrimmages

**[JUDGMENT]** Attend every scrimmage in reach, even at 60% robot completion. Ranked value:

1. **Free full-field time** with real elements and other robots — see §2.7.
2. **Free dry run of the event-day ritual** — load-in, pit setup, queue, checklist. The ritual is what fails first at a real event.
3. **Free failure discovery** under real conditions (other robots hitting yours; unfamiliar power; unfamiliar Wi-Fi environment).
4. **Free scouting relationships** for alliance selection later.
5. **Free inspection rehearsal** if an LRI is present — ask them to walk your robot even informally.

---

## 4. Data-driven tuning: measuring what you are actually bad at

### 4.1 The one metric that matters, and how to think about it

**[JUDGMENT]** Almost every FTC robot's teleop performance reduces to:

```
teleop points  ≈  (teleop seconds ÷ cycle time)  ×  points per cycle  ×  success rate
```

Three levers, and teams over-index on the wrong one:

| Lever | Typical small-team instinct | Where the gains actually are |
|---|---|---|
| **Cycle time** | "add a faster motor" | Travel path, driver decisiveness, and the acquire step. |
| **Points per cycle** | ignored | Carrying 2–4 game elements per trip instead of 1 is usually a bigger multiplier than any speed change. |
| **Success rate** | ignored until it fails on the field | A 70%-reliable fast cycle loses to an 95%-reliable slower one over 5 qualification matches. |

**[JUDGMENT] Decompose the cycle before optimising it.** Break every cycle into four stopwatch segments and time them separately:

| Segment | Definition | Usual bottleneck |
|---|---|---|
| **Acquire** | Contact-to-secured | ⚠️ **The most common real bottleneck.** Alignment, not intake power. |
| **Travel out** | Secured → in scoring position | Path choice and driver decisiveness. |
| **Score** | In position → element released and counted | Mechanism settle time; alignment tolerance. |
| **Travel back** | Released → next contact | Often ignored; frequently 30–40% of the cycle. |

**⚠️ The diagnosis rule:** if `Acquire` is your longest segment, **do not touch the drivetrain, the motors, or the PID gains.** Widen the intake, add a compliant lead-in, add a driver alignment aid, or change the approach angle. Small teams spend weekends on the wrong segment because segment timing is the step they skip.

### 4.2 The cheapest possible measurement rig

**[JUDGMENT]** Total cost: **$0–15**. Total setup: 20 minutes. This beats any dashboard for the first two months.

| Item | Cost | Use |
|---|---|---|
| Phone stopwatch with lap function | $0 | Segment timing — tap lap at each of the four segment boundaries. |
| Printed tally sheet on a clipboard | ~$2 | Cycle counts, failures, battery ID, driver name. |
| Whiteboard on the wall by the field | ~$10 | The weekly trend line. Visible = motivating = actually maintained. |
| Phone on a cheap tripod | $0–15 | Video for §4.5. |
| A single Google Sheet | $0 | Where the clipboard gets typed up. One row per session. |

**Minimum viable log columns:**

```
date | driver | battery_id | resting_V | drill_id | reps | cycles | failures | note
```

**[JUDGMENT] The discipline that makes it work: one person owns the clipboard for the whole session, and the numbers get typed into the sheet before anyone leaves.** A log that is written on paper and never digitised produces zero trend lines and zero portfolio evidence.

### 4.3 What "good" looks like — real numbers from the last season

**[FACT — WEB]** From the [FTCScout GraphQL API](https://api.ftcscout.org/graphql), queried 2026-08-21 for season 2025 (DECODE):

- **8,866 active teams**, **45,122 matches played**.
- Quick-stats (OPR-style contribution estimates, all-region rank in parentheses):

| Team | Name | Total | AUTO | Driver-controlled | Endgame |
|---|---|---|---|---|---|
| **30030** | Exodus (Austin, TX) | **236.5** (rank 11) | 65.7 (3) | **170.8** (16) | 20.4 (5) |
| **21087** | Velocity (Brăila, RO) | 195.5 (43) | 56.5 (21) | 146.3 (51) | 13.5 (204) |
| **11228** | OverClucked Bots (Zeeland, MI) | 146.1 (192) | 39.7 (243) | 107.9 (222) | 7.6 (3814) |
| **7172** | Technical Difficulties (Plano, TX) | 110.6 (504) | 37.7 (313) | 74.8 (609) | 11.6 (587) |
| **17792** | Amigos Droids (Belo Horizonte, BR) | 138.0 (247) | 44.1 (139) | 93.9 (351) | 7.7 (3654) |

**[FACT — WEB]** Those first three teams were the **2026 FIRST Championship winning alliance**; 7172 was on the finalist alliance; **17792 won the overall Inspire Award**. ([FIRST community: Congratulations to our DECODE FIRST Championship Teams](https://community.firstinspires.org/congratulations-to-our-decode-first-championship-teams))

**[FACT — LOCAL]** DECODE point values (`2025-26_DECODE_Competition_Manual_TU32.html` §10.5.4): ARTIFACT CLASSIFIED = **3 points** in both AUTO and TELEOP; a PATTERN-matching ARTIFACT adds **2**; OVERFLOW = 1; BASE = 5 partial / 10 full, +10 alliance bonus.

**[JUDGMENT] Converting that into a cycle-rate intuition.** Take 30030's driver-controlled OPR of ~171 points. At 3–5 points per scored ball, that is roughly **34–57 balls put away in a 120-second teleop**, i.e. **0.28–0.48 balls/second**, i.e. a *scoring event* every 2–3.5 seconds. That is only possible because DECODE was a launcher game where one "trip" delivers many elements — which is precisely the "points per cycle" lever from §4.1. ⚠️ OPR is a least-squares estimate over an alliance, not a measured count; treat these as order-of-magnitude anchors, not ground truth.

**[JUDGMENT] Three conclusions a small team should take from that table, and they are not the obvious ones:**

1. **The world-champion alliance captain ranked 11th, not 1st.** Its two partners ranked **43rd** and **192nd**. You do not need to be the best robot on Earth; you need to be reliable, pickable, and paired well.
2. **The Inspire Award winner ranked 247th in total OPR** — well inside the top 3% of 8,866 teams, but nowhere near the top of the performance table. Robot performance is a *gate*, not the *goal*, for the award that advances you.
3. **Endgame rank is wildly noisy** (rank 5 vs rank 3,814 on the same alliance). Endgame is usually a small, cheap, learnable behaviour. It is one of the best value-per-hour targets for a small team.

### 4.4 Logging — what to capture, and what to do with it

Deep implementation detail lives in `research/PROGRAMMING-PRACTICE.md` §7.7. What belongs *here* is the testing discipline around it.

**[JUDGMENT] The minimum log for tuning purposes**, written to a CSV on the Control Hub every OpMode run:

| Field | Why it earns its column |
|---|---|
| `timestamp`, `match_or_practice_id` | Correlate with the clipboard and the video. |
| `battery_voltage` | ⚠️ **The single most under-logged, most explanatory variable in FTC.** |
| `loop_time_ms` | A rising loop time explains "the robot feels laggy" without any mechanical cause. |
| Each subsystem's **state enum** | Lets you answer "was it in TRANSFER when it jammed?" |
| Setpoint **and** measured position, per mechanism | Distinguishes "commanded wrong" from "failed to reach". |
| Localizer pose | Autonomous drift analysis. |
| **Every driver button press** | Answers "did the driver press it, or did the macro not fire?" — a question you cannot answer any other way. |
| Vision accept/reject **with reason** | Prevents "the camera is broken" mis-diagnoses. |

**[FACT — LOCAL]** Two event-day constraints from the BIOBUZZ V0 rules that shape your tooling choices:

- **R704 (V0 line ~3298 / §12.7)** restricts communications originating from devices other than the ROBOT CONTROLLER and DRIVER STATION at events — which is why **file logging, not a live dashboard, is the event-safe debugging strategy**. See `research/PROGRAMMING-PRACTICE.md` §1.2 for the exact reading.
- **R904** forbids any wireless other than the RC↔DS link to, from or within the OPERATOR CONSOLE during a MATCH.

**[JUDGMENT] The habit that converts logs into wins:** after every practice-match block, **plot exactly one thing** — battery voltage over the match, with the cycle-completion timestamps marked on it. Nine times out of ten, the moment where cycle time degrades is visible on the voltage curve. That single plot has more diagnostic value than any other visualisation available to a small team.

### 4.5 Video review of your own matches

**[JUDGMENT]** This is free, high-yield, and nearly universally skipped by small teams.

**Where the video is [FACT — WEB]:** `ftc-events.firstinspires.org` is the official source of event information, results and **webcasts**; regions stream on **Twitch and YouTube** and direct stream links are posted on each event's page. FIRST's own channel is [twitch.tv/firstinspires](https://www.twitch.tv/firstinspires). Add your own on-robot GoPro (legal per R709/R710 with wireless disabled) and a phone on a tripod behind the driver station.

**The review protocol [JUDGMENT] — 25 minutes, same night, whole team:**

| Min | Step |
|---|---|
| 0–2 | Watch the match once at 1× without commentary. No talking. |
| 2–10 | Watch at **0.25×–0.5×**, and **count hesitations** — every moment the robot is moving but not progressing toward a cycle. Tally them. |
| 10–15 | For each hesitation, classify: **driver decision**, **mechanism slow**, **alignment retry**, **field traffic**, or **waiting on a partner**. |
| 15–20 | Time each of the four cycle segments (§4.1) off the video for two representative cycles. |
| 20–25 | Write **exactly one** change for the week, in the log. Not three. One. |

**[JUDGMENT] The hesitation tally is the killer metric.** In most small-team matches, 20–35 seconds of a 120-second teleop are spent hesitating or re-aligning. That is 20–30% of your teleop score sitting in plain sight on a free video, recoverable with zero dollars. And most hesitations classify as **driver decision** or **alignment retry** — neither of which is fixed by a bigger motor.

### 4.6 Finding the actual bottleneck — a decision tree

**[JUDGMENT]** Run this before any hardware change. It takes one practice session.

```
Is the robot completing fewer cycles than last week?
├─ YES → Check battery FIRST (resting V, IR — §5.1). Then loop time. Then fasteners.
│         Regressions are almost never design problems.
└─ NO  → Time the four segments (§4.1). Which is longest?
   ├─ ACQUIRE longest
   │   ├─ Failures on approach?      → alignment aid, wider lead-in, compliant intake edge
   │   ├─ Failures on grip/retain?   → surface material, compression, spring preload
   │   └─ Driver hunting for it?     → driver aid / camera / field-centric drive / practice drill D+E
   ├─ TRAVEL (either direction) longest
   │   ├─ Robot slow?                → gear ratio (last resort — check current draw first)
   │   ├─ Driver braking early?      → practice, and check accel/decel curves in code
   │   └─ Bad path choice?           → review video; it's usually a decision, not a speed problem
   ├─ SCORE longest
   │   ├─ Mechanism settle time?     → motion profile / feedforward (see PROGRAMMING-PRACTICE §6.1c)
   │   ├─ Alignment retries?         → widen tolerance mechanically before tightening it in software
   │   └─ Waiting on a sensor?       → check the sensor is actually the limiter, not just first in the code
   └─ TRAVEL BACK longest
       └─ Almost always driver decisiveness or an unnecessary turn. Fix in practice, not in CAD.
```

**[JUDGMENT] The three most common misdiagnoses in FTC, in order:**

1. **"We need more motor power."** Usually the robot is already traction-limited or the driver never reaches full speed. Log actual commanded power before believing this.
2. **"The PID needs tuning."** Usually the mechanism is mechanically inconsistent (backlash, a loose set screw, a rubbing wire) and no gain fixes that.
3. **"The camera/sensor is unreliable."** Usually the lighting, mounting rigidity, or accept/reject logic is unreliable. Log the reject reasons and the mystery evaporates.

---

## 5. Reliability engineering

**[JUDGMENT]** Reliability is the one performance axis where a small team can beat a big one outright, because it costs discipline rather than dollars. A 5-match qualifier is a reliability test with a scoring system attached: a robot that scores 60 points five times out of five beats a robot that scores 110 twice and zero three times, on both ranking and pick-ability.

### 5.1 Battery management — the single highest-leverage reliability investment

#### 5.1.1 What is legal, and what it costs

**[FACT — LOCAL]** BIOBUZZ V0 **R601** allows exactly one main battery, which must be one of seven approved packs (`manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`, Table 12-4). Only the fuse (COTS 20 A ATM mini blade) and the connector (Anderson Powerpole, XT30, or comparable rating) may be changed.

| Pack | Part number | Price (USD, as of Aug 2026) | Source |
|---|---|---|---|
| REV 12V Slim Battery | `REV-31-1302` | **$60.00** — 3000 mAh, XT30 female, 567 g, inline 20 A ATM fuse | [REV](https://www.revrobotics.com/rev-31-1302/) |
| goBILDA 12V NiMH Nested Battery | `3100-0012-0020` | **$64.99** — 3000 mAh, XT30 [MH-FC], 597 g, 16 AWG, nests inside 1120-series U-channel | [goBILDA](https://www.gobilda.com/12v-nimh-nested-battery-3000mah-mh-fc-xt30-connector/) |
| AndyMark Flat Pack Battery DC 12V | `am-5290` | **[UNVERIFIED]** — not priced for this document | R601 Table 12-4 |
| Matrix 12V 3000 mAh NiMH | `14-0014` (formerly 739023) | **[UNVERIFIED]** | R601 Table 12-4 |
| Studica 12V 3000 mAh NiMH | `70025` | **[UNVERIFIED]** | R601 Table 12-4 |
| TETRIX MAX 12V 3000 mAh NiMH | `W39057` | **[UNVERIFIED]** | R601 Table 12-4 |
| WATTOS 12V Battery | `WT-NMH1230` | **[UNVERIFIED]** | R601 Table 12-4 |

⚠️ **[FACT — LOCAL]** The list is closed. *"There are many other similar style batteries available from multiple VENDORS, but only the listed manufactures and part numbers are legal for use at FIRST Tech Challenge Events."* A hobby-shop NiMH pack of identical specification is an inspection failure.

#### 5.1.2 Chargers, and the rule that constrains them

**[FACT — LOCAL] E511** requires charging at a safe manufacturer-recommended rate, **never on a charger exceeding a 3-amp average channel current**, and never with alligator clips — the connector must be polarised and match the battery.

| Charger | Part number | Price | Rate | Practical charge time, 3000 mAh pack |
|---|---|---|---|---|
| goBILDA 12V Battery Charger (NiCad/NiMH, XT30) | `3101-0012-0001` | **$14.99** | **1.0 A**, trickling to 0.07 A when full | **~3.5–4.5 h** from flat |
| REV guidance for `REV-31-1302` | — | — | **1.8–2.0 A** recommended; **1.5 A min, 3.0 A max** | *"Typical charge time does not exceed 2 hours"* |

Sources: [goBILDA charger](https://www.gobilda.com/battery-charger-nicad-nimh-12-1/), [REV 12V Slim Battery](https://www.revrobotics.com/rev-31-1302/).

> ⚠️ **[JUDGMENT] The $14.99 charger is the hidden reason small teams practise on sagging packs.** At 1.0 A a flat pack needs most of a meeting to come back. Two of those chargers plus three batteries gives you a *maximum* of roughly one fresh pack per hour of practice. **Buy chargers before you buy a fourth battery**, and prefer a ~2 A unit (still inside E511's 3 A ceiling) if you can source one. **[UNVERIFIED]** — confirm the actual per-channel charge current on whatever unit you buy; E511 is written per channel and multi-bay chargers vary.

#### 5.1.3 How many batteries, honestly

**[JUDGMENT]**

| Team situation | Batteries | Chargers | Why |
|---|---|---|---|
| Absolute minimum to compete | **2** | 1 | One in the robot, one charging. You will run a sagging pack at least once. |
| **Recommended floor for a small team** ⭐ | **3** | **2** | One in the robot, one cooling, one charged and waiting. Survives a 6-match qualifier with a fresh pack every match. |
| Comfortable | 4 | 2 | Adds a dedicated practice-only pack so competition packs stay low-cycle. |
| Two-event day / championship | 5–6 | 2–3 | Playoffs run back-to-back with an 8-minute floor between matches (§7.4). |

**[FACT — WEB]** Community practice, from Chief Delphi (retrieved 2026-08-21 via search snippet — chiefdelphi.com returns HTTP 403 to direct fetch from this workspace): teams *"bring a few extra batteries to competition, because if batteries are drained a lot in a match it will take longer to power them back up"*, and a common rotation is to use next *"the battery that has been charging the longest"* ([Battery Tips for Competition?](https://www.chiefdelphi.com/t/battery-tips-for-competition/504798), [Battery Tracking for FTC/FRC](https://www.chiefdelphi.com/t/battery-tracking-for-ftc-frc/444600)). ⚠️ These are FRC-heavy forums; the principle transfers, the pack counts do not.

**Cost of the recommended floor:** 3 × $60 + 2 × $14.99 ≈ **$210** (as of August 2026). **[JUDGMENT]** That is the best $210 on a small team's reliability line — cheaper than one goBILDA motor set, and it fixes more matches.

#### 5.1.4 The rotation protocol

**[JUDGMENT]** Write this on the pit wall and never deviate.

| Step | Action |
|---|---|
| 1 | **Every pack gets a permanent number** (`B1`, `B2`, `B3`) in paint pen or engraved label, plus the month/year it entered service. |
| 2 | **A pack leaves the charger only when it is next in line.** Packs do not sit on a charger for hours — both REV and goBILDA warn that extended charger connection degrades the pack. |
| 3 | **A used pack goes into the "cooling" slot, not onto the charger.** *"Let the battery cool before and after charging"* (REV). Ten minutes on the bench is enough. |
| 4 | **Log it.** `battery_id, match_no, resting_V before, resting_V after` — five seconds with a $12 multimeter, or straight off the Driver Station screen. |
| 5 | **The next match uses the charged pack with the highest resting voltage**; ties broken by lowest measured internal resistance. |
| 6 | **Never charge a pack that has not been meaningfully discharged.** |
| 7 | **The highest-IR pack becomes the practice pack.** It never sees a qualification match again. |

#### 5.1.5 Internal resistance — the retirement criterion

**[FACT — WEB]** The **goBILDA 12V Battery Health Analyzer** (`3109-0010-0001`, **$49.99**) reports pack voltage and internal resistance in mΩ, and publishes explicit retirement thresholds ([goBILDA](https://www.gobilda.com/12v-battery-health-analyzer-nimh-3000mah/)):

| Robot type | Retire the pack when IR exceeds |
|---|---|
| Low-power robots | **> 200 mΩ** |
| Average robots | **> 160 mΩ** |
| High power-draw robots | **> 130 mΩ** |

goBILDA's guidance is to *"use batteries in order from lowest IR to highest in competitions"* — best packs early in the queue, high-IR packs demoted to practice.

**[JUDGMENT] The $0 substitute if you cannot spend $49.99.** IR is what turns a good resting voltage into a bad loaded voltage, so measure the symptom directly:

1. Fully charge the pack, rest it 15 minutes, record **resting voltage**. A healthy fresh 12 V NiMH pack reads well above 13 V.
2. Apply a fixed, repeatable load — e.g. all drive motors at 60 % against a wall for 3 seconds — and record the **minimum voltage** the Control Hub reports.
3. The number you care about is **sag = resting − minimum**. Log it per pack, per month.
4. **When one pack's sag is clearly worse than your other packs', that pack is done for competition.** You do not need the absolute mΩ figure; you need the ranking, and the ranking is free.

⚠️ Do this on blocks or against a wall with a spotter, never by driving, and do not repeat it many times in a session — you are deliberately stressing the pack.

#### 5.1.6 Voltage sag and why it wrecks autonomous repeatability

**[JUDGMENT]** This is the mechanism nobody explains to students, and it accounts for most "but our auto worked at home" stories.

A NiMH pack is a voltage source with internal resistance. Under load, terminal voltage drops by roughly `I × R_internal`. Everything downstream scales with that:

| What changes when the pack sags | Consequence for autonomous |
|---|---|
| Motor free speed is roughly proportional to applied voltage | A time-based or open-loop drive step travels **less far**. A 24-inch move becomes 21 inches. |
| Torque per unit of commanded power falls | Acceleration ramps stretch; a profile tuned at 13.4 V undershoots at 12.0 V. |
| A velocity PIDF's feedforward is calibrated in volts, implicitly | The feedforward is now wrong by the sag fraction and the integrator has to make it up — which it does late. |
| Servos move slower and hold with less force | Sequenced timing that "just barely" worked now misses its window. |
| Deep sag browns out the control system | Hub reboot mid-auto. REV warns that discharging below **9.0 V no-load** damages cells. |

**Three rules that follow, and they cost nothing:**

1. **A fresh pack goes in before every autonomous tuning session and before every match.** Autonomous is tuned at one voltage; run it at that voltage.
2. **Put battery voltage on the Driver Station telemetry, top line, always.** Then the first question at any failure is already answered.
3. **Log voltage into every run's CSV (§4.4) and check it before you change a single gain.** ⚠️ The commonest wasted weekend in FTC is retuning a perfectly good autonomous against a decaying battery.

**[JUDGMENT] Drill G in §3.4 exists precisely for this.** Your drivers must have felt an 11.5 V robot in practice, because they will drive one in match 6 of a qualifier.

**[FACT — LOCAL] E510** additionally forbids heating or cooling ROBOT components to gain an advantage — *"Heating batteries to increase their performance"* is named explicitly. A pack merely warm from its normal charge cycle is fine.

### 5.2 Fastener discipline

**[FACT — WEB]** GM0's fastener guide: *"Bolts on your robot may loosen over time, especially if there are heavy vibrations. It is highly recommended that teams use Loctite on all motor and servo mounts, as well as any mechanism prone to vibration."* Nyloc nuts are recommended broadly. ⚠️ **Blue or red Loctite must not contact polycarbonate — it is known to crack the plastic**; use a cyanoacrylate-based product or nylon-patch screws there. Note also that bottle colour is reversed from fluid colour: blue Loctite ships in a red bottle. ([GM0 Fastener Guide](https://gm0.org/en/latest/docs/hardware-components/fastener-guide.html))

**[FACT — LOCAL]** FIRST takes the same line for field structures: *"There are no specifications for torquing the various fasteners… all fasteners should be fully tightened"*, with nylocks run until no threads show between head and nut (`manuals/archive/supplemental/2025-26_DECODE_EventFieldSetupGuide.pdf`).

**[JUDGMENT] Where fasteners actually come loose on an FTC robot, ranked:**

| Rank | Location | Why it loosens | Prevention | How you notice |
|---|---|---|---|---|
| 1 | **Motor and gearbox mounting screws** | Torque reversals every cycle | Blue threadlocker + correct-length screw | Witness mark broken; motor rocks by hand |
| 2 | **Set screws on shaft collars, hubs, sprockets, pulleys** | Point contact on a round shaft plus vibration | Threadlocker on every set screw; use the shaft flat if the vendor provides one; two screws at 90° where possible | Mechanism gains slop but the motor still turns |
| 3 | **Odometry / dead-wheel pod mounts** | Light structure, constant road vibration | Nylock + threadlocker; check every session | Odometry drift appears suddenly |
| 4 | **Intake compliance-wheel hubs** | Highest impact loading on the robot | Threadlocker; spares in the kit | Intake "sometimes" misses |
| 5 | **Extrusion-to-extrusion structural bolts** | Preload creep in aluminium | Nylock, not plain nut; re-torque before each event | Chassis racks; wheels no longer square |
| 6 | **Electronics mounting plates** | Nobody ever checks them | Nylock; do not over-tighten into plastic | Rattle; hub moves relative to frame |
| 7 | **Wheel retention screws / hex hubs** | Direct impact loads | Threadlocker | Wheel wobble under load |

**[JUDGMENT] The fastener lap — 20 minutes, twice a season minimum, plus the night before every event:**

```
1. Robot on blocks, battery OUT, main switch OFF.
2. One student, one hex driver set, one direction of travel around the robot.
   Never two people at once - you will lose track of what has been checked.
3. Touch EVERY fastener. Not "look at" - touch it with a tool.
4. Mark each checked fastener with a paint-pen witness line across head and part.
   Next lap, a broken line = it moved = it gets threadlocker.
5. Any screw that turns more than ~1/8 turn: remove, threadlock, refit.
6. Log the count. "3 loose this lap." A RISING count is a design problem, not a
   maintenance problem - that joint needs redesigning, not re-tightening.
```

**Consumables [JUDGMENT; prices UNVERIFIED]:** blue threadlocker ~$8–12 at any hardware store, paint pen ~$4, an M3/M4 nylock assortment under $15. Under $35 for the season, and the highest-return $35 in this document.

### 5.3 Wiring and connector failure modes

**[JUDGMENT]** Connectors fail far more often than wire does. Every connector is a hinge, and hinges fatigue.

**[FACT — WEB]** From the official [FTC Robot Wiring Guide](https://ftc-docs.firstinspires.org/en/latest/robot_building/wiring_guide/wiring-guide.html) and [GM0 Wiring Tips and Tricks](https://gm0.org/en/latest/docs/power-and-electronics/tips-and-tricks.html):

| Failure mode | What the source says | Fix | Cost |
|---|---|---|---|
| **XT30 connectors break** | GM0: *"The traditional XT30 connector that is used to REV is prone to breaking."* | Adapt to Anderson Powerpole (`REV-31-1385` XT30↔Powerpole adapter) or replace; add a printed strain-relief shell at the hub | ~$0 printed / ~$5 adapter |
| **XT30 pins compress and go loose** | Wiring Guide: check XT30 connectors for snug fit — over time male pins compress and cause looseness | Check fit at every fastener lap; replace loose pairs | ~$2/pair |
| **Battery Tamiya connectors degrade** | GM0: Tamiya connectors on FTC-legal batteries are *"very weak and prone to becoming unreliable after many repeated plug/unplug cycles"* | Crimp Anderson Powerpole onto the battery — legal under **R601.B** | ~$3/pack |
| **USB / OTG disconnect mid-match** | GM0 driver-station guide: generally caused by *"poor quality cables/adapters between the driver station and the gamepads"* | Short known-good cables; right-angle connectors; REV USB strain relief; tape the joint | ~$10 |
| **Driver Hub USB port damage** | REV: most commonly caused by *"wrap[ping] USB cables that are plugged in around the Driver Hub"* | Unplug before coiling. Put it in the runbook as a line item | $0 |
| **Wire fatigue at the connector** | Wiring Guide: *"Immobilize the wire an inch or two from the connector and leave a little slack on the connector side."* | Zip tie 1–2 in back from every connector, with a slack service loop | $0 |
| **Wires crossing moving joints** | Wiring Guide: use **service loops** sized for the full range of motion; split sheathing anchored at both ends | Design it in; do not tape it on later | ~$8 loom |
| **Signal corruption from motor wiring** | Wiring Guide: route motor/servo wires away from USB cables | Physically separate the two bundles | $0 |
| **ESD kills Wi-Fi or I2C** | FTC Docs: ESD between foam tiles and robot causes *Wi-Fi disconnects from the Control Hub* and *disruption or damage to the I2C port*; arcs jump *"more than 3/8 in (1 cm)"*; below 30 % RH, ESD events are **3× more common** than above 50 % RH | Ferrite chokes on USB / sensor / encoder / servo cables; ≥3/8 in air gap or tape between connectors and metal frame; mount electronics on plywood or PVC; use the **USB 3.0** port on the Control Hub, not USB 2.0; approved grounding strap `REV-31-1269` (~$5) | ~$15 |

⚠️ **[FACT — WEB]** A grounding strap alone is **not** a guaranteed ESD fix — FTC Electrical's testing found straps without additional filtering produced inconsistent results. Ferrites *plus* isolation *plus* the strap, together. ([Managing Electrostatic Discharge Effects, FTC Docs](http://ftc-docs.firstinspires.org/hardware_and_software_configuration/configuring/managing_esd/managing-esd.html); [ftcelectrical.org](https://ftcelectrical.org/))

**[FACT — LOCAL]** Two BIOBUZZ V0 rules inspection will actually check:

- **R609 — minimum wire sizes.** **18 AWG** (19 SWG / 1 mm²) for 12 V main battery power and motor power; **22 AWG** (0.5 mm²) for 11–20 A fuse-protected circuits and for TETRIX MAX / REV Core Hex (`REV-14-1300`) motor power; **28 AWG** (0.08 mm²) for PWM/servo, LEDs, 10 A fuse-protected circuits and signal-level circuits. Manufacturer-integrated wiring is exempt. ⚠️ *"Combining multiple smaller wires in parallel cannot be used to create an equivalent larger wire."*
- **R610 — colour coding** on the 12 V main and +5 V aux buses: positive must be red, yellow, white, brown, or black-with-stripe; negative must be black or blue. Motor, encoder, sensor and servo wiring is exempt.

### 5.4 The spare-parts kit — what is actually in the box

**[FACT — LOCAL]** The rule that makes spares cheap: **I303** says re-inspection is *generally not necessary* for *"replacement of a COMPONENT with an identical COMPONENT"* or *"replacement of a MECHANISM with an identical MECHANISM (size, weight, material)"*. **A true like-for-like spare can go on the robot between matches without going back through inspection.** A *different* part cannot.

**[JUDGMENT] Tier the kit. A small team should not buy a spare of everything.**

| Tier | Contents | Approx. cost (Aug 2026; **[UNVERIFIED]** unless SKU-priced above) | Rationale |
|---|---|---|---|
| **Tier 0 — free, do this first** | Every offcut, every removed bracket, the old prototype intake, last year's chassis, all screws recovered from disassembly — in labelled bins | **$0** | Most pit repairs are solved by a bracket you already own |
| **Tier 1 — must have** | 3rd battery; 2 spare XT30 pigtails; 2 motor power cables; 2 servo extensions; 1 spare servo of your most-used model; 1 spare gamepad; full assortment of your two screw sizes + nylocks; zip ties; electrical tape; blue threadlocker; spare 20 A ATM fuses; **2 spare printed & laminated ROBOT SIGNS** | **~$150–200** | These are the parts that fail and cost you a match |
| **Tier 2 — should have** | 1 spare motor of your most-used type; 1 spare drive wheel + hub; spare chain/belt at your exact length plus a **chain breaker**; spare intake compliant wheels; spare encoder cable; spare USB cable; ferrite chokes | **~$150–250** | Buys back a match you would otherwise sit out |
| **Tier 3 — nice to have** | Spare Expansion Hub; spare Control Hub; second Driver Station device (legal as a *spare* under **R901** provided only one is connected and powered at a time) | **$300–600** | ⚠️ Only after Tiers 1 and 2. A spare Control Hub is a luxury; a third battery is not |

**[FACT — WEB]** GM0 on chain: **master links are unreliable** — *"There have been teams who have had master chain links fail during competition, costing them a match in the elimination rounds"* — and GM0 recommends buying a chain breaker instead. ([GM0 chain](https://github.com/gamemanual0/gm0/blob/main/source/docs/common-mechanisms/power-transmission/chain.rst)) **[JUDGMENT]** A chain breaker is roughly $20–30 (**[UNVERIFIED]**) and belongs in Tier 2 for any chain-driven robot.

**Tool kit [JUDGMENT], the honest minimum:** hex drivers covering every fastener on your robot (buy **two** of the size you use most — one will walk off), small ratcheting wrench set, needle-nose pliers, flush cutters, small file, zip-tie snips, multimeter, crimper if you crimp your own connectors, soldering iron, paint pen, sharpie, masking tape, tape measure, and a printed copy of §10.

**[FACT — LOCAL] Pit tooling rules.** **E505** allows only small benchtop machinery — *"machinery that can be easily lifted by one person"* (3D printers, small band saws, small drill presses, desktop CNC mills, sanders); floor-standing power tools are prohibited. **E506** prohibits brazing and welding. **E508** allows soldering *"using an electric iron/gun only."* **E504** restricts open flames and spark-throwing tools. **E509** restricts aerosols and noxious chemicals to approved areas.

### 5.5 The pre-match checklist — design principles

**[JUDGMENT]** The physical checklist lives in §9. What matters here is *how* to build one that survives contact with a nervous fifteen-year-old at 9:40 a.m.

| Principle | Why |
|---|---|
| **One page, one column, physical paper on a clipboard** | Phones die, get borrowed, and are a wireless liability near the field (**R904**, **E301**) |
| **Binary items only** — "battery ≥ 13.0 V", not "check battery" | A checklist with judgement in it is not a checklist |
| **One named runner reads aloud; a second person performs** | Read-and-do by one person is exactly how items get skipped |
| **The list ends with an initial** | Ownership is the mechanism; the paper is just the medium |
| **Never lengthen the list after a failure without deleting something** | A 40-item list gets skipped entirely; a 12-item list gets done |
| **Rehearse it cold, on a timer, weekly** (Drill J) | The list is a skill, not a document |

### 5.6 Post-match triage in the pit

**[FACT — LOCAL]** You have less time than you think. In DECODE, **T206** guaranteed only a **5-minute minimum** between back-to-back qualification matches (**8 minutes** in playoffs), measured from results posting to the next expected start; **G301** defined the expected start as the scheduled time or **~3 minutes after the previous match on that field**, whichever is later. ⚠️ BIOBUZZ Section 13 is a placeholder in V0 — re-verify at kickoff, but plan around these numbers.

**[JUDGMENT] The three-minute triage — run it every single match, win or lose:**

| Min | Who | What |
|---|---|---|
| 0:00 | Drive team | Robot on the cart, straight to the pit. **No debrief on the walk.** |
| 0:00–0:30 | Technician | Battery out, into the cooling slot. Fresh pack staged, not yet installed. |
| 0:30–1:30 | Technician | **Hands-on sweep in a fixed order**: wheels → intake → scoring mechanism → wiring → the fasteners you know are marginal. Same order every time. |
| 0:30–1:30 | Scout / coach | Write the match record: score, cycles, **one failure observed**, **one thing to change**. |
| 1:30–2:00 | Whole crew | **Triage decision** (below). |
| 2:00–3:00 | Technician | Execute the decision — or don't. Fresh pack in, power-on test, mechanism range test. |
| 3:00 | Runner | Robot staged, checklist ready, queue when called. |

**[JUDGMENT] The triage decision rules. Write them down, because in the moment nobody thinks clearly:**

1. **Did it stop us scoring?** No → **do not touch it.** It goes on the "after the event" list.
2. **Do we have an identical spare and a rehearsed sub-5-minute procedure?** No → **do not attempt it now.** Play the next match degraded; fix it during the lunch break.
3. **Does the fix change size, mass, materials, or add a part that was never inspected?** Yes → **it needs re-inspection (I303)** before the next match. Budget the walk to the LRI.
4. **Never change two things at once.** You will not know which one worked, and you have doubled the chance of introducing a new failure.
5. **Never change code and hardware in the same turnaround.** Pick one.
6. **After any change, run the mechanism through its full range on the cart before the robot leaves the pit.** Thirty seconds; catches most of what triage breaks.
7. **If the robot is fine, the crew rests.** ⚠️ A small team's real failure mode is three exhausted students by match 4. Idle hands in the pit are correct behaviour, not laziness.

---

## 6. Failure-mode catalogue

**[JUDGMENT]** Everything below is either sourced (marked inline) or is a recurring pattern worth designing against. Use the **Prevent** column during build season and the **Field fix** column on the day. ⚠️ Rule numbers prefixed **G**/**T** are from DECODE (2025-26) because BIOBUZZ Sections 11 and 13 are placeholders in V0 — re-verify every one of them on kickoff morning.

### 6.1 Power and electrical

| Failure | Symptom on the field | Root cause | Prevent | Field fix |
|---|---|---|---|---|
| **Sagging / worn pack** | Auto drifts short; robot "feels slow" late in the match; late-match brownouts | High internal resistance from age and cycles | IR or sag ranking (§5.1.5); retire at goBILDA thresholds | Swap pack. **Do not retune** |
| **Under-charged pack** | Same, but only in one match | Rotation broken; pack pulled early | Written rotation; voltage logged before every match | Swap pack |
| **Brownout / hub reboot mid-match** | Robot dies and comes back; DS shows a reconnect | Deep sag under stall — a mechanism grinding against a hard stop | Current limits in code; do not stall against hard stops (**R103** warns about thermal failure while holding STARTING CONFIGURATION for minutes) | Fresh pack; find and relieve the stall |
| **Blown 20 A battery fuse** | Robot completely dead | Short, or sustained over-current | Correct routing; no pinch points | Replace with a COTS 20 A ATM mini blade **only** — **R604/R605** forbid higher-rated or self-resetting fuses |
| **Main switch failure or knocked off** | Robot dies on contact | Switch exposed to robot-to-robot contact | **R603** — mount clear of moving parts, protected from contact | Replace with an approved switch (Table 12-5) |
| **XT30 backing out** | Intermittent total power loss | Compressed pins; no strain relief | Strain-relief shells; fit check every fastener lap | Replace the pair |
| **ESD Wi-Fi disconnect** | Robot drops link at one particular field, or on a dry day | Static between tiles and frame | Ferrites + isolation + USB 3.0 port + approved grounding strap (§5.3) | Move USB to the 3.0 port; add ferrites; tell the FTA |
| **I2C port killed by ESD** | One sensor permanently dead | Same | Same | Move the sensor to another port; re-map the config |

### 6.2 Control system and software

| Failure | Symptom | Root cause | Prevent | Field fix |
|---|---|---|---|---|
| **Gamepad disconnect mid-match** | One driver loses control | Poor-quality USB/OTG cable or hub — GM0 names this explicitly | Short known-good cables; strain relief; spare gamepad in Tier 1 | Swap cable, then gamepad. Rehearse the swap |
| **Driver Hub USB port broken** | Nothing works at the console | Cables wrapped around the Hub while plugged in (REV) | Unplug before coiling — runbook line item | Spare DS device, legal per **R901** if only one is connected and powered |
| **Wi-Fi congestion / high ping** | Laggy driving that "wasn't like this at home" | 2.4 GHz saturation at events; GM0 warns school Wi-Fi crowds this band | Expect it; test on 5 GHz; **R704.E** — use the band or channel event staff assign | Ask the FTA. Do not fight it yourself |
| **Device named wrong** | Cannot connect at the field | Names never set | **R705** — `<team>-RC`, `<team>-DS`, spares `<team>-A-DS` | Rename. It is a config screen, not a rebuild |
| **Default Control Hub password** | Inspection failure | Never changed | **R711.A** — the Control Hub Wi-Fi password must be non-default | Change it; also disable Bluetooth (**R711.C**) and clear stale Wi-Fi Direct groups on the DS (**R711.D**) |
| **Laptop still on the robot network during a match** | Rules violation; possible interference | Programmer forgot | **R704.C** — all non-DS devices off the RC network during MATCH play | Disconnect. Make it a checklist line |
| **Dashboard / Panels streaming at an event** | ⚠️ Rules violation | Live-telemetry habit carried over from practice | **R704.D** explicitly prohibits *"Additional logging/streaming services, such as those hosted by third party plugins and tools such as FTC Dashboard, FTControl Panels, and others"*, and *"No continuous video stream is allowed"* | Build the season around **file logging** (§4.4); see `research/PROGRAMMING-PRACTICE.md` §1.2 |
| **No OpMode selected / INIT not pressed** | Match will not start; possible DISABLED | Ritual never rehearsed | Drill J; runbook line | DECODE **G305** required an OpMode selected *and* INIT pressed regardless of whether an auto was planned |
| **Wrong OpMode selected** | Auto scores nothing or crosses the field | Ambiguous names under pressure | Name OpModes so they sort in match order and read unambiguously on a 5-inch screen | Re-select. Then rehearse |
| **Loop-time creep** | Robot "feels laggy"; control loops degrade | Blocking calls, per-loop hardware reads, logging in the hot path | Log `loop_time_ms` on every run (§4.4) | Nothing on the day — this is a build-season fix |
| **Self-inspect screen warnings** | Inspection stalls | RC/DS app version mismatch | Update both to the same SDK version well before the event | Update at the event only if you have a laptop and spare time |

### 6.3 Drivetrain

| Failure | Symptom | Root cause | Prevent | Field fix |
|---|---|---|---|---|
| **Set screw backed out of a wheel hub** | Motor spins, wheel doesn't; robot pulls to one side | Point contact + vibration | Threadlocker on every set screw; use the shaft flat | Retighten with threadlocker. Two minutes |
| **Chain master-link failure** | Drive or mechanism dead mid-match | Master links are *"not very reliable"* (GM0) | Chain breaker and a continuous chain | Spare chain of the exact length, in the kit |
| **Belt skipping teeth** | Position drift on a belt-driven mechanism | Insufficient tension; no idler | Tensioner designed in; check at every fastener lap | Re-tension |
| **Odometry pod knocked out of alignment** | Localization drift that gets worse across the event | Light mounts; robot-to-robot contact | Rigid, protected mounts; nylock + threadlocker | Re-seat, then **re-run a straight-line calibration** before trusting auto again |
| **Tread worn or glazed** | Loses traction late in the event | Tile abrasion | Inspect between matches; spare wheel in Tier 2 | Swap an identical wheel — no re-inspection needed (**I303.E**) |
| **Robot cannot be removed from the field powered off** | Field reset delay; possible rules issue | Mechanism design | **R203** requires removing both SCORING ELEMENTS and the robot while powered off | Design fix only. Find this in October, not in January |

### 6.4 Mechanisms

| Failure | Symptom | Root cause | Prevent | Field fix |
|---|---|---|---|---|
| **Intake misses on approach** | ⚠️ The most common real cycle-time killer (§4.1) | Alignment tolerance tighter than a human driver can hit | Widen the lead-in; add compliance; add a driver alignment aid | Drills D and E. This is not a pit fix |
| **Jam at hopper capacity** | Works at n = 1, fails at n = 5 | Never tested at capacity | Buy enough Pollen to test full-capacity cycles (§2.4.3) | Clear it, log it, redesign later |
| **Compliant wheel spins on its hub** | Intake "sometimes" works | Set screw or press fit failed | Threadlocker; spares in the kit | Replace |
| **Servo stripped or drifting** | Mechanism no longer reaches its endpoint | Over-travel into a hard stop; sustained stall | Software endpoints set inside the mechanical endpoints | Swap identical servo; re-set endpoints |
| **Stored energy surprises an inspector** | Safety incident at inspection | Springs stretched in the inspection configuration | ⚠️ **Section 3.3.1 explicitly asks teams to tell INSPECTORS about stored energy** and about needing the robot powered/enabled | Tell them *first*. Every time |
| **Sharp edge or protrusion** | Inspection failure | Cut aluminium; exposed screw ends | **R201/R202** — deburr everything, cap exposed threads | File and tape at the event |
| **Something falls off on the field** | Foul; possible damage | Loose ballast or unsecured decoration | **R201** names loose ballast — sand, coffee beans, kitty litter, glitter, ball bearings — explicitly | Remove it before the match |

### 6.5 Human and process

| Failure | Consequence | Prevent |
|---|---|---|
| **Late to the field** | DECODE **G301**: VERBAL WARNING → MAJOR FOUL on repeat → DISABLED if not match-ready within 2 minutes | Runbook §9; a named runner watching the queue; leave when called, not when ready |
| **Wrong ROBOT SIGN colour** | Match will not start (DECODE **G303.E**) | Reversible signs that cannot show both colours (**R402**); checklist line; two spare printed signs |
| **Robot not in STARTING CONFIGURATION** | Match will not start; DISABLED if not a quick remedy (DECODE **G304**) | Rehearse setup cold (Drill J); use a legal alignment device — DECODE **G302** explicitly allowed one |
| **Safety glasses missing** | Removed from the pit and the field | **E101.A** — ANSI/UL/CE EN166/AS-NZS/CSA rated. Only a **10-minute grace period** when the venue opens each day. Buy 4 spare pairs |
| **Only one adult present** | Eligibility problem | **I103** — at least one, preferably two, responsible adults present at all times |
| **Check-in missed** | Not on the match schedule at all | **I102** — an adult must check in **no later than 45 minutes** before quals start, with at least one student at the venue |
| **Three exhausted students by match 4** | Errors compound; triage quality collapses | Written roles (§7.3); mandatory idle time; food and water in the pit |

---

## 7. Competition-day operations for a small team

**[JUDGMENT]** The thesis of this section: a five-person team can run an event *well*, but only if every role is written down before load-in and nobody improvises. The failure mode is never "too few people". It is "all four people crowded around the same wheel while nobody is watching the queue display".

### 7.1 Inspection — pass it on the first try

#### 7.1.1 What the process actually is

**[FACT — LOCAL]** From `manuals/2026-27_BIOBUZZ/sections/03_Eligibility_Inspection_I_p22-26.txt`, Section 3.3.1:

- Inspection is *"often one of the first activities a team experiences upon arrival"*. Some events assign **specific inspection time slots**; others schedule a **general span of time**. **Teams are responsible for completing inspection within the scheduled time.**
- **Students** present the ROBOT, all COMPONENTS it will use, and the OPERATOR CONSOLE.
- The **LRI has final authority** on eligibility for Qualification and Playoff matches on ROBOT construction matters.
- Teams **may power on and enable** the robot during inspection to demonstrate compliance — and **should tell inspectors** if they need to, and **should tell inspectors about stored energy** (e.g. stretched springs). ⚠️ This is written into the manual as a collaboration expectation; volunteering it makes you look competent, hiding it makes you look evasive.
- ⚠️ *"Inspection is not comprehensive. Teams are expected to adhere to the spirit of the rules in Section 12… even if INSPECTORS do not check every part of the ROBOT."* Strategically circumventing construction rules is a **Competition Integrity Contract** matter, not a loophole.
- **I301** — bring the complete robot and supporting equipment, **including decorative parts**, and demonstrate **all** match configurations.
- **I302** — the electronics limits apply **across all configurations combined**, not per configuration.
- **I303** — re-inspection is required for most changes, but explicitly **not** for: fasteners (cable ties, tape, rivets), labelling/marking, the team SIGN, **ROBOT code revisions**, an identical COMPONENT, an identical MECHANISM, or reconfiguring with a subset of already-inspected mechanisms.
- **I304** — do not exploit re-inspection to circumvent other rules.
- **Practice matches:** teams may play *scheduled* practice matches before passing inspection, but **not unscheduled or "filler line" practice matches**. The FTA, LRI or Head Referee may bar an unsafe robot from any practice match.

**[FACT — LOCAL] The scheduling weapon, restated from §2.5.** **E116**: *"A team may only use a practice FIELD with a ROBOT that has passed an initial, complete inspection. This rule only applies to events not using scheduled inspection times."* At an open-inspection event, **inspection is the gate on practice-field access**, and practice-field minutes are the scarcest resource of the day.

#### 7.1.2 How to pass first try — the four-step method

**[JUDGMENT]**

| Step | When | What |
|---|---|---|
| **1. Self-inspect against §10** | **Two weeks before the event** | Run the full checklist with the robot on the bench. Two weeks gives you time to *order a part*. This is the step that matters most and the one everybody skips. |
| **2. Self-inspect again** | **The night before**, after the final fastener lap | Same list, same order, different student reading it. Fresh eyes catch the sign that got unscrewed. |
| **3. Measure, don't estimate** | Night before | Build or borrow an **18 in cube sizing box** from scrap plywood or cardboard and put the robot in it. ⚠️ "It looks like it fits" fails at events. |
| **4. Arrive early and go straight to inspection** | Doors open | Not after you unpack. Not after breakfast. **First.** Then you own the practice field (E116) while everyone else is still setting up their pit. |

#### 7.1.3 The BIOBUZZ-specific traps for 2026-27

⚠️ **[FACT — LOCAL]** These changed, and last season's checklist will fail you:

| Trap | Last season (DECODE) | BIOBUZZ V0 | Where |
|---|---|---|---|
| **Servo count** | 8 motors / **10 servos** | 8 motors / **8 servos** | **R503** |
| **Operator console depth** | 3 ft × **1 ft 2 in** × 2 ft | 3 ft × **1 ft 6 in** × 2 ft, *including all power sources such as power banks* | **R903** |
| **Expansion limits** | R105 gave explicit horizontal and height limits | ⚠️ **NOT PUBLISHED.** R105 says only *"Sizing Constraints and more details will be released at Kickoff"* | **R105** |
| **Rule numbering** | Main switch = R609, wire size = R615, colours = R616, console = R904 | Main switch = **R603**, wire size = **R609**, colours = **R610**, console = **R903** | §12 |
| **Weight limit** | none | still none — **R104** confirms *"There is no explicit weight limit"* | **R104** |

> ⚠️ **[JUDGMENT] Do not commit to an extension geometry before 12 September 2026.** R105 is the single most design-consequential unpublished rule in the V0 manual. Design the *interfaces* now; freeze the *reach* after kickoff.

#### 7.1.4 The failures inspectors actually catch

**[JUDGMENT]**, informed by the structure of the official checklist (`manuals/archive/supplemental/2025-26_DECODE_InspectionChecklist.pdf`):

| Failure | Fix time at the event | Prevent |
|---|---|---|
| ROBOT SIGNS too small, wrong colour, or only one | 10 min if you brought spares; an hour if you didn't | Two laminated spares in the kit (**R401–R403**) |
| Team number wrong size, stacked vertically, or powered/edge-lit | 15 min | **R403** — solid opaque white digits ~2.25 in tall, ≥0.25 in of background around them, **not vertically stacked**, **not powered** |
| Robot does not fit the 18 in cube | Anywhere from 5 min to fatal | Build a sizing box (step 3 above) |
| Exposed sharp edges | 10 min with a file | Deburr during build |
| Wire colour non-compliant on the 12 V bus | 20–40 min re-wiring | **R610** from day one |
| Wire gauge undersized / unlabelled | Can be fatal — you may not have compliant wire | **R609**; buy labelled wire; keep offcuts as evidence |
| Default Control Hub Wi-Fi password | 5 min | **R711.A** |
| Devices not named `<team>-RC` / `<team>-DS` | 5 min | **R705** |
| Self-inspect screen shows red warnings | 20 min–fatal without a laptop | Match RC and DS app versions before you leave home |
| Extra motors/servos across "all configurations" | Fatal for that mechanism | **I302** + **R503** — count them on paper, across every configuration |
| Grounding done with a non-approved cable | 10 min | **R605** — only `am-4648a`, `REV-31-1269`, or `SR-Ground-01`, connected to a fully COTS XT30 component |

### 7.2 Pit setup

**[FACT — LOCAL]** The governing rules, all from `sections/05_EventRules_E_p33-42.txt`:

| Rule | What it means for your layout |
|---|---|
| **E501** | No pit access outside designated hours. Plan for **no overnight access** and no overnight power at multi-day events. |
| **E502** | Everything must be **fully within your assigned pit space**. No running power or network lines to anywhere else; no swapping or squatting in empty pits. |
| **E503** | Aisles and exit pathways stay clear. |
| **E507** | No structure that supports a person's weight or stores items overhead; nothing that blocks sprinklers. Popup tents may violate this. |
| **E601** | Carts must be easy to control, safe, **fit through a 30-inch door**, **stay in the pit when not in use**, have **no sound devices**, and **no powered propulsion**. |
| **E702** | **No more than 5 team members in the pits during ceremonies.** |
| — | *"Team pits may or may not have a table and power outlet."* If individual outlets aren't provided, the venue must provide team-usable outlets for charging. |

**[FACT — WEB]** A regional's own checklist confirms the practical version: bring a **power strip** (one outlet is typical), **two ROBOT SIGNS (red and blue)**, a printed **team roster from the FIRST dashboard**, and **ANSI Z87.1 safety glasses — no exceptions**, with side shields or goggles over prescription lenses. ([Pennsylvania FTC Event Checklist](https://www.ftcpenn.org/event-checklist))

**[JUDGMENT] A small-team pit layout that works in a 10 ft × 10 ft box:**

```
        +---------------------------- pit boundary (E502) --------------+
        |  BACK WALL: team banner + printed match schedule + role card  |
        |                                                               |
        |  [ BATTERY STATION ]        [ WORK SURFACE / TABLE ]          |
        |  2 chargers, 3 packs,       tools in ONE open tray,           |
        |  cooling slot, log sheet    robot lives HERE between matches  |
        |  (near the outlet)                                            |
        |                                                               |
        |  [ SPARES BIN ]             [ CART - parked, E601.D ]         |
        |  labelled, Tier 1 on top                                      |
        |                                                               |
        |  ------ AISLE SIDE: keep clear (E503), judges approach here --|
        +---------------------------------------------------------------+
```

**[JUDGMENT] Five pit rules that save a small team an hour a day:**

1. **One tool tray, open, always in the same place.** Not a closed toolbox. Not three bags.
2. **The robot lives on the table, not the floor, not the cart.** The cart is transport only.
3. **The battery station is a station** — chargers, packs, log sheet, all together, next to the outlet, and nobody else's stuff on it.
4. **Print the match schedule the moment it is posted** and tape it at eye height with your matches highlighted. **[FACT — LOCAL]** DECODE §13.6.1: the schedule is available *"no later than 15 minutes before Qualification MATCHES are scheduled to begin"*.
5. **Print the role card (§7.3) and the runbook (§9) and tape them next to the schedule.** Roles that live in someone's head do not survive a bad match.

### 7.3 Role assignment for 4-10 students

**[FACT — LOCAL, prior season]** DRIVE TEAM composition (DECODE §10.2, and expect BIOBUZZ Section 10 to be similar — it is a **placeholder in V0**): *"up to 4 people from the same FIRST Tech Challenge team"*, of whom **no more than 1 may be a non-STUDENT**. Roles: **DRIVE COACH** (1, may be an adult, badge required), **DRIVER** (up to 3, students), **HUMAN PLAYER** (student, within the 4 total).

**[FACT — WEB]** Community consensus for small teams, from Chief Delphi's FTC forum (retrieved via search snippet; direct fetch blocked): a workable split is *"3 students on the drive team, a few more in the pit, and a few more going around to look at and talk to other teams"* ([Competition Roles for Students](https://www.chiefdelphi.com/t/competition-roles-for-students/416788)).

**[JUDGMENT] The six jobs that must exist at an FTC event, regardless of headcount:**

| # | Job | Non-negotiable duty | Can be doubled with |
|---|---|---|---|
| **J1** | **Driver(s)** | Drive. Nothing else, in the 20 minutes before a match. | Nothing |
| **J2** | **Drive coach** | Alliance strategy, field state, clock (§3.3). | Scouting lead, between matches |
| **J3** | **Technician** | Battery swap, triage sweep, all hands on the robot. **Only this person touches the robot in the pit** unless they ask for help. | Programmer |
| **J4** | **Checklist runner / queue watcher** | Reads the pre-match checklist aloud; watches the queue display; owns "we leave now". | Human player |
| **J5** | **Scout / recorder** | Match record, cycle count, one failure, one fix. Feeds alliance selection. | Drive coach between matches |
| **J6** | **Judging & logistics** | Portfolio, interview readiness, food, water, adult liaison, ceremonies. | Adult mentor (this is the one job an adult should own outright) |

**[JUDGMENT] Mapping jobs to real headcounts:**

| Students present | Assignment | What you consciously give up |
|---|---|---|
| **3 students + 1 adult** | S1 = driver. S2 = coach + scout. S3 = technician + checklist runner. Adult = J6. | Live match scouting; you scout from ftcscout.org between matches instead (§4 of `research/SCOUTING-AND-AWARDS.md`). |
| **4 students + 1 adult** ⭐ | S1 driver, S2 driver/human player, S3 coach, S4 technician + runner. Adult = J6 and **drive coach only if you must**. | Dedicated scouting; rotate S4 out for the interview. |
| **5–6 students** | Full drive team (2 drivers + coach + human player), 1 technician, 1 scout/runner. | Nothing critical. This is a complete event crew. |
| **7–10 students** | As above, plus a second technician, a dedicated pit-scout (walks the pits with a phone), and a judging pair who stay near the pit. | Nothing. |

⚠️ **[JUDGMENT] Two hard rules that make small crews work:**

1. **One hand on the robot.** When the technician is working, everyone else stands back and *hands them things*. Four students converging on one problem is how a 3-minute fix becomes an 11-minute fix and a missed match.
2. **The queue watcher is never also the technician.** If the person watching the clock is head-down in the robot, you will be late — and DECODE's **G301** escalates lateness from a verbal warning to a MAJOR FOUL to DISABLED.

**[JUDGMENT] Rotate roles across the season, not across the event.** Cross-training is a build-season activity. On event day, everyone does the job on the printed card.

### 7.4 Match cadence — what actually happens, minute by minute

**[FACT — LOCAL, prior season]** From DECODE Section 13 (⚠️ BIOBUZZ Section 13 is a **placeholder in V0**; re-verify at kickoff):

| Fact | Rule |
|---|---|
| **All event types schedule 5 or 6 Qualification MATCHES per team**, at the Event Director's discretion. Championships may schedule more. | §13.6.1 |
| Match schedule published **no later than 15 minutes** before quals begin. | §13.6.1 |
| **Minimum 5 minutes** between your back-to-back qualification matches, from results posting to expected start. **8 minutes** in playoffs. | **T206** |
| Expected start = scheduled time, or **~3 minutes after the previous match on that field**, whichever is later. | **G301** |
| **The ARENA may be open for at least 30 minutes before quals** for measurement and sensor calibration. Robot may be powered, may init an OpMode, may extend mechanisms, may control scoring elements, may be connected to a laptop, and team members may be on the field with tape measures — **but the chassis may not move under its own power** and the human player may not practise. | **T205** |
| Match periods (DECODE): **30 s AUTO + 8 s transition + 2:00 TELEOP.** | §10 |
| Being **"MATCH ready"** = robot on the field, in STARTING CONFIGURATION, powered on, and drive team in their starting positions. | **G301** |
| An **alignment device** may be brought to the field to aid pre-match setup — it is explicitly *not* a violation of the "limit what you bring" rule, provided it does not delay the match. | **G302** |
| A **cart** may not have powered propulsion or sound devices, must fit a 30-inch door, and must stay in the pit when not in use. | **E601** |

> ⚠️ **[JUDGMENT] T205 is the second free lever of the day, after E116.** Thirty minutes of legal field-measurement time before quals, where you may power the robot, run init, extend mechanisms and put a tape measure on the field — and most small teams spend it eating a bagel. Send two people with the robot, a tape measure and a printed list of the four measurements your autonomous depends on.

**[JUDGMENT] A realistic small-team match cycle, anchored on your match start time T:**

| Clock | Who | What |
|---|---|---|
| **T−20 min** | Coach | One-sentence strategy agreed with both alliance partners. Written on a wrist card. |
| **T−15** | Technician | Fresh battery in. Power-on test. Full mechanism range check on the cart. |
| **T−12** | Runner + technician | **Pre-match checklist (§9), read aloud, performed by a second person, initialled.** |
| **T−10** | Drive team | Robot on the cart. Move to the queue. **Leave when called, not when finished.** |
| **T−10 → T−3** | Queue | Wait. ⚠️ **E106** — you may not practise outside your pit or the designated practice areas, and **may not set up your own practice equipment outside your pit**. **E110** allows limited work while queued but with *"extra scrutiny regarding safety."* |
| **T−3** | Drive team | On the field. Place robot, alignment device, pre-load. Select OpMode, press INIT. Hands off. |
| **T+0** | — | AUTO (30 s), transition (8 s), TELEOP (2:00). |
| **T+3** | Drive team | Robot off the field. Straight to the pit. **No debrief on the walk.** |
| **T+3 → T+6** | Whole crew | **Three-minute triage (§5.6).** |
| **T+6 → T+8** | Scout | Log the match. One failure, one fix. |
| **T+8** | Everyone | **Rest.** Water. Sit down. |

**[JUDGMENT] The arithmetic that surprises people:** at 5–6 qualification matches spread over roughly six hours, you have **~50–70 minutes of actual robot time** and **five hours of waiting**. Small teams lose events by filling that waiting time with unplanned robot changes. **Plan the waiting time**: scouting, judging prep, portfolio, food, and deliberate rest.

### 7.5 Judging interruptions, and how a small team survives them

**[FACT — LOCAL]** From `sections/06_Awards_A_p43-58.txt` §6.1.2–6.1.3:

- The Initial Interview format (in a judging room vs **in the pits**) is set by the Event Director and communicated before the event. ⚠️ *"the pit area is an active and often noisy environment."*
- For pit interviews, *"JUDGES will work with MATCH queuers and technical volunteers to ensure teams are able to attend MATCHES and work on their ROBOTS."*
- **The Judge Advisor selects two questions from the Judge Interview Question Bank that every team at the event will be asked** — one on the **MCI** award category, one on the **TA** category — before any follow-up questions.
- **Pit Interviews** may follow later, informally, during the competition.

**[JUDGMENT] What this means operationally for a crew of five:** judging will collide with a match at least once. Decide the collision rule *in advance*:

1. **The drive team is never the judging team.** If your interview group and your drive team are the same three people, you have designed a guaranteed conflict.
2. **The adult (J6) owns judging logistics** — knows the interview time, has the portfolio in hand, and physically walks the interview group there.
3. **Two students must be able to give the interview without the other two.** Rehearse it that way.
4. **Prepare the two mandated questions.** Because the Judge Advisor picks one MCI and one TA question that *every* team gets, preparing crisp two-minute answers on those two axes is unusually high-value. See `research/SCOUTING-AND-AWARDS.md` §7.
5. **Keep the pit presentable at all times** — pit interviews are unannounced.

### 7.6 The rest of the day

**[JUDGMENT]**

| Phase | What a small team should do |
|---|---|
| **Load-in** | Two people to inspection with the robot; two people build the pit. Do not do these sequentially. |
| **Between quals blocks** | Scout via ftcscout.org and the pit walk. Build the alliance-selection tier list (see `research/SCOUTING-AND-AWARDS.md` §6). |
| **Lunch** | This is your only real repair window. Bank the non-urgent triage items for it. |
| **Alliance selection** | Your list must already exist. This is not the moment to form opinions. |
| **Playoffs** | 8-minute minimum turnarounds. Batteries become the binding constraint — see §5.1.3. |
| **Ceremonies** | **E701/E702** — quiet in the pits, **max 5 team members in the pits**, everyone else in the stands. |
| **Load-out** | Photograph your pit before teardown for the portfolio. Pack the battery station last so packs keep charging as long as possible. |
| **That night** | ⚠️ **Video review (§4.5) the same night.** 25 minutes. This is the single most-skipped high-yield activity in FTC. |

---

## 8. PRINTABLE — the weekly testing protocol

> **Print one copy per week. Tape it to the wall next to the practice surface. It is finished when every box is ticked and every blank is filled in. If a blank is empty at the end of the session, the session did not happen.**
>
> Owner (one named student, rotates monthly): `________________`  ·  Week of: `____ / ____ / 2026`  ·  Robot config: `____________`

### 8.0 Before anyone touches the robot (5 min)

- [ ] Charged battery installed. **Resting voltage recorded:** `______ V` · Pack ID: `____`
- [ ] Two other packs on chargers / in the cooling slot
- [ ] Clipboard, stopwatch, tally sheet, whiteboard marker on the field-side table
- [ ] Phone on tripod behind the driver position, recording
- [ ] Last week's sheet on the wall, visible. **Last week's headline number:** `______`
- [ ] Read out loud: **"This week's one fix was `______________________`. Did we do it?"**  Yes / No

### 8.1 Bench block — no field required (20 min)

| # | Test | Pass criterion | Result |
|---|---|---|---|
| 1 | Power-on, no errors on either self-inspect screen | Zero red exclamation marks | ☐ pass ☐ fail |
| 2 | Every motor commanded individually, correct direction | All correct | ☐ ☐ |
| 3 | Every servo to both endpoints | No buzzing at the stop, no over-travel | ☐ ☐ |
| 4 | Every mechanism through full range on blocks | No binding, no rub, no wire pull | ☐ ☐ |
| 5 | Loop time at idle and under full command | `______ ms` idle / `______ ms` loaded | ☐ ☐ |
| 6 | Encoder counts sane on every axis (hand-turn, watch telemetry) | Monotonic, correct sign | ☐ ☐ |
| 7 | Camera/vision: accept and reject each produce a **logged reason** | Reasons appear in the log | ☐ ☐ |
| 8 | Wiring tug test — gentle pull on every connector | Nothing moves | ☐ ☐ |

**Anything failing here stops the session.** Fix it now; a field test on a broken bench is wasted.

### 8.2 Drivetrain and localization block (15 min) — needs tiles

| # | Test | Record | Target |
|---|---|---|---|
| 9 | Straight line, 8 ft, measured with a tape | Lateral error `______ in` | < 2 in |
| 10 | 360° in place ×4, return to start heading | Heading error `______ °` | < 5° |
| 11 | Square drive, 4 ft per side, back to start | Position error `______ in` | < 4 in |
| 12 | Odometry pose after test 11, off telemetry | Reported vs measured `______ in` | < 3 in |

⚠️ If 9–12 got **worse** than last week: **check the battery, then the odometry pod mounts, then fasteners** — in that order — before touching any code. (§4.6)

### 8.3 Autonomous block (20 min) — needs tiles + tape reference

- [ ] Fresh battery. **Resting voltage:** `______ V`
- [ ] Run the full autonomous **5 times consecutively** from the identical start pose.

| Run | End-pose error (in) | Points scored | Battery V at end | Anomaly |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Success rate this week: `___ / 5`.  Worst-case error: `______ in`.**

> **[JUDGMENT] The number that matters is the worst run, not the average.** An autonomous that works 4 times in 5 will fail you in the match that decides your ranking.

### 8.4 Drive-practice block (60 min) — the schedule from §3.4

| Min | Drill | Metric | This week | Last week | Δ |
|---|---|---|---|---|---|
| 0–5 | **J** Setup ritual, cold, timed | seconds / errors | | | |
| 5–10 | Free warm-up | — | — | — | — |
| 10–20 | **A** Timed cycle count ×3 | best cycles / 90 s | | | |
| 20–30 | Skill of the week: ☐ D ☐ E ☐ K ☐ M | see §3.4 | | | |
| 30–40 | **B** Cold-start cycle ×2 | cycles / 90 s cold | | | |
| 40–50 | **H** Failure injection ×3 | seconds to recognise | | | |
| 50–55 | Backup driver runs **A** ×1 | cycles / 90 s | | | |
| 55–60 | Log everything on the wall chart | — | ☐ done | | |

**Cycle segment timing — do this once a month, off the video (§4.1):**

| Segment | Seconds | % of cycle |
|---|---|---|
| Acquire | | |
| Travel out | | |
| Score | | |
| Travel back | | |

⚠️ **If `Acquire` is longest, do not touch the drivetrain, the motors, or any PID gain this week.** Widen the intake, add a lead-in, add an alignment aid, or change the approach angle.

### 8.5 Reliability block (10 min)

- [ ] **Fastener spot-check** — 10 fasteners chosen at random. Loose count: `____`
- [ ] **Full fastener lap** (§5.2) — required **once a month** and **the night before every event**. Last full lap: `____ / ____`
- [ ] Battery log updated: every pack's resting V and post-run V recorded
- [ ] Battery sag test (§5.1.5) — **once a month**. Worst pack this month: `____` , sag `______ V`
- [ ] Spares bin restocked from what got used today
- [ ] Anything broken today written on the **spares to order** list: `______________________`

### 8.6 Close-out (10 min) — the part that makes the whole protocol worth doing

- [ ] All numbers from this sheet typed into the season spreadsheet **before anyone leaves**
- [ ] Whiteboard trend line updated (cycles/90 s and auto success rate)
- [ ] Video uploaded / saved with today's date
- [ ] **ONE fix named for next week — exactly one:** `________________________________________`
- [ ] Photo of this sheet taken for the engineering portfolio

**Session sign-off:** `________________`  ·  Total robot run time today: `______ min`

---

## 9. PRINTABLE — the match-day runbook

> **Print three copies: one for the pit wall, one on the checklist runner's clipboard, one in the cart.**
> Event: `______________________`  ·  Date: `____ / ____ / ______`  ·  Team: `__________`

### 9.1 The night before

- [ ] **Full fastener lap** completed (§5.2). Loose count: `____`
- [ ] **Full self-inspection** against §10 completed, by a student who did *not* build the robot. Failures found: `____`
- [ ] Robot fits the **18 in sizing box** — physically verified, not eyeballed
- [ ] All batteries charged; chargers, cords and power strip packed
- [ ] RC and DS on matching SDK versions; both self-inspect screens clean
- [ ] Devices named `<team>-RC` / `<team>-DS` (**R705**); Control Hub Wi-Fi password non-default (**R711.A**)
- [ ] Code committed and tagged. **No code changes after tonight** unless a match forces it
- [ ] Two spare ROBOT SIGNS printed and laminated
- [ ] Printed: team roster from the FIRST dashboard, portfolio (if submitting), §9, §10, role cards
- [ ] Safety glasses ×(team size + 4), closed-toe shoes confirmed for everyone
- [ ] Tier 1 spares bin packed and closed; tool tray packed
- [ ] Food, water, cash, phone chargers
- [ ] Roles assigned **in writing** (§7.3) and read aloud to the whole team
- [ ] Departure time announced. Arrival target: **doors-open time**

### 9.2 Load-in — the first 45 minutes

| Order | Who | Action |
|---|---|---|
| 1 | Adult (J6) | **Check in at Pit Administration** — required **no later than 45 min before quals** (**I102**), with at least one student present |
| 2 | Technician + 1 | **Robot straight to inspection.** Not after unpacking. First. |
| 3 | Runner + scout | Build the pit (§7.2): battery station at the outlet, tool tray open, spares bin, schedule wall |
| 4 | Everyone | Safety glasses on. There is only a **10-minute grace period** after doors open (**E101.A**) |
| 5 | Technician | The moment inspection passes → **practice field** (**E116** gates practice-field access on passing inspection at open-inspection events) |
| 6 | Runner | Print/photograph the match schedule the moment it posts (≤15 min before quals) and tape it up with your matches highlighted |

### 9.3 The field calibration window — do not miss this

**[FACT — LOCAL, prior season] T205:** the ARENA may be open for **at least 30 minutes before quals** for measurement and sensor calibration. Allowed: robot powered on, OpMode initialised, mechanisms extended, scoring elements controlled, laptop connected, team members on the field, tape measures and sensors used. **Not allowed:** driving the chassis under its own power, launching scoring elements, human-player practice.

**Bring this list, filled in during build season with the four measurements your autonomous depends on:**

| # | Measurement to take on the competition field | Value at home | Value here | Δ |
|---|---|---|---|---|
| 1 | `___________________________________` | | | |
| 2 | `___________________________________` | | | |
| 3 | `___________________________________` | | | |
| 4 | `___________________________________` | | | |

- [ ] Substrate under the tiles noted (hardwood / carpet / concrete / stage): `____________` — compare to your practice substrate (§2.6)
- [ ] Lighting noted (bright / dim / backlit windows): `____________` — matters for vision
- [ ] AprilTag / vision target sanity check run and accepted
- [ ] Any correction needed to autonomous distances: `____________`

### 9.4 THE PRE-MATCH CHECKLIST — read aloud, performed by a second person

> **Cut this out. One per match. Runner reads, technician performs, runner initials.**

**Match #: `____`  ·  Alliance: ☐ RED ☐ BLUE  ·  Partner: `______`  ·  Start time: `______`**

| ☐ | Item | Criterion |
|---|---|---|
| ☐ | Battery installed and secured | Pack ID `____`, resting **≥ 13.0 V**: `______ V` |
| ☐ | Main power switch ON, robot boots clean | No error lights |
| ☐ | Both self-inspect screens clean | No red exclamation marks |
| ☐ | Gamepads connected and mapped | Both sticks and every used button respond |
| ☐ | **ROBOT SIGNS show the correct alliance colour** | ☐ RED ☐ BLUE — matches the schedule |
| ☐ | Mechanisms cycled through full range | No binding, no unexpected noise |
| ☐ | Nothing loose, nothing hanging, no tools on the robot | Visual sweep, top and bottom |
| ☐ | Correct **AUTO OpMode** selected on the DS | Name read aloud: `______________` |
| ☐ | Pre-load in place (if any) | Count: `____` |
| ☐ | Laptop **disconnected** from the robot network | **R704.C** |
| ☐ | No Dashboard / Panels / streaming tool running | **R704.D** |
| ☐ | Alignment device, if used, in hand | **G302** permits one |
| ☐ | Strategy one-liner agreed and on the wrist card | `______________________` |

**Runner initials: `____`  ·  Time completed: `______`**

**On the field (T−3):**

- [ ] Robot placed legally — over the correct line / touching the correct element, **fully on your alliance's side**, inside the perimeter, in STARTING CONFIGURATION, not entangled with any field element (DECODE **G303/G304**)
- [ ] **OpMode selected AND INIT pressed** — required even if you are not running an auto (DECODE **G305**)
- [ ] Robot motionless after init (**G303.F**)
- [ ] Drive team in starting positions, hands off
- [ ] Safety glasses on

### 9.5 During the match — the coach's card

| Phase | Coach says | Coach does NOT say |
|---|---|---|
| AUTO | *(nothing to your drivers)* — watch the **opponents** | Narration of your own auto |
| TELEOP 0–30 s | Field state: "two left in the corner", "they're going for the goal" | Button presses |
| TELEOP middle | **One** instruction at a time. Countdown at 40 s / 30 s / 20 s | Three instructions in one breath |
| Endgame | Own the clock: "twelve seconds — go now" | Panic narration |
| Buzzer | "Hands off. Good work." | Anything critical, on the field |

### 9.6 POST-MATCH TRIAGE CARD — 3 minutes, every match

**Match #: `____`  ·  Score: `____` – `____`  ·  Cycles: `____`  ·  End battery V: `______`**

| Min | Who | Action | ☐ |
|---|---|---|---|
| 0:00 | Drive team | Robot to the pit on the cart. **No debrief on the walk.** | ☐ |
| 0:30 | Technician | Battery out → cooling slot. Fresh pack staged. | ☐ |
| 0:30–1:30 | Technician | Fixed-order sweep: **wheels → intake → scoring mech → wiring → known-marginal fasteners** | ☐ |
| 0:30–1:30 | Scout | **ONE failure observed:** `__________________________` | ☐ |
| | | **ONE thing to change:** `__________________________` | ☐ |
| 1:30–2:00 | Crew | **Triage decision** — circle one: **FIX NOW** / **FIX AT LUNCH** / **AFTER THE EVENT** | ☐ |
| 2:00–3:00 | Technician | Execute (or don't). Fresh pack in. Power-on test. Full mechanism range test. | ☐ |
| 3:00 | Runner | Robot staged; next checklist on the clipboard. | ☐ |

**The triage rules — read them before deciding:**

1. Did it stop us scoring? **No → do not touch it.**
2. Identical spare + rehearsed <5-minute procedure? **No → do not attempt it now.**
3. Changes size / mass / materials / adds an uninspected part? **Yes → re-inspection required (I303).** Walk to the LRI.
4. **Never change two things at once.**
5. **Never change code and hardware in the same turnaround.**
6. After any change: **full mechanism range test before the robot leaves the pit.**
7. Robot fine? **Crew rests.** Water. Sit down.

### 9.7 Between-match jobs (so the waiting time is not wasted)

| Who | Job |
|---|---|
| Scout | ftcscout.org / ftc-events for this event; build the alliance tier list (`research/SCOUTING-AND-AWARDS.md` §6) |
| Pit-scout (if you have one) | Walk the pits: 90 seconds per team, fixed question list |
| Adult (J6) | Judging logistics; keep the pit presentable — **pit interviews are unannounced** |
| Technician | Battery rotation log; restock the tool tray; nothing else unless triage said so |
| Drivers | **Rest.** Rehearse the setup ritual mentally. Do not touch the robot |

### 9.8 End of day

- [ ] **Ceremonies: max 5 team members in the pits (E702); everyone else in the stands (E701)**
- [ ] Photograph the pit and the robot before teardown — portfolio evidence
- [ ] Battery station packed last; log the final state of every pack
- [ ] All match records transferred from paper to the spreadsheet **before leaving the venue**
- [ ] **Tonight, 25 minutes, whole team: video review at 0.25× (§4.5). Hesitation tally: `____`**
- [ ] **ONE change named for the next practice:** `________________________________________`

### 9.9 Role cards — cut out, one per person, worn or pocketed

```
+-------------------------------------+  +-------------------------------------+
| DRIVER                              |  | DRIVE COACH                         |
| T-20 : stop touching the robot      |  | T-20 : agree 1-sentence strategy    |
| T-12 : watch the checklist, do not  |  |        with BOTH partners           |
|        perform it                   |  | T-5  : watch the RUNNER, not the    |
| T-3  : place robot, INIT, hands off |  |        robot                        |
| MATCH: drive. Ignore everything     |  | AUTO : watch the OPPONENTS          |
|        except the coach's ONE call  |  | TELEOP: field state, ONE call at a  |
| AFTER: hands off. Walk to the pit.  |  |        time, clock at 40/30/20 s    |
|        No debrief on the walk.      |  | AFTER: 1 positive, 1 specific fix   |
+-------------------------------------+  +-------------------------------------+

+-------------------------------------+  +-------------------------------------+
| TECHNICIAN                          |  | CHECKLIST RUNNER / QUEUE WATCHER    |
| ONLY person with hands on the robot |  | Owns the phrase "we leave NOW"      |
| T-15 : fresh battery, power-on test,|  | T-12 : READ the checklist aloud     |
|        full mechanism range test    |  |        (someone else performs it)   |
| POST : 60-second fixed-order sweep  |  | Initials the card. Every match.     |
|        wheels > intake > scoring    |  | Watches the queue display           |
|        > wiring > marginal bolts    |  | Carries: clipboard, pen, spare      |
| Triage rules 1-7. Never 2 changes.  |  |          signs, safety glasses      |
+-------------------------------------+  +-------------------------------------+

+-------------------------------------+  +-------------------------------------+
| SCOUT / RECORDER                    |  | ADULT (J6) - JUDGING & LOGISTICS    |
| Every match: score, cycles,         |  | Check-in <= 45 min before quals     |
|   ONE failure, ONE fix              |  | Owns the portfolio and the          |
| Between matches: ftcscout.org,      |  |   interview clock                   |
|   pit walk, alliance tier list      |  | Walks the interview group there     |
| Owns the trend numbers              |  | Food, water, responsible-adult      |
| Types paper -> spreadsheet before   |  |   presence (I103)                   |
|   leaving the venue                 |  | Does NOT touch the robot            |
+-------------------------------------+  +-------------------------------------+
```

---

## 10. PRINTABLE — BIOBUZZ self-inspection checklist (V0 rule numbers)

> ⚠️ **[JUDGMENT] This is a self-inspection aid, not the official checklist.** It is built by re-mapping the structure of the official **DECODE Inspection Checklist rev 25-26.2** (`manuals/archive/supplemental/2025-26_DECODE_InspectionChecklist.pdf`) onto the **BIOBUZZ V0 rule numbers** in `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`.
> **The official BIOBUZZ Inspection Checklist and Inspection Quick Reference are not published as of 2026-08-21.** Section 3.3.1 of the V0 manual says *"An Inspection Checklist is available to help teams self-inspect their ROBOT. Teams are strongly encouraged to self-inspect before every event."* **Download the official versions the moment they appear on `ftc-resources.firstinspires.org/ftc/2027/team` and replace this page.**
>
> **Run this twice: two weeks before the event, and the night before.** Second run by a student who did *not* build the robot.
>
> Team: `__________`  ·  Date: `____ / ____ / ______`  ·  Inspector (student): `______________`

### 10.1 General

| ☐ | Check | Rule |
|---|---|---|
| ☐ | Robot presented with **all** mechanisms, all components of each mechanism, **all configurations**, and **all decorations** used in matches | **I301** |
| ☐ | You can demonstrate every way the robot will be configured for a match | **I301** |
| ☐ | Electronics totals counted **across all configurations combined**, not per configuration | **I302** |
| ☐ | ROBOT was built by this team (no outside-supplied complete major mechanisms) | **R101** |
| ☐ | **Two ROBOT SIGNS**, on opposite **or** adjacent surfaces 90° apart, supported by the structure/frame, robust material | **R401** |
| ☐ | Each sign ≥ **6.5 in wide × 2.5 in tall**, readable by field staff from **12 ft** | **R401** |
| ☐ | Each sign has a **solid opaque red or blue rectangle ≥ 6.5 × 2.5 in**; reversible signs cannot show the opposite colour; **not powered/illuminated** | **R402** |
| ☐ | Team number: **solid opaque white digits ≈ 2.25 in tall**, ≥ 0.25 in of background around them, **not vertically stacked**, robust, **not powered/edge-lit** | **R403** |
| ☐ | Two spare printed signs in the kit | *[JUDGMENT]* |

### 10.2 Mechanical and safety

| ☐ | Check | Rule |
|---|---|---|
| ☐ | No sharp edges, sharp protrusions, or abrasive surfaces that could damage the arena, elements or other robots | **R201, R202** |
| ☐ | No traction device known to damage tiles; no excessive lubricant that could spin off or drip | **R201** |
| ☐ | **No loose ballast** (sand, coffee beans, kitty litter, glitter, ball bearings), no liquids/gels, no tire sealant, no graphite powder | **R201** |
| ☐ | No hazardous materials; no flame or pyrotechnics; no animal-based materials | **R202.D, .E, .G** |
| ☐ | No shields/curtains designed to limit any drive team's vision; no audio loud enough to distract or mimic match sounds | **R202.A, .B** |
| ☐ | **No imagery that uses or closely mimics 36h11 AprilTags**; nothing intended to interfere with another robot's sensing | **R202.C** |
| ☐ | No device designed to damage or flip other robots; no unnecessary entanglement risk | **R202.H, .I** |
| ☐ | High-intensity light sources only briefly illuminated while targeting; **no decorative lighting flashing above 5 Hz** | **R202.F, .J** |
| ☐ | **Scoring elements and the robot can both be removed from field elements with the robot powered OFF** | **R203** |
| ☐ | No mechanism that increases downforce by grabbing the floor or by suction | **R204** |
| ☐ | No pneumatic actuators, high-speed blowers, or vacuums | **R801** |
| ☐ | COTS major mechanisms within limits; COTS components/mechanisms **single degree of freedom** | **R301, R303** |
| ☐ | If the robot holds its starting configuration under power, no motor or servo is stalled against a hard stop for minutes at a time | **R103** |
| ☐ | **Stored energy identified in writing** (springs, elastics, gas struts) so you can warn the inspector: `______________________` | §3.3.1 |

### 10.3 Electrical

| ☐ | Check | Rule |
|---|---|---|
| ☐ | Every motor is on the Table 12-1 allowed list (NeveRest, goBILDA Yellow Jacket 520x / 5000 series, Modern Robotics/MATRIX, NFR Yuksel, REV HD Hex `REV-41-1291`, REV Core Hex `REV-41-1300`, Studica Maverick 75001, SWYFT Spike, TETRIX MAX / TorqueNADO, WATTOS Stingray) | **R501** |
| ☐ | Every servo meets **≤ 8 W mechanical output @ 6 V** and the stall-current limit, or is on the pre-approved list | **R502** |
| ☐ | ⚠️ **Total ≤ 8 motors AND ≤ 8 servos** across **all** configurations *(changed from 10 servos in DECODE)*. Motors: `____`  Servos: `____` | **R503** |
| ☐ | No actuator modified except as explicitly allowed | **R504** |
| ☐ | Actuators powered and controlled only from approved power-regulation devices | **R505** |
| ☐ | No relays, electromagnets, or electrical solenoid actuators | **R506** |
| ☐ | **Exactly one** main battery, from Table 12-4 (`am-5290`, `3100-0012-0020`, `14-0014`, `REV-31-1302`, `70025`, `W39057`, `WT-NMH1230`), securely mounted, unaltered except fuse and connector | **R601** |
| ☐ | Any COTS USB battery pack is **≤ 100 Wh**, electrically isolated from robot power, and does not power actuators | **R602** |
| ☐ | **Exactly one approved main power switch** (Table 12-5: `am-4969`, `3103-0005-0001`, `REV-31-1387`, `70182`, `W39129`, `WTS-SW1220`) controlling all battery power, accessible, clear of pinch hazards and high-speed parts | **R603** |
| ☐ | Fuses per manufacturer direction — **no higher-rated, no self-resetting** | **R604** |
| ☐ | **Frame is not a current path.** If grounded, only via `am-4648a`, `REV-31-1269`, or `SR-Ground-01`, connected to a fully COTS XT30 component and to the frame via the resistive terminal | **R605** |
| ☐ | All power-regulating devices, wiring and fuses **can be made visible for inspection**; ROBOT CONTROLLER mounted so diagnostic lights / screen can be seen | **R606** |
| ☐ | Custom circuits provide **no regulated output above 5 V** (except solely for LEDs) | **R607** |
| ☐ | Control/Expansion Hubs powered **only via their XT30 connectors from the main battery**; servo power injectors per Table 12-7 | **R608** |
| ☐ | Wire sizes: **18 AWG** min for 12 V main and motor power; **22 AWG** for 11–20 A fused circuits and TETRIX MAX / REV Core Hex motor power; **28 AWG** for PWM/servo, LEDs, 10 A circuits and signal-level circuits. **No paralleling small wires** | **R609** |
| ☐ | 12 V main and +5 V aux bus colour-coded end to end: **positive = red / yellow / white / brown / black-with-stripe**; **negative = black / blue** | **R610** |
| ☐ | Powered USB hubs draw only from an approved COTS USB battery pack or a hub 5 V aux port | **R611** |
| ☐ | No custom circuit alters the power path between battery↔switch, switch↔regulator, regulator↔regulator, or regulator↔actuator. **No boost/buck converters.** No goBILDA Servo Travel Tuner | **R612** |
| ☐ | No mixing power across regulation devices or ports | **R613** |

### 10.4 Control system

| ☐ | Check | Rule |
|---|---|---|
| ☐ | **One** robot controller: REV Control Hub `REV-31-1595`, **or** an Android phone connected to a REV Expansion Hub `REV-31-1153`. Optionally **one** additional Expansion Hub | **R701** |
| ☐ | No modified coprocessor software. Only Limelight 3A (`LL_3A`) is a permitted *programmable* vision coprocessor (Table 12-9) | **R702** |
| ☐ | If using a smartphone RC, it connects to the Expansion Hub **via USB** | **R703** |
| ☐ | No wireless other than the RC↔DS link; **laptops disconnected from the RC network during matches**; **no Dashboard / Panels / third-party streaming; no continuous video stream**; use any band/channel assigned by event staff | **R704** |
| ☐ | Devices named `<team>-RC`, `<team>-DS`; spares `<team>-A-DS` etc. | **R705** |
| ☐ | No tampering with DS device, Android RC, switches, power-regulation devices, fuses or batteries | **R706** |
| ☐ | USB carries only: webcams / optical vision sensors, a USB hub or switch, and a REV Expansion Hub | **R707** |
| ☐ | Vision devices are **single image sensor**, UVC-compatible (no stereoscopic cameras), or allowed coprocessors | **R708** |
| ☐ | Any GoPro-style recorder is self-contained, used only for **non-functional post-match viewing**, with **wireless disabled** | **R709** |
| ☐ | Any laser is part of a sensor, IEC/EN 60825-1 **Class 1 or Exempt**, and **non-visible** | **R710** |
| ☐ | Control Hub Wi-Fi password changed from default; smartphones in Airplane Mode; **Wi-Fi on, Bluetooth off**; stale Wi-Fi Direct groups and connections removed from the DS | **R711** |

⚠️ **[UNVERIFIED]** The V0 text extraction stacks the margin labels **R709 / R710 / R711** against three rule bodies (recording devices, lasers, Android configuration). The mapping above is the most likely reading. **Verify against the kickoff manual PDF before quoting a number to an inspector.**

### 10.5 Operator console

| ☐ | Check | Rule |
|---|---|---|
| ☐ | Exactly **one** approved DRIVER STATION device connected and powered: REV Driver Hub `REV-31-1596`, or an Android device with USB/OTG cables and hubs for gamepads. A spare may be carried but not connected/powered simultaneously | **R901** |
| ☐ | The DS **touch screen is accessible, clearly visible during inspection and matches, and functional without a mouse or other aid** | **R902** |
| ☐ | ⚠️ Console volume **≤ 3 ft wide × 1 ft 6 in deep × 2 ft tall**, *including all power sources such as power banks* *(depth grew from 1 ft 2 in in DECODE)*. Measured: `____ × ____ × ____` | **R903** |
| ☐ | Console under ~20 lb (over that invites extra scrutiny) | **R903** orange box |
| ☐ | **No wireless of any kind to, from, or within the console during a match** other than the RC↔DS link — no Wi-Fi cards, no Bluetooth | **R904** |
| ☐ | Both DS self-inspect screens clean — **no red exclamation marks** (app-version warnings excepted) | *official checklist "Operation" section* |

### 10.6 Sizing

| ☐ | Check | Rule |
|---|---|---|
| ☐ | In STARTING CONFIGURATION, **all parts fully stationary** and the robot fully self-contained within an **18 in × 18 in × 18 in** volume. Physically verified in a sizing box: ☐ yes | **R102** |
| ☐ | Robot is **fully self-supported** in starting configuration — exerts no force on the sides or top of the sizing tool. May be held mechanically while powered off and/or by an init OpMode pre-positioning servos and motors | **R103** |
| ☐ | Compliance demonstrated **in every configuration** you will use | **R102** orange box |
| ☐ | Robot does not intentionally detach components | **R105** |
| ☐ | ⚠️ **EXPANSION LIMITS: NOT PUBLISHED.** V0 R105 states only *"Sizing Constraints and more details will be released at Kickoff."* **Leave this line blank until 12 Sep 2026, then fill it in:** `______________________` | **R105** |
| ☐ | No weight limit exists — but note the mass anyway for battery-life and transport planning: `______ lb` | **R104** |

### 10.7 Team readiness (not the robot, but it stops you competing)

| ☐ | Check | Rule |
|---|---|---|
| ☐ | Team is "competition ready": registration complete, fee paid, 2 Lead Coaches with YPP screening, all youth registered on the dashboard | **I101** |
| ☐ | Adult checks in at Pit Administration **≤ 45 minutes before quals**, with at least one student at the venue; current roster printed from the FIRST dashboard | **I102** |
| ☐ | At least 1 (preferably 2) responsible adults present at all times | **I103** |
| ☐ | Portfolio printed if you intend to submit one | **I102.D**, **A201** |
| ☐ | ANSI/UL/CE EN166/AS-NZS/CSA-rated safety glasses for everyone **plus 4 spares**; closed-toe/heeled shoes; long hair tied back; lanyards and rings removed near the robot | **E101** |
| ☐ | Cart is easy to control, has **no powered propulsion**, no sound device, fits a 30 in door, and will stay in the pit when not in use | **E601** |
| ☐ | Charger does **not** exceed 3 A average channel current; batteries charged only with polarised matching connectors | **E511** |
| ☐ | Pit fits entirely in the assigned space; no lines run outside it; power strip packed | **E502** |

**Self-inspection result:** ☐ PASS ☐ ISSUES — count: `____`

**Issues found and their fix owners:**

| # | Issue | Rule | Owner | Fixed ☐ |
|---|---|---|---|---|
| 1 | | | | ☐ |
| 2 | | | | ☐ |
| 3 | | | | ☐ |
| 4 | | | | ☐ |

---

## 11. Where Claude Code earns its keep here

**[JUDGMENT]** The test for every item below is the one from `research/AI-IN-FTC-POLICY.md`: **does this give students more hands-on time, or does it do the students' engineering for them?** Testing and tuning is unusually favourable ground for AI, because most of the labour is *clerical* — transcription, arithmetic, cross-referencing rules — and none of the clerical work is what judges are assessing.

| Task | What you ask Claude Code to do | Labour it saves | ⚠️ Guardrail |
|---|---|---|---|
| **Rule diffing at kickoff** | *"Diff `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_*.txt` against the kickoff manual and list every R-rule whose number or numeric limit changed."* | 3–4 hours of manual reading, on the day you have least time | A student must confirm each change against the PDF before it goes on the checklist |
| **Regenerating §10 after kickoff** | *"Update the self-inspection checklist for the kickoff R105 sizing constraints and any renumbered rules."* | The whole page | Re-verify against the official Inspection Checklist when FIRST publishes it |
| **Practice-log analysis** | Point it at your session CSV: *"Plot cycles/90 s against battery resting voltage; flag sessions where the two are correlated."* | An afternoon of spreadsheet work | The **interpretation** is the students' job and the judges' question |
| **The battery-voltage plot (§4.4)** | *"For each match log, plot battery voltage over time with cycle-completion timestamps marked."* | 20 minutes per match, every match | — |
| **Cycle-segment extraction** | Paste your stopwatch splits: *"Compute median and worst-of-N for each of the four segments; tell me which is the bottleneck under the §4.6 decision tree."* | Arithmetic and consistency | Do not let it decide the *fix* — that is engineering judgement |
| **Log-schema and CSV writer** | *"Write a CSV logger for the Control Hub with these columns, no allocation in the loop."* | Half a build session | ⚠️ **R704.D** — file logging only at events. Never a live streaming dashboard |
| **Failure-mode triage rehearsal** | *"Given this symptom, walk me through §6 and rank the three most likely causes."* | Panic in the pit | The pit copy must be **printed**. No laptop-dependent process on match day |
| **Scouting pipeline** | See `research/SCOUTING-AND-AWARDS.md` §5.3a — the ftcscout.org GraphQL pull and tier list | Two students' full day | — |
| **Portfolio evidence assembly** | *"Turn 14 weeks of §8 sheets into a one-page test-and-iterate narrative with the trend chart."* | A weekend near the deadline | ⚠️ **A201 / the Competition Integrity Contract** — students must author the portfolio. Use it to *organise* their words, never to write in their place. See `research/AI-IN-FTC-POLICY.md` §8 |
| **Video review support** | *"Here are my hesitation tallies by match; is the trend improving?"* | Bookkeeping | The watching and the classifying must be human — that is where the learning is |
| **Checklist maintenance** | *"We failed on X at the last event. Add a line and delete the least-valuable existing line."* | Keeps the list from bloating past usefulness (§5.5) | — |

> **[JUDGMENT] The one place to *not* use AI in this document's scope: the pit, during matches.** Everything on match day must work from paper, because the venue Wi-Fi will be saturated, phones will be dead, and **E301 / R704** constrain what you may put on a network anyway. Use Claude Code to *produce* the printed artefacts in §8, §9 and §10 — then close the laptop.

---

## 12. Sources and known gaps

### 12.1 Local sources

| Path | Used for |
|---|---|
| `manuals/2026-27_BIOBUZZ/sections/03_Eligibility_Inspection_I_p22-26.txt` | I101–I304, inspection process, practice-match eligibility |
| `manuals/2026-27_BIOBUZZ/sections/05_EventRules_E_p33-42.txt` | E101, E105, E106, E110, E116, E301, E501–E511, E601, E701–E703 |
| `manuals/2026-27_BIOBUZZ/sections/06_Awards_A_p43-58.txt` | Initial Interview format, the two mandated question-bank questions, pit interviews |
| `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` | Every R-rule in §5, §6, §10 — including Tables 12-1 (motors), 12-2 (servos), 12-4 (batteries), 12-5 (switches), 12-7 (power regulation), 12-8 (wire sizes), 12-9 (coprocessors) |
| `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_INITIAL_kickoff.txt` | G301–G305, T201–T207, §13.6 qualification schedule and match counts |
| `manuals/archive/supplemental/2025-26_DECODE_Competition_Manual_TU32.html` | DRIVE TEAM composition, DECODE scoring values |
| `manuals/archive/supplemental/2025-26_DECODE_InspectionChecklist.pdf` | The structure and section order re-mapped in §10 |
| `manuals/archive/supplemental/2025-26_DECODE_EventFieldSetupGuide.pdf` | Substrate guidance, tile trimming, fastener-tightening guidance |
| `manuals/archive/supplemental/2025-26_DECODE_InitialFieldElementAssemblyGuide.pdf` | Full vs partial element quantities |
| `manuals/archive/supplemental/2025-26_DECODE_FieldCAD_STEP.zip` | Full-field STEP CAD precedent |
| `research/PROGRAMMING-PRACTICE.md`, `SMALL-TEAM-ECONOMICS.md`, `SEASON-CADENCE.md`, `SCOUTING-AND-AWARDS.md`, `AI-IN-FTC-POLICY.md` | Cross-referenced, not duplicated |

### 12.2 Web sources (all accessed 2026-08-21)

| Source | Used for |
|---|---|
| [AndyMark FTC 2026-27 collection](https://andymark.com/collections/first-tech-challenge-2026-2027) | Field, tile, perimeter, game-set and Pollen prices |
| [FIRST Low-Cost Field Perimeter Guide](https://ftc-resources.firstinspires.org/ftc/archive/2025/game/diy-perimeter) | DIY perimeter bill of materials |
| [Robosource Field Risers](https://www.robosource.net/field-risers-ftc) | Riser pricing tier |
| [REV 12V Slim Battery `REV-31-1302`](https://www.revrobotics.com/rev-31-1302/) | $60.00; 1.5–3.0 A charge window; 9.0 V floor; cool-before-charge guidance |
| [goBILDA 12V NiMH Nested Battery `3100-0012-0020`](https://www.gobilda.com/12v-nimh-nested-battery-3000mah-mh-fc-xt30-connector/) | $64.99; 597 g; 16 AWG; 20 A fuse |
| [goBILDA 12V Battery Charger `3101-0012-0001`](https://www.gobilda.com/battery-charger-nicad-nimh-12-1/) | $14.99; 1.0 A charge, 0.07 A trickle |
| [goBILDA 12V Battery Health Analyzer `3109-0010-0001`](https://www.gobilda.com/12v-battery-health-analyzer-nimh-3000mah/) | $49.99; IR retirement thresholds 200 / 160 / 130 mΩ |
| [FTC Robot Wiring Guide](https://ftc-docs.firstinspires.org/en/latest/robot_building/wiring_guide/wiring-guide.html) | Strain relief, service loops, XT30 pin compression, routing, do/don't list |
| [Managing Electrostatic Discharge Effects (FTC Docs)](http://ftc-docs.firstinspires.org/hardware_and_software_configuration/configuring/managing_esd/managing-esd.html) | Ferrites, 3/8 in air gap, isolation, `REV-31-1269`, `REV-31-1385` |
| [ftcelectrical.org](https://ftcelectrical.org/) | Grounding strap alone is insufficient; USB 3.0 vs 2.0 port; humidity/ESD relationship |
| [GM0 wiring tips and tricks](https://gm0.org/en/latest/docs/power-and-electronics/tips-and-tricks.html) | XT30 fragility; Tamiya→Powerpole; strain relief |
| [GM0 fastener guide](https://gm0.org/en/latest/docs/hardware-components/fastener-guide.html) | Threadlocker guidance; the polycarbonate warning; nyloc |
| [GM0 chain](https://github.com/gamemanual0/gm0/blob/main/source/docs/common-mechanisms/power-transmission/chain.rst) | Master-link failure; chain breaker |
| [GM0 driver station guide](https://github.com/gamemanual0/gm0/blob/main/source/docs/power-and-electronics/driver-station-guide.rst) | USB/OTG disconnects; 2.4 GHz congestion; sleep-mode drain |
| [REV control system troubleshooting](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/troubleshooting-the-control-system) | Driver Hub USB port damage; status LED as "check engine light" |
| [FTCScout GraphQL API](https://api.ftcscout.org/graphql) | 2025 season team counts and quick-stats in §4.3 |
| [FIRST community: DECODE Championship teams](https://community.firstinspires.org/congratulations-to-our-decode-first-championship-teams) | Winning-alliance and Inspire-award team identification |
| [Pennsylvania FTC Event Checklist](https://www.ftcpenn.org/event-checklist) | Regional-level what-to-bring confirmation |
| [Chief Delphi — drive practice](https://www.chiefdelphi.com/t/how-to-run-drive-practice/514296), [driver practice advice](https://www.chiefdelphi.com/t/looking-for-driver-practice-advice/512706), [battery tips](https://www.chiefdelphi.com/t/battery-tips-for-competition/504798), [battery tracking](https://www.chiefdelphi.com/t/battery-tracking-for-ftc-frc/444600), [competition roles](https://www.chiefdelphi.com/t/competition-roles-for-students/416788) | Community practice. ⚠️ Retrieved via search snippets only — chiefdelphi.com returns **HTTP 403** to direct fetch from this workspace, and these threads are FRC-heavy |

### 12.3 Known gaps — things to fix after kickoff

| # | Gap | Fix on |
|---|---|---|
| 1 | ⚠️ **R105 expansion limits are unpublished.** §10.6 has a deliberate blank | **12 Sep 2026** |
| 2 | ⚠️ **BIOBUZZ Sections 8–11, 13 and 15 are placeholders.** Every G-rule and T-rule cited in §6, §7.4 and §9 is from **DECODE** and must be re-verified: match periods, G301 promptness, G302 alignment devices, G303/G304 setup, G305 OpMode selection, T205 calibration window, T206 turnaround minimums, 5-or-6 qualification matches | **12 Sep 2026** |
| 3 | **BIOBUZZ DRIVE TEAM composition (Section 10)** is a placeholder. §3.2 and §7.3 assume the DECODE structure (up to 4, ≤1 non-student) | **12 Sep 2026** |
| 4 | **Official BIOBUZZ Inspection Checklist and Inspection Quick Reference are not published.** §10 is a re-mapping, not the official document | Check `ftc-resources.firstinspires.org/ftc/2027/team` weekly |
| 5 | ⚠️ **R709 / R710 / R711 margin-label ambiguity** in the V0 text extraction (recording devices / lasers / Android configuration) | Verify against the kickoff PDF |
| 6 | **No explicit gamepad-count limit found in BIOBUZZ V0 R901–R903**, whereas the DECODE inspection checklist checked "no more than two of the allowed gamepads". **[UNVERIFIED]** | Verify at kickoff |
| 7 | **AndyMark, Matrix, Studica, TETRIX and WATTOS battery prices unverified.** Only REV and goBILDA were priced | Before ordering |
| 8 | **AndyMark pre-order window closed 7 Aug 2026.** Whether a game set can still be obtained for the 2026-27 season, and whether the FIRST Storefront will carry them, is unresolved (§2.1) | Call `sales@andymark.com` **this week** |
| 9 | **BIOBUZZ field CAD, Event FIELD Setup Guide, and Initial FIELD Element Assembly Guide** not yet published | Kickoff or shortly after |
| 10 | **FIRST's tiered practice-element programme** (Team/Event Test Elements, Team Practice Elements, Wood Practice Perimeter) — the retrieved post read FRC-framed; FTC equivalents unconfirmed | Kickoff |
| 11 | **Chief Delphi is unfetchable from this workspace (HTTP 403).** All CD claims rest on search snippets and should be re-read directly by a human | Any time |
| 12 | **No verified FTC-specific benchmark for drive-practice hours.** The hour figures in §3.1 are FRC-sourced and labelled as directional | Ongoing |
| 13 | **Community 3D-printed Pollen model** (MakerWorld) returned HTTP 403 and is unverified (§2.4.3) | Any time |
| 14 | **The 2026-27 FTC Judging Process Guide** (which carries the AI guidance referenced in §11) is season-dependent and not yet published | Kickoff |

---

*End of document. Companion documents: `research/PROGRAMMING-PRACTICE.md`, `research/SMALL-TEAM-ECONOMICS.md`, `research/SEASON-CADENCE.md`, `research/SCOUTING-AND-AWARDS.md`, `research/AI-IN-FTC-POLICY.md`, `reference/CONSTRUCTION-RULES-R.md`.*
