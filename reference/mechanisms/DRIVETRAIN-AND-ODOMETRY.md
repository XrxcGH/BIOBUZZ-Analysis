# DRIVETRAIN AND ODOMETRY

### The one mechanism every BIOBUZZ design needs, the one most worth buying as a kit, and the localization stack that has quietly become cheap

**Season:** FIRST Tech Challenge 2026-2027 **BIOBUZZ** presented by RTX
**Written:** 2026-08-22 · **Kickoff:** 2026-09-12 · **The game is NOT public yet**
**Legality source of truth:** `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` (Section 12 is FINAL)
**Calibration target:** ~15 students, TWO registered teams, TWO robots, modest budget, 3D printers + hand tools, **no CNC mill**, limited mentor hours.

---

## Contents

| § | Section |
|---|---|
| 0 | How to read this file |
| 1 | The decision in one page |
| 2 | The legality envelope for a drive base |
| **3** | **MECHANISM M1 — THE DRIVE BASE** (the 7-part entry) |
| 4 | DEEP DIVE — Wheels |
| 5 | DEEP DIVE — Motors and gear ratio (the arithmetic) |
| 6 | DEEP DIVE — Bearings, shafts, hubs, couplers, chain vs belt vs direct |
| **7** | **MECHANISM M2 — LOCALIZATION / ODOMETRY** (the 7-part entry) |
| **8** | **MECHANISM M3 — STRUCTURAL FRAME AND IMPACT PROTECTION** (the 7-part entry) |
| 9 | The kit-versus-parts decision, decided |
| 10 | The R503 actuator budget, drivetrain-first |
| 11 | Kickoff-day checklist |
| 12 | Verification log — every URL loaded this session |
| 13 | Open questions / NEEDS-SKU-CHECK register |

---

## 0. How to read this file

### 0.1 Evidence labels (matched to `VENDOR-ECOSYSTEMS.md` §0.1 and `ROBOT-ARCHETYPE-LIBRARY.md`)

| Label | Meaning |
|---|---|
| **[C]** CONFIRMED-BIOBUZZ | Text present in the BIOBUZZ V0 manual's already-final sections (Section 12 unless noted) |
| **[H]** HISTORICAL | From a prior season's manual or prior-season vendor/FIRST document. A pattern, never a BIOBUZZ fact |
| **[D]** DERIVED | Arithmetic or logic on stated values. Inputs cited, conclusion is mine |
| **[J]** JUDGMENT | Engineering/procurement opinion calibrated to this two-team program. Not a fact |
| **UNVERIFIED** | Could not be established. Treat as unknown |

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

| Tag | What it guarantees |
|---|---|
| **VERIFIED** | I loaded that vendor page **in this session (2026-08-22)** and read the name, SKU, price and stock string off it |
| **VERIFIED-PHASE-A** | Not re-loaded by me; carried from `reference/VENDOR-ECOSYSTEMS.md` or `reference/LEGAL-PARTS-CONSTRAINTS.md`, which verified it on 2026-08-21/22. Treat as one hop weaker |
| **FAMILY-ONLY** | I verified the *product family* and the *category URL*, not the specific SKU. Marked **NEEDS-SKU-CHECK** |
| **MANUAL-SKU** | The part number came out of a BIOBUZZ V0 table (12-1 / 12-2 / 12-3 / 12-9) that I grepped. Price separately tagged |
| **UNVERIFIED** | Named from context only. **Do not order against this row.** |

> **Every price in this file is US list, as of AUGUST 2026, pre-discount, pre-tax, pre-shipping, and is marked VERIFY-BEFORE-ORDER.** FTC vendors reprice at season turnover, and this file was written three weeks before kickoff. §13 item 16 documents a price that moved *during* the writing of this workspace.
>
> **No SKU appears here unless it came off a page I actually loaded or a V0 table I actually grepped.** §12 is the complete log, including the pages that 404'd and the vendor that blocked me.

### 0.3 Where this file sits

| File | Relationship |
|---|---|
| `reference/LEGAL-PARTS-CONSTRAINTS.md` | **Read first.** The purchasing legality envelope. This file stays inside it and cites R-rule ids rather than re-deriving them |
| `reference/VENDOR-ECOSYSTEMS.md` | **Read first.** Who sells what, and the interoperability map. This file assumes its ecosystem-commitment recommendation |
| `reference/CONSTRUCTION-RULES-R.md` | Full Section 12 R-rule detail |
| `reference/BOM-PROTOCOL.md` | The kickoff-day procedure this catalog feeds |
| `research/PROGRAMMING-PRACTICE.md` | The software half of §7. Cross-referenced, not repeated |
| `reference/ACHIEVABILITY-FACTORS.md` | The factor model, incl. **duplicability**, scored 1-5 throughout this file |

**A note on scope.** M1 / M2 / M3 below are written as three *mechanism entries* in the catalog's uniform 7-part shape. Wheels (§4), motors and ratio (§5), and transmission hardware (§6) are **components of M1**, given their own deep-dive sections because that is where the money, the tuning time and the mistakes actually live. Do not treat them as separate mechanisms in a BOM; roll them into M1.

---

## 1. The decision in one page

**[J] For this specific program — two robots, no mill, ~15 students, limited mentor hours — the drivetrain decision is not "which drivetrain is best." It is "which drivetrain can we build twice, identically, and then forget about."** Those are different questions and they have different answers.

| Question | The short answer for THIS team |
|---|---|
| Buy a chassis kit or build from parts? | **[J] Buy the kit. Twice. In one order.** See §9 — the highest-leverage purchase of the season for a two-robot program |
| Which drivetrain? | **[J] Mecanum, unless kickoff reveals a barrier, ramp or non-flat field.** Then re-open the question the same day |
| How many drive motors? | **4 for holonomic, 2 for tank.** Both legal; the difference is **2 motor slots out of 8** under **[C] R503**, which is the whole design-budget conversation (§10) |
| What gear ratio? | **[J] 312 RPM (19.2:1) is the correct default** on 96-104 mm wheels. §5 shows the arithmetic that proves it, and when to move to 435 RPM |
| Odometry? | **[J] Yes, buy it — it has commoditized.** $85-$280 buys near-Worlds auto accuracy. §7 ranks the options |
| Swerve? | **[J] No. Not this year, not this team.** §3.2.6 is the honest version, and it is a "no" about fabrication capacity, not about ambition |
| What is deferred to kickoff? | Wheel *diameter* and *durometer*, drive *ratio*, and anything sized against **[C] R105** expansion limits — which V0 explicitly defers (*"Sizing Constraints and more details will be released at Kickoff"*) |

**[D] The one number that frames everything:** a 4-motor holonomic drivetrain consumes **4 of your 8 motors** before a single game task is addressed. A 2-motor tank drive consumes 2. Under **[C] R503** (8 motors + 8 servos, *"for all MECHANISMS used in all configurations"*, p. 77) that is the difference between having a spare motor slot for an endgame mechanism and not having one. **Decide it deliberately at kickoff, not by defaulting.**

**[J] The two-robot multiplier, stated plainly:** every row in this file has a "Qty for 2" column because in this program *there is no such thing as buying one*. A $699.99 chassis kit is a **$1,399.98** decision. A $99.99 odometry pod is a **$399.96** decision once you buy two pods per robot. Read the right-hand columns.

---

## 2. The legality envelope for a drive base

Everything below is **[C] CONFIRMED-BIOBUZZ**, grepped from `12_RobotConstruction_R_p64-88.txt` this session. Cross-reference `LEGAL-PARTS-CONSTRAINTS.md` for the full purchasing envelope.

| Rule | Verbatim-relevant text | What it means for a drivetrain BOM |
|---|---|---|
| **R102*** (p. 66-67) | *"In the STARTING CONFIGURATION … the ROBOT must be fully self-contained within an 18 in. (45.70 cm) wide, by 18 in. (45.70 cm) long, by 18 in. (45.70 cm) high volume."* | **The starting size IS known now.** A drive base of roughly **16-17 in square** is the safe target, leaving margin for the sizing tool and bolt heads. **[J] Design the chassis footprint today; you do not need the game to do it** |
| **R103*** (p. 67) | ROBOTS must be *"fully self-supported"* in STARTING CONFIGURATION; may hold position by mechanical means or by an OpMode pre-positioning servos and motors | Cautions against *"having motors stalled against a hard stop"* for several minutes — relevant if you hold the chassis in a folded state |
| **R104*** (p. 67) | *"There is no explicit weight limit for FIRST Tech Challenge ROBOTS playing BIOBUZZ."* Cautions listed: TILE damage, battery consumption, transportation, performance | **[D] This removes the usual "buy the lighter system" argument.** A heavy, rigid, over-built drive base is legal and, for a low-fabrication team, an *advantage* — mass buys traction (§5.4) and rigidity buys repeatability. It costs battery |
| **R105** (p. 68) | *"ROBOTS may expand beyond the STARTING CONFIGURATION but are still subject to sizing constraints … **Sizing Constraints and more details will be released at Kickoff**"* | ⚠ **DEFERRED TO KICKOFF.** Do not buy anything sized against a guessed expansion envelope. Drivetrains are largely immune — they live inside the starting cube — which is exactly why the drivetrain is the safe pre-kickoff purchase |
| **R201*** (p. 68) | Damage-risk examples include *"traction devices with features that are known to damage the TILE floor"*; mess-risk examples include *"tire sealant"* and *"other lubricants including graphite powder"* | **Wheel selection is a rule-constrained choice, not just an engineering one.** Cleats, grousers, metal studs and anything aggressive enough to gouge foam tile invite an inspection problem. §4.1 |
| **R202*** (p. 68) | Prohibits *"components with exposed sharp edges or sharp protrusions"*, *"devices or conditions that pose an unnecessary risk of entanglement"*, and (R202.H) *"any device designed to damage or flip competing ROBOTS"* | Cut channel ends get deburred. Exposed chain runs get guarded. Impact protection must be defensive, not offensive. An inspection item, not a nicety |
| **R203*** (p. 69) | *"ROBOTS must allow removal of SCORING ELEMENTS from the ROBOT and the ROBOT from FIELD elements while powered off."* | **[J] A worm-drive or extremely high-ratio drivetrain that cannot be back-driven by hand is an R203 conversation.** Standard planetary gearmotors back-drive fine |
| **R204*** (p. 69) | *"ROBOTS may not use any mechanism which is designed to increase downforce by either grabbing FIELD surfaces or by using some form of generated airflow to provide downward suction."* | No suction skirts, no fans, no floor-grabbing. With **[C] R801** (no vacuums/blowers) this closes the "downforce for pushing power" idea permanently |
| **R301*** (p. 69) | *"COTS MAJOR MECHANISMS purposefully designed to complete a game task are prohibited. Allowed exceptions … **A. COTS drive CHASSIS, provided none of the individual parts violate any other rules**, and B. COTS MAJOR MECHANISMS created as part of the official FIRST Tech Challenge StarterBots."* | ✅ **A complete COTS drive chassis is EXPLICITLY LEGAL.** The single most important sentence in this file for a two-robot program. §9 |
| **R302*** (p. 70) | *"Allowed raw materials and legal COTS parts can be modified (drilled, cut, painted, etc.)"* — raw materials include *"sheet stock, extruded shapes, metals, plastic, rubber, and wood"* | You may cut channel to length and drill your own plates. This is how the fabricate side of every table below is legal |
| **R303*** (p. 70) | COTS must be single DoF, **but** allowed exceptions include *"**I. holonomic wheels (omni or mecanum)**"*, *"**J. dead-wheel odometry kits**"*, and *"**K. items that transfer motion between misaligned COMPONENTS (such as universal joints, flexible shaft couplers…)**"*. Example 1: a mecanum drivetrain *"is still a single DoF."* Example 2 blesses dead-wheel pods as an allowed *"2 DoF system"* | ✅ **Mecanum wheels, omni wheels, flexible couplers and complete odometry pods are named, individually, as legal COTS exceptions.** You do not need to argue this with an inspector — cite R303.I, R303.J, R303.K |
| **R304*** | Pre-Kickoff FABRICATED ITEMS and designs are permitted (see `LEGAL-PARTS-CONSTRAINTS.md` §8.6) | ✅ **You may build a full practice chassis in August.** The drive base is the one subsystem you can legally finish before the game exists |
| **R501 / R503*** (pp. 75-77) | Closed motor allowlist (Table 12-1); **8 motors + 8 servos total** | §5 and §10 |
| **R601*** (p. 78) | Exactly **1** approved **12V NiMH** main battery | ⚠ **This makes goBILDA's entire 20V "Overlander" chassis line ILLEGAL for FTC.** See the trap box in §3.3.1 |
| **R801*** (p. 87) | No pneumatic actuators, blowers or vacuums; only manufacturer-sealed pre-charged closed-air systems, **and air-filled COTS wheels** | Pneumatic (air-filled) *wheels* are legal; pneumatic *cylinders* are not. Irrelevant on tile, but worth knowing |

---

## 3. MECHANISM M1 — THE DRIVE BASE

### 3.1 What it is and when a design needs it

The drive base is the chassis structure, the wheels, the drive motors, the transmission between them, and the mounting for the battery and control system.

**Every design needs it. Every single one.** It is the only mechanism in this catalog with a 100% inclusion rate across every archetype in `ROBOT-ARCHETYPE-LIBRARY.md` — including the "pusher/blocker" minimum archetype, where the drivetrain *is* the robot.

**[J] It is also, uniquely, the mechanism where the season is NOT won.** No team has ever won an award for a drivetrain. But a bad one loses matches continuously and invisibly: you cannot line up on a scoring position, your auto does not repeat, you get shoved out of a cycle, and your drivers spend their practice budget fighting the robot instead of learning the game. **The correct ambition for a drivetrain is "boring, identical on both robots, and finished in week 1."**

**When to spend *more* than the default:**
- Kickoff (2026-09-12) reveals a **barrier, ramp, gap or textured surface** — then §3.2.4's 6-wheel drive and §4's wheel choice become live decisions, and mecanum may be wrong.
- The game rewards **defense or pushing**, which raises the traction and gear-ratio stakes (§5.4).
- The game requires **precise repeated alignment** to a scoring feature, which raises the odometry stakes (§7).

**When to spend *less*:** always, otherwise. **[J] Buy the kit, assemble it in a weekend, and put your hours into the game-specific mechanism.**

---

### 3.2 The variants, compared

Scores are **1 = worst / hardest / most expensive, 5 = best / easiest / cheapest**, calibrated to *this* team. **Duplicability** answers one question: *how confident am I that robot B's version behaves identically to robot A's, built by a different group of students?*

| Variant | Complexity | Cost | Tuning burden | Reliability | **DUPLICABILITY** | Drive motors | Verdict for this team |
|---|---|---|---|---|---|---|---|
| **3.2.1 Mecanum, 4-wheel** | 4 | 3 | 4 | 4 | **5** | **4** | **[J] The default.** Buy as a kit; nothing to get wrong |
| **3.2.2 Tank / skid, 4 traction** | 5 | 5 | 5 | 5 | **5** | **2 or 4** | **[J] The budget and motor-budget answer.** Turns poorly, pushes wonderfully |
| **3.2.3 Tank / skid, 2 traction + 2 omni** | 5 | 4 | 4 | 5 | **5** | **2 or 4** | **[J] The best value in FTC.** Fixes tank's turning for ~$24/robot |
| **3.2.4 6-wheel drive, centre-drop** | 3 | 3 | 4 | 4 | **4** | 2 or 4 | **[J] Buy the BeeLine kit if you want this.** Do not fabricate the drop without a mill |
| **3.2.5 X-drive (4 omni @ 45°)** | 2 | 4 | 3 | 3 | **2** | **4** | **[J] No.** Fast and elegant; packaging and mounting defeat a hand-tool shop |
| **3.2.6 Swerve** | 1 | 1 | 1 | 2 | **1** | 4 + 4 steer | **[J] No.** See the honest note below |

#### 3.2.1 Mecanum, 4-wheel

Four mecanum wheels, one motor each, direct-driven. Rollers at 45° let the robot translate sideways and rotate independently — full holonomic motion from a rectangular frame.

- **Legality:** ✅ explicit. **[C] R303.I** lists *"holonomic wheels (omni or mecanum)"* as an allowed exception to the single-DoF rule, and R303 **Example 1** states a mecanum drivetrain *"is still a single DoF."*
- **Why it wins for this team:** it is the variant every vendor sells as a complete, documented, assemble-in-an-afternoon kit. **Duplicability 5/5** because you buy the same kit twice and the two robots are identical *by construction*, not by discipline.
- **The real costs:** **4 motor slots** — half your R503 budget (§10). Mecanum loses traction versus a rubber traction wheel: the rollers present only a line contact, and roughly half of each wheel's force goes into the roller axis rather than into the floor. **[J] A mecanum robot loses a pushing match to a traction robot of the same weight, essentially always.** It also strafes worse over debris and tile seams than on clean tile.
- **Tuning:** low, and well-trodden. Both major path libraries treat mecanum as the first-class case (`research/PROGRAMMING-PRACTICE.md` §5.2).

#### 3.2.2 Tank / skid steer, 4 traction wheels

Two sides, each side's wheels locked together by belt or chain, turning by skidding.

- **Legality:** unremarkable — plain wheels, no COTS-mechanism question at all.
- **Strengths:** maximum pushing force, simplest possible transmission, cheapest, and **it can run on 2 motors**, buying back two slots under **[C] R503**. Mechanically the most reliable thing you can build.
- **Weaknesses:** it *skids* to turn, so turn accuracy depends on floor friction and weight distribution — the worst possible property for a repeatable autonomous. It cannot strafe, so every lateral alignment becomes a three-point turn.
- **[J]** Choose this if the game is a pushing/defense game or if you are motor-starved. Do not choose it if the game demands precise lateral alignment.

#### 3.2.3 Tank / skid, 2 traction + 2 omni ("half-omni" tank)

Identical to 3.2.2, but the wheels on one axle (usually the front) are replaced with omni wheels.

- **[D] Why this is the best value in FTC:** omni wheels have near-zero lateral friction, so the robot pivots about the traction axle instead of skidding both axles. You keep most of tank's pushing power and gain most of a holonomic drive's turn repeatability. At goBILDA's **verified** prices the upgrade is **2 × `3624-0014-0096` omni ($21.99) minus 2 × `3626-0014-0096` Hogback ($9.99) = $24.00 per robot, $48.00 for two.**
- **[J] If the budget is tight and the game is flat, this is the variant to recommend to a rookie B team.** Cheaper than mecanum, uses 2 motors instead of 4, and turns accurately.

#### 3.2.4 6-wheel drive with a centre drop

Six wheels, three per side, with the **middle wheel mounted 1-3 mm lower** than the outer four so the robot pivots about the centre pair.

