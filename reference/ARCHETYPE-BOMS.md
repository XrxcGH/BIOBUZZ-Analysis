# ARCHETYPE BILLS OF MATERIALS

### Worked mechanism breakdowns and costed BOMs for every robot archetype, for a two-team, ~15-student, modest-budget FTC program

---

> ## ⚠ THESE ARE GAME-AGNOSTIC TEMPLATES
>
> **BIOBUZZ Kickoff is 2026-09-12. Today is 2026-08-22. The game is not public.**
>
> Nothing in this file knows what a SCORING ELEMENT looks like, how tall the goals are, or what the endgame
> pays. What it *does* know is **Section 12 ROBOT Construction Rules, which is already FINAL for BIOBUZZ** —
> so the legality envelope, the actuator budget, the 18-inch cube and the whole electronics bill are knowable
> **right now**, and they are the majority of every BOM below.
>
> **On kickoff day you do not write a BOM. You pick the archetype row that matches the game, open the
> matching §2 subsection, and substitute three numbers:** element size (sets intake geometry), scoring height
> (sets extension), and endgame task (sets the last motor). Everything else is already priced.
>
> **The one thing that is genuinely deferred: R105 expansion limits.** R105 is final in *text* but its
> numeric expansion allowance is game-dependent. Every mechanism below marked 🕐 **EXPANSION-GATED** cannot be
> finally sized until the kickoff manual and the first Team Updates land. Flag those rows in the design review;
> do not pre-buy against them.

---

## Contents

| § | Section |
|---|---|
| **0** | How to read this file — labels, confidence tags, cost conventions |
| **1** | **THE PROGRAM PLATFORM** — the BOM every archetype pays before it scores a point |
| **2** | The archetype BOMs (§2.1 – §2.11) |
| **3** | Cross-archetype comparison — ranked by two-robot cost and by student-hours |
| **4** | Verification log — every page loaded this session |
| **5** | NEEDS-SKU-CHECK / UNVERIFIED register |

---

## 0. How to read this file

### 0.1 Provenance labels

| Label | Meaning |
|---|---|
| **[C] CONFIRMED-BIOBUZZ** | Stated in the BIOBUZZ V0 manual. Rule ID cited; grepped from `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` this session |
| **[H] HISTORICAL** | True of a prior season. May not survive kickoff |
| **[J] JUDGMENT** | My recommendation, calibrated to *this* program |
| **[D] DERIVED** | Arithmetic on the above |

### 0.2 Confidence tags on every parts row

| Tag | Meaning |
|---|---|
| **VERIFIED** | I loaded the vendor page **with WebFetch in this session (2026-08-22)** and read the SKU and price off it. See §4 |
| **PHASE-B** | The SKU/price comes from a Phase B catalog in `reference/mechanisms/` that carries its own verification log. **Trustworthy, but verified by a different agent** — not by me. Treated as one notch below VERIFIED |
| **FAMILY-ONLY** | I verified the **product family and its category page**, but the vendor category page showed no SKU or no price. Buy from the family; confirm the SKU at checkout |
| **NEEDS-SKU-CHECK** | Neither SKU nor price confirmed. **Do not put this on a purchase order without loading the page** |

> **ANTI-HALLUCINATION NOTE.** Every SKU printed in this file is either in §4's verification log (I read it),
> or carries a **PHASE-B** / **FAMILY-ONLY** / **NEEDS-SKU-CHECK** tag. No SKU here was written from memory.
> Where I could not verify, I named the family and linked the category page rather than inventing a part number.

### 0.3 Cost conventions — read before quoting any number to a parent or a sponsor

1. **All prices are US list price as of August 2026, before tax, shipping and discounts. VERIFY-BEFORE-ORDER.**
2. **Storefront prices are [H] HISTORICAL.** The FIRST storefront PDF I loaded is **Revision 25-26.4, dated
   Feb 18, 2026** — the **2025-26 DECODE** season sheet. The 2026-27 BIOBUZZ sheet has not been published.
   [J] Budget the 25-26 numbers and expect a modest increase.
3. **"Per robot" excludes the platform in §1 unless the table says otherwise.** §2's numbers are the
   *marginal* cost of the archetype's game mechanisms on top of a common platform. Totals in §2.x's rollup
   add the platform back in explicitly.
4. **Hardware allowances** (fasteners, bearings, spacers, shafts, belt/pulley) are **FAMILY-ONLY estimates**,
   flagged as such. They are real money — typically **15–25 % of a mechanism's COTS cost** — and the row that
   teams most often forget.
5. **Student-hours** use the duplication ratios from `reference/mechanisms/IN-HOUSE-FABRICATION.md` §8:
   printing ≈ **0.13–0.25**, jigged sheet work ≈ **0.35–0.50**, sawn stock ≈ **0.25–0.45**,
   assembly ≈ **0.55–0.65**, hand-tapping/hand-fitting ≈ **0.9–1.0** (no discount at all).

### 0.4 What this file does NOT re-derive

This file is a **specialization layer**. It picks parts; it does not explain them. For the reasoning, the
physics, the alternatives considered and the full vendor tables, go to the Phase A/B catalogs:

| Question | File |
|---|---|
| Which drivetrain, which wheels, which odometry, kit-vs-parts | `reference/mechanisms/DRIVETRAIN-AND-ODOMETRY.md` |
| Which intake, which gripper, transfer and anti-jam | `reference/mechanisms/INTAKE-AND-MANIPULATION.md` |
| Slides, arms, four-bars, turrets, climbing, springs | `reference/mechanisms/EXTENSION-ARMS-LIFTS.md` |
| Flywheels, catapults, feeds, aiming, launcher tuning burden | `reference/mechanisms/LAUNCHERS-AND-FEEDING.md` |
| Control system, power, wiring, sensors, vision | `reference/mechanisms/ELECTRONICS-AND-SENSING.md` |
| What to print/cut/saw, tooling tiers, student-hour model | `reference/mechanisms/IN-HOUSE-FABRICATION.md` |
| Vendor comparison, official vs general suppliers, lead times | `reference/VENDOR-ECOSYSTEMS.md` |
| The R-rule allowlists and the do-not-buy list | `reference/LEGAL-PARTS-CONSTRAINTS.md`, `reference/CONSTRUCTION-RULES-R.md` |
| Which archetype to pick at all | `reference/ROBOT-ARCHETYPE-LIBRARY.md` |
| Why the second robot costs what it costs | `research/SMALL-TEAM-ECONOMICS.md`, `playbook/TWO-ROBOT-PROGRAM.md` |
| The BOM emission format for a design review | `reference/BOM-PROTOCOL.md` |

---

# 1. THE PROGRAM PLATFORM — what every archetype pays before it scores a point

**[D] This is the most important section in the file, and it is the one teams skip.** Between **55 % and 85 %**
of a two-robot BIOBUZZ budget is spent *before any archetype-specific decision is made*. Drivetrain, control
system, driver station, power and localization are nearly archetype-independent. That means:

> **[D] Archetype choice moves ~15–45 % of the money and ~50–70 % of the student-hours.**
> Choose the archetype for **hours and risk**, not for cost. The cost argument is mostly already lost or won
> in §1.

