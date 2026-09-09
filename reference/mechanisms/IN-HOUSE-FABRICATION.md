# IN-HOUSE FABRICATION — what to MAKE rather than BUY, and the shop that makes it

### The other half of every BOM: the buy-vs-fabricate decision framework, 3D printing for FTC, sheet and stock work with hand tools, the tiered tool list, fastener discipline, and the student-hour numbers that let a BOM carry a LABOR column

---

**Status:** written 2026-08-22, **21 days before Kickoff (2026-09-12)**.
**Legality source of truth:** BIOBUZZ V0 `Section 12 ROBOT Construction` — **FINAL, not a placeholder**.
Every legality claim cites a rule ID grepped from
`manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`.
**Game source of truth:** does not exist yet. Sections 8, 9, 10, 11, 13 and 15 are V0 PLACEHOLDERS.
**Calibration target:** ~15 students, TWO registered FTC teams (A + B), **two robots**, modest budget,
**3D printers and hand tools only — no CNC mill**, limited mentor hours.

**Read first, do not duplicate:**
`reference/VENDOR-ECOSYSTEMS.md` (who to buy from, the interoperability map, the procurement calendar,
§6.7 "What you FABRICATE, not buy") ·
`reference/LEGAL-PARTS-CONSTRAINTS.md` (the purchasing envelope, §8 FABRICATION vs COTS, Tables 12-1/12-2,
the 8+8 actuator budget).
This file cross-references both rather than repeating them. Where they name a family, this file tells you
whether to make it instead, with what tool, and in how many student-hours.

**Sibling mechanism files:** `DRIVETRAIN-AND-ODOMETRY.md` · `EXTENSION-ARMS-LIFTS.md` ·
`INTAKE-AND-MANIPULATION.md` · `LAUNCHERS-AND-FEEDING.md` · `ELECTRONICS-AND-SENSING.md`.
Each carries a per-mechanism FABRICATE/ASSEMBLE IN-HOUSE subsection. **This file is the shared back-end for
all of them**: the capability, the material, the tool, the jig, and the hours.

---

## Contents

