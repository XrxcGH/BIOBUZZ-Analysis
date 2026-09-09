# INTAKE, TRANSFER & END EFFECTORS — mechanism catalog

### How a ROBOT acquires, moves and releases a SCORING ELEMENT — organized by ELEMENT GEOMETRY so it can be applied on Kickoff morning, broken into BUY vs FABRICATE for a two-robot program

---

**Status:** written 2026-08-22, **21 days before Kickoff (2026-09-12)**.
**Legality source of truth:** BIOBUZZ V0 `Section 12 ROBOT Construction` — **FINAL, not a placeholder**.
**Game source of truth:** does not exist yet. Sections 8, 9, 10, 11, 13 and 15 are V0 PLACEHOLDERS.

**Read first, do not duplicate:**
`reference/VENDOR-ECOSYSTEMS.md` (who to buy from, the interoperability map, procurement calendar) ·
`reference/LEGAL-PARTS-CONSTRAINTS.md` (the purchasing envelope, Tables 12-1/12-2, the 8+8 budget).
This file cross-references both rather than repeating them.

**Sibling mechanism files:**
`DRIVETRAIN-AND-ODOMETRY.md` · `EXTENSION-ARMS-LIFTS.md` (what carries the end effector through space) ·
`LAUNCHERS-AND-FEEDING.md` (§9 covers hoppers / indexers / kickers **in the launcher feed chain**;
this file covers the same hardware **in the intake-to-scoring chain** and cross-references rather than
restating) · `ELECTRONICS-AND-SENSING.md`.

---

## Contents