## 1.1 The platform BUY table — verified this session

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Drive chassis kit ⭐** | goBILDA (general supplier) | Strafer® Chassis Kit **`3209-0001-0007`** — 104 mm GripForce mecanum, 4× 5203 312 RPM motors included | 1 | **2** | **$699.99 ea = $1,399.98** | **Buy** | **VERIFIED** — $699.99, **In Stock** 2026-08-22 | **[C] R301.A** explicitly permits a COTS drive CHASSIS. Cheaper *and* faster than building from parts (`DRIVETRAIN-AND-ODOMETRY.md` §9.3). Duplicability **5/5** — the two robots are identical by construction |
| Drive chassis kit (budget alt.) | REV Robotics | Mecanum Drivetrain Kit V2 **`REV-45-2470`** | 1 | 2 | **$520.00 ea = $1,040.00** | Buy | **VERIFIED** — $520.00 on `/ftc/motion/` | **−$359.98 across two robots.** 75 mm wheels, more small parts, more chances for the two robots to diverge. A legitimate call on a tight budget |
| **Control system kit ⭐** | **FIRST storefront (Pitsco)** — *official* | "Electronics Modules and Sensors Kit V1.1": Control Hub, Smart Robot Servo, Switch Cable & Bracket, Color Sensor V3, Touch Sensor, Resistive Grounding Strap, Cable Pack, M3 hardware | 1 | **2** | **$350 ea = $700** *(2026-27; was $325/$650 in 25-26)* | **Buy** | **VERIFIED** contents + price, contents from storefront PDF **Rev 25-26.4**; **price updated to the 2026-27 *FIRST* Cost & Registration figure ($350)** — see `research/SMALL-TEAM-ECONOMICS.md` §3.1 | 🕐 **"Limit one per registered team per season."** You have **two registrations**, so you get two. **This is the single largest financial return on the two-team structure.** Satisfies **[C] R701.A** in one order |
| **Driver station kit ⭐** | **FIRST storefront (Pitsco)** — *official* | "Driver Kit": REV Driver Hub ×1, FTC-legal gamepad ×2, FTC-legal webcam ×1 | 1 | **2** | **$295 ea = $590** *(2026-27; was $285/$570 in 25-26)* | **Buy** | **VERIFIED** contents + price, same PDF | 🕐 Same one-per-team limit. **The webcam in this kit is the vision system for archetypes §2.8 and §2.11 — you already own it.** |
| Control Hub (retail fallback) | REV Robotics | **`REV-31-1595`** — 4 motor ports, 6 servo ports, 8 DIO, 4 analog, 4 I²C, internal IMU | 0–1 | 0–2 | **$375.00 ea** | Buy | **VERIFIED** — $375.00, "In Stock & Ready To Ship!" | Only if the storefront limit is exhausted or you want a spare. **[C] R701** |
| Driver Hub (retail fallback) | REV Robotics | **`REV-31-1596`** | 0–1 | 0–2 | **$275.00 ea** | Buy | **VERIFIED** — $275.00, In Stock | Note **$275 retail vs $295 for the whole storefront Driver Kit** *including two gamepads and a webcam*. The storefront is not a small saving; it is a large one |
| **Main battery** | REV Robotics | 12V Slim Battery **`REV-31-1302`**, 10-cell 3000 mAh | 2 | **5 (program)** | **$60.00 ea ≈ $300** | Buy | **VERIFIED** price + In Stock. ⚠ **Chemistry NOT stated on the product page** — see Notes | **[C] R601** requires *"1 and only 1 approved 12V NiMH"* main battery. The REV page says "10-cell, 12V 3000 mAh" but does **not** print "NiMH" — **NEEDS-SKU-CHECK on chemistry before ordering.** [J] Buy **5 for the program, not 4**: batteries in rotation is what keeps two robots on a practice field |
| Battery charger | REV Robotics | Smart Charger family — 12V Slim Battery Accessories, **$6.00–$39.50** on `/ftc/electronics/` | — | **2 (shared)** | **≈ $80 (family)** | Buy | **FAMILY-ONLY** — accessory price band verified; the charger's own SKU page returned **HTTP 404** this session | One charger per robot is the minimum that lets both teams practise on the same night |
| Spare gamepad | REV Robotics | **`REV-31-2983`** USB PS4-compatible | 0 | **2 (shared pool)** | **$26.00 ea = $52** | Buy | **VERIFIED** — $26.00 | Gamepads die. Two in the pit kit covers both robots |
| Driver Hub battery (spare) | REV Robotics | **`REV-31-1876`** | 0 | 1 (shared) | **$21.75** | Buy | **VERIFIED** | A dead Driver Hub is a forfeited MATCH |
| **Odometry pack ⭐** | goBILDA | 4-Bar Odometry Pack **`3203-3110-0002`** (2 pods + 1 computer) | 1 | **2** | **$279.99 ea = $559.98** | Buy | **VERIFIED** — $279.99 | ✅ **Zero R503 cost — encoders are sensors, not actuators [C] R501/R503.** **[C] R303.J** names *"dead-wheel odometry kits"* as legal COTS |
| — component path | goBILDA | Pinpoint V2 **`3110-0002-0002`** $79.99 + 2× 4-Bar Pod **`3110-0001-0002`** $99.99 | 1 set | 2 sets | **$279.97 ea** | Buy | **VERIFIED** — all three, In Stock | Identical money to the pack. Buy the pack |
| Wiring / cable bundle | REV Robotics | FTC Cable Bundle **`REV-45-1901`** | 0–1 | **1–2** | **$220.00 ea** | Buy | **VERIFIED** — $220.00 | [J] One shared bundle is enough if the storefront Cable Pack came in both Electronics Kits |
| Sensor bundle (optional) | REV Robotics | FTC Sensor Bundle **`REV-45-1885`** | 0–1 | 1 (shared) | **$180.00** | Buy | **VERIFIED** — $180.00 | Buy **once**, split across both robots as the season reveals what it needs |
| External IMU (optional) | REV Robotics | 9-Axis IMU **`REV-31-3332`** | 0 | 0–1 | **$38.00** | Buy | **VERIFIED** — $38.00 | The Control Hub already has an internal IMU, and the Pinpoint has one. Buy only to diagnose a suspected Hub IMU fault |
| Structure / extrusion stock | goBILDA | **1120 Series U-Channel**, 1121 Low-Side, 1143 Mini Low-Side, 1122 Rail-Channel — [gobilda.com/u-channel/](https://www.gobilda.com/u-channel/) | as needed | as needed | **≈ $120–$180 per robot** | Buy | **FAMILY-ONLY** — families confirmed, **the category page prints no SKUs and no prices** | The Strafer kit is built on the 1120 pattern, so superstructure bolts straight on. **NEEDS-SKU-CHECK on every length before ordering** |
| Fastener / bearing / shaft allowance | goBILDA + REV | M3/M4 hardware, 1611-series bearings, 8 mm REX shaft, spacers | 1 lot | 2 lots | **≈ $90–$140 per robot** | Buy | **FAMILY-ONLY** | ⚠ Phase A recorded the goBILDA **M4 assortment out of stock**. Order early; **[C] R104** means you can over-build, and over-building consumes fasteners |

### 1.1a Platform subtotals

| Line | Per robot | **For 2 robots** |
|---|---|---|
| Strafer chassis kit | $699.99 | **$1,399.98** |
| Storefront Electronics Kit | $350 | **$700** |
| Storefront Driver Kit | $295 | **$590** |
| Odometry pack | $279.99 | **$559.98** |
| Batteries (2/robot + 1 program spare) | $120 | **$300** |
| Structure + hardware allowance (FAMILY-ONLY) | ≈$230 | **≈$460** |
| **PER-ROBOT PLATFORM SUBTOTAL** | **≈ $1,975** | **≈ $4,010** *(+$35/robot: storefront kits repriced to 2026-27 on 2026-08-22)* |
| **SHARED platform** (2 chargers ≈$80, 2 spare gamepads $52, Driver Hub battery $21.75, cable bundle $220, sensor bundle $180) | — | **≈ $554** |
| **PLATFORM TOTAL, TWO ROBOTS** | | ⭐ **≈ $4,564** |

> **[D] The number that should reframe every kickoff conversation: ≈ $4,560 is spent before a single game
> mechanism exists.** With the REV chassis instead of the Strafer it is **≈ $4,204**. Every §2 archetype total
> is *on top of this*.

## 1.2 The platform FABRICATE table

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (student-hours are **for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Control Hub / battery tray | in-house | 3D print, or cut 3 mm polycarbonate + hand drill | 1 | 2 | ≈$4 filament | **Fab** | **PHASE-B** (`ELECTRONICS-AND-SENSING.md` §E1.5) | **4.7 h both.** ⛔ **[C] R706** forbids replacing hub *enclosures*. Print **mounts**, never enclosures |
| Serviceability access panel | in-house | Design into the chassis plate | 1 | 2 | ≈$0 | Fab | **PHASE-B** | **1–2 h.** This is an **[C] R606** requirement, not a nicety |
| Diagnostic-LED sight window | in-house | Slot in a guard | 1 | 2 | ≈$0 | Fab | **PHASE-B** | **0.5 h. [C] R606.B** — FIELD STAFF cannot help you if they cannot see the lights |
| **ROBOT SIGNS ×2 per robot** | in-house | Sheet + template | **2** | **4** | ≈$6 | Fab | **PHASE-B** | **1.5 h. [C] R401** — *"Minimum of two ROBOT SIGNS per ROBOT… in at least 2 separate"* locations (grepped, V0 §12 line 399). 🕐 **Do this in August. It is the only inspection item you can finish before kickoff** |
| Wiring harness | in-house | Assembly, on a harness board | 1 | 2 | (in cable bundle) | Fab | **PHASE-B** | **8.0 h both** (2nd = 3.0 h; a harness board drops it to ~2.0 h). Ratio 0.60 — high, and legitimately so |
| Cable strain-relief anchors | in-house | 3D print + zip tie | 6–12 | 12–24 | ≈$3 | Fab | **PHASE-B** | **2 h both** |
| **Per-robot wiring diagram** | in-house | Draw, laminate, tape inside the pit toolbox | **1** | **2 — one per robot** | ≈$2 | Fab | **PHASE-B [J]** | **2 h.** [J] The single highest-value fabrication hour in this document |
| Drivetrain assembly | in-house | Assembly from the kit | 1 | 2 | — | Fab | **PHASE-B** | **≈ 20 h both** for the Strafer (`DRIVETRAIN-AND-ODOMETRY.md` §9.2). ✅ **Legal to build now — [C] R304** permits FABRICATED ITEMS created before Kickoff |
| OPERATOR CONSOLE box | in-house | Sheet/print + assembly | 1 | 2 | ≈$15 | Fab | **PHASE-B** | **5.5 h both.** R901–R903 are final — **build it in August** |
| **A chassis assembly fixture** | in-house | Plywood + printed locators | — | **1 (shared)** | ≈$10 | Fab | **PHASE-B [J]** | **3 h one-off.** 🕐 Two square, *identical* chassis. Pays for itself on robot B, every time |
| **Drill jigs** | in-house | Print or ply | — | 1–3 (shared) | ≈$5 | Fab | **PHASE-B [J]** | **1 h each.** Turns a 0.9-ratio hand-fitted part into a 0.4-ratio jigged one |

**Platform fabrication ≈ 45–50 student-hours for both robots**, of which ≈ 4 h is one-off jigs and fixtures.

## 1.3 The R503 actuator budget block — copy into every design proposal

**[C] R503*** (V0 §12, grepped line 591): *"ROBOTS are limited to a total of 8 motors and 8 servos… for all
MECHANISMS used in all configurations."*
⚠ **[H]→[C] This is a REDUCTION. DECODE allowed 10 servos; BIOBUZZ allows 8.** Any carried-over design, any
returning student's mental model, and any prior-season notebook may now be **illegal**. Re-check everything.

```
R503 ACTUATOR BUDGET — [design name], [A robot / B robot]
  Drivetrain          : ___ motors  ___ servos
  Intake              : ___ motors  ___ servos
  Transfer / indexer  : ___ motors  ___ servos
  Extension / arm     : ___ motors  ___ servos
  End effector        : ___ motors  ___ servos
  Endgame mechanism   : ___ motors  ___ servos
  ------------------------------------------------
  TOTAL               : ___ / 8     ___ / 8      <- MUST be <= 8 and <= 8
  Localization        :   0 motors    0 servos   (sensors are FREE — R501/R503)
  Spare slots left    : ___          ___         <- [J] target >= 2 motors
Checked against: R501 (Table 12-1), R502 (Table 12-2), R503 (8+8, all configurations)
```

**[J] The planning rule this file enforces everywhere: target 6 motors, never design to 8.** Every §2 rollup
below prints its motor/servo count, and any archetype that reaches 8/8 is flagged 🔴.

**Free against R503 [C]:** encoders, odometry pods, IMU, distance sensors, cameras, Limelight, gas springs,
constant-force springs, rubber bands, and — verbatim from **[C] R501** — motors integral to a COTS sensor and
motors inside a COTS computing device.

**Does NOT buy headroom:** the Servo Hub `REV-11-1855`, goBILDA Servo Power Injector `3125-0001-0001`,
SPARKmini `REV-31-1230` and Studica Servo Power Block `75005` are on **Table 12-3** and expand **ports and
power only**. They do not raise the cap of 8.

## 1.4 The shared-vs-duplicated split — the whole point of the exercise

**[D] Sort every line of a two-robot budget into one of four buckets. The buckets, not the total, are what a
two-team program can actually manage.**

| Bucket | Multiplier for robot B | Examples | [J] Strategy |
|---|---|---|---|
| **DOUBLED — COTS** | **× 2.00** | Control Hub, Driver Hub, chassis kit, every motor, every servo, slide kits, batteries | **Irreducible. There is no legal substitute and no way to share one between two robots that are both on a practice field.** Minimise the *count*, not the price |
| **DOUBLED — printed material** | × 2.00 material, **× 0.15–0.25 labour** | Rollers, jaws, brackets, hoods, trays | ⭐ **Push cost here.** A $1.40 bracket doubles to $2.80. This is the cheap half of the robot |
| **PAID ONCE — design** | **× 0.00** | CAD, geometry, fixtures, jigs, wiring-diagram template | ⭐ Freeze the design *before* building robot B, then both robots are the same design |
| **PAID ONCE — shared pool** | **× 1.00–1.20** | Spares kit, tooling, filament, chargers, sensor bundle, practice field | Explicitly a **program** asset. Budget it as one line, not two |

**[D] From `INTAKE-AND-MANIPULATION.md` §19.3, the duplication cost model:**

| Cost line | Robot A | Robot B | **Program total** |
|---|---|---|---|
| COTS parts | 100 % | **100 %** | **200 %** |
| Printed material | 100 % | 100 % | 200 % |
| **Design + CAD** | 100 % | **0 %** | **100 %** |
| Fabrication labour | 100 % | **15–25 %** printed / **70–100 %** hand-fitted | 115–200 % |
| Tuning + integration | 100 % | **40–50 %** | 140–150 % |
| **Software** | 100 % | **~5 %** (config file only) | **~105 %** |
| Spares | — | shared pool | ~120 % of one robot's |

> **[D] The two lines to stare at: COTS is 200 % and design is 100 %.**
> **[J] Therefore: push cost into design and printing (paid once, or nearly) and out of purchased components
> (paid twice).** Every archetype verdict in §2 is a restatement of that sentence.

## 1.5 The shared spares and tooling pool — one pool, not two kits

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Spare drive motor | goBILDA | 5203 Series Yellow Jacket, e.g. **`5203-2402-0019`** 312 RPM | 0 | **1 (shared)** | **$54.99** | Buy | **VERIFIED** — $54.99; 5202/5203 $54.99, 5204 $56.99 | One SKU covers all four drive positions on the Strafer. That single-SKU property is why the Strafer is recommended |
| Spare servo | goBILDA | 2000 Series Dual Mode **`2000-0025-0002`** (Torque) | 0 | **1–2 (shared)** | **$36.99 ea** | Buy | **VERIFIED** — $36.99 | ⚠ Phase B calls a stripped servo *"the most likely competition-day failure."* Speed `-0003` and Super-Speed `-0004` are the same price |
| Compliant wheels, alt. durometer | REV Robotics | **`REV-41-2034-PK4`** 40A / **`REV-41-2035-PK4`** 30A, 2 in, 5 mm hex, 4-pack | 0 | 1 pack ea | **$19.50 ea** | Buy | **VERIFIED** — both $19.50, **In Stock** | **Durometer is the cheapest tuning knob you own.** Buy both packs |
| Intake rollers | goBILDA | **`3618-4008-0016`** 16 mm OD 30A, 8-pack | 0 | 1 pack | **$12.99** | Buy | **VERIFIED** — $12.99 | Also `3618-4008-0012` (12 mm) same price |
| Polycarbonate sheet | REV Robotics | `REV-41-3049-PK5` | 0 | 1 pack | **$11.00** | Buy | **PHASE-B** | Guards, funnels and plows get bent |
| Bearings, shafts, belts, chain links, tubing, hardware | goBILDA | 1611-series bearings, 2106 shafts, 3405 round belts, 3308 chain links | — | assorted | **≈ $70** | Buy | **PHASE-B** (`INTAKE-AND-MANIPULATION.md` §19.4) | |
| **Printed spares — 2 of every critical printed part** | in-house | 3D print from the **frozen** files | — | 2 sets | **≈ $15 filament** | **Fab** | **PHASE-B [J]** | ⭐ **The most important row in this table, and it costs $15.** Print them the week you freeze the design, not the night before the qualifier |
| Tooling — hex drivers, taps, chain tool, spring scale, servo programmer, calipers | mixed | see `IN-HOUSE-FABRICATION.md` §6 tool tiers | — | 1 set (shared) | **≈ $200–$400** | Buy | **PHASE-B** | A **program** asset, not a robot asset |
| Filament | mixed | PLA/PETG + a TPU spool | — | shared | **≈ $80–$120/season** | Buy | **[J] FAMILY-ONLY** | Budget **2 kg per robot per season** for a mechanism-heavy archetype |

**[D] SHARED POOL TOTAL ≈ $500–$750 for the program** (spares ≈ $250–$290 per Phase B, plus tooling and
filament). **This is the line most often missing from a first-draft FTC budget, and it is the line that
decides whether a failure on Saturday morning is a five-minute swap or a lost season.**

---

# 2. THE ARCHETYPE BOMs

**Every §2 subsection prices only the MARGINAL cost of that archetype's game mechanisms.** Add §1's
**≈ $4,494 two-robot platform** and **≈ 45–50 h platform fabrication** to every total. Each subsection ends
with that addition made explicit.

Archetype numbering matches `reference/ROBOT-ARCHETYPE-LIBRARY.md` §3.

---

## 2.1 The ground-intake cycler

> **Library:** §3.1 · **Fit [D] 3.63** · Scoring ceiling **5** · Duplicability **4**
> **Identity:** acquire off the floor while moving, deliver, repeat. Its whole identity is **cycle time**.
> [H] The dominant FTC archetype of the last seven seasons.

### 2.1.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | Approach an element from any angle and stop where the driver wants. **Speed matters more than torque** | 4 | 0 | §1 platform |
| M2 | **Intake** | Accept the element at **any approach angle** without jamming; reverse to clear. Compress ~15–25 % on the element | **1** | 0–2 | 🕐 element size |
| M3 | **Transfer** | Move the element from the intake to the delivery point, single-file, without double-feeding | 0–1 | 1 | 🕐 element size |
| M4 | **Delivery** | Release into the scoring location, from wherever the game puts it | 0–1 | 1 | 🕐 goal height, **R105 EXPANSION-GATED** |
| M5 | **Endgame** | None in the base archetype. See §2.5 if the season pays for a climb | 0 | 0 | 🕐 kickoff |
| M6 | **Electronics** | §1 platform, unchanged | 0 | 0 | — |
| M7 | **Structure** | Hold the intake at a fixed height off the tile and survive being driven into a wall | 0 | 0 | — |

### 2.1.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Intake motor | goBILDA | **5203 Series Yellow Jacket**, 8 mm REX — ratio chosen at kickoff. Verified example **`5203-2402-0019`** (312 RPM) | 1 | **2** | **$54.99 ea = $109.98** | Buy | **VERIFIED** — 5202/5203 **$54.99**, 5204 **$56.99** | 🕐 **The ratio is the one intake decision you cannot make before kickoff.** Same physical SKU family whatever you pick — so the *mount* can be designed in August |
| Intake wheels — soft | REV Robotics | **`REV-41-2035-PK4`** 2 in, 5 mm hex, **30A soft**, 4-pack | 1 pack | **2 packs** | **$19.50 ea = $39.00** | Buy | **VERIFIED** — $19.50, **In Stock** | 30A grabs; 40A (`REV-41-2034-PK4`) lasts. [J] Buy one of each and let the element decide |
| Intake rollers | goBILDA | **`3618-4008-0016`** 16 mm OD, 30A, 8-pack (also `3618-4008-0012`, 12 mm) | 1 pack | **2 packs** | **$12.99 ea = $25.98** | Buy | **VERIFIED** — $12.99 | For a compact over-the-bumper roller. `3615-` Boot-Wheels ($4.99/$6.99/$8.99) and `3613-` Gecko wheels ($6.99–$9.99) are the larger-element alternatives, all **VERIFIED** |
| Intake deploy servo | goBILDA | 2000 Series Dual Mode **`2000-0025-0002`** (Torque) | 1 | **2** | **$36.99 ea = $73.98** | Buy | **VERIFIED** — $36.99 | Only if the intake must fold to meet **[C] R102**'s 18-in cube. A sprung passive deploy costs **0 servos** — prefer it |
| Transfer / gate servo | goBILDA | **`2000-0025-0003`** (Speed) | 1 | **2** | **$36.99 ea = $73.98** | Buy | **VERIFIED** — $36.99 | Speed variant: a gate wants travel time, not torque |
| Delivery slide (competitive only) | goBILDA | 2-Stage Viper-Slide Kit, belt-driven, 336 mm — **`3210-0003-0002`**; 384 mm retracted → 874 mm extended | 0–1 | 0–2 | **$159.99 ea** | Buy | **VERIFIED** — $159.99, **In Stock**, 490 mm stroke | ✅ **[C] R303.A** names *"linear slide kit"* as legal single-DoF COTS. 🕐 **R105 EXPANSION-GATED** — do not buy the stage count until kickoff |
| Delivery motor (competitive only) | goBILDA | 5203 Series Yellow Jacket, low-RPM/high-torque ratio | 0–1 | 0–2 | **$54.99 ea** | Buy | **VERIFIED** — $54.99 | |
| Shaft, bearing, belt, hardware allowance | goBILDA | 1611 bearings · 2106 8 mm REX shaft · 3405 round belts · M3/M4 | 1 lot | 2 lots | **≈ $45–$70 per robot** | Buy | **FAMILY-ONLY** | ⚠ The row teams forget. ≈20 % of the mechanism's COTS cost |

### 2.1.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**student-hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Intake side plates + roller hubs | in-house | 3D print (PLA/PETG), **slotted axle holes** | 2 | 4 | ≈$4 | **Fab** | **PHASE-B** | **≈ 6 h.** [J] Slots are how a program without a CNC mill gets repeatability — a rookie can assemble robot B and it still works |
| Full-width TPU roller (alt.) | in-house | 3D print, TPU | 0–1 | 0–2 | ≈$6 | Fab | **PHASE-B** | **6 h both.** TPU is slow to *print*, not slow to *design* |
| Sprung intake pivot | in-house | Print + COTS spring or rubber band | 1 | 2 | ≈$5 | Fab | **PHASE-B [J]** | **4 h.** ⭐ **Costs 0 servos against [C] R503 and 0 motors.** Prefer over a powered deploy wherever geometry allows |
| Transfer chute / path plate | in-house | Print, or bent polycarbonate | 1 | 2 | ≈$4 | Fab | **PHASE-B** | **8.5 h** if printed large; less if bent PC |
| Delivery bucket / dump box | in-house | Bent polycarbonate + printed corners | 1 | 2 | ≈$8 | Fab | **PHASE-B** | **4.2 h.** Bend jig makes or breaks this |
| Bumper / edge guard set | in-house | Sheet + TPU | 1 | 2 | ≈$8 | Fab | **PHASE-B** | **3.7 h.** **[C] R104** — no weight limit, so armour is free |

### 2.1.4 R503 actuator budget

| Configuration | Drivetrain | Intake | Transfer | Delivery | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|---|---|
| **Cheap** | 4 M | 1 M | 0 M / 1 S | 0 M / 1 S | **5 / 8** | **2 / 8** | ⭐ **3 motors in reserve.** This is the small-team build |
| **Competitive** | 4 M | 1 M + 1 S | 0 M / 1 S | 1 M / 1 S | **6 / 8** | **3 / 8** | ✅ Meets the [J] "target 6, never design to 8" rule |

### 2.1.5 BOM SUMMARY — competitive version

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform — Strafer `3209-0001-0007` | $699.99 | $1,399.98 | Assembly only | 20 h |
| M2 Intake | 5203 motor · `REV-41-2035-PK4` · `3618-4008-0016` · deploy servo | ≈$170 | ≈$340 | Side plates, hubs, sprung pivot | 19 h |
| M3 Transfer | 1× `2000-0025-0003` servo + hardware | ≈$57 | ≈$114 | Chute / path plate | 10 h |
| M4 Delivery | `3210-0003-0002` + 5203 motor + belt/hardware | ≈$275 | ≈$550 | Carriage, bucket, hard stops | 22 h |
| M5 Endgame | none | $0 | $0 | — | 0 h |
| M6 Electronics | §1 platform (storefront Electronics + Driver Kit) | $610 | $1,220 | Tray, harness, signs | 25 h |
| M7 Structure | §1 allowance | ≈$230 | ≈$460 | Superstructure cuts, bumpers | 12 h |
| **MARGINAL (M2–M4)** | | **≈ $502** | **≈ $1,004** | | **51 h** |

### 2.1.6 Totals, with the shared/duplicated split made explicit

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$502 | **≈$1,004** | DOUBLED — COTS |
| Printed/sheet material | ≈$35 | ≈$70 | DOUBLED — material |
| Shared spares + tooling | — | ≈$500–$750 | PAID ONCE |
| **TOTAL** | **≈ $2,477** | ⭐ **≈ $6,068–$6,318** | |
| Fabrication + assembly hours | ≈ 68 h | **≈ 96 h** | Design 0 % on robot B |
| Software | ≈ 25 h | **≈ 26 h** | ~5 % on robot B (config file only) |

> **[D] Robot B costs ≈ $2,477 in parts but only ≈ 28 more fabrication hours.** That ratio — money doubling
> while labour grows by ~40 % — is the whole two-robot economic case, and it only holds if the design is
> **frozen and printed**, not hand-fitted.

### 2.1.7 Duplicability verdict — **4/5. The archetype to duplicate.**

**Why the second copy is cheap in hours:** the intake is the most copy-able mechanism in FTC. Print the same
rollers, the same side plates, the same axle spacing. Phase B measures a roller intake at **13–16 h first,
4–5 h second (ratio ≈ 0.30)**.

**Where the second copy hurts:** the *delivery* slide. Two Viper-Slide kits is $319.98, and rigging tension
must be set identically twice.

**[J] Three changes that make the second copy less painful:**
1. **Make the intake deploy passive.** A sprung pivot instead of a servo removes a servo, a wire, a config
   constant and a failure mode — **twice**.
2. **Buy both slide kits in the same order.** Same production run, same tolerances, one shipping charge.
3. **Build robot B's intake FIRST from the frozen file.** If the less-experienced half of the program cannot
   build it from the file, the file is not done — and you find that out while there is still time.

### 2.1.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Delivery | Servo-released dump box, fixed height | 2-stage Viper-Slide + motor, height presets | |
| Intake deploy | Sprung, passive | Servo-deployed, encoder-homed | |
| Marginal COTS / robot | **≈ $289** | **≈ $502** | |
| **2-robot marginal** | **≈ $578** | **≈ $1,004** | **+$426** |
| Student-hours (both) | ≈ 45–60 h | ≈ 85–100 h | **+40 h** |
| R503 | 5 M / 2 S | 6 M / 3 S | +1 M, +1 S |
| **What the money buys** | — | 🕐 **Access to scoring locations above the dump box's fixed height, and a repeatable preset instead of a driver eyeballing it.** [J] **If the game's high goal is worth < 2× the low goal, do not spend this $426** — see `ROBOT-ARCHETYPE-LIBRARY.md` §6.1.1, the #1 historical trap | |

---

## 2.2 The stacker / builder (vertical placement)

> **Library:** §3.2 · **Fit [D] 2.13** · Build complexity **5** · Duplicability **2** · Cost **5**
> **Identity:** place elements precisely at height. **The highest-BOM archetype in the library, and the one
> §6.1.1 names as the #1 trap.** Read the library's warning before costing this.

### 2.2.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | Stay stable under a raised load. Wide track, low battery, deliberately heavy | 4 | 0 | §1 platform |
| M2 | **Intake** | Acquire (as §2.1) or accept from the human player (as §2.9) | 0–1 | 0–1 | 🕐 element |
| M3 | **Vertical extension** | Lift the end effector to the scoring height and hold it there | **1–2** | 0 | 🔴 🕐 **R105 EXPANSION-GATED — the stage count is unknowable before kickoff** |
| M4 | **Wrist / pivot** | Keep the element level through the arc (virtual four-bar) | 0 | **2** | 🕐 |
| M5 | **End effector** | Grip and release one element, repeatably, with alignment forgiveness | 0 | **1–2** | 🕐 element |
| M6 | **Folding** | Collapse the whole stack into **[C] R102**'s 18 in. cube, stationary and self-supported | 0 | 0 | **[C] R102/R103 — final now** |
| M7 | **Structure** | Resist the tipping moment of a mass at height | 0 | 0 | — |

> ⚠ **[C] R102 is the tax that defines this archetype.** *"all parts of the ROBOT must be fully stationary,
> and the ROBOT must be fully self-contained within an 18 in… volume"* (V0 §12, line 169). **[C] R103** permits
> holding the fold mechanically or with an init OpMode — but warns against motors *"stalled against a hard
> stop"* for minutes. **[J] Use a mechanical latch or a spring detent, not a stalled motor.**

### 2.2.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Linear slide kit ⭐** | goBILDA | **`3210-0003-0002`** 2-Stage Viper-Slide, belt-driven, 336 mm — 384 mm retracted, **874 mm extended, 490 mm stroke** | 1 | **2** | **$159.99 ea = $319.98** | Buy | **VERIFIED** — $159.99, **In Stock**; includes steel slides, GT2 2 mm belt parts, `1201-0043-0005` quad-block mount, 8 mm REX Sonic hub. **Motor sold separately** | ✅ **[C] R303.A.** ⭐ **Buy the kit, not the parts — it is a *guarantee* that robot A and robot B have identical geometry**, which is what makes one codebase and one spares set work for both |
| Linear slide kit — taller | goBILDA | **`3210-0003-0004`** 4-Stage, 336 mm slides · or **`3210-0004-0004`** 4-Stage, 240 mm slides | 0–1 | 0–2 | **$229.99 / $219.99 ea** | Buy | **VERIFIED** — both prices | 🕐 **EXPANSION-GATED.** **[J] Do not buy a 4-stage kit before kickoff.** +$140 across two robots for reach R105 may not let you use |
| Lift motor(s) | goBILDA | 5203 Series Yellow Jacket, **low-RPM / high-torque** ratio | **1–2** | **2–4** | **$54.99 ea** | Buy | **VERIFIED** — $54.99 | ⭐ **[J] One motor + a cross-shaft beats two motors**: saves a motor slot, $109.98 across two robots, and the entire class of "the two sides fought each other" failures |
| Wrist servos (virtual four-bar) | goBILDA | **`2000-0025-0002`** (Torque) ×2 | 2 | **4** | **$36.99 ea = $147.96** | Buy | **VERIFIED** — $36.99 | ⚠ **[C] R502** caps servos at **8 W mechanical @6 V**. A VFB is exactly where teams reach for an illegal oversized servo. Check the power formula in `LEGAL-PARTS-CONSTRAINTS.md` before substituting |
| Higher-torque servo (if the VFB stalls) | goBILDA | Axon MAX Servo MK2 **`2004-0025-0002`** | 0–2 | 0–4 | **$99.99 ea** | Buy | **VERIFIED** — $99.99, **In stock** (MINI `2004-0025-0001` **out of stock** 2026-08-22) | ⚠ **Must be checked against [C] R502's 8 W cap and Table 12-2's allowed-servo list before purchase. NEEDS-RULE-CHECK, not just SKU-check** |
| Gripper servo | goBILDA | **`2000-0025-0003`** (Speed) | 1–2 | **2–4** | **$36.99 ea** | Buy | **VERIFIED** — $36.99 | **[C] R303.G** permits a *"single DoF gripper"* as COTS. A printed jaw pair on one servo is cheaper and duplicates better |
| Slide spares | goBILDA | Steel Viper-Slide **`2500-0014-0336`** $19.99 / **`2500-0010-0240`** $16.99 · end-stops **`2501-0001-0001`** 6-pk $5.99 · pulley brackets **`2501-0001-0002`** 4-pk $8.99 | — | shared | **≈ $35** | Buy | **VERIFIED** — all four | A bent slide segment is repairable for $19.99 instead of $159.99 |
| Belt, pulley, spool, cord, hardware | goBILDA / REV | GT2 timing belt & pulley · UHMWPE cord **`REV-41-1162`** (1.2 mm × 10 m, 300 lb, $7.75) / **`REV-29-1244`** (3 mm, 1500 lb, $13.50) | 1 lot | 2 lots | **≈ $80 per robot** | Buy | **PHASE-B** (`EXTENSION-ARMS-LIFTS.md` §7.4.1) | ⚠ **`3210-0002-0002` (cable-driven 2-stage kit) is DISCONTINUED / SOLD OUT.** Do not spec it. Prior-season "buy the cable kit" advice is now invalid |
| Assist springs | goBILDA | 2915 / 2916 spring families, constant-force springs | 2 | 4 | **≈ $27** | Buy | **PHASE-B** | ⭐ **Zero R503 cost.** **[C] R801** permits springs; only *pre-charged sealed COTS closed-air* systems (gas shocks) are the air exception. **No pneumatic cylinders, ever** |
| Intake (if fitted) | — | as §2.1.2 | 1 set | 2 sets | **≈ $170** | Buy | see §2.1 | |

### 2.2.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Slide mounting brackets + hard stops | in-house | 3D print + hand-drilled plate | 4 | 8 | ≈$6 | **Fab** | **PHASE-B** | **≈ 7 h.** Hard stops are what stop a runaway lift from destroying a $159.99 kit |
| VFB pulley plates + belt tensioner | in-house | 3D print | 2 | 4 | ≈$5 | Fab | **PHASE-B** | **≈ 8 h.** Ratio ≈0.15 — a genuinely duplicable subsystem |
| Gripper jaw pair (rigid + TPU pads) | in-house | 3D print, 2 materials | 1 pair | 2 pairs | ≈$6 | Fab | **PHASE-B** | **5.8 h. Expect 3+ revisions — that IS the design.** ⚠ A *hand-fitted* linkage gripper is 22–28 h first, 7–8 h second |
| **Fold / latch mechanism** | in-house | Print + spring detent + hand fitting | 1 | 2 | ≈$8 | Fab | **PHASE-B [J]** | **≈ 12 h. 🔴 The hand-fitted part with no duplication discount.** It is the single biggest reason this archetype scores Duplicability 2 |
| Anti-tip ballast / wide stance | in-house | Steel plate low in the chassis | 1 | 2 | ≈$15 | Fab | **[J]** | **≈ 3 h.** ⭐ **[C] R104 — there is no weight limit in BIOBUZZ.** Ballast is the cheapest anti-tip fix in the game and costs zero motor slots |
| Slide guards | in-house | Bent polycarbonate | 2 | 4 | ≈$6 | Fab | **PHASE-B** | **≈ 4 h.** Keeps a SCORING ELEMENT out of the belt path |

### 2.2.4 R503 actuator budget

| Configuration | Drive | Intake | Lift | Wrist | Gripper | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Cheap** (2-stage, 1 lift motor, single pivot, 1-servo claw) | 4 M | 1 M | **1 M** | 1 S | 1 S | **6 / 8** | **2 / 8** | ✅ Fits the [J] rule with 2 motors spare |
| **Competitive** (4-stage, 2 lift motors, VFB, 2-servo gripper) | 4 M | 1 M + 1 S | **2 M** | 2 S | 2 S | 🔴 **7 / 8** | **5 / 8** | 🔴 **One motor from the cap.** No endgame mechanism is possible without dropping something |

> **[D] This is the archetype that eats the actuator budget.** In the competitive column, adding a climb
> (§2.5) puts you at **8/8 with zero reserve** — the classic over-committed build the library warns about.

### 2.2.5 BOM SUMMARY — competitive version

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain + ballast | §1 platform + steel ballast | $699.99 | $1,399.98 | Assembly, ballast | 23 h |
| M2 Intake | as §2.1 | ≈$170 | ≈$340 | Side plates, rollers | 19 h |
| M3 Vertical extension | `3210-0003-0004` + 2× 5203 + belt/cord/springs | ≈$420 | ≈$840 | Brackets, hard stops, guards | 25 h |
| M4 Wrist (VFB) | 2× `2000-0025-0002` + pulleys | ≈$188 | ≈$376 | Pulley plates, tensioner | 12 h |
| M5 End effector | 2× `2000-0025-0003` | ≈$110 | ≈$220 | Jaw pair + TPU pads | 14 h |
| M6 Folding | springs, latch hardware | ≈$25 | ≈$50 | 🔴 Fold/latch — hand-fitted | 12 h |
| M7 Electronics + structure | §1 platform | ≈$840 | ≈$1,680 | Tray, harness, signs, superstructure | 37 h |
| **MARGINAL (M2–M6)** | | **≈ $913** | **≈ $1,826** | | **82 h** |

### 2.2.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$913 | **≈$1,826** | DOUBLED — COTS |
| Printed/sheet material | ≈$46 | ≈$92 | DOUBLED — material |
| Shared spares + slide spares + tooling | — | ≈$550–$800 | PAID ONCE |
| **TOTAL** | **≈ $2,899** | 🔴 **≈ $6,962–$7,212** | |
| Fabrication + assembly hours | ≈ 88 h | **≈ 127 h** | |
| Software | ≈ 40 h | **≈ 42 h** | Position presets, anti-tip interlocks |

### 2.2.7 Duplicability verdict — **2/5. The second copy is a second project.**

**The honest sentence:** *two full slide assemblies is real money and real hours, and the fold mechanism does
not duplicate at all.* The kit parts copy perfectly (duplicability 5 on the Viper-Slide row of
`EXTENSION-ARMS-LIFTS.md` §10.1) — but the fold-to-18-inches solution is hand-fitted to each chassis, and
hand-fitting carries a **0.9–1.0 duplication ratio: no discount whatsoever**.

**[J] Four changes that make the second copy less painful:**
1. **One lift motor with a cross-shaft, not two.** Saves $109.98, one motor slot, and the entire class of
   "the two sides fought each other" failures — on both robots.
2. **Design the fold as a printed detent, not a fitted latch.** Moving that part from hand-fitting (ratio 1.0)
   to printing (ratio 0.2) saves ≈ **10 student-hours on robot B alone**.
3. **Buy both slide kits in one order** — `EXTENSION-ARMS-LIFTS.md` §10.2, rule 2.
4. **If robot B must be simpler, make it the *cheap version of the same design*, never a different design.**
   Two lift designs means two spare kits, two code paths, and half the students understanding each.

**[J] The blunt recommendation for this program: this is an A-team-only archetype.** A B team that commits to
a tall lift will spend the season debugging it. See `ROBOT-ARCHETYPE-LIBRARY.md` §3.2 and §6.1.1.

### 2.2.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Slides | 2-stage `3210-0003-0002` | 4-stage `3210-0003-0004` | |
| Lift | 1 motor + cross-shaft | 2 motors | |
| Wrist | Single servo pivot | Virtual four-bar, 2 servos | |
| Gripper | 1-servo printed claw | 2-servo gripper with TPU pads | |
| Marginal COTS / robot | **≈ $519** | **≈ $913** | |
| **2-robot marginal** | **≈ $1,038** | **≈ $1,826** | **+$788** |
| Student-hours (both) | ≈ 65–85 h | ≈ 120–140 h | **+50 h** |
| R503 | 6 M / 2 S | 🔴 7 M / 5 S | +1 M, +3 S |
| **What the money buys** | — | 🕐 **Extra reach (R105-gated), a level element through the arc, and a grip that tolerates ±4 mm of driver error.** [J] The VFB is the part that actually pays: a wrist that keeps the element level converts near-misses into scores. The 4th slide stage may buy nothing at all if R105 forbids the extension | |

---

## 2.3 The launcher / shooter

> **Library:** §3.3 · **Fit [D] 2.63** · Tuning load **5** (the worst in the library) · Duplicability **3**
> **Identity:** propel an element to a distant goal. **[C] R801** explicitly keeps this legal:
> *"High-speed flywheels or rollers used for manipulating SCORING ELEMENTS would not on their own be
> considered a high-speed airflow device."* Pneumatic launchers are **illegal** (V0 §12, line 1119).

### 2.3.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | **Stop precisely and repeatably** — matters more than being fast | 4 | 0 | §1 platform |
| M2 | **Intake** | Same roller intake as §2.1 — *a launcher is a cycler with a different delivery* | 1 | 0–1 | 🕐 element |
| M3 | **Magazine / feed** | Present **exactly one** element to the wheel, at a controlled rate, without double-feeding | 0–1 | 1 | 🔴 🕐 **"the feed eats the season"** |
| M4 | **Launcher** | Impart repeatable exit velocity. Must be **velocity-controlled**, not duty-cycle-controlled | **1–2** | 0 | 🕐 goal distance/height |
| M5 | **Aiming** | Fixed geometry (drive to a spot), adjustable hood servo, or a turret | 0–1 | 0–1 | 🕐 goal geometry |
| M6 | **Structure** | Hold the launcher rigid. **Any flex is a miss** | 0 | 0 | — |

### 2.3.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Flywheel mass | goBILDA | **`3628-0032-0082`** 82 mm, 152 g, 1651 g·cm² · or **`3628-0014-0060`** 60 mm, 115 g, 551 g·cm² | 1–2 | **2–4** | **$15.99 / $12.99 ea** | Buy | **VERIFIED** — both | ⭐ **Rotational inertia is what makes shot #2 match shot #1.** The 82 mm has **3× the inertia** of the 60 mm for $3 more. Buy the 82 mm |
| Launcher motor | goBILDA | 5203 Series Yellow Jacket, **high-RPM** ratio | **1** | **2** | **$54.99 ea = $109.98** | Buy | **VERIFIED** — $54.99 | 🕐 Ratio set by required exit velocity — computable only after kickoff. `LAUNCHERS-AND-FEEDING.md` §2 has the arithmetic |
| Launch wheel (compliant) | REV Robotics | **`REV-41-2034-PK4`** 40A medium, 2 in, 4-pack | 1 pack | **2 packs** | **$19.50 ea = $39.00** | Buy | **VERIFIED** — $19.50, In Stock | 40A for a launcher, 30A for an intake. Durometer is the primary tuning knob |
| Feed / kicker servo | goBILDA | **`2000-0025-0004`** (Super Speed) | 1 | **2** | **$36.99 ea = $73.98** | Buy | **VERIFIED** — $36.99 | Super Speed: a kicker's job is to clear the path fast |
| Indexer motor (competitive only) | goBILDA | 5203 Series Yellow Jacket | 0–1 | 0–2 | **$54.99 ea** | Buy | **VERIFIED** — $54.99 | ⭐ **[J] A serpentine magazine costs 0 motors.** Try that first |
| Hood adjust servo (optional) | goBILDA | **`2000-0025-0002`** (Torque) | 0–1 | 0–2 | **$36.99 ea** | Buy | **VERIFIED** — $36.99 | 🕐 Only if the game has more than one shooting distance |
| **Vision (competitive)** | Limelight Vision | **Limelight 3A** | 0–1 | **0–2** | **$189.00 ea = $378.00** | Buy | **VERIFIED** price $189.00; **stock status not stated on the page** | ⚠ **[C] R702** — coprocessor software may not be altered *except* programmable vision coprocessors natively supported by the FTC SDK, **listed in Table 12-9. ✅ CONFIRMED 2026-08-22: Table 12-9 contains exactly one row — "Limelight Vision Limelight 3A / LL_3A" — so the 3A is legal and reprogrammable. ⛔ The 3G is prohibited (R702 Example 6).** The storefront Driver Kit webcam costs **$0 extra** and is the honest first answer |
| Bearings, shaft, belt, hardware | goBILDA | 1611 bearings · 8 mm REX shaft · GT2 belt | 1 lot | 2 lots | **≈ $50 per robot** | Buy | **FAMILY-ONLY** | |
| Intake | — | as §2.1.2 | 1 set | 2 sets | **≈ $170** | Buy | see §2.1 | |

### 2.3.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| **Hood / exit channel** | in-house | 3D print (large) or bent polycarbonate | 1 | 2 | ≈$8 | **Fab** | **PHASE-B** | **8.5 h.** ⭐ **The single highest-iteration part in this archetype. Print it in cheap PLA and expect 4+ revisions** |
| Flywheel shroud + rigid mount | in-house | Print + hand-drilled plate | 1 | 2 | ≈$6 | Fab | **PHASE-B** | **≈ 7 h. Any flex here is a miss.** Over-build it — **[C] R104**, no weight limit |
| Serpentine magazine | in-house | Bent polycarbonate + printed guides | 1 | 2 | ≈$8 | Fab | **PHASE-B [J]** | **≈ 10 h.** ⭐ **Costs 0 motors and 0 servos.** Prefer over a powered indexer |
| Kicker paddle | in-house | 3D print | 1 | 2 (+2 spare) | ≈$3 | Fab | **PHASE-B** | **≈ 4 h.** Print spares — paddles are consumables |
| Anti-double-feed gate | in-house | Print + spring | 1 | 2 | ≈$3 | Fab | **PHASE-B** | **≈ 6 h.** 🔴 This is where the season is actually lost |
| Camera / Limelight mount | in-house | 3D print, **locked focus, known pose** | 0–1 | 0–2 | ≈$3 | Fab | **PHASE-B** | **2.3 h.** Angle matters; expect 2 revisions |

### 2.3.4 R503 actuator budget

| Configuration | Drive | Intake | Feed | Launcher | Aim | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Cheap** (single flywheel, serpentine, fixed aim) | 4 M | 1 M | 0 M / 1 S | **1 M** | 0 | **6 / 8** | **1 / 8** | ⭐ Excellent. 2 motors and 7 servos in reserve |
| **Competitive** (single flywheel, hopper + indexer, kicker, fixed aim) | 4 M | 1 M | **1 M** / 1 S | 1 M | 0 | 🔴 **7 / 8** | **2 / 8** | 🔴 At the practical ceiling |
| 🔴 **Maximum** (dual flywheel, hopper, indexer, hood, turret) | 4 M | 1 M | 1 M / 1 S | **2 M** | 1 M / 1 S | ⛔ **9 / 8** | 3 / 8 | ⛔ **ILLEGAL under [C] R503.** Not a menu option — it is what a design drifts into if nobody keeps the budget block |

> **[D] Worth stating plainly: the "obvious" full-featured launcher build is over the motor cap.** The dual
> flywheel and the turret are the two features to cut, in that order.

### 2.3.5 BOM SUMMARY — competitive version

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform | $699.99 | $1,399.98 | Assembly | 20 h |
| M2 Intake | as §2.1 | ≈$170 | ≈$340 | Side plates, rollers | 19 h |
| M3 Magazine / feed | indexer motor + kicker servo | ≈$115 | ≈$230 | Serpentine, gate, paddle | 26 h |
| M4 Launcher | `3628-0032-0082` + 5203 + `REV-41-2034-PK4` | ≈$100 | ≈$200 | Hood, shroud, rigid mount | 24 h |
| M5 Aiming | fixed geometry — $0 | $0 | $0 | Alignment marks | 3 h |
| M6 Electronics + structure | §1 platform | ≈$840 | ≈$1,680 | Tray, harness, signs | 37 h |
| **MARGINAL (M2–M5)** | | **≈ $407** | **≈ $814** | | **72 h** |

### 2.3.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$407 | **≈$814** | DOUBLED — COTS |
| Printed/sheet material | ≈$28 | ≈$56 | DOUBLED — material |
| Shared spares + tooling (incl. launcher spares ≈$232) | — | ≈$700–$950 | PAID ONCE |
| **TOTAL (no vision)** | **≈ $2,375** | **≈ $6,064–$6,314** | |
| **+ 2× Limelight 3A** | +$189 | **+$378** | DOUBLED — COTS |
| Fabrication + assembly hours | ≈ 85 h | **≈ 117 h** | |
| **Software + TUNING** | ≈ 45 h | 🔴 **≈ 75 h** | 🔴 **The exception to the ~5 % software rule — see §2.3.7** |

### 2.3.7 Duplicability verdict — **3/5. The geometry copies. The tuning does not.**

**This is the archetype where the standard duplication model breaks.** Everywhere else in this file, software
duplicates at ~5 %. Here it does not:

> **Two nominally identical flywheels need two separate velocity tables.** Wheel durometer varies batch to
> batch, bearing preload varies with assembly, and the hood's printed surface finish varies between machines.
> Phase B measures this as **≈ 30 extra student-hours on robot B** that no other archetype pays.

**[J] Four changes that make the second copy less painful:**
1. **Add flywheel mass.** `3628-0032-0082` at $15.99 has 3× the inertia of the 60 mm. **More inertia means
   less sensitivity to every one of the variations above** — a $3 fix for a 30-hour problem.
2. **Print both hoods in the same batch, from the same spool, on the same machine.** Free. Eliminates a whole
   class of "why does robot B shoot short?"
3. **Fixed aiming geometry, and drive to a spot.** A turret is duplicability **2** in
   `EXTENSION-ARMS-LIFTS.md` §10.1 — a hand-fabricated precision race, twice, with no mill.
4. **One codebase, two constants files.** Velocity tables live in the per-robot constants file. **Never fork
   the code.**

**[J] Blunt assessment (agreeing with `LAUNCHERS-AND-FEEDING.md` §14): a launcher is a defensible A-team
choice in a season that clearly pays for it, and a poor B-team choice in any season.** The build is cheap; the
*tuning* is the most expensive thing in this document per point scored.

### 2.3.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Feed | Serpentine magazine, gravity-fed | Hopper + powered indexer + kicker | |
| Flywheel | 60 mm `3628-0014-0060` | 82 mm `3628-0032-0082` + added steel mass | |
| Aiming | Fixed, alignment tape on the tile | Fixed + webcam pose correction | |
| Marginal COTS / robot | **≈ $182** | **≈ $407** | |
| **2-robot marginal** | **≈ $364** | **≈ $814** | **+$450** |
| Student-hours (both) | ≈ 45–75 h | ≈ 85–140 h | **+50 h** |
| R503 | 6 M / 1 S | 🔴 7 M / 2 S | +1 M, +1 S |
| **What the money buys** | — | **A higher sustained fire rate and a tighter shot group.** [J] The hopper + indexer turns "shoot 3, reload from the human player" into a continuous cycle. **The 82 mm flywheel is the single best $3 in this entire document** | |
| **+ Limelight 3A ×2** | — | **+$378** | 🕐 Automatic goal alignment — **only if Table 12-9 lists it (R702) and only if the game has a vision target.** ⚠ The Driver Kit webcam you already own does this for $0 |

---

## 2.4 The ramp / deposit bot (low-goal dumper)

> **Library:** §3.4 · **Fit [D] 4.25** · Duplicability **5** · Reliability **5** · Programming load **1**
> **Identity:** intake into a hopper, drive to the low goal, dump. **Zero vertical extension.**
> **[J] The best B-team project in the library, and every team's week-2 fallback.**

### 2.4.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | Get to the deposit point and back. Nothing exotic | 4 (or 2) | 0 | §1 platform |
| M2 | **Intake** | Same roller intake as §2.1, shared CAD | 1 | 0–1 | 🕐 element |
| M3 | **Hopper / bed** | Hold several elements without them escaping over a bump or a turn | 0 | 0 | 🕐 element count |
| M4 | **Release** | Open a gate, tip a bucket, or simply reverse the intake | 0–1 | 1 | 🕐 goal geometry |
| M5 | **Endgame** | None | 0 | 0 | — |
| M6 | **Electronics / structure** | §1 platform | 0 | 0 | — |

> ⭐ **[J] The cheapest legal release mechanism is "reverse the intake." It costs $0, 0 motors and 0 servos.**
> Cost it as the baseline and make anything fancier justify itself.

### 2.4.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Intake (whole subsystem) | goBILDA / REV | as §2.1.2 — 5203 motor + `REV-41-2035-PK4` + `3618-4008-0016` | 1 set | **2 sets** | **≈ $170 per robot** | Buy | **VERIFIED** components | Shared CAD with §2.1. **This is the same mechanism** — build it once, use it in both archetypes |
| Gate / dump servo | goBILDA | **`2000-0025-0003`** (Speed) | 0–1 | 0–2 | **$36.99 ea** | Buy | **VERIFIED** — $36.99 | ⭐ Or **zero** if the release is "reverse the intake" |
| Tipping-bucket motor (competitive) | goBILDA | 5203 Series Yellow Jacket, high-torque ratio | 0–1 | 0–2 | **$54.99 ea** | Buy | **VERIFIED** — $54.99 | Only if the deposit height needs the bed to lift, not just open |
| Polycarbonate sheet | REV Robotics | `REV-41-3049-PK5` | 1 pack | 2 packs | **$11.00 ea** | Buy | **PHASE-B** | Hopper walls. Bends with a heat gun and a wooden jig |
| Hardware allowance | goBILDA | hinges, M3/M4, bearings | 1 lot | 2 lots | **≈ $30** | Buy | **FAMILY-ONLY** | |

### 2.4.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Hopper walls | in-house | Bent polycarbonate + printed corners, on a **bend jig** | 1 set | 2 sets | ≈$10 | **Fab** | **PHASE-B** | **4.2 h.** ⭐ Ratio drops from 0.40 to ~0.25 once the bend jig exists — **build the jig** |
| Release gate + linkage | in-house | 3D print | 1 | 2 | ≈$4 | Fab | **PHASE-B** | **≈ 5 h** |
| Intake side plates / rollers | in-house | 3D print | 2 | 4 | ≈$6 | Fab | **PHASE-B** | **≈ 6 h.** Identical files to §2.1 |
| Element-retention lip | in-house | Print + silicone tubing `2928-0508-0002` | 1 | 2 | ≈$6 | Fab | **PHASE-B** | **≈ 3 h.** Stops elements bouncing out on a hard turn |

### 2.4.4 R503 actuator budget

| Configuration | Drive | Intake | Release | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|---|
| **Cheap** (reverse-the-intake release) | 4 M | 1 M | 0 | ⭐ **5 / 8** | ⭐ **0 / 8** | ⭐ **The most reserve-rich real scoring robot in this file.** 3 motors and 8 servos free |
| **Cheap, 2-motor tank drive** | 2 M | 1 M | 0 | ⭐ **3 / 8** | **0 / 8** | ⭐⭐ 5 motors in reserve |
| **Competitive** (tipping bucket + gate) | 4 M | 1 M + 1 S | 1 M / 1 S | **6 / 8** | **2 / 8** | ✅ Still comfortable |

### 2.4.5 BOM SUMMARY — competitive version

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform | $699.99 | $1,399.98 | Assembly | 20 h |
| M2 Intake | 5203 + compliant wheels + rollers | ≈$170 | ≈$340 | Side plates, rollers | 19 h |
| M3 Hopper / bed | `REV-41-3049-PK5` + hardware | ≈$30 | ≈$60 | Bent walls, retention lip | 8 h |
| M4 Release | 5203 motor + `2000-0025-0003` | ≈$92 | ≈$184 | Gate + linkage | 5 h |
| M5 Electronics + structure | §1 platform | ≈$840 | ≈$1,680 | Tray, harness, signs | 37 h |
| **MARGINAL (M2–M4)** | | **≈ $292** | **≈ $584** | | **32 h** |

### 2.4.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$292 | **≈$584** | DOUBLED — COTS |
| Printed/sheet material | ≈$26 | ≈$52 | DOUBLED — material |
| Shared spares + tooling | — | ≈$450–$650 | PAID ONCE |
| **TOTAL** | **≈ $2,258** | ⭐ **≈ $5,580–$5,780** | |
| Fabrication + assembly hours | ≈ 62 h | **≈ 82 h** | |
| Software | ≈ 12 h | **≈ 13 h** | One button in, one button out |

### 2.4.7 Duplicability verdict — **5/5. The most duplicable real scoring robot in this file.**

**Everything about it copies.** Printed intake parts (ratio 0.20), jigged sheet hopper (0.25–0.40 with the
jig), and a control scheme so simple that robot B's software is a config file. **[J] Two identical copies is a
realistic weekend once the design is frozen.**

**[J] Three changes that make the second copy even easier:**
1. **Build the bend jig before the first hopper.** 1 h of jig work halves every subsequent bend.
2. **Use "reverse the intake" as the release.** It removes a motor, a servo, a linkage and a mechanism —
   twice — and it never jams open.
3. **Two-motor tank drive.** If the game is flat and traffic is light, this frees two motor slots on both
   robots for whatever the season turns out to reward.

### 2.4.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Release | Reverse the intake | Tipping bucket + servo gate | |
| Hopper | Open bed with a lip | Bent walls + retention lip + guides | |
| Marginal COTS / robot | **≈ $200** | **≈ $292** | |
| **2-robot marginal** | **≈ $400** | **≈ $584** | **+$184** |
| Student-hours (both) | ≈ 32–42 h | ≈ 50–62 h | **+18 h** |
| R503 | ⭐ 5 M / 0 S | 6 M / 2 S | +1 M, +2 S |
| **What the money buys** | — | 🕐 **Deposit at a height the open bed cannot reach, and a controlled release rate instead of dumping everything at once.** [J] **This is the smallest cheap→competitive delta in the entire document — $184 and 18 hours.** That, not the scoring ceiling, is why this archetype scores Fit 4.25 | |

---

## 2.5 The climber / hanger / suspender (endgame specialist)

> **Library:** §3.5 · **Fit [D] 2.88** · Build complexity **4** (structural) · Duplicability **3**
> **Identity:** at 0:30, put the robot somewhere the floor is not. **[C] R104 removes the weight limit that
> used to bound this** — which means the load path now has to survive whatever you built.

### 2.5.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Reach** | Get a hook or grabber to the bar. Often shares the §2.2 slides | 0–1 | 0–1 | 🔴 🕐 **R105 EXPANSION-GATED and the bar geometry is unknown** |
| M2 | **Hook / grabber** | Engage the bar and not come off under load | 0 | 0–1 | 🕐 |
| M3 | **Winch / pull** | Lift the full robot mass | **1–2** | 0 | 🕐 climb height |
| M4 | **Latch / ratchet** | Hold the robot at 0:00 **without the motor holding it** | 0 | 0–1 | — |
| M5 | **Structure** | Carry full robot weight through one point into the chassis | 0 | 0 | **[C] R104** |

> ⚠ **[C] R103** warns against motors *"stalled against a hard stop"* for minutes. **A ratchet or a mechanical
> latch is not a nicety — it is the thermal-safety answer, and it costs $0 in motor slots.**

### 2.5.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Winch motor | goBILDA | 5203/5204 Series Yellow Jacket, **lowest-RPM / highest-torque** ratio | **1** | **2** | **$54.99 / $56.99 ea** | Buy | **VERIFIED** — 5203 $54.99, **5204 $56.99** | 5204 (80 mm) if the torque calc demands it. 🕐 Ratio computable only once climb height and robot mass are known |
| Winch cord | REV Robotics | UHMWPE **`REV-41-1162`** 1.2 mm × 10 m, 300 lb+ · **`REV-29-1244`** 3 mm × 10 m, 1500 lb+ | 1 | 2 | **$7.75 / $13.50 ea** | Buy | **PHASE-B** (`EXTENSION-ARMS-LIFTS.md` §7.4.1, verified there) | **[J] Buy the 3 mm.** $5.75 more for 5× the breaking strength, on a mechanism that lifts the whole robot |
| Ratchet / one-way bearing | goBILDA | ratcheting devices — **[C] R303.H** names *"ratcheting devices (wrenches, bearings, etc.)"* as an explicit COTS exception | 1 | 2 | **≈ $25** | Buy | **FAMILY-ONLY** — legality **CONFIRMED-BIOBUZZ**, SKU **NEEDS-SKU-CHECK** | ⭐ The single most valuable $25 on this robot: it is what lets the motor stop pulling at 0:00 |
| Hook release servo | goBILDA | **`2000-0025-0002`** (Torque) | 0–1 | 0–2 | **$36.99 ea** | Buy | **VERIFIED** — $36.99 | Only if the hook must deploy from inside the 18-in cube |
| Gas spring / assist (optional) | goBILDA | 2900-series shocks / dampers | 0–2 | 0–4 | **≈ $30** | Buy | **PHASE-B** | ✅ **[C] R801** permits *sealed COTS closed-air systems pre-charged by the manufacturer*. **A gas shock is legal; a pneumatic cylinder is not.** Zero R503 cost |
| Slides (if the climb shares the lift) | goBILDA | `3210-0003-0002` — see §2.2.2 | 0–1 | 0–2 | **$159.99 ea** | Buy | **VERIFIED** | ⭐ **[J] Sharing the lift is how this archetype becomes affordable.** A dedicated climb structure roughly doubles its cost |
| Structural stock + hardware | goBILDA | 1120 U-Channel + M4 hardware, **over-built** | 1 lot | 2 lots | **≈ $70** | Buy | **FAMILY-ONLY** | **[C] R104** — no weight limit. Over-build the load path; it is free |

### 2.5.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Hook / grabber | in-house | 3D print **in PETG or nylon, not PLA**, or cut aluminium | 1–2 | 2–4 | ≈$6 | **Fab** | **PHASE-B [J]** | **≈ 8 h.** ⚠ **PLA creeps under sustained load and is warm from the match.** This is the one printed part where material choice is a safety item |
| Winch spool | in-house | 3D print with a printed flange | 1 | 2 | ≈$3 | Fab | **PHASE-B** | **≈ 4 h.** Flanges stop the cord jumping the drum |
| **Load-path gussets** | in-house | Cut plate + hand-drilled, **or bolt through existing channel** | 4–6 | 8–12 | ≈$15 | Fab | **[J]** | **≈ 10 h. 🔴 The hand-fitted part — ratio ≈0.8, almost no duplication discount.** It is why this archetype scores Duplicability 3 |
| Latch / ratchet pawl | in-house | 3D print + spring | 1 | 2 | ≈$3 | Fab | **PHASE-B** | **≈ 5 h** |

### 2.5.4 R503 actuator budget

| Configuration | Drive | Scoring mech. | Reach | Winch | Latch | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Cheap** (hook on a passive deployable arm, 1 winch motor, mechanical ratchet) | 4 M | 1 M | 0 | **1 M** | 0 | **6 / 8** | **0 / 8** | ⭐ Excellent — the whole endgame for one motor slot |
| **Competitive** (climb shares the §2.2 lift, servo hook release) | 4 M | 1 M | shared | **1 M** | 1 S | **6 / 8** | **1 / 8** | ✅ |
| 🔴 **Bolted onto a competitive stacker** (§2.2) | 4 M | 1 M + 2 M lift | shared | 1 M | 1 S | ⛔ **8 / 8** | 6 / 8 | 🔴 **Zero reserve. This is `ROBOT-ARCHETYPE-LIBRARY.md` §6.1.5 — the endgame mechanism that costs a scoring mechanism** |

### 2.5.5 BOM SUMMARY — competitive version (climb sharing the lift)

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Reach | shares the §2.2 slides — $0 marginal | $0 | $0 | Mounting brackets | 4 h |
| M2 Hook | printed PETG/nylon + release servo | ≈$40 | ≈$80 | Hook, release tab | 8 h |
| M3 Winch | 5203/5204 + `REV-29-1244` cord + spool | ≈$70 | ≈$140 | Spool + flanges | 6 h |
| M4 Latch / ratchet | one-way bearing | ≈$25 | ≈$50 | Pawl + spring | 5 h |
| M5 Structure | U-channel + M4, over-built | ≈$70 | ≈$140 | 🔴 Load-path gussets | 10 h |
| **MARGINAL (M1–M5)** | | **≈ $205** | **≈ $410** | | **33 h** |

### 2.5.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS (climb only) | ≈$205 | **≈$410** | DOUBLED — COTS |
| Printed/sheet material | ≈$27 | ≈$54 | DOUBLED — material |
| Shared spares + tooling | — | ≈$500–$700 | PAID ONCE |
| **TOTAL (climb layer alone, on top of a scoring robot)** | **≈ $2,172** | **≈ $5,458–$5,658** | |
| Fabrication + assembly hours | ≈ 63 h | **≈ 83 h** | |
| Software | ≈ 10 h | **≈ 11 h** | Usually one held button plus an encoder limit |

### 2.5.7 Duplicability verdict — **3/5. The geometry copies; the structural fit to each chassis does not.**

The winch, spool, hook and ratchet all duplicate at printing ratios (~0.2). **The gussets do not** — they are
fitted to whatever the chassis and the scoring mechanism left room for, and hand-fitting carries **no
duplication discount at all**.

**[J] Three changes that make the second copy less painful:**
1. **Bolt through existing goBILDA channel patterns rather than drilling custom gussets.** Turns a 0.8-ratio
   fitted part into a 0.2-ratio printed spacer.
2. **Share the lift.** A dedicated climb structure roughly doubles this archetype's marginal cost and its
   hours, on both robots.
3. **Decide the climb before the chassis is finished.** Retro-fitting a load path into a finished robot is
   where the 10 gusset hours actually go.

### 2.5.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Reach | Passive spring-deployed arm | Shares the powered lift, encoder-homed | |
| Latch | Printed pawl + spring | COTS one-way bearing | |
| Cord | `REV-41-1162` 1.2 mm | `REV-29-1244` 3 mm, 1500 lb | |
| Marginal COTS / robot | **≈ $130** | **≈ $205** | |
| **2-robot marginal** | **≈ $260** | **≈ $410** | **+$150** |
| Student-hours (both) | ≈ 25–35 h | ≈ 33–45 h | **+10 h** |
| R503 | 6 M / 0 S | 6 M / 1 S | +1 S |
| **What the money buys** | — | 🕐 **Repeatability under time pressure.** [J] A climb attempted at 0:25 that fails scores zero. The competitive version buys a *deterministic* engagement instead of a driver aligning a passive hook by eye — and the whole delta is $150 | |

---

## 2.6 The pusher / plow

> **Library:** §3.6 · **Fit [D] 4.50 — the highest in the library** · Build complexity **1** · Cost **1**
> **Identity:** a drivetrain and a shaped plate. **Zero extra motors.**
> **[J] Build the pusher first. It is every team's week-2 fallback and the B team's starting point.**

### 2.6.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | Move elements by pushing. Traction matters more than speed | 4 (or 2) | 0 | §1 platform |
| M2 | **Plow / plate** | Corral elements and steer them, without becoming an illegal entanglement hazard | **0** | **0** | 🕐 element size, **R105** |
| M3 | **Structure** | Survive being driven into a wall repeatedly | 0 | 0 | **[C] R104** |

### 2.6.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Polycarbonate sheet | REV Robotics | `REV-41-3049-PK5` (5-pack) · REV also lists polycarbonate **$11–$75** on `/ftc/structure/` | 1 pack | **1–2 packs** | **$11.00 ea** | Buy | **PHASE-B** (price band re-confirmed by the Phase B drivetrain log) | ⭐ **Polycarbonate, not acrylic. Acrylic shatters on tile impact** |
| Mounting hardware | goBILDA | M4 hardware, brackets, standoffs | 1 lot | 2 lots | **≈ $25** | Buy | **FAMILY-ONLY** | ⚠ goBILDA M4 assortment was recorded **out of stock** in Phase A. Order early |
| Compliant edge (optional) | REV Robotics | `REV-41-2035-PK4` 30A wheels as free-spinning corner rollers | 0–1 pack | 0–2 packs | **$19.50 ea** | Buy | **VERIFIED** — $19.50, In Stock | Turns a plow into a plow that does not snag on the field wall |

### 2.6.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Plow plate | in-house | Cut + bent polycarbonate, on a template | 1 | 2 | ≈$8 | **Fab** | **PHASE-B** | **1.8 h with a jig, 3.7 h without.** ⭐ Make the template first |
| Deployable wing (optional) | in-house | Print + spring hinge | 0–2 | 0–4 | ≈$5 | Fab | **[J]** | **≈ 5 h.** 🕐 **R105 EXPANSION-GATED** — a wing that unfolds is an expansion; do not size it before kickoff |
| Bumper / edge guard | in-house | Sheet + TPU | 1 | 2 | ≈$8 | Fab | **PHASE-B** | **3.7 h** |

### 2.6.4 R503 actuator budget

| Configuration | Drive | Plow | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|
| **Cheap** (fixed plate, 2-motor tank) | 2 M | 0 | ⭐⭐ **2 / 8** | ⭐⭐ **0 / 8** | ⭐⭐ **6 motors and 8 servos in reserve. Nothing else in this file comes close** |
| **Competitive** (mecanum, sprung wings) | 4 M | 0 | ⭐ **4 / 8** | ⭐ **0 / 8** | ⭐ **4 motors free for whatever kickoff reveals** |

> **[D] This archetype's real product is not points — it is reserve capacity.** It leaves 4–6 motor slots and
> 8 servo slots open, which means it can be *upgraded into* §2.1 or §2.4 mid-season without tearing anything
> out. **[J] That is exactly why the library says build it first.**

### 2.6.5 BOM SUMMARY

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform | $699.99 | $1,399.98 | Assembly | 20 h |
| M2 Plow | `REV-41-3049-PK5` + hardware | ≈$45 | ≈$90 | Plate, template, wings | 7 h |
| M3 Structure / electronics | §1 platform | ≈$840 | ≈$1,680 | Bumpers, tray, harness, signs | 40 h |
| **MARGINAL (M2)** | | **≈ $45** | **≈ $90** | | **7 h** |

### 2.6.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$45 | **≈$90** | DOUBLED — COTS |
| Printed/sheet material | ≈$21 | ≈$42 | DOUBLED — material |
| Shared spares + tooling | — | ≈$400–$550 | PAID ONCE |
| **TOTAL** | **≈ $2,006** | ⭐⭐ **≈ $5,026–$5,176** | **The cheapest complete two-robot program in this file** |
| Fabrication + assembly hours | ≈ 55 h | **≈ 67 h** | |
| Software | ≈ 6 h | **≈ 7 h** | Drive code and nothing else |

### 2.6.7 Duplicability verdict — **5/5. Trivial.**

Cut two plates off one template in the same session (sawn/sheet ratio ≈0.25–0.5 with a jig). **[J] There is
no meaningful second-robot penalty at all.** If a design review ever produces a two-robot plan that this
program cannot afford, this is the row it falls back to.

**[J] The only real risk is a rules risk, not a cost risk:** a plow is an easy shape to make illegal — check
it against **[C] R102** (18-in cube in STARTING CONFIGURATION), **[C] R105** (expansion — 🕐 deferred), and the
G-rules on entanglement and element control at kickoff.

### 2.6.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Plow | Fixed flat plate | Bent plate + sprung deployable wings + corner rollers | |
| Drive | 2-motor tank | 4-wheel mecanum | |
| Marginal COTS / robot | **≈ $30** | **≈ $65** | |
| **2-robot marginal** | **≈ $60** | **≈ $130** | **+$70** |
| Student-hours (both) | ≈ 5 h | ≈ 14 h | **+9 h** |
| R503 | ⭐⭐ 2 M / 0 S | ⭐ 4 M / 0 S | +2 M |
| **What the money buys** | — | 🕐 **A wider capture width (R105-gated) and the ability to approach from any angle.** [J] **$70 and 9 hours is the cheapest capability upgrade in this document** — but it is also the archetype with the lowest ceiling, so spend the savings on §2.1 rather than on a better plow | |

---

## 2.7 The dedicated defender

> **Library:** §3.7 · **Fit [D] 3.50 ⚠** · Scoring ceiling **1**
> ⚠ **The library flags this Fit index as deliberately misleading: it measures buildability against payoff and
> does NOT price rules risk.** Read `reference/PENALTY-AND-ENFORCEMENT.md` before acting on it.
> **Identity:** a heavy, wide, low robot that denies opponents. **[C] R104** removes the weight limit, so mass
> is free — which is precisely what makes this archetype cheap to build and expensive to get wrong.

### 2.7.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | Push, hold position, and survive repeated contact. **Traction and gear ratio, not speed** | 4 | 0 | §1 platform |
| M2 | **Armour / structure** | Absorb contact without deforming the frame or exposing electronics | 0 | 0 | **[C] R104** |
| M3 | **Ballast** | Add mass low in the chassis | 0 | 0 | **[C] R104** |
| M4 | **Manipulator** | Often none — which frees 4+ motors | 0 | 0 | 🕐 |

> ⛔ **[C] R204** prohibits any mechanism designed to increase downforce ("no grabbing the floor").
> ⛔ **[C] R801** prohibits vacuums and suction. **There is no legal adhesion defender in BIOBUZZ.**

### 2.7.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| High-traction wheels | goBILDA | **Hogback Traction Wheels** (50A) and **Rhino Wheels** families — [gobilda.com/wheels-tires/](https://www.gobilda.com/wheels-tires/) | 4 | 8 | **≈ $60–$90 per robot** | Buy | **FAMILY-ONLY** — categories confirmed this session; **per-SKU prices verified in `DRIVETRAIN-AND-ODOMETRY.md` §4.3, not by me.** NEEDS-SKU-CHECK | Swapping mecanum for traction wheels **removes strafing**. Decide which you actually want before ordering |
| Lower-RPM drive motors | goBILDA | 5203 Series Yellow Jacket, high-torque ratio | 0–4 | 0–8 | **$54.99 ea** | Buy | **VERIFIED** — $54.99 | 🔴 **A full re-gear is $219.96 per robot, $439.92 for two.** Cost this honestly before choosing to defend |
| Polycarbonate armour | REV Robotics | `REV-41-3049-PK5` · REV polycarbonate $11–$75 | 1–2 packs | 2–4 packs | **$11.00 ea** | Buy | **PHASE-B** | |
| Structural stock | goBILDA | 1120 U-Channel, doubled up | 1 lot | 2 lots | **≈ $80** | Buy | **FAMILY-ONLY** | |

### 2.7.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Armour panels | in-house | Cut polycarbonate on a template | 4–6 | 8–12 | ≈$14 | **Fab** | **PHASE-B** | **≈ 6 h with a template** |
| Ballast mounting | in-house | Steel plate bolted low and central | 1 | 2 | ≈$20 | Fab | **[J]** | **≈ 3 h.** ⭐ **[C] R104 makes ballast free.** Mass low in the chassis is worth more than mass anywhere else |
| Reinforced bumper set | in-house | Sheet + TPU, doubled | 1 set | 2 sets | ≈$12 | Fab | **PHASE-B** | **≈ 5 h** |
| Electronics protection | in-house | Enclosing guards — **mounts, not enclosures** | 1 set | 2 sets | ≈$6 | Fab | **PHASE-B** | **≈ 4 h.** ⛔ **[C] R706** forbids replacing hub enclosures with custom ones. **[C] R606.B** still requires the diagnostic LEDs to be visible |

### 2.7.4 R503 actuator budget

| Configuration | Drive | Manipulator | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|
| **Pure defender** | 4 M | 0 | ⭐ **4 / 8** | ⭐ **0 / 8** | Enormous reserve — and **[J] that reserve is the argument against ever building a pure defender.** Spend those four motors on scoring |

### 2.7.5 BOM SUMMARY

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform + traction wheels (+ optional re-gear) | ≈$780 | ≈$1,560 | Assembly, wheel swap | 24 h |
| M2 Armour | polycarbonate + structural stock | ≈$100 | ≈$200 | Panels, bumpers, guards | 15 h |
| M3 Ballast | steel plate | ≈$20 | ≈$40 | Mounting | 3 h |
| M4 Electronics | §1 platform | $610 | $1,220 | Tray, harness, signs | 25 h |
| **MARGINAL (M1 wheels + M2 + M3)** | | **≈ $200** | **≈ $400** | | **22 h** |

### 2.7.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$200 | **≈$400** | DOUBLED — COTS |
| Printed/sheet material | ≈$52 | ≈$104 | DOUBLED — material |
| Shared spares + tooling | — | ≈$400–$550 | PAID ONCE |
| **TOTAL** | **≈ $2,192** | **≈ $5,398–$5,548** | |
| Fabrication + assembly hours | ≈ 58 h | **≈ 72 h** | |
| Software | ≈ 6 h | **≈ 7 h** | |

### 2.7.7 Duplicability verdict — **4/5. Easy to copy, and that is the trap.**

Armour panels cut from a template and ballast bolted low both duplicate cheaply. **[J] The archetype is
genuinely easy to build twice — which is exactly why a small program can talk itself into it.**

> **⚠ [J] THE HONEST VERDICT: do not build this as a primary identity for either robot.**
> `ROBOT-ARCHETYPE-LIBRARY.md` §3.7 and §6.1.3 both say so, and the reasoning is not about cost. It is that
> (a) the scoring ceiling is **1**, (b) the penalty exposure is real and the G-rules governing it are
> **🕐 not published until kickoff**, and (c) an alliance partner cannot carry two non-scoring robots.
> **Every robot should be *capable* of incidental legal defense. Neither robot should be *designed* for it.**

### 2.7.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Wheels | Keep the Strafer's mecanum | Traction wheel swap | |
| Gearing | Stock 312 RPM | Re-geared high-torque 5203s | |
| Armour | Polycarbonate panels | Doubled structure + full guards | |
| Marginal COTS / robot | **≈ $60** | **≈ $420** (incl. re-gear) | |
| **2-robot marginal** | **≈ $120** | **≈ $840** | **+$720** |
| Student-hours (both) | ≈ 10 h | ≈ 30 h | **+20 h** |
| R503 | 4 M / 0 S | 4 M / 0 S | — |
| **What the money buys** | — | 🔴 **More pushing force and better survivability — and nothing on the scoring table.** [J] **This is the only row in the document where I recommend against the competitive version outright.** $720 buys four extra Yellow Jackets; spend them on §2.1's intake and delivery instead | |

---

## 2.8 The park-and-AUTO specialist

> **Library:** §3.8 · **Fit [D] 4.00** · Build complexity **1** · Duplicability **5** · Reliability **5**
> **Identity:** adds no mechanism. It is odometry, a camera, a path and a state machine.
> ⭐ **[J] The single best shared investment a two-team program can make: written once, deployed twice.**

### 2.8.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | Repeat the same path to ±2 cm, cold, on the first run of the day | 4 | 0 | §1 platform |
| M2 | **Localization** | Know where the robot is without depending on wheel slip | **0** | **0** | §1 platform |
| M3 | **Vision** | Read the randomization / target and branch | **0** | **0** | 🕐 kickoff |
| M4 | **Scoring mechanism** | Whatever the teleop robot already has | reuse | reuse | 🕐 |
| M5 | **Structure** | A rigid, repeatable camera pose and a known starting alignment | 0 | 0 | **[C] R102** |

> ⭐ **[C] R501 verbatim: motors integral to a COTS sensor "do not count toward the limit in R503."**
> Encoders, odometry pods, IMUs, distance sensors and cameras are **all free against the actuator cap**.
> This archetype's entire hardware story costs **zero motor and zero servo slots**.

### 2.8.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Odometry (already in §1) | goBILDA | 4-Bar Odometry Pack **`3203-3110-0002`** (2 pods + Pinpoint V2) | 1 | **2** | **$279.99 ea** | Buy | **VERIFIED** — $279.99 | **[C] R303.J** names *"dead-wheel odometry kits"* as legal COTS. **Already counted in §1** — marginal cost here is **$0** |
| Webcam (already in §1) | FIRST storefront | FTC-legal webcam, **included in the $295 Driver Kit** | 1 | **2** | **$0 marginal** | Buy | **VERIFIED** — contents of the storefront Driver Kit | ⭐ **You already own two. This archetype's true marginal hardware cost is zero** |
| Vision coprocessor (optional) | Limelight Vision | Limelight 3A | 0–1 | **0–2** | **$189.00 ea = $378.00** | Buy | **VERIFIED** price; stock not stated | ⚠ **[C] R702** permits programmable vision coprocessors *"natively supported by the FTC SDK"* — **Table 12-9 is the closed list. Verify before ordering** |
| Through-bore encoder (alt. path) | REV Robotics | **`REV-11-3174`** V2, 8192 cts/rev | 0–3 | 0–6 | **$48.00 ea** | Buy | **PHASE-B** (`DRIVETRAIN-AND-ODOMETRY.md` §7.3, verified there) | ⚠ **`REV-11-1271` V1 is marked DISCONTINUED.** Do not order the V1 |
| Distance / limit sensors | REV Robotics | FTC Sensor Bundle **`REV-45-1885`** | shared | 1 (shared) | **$180.00** | Buy | **VERIFIED** — $180.00 | Buy **once** for the program. A wall-reference distance sensor is the cheapest AUTO reliability fix there is |

### 2.8.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| **Camera mount, locked pose** | in-house | 3D print, **locked focus, measured angle** | 1 | 2 | ≈$3 | **Fab** | **PHASE-B** | **2.3 h.** ⭐ **Standardise the mount geometry across both robots and one calibration serves both** |
| Odometry pod mounts | in-house | 3D print, sprung against the tile | 2 | 4 | ≈$4 | Fab | **PHASE-B** | **≈ 4 h.** Consistent preload is what makes the two robots agree |
| **Starting-alignment jig** | in-house | Printed corner blocks + field tape | 1 | **1–2 (shared)** | ≈$3 | Fab | **[J]** | **≈ 3 h.** ⭐ A repeatable start pose is worth more than a better path planner, and it costs $3 |
| Sensor / limit-switch brackets | in-house | 3D print | 2–4 | 4–8 | ≈$3 | Fab | **PHASE-B** | **1.4 h.** The archetypal printed part — ratio 0.17 |

### 2.8.4 R503 actuator budget

| Configuration | Drive | Sensors | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|
| Any | 4 M | **0 M / 0 S — free under [C] R501/R503** | **4 / 8** | **0 / 8** | ⭐ **Adds nothing to the budget. It is the only archetype in this file that is free against R503** |

### 2.8.5 BOM SUMMARY

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform | $699.99 | $1,399.98 | Assembly | 20 h |
| M2 Localization | §1 odometry pack | $279.99 (in §1) | $559.98 (in §1) | Pod mounts | 4 h |
| M3 Vision | storefront webcam — **$0 marginal** | $0 | $0 | Camera mount | 2.3 h |
| M4 Scoring | reuses the teleop robot's mechanism | $0 | $0 | — | 0 h |
| M5 Alignment | — | ≈$3 | ≈$6 | Start jig, brackets | 4.4 h |
| **MARGINAL** | | ⭐ **≈ $3** | ⭐ **≈ $6** | | **≈ 11 h** |
| **SOFTWARE (the real cost)** | — | — | — | — | 🔴 **50–80 h robot A · +3–5 h robot B** |

### 2.8.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform (incl. odometry + webcam) | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ⭐ ≈$3 | ⭐ **≈$6** | negligible |
| Optional 2× Limelight 3A | +$189 | +$378 | DOUBLED — COTS |
| Shared spares + tooling | — | ≈$400–$550 | PAID ONCE |
| **TOTAL (webcam path)** | **≈ $1,943** | ⭐ **≈ $4,900–$5,050** | |
| Fabrication hours | ≈ 42 h | **≈ 53 h** | |
| **Software hours** | 🔴 **50–80 h** | 🔴 **53–85 h** | ⭐ **Robot B costs 3–5 h. This is the best labour ratio in the entire document** |

### 2.8.7 Duplicability verdict — **5/5. Software duplicates for free.**

> **[D] Robot B's AUTO costs ≈ 4 student-hours and ≈ $3.** Nothing else in this file is remotely close.
> One programming pair writes one localization stack, one path library and one vision branch, and **both
> robots run it from a per-robot constants file**.

**[J] Three things that protect that ratio:**
1. **Standardise the camera mount and the odometry pod positions across both robots.** The moment the two
   robots have different sensor geometry, you have two calibrations and the ratio collapses.
2. **Never fork the code.** Per-robot constants file, always — the rule from
   `INTAKE-AND-MANIPULATION.md` §19.2 rule 7.
3. **Build a fallback path with no vision.** `ROBOT-ARCHETYPE-LIBRARY.md` §6.1.6: vision without a fallback
   is a listed underperformer. A dead-reckoning park that always works beats a vision routine that works 70 %
   of the time.

### 2.8.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Localization | Drive encoders + IMU | 2-pod dead-wheel odometry + Pinpoint V2 | |
| Vision | Storefront webcam | Limelight 3A | |
| Marginal COTS / robot | **≈ $3** | **≈ $192** | |
| **2-robot marginal** | **≈ $6** | **≈ $384** | **+$378** |
| Student-hours (both) | ≈ 40–55 h software | ≈ 55–90 h software | **+30 h** |
| R503 | ⭐ 0 M / 0 S | ⭐ 0 M / 0 S | — |
| **What the money buys** | — | 🕐 **A vision pipeline that runs off the Control Hub's CPU budget instead of on it, and detection at longer range.** [J] **Buy one Limelight for the A robot only, and only if AUTO scoring is the strategy.** The odometry pack, by contrast, is worth its $279.99 on both robots in almost any season | |

---

## 2.9 The human-player-feed specialist

> **Library:** §3.9 · **Fit [D] 3.88** · Duplicability **4** · Scoring ceiling **4**
> **Identity:** acquire from a **known, staged presentation** rather than from an arbitrary floor orientation —
> which is dramatically easier — and shuttle a short, repeated path.

### 2.9.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Drivetrain** | Run one short shuttle path fast and repeatably | 4 (or 2) | 0 | §1 platform |
| M2 | **Acquisition** | Accept an element **in a known orientation**. Often a passive funnel or a fixed claw | 0–1 | 0–1 | 🔴 🕐 **entirely dependent on how the game stages elements** |
| M3 | **Retention** | Hold it through a fast drive without dropping it | **0** | 0–1 | 🕐 |
| M4 | **Release** | Deposit at the scoring location | 0 | 0–1 | 🕐 |
| M5 | **Structure** | A lead-in geometry the human player can hit without aiming | 0 | 0 | **[C] R102** |

> 🔴 **This is the most kickoff-dependent archetype in the file.** If BIOBUZZ has no human-player feed, it
> does not exist. Cost it, but do not commit to it before 2026-09-12.

### 2.9.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Retention / release servo | goBILDA | **`2000-0025-0003`** (Speed) | 1 | **2** | **$36.99 ea = $73.98** | Buy | **VERIFIED** — $36.99 | Often the **only** actuator this archetype adds |
| Compliant lead-in wheels | REV Robotics | **`REV-41-2035-PK4`** 30A, 4-pack | 0–1 pack | 0–2 packs | **$19.50 ea** | Buy | **VERIFIED** — $19.50, In Stock | Free-spinning rollers on the funnel mouth: guides the element in without a motor |
| Silicone tubing (grip liner) | goBILDA | `2928-0508-0002` | 1 | 2 | **$5.99 ea** | Buy | **PHASE-B** | Jaw liners and lead-in lips |
| Springs (passive retention) | goBILDA | 2915 / 2916 spring families | 2 | 4 | **≈ $14** | Buy | **PHASE-B** | ⭐ **Zero R503 cost.** Over-centre spring retention holds without any actuator at all |
| Polycarbonate | REV Robotics | `REV-41-3049-PK5` | 1 pack | 1–2 packs | **$11.00 ea** | Buy | **PHASE-B** | Funnel walls |
| Hardware allowance | goBILDA | M3/M4, hinges, bearings | 1 lot | 2 lots | **≈ $25** | Buy | **FAMILY-ONLY** | |

### 2.9.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| **Passive funnel / lead-in** | in-house | Bent polycarbonate + printed corners | 1 | 2 | ≈$8 | **Fab** | **PHASE-B [J]** | **≈ 8 h.** ⭐ **Phase B costs this whole subsystem at ≈$28 in parts.** It is the single cheapest scoring mechanism in the catalogs |
| Over-centre latch / retention | in-house | Print + spring | 1 | 2 | ≈$4 | Fab | **PHASE-B** | **≈ 6 h.** ⭐ **Zero-actuator retention — [C] R503 costs nothing** |
| Release tab | in-house | 3D print | 1 | 2 (+2 spare) | ≈$2 | Fab | **PHASE-B** | **≈ 3 h** |
| Human-player target markings | in-house | Tape / printed guide on the robot | 1 | 2 | ≈$1 | Fab | **[J]** | **≈ 1 h.** ⚠ Must not conflict with **[C] R401**'s ROBOT SIGNS requirement or obscure them |

### 2.9.4 R503 actuator budget

| Configuration | Drive | Acquisition | Retention | Release | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|---|---|
| **Cheap** (passive funnel + over-centre latch) | 4 M | 0 | 0 | 1 S | ⭐ **4 / 8** | ⭐ **1 / 8** | ⭐⭐ Nearly the whole budget still free |
| **Competitive** (powered assist roller + servo gate) | 4 M | 1 M | 0 | 1 S | **5 / 8** | **1 / 8** | ⭐ Still 3 motors in reserve |

### 2.9.5 BOM SUMMARY — competitive version

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform | $699.99 | $1,399.98 | Assembly | 20 h |
| M2 Acquisition | 5203 assist motor + `REV-41-2035-PK4` | ≈$75 | ≈$150 | Funnel, lead-in rollers | 8 h |
| M3 Retention | springs + tubing | ≈$20 | ≈$40 | Over-centre latch | 6 h |
| M4 Release | `2000-0025-0003` | ≈$37 | ≈$74 | Release tab | 3 h |
| M5 Electronics + structure | §1 platform | ≈$840 | ≈$1,680 | Tray, harness, signs | 37 h |
| **MARGINAL (M2–M4)** | | **≈ $132** | **≈ $264** | | **17 h** |

### 2.9.6 Totals, with the shared/duplicated split

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | **≈$3,940** | DOUBLED — COTS |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$132 | **≈$264** | DOUBLED — COTS |
| Printed/sheet material | ≈$15 | ≈$30 | DOUBLED — material |
| Shared spares + tooling | — | ≈$400–$550 | PAID ONCE |
| **TOTAL** | **≈ $2,087** | ⭐ **≈ $5,188–$5,338** | |
| Fabrication + assembly hours | ≈ 55 h | **≈ 67 h** | |
| Software | ≈ 10 h | **≈ 11 h** | |

### 2.9.7 Duplicability verdict — **4/5. Small BOM, small CAD, both printed.**

The funnel and latch are printed or jigged sheet parts at ratios of 0.2–0.4. **[J] The only duplication cost
worth naming is human-player training**, which is a program cost, not a robot cost — and with two teams you
are training two human players anyway.

**[J] Three changes that make the second copy less painful:**
1. **Make retention passive (over-centre latch + spring).** Removes a servo, a wire and a config constant on
   both robots, and it cannot fail electrically.
2. **Standardise the lead-in geometry across both robots** so one human player can feed either robot without
   re-learning the target.
3. **Print the funnel from the same file, in the same batch.** A 4 mm difference between the two lead-ins is
   a 4 mm difference in how forgiving each robot is.

### 2.9.8 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Acquisition | Passive funnel, gravity | Funnel + powered assist roller | |
| Retention | Over-centre spring latch | Servo-held gate | |
| Marginal COTS / robot | **≈ $60** | **≈ $132** | |
| **2-robot marginal** | **≈ $120** | **≈ $264** | **+$144** |
| Student-hours (both) | ≈ 12–18 h | ≈ 17–25 h | **+7 h** |
| R503 | ⭐ 4 M / 1 S | 5 M / 1 S | +1 M |
| **What the money buys** | — | 🕐 **Tolerance of a sloppier human-player throw and a faster hand-off.** [J] $144 for a mechanism that removes a whole class of "the human player missed" losses is good value — *if* the game has a human-player feed at all | |

---

## 2.10 The specialist / generalist axis

`ROBOT-ARCHETYPE-LIBRARY.md` §3.10 frames these as the two ends of one decision. **Their BOMs are the two
ends of one budget**, so they are costed together here — plus a third option (§2.10c) that this file
recommends over both.

### 2.10a The specialist (one task, done at high rate)

> **Library:** §3.10a · Duplicability **4** · Cost **2** · Scoring ceiling **4**
> **Identity:** one scoring action, refused everything else by design, optimised for cycle time.

**Mechanism breakdown:** drivetrain (§1) + **exactly one** of §2.1's intake+delivery, §2.3's launcher, §2.4's
hopper, or §2.9's funnel. **Nothing else.** Endgame: none unless the season forces it.

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform | $699.99 | $1,399.98 | Assembly | 20 h |
| M2 The one mechanism | whichever §2.x it is | **≈$180–$300** | **≈$360–$600** | That §2.x's fab table | 25–40 h |
| M3 Electronics + structure | §1 platform | ≈$840 | ≈$1,680 | Tray, harness, signs | 37 h |
| **MARGINAL** | | **≈ $180–$300** | **≈ $360–$600** | | **25–40 h** |

| Line | 1 robot | **2 robots** |
|---|---|---|
| Platform + marginal + material + shared pool | **≈ $2,150–$2,270** | **≈ $5,290–$5,590** |
| Fabrication hours | ≈ 55–70 h | **≈ 70–90 h** |
| Software | ≈ 15 h | ≈ 16 h |
| R503 | **5–6 M / 1–2 S** | ⭐ 2–3 motors in reserve |

**Duplicability verdict — 4/5.** Small BOM, small CAD, one set of tolerances, one state machine. **[J] The
duplication penalty is genuinely low, and the reserve capacity means a mid-season pivot is affordable.**

**Cheap vs competitive:** the delta is **whichever §2.x you chose** — see that section. **[J] The specialist's
real "competitive upgrade" is not a better mechanism, it is *driver practice hours*, which cost $0.**

### 2.10b The generalist (a mechanism for every scoring action)

> **Library:** §3.10b · Build complexity **5** · **Duplicability 1** · Cost **5** · **Fit [D] 1.88 — the worst
> in the library.** *"Fatal for a two-team program."*

**Mechanism breakdown:** drivetrain + intake + transfer + lift + wrist + gripper + endgame + vision. Every
subsystem in §2.1 through §2.5, at once, inside **[C] R102**'s 18-inch cube.

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 platform | $699.99 | $1,399.98 | Assembly + ballast | 23 h |
| M2 Intake | §2.1 | ≈$170 | ≈$340 | Side plates, rollers | 19 h |
| M3 Transfer | §2.1 | ≈$57 | ≈$114 | Chute | 10 h |
| M4 Lift | §2.2 | ≈$420 | ≈$840 | Brackets, guards | 25 h |
| M5 Wrist + gripper | §2.2 | ≈$298 | ≈$596 | VFB plates, jaws | 26 h |
| M6 Fold | §2.2 | ≈$25 | ≈$50 | 🔴 Hand-fitted latch | 12 h |
| M7 Endgame | §2.5 | ≈$205 | ≈$410 | 🔴 Gussets, hook, spool | 33 h |
| M8 Electronics + structure | §1 platform | ≈$840 | ≈$1,680 | Tray, harness, signs | 37 h |
| **MARGINAL (M2–M7)** | | 🔴 **≈ $1,175** | 🔴 **≈ $2,350** | | 🔴 **125 h** |

| Line | 1 robot | **2 robots** |
|---|---|---|
| Platform + marginal + material + shared pool | 🔴 **≈ $3,170** | 🔴 **≈ $7,600–$7,900** |
| Fabrication hours | ≈ 130 h | 🔴 **≈ 185 h** |
| Software | ≈ 55 h | ≈ 60 h |
| **R503** | ⛔ **8 M / 6 S — AT THE CAP** | ⛔ **Zero motor reserve** |

**Duplicability verdict — 1/5. A second copy is a second full season of work.**

> ⛔ **[D] The arithmetic that should end the conversation: the generalist costs ≈ $2,500 more and ≈ 118 more
> student-hours than the ground-intake cycler across two robots, and it arrives at the R503 cap with zero
> reserve.** With ~15 students across two teams and limited mentor hours, **≈185 fabrication hours on
> mechanisms alone** is not a schedule this program has.
>
> **[J] Do not build this. It is listed here so that a design proposal claiming to be "just a cycler with a
> lift and a climb" can be priced against it and recognised for what it is.**

**Cheap vs competitive:** there is no cheap version of a generalist. **[J] The cheap version of a generalist
*is* §2.10a, the specialist.** That is the entire recommendation.

### 2.10c The reliability-first generalist ⭐ [J] — the shape this file recommends

> **[J] Not in the library as a numbered archetype; it is the synthesis §6.2 calls "boring but fast."**
> **Identity:** a *ground-intake cycler* (§2.1) that also parks and runs a strong AUTO (§2.8), with the
> **cheap** version of at most **one** additional capability, and **two motors held in reserve**.

**The rule that defines it:** every subsystem must pass three tests before it goes on the robot —
(1) does it duplicate at a ratio below 0.35? (2) does it leave ≥ 2 motor slots free? (3) can a rookie on the
B team assemble it from the frozen file? **Anything that fails two of the three is cut.**

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Drivetrain | §1 Strafer `3209-0001-0007` | $699.99 | $1,399.98 | Assembly | 20 h |
| M2 Intake | §2.1 competitive | ≈$170 | ≈$340 | Side plates, sprung pivot | 19 h |
| M3 Transfer | §2.1 cheap (gravity + gate servo) | ≈$57 | ≈$114 | Chute | 10 h |
| M4 Delivery | §2.1 competitive — `3210-0003-0002` + motor | ≈$275 | ≈$550 | Carriage, hard stops | 22 h |
| M5 AUTO + localization | §2.8 webcam path — **$0 marginal** | ≈$3 | ≈$6 | Camera mount, start jig | 11 h |
| M6 Endgame | ⛔ **deliberately omitted unless kickoff pays for it** | $0 | $0 | — | 0 h |
| M7 Electronics + structure | §1 platform | ≈$840 | ≈$1,680 | Tray, harness, signs | 37 h |
| **MARGINAL (M2–M6)** | | **≈ $505** | **≈ $1,010** | | **62 h** |

| Line | 1 robot | **2 robots** | Bucket |
|---|---|---|---|
| §1 per-robot platform | ≈$1,940 | ≈$3,940 | DOUBLED |
| §1 shared platform | — | ≈$554 | PAID ONCE |
| Archetype marginal COTS | ≈$505 | **≈$1,010** | DOUBLED |
| Printed/sheet material | ≈$38 | ≈$76 | DOUBLED |
| Shared spares + tooling | — | ≈$500–$750 | PAID ONCE |
| **TOTAL** | **≈ $2,483** | ⭐ **≈ $6,080–$6,330** | |
| Fabrication hours | ≈ 79 h | **≈ 107 h** | |
| **Software** | ≈ 65 h | **≈ 69 h** | Robot B ≈ 4 h |
| **R503** | ⭐ **6 M / 3 S** | ⭐ **2 motors, 5 servos in reserve** | |

**Duplicability verdict — 4/5**, and deliberately so: it is §2.1 with the two lowest-duplicability options
(the fold-dependent lift and the fitted climb) refused on principle.

> ⭐ **[J] If a design proposal on kickoff day does not clearly beat this shape on expected points per dollar
> and per student-hour, build this shape.** It is the row every other proposal should be measured against.

---

## 2.11 The randomized-target responder

> **Library:** §3.11 · **Fit [D] 3.75** · Build complexity **1** · Duplicability **5** · Programming load **5**
> **Identity:** read the season's randomization and branch. **Zero motors, zero servos, near-zero hardware.**

### 2.11.1 Mechanism breakdown

| # | Mechanism | What it must do | Motors | Servos | Gate |
|---|---|---|---|---|---|
| M1 | **Sensor** | See the randomization target reliably under venue lighting | **0** | **0** | 🕐 what the target *is* |
| M2 | **Mount** | Hold a **known pose with locked focus**, identically on both robots | 0 | 0 | **[C] R102** |
| M3 | **Branch logic** | Choose one of N paths, and **fall back safely when detection fails** | 0 | 0 | 🕐 |

### 2.11.2 BUY — marginal parts beyond the §1 platform

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Webcam | FIRST storefront | FTC-legal webcam — **included in the $295 Driver Kit** | 1 | **2** | ⭐ **$0 marginal** | Buy | **VERIFIED** — storefront Driver Kit contents | ⭐ **You already own two. Start here** |
| Vision coprocessor (optional) | Limelight Vision | Limelight 3A | 0–1 | 0–2 | **$189.00 ea** | Buy | **VERIFIED** price; stock not stated | ⚠ **[C] R702**: allowed only if natively supported by the FTC SDK per **Table 12-9**. **Check the table before ordering** |
| Colour / distance sensor (fallback) | FIRST storefront / REV | Color Sensor V3 — **included in the $350 Electronics Kit**; more in Sensor Bundle **`REV-45-1885`** | 1 | 2 | ⭐ **$0 marginal** | Buy | **VERIFIED** — storefront Electronics Kit contents | ⭐ **A non-vision fallback that costs nothing, because it is already in the box you bought** |

### 2.11.3 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Vendor | Method / material | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes (**hours for both robots**) |
|---|---|---|---|---|---|---|---|---|
| Camera mount, locked pose | in-house | 3D print | 1 | 2 | ≈$3 | **Fab** | **PHASE-B** | **2.3 h.** ⭐ **Identical geometry on both robots is what makes one calibration serve two** |
| Light shroud / hood | in-house | Print in **black** filament | 1 | 2 | ≈$2 | Fab | **[J]** | **≈ 2 h.** Venue lighting is the #1 cause of vision failure at events |
| Calibration target board | in-house | Printed sheet on rigid board | — | **1 (shared)** | ≈$3 | Fab | **[J]** | **≈ 2 h.** A **program** asset |

### 2.11.4 R503 actuator budget

| Configuration | Drive | Vision | **Motors** | **Servos** | Verdict |
|---|---|---|---|---|---|
| Any | 4 M | ⭐ **0 / 0 — [C] R501 carve-out** | **4 / 8** | **0 / 8** | ⭐ Free against the cap |

### 2.11.5 BOM SUMMARY and totals

| Mechanism | Key purchases | ≈ Cost / robot | ≈ Cost for 2 | In-house fabrication required | Student-hours (both) |
|---|---|---|---|---|---|
| M1 Sensor | storefront webcam + Color Sensor V3 — **$0 marginal** | $0 | $0 | — | 0 h |
| M2 Mount | — | ≈$5 | ≈$10 | Mount, shroud, cal. board | 6.3 h |
| M3 Branch logic | — | $0 | $0 | — | **20–35 h software (robot A); +2 h robot B** |
| **MARGINAL** | | ⭐ **≈ $5** | ⭐ **≈ $10** | | **≈ 6 h fab + 22–37 h software** |

| Line | 1 robot | **2 robots** |
|---|---|---|
| Platform + marginal + material + shared pool | **≈ $1,945** | ⭐⭐ **≈ $4,900–$5,050** |
| Optional 2× Limelight 3A | +$189 | +$378 |
| Fabrication hours | ≈ 42 h | **≈ 50 h** |
| Software hours | ≈ 30 h | **≈ 32 h** |

### 2.11.6 Duplicability verdict — **5/5. Written once, deployed twice.**

**[J] Provided the mounting geometry is standardised across the two robots, robot B's entire cost here is
≈ $5 and ≈ 2 hours.** If it is *not* standardised, you have two calibrations, two failure modes and two
debugging sessions in a loud gym — and the archetype's whole advantage evaporates.

### 2.11.7 Cheap vs competitive

| | **CHEAP** | **COMPETITIVE** | **Δ (2 robots)** |
|---|---|---|---|
| Sensor | Storefront webcam + Color Sensor V3 fallback | Limelight 3A + webcam fallback | |
| **2-robot marginal** | ⭐ **≈ $10** | **≈ $388** | **+$378** |
| Student-hours (both) | ≈ 25–35 h | ≈ 35–50 h | **+15 h** |
| R503 | ⭐ 0 M / 0 S | ⭐ 0 M / 0 S | — |
| **What the money buys** | — | 🕐 **Detection at longer range and off the Hub's CPU budget.** ⚠ **[J] `ROBOT-ARCHETYPE-LIBRARY.md` §6.1.6 lists "vision without a fallback" as a reliable underperformer. Spend the 15 hours on the fallback path before spending the $378 on the camera** | |

---

# 3. CROSS-ARCHETYPE COMPARISON

**[D] The two budgets this program is actually constrained by are dollars and student-hours.** Everything
below ranks the archetypes on exactly those two axes, for **two robots**, competitive version, with the §1
platform included.

> ⚠ **Read the LAYER column first.** Three entries — §2.5 climber, §2.8 park-and-AUTO, §2.11 randomized-target
> responder — are **overlays, not standalone robots.** They add capability to a scoring robot. Ranking them as
> "cheapest" without that caveat would be actively misleading: a §2.11 robot that scores nothing in teleop is
> not a $4,975 competitive robot, it is a $4,975 chassis with good AUTO.

## 3.1 Ranked by TWO-ROBOT TOTAL COST (competitive version, platform included)

| Rank | Archetype | § | **2-robot total** | Marginal COTS ×2 | Layer or standalone | Fit [D] | Duplic. |
|---:|---|---|---:|---:|---|:---:|:---:|
| 1 | **Park-and-AUTO specialist** | 2.8 | **≈ $4,975** | ≈$6 | 🔷 **LAYER** | 4.00 | **5** |
| 1= | **Randomized-target responder** | 2.11 | **≈ $4,975** | ≈$10 | 🔷 **LAYER** | 3.75 | **5** |
| 3 | **Pusher / plow** | 2.6 | ⭐ **≈ $5,101** | ≈$90 | ✅ standalone | **4.50** | **5** |
| 4 | **Human-player-feed specialist** | 2.9 | **≈ $5,263** | ≈$264 | ✅ standalone (game-dependent) | 3.88 | 4 |
| 5 | **Specialist (single-task)** | 2.10a | **≈ $5,440** | ≈$360–$600 | ✅ standalone | 3.88 | 4 |
| 6 | **Dedicated defender** | 2.7 | ≈ $5,473 | ≈$400 | ⚠ standalone, ceiling **1** | 3.50 ⚠ | 4 |
| 7 | **Climber / hanger** | 2.5 | ≈ $5,558 | ≈$410 | 🔷 **LAYER** | 2.88 | 3 |
| 8 | **Ramp / deposit bot** | 2.4 | ⭐ **≈ $5,630** | ≈$584 | ✅ standalone | **4.25** | **5** |
| 9 | **Launcher / shooter** | 2.3 | ≈ $6,189 (+$378 vision) | ≈$814 | ✅ standalone | 2.63 | 3 |
| 10 | **Ground-intake cycler** | 2.1 | ≈ $6,193 | ≈$1,004 | ✅ standalone | 3.63 | 4 |
| 11 | **Reliability-first generalist** ⭐ | 2.10c | ≈ $6,205 | ≈$1,010 | ✅ standalone | [J] — | 4 |
| 12 | **Stacker / builder** | 2.2 | 🔴 ≈ $7,087 | ≈$1,826 | ✅ standalone | 2.13 | **2** |
| 13 | **Generalist** | 2.10b | ⛔ **≈ $7,750** | ≈$2,350 | ✅ standalone | **1.88** | **1** |

**[D] The spread between the cheapest standalone competitive robot (§2.6, ≈$5,101) and the most expensive
(§2.10b, ≈$7,750) is ≈ $2,649 — about 52 % of the cheapest option.** But the spread in *marginal* cost is
**26×** ($90 vs $2,350). **The platform compresses everything.** That is the single most useful fact in this
section: archetype choice is a modest lever on money and an enormous lever on hours.

## 3.2 Ranked by TOTAL STUDENT-HOURS, both robots (fabrication + assembly + software)

| Rank | Archetype | § | **Fab + assy (2 robots)** | **Software (2 robots)** | **TOTAL hours** | Weeks at 30 h/wk | Layer? |
|---:|---|---|---:|---:|---:|---:|---|
| 1 | **Pusher / plow** | 2.6 | 67 h | 7 h | ⭐⭐ **74 h** | **2.5** | ✅ |
| 2 | **Human-player-feed specialist** | 2.9 | 67 h | 11 h | ⭐ **78 h** | 2.6 | ✅ |
| 3 | **Dedicated defender** | 2.7 | 72 h | 7 h | **79 h** | 2.6 | ⚠ |
| 4 | **Randomized-target responder** | 2.11 | 50 h | 32 h | **82 h** | 2.7 | 🔷 |
| 5 | **Climber / hanger** | 2.5 | 83 h | 11 h | **94 h** | 3.1 | 🔷 |
| 6 | **Ramp / deposit bot** | 2.4 | 82 h | 13 h | ⭐ **95 h** | 3.2 | ✅ |
| 7 | **Specialist (single-task)** | 2.10a | 80 h | 16 h | **96 h** | 3.2 | ✅ |
| 8 | **Ground-intake cycler** | 2.1 | 96 h | 26 h | **122 h** | 4.1 | ✅ |
| 8= | **Park-and-AUTO specialist** | 2.8 | 53 h | 69 h | **122 h** | 4.1 | 🔷 |
| 10 | **Stacker / builder** | 2.2 | 127 h | 42 h | 🔴 **169 h** | 5.6 | ✅ |
| 11 | **Reliability-first generalist** ⭐ | 2.10c | 107 h | 69 h | **176 h** | 5.9 | ✅ |
| 12 | **Launcher / shooter** | 2.3 | 117 h | 🔴 75 h | 🔴 **192 h** | 6.4 | ✅ |
| 13 | **Generalist** | 2.10b | 🔴 185 h | 60 h | ⛔ **245 h** | **8.2** | ✅ |

> **[D] The hours ranking is NOT the cost ranking, and where they disagree is where the real decision lives.**
> The launcher (§2.3) is *cheaper* than the cycler (§2.1) by $4 and *more expensive in hours* by 70 — because
> **tuning, not parts, is what a launcher costs.** A program short of money and long on students should look
> at the launcher differently than a program long on money and short on students. **This one has ~15 students
> across two teams and limited mentor hours, so it is short on both — and hours is the binding constraint.**

## 3.3 The hours-per-dollar view — where the money actually goes

| Archetype | § | 2-robot $ | 2-robot hours | **$ per hour of build** | [J] Reading |
|---|---|---:|---:|---:|---|
| Generalist | 2.10b | $7,750 | 245 h | $32/h | ⛔ Expensive in *both* budgets. No trade-off, just worse |
| Stacker / builder | 2.2 | $7,087 | 169 h | $42/h | 🔴 Expensive in both |
| Launcher | 2.3 | $6,189 | 192 h | $32/h | 🔴 Cheap parts, expensive hours |
| Reliability-first generalist ⭐ | 2.10c | $6,205 | 176 h | $35/h | ⭐ Hours are mostly AUTO software, which duplicates at ~5 % |
| Ground-intake cycler | 2.1 | $6,193 | 122 h | $51/h | ⭐ The best hours-to-ceiling ratio of any 5-ceiling archetype |
| Ramp / deposit | 2.4 | $5,630 | 95 h | $59/h | ⭐ Cheap in hours; the money is nearly all platform |
| Specialist | 2.10a | $5,440 | 96 h | $57/h | ⭐ |
| Human-player-feed | 2.9 | $5,263 | 78 h | $67/h | ⭐ Game-dependent, but superb when it applies |
| Pusher / plow | 2.6 | $5,101 | 74 h | $69/h | ⭐⭐ The floor of the whole table |

## 3.4 Ranked by CHEAP-VERSION two-robot marginal cost

**[J] This is the table to use when the question is "what can we afford *this month*?"** It strips the
platform out and shows only what each archetype adds.

| Rank | Archetype | § | **Cheap 2-robot marginal** | **Competitive 2-robot marginal** | **Δ** | [J] Is the delta worth it? |
|---:|---|---|---:|---:|---:|---|
| 1 | Park-and-AUTO | 2.8 | **$6** | $384 | +$378 | ⚠ Only on the A robot, only if AUTO is the strategy |
| 2 | Randomized-target | 2.11 | **$10** | $388 | +$378 | ⚠ Spend the hours on a fallback path first |
| 3 | Pusher / plow | 2.6 | **$60** | $130 | +$70 | ⭐ Cheapest upgrade in the file, but lowest ceiling |
| 4 | Human-player-feed | 2.9 | **$120** | $264 | +$144 | ⭐ Yes — removes a whole class of hand-off losses |
| 5 | Dedicated defender | 2.7 | **$120** | $840 | +$720 | ⛔ **No.** The only outright "do not upgrade" in the file |
| 6 | Climber | 2.5 | **$260** | $410 | +$150 | ⭐ Yes — buys a deterministic engagement under time pressure |
| 7 | Launcher | 2.3 | **$364** | $814 | +$450 | ⭐ Yes for the feed; the 82 mm flywheel is the best $3 here |
| 8 | Ramp / deposit | 2.4 | **$400** | $584 | +$184 | ⭐⭐ **Smallest delta of any scoring archetype.** Yes |
| 9 | Ground-intake cycler | 2.1 | **$578** | $1,004 | +$426 | 🕐 **Only if the high goal pays > 2× the low goal** |
| 10 | Stacker / builder | 2.2 | **$1,038** | $1,826 | +$788 | 🕐 The VFB yes; the 4th slide stage probably not |
| 11 | Generalist | 2.10b | — | $2,350 | — | ⛔ There is no cheap version. The cheap version is §2.10a |

## 3.5 The A-team / B-team assignment, priced

**[J] The recommended two-robot program shape, with the actual money attached.** Cross-reference
`ROBOT-ARCHETYPE-LIBRARY.md` §5 and `playbook/TWO-ROBOT-PROGRAM.md`.

| | **A robot** | **B robot** | **Program** |
|---|---|---|---|
| Archetype | §2.10c reliability-first generalist (= §2.1 competitive + §2.8) | §2.4 ramp/deposit competitive, sharing §2.1's intake CAD | |
| Per-robot platform | ≈$1,940 | ≈$1,940 | ≈$3,880 |
| Marginal COTS | ≈$505 | ≈$292 | ≈$797 |
| Printed/sheet material | ≈$38 | ≈$26 | ≈$64 |
| Shared platform + spares + tooling | — | — | ≈$1,054–$1,304 |
| **TOTAL** | **≈$2,483** | **≈$2,258** | ⭐ **≈ $5,795–$6,045** |
| Fabrication hours | ≈79 h | ≈62 h, of which **≈19 h is shared intake CAD already paid** | **≈ 122 h** |
| Software hours | ≈65 h | **≈4 h** (config file only) | **≈ 69 h** |
| R503 | 6 M / 3 S | 6 M / 2 S | ⭐ Both hold ≥2 motors in reserve |

> ⭐ **[D] Why this pairing and not two identical robots:** the B robot reuses the A robot's intake CAD, its
> entire software stack and its odometry configuration, so its *marginal* cost to the program is
> **≈ $2,258 and ≈ 47 genuinely new fabrication hours**. Two identical §2.10c robots would cost ≈ $370 more
> and ≈ 30 more hours for a capability the B team is less likely to operate well.
>
> ⚠ **[C] Both teams are separately registered, so both get their own storefront Electronics Kit and Driver
> Kit at the one-per-team limit.** That is **$610 of discount per team** and it is the largest single
> financial argument for the two-team structure.

## 3.6 Kickoff-day costing procedure — 20 minutes per proposal

**2026-09-12.** Do this, in this order, for each design proposal the review produces.

| Step | Action | Time | Output |
|---|---|---|---|
| 1 | Match the proposal to the closest §2 archetype (or the closest **two**, if it is a hybrid) | 2 min | Archetype ID |
| 2 | Copy that §2.x.1 mechanism-breakdown table; strike mechanisms the game does not need; add any the game demands | 5 min | Mechanism list |
| 3 | Fill in the §1.3 **R503 budget block**. ⛔ **If it exceeds 8+8, stop. The design is illegal, not expensive** | 3 min | Motor/servo count |
| 4 | Copy the §2.x BUY table; substitute element-size-dependent SKUs; keep every confidence tag | 4 min | Marginal COTS |
| 5 | Add §1's **$4,494** two-robot platform + the shared pool | 1 min | Two-robot total |
| 6 | Copy the §2.x.5 rollup; adjust hours for any added or removed mechanism | 3 min | Student-hours |
| 7 | Read the §2.x.7 duplicability verdict aloud and apply its 3–4 changes to the proposal | 2 min | Revised design |
| 8 | Compare against §3.1 and §3.2. **If it is worse than §2.10c on both axes, say so in writing** | — | Recommendation |

**[J] The three questions to ask about any proposal that comes back over ≈ $6,500 or ≈ 180 hours for two
robots:**
1. Which mechanism can be replaced by its **cheap** version (§2.x.8) without losing the scoring identity?
2. Which hand-fitted part can become a **printed** part (ratio 1.0 → 0.2)?
3. **Is this actually a generalist wearing a specialist's name?** Price it against §2.10b and find out.

---

# 4. VERIFICATION LOG — every page loaded in this session (2026-08-22)

**[J] This log exists so a future reader can tell the difference between what I read and what I inherited.**
Everything tagged **VERIFIED** in this file traces to a row below. Anything tagged **PHASE-B** traces to a
sibling catalog's own log, not to mine. Anything not on either list was not read, and is tagged accordingly.

| # | URL | What it yielded | Result |
|---:|---|---|---|
| 1 | [gobilda.com/strafer-chassis-kit-104mm-gripforce-mecanum-wheels/](https://www.gobilda.com/strafer-chassis-kit-104mm-gripforce-mecanum-wheels/) | **`3209-0001-0007`, $699.99, In Stock**; 4× 5203 312 RPM motors, 104 mm GripForce mecanum, 1120-series U-channel, 5.57 ft/s theoretical | ✅ §1.1 headline |
| 2 | [revrobotics.com/rev-31-1595/](https://www.revrobotics.com/rev-31-1595/) | Control Hub **$375.00, "In Stock & Ready To Ship!"**; **4 motor / 6 servo / 8 DIO / 4 analog / 4 I²C** ports | ✅ §1.1, §1.3 |
| 3 | [revrobotics.com/rev-31-1596/](https://www.revrobotics.com/rev-31-1596/) | Driver Hub **$275.00, In Stock** | ✅ §1.1 — and the reason the storefront Driver Kit at $295 is a large saving |
| 4 | [revrobotics.com/rev-31-1302/](https://www.revrobotics.com/rev-31-1302/) | 12V Slim Battery **$60.00, In Stock**, "10-cell, 12V 3000 mAh, 10C" | ⚠ **Chemistry NOT stated on the page.** R601 requires NiMH → **NEEDS-SKU-CHECK**, logged in §5 |
| 5 | [revrobotics.com/ftc/electronics/](https://www.revrobotics.com/ftc/electronics/) | `REV-45-1901` **$220**, `REV-45-1885` **$180**, `REV-31-3332` **$38**, `REV-11-1855` **$90**, `REV-31-2983` **$26**, `REV-31-1876` **$21.75**, `REV-35-1906` **$750**, `REV-35-2709` **$650**, `REV-31-1595-RFB` **$165**, `REV-31-1596-RFB` **$125**, `REV-31-2010-PK4` $14.75, `REV-31-1807` $7.75, `REV-25-1870` $4.00 | ✅ §1.1, §1.5, §2.8 |
| 6 | [revrobotics.com/ftc/motion/](https://www.revrobotics.com/ftc/motion/) | **`REV-45-2470` $520.00**, `REV-41-2080` $45.00, `REV-41-1683` $4.50, DUO Flap Wheels **$17.50**, GT2 belts $5.00–$12.50, #25 sprockets $5.00–$12.50, 5 mm hex shafts $12.50–$23.25 | ✅ §1.1 budget alternative |
| 7 | [revrobotics.com/duo-compliant-wheels/](https://www.revrobotics.com/duo-compliant-wheels/) | **`REV-41-2034-PK4` (40A) $19.50** and **`REV-41-2035-PK4` (30A) $19.50**, both 2 in / 5 mm hex / 4-pack, **In Stock** | ✅ §2.1, §2.3, §2.6, §2.9 |
| 8 | [gobilda.com/linear-slides/](https://www.gobilda.com/linear-slides/) | **`3210-0003-0002` $159.99**, **`3210-0003-0004` $229.99**, **`3210-0004-0004` $219.99**, `2500-0014-0336` $19.99, `2500-0010-0240` $16.99, `2501-0001-0001` $5.99, `2501-0001-0002` $8.99 | ✅ §2.1, §2.2 |
| 9 | [gobilda.com/2-stage-viper-slide-kit-belt-driven-336mm-slides/](https://www.gobilda.com/2-stage-viper-slide-kit-belt-driven-336mm-slides/) | `3210-0003-0002` **$159.99, In stock**; **384 mm retracted → 874 mm extended, 490 mm stroke**; includes `1201-0043-0005` quad-block mount + 8 mm REX Sonic hub; **motor sold separately** | ✅ §2.2 |
| 10 | [gobilda.com/yellow-jacket-planetary-gear-motors/](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | **5202 / 5203 $54.99, 5204 $56.99**; example `5203-2402-0019` 312 RPM / 24.3 kg·cm | ✅ every motor row |
| 11 | [gobilda.com/standard-size-servos/](https://www.gobilda.com/standard-size-servos/) | **`2000-0025-0002/-0003/-0004` $36.99**, `2000-0025-0502/-0503/-0504` $49.99, **`2004-0025-0002` Axon MAX MK2 $99.99 In stock**, `2004-0025-0001` Axon MINI **out of stock**, `2002-0180-0002/-0003` Proton $17.99 | ✅ every servo row. ⚠ **No numerical torque values printed — R502's 8 W check cannot be done from this page** |
| 12 | [gobilda.com/odometry/](https://www.gobilda.com/odometry/) | **`3110-0002-0002` $79.99**, **`3203-3110-0002` $279.99**, `3203-3110-0001` $279.99, **`3110-0001-0002` $99.99**, `3110-0001-0001` $99.99 | ✅ §1.1, §2.8 |
| 13 | [gobilda.com/pinpoint-v2-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/](https://www.gobilda.com/pinpoint-v2-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/) | `3110-0002-0002` **$79.99, In Stock** | ✅ §1.1 |
| 14 | [gobilda.com/intake-wheels](https://www.gobilda.com/intake-wheels) | **`3618-4008-0016` / `3618-4008-0012` 8-pack $12.99**; Boot-Wheels `3615-4008-0048/-0072/-0096` $4.99/$6.99/$8.99; Gecko `3613-4008-0032/-0048`, `3613-0014-0072/-0096` $6.99–$9.99. All 30A | ✅ §2.1, §2.4 |
| 15 | [gobilda.com/flywheels/](https://www.gobilda.com/flywheels/) | **`3628-0014-0060`** 60 mm / 115 g / **551 g·cm² / $12.99**; **`3628-0032-0082`** 82 mm / 152 g / **1651 g·cm² / $15.99** | ✅ §2.3 — the 3× inertia claim is arithmetic on these two rows |
| 16 | [gobilda.com/wheels-tires/](https://www.gobilda.com/wheels-tires/) | 14 sub-categories incl. Hogback Traction, Rhino, Intake Wheels, Flywheels | ⚠ **Navigation only — FAMILY-ONLY.** §2.7's traction-wheel row is tagged accordingly |
| 17 | [gobilda.com/u-channel/](https://www.gobilda.com/u-channel/) | Families **1120 / 1121 / 1143 / 1122** confirmed | ⚠ **No SKUs, no prices — FAMILY-ONLY.** §1.1 structure row tagged accordingly |
| 18 | [gobilda.com/servos/](https://www.gobilda.com/servos/) | 9 sub-category names only | ⚠ Navigation only; superseded by #11 |
| 19 | [limelightvision.io/products/limelight-3a](https://limelightvision.io/products/limelight-3a) | **$189.00** sale price; **stock status not stated on the page** | ✅ price; ⚠ stock unverified |
| 20 | [info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf) (fetched, then extracted locally with `pdftotext -layout`) | **Revision 25-26.4, Feb 18 2026.** Registration **$325**. **Driver Kit $285** (Driver Hub ×1, FTC-legal gamepad ×2, FTC-legal webcam). **Electronics Kit $325** (Control Hub, Smart Robot Servo, Switch Cable & Bracket, Color Sensor V3, Touch Sensor, Resistive Grounding Strap, Cable Pack, M3 hardware). **Build Kit $650** (REV FTC Competition Set V3.1). **All three: "Limit one per registered team per season."** | ✅ **The primary source for §1.1's storefront rows.** ⚠ **This is the 2025-26 DECODE sheet — the 2026-27 BIOBUZZ sheet is not yet published. Prices are [H] HISTORICAL** |
| 21 | Local: `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` | Grepped and read verbatim: **R102** (line 169), **R104** (197), **R105** (211), **R301** (301), **R303** (328), **R401** (399), **R503** (591), **R601** (650), **R701** (911), **R801** (1119), and R501's *"These motors do not count toward the limit in R503"* (519, 522) | ✅ **Every [C] legality claim in this file traces to a grep of this file** |
| ⛔ | `revrobotics.com/ftc/motion/wheels/`, `revrobotics.com/rev-41-2034/`, `revrobotics.com/rev-31-1299/`, `revrobotics.com/ftc/electronics/power/`, `gobilda.com/compliant-wheels/` | **HTTP 404 ×5** | ⛔ Dead URLs — **do not cite.** Charger row in §1.1 is FAMILY-ONLY as a direct result |

**Vendor status.** **Official FIRST suppliers:** AndyMark, Studica, Pitsco (the storefront operator).
**General suppliers used heavily here:** goBILDA, REV Robotics, Limelight Vision.
⚠ **[J] AndyMark and Studica were not fetched this session, and Phase A/B record Studica returning HTTP 403
and AndyMark rendering no product data.** Nothing in **[C] R301/R302/R303** cares which storefront a legal
part came from — but a team ordering through official-supplier purchase orders should browse those two
catalogues manually, because this file does not cover them.

---

# 5. NEEDS-SKU-CHECK / UNVERIFIED REGISTER

**[J] Every row here is a place where an AI would be tempted to invent a plausible answer. I did not.
Resolve each by loading the page or calling the vendor before it goes on a purchase order.**

| # | Item | What is unresolved | Where it bites | Priority |
|---:|---|---|---|---|
| 1 | **REV 12V Slim Battery `REV-31-1302`** | Product page states "10-cell, 12V 3000 mAh" but **does not state NiMH chemistry**. **[C] R601** requires *"1 and only 1 approved 12V NiMH"* main battery | Every archetype. **An illegal battery fails inspection for both robots** | 🔴 **HIGHEST — resolve first** |
| 2 | ~~**Battery charger SKU**~~ **RESOLVED 2026-08-22 (fact-check pass).** `REV-31-1299` is confirmed on `revrobotics.com/ftc/electronics/` as **"12V Slim Battery Accessories, MSRP $6.00–$39.50"** — a *family*, not one SKU. **Buy a specific charger instead: goBILDA `3101-0012-0001` 12V Battery Charger (NiCad/NiMH, XT30) $14.99 — VERIFIED** on `gobilda.com/battery-chargers/`; AndyMark `am-5473` $16.00 is the second source | §1.1 shared platform | 🟢 **Closed** — order the goBILDA charger |
| 3 | ~~**Limelight 3A in Table 12-9**~~ **RESOLVED 2026-08-22 (fact-check pass).** Table 12-9 was re-grepped directly from `sections/12_RobotConstruction_R_p64-88.txt`: it contains **exactly one row — "Limelight Vision Limelight 3A / LL_3A"**. The 3A **is** listed and **is** reprogrammable under **[C] R702**. ⛔ The **3G remains prohibited** (R702 Example 6, which names *"The OpenMV Cam, Luxonis OAK-1, and LimeLight Vision Limelight 3G"*). Price **$189.00 re-VERIFIED** this session | §2.3, §2.8, §2.11 — a **$378** two-robot purchase | 🟢 **Closed** — legal to buy; still a *want*, not a need |
| 4 | **Servo power ratings vs R502's 8 W cap** | goBILDA's standard-servo page prints **no numerical torque or speed values**. **[C] R502** requires `0.25 × stall torque (N·m) × no-load speed (rad/s) ≤ 8 W` | §2.2's Axon MAX `2004-0025-0002` row especially | 🔴 High — this is a *legality* gap, not a price gap |
| 5 | goBILDA U-channel SKUs and prices | Category page confirms families 1120/1121/1143/1122 but prints **no SKUs, no prices** | §1.1's ≈$120–$180/robot structure allowance | 🟡 Medium |
| 6 | goBILDA traction wheels (Hogback, Rhino) | Categories confirmed via `/wheels-tires/`; **per-SKU prices verified only in `DRIVETRAIN-AND-ODOMETRY.md`, not by me** | §2.7's ≈$60–$90/robot row | 🟡 Medium |
| 7 | Ratchet / one-way bearing SKU | **[C] R303.H** confirms *ratcheting devices* are legal COTS. **No specific FTC-vendor SKU verified in any session** | §2.5's climb latch — the row that keeps a motor from stalling at 0:00 | 🟡 Medium |
| 8 | Fastener / bearing / shaft allowances | Every "≈$45–$140 allowance" row is a **FAMILY-ONLY estimate**, not a priced basket | Every archetype total, ±5 % | 🟡 Medium |
| 9 | Storefront 2026-27 prices | The only storefront sheet published is **Rev 25-26.4 (DECODE)**. BIOBUZZ prices are unknown | §1.1's storefront rows, now carried at the 2026-27 website prices ($350 + $295), i.e. **$1,290 of a two-robot budget** | 🟡 Medium — re-check the week of kickoff |
| 10 | REV Expansion Hub `REV-31-1153` availability | Phase B recorded it **out of stock two days running (2026-08-22)** | Only matters if a design needs a second hub — **§1.3 says design so it does not** | 🟢 Low |
| 11 | AndyMark and Studica catalogues | **Not fetched this session**; Phase A/B record 403 and no-render | Alternative sourcing for every mechanical row | 🟢 Low, but worth a manual browse |
| 12 | **R105 expansion numbers** | **[C] R105 exists and is final in text, but its numeric allowance is game-dependent** | 🕐 Every row marked **EXPANSION-GATED**: §2.1 M4, §2.2 M3, §2.5 M1, §2.6 M2 | 🔴 **Deferred to kickoff by design — flag it, do not resolve it early** |

---

## Closing note

**[J] The single sentence this file exists to make sayable on kickoff day:**

> *"That proposal is a §2.2 stacker with a §2.5 climb bolted on. That is **8 motors with zero reserve**,
> **≈$7,100 for two robots**, and **≈170 student-hours**. The §2.10c shape is **$900 cheaper**, **60 hours
> lighter**, and holds **two motors in reserve**. Here is what we would have to believe about the scoring
> table for the stacker to be worth it."*

Everything above §3 is the machinery for producing that sentence in twenty minutes instead of two weeks.

**Three things to do before 2026-09-12, all of which are legal now under [C] R304 and independent of the
game:**
1. **Order the two chassis kits, the two storefront kits and the batteries in ONE order.** §1.1. Lead time is
   the resource this program is shortest on after student-hours.
2. **Build the chassis assembly fixture, the bend jig and the drill jigs.** §1.2. ≈4 one-off hours that
   change the duplication ratio of every part built afterwards.
3. **Cut and mount the four ROBOT SIGNS.** **[C] R401**. It is the only inspection item that can be
   *finished*, not merely started, before the game is published.

**Resolve register item #1 (the battery chemistry) this week.** Everything else in §5 can wait for kickoff;
that one cannot, because it is the difference between two legal robots and two robots that fail inspection.