- [0. How to read this file](#0-how-to-read-this-file)
- [1. The legality envelope for anything you make yourself](#1-the-legality-envelope-for-anything-you-make-yourself)
- [2. THE BUY-VS-FABRICATE DECISION FRAMEWORK](#2-the-buy-vs-fabricate-decision-framework)
- [3. CAPABILITY F-1 — 3D PRINTING](#3-capability-f-1--3d-printing)
- [4. CAPABILITY F-2 — SHEET AND PLATE WORK WITH HAND TOOLS](#4-capability-f-2--sheet-and-plate-work-with-hand-tools)
- [5. CAPABILITY F-3 — CUTTING STOCK: EXTRUSION, CHANNEL, TUBE, SHAFT](#5-capability-f-3--cutting-stock-extrusion-channel-tube-shaft)
- [6. THE TOOL LIST BY TIER](#6-the-tool-list-by-tier)
- [7. FASTENER AND HARDWARE DISCIPLINE](#7-fastener-and-hardware-discipline)
- [8. STUDENT-HOUR ESTIMATES — the LABOR column for every BOM](#8-student-hour-estimates--the-labor-column-for-every-bom)
- [9. DESIGN-FOR-FABRICATION RULES OF THUMB](#9-design-for-fabrication-rules-of-thumb)
- [10. Shop safety, and the R-rules that are really fabrication-quality rules](#10-shop-safety-and-the-r-rules-that-are-really-fabrication-quality-rules)
- [11. Kickoff-day application procedure](#11-kickoff-day-application-procedure)
- [12. Open questions — the NEEDS-SKU-CHECK / UNVERIFIED register](#12-open-questions--the-needs-sku-check--unverified-register)
- [13. Verification log — every URL loaded in this session](#13-verification-log--every-url-loaded-in-this-session)

---

## 0. How to read this file

### 0.1 Claim labels (matched to `LEGAL-PARTS-CONSTRAINTS.md` §0.1)

| Label | Meaning |
|---|---|
| **[C]** CONFIRMED-BIOBUZZ | Text present in the BIOBUZZ V0 manual's already-final sections (Section 12 unless noted), grepped this session |
| **[H]** HISTORICAL | From a prior season or a prior-season published document. A pattern, never a BIOBUZZ fact |
| **[D]** DERIVED | Arithmetic on stated values. Inputs cited, conclusion is mine |
| **[J]** JUDGMENT | Engineering opinion calibrated to *this* two-team, no-mill, low-mentor-hour program. Not a fact |
| **UNVERIFIED** | Could not be established. Treat as unknown |

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

| Tag | What it guarantees |
|---|---|
| **VERIFIED** | I loaded that vendor page **in this session** and read the name, SKU and price off it |
| **FAMILY-ONLY** | I verified the *product family* and a *category URL*, but **not** the specific SKU or price. Marked **NEEDS-SKU-CHECK** |
| **SEARCH-SNIPPET** | Name/price came from a search-result summary, **not** a loaded product page. Weaker than VERIFIED — treat the price as indicative only |
| **UNVERIFIED** | Named from context only. Do not order against this row without checking |

**Cross-referenced rows:** where a SKU or price was verified by a *sibling document* rather than by me, the
row says so explicitly (e.g. *"VERIFIED in `VENDOR-ECOSYSTEMS.md` §6.4, not re-loaded here"*). That is a
weaker guarantee than a bare **VERIFIED** in this file, and it is labelled that way on purpose. **§13 lists
every URL I personally loaded; if a SKU is not traceable to that list or to a named sibling section, it does
not appear in this document.**

**Every price is "as of 2026-08-22", US list, pre-discount, pre-tax, pre-shipping, and is marked
VERIFY-BEFORE-ORDER.** Vendors reprice at season turnover and again in the Sept–Oct demand spike
(`VENDOR-ECOSYSTEMS.md` §5.2).

**Sites that blocked fetching this session — stated explicitly so you know why some rows are weak:**
`store.bambulab.com` (HTTP 402), `bambulab.com` (403), `tapplastics.com` (403), `homedepot.com` (403),
`onlinemetals.com` (403), `metalsdepot.com` (403), `acmeplastics.com` (403), and `harborfreight.com`
product pages after the first two loads (403 rate-limit). **No aluminium sheet or bar price in this file
came off a loaded page** — every aluminium raw-stock row is therefore UNVERIFIED on price, and says so.

### 0.3 Three things this file deliberately does not do

1. **It does not decide your mechanism.** Geometry is game-dependent and the game is not public. This file
   tells you what your shop can make once the mechanism is chosen.
2. **It does not re-derive the purchasing envelope.** `LEGAL-PARTS-CONSTRAINTS.md` owns that.
3. **It does not assume a mill, lathe, laser or waterjet.** Every technique below is achievable with a
   3D printer, a drill press, a saw and hand tools. Where a process genuinely needs a machine you do not
   have, the answer given is **buy the part**, not "borrow a mill."

---

## 1. The legality envelope for anything you make yourself

Fabrication in FTC is unusually permissive — and the few limits that exist are exactly the ones a team
discovers at inspection. All rules below are **[C] CONFIRMED-BIOBUZZ**, grepped from the V0 Section 12 text.

### 1.1 R302 — the rule that makes this whole file possible

> **R302** \**Legal COTS parts and raw materials can be modified.* "Allowed raw materials and legal COTS
> parts can be modified (drilled, cut, painted, etc.) as long as no other rules are violated."
> Raw materials refers to unfinished building stock including, but not limited to: **A. sheet stock,
> B. extruded shapes, C. metals, plastic, rubber, and wood, and D. magnets.**

**Read what that actually authorises [D]:** 3D-printed parts are "plastic"; polycarbonate sheet is "sheet
stock"; goBILDA channel and REV extrusion are "extruded shapes"; and **magnets are named outright** — which
means passive detents, alignment aids and magnetic retention cost **zero** of your 8+8 actuator budget
(R503) and are explicitly legal raw material. That is the cheapest design lever in the manual.

### 1.2 R301 / R303 / R101 — what you are *required* to build

- **R301 [C]:** "COTS MAJOR MECHANISMS purposefully designed to complete a game task are prohibited,"
  excepting **(A)** a COTS drive CHASSIS and **(B)** official FIRST **StarterBot** mechanisms. Blue box:
  a vendor selling *"build to print"* manufacturing of publicly available purpose-built solutions is
  against the spirit of the rule.
- **R303 [C]:** COTS COMPONENTS and MECHANISMS "must not exceed a single degree of mechanical freedom."
  Allowed single-DoF COTS: linear slide kit, linear actuator kit, single-speed gearbox, pulley, turntable,
  lead screw, single-DoF gripper. Exceptions: ratcheting devices, holonomic wheels, **dead-wheel odometry
  kits**, universal joints / flex couplers, ball-joint linkages / rod ends.
- **R101 [C]:** the ROBOT and its MAJOR MECHANISMS must be built by the registered team; gearbox
  assemblies, sub-mechanisms and COTS items are explicitly *not* subject to R101.

**[D] The consequence for this file:** the *integration* is always fabrication. You may buy the slide kit,
the gearbox and the single-DoF gripper — you may **not** buy the thing that ties them into a scoring
mechanism. Every design proposal will therefore always have a non-empty FABRICATE column, and the size of
that column is the real build-season schedule.

### 1.3 R304 — you may fabricate *right now*, before the game is public

> **R304** \**Custom software, designs, and parts can be reused year-to-year.* ROBOT software, designs, and
> FABRICATED ITEMS created before Kickoff are permitted.

⚠ **Extraction artifact, same as the one flagged in `LEGAL-PARTS-CONSTRAINTS.md` §8.5.** In the sectioned
`.txt` the label `R305` is interleaved *inside* R304's sentence (lines 381-382 read `R304 *Custom software,
designs, and parts can be reused year-to-year. ROBOT software, designs, and` / `R305 FABRICATED ITEMS
created before Kickoff are permitted.`). **The pre-Kickoff allowance is R304. Cite R304.**
The identical artifact occurs at **R504/R505** — the `R505` label sits inside R504's first sentence. Cite
carefully; a wrong rule ID in a design review costs credibility with an inspector.

**R305 [C]** is the separate rule: *"SCORING ELEMENTS are not allowed for ROBOT construction. Current
season SCORING ELEMENTS or replicas of SCORING ELEMENTS are not allowed to be used as part of ROBOT
construction."* Game pieces are a **practice consumable, never a BOM row.**

### 1.4 R201 / R202 / R203 / R204 — the rules that are really *fabrication-quality* rules

These are where hand-made parts fail inspection, and every one is a workmanship issue:

| Rule | The fabrication consequence [D] |
|---|---|
| **R201 [C]** — no damage, no mess. Named examples include **"components with exposed sharp edges or sharp protrusions"**, **"features with abrasive surfaces that scratch objects that rub across them"**, **"excessive use of lubricants that may spin off or drip"**, and **"any component not secured sufficiently … such that it may be released on the FIELD"** | **Deburr everything.** A saw-cut extrusion end and a drilled polycarbonate hole are both sharp until you break the edge. A coarse print surface that rubs a SCORING ELEMENT *is* an abrasive surface. Printed parts that vibrate loose are "components not secured sufficiently" |
| **R202 [C]** — safety and fair play. Bans hazardous materials (**"liquid mercury or lead"**), **"animal based materials"**, flames/pyrotechnics, and **"devices or conditions that pose an unnecessary risk of entanglement"** | No lead ballast. No leather/fur/bone. **No exposed cord loops, zip-tie tail forests, or open lattice that a hand or another ROBOT can hook** — entanglement is a fabrication-detail failure, not a design failure |
| **R203 [C]** — the ROBOT must allow removal of SCORING ELEMENTS, and removal of the ROBOT from FIELD elements, **while powered off** | A fabricated gripper that only opens under power fails this. Design in a manual release, a back-drivable jaw, or an accessible spring |
| **R204 [C]** — no mechanism designed to increase downforce by grabbing FIELD surfaces or by generated airflow | Suction cups and skirts are out. So is a fabricated "sticky" tread compound intended to grab TILE |

### 1.5 R504/R505, R506, R601, R801 — the four hard "do not modify / do not make" walls

- **R504 [C]** — *"The integral mechanical and electrical system of any motor or servo must not be
  modified."* Exceptions that matter to a shop: **(A) the mounting brackets and/or output shaft/interface
  (including pinion gears) may be modified** to facilitate the physical connection to the ROBOT;
  **(B)** leads may be trimmed and connectors/splices added; **(C)** servos may be modified *as specified by
  the manufacturer* (soft limits, continuous-rotation conversion); **(D)** labels may be applied if they do
  not obstruct device markings; **(E)** insulation may be applied to terminals; **(F)** repairs that leave
  original performance unchanged; **(G)** manufacturer-recommended maintenance.
  **[D] So: you may cut a motor output shaft or swap its pinion. You may not open the gearbox, re-wind it,
  or drill the case.** Continuous-rotation servo conversion is legal **only where the manufacturer specifies
  it** — a hand-hacked potentiometer-removal on a servo that does not document it is a rules risk.
- **R505 [C]** — all actuator control signals must originate from an approved power-regulating device
  (Table 12-3). **Nothing you fabricate may drive an actuator.**
- **R506 [C]** — *"The use of relays, electromagnets, and electrical solenoid actuators is prohibited."*
  A hand-wound electromagnet is not a clever workaround; it is explicitly banned. *(Permanent magnets are
  a different thing entirely and are explicitly legal raw material under R302(D).)*
- **R601 [C]** — exactly one approved 12 V NiMH main battery, unaltered, except that the fuse may be
  replaced with a COTS in-line **20 A ATM mini blade fuse**. **Never fabricate anything battery-side.**
- **R801 [C]** — no pneumatic actuators, no high-speed blowers, no vacuums; **"ROBOTS may not generate
  pressure or vacuum"**; only **sealed COTS closed-air systems pre-charged by the manufacturer (gas
  shocks, gas springs, dampers)** are permitted. **[D] Do not fabricate a bellows, a syringe actuator, a
  shop-vac intake, or a blower hood.** Coil springs, constant-force springs and surgical tubing remain
  fully available and unrestricted.

### 1.6 The ROBOT SIGN — the one fabricated part that is 100% game-independent, and the one teams forget

**R401 [C]:** minimum **two** ROBOT SIGNS per ROBOT, in ≥2 separate locations, on **opposite or adjacent
surfaces, 90 degrees apart**; each must **(A) be made of a robust material, (B) minimally be 6.5 in.
(16.5 cm) wide, (C) minimally be 2.5 in. (6.4 cm) tall, (D) be supported by the structure/frame of the
ROBOT.** Intent: legible from **12 ft (3.65 m)**.
**R402 [C]:** a solid red or blue **opaque** rectangle ≥ 6.5 × 2.5 in. (16.50 × 6.35 cm); **cannot be
powered** to illuminate/reveal ALLIANCE colour; reversible or configurable signs must not let the opposite
colour show to FIELD STAFF. Permitted extra visible markings include **"small amounts of hook-and-loop
tape, hard fasteners, or functional equivalents."**
**R403 [C]:** **solid opaque white** Arabic numerals **≈2.25 in. (5.70 cm) tall**, with ≥ **0.25 in.
(0.60 cm)** of background around them, **not vertically stacked**, robust materials, **not powered**.
Edge-lit engraved plastic and LED number displays are named as prohibited.

🕐 **[J] Four signs (two robots × two signs), in two ALLIANCE colours each, is a 90-minute job in August and
a disaster on a Saturday morning in November.** Print the official FIRST template, laminate or clear-coat,
bond to 1 mm polycarbonate (REV `REV-41-3049-PK5`, §4.1) or a 2 mm printed backer, mount with hook-and-loop
per R402(B). **Make eight and keep four as spares.**

---

## 2. THE BUY-VS-FABRICATE DECISION FRAMEWORK

### 2.1 The decision in one table

**[J] Run every candidate part through this. It resolves ~90% of cases in under a minute.**

| If the part is… | Then… | Because |
|---|---|---|
| A **bearing, gear, sprocket, pulley, belt, chain, shaft, or screw** | **BUY. Always. No exceptions.** | These are precision, heat-treated or ground parts. Nothing in a hand-tool shop can make them to tolerance, and a bad one destroys the parts around it |
| A **structural member in the main load path** (chassis rail, lift tower, arm spine) | **BUY the extrusion/channel; FABRICATE only the length cut** | Extruded aluminium at $5–$50/piece beats anything you can build up, and R302(B) explicitly blesses cutting extruded shapes |
| A **motor, servo, hub, encoder, or anything with a datasheet** | **BUY**, and note R504's modification limits | Illegal to modify internally; economically absurd to reproduce |
| A **bracket, mount, spacer, standoff, or adapter whose geometry is standard** | **BUY** if it exists in the catalogue at < ~$8 | goBILDA/REV bracket geometry is already on-pattern. A printed copy costs more student-hours than $8 buys |
| A **bracket/mount/adapter whose geometry is NOT in any catalogue** | **FABRICATE — 3D print** | This is the single most common fabrication job in FTC. Custom geometry is exactly what printing is for |
| A **roller, hub, guide, hood, funnel, deflector, chute, or hopper** | **FABRICATE — 3D print (rigid) or bend polycarbonate (large area)** | Game-specific geometry; no catalogue part can exist for it |
| A **gripper jaw, finger, or compliant contact surface** | **FABRICATE — print rigid + TPU** | R301 makes a purpose-built COTS version illegal anyway; R303 caps COTS at single-DoF |
| A **guard, shield, cover, or large flat panel** | **FABRICATE — cut polycarbonate sheet** | Cheap, fast, hand-tool friendly, and lighter than a printed panel of equal area |
| A **complete drive chassis** | **BUY is explicitly legal (R301.A)** — but see §2.3 | The one COTS MAJOR MECHANISM exception in the rules |
| A **gearbox** (single-speed) | **BUY (R303.C)** | Gear cutting is not a hand-tool operation. This is the clearest false economy in the whole file |
| Anything requiring **±0.05 mm on a mating surface** | **BUY**, or **redesign so it doesn't** | You have no mill. Design the tolerance out |
| Anything you would have to make **by hand-fitting** | 🕐 **STOP. Redesign.** | A hand-fitted part cannot be duplicated for robot B without repeating the fitting — see §2.4 |

### 2.2 When fabricating actually wins — the five real reasons

**[J], in descending order of how often they apply to this program:**

1. **Custom geometry that no catalogue contains.** The overwhelming majority of FTC fabrication. A
   sensor bracket that straddles a specific channel at a specific offset simply is not for sale.
2. **Iteration speed.** A printed part can go design → test → revised design → test in a single evening.
   An ordered part cannot, and in a 3-month season **the number of iterations you can run is the design**.
   `VENDOR-ECOSYSTEMS.md` §5.1-5.2 documents the lead-time and stock-out risk this dodges.
3. **Lead time, especially in the Sept–Oct spike.** A stocked-out $9 bracket can hold a build for two weeks.
   Filament on the shelf never stocks out.
4. **Cost, but only in specific shapes.** Printing beats buying for **odd-length spacers, many-off small
   parts, and anything you'd otherwise buy in a 10-pack to use two of**. It does *not* beat buying for
   anything that is already a $2 catalogue item.
5. **Duplicability** — see §2.4. This is the reason that matters most here and it is usually stated last.

### 2.3 When fabricating is a false economy — name these out loud in design review

**[J] The five traps, with the honest reason:**

| Trap | Why it fails | What to do instead |
|---|---|---|
| **Printing gears** | Printed spur gears in PLA/PETG strip under FTC motor torque; the tooth root is a layer boundary in exactly the wrong direction. Even printed in nylon-CF, backlash and wear are far worse than a $3 COTS gear | Buy the gearbox (R303.C) or use chain/belt |
| **Printing structural load-path members** | A printed "channel" is 3–10× less stiff than the extrusion it replaces, at similar mass and 4 hours of print time | Buy channel/extrusion. Cut it to length (R302.B) |
| **Hand-machining a precision part "just this once"** | It works, on robot A. Robot B then needs the same hours from the same one person | Redesign the part to be printable or bought |
| **Building a COTS-equivalent to save money** | A 2-stage slide kit at $159.99 (goBILDA `3210-0003-0002`, VERIFIED in `VENDOR-ECOSYSTEMS.md` §6.4 on 2026-08-22 — **not re-loaded here**) is under a day of student time; building an equivalent is a week and it will bind | Buy it. R303(A) explicitly permits linear slide kits |
| **"We'll machine it at Dad's shop"** | The single-point-of-failure resource. It is not available at 9 pm on the Thursday before an event, and it produces exactly one part | Any part that cannot be remade in your own shop, at night, is a schedule risk |

### 2.4 ⭐ DUPLICABILITY — the multiplier that reorders every other factor for THIS program

**The core asymmetry [D]:**

| Fabrication method | Cost of part #1 | Cost of part #2 (robot B) | Marginal student-hours for #2 |
|---|---|---|---|
| **3D printed** | design + slice + print | **filament + machine time only** | **≈0.1–0.3 h** (start the job, come back) |
| **Cut sheet, made with a jig** | design + jig + cut + drill | material + cut + drill | ≈0.4–0.7 × the first |
| **Cut sheet, made freehand** | design + cut + drill + fit | cut + drill + **re-fit** | ≈0.9–1.0 × the first |
| **Hand-fitted / filed-to-fit metal part** | long | **just as long, and it won't match** | **≈1.0 ×, plus a mismatch you now have to code around** |

🕐 **[J] Therefore, the design rule for this program, stated as strongly as it deserves: DESIGN CUSTOM PARTS
TO BE PRINTABLE.** A printed part's second copy is essentially free in labour, which is this program's
scarcest resource. A hand-fitted part's second copy costs the same hours as the first *and* produces a robot
that behaves differently — which then costs *programming* hours to compensate, on both robots, forever.

**The corollary rules [J]:**
- **Every print job runs qty 2 the first time.** Not "we'll print the other one later." Later is November.
- **If it cannot be printed, it must be jig-made.** No jig = no second copy at acceptable cost (§4.5).
- **Duplicability is scored 1-5 in every variant table in this workspace** (`ACHIEVABILITY-FACTORS.md`).
  In this file, a 5 means "second copy is a machine job", a 1 means "second copy needs the same skilled
  person for the same hours."
- **Ban single-copy custom parts from the critical path.** If robot B cannot have it, robot A should not
  depend on it.

### 2.5 The scoring rubric — score a candidate part, get a decision

**[J] Score 1-5, sum, and read the verdict. Designed to be machine-usable in a review harness.**

| Factor | 1 point | 3 points | 5 points |
|---|---|---|---|
| **Geometry availability** | Exact part is in a catalogue | Close but needs adapters | Nothing like it exists |
| **Precision demand** | Needs ±0.05 mm mating fit | ±0.2 mm is fine | ±0.5 mm is fine |
| **Load path** | Primary structure / gear train | Secondary structure | Non-structural / guiding |
| **Duplicability if fabricated** | Hand-fitted, one-off | Jig-made | Printable, unattended |
| **Iteration expectation** | Design is frozen | 2-3 revisions likely | Many revisions expected |
| **Lead-time exposure** | In stock, ships fast | Uncertain stock | Stocked out / long lead |

| Total | Verdict [J] |
|---|---|
| **6–12** | **BUY.** Fabricating is a false economy |
| **13–20** | **Either.** Decide on whichever of cost or hours is tighter this week |
| **21–30** | **FABRICATE**, and design it printable |

### 2.6 Putting LABOR in the BOM — the column this workspace has been missing

**[J] Every BOM row this harness produces should carry three numbers, not one:**

`Approx cost (2 robots)` · `Student-hours (first article)` · `Student-hours (second copy)`

**Why the split matters [D]:** for a printed part the two numbers might be 2.5 h and 0.2 h; for a
hand-fitted part they are 2.5 h and 2.5 h. A BOM that reports only "5 h for two" hides the entire
duplicability argument. Report both, and total them separately:

```
MECHANISM LABOR BUDGET
  First-article hours  : ____  (design + build + debug robot A)
  Duplication hours    : ____  (build robot B from the proven design)
  Total student-hours  : ____
  Calendar check: at ~8 productive student-hours per build session and
  ~2 sessions/week, is Total / 16 fewer than the weeks remaining?   YES / NO
```

🕐 **[J] The calendar check is the one that kills designs.** With ~15 students across two teams, realistic
throughput is roughly **60–100 useful student-hours per week across both robots combined** — and a large
fraction of that is drive practice, programming, and portfolio work, not fabrication. Budget
**25–40 fabrication hours/week for the whole program**, and treat any mechanism needing more than ~60 total
fabrication hours (both robots) as a serious schedule risk. Use §8 for the per-part inputs.

---

## 3. CAPABILITY F-1 — 3D PRINTING

### 3.1 What it is and when a design needs it

**3D printing is this program's only real fabrication capability, and it is a genuinely good one.** With no
mill, printing is how custom geometry enters the robot at all. Under **R302 [C]** printed parts are "plastic"
raw material, freely modifiable and freely used; under **R101/R301 [C]** the custom integration parts are
things you are *required* to make anyway.

**A design needs printing whenever it needs a shape that does not exist in a catalogue.** In practice that is
every mechanism except the drivetrain, and even the drivetrain needs a Control Hub tray.

**The FTC printed-part census [J], roughly in order of how often teams print them:**

| Printed part | Typical mass | Why printed rather than bought |
|---|---|---|
| **Motor / gearbox mount plates and adapters** | 25–70 g | The interface between two ecosystems (`VENDOR-ECOSYSTEMS.md` §3) |
| **Sensor, camera and limit-switch brackets** | 8–25 g | Every sensor sits at a robot-specific angle |
| **Control Hub / Driver Hub / battery trays** | 60–150 g | The goBILDA↔REV mechanical interface |
| **Roller hubs, spacers and shaft adapters** | 10–40 g | Odd lengths; hex/REX-to-anything |
| **Intake rollers, star wheels, flails, compliant contact wheels** | 30–90 g | Pure game geometry; often TPU |
| **Gripper jaws and fingers** | 15–50 g | R301 makes a purpose-built COTS version illegal |
| **Guides, funnels, hoods, chutes, deflectors, ramps** | 40–200 g | Game geometry, curved surfaces |
| **Spacers and standoffs in non-catalogue lengths** | 1–6 g | Cheaper and faster than a 10-pack |
| **Cable clips, strain reliefs, connector retainers** | 2–8 g | Supports R606 inspectability [C] |
| **Bumper/impact pads, wheel-well liners** | 10–40 g | TPU; protects both robot and FIELD (R201) |
| **Jigs, drill guides, assembly fixtures** | 20–120 g | 🕐 Not a robot part at all — see §4.5. **The highest-leverage prints you will make** |

### 3.2 The main variants — filament materials, compared

**Ratings are 1-5, [J], calibrated to a hand-tool FTC shop. DUPLICABILITY here means "how reliably does the
second copy come out identical, unattended?"**

| Material | Complexity | Cost | Tuning burden | Reliability (as a robot part) | Duplicability | Verified price / kg |
|---|---|---|---|---|---|---|
| **PLA / PLA+** | 1 | 1 | 1 | 3 | **5** | **$18.99** Polymaker Panchroma Matte PLA · **$23.99** PolyLite PLA Pro — *VERIFIED* |
| **PETG** | 2 | 1 | 2 | **4** | **5** | **$18.99** Polymaker PETG · **$29.99** PolyMax PETG — *VERIFIED* |
| **ABS** | 4 | 1 | 4 | 3 | 3 | **$18.99** PolyLite ABS · **$24.99** Polymaker ABS Pro — *VERIFIED* |
| **ASA** | 4 | 2 | 4 | 3 | 3 | family verified at MatterHackers; **NEEDS-SKU-CHECK** |
| **TPU 95A** | 3 | 2 | 3 | **5** (impact) | 4 | **$29.99** PolyFlex TPU95 · **$39.99** TPU90 · **$49.99** TPU95-HF — *VERIFIED* |
| **Polycarbonate (PC)** | **5** | 3 | **5** | **5** (heat + toughness) | 2 | **$29.99** PolyLite PC · **$38.99** PolyMax PC — *VERIFIED* |
| **PC-ABS blend** | 4 | 3 | 4 | 4 | 3 | **$49.99** Polymaker PC-ABS — *VERIFIED* |
| **Nylon-CF (PA6-CF / PA12-CF)** | **5** | **4** | **5** | **5** (stiff + tough) | 2 | **$39.99** Fiberon PA6-CF20 · **$69.99** Fiberon PA12-CF10 · **$29.99** PA6-GF25 — *VERIFIED* |
| **PLA-CF / PETG-CF** | 2 | 2 | 3 | 3 (stiff, **brittle**) | 4 | **$19.99** Fiberon PETG-rCF08 — *VERIFIED* |
| **Nylon (unfilled CoPA)** | 4 | 3 | 4 | 4 | 2 | **$49.99** PolyMide CoPA — *VERIFIED* |

**[J] The honest per-material verdict for an FTC robot:**

- **PETG is the default.** It is tougher than PLA, does not creep in a hot van or a gym, is cheap, prints on
  any machine, and does not need an enclosure. **If you standardise on one material, standardise on PETG.**
- **PLA+ is fine for prototypes, jigs and non-structural brackets** and prints faster and more accurately
  than anything else. Its two disqualifying weaknesses on a robot: **it creeps under sustained load** (a
  PLA bracket under spring tension will slowly sag over a season) and **it softens near a hot motor**
  (a Yellow Jacket after a long match is warm enough to matter). Never use PLA on a part that is both
  loaded and near a motor.
- **TPU 95A is not optional — it is a second material you should own.** It is the correct answer for
  compliant intake surfaces, impact pads, gaskets and anything that must survive being hit.
  **[J] TPU 95A over TPU 85A/90A for robot parts** — softer TPU is harder to print and too floppy for
  rollers. Print it slow, direct-drive, with a dry spool.
- **ABS/ASA are worth it only if you have an enclosed printer** and are solving a specific heat problem.
  Warping and the smell make them a poor fit for a school room. **[J] Skip.**
- **PC and Nylon-CF are real engineering wins and real operational costs.** Both are hygroscopic (they must
  be dried, see §3.9), both want a hardened nozzle for the filled grades, and Polymaker's own PC pages state
  annealing is essential (**"90 °C oven for at least 2 hours"**, VERIFIED) and that PA parts want
  **80–100 °C for 6–16 hours** annealing — that is an oven and a schedule, not a click.
- **Carbon-filled PLA/PETG buys stiffness and loses toughness.** It is *more* brittle, not less. Use for
  parts that must not flex; never for parts that get hit.

### 3.3 When a tougher filament is actually worth it — the decision rules

**[J] Escalate material only when one of these is true. Otherwise PETG.**

| Symptom on the robot | Escalate to | Do NOT escalate if |
|---|---|---|
| Part sits within ~40 mm of a motor case or inside a hot gearbox tunnel | **PC or PC-ABS** (or move the part) | You can simply move it |
| Part is repeatedly struck by another robot or by a SCORING ELEMENT | **TPU** (compliant) or **PC** (tough rigid) | The impact energy is low — PETG absorbs a lot |
| Part is a thin cantilever that must not flex (camera mast, sensor arm) | **Nylon-CF or PETG-CF** | You can add a rib or a gusset instead — geometry beats material |
| Part sees sustained spring/elastic preload for weeks | **PETG minimum; PC if hot** | It is PLA. Just stop using PLA there |
| Part is a bearing seat or press-fit boss that keeps loosening | **Nylon or PC** — or better, **redesign to a heat-set insert or a bolted bearing** (§3.7) | A metal insert solves it more cheaply than a material change |
| Part failed and you do not know why | **Nothing.** Find the failure mode first | Always |

🕐 **[J] Geometry beats material almost every time.** A PETG bracket with a 3 mm gusset and a 5-wall
perimeter is stronger, cheaper and easier to duplicate than the same bracket printed in $70/kg PA12-CF with
the same thin section. **Escalating material to fix a design problem is the most expensive habit a team can
acquire**, because the second robot pays for it too.

### 3.4 Print orientation — the single highest-impact setting

**The physics [J]:** FDM parts are strong in the XY plane and weak in Z, because Z strength is only the
inter-layer weld. Depending on material and settings, **Z strength is commonly on the order of half of XY
strength, and Z *impact* toughness is worse than that.** Every printed failure you will see this season is a
layer separation.

**The rules, in priority order [J]:**

1. **Orient so that the principal tensile/bending stress runs *along* layers, never *across* them.**
   For an L-bracket: print it lying on the inside of the L (the "flat on its back" orientation) so the
   corner is continuous material, not a stack of layers being peeled apart.
2. **Never let a bolt's clamping or a bearing's press-out force try to separate layers.** Put screw axes in
   the XY plane where you can.
3. **Small cross-sections in Z are a fracture invitation.** A 4 mm-wide tab printed standing up will snap.
4. **Round or fillet every internal corner** — a sharp internal corner is a stress riser exactly where the
   layer weld is already the weak point. **[J] R2–R3 mm minimum on any loaded internal corner.**
5. **When you cannot orient favourably, add material** (a gusset, a thicker web) or **split the part** and
   bolt the two favourably-oriented halves together. A bolted two-piece printed part is much stronger than
   a one-piece part printed in the wrong direction.
6. **For impact parts, orient so the impact compresses layers rather than peels them.**

### 3.5 Walls, infill, and what actually carries the load

**🕐 [J] The most commonly misunderstood setting in FTC: WALLS carry the load, not infill.** A part at
5 walls / 20% infill is far stronger in bending than the same part at 2 walls / 60% infill, and prints
faster and lighter. Infill's real jobs are (a) supporting the top surface and (b) resisting crushing.

**[J] Recommended profiles — a good starting table for a 0.4 mm nozzle:**

| Part class | Layer height | Walls (perimeters) | Top/bottom layers | Infill | Infill pattern | Notes |
|---|---|---|---|---|---|---|
| **Structural bracket / mount** | 0.20 mm | **4–6** | 5 / 5 | 25–40 % | Gyroid or cubic | The FTC default. Walls do the work |
| **High-load: gearbox mount, lift bracket** | 0.20 mm | **6–8** | 6 / 6 | 40–60 % | Cubic | Approaching solid; consider whether a bought part is better |
| **Impact part (bumper, guard, roller face)** | 0.20–0.24 mm | **4–5** | 4 / 4 | 15–25 % | Gyroid | Some flex is protective. Do NOT print impact parts near-solid — they shatter |
| **Spacer / standoff (compressive)** | 0.20 mm | 3 | 4 / 4 | **60–100 %** | Concentric | The one case where infill genuinely matters |
| **Roller hub / anything on a shaft** | 0.16–0.20 mm | **5–6** | 5 / 5 | 40 % | Cubic | Grub-screw boss must be solid — use a modifier |
| **Cosmetic / cable clip / non-structural** | 0.24–0.28 mm | 2 | 3 / 3 | 10–15 % | Lightning/gyroid | Fast and cheap; most prints should be this |
| **Jig / drill guide** | 0.20 mm | **5** | 5 / 5 | 40 % | Cubic | It must not deflect while you drill against it — see §4.5 |
| **TPU (any)** | 0.20 mm | 3–4 | 4 / 4 | 10–20 % | Gyroid | Print slow (≤ 30–40 mm/s on a bowden machine); infill sets the effective softness |

**Other settings that matter [J]:**
- **Nozzle 0.4 mm is the right default; a 0.6 mm nozzle is a genuine upgrade for FTC** — most robot parts
  are chunky, and 0.6 mm cuts print time roughly 40% with *stronger* walls. Keep a 0.4 mm for fine detail.
- **Ironing off, brim on for tall/narrow parts, supports minimised by design (§9.2).**
- **Seam position:** move the Z-seam away from loaded corners and from bearing bores.
- **Cooling:** PLA/PETG high; ABS/ASA/PC low. Over-cooled PETG delaminates — a classic "why did the bracket
  snap in half along a line" cause.

### 3.6 Embedding fasteners and bearings — the technique that makes printed parts robust

**🕐 [J] A printed part bolted through with a screw into raw plastic will strip. This section is the fix, and
it is the difference between printed parts that survive a season and printed parts that get reprinted every
weekend.**

**A. Heat-set threaded inserts — the best answer, and worth learning this month.**
Brass knurled inserts melted into a printed boss with a soldering iron give a real metal thread that can be
assembled and disassembled dozens of times. MatterHackers' technique guide (VERIFIED this session) describes
it as: *use a soldering iron on a low setting with a shallow tapered tip to preheat the insert, apply it to
the hole with light pressure, let the plastic flow around the knurl, and make sure it sits square and flush
before removing the iron.* That page names **McMaster-Carr** as the supplier with the insert sizing chart —
**I did not load a McMaster page this session, so no insert SKU appears in this file.**

- **[J] Size to your fastener standard: M3 inserts for electronics/sensor mounts, M4 inserts for anything
  structural** (goBILDA is M4-primary — §7.1).
- **[J] Boss design:** wall thickness ≥ 2× the insert OD around the hole; boss depth ≥ insert length + 1 mm;
  hole diameter per the manufacturer's chart (do **not** guess — it is typically a few tenths under the
  insert OD, and getting it wrong either strips or bulges the part).
- **[J] Buy an insert-specific soldering tip.** A generic chisel tip works badly and cants the insert.

**B. Captive nuts (hex pockets) — the zero-extra-tool answer.**
Model a hex pocket sized for an M4 nut, bridged over so it prints without support, and drop the nut in
mid-print (pause) or slide it in from the side. **[J] Cheaper than inserts, uses hardware you already stock
(goBILDA M4 nylock nuts, `VENDOR-ECOSYSTEMS.md` §6.5), and fine for parts that are assembled once.** Side-
entry pockets are better than pause-inserted ones for a school shop — no pause discipline required.

**C. Thread-forming screws directly into plastic.** goBILDA sells **M4 Thread-Forming Socket Head Screws**
(family VERIFIED on the goBILDA screws category page). **[J] Acceptable for light, few-cycle joints; they
will strip if repeatedly removed.** Use only where the joint is not serviced.

**D. Tapping printed plastic directly.** Works (M4 tap, goBILDA `4204-0001-0004`, $13.99 VERIFIED) but the
thread is weak and single-use. **[J] Last resort.**

**E. Bearing pockets — press-fit, and how not to get it wrong.**
- **[J] Design the pocket at the bearing OD, then tune with a test coupon**, not by guessing. Printers
  differ; a pocket that is right on one machine is loose on another. **Print a 5-step test coupon
  (OD-0.10 / -0.05 / +0.00 / +0.05 / +0.10 mm) once per printer per material, write the answer on the
  printer, and never guess again.** 🕐 This single 20-minute exercise removes most printed-part rework.
- **Prefer a shoulder + through-bolt over a pure press fit** for anything that takes real load: let the
  bolt clamp the bearing, not the plastic.
- **A printed part is not a substitute for a pillow block.** goBILDA `1602`/`1605`/`1606`/`1621` pillow
  blocks exist precisely so you don't need a mill (`VENDOR-ECOSYSTEMS.md` §6.4). **[J] Bolt a COTS pillow
  block to a printed plate rather than printing a bearing seat, whenever the load is real.**

**F. Never print a threaded hole for a load-bearing screw.** Model a clearance hole (§7.2) and use a nut,
an insert, or a threaded plate (goBILDA sells Threaded Plates — family VERIFIED).

### 3.7 Realistic print times and material cost per part

**[J] Times are for a modern CoreXY/bed-slinger at 0.2 mm layers with a 0.4 mm nozzle and default
"standard" speeds. Material cost is [D], computed from the VERIFIED filament prices in §3.2 at
$19/kg for PLA/PETG (= $0.019/g) and $40/kg for PA6-CF (= $0.040/g).**

| Typical part | Mass | Print time (0.4 mm) | Print time (0.6 mm) | Material cost @ PETG | Material @ PA6-CF |
|---|---|---|---|---|---|
| Cable clip / connector retainer | 3 g | 8–12 min | 5–8 min | **$0.06** | $0.12 |
| Sensor or limit-switch bracket | 12 g | 30–45 min | 20–30 min | **$0.23** | $0.48 |
| Camera / Limelight mount | 25 g | 1.0–1.5 h | 0.6–0.9 h | **$0.48** | $1.00 |
| Odd-length spacer set (×8) | 12 g | 25–40 min | 15–25 min | **$0.23** | $0.48 |
| Motor mount / gearbox adapter plate | 55 g | 2.5–3.5 h | 1.5–2.2 h | **$1.05** | $2.20 |
| Roller hub (pair) | 30 g | 1.5–2.0 h | 0.9–1.2 h | **$0.57** | $1.20 |
| Gripper jaw (pair, rigid + TPU pads) | 45 g | 2.5–4.0 h | 1.6–2.5 h | **$0.86** | $1.80 |
| Control Hub / battery tray | 110 g | 5–7 h | 3–4.5 h | **$2.09** | $4.40 |
| Intake roller, full width (TPU or rigid) | 85 g | 4–6 h | 2.5–3.8 h | **$1.62** | — |
| Hood / chute / deflector (large, thin) | 160 g | 7–10 h | 4.5–6.5 h | **$3.04** | $6.40 |
| Drill jig / assembly fixture | 70 g | 3.5–5 h | 2.2–3 h | **$1.33** | — |

**[D] The number that should reframe your thinking: a complete set of custom printed parts for one FTC
robot is typically 1.5–3 kg of filament, i.e. roughly $30–$60 of material.** For **two robots, $60–$120.**
Filament is not the cost. **Printer hours and student attention are the cost** — which is why §3.9's
"two printers" recommendation is about throughput, not capability.

**[J] Throughput planning:** at ~20 productive printer-hours per day per machine (realistically ~14 once you
count failed prints and gaps between jobs), **one printer produces roughly 2–4 robot parts per day.** A
mechanism with 12 printed parts, in duplicate, is **24 parts ≈ 6–12 printer-days on one machine, 3–6 on
two.** That is the real reason to own two printers.

### 3.8 BUY — the 3D printing COTS table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Printer, budget entry** | MatterHackers | **Creality Ender-3 V3 SE** | — | **1–2 shared** | **$179.00 ea** | Buy | **VERIFIED** (loaded 2026-08-22) | 🕐 **[J] The cheapest credible way to get a second machine.** Open frame, PLA/PETG only. Two of these ($358) beat one mid printer for a two-robot program's throughput |
| **Printer, mainstream workhorse** | MatterHackers | **Bambu Lab P1S** (sampler bundles: PLA / ABS / PETG) | — | **1 shared** | **$969.00** (bundle, reduced from $988–$994) | Buy | **VERIFIED** | **Enclosed**, 256×256×256 mm, product page states support for PLA, PETG, TPU **plus ABS, ASA, Nylon (PA) and PC**. The "buy one good printer" answer |
| Printer, workhorse + multi-material | MatterHackers | **Bambu Lab P1S Combo** (w/ AMS, sampler bundles) | — | 1 shared | **$1,219.00** | Buy | **VERIFIED** | AMS is a *convenience*, not a capability, for FTC. **[J] Skip unless you want multi-colour signage** |
| Printer, open-frame fast | MatterHackers | **Bambu Lab A1** | — | 1–2 | **price not on loaded page** | Buy | **FAMILY-ONLY — NEEDS-SKU-CHECK** | 256×256×256 mm; product page explicitly states **"It is NOT recommended to enclose the Bambu Lab A1"** — so it is a PLA/PETG/TPU machine. An 8-pack lists at **$4,800.00** (VERIFIED) = $600/unit in bulk |
| Printer, on sale this session | MatterHackers | **Bambu Lab X1-Carbon Combo** | — | 1 | **$999.00** (reduced from $1,249.00) | Buy | **VERIFIED** | 🕐 **[J] If this price holds, it is the best capability-per-dollar on the page** — enclosed, hardened, AMS included |
| Printer, open-source / repairable | Prusa Research | **Original Prusa MK4S** | — | 1 | **$657.40 kit / $925.00 assembled** | Buy | **VERIFIED** (prusa3d.com loaded) | **[J] The kit is a legitimate student build project** and teaches the machine. Open frame |
| Printer, enclosed open-source | Prusa Research | **Prusa CORE One+ (Gen 2)** | — | 1 | **$925.00 kit / $1,202.78 assembled** | Buy | **VERIFIED** | Enclosed CoreXY. Direct competitor to the P1S |
| Printer, small/cheap | Prusa Research | **Original Prusa MINI+** | — | 1–2 | **$508.33 semi-assembled** | Buy | **VERIFIED** | Build volume is small for FTC hoods/trays |
| **Filament — PETG (default)** | Polymaker | **Polymaker™ PETG** | 1.5–3 kg | **3–6 kg** | **$18.99 / kg** | Buy | **VERIFIED** | 🕐 **[J] Standardise here.** Buy black + one bright colour so A/B robot parts are visually distinguishable |
| Filament — PETG tough grade | Polymaker | **PolyMax™ PETG** | 0.5–1 kg | 1–2 kg | **$29.99 / kg** | Buy | **VERIFIED** | For the handful of parts that keep breaking |
| Filament — PLA (prototype/jig) | Polymaker | **Panchroma™ Matte PLA** · **PolyLite™ PLA Pro** | 1 kg | **2 kg** | **$18.99** · **$23.99** | Buy | **VERIFIED** | Jigs, mockups, non-structural |
| **Filament — TPU 95A** | Polymaker | **PolyFlex™ TPU95** (95A) | 0.5 kg | **1 kg** | **$29.99 / kg** | Buy | **VERIFIED** | 🕐 Rollers, pads, gaskets. TPU90 is $39.99, TPU95-HF $49.99 |
| Filament — PC (heat/tough) | Polymaker | **PolyLite™ PC** · **PolyMax™ PC** | 0–0.5 kg | 0–1 kg | **$29.99** · **$38.99** | Buy | **VERIFIED** | Needs enclosure; Polymaker states annealing at **90 °C for ≥2 h** |
| Filament — Nylon-CF (stiff) | Polymaker | **Fiberon™ PA6-CF20** · **PA12-CF10** · **PA6-GF25** | 0–0.5 kg | 0–1 kg | **$39.99** · **$69.99** · **$29.99** | Buy | **VERIFIED** | Hardened nozzle required for filled grades; Polymaker states annealing **80–100 °C for 6–16 h** |
| Filament — CF-PETG | Polymaker | **Fiberon™ PETG-rCF08** | 0–0.5 kg | 0–1 kg | **$19.99** | Buy | **VERIFIED** | Stiffer, more brittle than plain PETG |
| Filament — general marketplace | MatterHackers | PETG **from $14.99** · ABS **from $14.24** · Nylon **from $31.69** · PC **$101.00 listed** | — | — | as listed | Buy | **VERIFIED** (category ranges) | Useful cross-check on Polymaker pricing |
| Filament — Bambu ecosystem | MatterHackers | **Bambu Lab Filament** category | — | — | **$17.99 – $3,749.00** range | Buy | **VERIFIED** (range only) | **NEEDS-SKU-CHECK** per spool |
| **Filament dryer** | MatterHackers | **Creality SpacePi x4 Filament Dryer** | — | **1 shared** | **$179.00** | Buy | **VERIFIED** | 🕐 **[J] Mandatory the moment you buy PETG, TPU, PC or Nylon.** Wet filament is the #1 cause of weak, stringy, ugly prints — and it looks like a "bad printer" |
| Hardened nozzle (0.4 + 0.6 mm) | printer vendor | hardened steel nozzle for your machine | — | 2–4 | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | Required for any CF/GF-filled filament; brass wears out in hours |
| Heat-set inserts, M3 + M4 brass | McMaster-Carr (named by MatterHackers guide) | knurled heat-set inserts for plastics | 20–60 | **40–120** | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | 🕐 No SKU stated — **I did not load a McMaster page this session.** VENDOR test met per `LEGAL-PARTS-CONSTRAINTS.md` §8.2 |
| Soldering iron + insert tips | any | temperature-controlled iron, insert-specific tips | — | **1 shared** | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | Doubles as the wiring iron |
| Print-removal + finishing set | any | flush cutters, deburring tool, needle files, scraper | — | **1–2 sets** | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | R201 [C]: no sharp edges/protrusions |
| Spare build plate / PEI sheet | printer vendor | textured PEI plate for your machine | — | **1 per printer** | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | A scratched plate ruins every subsequent print |

### 3.9 FABRICATE / ASSEMBLE IN-HOUSE — what the printing capability itself requires of you

| Task | Tooling / material | Student-hours [J] | Notes |
|---|---|---|---|
| **Printer setup, levelling, first-layer calibration** | the printer | 2–4 h per machine, once | Do this in **August**, not on kickoff night |
| **Per-material tuning: flow, temperature tower, retraction** | printer + test prints | 1.5–3 h per material | Do PETG and TPU now. Write results on a card taped to the printer |
| **Press-fit test coupon per printer per material** | printer | **0.3 h**, once | 🕐 §3.6E. Highest return-per-minute activity in this document |
| **A parameterised CAD library of standard brackets** | CAD (Onshape free EDU / Fusion EDU) | **8–20 h**, once, reusable forever | Explicitly legal to build **now** under **R304 [C]** |
| **Slicer profile set: "FTC-structural", "FTC-light", "FTC-TPU", "FTC-jig"** | slicer | 2–3 h, once | Removes per-print judgement calls from students |
| **A print queue board (part, qty 2, material, owner, status)** | whiteboard or spreadsheet | 1 h to set up | 🕐 **[J] The mechanism that enforces "always print two."** |
| Filament storage: dry boxes / sealed bins + desiccant | bins, desiccant | 1 h | Cheaper than the dryer; use both |

### 3.10 Approximate subtotal — the printing capability

| Line | One-time (shared across both robots) | Per season, both robots |
|---|---|---|
| **Rookie-minimum printer set:** 2 × Ender-3 V3 SE | **$358.00** *(VERIFIED)* | — |
| **Recommended set [J]:** 1 × Bambu P1S bundle + 1 × Ender-3 V3 SE | **$1,148.00** *(VERIFIED)* | — |
| **Competitive set [J]:** 1 × P1S (or X1-C Combo at $999) + 1 × A1-class open frame | **$1,600–$2,000** | — |
| Filament dryer (Creality SpacePi x4) | **$179.00** *(VERIFIED)* | — |
| Consumables: nozzles, plates, insert tips, finishing tools | **$150–$300** *(FAMILY-ONLY)* | — |
| Heat-set inserts, M3 + M4 | **$40–$90** *(FAMILY-ONLY)* | — |
| **Filament, 3–6 kg PETG + 2 kg PLA + 1 kg TPU** | — | **$110–$190** *(VERIFIED unit prices, [D] totals)* |
| **Capability subtotal, rookie path** | **≈$730–$930** | **+$110–$190/season** |
| **Capability subtotal, recommended path** | **≈$1,520–$1,720** | **+$110–$190/season** |

🕐 **[D] Note the shape of this: the machines are ~90% of the cost and are a one-time, multi-season asset;
the per-robot consumable is $55–$95.** Printing is the *cheapest* marginal fabrication capability this
program can own, and the second robot's printed parts cost about **$30–$60 of filament**.

### 3.11 Common failure modes and the spares to stock

| Failure mode | What it looks like | Fix | Spare to stock |
|---|---|---|---|
| **Layer separation under load** | Part snaps cleanly along a horizontal line | Re-orient (§3.4); raise nozzle temp ~5–10 °C; reduce part cooling for PETG | 🕐 **A printed spare of every load-bearing custom part, per robot** |
| **Stripped screw thread in plastic** | Screw spins forever | Heat-set insert or captive nut (§3.6) | Inserts, M4 nylock nuts |
| **Press-fit bearing falls out / crushes boss** | Wobble, then noise | Test coupon; move to bolted pillow block | Pillow blocks (goBILDA `1602`/`1605`/`1606`) |
| **Wet filament** | Stringing, popping, weak and rough parts | Dry it (dryer, §3.8); store with desiccant | Desiccant packs |
| **Print detaches mid-job** | Spaghetti; 6 lost hours **and the second copy is lost too** | Clean plate with IPA; brim; fresh PEI | Spare build plate per printer |
| **Nozzle wear from CF filament** | Degrading quality, then under-extrusion | Hardened nozzle from the start | 2 × hardened nozzles |
| **PLA creep near a motor** | Bracket slowly sags; alignment drifts | Reprint in PETG; move the part | — |
| **Part too rough → abrasive on SCORING ELEMENTS (R201 [C])** | Marking on game pieces | Sand/deburr contact faces; use TPU pads | Sandpaper, TPU |
| 🕐 **Only one copy existed** | Robot B is down for a day | **Always print two** (§2.4) | The rule *is* the spare |

### 3.12 The rookie-friendly minimum vs. the competitive version

| | **Rookie minimum [J]** | **Competitive [J]** |
|---|---|---|
| Printers | 1 × Ender-3 V3 SE ($179 VERIFIED) | 1 enclosed (P1S $969 / X1-C Combo $999) + 1 open frame |
| Materials | **PETG only** | PETG + TPU95 + PLA (jigs) + PC or PA-CF for 2–3 named parts |
| Drying | Sealed bin + desiccant | Dedicated dryer ($179 VERIFIED) + sealed storage |
| Fastening into plastic | Captive M4 hex-pocket nuts | Heat-set inserts throughout, M3 electronics / M4 structural |
| Profiles | Slicer defaults + "5 walls" | 4 named profiles, per-material tuned, documented |
| Duplication | Print the second copy when needed | 🕐 **Every job queued at qty 2 from the start**; 3MF + STL committed to the team repo with the part number |
| Design | Print catalogue-like brackets | Parameterised CAD library built pre-Kickoff under **R304 [C]** |

---

## 4. CAPABILITY F-2 — SHEET AND PLATE WORK WITH HAND TOOLS

### 4.1 What it is and when a design needs it

Sheet work covers every flat part bigger than a printer bed or thinner than a print wants to be: **guards,
shields, deflectors, hopper walls, chute liners, mounting plates, ROBOT SIGN backers, bellypans and
sponsor/branding panels.** **R302(A) [C]** names *sheet stock* as legal raw material outright, and cutting
and drilling it is the named example of legal modification.

**[J] Reach for sheet instead of a print when the part is:** larger than ~200 mm in two dimensions ·
essentially 2D · needs to be thin and stiff at low mass · needs to be transparent so drivers and referees can
see through it · needs to be made in an hour rather than overnight.

**[J] Do not reach for sheet when:** the part is genuinely 3D · it needs bosses, pockets or bearing seats ·
it needs many precise holes in a non-rectangular pattern (that is a print, or a printed drill jig).

### 4.2 The main variants — sheet materials, compared

**Ratings 1-5, [J]. DUPLICABILITY = how reliably the second copy comes out identical with hand tools.**

| Material | Complexity to work | Cost | Tuning burden | Reliability on a robot | Duplicability | Verdict [J] |
|---|---|---|---|---|---|---|
| **Polycarbonate (Lexan/Tuffak/Makrolon), 1–3 mm** | 2 | 2 | 1 | **5** | 4 (with a jig) | 🕐 **The default. Nearly unbreakable, drills and cuts with hand tools, bends cold** |
| **Polycarbonate, 4.5–6 mm** | 3 | 3 | 1 | 5 | 3 | Structural plates; heavier and slower to cut |
| **Acrylic (Plexiglas/PMMA)** | 1 | 1 | 1 | **1** | 4 | ❌ **[J] NEVER on a robot.** It shatters, and shattering on the FIELD is an R201 [C] "making a mess"/hazard problem |
| **Aluminium sheet 6061, 1–2 mm** | 4 | 3 | 2 | 4 | 3 | Stiff and light, but cutting and deburring by hand is slow and sharp (R201 [C]) |
| **Aluminium plate 6061, 3–6 mm** | **5** | 4 | 3 | 5 | 2 | ❌ **[J] Without a mill, don't.** Buy channel/plate on-pattern instead |
| **HDPE / UHMW, 3–6 mm** | 1 | 2 | 1 | 4 | 4 | Excellent low-friction wear surfaces, guides and slides. Does not glue or paint |
| **Delrin/POM, 3–6 mm** | 2 | 4 | 1 | 5 | 4 | Superb bearing/wear plates; expensive |
| **Baltic birch ply, 3–6 mm** | 1 | 1 | 1 | 3 | **5** | 🕐 **[J] Underrated for jigs, mock-ups and practice-field fixtures.** R302(C) names wood as legal raw material |
| **FR4 / G10 sheet** | 3 | 4 | 1 | 5 | 3 | Very stiff, electrically insulating; dust is nasty — respirator required |

**BUY — sheet stock table**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Polycarbonate sheet, 1 mm, 400×350 mm, 5-pack** | REV Robotics | **`REV-41-3049-PK5`** | 1 pack | **1–2 packs** | **$11.00 ea** | Buy | **VERIFIED** | 🕐 **[J] The best-value sheet in FTC.** Cuts with scissors/shears. Ideal ROBOT SIGN backers (R401(A) "robust material" [C]), light guards, sponsor panels |
| Polycarbonate sheet, 2 mm, 8 mm grid pattern, 456×296 mm | REV Robotics | **`REV-41-7537`** | 1 | **2** | within **$11.00–$75.00** family range | Buy | **VERIFIED SKU**, price **NEEDS-SKU-CHECK** | Pre-printed grid = free layout lines (§4.5) |
| Polycarbonate sheet, 3 mm, 1/2 in. grid, 1194×584 mm | REV Robotics | **`REV-21-3410`** | 0–1 | **1** | within **$11.00–$75.00** family range | Buy | **VERIFIED SKU**, price **NEEDS-SKU-CHECK** | Large structural sheet; the grid is a genuine time-saver for hand layout |
| Polycarbonate sheet, 1/16 in. (1.6 mm), 24×48 in. | ePlastics | **`PCCLR0.060AM24X48`** | 1 | **2** | **$26.92 ea** (qty 1–2) | Buy | **VERIFIED** | General-purpose supplier; meets the VENDOR test (`LEGAL-PARTS-CONSTRAINTS.md` §8.2). Cut-to-size offered |
| **Polycarbonate sheet, 1/8 in. (3.2 mm), 24×48 in.** | ePlastics | **`PCCLR0.125AM24X48`** | 1 | **2** | **$44.21 ea** (qty 1–2) | Buy | **VERIFIED** | 🕐 **[J] The workhorse thickness** for guards and structural panels. One sheet supplies both robots for most seasons |
| MAXComposite sheet | REV Robotics | **`REV-21-3098`** | 0–1 | 0–2 | **$150.00–$225.00** | Buy | **VERIFIED** (range) | High-performance stiff panel. **[J] Nice, not necessary** |
| Aluminium sheet/plate 6061 | local metal supplier / online | 0.063–0.125 in. sheet | as needed | ×2 | **UNVERIFIED** | Buy | **UNVERIFIED** | 🕐 **No aluminium price in this file came off a loaded page** (§0.2). Local suppliers meet the VENDOR test |
| HDPE / UHMW sheet | plastics distributor | 1/8–1/4 in. sheet | 0–1 | 0–2 | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | Wear strips, low-friction guides |
| Baltic birch plywood, 1/8–1/4 in. | local hardware / hobby | 12×24 in. sheets | — | 2–4 | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | **Jigs and mock-ups only** — see §4.5 |

### 4.3 Cutting sheet with hand tools — the actual techniques

**Polycarbonate, thin (≤1.5 mm) [J]:** heavy scissors, tin snips or a rotary cutter. Fast, silent, no dust.
This is why the REV 1 mm 5-pack is such good value.

**Polycarbonate, 1.5–3 mm [J]:**
- **Score-and-snap** with a plastic scoring knife against a straightedge: score 5–8 passes, overhang the
  bench edge, snap down. Only works for **straight cuts to an edge**. Cheapest possible method.
- **Jigsaw** with a fine metal-cutting blade (~24 TPI), slow speed, tape over the cut line to prevent
  chipping and to hold the layout. **[J] Best all-round tool for curves in a school shop.**
- **Portable band saw or benchtop band saw** with a fine blade — the cleanest cut, minimal chatter.
- ❌ **Do not use a table saw or circular saw on polycarbonate unless the blade is a plastics/laminate blade
  and the sheet is fully supported.** A grabbing blade throws sheet.
- **Deburr every cut edge with a scraper or fine file** — R201 [C] names *"components with exposed sharp
  edges or sharp protrusions"* as a damage-risk example.

**Polycarbonate, 4.5 mm+ [J]:** band saw or jigsaw only. Expect to spend real time on edge finishing.

**Aluminium sheet [J]:** hacksaw or jigsaw with a metal blade and cutting wax; a hand nibbler for
straight-ish interior cuts; **always deburr with a file and a deburring tool.** Aluminium chips are sharp
and get into bearings — clean up before assembly.

**Universal rules [J]:** support the workpiece close to the cut; clamp, never hand-hold; cut **outside** the
line and file to it; eye protection always (§10).

### 4.4 Drilling and hole accuracy without a mill

**🕐 [J] This is the single skill that most separates a "hand-tool" team from a "we need a mill" team.
You do not need a mill to get accurate holes. You need a drill press, a centre punch, and a jig.**

**The technique stack, in order of accuracy:**

| Method | Realistic positional accuracy [J] | When to use |
|---|---|---|
| Hand drill, eyeballed | ±1.5 mm and out of square | Never, on a part that matters |
| Hand drill + centre punch | ±0.8 mm | Field repairs |
| **Drill press + centre punch + clamped work** | **±0.3–0.5 mm** | **The standard method** |
| **Drill press + printed/COTS drill jig** | **±0.15–0.25 mm, and repeatable** | 🕐 **The two-robot method** |
| **Use an existing COTS plate as the drill template** | Matches the pattern exactly, by definition | Best of all — see below |

**The rules [J]:**
1. **Centre punch every hole.** A drill bit walks on smooth polycarbonate and on aluminium alike. An
   automatic centre punch is under $15 and removes a whole class of error.
2. **Back the work with scrap wood.** It stops break-out, stops the drill grabbing on exit, and stops
   polycarbonate from cracking around the hole.
3. **Pilot then final** for anything over ~5 mm: 3 mm pilot, then the finish size.
4. **Polycarbonate wants a slow speed and a modified (blunted) drill point** or a plastics-specific bit;
   a standard sharp twist drill grabs and cracks. **A step drill is excellent in thin polycarbonate**
   and gives a clean, deburred hole in one operation.
5. **Aluminium wants cutting fluid or wax and a moderate speed.** Cobalt bits last far longer — goBILDA
   sells **3.3 mm** (`4207-0001-0033`, $5.49) and **4.0 mm** (`4207-0001-0040`, $5.49) cobalt bits, both
   VERIFIED, and those are exactly the two sizes an M4 ecosystem needs (§7.2).
6. **🕐 The highest-accuracy trick available to a no-mill team: let a COTS part be the jig.** Clamp a
   goBILDA grid plate, pattern plate or a length of channel onto your blank sheet and drill *through* its
   existing holes. The result is on-pattern by construction, matches every other goBILDA part, and is
   exactly repeatable for robot B. **[J] Design custom plates to be drilled through a COTS plate wherever
   possible; it converts a precision problem into a clamping problem.**
7. **Never drill a hole you can avoid.** A slot cut with two drilled ends and a file between them is
   forgiving; a single precisely-placed hole is not. **Design in slots and clearance** (§9.1).

### 4.5 🕐 JIGS — the single highest-leverage habit for a two-robot program

**The argument [D]:** a jig converts a *skill-dependent* operation into a *repeatable* one. Its cost is paid
once; its benefit is paid on every copy. With two robots, every jig is amortised over at least two parts
immediately — and over every spare and every replacement for the rest of the season.

**The rule [J]: if you are about to make the same part twice, make the jig first.** For this program that
means *almost always*, because everything is made twice by definition.

| Jig type | Made from | Build time [J] | What it buys |
|---|---|---|---|
| **Drill jig / hole template** | 3D print (5 walls, 40% infill) or ply | 0.5–1.5 h | Identical hole patterns on both robots; ±0.15–0.25 mm |
| **Cut-length stop block** | scrap ply or printed block clamped to the saw table | 0.2 h | Identical channel/extrusion lengths — the #1 cause of a crooked second chassis |
| **Bend jig / form block** | ply or printed form | 0.5–1 h | Repeatable polycarbonate bends (§4.6) |
| **Assembly fixture** ("build both chassis in this") | ply base + printed locators | 2–4 h | Two square, identical chassis. Squareness is invisible until odometry disagrees |
| **Wiring/harness board** | ply sheet with the layout drawn 1:1 | 1–2 h | Two identical harnesses, made off-robot, R606-inspectable [C] |
| **Sign template** | printed FIRST template + backer | 0.3 h | Four legal ROBOT SIGNS (R401–R403 [C]) |
| **Motor-mount hole jig** | printed | 0.5 h | Every motor mounts identically on both robots |

**[J] The layout method that needs no mill and no CAD-to-machine path:**
1. Draw the part 1:1 in CAD; print it on paper at exactly 100% (verify with a ruler against a known
   dimension — printers lie).
2. Spray-adhesive or tape the paper to the sheet.
3. Centre punch through the paper at every hole.
4. Cut outside the line, drill on the punch marks, file to the line, deburr.
5. **Keep the paper template.** It is your jig for robot B.

**[J] Even better: skip step 1-2 by using pre-gridded stock.** REV's 2 mm 8 mm-grid (`REV-41-7537`) and
3 mm 1/2 in.-grid (`REV-21-3410`) polycarbonate sheets are printed with a layout grid — VERIFIED SKUs — which
turns "measure and mark" into "count squares". For a team with limited mentor hours, that is a real
error-rate reduction.

### 4.6 Bending polycarbonate

**[J] Polycarbonate's superpower over acrylic and aluminium: it bends cold without cracking.**
- **Cold bending** over a form block or a bench edge works for gentle radii in 1–2 mm sheet. Radius ≥ ~6×
  thickness. No heat, no tools, instantly repeatable with a form block.
- **Heat bending** with a strip heater or a heat gun and a bend jig gives crisp lines in 2–3 mm sheet. Go
  slow and even; scorched polycarbonate is brittle and cloudy. **Dry the sheet first** if it has been stored
  damp, or it will bubble — polycarbonate absorbs moisture.
- **Always bend so the protective film side that faces outward is on the outside of the bend**; leave the
  masking on as long as possible.
- ❌ **Never try this with acrylic** — see §4.2.

### 4.7 FABRICATE / ASSEMBLE IN-HOUSE — the sheet-work jobs themselves

| Job | Tooling / material | Student-hours (first) [J] | Hours (second copy) [J] |
|---|---|---|---|
| ROBOT SIGN set (2 signs + backers) | printed template, 1 mm PC, hook-and-loop | 1.0 h | 0.5 h |
| Simple flat guard/shield | 1/16 in. PC, jigsaw, drill press | 0.8–1.5 h | 0.4–0.8 h |
| Bent deflector / hopper wall | 1/8 in. PC, heat gun + bend jig | 2.0–3.5 h | 0.8–1.5 h |
| Electronics bellypan / mounting plate | 1/8 in. PC, drilled through a COTS grid plate | 1.5–2.5 h | 0.5–1.0 h |
| Bumper/edge guard set | 1/16 in. PC + TPU pads | 2.0–3.0 h | 1.0–1.5 h |
| Sponsor / branding panels | 1 mm PC + vinyl or print | 1.0 h | 0.5 h |
| **A drill jig for any of the above** | print or ply | +0.5–1.5 h once | **saves ≥0.5 h every copy** |

### 4.8 Approximate subtotal — the sheet-work capability

| Line | Per robot | For 2 robots |
|---|---|---|
| REV 1 mm PC 5-pack `REV-41-3049-PK5` | $11.00 | **$11.00–$22.00** *(VERIFIED)* |
| ePlastics 1/8 in. PC 24×48 `PCCLR0.125AM24X48` | (shared) | **$44.21–$88.42** *(VERIFIED)* |
| ePlastics 1/16 in. PC 24×48 `PCCLR0.060AM24X48` | (shared) | **$26.92** *(VERIFIED)* |
| Optional REV gridded sheets (`REV-41-7537`, `REV-21-3410`) | — | within **$11–$75** each *(VERIFIED range)* |
| Blades, bits, files, deburring tool, spray adhesive | — | **$60–$120** *(FAMILY-ONLY)* |
| **Sheet-work material subtotal, both robots** | — | **≈$145–$260** |

### 4.9 Common failure modes and the spares to stock

| Failure mode | Cause | Fix | Spare to stock |
|---|---|---|---|
| **Crack radiating from a hole in polycarbonate** | Sharp drill grabbed; no backing; hole too close to the edge | Blunt the drill point / use a step drill; back with wood; **hole centre ≥ 2× diameter from any edge** | Offcut sheet |
| **Sharp cut edge (R201 [C] inspection risk)** | Not deburred | Scrape/file every edge; a 0.5 mm chamfer is enough | Deburring tool blades |
| **Panel cracks at a bolt under vibration** | Bolt clamped directly onto thin sheet | **Add a washer, or a printed spreader plate**; never over-torque plastic | Washers, printed spreaders |
| **The two robots' panels don't interchange** | Made freehand, no jig | Make the jig, remake both | The jig itself |
| **Cloudy/brittle bend** | Overheated during heat bending | Slower, lower heat, even pass; dry the sheet first | Offcut sheet |
| **Acrylic shattered on the FIELD** | Acrylic was used at all | Replace with polycarbonate. **Never use acrylic** | — |

### 4.10 The rookie-friendly minimum vs. the competitive version

| | **Rookie minimum [J]** | **Competitive [J]** |
|---|---|---|
| Material | REV 1 mm PC 5-pack ($11.00 VERIFIED) + one 1/16 in. sheet | Gridded REV sheets + 1/16 in. and 1/8 in. ePlastics stock + HDPE for wear surfaces |
| Cutting | Scissors + hacksaw + a fine-blade jigsaw | Band saw + jigsaw + scoring knife |
| Holes | Hand drill + centre punch + wood backing | Drill press + printed jigs + COTS-plate-as-template |
| Layout | Paper template glued to the sheet | Gridded stock + printed drill jigs, filed in the team repo with part numbers |
| Bending | Cold bends over a bench edge | Heat gun + dedicated bend jigs |
| Duplication | Trace part A to make part B | 🕐 Both parts cut from one jig, in one session, and marked "A" and "B" |

---

## 5. CAPABILITY F-3 — CUTTING STOCK: EXTRUSION, CHANNEL, TUBE, SHAFT

### 5.1 What it is and when a design needs it

Almost every FTC robot is mostly **bought aluminium cut to length**. goBILDA U-channel, low-side channel,
goRAIL, beams and tubing, and REV extrusion all arrive in fixed lengths and become a chassis only after
somebody cuts them. **R302(B) [C]** explicitly names *extruded shapes* as legal raw material, and the manual
is careful on a related point: a length of stock *"cut into 5 ft. pieces by the team for storage or
transport"* is **neither COTS nor a FABRICATED ITEM** because *"the cuts were not made to advance the part
towards its final form"* (`LEGAL-PARTS-CONSTRAINTS.md` §8.1, quoting the V0 definitions). **Cut it to a
mechanism dimension and it becomes a FABRICATED ITEM — which is entirely legal, and permitted pre-Kickoff
under R304 [C].**

**🕐 [J] The cheapest way to avoid this whole capability: buy the length you need.** goBILDA sells U-channel
in **27 length variants from 1-hole/48 mm to 49-hole/1200 mm** (`VENDOR-ECOSYSTEMS.md` §6.3, VERIFIED), and
the 17-piece channel bundles (`3203-1120-0001` $219.99, `3203-1121-0001` $199.99, `3203-1143-0001` $184.99 —
all VERIFIED in `VENDOR-ECOSYSTEMS.md` §6.3/§6.10 on 2026-08-22, **not re-loaded in this session**) exist precisely so a team without a saw can build a chassis. **Cut only what the catalogue
cannot give you.**

### 5.2 The main variants — how to cut aluminium stock

**Ratings 1-5, [J]. DUPLICABILITY = "will the second piece be the same length and square?"**

| Method | Complexity | Cost | Tuning burden | Cut quality | Duplicability | Verdict [J] |
|---|---|---|---|---|---|---|
| **Hacksaw + mitre box** | 1 | **1** | 1 | 2 | 2 | The true minimum. Slow, tiring, and squareness depends on the box |
| **Hand hacksaw, freehand** | 1 | 1 | 1 | 1 | **1** | ❌ Not acceptable for a chassis rail |
| **Portable band saw (with stand)** | 3 | 2 | 2 | 4 | 4 | 🕐 **[J] The sweet spot for a school shop** — quiet, safe, cuts anything, small footprint |
| **Benchtop horizontal band saw** | 3 | 3 | 2 | **5** | **5** | Set a stop, walk away, repeatable lengths |
| **Mitre saw with a non-ferrous blade** | 3 | 3 | 3 | **5** | **5** | Fast and very square — **but loud, throws chips, and demands full PPE and a mentor present** |
| **Abrasive chop saw** | 2 | 2 | 2 | 2 | 3 | ❌ **[J] Avoid for aluminium** — it loads the wheel, burns, and throws sparks |
| **Angle grinder with cut-off wheel** | 2 | 1 | 3 | 1 | 1 | ❌ Emergency only. Not a length-cutting tool |

**[J] Recommendation for this program: a portable band saw with a stand (Tier 2, §6), plus a hacksaw and
mitre box as the Tier 1 fallback and the travel-kit tool.**

### 5.3 Squareness and length repeatability — the two-robot problem

**[D] A chassis is four rails. If rail A and rail A' differ by 1.5 mm, robot A and robot B will have
different wheelbases, different odometry constants, and different autonomous behaviour — and you will spend
programming hours you did not budget compensating for a saw.**

**The protocol [J]:**
1. **Cut both robots' pieces in the same session, from the same setup.** Never "we'll cut robot B's later."
2. **Use a stop block** clamped to the saw table or fence — not a tape measure per cut. This is the
   cheapest jig in the shop (§4.5) and the highest-value one.
3. **Cut long, then face to length.** Cut ~1 mm over, then file/sand both pieces together to identical
   length.
4. **Measure the pair against each other, not against a ruler.** Stack them; any step is your error.
5. **Deburr, then mark them** — "A-FL", "B-FL" — with a paint pen. Mixed-up rails are a real failure mode.
6. **Cut *between* holes, never through one.** goBILDA channel and REV extrusion are on a fixed hole
   pattern; a cut that clips a hole leaves a weak, sharp, useless end. **Count holes, then cut.**
   🕐 **[J] This is the most common irreversible mistake a new student makes with $30 of channel.**

### 5.4 Deburring and edge finishing — an R201 inspection item, not a nicety

**R201 [C]** names *"components with exposed sharp edges or sharp protrusions"* as a damage-risk example.
Every saw cut and every drilled hole is sharp until treated.

**[J] The three-tool deburring kit:** a **hand deburring tool** with a swivel blade (for hole edges and
extrusion ends), a **fine flat file** (for cut faces), and **220-grit sandpaper** on a block. Thirty seconds
per cut. Add a **countersink or a larger drill spun by hand** to break hole edges in polycarbonate.

**[J] Chips and swarf:** vacuum the work area and blow out channel interiors before assembly. Aluminium
chips migrate into bearings and into the FIELD, and loose material released on the FIELD is explicitly an
R201 [C] problem.

### 5.5 Tapping — putting threads in aluminium and in printed plastic

**The M4 numbers you need [D], from the verified goBILDA drill-bit SKUs:**

| Operation | Drill size | goBILDA SKU | Price | Confidence |
|---|---|---|---|---|
| **M4 × 0.7 tap drill** (thread) | **3.3 mm** | **`4207-0001-0033`** | **$5.49** | **VERIFIED** |
| **M4 clearance hole** (screw passes through) | **4.0 mm** | **`4207-0001-0040`** | **$5.49** | **VERIFIED** |
| **M4 × 0.7 thread-starting tap** | — | **`4204-0001-0004`** | **$13.99** | **VERIFIED** |
| **Sliding T-handle tap wrench** | — | **`4204-0002-0001`** | **$14.99** | **VERIFIED** |

🕐 **[J] That four-line table is worth memorising: 3.3 to tap, 4.0 to clear.** Getting these backwards is
the most common tapping mistake, and drilling 4.0 where you meant 3.3 destroys the part.

**Technique [J]:**
- **Tap squarely.** Start the tap in the drill press chuck *by hand* (power off, spin the chuck) to
  guarantee perpendicularity, then finish with the T-handle.
- **Quarter-turn back for every half-turn forward** to break the chip. In aluminium, use cutting fluid or
  even soap; a dry tap in aluminium galls and snaps.
- **Broken taps are effectively unrecoverable without a mill.** Buy spares — a snapped tap in a $40 channel
  ruins the channel.
- **In printed plastic:** tapping works but the thread is weak and single-use. **Prefer heat-set inserts or
  captive nuts (§3.6).**
- **Thread-forming screws** (goBILDA sells **M4 Thread-Forming Socket Head Screws**, family VERIFIED) form
  their own thread in plastic and in thin sheet — good for few-cycle joints.

### 5.6 Cutting shaft, tube, chain and belt

- **Shaft (REX / hex / round) [J]:** goBILDA sells **8 mm and 12 mm REX shafting in lengths from 24 mm to
  624 mm** (VERIFIED family and price range, `VENDOR-ECOSYSTEMS.md` §6.4). **Buy the length. Cutting hardened
  stainless shaft with hand tools is slow, and a square, deburred, chamfered end is hard to achieve — and a
  bad end will not enter a bearing.** If you must cut: band saw or abrasive cut-off, then file the end
  square and chamfer it all the way round.
- **Tube and standoff stock [J]:** easy to cut with a band saw or a tubing cutter; deburr the bore, not just
  the outside, or it will not seat flat.
- **Chain [J]:** use the right tool — goBILDA **8 mm Pitch Chain Tool `4203-0001-0008`, $29.99 (VERIFIED)**.
  🕐 **[J] Buy it.** Breaking chain with a punch and a vice mangles links, and the 8 mm chain standard has
  no cross-vendor substitute (`VENDOR-ECOSYSTEMS.md` §3.5). Also buy master links and a chain tensioner
  (`1524-0001-0001`, $5.99 — VERIFIED in `VENDOR-ECOSYSTEMS.md` §6.4, **not re-loaded here**).
- **Timing belt [J]:** buy closed loops in the size you need. Cutting and welding belt to length is a
  FABRICATED ITEM the manual explicitly discusses (§8.2 of `LEGAL-PARTS-CONSTRAINTS.md`) but is not a
  hand-tool operation you should attempt.
- **Snap rings / E-clips [J]:** goBILDA **3-in-1 Snap Ring Pliers `4205-0001-0001`, $12.99 (VERIFIED)**.
  Small tool, prevents a lot of swearing.

### 5.7 FABRICATE / ASSEMBLE IN-HOUSE — the stock-cutting jobs

| Job | Tooling | Hours (first) [J] | Hours (second copy) [J] |
|---|---|---|---|
| Chassis rail set (4 pieces, cut + deburr + mark) | band saw + stop block | 1.5–2.5 h | **0.8–1.2 h** (same setup: ~0.5 h) |
| Superstructure uprights (4–6 pieces) | band saw + stop block | 1.5–2.0 h | 0.8 h |
| Arm/lift members cut to a game dimension | band saw | 1.0–1.5 h | 0.5 h |
| Tapping 8–12 holes M4 in aluminium | tap + T-handle + fluid | 1.0–1.5 h | 1.0–1.5 h *(does not get faster)* |
| Chain loops sized and joined (2 loops) | chain tool | 0.5–0.8 h | 0.5 h |
| Custom-length standoffs/spacers (×8) | tubing cutter or **print them instead** | 0.5 h | 0.2 h *(printed: ~0.1 h)* |

**[D] Note the tapping row: hand tapping is one of the few fabrication tasks with NO duplication discount.**
That is a direct argument for **through-holes with nuts, or heat-set inserts, over tapped holes**, wherever
the design allows.

### 5.8 Approximate subtotal — the stock-cutting capability (tools only; stock is in `VENDOR-ECOSYSTEMS.md` §6.3)

| Line | Cost | Confidence |
|---|---|---|
| Hacksaw + mitre box + blades (Tier 1) | **$30–$60** | FAMILY-ONLY |
| goBILDA M4 tap + T-handle + 3.3 mm + 4.0 mm cobalt bits | **$39.96** | **VERIFIED** ($13.99 + $14.99 + $5.49 + $5.49) |
| goBILDA 8 mm chain tool `4203-0001-0008` | **$29.99** | **VERIFIED** |
| goBILDA snap-ring pliers `4205-0001-0001` | **$12.99** | **VERIFIED** |
| Deburring tool + files + sandpaper | **$25–$50** | FAMILY-ONLY |
| Portable band saw (Tier 2) | **≈$120** | **SEARCH-SNIPPET** — BAUER 10 A deep-cut variable-speed band saw, item 64194; **product page 403'd, do not treat the price as verified** |
| **Subtotal, Tier 1 (hand tools only)** | **≈$140–$195** | mostly VERIFIED |
| **Subtotal, Tier 2 (adds band saw)** | **≈$260–$315** | band saw price unverified |

### 5.9 Common failure modes and the spares to stock

| Failure mode | Cause | Fix | Spare to stock |
|---|---|---|---|
| **Cut through a hole in channel** | Didn't count holes | None — recut a new piece | 🕐 **One spare long channel per robot** |
| **Rails differ in length between robots** | Cut in separate sessions without a stop block | Recut both to the shorter | Spare stock |
| **Snapped tap in a channel** | Dry tapping, no chip break | Usually scraps the part | **2 spare M4 taps** |
| **Bearing won't seat on a cut shaft** | End not square/chamfered | File square, chamfer | Spare shaft lengths |
| **Mangled chain link** | Chain broken with a punch | Rebuild the loop | Master links, spare chain (`3308-0008-1000` $11.99 — VERIFIED in `VENDOR-ECOSYSTEMS.md` §6.4, not re-loaded here) |
| **Sharp cut ends at inspection (R201 [C])** | Not deburred | Deburr; it takes 30 s | Deburring blades |

### 5.10 The rookie-friendly minimum vs. the competitive version

| | **Rookie minimum [J]** | **Competitive [J]** |
|---|---|---|
| Cutting | Buy catalogue lengths; hacksaw + mitre box for the rest | Portable/benchtop band saw with a stop block |
| Length control | Tape measure and care | Stop block, cut both robots' parts in one session |
| Threads | Through-holes + nylock nuts everywhere | Tapped holes where needed, inserts in plastic, standardised |
| Chain | Buy pre-made loops if available | Chain tool + master links + tensioners in stock |
| Marking | Sharpie | Paint pen, "A"/"B" convention, parts bagged per robot |

---

## 6. THE TOOL LIST BY TIER

**[J] The organising principle: buy the tier that unlocks a capability you actually need, and buy the
*duplicates* the two-robot structure demands before you buy the next tier up.** Two teams working in one
room contend for one drill press; they do not contend for two sets of hex keys.

### 6.1 TIER 0 — the travel / pit kit (goes to every event, duplicated per team)

**Unlocks: you can fix the robot at a competition. Without this you are borrowing tools between matches.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **12-Piece Tool Set for M4 Hardware** | goBILDA | **`3201-0015-0001`** | 1 | **2** | **$69.99 ea = $139.98** | Buy | **VERIFIED** | 🕐 **[J] The single best "just buy this" tool purchase in FTC.** Matches the M4 ecosystem exactly |
| 2.5 mm Hex-Plus T-handle | goBILDA (Wera) | **`5023332001`** | 1 | **2** | **$10.99 ea** | Buy | **VERIFIED** | T-handles are far faster than L-keys for repeated work |
| 3 mm Hex-Plus T-handle | goBILDA (Wera) | **`5023334001`** | 1 | **2** | **$13.99 ea** | Buy | **VERIFIED** | |
| Ball-end hex keys 2 / 2.5 / 3 / 4 mm | goBILDA | **`5027102001`** $2.49 · **`5027103001`** $2.49 · **`5027104001`** $2.99 · **`5027105001`** $3.49 | 1 set | **2 sets + 1 spare** | **$11.46/set** | Buy | **VERIFIED** | Ball ends reach fasteners at an angle — essential inside a chassis |
| 7 mm combination wrench | goBILDA | **`4202-0070-1070`** | 2 | **4** | **$1.99 ea** | Buy | **VERIFIED** | M4 nut size in the goBILDA system |
| 7 mm combination nut driver | goBILDA | **`4206-0070-0001`** | 1 | **2** | **$2.99 ea** | Buy | **VERIFIED** | |
| Wera 7 mm Joker combination wrench | goBILDA (Wera) | **`5020199001`** | 0–1 | **1–2** | **$15.99 ea** | Buy | **VERIFIED** | **[J] Luxury, but the ratcheting jaw genuinely speeds up nut work in tight chassis** |
| 3 mm Hex-Plus bit, 1/4 in. drive | goBILDA (Wera) | **`5059630001`** | 1 | **2** | **$8.99 ea** | Buy | **VERIFIED** | For the cordless driver — **[J] set the clutch low; stripped M4 heads are the top pit failure** |
| 3-in-1 snap ring pliers | goBILDA | **`4205-0001-0001`** | 1 | **1–2** | **$12.99 ea** | Buy | **VERIFIED** | |
| Loctite Threadlocker Blue 242, 6 mL | goBILDA | **`2922-0001-0001`** | 1 | **2** | **$7.99 ea = $15.98** | Buy | **VERIFIED** | 🕐 **BLUE, never red.** Red is effectively permanent |
| Flush cutters, needle-nose, small adjustable wrench | any | — | 1 set | **2 sets** | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | |
| Multimeter | any | basic auto-ranging DMM | 1 | **1–2** | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** | Electrical inspection and dead-motor triage |
| Zip ties, hook-and-loop, spare fasteners, spare fuses | goBILDA | see `VENDOR-ECOSYSTEMS.md` §6.5–6.6 | — | ×2 | — | Buy | cross-ref | **R601 [C]:** 20 A ATM mini blade fuse is the legal replacement |
| **Pit tool board (shadow board)** | — | ply + printed hooks | 1 | **2** | ~$20 | **Fab** | **[J]** | 🕐 A missing tool at an event costs a match. A shadow outline makes "missing" visible instantly |

**Tier 0 subtotal, both teams: ≈$290–$400 [D]** (VERIFIED goBILDA lines total **≈$300**, plus FAMILY-ONLY rows).

### 6.2 TIER 1 — the minimum shop (one set, shared)

**Unlocks: you can build the whole robot. Everything in §3, §4 and §5 at the "rookie minimum" level.**

| Item | Approx cost | Confidence | What it unlocks |
|---|---|---|---|
| **1 × 3D printer** (Creality Ender-3 V3 SE) | **$179.00** | **VERIFIED** | 🕐 **All custom geometry.** The single highest-value tool purchase in this document |
| Filament: PETG + PLA | **$38–$45** | **VERIFIED** unit prices | — |
| Cordless drill/driver + bit set | **$60–$120** | FAMILY-ONLY | Every hole, every screw |
| Centre punch (automatic) + steel rule + square | **$25–$40** | FAMILY-ONLY | Hole accuracy without a mill (§4.4) |
| Hacksaw + mitre box + spare blades | **$30–$60** | FAMILY-ONLY | Channel and extrusion to length |
| Jigsaw + fine metal/plastic blades | **$50–$90** | FAMILY-ONLY | Curved cuts in polycarbonate |
| Files (flat, round, half-round) + deburring tool | **$25–$50** | FAMILY-ONLY | **R201 [C] compliance** |
| goBILDA M4 tap `4204-0001-0004` + T-handle `4204-0002-0001` | **$28.98** | **VERIFIED** | Threads in aluminium |
| Cobalt bits 3.3 mm `4207-0001-0033` + 4.0 mm `4207-0001-0040` | **$10.98** | **VERIFIED** | 🕐 The two M4 sizes |
| Digital caliper, 6 in. | **$10–$25** | **SEARCH-SNIPPET** (PITTSBURGH composite ≈$9.99 / stainless ≈$24.99, item 63586 / 63711; **product pages 403'd**) | Measuring what you print and what you buy |
| Clamps (6 × spring, 4 × F-clamp) | **$30–$60** | FAMILY-ONLY | Safe cutting and drilling; jig holding |
| Bench vise | **$40–$90** | FAMILY-ONLY | Tapping, filing, chain work |
| Soldering iron (temp-controlled) + insert tips | **$35–$80** | FAMILY-ONLY | Wiring **and** heat-set inserts (§3.6) |
| Safety glasses ×15, first aid kit | **$60–$100** | FAMILY-ONLY | §10. Non-negotiable |
| goBILDA 8 mm chain tool `4203-0001-0008` | **$29.99** | **VERIFIED** | Chain, correctly |
| **TIER 1 TOTAL** | **≈$650–$1,000** | | **A complete, legal, two-robot-capable shop** |

### 6.3 TIER 2 — what to add next, in priority order

**Unlocks: repeatability, throughput, and the ability to make the second robot cheaply.**

| # | Item | Approx cost | Confidence | What it unlocks — and why it is at this rank [J] |
|---|---|---|---|---|
| **1** | **A SECOND 3D PRINTER** (Ender-3 V3 SE, or a P1S if budget allows) | **$179.00** / **$969.00** | **VERIFIED** | 🕐 **Rank 1 by a wide margin.** Doubles print throughput, and §3.7 shows printer-days are the real fabrication bottleneck for two robots. Also removes the single point of failure |
| **2** | **Benchtop drill press** — BAUER 8 in. 5-speed with light, item **58780** | **$89.99** | **VERIFIED** (page loaded 2026-08-22; 1/2 in. keyed chuck, 750–3200 RPM) | 🕐 Turns ±1.5 mm hand-drilled holes into ±0.3 mm holes. **The cheapest accuracy in the whole document** |
| **3** | **Filament dryer** — Creality SpacePi x4 | **$179.00** | **VERIFIED** | Removes the single biggest cause of "our prints are bad" once you use PETG/TPU/PC |
| **4** | **Portable band saw + stand** | ≈**$120–$170** | **SEARCH-SNIPPET** (BAUER item 64194; page 403'd) | Square, repeatable, quiet stock cutting (§5.2) |
| **5** | **Heat-set insert kit** (M3 + M4 + tips) | **$60–$150** | FAMILY-ONLY | Printed parts that survive a season (§3.6) |
| **6** | **Second set of hand tools** (so A team and B team don't queue) | ≈**$150–$250** | mixed | 🕐 **[J] Underrated.** Two teams, one toolbox, is a throughput loss disguised as a savings |
| **7** | **Metric tap and die set** — PITTSBURGH Carbon Steel Metric 40-pc | **$24.99** | **VERIFIED** (search page loaded) | Sizes beyond M4. Alternatives on the same page: PITTSBURGH SAE+Metric 60-pc **$42.99**, WARRIOR Metric Drill/Tap/Deburr 13-pc **$19.99**, ICON Metric 41-pc **$149.99** |
| **8** | **Heat gun + bend jigs** | **$30–$60** | FAMILY-ONLY | Formed polycarbonate (§4.6) |
| **9** | **Shop vacuum** | **$60–$120** | FAMILY-ONLY | Chips out of bearings and off the floor (R201 [C]) |
| **10** | **Parts storage: labelled bins, one drawer set per robot** | **$80–$200** | FAMILY-ONLY | 🕐 **[J] The "A parts / B parts" separation is a fabrication tool.** Mixed hardware bins are how robot B ends up different |
| **TIER 2 TOTAL** | | **≈$1,000–$1,600** | | |

### 6.4 TIER 3 — luxuries, honestly labelled

| Item | Approx cost | Confidence | Verdict [J] |
|---|---|---|---|
| **Enclosed printer** (Bambu P1S **$969.00** VERIFIED / X1-Carbon Combo **$999.00** VERIFIED / Prusa CORE One+ **$925.00 kit** VERIFIED) | $925–$1,219 | **VERIFIED** | 🕐 **Worth it if** you need ABS/ASA/PC/PA-CF, or you want prints that just work. **Not worth it** if PETG covers your needs — and it usually does |
| Mitre saw with non-ferrous blade | $200–$400 | FAMILY-ONLY | Faster and squarer than a band saw, but louder and more dangerous. **[J] Only with a trained mentor present** |
| Larger drill press (BAUER 10 in. **$169.99**, 12 in. variable-speed w/ laser **$299.99**, 17 in. **$499.99**) | $170–$500 | **VERIFIED** (category page loaded) | **[J] The 8 in. at $89.99 is enough for FTC.** Spend the difference on a second printer |
| Benchtop belt/disc sander | $100–$200 | FAMILY-ONLY | Genuinely useful for filing-to-a-line fast. **[J] The best Tier 3 buy for the money** |
| Rotary tool (Dremel-class) + cut-off wheels | $60–$120 | FAMILY-ONLY | Handy, imprecise, easy to misuse. **[J] Nice to have** |
| Resin (MSLA) printer | $200–$400 | UNVERIFIED | ❌ **[J] No.** Resin parts are brittle and the chemistry is a school-shop liability. FDM only |
| Laser cutter | $400–$3,000+ | UNVERIFIED | **[J] Cannot cut polycarbonate safely** (chlorine-free but produces a hazardous plume and a poor edge); cuts ply and acrylic — and acrylic is banned on this robot (§4.2). Low value here |
| Benchtop CNC mill/router | $1,500–$5,000+ | UNVERIFIED | ❌ **[J] Out of scope, and out of budget.** Everything in this document is designed so you never need one |
| Multi-material unit (AMS) | +$250 | **VERIFIED** (P1S Combo delta = $1,219 − $969) | **[J] Convenience, not capability**, for FTC |

### 6.5 What must be duplicated, and what must not

| Duplicate for two teams [J] | Share one [J] |
|---|---|
| Hex keys, T-handles, drivers, wrenches (Tier 0, per team) | Drill press |
| Thread locker, flush cutters, pliers | Band saw / mitre saw |
| Pit kit and shadow board | Filament dryer |
| Multimeter (ideally) | Bench vise |
| Parts bins — **"A parts" and "B parts" never mix** | Soldering station |
| Safety glasses (one per student, not one per team) | 3D printers *(but own two for throughput, §6.3 rank 1)* |

---

## 7. FASTENER AND HARDWARE DISCIPLINE

### 7.1 Standardise on ONE thread — and for this program that thread is M4

**VERIFIED this session on the goBILDA screws category page:** goBILDA's metric screw system uses
**M3, M4 and M5**, with **M4 as the primary standard across their hardware ecosystem**. Separately VERIFIED
on REV's FTC page: REV sells **M3 Nuts ($6.00–$8.75)** — the REV ION/DUO ecosystem is **M3-primary**.
`VENDOR-ECOSYSTEMS.md` §3.4 calls this "the quiet incompatibility," and §4.2 recommends committing to
goBILDA structurally.

**[J] The rule for this program, stated flatly:**

> **Structure is M4. Electronics and sensors are M3. Set-screws are M5. Nothing else exists.**

**Why this matters more for two robots than for one [D]:** every additional thread size doubles across
robots — two more bins, two more drivers in each pit kit, two more chances to grab the wrong screw at
11 pm. A three-size standard means **one 3 mm hex key drives essentially the whole robot**, and the goBILDA
12-piece M4 tool set (`3201-0015-0001`, $69.99 VERIFIED) is a complete kit rather than a partial one.

**The exceptions you will actually meet [J]:** motor face-mount screws (whatever the motor takes — R504(A)
[C] lets you modify the mounting bracket, not the motor), Control Hub / Expansion Hub mounting (M3 or M4
depending on your tray), and #10-32 / 1/4-20 if any AndyMark or legacy imperial parts sneak in — which is
exactly why `VENDOR-ECOSYSTEMS.md` §4 says pick one ecosystem and stay in it.

### 7.2 The approved screw-length list — a real discipline, not a suggestion

**[J] Stock these M4 lengths and no others: 8, 10, 12, 16, 20, 25, 30, 35, 40 mm.** Anything longer is
almost always a design smell (use a standoff). Anything in between is a bin you will regret.

**[J] Head-style policy:**

| Head style | Use it for | Why |
|---|---|---|
| **Button head** | **The default for everything visible or exposed** | Lower profile, less snag (**R202(I) [C]** entanglement), fewer sharp corners (**R201 [C]**) |
| **Socket head (cap)** | Higher-torque structural joints, anywhere you need clamping force | Deeper socket, less likely to strip |
| **Low-profile socket head** | Tight clearances, under moving parts | |
| **Hex head** | Where a wrench is faster than a hex key | 7 mm across flats in the goBILDA M4 system (VERIFIED tool sizes) |
| **Thread-forming socket head** | Into printed plastic or thin sheet, few-cycle joints | §3.6C |
| **Thread-locking socket head** | Vibration-critical joints where you don't want liquid Loctite | goBILDA lists **M4 Socket Head Thread-Locking Screws** (family VERIFIED) |
| **Set screw (M5)** | Collars, some hubs | 🕐 **[J] Prefer CLAMPING hubs over set-screw hubs wherever possible** — `VENDOR-ECOSYSTEMS.md` §3.8 |

**Hole-size discipline [D], from the VERIFIED goBILDA bit SKUs (§5.5):**
**M4 clearance = 4.0 mm** (`4207-0001-0040`) · **M4 tap drill = 3.3 mm** (`4207-0001-0033`) ·
M3 clearance = 3.2 mm · M3 tap drill = 2.5 mm *(M3 sizes are standard metric practice, **[J]**, not from a
loaded vendor page)*.

### 7.3 Thread locking, and the three ways a joint comes undone

**A season of vibration will undo any untreated threaded joint on this robot.** The three fixes, in order
of preference [J]:

1. **Nylock (nyloc) nuts** — best where you can reach both sides. Reusable ~5–10 times before the nylon
   gives up. goBILDA's Starter Kit ships ~200 locknuts per kit (`VENDOR-ECOSYSTEMS.md` §6.5).
2. **Blue threadlocker** — goBILDA **Loctite Threadlocker Blue 242, 6 mL, `2922-0001-0001`, $7.99
   (VERIFIED)**. 🕐 **BLUE (242), never RED (271).** Red is designed to require heat to remove and will
   cost you a part. Use blue on blind tapped holes, set screws, and anything you cannot reach with a wrench.
   **Let it cure — it is not at strength for several hours.**
3. **Thread-locking screws** (patch-coated) — goBILDA family VERIFIED. Convenient, single-use-ish.

❌ **[J] Split lock washers are near-useless on aluminium** and are not a substitute for either of the above.

**[J] The torque rule for a school shop:** **hand tools for final tightening, cordless drivers only for
running screws down.** Set the driver clutch low. **Stripped M4 sockets are the #1 avoidable pit failure**,
and an M4 screw in aluminium needs far less torque than a student's arm can produce.

### 7.4 Consumables to keep stocked — the two-robot standing inventory

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **M4 Hardware Starter Pack (2,625 pc)** | goBILDA | **`3201-0010-0001`** | — | **1 shared** | **$139.99** | Buy | **VERIFIED** | 🕐 **Buy in August.** Best hardware value found; fasteners stock out first (`VENDOR-ECOSYSTEMS.md` §5.2) |
| M4 Button Head Screw Assortment (600 pc) | goBILDA | **`3201-0004-0002`** | — | **1–2** | **$54.99 ea** | Buy | **VERIFIED** | The default head style (§7.2) |
| M4 Socket Head Screw Assortment (600 pc) | goBILDA | **`3201-0004-0001`** | — | 1 | **$54.99** | Buy | **VERIFIED** price/SKU on the screws category page 2026-08-22 | ⚠ `VENDOR-ECOSYSTEMS.md` recorded this **out of stock on 2026-08-21**. It is listed today; **stock status NEEDS-RE-CHECK before you rely on it** |
| M5 Set-Screw Bundle (75 pc) | goBILDA | **`3203-2806-0001`** | — | **1** | **$14.99** | Buy | **VERIFIED** | |
| M4 nylock nuts | goBILDA | Nuts category | 200+ | **400+** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | Starter Kit includes ~200/kit |
| M4 washers | goBILDA | Washers category | assorted | assorted | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🕐 **Always use a washer against plastic** (§4.9) |
| **M3 screws + nuts** (electronics/sensors) | REV | **M3 Nuts $6.00–$8.75**; M3 socket head screws (goBILDA family) | assorted | ×2 | **$6.00–$8.75** + NEEDS-SKU-CHECK | Buy | **VERIFIED** (REV nuts price range) / FAMILY-ONLY | The REV ecosystem is M3-primary |
| **Loctite Blue 242, 6 mL** | goBILDA | **`2922-0001-0001`** | 1 | **2** | **$7.99 ea** | Buy | **VERIFIED** | Blue. Not red |
| Heat-set inserts M3 + M4 | McMaster-Carr (named by MatterHackers guide) | knurled inserts for plastics | 20–60 | **40–120** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🕐 No SKU — no McMaster page loaded this session |
| Standoffs & spacers bundles | goBILDA | **`3203-1501-0001`** (148 pc) **$139.99** · **`3203-1502-0001`** (80 pc) **$46.99** | — | **1 of each, shared** | **$186.98** | Buy | **VERIFIED** (via `VENDOR-ECOSYSTEMS.md` §6.3) | Cross-referenced, not re-verified here |
| Zip ties, hook-and-loop, heat shrink, grommets | goBILDA | see `VENDOR-ECOSYSTEMS.md` §6.6 | — | ×2 | — | Buy | cross-ref | Supports **R606 [C]** inspectability |
| **20 A ATM mini blade fuses** | any auto-parts / goBILDA | Fuses category | 2 | **4–6** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **R601(A) [C]** names this exact fuse as the legal replacement |
| **Fastener subtotal, both robots** | | | | | **≈$400–$520** | | **[D]** | VERIFIED lines total ≈$400 |

### 7.5 The two-bin habit — how hardware discipline survives contact with 15 students

**[J] Four rules, all cheap, all high-return for a two-robot program:**

1. **One bin per screw length, labelled with the length in mm and nothing else.** Not "short/medium/long."
2. **Two-bin kanban:** each size has a working bin and a sealed reserve bag. **When you open the reserve,
   you write the item on the order list that day.** This is how a program with limited mentor hours avoids
   a Thursday-night stock-out.
3. 🕐 **"A parts" and "B parts" bins never mix.** Sub-assemblies for robot B live in a separate labelled
   box from the moment they are made. This is the physical enforcement of §2.4.
4. **A written "hardware standard" card taped inside the toolbox lid:** the three thread sizes, the nine
   lengths, the two drill sizes (3.3 / 4.0 mm), blue-not-red, washer-against-plastic. **[J] One index card
   prevents more rework than any lecture.**

---

## 8. STUDENT-HOUR ESTIMATES — the LABOR column for every BOM

### 8.1 How to read and use this table

**[J] All figures are judgement estimates calibrated to *this* program: high-school students of mixed
experience, a mentor available part-time, hand tools and 3D printers.** They include design time, making
time, and the first round of debugging/re-fitting — but **not** the mechanism-level integration and tuning
that the sibling mechanism files estimate separately.

**Columns:** *First* = hours to produce the first working article including its design. *Second* = hours to
produce the identical part for the other robot **from the proven design**. *Ratio* = Second ÷ First — the
**duplicability number**, and the single most useful figure in this file.

### 8.2 The table

| Fabricated part | Method | Skill | **First (h)** | **Second (h)** | **Both (h)** | Ratio | Notes |
|---|---|---|---|---|---|---|---|
| Cable clip / connector retainer | Print | Novice | 0.4 | **0.1** | 0.5 | **0.25** | Design once, print forever |
| Odd-length spacer set (×8) | Print | Novice | 0.5 | **0.1** | 0.6 | **0.20** | Cheaper than a catalogue 10-pack |
| Sensor / limit-switch bracket | Print | Novice | 1.2 | **0.2** | 1.4 | **0.17** | 🕐 The archetypal printed part |
| Camera / Limelight mount | Print | Intermediate | 2.0 | **0.3** | 2.3 | 0.15 | Angle matters; expect 2 revisions |
| Motor / gearbox mount plate | Print | Intermediate | 3.0 | **0.4** | 3.4 | 0.13 | Test-fit the bolt pattern first |
| Roller hub pair | Print | Intermediate | 2.5 | **0.4** | 2.9 | 0.16 | Press-fit coupon first (§3.6E) |
| Gripper jaw pair (rigid + TPU pads) | Print | Intermediate | 5.0 | **0.8** | 5.8 | 0.16 | Expect 3+ revisions; that IS the design |
| Control Hub / battery tray | Print | Intermediate | 4.0 | **0.7** | 4.7 | 0.18 | The goBILDA↔REV interface |
| Intake roller, full width | Print (TPU) | Intermediate | 5.0 | **1.0** | 6.0 | 0.20 | TPU is slow to print, not slow to design |
| Hood / chute / deflector (large) | Print | Advanced | 7.0 | **1.5** | 8.5 | 0.21 | Consider bent polycarbonate instead |
| **ROBOT SIGN set (2 per robot)** | Sheet + template | Novice | **1.0** | **0.5** | **1.5** | 0.50 | 🕐 **R401–R403 [C]. Do it in August** |
| Flat guard / shield | Sheet | Novice | 1.2 | **0.6** | 1.8 | 0.50 | With a jig: 0.4 h second |
| Bent deflector / hopper wall | Sheet + heat | Intermediate | 3.0 | **1.2** | 4.2 | 0.40 | Bend jig makes or breaks this |
| Electronics bellypan | Sheet, drilled via COTS plate | Novice | 2.0 | **0.8** | 2.8 | 0.40 | §4.4 rule 6 |
| Bumper / edge guard set | Sheet + TPU | Intermediate | 2.5 | **1.2** | 3.7 | 0.48 | |
| Chassis rail set (4 cuts + deburr) | Saw | Novice | 2.0 | **0.9** | 2.9 | 0.45 | **0.5 h if cut in the same session** |
| Superstructure uprights | Saw | Novice | 1.8 | **0.8** | 2.6 | 0.44 | |
| Tapping 10 × M4 in aluminium | Tap | Intermediate | 1.2 | **1.2** | 2.4 | **1.00** | 🕐 **No duplication discount at all.** Argues for through-holes + nuts |
| Chain loops sized and joined (×2) | Chain tool | Novice | 0.7 | **0.5** | 1.2 | 0.71 | |
| **Full wiring harness** | Assembly | Intermediate | 5.0 | **3.0** | 8.0 | 0.60 | Harness board (§4.5) drops second to ~2.0 h |
| **Drivetrain assembly (from cut parts)** | Assembly | Intermediate | 8.0 | **4.5** | 12.5 | 0.56 | Legal to build now — **R304 [C]** |
| **OPERATOR CONSOLE box** | Sheet/print + assembly | Intermediate | 4.0 | **1.5** | 5.5 | 0.38 | R901–R903 are final; build now |
| **A drill jig** | Print or ply | Intermediate | 1.0 | — | 1.0 | — | 🕐 **Pays for itself on the second part, every time** |
| **An assembly fixture (chassis)** | Ply + printed locators | Advanced | 3.0 | — | 3.0 | — | Two square, identical chassis |

### 8.3 What the ratios tell you [D]

| Method | Typical ratio | Meaning |
|---|---|---|
| **3D printing** | **0.13 – 0.25** | The second robot's part costs ~15–25% of the first. **This is the duplicability argument, quantified** |
| **Jig-made sheet work** | 0.35 – 0.50 | Good, if and only if the jig exists |
| **Sawn stock, same session** | 0.25 – 0.45 | Same session is doing the work, not the tool |
| **Assembly** | 0.55 – 0.65 | Assembly is inherently repeated labour; only practice helps |
| **Hand tapping / hand fitting** | **0.9 – 1.0** | 🕐 **No discount. Design it out** |

**[D] Worked example — the argument in one number.** A mechanism with 10 printed parts, 3 sheet parts,
2 sawn members and 8 tapped holes:
- **Printed:** ~25 h first, ~4 h second → 29 h
- **Sheet (jigged):** ~6 h first, ~2.5 h second → 8.5 h
- **Sawn (same session):** ~3 h first, ~1.3 h second → 4.3 h
- **Tapping:** ~1 h first, ~1 h second → 2 h
- **Total ≈ 44 h for both robots**, of which **only ~9 h is the second robot.**
Redesign the same mechanism with 6 hand-fitted aluminium parts instead of 6 of the prints and the second
robot's share jumps from ~9 h to ~25 h — **an extra ~16 student-hours, or roughly half a week of this
program's entire fabrication capacity, for zero performance gain.**

### 8.4 The BOM LABOR block to emit for every mechanism

```
LABOR (student-hours)
  First article (robot A) : ____ h
  Duplication (robot B)   : ____ h
  Jigs/fixtures (one-off) : ____ h
  TOTAL                   : ____ h
  Duplication ratio       : ____   (target < 0.35; > 0.6 needs justification)
  Weeks at 25-40 fab-h/wk : ____
```

🕐 **[J] Flag any mechanism whose duplication ratio exceeds 0.6 in a design review.** It is not necessarily
wrong — a wiring harness is legitimately 0.6 — but it means the second robot is expensive, and for this
program that is the number that decides whether the B team competes with the same machine or a worse one.

---

## 9. DESIGN-FOR-FABRICATION RULES OF THUMB

**[J] Print this section on one page and put it on the wall. These are the rules that make a student's CAD
model into a part their own shop can actually produce, twice.**

### 9.1 Universal — applies to every custom part

1. **If it cannot be made twice, it is not designed yet.** (§2.4)
2. **Design the tolerance out, not the tolerance in.** Slots instead of holes. Clearance instead of fit.
   Adjustment instead of precision. You have no mill; stop pretending you do.
3. **Put adjustment in one axis per joint** — a slot, a shim stack, a turnbuckle. A part that can be
   adjusted can be built imprecisely and still work.
4. **Bolt to a COTS pattern wherever possible.** goBILDA's 8 mm/32 mm patterns and REV's extrusion patterns
   are free accuracy. A custom part that mates to a catalogue hole pattern is a solved alignment problem.
5. **Never design a part that needs a hole closer than 2× its diameter to an edge** — it will crack in
   polycarbonate and tear out in printed plastic.
6. **Every fastener must be reachable with a straight or ball-end hex key.** Draw the tool in CAD if you
   have to. 🕐 **[J] "We can't get a driver in there" is discovered at 10 pm, twice.**
7. **Every part gets a part number and a home in the team repo**: `MECH-PARTNAME-rev`. The CAD, the STL/3MF,
   the drawing, and the jig live together. Robot B is built from files, not from memory.
8. **Deburr, chamfer, and break every edge** — **R201 [C]** makes this a rules issue, not a finish issue.
9. **Nothing may detach in a MATCH** — **R105 [C]** ("ROBOTS may not be designed to intentionally detach
   COMPONENTS") and **R201 [C]** ("any component not secured sufficiently … may be released on the FIELD").
   Retain every fastener; thread-lock or nylock everything that rotates or vibrates.
10. **No loops, no snag points, no open lattice at the perimeter** — **R202(I) [C]** entanglement.
11. **Design for powered-off removal** — **R203 [C]**. Every gripper needs a manual release.
12. **Weigh nothing.** **R104 [C]: there is no ROBOT weight limit in BIOBUZZ.** Do not compromise a part's
    strength to save 40 g. *(Do still consider the manual's listed side effects: TILE damage, battery
    consumption, transportation, performance.)*
13. **Fit in the cube.** **R102 [C]: 18 × 18 × 18 in. (45.70 cm) STARTING CONFIGURATION, fully self-contained
    and stationary.** Build an 18-inch sizing box out of ply **in August** and check every sub-assembly
    against it as you go. ⚠ **Expansion limits are DEFERRED TO KICKOFF (R105 [C]: "Sizing Constraints and
    more details will be released at Kickoff")** — so do not fabricate anything whose *length* depends on
    them yet.

### 9.2 3D-printed parts

14. **Load along layers, never across them.** (§3.4) Print L-brackets on their back.
15. **Walls before infill.** 4–6 walls is the FTC default; infill 25–40%. (§3.5)
16. **Fillet every internal corner, R2–R3 mm minimum.**
17. **Design for zero supports:** 45° overhang maximum, bridge ≤ 10 mm, put the flat face on the bed.
    Supports cost print time, surface quality and student patience — and every hour is doubled.
18. **Never print a load-bearing thread.** Heat-set insert, captive nut, or through-bolt. (§3.6)
19. **Boss wall ≥ 2× insert OD; hole per the insert chart, not per guesswork.**
20. **Bearing pockets get a test coupon, once per printer per material.** (§3.6E)
21. **Keep parts under ~200 mm in the longest dimension** where you can — it fits every printer you own,
    prints faster, and warps less. **Split-and-bolt beats one huge print.**
22. **Add a printed-in part number and a revision letter** on a non-functional face. When two robots have
    different revisions, you will need to know which is which.
23. **Print two. Always.** (§2.4)

### 9.3 Sheet parts

24. **Polycarbonate, never acrylic.** (§4.2)
25. **Design for a straight-cut-and-drill workflow.** Curves are fine; internal cutouts are expensive by
    hand — put them on the printer instead.
26. **Every hole pattern that appears twice gets a jig.** (§4.5)
27. **Washer or a printed spreader under every fastener head on plastic.** Never clamp a bolt head directly
    onto thin sheet.
28. **Bend radius ≥ 6× thickness for cold bends.**
29. **Leave the protective masking on until final assembly.**

### 9.4 Cut stock

30. **Buy the length if the catalogue has it.** (§5.1)
31. **Cut between holes, never through one.** (§5.3)
32. **Cut both robots' parts in one session, off one stop block.** (§5.3)
33. **Prefer through-holes + nylock nuts to tapped holes** — tapping has a 1.0 duplication ratio. (§8.3)
34. **Buy shafts to length; don't cut hardened stainless if you can avoid it.** (§5.6)

### 9.5 The final test — say it out loud in design review

> 🕐 **"Can two students of average skill, using only the tools in our shop, make TWO of this part in one
> Saturday — without the mentor?"**
>
> **If no: redesign, or buy it.** That is the whole file in one sentence.

---

## 10. Shop safety, and the R-rules that are really fabrication-quality rules

**[J] Non-negotiables for a school shop with 15 students:**

- **Eye protection for everyone in the room whenever anything is cut, drilled or ground** — not just the
  person holding the tool. One pair per student, not one per team.
- **Clamp the work. Never hand-hold a part being drilled.** A drill bit grabbing a small polycarbonate part
  turns it into a spinning blade — this is the most likely injury in this shop.
- **Tie back hair, no loose sleeves, no gloves near rotating tools** (gloves pull hands in).
- **A mentor present for the saw, the drill press, and any powered cutting.** Full stop.
- **Ventilation for ABS/ASA printing and for any heat-forming of plastic.** Print in a ventilated space;
  an enclosed printer helps but is not a fume extractor.
- **Respirator for FR4/G10 dust** if you ever use it (§4.2).
- **Soldering irons live in a stand, and the stand lives away from the edge of the bench.**
- **Battery safety is a separate discipline** — see `LEGAL-PARTS-CONSTRAINTS.md` §6. **R601 [C]:** never
  modify the battery.
- **First aid kit, stocked, and everyone knows where it is.**

**The four R-rules that fail at inspection because of shop workmanship, restated as a pre-inspection
checklist [C]:**

| Check | Rule |
|---|---|
| No exposed sharp edges or sharp protrusions anywhere on the robot | **R201** |
| No abrasive surfaces that will scratch SCORING ELEMENTS | **R201** |
| No unsecured components that could be released on the FIELD; no loose ballast | **R201** |
| No excessive lubricant that can spin off or drip | **R201** |
| No entanglement risks — cords, loops, open lattice | **R202(I)** |
| No hazardous or animal-based materials | **R202(E), R202(G)** |
| SCORING ELEMENTS and the ROBOT can be removed with power off | **R203** |
| Two ROBOT SIGNS, ≥90° apart, robust, ≥6.5 × 2.5 in., correct numerals, unpowered | **R401 / R402 / R403** |
| Robot fits the 18 in. cube, self-supported, stationary | **R102 / R103** |
| Wiring tidy and inspectable | **R606** |

---

## 11. Kickoff-day application procedure

**[J] How the review harness should use this file on 2026-09-12.**

**Before Kickoff — do this now, all of it legal under R304 [C]:**

| # | Action | Owner | Hours [J] |
|---|---|---|---|
| 1 | Buy and commission the printers; calibrate; run the press-fit coupons (§3.6E, §3.9) | build lead | 6–10 |
| 2 | Build the four slicer profiles and write them down (§3.9) | build lead | 2–3 |
| 3 | Buy the M4 Hardware Starter Pack, taps, cobalt bits, thread locker, tool sets (§6.1, §7.4) | mentor | 1 |
| 4 | **Make four ROBOT SIGNS + four spares** (R401–R403 [C], §1.6) | any student | 1.5 |
| 5 | Build the 18 in. sizing box from ply (R102 [C]) | any student | 1.5 |
| 6 | Build the parameterised CAD bracket library (§3.9) | CAD lead | 8–20 |
| 7 | Build the chassis assembly fixture and the harness board (§4.5) | build lead | 4–6 |
| 8 | Set up "A parts / B parts" bins and the two-bin kanban (§7.5) | any student | 2 |
| 9 | Set up the print queue board with **qty 2 as the default column** (§3.9) | build lead | 1 |
| 10 | Run one full practice part end-to-end: design → jig → two copies → deburr → inspect | whole team | 4 |

**On Kickoff day, for each candidate design:**

1. **Split the design into MAJOR MECHANISMS.** Use the sibling mechanism files.
2. **For each mechanism, split the parts list into BUY / FABRICATE** using §2.1, and score any contested
   part with §2.5.
3. **For every FABRICATE row, assign a method** (print / sheet / cut stock) and pull the hours from §8.2.
4. **Emit the LABOR block** (§8.4) and compute the duplication ratio. 🕐 **Flag ratio > 0.6.**
5. **Check the total against the calendar** (§2.6). If it does not fit, the design does not fit — say so
   in the review, with the number.
6. **Check every fabricated part against §9**, and every mechanism against the §10 inspection checklist.
7. **Confirm the actuator budget** against `LEGAL-PARTS-CONSTRAINTS.md` §3 — **8 motors + 8 servos, R503
   [C]** — before spending an hour on any fabrication estimate. A design that fails 8+8 does not need a BOM.
8. **Re-verify every price and stock status.** Everything here is dated **2026-08-22** and the Sept–Oct
   spike is documented in `VENDOR-ECOSYSTEMS.md` §5.2.

---

## 12. Open questions — the NEEDS-SKU-CHECK / UNVERIFIED register

| # | Item | What is missing | Why it matters | How to close it |
|---|---|---|---|---|
| 1 | **Heat-set inserts (M3, M4)** | No SKU, no price | §3.6's core technique has no orderable row | Load a McMaster-Carr insert page (named by the VERIFIED MatterHackers guide) and record size chart + SKU |
| 2 | **Aluminium sheet / plate / bar** | **No price from any loaded page** | Four suppliers 403'd (`onlinemetals`, `metalsdepot`, `homedepot`, `acmeplastics`) | Call a local metal supplier; they meet the VENDOR test (`LEGAL-PARTS-CONSTRAINTS.md` §8.2) |
| 3 | **Bambu Lab A1 / A1 mini price** | Specs VERIFIED, price not on the loaded page; `bambulab.com` 403, `store.bambulab.com` 402 | The likely best budget-to-capability printer | Load the MatterHackers A1 SKU pages directly, or call |
| 4 | **Digital caliper price** | SEARCH-SNIPPET only (≈$9.99 / ≈$24.99, items 63586 / 63711); product pages 403'd | Tier 1 tool | Re-fetch when Harbor Freight is not rate-limiting |
| 5 | **Portable band saw price** | SEARCH-SNIPPET only (BAUER item 64194, ≈$120); page 403'd | Tier 2 rank 4 | Same |
| 6 | **REV `REV-41-7537` and `REV-21-3410` prices** | SKUs VERIFIED; individual prices not shown (family range $11.00–$75.00 VERIFIED) | Gridded sheet is a real hand-layout time-saver | Load each product page |
| 7 | **goBILDA `3201-0004-0001` stock status** | Listed at $54.99 today; `VENDOR-ECOSYSTEMS.md` recorded **out of stock 2026-08-21** | Fasteners stock out first | Re-check before ordering |
| 8 | Hardened nozzles, spare PEI plates, insert tips, finishing tools | FAMILY-ONLY | Tier 1/2 consumables | Load the printer vendor's accessory pages |
| 9 | HDPE/UHMW and Baltic birch pricing | FAMILY-ONLY | Jig and wear-surface material | Local supplier |
| 10 | **Print-time figures in §3.7** | **[J] estimates, not measured** | They drive the throughput argument | Slice five representative parts on your actual printer and replace the column with measured numbers |
| 11 | **Student-hour figures in §8.2** | **[J] estimates** | They drive the LABOR column | Log actual hours on the first three parts of build season and recalibrate |
| 12 | Bambu X1-Carbon Combo at **$999.00** | VERIFIED but flagged "reduced from $1,249.00" | A promotional price may not hold | Re-check before purchase |

---

## 13. Verification log — every URL loaded in this session

**Manual text (grepped directly from `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`,
2026-08-22):** R102, R103, R104, R105 · R201, R202, R203, R204 · R301, R302, R303, R304, R305 ·
R401, R402, R403 · R504, R505, R506 · R801. The **R304/R305** and **R504/R505** label-interleaving artifacts
were observed directly in the text and are documented in §1.3.

**Vendor pages — LOADED AND READ (VERIFIED rows draw only on these):**

| URL | What it produced |
|---|---|
| `https://www.gobilda.com/tools/` | Full tool list with SKUs and prices (taps, cobalt bits, chain tool, snap-ring pliers, hex keys, Wera items, 12-piece M4 set) |
| `https://www.gobilda.com/screws/` | Bundle SKUs + prices; **M3/M4/M5 with M4 primary** |
| `https://www.gobilda.com/thread-locker/` | Loctite Blue 242 6 mL `2922-0001-0001` **$7.99** |
| `https://www.gobilda.com/hardware/` | Hardware subcategory list (no prices shown) |
| `https://www.gobilda.com/structure/` | Structure subcategory list (no prices shown) |
| `https://www.revrobotics.com/ftc/` | FTC bundles + **Polycarbonate Sheets $11.00–$75.00**, M3 Nuts $6.00–$8.75 |
| `https://www.revrobotics.com/Polycarbonate-Sheets/` | `REV-41-3049-PK5` 1 mm 400×350 5-pack **$11.00**; `REV-41-7537` 2 mm 8 mm-grid; `REV-21-3410` 3 mm 1/2 in.-grid 1194×584 |
| `https://www.revrobotics.com/ftc/structure/material/` | Polycarbonate $11.00–$75.00; MAXComposite `REV-21-3098` $150.00–$225.00 |
| `https://www.eplastics.com/LEXAN-CLR-0-125AM24X48` | 1/8 in. × 24 × 48 in. clear PC, SKU `PCCLR0.125AM24X48`, **$44.21** |
| `https://www.eplastics.com/LEXAN-CLR-0-060AM24X48` | 1/16 in. × 24 × 48 in. clear PC, SKU `PCCLR0.060AM24X48`, **$26.92** |
| `https://www.eplastics.com/polycarbonate/sheets` | Cut-to-size confirmed; sheet sizes; no prices |
| `https://www.prusa3d.com/category/3d-printers/` | MINI+ $508.33 · MK4S $657.40 kit / $925.00 · CORE One+ $925.00 kit / $1,202.78 · CORE One L+ $1,850.93 · XL+ $2,128.70 |
| `https://www.matterhackers.com/store/c/bambu-lab-3d-printers` | P1S bundles **$969.00**; P1S Combo bundles **$1,219.00**; X1-Carbon Combo **$999.00**; H2S Combo $1,399.00; A1 8-pack $4,800.00 |
| `https://www.matterhackers.com/store/l/bambu-lab-p1s-3d-printer/sk/MU1E513G` | P1S: 256³ mm, **enclosed**, PLA/PETG/TPU + ABS/ASA/PA/PC |
| `https://www.matterhackers.com/store/l/bambu-lab-a1-combo-3d-printer/sk/MK86YM0Y` | A1: 256³ mm, **"NOT recommended to enclose"**; price not shown |
| `https://www.matterhackers.com/store/c/creality-3d-printers` | **Ender-3 V3 SE $179.00**; Ender-5 Max $749.00; K2 Pro $849.00 / Combo $1,049.00; **SpacePi x4 dryer $179.00** |
| `https://www.matterhackers.com/store/c/3d-printer-filament` | PETG from $14.99 · ABS from $14.24 · Nylon from $31.69 · PC $101.00 |
| `https://www.matterhackers.com/store/c/3d-printers` | Catalogue scale only (80+ printers; Creality range $179–$1,949) |
| `https://www.matterhackers.com/store/c/bambu-lab` | Bambu filament range **$17.99–$3,749.00** |
| `https://www.matterhackers.com/articles/fasteners-for-3d-printing` | Heat-set insert technique; McMaster-Carr named as the sizing-chart source |
| `https://shop.polymaker.com/collections/pla` | Panchroma Matte PLA $18.99 · PolyLite PLA Pro $23.99 |
| `https://shop.polymaker.com/collections/petg` | Polymaker PETG $18.99 · PolyLite Translucent $19.99 · Fiberon PETG-rCF08 $19.99 · PolyMax PETG $29.99 |
| `https://shop.polymaker.com/collections/abs` | PolyLite ABS $18.99 · ABS Pro $24.99 · ABS Max $29.99 · PC-ABS $49.99 |
| `https://shop.polymaker.com/collections/nylon` | PA6-CF20 $39.99 · PA6-GF25 $29.99 · PA612-CF15 $34.99 · PA12-CF10 $69.99 · CoPA $49.99; annealing 80–100 °C / 6–16 h |
| `https://shop.polymaker.com/collections/flexible` | TPU95 $29.99 · TPU90 $39.99 · TPU95-HF $49.99 |
| `https://shop.polymaker.com/collections/polycarbonate` | PolyLite PC $29.99 · PolyMax PC $38.99 · PC-ABS $49.99; annealing 90 °C / ≥2 h |
| `https://www.harborfreight.com/8-in-5-speed-bench-drill-press-with-light-58780.html` | BAUER 8 in. 5-speed, **$89.99** (from $109), 1/2 in. keyed chuck, 750–3200 RPM |
| `https://www.harborfreight.com/power-tools/drills-drivers/drill-presses.html` | 8 in. $89.99 · 10 in. $169.99 · 12 in. $299.99 · 17 in. $499.99 |
| `https://www.harborfreight.com/search?q=metric+tap+and+die+set` | PITTSBURGH Metric 40-pc **$24.99** · SAE+Metric 60-pc $42.99 · WARRIOR 13-pc $19.99 · ICON 41-pc $149.99 |

**Fetch attempts that FAILED — recorded so no row silently depends on them:**

| URL | Result |
|---|---|
| `https://us.store.bambulab.com/collections/3d-printer` | **HTTP 402** |
| `https://bambulab.com/en-us/a1` | **HTTP 403** |
| `https://www.tapplastics.com/product/plastics/cut_to_size_plastic/polycarbonate_sheets/512` | **HTTP 403** |
| `https://www.homedepot.com/b/...Polycarbonate-Sheets/N-5yc1vZcbtd` | **HTTP 403** |
| `https://www.onlinemetals.com/en/buy/polycarbonate` · `/aluminum` | **HTTP 403** (both) |
| `https://www.metalsdepot.com/aluminum-products/aluminum-sheet` | **HTTP 403** |
| `https://www.acmeplastics.com/polycarbonate-sheet` | **HTTP 403** |
| `https://www.harborfreight.com/6-in-digital-caliper-63711.html` | **HTTP 403** (rate-limited) |
| `https://www.harborfreight.com/10-amp-5-in-deep-cut-variable-speed-band-saw-64194.html` | **HTTP 403** (rate-limited) |
| `https://www.harborfreight.com/search?q=portable+band+saw` | **HTTP 403** |
| `https://www.harborfreight.com/power-tools/saws/band-saws.html` · `/hand-tools/taps-dies.html` | **HTTP 404** |
| `https://www.revrobotics.com/rev-21-3410/` | **HTTP 404** |
| `https://us.polymaker.com/collections/all-filaments` | **301** → `shop.polymaker.com` (followed) |
| `https://shop.polymaker.com/collections/all-filaments` · `/abs-asa` · `/tpu` · `/pc` | **HTTP 404** (correct paths found and loaded instead) |
| `https://www.matterhackers.com/store/c/PETG` · `/bambu-lab-a-series-3d-printers` | Loaded but returned no product rows |

**Official FIRST supplier status:** see `VENDOR-ECOSYSTEMS.md` §2.0. **[J] Note for this file specifically:**
ePlastics, MatterHackers, Polymaker, Harbor Freight and local metal suppliers are **general suppliers, not
FIRST suppliers** — which is fine, because **the VENDOR test in the V0 definitions (Federal Tax ID, not
team-owned, adequate stock, available to all teams — `LEGAL-PARTS-CONSTRAINTS.md` §8.2) is what the rules
actually require**, and all of them meet it. Nothing in Section 12 restricts where raw material comes from.

---

*End of `IN-HOUSE-FABRICATION.md`. Written 2026-08-22. Every price VERIFY-BEFORE-ORDER. Every [J] is an
opinion calibrated to a 15-student, two-robot, no-mill program — argue with it, but argue with the numbers
in §8.*