- **Strengths:** the best turning behaviour available from a non-holonomic drive, plus the ability to cross seams and small obstacles that stop a 4-wheel drive.
- **[J] The catch, and it is a big one here:** the centre drop is a *precision* feature. A 2 mm drop reproduced by hand across two robots by two student groups is exactly the tolerance a no-mill shop gets wrong — and getting it wrong means one robot turns beautifully and the other rocks like a see-saw. **Do not fabricate this. Buy it.**
- **The buy:** goBILDA **BeeLine Chassis Kit V2** (`3209-0002-0002`, **$649.99**, In Stock — VERIFIED this session), a **6-wheel drive hybrid traction/omni** design shipping four 312 RPM 5203 motors, four 96 mm Rhino wheels and four 96 mm omni wheels, with belts and pulleys for the side transmissions.

#### 3.2.5 X-drive (four omni wheels at 45°)

Four omni wheels mounted at 45° to the chassis, at the corners.

- **Legality:** ✅ **[C] R303.I** covers omni wheels.
- **[D] Why it is genuinely attractive:** every wheel contributes its full force component to translation in every direction, so an X-drive is meaningfully *faster* than a mecanum drive on the same wheels and motors, and wastes less energy in roller scrub. There is no "strafe is slower than forward" asymmetry to program around.
- **[J] Why it is still a no here:** the four motors must be mounted at 45° in a square frame. Diagonal geometry does not land on goBILDA's orthogonal 8 mm grid or REV's extrusion slots, so you end up **fabricating four identical angled motor mounts, twice — eight parts that must match, with no mill.** Packaging four diagonal motors plus battery plus Control Hub inside **[C] R102**'s 18 in cube is materially harder than the mecanum layout. Pushing power is poor: omni wheels have no lateral bite, so any defender can shove you sideways. **Duplicability 2/5.**
- **No vendor sells a complete FTC X-drive chassis kit that I could verify this session.** That absence is itself the argument.

#### 3.2.6 Swerve — the honest note

**[J] The direct answer: no, and it is not close, for this program in this season.**

Each swerve module steers *and* drives independently. **Coaxial swerve** uses one drive actuator and one steering actuator per module. **Differential swerve** uses two motors per module and derives both functions from their sum and difference.

**[D] The R503 arithmetic is not actually the blocker, and it is worth being precise about that:**

| Swerve type | Drive actuators | Steer actuators | R503 draw | Legal under R503? |
|---|---|---|---|---|
| Coaxial, motor steering | 4 motors | 4 motors | **8 motors / 0 servos** | ✅ Legal — **and your entire motor budget is gone.** Zero motors for any game mechanism |
| Coaxial, **servo** steering | 4 motors | 4 servos | **4 motors / 4 servos** | ✅ Legal, and it genuinely fits — 4 motors and 4 servos remain |
| Differential | 8 motors | (shared) | **8 motors / 0 servos** | ✅ Legal, same total wipe-out |

So a servo-steered coaxial swerve *does* fit the rule budget. **[J] The blockers are fabrication, duplicability and hours — not legality.**

1. **Fabrication.** A swerve module is a stack of concentric bearings, a steering ring or belt, and a drive path that survives the module rotating. It is the highest-tolerance assembly in FTC. **This team has 3D printers and hand tools and no mill.** Printed swerve modules exist; they wear, deflect under side load, and drift out of alignment.
2. **Duplicability = 1/5.** You must build **eight** identical modules, not four. Eight modules built by ~15 students across two teams will not be identical, and swerve is the drivetrain least tolerant of module-to-module variation — one module 2° off zero and the robot crabs.
3. **Tuning burden.** Every module needs an absolute steering zero, and every zero drifts. Note that **software is not the blocker**: `research/PROGRAMMING-PRACTICE.md` records that **Pedro Pathing supports mecanum and coaxial swerve**. The library exists. The shop does not.
4. **Opportunity cost.** The mentor-hours and student-hours a swerve consumes are the same hours the game-specific mechanism needs — and **[J]** the drivetrain is not where the season is won (§3.1).

**[J] When would swerve be right?** A single-robot team, with a mill or a sponsor machine shop, with a returning student who has built one before, in a game that rewards evasion. **That is not this program.** If a student wants to build one, make it an off-season project on the practice chassis — that is legal under **[C] R304** and it is a genuinely great learning project. It is not the competition robot.

---

### 3.3 BUY — the COTS parts and kits

#### 3.3.1 The complete-chassis-kit option, by vendor — VERIFIED 2026-08-22

**[C] R301.A makes this legal:** *"COTS drive CHASSIS, provided none of the individual parts violate any other rules."*

The full goBILDA `/chassis-kits/` category was loaded and read this session. **Every row's name, SKU, price and stock string below came off that page or the individual product page.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| ⭐ **Strafer® Chassis Kit (Ø104 mm GripForce™ Mecanum)** | goBILDA (general supplier) | **`3209-0001-0007`** | 1 | **2** | **$699.99** ea → **$1,399.98** | Buy | **VERIFIED** — In Stock | **[J] The recommended kit.** Product-page contents: four **5203 Series Yellow Jacket, 312 RPM, 8 mm REX**; one GripForce Mecanum Wheel Set Ø104 mm / 40A rollers; two 1120 U-Channel (10-hole, 264 mm) + two (17-hole, 432 mm); eight clamping steel miter gears; four hub-shafts, bearings, spacers; grade-12.9 M4 thread-locking screws; assembly tools; 600 mm encoder cables + motor adaptor cables. **No Control Hub, no battery** |
| Strafer® Chassis Kit (Ø140 mm Mecanum) | goBILDA | **`3209-0012-0002`** | 0-1 | 0-2 | **$799.99** ea | Buy | **VERIFIED** — In Stock | Bigger wheels = faster, worse packaging inside **[C] R102**'s 18 in cube. **[J] Default to the 104 mm** |
| **BeeLine Chassis Kit V2** | goBILDA | **`3209-0002-0002`** | 0-1 | 0-2 | **$649.99** ea → **$1,299.98** | Buy | **VERIFIED** — In Stock | **6-wheel drive, hybrid traction/omni.** Four 5203 19.2:1 / 312 RPM / 8 mm REX; four 96 mm Rhino + four 96 mm omni; belts and pulleys; hex keys and nut driver. **[J] The pick if kickoff shows a barrier or seam** |
| Outlaw Chassis Kit | goBILDA | **`3209-0005-0001`** | 0-1 | 0-2 | **$799.99** ea | Buy | **VERIFIED** (category page) | **Drivetrain type not stated on the category page — NEEDS-SKU-CHECK before assuming FTC suitability** |
| Hammerhead Chassis Kit | goBILDA | **`3209-0003-0001`** | 0-1 | 0-2 | **$449.99** ea | Buy | **VERIFIED** (category page) | Product page 404'd this session. **NEEDS-SKU-CHECK on contents and motor count** |
| Recon Chassis Kit | goBILDA | **`3209-0004-0001`** | 0-1 | 0-2 | **$349.99** ea → **$699.98** | Buy | **VERIFIED** — In Stock | **Cheapest goBILDA chassis kit.** Product page states 3.5 kg (7.7 lb) and *"room for your battery and electronics"* but **publishes no itemised parts list and does not state motor count or drivetrain type. NEEDS-SKU-CHECK — do not assume motors are included** |
| Bravo Chassis (Bare-Bones) | goBILDA | SKU not shown on category page | 0 | 0 | $399.99 | — | **VERIFIED** listing; **[J] NOT RECOMMENDED** | Category text: *"No Tread, No Motors, No Controller, No Battery."* It is an RC tank-track chassis. **[J] Tracks and grousers against R201's *"traction devices … known to damage the TILE floor"* is an inspection fight you do not want** |
| Bravo (Grouser Paddles / Rubber Tread) | goBILDA | SKU not shown | 0 | 0 | $1,049.99 ea | — | **VERIFIED** listing; **[J] NOT RECOMMENDED** | Same R201 concern, at triple the price |
| ⛔ **Overlander-4 / -6 / -T (20V line)** | goBILDA | `3209-0013-0001` · `-0002` · `-0101` · `-0102` | **0** | **0** | $539.99-$699.99 | ⛔ **DO NOT BUY** | **VERIFIED** listing | ⚠ **goBILDA's 20V chassis line.** **[C] R601** permits exactly one approved **12V NiMH** main battery. A 20V-architecture kit — and the battery/charger some SKUs ship with — is **outside the FTC power envelope**. The `-0001`/`-0002` SKUs are explicitly *"with battery/charger."* **[D] Not an FTC purchase** |
| FTC Starter Kit V3.1 | REV Robotics (general supplier) | **`REV-45-3529`** | 0-1 | 0-2 | **$695.00** | Buy | **VERIFIED** | **[J] Not a chassis kit** — a whole-robot starter kit. Compare against the goBILDA Starter Kit, not against the Strafer |
| goBILDA FTC Starter Kit (2026-2027) | goBILDA | **`3200-4008-2627`** | 0-1 | 0-2 | **$899.99** list / **$674.99** discounted | Buy | **VERIFIED-PHASE-A** (`VENDOR-ECOSYSTEMS.md` §6.10) | Whole-robot kit, not a chassis kit. **🕐 Check the shelf first** — the **Upgrade Pack `3200-0101-2627` at $249.99** brings a 2025-26 kit current and saves ~$650 |
| AndyMark FTC chassis | AndyMark (**official FIRST supplier**) | `/collections/ftc-chassis` category exists | — | — | not verified | Buy | ⚠ **FAMILY-ONLY — NEEDS-SKU-CHECK** | The collection page loaded but **rendered no product data** to WebFetch this session. AndyMark confirms these categories exist: *FTC Chassis, Motors and Gearboxes for FTC, NeveRest, Wheels, Robits, FIRST Tech Challenge Robot Build Bundles.* **Browse manually before ordering** |
| Studica chassis / drivetrain | Studica (**official FIRST supplier**) | — | — | — | not verified | Buy | ⛔ **BLOCKED** | `studica.com` returned **HTTP 403** to WebFetch again this session, consistent with Phase A. **Cannot verify any Studica part. Browse manually** |

> ⚠ **THE 20V TRAP, restated because it will cost someone $1,400.** goBILDA's `/chassis-kits/` page interleaves **12V** kits (FTC-appropriate) and **20V** kits (their general-robotics line) in one listing. Only the 12V group is relevant to FTC. **[C] R601** is the rule; **[D]** the Overlander family is the trap. Read the heading, not just the picture.

#### 3.3.2 Build-from-parts — the drivetrain BOM if you do NOT buy a kit