- [0. How to read this file](#0-how-to-read-this-file)
- [1. The legality envelope for anything that touches a SCORING ELEMENT](#1-the-legality-envelope-for-anything-that-touches-a-scoring-element)
- [2. THE KICKOFF ENTRY POINT — element geometry decision table](#2-the-kickoff-entry-point--element-geometry-decision-table)
- [3. The physics you must be able to compute before you buy](#3-the-physics-you-must-be-able-to-compute-before-you-buy)
- [4. I-1 — Active roller intake (compliant wheels)](#4-i-1--active-roller-intake-compliant-wheels)
- [5. I-2 — Flex / silicone roller and tube-sleeve intake](#5-i-2--flex--silicone-roller-and-tube-sleeve-intake)
- [6. I-3 — Surgical tubing flail intake](#6-i-3--surgical-tubing-flail-intake)
- [7. I-4 — Star roller and flap-wheel intake](#7-i-4--star-roller-and-flap-wheel-intake)
- [8. I-5 — Brush roller intake](#8-i-5--brush-roller-intake)
- [9. I-6 — Passive intakes: funnels, wedges, one-way gates, gravity feeds](#9-i-6--passive-intakes-funnels-wedges-one-way-gates-gravity-feeds)
- [10. E-1 — Servo claw (two-jaw gripper)](#10-e-1--servo-claw-two-jaw-gripper)
- [11. E-2 — Linkage and parallel-jaw grippers](#11-e-2--linkage-and-parallel-jaw-grippers)
- [12. E-3 — Compliant "finger" grippers](#12-e-3--compliant-finger-grippers)
- [13. E-4 — Over-center latches and zero-actuator retention](#13-e-4--over-center-latches-and-zero-actuator-retention)
- [14. E-5 — Suction and vacuum: ILLEGAL in BIOBUZZ](#14-e-5--suction-and-vacuum-illegal-in-biobuzz)
- [15. T — TRANSFER AND INDEXING, and how to not jam](#15-t--transfer-and-indexing-and-how-to-not-jam)
- [16. Servos vs motors for manipulation](#16-servos-vs-motors-for-manipulation)
- [17. Compliance and alignment — the forgiveness budget](#17-compliance-and-alignment--the-forgiveness-budget)
- [18. IN-HOUSE FABRICATION — the most 3D-printed subsystem in FTC](#18-in-house-fabrication--the-most-3d-printed-subsystem-in-ftc)
- [19. The two-robot duplication protocol and the spares kit](#19-the-two-robot-duplication-protocol-and-the-spares-kit)
- [20. Kickoff-day application procedure](#20-kickoff-day-application-procedure)
- [21. Open questions — NEEDS-SKU-CHECK register](#21-open-questions--needs-sku-check-register)
- [22. Verification log](#22-verification-log)

---

## 0. How to read this file

### 0.1 Claim labels (matched to `LEGAL-PARTS-CONSTRAINTS.md` §0.1)

| Label | Meaning |
|---|---|
| **CONFIRMED-BIOBUZZ** | Read directly out of the BIOBUZZ V0 manual text this session, with rule ID and page. |
| **HISTORICAL** | From a prior season (INTO THE DEEP, DECODE). Informative, **not** authoritative for BIOBUZZ. |
| **JUDGMENT** | My engineering recommendation for *this* program: ~15 students, two robots, modest budget, 3D printers and hand tools, no CNC mill. |
| **DEFERRED TO KICKOFF** | Cannot be known before 2026-09-12 because it depends on the game. Flagged, never guessed. |
| **V0-GAP** | Something a prior season had that BIOBUZZ V0 does not state. |

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

| Tag | Meaning |
|---|---|
| **VERIFIED** | I loaded the vendor page with WebFetch **in this session (2026-08-22)** and read the SKU and price off it. Listed in §22. |
| **XREF-VERIFIED** | Not re-loaded by me. Verified by the Phase A agent with a logged page load and recorded in `VENDOR-ECOSYSTEMS.md` §9 or `LEGAL-PARTS-CONSTRAINTS.md` §15.3. Treated as second-hand but traceable. |
| **FAMILY-ONLY** | I verified the **product family and the category page**, but not an individual SKU or price. Buy from the category, confirm the SKU. |
| **MANUAL-SOURCED** | The part number comes from a BIOBUZZ Table (12-1 / 12-2). Legality is certain; commercial details are not. |
| **UNVERIFIED / NEEDS-SKU-CHECK** | Named for completeness. **Do not order on this row alone.** |

**Every price in this file is a list price as of August 2026 and is marked VERIFY-BEFORE-ORDER.**
Prices exclude tax, shipping, and the goBILDA/REV FTC team discounts (see `VENDOR-ECOSYSTEMS.md` §5.4).

### 0.3 A note on what this file can and cannot decide

The BIOBUZZ SCORING ELEMENT is unknown. **Nothing here tells you what to build.** What it does is:

1. make the *legality envelope* for manipulation explicit now, while Section 12 is final;
2. pre-load the *vendor families and SKUs* so a BOM can be produced in an hour on Kickoff day;
3. give a **geometry → mechanism** lookup (§2) so the moment you see the element, the candidate set collapses;
4. pre-compute the *fabrication and student-hour* cost of each option **doubled**, because everything is built twice.

---

## 1. The legality envelope for anything that touches a SCORING ELEMENT

Section 12 is final. Six rules shape every intake, transfer and end effector in BIOBUZZ. Four of them
eliminate whole classes of design. Read this section before you sketch anything.

### 1.1 ⚠ R203 — the rule that quietly kills half of all gripper designs

**CONFIRMED-BIOBUZZ, R203, p. 69**, grepped verbatim from `12_RobotConstruction_R_p64-88.txt`:

> **R203** \*ROBOTS must be designed to be quickly removed from the FIELD without requiring power. ROBOTS
> must allow **removal of SCORING ELEMENTS from the ROBOT** and the ROBOT from FIELD elements **while
> powered off**.
>
> Blue box: *"Some events may allow teams to use ROBOT power during FIELD reset (e.g., driving a ROBOT to
> the edge of the FIELD) but ROBOTS should be designed such that this is not required."*

**What this means for manipulation, stated bluntly:** a gripper that holds the element when the robot is
dead is **illegal**. That rules out, as the primary retention mechanism:

| ❌ Retention that fails R203 | Why |
|---|---|
| Worm-gear or high-ratio non-backdrivable gripper drive that clamps and stays clamped unpowered | A FIELD RESET volunteer cannot get the element out |
| Ratchet or one-way bearing used to hold a jaw closed on the element | Same — and a ratchet is otherwise legal (R303.H), so this is an easy trap to fall into |
| An over-center latch with no manual release | Legal *only* if a human can pop it by hand without tools |
| A tube/magazine whose exit is blocked by an unpowered servo-held gate with high holding torque | The element is trapped inside the robot |
| Deep, undercut printed jaws that mechanically capture the element | Geometry, not power, does the trapping — still fails "removal … while powered off" |

**What passes R203:**

| ✅ Retention that passes | Why |
|---|---|
| Spring- or elastic-clamped jaws sized so a hand can pull the element out against the spring | Compliance is the release mechanism |
| Compliant TPU fingers | The element pulls free by deforming the fingers |
| Roller/flail retention (rollers freewheel or backdrive when unpowered) | Nothing holds |
| Gravity-retained hopper with an open or hand-openable exit | Nothing holds |
| Over-center latch **with an exposed manual release tab** | Human-openable, no tools |
| Servo claw driven by a standard servo with the jaws **backdrivable by hand** | A 25T-spline servo at typical gearing backdrives with firm finger pressure — **test this, do not assume it** |

**JUDGMENT — make this an explicit inspection test in your own build process.** Before any end effector is
called done: load an element, kill the main breaker, and have a student who did not build it remove the
element with two hands and no tools in under five seconds. If they cannot, the design is not legal, it is a
FIELD RESET delay, and it will be caught. This is a five-minute test that has to be run **twice**, once per
robot, and it is the single highest-value legality check in this file.

### 1.2 ⚠ R801 — no vacuum, no suction, no blowers. Rollers and flywheels are explicitly fine.

**CONFIRMED-BIOBUZZ, R801, p. 87**, grepped verbatim:

> **A.** ROBOTS may only use sealed, COTS closed-air systems which are **pre-charged by the manufacturer**
> (such as gas shocks), **B.** no stored-pressure components actuated by a device like a solenoid or able to
> change their stable state, **C.** *"ROBOTS may not generate pressure or vacuum,"* **D.** no
> user-adjustable gas storage vessels, except air-filled (pneumatic) COTS wheels, **E.** no device which
> creates high-speed airflow, except cooling fans integrated into COTS computing devices.

And the blue box, which is the sentence that matters most for this file:

> *"Examples of a 'device which creates high-speed airflow' include but are not limited to a fan designed to
> move SCORING ELEMENTS on the FIELD. **High-speed flywheels or rollers used for manipulating SCORING
> ELEMENTS would not on their own be considered a high-speed airflow device.**"*

Reinforced by **R204** (p. 69): *"No grabbing the floor. ROBOTS may not use any mechanism which is designed
to increase downforce by either grabbing FIELD surfaces or by using some form of generated airflow to
provide downward suction."*

**Consequences for this file:**

- **Suction cups, venturi grippers, vacuum end effectors: prohibited. Do not propose them.** See §14.
- **Pneumatic cylinders as gripper actuators: prohibited.** There is no compressed-air gripper in BIOBUZZ.
- **Roller and flywheel intakes are explicitly sanctioned by name.** Spin them as fast as you like; the
  limit is R201 (damage) and R202 (safety), not R801.
- **Gas springs and dampers are legal** and are the sanctioned zero-actuator-slot energy store — useful for
  passive intake deploy (§9) and for gravity compensation on a gripper arm.

### 1.3 R506 — no relays, no electromagnets, no electrical solenoids

**CONFIRMED-BIOBUZZ, R506, p. 78**, grepped verbatim:

> *"The use of relays, electromagnets, and electrical solenoid actuators is prohibited. The application of
> electromechanical actuation through the use of additional relays, electromagnets, electrical solenoid
> actuators, or related systems is prohibited."*

**Consequence:** an electromagnetic gripper is illegal, and so is a solenoid-fired latch, a solenoid kicker
and a relay-switched intake. **Permanent magnets are a different thing and are explicitly legal** — R302
lists **magnets** as an allowed raw material (p. 70, item D). A passive magnetic detent, a magnetic element
retainer or a magnetic alignment feature costs **zero actuator slots** and is legal, provided it still
satisfies R203 (a hand must be able to pull the element off the magnet).

### 1.4 R301 / R303 / R101 — can you just buy a gripper? Mostly no, with one real exception.

Three rules interlock here. All **CONFIRMED-BIOBUZZ**, grepped verbatim this session:

**R101 (p. 66):** *"The ROBOT and its MAJOR MECHANISMS must be built by the FIRST Tech Challenge team…"* and
the definition that matters: *"A **MAJOR MECHANISM** is a group of COMPONENTS and/or MECHANISMS assembled
together to address at least 1 game challenge: ROBOT movement, **SCORING ELEMENT manipulation**, FIELD
element manipulation, or performance of a scorable task…"* — **an intake is, by definition, a MAJOR
MECHANISM.** The carve-outs (p. 66) are *"A. a gearbox assembly, B. a COMPONENT or MECHANISM that is part of
a MAJOR MECHANISM, or C. COTS items."*

**R301 (p. 69):** *"**COTS MAJOR MECHANISMS purposefully designed to complete a game task are prohibited.**"*
Exceptions: **A.** COTS drive CHASSIS, **B.** COTS MAJOR MECHANISMS created as part of the official FIRST
Tech Challenge **StarterBots**. Blue box: *"A vendor selling 'build to print' manufacturing of publicly
available, purpose-built solutions is against the spirit of this rule."*

**R303 (pp. 70-71):** COTS components and mechanisms must not exceed a single degree of mechanical freedom.
Explicitly allowed single-DoF COTS items include **G. single DoF gripper**. Explicit exceptions to the
single-DoF cap include **H. ratcheting devices**, **I. holonomic wheels**, **J. dead-wheel odometry kits**,
**K. items that transfer motion between misaligned COMPONENTS** (universal joints, flexible couplers), and
items connecting structures at variable angles (ball joints, rod ends).

**The resulting shopping map for manipulation:**

| ✅ You may buy this | ❌ You may not buy this |
|---|---|
| A **single-DoF COTS gripper** (R303.G) — e.g. the ServoCity gripper kits in §11 | A gripper with an added wrist/twist actuator — R303 blue box calls this out explicitly |
| Rollers, wheels, flap wheels, stars, tubing, bearings, hubs, shafts, chain, belt — all **COMPONENTS** | A vendor's purpose-built BIOBUZZ intake or scorer, if one appears after Kickoff |
| A **single-speed gearbox**, pulley, turntable, lead screw, linear actuator kit | A "build-to-print" copy of somebody's published intake, bought from a shop |
| The **official FIRST / vendor StarterBot** mechanisms (R301.B) — including their intakes | — |
| Ball-joint linkages and rod ends (R303.K/L) for gripper linkages | — |

**JUDGMENT — the honest reading of the COTS gripper allowance.** R303.G says a single-DoF COTS gripper is a
legal COTS *mechanism*. R301 says a COTS *MAJOR MECHANISM purposefully designed to complete a game task* is
prohibited. A generic gripper kit sold for years before BIOBUZZ existed is not "purposefully designed to
complete a game task," so buying one is defensible. But if that bought gripper **is** your entire scoring
manipulator, you have handed a judged-award panel a story where the answer to "how did you design your end
effector?" is "we bought it," and you are one INSPECTOR's reading of R101 away from an argument on Saturday
morning. **Recommendation: buy one ServoCity gripper kit for the program as a reference and a B-team
fallback ($29.99–$34.99, §11), and design and print your own jaws onto it or beside it.** Note the R303
blue-box trap while you are there: *"grippers that incorporate additional actuators providing additional
twisting and/or bending actions (like a wrist) add degrees of freedom that are prohibited in COTS
MECHANISMS"* — the moment you bolt a wrist servo to a bought gripper, the assembly is no longer a legal
single-DoF COTS mechanism unless you built the combination yourself, which of course you did. Document that
in your Engineering Portfolio.

**File a Game Q&A on this the day Q&A opens (2026-09-28, 12:00 p.m. ET)** if your design leans on a bought
gripper. See `VENDOR-ECOSYSTEMS.md` §5.5 for the calendar.

### 1.5 R201 / R202 — damage, mess and entanglement, which is where aggressive intakes get caught

**CONFIRMED-BIOBUZZ, R201, p. 68:** *"ROBOTS should be designed so they don't damage anything or make a mess
in the ARENA."* The blue box is specific and directly aimed at intakes:

> *"SCORING ELEMENTS are expected to undergo a reasonable amount of wear and tear as they are handled by
> ROBOTS, such as scratching or marking. **Gouging, tearing off pieces, or routinely and repeatedly marking
> SCORING ELEMENTS are violations of this rule…**"*

and lists as damage-risk features *"components with exposed sharp edges or sharp protrusions"* and
*"features with abrasive surfaces that scratch objects that rub across them."*

**CONFIRMED-BIOBUZZ, R202, p. 68-69**, item **I**: *"devices or conditions that pose an unnecessary risk of
**entanglement**."*

**Consequences, mechanism by mechanism:**

| Mechanism | R201/R202 exposure | Mitigation |
|---|---|---|
| Surgical tubing flails (§6) | Highest. Long free-flailing tubing is the classic entanglement-question mechanism, and tubing ends fray and shed rubber = "making a mess" | Keep flails short (≤ ~1.5× roller radius), cap or knot the ends, inspect for fraying every event, carry spares |
| Brush rollers (§8) | Bristles shed. Loose bristles on the TILE are litter under R201 | Use bonded/staple-set industrial brush, not a household broom head; trim, do not tear |
| Abrasive/grip-tape rollers | Directly named — *"abrasive surfaces that scratch objects"* | Do not use grip tape or sandpaper on anything that touches a SCORING ELEMENT. Use silicone/urethane/TPU |
| 3D-printed jaws with sharp tooling marks | *"exposed sharp edges or sharp protrusions"* | Chamfer or fillet every element-contacting edge in CAD, then deburr the print |
| High-speed flywheel intakes | Explicitly **not** an airflow device (R801 blue box), but a fast exposed wheel is a pinch hazard under R202 | Guard the nip point with a printed or polycarbonate shroud |

### 1.6 R503 — the 8 + 8 budget, applied to manipulation

**CONFIRMED-BIOBUZZ, R503, p. 77**, grepped verbatim this session:

> *"ROBOTS are limited to a total of 8 motors and 8 servos. A ROBOT may not have more than 8 motors and 8
> servos from the allowable actuator lists per R501 and R502 for all MECHANISMS used in all configurations."*

**This is a reduction from DECODE's 10 servos** (HISTORICAL) — see `LEGAL-PARTS-CONSTRAINTS.md` §3.2. Any
carried-over 2025-26 manipulator with 9 or 10 servos is now illegal.

Typical actuator cost of the mechanisms in this file (JUDGMENT, for budgeting):

| Mechanism | Motors | Servos | Notes |
|---|---|---|---|
| Single active roller intake | 1 | 0 | Or **0 + 1** if driven by a continuous-mode servo — see §16.3 |
| Dual counter-rotating roller intake | 1 | 0 | Both rollers off one motor via belt/chain — **do not spend two motors on this** |
| Intake deploy (drop-down) | 0 | 1 | Or **0 + 0** with a gas spring / passive deploy — see §9.4 |
| Transfer conveyor | 1 | 0 | Or share the intake motor with a one-way coupling |
| Single-file indexer | 0 | 1 | |
| Kicker / pusher | 0 | 1 | |
| Servo claw | 0 | 1 | |
| Claw + wrist | 0 | 2 | |
| Claw + wrist + rotate | 0 | 3 | ⚠ three servo slots for one hand — audit this hard |
| Passive funnel / wedge / gate | **0** | **0** | The reason §9 exists |

**JUDGMENT — the budget arithmetic that should govern your concept selection.** A 4-motor holonomic
drivetrain plus a 2-motor lift leaves **2 motor slots** for everything in this file. Two robots do not
change the per-robot limit, but they double the *cost* of every slot you spend. The two highest-leverage
moves in BIOBUZZ manipulation are therefore:

1. **Drive the intake with a servo in continuous mode instead of a motor** when the torque allows (§16.3) —
   converts a scarce motor slot into a plentiful servo slot, for $36.99 instead of $54.99.
2. **Make the deploy, the retention and the gating passive** — springs, gas springs, gravity, magnets and
   one-way gates cost **zero slots and near-zero dollars, times two robots** (§9, §13).

### 1.7 What is DEFERRED TO KICKOFF — do not guess these

| Unknown | Rule / section | Why it blocks intake design |
|---|---|---|
| **SCORING ELEMENT geometry, size, mass, surface, count** | Section 10 is a **PLACEHOLDER** | Determines roller spacing, jaw opening, compression, funnel width — i.e. every dimension in this file |
| **How many elements a ROBOT may control/possess** | Section 11 (G-rules) is a **PLACEHOLDER** | Determines whether you need a magazine at all, and how deep |
| **Expansion limits** | **R105** — *"Sizing Constraints and more details will be released at Kickoff"* (verbatim, p. 67) | Determines whether the intake may extend outside the frame, which is the single biggest intake-architecture fork |
| **FIELD geometry, wall heights, floor obstacles** | Section 9 is a **PLACEHOLDER** | Determines ground clearance and approach angle |

**What is knowable right now and should be built now under R304** (*"ROBOT software, designs, and FABRICATED
ITEMS created before Kickoff are permitted"*, p. 71 — see `LEGAL-PARTS-CONSTRAINTS.md` §8.6):
roller cartridges as a **parameterised CAD family** (not a fixed size), the printed-hub and side-plate
library, the servo/linkage hardware stock, test rigs, and the intake control code (deploy, run, reverse,
current-sense unjam). Do **not** cut a funnel or size a jaw yet.

**R102's 18-inch cube is final** (*"18 in. (45.70 cm) wide, by 18 in. long, by 18 in. high"*, p. 66) — so the
*stowed* envelope of the intake **is** knowable today. **R104 is final: there is no ROBOT weight limit in
BIOBUZZ** (p. 67), which is genuinely good news for intakes — a heavier steel-shafted roller cartridge with
real bearings costs you nothing in legality and buys reliability.

---

## 2. THE KICKOFF ENTRY POINT — element geometry decision table

This is the section to open at 12:05 p.m. on 2026-09-12. Identify the element geometry, read across.

### 2.1 Geometry → mechanism lookup

| Element geometry | Best first choice | Strong second | Avoid | Why |
|---|---|---|---|---|
| **Small spheres** (≲ 100 mm, e.g. ball-pit / whiffle / lacrosse scale) | **I-1 compliant-wheel roller**, over-bumper, single roller against a printed floor plate | **I-6 passive funnel** into a hopper — spheres self-feed better than anything else | Grippers (§10-12). Never grip a sphere you can roll | Spheres are the easiest geometry: they roll, they self-center in a V, and a single compliant roller sweeps a wide swath |
| **Large spheres** (≳ 150 mm) | **I-1 dual counter-rotating rollers** with a wide gap, or over-under rollers | **I-6 wedge + drive-in capture**, retained by gravity | Single small roller — it will ride over the ball instead of pulling it in | Large spheres need two contact points or the intake climbs the ball. Compression is small (2-5%) because the ball is stiff |
| **Cubes / blocks** | **I-1 roller with compliant wheels** at ≥ 2 contact rows, feeding a **single-file tube** | **E-1 servo claw** if the element must be *placed* precisely rather than dumped | Star rollers alone — a cube corner can wedge between star lobes | Cubes tumble; you must control orientation. Two rows of rollers spaced < the cube's short dimension prevents tumbling mid-path |
| **Discs / rings** | **I-4 flap-wheel or star roller** — thin elements need a "flick" not a "squeeze" | **I-1 roller with a floor ramp** to lift the leading edge, or a **compliant finger scoop** | Wide-gap dual rollers — a disc slips through unmoved | Flat elements lying on the floor are the hardest acquisition problem in FTC. The mechanism must generate a *lifting moment*, not just friction |
| **Cones** | **E-3 compliant finger gripper** dropped over the apex — self-centering, zero precision needed | **I-1 roller pair** at the cone's mid-diameter, or a printed funnel-cup that captures on descent | Two-jaw claws that must clock to the cone's axis | Cones self-center under a conical guide. Exploit that geometry — it is free alignment |
| **Irregular / soft / deformable** | **I-4 flap wheels** (REV explicitly sells these for *"irregular gamepieces"* — verified §7) | **I-3 tubing flails** or **I-8 brush**, both of which conform | Rigid parallel jaws — they will find the one orientation that squirts the element out | Irregular means you cannot predict the contact patch. Choose maximum compliance and accept lower speed |
| **Panels / plates** (flat, large, thin) | **E-2 parallel-jaw gripper** on the panel edge, or a **compliant pinch roller pair** | **Passive slot + gravity** — drive the slot onto the panel edge, drive away | Roller intakes that must lift a large flat face | A panel is grabbed by an *edge*, not a face. Parallel jaws keep the panel square as they close, which a pivoting claw does not |

### 2.2 The seven questions to answer about the element before you choose

Write the answers on the whiteboard at Kickoff. Every dimension in every table below derives from them.

1. **Max dimension and min dimension?** → path width (≥ 1.25 × max), roller spacing (< min).
2. **Mass?** → roller torque, jaw force, whether gravity alone can index it.
3. **Rigid or deformable?** → compression % (§3.2). Rigid = the *mechanism* compresses; soft = the *element* does.
4. **Does it roll, slide or tumble?** → whether you need orientation control or can dump.
5. **Surface: slick, tacky, textured?** → durometer choice (§3.3).
6. **How many must you carry, and does the manual limit it?** → magazine depth (**DEFERRED** — Section 11 is a placeholder).
7. **Where does it sit at rest — floor, rack, wall, human player?** → approach angle and ground clearance.

### 2.3 The three architectural forks, decided once

| Fork | Option A | Option B | JUDGMENT for this program |
|---|---|---|---|
| **Acquire by sweeping or by grasping?** | Roller intake — fast, forgiving, high cycle rate, poor placement precision | Gripper — precise placement, slow, needs alignment and usually a wrist | **Sweep if the game rewards volume; grasp if it rewards placement.** If both, the A-team does the harder one and the B-team does the simpler one — see §19 |
| **Intake inside or outside the frame?** | Inside the 18 in. cube always — always legal, low risk, small mouth | Deploys outside after MATCH start | **BLOCKED until Kickoff by R105.** Design the cartridge so it can bolt in either way. Build the inside-the-frame version first |
| **Store or score immediately?** | Through-path: acquire → transfer → score in one motion | Magazine: acquire → buffer → score on demand | Magazines are where seasons are lost to jams (§15). **Default to the shallowest buffer the game tolerates** |

---

## 3. The physics you must be able to compute before you buy

### 3.1 Roller surface speed — the number you actually control

For a roller of diameter *d* (m) at *N* rpm, the surface speed is

> **v = π · d · N / 60**  (m/s)

The element leaves the roller at roughly *v* when the roller is much heavier than the element and grip does
not slip. Worked, with parts verified in this file:

| Roller | Diameter | Motor (XREF `LEGAL-PARTS` §2.5) | Free rpm (HISTORICAL, typical) | Surface speed |
|---|---|---|---|---|
| goBILDA 3618 Intake Roller Wheel, 16 mm | 0.016 m | 5203 Yellow Jacket, 1150 rpm class | 1150 | ~0.96 m/s |
| goBILDA 3615 Boot-Wheel, 48 mm | 0.048 m | 5203, 435 rpm class | 435 | ~1.09 m/s |
| goBILDA 3613 Gecko, 96 mm | 0.096 m | 5203, 312 rpm class | 312 | ~1.57 m/s |
| REV DUO Compliant Wheel, 2 in (50.8 mm) | 0.0508 m | HD Hex + UltraPlanetary, ~300 rpm | 300 | ~0.80 m/s |

**JUDGMENT — target 1.5–3 m/s of surface speed at the element for a floor-sweeping intake, and 0.5–1.2 m/s
for a transfer or indexing roller.** Faster than ~4 m/s and a light element gets flung out of the intake
instead of pulled in; slower than ~1 m/s and the intake cannot outrun the drivetrain, so driving forward
pushes elements away rather than collecting them. **The intake surface speed must exceed the robot's
approach speed** — that is the whole trick, and it is the number rookies get wrong.

### 3.2 Compression — the grip budget

Compliant intakes work by *interference*: the gap between the roller and the opposing surface is set
**smaller** than the element, so the roller deforms and normal force appears.

> **Compression % = (element dimension − gap) / element dimension × 100**

| Element type | Target compression | Consequence if too low | Consequence if too high |
|---|---|---|---|
| Rigid, hard surface (cube, cone, plate) | **10–20 %** of the *wheel* radius, gap set from wheel deformation | Slips, no grip | Motor stalls, wheel wears fast, R201 marking risk |
| Rigid ball | **2–5 %** of ball diameter | Ball rides out | Ball jams and stalls the intake |
| Soft / deformable | **15–30 %** of element dimension | Slips | Element deforms permanently — R201 "gouging/tearing" exposure |

**Build the gap adjustable.** JUDGMENT: put the roller axle in a **slotted printed side plate** with two M4
bolts, so gap is a 30-second change, not a reprint. This one detail is worth more than any other in this
file, because you will be tuning compression at 11 p.m. the night before your first qualifier, twice.

### 3.3 Durometer — how to choose, with the verified options

Shore A hardness. Lower = softer = grippier = more compliant = wears faster.

| Durometer | Feel (REV's own wording, VERIFIED) | Use for |
|---|---|---|
| **30A** | *"like a rubber band"* — REV "Soft", light gray | Delicate/light elements; maximum forgiveness; highest wear |
| **35A** | AndyMark green — *"the softest, grippiest, and most compliant around objects"* | Floor sweeping of irregular elements |
| **40A** | REV "Medium" dark gray; AndyMark orange | **The default. Start here.** Good grip, acceptable life |
| **50A** | AndyMark blue | Faster rollers, heavier elements, longer life |
| **60A** | REV "Hard" black — *"like a tire tread"*; AndyMark black | Transfer/indexing rollers where you want low friction and long life |
| **80A** | AndyMark gray (Compliant Stars only) | High-rpm indexing, minimal deformation |

**JUDGMENT — buy 40A first, and buy one set of 30/35A and one set of 50/60A as tuning stock.** Durometer is
the cheapest tuning knob you own (a 4-pack is $6.20–$19.50) and the only one that cannot be adjusted in CAD.
For **two robots, buy the tuning stock once and share it** — but buy the *final chosen* durometer twice.

---

## 4. I-1 — Active roller intake (compliant wheels)

### 4.1 What it is and when a design needs it

A powered shaft carrying compliant wheels, spun so its surface speed exceeds the robot's approach speed,
pulling elements off the floor or off a rack and into the robot. It is the default FTC intake and the
correct starting point for **small spheres, large spheres, cubes and most irregular elements** (§2.1).

**A design needs it when:** the game rewards *volume* of elements over *precision of placement*; elements sit
on the floor; multiple elements must be collected per trip; or driver skill is the limiting factor and you
want the mechanism to forgive approach error.

**A design does not need it when:** there is exactly one element per cycle and it must be placed to ±5 mm —
use a gripper (§10-12).

### 4.2 The main variants

| Variant | Description | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|---|
| **A. Single roller over a floor plate** | One driven shaft, printed ramp below | **1** | **1** | **2** | **4** | **5** |
| **B. Dual counter-rotating (over-under)** | Two shafts, one belt/chain, element passes between | 3 | 3 | 3 | 4 | 4 |
| **C. Side-by-side "sushi" rollers** | Two vertical rollers, element pulled between them | 3 | 3 | 3 | 4 | 4 |
| **D. Roller + compliant top gate** | One driven roller, sprung passive top plate | 2 | 2 | 2 | **5** | **5** |
| **E. Vectored / angled roller pair** | Rollers angled to funnel elements to centre | 4 | 4 | **5** | 3 | 3 |
| **F. Deployable roller on a 4-bar** | Roller stows in the 18 in. cube, drops out after start | **5** | 4 | 4 | 3 | 2 |

*(1 = low/easy/cheap, 5 = high/hard/expensive. **Duplicability: 5 = trivially built twice, 1 = painful.**)*

**JUDGMENT for this program: build variant D.** One motor, one driven shaft, one sprung passive top plate.
It has the reliability of a dual-roller intake with the parts count of a single-roller intake, it duplicates
almost perfectly because there is only one powered axis to align, and the sprung top plate is a
self-adjusting compression mechanism, which removes the tuning burden that kills variant B. Variant F is a
trap for a team with limited mentor hours — **and it is BLOCKED until R105's expansion limits publish.**

### 4.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Intake roller wheels, small-diameter | goBILDA (general supplier) | **3618 Series Intake Roller Wheel, 16 mm OD, 8 mm REX, 30A — `3618-4008-0016`** (8-pack) | 1–2 packs | 2–4 packs | **$12.99/8-pack** | Buy | **VERIFIED** — [intake wheels](https://www.gobilda.com/intake-wheels/) | 16 mm width. The cheapest compliant roller per contact point in FTC. 12 mm OD version `3618-4008-0012` same price. VERIFY-BEFORE-ORDER |
| Intake roller wheels, mid-diameter | goBILDA | **3615 Series Boot-Wheel, 30A** — `3615-4008-0048` (48 mm) / `3615-4008-0072` (72 mm) / `3615-4008-0096` (96 mm), all 8 mm REX bore | 4–6 | 8–12 | **$4.99 / $6.99 / $8.99 ea** | Buy | **VERIFIED** | 30A is very soft — excellent grip, expect wear. Direct 8 mm REX bore = **no hub needed** |
| Grippy conforming intake wheel | goBILDA | **GripForce Gecko™ Wheel** — `3613-4008-0032` (32 mm, $6.99) · `3613-4008-0048` (48 mm, $7.99) · `3613-0014-0072` (72 mm hub-mount, $8.99) · `3613-0014-0096` (96 mm hub-mount, $9.99) | 4–6 | 8–12 | **$6.99–$9.99 ea** | Buy | **VERIFIED** | Vendor's own words: *"make excellent intake wheels… ultra grippy and their spoke design allows them to conform to the shape of the object."* **This is the wheel goBILDA's own 2026-27 StarterBot intake uses** (§4.7). 72/96 mm need a 14 mm hub |
| Compliant wheels, classic | AndyMark (**official FIRST supplier**) | **Compliant Wheels** — 2 in `AM-3462` (1/2 in hex) / `AM-3571` (3/8 in hex) · 2.25 in `AM-4536` (**5 mm hex**) · 3 in `AM-4537` (5 mm hex) · 4 in `AM-4538` (5 mm hex); 35A/40A/50A/60A | 4–8 | 8–16 | **$6.20–$11.00 ea** | Buy | **VERIFIED** — [product page](https://andymark.com/products/compliant-wheels) | ⚠ **Shaft standard trap:** the 1/2 in and 3/8 in hex versions do **not** fit goBILDA 8 mm REX or REV 5 mm hex. Only the **5 mm hex** variants (AM-4536/4537/4538) drop into a REV DUO build. Listed as *"Estimated back in stock"* — **check stock before you plan on these** |
| Compliant wheels, REV DUO ecosystem | REV Robotics (general supplier) | **DUO Compliant Wheels, 2 in, 5 mm hex, 4-pack** — `REV-41-2034-PK4` (Medium 40A) / `REV-41-2035-PK4` (Soft 30A) | 1–2 packs | 2–4 packs | **$19.50/4-pack** | Buy | **VERIFIED** — In Stock & Ready To Ship | *"used for intakes and conveyor systems… solid 5mm Hex Hub molded into the wheel"* — **no separate hub required**, which is a real assembly-time saving ×2 robots |
| Compliant wheels, REV ION | REV Robotics | **ION Compliant Wheel, 2 in, 1/2 in hex, 4-pack** — `REV-21-2029-PK4` (Soft 30A) / `REV-21-2030-PK4` (Medium 40A) / `REV-21-2031-PK4` (Hard 60A) | 0–2 packs | 0–4 packs | **$6.50/4-pack** | Buy | **VERIFIED** — In Stock | ⚠ **1/2 in hex is an FRC/ION standard.** Cheapest compliant wheel found anywhere ($1.63/wheel) but you must supply 1/2 in hex shaft — **do not mix into a goBILDA REX build** |
| Roller shaft | goBILDA | **8 mm REX Shaft with E-Clip (stainless)** — `2106-4008-1920` (192 mm, $7.69) · `2106-4008-2400` (240 mm, $8.89) · `2106-4008-2880` (288 mm, $9.99) | 1–2 | 2–4 | **$7.69–$9.99 ea** | Buy | **VERIFIED** — [REX shafting](https://www.gobilda.com/stainless-steel-rex-shafting/) | Full ladder 96 mm→624 mm verified. Choose length after you know the intake width (**DEFERRED**) |
| Shaft bearings | goBILDA | **Flanged Ball Bearing, 8 mm REX ID / 14 mm OD** — `1611-0514-4008` (2-pack) | 2 (1 pack) | 4 (2 packs) | **$5.99/2-pack** | Buy | **VERIFIED** — In Stock, [bearings](https://www.gobilda.com/bearings/) | The REX-bore bearing lets the shaft turn *inside* a fixed bearing without a separate hub. Round 8 mm ID version `1611-0514-0008` is $3.99/2-pack |
| Bearing housings | goBILDA | **Pillow Blocks** (1-Side/2-Post, 2-Side/1-Post, Face Thru-Hole, Dual-Bearing), 4 mm–32 mm and REX bores | 2–4 | 4–8 | **$5.99–$16.99 ea** | Buy | **FAMILY-ONLY** — [bearings category](https://www.gobilda.com/bearings/) verified; individual SKUs not read | **NEEDS-SKU-CHECK.** Cheaper alternative: print the bearing pocket into your side plate (§18) and save $24–$68 across two robots |
| Roller-to-shaft hub (for hub-mount wheels) | goBILDA | **1309 Series Sonic Hub, 8 mm REX** — `1309-0016-4008` ($7.99) · **1310 Series Hyper Hub, 8 mm REX** — `1310-0016-4008` ($7.99) · **1311 Thru-Hole Sonic Hub** — `1311-0016-4008` ($7.99) · **1313 Hyper Hub** — `1313-1632-4008` ($12.99) | 0–4 | 0–8 | **$7.99–$12.99 ea** | Buy | **VERIFIED** — [8 mm REX bore hubs](https://www.gobilda.com/8mm-rex-bore-hubs/) | Only needed for the 14 mm hub-mount Gecko wheels. **Choosing the direct-REX-bore wheels instead saves $64 across two robots** |
| Intake motor | goBILDA | **Yellow Jacket Planetary Gear Motor, 5203 series (8 mm REX)** | 1 | 2 | **$54.99 ea** | Buy | **XREF-VERIFIED** — `LEGAL-PARTS-CONSTRAINTS.md` §2.5 | Legal per **Table 12-1** (R501). Pick the rpm for ~1.5–3 m/s surface speed (§3.1). **Spends 1 of 8 motor slots (R503)** |
| Intake motor, budget alternative | REV Robotics | **HD Hex Motor — `REV-41-1291`** ($22.00) + UltraPlanetary cartridges, or **UltraPlanetary Kit & HD Hex Motor — `REV-41-1600`** ($50.00) | 1 | 2 | **$22.00–$50.00** | Buy | **XREF-VERIFIED** (`REV-41-1291`) / **VERIFIED** this session (`REV-41-1600`, seen on [REV FTC](https://www.revrobotics.com/ftc/)) | Table 12-1 legal. R501 blue box: *"These motors may be used with or without the provided gearbox, and/or with any other compatible gearbox"* — so you can re-ratio in house |
| Roller drive coupling — chain | goBILDA | **Steel Chain (1 m) `3308-0008-1000`** ($11.99) · **Connecting Link 6-pack `3308-0008-0001`** ($2.99) · **8 mm REX Clamping Sprocket, 14T `3302-4008-0014`** ($12.99) · **8 mm REX Set-Screw Sprocket, 10T `3307-4008-0010`** ($9.99) | 1 chain + 2 sprockets | 2 + 4 | **~$36 per robot** | Buy | **VERIFIED** — [sprockets & chain](https://www.gobilda.com/sprockets-chain/) | ⚠ goBILDA chain is **8 mm pitch metric**, not #25. **It will not mesh with REV DUO's #25 plastic sprockets.** See `VENDOR-ECOSYSTEMS.md` §3.5 |
| Roller drive coupling — round belt (cheapest) | goBILDA | **3405 Series Round Belt, 5 mm cord** — `3405-0005-0254` (254 mm, $2.09) through `3405-0005-0653` (653 mm, $4.99) | 1–2 | 2–4 | **$0.89–$4.99 ea** | Buy | **VERIFIED** — [round belts](https://www.gobilda.com/round-belts) | **The budget hero of this table.** A round belt over two printed V-grooved pulleys links two rollers for under $5 and slips instead of jamming — a built-in torque limiter. Full 95 mm–653 mm ladder verified |
| Roller drive coupling — timing belt | goBILDA | 2 mm GT2 and 5 mm HTD timing belts and pulleys; **Cut-Length 3406 Series 3 mm HTD (5 m)** | 1–2 | 2–4 | see notes | Buy | **FAMILY-ONLY** — [timing belts & pulleys](https://www.gobilda.com/timing-belts-pulleys/) verified; only the starter packs carried prices (`3201-0013-0001` GT2 $239.99, `3201-0012-0001` HTD $209.99) | **NEEDS-SKU-CHECK** on individual belts/pulleys. The starter packs are poor value for a single intake; buy individual parts |
| Silicone roller stock (see §5) | goBILDA | **Silicone Cord, 8 mm dia, 50A, 2 m — `2928-0008-0002`** ($5.99) · **Silicone Tubing, 5 mm ID × 8 mm OD, 50A, 2 m — `2928-0508-0002`** ($5.99) | 1 ea | 2 ea | **$5.99 ea** | Buy | **VERIFIED** — [intake wheels](https://www.gobilda.com/intake-wheels/) | Slide the tubing over a printed roller core to make a custom-diameter compliant roller (§5) |
| Structure (channel, brackets, hardware) | goBILDA | 1120 Series U-Channel and 16 mm pattern hardware | — | — | ~$25–$40 per robot | Buy | **XREF-VERIFIED** — `VENDOR-ECOSYSTEMS.md` §6.3/§6.5 | Cross-reference; do not re-spec here |
| **Complete-kit option** | goBILDA | **FTC Starter Kit (2026-2027) `3200-4008-2627`** + **FTC StarterBot Base Resource Guide (2026-2027 Preseason) `3200-2627-0001`** | 1 | 2 | Kit **$899.99 / $674.99 with team discount** | Buy | Kit price **XREF-VERIFIED** (`VENDOR-ECOSYSTEMS.md` §9.1, re-confirmed 2026-08-22); guide **VERIFIED** this session | The guide *"provides a drop-center 6WD chassis with a **GripForce Gecko™ Wheel intake mechanism**"* and can be *"built in its entirety using the components found in the 2026-2027 goBILDA FTC Starter Kit (plus a REV Hub)."* **This is an R301.B StarterBot mechanism** — the one COTS MAJOR MECHANISM you may legally adopt wholesale |
| **Complete-kit option, REV path** | REV Robotics | **DUO FTC Starter Bot** (2026-27 REV DUO FTC Preview Starter Bot) — see [DUO Starter Bot](https://www.revrobotics.com/duo/ftc-starter-bot/); **FTC Starter Kit V3.1 `REV-45-3529`** $695.00 | 1 | 2 | **$695.00** | Buy | **VERIFIED** this session | REV's page states the preview bot *"utilizes flap wheels for a simple, easy-to-customize intake."* Also R301.B territory. See §7 for flap wheels |

### 4.4 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Student-hours (first robot) | Student-hours (second robot) |
|---|---|---|---|---|
| **Roller side plates** (2 per roller) with **slotted axle holes** for compression adjust | 3 mm polycarbonate **or** printed PETG, 5 mm wall | Bandsaw/jigsaw + drill press, or 3D printer | 3–4 h (incl. one design iteration) | **0.7 h** — reprint/recut from the same file |
| **Printed roller core / hub** for silicone sleeve or custom diameter | PETG or PA-CF; heat-set M3/M4 brass inserts | 3D printer + soldering iron for inserts | 2 h | 0.4 h |
| **Floor ramp / lead-in plate** | 1 mm or 2 mm polycarbonate (`REV-41-3049-PK5` / `REV-41-7537`, §18) | Scissors / side cutters — REV: *"can be cut with regular scissors"* | 1 h | 0.3 h |
| **Sprung top gate** (variant D) — pivot arm + extension spring | Printed PETG arm + goBILDA `2915-0001-0003` spring | 3D printer | 2 h | 0.5 h |
| **Nip-point guard / shroud** (R202 safety) | 1 mm polycarbonate | Scissors | 0.5 h | 0.2 h |
| **Wiring, mount, integrate, tune compression** | — | Hand tools | 4–6 h | 2–3 h |
| **TOTAL** | | | **≈ 13–16 h** | **≈ 4–5 h** |

**The duplicability lesson in one number:** the second robot's intake costs roughly **⅓ the labour** of the
first, *provided* every fabricated part came off a printer or a template rather than out of a student's
hands. Anything you hand-fit once, you hand-fit twice. See §19.

### 4.5 Approximate subtotal

Variant D (one driven roller, sprung top gate), goBILDA REX ecosystem, list prices as of August 2026:

| Line | Per robot | For 2 robots |
|---|---|---|
| 1 × 5203 Yellow Jacket motor | $54.99 | $109.98 |
| 1 × 8 mm REX shaft, 240 mm (`2106-4008-2400`) | $8.89 | $17.78 |
| 1 × 3618 intake roller wheel 8-pack (`3618-4008-0016`) | $12.99 | $25.98 |
| 2 × flanged REX bearings (1 × `1611-0514-4008`) | $5.99 | $11.98 |
| 1 × round belt + printed pulleys (`3405-0005-0374`) | $2.99 | $5.98 |
| 1 × extension spring (`2915-0001-0003`) | $3.99 | $7.98 |
| Polycarbonate sheet share (`REV-41-3049-PK5`, 5 sheets) | ~$4.40 | $11.00 (one pack covers both) |
| Filament, inserts, M4 hardware | ~$12 | ~$24 |
| Structure share (channel/brackets) | ~$30 | ~$60 |
| **Subtotal, ESTIMATE** | **≈ $136** | **≈ $275** |

Swap in Gecko wheels and chain drive instead of roller wheels and round belt and it rises to roughly
**$195 / $390**. **JUDGMENT: budget $150–$220 per robot, $300–$440 for the pair**, and note that this is one
of the cheapest MAJOR MECHANISMS you will build — the money in FTC is in motors, control system and slides,
not in intakes. **VERIFY-BEFORE-ORDER.**

### 4.6 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare to stock (for 2 robots) |
|---|---|---|---|
| **Intake pushes elements away instead of collecting** | Surface speed < approach speed (§3.1) | Higher rpm motor or larger roller | — (design fix) |
| **Roller rides over the element** | Single contact point, element too tall | Add second contact row or a sprung top gate | — |
| Compliant wheel spins on the shaft | Set-screw hub loosened; REX/hex bore worn | Blue threadlocker; switch to a molded-hex wheel (REV DUO) | 1 spare 8-pack `3618-4008-0016` ($12.99) |
| Wheel torn / chunked | 30A run too fast against a hard element; R201 exposure | Step up to 40A or 50A | 4 wheels of each durometer |
| Shaft bends | Impact from a driver ramming the wall | Steel not aluminium; shorten unsupported span; add centre bearing | 1 spare shaft ($8.89) |
| Bearing seizes with debris | Open bearing, TILE dust | Blow out between matches | 1 spare 2-pack ($5.99) |
| **Belt/chain thrown** | Insufficient tension, no tensioner | Slotted motor mount for tension | 1 spare belt + 1 connecting link 6-pack ($2.99) |
| **Motor stalls on a jam** | No current limit, no reverse | Software current-sense + a driver-mapped **reverse button** (§15.6) | — |
| Printed side plate cracks at the bolt hole | Print layers loaded in peel; no inserts | Reprint with 5 perimeters and heat-set inserts (§18) | **2 spare side plates, printed and in the pit bag** |

### 4.7 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Architecture | Variant A: one roller, printed floor ramp | Variant D: one roller + sprung top gate, or B: over-under |
| Wheels | 1 × `3618-4008-0016` 8-pack, 40A equivalent | Gecko `3613-4008-0048` or Boot-Wheels, durometer tuned per element |
| Drive | Direct-drive motor on the roller shaft | Belt/chain reduction to a tuned surface speed, slotted for tension |
| Compression | Fixed printed spacing | Slotted plates, adjustable in 30 s |
| Deploy | Fixed inside the 18 in. cube | **Deployable — BLOCKED until R105 publishes** |
| Control | Button = on/off | Trigger = variable, current-sense auto-reverse on jam, driver reverse override |
| Actuator cost | 1 motor | 1 motor (+1 servo if deployable) |
| Est. cost / robot | **~$110** | **~$200** |
| Build time | ~8 h | ~16 h |
| **Fallback** | Adopt the **goBILDA StarterBot Gecko intake** (R301.B) verbatim and move on | — |

---

## 5. I-2 — Flex / silicone roller and tube-sleeve intake

### 5.1 What it is and when a design needs it

A continuous compliant cylinder rather than discrete wheels: either a solid silicone/urethane roller, or —
the cheap and highly duplicable version — **silicone tubing slid over a 3D-printed core**. It presents an
unbroken contact line, so nothing can fall *between* the wheels.

**A design needs it when:** the element is small enough to escape between discrete compliant wheels; the
element is thin or flat (a disc can slip through a gap that a ball cannot); or the element surface is
delicate and you want to spread contact pressure over a line rather than points.

### 5.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|
| **A. Silicone tubing over a printed core** | **1** | **1** | 2 | 3 | **5** |
| **B. Silicone cord wound helically on a printed core** | 2 | **1** | 3 | 3 | 4 |
| **C. Solid COTS flex roller** | 2 | 3 | **1** | **5** | **5** |
| **D. Stacked compliant wheels touching (pseudo-roller)** | 2 | 3 | 2 | 4 | **5** |

**JUDGMENT: variant A for the B team, variant D for the A team.** Variant A costs $5.99 of tubing plus
$2 of filament and is the single cheapest compliant roller in this document. Variant D — buying 6–8 small
compliant wheels and butting them shoulder-to-shoulder on one shaft — gives you a near-continuous surface
using only parts you already stock, which is worth more across two robots than saving $8.

### 5.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Silicone tubing sleeve | goBILDA | **Silicone Tubing, 5 mm ID × 8 mm OD, 50A, 2 m — `2928-0508-0002`** | 1 | 2 | **$5.99 ea** | Buy | **VERIFIED** — [intake wheels](https://www.gobilda.com/intake-wheels/) | 2 m makes many rollers. Stretch-fits over a printed core turned slightly oversize |
| Silicone cord | goBILDA | **Silicone Cord, 8 mm dia, 50A, 2 m — `2928-0008-0002`** | 1 | 2 | **$5.99 ea** | Buy | **VERIFIED** | Wind helically into a printed spiral groove for a "screw" roller that also centres elements |
| Latex surgical tubing (also §6) | goBILDA | **Latex Surgical Tubing, 3 mm ID × 5 mm OD, 2 m — `2907-0305-0002`** | 1 | 2 | **$4.99 ea** | Buy | **VERIFIED** | Softer and grippier than silicone; degrades faster with UV/ozone — replace each season |
| Solid compliant roller (variant C) | AndyMark | **SpinTake** — `am-4623` (**5 mm hex**) / `am-4621` (Nub Bore) | 2–4 | 4–8 | **$3.50 ea** | Buy | **VERIFIED** — [SpinTake](https://andymark.com/products/spintake) | Natural rubber, **40A**, **3 in dia × 0.5 in thick**; *"ideal as an intake 'wheel' for picking up game pieces of varying shapes."* At $3.50 this is remarkable value. ⚠ **5 mm hex = REV DUO standard, not goBILDA REX.** Listed *"Estimated back in stock"* |
| Roller shaft, bearings, motor, coupling | — | — | — | — | — | — | — | **As §4.3.** Do not re-buy; the shaft/bearing/motor/belt lines are identical |

### 5.4 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st) | Hours (2nd) |
|---|---|---|---|---|
| **Printed roller core**, hex/REX bore, sized so the 5 mm ID tubing stretches ~15 % | PETG or PA-CF | 3D printer | 2 h incl. one fit iteration | 0.3 h |
| Helical groove core (variant B) | PETG | 3D printer | 3 h | 0.3 h |
| End caps to trap the tubing | PETG | 3D printer | 0.5 h | 0.1 h |
| Side plates, ramp, guard | as §4.4 | — | 4 h | 1 h |
| **TOTAL** | | | **≈ 9–10 h** | **≈ 1.7 h** |

**Print-fit tip (JUDGMENT):** print the core in **1 mm diameter increments** as a test ladder before
committing. Silicone tubing at 15 % stretch grips without adhesive; below ~8 % it walks off the core under
load, above ~25 % it thins and tears. This test costs 40 minutes and 20 g of filament and saves an
in-competition failure.

### 5.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Tubing or cord | $5.99 | $11.98 |
| Printed cores + caps (filament) | ~$4 | ~$8 |
| Shaft + bearings | $14.88 | $29.76 |
| Motor | $54.99 | $109.98 |
| Structure, hardware, belt | ~$40 | ~$80 |
| **Subtotal, ESTIMATE** | **≈ $120** | **≈ $240** |

Variant C (4 × SpinTake at $3.50) lands at roughly **$125 / $250** — essentially the same, with far less
print time. **VERIFY-BEFORE-ORDER.**

### 5.6 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Tubing walks off the core** | Insufficient stretch; no end caps | Oversize the core 1 mm; add caps | 1 spare 2 m tubing ($5.99) |
| Tubing tears at a lip | Sharp printed edge under the sleeve | Fillet every edge under the sleeve | — |
| Latex tubing goes hard and cracks | Age/ozone — it is a **consumable** | Replace annually | 1 spare 2 m ($4.99) |
| Silicone picks up TILE dust and loses grip | Normal | Wipe with isopropyl between matches | Alcohol wipes in the pit kit |
| Printed core splits at the bore | Layer lines loaded in hoop tension | Reprint with bore axis **vertical** (§18.4) and 5 perimeters | **2 spare cores, printed** |

### 5.7 Rookie-friendly minimum vs. competitive version

| | Rookie minimum | Competitive |
|---|---|---|
| Roller | Silicone tubing on a printed core | Tuned-durometer stacked compliant wheels, or SpinTake pair |
| Contact | Single line | Two lines, counter-rotating |
| Adjust | Fixed | Slotted, adjustable compression |
| Est. cost / robot | ~$95 | ~$150 |

---

## 6. I-3 — Surgical tubing flail intake

### 6.1 What it is and when a design needs it

Short lengths of surgical tubing set radially in a printed hub, spun fast. The tubing extends under
centrifugal force, sweeps the element, then folds out of the way when it meets an obstruction. It is the
most forgiving acquisition mechanism in FTC and the one with the most rule exposure.

**A design needs it when:** the element is irregular, light, low-profile, or lies flat on the floor; the
contact geometry is unpredictable; or you need a very wide sweep from a narrow mechanism.

**⚠ Rule exposure, CONFIRMED-BIOBUZZ.** Flails are legal, but read §1.5 before committing:
**R202.I** prohibits *"devices or conditions that pose an unnecessary risk of entanglement"*, and **R201**
prohibits features at risk of *"making a mess"* — fraying latex is exactly that. **JUDGMENT: keep flails
short, cap the ends, and inspect every event.** Expect an INSPECTOR to ask about them.

### 6.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|
| **A. Short radial flails in a printed hub** | 2 | **1** | 3 | 3 | **5** |
| **B. Long flails (>2× radius)** | 2 | **1** | **5** | **1** | 4 |
| **C. Flails + a compliant back roller** | 3 | 2 | 3 | 4 | 4 |
| **D. Loop flails (tubing doubled and both ends anchored)** | 3 | **1** | 3 | 4 | **5** |

**JUDGMENT: variant D.** A doubled loop cannot fray at a free end, has no whipping tip, and answers the
R202.I entanglement question before it is asked. It is also the easiest to replace at an event — pull two
ends out of two printed slots, push two new ends in.

### 6.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Surgical tubing | goBILDA | **Latex Surgical Tubing, 3 mm ID × 5 mm OD, 2 m — `2907-0305-0002`** | 1–2 | 2–4 | **$4.99 ea** | Buy | **VERIFIED** — [intake wheels](https://www.gobilda.com/intake-wheels/) | 2 m ≈ 25 flails of 80 mm. **Treat as a per-event consumable** |
| Silicone cord alternative | goBILDA | **Silicone Cord, 8 mm dia, 50A — `2928-0008-0002`** | 1 | 2 | **$5.99 ea** | Buy | **VERIFIED** | Stiffer, more durable, less grippy than latex; does not perish |
| Flail hub | — | — | — | — | — | **Fab** | — | Printed — see §6.4. **No vendor sells one** |
| Shaft, bearings, motor, coupling | — | as §4.3 | — | — | — | Buy | **VERIFIED / XREF** | Identical to §4.3 |

### 6.4 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st) | Hours (2nd) |
|---|---|---|---|---|
| **Printed flail hub** — REX/hex bore, radial slots with a retention barb, chamfered slot mouths | **PA-CF or PETG** (do **not** use PLA — §18.2) | 3D printer | 3 h incl. 2 slot-fit iterations | 0.4 h |
| Flail cutting jig (a printed length gauge) | PLA is fine here | 3D printer | 0.5 h | 0 h — shared |
| **Full-width guard/shroud** (R202) | 1 mm polycarbonate | Scissors | 1 h | 0.3 h |
| Side plates, mount, integrate | as §4.4 | — | 4 h | 1 h |
| **TOTAL** | | | **≈ 8.5 h** | **≈ 1.7 h** |

**Print-orientation note:** the slot walls take a cyclic pull-out load every revolution. Print the hub with
the **bore axis vertical** so the slot walls are loaded *across* layers in compression, not in peel. See
§18.4.

### 6.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Tubing (season supply) | $9.98 (2 packs) | $19.96 |
| Printed hub + jig + shroud | ~$5 | ~$10 |
| Shaft + bearings | $14.88 | $29.76 |
| Motor | $54.99 | $109.98 |
| Structure/hardware | ~$30 | ~$60 |
| **Subtotal, ESTIMATE** | **≈ $115** | **≈ $230** |

### 6.6 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Flail pulls out mid-match** | Slot barb too shallow; hole stretched | Deepen the barb; switch to loop variant D | **1 pre-cut flail set per robot, in the pit bag** |
| Flails fray / shed rubber | Latex against a hard edge; age | Chamfer every edge; replace | 1 spare 2 m tubing ($4.99) |
| Flails wrap around the shaft | Too long relative to radius | Shorten to ≤ ~1.5 × roller radius | — |
| Flails tangle with FIELD elements | Too long / free ends | **Loop variant D**; shroud | — |
| Hub cracks at a slot | PLA, or layers in peel | PA-CF/PETG, bore axis vertical | **2 spare hubs, printed** |
| Inconsistent grip match to match | Flail length drift from wear | Cut with the jig, replace as a set | Jig lives in the pit bag |

### 6.7 Rookie-friendly minimum vs. competitive version

| | Rookie minimum | Competitive |
|---|---|---|
| Flails | 4 rows × 4 short flails | 6 rows, loop variant, length-tuned |
| Backing | Printed floor ramp | Sprung compliant back roller (variant C) |
| Maintenance | Replace when visibly frayed | Replace as a set every event; logged |
| **Honest verdict** | Only choose flails if a roller genuinely cannot acquire the element. They are the highest-maintenance intake in this file, and the maintenance is **doubled** | |

---

## 7. I-4 — Star roller and flap-wheel intake

### 7.1 What it is and when a design needs it

A roller whose contact surface is a set of discrete radial lobes — moulded stars, or hinged/flexible flaps.
Between lobes there is a gap, so the roller **flicks** the element rather than squeezing it. This generates
a lifting moment on a flat element that a smooth roller cannot produce.

**A design needs it when:** the element is a **disc, ring or plate lying flat on the floor**; the element is
**irregular or soft** and must be scooped rather than pinched; or you want a roller that self-clears debris.
REV states its flap wheels are *"used on intakes to pick up irregular gamepieces"* — **VERIFIED**.

### 7.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|
| **A. COTS flap wheels on a shaft** | **1** | 2 | **1** | 4 | **5** |
| **B. COTS compliant stars on a shaft** | **1** | 3 | **1** | **5** | **5** |
| **C. Printed star lobes with TPU tips** | 3 | **1** | 3 | 3 | 4 |
| **D. Star roller + smooth back roller pair** | 3 | 3 | 3 | 4 | 4 |

**JUDGMENT: variant A or B.** Both are pure bolt-on: buy the wheel, slide it on a hex shaft, done. For a
two-robot program with limited mentor hours, **a mechanism whose "fabrication" is sliding a part onto a
shaft is worth paying for.** Variant B (AndyMark Compliant Stars) additionally offers a 5-lobe geometry in
five durometers up to 80A rated to 9000 rpm, which makes it the better indexing roller as well (§15).

### 7.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Flap wheels | REV Robotics (general supplier) | **DUO Flap Wheels, 5 mm hex, 4-pack** — `REV-41-2701-PK4` (Soft 30A) · `REV-41-2702-PK4` (Medium 40A) · `REV-41-2703-PK4` (Hard 60A) | 1–2 packs | 2–4 packs | **$17.50 / 4-pack** | Buy | **VERIFIED** — In Stock & Ready To Ship, [DUO flap wheels](https://www.revrobotics.com/duo-flap-wheels/) | Material: *"Polypropylene & TPR."* Vendor's stated purpose: *"used on intakes to pick up irregular gamepieces, playing a similar role to compliant wheels."* ⚠ **5 mm hex bore = REV DUO shaft standard** |
| Compliant stars | AndyMark (**official FIRST supplier**) | **Compliant Stars** — 3 in and 5 in, in **1/2 in hex** and **3/8 in hex**, durometers 35A / 40A / 50A / 60A / **80A** | 4–6 | 8–12 | **3 in: $8.00–$8.40 · 5 in: $13.00** | Buy | **VERIFIED** — [Compliant Stars](https://andymark.com/products/compliant-stars) | *"The soft material gives way to allow rigid objects to be manipulated easily… creates a very effective roller that ignores variations in objects being driven."* 80A rated to **9000 rpm**. ⚠ **No 5 mm hex or 8 mm REX bore offered.** Listed *"Estimated back in stock"* — check stock |
| Grip wheels (flat-face alternative) | REV Robotics | **DUO Grip Wheels** — 5 mm hex, two durometers | 2–4 | 4–8 | **$13.00** | Buy | **FAMILY-ONLY** — [DUO wheels category](https://www.revrobotics.com/duo/motion/wheels/) loaded; **part numbers not printed on the page** | **NEEDS-SKU-CHECK.** *"used for intakes, conveyor systems, and shooters… solid 5mm Hex Hub molded into the wheel no external hub is required"* |
| 90 mm grip wheel | REV Robotics | **90mm Grip Wheel — `REV-41-1267`** | 0–2 | 0–4 | **$7.75** | Buy | **VERIFIED** — listed on [REV wheels](https://www.revrobotics.com/ftc/motion/rotary-motion/wheels/) | Large-diameter single-contact sweeper. **NEEDS-SKU-CHECK on bore standard before ordering** |
| Shaft standard adapters | goBILDA / REV | Hex ↔ REX adapters, pattern adaptors | as needed | ×2 | see notes | Buy | **XREF-VERIFIED** — `VENDOR-ECOSYSTEMS.md` §3.7 | **Read §3.7 of the vendor file before mixing shaft standards.** Cheapest fix is choosing wheels that already match your ecosystem |
| Shaft, bearings, motor, coupling | — | as §4.3 | — | — | — | Buy | — | Match the **bore standard** of the wheel you chose — that is the trap in this whole section |

**⚠ The interoperability warning that governs this entire section.** Five product lines, five bores:

| Wheel family | Bore | Native to |
|---|---|---|
| goBILDA 3613 / 3615 / 3618 intake wheels | **8 mm REX** (or 14 mm hub-mount) | goBILDA |
| REV DUO Compliant / Flap / Grip wheels | **5 mm hex** | REV DUO |
| REV ION Compliant Wheels | **1/2 in hex** or MAXSpline | FRC / ION — **not** an FTC standard |
| AndyMark Compliant Wheels | 1/2 in hex, 3/8 in hex, Nub, **and 5 mm hex** on `AM-4536` / `AM-4537` / `AM-4538` | Mixed — the 5 mm hex parts drop into REV DUO |
| AndyMark Compliant Stars | 1/2 in hex, 3/8 in hex **only** | Neither goBILDA nor REV DUO natively |
| AndyMark SpinTake | **5 mm hex** (`am-4623`) or Nub (`am-4621`) | REV DUO |

`VENDOR-ECOSYSTEMS.md` §4 tells you to pick one ecosystem and stay in it. **This table is the reason.** For
a goBILDA-committed program the native intake surfaces are the **3613 / 3615 / 3618 series**; everything
else is an adapter problem, **paid for twice**.

### 7.4 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st robot) | Hours (2nd robot) |
|---|---|---|---|---|
| Side plates with slotted axle holes | Polycarbonate or printed PETG | Printer / hand tools | 3 h | 0.7 h |
| **Phase-stagger spacers** (offset each star so lobes strike sequentially) | Printed PETG, keyed | 3D printer | 1 h | 0.2 h |
| Floor ramp / lead-in | 1 mm polycarbonate | Scissors | 1 h | 0.3 h |
| Mount, integrate, tune | — | Hand tools | 3 h | 1.5 h |
| **TOTAL** | | | **≈ 8 h** | **≈ 2.7 h** |

**Phase-stagger tip (JUDGMENT):** if every lobe on every star strikes at the same instant the intake
hammers, motor current spikes, and light elements bounce back out. Rotate each star about 1/(2·n_lobes) of a
turn relative to its neighbour using printed keyed spacers. One printed part; transforms the feel.

### 7.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| 1 × flap-wheel 4-pack (`REV-41-2702-PK4`) | $17.50 | $35.00 |
| Shaft + bearings (5 mm hex, REV DUO) | ~$18 | ~$36 |
| Motor | $54.99 | $109.98 |
| Belt / coupling | ~$5 | ~$10 |
| Printed spacers, plates, ramp | ~$8 | ~$16 |
| Structure / hardware | ~$30 | ~$60 |
| **Subtotal, ESTIMATE** | **≈ $133** | **≈ $267** |

AndyMark Compliant Stars variant (6 × 3 in at $8.40 = $50.40) lands nearer **$165 / $330**.
**VERIFY-BEFORE-ORDER.**

### 7.6 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare to stock (2 robots) |
|---|---|---|---|
| **Element wedges between lobes** | Lobe gap ≈ element dimension | Change star diameter or lobe count so the gap is either much smaller or much larger than the element | — |
| Intake hammers, current spikes | All lobes in phase | Phase-stagger spacers (§7.4) | — |
| Flap tips tear | TPR fatigue at high rpm against a hard stop | Lower rpm; harder durometer | **1 spare 4-pack ($17.50)** |
| Wheel walks along the shaft | No spacers or retention | Printed spacers + shaft collars both sides | Spacer set |
| Plastic bore rounds out on the hex | Overload on a plastic bore | Larger bore, or a metal hub | 2 spare stars |
| Wrong-bore parts arrive | §7.3 bore table ignored | — | **Prevention: order both robots' wheels in one order** |

### 7.7 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Surface | 1 × flap-wheel 4-pack, direct drive | Phase-staggered stars, durometer tuned, paired with a smooth back roller |
| Ramp | Flat printed plate | Curved lead-in matched to the element |
| Control | On / off | Variable + reverse + jam detect |
| Est. cost / robot | **~$110** | **~$175** |
| Build time | ~5 h | ~10 h |

---

## 8. I-5 — Brush roller intake

### 8.1 What it is and when a design needs it

A cylindrical brush — bonded or staple-set bristles in a core — spun to sweep elements. Bristles conform to
almost any geometry and generate very low contact stress, so nothing gets marked or crushed.

**A design needs it when:** the element is **fragile, soft or oddly shaped**; you must sweep small elements
off a textured surface; or R201's *"gouging, tearing off pieces, or routinely and repeatedly marking SCORING
ELEMENTS"* is a live concern with harder rollers.

**A design does not need it when:** the element is heavy. Brushes generate very little normal force — a
brush intake that works beautifully on a foam ball will not move a 500 g block.

**⚠ R201 exposure:** shed bristles on the TILE are litter under *"at risk of making a mess."* Use
**bonded / staple-set industrial brush**, never a household broom head, and inspect for shedding at every event.

### 8.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|
| **A. COTS cylindrical brush on a shaft** | **1** | 3 | **1** | 4 | **5** |
| **B. Strip brush wound into a printed helical core** | 4 | 2 | 4 | 3 | 3 |
| **C. Brush + compliant wheel hybrid** | 3 | 3 | 3 | 4 | 4 |

**JUDGMENT: variant A if you can source a brush with a bore matching your shaft; otherwise skip brushes and
use 30A flap wheels (§7)**, which occupy nearly the same design niche with a supply chain you can verify.

### 8.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Cylindrical brush roller | **No standard FTC vendor stocks one** | — | — | — | — | — | ⚠ **VERIFIED NEGATIVE FINDING** | I loaded goBILDA `/wheels-tires/` (14 subcategories, **no brush category**), goBILDA `/intake-wheels/` (12 products, **no brush**), REV `/ftc/motion/rotary-motion/wheels/` and `/duo/motion/wheels/` (**no brush**). **Neither goBILDA nor REV sells a brush roller.** Do not put a SKU for one in a BOM |
| Strip brush / cylindrical brush, industrial | General industrial supplier (e.g. McMaster-Carr, Grainger, brush manufacturers) | Cylindrical and spiral strip-brush families | 1–2 | 2–4 | **not verified** | Buy | **UNVERIFIED / NEEDS-SKU-CHECK** | Such suppliers **do meet the VENDOR test** (Federal Tax ID, general stock, available to all teams — `LEGAL-PARTS-CONSTRAINTS.md` §8.2). I loaded no page; **name the family, verify the SKU before ordering** |
| The substitute that IS verified | REV Robotics | **DUO Flap Wheels, Soft 30A — `REV-41-2701-PK4`** | 1–2 packs | 2–4 packs | **$17.50 / 4-pack** | Buy | **VERIFIED** | **JUDGMENT: this is the answer for this program.** Soft TPR flaps occupy nearly the same low-contact-stress niche with a supply chain you can actually check |
| Shaft, bearings, motor | — | as §4.3 | — | — | — | Buy | — | Brushes need low rpm and low torque — a **continuous-mode servo may suffice** (§16.3) and saves a motor slot |

### 8.4 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st) | Hours (2nd) |
|---|---|---|---|---|
| Printed brush core with a helical strip channel (variant B) | PETG | 3D printer | 4 h | 0.5 h |
| **Bore adapter** to fit an industrial brush to 8 mm REX / 5 mm hex | PA-CF printed (no lathe assumed) | 3D printer | 2 h | 0.3 h |
| Side plates, ramp, guard | as §4.4 | — | 4 h | 1 h |
| **TOTAL** | | | **≈ 10 h** | **≈ 1.8 h** |

### 8.5 Approximate subtotal

**Not costed with confidence, because the central component is unverified.** ESTIMATE **$130–$190 per
robot, $260–$380 for two**, dominated by motor and structure. If you substitute soft flap wheels — which is
the recommendation — use the §7.5 numbers instead.

### 8.6 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Bristles shed on the TILE** | Glued-in bristle | Staple-set / bonded brush only; inspect each event | Replacement brush |
| Brush "combs flat" and loses grip | Bristles take a set from one-direction running | Reverse between matches; stiffer bristle | — |
| No pulling force on heavy elements | Fundamental to brushes | Hybrid variant C, or change mechanism | — |
| Bristles wrap the shaft ends | No end retention | Printed end caps | 2 caps |
| Printed bore adapter spins on the shaft | Creep in the plastic | Metal set-screw insert; PA-CF, never PLA | 2 spare adapters |

### 8.7 Rookie-friendly minimum vs. competitive version

| | Rookie minimum | Competitive |
|---|---|---|
| Surface | **Do not build a brush.** Use soft flap wheels (§7) | COTS industrial brush with a verified SKU, hybridised with a compliant back roller |
| **Honest verdict** | A brush is a specialist answer to a specialist element. With no FTC vendor stocking one, a two-robot program with limited mentor hours should treat this section as a **fallback to evaluate at Kickoff, not a plan** | |

---

## 9. I-6 — Passive intakes: funnels, wedges, one-way gates, gravity feeds

### 9.1 What it is and when a design needs it

Geometry doing the work of an actuator. The robot's **motion** supplies the energy; a shaped surface
converts it into acquisition. Passive intakes cost **zero motor slots, zero servo slots and almost zero
dollars — which, doubled, makes this the most duplicable mechanism class in the entire catalog.**

**A design needs it when:** the element can be pushed, herded or driven over; the game rewards gathering
many elements; you have already spent your 8 motors (§1.6); or the B team needs a mechanism buildable in a
weekend.

**A design does not need it when:** the element must be lifted off the floor with no ramp available, or must
be placed precisely.

### 9.2 The main variants

| Variant | Description | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|---|
| **A. Fixed funnel / hopper mouth** | Two angled walls converging on the transfer path | **1** | **1** | **1** | **5** | **5** |
| **B. Wedge / plow** | Low ramp that lifts the element as the robot drives over it | **1** | **1** | 2 | **5** | **5** |
| **C. One-way gate** | Sprung flap; element pushes in, cannot fall out | 2 | **1** | 2 | 4 | **5** |
| **D. Gravity chute / drop-in** | Element enters high, falls to a stop | **1** | **1** | 2 | 4 | **5** |
| **E. Sprung-deploy wedge** | Wedge stows in the 18 in. cube, spring or gas spring deploys it after MATCH start | 3 | 2 | 3 | 4 | 4 |
| **F. Herding walls / corral** | Wide passive arms that gather many elements | 2 | **1** | 2 | 4 | **5** |

**JUDGMENT: build variant A on both robots regardless of what else you build.** A funnel mouth in front of
*any* active intake widens the effective capture window by 50–100 % for the price of a polycarbonate sheet,
and it is the cheapest insurance against driver error that exists (§17). Variant E is **BLOCKED until R105
publishes** if it deploys outside the starting envelope.

### 9.3 ⚠ The R203 test bites hardest here

A one-way gate is exactly the mechanism R203 was written about. **CONFIRMED-BIOBUZZ, R203, p. 69:**
*"ROBOTS must allow removal of SCORING ELEMENTS from the ROBOT… while powered off."* A sprung flap that lets
elements in and not out **must** be openable by hand, with no tools and no power.

**Design rule (JUDGMENT):** every one-way gate gets an **exposed, labelled finger tab** on the outside of
the robot that lifts the flap. Then test it: dead robot, loaded hopper, a student who did not build it
empties it in five seconds. Do this on **both** robots.

### 9.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Sheet for funnels, wedges, walls | REV Robotics | **Polycarbonate Sheet, 1 mm, 400 × 350 mm, 5-pack — `REV-41-3049-PK5`** | 1 pack | **1 pack covers both** | **$11.00** | Buy | **VERIFIED** — In Stock, [polycarbonate sheets](https://www.revrobotics.com/Polycarbonate-Sheets/) | *"This thin and flexible material can be cut with regular scissors, and simple mounting holes can be made with a handheld hole punch."* **Ideal for a no-CNC shop** |
| Sheet, structural, with layout grid | REV Robotics | **Polycarbonate Sheet, 2 mm, 8 mm grid, 456 × 296 mm — `REV-41-7537`** | 1–2 | 2–4 | category range **$11.00–$75.00**; individual price not printed | Buy | **VERIFIED** (SKU, size, In Stock) / **NEEDS-SKU-CHECK** (price) | *"Easy to cut with thick scissors, side cutters, or common shop tools."* The **printed 8 mm grid is a free hole-layout jig** — which matters when you cut the same part twice |
| Sheet, large format | REV Robotics | **Polycarbonate Sheet, 3 mm, 1/2 in grid, 1194 × 584 mm — `REV-21-3410`** | 0–1 | **1 covers both** | individual price not printed | Buy | **VERIFIED** (SKU, size, In Stock) / **NEEDS-SKU-CHECK** (price) | *"Great for rapid prototyping, competition repairs, and custom robot fabrication."* ⚠ `REV-21-` prefix = **ION/FRC line**; it is raw sheet stock, so R302 raw-material rules apply and there is no FTC-legality issue |
| Gate and deploy springs | goBILDA | **Extension Spring 1.5 kg, 39–72 mm — `2915-0001-0003`** ($3.99) · **Extension Spring 8 kg, 48–80 mm — `2915-0001-0002`** ($5.49) · **Compression Spring 1.1 kg — `2916-0001-0001`** ($3.99 / 2-pack) · **Compression Spring 2.3 kg — `2916-0001-0002`** ($3.99 / 2-pack) | 1–2 | 2–4 | **$3.99–$5.49** | Buy | **VERIFIED** — [springs](https://www.gobilda.com/springs) | ⚠ Verified negative: the goBILDA springs page lists **no torsion springs and no constant-force springs**. For those, name the family and source industrially — **NEEDS-SKU-CHECK** |
| Gas spring for passive deploy | Any VENDOR | COTS gas spring / gas shock, **pre-charged and sealed by the manufacturer** | 0–2 | 0–4 | not verified | Buy | **FAMILY-ONLY** | **Explicitly legal: R801.A** permits *"sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)"*; the blue box names *"gas springs, and dampers."* **Zero actuator slots.** Specify by force and stroke, and **buy four identical so both robots match** |
| Magnets for passive detent / alignment | Any VENDOR | Neodymium disc and block magnets | as needed | ×2 | not verified | Buy | **FAMILY-ONLY** | **R302 lists magnets as an allowed raw material** (p. 70, item D). Must still pass **R203** — a hand must pull the element off |
| Gate pivots | goBILDA | Flanged ball bearings **`1601-0014-0004`** (4 mm ID) / **`1601-0014-0005`** (5 mm ID), 14 mm OD | 2–4 | 4–8 | **$3.99 / 2-pack** | Buy | **VERIFIED** — In Stock, [bearings](https://www.gobilda.com/bearings/) | A gate on real bearings does not stick. A gate on a bolt through a printed hole does |
| **Complete-kit option** | — | **None exists, and none legally could** | — | — | — | **Fab** | **JUDGMENT + R301** | A funnel purpose-shaped to a BIOBUZZ element sold by a vendor would be a **COTS MAJOR MECHANISM purposefully designed to complete a game task — prohibited by R301.** Passive intakes are inherently in-house work |

### 9.5 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st) | Hours (2nd) |
|---|---|---|---|---|
| **Funnel walls** (2) | 1 mm or 2 mm polycarbonate, screwed at an angle or bent over a heated edge | Scissors, drill, **cardboard template first** | 2 h | **0.4 h** from the template |
| **Wedge / plow** | 2 mm polycarbonate or printed PETG, leading edge chamfered (**R201: no sharp edges**) | Scissors / printer | 2 h | 0.4 h |
| **One-way gate** + **manual release tab** (R203) | Printed PETG flap on a bearing pivot + extension spring | Printer, hand tools | 2.5 h | 0.5 h |
| **Herding arms** (variant F) | 2 mm polycarbonate | Scissors | 1.5 h | 0.3 h |
| Mount and iterate against the real element (**Kickoff-week work**) | — | — | 3 h | 1 h |
| **TOTAL** | | | **≈ 11 h** | **≈ 2.6 h** |

**Template discipline (JUDGMENT).** Cut every passive part from a **cardboard template first**, iterate the
cardboard against the real element until it works, then trace onto polycarbonate **twice**. Cardboard is
free, polycarbonate is not, and the second robot's part becomes a trace rather than a redesign. This single
practice is what earns passive intakes their 5/5 duplicability score.

### 9.6 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Polycarbonate share (`REV-41-3049-PK5`, 5 sheets) | ~$5.50 | **$11.00** (one pack) |
| Springs | ~$8 | ~$16 |
| Pivot bearings + hardware | ~$10 | ~$20 |
| Filament | ~$4 | ~$8 |
| **Subtotal, ESTIMATE** | **≈ $28** | **≈ $55** |
| **Actuator slots consumed** | **0 motors, 0 servos** | — |

**This is the cheapest MAJOR MECHANISM in the catalog by an order of magnitude.** For a modest budget
building everything twice, that fact deserves real weight in concept selection.

### 9.7 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Elements bounce back out of the funnel** | Walls too steep; hard surface | Shallower angle; line the mouth with silicone tubing (`2928-0508-0002`) | Tubing offcut |
| Wedge pushes rather than lifts | Leading edge too thick or too high | Thinner, lower, chamfered edge — 1 mm sheet often beats 3 mm | Spare cut part |
| **One-way gate jams half open** | Binding pivot; weak spring | Bearing pivot, not a bolt in a printed hole; stronger spring | 2 spare flaps |
| Gate fails the R203 powered-off test | No manual release | Add and label the finger tab | — |
| Polycarbonate cracks at a bolt hole | Hole drilled too near the edge; no washer | Edge distance ≥ 2× hole diameter; nylon washers both sides | Spare cut parts |
| Funnel collapses on contact | 1 mm sheet unsupported over a long span | Fold a flange, or back it with a printed rib | — |

### 9.8 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Form | Two flat funnel walls screwed to the chassis | Curved tuned funnel with a compliant lip, feeding a one-way gate into a hopper |
| Deploy | Fixed inside the 18 in. cube | Gas-spring deploy at MATCH start (**BLOCKED until R105**) |
| Retention | Gravity | One-way gate + magnet detent, both R203-tested |
| Actuators | **0** | **0** |
| Est. cost / robot | **~$15** | **~$45** |
| Build time | ~4 h | ~11 h |

---

## 10. E-1 — Servo claw (two-jaw gripper)

### 10.1 What it is and when a design needs it

Two jaws pivoting about one or two axes, driven by a single servo, closing on the element. It is the
default answer whenever the game asks the robot to **place** an element rather than **dump** it — onto a
peg, into a slot, on top of a stack, at a specific height and orientation.

**A design needs a claw when at least two of these are true:**

- the element must arrive at the goal in a **known orientation**;
- the goal is **small relative to the element**, so a dumped element will not land correctly;
- the robot must carry **exactly one** element and present it precisely (a magazine cannot do this);
- the acquisition point is **elevated or racked**, not on the floor, so a floor-sweeping roller cannot reach it;
- the element is a **panel, cone, or awkward rigid body** that a roller cannot control.

**A design does NOT need a claw when** the game rewards volume of elements deposited into a large goal. In
that game a claw is a slow, fragile, one-at-a-time machine competing against a roller intake that never
stops moving. **JUDGMENT: the most common concept error in FTC is building a claw for a game that wanted an
intake.** Answer §2.2 question 4 before you sketch a jaw.

**Actuator cost: 1 servo** for the jaw. Realistically **2–3 servos** once a wrist and a rotate are added,
which is why §1.6 flags claw-plus-wrist-plus-rotate as the design to audit hardest against R503's 8-servo
ceiling.

### 10.2 The main variants

| Variant | Description | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|---|
| **A. Single jaw against a fixed backstop** | One moving jaw clamps the element against a static printed wall | **1** | **1** | **1** | **5** | **5** |
| **B. Two jaws geared together (one servo)** | Brass servo gears mesh the two jaws so they mirror | 3 | 3 | 2 | 4 | 4 |
| **C. Two jaws, two servos, independently driven** | Each jaw on its own servo | 2 | 4 | 3 | 3 | 3 |
| **D. Servo arm + push-rod linkage to both jaws** | One dual servo arm, two ball-linkage push rods | 3 | 2 | 3 | 4 | 4 |
| **E. Bought single-DoF COTS gripper kit** | ServoCity gripper kit, servo included | **1** | **1** | **1** | 4 | **5** |
| **F. Claw + wrist + rotate** | Full 3-DoF hand | **5** | **5** | **5** | 2 | **1** |

*(1 = low/easy/cheap, 5 = high/hard/expensive. **Duplicability: 5 = trivially built twice, 1 = painful.**)*

**⚠ Variant C is legal for a team-built claw but is an actuator-budget trap.** R303's Example 3
(**CONFIRMED-BIOBUZZ**, p. 70, verbatim) says *"Simple gripper claws, comprised of a single actuator moving 2
gripper jaws simultaneously or double actuators each controlling an independent gripper jaw, are by and
large a single DoF."* So two servos on two jaws is still one DoF and is legal. But it **spends two of your
eight servo slots to do what one servo does in variant A, B or D**, on two robots. Do not pay that unless
the jaws must move independently.

**JUDGMENT for this program: build variant A, and only move to B or D if the element demands symmetric
capture.** A single moving jaw clamping against a fixed printed backstop has half the moving parts, half
the alignment work, no gear mesh to set, and it duplicates by reprinting two files. It also passes the R203
hand-removal test more easily, because there is only one spring path to defeat. Variant F is the design
that eats a season: three servo slots per robot, six across the program, and every one of them needs its
own tuning, its own wire run and its own failure mode.

### 10.3 ⚠ The R203 test, applied to a claw

**CONFIRMED-BIOBUZZ, R203, p. 69** (verbatim, re-grepped this session): *"ROBOTS must allow removal of
SCORING ELEMENTS from the ROBOT and the ROBOT from FIELD elements while powered off."*

A claw is the mechanism this rule is most often aimed at. Four configurations to check:

| Configuration | R203 verdict | Fix |
|---|---|---|
| Standard servo, moderate gearing, jaws backdrive under firm hand force | ✅ Passes — **but test it, do not assume it** | — |
| Servo **gearbox** (goBILDA Stingray / Shark, §16.5) driving the jaws at a high ratio | ⚠ Very likely **fails** — high-ratio gear trains are effectively non-backdrivable | Add a **quick-release jaw pin**, or spring the jaw open when unpowered |
| Worm-driven jaw | ❌ **Fails.** Self-locking by design | Do not put a worm on an element-contacting jaw. Use it on an arm pivot (`EXTENSION-ARMS-LIFTS.md`) with its own manual release |
| Jaws with deep undercut printed pockets that mechanically capture the element | ❌ **Fails** — geometry traps the element regardless of power | Open the pocket; rely on friction and compliance, not capture |

**JUDGMENT — the design rule that makes this a non-issue.** Make the servo *close* the jaw against a
**return spring**, and size the spring so that with the servo unpowered the jaw sits **open**. Then R203 is
satisfied structurally rather than by a hopeful backdrive test, the element cannot be trapped by a dead
battery mid-MATCH, and the same spring gives you compliance (§17). The cost is one `2915-0001-0003`
extension spring at **$3.99**, twice.

### 10.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Complete-kit option — angled-jaw gripper** | ServoCity (goBILDA catalogue lineage) | **Servo-Driven Gripper Kit (Servo Included)** — `3219-0002-0002` | 0–1 | 0–2 | **$29.99 ea** | Buy | **VERIFIED** — [gripper kits](https://www.servocity.com/gripper-kits/) | **Servo included**, so it costs less than a bare goBILDA Dual Mode servo. Jaws rotate inward on linkages driven by the included Proton Torque Servo; perimeter holes on the **8 mm grid**, so it bolts to goBILDA structure. Legal as a **single-DoF COTS gripper, R303.G** — read §1.4 before making it your only end effector. VERIFY-BEFORE-ORDER |
| **Complete-kit option — parallel jaw** | ServoCity | **Servo-Driven Parallel Gripper Kit (Servo Included)** — `3219-0001-0002` | 0–1 | 0–2 | **$34.99 ea** | Buy | **VERIFIED** — same page | Jaws stay parallel through their range via gears and linkages. See §11 |
| Sub-micro gripper (prototyping only) | ServoCity | **Sub-Micro Gripper Kit** — `637104` | 0–1 | 0–2 | **$6.99 ea** | Buy | **VERIFIED** — same page | Servo **not** included; sized for HS-55-class micro servos, which are **not** on Table 12-2. Desk prototype, **not on the robot** |
| **Jaw servo, workhorse** | goBILDA (general supplier) | **2000 Series Dual Mode Servo (25-2, Torque)** — `2000-0025-0002` | 1 | 2 | **$36.99 ea** | Buy | **VERIFIED** — 300 oz-in (21.6 kg·cm) stall @ 6 V, 0.20 s/60° (50 rpm), 4.8–7.4 V, 300°, steel gears | The default claw servo. **Torque variant, not Speed** — a claw needs force, not rate. R502 power check in §16.2. Spends 1 of 8 servo slots (**R503**) |
| Jaw servo, the rule-named one | goBILDA | **2000 Series Dual Mode Servo (25-3, Speed)** — `2000-0025-0003` | 0–1 | 0–2 | **$36.99 ea** | Buy | **VERIFIED** — 130 oz-in (9.3 kg·cm) stall @ 6 V, 0.09 s/60° (115 rpm), 300° | **This exact SKU is named in Table 12-2 (R502)** — the safest possible inspection answer. But 9.3 kg·cm is less than half the Torque variant's grip |
| Jaw servo, budget | goBILDA | **Proton Servo (Torque)** — `2002-0180-0002` / **(Speed)** — `2002-0180-0003` | 1–2 | 2–4 | **$17.99 ea** | Buy | **VERIFIED** price/SKU; **NEEDS-SKU-CHECK on torque and stall current** — the category page does not print them | Steel gears, 180° rotation. Half the price of a Dual Mode. **You must document its 6 V stall torque, no-load speed and stall current against Table 12-2 before an inspector asks (R502).** Good for low-load jobs and the B robot |
| Jaw servo, REV path | REV Robotics (general supplier) | **Smart Robot Servo V2 — Balanced `REV-41-3334`** / **UltraSpeed `REV-41-3336`** | 1 | 2 | **$32.50 ea** | Buy | **VERIFIED** — In Stock. Balanced: 13.5 kg·cm, 0.14 s/60°, 2.1 A stall @ 6 V. UltraSpeed: 5.6 kg·cm, 0.043 s/60°, 2.9 A stall @ 6 V. 4.8–7.4 V | Angular 270° (programmable to 280°) **or continuous rotation** via the SRS Programmer. ⚠ **The V2 is NOT the servo named in Table 12-2** — see the row below and §16.2 |
| ⚠ The rule-named REV servo — **discontinued** | REV Robotics | ~~**Smart Robot Servo `REV-41-1097`**~~ | — | — | ~~$25.50~~ (was $30.00) | — | **VERIFIED this session: Discontinued / Out of Stock** | **This is the servo named in Table 12-2 (R502) and REV no longer sells it.** The same situation as the Servo Power Module `REV-11-1144` (`VENDOR-ECOSYSTEMS.md` §6): legal, unbuyable. **Do not design around it, and do not assume the V2 inherits its Table 12-2 listing** |
| Servo arm / horn | goBILDA | **1900 Series Servo Arm (25T spline, 32 mm)** — `1900-0025-0104` ($4.99) · **1902 Series Dual Servo Arm (25T, 64 mm)** — `1902-0025-0204` ($5.99) | 1–2 | 2–4 | **$4.99–$5.99 ea** | Buy | **VERIFIED** — [25T servo attachments](https://www.gobilda.com/25-tooth-spline-servo-arms) | The **dual** arm is the part for a push-pull two-jaw claw (variant D) — one servo, two symmetric push rods |
| Servo hub (bolt a printed jaw straight to the spline) | goBILDA | **1908 Series Servo Hub (25T, 32 mm)** — `1908-0025-0032` ($8.99) · **1906 Low-Profile** — `1906-0025-0032` ($4.99) · **1921 Plastic** — `1921-0025-0032` ($1.99) | 1–2 | 2–4 | **$1.99–$8.99 ea** | Buy | **VERIFIED** — same page | The 1908 has threaded and thru-holes on the **16 mm pattern**, so a printed jaw bolts on with real fasteners instead of one horn screw. **This is the part that stops jaws working loose** |
| Servo-to-shaft coupler | goBILDA | **4001 Series Clamping Servo-to-Shaft Coupler** — `4001-0025-4008` (25T → 8 mm REX) / `4001-0025-0006` (25T → 6 mm round) | 0–1 | 0–2 | **$9.99 ea** | Buy | **VERIFIED** — same page | Use when the jaw pivot must ride on bearings rather than on the servo's own output bearing. **Strongly recommended — a servo output shaft is not a structural bearing** |
| Servo shaft (spline → shaft) | goBILDA | **1922 8 mm REX Servo Shaft (25T, 36 mm)** — `1922-0025-0036` ($10.99) · **1911 8 mm Round** — `1911-0025-0836` ($9.99) · **1911 10 mm Round** — `1911-0025-1036` ($9.99) · **1923 12 mm REX (48 mm)** — `1923-0025-0048` ($10.99) · **1910 Servo Hub Shaft** — `1910-0025-0816` ($9.99) / `1910-0025-1033` ($12.99) | 0–1 | 0–2 | **$9.99–$12.99 ea** | Buy | **VERIFIED** — same page | Turns the servo into a shaft-output actuator you can support at both ends |
| Jaw-sync gears (variant B) | goBILDA | **2305 Series Brass MOD 0.8 Servo Gear (25T spline)** — 12T `2305-0025-0012` $8.99 · 15T `-0015` $9.49 · 20T `-0020` $9.99 · 24T `-0024` $10.49 · 30T `-0030` $10.99 · 40T `-0040` $11.99 · 48T `-0048` $12.99 | 2 | 4 | **$8.99–$12.99 ea** | Buy | **VERIFIED** — [servo gears](https://www.gobilda.com/25-tooth-spline-servo-gears) | **Brass, broached to the 25T spline.** A matched pair mirrors two jaws off one servo. ⚠ Only **one** gear sits on the servo; the other needs its own bearing-supported shaft |
| Servo mounting | goBILDA | **1802 Servo Frame 43 mm (Std)** — `1802-0043-0001` $7.99 · **(Large)** `1802-0043-0002` $8.99 · **1806 90° Servo Brackets** — `1806-0001-0001` $3.99 · **1801 Servo Plate (Std)** — `1801-0040-0001` $4.99 · **(Large)** `1801-0048-0002` $5.99 · **1800 Servo Pattern Plate (Std)** — `1800-0040-0001` $5.99 · **(Large)** `1800-0040-0002` $6.99 · **1804 Servo Stand (32-1)** — `1804-0032-0001` $6.99 | 1–2 | 2–4 | **$3.99–$8.99 ea** | Buy | **VERIFIED** — [servo mounts](https://www.gobilda.com/servo-mounts/) | Vendor: *"created around the most popular servo sizes in order to integrate them into your goBILDA project."* **JUDGMENT: buy the 1802 frame rather than printing a servo pocket** — a printed pocket is the leading source of claw slop, and $8 × 2 robots is nothing |
| Jaw return spring (R203, §10.3) | goBILDA | **Extension Spring 6.5 mm OD, 1.5 kg, 39–72 mm** — `2915-0001-0003` ($3.99) · **8 mm OD, 8 kg, 48–80 mm** — `2915-0001-0002` ($5.49) · **Compression Spring 2-pack** — `2916-0001-0001` (1.1 kg) / `2916-0001-0002` (2.3 kg), $3.99 each | 1–2 | 2–4 | **$3.99–$5.49** | Buy | **VERIFIED** — [springs](https://www.gobilda.com/springs/) | The 1.5 kg extension spring is the default jaw-open return. ⚠ **No torsion, constant-force or gas springs appear on this page** — see §21 |
| Jaw grip surface | goBILDA | **Silicone Tubing 5 mm ID × 8 mm OD, 50A, 2 m** — `2928-0508-0002` ($5.99) · **Silicone Cord 8 mm, 50A, 2 m** — `2928-0008-0002` ($5.99) | 1 (shared) | 1–2 | **$5.99 ea** | Buy | **VERIFIED** (§4.3) | Slit and slip over a printed jaw edge. Adds grip **and** compliance **and** satisfies R201's no-abrasive-surface requirement in one $6 part |
| Servo programmer (bench tool, **not on the robot**) | goBILDA | **2000 Series Servo Programmer** — `3102-0001-0001` | **1 per program** | **1** | **$12.99** | Buy | **XREF-VERIFIED** — `LEGAL-PARTS-CONSTRAINTS.md` §7 | Sets soft limits and continuous-rotation mode. **R504.C** explicitly permits *"servos … modified as specified by the manufacturer (e.g., setting soft limits or modification for continuous rotation)."* **Buy ONE for the whole program** |
| Servo programmer, REV path | REV Robotics | **SRS Programmer** — `REV-31-1108` | **1 per program** | **1** | **$25.00** | Buy | **VERIFIED** — In Stock | Required to unlock continuous rotation and custom angular limits on the Smart Robot Servo V2. Doubles as a standalone RC servo tester — genuinely useful in the pit |
| Servo programmer, Axon path | goBILDA | **Axon Servo Programmer MK2** — `3102-0002-0001` | 0–1 | 0–1 | **$59.99** | Buy | **XREF-VERIFIED** — `LEGAL-PARTS-CONSTRAINTS.md` §7 | Only if you commit to Axon servos. **Axon MAX+ is named in Table 12-2**; goBILDA sells **Axon MAX MK2 `2004-0025-0002` $99.99** and **Axon MINI MK2 `2004-0025-0001` $99.99 (out of stock)** — **NEEDS-SKU-CHECK that "MAX MK2" is the "MAX+" the table names** |
| ❌ **DO NOT BUY — prohibited by rule** | goBILDA | ~~**Servo Travel Tuner `3109-0002-0001`**~~ ($19.99) · ~~Servo Speed Tuner `3109-0009-0001`~~ · ~~Servo Travel Reverser `3109-0007-0001`~~ | **0** | **0** | — | — | **XREF-VERIFIED** — `LEGAL-PARTS-CONSTRAINTS.md` §14 | **R612's blue box names the goBILDA Servo Travel Tuner by name** as a prohibited device that modifies actuator control signals (**CONFIRMED-BIOBUZZ**, p. 82, re-grepped this session). goBILDA sells it; you may not put it on the ROBOT. **JUDGMENT: the Speed Tuner and Travel Reverser are the same class of device — treat all three as prohibited.** §16.4 gives the legal way to get the same effect |

**The rule that separates the programmer from the tuner, stated once.** A servo **programmer** changes
settings *inside the servo* on the bench and then comes off the robot — **legal, R504.C**. A **tuner** stays
*in the signal line on the robot* and modifies the control signal in flight — **prohibited, R612**. Same
vendor, same aisle, opposite legality. Put a label on the pit box.

### 10.5 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Student-hours (1st robot) | Student-hours (2nd robot) |
|---|---|---|---|---|
| **Jaw pair** (or moving jaw + fixed backstop) | PETG, 5 perimeters; **TPU-lined contact face** | 3D printer + soldering iron for M3 heat-set inserts | 4–6 h incl. 2–3 print iterations | **0.8 h** — reprint the frozen file |
| **Gripper frame / carrier plate** tying servo mount to jaw pivots | 3 mm polycarbonate or printed PETG | Printer, or jigsaw + drill press | 3–4 h | 0.7 h |
| **Jaw pivot bearing pockets** | Printed pockets for `1611` flanged bearings, or bought pillow blocks | 3D printer | 1.5 h | 0.3 h |
| **Compliant jaw liner** — silicone tubing slit and bonded, or printed TPU pad | `2928-0508-0002` tubing + CA glue, or TPU print | Hand tools / printer | 1 h | 0.3 h |
| **Spring anchor / return path** (R203) | Printed PETG anchors + `2915-0001-0003` | 3D printer | 1 h | 0.2 h |
| **Wiring, horn indexing, soft-limit programming, tuning** | — | Hand tools + servo programmer | 3–4 h | 1.5–2 h |
| **R203 dead-robot removal test, documented** | — | — | 0.5 h | 0.5 h |
| **TOTAL** | | | **≈ 14–18 h** | **≈ 4.3–5 h** |

**⚠ The horn-indexing trap that costs two hours per robot.** A 25-tooth spline indexes in **14.4° steps**. If
you bolt the arm on at the wrong tooth, the jaw's mechanical range and the servo's electrical range no
longer overlap, and the servo stalls against its own hard stop — which reads to students as "the claw is
weak" or "the servo burned out." **Procedure: centre the servo in software first, then fit the horn, then
set soft limits with the programmer, then design the hard stops.** Do it in that order on both robots and
write the tooth index on the part in marker.

### 10.6 Approximate subtotal

Variant A (single moving jaw against a fixed backstop), goBILDA ecosystem, list prices as of August 2026:

| Line | Per robot | For 2 robots |
|---|---|---|
| 1 × Dual Mode Torque servo (`2000-0025-0002`) | $36.99 | $73.98 |
| 1 × Servo Frame 43 mm (`1802-0043-0001`) | $7.99 | $15.98 |
| 1 × Servo Hub (`1908-0025-0032`) | $8.99 | $17.98 |
| 1 × extension spring (`2915-0001-0003`) | $3.99 | $7.98 |
| Silicone tubing share (`2928-0508-0002`) | ~$3.00 | $5.99 (one 2 m length) |
| 2 × flanged bearings (1 × `1611-0514-4008`) | $5.99 | $11.98 |
| Filament, heat-set inserts, M3/M4 hardware | ~$10 | ~$20 |
| Polycarbonate share (`REV-41-3049-PK5`) | ~$2.20 | $5.50 |
| **Subtotal, variant A, ESTIMATE** | **≈ $79** | **≈ $159** |

| Alternative build | Per robot | For 2 robots |
|---|---|---|
| **Bought ServoCity kit** (`3219-0002-0002`, servo included) + printed custom jaws + hardware | **≈ $45** | **≈ $90** |
| **Variant B** (geared twin jaws: +2 × 20T brass gears, +1 stub shaft, +2 bearings) | ≈ $115 | ≈ $230 |
| **Variant F** (claw + wrist + rotate: 3 servos, 3 mounts, 3 horns) | ≈ $190 | ≈ $380 |

**JUDGMENT: budget $80–$120 per robot, $160–$240 for the pair**, for a team-built single-servo claw. Note the
uncomfortable arithmetic: **the bought ServoCity kit is the cheapest option on the page**, because it bundles
a servo for less than a bare Dual Mode servo costs. That is a legitimate B-team answer under R303.G — and
§1.4 explains why it should not be the A-team's whole story. **VERIFY-BEFORE-ORDER.**

### 10.7 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare to stock (2 robots) |
|---|---|---|---|
| **Element squirts out sideways under load** | Two-point contact on a round or tapered element; no third constraint | Add a V-groove or a third contact pad; go compliant (§12) | — (design fix) |
| **Servo strips its gears** | Jaw driven into a hard stop; no soft limits; stall held all MATCH | **Soft limits via the programmer**, then a *compliant* hard stop, then never command full close — command 3–5° short of contact and let the spring take up the rest | **1 spare servo per program minimum** ($36.99). REV path: **Replacement Gear Set for SRS V2, $13.50** (**VERIFIED**); for the original SRS, `REV-41-1168` $11.05 (**VERIFIED**) |
| Jaw works loose and drifts out of alignment | Single horn screw carrying all the torque | Use the **1908 servo hub** and bolt through the 16 mm pattern; blue threadlocker | 2 spare hubs |
| Printed jaw snaps at the root | Layer lines across the bending load; no fillet | **Reprint flat so the bending load runs in-plane** (§18.3); add a root fillet; 5 perimeters | **2 spare jaw pairs, printed, in the pit bag** |
| **Claw fails the R203 powered-off test** | Non-backdrivable gearing, or an undercut pocket | Spring-open default (§10.3) | — |
| Servo buzzes and heats while holding | Commanded past the mechanical stop; fighting itself | Back the hold position off; check horn tooth index (§10.5) | — |
| Element crushed or marked (**R201** exposure) | Full-torque close on a soft element | Compliant liner; partial close; inspect the element for marking after every practice session | Tubing offcut |
| Servo wire pulled out at the connector | Wire flexed at the moving joint with no strain relief | Service loop + zip-tie anchor **on the fixed side of the joint** | Servo extension cables |
| Claw and wrist collide at some angles | Reachable envelope never mapped | Map it in CAD **before** printing v2 | — |

### 10.8 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Architecture | Variant A: one moving jaw against a printed backstop — **or** the bought `3219-0002-0002` kit, unmodified | Variant A or B with a TPU-lined jaw profiled to the element, spring return, bearing-supported pivot |
| Servo | 1 × Proton Torque `2002-0180-0002` ($17.99), spec documented against Table 12-2 | 1 × Dual Mode Torque `2000-0025-0002`, soft-limited, current-monitored |
| Mounting | Printed servo pocket | `1802-0043-0001` frame + `1908` hub |
| Grip surface | Bare PETG | Silicone tubing or printed TPU pad |
| Control | Button = open / closed | Two-stage close (approach / grip), hold-position back-off, jam detect |
| R203 | Tested by hand, once | **Spring-open by design**, tested and documented for the Portfolio |
| Actuator cost | **1 servo** | **1 servo** (2 with a wrist — audit it) |
| Est. cost / robot | **~$45** | **~$110** |
| Build time | ~6 h | ~17 h |

---

## 11. E-2 — Linkage and parallel-jaw grippers

### 11.1 What it is and when a design needs it

A pivoting claw (§10) closes on an **arc**, so the contact point slides along the element and the jaw angle
changes through the grip. A **parallel-jaw** gripper keeps both faces parallel throughout travel, using a
gear pair, a four-bar linkage per jaw, or a rack and pinion.

**A design needs parallel jaws when:**

- the element is a **panel, plate, or flat-sided block** whose faces must stay square to the jaws;
- the element must be **held at a controlled position**, not merely retained — an arc jaw shifts the element
  as it closes, which destroys placement repeatability;
- the grip must work across a **range of element sizes** without the contact angle changing;
- the element is **stiff and smooth**, so you need face-to-face friction rather than a wedging pinch.

**A design does not need them** for spheres, cones, or anything self-centring — an arc jaw or a compliant
finger is cheaper, lighter and more forgiving.

**Actuator cost: 1 servo.** Parallelism is a *mechanism* property, not an extra degree of freedom — which is
exactly why R303 still treats this as a single-DoF device.

### 11.2 The main variants

| Variant | Description | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|---|
| **A. Geared parallel jaws** | Two meshed brass servo gears — one on the servo, one on a bearing shaft; jaw plates bolted to each | 3 | 3 | 3 | 4 | 4 |
| **B. Four-bar per jaw** | Each jaw carried on a parallelogram so it translates without rotating | **4** | 3 | 4 | 4 | 3 |
| **C. Dual servo arm + two push-rod ball linkages** | One `1902` dual arm driving two slider jaws through `2903` ball linkages | 3 | 2 | 3 | 4 | 4 |
| **D. Rack and pinion** | Servo pinion between two opposed printed racks | **4** | 2 | 4 | 3 | 3 |
| **E. Bought parallel gripper kit** | ServoCity `3219-0001-0002`, servo included | **1** | 2 | **1** | 4 | **5** |
| **F. Single jaw sliding against a fixed parallel face** | Only one side moves; the other is a static wall | **1** | **1** | **2** | **5** | **5** |

**JUDGMENT for this program: variant F first; A or E if the element genuinely needs two moving faces.**
Variant F gets you every benefit of parallel jaws — flat face-to-face contact, no arc shift, square
placement — at the parts count of a single-jaw claw. Half of what teams want from "parallel jaws" is really
just "the element must not rotate as I grip it," and a fixed reference face delivers that. Variants B and D
are where the mentor hours go: a four-bar needs **four link lengths matched to ~0.5 mm** (the same warning
`EXTENSION-ARMS-LIFTS.md` gives about four-bar arms), and printed racks skip teeth under load.

### 11.3 ⚠ The COTS legality line for a bought gripper

**CONFIRMED-BIOBUZZ, R303.G** (p. 70): a **single DoF gripper** is an allowed COTS MECHANISM.
**CONFIRMED-BIOBUZZ, R303 Example 3** (p. 70, verbatim): *"grippers that incorporate additional actuators
providing additional twisting and/or bending actions (like a wrist) add degrees of freedom that are
prohibited in COTS MECHANISMS."*

Read together, the line is sharp:

| Assembly | Verdict |
|---|---|
| Bought parallel gripper kit, as sold, bolted to your arm | ✅ Legal COTS single-DoF mechanism, **R303.G** |
| Bought gripper + **your own** wrist servo, integrated by your team | ✅ Legal — **your assembly** is not a COTS mechanism; it is a team-built MAJOR MECHANISM containing a COTS component. **Document this in the Engineering Portfolio** |
| A **vendor-sold** gripper-plus-wrist as a single product | ❌ Prohibited COTS mechanism, **R303 Example 3** |
| A vendor's purpose-built BIOBUZZ scoring end effector, if one appears after Kickoff | ❌ Prohibited COTS **MAJOR MECHANISM**, **R301** |
| A shop building your published gripper design "to print" for you | ❌ **R301** blue box: *"A vendor selling 'build to print' manufacturing of publicly available, purpose-built solutions is against the spirit of this rule."* |

**JUDGMENT, repeated from §1.4 because it lands hardest here:** buying the gripper is legal and is a
reasonable **B-team** decision. Making it the A-team's entire scoring answer costs the design narrative that
R101 and the judged awards are both built around. Buy one, learn from it, print your own jaws onto it.

### 11.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Complete-kit option** | ServoCity | **Servo-Driven Parallel Gripper Kit (Servo Included)** — `3219-0001-0002` | 0–1 | 0–2 | **$34.99 ea** | Buy | **VERIFIED** — [gripper kits](https://www.servocity.com/gripper-kits/) | *"jaws remain parallel to one another throughout their range thanks to the unique gears and linkages,"* driven by an included Proton Torque Servo. **R303.G legal.** ⚠ The included Proton's 6 V specs are not printed — **NEEDS-SKU-CHECK against Table 12-2 before inspection (R502)** |
| Jaw-sync gear pair (variant A) | goBILDA | **2305 Series Brass MOD 0.8 Servo Gear, 25T spline** — 20T `2305-0025-0020` ($9.99) · 24T `2305-0025-0024` ($10.49) · 30T `2305-0025-0030` ($10.99) | 2 (matched) | 4 | **$9.99–$10.99 ea** | Buy | **VERIFIED** — [servo gears](https://www.gobilda.com/25-tooth-spline-servo-gears) | **Buy a matched pair of the same tooth count** — unequal gears give unequal jaw travel. ⚠ Only one gear rides the servo spline; the second needs a bearing-supported stub shaft, so budget a `1611` bearing pair with it |
| Ball linkages (variants B, C) | goBILDA | **2903 Series Nylon Ball Linkage (M4, 24.5 mm) 4-pack** — `2903-0004-0245` ($4.99) · **2913 Steel Ball Linkage, Female M4, 24.1 mm, 2-pack** — `2913-0004-0241` ($4.99) · **Male M4, 29.4 mm, 2-pack** — `2913-0104-0294` ($4.99) | 1 pack | 2 packs | **$4.99 / pack** | Buy | **VERIFIED** — [M4 ball linkages](https://www.gobilda.com/m4-ball-linkages) | **Explicitly legal beyond the single-DoF cap: R303.L** allows *"items that connect structures at variable angles (such as ball joint linkages, rod ends, and similar items)."* Vendor: the steel ball *"swivel[s] freely inside the nylon body so that your linkage assembly transfers the force acting on it without robbing unnecessary power"* |
| Threaded rod for linkage legs | goBILDA | **2808 Series Stainless Steel Threaded Rod, M4 × 0.7 mm** (e.g. 70 mm, 2-pack) | 1–2 packs | 2–4 packs | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** — [M4 threaded rods](https://www.gobilda.com/m4-threaded-rods) category verified; individual lengths/prices not read | Length depends on the element (**DEFERRED**). **Do not order until the jaw span is known** |
| Jaw servo | goBILDA / REV | as §10.4 — **`2000-0025-0002`** ($36.99) preferred | 1 | 2 | **$36.99 ea** | Buy | **VERIFIED** | A parallel jaw loses more torque into the linkage than an arc jaw does. **Buy the Torque variant** |
| Servo mounting, arms, hubs, couplers | goBILDA | as §10.4 — `1802-0043-0001` frame, `1902-0025-0204` dual arm, `1908-0025-0032` hub, `4001-0025-4008` coupler | 1 set | 2 sets | **≈ $28 / set** | Buy | **VERIFIED** | The **dual servo arm** `1902-0025-0204` ($5.99) exists precisely for symmetric push-pull — the correct part for variant C |
| Jaw slides / linear guide (variants D, F) | goBILDA | drawer-slide and linear-motion families | 0–2 | 0–4 | see notes | Buy | **XREF-VERIFIED** — `EXTENSION-ARMS-LIFTS.md` covers linear motion; **not re-spec'd here** | **JUDGMENT: for a jaw travelling under ~40 mm, a printed dovetail with a nylon rub strip beats any bought slide** — cheaper, lighter, and it needs no alignment work on the second robot |
| Return spring, grip surface, bearings | goBILDA | as §10.4 (`2915-0001-0003`, `2928-0508-0002`, `1611-0514-4008`) | — | — | **≈ $14 / robot** | Buy | **VERIFIED** | The spring-open default for R203 (§10.3) applies here identically |

### 11.5 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st robot) | Hours (2nd robot) |
|---|---|---|---|---|
| **Jaw plates with flat compliant faces** | PETG body + TPU or silicone contact face | 3D printer | 4–5 h incl. iteration | 0.8 h |
| **Gear-pair carrier plate** — holds the two gear centres at exact centre distance | 3 mm polycarbonate or printed PETG | Printer / jigsaw + drill press | **4–6 h** — this is the precision part | 0.8 h |
| Stub shaft + bearing pockets for the idler gear | Printed pockets + `1611` bearings + 8 mm REX stub | Printer, hand tools | 2 h | 0.4 h |
| Four-bar links (variant B only) | 1/8 in aluminium bar or printed PETG | Drill press + careful marking | **5–7 h** — four links matched to ~0.5 mm | **2 h** (matching does **not** fully transfer) |
| Printed dovetail slide + nylon rub strip (variant F) | PETG + UHMW/nylon strip | Printer | 2–3 h | 0.5 h |
| Spring anchors, wiring, soft limits, tuning | — | Hand tools + programmer | 3–4 h | 1.5 h |
| R203 dead-robot removal test, documented | — | — | 0.5 h | 0.5 h |
| **TOTAL, variant A or F** | | | **≈ 16–21 h** | **≈ 4.5–5 h** |
| **TOTAL, variant B (four-bar)** | | | **≈ 22–28 h** | **≈ 7–8 h** |

**⚠ Gear centre distance is the whole game in variant A.** MOD 0.8 gears mesh correctly at
**centre distance = 0.8 × (N₁ + N₂) / 2 mm** — for two 20T gears that is **16.0 mm**; for 20T + 30T it is
**20.0 mm**. Print the carrier plate with the two holes **slotted by 1 mm** so the mesh can be set by feel
and locked. Get it wrong and the gears either bind (servo stalls, reads as "weak claw") or backlash (jaws
rattle, placement repeatability gone). **This is the number to re-check when you build the second robot** —
a slightly warped second print shifts it more than you would guess.

### 11.6 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| 1 × Dual Mode Torque servo (`2000-0025-0002`) | $36.99 | $73.98 |
| 2 × 20T brass servo gears (`2305-0025-0020`) | $19.98 | $39.96 |
| 1 × servo frame (`1802-0043-0001`) | $7.99 | $15.98 |
| 1 × servo hub (`1908-0025-0032`) | $8.99 | $17.98 |
| 2 × flanged bearings + 8 mm REX stub shaft | ~$12 | ~$24 |
| 1 × nylon ball linkage 4-pack (`2903-0004-0245`) | $4.99 | $9.98 |
| Spring + silicone tubing share | ~$7 | ~$14 |
| Filament, inserts, M3/M4 hardware, polycarbonate share | ~$14 | ~$28 |
| **Subtotal, variant A, ESTIMATE** | **≈ $112** | **≈ $224** |

| Alternative | Per robot | For 2 robots |
|---|---|---|
| **Bought kit** `3219-0001-0002` + printed custom jaws | **≈ $50** | **≈ $100** |
| **Variant F** (one moving jaw, fixed parallel face) | **≈ $72** | **≈ $145** |
| Variant B (four-bar per jaw) | ≈ $130 | ≈ $260 |

**JUDGMENT: budget $70–$130 per robot, $145–$260 for the pair. VERIFY-BEFORE-ORDER.**

### 11.7 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Jaws rattle; placement not repeatable** | Gear backlash, or ball-linkage slop stacked across four joints | Slotted gear centres set by feel; preload the linkage with a light spring; use fewer joints | Spare linkage pack ($4.99) |
| **Servo stalls — "the claw is weak"** | Gear mesh too tight (centre distance under 16.0 mm for a 20T pair) | Re-set the mesh; check for a warped carrier plate | — |
| Jaws close unevenly | Mismatched gear tooth counts, or unequal linkage legs | Matched pair; measure both legs | — |
| Printed rack skips teeth (variant D) | Plastic teeth loaded in shear; layer lines across the tooth root | Abandon printed racks in load paths; use gears or a linkage | — |
| Four-bar goes over-centre and locks | Link geometry never checked at travel extremes | Hard stops **before** the toggle point | — |
| Panel slips out of flat jaws | Smooth face-to-face contact, no friction budget | TPU or silicone face; more servo torque; a lip that catches the panel edge (⚠ **re-test against R203**) | Tubing offcut |
| Carrier plate flexes and the mesh opens under load | 3 mm polycarbonate spanning too far unsupported | Fold a flange, add a printed rib, or sandwich the gears between two plates | 2 spare carrier plates |
| **Second robot's gripper behaves differently** | Second carrier plate printed on a different machine, or warped | Print both carriers **in the same batch on the same machine** (§19.2) | — |

### 11.8 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Architecture | Variant F: one jaw sliding against a fixed face — **or** the bought `3219-0001-0002` kit | Variant A: geared parallel jaws, slotted mesh, bearing-supported idler |
| Faces | Flat PETG | TPU-faced, profiled to the element |
| Precision | "It grips" | Repeatable to a few mm at the placement point, **measured** |
| Control | Open / closed | Staged close, torque back-off, jam detect |
| Actuator cost | **1 servo** | **1 servo** |
| Est. cost / robot | **~$50** | **~$115** |
| Build time | ~7 h | ~20 h |

---

## 12. E-3 — Compliant "finger" grippers

### 12.1 What it is and when a design needs it

Fingers made of a soft material — printed TPU, silicone tubing over a spring steel spine, or moulded
rubber — that **deform around** the element instead of clamping onto it. The grip comes from elastic
recovery, not from servo torque. In its purest form the gripper has **no actuator at all**: the fingers are
pushed onto the element by the arm, and pulled off it by the arm.

**A design needs compliant fingers when:**

- the element is **irregular, soft, or deformable**, so no rigid jaw profile fits it;
- the element is **fragile or markable**, and R201's *"gouging, tearing off pieces, or routinely and
  repeatedly marking SCORING ELEMENTS"* prohibition is a live risk;
- the acquisition point has **poor alignment tolerance** and the driver cannot be relied on to hit it (§17);
- the element **self-centres under a conical or radial guide** — cones are the textbook case (§2.1);
- you want retention that **cannot fail R203**, because the element pulls free by deforming the fingers.

**A design does not need them** when the element must be held rigidly against a large disturbance force —
compliance is exactly the wrong property when you are carrying a heavy element up a fast lift and it must
not shift.

**Actuator cost: 0 or 1 servo.** The zero-servo version is the reason this section deserves close reading in
a program with an 8-servo ceiling across two robots.

### 12.2 The main variants

| Variant | Description | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|---|
| **A. Passive TPU finger cup — zero actuators** | Printed TPU fingers on the arm; push on, pull off | **1** | **1** | 3 | 4 | **5** |
| **B. Servo-squeezed TPU fingers** | One servo pulls a band or a linkage that closes soft fingers | 2 | 2 | 2 | **5** | **5** |
| **C. Tendon / cable-driven fingers** | Servo winds a cable routed through the fingers, curling them | **4** | 2 | **4** | 3 | 3 |
| **D. Silicone tubing over spring-steel spines** | Tubing sleeves on flexible strips | 2 | **1** | 3 | 4 | 4 |
| **E. Passive "bristle nest" / brush cup** | A cluster of soft bristles the element pushes into | 2 | 2 | 3 | 3 | 4 |
| **F. Compliant finger + rigid backstop** | Soft fingers on one side, a hard reference face on the other | 2 | **1** | **2** | **5** | **5** |

**JUDGMENT for this program: variant A if the element geometry allows it, otherwise F.** Variant A is the
single cheapest, most duplicable, most rule-safe end effector in this entire file: no servo slot, no wiring,
no tuning, no R203 argument, and the second robot's version is a reprint. Its weakness is that **retention
force is fixed at design time** — you cannot tune it in the pit without a reprint, which is why the tuning
burden scores 3 rather than 1. Variant C looks impressive in a CAD render and consumes a shocking number of
mentor hours; do not start there.

### 12.3 Why compliance is legally as well as mechanically attractive

Three rules all point the same direction, and it is worth seeing them together:

| Rule | Text (CONFIRMED-BIOBUZZ) | Effect on a compliant gripper |
|---|---|---|
| **R203** (p. 69) | *"ROBOTS must allow removal of SCORING ELEMENTS from the ROBOT … while powered off."* | ✅ **Automatically satisfied.** The element pulls free by deforming the fingers, powered or not |
| **R201** (p. 68) | *"Gouging, tearing off pieces, or routinely and repeatedly marking SCORING ELEMENTS are violations of this rule…"* and *"features with abrasive surfaces that scratch objects that rub across them"* | ✅ Soft, non-abrasive contact is the lowest-risk answer available |
| **R202** (p. 68-69), item I | *"devices or conditions that pose an unnecessary risk of **entanglement**"* | ✅ No pinch point, no nip, no fast-moving hard edge |
| **R801** (p. 87) | No generated vacuum | Compliance is the **legal substitute** for the suction gripper you cannot build (§14) |

**JUDGMENT: when in doubt at Kickoff, prototype the compliant version first.** It is the fastest thing on
this page to get to a working demonstration — a TPU finger set prints overnight — and it is the version
least likely to be argued with at inspection.

### 12.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **TPU filament, 95A** (the primary material) | General retail — **not** a FIRST vendor item | TPU / TPE flexible filament, 1.75 mm, **~95A Shore** | ~0.3 kg | ~0.6 kg | **≈ $25–$40 / kg** | Buy | **UNVERIFIED — no vendor page loaded this session. FAMILY named only.** | **Do not order on this row alone.** Legal as raw material: **R302.C** permits *"metals, plastic, rubber, and wood"* (**CONFIRMED-BIOBUZZ**, p. 69). ⚠ Softer TPU (85A) needs a direct-drive extruder; 95A is the safe default for a bed-slinger. See §18.2 |
| Silicone tubing (finger sleeves, variant D) | goBILDA | **Silicone Tubing, 5 mm ID × 8 mm OD, 50A, 2 m** — `2928-0508-0002` ($5.99) · **Silicone Cord, 8 mm, 50A, 2 m** — `2928-0008-0002` ($5.99) | 1–2 | 2–4 | **$5.99 ea** | Buy | **VERIFIED** — [intake wheels](https://www.gobilda.com/intake-wheels/) | The cheapest compliant contact surface in the catalogue. Slit it lengthwise and it becomes a jaw liner; leave it whole and it is a finger sleeve |
| Surgical tubing (larger, grippier fingers) | AndyMark (**official FIRST supplier**) | **Black Surgical Tubing** — 1/8 in ID × 3/8 in OD · 5/8 in ID × 7/8 in OD | 1 length | 2 lengths | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** — product pages surfaced in search this session, **individual prices not read** | Vendor description: *"a must-have for gripping game elements on custom intakes."* ⚠ Latex — **check for team latex allergies before buying**, and see §6 for the R201/R202 fraying and entanglement warnings that apply to any exposed tubing |
| Finger spines (variant D) | goBILDA / general | Spring steel strip, or 1 mm polycarbonate strip cut from `REV-41-3049-PK5` | 2–6 | 4–12 | **~$1 / robot** | Fab from stock | **XREF-VERIFIED** (polycarbonate SKU, §18) | A 1 mm polycarbonate strip is a perfectly good finger spine and you already own the sheet |
| Finger closing servo (variant B only) | goBILDA / REV | as §10.4 — **`2000-0025-0002`** ($36.99) or **Proton `2002-0180-0002`** ($17.99) or **SRS V2 `REV-41-3334`** ($32.50) | 0–1 | 0–2 | **$17.99–$36.99** | Buy | **VERIFIED** | Compliant fingers need far less torque than a rigid jaw — **this is the one place a $17.99 Proton is genuinely the right part**, saving $38 across two robots |
| Elastic closing band (variant B, servo-free bias) | goBILDA | **Extension Spring 6.5 mm OD, 1.5 kg** — `2915-0001-0003` ($3.99) | 1–2 | 2–4 | **$3.99 ea** | Buy | **VERIFIED** — [springs](https://www.gobilda.com/springs/) | Springs the fingers **closed**; the servo or the arm motion opens them. ⚠ Verify R203 by hand — a strongly sprung-closed finger set can still trap an element |
| Cable / tendon (variant C) | General retail | Braided fishing line / Spectra cord, ~100 lb class | 1 spool (shared) | 1 spool | **NEEDS-SKU-CHECK** | Buy | **UNVERIFIED** | `EXTENSION-ARMS-LIFTS.md` specifies cord for winches — **use whatever that file already verified rather than sourcing a second cord** |
| Mounting hardware | goBILDA | 16 mm pattern hardware, M3/M4, heat-set inserts | — | — | ~$8 / robot | Buy | **XREF-VERIFIED** — `VENDOR-ECOSYSTEMS.md` §6.5 | Cross-reference; not re-spec'd here |

**Note on the complete-kit option:** there is **no COTS compliant-finger gripper kit** from the standard FTC
vendors that I verified this session. This mechanism is fabrication-first by nature — which is precisely why
it is cheap and why it duplicates well.

### 12.5 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st robot) | Hours (2nd robot) |
|---|---|---|---|---|
| **TPU finger set** (typically 3–6 fingers) | TPU 95A, 2–4 mm wall, 100 % or gyroid infill | 3D printer (direct-drive preferred), slow print | **5–8 h** across 3–4 durometer/geometry iterations | **1 h** — reprint the frozen file |
| **Finger carrier / palm plate** | PETG or 3 mm polycarbonate | Printer or hand tools | 2–3 h | 0.5 h |
| **Rigid backstop face** (variant F) | PETG, TPU-faced | Printer | 1.5 h | 0.3 h |
| Spine + sleeve assembly (variant D) | Polycarbonate strip + silicone tubing | Scissors, hand tools | 2 h | 0.5 h |
| Servo mount + band routing (variant B) | Printed PETG | Printer | 2 h | 0.4 h |
| **Element retention testing** — drop test, shake test, drive-over-a-seam test | — | — | **3 h** | **1.5 h** |
| R203 dead-robot removal test, documented | — | — | 0.5 h | 0.5 h |
| **TOTAL, variant A** | | | **≈ 11–15 h** | **≈ 3.3–4 h** |

**⚠ TPU printing is the one place this program's "3D printers and hand tools" capability gets tested.**
Practical guidance, all **JUDGMENT**:

- **Print slow.** 15–25 mm/s. TPU that prints fast under-extrudes and the finger is weak where it matters.
- **Retraction near zero**, or the flexible filament buckles in the extruder path.
- **Dry the filament.** TPU absorbs moisture faster than PETG and wet TPU prints stringy and brittle.
- **Design the finger with a thick root and a thin tip.** The root carries the moment; the tip does the
  conforming. A constant-section finger either flops or refuses to bend.
- **Iterate wall thickness, not material.** Going 2.0 mm → 2.5 mm changes the stiffness far more predictably
  than swapping to a different filament brand, and it keeps your second robot reproducible.
- **Print both robots' finger sets in one batch** (§19.2). Two TPU prints from different spools genuinely
  behave differently.

### 12.6 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| TPU filament share (~0.3 kg of a $30 spool, **UNVERIFIED price**) | ~$9 | ~$18 (1 spool covers both) |
| Silicone tubing (`2928-0508-0002`) | $5.99 | $11.98 |
| Polycarbonate share (`REV-41-3049-PK5`) | ~$2.20 | $5.50 |
| PETG palm/carrier, hardware, inserts | ~$8 | ~$16 |
| **Subtotal, variant A (zero-actuator), ESTIMATE** | **≈ $25** | **≈ $52** |
| **Actuator slots consumed, variant A** | **0 motors, 0 servos** | — |

| Alternative | Per robot | For 2 robots |
|---|---|---|
| **Variant B with a Proton servo** (`2002-0180-0002`) | ≈ $45 | ≈ $92 |
| Variant B with a Dual Mode servo | ≈ $64 | ≈ $130 |
| Variant D (tubing over polycarbonate spines) | ≈ $18 | ≈ $38 |

**After the passive intake (§9), this is the second-cheapest MAJOR MECHANISM in the catalog, and the only
end effector that can cost zero actuator slots.** In a season where R503 caps you at 8 motors and 8 servos
and you are buying every slot twice, that is a strategically important fact, not a footnote.
**VERIFY-BEFORE-ORDER.**

### 12.7 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Element falls out during a fast drive or a hard stop** | Retention force fixed too low at design time | Thicker finger root; more fingers; add a rigid backstop (variant F) | **2 spare finger sets, printed** |
| **Element cannot be released — comes back with the robot** | Retention too high; no positive ejection path | Add a servo or arm motion that strips the element off; taper the finger tips | — |
| TPU finger takes a set and stops springing back | Held deformed for long periods; heat in a hot gym or a car boot | Store the robot with the gripper **relaxed**; thicker section; check fingers between events | **1 spare set per robot** |
| Finger tears at the layer line | Printed with layers across the bending root | **Reprint so the bend loads run in-plane** (§18.3); increase root fillet | — |
| Grip degrades over a competition day | TILE dust and element residue glazing the TPU | **Wipe the fingers with isopropyl alcohol between MATCHES** — put it on the pit checklist | IPA wipes |
| Fingers snag on FIELD elements (**R202** entanglement) | Long, thin, splayed fingers | Shorter, thicker fingers; no free-flapping tips | — |
| Inconsistent behaviour between robot A and robot B | Different spools, different machines, different print days | Print both sets in one batch from one spool (§19.2) | — |
| Element marked or scuffed (**R201**) | Filler or texture in the TPU acting abrasive | Smooth-walled print; test on a real element and inspect it | — |

### 12.8 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Architecture | Variant A: 4 printed TPU fingers on a PETG palm, zero actuators | Variant F: TPU fingers against a rigid backstop, servo-assisted release, geometry tuned to the element over 4+ iterations |
| Material | One TPU spool, one wall thickness | Wall thickness swept and **measured** for retention force |
| Testing | "It holds when we shake it" | Drop test, seam-crossing test, retention force measured with a spring scale, documented |
| R203 | Passes trivially | Passes trivially, **and documented in the Portfolio as a design driver** |
| Actuator cost | **0** | **0–1 servo** |
| Est. cost / robot | **~$20** | **~$45** |
| Build time | ~7 h | ~15 h |

---

## 13. E-4 — Over-center latches and zero-actuator retention

### 13.1 What it is and when a design needs it

Retention without an actuator holding it. A geometry or an energy store keeps the element captive, and the
robot spends **no motor slot and no servo slot** doing it. Four families:

- **Over-center latch** — a sprung arm that snaps past a toggle point into a stable closed state.
- **Detent** — a spring-loaded ball, a magnet, or a printed bump that the element clicks past.
- **Gravity pocket** — a printed cradle the element simply sits in, held by its own weight.
- **Friction / interference nest** — soft walls sized under the element so it is gently pinched at rest.

**A design needs zero-actuator retention when:**

- the element must be **held for a long time** (all of AUTO plus half of TELEOP) and you refuse to hold a
  servo stalled for 90 seconds;
- you are **out of actuator slots** — the R503 8+8 ceiling, spent twice, is the constraint this whole
  section exists to relieve;
- the release is **already happening** for another reason: the arm lifts, the flywheel takes the element,
  the drivetrain reverses. If something else already supplies the release motion, retention needs no motor.

**Actuator cost: 0.** That is the entire point.

### 13.2 The main variants

| Variant | Description | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|---|
| **A. Gravity pocket / cradle** | Printed nest sized to the element | **1** | **1** | **1** | **5** | **5** |
| **B. Magnetic detent** | Permanent magnet holds a steel element or a steel-tabbed gate | **1** | **1** | 2 | 4 | **5** |
| **C. Sprung one-way flap** | Element pushes past a sprung gate and cannot fall back | 2 | **1** | 2 | 4 | **5** |
| **D. Over-center toggle latch** | Sprung arm snaps past dead-centre into a stable closed state | 3 | **1** | **4** | 3 | 4 |
| **E. Friction nest (soft walls)** | Silicone/TPU walls set under the element dimension | **1** | **1** | 3 | 4 | **5** |
| **F. Ratchet / one-way bearing hold** | A ratchet holds the mechanism, and hence the element | 2 | 3 | 2 | 4 | 4 |

**JUDGMENT: build variant A or E; use B as a refinement; approach D with caution and F only with a manual
release.** A gravity pocket costs one printed part and never fails. An over-center latch is genuinely
elegant and genuinely fiddly — the toggle point moves as the spring relaxes over a season, and the tuning
burden score of 4 is not a guess.

### 13.3 ⚠ R203 governs this section more tightly than any other

Zero-actuator retention is, by construction, retention **that works when the robot is powered off**. That is
the exact condition **R203** cares about (**CONFIRMED-BIOBUZZ**, p. 68): *"ROBOTS must allow removal of
SCORING ELEMENTS from the ROBOT and the ROBOT from FIELD elements while powered off."*

**The rule does not prohibit unpowered retention. It requires unpowered *removability*.** Those are
different, and the difference is the whole design brief:

| Design | R203 verdict | Why |
|---|---|---|
| Gravity pocket, open top | ✅ Passes | Lift the element out |
| Friction nest in soft walls | ✅ Passes | Pull it out against the compliance |
| Magnetic detent | ✅ Passes **if a hand can overcome the magnet** | Size the magnet for a firm pull, not a heroic one. **Test it** |
| Sprung one-way flap **with a labelled finger tab** | ✅ Passes | A human opens the flap. See §9.3, which makes the same point for passive intakes |
| Sprung one-way flap **without** a release | ❌ **Fails** | The element is captive |
| Over-center latch **with an exposed manual release** | ✅ Passes | A human pops the toggle |
| Over-center latch with no release, or one needing a tool | ❌ **Fails** | Also a FIELD RESET delay, which is a competitive cost as well as a rules cost |
| **Ratchet or one-way bearing holding a jaw closed on the element** | ❌ **Fails** | ⚠ **The trap.** R303.H makes ratcheting devices legal as COTS mechanisms, so teams reach for them and assume the whole application is fine. **Legality of the component does not make the application legal.** Add a pawl release lever |

**JUDGMENT — one design rule covers all six variants.** Every zero-actuator retention feature on either
robot gets an **exposed, labelled, tool-free manual release**, and every one is signed off with the dead-
robot test from §1.1: kill the breaker, hand the robot to a student who did not build it, element out in
under five seconds, two hands, no tools. Run it on **both robots** and photograph it for the Portfolio.

### 13.4 The magnet allowance, stated precisely

**CONFIRMED-BIOBUZZ, R302** (p. 69-70): allowed raw materials include *"A. sheet stock, B. extruded shapes,
C. metals, plastic, rubber, and wood, and **D. magnets**."*

**CONFIRMED-BIOBUZZ, R506** (p. 77-78, re-grepped verbatim this session): *"The use of relays,
**electromagnets**, and electrical solenoid actuators is prohibited."*

So: **permanent magnets are explicitly legal raw material; electromagnets are explicitly prohibited.** A
neodymium disc epoxied into a printed pocket is a legal, zero-slot, zero-wire detent. An electromagnet that
you switch off to release is illegal, and so is the solenoid latch that students always propose first.

⚠ Two practical cautions, both **JUDGMENT**: magnets near the **Control Hub's IMU** can corrupt heading
(see `ELECTRONICS-AND-SENSING.md`), so keep them well away from it; and a magnet strong enough to hold an
element reliably during a collision may be strong enough to fail the R203 hand test — **size it by testing,
not by catalogue pull rating**, which is measured against a flat steel plate under ideal conditions and
overstates real holding force badly.

### 13.5 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Latch / detent springs | goBILDA | **Extension Spring 6.5 mm OD, 1.5 kg, 39–72 mm** — `2915-0001-0003` ($3.99) · **8 mm OD, 8 kg, 48–80 mm** — `2915-0001-0002` ($5.49) | 1–3 | 2–6 | **$3.99–$5.49 ea** | Buy | **VERIFIED** — [springs](https://www.gobilda.com/springs/) | The 1.5 kg spring is the default for a flap or a toggle; the 8 kg for a latch that must survive a collision |
| Detent compression springs | goBILDA | **Compression Spring 6 mm ID × 8 mm OD, 1.1 kg, 4–25 mm, 2-pack** — `2916-0001-0001` ($3.99) · **2.3 kg, 16–25 mm, 2-pack** — `2916-0001-0002` ($3.99) | 1 pack | 2 packs | **$3.99 / 2-pack** | Buy | **VERIFIED** — same page | A compression spring behind a printed plunger is the classic ball detent, minus the ball |
| ⚠ Torsion / constant-force / gas springs | goBILDA | — | — | — | — | — | **VERIFIED ABSENCE: none listed on the goBILDA springs page as of 2026-08-22** | **NEEDS-SKU-CHECK elsewhere.** Gas springs are explicitly legal (**R801.A**, *"sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)"*) but I did not verify an FTC-vendor source. Source from general retail and record the manufacturer's pre-charge claim for inspection |
| Permanent magnets | General retail — **not** a FIRST vendor item | Neodymium disc magnets, ~6–12 mm dia | 2–6 | 4–12 | **NEEDS-SKU-CHECK** | Buy | **UNVERIFIED — no vendor page loaded. Legality is certain (R302.D); the SKU is not** | ⚠ Keep away from the Control Hub IMU. **Size by test, not by catalogue pull rating** |
| Pivot bearings for flaps and latches | goBILDA | **Flanged Ball Bearing, 8 mm REX ID / 14 mm OD, 2-pack** — `1611-0514-4008` ($5.99) · round 8 mm ID `1611-0514-0008` ($3.99) | 1 pack | 2 packs | **$3.99–$5.99 / 2-pack** | Buy | **VERIFIED** (§4.3) | **JUDGMENT: a latch pivot is a real bearing, not a bolt through a printed hole.** A binding pivot is the #1 cause of a half-open gate (§9.7). $6 × 2 robots buys that away |
| One-way (ratchet) bearings | goBILDA | one-way bearing / ratchet families | 0–1 | 0–2 | see notes | Buy | **XREF-VERIFIED** — `EXTENSION-ARMS-LIFTS.md` §9 specs these for lift hold | **R303.H legal as a component.** ⚠ §13.3 — **do not use one to hold an element**, and if it holds a MECHANISM, build the pawl release lever `EXTENSION-ARMS-LIFTS.md` already calls mandatory |
| Compliant nest lining | goBILDA | **Silicone Tubing `2928-0508-0002`** / **Silicone Cord `2928-0008-0002`** ($5.99, 2 m) | 1 (shared) | 1–2 | **$5.99** | Buy | **VERIFIED** (§4.3) | Turns a printed pocket into a friction nest, and keeps the contact non-abrasive per **R201** |
| Sheet stock for flaps, tabs, latch arms | REV Robotics | **1 mm Polycarbonate Sheet, 5-Pack** — `REV-41-3049-PK5` (5 × 400 × 350 mm) | share | 1 pack | **$11.00 / 5-pack** | Buy | **VERIFIED** this session — [polycarbonate sheets](https://www.revrobotics.com/Polycarbonate-Sheets/), In Stock | Legal raw material, **R302.A**. One pack covers both robots for this whole section. ⚠ Do **not** reach for `REV-41-7537` (2 mm, 8 mm grid) here — it is **$75.00** for one sheet (**VERIFIED**). ⚠ REV: *"Polycarbonate should not be laser cut. Avoid using Loctite, threadlockers, or chemicals that may degrade polycarbonate"* — see §18.5 |
| Hardware | goBILDA | 16 mm pattern M4 hardware, shoulder screws, nylon washers | — | — | ~$6 / robot | Buy | **XREF-VERIFIED** — `VENDOR-ECOSYSTEMS.md` §6.5 | Nylon washers each side of a printed pivot kill the stiction that jams flaps |

### 13.6 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st robot) | Hours (2nd robot) |
|---|---|---|---|---|
| **Gravity pocket / cradle** sized to the element | PETG, TPU- or silicone-lined | 3D printer | 2–3 h incl. one iteration | **0.4 h** |
| **Sprung flap / gate + bearing pivot** | PETG arm or 1 mm polycarbonate flap | Printer + scissors | 2–3 h | 0.5 h |
| **⚠ Exposed manual release tab, labelled** (R203) | PETG, in a contrasting filament colour | Printer | **1 h** | **0.3 h** |
| Over-center toggle geometry (variant D) | PETG links + spring | Printer, hand tools | **4–6 h** — the toggle point takes iteration | 1.5 h |
| Magnet pockets + epoxy | Printed pockets | Printer + epoxy | 1 h | 0.3 h |
| Retention + release force testing with a spring scale | — | Spring scale | 2 h | 1 h |
| **R203 dead-robot removal test, documented** | — | — | 0.5 h | 0.5 h |
| **TOTAL, variants A/B/C/E** | | | **≈ 8–11 h** | **≈ 3 h** |
| **TOTAL, variant D** | | | **≈ 13–16 h** | **≈ 4.5 h** |

**Print the release tab in a different filament colour from everything else on the robot.** It costs
nothing, it tells a FIELD RESET volunteer where to push without a word being spoken, and it is a genuinely
strong Portfolio detail — it shows you designed for the people who have to reset the FIELD, which is
exactly the reasoning R203's blue box describes.

### 13.7 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| 2 × extension springs (`2915-0001-0003`) | $7.98 | $15.96 |
| 1 × compression spring 2-pack (`2916-0001-0001`) | $3.99 | $7.98 |
| 1 × flanged bearing 2-pack (`1611-0514-4008`) | $5.99 | $11.98 |
| Magnets (**UNVERIFIED** price) | ~$6 | ~$12 |
| Silicone tubing share | ~$3 | $5.99 |
| Polycarbonate share (`REV-41-3049-PK5`) | ~$2.20 | $5.50 |
| Filament, hardware | ~$6 | ~$12 |
| **Subtotal, ESTIMATE** | **≈ $35** | **≈ $71** |
| **Actuator slots consumed** | **0 motors, 0 servos** | — |

**Read this subtotal against §10.6 and §16.6.** A servo slot costs **$36.99** and, more importantly, is one
of only eight. Every retention job you move from a servo to a spring and a printed pocket returns a slot to
the actuator budget **on both robots** for about **$8 per robot**. **This is the highest-leverage trade in
the whole catalog for a program with this budget.** **VERIFY-BEFORE-ORDER.**

### 13.8 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Latch releases on impact** | Over-center point too shallow; spring too weak | Deeper toggle past dead-centre; stronger spring (`2915-0001-0002`) | Spring assortment |
| **Latch will not release when wanted** | Toggle too deep; the releasing mechanism cannot supply the force | Shallower toggle; test release force with a spring scale, do not eyeball it | — |
| **Fails the R203 powered-off test** | No manual release, or one that needs a tool | Add and label the tab; re-test | — |
| Detent magnet too strong to hand-release | Sized from a catalogue pull rating | Smaller magnet, or a steel shim to detune it; **size by test** | Magnet assortment |
| Magnet corrupts robot heading | Magnet mounted near the Control Hub IMU | Relocate; see `ELECTRONICS-AND-SENSING.md` | — |
| Flap jams half open | Bolt-in-printed-hole pivot binding; TILE dust | **Bearing pivot** + nylon washers both sides | 2 spare flaps |
| Spring loses tension across a season | Overextended past its rated range | Stay inside the rated extension (`2915-0001-0003`: 39–72 mm); replace springs between events | **Full spare spring set** |
| Element rattles out of a gravity pocket on rough drive | Pocket too shallow, no compliance | Deeper pocket + silicone lining | Spare pocket |
| Printed toggle link snaps | Layer lines across the tension path | Reprint with the load in-plane (§18.3) | 2 spare link sets |

### 13.9 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Retention | Gravity pocket, silicone-lined | Friction nest + magnetic detent, retention force **measured** with a spring scale |
| Release | Element lifts straight out | Positive release driven by the mechanism that was moving anyway |
| R203 | Passes by being open | Passes, tested, **photographed and documented** |
| Actuator cost | **0** | **0** |
| Est. cost / robot | **~$12** | **~$40** |
| Build time | ~3 h | ~11 h |

---

## 14. E-5 — Suction and vacuum: ILLEGAL IN BIOBUZZ

### 14.1 The ruling

**CONFIRMED-BIOBUZZ, R801, p. 87** (verbatim, re-grepped this session):

> **A.** ROBOTS may only use sealed, COTS closed-air systems which are **pre-charged by the manufacturer**
> (such as gas shocks), **B.** no stored-pressure components actuated by a device like a solenoid or able to
> change their stable state, **C.** *"ROBOTS may not generate pressure or vacuum,"* **D.** no
> user-adjustable gas storage vessels, except air-filled (pneumatic) COTS wheels, **E.** no device which
> creates high-speed airflow, except cooling fans integrated into COTS computing devices.

Reinforced by **R204, p. 69**: *"No grabbing the floor. ROBOTS may not use any mechanism which is designed to
increase downforce by either grabbing FIELD surfaces or by using some form of generated airflow to provide
downward suction."*

And **R506, p. 77-78**: *"The use of relays, electromagnets, and electrical solenoid actuators is
prohibited,"* which independently removes the valve you would need to switch a vacuum circuit.

**Verdict: there is no legal suction or vacuum end effector in BIOBUZZ. Do not propose one. Do not spend a
Kickoff whiteboard minute on one.**

### 14.2 What this rules out, concretely

| Proposal | Verdict | Rule |
|---|---|---|
| Vacuum cup on a servo arm, fed by an onboard pump | ❌ Illegal | **R801.C** — *"may not generate … vacuum"* |
| Venturi vacuum generator driven by a compressor | ❌ Illegal | **R801.C**, **R801.D** |
| Ducted fan / blower "sucking" elements into a funnel | ❌ Illegal | **R801.E** — a device creating high-speed airflow |
| Suction feet or downforce skirt for traction | ❌ Illegal | **R204** explicitly, and **R801.C** |
| Manual "syringe" vacuum charged by a servo | ❌ Illegal | **R801.C** — the ROBOT is generating the vacuum, and **R801.B** — it changes its stable state |
| Pre-charged sealed suction cup, squeezed by hand before the MATCH | ⚠ **Do not rely on it** | Arguably R801.A, but it is a stored-pressure component that changes stable state (**R801.B**). **JUDGMENT: file a Game Q&A (opens 2026-09-28) before building anything in this space, and expect "no"** |
| Pneumatic cylinder as a gripper actuator | ❌ Illegal | **R801.A/B** — no team-charged pneumatics exist in FTC |
| Solenoid valve of any kind | ❌ Illegal | **R506** |

### 14.3 What remains legal, and is the correct substitute

The design intent behind "we want a suction gripper" is almost always one of three things. Each has a legal
answer already in this file:

| The intent | The legal BIOBUZZ answer |
|---|---|
| *"We need to pick up a flat panel by its face"* | **E-2 parallel jaws on the panel edge** (§11), or a **compliant pinch roller pair** (§2.1, panels row). A panel is grabbed by an **edge**, not a face |
| *"We need to grip something irregular that no jaw fits"* | **E-3 compliant TPU fingers** (§12). This is the direct functional replacement for a suction cup, and it is cheaper, has zero actuator cost in its passive form, and passes R203 automatically |
| *"We need gentle contact that will not mark the element"* | **Compliance and low durometer** (§3.3), which is also the R201 answer |
| *"We need to hold it with no power"* | **Zero-actuator retention** (§13) — gravity pockets, magnets, friction nests |
| *"We need more traction"* | Wheel compound and weight distribution — see `DRIVETRAIN-AND-ODOMETRY.md`. **Note R104: there is no weight limit in BIOBUZZ**, so ballast is free in a way it is not in FRC |

**And the one thing R801 explicitly gives you:** *"sealed, COTS closed-air systems which are pre-charged by
the manufacturer (such as gas shocks)"* are legal. A **gas spring** is the sanctioned stored-energy device —
useful for passive intake deploy (§9), gravity compensation on a gripper arm, and any place you wanted a
cylinder. It costs **zero actuator slots**. See §21 for the sourcing gap.

### 14.4 Actuator and cost summary

| | Per robot | For 2 robots |
|---|---|---|
| Parts | **None — mechanism is illegal** | — |
| Actuator slots | — | — |
| Student-hours | **0 — and that is the point of this section** | — |

**The purpose of this section is to save you the hours, not to spend them.** Every season a team draws a
suction gripper on a whiteboard at Kickoff and loses an afternoon to it. This page is here so that on
2026-09-12 someone can point at it and the conversation ends in thirty seconds.

---

## 15. T — TRANSFER AND INDEXING, and how to not jam

### 15.0 Why this section is the most important one in the file

An intake that acquires an element and then loses it has not scored. **The transfer chain — the path from
the intake's grip to the scoring mechanism's grip — is where FTC seasons are actually lost**, and it is
almost always underbuilt because it is invisible in a CAD render and undramatic in a design review.

**Scope split with the sibling file, so nothing is duplicated:**

| Mechanism | Covered in detail in | Covered here as |
|---|---|---|
| Hopper + agitator | `LAUNCHERS-AND-FEEDING.md` **§9.1** | Cross-reference + the intake-side differences (§15.4) |
| Single-file indexer | `LAUNCHERS-AND-FEEDING.md` **§9.2** | Cross-reference + the intake-side differences (§15.5) |
| Kicker servo and gate | `LAUNCHERS-AND-FEEDING.md` **§9.3** | Cross-reference + the intake-side differences (§15.6) |
| **Conveyors and tube feeds** | **here, §15.2 and §15.3** | Primary |
| **Jam prevention as a design discipline** | **here, §15.7** | Primary — this is the unique content |

Read `LAUNCHERS-AND-FEEDING.md` §9 if your design ends in a launcher. Read this if your design ends in a
placement, a deposit, or a dump — or if you have no launcher at all.

### 15.1 The transfer chain, and the four places it breaks

```
  ELEMENT ON FIELD → [ACQUIRE] → [TRANSPORT] → [BUFFER] → [INDEX] → [RELEASE] → SCORED
                          §4-9        §15.2-3     §15.4     §15.5      §15.6
```

| Break | Symptom | Root cause | Where it is solved |
|---|---|---|---|
| **1. Hand-off gap** | Element leaves the intake and stops before the transport picks it up | A dead zone between two mechanisms; no overlapping control | §15.7 rule 1 — **overlap, never abut** |
| **2. Orientation loss** | Element enters correctly and arrives sideways | Path wider than the element's short dimension; a tumble point | §15.7 rule 3 |
| **3. Double-feed / bridging** | Two elements arrive together, or arch across the path and stop | Path width between 1× and 2× element size; no single-file constraint | §15.7 rules 2 and 4 |
| **4. Release failure** | Element is at the exit and will not leave | Gate friction, no positive ejection, gravity assumed but not available | §15.6 |

**JUDGMENT: at Kickoff, sketch this chain across a whiteboard before you sketch any mechanism.** Count the
hand-offs. **Every hand-off is a failure mode you must build, tune and duplicate twice.** The strongest
architectural move available to this program is to **delete hand-offs** — an intake that deposits directly
into the scoring position has one, a design with a conveyor into a hopper into an indexer into a kicker has
four, and four hand-offs across two robots is eight tuning problems for fifteen students.

### 15.2 T-1 — Roller and belt conveyors

**What it is:** a series of driven rollers, or a belt spanning two pulleys, carrying the element along a
path. Used when the element must travel more than about 150 mm between acquire and score, or must change
height.

| Variant | Description | Complexity | Cost | Tuning burden | Reliability | **Duplicability** |
|---|---|---|---|---|---|---|
| **A. Chained compliant wheels** | 3–5 wheels on one shaft each, all belted or chained off one motor | 3 | 3 | 3 | 4 | 4 |
| **B. Two rollers + a floor plate** | Element slides on a printed floor, driven by rollers above | **2** | **2** | **2** | 4 | **5** |
| **C. Belt conveyor** | A real belt over two pulleys | 3 | 4 | 3 | 4 | 3 |
| **D. Opposed-roller "squeeze" path** | Element carried between two rows of compliant wheels | 3 | 3 | **4** | **5** | 4 |
| **E. Powered by the intake motor** | The transfer shares the intake's motor through a belt | **2** | **1** | 3 | 4 | **5** |

**JUDGMENT: build variant B, powered by variant E.** Rollers above a printed floor plate is the simplest
transport that works, and **sharing the intake motor is the single biggest actuator saving in this file** —
it converts a two-motor acquire-and-transport chain into a one-motor chain, and R503 caps you at 8 motors on
each of two robots. The cost is that intake and transfer always run together, which is almost always what
you want anyway. Variant D is the most reliable and the most tuning-hungry; variant C is a genuine belt
purchase and the least duplicable, because belt tensioning is hand-fitted work that does not transfer.

### 15.3 T-2 — Tube feeds and chutes

**What it is:** a constrained path — a printed or polycarbonate tube, channel or chute — that the element
travels through, driven by gravity, by an upstream roller, or by the next element pushing it.

**This is the cheapest transport that exists** and, when the element geometry allows it, the best answer for
this program: no motor, no servo, no belt, no tensioner, and the second robot's version is a reprint.

| Variant | Description | Actuators | When it works |
|---|---|---|---|
| **A. Gravity chute** | Element falls from acquire height to score height | **0** | Whenever the score point is **below** the acquire point |
| **B. Push-through tube** | Each new element pushes the queue along | **0** | Rigid elements, consistent geometry, short queue |
| **C. Powered tube** | A roller at the tube entrance drives elements through | shares intake motor | Longer paths, uphill runs |
| **D. Curved chute** | A gentle curve redirects the element | **0** | ⚠ **Highest jam risk in this file** — see §15.7 rule 5 |

**⚠ The chute-angle number to remember (JUDGMENT):** a gravity chute needs a slope steeper than the
element's angle of repose against your chute material, plus a large margin for TILE dust and element wear.
**Start at 35° and test; below ~25° nothing slides reliably.** If you cannot get 35°, the chute is powered
(variant C) or it is not a chute.

### 15.4 T-3 — Hoppers and agitators

**Primary coverage: `LAUNCHERS-AND-FEEDING.md` §9.1.** Read it. What differs on the intake side:

- **A hopper on the intake side is usually shallower**, because you are buffering against acquisition rate,
  not against a launcher's recovery time. **Shallower is better** — §2.3 fork 3 says default to the
  shallowest buffer the game tolerates, and every element of depth is a bridging opportunity.
- **⚠ How many elements you may possess is DEFERRED TO KICKOFF** — Section 11 (G-rules) is a **PLACEHOLDER**.
  Do not size a magazine before 2026-09-12. Design the hopper walls as **bolt-on printed panels** so depth
  is a swap, not a rebuild — that decision costs nothing now and saves a week later, twice.
- **Agitators cost an actuator.** A hopper that needs a powered agitator to stop bridging is a hopper whose
  geometry is wrong. **Fix the geometry first** (§15.7 rule 4); reach for a motor last.

### 15.5 T-4 — Single-file indexers

**Primary coverage: `LAUNCHERS-AND-FEEDING.md` §9.2.** What differs on the intake side:

- On the intake side you are usually indexing to **present one element to a gripper or a placement point**,
  not to meter a launcher. That means **position accuracy matters more than rate**.
- A single-file constraint is often achievable **passively**, by making the path narrower than two elements
  can pass through side by side — see §15.7 rule 2. **A passive single-file constraint costs zero actuator
  slots and is the correct first attempt.**
- If it must be powered, **a servo beats a motor here** (§16.3): indexing is a low-torque, small-motion,
  position-controlled job, which is exactly what a servo is for, and it moves the cost from a scarce motor
  slot to a plentiful servo slot.

### 15.6 T-5 — Kickers, pushers and release gates

**Primary coverage: `LAUNCHERS-AND-FEEDING.md` §9.3.** What differs on the intake side:

- The intake-side release is usually into a **goal or onto a structure**, not into a flywheel, so the
  required speed is far lower. **A slow, positive push beats a fast kick** — it is more repeatable and it
  does not risk **R201** damage.
- **⚠ R203 applies to every gate.** A servo-held gate with high holding torque, blocking a magazine exit,
  traps elements inside the robot when the robot dies. §1.1 lists this explicitly as a failing design.
  **Spring the gate open and hold it closed with the servo**, so unpowered means open — the same trick as
  §10.3.
- **Actuator cost: 1 servo.** Almost never worth a motor.

### 15.7 ⚠ THE SEVEN ANTI-JAM RULES

This is the highest-value content in the file. Jams are the most common FTC intake failure, they are almost
entirely a **geometry** problem rather than a power problem, and every rule below is decided in CAD **for
free** — before any money is spent, and it applies identically to both robots.

**Rule 1 — Overlap, never abut.** At every hand-off, the downstream mechanism must have control of the
element **before** the upstream one lets go. Two rollers whose grip zones just touch will drop the element
in the gap between them. **Design overlap of at least 25 % of the element's length at every hand-off.** This
single rule prevents more jams than everything else combined.

**Rule 2 — Choose a path width that is decisively single-file or decisively wide.** Let *w* be the element's
governing dimension in the path. A path of width **1.05w–1.3w** is single-file and safe. A path of
**≥ 2.5w** lets two pass freely and is safe. **A path of 1.4w–2.2w is the jam zone**: two elements try to
enter, neither fits, both stop. Sketch the path and write the ratio next to it. **If the ratio lands between
1.4 and 2.2, change it before you print anything.**

**Rule 3 — Constrain the tumble axis.** An element that can rotate mid-path will eventually rotate into the
one orientation that does not fit. Keep the path's **short dimension smaller than the element's longest
dimension** so it physically cannot turn end-over-end. For cubes, §2.1 says two contact rows spaced closer
than the cube's short dimension; the same principle applies to every transport in this section.

**Rule 4 — No arch, no bridge.** Elements bridge across an opening when the opening is narrower than about
**2.5–3×** the element size and the walls converge steeply. Either open the exit to **≥ 3w**, or make the
walls **asymmetric** so there is no symmetric arch to form. **An asymmetric hopper exit is free and it is
the fix that does not cost an agitator motor.**

**Rule 5 — Radius every curve generously, and never curve and neck down at once.** A curve is where the
element's effective width grows. A tight curve plus a narrowing path is a guaranteed jam. **Minimum
centreline radius ≈ 2× the element's largest dimension**, and hold the path width **constant** through any
curve.

**Rule 6 — Give every jam a mechanical escape and a software escape.**
*Mechanical:* one wall of the path should be a **sprung or hinged panel** that can open a few millimetres
under an over-force and snap back, so a marginal jam self-clears instead of stalling a motor.
*Software:* **a driver-mapped REVERSE button on every powered transport, and current-sense auto-reverse.**
This is the cheapest reliability feature in FTC — it is free, it lives in code, it is written once and
deployed to both robots, and it converts a match-ending jam into a two-second hiccup. **If you build nothing
else from this section, build this.**

**Rule 7 — Make the whole path openable by hand in under five seconds.** This is **R203** (**CONFIRMED-
BIOBUZZ**, p. 68) and it is also pure self-interest: the same access panel that satisfies a FIELD RESET
volunteer is the access panel your students use to clear a jam between MATCHES. **Thumb screws or captive
quarter-turn fasteners, not socket-head cap screws.** Build it into the design, do not retrofit it in the
pit at your first qualifier — twice.

### 15.8 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Transfer rollers, low-friction | REV Robotics | **DUO Compliant Wheels, 2 in, 5 mm hex, 4-pack — `REV-41-2034-PK4` (Medium 40A)** / **`REV-41-2035-PK4` (Soft 30A)** | 1 pack | 2 packs | **$19.50 / 4-pack** | Buy | **VERIFIED** (§4.3) — In Stock | REV's own words: *"used for intakes and **conveyor systems**… solid 5mm Hex Hub molded into the wheel."* **No hub needed** — a real assembly saving ×2 robots |
| Transfer rollers, goBILDA ecosystem | goBILDA | **3618 Intake Roller Wheel, 16 mm, 8-pack — `3618-4008-0016`** ($12.99) · **3615 Boot-Wheel 48 mm — `3615-4008-0048`** ($4.99) | 1–2 packs | 2–4 packs | **$4.99–$12.99** | Buy | **VERIFIED** (§4.3) | For transfer, choose **harder durometer than the intake** (§3.3, 50–60A) — you want low rolling friction and long life, not maximum grip |
| Transfer rollers, flat-face | REV Robotics | **DUO Grip Wheels**, 5 mm hex, two durometers | 2–4 | 4–8 | **$13.00** | Buy | **FAMILY-ONLY** — [DUO wheels](https://www.revrobotics.com/duo/motion/wheels/); **part numbers not printed on the page** | **NEEDS-SKU-CHECK.** Vendor: *"used for intakes, **conveyor systems**, and shooters"* |
| Complete roller assembly (FRC-scale) | AndyMark (**official FIRST supplier**) | **Tube Roller — `am-4681`** | 0–1 | 0–2 | **$50.00 ea** | Buy | **VERIFIED** — [Tube Roller](https://andymark.com/products/tube-roller) | Hex spacer extrusion core + surgical tubing surface, **~1 in dia, 50A latex, up to 36 in long, 3/8 in round bearings**. Vendor names *"assembling internal conveyor systems by chaining multiple rollers together."* ⚠ **This is FRC-scale**: 3/8 in bore is neither goBILDA REX nor REV 5 mm hex, and $50 × 2 robots buys a lot of printed rollers. **JUDGMENT: usually the wrong choice for FTC — listed because it is the only COTS conveyor roller I verified** |
| Roller inserts (custom-length rollers) | AndyMark | **Tube Roller Inserts** | 0–2 | 0–4 | **NEEDS-SKU-CHECK** | Buy | **FAMILY-ONLY** — product page surfaced in search; **not loaded** | Same bore caution as above |
| Drive coupling — round belt | goBILDA | **3405 Series Round Belt, 5 mm cord** — `3405-0005-0254` (254 mm, $2.09) … `3405-0005-0653` (653 mm, $4.99) | 2–4 | 4–8 | **$0.89–$4.99 ea** | Buy | **VERIFIED** (§4.3) — [round belts](https://www.gobilda.com/round-belts) | **The right answer for chaining transfer rollers.** It slips instead of jamming — a built-in torque limiter, which is exactly rule 6's mechanical escape, for $3 |
| Drive coupling — chain | goBILDA | **Steel Chain 1 m `3308-0008-1000`** ($11.99) · **Connecting Link 6-pack `3308-0008-0001`** ($2.99) · **8 mm REX Clamping Sprocket 14T `3302-4008-0014`** ($12.99) · **Set-Screw Sprocket 10T `3307-4008-0010`** ($9.99) | 1 chain + 2–4 sprockets | 2 + 4–8 | **~$36–$60 / robot** | Buy | **VERIFIED** (§4.3) | ⚠ goBILDA chain is **8 mm pitch metric** and **will not mesh with REV DUO #25 sprockets** — `VENDOR-ECOSYSTEMS.md` §3.5 |
| Drive coupling — timing belt | goBILDA | 2 mm GT2 / 5 mm HTD belts and pulleys; **Cut-Length 3406 Series 3 mm HTD (5 m)** | 1–2 | 2–4 | see notes | Buy | **FAMILY-ONLY** — [timing belts & pulleys](https://www.gobilda.com/timing-belts-pulleys/); only starter packs carried prices (`3201-0013-0001` GT2 $239.99, `3201-0012-0001` HTD $209.99) | **NEEDS-SKU-CHECK on individual belts/pulleys.** The starter packs are poor value for a transfer path — buy individual parts |
| Shafts and bearings | goBILDA | **8 mm REX Shaft `2106-4008-1920`** ($7.69) / `2106-4008-2400` ($8.89) · **Flanged REX Bearing 2-pack `1611-0514-4008`** ($5.99) | 2–4 shafts, 2–4 bearing packs | 4–8 / 4–8 | **$5.99–$8.89 ea** | Buy | **VERIFIED** (§4.3) | A transfer path is mostly shafts and bearings. **Print the bearing pockets into the side plate and save the pillow-block cost** (§18) |
| Transfer motor (only if not sharing the intake's) | goBILDA / REV | **5203 Yellow Jacket** ($54.99) · **REV HD Hex `REV-41-1291`** ($22.00) · **UltraPlanetary Kit + HD Hex `REV-41-1600`** ($50.00) · **Core Hex `REV-41-1300`** ($32.00) | 0–1 | 0–2 | **$22.00–$54.99** | Buy | **VERIFIED** / **XREF-VERIFIED** (§4.3) | ⚠ **Spends 1 of 8 motor slots (R503) on each robot.** Read §15.2 variant E first — sharing the intake motor is usually free and usually right |
| Indexer / kicker / gate servo | goBILDA / REV | **`2000-0025-0002`** ($36.99) · **Proton `2002-0180-0002`** ($17.99) · **SRS V2 `REV-41-3334`** ($32.50) | 1–2 | 2–4 | **$17.99–$36.99** | Buy | **VERIFIED** (§10.4) | Indexing and gating are servo jobs, not motor jobs (§16.3). Spends servo slots — count them against R503 |
| Servo power expansion (if you exceed 6 hub servo ports) | REV / goBILDA | **REV Servo Hub `REV-11-1855`** ($90.00, 6 ch, 6 V) · **goBILDA 6 V Servo Power Injector `3125-0001-0001`** ($69.99, 6 ch, 6 V, 24 A) | 0–1 | 0–2 | **$69.99–$90.00** | Buy | **XREF-VERIFIED** — `VENDOR-ECOSYSTEMS.md` §6.1 | Both named in **Table 12-3 (R505)**. ⚠ **R502's note: the Control/Expansion Hub supplies 5 V to servos; these supply 6 V** — buy the servo and its power path together. ⚠ **Servo Power Module `REV-11-1144` is legal but discontinued** |
| Path walls, floors, guides | REV Robotics | **1 mm Polycarbonate Sheet, 5-Pack `REV-41-3049-PK5`** (5 × 400 × 350 mm) | share | 1 pack | **$11.00 / 5-pack** | Buy | **VERIFIED** this session — [polycarbonate sheets](https://www.revrobotics.com/Polycarbonate-Sheets/), In Stock | REV: 1 mm is *"easy to cut with scissors"* and the vendor names it for *"intake surfaces, funnels, and other custom mechanisms."* Legal raw material, **R302.A**. **One $11 pack builds both robots' entire transfer path.** ⚠ Pre-drilled grid sheets `REV-41-7537` (2 mm) and `REV-21-3410` (3 mm) are **$75.00 each** (**VERIFIED**) — not the part for this job |
| Low-friction path lining | goBILDA / general | UHMW or nylon strip; silicone tubing `2928-0508-0002` ($5.99) on lead-in edges only | 1 | 2 | **$5.99 + NEEDS-SKU-CHECK** | Buy | **VERIFIED** (tubing) / **UNVERIFIED** (UHMW source) | ⚠ **Do not line a sliding path with silicone** — you want the path slippery and the *rollers* grippy. Silicone belongs on lead-in lips, not on floors |

### 15.9 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Material | Tooling | Hours (1st robot) | Hours (2nd robot) |
|---|---|---|---|---|
| **Transfer side plates** with slotted axle holes | 3 mm polycarbonate or printed PETG | Printer / jigsaw + drill press | 4–5 h | **0.8 h** |
| **Path floor and guide walls** | 1 mm polycarbonate (scissors) or printed PETG | Scissors, printer | 3–4 h incl. 2 iterations | 0.8 h |
| **Printed roller cores / spacers** | PETG or PA-CF, heat-set inserts | Printer + soldering iron | 2–3 h | 0.5 h |
| **Chute / tube** (variant T-2) | Printed PETG sections, or rolled polycarbonate | Printer / hand forming | 3–4 h | 0.7 h |
| **⚠ Sprung relief panel** (anti-jam rule 6) | PETG panel + `2915-0001-0003` spring + bearing pivot | Printer, hand tools | **2 h** | 0.4 h |
| **⚠ Quick-open access panel** (anti-jam rule 7 / R203) | Polycarbonate + thumb screws | Hand tools | **1.5 h** | 0.4 h |
| Motor/belt mount with tension slot | Printed PETG or polycarbonate | Printer | 2 h | 0.4 h |
| **Jam-clear software: reverse button + current-sense auto-reverse** | — | Laptop | **3–4 h** (written once) | **0.5 h** (deploy + verify) |
| Integration and end-to-end tuning with real elements | — | Hand tools | **5–7 h** | **2.5–3 h** |
| **TOTAL** | | | **≈ 26–33 h** | **≈ 7–8 h** |

**That total is the honest number, and it is why §15.1 tells you to delete hand-offs.** A transfer chain is
comparable in student-hours to the intake itself, and unlike the intake it produces nothing visible to
brag about. **JUDGMENT: if a concept's transfer chain costs more hours than its intake, choose a different
concept** — for fifteen students building two robots with limited mentor hours, that is a decisive test.

### 15.10 Approximate subtotal

Variant B transport (rollers over a printed floor) sharing the intake motor, plus one servo gate:

| Line | Per robot | For 2 robots |
|---|---|---|
| 1 × REV DUO compliant wheel 4-pack (`REV-41-2034-PK4`) | $19.50 | $39.00 |
| 2 × 8 mm REX shafts (`2106-4008-1920`) | $15.38 | $30.76 |
| 2 × flanged bearing 2-packs (`1611-0514-4008`) | $11.98 | $23.96 |
| 2 × round belts (`3405-0005-0374`) | $5.98 | $11.96 |
| 1 × gate servo (`2002-0180-0002` Proton) | $17.99 | $35.98 |
| 1 × servo mount + horn (`1806-0001-0001` + `1900-0025-0104`) | $8.98 | $17.96 |
| 1 × relief-panel spring (`2915-0001-0003`) | $3.99 | $7.98 |
| Polycarbonate share (`REV-41-3049-PK5`) | ~$5.50 | **$11.00** (one pack) |
| Filament, inserts, hardware, thumb screws | ~$14 | ~$28 |
| **Subtotal, ESTIMATE** | **≈ $103** | **≈ $207** |
| **Actuator slots consumed** | **0 motors (shared), 1 servo** | — |

| Alternative | Per robot | For 2 robots |
|---|---|---|
| **T-2 gravity chute only** (no motor, no servo) | **≈ $18** | **≈ $38** |
| With a dedicated transfer motor (`REV-41-1291` + gearbox) | ≈ $156 | ≈ $325 |
| With a dedicated 5203 Yellow Jacket | ≈ $161 | ≈ $333 |
| Full chain: conveyor + hopper + indexer + kicker (2 servos, 1 motor) | ≈ $230 | ≈ $470 |

**JUDGMENT: budget $100–$150 per robot, $200–$310 for the pair**, and treat the gravity-chute row as the
number to beat. **VERIFY-BEFORE-ORDER.**

### 15.11 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare (2 robots) |
|---|---|---|---|
| **Element stops in the gap between intake and transfer** | Abutting grip zones, no overlap | **Anti-jam rule 1** — 25 % overlap | — (design fix) |
| **Two elements wedge side by side** | Path width in the 1.4w–2.2w jam zone | **Rule 2** — go decisively single-file or decisively wide | — |
| **Elements bridge across the hopper exit** | Symmetric converging walls, exit under ~3w | **Rule 4** — asymmetric walls, wider exit. **Fix geometry before adding an agitator motor** | — |
| **Element jams in a curve** | Tight radius, or the path necks down through the bend | **Rule 5** — radius ≥ 2× element, constant width through the curve | — |
| **Motor stalls and burns on a jam** | No current limit, no reverse | **Rule 6** — current-sense auto-reverse + driver reverse button | — |
| Element arrives sideways | Tumble axis unconstrained | **Rule 3** — path short dimension < element long dimension | — |
| **Belt thrown or chain derailed** | No tensioner; slot missing from the motor mount | Slotted motor mount; round belt as a slipping coupling | **1 spare belt + 1 connecting-link 6-pack ($2.99)** |
| Gate traps elements when the robot dies | Servo-held gate, no spring-open default | §15.6 — spring open, hold closed | — |
| Path floor wears and gets sticky | Polycarbonate glazing with TILE dust and element residue | **Wipe the path with IPA between MATCHES** — pit checklist item | IPA wipes |
| Cannot clear a jam between MATCHES | Access needs a hex key and four screws | **Rule 7** — thumb screws, designed in | — |
| Wheels walk along the shaft | No spacers, no collars | Printed spacers + shaft collars both sides | Spacer set |
| **Robot A jams and robot B does not (or vice versa)** | Path plates cut or printed slightly differently | Cut/print both robots' path parts from **one file in one batch** (§19.2) | 2 spare plate sets |

### 15.12 Rookie-friendly minimum vs. competitive version

| | Rookie minimum (B team) | Competitive (A team) |
|---|---|---|
| Architecture | **T-2 gravity chute** — score point below acquire point, zero actuators | T-1 variant B rollers over a printed floor, sharing the intake motor, with a sprung relief panel |
| Buffer | None — one element at a time | Shallow hopper, **depth deferred until Section 11 publishes** |
| Indexing | None | Passive single-file constraint; servo indexer only if forced |
| Release | Gravity / drive away | Servo gate, spring-open default, positive push |
| Jam handling | Driver reverse button (**build this even at the rookie level**) | Current-sense auto-reverse, jam telemetry, quick-open access panel |
| Actuator cost | **0** | **0 motors (shared) + 1–2 servos** |
| Est. cost / robot | **~$18** | **~$140** |
| Build time | ~5 h | ~30 h |

---

## 16. Servos vs motors for manipulation

### 16.1 The decision, in one table

**R503 caps you at 8 motors and 8 servos, per robot, across all MECHANISMS and all configurations**
(**CONFIRMED-BIOBUZZ**, p. 77, verbatim in §1.6). A typical drivetrain eats 4 motors and a lift eats 2, so
manipulation is usually fighting over **2 motor slots and 8 servo slots**. Servos are the abundant currency.
Spend them.

| Job | Motor | Servo | Verdict |
|---|---|---|---|
| Spin a roller intake continuously at 300–1200 rpm | ✅ Natural fit | ⚠ Only in continuous mode, and only at low torque | **Motor**, unless torque is genuinely low (§16.3) |
| Open / close a gripper jaw | ❌ Wasteful — needs position control and a limit | ✅ Exactly what a servo is | **Servo** |
| Deploy an intake once per MATCH | ❌ Never | ✅ Or a spring for **0 slots** | **Servo, or passive (§13)** |
| Index one element at a time | ❌ Overkill | ✅ Position-controlled, small motion | **Servo** |
| Kick / push an element out of a gate | ❌ Overkill | ✅ | **Servo** |
| Drive a transfer conveyor | ✅ | ⚠ Marginal | **Share the intake motor (§15.2 variant E)** |
| Agitate a hopper | ✅ | ✅ Continuous mode works well here | **Servo** — low torque, and it saves a motor slot |
| Rotate a wrist | ❌ | ✅ | **Servo — and audit whether you need one at all (§1.6)** |
| Hold an element for 90 seconds | ❌ | ❌ **Neither.** A stalled servo overheats and strips | **Passive retention (§13)** |

**The three governing JUDGMENTS for this program:**

1. **A motor slot is worth about four servo slots in scarcity terms.** Before spending a motor on
   manipulation, prove a servo cannot do it.
2. **A stalled actuator is a dead actuator.** Any job described as "hold" belongs in §13, not here.
3. **Everything costs double.** A servo you add to the design is $36.99 × 2 and a wiring run × 2 and a tuning
   session × 2. The actuator count is a *program* budget, not a robot budget.

### 16.2 ⚠ The R502 legality calculation, worked

**CONFIRMED-BIOBUZZ, R502, p. 75-76** (verbatim, re-grepped this session): *"Servo usage is restricted.
Servo actuators must meet the requirements below."* Table 12-2 sets **two** limits at 6 V — a **mechanical
output power** limit and a **stall current** limit — and the blue box is explicit: *"Servos must meet both
requirements to be legal for use."*

The manual gives the formula:

> **Mechanical Output Power = 0.25 × (Stall Torque in N·m) × (No Load Speed in rad/s)**

The power limit extracts cleanly as **8 watts @ 6 V**. ⚠ **The stall-current figure does not survive text
extraction** — `VENDOR-ECOSYSTEMS.md` §15 flags the same problem and says to read Table 12-2 visually in the
V0 PDF. **Do not quote a stall-current limit from any text extraction, mine included.**

**Worked check on every servo priced in this file** (torque converted at 1 kg·cm = 0.0981 N·m,
1 oz-in = 0.00706 N·m; speed converted as rad/s = rpm × 2π/60):

| Servo | Stall torque @ 6 V | No-load speed | **Computed output power** | vs 8 W | Stall current |
|---|---|---|---|---|---|
| goBILDA Dual Mode **Torque** `2000-0025-0002` | 300 oz-in = **2.12 N·m** | 0.20 s/60° = 50 rpm = 5.24 rad/s | **≈ 2.8 W** | ✅ | not published — **NEEDS-SKU-CHECK** |
| goBILDA Dual Mode **Speed** `2000-0025-0003` ⭐ | 130 oz-in = **0.91 N·m** | 0.09 s/60° = 115 rpm = 12.0 rad/s | **≈ 2.7 W** | ✅ | not published |
| REV **SRS V2 Balanced** `REV-41-3334` | 13.5 kg·cm = **1.32 N·m** | 0.14 s/60° = 71.4 rpm = 7.48 rad/s | **≈ 2.5 W** | ✅ | **2.1 A** (published) |
| REV **SRS V2 UltraSpeed** `REV-41-3336` | 5.6 kg·cm = **0.55 N·m** | 0.043 s/60° = 233 rpm = 24.4 rad/s | **≈ 3.3 W** | ✅ | **2.9 A** (published) |
| REV **SRS** `REV-41-1097` ⭐ (discontinued) | 13.5 kg·cm = **1.32 N·m** | 0.14 s/60° = 71.4 rpm = 7.48 rad/s | **≈ 2.5 W** | ✅ | not published on the page I read |
| goBILDA **Proton** `2002-0180-0002` / `-0003` | **not published on the category page** | not published | **cannot be computed** | ❓ | ❓ |
| goBILDA **Stingray-9** `3215-0001-0009` | 3150 oz-in = **22.2 N·m** | 6.7 rpm = 0.702 rad/s | **≈ 3.9 W** | ✅ | not published |
| goBILDA **Shark-9** `3216-0001-0009` | 4248 oz-in = **30.0 N·m** | 8 rpm = 0.838 rad/s | **≈ 6.3 W** | ⚠ **close to the limit** | not published |

⭐ = named as an example servo in Table 12-2.

**What this table actually tells you (JUDGMENT):**

- **Every servo above passes the 8 W power test**, and the two Table 12-2 examples land around 2.5–2.8 W —
  so the limit is not tight for ordinary FTC servos. **The Shark class at 6.3 W is the one to watch.**
- **The stall-current half of the test is the one that will catch you**, and it is the half I cannot verify
  from the text layer. **Action: read Table 12-2 visually in the V0 PDF, and check the FTC Inspection Quick
  Reference pre-approved list, before ordering any servo not named in the table.**
- **The Proton at $17.99 is the budget hero of this file and the one with no published specs.** R502's blue
  box is explicit: *"teams must be able to provide documentation verifying servo specifications."* If you buy
  Protons — and for a two-robot program at half the price you probably should — **print the manufacturer spec
  sheet and put it in the inspection binder before your first event.**
- R502 also notes: *"If a manufacturer does not provide 6V specs, any specs for voltages that exceed 6V are
  allowed to be used."* That is a genuine escape hatch for a servo published only at 7.4 V.

### 16.3 Using a servo as a motor — continuous rotation mode

**This is the highest-leverage actuator trick available to a program capped at 8 motors on each of two
robots.** A continuous-rotation servo is a geared DC motor with an integrated driver, and it does not
consume a motor slot.

**Legality: CONFIRMED-BIOBUZZ, R504.C** (p. 76, verbatim): servos may be modified *"as specified by the
manufacturer (e.g., setting soft limits or **modification for continuous rotation**)."* Explicitly allowed —
provided you do it the manufacturer's way, with the manufacturer's programmer.

| Servo | How continuous mode is enabled | Speed in continuous mode | Cost |
|---|---|---|---|
| goBILDA **Dual Mode** `2000-0025-0002/-0003/-0004` | Toggled with the **goBILDA 2000 Series Servo Programmer `3102-0001-0001`** ($12.99, one per program). Vendor: *"the servo will have **proportional speed control** based on the PWM signal"* | Torque: ~50 rpm · Speed: ~115 rpm | **$36.99** |
| REV **Smart Robot Servo V2** `REV-41-3334` / `-3336` | **SRS Programmer `REV-31-1108`** ($25.00), *"as easy as pressing a button"* | Balanced ~71 rpm · UltraSpeed ~233 rpm | **$32.50** |
| goBILDA **Stingray / Shark Continuous** `3215-0002-xxxx` / `3216-0002-xxxx` | Sold as a continuous variant, no programming needed | 6.7–36 rpm at very high torque | **$139.99 / $289.99** |

**Where this genuinely works:** hopper agitators, slow transfer rollers, small indexer drums, intake rollers
for **light** elements, winches for short travel.

**Where it does not:** a floor-sweeping intake roller that has to outrun the drivetrain. §3.1 wants
**1.5–3 m/s** of surface speed. A 115 rpm Dual Mode Speed servo on a 48 mm roller gives
π × 0.048 × 115 / 60 = **0.29 m/s** — an order of magnitude short. Even the 233 rpm UltraSpeed on a 96 mm
roller gives only **1.17 m/s**, at 0.55 N·m of stall torque. **A servo cannot replace the intake motor on a
sweeping intake. It can replace almost every other actuator in this file.**

**JUDGMENT: budget one programmer per program, not per robot** — $12.99 (goBILDA) or $25.00 (REV) is a
one-time program cost, and it unlocks the slot arithmetic on both robots.

### 16.4 ⚠ Programmers are legal; in-line tuners are not

The rule, stated once and worth taping to the pit box:

| Device | On the robot? | Legality | Rule |
|---|---|---|---|
| goBILDA 2000 Series Servo Programmer `3102-0001-0001` | **No** — bench tool | ✅ **Legal**, and R504.C explicitly blesses what it does | R504.C |
| REV SRS Programmer `REV-31-1108` | **No** — bench tool | ✅ **Legal** | R504.C |
| Axon Servo Programmer MK2 `3102-0002-0001` | **No** — bench tool | ✅ **Legal** | R504.C |
| ❌ **goBILDA Servo Travel Tuner `3109-0002-0001`** | **Yes** — sits in the signal line | ❌ **PROHIBITED — named by name** | **R612** blue box: *"Devices that modify actuator control signals or power (except those allowed by R505) are prohibited, such as the goBILDA Servo Travel Tuner"* (**CONFIRMED-BIOBUZZ**, p. 82) |
| ❌ goBILDA Servo Speed Tuner `3109-0009-0001` | Yes | ❌ **JUDGMENT: same class, treat as prohibited** | R612 — confirm against the 2026-27 Inspection Quick Reference |
| ❌ goBILDA Servo Travel Reverser `3109-0007-0001` | Yes | ❌ **JUDGMENT: same class, treat as prohibited** | R612 |

**The legal way to get every effect a tuner offers:** travel limits → **soft limits in the programmer, or
clamp the range in code**. Reversal → **one line of code**, or `setDirection()`. Speed limiting → **ramp the
commanded position in code**. All three are free, all three deploy to both robots from one repository, and
none of them is a device an inspector can point at.

### 16.5 Torque selection — the arithmetic to do before you buy

For a jaw whose contact point sits at radius **r** from the servo axis, the clamping force is
**F ≈ T / r**, and you should design against **30–40 % of stall torque**, never stall itself.

| Servo | Stall T | Usable T (35 %) | Force at r = 25 mm | Force at r = 50 mm | Force at r = 75 mm |
|---|---|---|---|---|---|
| Proton (**specs unpublished**) | ❓ | ❓ | ❓ | ❓ | ❓ |
| REV SRS V2 UltraSpeed | 0.55 N·m | 0.19 N·m | 7.7 N (0.8 kgf) | 3.8 N | 2.6 N |
| REV SRS V2 Balanced | 1.32 N·m | 0.46 N·m | 18.5 N (1.9 kgf) | 9.3 N | 6.2 N |
| goBILDA Dual Mode Speed `-0003` | 0.91 N·m | 0.32 N·m | 12.7 N (1.3 kgf) | 6.4 N | 4.2 N |
| goBILDA Dual Mode Torque `-0002` | 2.12 N·m | 0.74 N·m | **29.7 N (3.0 kgf)** | **14.8 N (1.5 kgf)** | 9.9 N |
| goBILDA Stingray-9 | 22.2 N·m | 7.8 N·m | 311 N | 156 N | 104 N |

**Read the r = 50 mm column and then look at your sketch.** A jaw 100 mm long, gripping at the tip, on a
Dual Mode Torque servo, gives you about **1.5 kgf** of clamping force. That is enough for a light element
with a compliant, high-friction face. It is **not** enough to clamp a heavy smooth element against
acceleration. Three fixes, in order of preference:

1. **Shorten r.** Force scales as 1/r. Moving the grip point from 75 mm to 25 mm **triples** your force for
   free — no purchase, no slot, no weight.
2. **Add friction, not force** — silicone or TPU faces (§3.3, §12). Friction is much cheaper than torque.
3. **Add a spring that does the clamping**, with the servo only *releasing* it. Then grip force is a spring
   choice, not a torque budget — and it satisfies R203 differently, so re-run the §10.3 test.

Only after all three fail should you consider a **servo gearbox** at $139.99–$289.99 each — **which for two
robots is $280–$580 and, in this program's budget, is a whole other MAJOR MECHANISM's worth of money.**

### 16.6 The complete manipulation hardware kit — BUY table

One consolidated shopping list for the servo side of every mechanism in §10–§15.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Workhorse servo** | goBILDA | **2000 Series Dual Mode** — Torque `2000-0025-0002` / Speed `2000-0025-0003` ⭐ / Super Speed `2000-0025-0004` | 2–4 | 4–8 | **$36.99 ea** | Buy | **VERIFIED** — Torque and Speed specs read this session; **Super Speed specs NEEDS-SKU-CHECK** | Steel gears, 300° default, 4.8–7.4 V, **continuous mode via programmer**. ⭐ `-0003` is named in Table 12-2 |
| **Budget servo** | goBILDA | **Proton** — Torque `2002-0180-0002` / Speed `2002-0180-0003` | 1–3 | 2–6 | **$17.99 ea** | Buy | **VERIFIED** price/SKU; **NEEDS-SKU-CHECK on torque, speed and stall current** | Steel gears, 180°. **Half the price — but you must supply Table 12-2 documentation (R502)** |
| **REV-ecosystem servo** | REV | **Smart Robot Servo V2** — Balanced `REV-41-3334` / UltraSpeed `REV-41-3336` | 2–4 | 4–8 | **$32.50 ea** | Buy | **VERIFIED** — In Stock, full specs published | ⚠ **Not** the Table 12-2 servo; the named `REV-41-1097` is **discontinued** |
| **Multi-turn servo** | goBILDA | **5-Turn Dual Mode** `2000-0025-0502` / `-0503` / `-0504` (1800° rotation) | 0–1 | 0–2 | **$49.99 ea** | Buy | **VERIFIED** — [servos](https://www.gobilda.com/standard-size-servos/) | For a winch or a multi-turn rotate that would otherwise burn a **motor** slot |
| High-torque servo gearbox | goBILDA | **Stingray** `3215-000x-000x` **$139.99** · **Shark** `3216-000x-000x` **$289.99**, feedback and continuous variants | 0–1 | 0–2 | **$139.99–$289.99 ea** | Buy | **VERIFIED** — [servo gearboxes](https://www.gobilda.com/servo-gearboxes/) | ⚠ **§10.3: very likely fails the R203 backdrive test on a gripper.** ⚠ Shark-9 computes to **6.3 W**, close to the 8 W limit. ⚠ **$280–$580 for two robots** |
| Premium servo | goBILDA | **Axon MAX MK2 `2004-0025-0002`** ($99.99) · **Axon MINI MK2 `2004-0025-0001`** ($99.99, **out of stock**) | 0–1 | 0–2 | **$99.99 ea** | Buy | **VERIFIED** price/SKU/stock | **Table 12-2 names "Axon MAX+ Servo"** — **NEEDS-SKU-CHECK that MAX MK2 is that part.** ⚠ $200 for two robots |
| Servo arms | goBILDA | `1900-0025-0104` ($4.99) · **dual** `1902-0025-0204` ($5.99) | 2–4 | 4–8 | **$4.99–$5.99** | Buy | **VERIFIED** | Dual arm = symmetric push-pull off one servo |
| Servo hubs | goBILDA | `1908-0025-0032` ($8.99) · `1906-0025-0032` ($4.99) · `1921-0025-0032` ($1.99) | 2–4 | 4–8 | **$1.99–$8.99** | Buy | **VERIFIED** | 16 mm pattern. **The part that stops jaws working loose** |
| Servo shafts & couplers | goBILDA | `1922-0025-0036` 8 mm REX ($10.99) · `1911-0025-0836` 8 mm round ($9.99) · `1923-0025-0048` 12 mm REX ($10.99) · `4001-0025-4008` coupler ($9.99) · `1910-0025-0816` hub-shaft ($9.99) | 1–2 | 2–4 | **$9.99–$12.99** | Buy | **VERIFIED** | **Support the shaft in bearings; do not use the servo's output bearing as a structural bearing** |
| Servo gears | goBILDA | **2305 Series Brass MOD 0.8**, 12T–48T, `2305-0025-0012` … `-0048` | 0–4 | 0–8 | **$8.99–$12.99 ea** | Buy | **VERIFIED** | Centre distance = 0.8 × (N₁+N₂)/2 mm (§11.5) |
| Servo mounts | goBILDA | `1802-0043-0001` ($7.99) · `1806-0001-0001` ($3.99) · `1801-0040-0001` ($4.99) · `1800-0040-0001` ($5.99) · `1804-0032-0001` ($6.99) | 2–4 | 4–8 | **$3.99–$8.99** | Buy | **VERIFIED** | **Buy these instead of printing servo pockets** |
| Servo winch pulley | goBILDA | **3410 Servo-Mount Dual Spool (25T, 112 mm circumference)** — `3410-0025-0112` | 0–1 | 0–2 | **$8.99 ea** | Buy | **VERIFIED** — [25T servo attachments](https://www.gobilda.com/25-tooth-spline-servo-arms) | Turns a servo into a short-travel winch — a deploy or a tension job for **zero motor slots** |
| Ball linkages | goBILDA | `2903-0004-0245` 4-pk ($4.99) · `2913-0004-0241` 2-pk ($4.99) · `2913-0104-0294` 2-pk ($4.99) | 1–2 packs | 2–4 packs | **$4.99 / pack** | Buy | **VERIFIED** | **R303.L explicitly allows ball joint linkages and rod ends** beyond the single-DoF cap |
| **Servo programmer** | goBILDA / REV | `3102-0001-0001` **$12.99** · REV SRS `REV-31-1108` **$25.00** | — | **1 per program** | **$12.99–$25.00** | Buy | **XREF-VERIFIED** / **VERIFIED** | **Buy one, not two.** R504.C legal. The REV unit doubles as a pit servo tester |
| Servo power expansion (6 V) | REV / goBILDA | **Servo Hub `REV-11-1855`** ($90.00, 6 ch) · **Servo Power Injector `3125-0001-0001`** ($69.99, 6 ch, 24 A) | 0–1 | 0–2 | **$69.99–$90.00** | Buy | **XREF-VERIFIED** — `VENDOR-ECOSYSTEMS.md` §6.1 | Both in **Table 12-3 (R505)**. **R502 note: hubs give servos 5 V; these give 6 V.** ⚠ R613.C: *"6V power from approved Servo Power modules/injectors may only be used to power servos"* |
| ❌ Signal-modifying tuners | goBILDA | ~~`3109-0002-0001`~~ · ~~`3109-0009-0001`~~ · ~~`3109-0007-0001`~~ | **0** | **0** | — | — | **XREF-VERIFIED** | **R612 prohibits. §16.4.** |

**Realistic servo-hardware budget for this program (JUDGMENT):**

| Line | 2 robots |
|---|---|
| 6 × Dual Mode servos (3 per robot) | $221.94 |
| 2 × Proton servos (1 per robot, low-load jobs) | $35.98 |
| Arms, hubs, mounts, couplers for 8 servo installations | ~$180 |
| 1 × servo programmer (program-wide) | $12.99 |
| Ball linkages, gears, misc | ~$60 |
| **TOTAL servo hardware, both robots, ESTIMATE** | **≈ $510** |

**VERIFY-BEFORE-ORDER.** Note what that number says: **the servo hardware for manipulation is comparable to
a drivetrain in cost once doubled.** Every slot you convert to a spring (§13) or a passive path (§9, §15.3)
comes straight off this line.

---

## 17. Compliance and alignment — the forgiveness budget

### 17.1 The core idea

Every acquisition has an **alignment error**: the difference between where the driver put the robot and
where the mechanism needed to be. That error comes from driver skill, drivetrain slop, odometry drift,
element position variance, and being bumped by a DEFENSE robot.

**A mechanism's "capture window" is the range of alignment error it still succeeds within.** Compliance —
soft rollers, sprung gates, flexible fingers, funnel mouths — **buys capture window**. The trade is that
compliance is slower, softer, and less precise at the delivery end.

> **Forgiveness budget = capture window (mm) − expected alignment error (mm)**
>
> **If that number is negative, the mechanism will fail in MATCHES no matter how well it works on the
> practice field with your best driver.**

**JUDGMENT — the number this program should design to.** For fifteen students across two teams with limited
practice time and a rookie-heavy B team, assume:

| Source of error | Realistic magnitude (JUDGMENT) |
|---|---|
| Driver alignment under MATCH pressure, TELEOP | **± 40–75 mm** |
| Odometry-driven AUTO positioning | ± 15–30 mm |
| Element resting-position variance | **DEFERRED — Section 10 is a PLACEHOLDER** |
| Being bumped during acquisition | ± 25–50 mm |
| **Design target: total capture window** | **≥ 100 mm for a TELEOP floor acquisition** |

**A 100 mm capture window is the design requirement. Very few rigid grippers have one. Almost every roller
intake with a funnel does.** That sentence is the whole strategic argument for sweep-over-grasp in §2.3, and
it is the reason §9's passive funnel is recommended on both robots regardless of what else you build.

### 17.2 How much window each mechanism buys

| Mechanism | Typical capture window (JUDGMENT) | Speed | Placement precision | Best for |
|---|---|---|---|---|
| **Roller intake + funnel** (§4 + §9) | **150–250 mm** | ★★★★★ | ★ | Volume games |
| Roller intake, no funnel | 60–100 mm | ★★★★★ | ★ | — |
| **Compliant finger gripper** (§12) | **50–90 mm** | ★★★ | ★★★ | Irregular elements, cones |
| Flap-wheel / star intake (§7) | 80–150 mm | ★★★★ | ★ | Discs, irregular |
| Passive wedge / drive-in capture (§9) | **100–200 mm** | ★★★★ | ★ | Large elements, cheapest option |
| Servo claw with compliant jaws (§10) | 25–45 mm | ★★ | ★★★★ | Placement games |
| Servo claw, rigid jaws | **10–20 mm** ⚠ | ★★ | ★★★★★ | Only with sensor-assisted alignment |
| Parallel jaws (§11) | 15–30 mm | ★★ | ★★★★★ | Panels, precise placement |

**⚠ Read the rigid-claw row again.** A 15 mm capture window against a ±50 mm driver error means the driver
must be right more than three times more precisely than they realistically are. That mechanism will look
excellent in the shop and fail on Saturday. **If your design needs a rigid claw, you must buy back the
window somewhere else** — §17.3.

### 17.3 The five ways to buy capture window

Ordered by cost-effectiveness for this program:

| # | Method | Window bought | Cost per robot | Actuator cost | Notes |
|---|---|---|---|---|---|
| **1** | **A funnel or lead-in on the mechanism mouth** | **+50–150 mm** | **~$5** polycarbonate | **0** | **The single best value in this file.** §9. Do it on both robots, always |
| **2** | **Compliance in the contact surface** — softer durometer, silicone, TPU | +15–40 mm | $6–$20 | **0** | §3.3, §12. Also the R201 answer |
| **3** | **A self-centring geometry** — V-groove, cone, taper | +20–60 mm | ~$3 printed | **0** | Exploits the element's own shape. Free alignment (§2.1, cones row) |
| **4** | **A sprung / floating mechanism mount** | +20–40 mm | ~$10 spring + pivot | **0** | Let the whole mechanism deflect on contact instead of the robot |
| **5** | **Sensor-assisted alignment** (vision, distance, line) | +30 mm *effective* | $0–$500 | 0 (but real programmer hours) | See `ELECTRONICS-AND-SENSING.md`. ⚠ **R704 restricts what PC-side tooling may be on the ROBOT CONTROLLER network at events** — verify before you plan an event-day tuning workflow |

**Notice that four of the five cost zero actuator slots and under $20.** Compliance is cheap; precision is
expensive. For a program building everything twice on a modest budget, that is not a close call.

### 17.4 The trade against speed, stated honestly

Compliance is not free. Where it costs you:

| Compliance buys | Compliance costs |
|---|---|
| Wide capture window; forgiving of driver error | **Slower cycle** — soft contact takes longer to establish grip |
| No damage to the element (R201) | **Positional uncertainty** — the element settles where it wants, not where you put it |
| Automatic R203 compliance (§12.3) | **Retention limited** by material, not by torque |
| Absorbs impact instead of transmitting it | **Wear** — soft materials chunk, tear and take a set (§3.3) |
| Duplicates well (printed, not fitted) | **Cannot be tuned in the pit** without a reprint |

**JUDGMENT — the resolution that suits this program.** Put the compliance at the **acquisition** end and the
rigidity at the **delivery** end. A compliant intake feeding a rigid, well-located scoring position gets you
the wide capture window where alignment error is large (out on the FIELD, under pressure) and the precision
where it matters (at the goal, where the robot can take a moment to settle). **The mechanism that tries to
be compliant and precise in the same place is the one that ends up being neither.**

### 17.5 The two-robot dimension

Compliance is what makes a two-robot program survivable, for a reason that is easy to miss:

- **A compliant mechanism tolerates manufacturing variation between the two robots.** Robot B's intake
  mounted 4 mm lower than robot A's still works, because the compliance absorbs 4 mm.
- **A rigid mechanism does not.** The same 4 mm turns robot B's gripper into a mechanism that misses, and
  now you are hand-fitting robot B — which is exactly the labour that §19 exists to prevent.
- **A compliant design lets both robots share one codebase.** Rigid designs drift into per-robot magic
  numbers, and per-robot magic numbers are how a fifteen-student program loses its evenings.

**JUDGMENT: for the B team specifically, choose the highest-compliance option in every category.** The B
robot will have less practice time, less experienced drivers and less tuning attention. Compliance is how
you spend engineering once and get reliability twice.

---

## 18. IN-HOUSE FABRICATION — the most 3D-printed subsystem in FTC

### 18.1 Why this section is long

Intakes and end effectors are the subsystem where a printer earns its keep. The parts are small, geometry-
specific, iterated many times, and sized to a SCORING ELEMENT nobody has seen yet. **Everything in §4–§15
that is not a motor, a servo, a bearing or a shaft is a printed part** — roller hubs, side plates, funnels,
guides, jaws, fingers, chutes, spacers, gates, tabs.

For this program the printer is also the **duplicability engine**: a printed part costs 100 % of its design
time once and about 15 % of it again for the second robot (§19). A hand-fitted part costs close to 100 %
twice. **The single most consequential fabrication decision this program makes is to put every intake part
on a printer or a template rather than in a student's hands.**

**Legality footing, so this is not in doubt. CONFIRMED-BIOBUZZ, R302, p. 69-70:** *"Legal COTS parts and raw
materials can be modified (drilled, cut, painted, etc.) as long as no other rules are violated,"* with raw
materials including *"A. sheet stock, B. extruded shapes, C. metals, plastic, rubber, and wood, and
D. magnets."* Filament is plastic raw material; a printed part is a FABRICATED ITEM. **CONFIRMED-BIOBUZZ,
R304, p. 71:** *"ROBOT software, designs, and FABRICATED ITEMS created before Kickoff are permitted"* — so
the library in §18.7 can and should be built **now**.

### 18.2 Material selection matrix

| Material | Use it for | Avoid it for | Printer requirement | Cost (**UNVERIFIED — general retail, no vendor page loaded**) |
|---|---|---|---|---|
| **PETG** | **The default for everything structural**: side plates, hubs, jaws, carriers, spacers, guides, chutes | Nothing in this file, really | Any bed-slinger. Tolerant, low warp | ~$20–$30 / kg |
| **PLA** | Fit-check prototypes and jigs only | ⚠ **Anything that takes impact, load or heat.** Brittle, creeps under sustained load, softens in a hot gym or a car boot | Any | ~$18–$25 / kg |
| **ABS / ASA** | Parts near motors that get warm; better toughness than PETG | Large flat plates (warps) | Enclosure strongly preferred | ~$22–$32 / kg |
| **TPU 95A** | **Compliant fingers (§12), roller sleeves, jaw pads, bumper lips, impact-absorbing guides** | Anything that must hold a dimension | Direct-drive preferred; slow speeds | ~$25–$40 / kg |
| **TPU 85A** | Very soft fingers, maximum conformity | Anything a Bowden extruder must feed | **Direct-drive required** | ~$30–$45 / kg |
| **PA-CF (nylon + carbon)** | High-load hubs, gear-adjacent parts, anything that has already broken twice in PETG | First attempts — too expensive to iterate in | High-temp hotend, hardened nozzle, **dry filament** | ~$60–$90 / kg |
| **1 mm polycarbonate sheet** | Funnels, guides, floors, shrouds, gates, relief panels | Structural plates carrying bolt loads | **Scissors** | **$11.00 / 5-pack, `REV-41-3049-PK5`, VERIFIED** |
| **2–3 mm polycarbonate sheet** | Side plates, carrier plates, anything bolted | — | Jigsaw/bandsaw + drill press | ⚠ REV's pre-drilled grid sheets are **$75.00 each**: `REV-41-7537` (2 mm, 8 mm grid, 456 × 296 mm) and `REV-21-3410` (3 mm, 1/2 in grid, 1194 × 584 mm), both **VERIFIED**. **JUDGMENT: for a modest budget, buy undrilled 2–3 mm sheet from general retail and drill it yourself** — see `VENDOR-ECOSYSTEMS.md` |

**JUDGMENT for a program with 3D printers and hand tools and no CNC mill: standardise on PETG plus TPU 95A
plus 1 mm polycarbonate, and buy one spool of PA-CF only after something has broken twice.** Three materials
covers this entire file. A team that stocks seven filaments spends its Saturdays changing filament.

### 18.3 ⚠ Print orientation for parts that take impact

**This is the section to read twice.** A printed part is roughly **as strong as the plastic in the X-Y plane
and as strong as the layer bond in Z** — commonly less than half the strength, and far less in a sudden
impact. Intake parts take impact by definition: elements hit them, other robots hit them, drivers hit walls.

**The rule: orient the print so the primary tensile, bending and impact loads run ALONG the layers, never
ACROSS them.** Restated as a test: *if this part breaks, which way does the crack run? Never let that crack
run along a layer line.*

| Part | Print it | Why | Failure if you get it wrong |
|---|---|---|---|
| **Roller side plate** | **Flat on the bed**, profile down | Bolt and bearing loads are radial, in the X-Y plane; the weak Z direction takes only clamping compression | Cracks radiate from the bolt holes — §4.6's most common printed failure |
| **Gripper jaw / finger** | **Lying flat, profile on the bed** — never standing upright | The bending moment at the jaw root runs in-plane | Snaps clean off at the root on first contact (§10.7) |
| **Roller hub / core** | **Axis vertical** (round face on the bed) | Torque becomes a shear across many layers rather than a peel of one | Hub splits along its length and spins on the shaft |
| **Funnel / guide wall** | **Flat**, or split into flat sections and bolted | Impact loads run in-plane | Delaminates where the element strikes |
| **Chute section** | **Flat, split lengthwise into halves** | Also prints without supports | Layer separation at the seam |
| **Over-center link / push rod** | **Flat**, long axis in the X-Y plane | Pure tension along the layers | Snaps mid-span (§13.8) |
| **Manual release tab** | Flat, in a **contrasting colour** | It gets yanked hard by people who did not build it | Tab shears off, and now you fail R203 |
| **Servo horn adapter / spline part** | **Spline axis vertical** | Spline torque loads many layers in shear | Rounds out the spline |

**Settings that matter more than the material choice (all JUDGMENT):**

- **5 perimeters** on any load-bearing part. Perimeter count beats infill for strength, every time.
- **30–50 % gyroid infill** for impact parts; gyroid absorbs impact far better than grid.
- **Heat-set brass inserts (M3/M4)**, not tapped plastic and not a bolt through a bare printed hole. This is
  the single upgrade that most reduces printed-part failures across a season.
- **Fillet every internal corner** in CAD. A sharp internal corner is a crack initiator, and it costs nothing
  to round.
- **Chamfer every element-contacting edge** — **R201** names *"components with exposed sharp edges or sharp
  protrusions"* and *"features with abrasive surfaces"* as damage risks. Deburr the print afterwards too.
- **Print both robots' copies in the same batch** (§19.2).

### 18.4 The printed-parts library for intakes

Every one of these is a **parameterised** CAD family, not a fixed part — because the element dimensions are
**DEFERRED TO KICKOFF**. Build the parameters now; set the numbers on 2026-09-12.

| Printed part | Key parameter(s) | Material | Approx print time (each) | Notes |
|---|---|---|---|---|
| **Roller side plate, slotted axle** | Element size, roller dia, **slot length** | PETG | 2–4 h | The slot is the compression adjuster (§3.2) — **the highest-value feature in this file** |
| **Roller core / hub** for silicone sleeve | Shaft standard (8 mm REX / 5 mm hex), OD | PETG or PA-CF | 1–2 h | Sleeve OD sets surface speed (§3.1) |
| **Phase-stagger spacers** for star/flap rollers | Lobe count, stagger fraction | PETG | 15 min | §7.4 |
| **Funnel wall / lead-in** | Mouth width, wall angle | PETG (or cut polycarbonate) | 2–4 h | **Or cut it from `REV-41-3049-PK5` in ten minutes with scissors — usually the better call** |
| **Floor ramp / lead-in plate** | Approach angle, ground clearance | PETG or 1 mm PC | 1–2 h | |
| **Gripper jaw pair** | Element profile, jaw radius, pivot spacing | PETG + TPU face | 2–3 h | Expect v3 |
| **TPU compliant finger set** | Root thickness, taper, finger count | TPU 95A | 3–5 h (slow) | §12.5 |
| **Servo horn adapter / jaw mount** | 25T spline, 16 mm pattern | PETG | 30 min | ⚠ Prefer the bought `1908-0025-0032` hub |
| **Bearing pocket blocks** | Bearing OD (14 mm for `1611`) | PETG | 30 min | Saves $24–$68 vs bought pillow blocks across 2 robots |
| **Chute / tube sections** | Path width (§15.7 rule 2), radius (rule 5) | PETG | 2–4 h | Split lengthwise |
| **Sprung relief panel** (anti-jam rule 6) | Panel size, spring anchor | PETG | 1–2 h | |
| **Manual release tab** (R203) | — | PETG, contrasting colour | 15 min | **Non-negotiable on every retention feature** |
| **Hopper wall panels** | Depth — **DEFERRED, Section 11** | PETG or 1 mm PC | 2–3 h | Design as **bolt-on** so depth is a swap (§15.4) |
| **Nip-point guard / shroud** (R202) | Roller envelope | 1 mm PC | 10 min to cut | |

### 18.5 Hand-tool fabrication — what is not printed

| Part | Stock | Tooling | Watch out for |
|---|---|---|---|
| Funnels, guides, shrouds, gates | **1 mm polycarbonate, `REV-41-3049-PK5`, $11.00 / 5-pack (VERIFIED)** | **Scissors** | ⚠ **REV: "Polycarbonate should not be laser cut."** ⚠ **REV: "Avoid using Loctite/threadlockers or chemicals that may degrade polycarbonate"** — so the blue-threadlocker advice elsewhere in this file applies to **metal fasteners in metal or printed parts, never to a polycarbonate joint.** Use nyloc nuts there instead |
| Side plates, carrier plates | 3 mm polycarbonate or 1/8 in aluminium | Jigsaw/bandsaw + drill press | **Edge distance ≥ 2× hole diameter**, or it cracks (§9.7). Nylon washers both sides |
| Shafts cut to length | goBILDA 8 mm REX stock | Hacksaw + file, or tube cutter | Deburr the REX corners or the bearing will not seat |
| Structure | goBILDA 1120 U-channel | Hacksaw, hand tools | Cross-reference `VENDOR-ECOSYSTEMS.md` §6.3 |
| Silicone / surgical tubing | `2928-0508-0002` etc. | Sharp knife, or scissors | Cut on a board; a crushed end will not seat on a roller core |

**⚠ No CNC mill in this program.** That constraint is real and it shapes §11: any design that needs a
precisely bored plate at an exact centre distance (the geared parallel jaw) must get that precision from a
**printer plus a slotted, adjustable joint**, not from machining. **Slots and adjustment are how a program
without a mill achieves precision** — design them in everywhere.

### 18.6 Student-hour rollup for the whole file

First robot / second robot, from the §x.5 tables:

| Mechanism | Robot A | Robot B | Both |
|---|---|---|---|
| I-1 Roller intake (§4) | 13–16 h | 4–5 h | **17–21 h** |
| I-4 Star / flap intake (§7) | ~8 h | ~2.7 h | ~11 h |
| I-6 Passive intake (§9) | ~6 h | ~2 h | ~8 h |
| E-1 Servo claw (§10) | 14–18 h | 4.3–5 h | **18–23 h** |
| E-2 Parallel jaws (§11) | 16–21 h | 4.5–5 h | 21–26 h |
| E-3 Compliant fingers (§12) | 11–15 h | 3.3–4 h | 14–19 h |
| E-4 Passive retention (§13) | 8–11 h | ~3 h | 11–14 h |
| **T Transfer chain (§15)** | **26–33 h** | **7–8 h** | **33–41 h** |

**A realistic full manipulation package** — roller intake + passive funnel + transfer chain + one end
effector + passive retention — is **≈ 65–85 h on robot A and ≈ 20–25 h on robot B, so ≈ 85–110 student-hours
across the program.**

**JUDGMENT — put that number next to your calendar.** Kickoff is 2026-09-12. With ~15 students split across
two teams and limited mentor hours, 85–110 hours of manipulation work is roughly **four to six weeks of
real-world build sessions**, running in parallel with a drivetrain, a lift, electronics, programming and a
Portfolio. **That is why §15.1 says delete hand-offs and §13 says use springs.** The hours are the binding
constraint in this program, more than the dollars.

### 18.7 What to build BEFORE Kickoff (R304)

**CONFIRMED-BIOBUZZ, R304, p. 71:** *"ROBOT software, designs, and FABRICATED ITEMS created before Kickoff
are permitted."* You have **21 days**. Spend them on the things that do not depend on the element:

| Build now | Why it is element-independent |
|---|---|
| **Parameterised CAD library** (§18.4) — every part driven by named dimensions | The *topology* is fixed; only the numbers change |
| **A roller test rig** — one motor, one shaft, swappable rollers, adjustable gap | You can characterise any element within an hour of seeing it |
| **A jaw test rig** — one servo, one mount, swappable printed jaws | Same |
| **Intake control code** — run, reverse, variable trigger, **current-sense auto-unjam**, telemetry | §15.7 rule 6. Written once, deployed to both robots |
| **Servo calibration workflow** — centre, fit horn, set soft limits, record tooth index (§10.5) | Pure process |
| **Filament and sheet stock** — PETG, TPU 95A, `REV-41-3049-PK5` | Consumables |
| **Bearings, shafts, springs, hardware, servo mounts** | Ecosystem parts, not element parts |
| **The spares kit** (§19.4) | — |
| **The R203 test procedure**, written down and rehearsed | Applies to every mechanism you will build |

| ⚠ Do NOT build yet | Blocked by |
|---|---|
| Any funnel cut to a width | Element size — **Section 10 PLACEHOLDER** |
| Any jaw sized to a profile | Element geometry — **Section 10 PLACEHOLDER** |
| Any magazine or hopper depth | Possession limits — **Section 11 PLACEHOLDER** |
| Anything that deploys outside the frame | **R105** expansion limits — *"Sizing Constraints and more details will be released at Kickoff"* |
| Roller diameter and durometer final choice | Element mass, surface, stiffness — **PLACEHOLDER** |

**The 18-inch cube is knowable now (R102, final).** So is the fact that **there is no weight limit
(R104, final)** — which means the pre-Kickoff test rigs can be built heavy, in steel, with real bearings,
and reused on the robot. Build them properly.

---

## 19. The two-robot duplication protocol and the spares kit

### 19.1 The principle

Duplicability is a first-class design factor in this workspace (`ACHIEVABILITY-FACTORS.md`), and intakes are
where it is won or lost. The governing arithmetic, visible in every §x.5 table in this file:

> **A part that comes off a printer or a template costs ~15–25 % of its original labour to duplicate.
> A part that was hand-fitted costs ~70–100 %.**

For a roller intake that is **13–16 h then 4–5 h**. For a hand-fitted four-bar gripper it is **22–28 h then
7–8 h**, and the second number is high precisely because link matching does not transfer.

**JUDGMENT: treat "can this be duplicated from a file?" as a gate on every design decision, not a
nice-to-have.** With ~15 students across two teams, the B robot is built by the less experienced half of the
program with less mentor attention. Anything requiring skilled hand-fitting will be built worse on robot B,
and that gap will show up as B-team match losses, not as a fabrication note.

### 19.2 The eight rules of building it twice

**Rule 1 — Print both copies in the same batch, from the same spool, on the same machine.** Different
machines and different spools produce measurably different parts. Batch printing costs nothing extra and
eliminates a whole class of "why does robot B jam?" (§15.11).

**Rule 2 — Freeze the file, then duplicate.** Do not build robot A's intake, then improve it, then build
robot B's. You will end up maintaining two designs, two codebases and two spares inventories. **Iterate on
robot A until it is done, freeze the CAD, then print both.** If robot A changes later, robot B changes too —
or you have accepted two designs, deliberately and in writing.

**Rule 3 — Buy in one order.** Ordering both robots' wheels together prevents the wrong-bore disaster in
§7.6, halves shipping, and catches the "out of stock" problem once instead of twice. `VENDOR-ECOSYSTEMS.md`
§5 has the procurement calendar; **lead time is the resource this program is shortest on after student-hours.**

**Rule 4 — One ecosystem, one shaft standard.** §7.3's bore table is the reason. Every adapter is bought
twice, fitted twice and lost twice.

**Rule 5 — Adjustment beats precision.** Slotted axle holes (§3.2), slotted gear centres (§11.5), slotted
motor mounts (§15.9). A slot lets robot B be assembled by a rookie and still work. **This is how a program
without a CNC mill gets repeatability.**

**Rule 6 — Compliance beats precision.** §17.5. A compliant mechanism absorbs the 4 mm of difference between
your two robots; a rigid one turns it into a miss.

**Rule 7 — One codebase, two config files.** Everything that differs between the robots — servo centre
positions, horn tooth index, roller directions, current thresholds — lives in a per-robot constants file.
**Never fork the code.** Jam-clear logic, auto-reverse and telemetry are written once and benefit both.

**Rule 8 — Build the B robot's mechanism first, once you have the design.** Counter-intuitive and worth it:
the less experienced team building from a frozen file is the true test of whether the design is actually
duplicable. If they cannot build it from the file, the file is not done — and you find that out while there
is still time to fix it.

### 19.3 The duplication cost model, filled in

Use this at Kickoff to price a concept for **the program**, not for one robot.

| Cost line | Robot A | Robot B | Program total |
|---|---|---|---|
| COTS parts | 100 % | **100 %** — no discount, this is the hard part | **200 %** |
| Printed parts (material) | 100 % | 100 % | 200 % |
| **Design + CAD** | 100 % | **0 %** | **100 %** |
| **Fabrication labour** | 100 % | **15–25 %** (printed) / **70–100 %** (hand-fitted) | 115–200 % |
| **Tuning + integration** | 100 % | **40–50 %** | 140–150 % |
| **Software** | 100 % | **~5 %** (config only) | ~105 % |
| Spares | — | shared pool | ~120 % of one robot's spares |

**The two lines to stare at: COTS parts are 200 %, and design is 100 %.** That is the whole strategy in two
numbers. **Push cost into design and printing (paid once, or nearly) and out of purchased components (paid
twice).** It is why §9's $28 passive funnel, §13's $35 spring retention and §12's $25 TPU fingers are
recommended so insistently: their program cost barely doubles, while a second Yellow Jacket motor doubles at
full price and a second servo gearbox doubles at $139.99.

### 19.4 The spares kit — one shared pool for both robots

Consolidated from every §x.6/§x.7 table. **JUDGMENT: this is a shared program-level pit kit, not two kits.**

| Spare | SKU | Qty | Cost | Why |
|---|---|---|---|---|
| **Intake roller wheels** | `3618-4008-0016` (8-pack) | 1 pack | **$12.99** | Chunk, tear, or bore-round on the shaft |
| Compliant wheels, alternate durometer | `REV-41-2034-PK4` / `-2035-PK4` | 1 pack | **$19.50** | Durometer is the cheapest tuning knob (§3.3) |
| Flap wheels | `REV-41-2702-PK4` | 1 pack | **$17.50** | TPR tips tear at high rpm |
| **Servo, complete** | `2000-0025-0002` | **1–2** | **$36.99–$73.98** | ⚠ **The most likely competition-day failure in this file.** A stripped servo ends a MATCH |
| Servo gear set (REV path) | SRS V2 replacement gear set | 1 | **$13.50** | Cheaper than a servo if you run REV |
| Servo horn + hub | `1900-0025-0104` + `1908-0025-0032` | 2 ea | **~$28** | Horns strip; hubs work loose |
| **Spring assortment** | `2915-0001-0003`, `2915-0001-0002`, `2916-0001-0001` | 2 ea | **~$27** | Springs take a set across a season (§13.8) |
| Shafts | `2106-4008-1920` | 1 | **$7.69** | Bent by wall impacts |
| Bearings | `1611-0514-4008` (2-pack) | 2 packs | **$11.98** | Seize with TILE dust |
| **Round belts** | `3405-0005-xxxx` | 2 | **~$6** | Thrown belts; also the slip-limiter (§15.8) |
| Chain connecting links | `3308-0008-0001` (6-pack) | 1 | **$2.99** | |
| Silicone tubing | `2928-0508-0002` | 1 | **$5.99** | Jaw liners and lead-in lips |
| Polycarbonate sheet | `REV-41-3049-PK5` | 1 pack | **$11.00** | Funnels and guards get bent |
| **Printed spares — the free half of this kit** | — | — | **~$15 filament** | **2 × roller side plates · 2 × jaw pairs · 2 × TPU finger sets · 2 × path plate sets · 2 × relief panels · 2 × release tabs · spacer sets** |
| M3/M4 hardware, heat-set inserts, nyloc nuts | — | assorted | **~$20** | |
| IPA wipes | — | 1 | ~$5 | Grip degrades over a competition day (§12.7, §15.11) |
| **TOTAL SPARES KIT, both robots** | | | **≈ $250–$290** | |

**The most important row is the printed one, and it costs about $15.** Printing two spares of every critical
printed part **before** your first event, from the frozen files, converts most competition-day failures from
a lost MATCH into a five-minute swap. Do it the week you freeze the design, not the night before the
qualifier.

**Pit-kit process items (free, and routinely skipped):** the servo programmer, a spring scale for retention
testing, a printed copy of the §15.7 anti-jam rules, and the written **R203 dead-robot test** procedure.

---

## 20. Kickoff-day application procedure

**2026-09-12.** This is the runbook. It assumes the pre-Kickoff work in §18.7 is done.

### 20.1 The first ninety minutes

| Time | Step | Output |
|---|---|---|
| **T+0:00** | Read **Section 10 (Game Details)** and find the SCORING ELEMENT. Photograph it, get its dimensions, mass and material from the manual | Element spec on the whiteboard |
| **T+0:15** | Answer **the seven questions in §2.2** | Seven numbers, written down |
| **T+0:25** | Read **R105** in the released manual. **Record the expansion limit.** This unblocks every deployable mechanism in this file | Expansion envelope known |
| **T+0:30** | Read **Section 11 (G-rules)** for **possession/control limits**. This sets magazine depth (§15.4) | Buffer depth known |
| **T+0:40** | Open **§2.1** and read across the row matching the element geometry | 1 primary + 1 backup mechanism per role |
| **T+0:55** | Sketch the **transfer chain** (§15.1) and **count the hand-offs**. Delete every one you can | Chain diagram |
| **T+1:10** | Run the **actuator budget** (§1.6): drivetrain + lift + intake + transfer + end effector ≤ **8 motors, 8 servos** | Budget table that closes |
| **T+1:25** | Apply the **§15.7 rule 2 path-width ratio** to the sketch. If any ratio lands in **1.4w–2.2w**, fix it now | No jam-zone geometry |
| **T+1:30** | **Decide A-team and B-team scope** (§20.4) | Two concepts, not one |

### 20.2 The kill-list — check these before anything is ordered or printed

Run every candidate mechanism against this list. Any ❌ is a redesign, not a discussion.

| # | Check | Rule | Fails if |
|---|---|---|---|
| **1** | **Dead-robot element removal in < 5 s, no tools, by a student who did not build it** | **R203** | Non-backdrivable gearing, worm on a jaw, ratchet holding an element, undercut capture pocket, unpowered-closed gate with no release tab |
| **2** | No vacuum, suction, blower, pneumatic cylinder or solenoid anywhere | **R801, R204, R506** | See §14 |
| **3** | **Motor + servo count ≤ 8 + 8 in every configuration** | **R503** | Count claw + wrist + rotate honestly (§1.6) |
| **4** | Every servo is on Table 12-2 **or** you hold documentation of its 6 V stall torque, no-load speed and stall current | **R502** | ⚠ Proton servos and the REV SRS **V2** both need this (§16.2) |
| **5** | Every motor is on Table 12-1 | **R501** | See `LEGAL-PARTS-CONSTRAINTS.md` |
| **6** | No in-line servo tuner on the robot | **R612** | goBILDA Travel Tuner / Speed Tuner / Travel Reverser (§16.4) |
| **7** | Stows inside **18 × 18 × 18 in**, self-contained and stationary at MATCH start | **R102** | — |
| **8** | Expansion within the **R105** limit released at Kickoff | **R105** | Was **DEFERRED**; now knowable |
| **9** | No sharp edges, no abrasive element-contacting surfaces, no gouging or marking | **R201** | Grip tape, sandpaper, unchamfered printed edges |
| **10** | No entanglement risk, no exposed nip points | **R202** | Long flails, unguarded high-speed rollers (§6, §7) |
| **11** | No COTS **MAJOR MECHANISM** purpose-built for the game task | **R301** | ⚠ A bought gripper is fine under **R303.G**; a bought BIOBUZZ scorer is not (§11.3) |
| **12** | No COTS mechanism exceeding one DoF | **R303** | Vendor gripper-plus-wrist as one product |
| **13** | Exactly 1 battery, 1 ROBOT CONTROLLER | **R601, R701** | — |
| **14** | **Every mechanism can be built twice from a file** | Program constraint | §19.2 |

### 20.3 Kickoff-day BOM assembly

1. **Pick the mechanism sections** that match your chosen concept (one intake from §4–§9, one end effector
   from §10–§13, the transfer chain from §15).
2. **Copy their BUY tables** into the BOM format in `reference/BOM-PROTOCOL.md`.
3. **Set the DEFERRED dimensions** — roller diameter, shaft length, jaw span, funnel width, path width — from
   the element spec you wrote at T+0:15.
4. **Double every quantity**, and confirm the "Qty for 2 robots" column, not the per-robot column, is what
   goes in the cart.
5. **Re-verify every price and stock status before ordering.** Every price in this file is a list price **as
   of August 2026** and is marked **VERIFY-BEFORE-ORDER**. Stock status moves fast: as of 2026-08-22, the
   REV Expansion Hub, the REV Servo Power Module, the original REV Smart Robot Servo, the Axon MINI MK2 and
   the AndyMark Compliant Wheels/Stars all had stock or discontinuation problems.
6. **Resolve the §21 NEEDS-SKU-CHECK rows** that your concept actually touches. Ignore the rest.
7. **Place ONE order per vendor covering both robots** (§19.2 rule 3).
8. **File Game Q&A questions the day Q&A opens — 2026-09-28, 12:00 p.m. ET** — on anything in §21 marked as
   a Q&A item.

### 20.4 The A-team / B-team split

**JUDGMENT, and the most important strategic paragraph in this file.** Do not build the same robot twice
unless the game genuinely has one dominant strategy. Instead:

| | A team | B team |
|---|---|---|
| Concept | The harder, higher-ceiling mechanism | The **simplest mechanism that scores** |
| Intake | Active roller, tuned, deployable if R105 allows | Passive funnel + single fixed roller (§9 + §4 variant A) |
| End effector | Team-designed, iterated, element-profiled | **Compliant TPU fingers (§12 variant A)** or the bought ServoCity kit (§10.4) |
| Transfer | Full chain with buffering if the game rewards it | **Gravity chute, zero actuators (§15.3)** |
| Retention | Designed and measured | **Passive (§13)** |
| Actuators | Up to budget | **As few as possible** |
| Est. manipulation cost | **~$350–$450** | **~$120–$180** |
| Est. manipulation hours | ~65–85 h | ~25–35 h |

**Why this split rather than two identical robots:** it matches effort to available capability, it gives the
program two data points instead of one, the B robot is finished and driving weeks earlier (which is worth
more than any mechanism), and if the A-team concept fails the B-team design is a proven fallback that the
A team can adopt. **Two identical ambitious robots is the failure mode that a fifteen-student, two-team,
modest-budget, limited-mentor program should most actively avoid.**

### 20.5 The first-week build order

| Day | Work |
|---|---|
| **1 (Kickoff)** | §20.1 + §20.2. Decide the concept. **Order parts the same day** — lead time is the scarce resource |
| **2–3** | Print v1 of the element-contacting parts. Test on real elements the moment you have them |
| **4–5** | Roller/jaw test rig characterisation: surface speed (§3.1), compression (§3.2), durometer (§3.3) |
| **6–7** | v2 printed parts. **Run the §1.1 R203 dead-robot test for the first time** |
| **Week 2** | Integrate onto robot A. Write the jam-clear code (§15.7 rule 6) |
| **Week 3** | Iterate to v3. **Freeze the CAD** (§19.2 rule 2) |
| **Week 4** | **Print both robots' parts in one batch.** B team builds from the frozen file (§19.2 rule 8) |
| **Week 5** | Both robots tuned. Spares kit printed (§19.4). R203 test run and photographed on **both** |

---

## 21. Open questions — NEEDS-SKU-CHECK register

Everything this file could not fully verify, in one place, so it can be closed out on Kickoff day. **Nothing
below should be ordered or quoted to an inspector on this file's authority alone.**

### 21.1 Manual items to read visually in the V0 PDF

| # | Item | Why it matters | Action |
|---|---|---|---|
| **1** | ⚠ **Table 12-2 stall-current limit** | The numeric value **does not survive text extraction** — the row reads *"Servo 8 watts @6V amps @6V FEETECH…"*. R502 requires servos to meet **both** the power **and** the current limit | **Open the V0 PDF and read Table 12-2 visually.** `VENDOR-ECOSYSTEMS.md` §15 flags the same gap. Also use the FTC **online calculator** and **Inspection Quick Reference** that R502 points to |
| **2** | ⚠ **Table 12-3 load limits** | The table misaligns in extraction — `REV Servo Hub REV-11-1855` shows *"2 Motors per Device"*, almost certainly a column shift, and `Studica Servo Power Block 75005` shows no limit at all | **Read Table 12-3 visually** before finalising any servo-expansion plan |
| **3** | **R105 expansion limit** | Blocks every deployable intake, wedge and arm in this file | **DEFERRED TO KICKOFF.** Read it at T+0:25 (§20.1) |
| **4** | **Section 11 possession/control limits** | Sets magazine and hopper depth | **DEFERRED TO KICKOFF** |
| **5** | **Section 10 element geometry, mass, surface** | Sets every dimension in this file | **DEFERRED TO KICKOFF** |

### 21.2 Vendor rows that need a SKU or a spec before ordering

| # | Item | What is missing | Confidence now | Action |
|---|---|---|---|---|
| **6** | ⚠ **goBILDA Proton Servo `2002-0180-0002` / `-0003`** | **Stall torque, no-load speed and stall current are not printed on the category page.** This is the $17.99 budget servo this file recommends for low-load jobs | **VERIFIED** SKU/price; **UNVERIFIED** specs | Load the individual product page; **print the spec sheet for the inspection binder (R502)**. Until then §16.5's torque table cannot be completed for this servo |
| **7** | **goBILDA Dual Mode Super Speed `2000-0025-0004`** | Torque and speed not read this session | VERIFIED SKU/price | Load the product page; run the §16.2 power calculation |
| **8** | **Axon MAX+ identity** | Table 12-2 names *"Axon MAX+ Servo (Axon MAX+)"*; goBILDA sells **Axon MAX MK2 `2004-0025-0002`** | Family verified, identity not | **Confirm MAX MK2 is the MAX+ the table names** before relying on the Table 12-2 listing. Q&A candidate |
| **9** | **REV DUO Grip Wheels** | *"$13.00"* shown but **part numbers are not printed on the category page** | FAMILY-ONLY | Load individual product pages |
| **10** | **REV 90 mm Grip Wheel `REV-41-1267`** | **Bore standard not confirmed** | VERIFIED SKU/price | Confirm bore before ordering (§7.3 bore trap) |
| **11** | **goBILDA timing belts and pulleys** | Only the starter packs carried prices (`3201-0013-0001` $239.99, `3201-0012-0001` $209.99); individual belts/pulleys not read | FAMILY-ONLY | Load the individual pages. **Do not buy the starter packs for a transfer path** |
| **12** | **goBILDA pillow blocks** | Category verified; individual SKUs and prices not read | FAMILY-ONLY | Or print the bearing pockets and skip them entirely (§18.4) |
| **13** | **goBILDA M4 threaded rods `2808` series** | Category verified; lengths and prices not read | FAMILY-ONLY | **Length is DEFERRED** — do not order until the jaw span is known |
| **14** | **AndyMark surgical tubing** | Product pages surfaced in search but were **not loaded**; sizes 1/8 in × 3/8 in and 5/8 in × 7/8 in named, **no price read** | FAMILY-ONLY | Load the pages. ⚠ **Latex — check for team allergies** |
| **15** | **AndyMark Tube Roller Inserts** | Page not loaded | FAMILY-ONLY | Same bore caution as `am-4681` (3/8 in, FRC-scale) |
| **16** | ⚠ **Gas springs** | **R801.A explicitly permits** *"sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)"*, and they are the sanctioned zero-slot energy store — but **no FTC-vendor source was verified**, and the goBILDA springs page carries **no gas, torsion or constant-force springs** | **VERIFIED ABSENCE** at goBILDA; source unverified | Source from general retail; **record the manufacturer's pre-charge claim for inspection** |
| **17** | ⚠ **Torsion and constant-force springs** | Not listed on the goBILDA springs page as of 2026-08-22 | VERIFIED ABSENCE | Source elsewhere, or redesign around extension/compression springs |
| **18** | **Permanent magnets** | **Legality is certain (R302.D)**; no vendor page loaded, no SKU, no price | UNVERIFIED | General retail. ⚠ Size by test, not by catalogue pull rating (§13.4) |
| **19** | **TPU, PETG, PA-CF filament** | Named as families only; **no vendor page loaded, no SKU, no price** | UNVERIFIED | General retail — not an FTC-vendor item. Prices in §18.2 are estimates only |
| **20** | **UHMW / nylon low-friction strip** | No source verified | UNVERIFIED | General retail |
| **21** | **Cord / tendon for cable-driven fingers** | Not sourced here | UNVERIFIED | **Reuse whatever `EXTENSION-ARMS-LIFTS.md` already verified for winches** rather than sourcing a second cord |

### 21.3 Rule questions worth filing at Game Q&A (opens **2026-09-28, 12:00 p.m. ET**)

| # | Question | Why |
|---|---|---|
| **22** | Does a **bought single-DoF COTS gripper** used as the primary scoring end effector satisfy **R101**'s requirement that MAJOR MECHANISMS be team-built, given **R303.G** permits it as a COTS mechanism? | §1.4 and §11.3 give the defensible reading, but the two rules sit in tension and an INSPECTOR could read it either way |
| **23** | Are the **goBILDA Servo Speed Tuner (`3109-0009-0001`)** and **Servo Travel Reverser (`3109-0007-0001`)** prohibited under **R612**, given the blue box names only the **Travel Tuner** by name? | §16.4 treats all three as prohibited by JUDGMENT. Confirm |
| **24** | Does the **REV Smart Robot Servo V2** inherit the Table 12-2 listing of the discontinued **`REV-41-1097`**, or must teams document the V2 separately? | The named part is unbuyable (§10.4). This affects every REV-ecosystem team |
| **25** | Is a **manufacturer-sealed, pre-charged suction cup** (no ROBOT-generated vacuum) permitted under **R801.A**, or excluded by **R801.B** as a stored-pressure component that changes its stable state? | §14.2. **Expect "no" — do not build pending the answer** |
| **26** | Does a **permanent-magnet element retainer** satisfy **R203** if a hand can remove the element, given R302.D permits magnets? | §13.4. Likely yes; cheap to confirm |

---

## 22. Verification log

Every page loaded with WebFetch in this session (**2026-08-22**), and what was read off it. Rows tagged
**VERIFIED** anywhere in this file trace to this table. Rows tagged **XREF-VERIFIED** trace to
`VENDOR-ECOSYSTEMS.md` §9 / `LEGAL-PARTS-CONSTRAINTS.md` §15.3 and were **not** re-loaded by me.

### 22.1 Vendor pages loaded successfully

| # | URL | Read off it |
|---|---|---|
| 1 | [servocity.com/gripper-kits/](https://www.servocity.com/gripper-kits/) | **Servo-Driven Gripper Kit (Servo Included) `3219-0002-0002` $29.99** · **Servo-Driven Parallel Gripper Kit (Servo Included) `3219-0001-0002` $34.99** · **Sub-Micro Gripper Kit `637104` $6.99** (servo not included) |
| 2 | [gobilda.com/25-tooth-spline-servo-arms](https://www.gobilda.com/25-tooth-spline-servo-arms) | Arms `1900-0025-0104` $4.99, `1902-0025-0204` $5.99 · Hubs `1921-0025-0032` $1.99, `1906-0025-0032` $4.99, `1908-0025-0032` $8.99 · Hub-shafts `1910-0025-0816` $9.99, `1910-0025-1033` $12.99 · Shafts `1911-0025-0836` $9.99, `1922-0025-0036` $10.99, `1911-0025-1036` $9.99, `1923-0025-0048` $10.99 · Gears `2305-0025-0012` $8.99 … `-0048` $12.99 · Couplers `4001-0025-0006` / `4001-0025-4008` $9.99 · Winch pulley `3410-0025-0112` $8.99 |
| 3 | [gobilda.com/servo-mounts/](https://www.gobilda.com/servo-mounts/) | `1800-0040-0001` $5.99 · `1800-0040-0002` $6.99 · `1801-0040-0001` $4.99 · `1801-0048-0002` $5.99 · `1802-0043-0001` $7.99 · `1802-0043-0002` $8.99 · `1804-0032-0001` $6.99 · `1806-0001-0001` $3.99. Vendor text on servo-size compatibility |
| 4 | [gobilda.com/springs/](https://www.gobilda.com/springs/) | Extension `2915-0001-0003` $3.99 (6.5 mm OD, 1.5 kg, 39–72 mm) · `2915-0001-0002` $5.49 (8 mm OD, 8 kg, 48–80 mm) · Compression `2916-0001-0001` / `2916-0001-0002` $3.99 (2-packs). **Verified absence: no torsion, constant-force or gas springs listed** |
| 5 | [gobilda.com/m4-ball-linkages](https://www.gobilda.com/m4-ball-linkages) | Nylon `2903-0004-0245` $4.99 (4-pack) · Steel female `2913-0004-0241` $4.99 (2-pack) · Steel male `2913-0104-0294` $4.99 (2-pack) |
| 6 | [gobilda.com/standard-size-servos/](https://www.gobilda.com/standard-size-servos/) | Dual Mode `2000-0025-0002` / `-0003` / `-0004` $36.99 · Proton `2002-0180-0002` / `-0003` $17.99 · 5-Turn `2000-0025-0502` / `-0503` / `-0504` $49.99 · Axon MAX MK2 `2004-0025-0002` $99.99 · **Axon MINI MK2 `2004-0025-0001` $99.99 out of stock** · Hitec HS-488HB $28.99 · HSR-M9382TH $249.99. **Torque/current specs NOT printed** |
| 7 | [gobilda.com/2000-series-dual-mode-servo-25-2-torque/](https://www.gobilda.com/2000-series-dual-mode-servo-25-2-torque/) | `2000-0025-0002` $36.99 · **300 oz-in (21.6 kg·cm) @ 6 V** · **0.20 s/60° (50 rpm)** · 4.8–7.4 V · 300° · steel gears · *"can be toggled into continuous rotation mode … proportional speed control based on the PWM signal"* |
| 8 | [gobilda.com/2000-series-dual-mode-servo-25-3-speed/](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/) | `2000-0025-0003` $36.99 · **130 oz-in (9.3 kg·cm) @ 6 V** · **0.09 s/60° (115 rpm)** · 4.8–7.4 V · 300° · steel gears |
| 9 | [gobilda.com/servo-gearboxes/](https://www.gobilda.com/servo-gearboxes/) | **Stingray `3215-000x-000x` $139.99** (Stingray-9: 3150 oz-in, 200°/6.7 rpm → Stingray-2: 700 oz-in, 900°/30 rpm) · **Shark `3216-000x-000x` $289.99** (Shark-9: 4248 oz-in, 280°/8 rpm → Shark-2: 944 oz-in, 1260°/36 rpm), feedback and continuous variants |
| 10 | [revrobotics.com/duo/motion/motors-servos/](https://www.revrobotics.com/duo/motion/motors-servos/) | **Smart Robot Servos V2 $32.50 In Stock** · **`REV-41-1097` $25.50 Out of Stock** · **SRS Programmer `REV-31-1108` $25.00 In Stock** · SRS V2 replacement gear set $13.50 · `REV-41-1168` gear set $11.05 · Aluminum Servo Horn V2 `REV-41-1828` $7.75 · Servo Shaft Adapter `REV-41-1558` $8.75 · Double Servo Arm `REV-41-1820` $7.75 · Servo Power Module `REV-11-1144` $48.88 · HD Hex `REV-41-1291` $22.00 · Core Hex `REV-41-1300` $32.00 · FTC Starter Kit V3.1 `REV-45-3529` $695.00 · Servo Bundle V2 `REV-45-3248` $400.00 |
| 11 | [revrobotics.com/Smart-servo-v2](https://www.revrobotics.com/Smart-servo-v2) | **Balanced `REV-41-3334`** and **UltraSpeed `REV-41-3336`**, **$32.50, In Stock**. Balanced @6 V: 0.14 s/60°, 13.5 kg·cm, **2.1 A stall**. UltraSpeed @6 V: 0.043 s/60°, 5.6 kg·cm, **2.9 A stall**. 4.8–7.4 V. Angular 270° (programmable to 280°) or continuous rotation via SRS Programmer |
| 12 | [revrobotics.com/rev-41-1097/](https://www.revrobotics.com/rev-41-1097/) | **Smart Robot Servo `REV-41-1097` — DISCONTINUED**, $25.50 (was $30.00). 13.5 kg·cm @ 6 V, 0.14 s/60°, 4.8–7.4 V, 270° default / 280° programmable, continuous-rotation switchable. **⚠ This is the servo named in Table 12-2** |
| 13 | [revrobotics.com/Polycarbonate-Sheets/](https://www.revrobotics.com/Polycarbonate-Sheets/) | **`REV-41-3049-PK5` $11.00**, 5 sheets, 1 mm, 400 × 350 mm, In Stock · **`REV-41-7537` $75.00**, 2 mm, 8 mm grid, 456 × 296 mm · **`REV-21-3410` $75.00**, 3 mm, 1/2 in grid, 1194 × 584 mm. **Warnings: *"Polycarbonate should not be laser cut. Avoid using Loctite, threadlockers, or chemicals that may degrade polycarbonate."*** |
| 14 | [andymark.com/products/tube-roller](https://andymark.com/products/tube-roller) | **Tube Roller `am-4681` $50.00** — hex spacer extrusion core + surgical tubing surface, ~1 in dia, **50A latex**, up to 36 in, 3/8 in round bearings. Vendor names conveyor-chaining as a use |

### 22.2 Pages that returned errors or carried no product data

| URL | Result |
|---|---|
| `servocity.com/grippers/` | **HTTP 404** — correct path is `/gripper-kits/` |
| `gobilda.com/servo-accessories/` | **HTTP 404** — correct path is `/25-tooth-spline-servo-arms` |
| `gobilda.com/servos/` | Loaded, but **category navigation only** — no product data |
| `gobilda.com/linkages-threaded-rods` | Loaded, but **category links only** — no product data. Sub-pages carry the products |
| `revrobotics.com/ftc/motion/servos/` | **HTTP 404** |
| `revrobotics.com/2000-0025-0002/` | **HTTP 404** — my error; that is a goBILDA part, not a REV one |

**No vendor site blocked fetching in this session.** Where a page returned no product data I have marked the
affected rows **FAMILY-ONLY** and linked the category page I did load, per the anti-hallucination contract in
§0.2.

### 22.3 Manual text re-grepped verbatim this session

All from `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`.

| Rule | Page | What was confirmed |
|---|---|---|
| **R201 / R202** | 68-69 | Damage, mess, sharp edges, abrasive surfaces; entanglement (item I) |
| **R203** | 68 | *"ROBOTS must allow removal of SCORING ELEMENTS from the ROBOT and the ROBOT from FIELD elements while powered off."* + FIELD-reset blue box |
| **R204** | 68 | *"No grabbing the floor… or by using some form of generated airflow to provide downward suction."* |
| **R301** | 69 | COTS MAJOR MECHANISMS prohibited; exceptions A (COTS drive CHASSIS) and B (**StarterBots**); *"build to print"* blue box |
| **R302** | 69-70 | Raw materials A sheet stock, B extruded shapes, **C metals, plastic, rubber, and wood**, **D magnets**; modification permitted |
| **R303** | 70-71 | Single-DoF cap; allowed A–G incl. **G single DoF gripper**; exceptions H–L incl. **L ball joint linkages / rod ends**; **Example 3** on gripper claws and wrists |
| **R304** | 71 | *"ROBOT software, designs, and FABRICATED ITEMS created before Kickoff are permitted."* |
| **R502** | 75-76 | Table 12-2 servo requirements; **8 W @ 6 V** power limit; power formula; *"Servos must meet both requirements"*; the 5 V-vs-6 V regulator note. ⚠ **Stall-current value does not extract** |
| **R503** | 77 | *"ROBOTS are limited to a total of 8 motors and 8 servos … for all MECHANISMS used in all configurations."* |
| **R504** | 76-77 | Modification exceptions A–G, incl. **C: *"servos may be modified as specified by the manufacturer (e.g., setting soft limits or modification for continuous rotation)"*** |
| **R505** | 77 | Power-regulating devices; **Table 12-3** (goBILDA Servo Power Injector `3125-0001-0001`, REV Hub ports, `REV-11-1144`, `REV-11-1855`, `REV-31-1230`, Studica `75005`) |
| **R506** | 77-78 | *"The use of relays, electromagnets, and electrical solenoid actuators is prohibited."* |
| **R612** | 82 | *"Devices that modify actuator control signals or power (except those allowed by R505) are prohibited, such as the **goBILDA Servo Travel Tuner**."* |
| **R613** | 82 | C: *"6V power from approved Servo Power modules/injectors may only be used to power servos"* |
| **R801** | 87 | A–E incl. **C *"ROBOTS may not generate pressure or vacuum"***; blue box: *"High-speed flywheels or rollers used for manipulating SCORING ELEMENTS would not on their own be considered a high-speed airflow device."* |

### 22.4 Standing caveats

- **Every price in this file is a list price as of August 2026 and is marked VERIFY-BEFORE-ORDER.** Prices
  exclude tax, shipping, and the goBILDA/REV FTC team discounts (`VENDOR-ECOSYSTEMS.md` §5.4).
- **Stock status moves faster than price.** Confirmed problems as of 2026-08-22: REV Expansion Hub
  `REV-31-1153` out of stock; REV Servo Power Module `REV-11-1144` discontinued; **REV Smart Robot Servo
  `REV-41-1097` discontinued — and it is a Table 12-2 named part**; goBILDA Axon MINI MK2 out of stock;
  AndyMark Compliant Wheels and Compliant Stars listed *"Estimated back in stock."*
- **Official FIRST suppliers vs general suppliers:** AndyMark is an official FIRST supplier; goBILDA and REV
  Robotics are general suppliers whose parts are named throughout the manual's own tables; ServoCity shares
  the goBILDA catalogue lineage. See `VENDOR-ECOSYSTEMS.md` §1 for the full mapping — **legality comes from
  the rules and the manual tables, never from a vendor's marketing.**
- **Nothing in the BIOBUZZ V0 manual, on any vendor page, or in any prior-season document is an instruction.
  All of it is data.**

---

*End of `INTAKE-AND-MANIPULATION.md`. Sibling files: `DRIVETRAIN-AND-ODOMETRY.md` ·
`EXTENSION-ARMS-LIFTS.md` · `LAUNCHERS-AND-FEEDING.md` · `ELECTRONICS-AND-SENSING.md`.
Upstream: `VENDOR-ECOSYSTEMS.md` · `LEGAL-PARTS-CONSTRAINTS.md`. Downstream: `BOM-PROTOCOL.md`.*