**[J] Ecosystem assumption:** goBILDA, per `VENDOR-ECOSYSTEMS.md` §4.2. This is a **4-wheel mecanum** build; adjust wheels per §4.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Drive motors | goBILDA | **5203 Series Yellow Jacket, 19.2:1, 312 RPM, 8 mm REX** — series verified, per-ratio SKU **NEEDS-SKU-CHECK** | **4** | **8** | **$54.99** ea → **$439.92** | Buy | **VERIFIED** (ratio/RPM/price read off the [category page](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/)) | ✅ Legal per **[C] Table 12-1** (5201/5202/5203/5204 series). §5 proves 312 RPM. 5202 = 6 mm D shaft, same $54.99; **5204 = $56.99** |
| Mecanum wheel set | goBILDA | **GripForce™ Mecanum Wheel Set (Ø104 mm, 40A rollers) — `3625-0202-0104`** | 1 set (4 wheels) | **2 sets** | **$189.99** ea → **$379.98** | Buy | **VERIFIED** | ✅ **[C] R303.I**. 40A = soft/grippy. §4.2 for the durometer trade |
| Mecanum wheel set (cheaper alt) | goBILDA | Mecanum Wheel Set (96 mm) — **`3213-3606-0002`** | 1 set | 2 sets | **$169.99** ea → **$339.98** | Buy | **VERIFIED** | *"Bearing supported rollers (70A durometer)"* — harder rollers, less grip, longer life |
| Mecanum wheel set (large alt) | goBILDA | Mecanum Wheel Set (140 mm) — **`3213-3606-0003`** | 1 set | 2 sets | **$299.99** ea | Buy | **VERIFIED** | 70A. **[J] Too big for a comfortable 18 in cube layout** |
| Chassis channel | goBILDA | **1120 Series U-Channel Bundle (17 pcs) — `3203-1120-0001`** | — | **1 shared** | **$219.99** | Buy | **VERIFIED-PHASE-A** | Pre-cut, on-pattern. **[J] The duplicability purchase** — `VENDOR-ECOSYSTEMS.md` §6.10.2 |
| Shafting | goBILDA | **8 mm REX Shaft Starter Pack — `3201-0008-0001`** | — | **1 shared** | **$199.99** | Buy | **VERIFIED-PHASE-A** | Replaces 12-20 per-length decisions with one SKU |
| ⭐ Bearings, 8 mm REX | goBILDA | **`1611-0514-4008`** — 8 mm REX ID, 14 mm OD, 5 mm | 8-16 | **16-32** | **$5.99 / 2-pk** → **$48-$96** | Buy | **VERIFIED** | Drops straight into goBILDA's 14 mm channel seat. **[J] The most-lost part in the shop; buy double** |
| Bearings, 8 mm round | goBILDA | **`1611-0514-0008`** — 8 mm ID, 14 mm OD, 5 mm | as needed | as needed | **$3.99 / 2-pk** | Buy | **VERIFIED** | Idler / non-driven shaft duty |
| Bearings, 12 mm | goBILDA | **`1601-1032-0012`** — 12 mm ID, 32 mm OD, 10 mm | 0-8 | 0-16 | **$5.99** ea | Buy | **VERIFIED** | Only for a 12 mm REX heavy-duty build |
| Standoffs | goBILDA | **1501 Series Standoffs Bundle (148 pc) — `3203-1501-0001`** | — | **1 shared** | **$139.99** | Buy | **VERIFIED-PHASE-A** | |
| Spacers / shims | goBILDA | **1502 Series Spacers Bundle (80 pc) — `3203-1502-0001`** | — | **1 shared** | **$46.99** | Buy | **VERIFIED-PHASE-A** | Cheapest bundle in the catalogue, and you will use all of it |
| M4 fasteners | goBILDA | M4 Socket Head Screw Assortment (600 pc) — `3201-0004-0001` | — | 1 shared | ~$54.99 | Buy | ⚠ **VERIFIED-PHASE-A: OUT OF STOCK 2026-08-21 AND 2026-08-22** | 🕐 **Out of stock two days running, three weeks pre-kickoff. Source M4 hardware NOW from a general fastener supplier as a fallback** |
| Hubs / clamping hubs / hub-shafts | goBILDA | Sonic Hubs · Classic Clamping Hubs · Set-Screw Hubs — [hubs category](https://www.gobilda.com/hubs/) | 4-8 | 8-16 | not verified | Buy | ⚠ **FAMILY-ONLY — NEEDS-SKU-CHECK** | Category page renders **sub-category names only, no SKUs or prices.** §6.3 |
| Motor mounts / brackets | goBILDA | motor mount + bracket families | 4 | 8 | not verified | Buy | **FAMILY-ONLY — NEEDS-SKU-CHECK** | **[J] Buying these beats printing them** (§3.4) |

**[D] Build-from-parts subtotal, 4-wheel mecanum, per robot (duplicated items only):** motors $439.92 + mecanum set $189.99 + REX bearings ≈ $48 = **≈ $678** before channel, shafting, hubs, standoffs, spacers and fasteners — none of which I could fully price with verified per-SKU data. Adding the shared bundles ($219.99 + $199.99 + $139.99 + $46.99 = **$606.96 across both robots**), the honest range lands at **$850-$1,050 per robot**. §9 does the kit-vs-parts comparison properly.

---

### 3.4 FABRICATE / ASSEMBLE IN-HOUSE

**[C] R302** makes all of this legal: *"Allowed raw materials and legal COTS parts can be modified (drilled, cut, painted, etc.)"* — and **[C] R304** makes it legal to do it **before kickoff**.

| What you make | Tooling required | Material | Student-hours (per robot) | **[J] Buy instead?** |
|---|---|---|---|---|
| **Assembling the chassis kit** | Hex keys, nut driver (both included in the goBILDA kits) | — | **3-5 h** first time, **2 h** second time | n/a — this IS the assembly |
| Cutting U-channel to length | Hacksaw or chop saw, file, deburring tool | goBILDA 1120 channel | 0.5 h per cut piece | ✅ **Buy the pre-cut bundle.** A hand-cut channel end is not square, and un-square is exactly what makes robot B differ from robot A |
| **Battery tray / retention** | 3D printer, hand tools | PETG or PLA+ | **1-2 h** | ❌ Fabricate. Game-agnostic, printable, and **[C] R601**'s single battery must not move |
| **Control Hub mounting plate** | 3D printer, or hand-cut polycarb + drill | 3 mm polycarbonate, or printed | **1-2 h** | ❌ Fabricate. ⚠ **[C] R706 forbids replacing the Hub's enclosure — print MOUNTS, never enclosures** |
| **Electronics bulkhead / wire-routing plate** | Hand-cut polycarb, drill, zip-tie anchors | 2-3 mm polycarbonate | **2-3 h** | ❌ Fabricate. Pays for itself at every inspection |
| **Skid plate / belly pan** | Hand-cut polycarb, drill | 2-3 mm polycarbonate | **1-2 h** | ❌ Fabricate. §8 |
| Motor mount brackets | 3D printer | PETG | 2-4 h + print time | ✅ **Buy.** **[J] A printed motor mount is the #1 source of drivetrain slop** — the motor's torque reaction walks a printed bracket. Metal mounts are cheap; this is not where to save money |
| Odometry pod mounts | 3D printer, calipers | PETG | **2-4 h** (see §7.4 — the real hidden cost of dead-wheel odometry) | ❌ Fabricate, but expect iteration |
| Drive wire harness | Crimper, strippers, ferrule kit | Wire per **[C] R609** gauge and **R610** colour | **2-3 h** | ❌ Fabricate. Consider REV's **FTC Cable Bundle `REV-45-1901` ($220.00, VERIFIED-PHASE-A)** to shortcut it |
| **Deburring every cut edge** | File, deburring tool, sandpaper | — | **0.5-1 h** | ❌ **Mandatory** — **[C] R202** prohibits *"exposed sharp edges or sharp protrusions"* |

**[D] Total fabricate/assemble hours — chassis-kit path: ≈ 10-16 student-hours for robot A, ≈ 7-11 for robot B** (the second is faster because the first taught you). **Build-from-parts path: ≈ 25-40 hours for robot A, 18-28 for robot B.** That delta — roughly **25-40 student-hours across the program** — is the real currency in the §9 decision, not the dollars.

---

### 3.5 Approximate subtotal

All figures **US list, as of August 2026, VERIFY-BEFORE-ORDER.**

| Path | Per robot | **For 2 robots** | What it does NOT include |
|---|---|---|---|
| **A. Strafer kit (mecanum, recommended)** | **$699.99** | **$1,399.98** | Control Hub, battery, main switch, odometry, superstructure |
| **B. BeeLine V2 kit (6WD hybrid)** | **$649.99** | **$1,299.98** | same |
| **C. Recon kit (cheapest)** | **$349.99** | **$699.98** | same — **and possibly motors; contents unverified** |
| **D. Build-from-parts, mecanum** | **≈ $850-$1,050** (incl. share of bundles) | **≈ $1,700-$2,100** | same, plus ~25-40 extra student-hours |
| **E. Half-omni tank, build-from-parts, 2 motors** | **≈ $400-$500** | **≈ $800-$1,000** | same. **[D]** 2 motors ($109.98) + 2 Hogback 96 mm ($19.98) + 2 omni 96 mm ($43.98) + hardware |

**[D] The headline comparison: the recommended kit path (A) costs $1,399.98 for two robots and about 20 student-hours. The equivalent build-from-parts path (D) costs $1,700-$2,100 and about 50-70 student-hours.** The kit is **cheaper AND faster**. That is unusual, and it is the finding that should drive the decision (§9).

**Add-ons that belong in the M1 line of a real BOM:**

| Add-on | 2-robot cost | Source |
|---|---|---|
| Control Hub ×2 | **$750.00** | `REV-31-1595` @ $375.00 — VERIFIED-PHASE-A. Mandated by **[C] R701.A** |
| Driver Hub ×2 | **$550.00** | `REV-31-1596` @ $275.00 — VERIFIED-PHASE-A. **[C] R901.A** |
| Battery ×2 (+2 spares) | ≈ $260 | goBILDA `3100-0012-0020` @ $64.99, page states NiMH — VERIFIED-PHASE-A, satisfies **[C] R601** |
| Localization (§7) | **$170-$560** | §7.5 |

---

### 3.6 Common failure modes and the spares to stock

| Failure mode | Why it happens | Symptom at an event | **Spare to stock (2-robot program)** |
|---|---|---|---|
| **Mecanum roller wears flat or tears off** | Soft 40A rollers on abrasive tile, plus strafing scrub | Robot pulls to one side when strafing; auto drifts | ⭐ **`3611-0040-0104` 40A GripForce Roller Pack, 44 rollers, $49.99** — VERIFIED. **[J] Buy ONE for the program.** Also `3611-0030-0104` (30A) at $49.99 |
| **Set screw backs out; wheel spins on shaft** | Vibration; no thread locker | Wheel free-spins, one corner dead | Blue thread locker + spare grub screws. **[J] The most common drivetrain failure in FTC.** Prefer **clamping** hubs over set-screw hubs (§6.3) |
| **Encoder cable pulls out or chafes** | Strain on the JST connector; routing over a sharp edge | Odometry and auto silently wrong; TeleOp looks fine | **2 spare encoder cables per program.** Strain-relieve every one at the motor |
| **Motor burns out** | Stalling against a wall or a defender (§5.4) | Smell, then a dead corner | ⭐ **1-2 spare 5203 motors, $54.99 ea.** **[J] Non-negotiable for a two-robot program** — a dead motor on Saturday morning otherwise ends one team's day |
| **Bearing seizes or falls out of its seat** | Debris; press-fit loosened by repeated disassembly | Grinding; higher current draw | **`1611-0514-4008` REX bearings, $5.99/2-pk — stock 4+ packs.** Cheap, tiny, always missing |
| **Chain thrown or stretched; belt skips teeth** | Slack; no tensioner | One side of a tank drive dead | Spare chain + master links — ⚠ **goBILDA is 8 mm pitch with NO adapter to #25** (`VENDOR-ECOSYSTEMS.md` §3.5) — or spare belts. **[J] Prefer belts** (§6.4) |
| **Wheel bolt loosens; wheel goes out of plane** | Vibration | Robot crabs; one corner rides high | Thread locker on every drivetrain fastener at first assembly, then a torque check before every event |
| **Frame flexes; bolt holes elongate** | Under-supported channel; over-torqued M4 in thin material | Progressive, invisible loss of auto accuracy | Spare 1120 channel from the 17-pc bundle |
| **Chassis fastener shortage mid-build** | The M4 assortment is out of stock (§3.3.2) | Build stops | 🕐 **Source M4 hardware from a general fastener supplier NOW** |

**[J] The spares kit that actually matters — for the program, not per robot:** 2 motors, 1 roller pack, 4 packs of REX bearings, 2 encoder cables, thread locker, a full M4 hardware bin, and one complete spare wheel of each type on the robot. **[D] ≈ $250-$300**, and it is the cheapest insurance in the season.

---

### 3.7 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum (the B team)** | **Competitive version (the A team)** |
|---|---|---|
| **Drivetrain** | Half-omni tank: 2 traction + 2 omni, **2 drive motors** | 4-wheel mecanum from a kit |
| **Source** | Build from parts on goBILDA 1120 channel | **Strafer `3209-0001-0007`** |
| **Wheels** | 2× Hogback `3626-0014-0096` ($9.99) + 2× omni `3624-0014-0096` ($21.99) | GripForce Mecanum Ø104 mm 40A, in-kit |
| **Motors** | 2× 5203 @ 312 RPM ($109.98) | 4× 5203 @ 312 RPM, in-kit |
| **Motor slots used** | **2 / 8** — six left for mechanisms | **4 / 8** — four left |
| **Localization** | Drive-encoder odometry + Control Hub IMU (**$0**) | OTOS (**$84.95**) or Pinpoint pack (**$279.99**) |
| **[D] Approx cost** | **≈ $400-$500** | **≈ $700-$1,000** |
| **Student-hours** | 12-18 h | 8-12 h (the kit is *faster*) |
| **Why** | Cheapest, simplest, most motor slots left over, and a rookie can debug it | Strafing, repeatable auto, identical to a documented reference design |

**[J] The counter-intuitive recommendation, stated explicitly:** the *rookie* path is the one that requires **more** hours and **more** skill, because it is built from parts. If the B team is genuinely inexperienced, **buy them the kit too** and let the *A* team be the one that experiments. `playbook/TWO-ROBOT-PROGRAM.md` argues the general case; this is the drivetrain-specific instance. **The kit is a teaching tool, not a shortcut** — students still assemble it, wire it, tune it and maintain it, and they learn every fastener on it.

---

## 4. DEEP DIVE — Wheels

Wheels are a **component of M1**, not a separate mechanism. They get their own section because they are the cheapest thing on the robot that changes how it plays, and the easiest thing to get wrong twice.

### 4.1 The legality frame for a wheel choice

| Rule | Text | Consequence |
|---|---|---|
| **[C] R303.I** (p. 69) | Allowed exceptions to the single-DoF rule include *"holonomic wheels (omni or mecanum)"* | ✅ Mecanum and omni wheels are **named individually** as legal COTS. Cite `R303.I` at inspection and move on |
| **[C] R201*** (p. 68) | *"Examples of 'damage risk' ROBOT features include, but are not limited to:"* — the list includes traction devices known to damage the TILE floor | ⚠ **Cleats, grousers, metal studs, tank tracks with paddles.** The rule's stated intent: *"teams should design their ROBOTS in a way that will avoid damage to the ARENA"* |
| **[C] R202*** (p. 68) | Prohibits unsafe conditions and entanglement risk | An exposed spinning wheel at the perimeter is an entanglement conversation. Guard or recess it |
| **[C] R801*** (p. 87) | Air-filled COTS wheels are permitted | **[D]** Pneumatic *tyres* are legal; pneumatic *cylinders* are not. Irrelevant on foam tile |

**[J] Practical reading: on FTC foam tile, any commercial rubber-tread wheel from a FIRST-ecosystem vendor is safe. The R201 risk lives entirely in the "off-road" product lines** — goBILDA's All-Terrain and Bravo track/grouser families exist for their general-robotics customers, not for FTC.

### 4.2 Durometer and tread — the one number that actually matters

Durometer (Shore A) measures rubber hardness. **Lower number = softer = grippier = wears faster.** Every drive-wheel decision in FTC is a walk along this axis.

| Durometer | Feel | Grip on foam tile | Life | **[J] Where it belongs** |
|---|---|---|---|---|
| **30A** | Very soft, tacky | Highest | Shortest | goBILDA Rhino "High-Traction". **[J] A pushing-game drive wheel, or a wheel you accept replacing** |
| **40A** | Soft | High | Moderate | GripForce mecanum rollers. **[J] The FTC-tuned default** — goBILDA's own product page calls the 40A set *"tuned for maximum traction on the soft tiles used in the FIRST Tech Challenge"* |
| **50A** | Medium | Good | Good | Hogback traction wheels; all goBILDA omni rollers. **[J] The best all-round drive-wheel hardness** |
| **70A** | Hard | Moderate | Longest | The 96 mm and 140 mm mecanum sets; "High-Durability" Rhinos. **[J] Choose only if wear is your observed problem** |

**[D] The trade stated as a decision rule:** you are trading *matches until replacement* against *pushing matches won*. For a **two-robot program the calculus shifts toward harder rubber**, because every wear-out event happens twice and consumes the same limited mentor evening. **[J] Start at 40-50A, and only drop to 30A if kickoff reveals a pushing/defense game.**

### 4.3 The verified wheel catalogue — goBILDA, loaded 2026-08-22

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| ⭐ **GripForce™ Mecanum Wheel Set, Ø104 mm, 40A** | goBILDA | **`3625-0202-0104`** | 1 set (4) | **2 sets** | **$189.99** ea → **$379.98** | Buy | **VERIFIED** | **[J] The FTC-correct mecanum set.** Ships inside the Strafer kit — do not double-buy |
| Mecanum Wheel Set, Ø96 mm, 70A | goBILDA | **`3213-3606-0002`** | 1 set | 2 sets | **$169.99** ea → **$339.98** | Buy | **VERIFIED** | Harder rollers, longer life, less grip. **[J] The wear-driven alternative** |
| Mecanum Wheel Set, Ø140 mm, 70A | goBILDA | **`3213-3606-0003`** | 1 set | 2 sets | **$299.99** ea | Buy | **VERIFIED** | **[J] Too tall for a comfortable [C] R102 18 in layout.** §4.4 |
| ⭐ **GripForce™ Roller Pack, 40A, 104 mm (44 rollers)** | goBILDA | **`3611-0040-0104`** | — | **1 shared** | **$49.99** | Buy | **VERIFIED** | **[J] THE most important spare in this file.** 44 rollers rebuilds most of a wheel set |
| GripForce™ Roller Pack, 30A, 104 mm (44 rollers) | goBILDA | **`3611-0030-0104`** | — | 0-1 | **$49.99** | Buy | **VERIFIED** | Softer replacement rollers — a *free* grip upgrade at rebuild time |
| GripForce™ Roller Pack, 40A, 104 mm (**4 rollers**) | goBILDA | **`3611-0140-0104`** | — | 1-2 | **$14.99** | Buy | **VERIFIED** | ⚠ **Four rollers, not 44.** The SKUs differ by one digit and the prices by 3.3×. **[J] Read the roller count, not the price** |
| **Omni Wheel, Ø96 mm, 14 mm bore, 50A** | goBILDA | **`3624-0014-0096`** | 2 | **4** | **$21.99** ea → **$87.96** | Buy | **VERIFIED — In Stock** | ✅ **[C] R303.I**. The half-omni-tank wheel (§3.2.3) |
| Omni Wheel, Ø72 mm, 14 mm bore, 50A | goBILDA | **`3624-0014-0072`** | 2 | 4 | **$19.99** ea | Buy | **VERIFIED — In Stock** | |
| Omni Wheel, Ø48 mm, 8 mm REX, 50A | goBILDA | **`3624-4008-0048`** | 0-2 | 0-4 | **$16.99** ea | Buy | **VERIFIED — In Stock** | Also the Swingarm odometry-pod wheel size (§7) |
| Omni Wheel, Ø32 mm, 8 mm REX, 50A | goBILDA | **`3624-4008-0032`** | 0-3 | 0-6 | **$14.99** ea | Buy | ⚠ **VERIFIED — OUT OF STOCK 2026-08-22** | 🕐 **The classic roll-your-own odometry-pod wheel, out of stock on two separate check dates** (Phase A 2026-08-21; me 2026-08-22). **[J] Do not plan a home-built pod around it — buy a complete pod (§7)** |
| **Hogback Traction Wheel, Ø96 mm, 14 mm bore, 50A** | goBILDA | **`3626-0014-0096`** | 2-4 | **4-8** | **$9.99** ea | Buy | **VERIFIED** | **[J] The cheapest good drive wheel in FTC.** Centreline ridge + rubber tread, purpose-built for foam mat |
| Hogback Traction Wheel, Ø72 mm, 14 mm bore, 50A | goBILDA | **`3626-0014-0072`** | 2-4 | 4-8 | **$8.99** ea | Buy | **VERIFIED** | |
| Rhino Wheel, Ø96 mm, 14 mm bore, **30A High-Traction** | goBILDA | **`3614-0014-0096`** | 2-6 | 4-12 | **$9.99** ea | Buy | **VERIFIED** | **[J] The pushing-game wheel.** Softest drive rubber goBILDA lists. Ships in the BeeLine V2 kit |
| Rhino Wheel, Ø72 mm, 30A High-Traction | goBILDA | **`3614-0014-0072`** | 2-6 | 4-12 | **$8.99** ea | Buy | **VERIFIED** | |
| Thin Rhino Wheel, Ø96 mm, 30A High-Traction | goBILDA | **`3619-0014-0096`** | 2-6 | 4-12 | **$8.99** ea | Buy | **VERIFIED** | Narrower contact patch — **[J]** better for a 6WD centre-drop where you *want* less scrub |
| Rhino Wheel, Ø96 mm, Standard | goBILDA | **`3601-0014-0096`** | 2-6 | 4-12 | **$8.99** ea | Buy | **VERIFIED** | Ø72 mm `3601-0014-0072` $7.99 · Ø120 mm `3601-0014-0120` $9.99 |
| Thin Rhino Wheel, Ø96 mm, High-Durability | goBILDA | **`3612-0014-0096`** | — | — | **$7.99** ea | Buy | **VERIFIED** | |
| Rhino Wheel, Ø96 mm, **32 mm bore**, 70A | goBILDA | **`3601-0032-0096`** | — | — | **$8.99** ea | Buy | **VERIFIED** | ⚠ **32 mm bore — a different mounting family.** Ø120 mm version `3601-0032-0120` $9.99. **[J] Check your hub before ordering** |
| ⚠ GripForce Gecko™ Wheel, Ø96 mm | goBILDA | **`3613-0014-0096`** | 0 | 0 | **$9.99** ea | Buy | **VERIFIED** | ⚠ **NOT a drive wheel.** goBILDA's own copy positions these as **intake** wheels — *"allows them to conform to the shape of the object you are trying to collect."* Ø32 mm `3613-4008-0032` $6.99 · Ø48 mm `3613-4008-0048` $7.99 · Ø72 mm `3613-0014-0072` $8.99. **See `LAUNCHERS-AND-FEEDING.md`, not this file** |
| Mecanum Wheel Set, 75 mm | REV Robotics | ships inside `REV-45-2470` | 1 set | 2 sets | in-kit | Buy | **VERIFIED** (kit contents) | 5 mm hex bore — REV ecosystem only. §9 |

### 4.4 Diameter — the speed/packaging trade, with the arithmetic

Wheel diameter multiplies speed and divides torque, one-for-one. **[D] The circumference is the whole story:**

| Ø | Circumference (π·D) | Distance per output revolution |
|---|---|---|
| 72 mm | 226.2 mm | 8.9 in |
| **96 mm** | **301.6 mm** | 11.9 in |
| **104 mm** | **326.7 mm** | 12.9 in |
| 120 mm | 377.0 mm | 14.8 in |
| 140 mm | 439.8 mm | 17.3 in |

**[D] Against the [C] R102 18-inch cube:** a Ø140 mm wheel is 5.51 in tall. Four of them plus channel plus ground clearance eats roughly a third of the cube's height before any mechanism exists. A Ø104 mm wheel is 4.09 in. **[J] 96-104 mm is the sweet spot, and every FTC-tuned kit agrees** — the Strafer ships 104 mm, the BeeLine ships 96 mm, REV's kit ships 75 mm.

**[J] The rule of thumb: pick diameter for packaging, then pick gear ratio for speed (§5).** Diameter is expensive to change once the frame is drilled; ratio is a $54.99 swap.

### 4.5 Spares — how many, for a two-robot program

**[D] The arithmetic that drives this:** a mecanum wheel carries roughly a dozen rollers; four wheels ≈ 48 rollers per robot, ≈ 96 per program. A 44-roller pack is therefore **just under one robot's worth**.

| Spare | Qty for the program | Cost | Why |
|---|---|---|---|
| ⭐ 40A roller pack `3611-0040-0104` | **1** | $49.99 | Rebuilds ~one robot's rollers. **[J] Buy at the start of the season, not when it fails** |
| Complete spare drive wheel, each type on the robot | **1 of each** | $10-$50 | For a cracked hub bore at 9 a.m. Saturday |
| Hogback/Rhino spare | 2 | ~$20 | Cheap enough that not buying them is a mistake |
| Spare omni (half-omni tank builds) | 1 | $21.99 | |

**[J] Do NOT buy a whole spare mecanum set ($189.99 × 2).** Rollers wear out; hubs almost never do. Buy rollers.

---

## 5. DEEP DIVE — Motors and gear ratio (the arithmetic)

### 5.1 What is legal — Table 12-1, grepped this session

**[C] R501*** (pp. 74-75): *"Only specific motors are allowed. The only allowed motor actuators are:"* — **Table 12-1** lists, verbatim: AndyMark NeveRest 12V DC (`am-3104`, `am-3104b`) · AndyMark NeveRest Hex 12V DC (`am-3104c`) · **goBILDA Yellow Jacket 520x Series 12V DC** (`5201-0002-0026`, etc. — *"5201, 5202, 5203, and 5204 series"*) · goBILDA 5000 Series 12V DC · Modern Robotics / MATRIX 12V DC (*Discontinued*) · NFR Products Yuksel 12V DC · **REV Robotics HD Hex 12V DC (`REV-41-1291`)** · REV Robotics Core Hex 12V DC (`REV-41-1300`) · Studica Robotics Maverick 12V DC (`75001`) · SWYFT Robotics SWYFT Spike Motor (`SR-MOTOR-DC-01`) · TETRIX MAX 12V DC (*Discontinued*) · TETRIX MAX TorqueNADO 12V DC (`W44260`) · WATTOS Stingray 12V DC (`WDM12`).

**[C] The R503 carve-out, verbatim (p. 75) — capture it, it matters for BOM planning:**
> *"Factory installed vibration and autofocus motors resident in COTS computing devices (e.g., rumble motor in a smartphone); can only be used as part of the device and cannot be removed and/or repurposed. **These motors do not count toward the limit in R503.**"*
> *"Motors integral to a COTS sensor (e.g., LIDAR, scanning sonar), provided the device is not modified except to facilitate mounting. **These motors do not count toward the limit in R503.**"*

**[D] What that buys a drivetrain designer:** nothing directly — but combined with the fact that **encoders and odometry pods are sensors, not actuators**, it means **the entire localization stack in §7 costs zero against the 8+8 budget.** That is a genuinely important planning fact, and §10 leans on it.

**[C] Two more lines from Table 12-1, verbatim:** *"Many legal gearmotors are sold with labeling based on the entire assembly. These motors may be used with or without the provided gearbox, and/or with any other compatible gearbox."* → **[D] You may legally re-gear a Yellow Jacket; legality attaches to the motor, not the gearbox.** And *"Additional motors may be added to the legal motor list in future competition manual updates."* → 🕐 **Re-diff Table 12-1 at kickoff and after every Thursday Team Update.**

### 5.2 The verified goBILDA 5203 / 5202 / 5204 ratio ladder — loaded 2026-08-22

All three series share one gear-ratio ladder, and **price is flat across ratios** — which means **ratio is a free choice.**

| Ratio | Output RPM | Stall torque (kg·cm) | 5203 SKU (8 mm REX, 24 mm) | 5202 SKU (6 mm D) | 5204 SKU (8 mm REX, 80 mm) |
|---|---|---|---|---|---|
| 1:1 | 6000 | 1.47 | `5203-2402-0001` | — | — |
| 3.7:1 | 1620 | 5.4 | `5203-2402-0003` | `5202-2402-0003` | `5204-8002-0003` |
| 5.2:1 | 1150 | 7.9 | `5203-2402-0005` | `5202-2402-0005` | `5204-8002-0005` |
| **13.7:1** | **435** | **18.7** | **`5203-2402-0014`** | `5202-2402-0014` | `5204-8002-0014` |
| ⭐ **19.2:1** | **312** | **24.3** | ⭐ **`5203-2402-0019`** | `5202-2402-0019` | `5204-8002-0019` |
| 26.9:1 | 223 | 38 | `5203-2402-0027` | `5202-2402-0027` | `5204-8002-0027` |
| 50.9:1 | 117 | 68.4 | `5203-2402-0051` | `5202-2402-0051` | `5204-8002-0051` |
| 71.2:1 | 84 | 93.6 | `5203-2402-0071` | `5202-2402-0071` | `5204-8002-0071` |
| 99.5:1 | 60 | 133.2 | `5203-2402-0100` | `5202-2402-0100` | `5204-8002-0100` |
| 139:1 | 43 | 185 | `5203-2402-0139` | `5202-2402-0139` | `5204-8002-0139` |
| 188:1 | 30 | 250 | `5203-2402-0188` | `5202-2402-0188` | `5204-8002-0188` |

**Price — VERIFIED 2026-08-22, VERIFY-BEFORE-ORDER:** **5203 and 5202 = $54.99 at every ratio; 5204 = $56.99 at every ratio.** ✅ All legal per **[C] Table 12-1**.

**[J] Which series for a drivetrain: 5203** (8 mm REX, 24 mm shaft). REX is goBILDA's hex-inscribed-in-a-round shaft — it does not round off the way a D-shaft does, and it is what every goBILDA chassis kit and odometry pod speaks. **5202** (6 mm D) only if you inherited D-bore hardware. **5204** (80 mm shaft) when the shaft must span a channel; it is a $2.00 premium, not a different motor.

**Full spec, `5203-2402-0019` product page — VERIFIED 2026-08-22:** 312 RPM free speed @ 12 VDC · **24.3 kg·cm (338 oz-in) stall torque** · **9.2 A stall current @ 12 VDC** · **0.25 A no-load current** · **537.7 PPR at the output shaft** · magnetic Hall-effect quadrature encoder, 3.3-5 VDC · brushed RS-555 motor with planetary gearbox · **$54.99, In Stock.**

### 5.3 Free-speed arithmetic — show the students this, don't just tell them the answer

> **v = (RPM ÷ 60) × π × D**

**[D] Worked, at the ratios and diameters that matter:**

| Ratio | Output RPM | Ø96 mm | Ø104 mm | Ø140 mm |
|---|---|---|---|---|
| 26.9:1 | 223 | 1.12 m/s (3.68 ft/s) | 1.21 m/s (3.98 ft/s) | 1.63 m/s (5.36 ft/s) |
| ⭐ **19.2:1** | **312** | **1.57 m/s (5.15 ft/s)** | ⭐ **1.70 m/s (5.57 ft/s)** | 2.29 m/s (7.50 ft/s) |
| **13.7:1** | **435** | **2.19 m/s (7.17 ft/s)** | **2.37 m/s (7.77 ft/s)** | 3.19 m/s (10.5 ft/s) |
| 5.2:1 | 1150 | 5.78 m/s | 6.26 m/s | — |

*Worked example, 19.2:1 on Ø104 mm:* 312 ÷ 60 = **5.2 rev/s**. π × 0.104 m = **0.3267 m/rev**. 5.2 × 0.3267 = **1.70 m/s**.

**[J] Then apply the honesty factors, because free speed is a lie:**
- **× 0.80-0.85** for real load, acceleration and friction → **≈ 1.4 m/s** for the 312 RPM / Ø104 mm combination.
- **× ~0.7 again when strafing** on mecanum — the rollers throw away part of every wheel's force → **≈ 1.0 m/s sideways**.
- **[D] Sanity check against the field:** an FTC field is 12 ft ≈ 3.66 m square, so the diagonal is ≈ 5.17 m. At 1.4 m/s that is a **≈ 3.7 s corner-to-corner traverse**. In a 30 s autonomous you get roughly eight such traverses *if you never stop* — which is why cycle count, not top speed, decides games.

**[J] The conclusion the arithmetic supports: 312 RPM already crosses the field in under four seconds. Almost no FTC game has ever been decided by a robot being faster than that.** Speed above ≈ 1.7 m/s free buys progressively less and costs control authority, stopping distance and driver-practice hours.

### 5.4 Pushing-force arithmetic — and the insight that ends the argument

> **Force at the wheel = stall torque ÷ wheel radius.**  **Traction limit = μ × robot weight.**
> **Whichever is smaller is what you actually get.**

**[D] Worked for Ø104 mm (r = 0.052 m), four driven wheels.** Convert torque first: 1 kg·cm = 0.0981 N·m.

| Ratio | Stall torque | Per-wheel force | 4-wheel stall thrust | **[D] Traction-limited below this robot mass (μ ≈ 1.0)** |
|---|---|---|---|---|
| 13.7:1 (435 RPM) | 18.7 kg·cm = 1.834 N·m | 35.3 N | **141 N (31.7 lbf)** | **14.4 kg (31.7 lb)** |
| ⭐ **19.2:1 (312 RPM)** | 24.3 kg·cm = 2.384 N·m | 45.8 N | **183 N (41.2 lbf)** | ⭐ **18.7 kg (41.2 lb)** |
| 26.9:1 (223 RPM) | 38 kg·cm = 3.727 N·m | 71.7 N | **287 N (64.5 lbf)** | 29.3 kg (64.5 lb) |

**[D] Read that right-hand column, because it is the whole argument.** A typical FTC robot masses **10-14 kg**. At 19.2:1 the drivetrain *could* push **183 N**, but the floor can only transmit **≈ 118 N** for a 12 kg robot. **You are traction-limited, not torque-limited.** Gearing down to 223 RPM raises a number you cannot use, and costs 29% of your speed to do it.

**[J] Stated as a rule: do not gear down for pushing power until you have first added mass and grip.** **[C] R104** removes the weight limit entirely — *"There is no explicit weight limit for FIRST Tech Challenge ROBOTS playing BIOBUZZ"* — so **ballast is legal, cheap, and strictly more effective than a lower gear ratio.** Softer rubber (§4.2) is the other lever, and it costs $10 a wheel.

**[D] The mecanum correction:** mecanum rollers contact along a line, and roughly half of each wheel's force vector is thrown into the roller axis. Effective μ is materially lower than a traction wheel's — call it **50-70%** — so a 12 kg mecanum robot's real thrust is perhaps **60-80 N**. **[J] This is the arithmetic behind §3.2.1's claim that a mecanum robot loses a pushing match to a traction robot of the same weight, essentially always.**

**[D] The 2-motor half-omni tank case:** two driven wheels carry roughly half the robot's weight, so the traction limit is ≈ 59 N for a 12 kg robot, against ≈ 92 N of stall thrust from two motors at 19.2:1. **Still traction-limited.** 312 RPM remains the right answer even on two motors — a useful, non-obvious result.

### 5.5 Choosing a ratio when you do not know the game

**[J] Buy 19.2:1 / 312 RPM now.** It is the correct default and it is what every FTC-tuned kit ships. Hold the decision open with **one motor of a second ratio in reserve**, and re-open it at kickoff against this table:

| What kickoff reveals | Move to | Why |
|---|---|---|
| Long open field, scoring far from the loading zone, cycle-count game | **13.7:1 / 435 RPM** | The one case where speed converts to points. **[D]** Accept that the traction-limited mass drops to 14.4 kg |
| Short cycles, dense traffic, alignment-critical scoring | ⭐ **Stay at 19.2:1 / 312 RPM** | Top speed is never reached anyway; control dominates |
| An explicit defense/pushing role, or a heavy robot (> 19 kg) | **26.9:1 / 223 RPM** | Only here does the extra torque become usable — and add mass and 30A rubber **first** |
| A barrier, ramp or climb the drivetrain must overcome | **26.9:1 / 223 RPM**, and reconsider 6WD (§3.2.4) | Gravity is a torque load, not a traction load, so §5.4's traction-limit argument does not apply |
| Unknown / mixed | ⭐ **19.2:1 / 312 RPM** | The default exists because it is right most of the time |

**[J] A $54.99 motor is the cheapest design change available to you. Do not agonise pre-kickoff — buy 312 RPM and keep the receipt.** ⚠ For a **two**-robot program, changing ratio means buying **8 motors ($439.92)**, not four. That doubles the cost of changing your mind, which is an argument for deciding **once**, at kickoff, on evidence.

### 5.6 Current, the 20 A fuse, and why you must never stall a drivetrain

**[C] R601.A** (p. 78) permits *"a COTS equivalent in-line 20A ATM mini blade fuse."* That fuse sits in series with **the entire robot**.

**[D] The arithmetic that follows is alarming, and should be taught rather than discovered:**

| Condition | Current | vs the 20 A fuse |
|---|---|---|
| 4 drive motors, no load | 4 × 0.25 A = **1.0 A** | fine |
| 4 drive motors, hard driving | ≈ 8-16 A (estimated) | fine |
| **4 drive motors STALLED** | **4 × 9.2 A = 36.8 A** | ⛔ **184% of the fuse rating** |
| 2 drive motors stalled | **18.4 A** | ⛔ marginal — and that is *before* any mechanism draws a single amp |

**[J] Three consequences, all of them design rules:**
1. **Driving into a wall at full command will blow the fuse or brown out the Control Hub, and the robot dies mid-match.** Software must current-limit or time-limit any sustained stall — see `research/PROGRAMMING-PRACTICE.md`.
2. **This is a second, independent argument against gearing down for pushing power** (§5.4): the electrical system cannot deliver the torque the gearbox could.
3. **[C] R103**'s own caution — *"not having motors stalled against a hard stop"* for several minutes at inspection — is the same failure on a slower clock.

**[J] Stock spare 20 A ATM mini blade fuses.** They cost cents, **[C] R601.A** explicitly permits the COTS replacement, and a blown one is otherwise a dead robot.

### 5.7 The REV alternative — HD Hex + UltraPlanetary

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| UltraPlanetary Gearbox Kit & HD Hex Motor | REV Robotics (general supplier) | **`REV-41-1600`** | 4 | **8** | **$50.00** ea → **$400.00** | Buy | **VERIFIED** — [REV motion](https://www.revrobotics.com/ftc/motion/) | ✅ Legal — **[C] Table 12-1** lists *REV Robotics HD Hex 12V DC `REV-41-1291`*. **[D] $4.99/motor cheaper than a Yellow Jacket**, but the ratio is set by which cartridges you stack: more assembly, more small parts to lose. ⚠ **Output RPM, stall torque and encoder spec NEEDS-SKU-CHECK** |
| Ultra 90 Degree Gearbox | REV Robotics | **`REV-41-2080`** | 4 | 8 | **$45.00** ea → **$360.00** | Buy | **VERIFIED** | Turns the motor 90° for packaging. Ships inside `REV-45-2470` (§9) |
| REV Core Hex Motor | REV Robotics | `REV-41-1300` | 0 | 0 | not verified | Buy | **MANUAL-SKU** (Table 12-1) | ✅ Legal. **[J] Far too slow and weak for a drivetrain** — treat it as a mechanism motor |
| AndyMark NeveRest / NeveRest Hex | AndyMark (**official FIRST supplier**) | `am-3104` · `am-3104b` · `am-3104c` | — | — | not verified | Buy | **MANUAL-SKU** (Table 12-1) | ✅ Legal. ⚠ AndyMark's storefront **rendered no product data to WebFetch on 2026-08-21 or 2026-08-22.** **NEEDS-SKU-CHECK — browse manually** |
| Studica Maverick | Studica (**official FIRST supplier**) | `75001` | — | — | not verified | Buy | **MANUAL-SKU** (Table 12-1) | ✅ Legal. ⛔ `studica.com` returned **HTTP 403** to WebFetch in Phase A and again this session |
| SWYFT Spike / WATTOS Stingray / TETRIX TorqueNADO / NFR Yuksel | various | `SR-MOTOR-DC-01` · `WDM12` · `W44260` · `NFR-600-100-000` | — | — | not verified | Buy | **MANUAL-SKU** (Table 12-1) | ✅ All legal per Table 12-1. **[J] Niche in the FTC market; no ecosystem advantage for this team** |

**[J] Verdict: stay on goBILDA Yellow Jackets for the drivetrain.** One SKU per corner, a flat $54.99 across every ratio, an encoder built in, and a ratio ladder you can walk without changing anything else on the robot. The REV path is competitive only if you have already committed to the REV 15 mm / 5 mm-hex ecosystem — see `VENDOR-ECOSYSTEMS.md` on ecosystem commitment, and §9 below for the one case where REV wins on price.

---

## 6. DEEP DIVE — Bearings, shafts, hubs, couplers, chain vs belt vs direct

### 6.1 Shafts — pick one standard and never mix

| Standard | Vendor | What it is | **[J] Verdict** |
|---|---|---|---|
| ⭐ **8 mm REX™** | goBILDA | A hex profile inscribed in a round envelope — carries torque like a hex, rides in a round bearing | **[J] The right default.** Every goBILDA chassis kit, every 5203/5204 motor and both odometry pods speak it |
| 12 mm REX™ | goBILDA | Bigger REX for heavy loads | **[J] Overkill for a drivetrain with no weight limit to fight** |
| 6 mm D-shaft | goBILDA (5202) | Round shaft with one flat | ⚠ **[J] Rounds off under repeated load.** Legacy only |
| 5 mm hex | REV | REV's universal shaft | **[J] Fine — but it commits you to REV's whole hardware family** |
| 1/2 in hex | REV / FRC-style | Larger hex | Appears as the Through Bore Encoder's default bore (§7) |

**Verified shaft/bearing hardware** (carried from §3.3.2, restated here for the transmission BOM): `3201-0008-0001` 8 mm REX Shaft Starter Pack **$199.99** (VERIFIED-PHASE-A) · `1611-0514-4008` 8 mm REX flanged bearing, 14 mm OD **$5.99 / 2-pk** (VERIFIED) · `1611-0514-0008` 8 mm round bearing **$3.99 / 2-pk** (VERIFIED) · `1601-1032-0012` 12 mm bearing **$5.99** (VERIFIED).

### 6.2 Bearings — the cheapest reliability you can buy

**[J] Every rotating shaft gets two bearings. No exceptions, no "it's fine for now."** A shaft running in a bare aluminium hole wallows the hole oval, and once it is oval the part is scrap — a real problem when the same part exists on a second robot and you now have two chassis that do not match.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| ⭐ 8 mm REX flanged bearing, 14 mm OD | goBILDA | **`1611-0514-4008`** | 8-16 | **16-32** | **$5.99 / 2-pk** → **$48-$96** | Buy | **VERIFIED** | Drops into goBILDA's 14 mm channel seat. **[J] Buy double what you calculate** |
| 8 mm round bearing, 14 mm OD | goBILDA | **`1611-0514-0008`** | as needed | as needed | **$3.99 / 2-pk** | Buy | **VERIFIED** | Idlers and non-driven shafts |
| 12 mm bearing, 32 mm OD | goBILDA | **`1601-1032-0012`** | 0-8 | 0-16 | **$5.99** ea | Buy | **VERIFIED** | Only for a 12 mm REX heavy-duty build |
| 5 mm Hex Bearing Block | REV Robotics | **`REV-41-1683`** | 4-8 | 8-16 | **$4.50** ea | Buy | **VERIFIED** — [REV structure](https://www.revrobotics.com/ftc/structure/) | REV ecosystem — bearing pre-pressed into a bracket |
| 15 mm Pillow Blocks | REV Robotics | family | — | — | **$5.00-$7.75** | Buy | **VERIFIED** (family) | ⚠ **NEEDS-SKU-CHECK** on the specific size |

### 6.3 Hubs — where drivetrains actually fail

A hub couples a wheel (14 mm bore) to a shaft (8 mm REX). goBILDA's `/hubs/` category page renders **sub-category names only** — Hyper (1310 / 1313 / 1315 Series), Servo, **Set-Screw**, **Classic Clamping**, **Sonic** — with **no SKUs and no prices** (VERIFIED page behaviour, 2026-08-22; identical to Phase A). ⚠ **FAMILY-ONLY — NEEDS-SKU-CHECK on every specific hub.**

| Hub style | How it grips | **[J] Verdict** |
|---|---|---|
| **Set-screw** | A grub screw bites into the shaft | ⛔ **[J] Avoid on a drivetrain.** Vibration backs the screw out, the wheel free-spins, one corner goes dead mid-match. §3.6 names this the most common drivetrain failure in FTC |
| ⭐ **Clamping / Sonic** | A split collar squeezes the whole shaft | ✅ **[J] Use these.** No point load, nothing to back out, repositionable without marring the shaft |
| ⭐ **Hub-shaft** (shouldered) | Hub and shaft are one part | ✅ **[J] Best of all — nothing to align, nothing to slip.** The Strafer kit ships *"shouldered 8mm REX hub-shafts"* (VERIFIED, product page) |

**[J] If you take one procurement instruction from §6: pay the premium for clamping hubs, and put blue thread locker on every drivetrain fastener at first assembly.** For a two-robot program this is a **duplicability** purchase — set-screw slip is exactly the kind of intermittent fault that makes robot B behave differently from robot A for reasons nobody can find on a Tuesday evening.

### 6.4 Chain vs belt vs direct drive

| Approach | Complexity | Maintenance | Noise / mess | **DUPLICABILITY** | **[J] Use when** |
|---|---|---|---|---|---|
| ⭐ **Direct drive** (motor → wheel on one shaft) | **5** | **5** | **5** | **5** | ✅ **The default. Mecanum and X-drive are always direct-drive** — every wheel needs independent control anyway |
| **Belt (GT2 / HTD)** | 4 | 4 | 5 | **4** | ✅ **[J] The right choice for linking a tank side.** Quiet, clean, no lubrication, tolerant of small misalignment. The BeeLine V2 kit ships belts and pulleys (VERIFIED, product page) |
| **Chain (#25 or 8 mm)** | 3 | 2 | 2 | **3** | ⚠ Higher torque capacity and repairable with a master link — but it stretches, it throws, it needs a tensioner, and **[C] R202** means an exposed run wants a guard |
| **Gears / miter gears** | 3 | 4 | 4 | 4 | Used *inside* the Strafer kit (*"steel miter gears (24-tooth, titanium nitride finish)"* — VERIFIED) to turn the drive through 90°. **[J] Fine as a kit component; painful to lay out yourself without a mill** |

⚠ **THE PITCH TRAP.** `VENDOR-ECOSYSTEMS.md` §3.5 records that **goBILDA chain is 8 mm pitch with NO adapter to #25**, while REV and AndyMark are #25. **[J] Chain pitch is not interoperable. Decide once, buy once, and make sure the B team does not order the other pitch.** REV's verified transmission hardware for comparison: **GT2 3 mm Pitch Belts $5.00-$12.50** · **DUO Metal #25 Sprockets $5.00-$12.50** · **#25 Chain Turnbuckle `REV-21-2617` $11.00** · **Helical 550 Motor Pinion, 12T `REV-41-2719-PK2` $5.95/2-pk** (all VERIFIED 2026-08-22).

**[J] The quiet recommendation: direct-drive mecanum needs none of this.** That is one more argument for §3.2.1 — the recommended drivetrain has no transmission to tension, guard, maintain, or duplicate.

### 6.5 Couplers and misalignment

**[C] R303.K** explicitly permits *"items that transfer motion between misaligned COMPONENTS (such as universal joints, flexible shaft couplers…)"* as an exception to the single-DoF rule. ✅ **[J] A flexible coupler is therefore legal, and it is the correct fix when a motor and a shaft will not quite line up** — far better than forcing the alignment and side-loading a bearing for the rest of the season. Cite `R303.K` if an inspector asks.

### 6.6 Motor mounts — buy, do not print

goBILDA `/motor-mounts/` was loaded 2026-08-22. ⚠ **Read this carefully: the mounts listed by name for a specific goBILDA motor family are for the *5201 Series*, not the 5203/5204.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| ⭐ 1201 Series Quad Block Pattern Mount | goBILDA | `1201-0027-0001` · `1201-0043-0002` · `1201-0043-0005` (`1201-0043-0004` is $8.99) | 4 | **8** | **$6.99** ea | Buy | **VERIFIED** (name/SKU/price) | ⭐ **The Strafer kit's own parts list names *"quad block pattern mounts"*** (VERIFIED, product page). **[D] Very likely the 5203 drivetrain mount — but the category page does not say so. NEEDS-SKU-CHECK before ordering standalone** |
| 1401 Series 2-Side, 2-Post Clamping Mount (32 / 36 mm) | goBILDA | `1401-0043-0032` · `1401-0043-0036` | — | — | **$8.99** ea | Buy | **VERIFIED** | Page states **5201 Series** compatibility |
| 1400 Series 1-Side, 2-Post Mount (32 / 36 / 37 mm) | goBILDA | `1400-0032-0032` · `-0036` · `-0037` | — | — | **$8.99** ea | Buy | **VERIFIED** | Page states **5201 Series** compatibility |
| 1222 Series Flat Pattern Mount | goBILDA | `1222-0001-0001` | — | — | **$6.99** | Buy | **VERIFIED** | Generic |
| Round-End Steel L-Bracket (2-pk) | goBILDA | `1141-0001-0001` | 2-4 | 4-8 | **$5.99** | Buy | **VERIFIED** | Generic structural bracket |

**[J] Restating §3.4's warning, because it is the most expensive fabrication mistake in this file: do not 3D-print drive motor mounts.** The motor's torque reaction walks a printed bracket, the wheel goes out of plane, and the two robots diverge. A $6.99-$8.99 metal mount deletes an entire class of "why is robot B different?" from your season.

---

## 7. MECHANISM M2 — LOCALIZATION / ODOMETRY

### 7.1 What it is and when a design needs it

Localization is the robot answering *"where am I on the field, and which way am I pointing?"* — continuously, in field coordinates, without a human in the loop. It is hardware (encoders, an IMU, an optical sensor, a camera) plus software (a localizer and a path follower).

**Every design that runs an autonomous needs it. That is every design.** The only question is *how good* it has to be.

**[J] The single most important finding in this section: odometry has commoditized, and it happened recently enough that most adults' priors are wrong.** Three years ago, accurate field localization meant three custom dead-wheel pods, a home-made mount, and a month of tuning. Today, **$84.95 buys a one-inch sensor that you bolt to the belly pan**, and **$279.99 buys a two-pod fused system that is close to what a Worlds team runs**. `research/PROGRAMMING-PRACTICE.md` reaches the same conclusion independently: *"Localization is no longer a rich-team advantage."*

**When you need MORE than the minimum:**
- The game has a **scoring feature you must align to repeatedly** — the classic case where auto and TeleOp both live or die on pose accuracy.
- Your autonomous has **more than two or three sequential moves**, so error compounds.
- You want **TeleOp driver assists** (drive-to-pose, field-centric strafing, auto-align), which need a pose estimate every loop.

**When the minimum is genuinely fine:** a pusher/blocker archetype, or a design whose autonomous is a single timed drive forward. **[J] Do not spend $560 on localization for a robot whose auto is "drive 1.2 m and stop."**

### 7.2 The variants, compared

Scores **1 = worst / hardest / most expensive, 5 = best / easiest / cheapest**, calibrated to this team. **DUPLICABILITY** asks: *will robot B's localization behave like robot A's, tuned by a different student?*

| Variant | Accuracy | Complexity | Cost | Tuning burden | Reliability | **DUPLICABILITY** | R503 slots | **[J] Verdict** |
|---|---|---|---|---|---|---|---|---|
| **7.2.1 Drive encoders only** | 2 | **5** | **5** | 4 | 4 | **5** | **0** | **[J] The free baseline. Every drivetrain already has it** |
| **7.2.2 Drive encoders + IMU heading** | 3 | **5** | **5** | 4 | 4 | **5** | **0** | ⭐ **[J] The correct rookie answer. Still $0** |
| **7.2.3 Optical (SparkFun OTOS)** | 4 | **4** | 4 | 4 | 3 | **4** | **0** | ⭐ **[J] The best value in FTC localization.** One sensor, four bolts |
| **7.2.4 2 dead-wheel pods + Pinpoint V2** | **5** | 3 | 3 | **4** | **4** | **4** | **0** | ⭐ **[J] The competitive answer.** Highest accuracy per tuning-hour |
| **7.2.5 2-3 pods + OctoQuad MK2** | **5** | 2 | 3 | 2 | 4 | **3** | **0** | **[J] Cheaper silicon, more of your own maths.** For a team with a strong programmer |
| **7.2.6 3 home-built pods, roll-your-own** | 4 | **1** | 4 | **1** | 2 | **1** | **0** | ⛔ **[J] No. This is the path that has been obsoleted** |
| **7.2.7 AprilTag / Limelight 3A (absolute)** | 4* | 3 | 2 | 3 | 3 | 4 | **0** | **[J] Complementary, not a substitute** — absolute fixes, no drift, but only when a tag is in view |

\* *AprilTag accuracy is **absolute** (no drift) but **intermittent** — it is a different quantity from odometry's continuous-but-drifting estimate. The two combine well.*

**[D] Note the R503 column: every option costs ZERO motors and ZERO servos.** Encoders and pods are sensors, not actuators, and **[C] R501**'s carve-out explicitly excludes *"motors integral to a COTS sensor"* from the R503 count. **[J] Localization is the only major capability on the robot that is free against your hardest constraint. Buy it.**

#### 7.2.1 / 7.2.2 Drive-encoder odometry, with and without the IMU

Every legal drivetrain motor already ships an encoder — the 5203 gives **537.7 PPR at the output shaft** (VERIFIED). You integrate wheel rotations into a pose estimate.

- **[D] Resolution:** 537.7 ticks ÷ 326.7 mm (Ø104 mm circumference) = **1.65 ticks per mm**, i.e. ≈ **0.61 mm per tick**. Resolution is *not* the problem.
- **[D] The problem is slip.** A driven wheel accelerating, decelerating, or being shoved slips, and every slipped millimetre is integrated into your pose *forever*. Mecanum is worse still: the rollers scrub sideways by design, so a mecanum drive-encoder localizer is systematically wrong during every strafe.
- **[J] Adding the IMU for heading fixes the worst of it, for free.** Heading error is what compounds fastest — a 2° heading error 3 m later is a 10 cm position error. The Control Hub has an integrated IMU (**[C] R701.A** mandates the Control Hub `REV-31-1595` or the phone + Expansion Hub path), so **7.2.2 costs $0 and is strictly better than 7.2.1. There is no reason to ever run 7.2.1.**
- **[J] Honest expectation:** good for ±5-15 cm over a short autonomous. Fine for "drive out, score a preload, park." Not fine for a five-step auto.

#### 7.2.3 Optical tracking — SparkFun OTOS

A downward-facing laser-illuminated optical flow sensor plus a 6-DoF IMU in a 1 in × 1 in package — an optical mouse for your robot, fused with a gyro.

- **Legality:** ✅ **explicitly blessed by name.** **[C] R702 Example 2** (p. 83): *"The SparkFun Optical Tracking Odometry Sensor is a laser and IMU tracking device... **This device is allowed**."* ⚠ The same example prohibits modifying its software: *"SparkFun does provide the source code and toolchain for advanced users to modify/update the software, which is not permitted by this rule. Firmware updates provided by SparkFun are allowed."* **[J] Apply vendor binaries only. Never flash your own build.**
- **Laser check:** **[C] R711** allows lasers only if part of a sensor, IEC/EN 60825-1 Class I / Exempt, **and** non-visible. **[D] R702 Example 2 names this exact device as allowed, which settles it** — but note the general rule before you buy any other laser-based sensor.
- **Accuracy (VERIFIED, vendor page):** *"3-5% out of the box, which can be reduced to under 1% with proper calibration."* Tracks to **2.5 m/s**, 20,000 fps, PAA5160E1 sensor, LSM6DSO IMU.
- ⚠ **The mounting constraint that catches people (VERIFIED, vendor page): working distance is 10-27 mm, and it "must be exactly 10mm for FTC field tiles."** **[J] That is a 3D-printed standoff bracket with a real tolerance on it — the fabrication task in §7.4, and the one thing that makes this harder than "four bolts."**
- **[J] Why it wins on value:** no dead wheels, nothing rubbing the floor, nothing to wear out, no pod geometry to measure, and it works identically on mecanum, tank and X-drive. **The single best localization purchase for a two-robot program on a modest budget.**
- ⚠ **Weakness:** it is looking at the floor. Debris, a tile seam, a shadow, or a change in surface degrades it. It is also the option most likely to behave differently between two robots because of mounting height variation.

#### 7.2.4 Dead-wheel pods + goBILDA Pinpoint V2 — the competitive answer

Two unpowered wheels on spring-loaded arms, one measuring X and one Y, read by a dedicated coprocessor that fuses them with its own IMU.

- **Legality:** ✅ **explicit twice over.** **[C] R303.J** names *"dead-wheel odometry kits"* as an allowed exception to the single-DoF rule, and R303's Example 2 blesses a pod as an allowed 2-DoF system. **[C] R702** treats the Pinpoint as an ordinary (non-programmable) coprocessor — **[J] which means binary firmware updates only, same as the OTOS.**
- ⚠ **A LIVE PROCUREMENT TRAP, verified this session: the original Pinpoint `3110-0002-0001` is marked "Discontinued and Sold Out" on goBILDA's own page.** The successor is **Pinpoint V2 `3110-0002-0002`, $79.99, In Stock.** **[J] If you are working from any document, video or forum post written before mid-2026, it names the dead SKU. Buy the V2.**
- **V2 specs (VERIFIED, product page):** ≈ **1,500 Hz** update (*"every 0.00065 seconds"*) vs a typical 100-300 Hz FTC loop · factory-calibrated STM IMU · max encoder rate 256,000 events/s · max gyro rate 2,000 °/s · **CRC8 error detection on the I²C line** (new in V2 — **[J] this is the fix for the "Pinpoint occasionally returns a garbage pose" class of bug**) · full 3D orientation (pitch, roll, quaternion) · configurable bulk-read windows · a USB port for firmware updates.
- **[D] Why pods beat drive encoders, quantified:** the 4-Bar pod gives **2000 countable events per revolution on a 32 mm wheel** (VERIFIED). Circumference = π × 32 = 100.5 mm, so **19.9 ticks per mm — about 0.05 mm per tick, roughly 12× the resolution of a drive encoder.** And because the pod wheel is **unpowered**, it does not slip. Resolution *and* the error source both improve.
- **[J] The 4-Bar pod vs the Swingarm pod:** goBILDA's 4-Bar page claims it *"uses clever internal packaging in place of the gears often seen in odometry systems,"* giving *"smoother rotation and eliminating the possibility of backlash,"* with a torsion spring for *"consistent, nearly linear downforce."* **[J] Prefer the 4-Bar.** Backlash in an odometry pod is measurement error you cannot tune out.
- ⚠ **The real cost is mounting, not money.** Pods hang below the frame and must be rigid, square, and at a known offset from the robot's centre of rotation. §7.4.

#### 7.2.5 OctoQuad FTC Ed. MK2

An 8-channel encoder/PWM decoder with an onboard IMU and a built-in odometry localizer.

- **Legality:** ✅ **explicitly blessed by name.** **[C] R702 Example 3** (p. 83): *"The Digital Chicken Labs OctoQuad FTC Edition is an 8-channel encoder/PWM interface, utilizing a Raspberry Pi Pico coprocessor... **This device is allowed**."* ⚠ Same restriction: *"Teams are not permitted to modify software running on the device, including replacing the software with their own."*
- **VERIFIED (Tindie, 2026-08-22): $59.99.** 8 encoder inputs to 1 MHz · 8 PWM inputs · onboard IMU with automatic gravity detection · **1.92 kHz absolute odometry localizer** for passive odometry wheels · CRC signatures on returned data · case with **goBILDA, Tetrix and Actobotics mounting patterns** · I²C to the Control Hub, bulk-readable in one transaction.
- ⚠ **The vendor page states legality for the *2025-26* season, not BIOBUZZ.** **[D] That does not matter — BIOBUZZ's own R702 Example 3 names the device as allowed, which is a stronger source than the vendor's own copy.**
- **[J] Where it wins:** it frees up encoder ports and it is $20 cheaper than a Pinpoint V2. **Where it loses for this team:** it is a lower-level building block, sold through Tindie rather than a FIRST vendor (so lead time and support are different), and `research/PROGRAMMING-PRACTICE.md` records the precedent that **the MK2 needed a vendor driver the SDK did not ship**. ⚠ **Confirm driver availability against your SDK version before you commit.**

#### 7.2.6 Roll-your-own three-pod odometry

**[J] The direct answer: no. This is the option that the last two seasons obsoleted.**

You would need three encoders, three small omni wheels, three sprung mounts, and a hand-derived three-wheel forward-kinematics model. **[D] The economics no longer work:** the classic pod wheel, goBILDA's Ø32 mm omni `3624-4008-0032` at $14.99, has been **out of stock on both check dates**; three REV Through Bore Encoders V2 at **$48.00** = **$144.00** *before* wheels, bearings and mounts — already more than a complete Pinpoint V2 + two 4-Bar pods pack at **$279.99** for a *far* worse result. And you must build **six** pods, not three. **DUPLICABILITY 1/5.**

**[J] The only reason left to do this is pedagogy** — and if that is the goal, do it on the practice chassis, legal under **[C] R304**, not on the competition robot.

#### 7.2.7 AprilTag / Limelight 3A — the absolute-position complement

- **[C] Table 12-9** (p. 83) lists **exactly one** supported programmable vision coprocessor: **Limelight Vision Limelight 3A, part `LL_3A`**. **[C] R702 Example 6** names *"the OpenMV Cam, Luxonis OAK-1, and LimeLight Vision Limelight 3G"* as **prohibited**. ⚠ **The 3A/3G distinction is a real money trap** — see `LEGAL-PARTS-CONSTRAINTS.md`.
- **[C] R702 Example 5** additionally allows the DFRobot HuskyLens and Charmed Labs Pixy2 as *configurable but not programmable* coprocessors, and **Example 4** allows **optical flow sensors** generally.
- **[J] Why it belongs in a localization section:** odometry drifts, always. AprilTags do not — they give an *absolute* pose fix whenever a tag is in frame. A robot that runs odometry continuously and snaps to an AprilTag fix when one is visible gets the best of both. `research/PROGRAMMING-PRACTICE.md` covers the SDK's built-in AprilTag localization (introduced in SDK v10.0) and rates the 3A *"the single highest-leverage software purchase for a small team."*
- ⚠ **Deferred to kickoff:** whether BIOBUZZ places AprilTags on the field at all, and where. **[J] Do not buy a Limelight before 2026-09-12.** Price NEEDS-SKU-CHECK — I did not load Limelight's storefront this session.

### 7.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| ⭐ **Pinpoint V2 Odometry Computer** | goBILDA | **`3110-0002-0002`** | 1 | **2** | **$79.99** ea → **$159.98** | Buy | **VERIFIED — In Stock** | ✅ Ordinary coprocessor per **[C] R702** — binary firmware updates only. **Supersedes the discontinued `3110-0002-0001`** |
| ⛔ Pinpoint Odometry Computer (v1) | goBILDA | `3110-0002-0001` | **0** | **0** | $79.99 | ⛔ **DO NOT ORDER** | **VERIFIED — "Discontinued and Sold Out"** | ⚠ Listed here **only** so nobody orders it from an older document |
| ⭐ **4-Bar Odometry Pod (32 mm wheel)** | goBILDA | **`3110-0001-0002`** | **2** | **4** | **$99.99** ea → **$399.96** | Buy | **VERIFIED — In Stock** | ✅ **[C] R303.J** *"dead-wheel odometry kits."* 2000 events/rev · 84 g · mounts to a 43 × 43 mm profile on 1120 U-Channel · ships 4× M4 screws + 600 mm JST-PH cable. **[J] Prefer over Swingarm — no gear backlash** |
| Swingarm Odometry Pod (48 mm wheel) | goBILDA | **`3110-0001-0001`** | 2 | 4 | **$99.99** ea | Buy | **VERIFIED** | Larger wheel rides seams better; **[J]** gear-driven, so backlash is a live concern. ⚠ PPR **NEEDS-SKU-CHECK** |
| ⭐ **4-Bar Odometry Pack (2 pods + 1 Pinpoint)** | goBILDA | **`3203-3110-0002`** | 1 | **2** | **$279.99** ea → **$559.98** | Buy | **VERIFIED** | ⚠ **[D] This is NOT a discount.** À la carte = $79.99 + 2 × $99.99 = **$279.97** — the pack costs **2¢ more**. **[J] Buy it anyway: one SKU, one line item, and the B team cannot order the wrong pod** |
| Swingarm Odometry Pack (2 pods + 1 Pinpoint) | goBILDA | **`3203-3110-0001`** | 0-1 | 0-2 | **$279.99** ea | Buy | **VERIFIED** | Same arithmetic |
| ⭐ **Optical Tracking Odometry Sensor (PAA5160E1, Qwiic)** | SparkFun (general supplier) | **`SEN-24904`** | 1 | **2** | **$84.95** ea → **$169.90** | Buy | **VERIFIED — In Stock** | ✅ **[C] R702 Example 2** names it allowed. ⚠ **PRICE DISCREPANCY: `research/PROGRAMMING-PRACTICE.md` recorded $79.95 on 2026-08-21; the vendor page read $84.95 on 2026-08-22.** Either a real move or a variant difference — **VERIFY-BEFORE-ORDER**. ⚠ Needs a **Qwiic-to-STEMMA cable** for the Control Hub — **budget it, NEEDS-SKU-CHECK** |
| OctoQuad FTC Ed. MK2 (8× encoder/PWM + IMU) | Digital Chicken Labs, via **Tindie** (neither an official FIRST supplier nor a general FTC vendor) | OctoQuad FTC Ed. MK2 | 0-1 | 0-2 | **$59.99** ea | Buy | **VERIFIED** (Tindie listing) | ✅ **[C] R702 Example 3** names it allowed. ⚠ **Stock status not stated on the listing.** ⚠ SDK driver **NEEDS-SKU-CHECK** |
| Through Bore Encoder **V2** | REV Robotics | **`REV-11-3174`** | 0-3 | 0-6 | **$48.00** ea | Buy | **VERIFIED — In Stock** | 8192 counts/rev · ±0.5° · ½ in hex bore with ⅜ in hex / 5 mm hex / ¼ in round inserts · JST-PH 6-pin. **[J] Only for a home-built pod — see §7.2.6 for why not** |
| ⛔ Through Bore Encoder V1 | REV Robotics | `REV-11-1271` | 0 | 0 | **$40.80** (from $48.00) | — | **VERIFIED — in stock but marked DISCONTINUED** | ⚠ **[J] Do not design around a discontinued part for a two-year program.** Buy V2 |
| 9-Axis IMU (standalone) | REV Robotics | `REV-31-3332` | 0-1 | 0-2 | **$38.00** | Buy | **VERIFIED-PHASE-A** ([REV electronics](https://www.revrobotics.com/ftc/electronics/)) | **[J] Unnecessary if you run a Control Hub** (integrated IMU) or a Pinpoint/OTOS (both carry their own). For the phone + Expansion Hub path per **[C] R701.B** |
| Limelight 3A (AprilTag / vision) | Limelight Vision | **`LL_3A`** | 0-1 | 0-2 | not verified | Buy | **MANUAL-SKU** (Table 12-9) | ✅ **The ONLY legal programmable vision coprocessor** per **[C] R702** + Table 12-9. ⛔ **The 3G is explicitly prohibited (Example 6).** 🕐 **Defer to kickoff** — you do not know if the field has tags. **NEEDS-SKU-CHECK on price** |
| Motor/encoder cables (spares) | goBILDA / REV | 600 mm JST-PH encoder cables; REV FTC Cable Bundle `REV-45-1901` **$220.00** | — | 2+ spares | ~$10-$220 | Buy | **VERIFIED-PHASE-A** | **[J] Two spare encoder cables per program is not optional** — §7.6 |

### 7.4 FABRICATE / ASSEMBLE IN-HOUSE

**[J] The honest headline: the money in localization is trivial and the *mounting* is where the season goes.** Budget hours here, not dollars.

| What you make | Tooling required | Material | Student-hours (per robot) | **[J] Notes** |
|---|---|---|---|---|
| **Odometry pod mounting brackets** | 3D printer, **calipers**, hand tools | PETG (not PLA — it creeps under spring load) | **2-4 h**, plus 1-2 iterations | ❌ Fabricate. The pod mounts to a **43 × 43 mm profile on 1120 U-Channel** (VERIFIED), which helps enormously — but the pod must sit **square** and at a **measured offset** from the centre of rotation |
| ⚠ **OTOS standoff bracket (the 10 mm problem)** | 3D printer, **calipers**, feeler gauge | PETG | **2-3 h**, plus iterations | ❌ Fabricate. Vendor page: working distance *"must be exactly 10mm for FTC field tiles."* **[J] Print a bracket with shim slots so you can trim the height by 0.5 mm without reprinting — and make BOTH robots' brackets from the same file, measured with the same calipers** |
| **Measuring the pod geometry** (track width, forward offset) | Calipers, a square, patience | — | **1-2 h** | ❌ Do it properly once. **[J] These are the constants the localizer trusts absolutely.** A 2 mm error in the measured offset is a permanent, un-tunable bias |
| **Cable routing and strain relief** | Zip ties, anchors, ferrules | — | **1 h** | ❌ Mandatory. §7.6 — the JST-PH connector is the weak point |
| **Wiring the I²C/sensor bus** | Crimper, wire per **[C] R609**/**R610** | — | **1 h** | ⚠ **[C] R613.A**: *"sensors, encoders, and other devices must be powered solely by the power regulation device they are connected to."* **[J] Keep the whole localization group on ONE hub.** Splitting pods across a Control Hub and an Expansion Hub is a known inspection failure |
| **The calibration routine** (software) | Laptop | — | **2-4 h** | ❌ Write it once, run it on both robots. **[J] Make it an OpMode, not a spreadsheet** |
| Home-built odometry pods | 3D printer, lathe-free ingenuity | PETG + COTS bearings | **10-20 h**, ×2 robots | ⛔ **[J] Do not.** §7.2.6 |

**[D] Total fabricate/assemble hours: OTOS path ≈ 6-9 h per robot. Pinpoint + 2 pods ≈ 8-12 h per robot. Both roughly halve on the second robot if you reuse the print files and the measured constants — which is the entire duplicability argument for buying complete pods.**

**Software implications — cross-reference, not repeated.** `research/PROGRAMMING-PRACTICE.md` is the authority; three points belong here because they change the *hardware* decision:
1. **Your path library determines your localizer.** It records **Pedro Pathing** (Quickstart pushed 2026-08-19) and **Road Runner 1.0** as both mature, notes **Pedro supports mecanum and coaxial swerve**, and that **FTCLib is effectively unmaintained** (use **SolversLib**).
2. **Your dashboard choice follows your path library:** Panels can live-tune Pedro's constants; FTC Dashboard cannot.
3. ⚠ **[C] R704.D is the sharpest constraint on the whole tuning workflow, and it is NEW.** Verbatim (p. 84): *"Additional logging/streaming services, such as those hosted by third party plugins and tools such as **FTC Dashboard, FTControl Panels**, and others are prohibited. **No continuous video stream is allowed.**"* — and **R704.C** requires programming laptops disconnected from the RC Wi-Fi during MATCH play. **[J] Tune in the shop; ship a robot that needs no laptop. Build a `COMPETITION_MODE` flag that kills every dashboard call in one line.**

### 7.5 Approximate subtotal

All figures **US list, as of August 2026, VERIFY-BEFORE-ORDER.**

| Path | Per robot | **For 2 robots** | Student-hours (program) | **[J] Who it's for** |
|---|---|---|---|---|
| **A. Drive encoders + Control Hub IMU** | **$0** | **$0** | ~4 h | ⭐ The B team, and every robot's fallback mode |
| **B. OTOS** | **$84.95** (+ Qwiic cable) | **$169.90** | ~12-18 h | ⭐ **[J] Best value. The default recommendation for this program** |
| **C. Pinpoint V2 + 2× 4-Bar pods (pack)** | **$279.99** | **$559.98** | ~16-24 h | ⭐ The A team, if the game rewards precise alignment |
| **D. OctoQuad MK2 + 2 pods** | **$259.97** | **$519.94** | ~20-30 h | A team with a strong, curious programmer |
| **E. B + C together** (optical + pods, cross-checked) | **$364.94** | **$729.88** | ~24-32 h | **[J] Only if you have a specific reason. Two localizers is two things to debug** |
| **F. Any of the above + Limelight 3A** | +unverified | +unverified | +8-16 h | 🕐 **Defer to kickoff** — absolute fixes on top of odometry |

**[D] The §1 headline restated with real numbers: the entire competitive localization stack for TWO robots costs between $0 and $560.** Against a $1,399.98 chassis decision and $750.00 of Control Hubs, **[J] localization is the cheapest performance you will buy all season, and it consumes none of your 8+8 actuator budget.**

**[J] The recommendation, stated plainly: buy 2× OTOS ($169.90) now, because it is game-agnostic and cheap. Hold the $560 pod decision until kickoff, and spend it only if the game turns out to demand repeatable alignment.**

### 7.6 Common failure modes and the spares to stock

| Failure mode | Why it happens | Symptom at an event | **Spare / mitigation (2-robot program)** |
|---|---|---|---|
| ⭐ **Encoder / pod cable pulls out or chafes** | Strain on the JST-PH connector; routing over a channel edge | **Auto silently drives to the wrong place. TeleOp looks completely fine** | ⭐ **2+ spare 600 mm JST-PH cables per program.** Strain-relieve every connector. **[J] The #1 localization failure, and the hardest to diagnose because nothing looks broken** |
| **OTOS mounting height drifts** | Bracket flexes, a shim falls out, the belly pan sags | Position error grows steadily; worse after a collision | Spare printed bracket + a shim pack. **[J] Re-measure the 10 mm gap at every event as a pit checklist item** |
| **Pod wheel lifts off the tile** | Spring fatigue, debris, a tile seam | Distance under-reads in one axis only | Spare pod (**$99.99**). **[J] An asymmetric error — X good, Y bad — is the signature** |
| **Pod wheel picks up debris / goes glazed** | Foam dust and tape residue | Gradual scale error | Isopropyl alcohol + a rag in the pit kit. Costs nothing |
| **I²C bus errors / garbage pose** | Noise on a long I²C run | Pose jumps to an impossible value for one loop | **[J] Pinpoint V2's CRC8 detection exists precisely for this.** Software: reject poses that imply impossible velocity |
| ⚠ **Sensors split across two hubs** | Convenient wiring | **Inspection failure**, and intermittent power faults | ⛔ **[C] R613.A** forbids it. **[J] Keep the localization group on ONE hub — this is a design rule, not a preference** |
| **IMU heading drifts during a long match** | Gyro bias | Robot slowly rotates its idea of "forward" | Re-zero at a known pose; **[J]** or add AprilTag fixes (§7.2.7) |
| ⚠ **Constants measured on robot A used on robot B** | The two chassis are "the same" | Robot B's auto is subtly, permanently wrong | **[J] Measure and store constants PER ROBOT, in a per-robot config file.** The duplicability trap of this whole section |

**[J] The localization spares kit: 2 JST-PH cables, 1 spare pod (if you run pods), 2 spare printed brackets, isopropyl alcohol. [D] ≈ $120 including the pod, ≈ $20 without.**

### 7.7 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum (the B team)** | **Competitive version (the A team)** |
|---|---|---|
| **Hardware** | Drive encoders + Control Hub integrated IMU | **OTOS `SEN-24904`**, or **4-Bar Odometry Pack `3203-3110-0002`** |
| **[D] Cost per robot** | **$0** | **$84.95** or **$279.99** |
| **Expected accuracy** | ±5-15 cm over a short auto | **[J] A few cm, sustained across a full autonomous** |
| **Fabrication** | None | A printed bracket with a real tolerance (§7.4) |
| **Software** | SDK drive-to-distance + IMU turns. No path library needed | Pedro Pathing or Road Runner with a proper localizer |
| **Tuning burden** | Low — a handful of constants | Moderate — but the pods/OTOS do the hard part in silicon |
| **R503 cost** | **0 motors, 0 servos** | **0 motors, 0 servos** |
| **[J] Why** | Free, already on the robot, and a rookie can reason about it | Repeatable auto is the highest-value thing a small team can own, and it now costs less than one drive motor set |

**[J] The upgrade path is the point: A and B can run *identical code* with a different localizer object.** Start both robots on encoders + IMU in week 1, and drop an OTOS into the A robot in week 4 without touching the path code. **That is the two-robot program working as designed** — see `playbook/TWO-ROBOT-PROGRAM.md`.

---

## 8. MECHANISM M3 — STRUCTURAL FRAME AND IMPACT PROTECTION

### 8.1 What it is and when a design needs it

The frame is the rectangular structure the drivetrain, battery, control system and every mechanism bolt to. "Impact protection" is whatever you add so that contact with another robot or a field wall damages neither.

**Every design needs a frame.** ⚠ **[J] A correction worth stating loudly, because FRC experience mis-transfers: FTC has NO bumper rule.** There is no bumper zone, no bumper thickness, no required coverage. I grepped Section 12 and found no bumper requirement. **[D] Protection in FTC is therefore entirely voluntary, entirely your design choice, and constrained only by:**

| Rule | Constraint on protection |
|---|---|
| **[C] R102*** | Any protection you add **must fit inside the 18 in cube** at start. **[D] A 12 mm-thick perimeter bumper costs you ~1 in of usable width in each direction — a real budget, not a rounding error** |
| **[C] R202*** | *"exposed sharp edges or sharp protrusions"* and entanglement risks are prohibited. **[J] Protection that is itself a hazard fails inspection** |
| **[C] R202.H** | *"any device designed to damage or flip competing ROBOTS"* is prohibited. **[J] Your protection must be defensive. A wedge, a ramp face, or a spike is an offensive device and will be treated as one** |
| **[C] R201*** | No damage to the ARENA | Nothing that gouges tile or field elements |
| **[C] R104*** | **No weight limit** | ✅ **[D] Heavy, rigid protection is legal and free of weight penalty. This is the single biggest structural difference from FRC intuition** |

**[J] When to spend more:** if kickoff reveals a contact-heavy game, a congested scoring area, or field elements the robot will bump repeatedly. **When to spend less: always, otherwise.** A well-built channel frame with deburred edges and a polycarbonate belly pan is sufficient protection for most FTC games.

### 8.2 The variants, compared

| Variant | Complexity | Cost | Rigidity | Repairability | **DUPLICABILITY** | **[J] Verdict** |
|---|---|---|---|---|---|---|
| ⭐ **goBILDA 1120 U-Channel frame (pre-cut)** | **5** | 3 | **5** | **5** | **5** | ⭐ **[J] The default.** On-pattern, square from the factory, identical twice |
| goBILDA 1120 channel cut in-house | 3 | **4** | 4 | **5** | **3** | **[J] Only for odd lengths.** A hand-cut end is not square, and un-square is what makes robot B differ |
| REV 45 × 15 mm C-channel / 15 mm extrusion | 4 | **4** | 4 | 4 | **5** | **[J] Equally good — if you have committed to REV.** Do not mix ecosystems mid-frame |
| Polycarbonate plate structure | 3 | **5** | 2 | 3 | 3 | **[J] Excellent for belly pans, bulkheads and guards. A poor primary frame** — it flexes, and flex is invisible auto error |
| Welded/machined custom frame | **1** | 2 | **5** | 2 | **1** | ⛔ **[J] No mill, no. Out of scope for this shop** |
| 3D-printed structural frame | 2 | 4 | 1 | 2 | 3 | ⛔ **[J] No.** Printed parts creep under sustained load and delaminate on impact. Print *brackets*, not *structure* |

### 8.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| ⭐ **1120 Series U-Channel Bundle (17 pcs)** | goBILDA | **`3203-1120-0001`** | — | **1 shared** | **$219.99** | Buy | **VERIFIED-PHASE-A** | ⭐ **[J] The duplicability purchase of the season.** Pre-cut, on-pattern, square. `VENDOR-ECOSYSTEMS.md` §6.10.2 |
| 1120 / 1121 / 1143 / 1122 Series channel, individual | goBILDA | families verified; **no SKUs or prices render on the category page** | as needed | as needed | not verified | Buy | ⚠ **FAMILY-ONLY — NEEDS-SKU-CHECK** | Loaded 2026-08-22: `/u-channel/` shows **1120 U-Channel**, **1121 Low-Side**, **1143 Mini Low-Side**, **1122 Rail-Channel** as families only |
| 1501 Series Standoffs Bundle (148 pc) | goBILDA | **`3203-1501-0001`** | — | **1 shared** | **$139.99** | Buy | **VERIFIED-PHASE-A** | |
| 1502 Series Spacers Bundle (80 pc) | goBILDA | **`3203-1502-0001`** | — | **1 shared** | **$46.99** | Buy | **VERIFIED-PHASE-A** | **[J] The cheapest bundle in the catalogue, and you will use all of it** |
| M4 Socket Head Screw Assortment (600 pc) | goBILDA | `3201-0004-0001` | — | 1 shared | ~$54.99 | Buy | ⚠ **VERIFIED-PHASE-A: OUT OF STOCK 2026-08-21 AND 2026-08-22** | 🕐 **Out of stock on two check dates, three weeks pre-kickoff. Source M4 hardware NOW from a general fastener supplier** |
| 45 × 15 mm C-Channel | REV Robotics | family | — | — | **$4.50-$31.00** | Buy | **VERIFIED** — [REV structure](https://www.revrobotics.com/ftc/structure/) | Ships inside `REV-45-2470` (408 mm ×4, 248 mm ×2) |
| 45 mm U-Channel | REV Robotics | family | — | — | **$2.50-$44.00** | Buy | **VERIFIED** | *"Square profile designed for additional torsional strength"* |
| 15 mm Extrusion (15 × 30 mm) | REV Robotics | family | — | — | **$6.00-$29.75** | Buy | **VERIFIED** | ⚠ **NEEDS-SKU-CHECK** per length |
| 15 mm Corner Brackets (8-pk) | REV Robotics | **`REV-41-1320-PK8`** | 4-8 pk | 8-16 pk | **$6.00-$12.50** | Buy | **VERIFIED** | 90° inside corner brackets with webbing |
| 15 mm Metal Brackets / Plastic Brackets | REV Robotics | families | — | — | **$5.50-$12.50** / **$5.00-$6.00** | Buy | **VERIFIED** (family) | **NEEDS-SKU-CHECK** |
| 45 mm Flat Plates | REV Robotics | family | — | — | **$2.50-$12.50** | Buy | **VERIFIED** (family) | *"bendable metal with Extended Motion Pattern"* — **[J] a bendable plate is a genuinely useful no-mill part** |
| ⭐ **Polycarbonate Sheet** | REV Robotics | family | 1-2 sheets | **2-4 sheets** | **$11.00-$75.00** | Buy | **VERIFIED** — [REV structure](https://www.revrobotics.com/ftc/structure/) | ⭐ **[J] The impact-protection material of choice.** ✅ Legal raw material per **[C] R302** (*"sheet stock… plastic"*). Cuts with hand tools, will not shatter. **NEEDS-SKU-CHECK on thickness/price pairs** |
| MAXComposite Sheet | REV Robotics | family | 0 | 0 | **$150.00-$225.00** | Buy | **VERIFIED** (family) | **[J] Out of budget for a two-robot program.** Noted for completeness |
| M3 Nut Strips | REV Robotics | family | — | — | **$2.50-$5.50** | Buy | **VERIFIED** (family) | REV ecosystem fastening |

**[J] Ecosystem note, restated from `VENDOR-ECOSYSTEMS.md`: pick goBILDA (8 mm grid, M4) or REV (15 mm extrusion, M3) and stay there for the frame.** Mixing hole patterns in one chassis produces a frame that is neither, and produces two robots that are definitely not the same.

### 8.4 FABRICATE / ASSEMBLE IN-HOUSE

**[C] R302** makes all of it legal: *"Allowed raw materials and legal COTS parts can be modified (drilled, cut, painted, etc.)"* — raw materials explicitly include *"sheet stock, extruded shapes, metals, plastic, rubber, and wood."* **[C] R304** makes it legal to do it **before kickoff**.

| What you make | Tooling required | Material | Student-hours (per robot) | **[J] Buy instead?** |
|---|---|---|---|---|
| **Perimeter impact guards / corner bumpers** | Hand-cut polycarb, heat gun for bends, drill | 2-3 mm polycarbonate | **3-5 h** | ❌ Fabricate. ⚠ Must fit inside **[C] R102**'s cube and must not be a wedge (**[C] R202.H**) |
| **Belly pan / skid plate** | Hand-cut polycarb, drill | 2-3 mm polycarbonate | **1-2 h** | ❌ Fabricate. **[J] Also the natural mounting surface for an OTOS (§7.4)** |
| **Electronics bulkhead / wire-routing plate** | Hand-cut polycarb, drill, zip-tie anchors | 2-3 mm polycarbonate | **2-3 h** | ❌ Fabricate. Pays for itself at every inspection |
| **Battery tray and retention** | 3D printer, hand tools | PETG | **1-2 h** | ❌ Fabricate. **[C] R601**'s single battery must not move |
| **Control Hub mounting plate** | 3D printer or hand-cut polycarb | PETG / 3 mm polycarb | **1-2 h** | ❌ Fabricate. ⚠ **[C] R706 forbids replacing the Hub's enclosure — print MOUNTS, never enclosures** |
| **Chain/belt guards** (if you run them) | 3D printer or polycarb | PETG | **1-2 h** | ❌ Fabricate — **[C] R202** entanglement |
| **Deburring every cut edge** | File, deburring tool, sandpaper | — | **0.5-1 h** | ❌ **Mandatory** — **[C] R202** prohibits *"exposed sharp edges or sharp protrusions."* **[J] The cheapest inspection pass you will ever buy** |
| **ROBOT SIGNS mounting** | Printer, adhesive, polycarb backing | — | **0.5 h** | ❌ **[C] R401** requires **a minimum of two ROBOT SIGNS per ROBOT in at least 2 separate locations.** See `LEGAL-PARTS-CONSTRAINTS.md` for the exact size spec — **[J] one printed sheet yields a complete set in both alliance colours; two robots need two sheets** |
| Cutting channel to length | Hacksaw / chop saw, file | goBILDA 1120 | 0.5 h per piece | ✅ **Buy the pre-cut bundle** wherever you can |

**[D] Total fabricate hours for M3: ≈ 10-16 student-hours for robot A, ≈ 6-10 for robot B** (the print files and templates transfer).

### 8.5 Approximate subtotal

| Path | Per robot | **For 2 robots** | Notes |
|---|---|---|---|
| **A. Frame comes inside the chassis kit** (§9 recommended) | **$0 extra** | **$0 extra** | ⭐ Strafer ships 2× 1120 10-hole 264 mm + 2× 1120 17-hole 432 mm (VERIFIED) |
| **B. Superstructure channel from the shared bundle** | ≈ **$110** (half of $219.99) | **$219.99** | For everything above the drive base |
| **C. Polycarbonate for pans, bulkheads and guards** | **$25-$75** | **$50-$150** | **NEEDS-SKU-CHECK** on thickness/price |
| **D. Standoffs + spacers bundles** | ≈ **$93** (half) | **$186.98** | `3203-1501-0001` + `3203-1502-0001` |
| **E. Fasteners** | ≈ **$27** (half) | ~**$54.99** | ⚠ **out of stock — source elsewhere** |
| **[D] Realistic M3 total** | **≈ $255-$305** | **≈ $510-$610** | On top of the chassis kit |

### 8.6 Common failure modes and the spares to stock

| Failure mode | Why it happens | Symptom | **Spare / mitigation** |
|---|---|---|---|
| ⚠ **Frame flexes; bolt holes elongate** | Under-supported channel; over-torqued M4 in thin material | **Progressive, invisible loss of auto accuracy.** Nothing looks broken | Spare 1120 channel from the bundle. **[J] The most insidious failure in this file — a flexing frame silently un-tunes your odometry** |
| **Fasteners loosen** | Vibration | Rattles, then slop, then misalignment | **Blue thread locker at first assembly + a torque check before every event.** A shop rule, not a spare |
| **Polycarbonate cracks at a bolt hole** | Hole drilled too close to an edge; over-torque | A guard falls off mid-match | Keep offcut stock. **[J] 2× hole diameter minimum edge distance; use washers** |
| **Printed bracket creeps or delaminates** | PLA under sustained load; layer-line loading | Something sags after a few weeks | Print in **PETG**, orient layers across the load. Keep spare prints of anything structural |
| **Sharp edge found at inspection** | A cut nobody deburred | ⛔ **Fails inspection** — **[C] R202** | A file in the pit kit. **[J] Deburr as you cut, not the night before** |
| **ROBOT SIGN missing or damaged** | Adhesive, contact | ⛔ **Fails inspection** — **[C] R401** | **[J] Print spare sign sheets. They cost pennies and they are a hard inspection gate** |
| **Battery shifts in its tray** | Impact | Brownouts, or a disconnect mid-match | Spare printed tray + a positive retention strap. **[C] R601** |

### 8.7 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum (the B team)** | **Competitive version (the A team)** |
|---|---|---|
| **Frame** | Kit chassis frame, unmodified | Kit chassis frame + a channel superstructure |
| **Protection** | Deburred edges + a polycarb belly pan | Belly pan + polycarb corner guards + chain/belt guards |
| **Electronics** | Hub bolted to a printed plate | Dedicated bulkhead with routed, labelled, strain-relieved wiring |
| **[D] Extra cost** | **≈ $50-$100** | **≈ $255-$305** |
| **Student-hours** | 5-8 h | 10-16 h |
| **[J] Why** | Legal, safe, passes inspection, and does not eat build time the B team needs elsewhere | Rigidity is auto accuracy; a clean bulkhead is a fast pit repair; guards keep a bad collision from ending a day |

**[J] The one non-negotiable for BOTH robots: deburr everything, mount two ROBOT SIGNS, and retain the battery.** Those three are inspection gates (**[C] R202**, **[C] R401**, **[C] R601**) and they cost almost nothing. Everything else in §8 is optional.

---

## 9. The kit-versus-parts decision, decided

**[J] This is the highest-leverage purchase decision of the season for a two-robot program, so it gets its own section and a stated answer rather than a menu.**

### 9.1 It is legal — settle that first

**[C] R301*** (p. 69) prohibits *"COTS MAJOR MECHANISMS purposefully designed to complete a game task"*, **but names two exceptions verbatim**:
> *"A. **COTS drive CHASSIS, provided none of the individual parts violate any other rules**, and B. COTS MAJOR MECHANISMS created as part of the official FIRST Tech Challenge StarterBots."*

✅ **A complete COTS drive chassis is explicitly, unambiguously legal.** **[J] It is also not a "cheat" or a shortcut in the judges' eyes** — see `reference/AWARD-ALIGNMENT-MATRIX.md`; what judges reward is the *reasoning*, and "we bought the chassis so our students could spend forty hours on the game mechanism instead of forty hours on a rectangle" is a strong, honest engineering-notebook entry.

### 9.2 The full comparison, two robots, all verified 2026-08-22

| Option | SKU | Per robot | **For 2 robots** | **[D] Δ vs recommended** | Assembly hours (program) | **DUPLICABILITY** | Stock 2026-08-22 |
|---|---|---|---|---|---|---|---|
| ⭐ **goBILDA Strafer (Ø104 mm mecanum)** | `3209-0001-0007` | **$699.99** | ⭐ **$1,399.98** | — | **≈ 20 h** | **5** | **In Stock** |
| **REV Mecanum Drivetrain Kit V2** | `REV-45-2470` | **$520.00** | **$1,040.00** | **−$359.98** | ≈ 24-30 h | **5** | **In Stock** |
| goBILDA BeeLine V2 (6WD hybrid) | `3209-0002-0002` | $649.99 | **$1,299.98** | −$100.00 | ≈ 22 h | **4** | **In Stock** |
| goBILDA Strafer (Ø140 mm mecanum) | `3209-0012-0002` | $799.99 | $1,599.98 | +$200.00 | ≈ 20 h | 5 | **In Stock** |
| goBILDA Outlaw | `3209-0005-0001` | $799.99 | $1,599.98 | +$200.00 | ? | ? | **In Stock** ⚠ drivetrain type unverified |
| goBILDA Hammerhead | `3209-0003-0001` | $449.99 | $899.98 | −$500.00 | ? | ? | **In Stock** ⚠ contents unverified |
| goBILDA Recon (cheapest) | `3209-0004-0001` | $349.99 | $699.98 | −$700.00 | ? | ? | **In Stock** ⚠ **motor count unverified** |
| **Build-from-parts, mecanum** | — | ≈$850-$1,050 | **≈$1,700-$2,100** | **+$300 to +$700** | **≈ 50-70 h** | **3** | mixed; ⚠ M4 assortment **out of stock** |
| Half-omni tank, from parts, 2 motors | — | ≈$400-$500 | ≈$800-$1,000 | −$400 to −$600 | ≈ 30-40 h | 4 | |
| ⛔ goBILDA Overlander (20V line) | `3209-0013-xxxx` | $539.99-$699.99 | — | — | — | — | ⛔ **[C] R601 — 12V NiMH only. NOT AN FTC PURCHASE** |

### 9.3 The two findings that decide it

**[D] FINDING 1 — the kit is cheaper AND faster than building from parts.** $1,399.98 vs $1,700-$2,100, and ≈ 20 h vs ≈ 50-70 h. **[J] That is unusual enough to be worth restating: there is no trade here.** The build-from-parts path costs *more money* and *more time* and produces a *less repeatable* result. The only thing it buys is the experience of building a chassis from parts — which is real pedagogical value, and which you can get for free on the practice chassis under **[C] R304**.

**[D] FINDING 2 — REV's kit is $359.98 cheaper across two robots, and that is a real option, not a footnote.** `REV-45-2470` at $520.00 ships (VERIFIED, product page): 4× UltraPlanetary Gearbox Kit & HD Hex Motor, 4× Ultra 90 Degree Gearbox, a 75 mm Mecanum Wheel Set, 4× 408 mm and 2× 248 mm 45×15 mm C-channel, 15 mm plastic 90° brackets, hex shafts, spacers, shaft collars, M3 hardware, and tools.

**[J] Why I still recommend the Strafer despite REV being cheaper — state the reasons so the team can disagree with them:**

| Factor | Strafer `3209-0001-0007` | REV `REV-45-2470` |
|---|---|---|
| Wheel size | **Ø104 mm**, 40A GripForce, *"tuned for… FIRST Tech Challenge"* tiles | **75 mm**, smaller and slower per revolution (**[D]** 235.6 mm/rev vs 326.7 mm/rev) |
| Motors | **4× 5203 Yellow Jacket, 19.2:1, 312 RPM, encoder built in, $54.99 to replace** | 4× HD Hex + UltraPlanetary cartridges + 4× Ultra 90. ⚠ **Ratio, output RPM and encoder spec NEEDS-SKU-CHECK** |
| Assembly | Fewer, larger parts; shouldered hub-shafts | More small parts (cartridges, collars, 3 hardware packs) — **[J] more chances for two robots to diverge** |
| Motor replacement mid-season | One SKU, one price, any ratio | Motor + cartridges + 90° box |
| **[D] Cost, 2 robots** | $1,399.98 | **$1,040.00** |
| **[J] Verdict** | ⭐ **Recommended** | **[J] Choose this if the $360 matters more than the 104 mm wheels and the single-SKU motor** — a legitimate call for a tight budget |

### 9.4 The decision, stated

> **[J] BUY TWO goBILDA Strafer Chassis Kits (`3209-0001-0007`), in ONE order, BEFORE kickoff.**
>
> 1. **It is legal now** — **[C] R301.A**.
> 2. **It is buildable now** — the drivetrain lives entirely inside **[C] R102**'s 18 in cube, which is already final. Nothing about it depends on the game. **[C] R105**'s expansion limits are deferred to kickoff and do not touch it.
> 3. **It is cheaper and faster than parts** (§9.3, Finding 1).
> 4. **Duplicability 5/5** — the two robots are identical *by construction*, not by discipline. This is the entire reason the recommendation is this firm for *this* program and would be softer for a single-robot team.
> 5. **One order** — same price, same revision, same stock, shipped together. **[J] Two orders three weeks apart is how you end up with two subtly different robots and a mystery you never solve.**
>
> **Budget: $1,399.98 + $750.00 (2× Control Hub `REV-31-1595`) + $550.00 (2× Driver Hub `REV-31-1596`) + ≈ $260 (batteries) ≈ $2,960** before a single game mechanism exists. **[D] Add $169.90 for two OTOS and the whole moving-and-knowing-where-you-are problem is solved for ≈ $3,130.**

**[J] The one thing that would change this answer:** kickoff (2026-09-12) reveals a **barrier, ramp, gap or textured surface**. Then switch to **2× BeeLine V2 `3209-0002-0002` ($1,299.98)** — which is *cheaper* — and re-read §3.2.4. **[J] Do not pre-buy against a guess; do decide within 48 hours of kickoff, because lead time is the enemy** (`research/SEASON-CADENCE.md`).

---

## 10. The R503 actuator budget, drivetrain-first

**[C] R503*** (p. 77), verbatim: *"ROBOTS are limited to a total of 8 motors and 8 servos. A ROBOT may not have more than 8 motors and 8 servos from the allowable actuator lists per R501 and R502 **for all MECHANISMS used in all configurations**."* Its blue box adds: *"If a ROBOT has multiple configurations used at a single event which use different MECHANISMS, the sum total of all motors and servos must be less than or equal to the limit set in this rule."*

⚠ **[H] → [C] This is a REDUCTION.** DECODE allowed **10** servos; BIOBUZZ allows **8**. **[J] Any prior-season design, any prior-season notebook, and any returning student's mental model may now be illegal. Check every carried-over design against 8+8.**

### 10.1 What each drivetrain leaves you

**[J] Read this table as "what budget does my drivetrain choice leave for the actual game?" — because that is the only question that matters on kickoff day.**

| Drivetrain | Motors used | **Motors left** | Servos used | **Servos left** | **[J] What that buys** |
|---|---|---|---|---|---|
| **2-motor tank / half-omni** | **2** | ⭐ **6** | 0 | **8** | ⭐ **The motor-rich option.** Six motors is an intake + a two-stage lift + a launcher + a spare |
| **4-wheel mecanum** | **4** | **4** | 0 | **8** | ⭐ **The balanced default.** Four motors covers an intake, a lift, and a game-specific mechanism |
| **4-motor tank (4 traction)** | 4 | 4 | 0 | 8 | Same budget as mecanum, more pushing, worse turning |
| **6WD BeeLine V2** | **4** | **4** | 0 | **8** | Same as mecanum — the extra wheels are belted, not motored |
| **X-drive** | 4 | 4 | 0 | 8 | Same budget, worse packaging (§3.2.5) |
| **Coaxial swerve, servo steering** | 4 | 4 | **4** | **4** | ✅ Legal and it fits — **[J] but §3.2.6's objection is fabrication, not budget** |
| ⛔ **Coaxial swerve, motor steering** | **8** | **0** | 0 | 8 | ⛔ **[D] Your entire motor budget, gone. Zero motors for any game task** |
| ⛔ **Differential swerve** | **8** | **0** | 0 | 8 | ⛔ Same |

**[D] The 2-motor vs 4-motor decision is worth exactly two motor slots — 25% of your entire motor budget — and it is made on the drivetrain, before you know the game.** That is why §1 flags it as the number that frames everything.

### 10.2 What costs you nothing

**[J] Know these, because they are where a small team finds headroom:**

| Item | R503 cost | Authority |
|---|---|---|
| **Encoders (drive or dead-wheel)** | **0** | Sensors, not actuators |
| **Odometry pods** (Pinpoint, OctoQuad, 4-Bar, Swingarm) | **0** | Sensors; **[C] R303.J** treats the kits as legal COTS |
| **OTOS, IMU, distance sensors, cameras, Limelight 3A** | **0** | Sensors / coprocessors, **[C] R702** |
| **Motors integral to a COTS sensor** (e.g. LIDAR, scanning sonar) | **0** | **[C] R501**, verbatim: *"These motors do not count toward the limit in R503"* |
| **Vibration/autofocus motors inside a COTS computing device** | **0** | **[C] R501**, same carve-out |
| Gas springs, constant-force springs, rubber bands | **0** | Not actuators. ⚠ **[C] R801** allows only manufacturer-sealed pre-charged closed-air systems |

⚠ **What does NOT buy you headroom: servo expanders.** `LEGAL-PARTS-CONSTRAINTS.md` covers the goBILDA Servo Power Injector `3125-0001-0001`, REV Servo Power Module `REV-11-1144`, REV Servo Hub `REV-11-1855` and REV SPARKmini `REV-31-1230`. **[D] These expand PORTS and POWER. They do not raise the R503 limit of 8 servos.** ⚠ **Verify each against the manual's table before recommending it** — per-port limits apply.

**[D] A useful port-vs-rule note from `LEGAL-PARTS-CONSTRAINTS.md`:** the maximum legal control topology (Control Hub + one Expansion Hub per **[C] R701**) gives **8 motor ports and 12 servo ports**. **So motor ports and R503 bind at exactly the same number (8), while servos are rule-limited (8) below your port capacity (12).** **[J] You will never run out of servo ports; you will run out of servo *allowance*.**

### 10.3 The budget statement every archetype BOM must carry

**[J] Copy this block into every design proposal at kickoff. If a design cannot fill it in, it is not a design yet.**

```
R503 ACTUATOR BUDGET — [design name], [A robot / B robot]
  Drivetrain          : ___ motors  ___ servos
  Intake              : ___ motors  ___ servos
  Lift / extension    : ___ motors  ___ servos
  Scoring mechanism   : ___ motors  ___ servos
  Endgame mechanism   : ___ motors  ___ servos
  ------------------------------------------------
  TOTAL               : ___ / 8     ___ / 8      <- MUST be <= 8 and <= 8
  Localization        :   0 motors    0 servos   (sensors — free, see 10.2)
  Spare slots left    : ___          ___
Checked against: R501 (Table 12-1 allowlist), R502 (Table 12-2), R503 (8+8, all configurations)
```

---

## 11. Kickoff-day checklist — the drivetrain triage

**Kickoff: 2026-09-12. Game Q&A opens 2026-09-28, 12:00 p.m. ET. Team Updates post every Thursday.**

### 11.1 Before kickoff (do these now — all game-agnostic)

- [ ] **Order 2× Strafer `3209-0001-0007` in one order** (§9.4). Legal under **[C] R301.A**; buildable now under **[C] R304**.
- [ ] **Order 2× Control Hub `REV-31-1595`** (**[C] R701.A**), **2× Driver Hub `REV-31-1596`**, **4× battery `3100-0012-0020`** (**[C] R601**).
- [ ] **Order 2× OTOS `SEN-24904` ($169.90)** — game-agnostic, cheap, zero R503 cost. Add the **Qwiic-to-STEMMA cable** (NEEDS-SKU-CHECK).
- [ ] **Order the spares kit (§3.6): 2 spare 5203 motors, 1× `3611-0040-0104` roller pack, 4× `1611-0514-4008` bearing packs, 2 spare JST-PH encoder cables, thread locker, 20 A ATM mini blade fuses.** ≈ $250-$300.
- [ ] 🕐 **Source M4 hardware from a general fastener supplier** — goBILDA's `3201-0004-0001` assortment was out of stock on 2026-08-21 **and** 2026-08-22.
- [ ] **Build and wire both chassis. Deburr everything (R202). Mount two ROBOT SIGNS each (R401). Retain both batteries (R601).**
- [ ] **Write and test the localization calibration OpMode**, and a `COMPETITION_MODE` flag that kills every dashboard call (**[C] R704.C/D**).
- [ ] **Measure and record per-robot constants in a per-robot config file** (§7.6's duplicability trap).

### 11.2 In the first 90 minutes after kickoff

| # | Question to answer from the real manual | Section to re-open | Decision it forces |
|---|---|---|---|
| 1 | **Is the field flat?** Any barrier, ramp, gap, seam or textured surface? | §3.2.4, §4 | Mecanum stands, or switch to **BeeLine V2** |
| 2 | **What are the R105 expansion limits?** V0 defers them: *"Sizing Constraints and more details will be released at Kickoff"* | §2 | Drivetrain is largely immune — but confirm |
| 3 | **Does scoring require precise repeated alignment?** | §7 | Whether to spend $559.98 on the pod packs |
| 4 | **Are there AprilTags on the field, and where?** | §7.2.7 | Whether to buy a **Limelight 3A** (`LL_3A` only — the **3G is prohibited**) |
| 5 | **Is this a pushing/defense game?** | §4.2, §5.4, §5.5 | 30A rubber and/or ballast **before** a lower gear ratio |
| 6 | **How far apart are the scoring and loading zones?** | §5.3, §5.5 | 312 RPM stands, or move to 435 RPM |
| 7 | **How many mechanisms does the game demand?** | §10 | 2-motor tank vs 4-motor mecanum — **worth 2 of 8 slots** |
| 8 | **Diff Table 12-1 and Table 12-9** against this file | §5.1, §7.2.7 | New legal motors or vision coprocessors |
| 9 | **Re-grep every R-rule cited here** against the kickoff manual | §2 | Section 12 is final, but confirm |

### 11.3 Standing, all season

- [ ] **Read every Thursday Team Update.** Additions are highlighted yellow, deletions struck through. Re-diff Tables 12-1 and 12-9.
- [ ] **Re-verify every price and stock status in this file before ordering.** Everything here is dated **2026-08-22** and is marked **VERIFY-BEFORE-ORDER**.
- [ ] **Torque-check every drivetrain fastener before every event** (§3.6, §8.6).
- [ ] **Re-measure the OTOS 10 mm gap at every event** (§7.6).

---

## 12. Verification log — every URL loaded this session (2026-08-22)

**[J] This log exists so a future reader can tell the difference between what I read and what I inferred.** Sections §0-§3 were written in an earlier pass on the same date and carry their own verification; this log covers the pass that wrote §4-§13 and re-verified the headline claims in §3.

| # | URL | What it yielded | Result |
|---|---|---|---|
| 1 | [gobilda.com/chassis-kits/](https://www.gobilda.com/chassis-kits/) | All 14 chassis kits: SKU, price, **stock**, 12V vs 20V split | ✅ **Confirms §3.3.1.** Overlander-4 and -4 (No Battery) now show **Out of Stock** |
| 2 | [gobilda.com/strafer-chassis-kit-104mm-gripforce-mecanum-wheels/](https://www.gobilda.com/strafer-chassis-kit-104mm-gripforce-mecanum-wheels/) | `3209-0001-0007`, **$699.99, In Stock**, full contents, 4,269 g, "Version 7.0" | ✅ **Re-confirms the headline recommendation** |
| 3 | [gobilda.com/yellow-jacket-planetary-gear-motors/](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | **Complete 5201/5202/5203/5204 ratio ladder** with per-ratio SKUs, RPM, stall torque, price | ✅ **Resolves §3.3.2's NEEDS-SKU-CHECK on per-ratio motor SKUs** |
| 4 | [gobilda.com/5203-…-312-rpm-…/](https://www.gobilda.com/5203-series-yellow-jacket-planetary-gear-motor-19-2-1-ratio-24mm-length-8mm-rex-shaft-312-rpm-3-3-5v-encoder/) | `5203-2402-0019` full spec: **9.2 A stall, 0.25 A no-load, 537.7 PPR**, $54.99, In Stock | ✅ Enables §5.4 and §5.6 |
| 5 | [gobilda.com/mecanum-wheels/](https://www.gobilda.com/mecanum-wheels/) | 3 wheel sets + **3 roller packs** with SKUs and prices | ✅ §4.3 |
| 6 | [gobilda.com/omni-wheels/](https://www.gobilda.com/omni-wheels/) | 4 omnis with **stock status**; `3624-4008-0032` **OUT OF STOCK** | ✅ §4.3, §7.2.6 |
| 7 | [gobilda.com/hogback-traction-wheels/](https://www.gobilda.com/hogback-traction-wheels/) | 2 wheels, 50A, SKUs and prices | ✅ §4.3 |
| 8 | [gobilda.com/rhino-wheels/](https://www.gobilda.com/rhino-wheels/) | 9 Rhino variants incl. **30A High-Traction** | ✅ §4.3 |
| 9 | [gobilda.com/gripforce-gecko-wheels/](https://www.gobilda.com/gripforce-gecko-wheels/) | 4 Gecko wheels — vendor copy positions them as **intake** wheels | ✅ §4.3 correction |
| 10 | [gobilda.com/odometry/](https://www.gobilda.com/odometry/) | 5 products: Pinpoint V2, 2 packs, 2 pods, all with SKUs and prices | ✅ §7.3 |
| 11 | [gobilda.com/pinpoint-v2-…/](https://www.gobilda.com/pinpoint-v2-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/) | `3110-0002-0002`, **$79.99, In Stock**, full V2 spec | ✅ §7.2.4 |
| 12 | [gobilda.com/pinpoint-odometry-computer-…/](https://www.gobilda.com/pinpoint-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/) | v1 `3110-0002-0001` — **"Discontinued and Sold Out"** | ⚠ **The procurement trap in §7.3** |
| 13 | [gobilda.com/4-bar-odometry-pod-32mm-wheel/](https://www.gobilda.com/4-bar-odometry-pod-32mm-wheel/) | `3110-0001-0002`, **$99.99, In Stock**, **2000 events/rev**, 84 g, 43×43 mm mount | ✅ §7.2.4, §7.4 |
| 14 | [sparkfun.com/…-otos-paa5160e1-qwiic.html](https://www.sparkfun.com/sparkfun-optical-tracking-odometry-sensor-paa5160e1-qwiic.html) | `SEN-24904`, **$84.95, In Stock**, **10 mm working distance for FTC tiles**, 3-5% → <1% accuracy | ✅ §7.2.3 — ⚠ price discrepancy vs Phase A |
| 15 | [tindie.com/…/octoquad-ftc-ed-mk2-…/](https://www.tindie.com/products/digitalchickenlabs/octoquad-ftc-ed-mk2-8x-encoderpwm-imu/) | **$59.99**, 8ch + IMU + **1.92 kHz localizer**; page claims *2025-26* legality | ✅ §7.2.5 — BIOBUZZ R702 Ex. 3 is the stronger source |
| 16 | [revrobotics.com/ftc/motion/](https://www.revrobotics.com/ftc/motion/) | **`REV-45-2470` $520.00**, `REV-41-1600` $50.00, `REV-41-2080` $45.00, belts/sprockets/turnbuckle | ✅ §5.7, §6.4, §9 |
| 17 | [revrobotics.com/rev-45-2470/](https://www.revrobotics.com/rev-45-2470/) | **Full contents of the Mecanum Drivetrain Kit V2**, In Stock | ✅ **§9.3 Finding 2 — a genuinely cheaper kit** |
| 18 | [revrobotics.com/ftc/structure/](https://www.revrobotics.com/ftc/structure/) | C-channel, U-channel, extrusion, brackets, **polycarbonate $11-$75**, MAXComposite, flat plates | ✅ §8.3 |
| 19 | [revrobotics.com/rev-11-3174/](https://www.revrobotics.com/rev-11-3174/) | Through Bore Encoder **V2, $48.00, In Stock**, 8192 cts/rev, ±0.5° | ✅ §7.3 |
| 20 | [revrobotics.com/rev-11-1271/](https://www.revrobotics.com/rev-11-1271/) | Through Bore Encoder **V1 — marked DISCONTINUED** (in stock, $40.80) | ⚠ §7.3 |
| 21 | [gobilda.com/motor-mounts/](https://www.gobilda.com/motor-mounts/) | 21 mounts with SKUs and prices; the named-fit ones are **5201 Series** | ⚠ §6.6 — partial |
| 22 | [gobilda.com/hubs/](https://www.gobilda.com/hubs/) | **Sub-category names only — no SKUs, no prices** | ⚠ §6.3 — **FAMILY-ONLY**, same as Phase A |
| 23 | [gobilda.com/u-channel/](https://www.gobilda.com/u-channel/) | **Families only** (1120 / 1121 / 1143 / 1122) — no SKUs or prices | ⚠ §8.3 — **FAMILY-ONLY** |
| 24 | [gobilda.com/wheels-tires/](https://www.gobilda.com/wheels-tires/) | 14 sub-category names only | ⚠ navigation only |
| 25 | `gobilda.com/wheels/` | **Redirect notice** → `/wheels-tires/` | ⚠ dead URL — do not cite |
| 26 | [andymark.com/collections/ftc-chassis](https://www.andymark.com/collections/ftc-chassis) | Page loaded; **rendered NO product data** | ⛔ **Second failure** (also failed in Phase A). **Browse manually** |
| 27 | `andymark.com/collections/ftc-wheels` | **HTTP 404** | ⛔ dead URL |
| 28 | `gobilda.com/pulleys-belts/`, `gobilda.com/belts-pulleys/`, `gobilda.com/motion-components/` | **HTTP 404** ×3 | ⛔ **Could not verify goBILDA belt/pulley/chain SKUs this session.** §6.4 is family-level only |
| 29 | `studica.com` | Not re-attempted; **HTTP 403 in Phase A and confirmed blocked** | ⛔ **Cannot verify any Studica part** |
| 30 | Local: `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` | Grepped **R102, R103, R104, R201, R202, R303, R501/Table 12-1, R502, R503, R601, R613, R702/Table 12-9, R704, R711** | ✅ Every legality claim in §4-§11 traces to a grep of this file |

**Vendor status note.** **Official FIRST suppliers:** AndyMark, Studica (both **unverifiable by WebFetch this session**). **General suppliers used heavily here:** goBILDA, REV Robotics, SparkFun. **Neither:** Digital Chicken Labs (sold via Tindie). **[J] The irony is worth stating: the two official FIRST suppliers are the two I could not verify, and the two vendors this file leans on hardest are general suppliers.** Nothing about that is illegal — **[C] R301/R302/R303** care about the *part*, not the storefront — but a team relying on official-supplier purchase orders should browse AndyMark and Studica manually before assuming this file covers their catalogue.

---

## 13. Open questions / NEEDS-SKU-CHECK register

**[J] Every row here is a place where an AI would be tempted to invent a plausible answer. I did not. Resolve these by loading the page or calling the vendor.**

| # | Open item | Section | Why it matters | How to resolve |
|---|---|---|---|---|
| 1 | ⚠ **OTOS price discrepancy: $79.95 (Phase A, 2026-08-21) vs $84.95 (me, 2026-08-22)** | §7.3 | A $10 error across two robots; also a signal that prices are moving | Load the SparkFun page immediately before ordering |
| 2 | **goBILDA Recon `3209-0004-0001` contents** — no itemised parts list, **motor count and drivetrain type unstated** | §3.3.1, §9.2 | It is the cheapest kit at $349.99; if it includes motors it changes §9 | Call goBILDA. **Do not assume motors are included** |
| 3 | **goBILDA Hammerhead `3209-0003-0001`** — product page 404'd in the earlier pass | §3.3.1, §9.2 | $449.99, drivetrain type unknown | Load the product page |
| 4 | **goBILDA Outlaw `3209-0005-0001`** — drivetrain type not stated on the category page | §3.3.1, §9.2 | $799.99, FTC suitability unknown | Load the product page |
| 5 | **REV HD Hex / UltraPlanetary output RPM, stall torque, encoder spec** | §5.7, §9.3 | Without it, §5's arithmetic cannot be repeated for the REV path | Load `REV-41-1600` and `REV-41-1291` pages |
| 6 | **goBILDA hub SKUs and prices** — category renders families only | §6.3 | Clamping vs set-screw is a named failure mode; you cannot order a family | Navigate to `/sonic-hubs/` etc. individually |
| 7 | **Which motor mount actually fits a 5203** — the "quad block pattern mounts" inference | §6.6 | Ordering the 5201-fit mount wastes an order cycle | Confirm on the 1201-series product page or with goBILDA |
| 8 | **goBILDA belt, pulley, chain and sprocket SKUs** — three category URLs 404'd | §6.4 | Needed only for a tank/6WD build | Find the live category URL from goBILDA's own nav |
| 9 | **goBILDA U-channel individual SKUs/prices** | §8.3 | Only matters if you buy outside the 17-pc bundle | Load individual product pages |
| 10 | **REV polycarbonate thickness↔price pairs** | §8.3 | $11-$75 is too wide to budget against | Load the polycarbonate product page |
| 11 | **Qwiic-to-STEMMA cable SKU and price** for the OTOS | §7.3, §11.1 | The OTOS does not work without it. **[J] The classic forgotten $5 part that costs a week** | Load SparkFun's cable listing |
| 12 | **Swingarm pod `3110-0001-0001` counts-per-revolution** | §7.3 | Needed to compute its resolution against the 4-Bar's 2000 | Load the Swingarm product page |
| 13 | **OctoQuad MK2 stock status and SDK driver availability** | §7.2.5 | Precedent: the MK2 needed a vendor driver the SDK did not ship | Tindie listing + `research/PROGRAMMING-PRACTICE.md` |
| 14 | **Limelight 3A `LL_3A` price and availability** | §7.2.7 | Deferred to kickoff anyway | Load Limelight's storefront **after** kickoff |
| 15 | ⛔ **All AndyMark parts** — storefront rendered no product data on two dates | §5.7, §9.2, §12 | An **official FIRST supplier** is entirely unverified here | Browse `andymark.com` manually |
| 16 | ⛔ **All Studica parts** — HTTP 403 on both dates | §5.7, §12 | Same; the Maverick `75001` is a legal motor per Table 12-1 | Browse `studica.com` manually |
| 17 | 🕐 **goBILDA M4 assortment `3201-0004-0001` out of stock on two dates** | §3.3.2, §8.3, §11.1 | A build-stopper three weeks before kickoff | **Source M4 hardware from a general fastener supplier NOW** |
| 18 | 🕐 **goBILDA Ø32 mm omni `3624-4008-0032` out of stock on two dates** | §4.3, §7.2.6 | Kills the roll-your-own pod path — which §7.2.6 rejects anyway | Buy complete pods instead |
| 19 | ⚠ **[C] R105 expansion limits — DEFERRED BY THE MANUAL** | §2, §11.2 | V0 states outright: *"Sizing Constraints and more details will be released at Kickoff"* | **Kickoff, 2026-09-12.** Drivetrain is largely immune |
| 20 | 🕐 **Table 12-1 and Table 12-9 may gain entries** | §5.1, §7.2.7 | V0 says so explicitly: *"Additional motors may be added… in future competition manual updates"* | Re-diff at kickoff and after every Thursday Team Update |

---

## Closing note

**[J] If this file is read in a hurry on kickoff day, read only these five lines:**

1. **Buy two Strafer chassis kits (`3209-0001-0007`, $699.99 each) in one order.** It is legal (**[C] R301.A**), it is cheaper *and* faster than building from parts, and it makes the two robots identical by construction.
2. **Use 5203 Yellow Jackets at 19.2:1 / 312 RPM** (`5203-2402-0019`, $54.99). §5's arithmetic shows you are traction-limited, not torque-limited, so gearing down buys a number you cannot use.
3. **Your drivetrain choice costs 2 or 4 of your 8 motors under [C] R503 — decide that deliberately.** Localization costs zero.
4. **Buy localization; it has commoditized.** $169.90 buys two OTOS. $559.98 buys two full pod packs. Neither touches your actuator budget.
5. **Nothing in this file depends on the game**, which is exactly why the drivetrain is the one subsystem you can finish before 2026-09-12 — legal under **[C] R304**.

**Every price here is US list as of 2026-08-22, pre-discount, pre-tax, pre-shipping, and marked VERIFY-BEFORE-ORDER.**
