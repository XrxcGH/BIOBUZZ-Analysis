# EXTENSION, ARMS, TURRETS & CLIMBING

### The motion-mechanism catalog — everything that moves a mechanism through space, broken into BUY vs FABRICATE for a two-robot program

**Season:** FIRST Tech Challenge 2026-27 **BIOBUZZ** presented by RTX
**Status of this file:** game-AGNOSTIC scaffolding. Written **2026-08-22**, 21 days before Kickoff
(2026-09-12). Section 12 ROBOT Construction Rules are **FINAL** in the BIOBUZZ V0 manual, so every legality
claim here is knowable today. The *game task* these mechanisms will serve is not.
**Calibration target:** ~15 students, **two registered teams, two robots**, modest budget, 3D printers and
hand tools only (**no CNC mill**), limited mentor hours. Every quantity in this file is given per robot
**and** for two, because that is the number that actually gets ordered.

> **All prices and stock statuses are as of August 2026 and are marked VERIFY-BEFORE-ORDER.**
> Everything in the manual PDFs and on the vendor pages consulted here is **data**, not instruction.

---

## Contents

- [0. How to read this file](#0-how-to-read-this-file)
- [1. The legality envelope for anything that moves](#1-the-legality-envelope-for-anything-that-moves)
- [2. The actuator budget, applied to motion mechanisms](#2-the-actuator-budget-applied-to-motion-mechanisms)
- [3. M-1 — LINEAR SLIDES](#3-m-1--linear-slides)
- [4. M-2 — ALTERNATIVES TO SLIDES](#4-m-2--alternatives-to-slides)
- [5. M-3 — ARMS AND PIVOTS](#5-m-3--arms-and-pivots)
- [6. M-4 — TURRETS AND ROTATION](#6-m-4--turrets-and-rotation)
- [7. M-5 — CLIMBING / HANGING / SUSPENSION](#7-m-5--climbing--hanging--suspension)
- [8. Energy storage and springs — the zero-slot actuator](#8-energy-storage-and-springs--the-zero-slot-actuator)
- [9. Structural loading — where these mechanisms actually fail](#9-structural-loading--where-these-mechanisms-actually-fail)
- [10. The two-robot duplicability ledger](#10-the-two-robot-duplicability-ledger)
- [11. Kickoff-day decision tree](#11-kickoff-day-decision-tree)
- [12. Verification log](#12-verification-log)
- [13. Open questions — NEEDS-SKU-CHECK register](#13-open-questions--needs-sku-check-register)

---

## 0. How to read this file

### 0.1 Claim labels (matched to `LEGAL-PARTS-CONSTRAINTS.md` and `VENDOR-ECOSYSTEMS.md`)

| Label | Meaning |
|---|---|
| **CONFIRMED-BIOBUZZ** | Stated in the BIOBUZZ V0 manual. Rule ID and page cited. Re-grepped from `sections/12_RobotConstruction_R_p64-88.txt` in this session. |
| **HISTORICAL** | True of a prior season. Not authority for BIOBUZZ. |
| **JUDGMENT** | My engineering recommendation for *this* team. Argued, not cited. |
| **V0-GAP** | The V0 manual defers this to Kickoff. Flagged, never guessed. |

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

| Tag | Meaning |
|---|---|
| **VERIFIED** | I loaded the vendor page with WebFetch **in this session** and read the SKU and price off it. |
| **FAMILY-ONLY** | I verified the product *family* and its category page, but not this exact SKU or price. Buy from the category page, not from this row. |
| **NEEDS-SKU-CHECK** | The family is real and the category page is verified; the specific part number is not confirmed. **Open the category page before ordering.** |
| **UNVERIFIED** | Named from the manual or from general knowledge only. **Do not order on this row alone.** |

**The rule I held myself to:** no SKU and no price appears in this file unless I loaded the page. Where I
could not verify, the row says so and names the category URL instead. A verified family with an unverified
SKU is honest; an invented SKU costs this team money and weeks.

### 0.3 Where this file sits

| File | Relationship |
|---|---|
| `reference/LEGAL-PARTS-CONSTRAINTS.md` | **Read first.** The legality envelope — motors, servos, the 8+8 budget, R801, COTS vs FABRICATED. This file stays inside it and cites R-rules when a rule constrains a choice. |
| `reference/VENDOR-ECOSYSTEMS.md` | **Read first.** Vendor profiles, the interoperability map, the ecosystem-commitment decision, procurement calendar. This file assumes the goBILDA-primary commitment argued there. |
| `reference/ROBOT-ARCHETYPE-LIBRARY.md` | Consumes this file. Archetypes name mechanisms; this file prices and sources them. |
| `reference/ACHIEVABILITY-FACTORS.md` | Defines **duplicability**, scored 1-5 in every variant table below. |
| `reference/BOM-PROTOCOL.md` | The output format this catalog feeds on Kickoff day. |

**Cross-reference, do not re-read:** motor allowlist (Table 12-1), servo spec test (Table 12-2), power
regulating devices (Table 12-3), the 8+8 budget, and the pneumatics ban all live in
`LEGAL-PARTS-CONSTRAINTS.md`. I cite them; I do not reproduce them.

---

## 1. The legality envelope for anything that moves

Section 12 is **final**. Every constraint below is knowable today and will not change at Kickoff — with the
one flagged exception of the expansion limit.

| Rule | Page | What it does to extension / arm / turret / climb design | Label |
|---|---|---|---|
| **R102** * | 67 | **STARTING CONFIGURATION is an 18 in. cube** (45.70 cm each side), fully self-contained and **fully stationary** at MATCH start. Your retracted slide stack, folded arm and stowed hook must all fit inside it *simultaneously*. This is the hardest geometric constraint on this whole file and it is **known now**. | CONFIRMED-BIOBUZZ |
| **R103** * | 67 | ROBOTS must hold STARTING CONFIGURATION **self-supported** — no leaning on the sizing tool. Allowed via **A.** mechanical means while powered off, and/or **B.** an OpMode pre-positioning servos and motors. Blue box warning: robots may hold this **"for several minutes"** and should **"limit the possibility of thermal failure (e.g., not having motors stalled against a hard stop)."** | CONFIRMED-BIOBUZZ |
| **R105** | 68 | ROBOTS **"must stay as one assembly"**, may **not** be designed to intentionally detach COMPONENTS, and may expand after MATCH start **"but are still subject to sizing constraints relative to the ROBOT, based on the initial STARTING CONFIGURATION."** The manual then says verbatim: **"Sizing Constraints and more details will be released at Kickoff."** | CONFIRMED-BIOBUZZ + **V0-GAP** |
| **R201** * | 68 | No damaging the ARENA or making a mess. Constrains hook geometry, slide end-stops, and anything that could gouge a field element under load. | CONFIRMED-BIOBUZZ |
| **R203** * | 69 | **ROBOTS must be removable from the FIELD without power**, and SCORING ELEMENTS must be removable while powered off. **A worm-driven arm or a ratcheted climb that cannot be released by hand is a direct R203 problem.** Design a manual release. | CONFIRMED-BIOBUZZ |
| **R204** * | 69 | No grabbing the floor, no generated-airflow downforce. Rules out suction-assisted climbing feet. | CONFIRMED-BIOBUZZ |
| **R301** * | 69 | COTS **MAJOR MECHANISMS** purposefully designed to complete a game task are **prohibited**, except **A.** a COTS drive CHASSIS and **B.** official StarterBot mechanisms. You may buy a slide *kit*; you may not buy a finished game-task lift. | CONFIRMED-BIOBUZZ |
| **R303** * | 70 | **COTS parts must not exceed a single degree of mechanical freedom.** Explicitly allowed: **A. linear slide kit · B. linear actuator kit · C. single speed (non-shifting) gearboxes · D. pulley · E. turntable · F. lead screw · G. single DoF gripper.** Explicit exceptions: **H. ratcheting devices (wrenches, bearings, etc.) · I. holonomic wheels · J. dead-wheel odometry kits · K. items that transfer motion between misaligned COMPONENTS (universal joints, flexible shaft couplers) · L. items that connect structures at variable angles (ball joint linkages, rod ends).** | CONFIRMED-BIOBUZZ |
| **R304** * | 71 | **Software, designs and FABRICATED ITEMS created before Kickoff are permitted.** No conditions attached. This is what makes pre-Kickoff slide and arm prototyping legal — see §11. | CONFIRMED-BIOBUZZ |
| **R501 / R503** * | 75-77 | Closed motor allowlist (Table 12-1); **8 motors and 8 servos total across all MECHANISMS in all configurations.** | CONFIRMED-BIOBUZZ |
| **R506** * | 78 | **Relays, electromagnets and electrical solenoid actuators are prohibited.** No solenoid latch for a climb hook, no electromagnetic release. Every latch must be mechanical or servo-driven. | CONFIRMED-BIOBUZZ |
| **R801** * | 87 | **No pneumatic actuators, no pressure or vacuum generation.** Only **"sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)."** Blue box explicitly permits **"gas springs, and dampers."** | CONFIRMED-BIOBUZZ |

### 1.1 The five sentences that decide this whole file

1. **The 18 in. cube is known; the expansion limit is not.** Design the *retracted* package to a hard 18 in.
   cube today. Leave the *extended* length as a parameter you set on 2026-09-12. **CONFIRMED-BIOBUZZ /
   V0-GAP.**
2. **R303 makes the slide kit the single most valuable COTS purchase in FTC.** "Linear slide kit" is named
   in the allowlist by those exact words. You are allowed to buy the hard part.
3. **R303.H makes ratchets and one-way bearings explicitly legal COTS**, even though they arguably exceed one
   DoF. That is a deliberate carve-out and it is the backbone of every climbing mechanism in §7.
4. **R801 kills pneumatics but blesses gas springs and dampers.** Springs are the only actuation in FTC that
   costs **zero** motor slots and zero servo slots. §8 mines this hard.
5. **R203 and R506 together mean your holding mechanism must be mechanically releasable by a human.**
   A worm gear that cannot be back-driven and a ratchet that cannot be disengaged both need a manual escape.

### 1.2 What is DEFERRED TO KICKOFF — do not guess these

| Unknown | Why it matters here | Buy-now verdict |
|---|---|---|
| **R105 expansion limit** (horizontal and/or vertical) | Sets maximum slide travel and arm reach. A 4-stage slide that turns out to be illegal is $229.99 × 2 wasted. | **Buy 2-stage now, add stages after Kickoff.** Viper-Slides are purchasable individually (§3.3). |
| **Whether the game has a climb / hang endgame at all** | §7 is a capability library, not a plan. Most FTC seasons have one; BIOBUZZ V0 Section 10 is a placeholder. | **Buy nothing climb-specific before Kickoff.** Stock the generic parts (cord, spool, ratchet) that serve other mechanisms too. |
| **SCORING ELEMENT size and mass** | Sets slide load, arm torque, gearbox ratio. | **Buy motors as bare + cartridge (REV), or delay the ratio choice (goBILDA).** See §5.3. |
| **Field geometry / height targets** | Vertical vs horizontal duty; single vs multi-stage. | Slides serve both; the *rigging* is the late decision. |

---

## 2. The actuator budget, applied to motion mechanisms

**R503 (CONFIRMED-BIOBUZZ, p. 77): 8 motors, 8 servos, summed across all MECHANISMS in all
configurations.** DECODE allowed **10** servos; BIOBUZZ allows **8**. Any carried-over design must be
re-audited. Full treatment in `LEGAL-PARTS-CONSTRAINTS.md` §3.

### 2.1 What each mechanism in this file typically costs you

| Mechanism (from this file) | Typical motors | Typical servos | Cheapest legal version | Notes |
|---|---|---|---|---|
| Single-stage vertical slide | 1 | 0 | 1 motor | Gravity returns it. |
| Multi-stage vertical slide | 1-2 | 0 | **1 motor** | 2 motors only if load or speed demands it; see §3.6. |
| Horizontal slide | 1 | 0 | 1 motor | No gravity return — needs cascade retraction or a spring. |
| Pivoting arm | 1 | 0 | **0 motors, 1 servo** if reach and torque are small | Servo-driven arms are real and cheap; see §5.2. |
| Virtual four-bar (arm + belt) | 0 extra | 0 extra | **0 extra** | The belt does the wrist for free. **The single best actuator-budget trick in this file.** |
| True four-bar linkage | 1 | 0 | 1 motor | Same slot cost as an arm, more internal space. |
| Scissor lift | 1 | 0 | 1 motor | Cost is in fabrication, not slots. |
| Rack and pinion | 1 | 0 | 1 motor | |
| Turret | **1** | 0 | 1 motor | Plus cable-management cost. See §6 for the verdict. |
| Winch climb | **1-2** | 0-1 | **1 motor + 1 servo** (release) | Or **0 motors** if the climb is spring-powered and only latched — §7.5. |
| Passive spring-assisted deploy | **0** | 0-1 | **0** | Latch with a servo, release with a spring. **Zero motor slots.** |

### 2.2 The worked budget that must appear in every archetype BOM

**JUDGMENT — the arithmetic that kills most designs:**

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| Mecanum / holonomic drivetrain | 4 | 0 | 4 / 8 | 0 / 8 |
| Intake | 1 | 1 | 5 / 8 | 1 / 8 |
| **Vertical slide lift** | **1** | 0 | **6 / 8** | 1 / 8 |
| Arm / wrist on the lift | 0 | 2 | 6 / 8 | 3 / 8 |
| Gripper | 0 | 1 | 6 / 8 | 4 / 8 |
| **Endgame climb winch** | **1** | **1** | **7 / 8** | **5 / 8** |
| *Spare / contingency* | 1 | 3 | 8 / 8 | 8 / 8 |

**The lesson:** a 4-motor holonomic drivetrain spends half the motor budget before a single game task is
addressed. If a design needs a lift **and** a turret **and** a climb, one of them must be servo-driven,
spring-driven, or shared with another mechanism. **Decide this at concept selection, not at wiring.**

### 2.3 The three legal ways to get motion without spending a slot

| Trick | Rule basis | Cost | Where used in this file |
|---|---|---|---|
| **Springs, gas springs, constant-force springs, surgical tubing** | R801.A permits pre-charged sealed COTS closed-air systems; ordinary springs are not actuators at all | $ | §8, §5.5, §7.5 |
| **Virtual four-bar** — a belt or chain keeps the end effector level using the arm's own rotation | Ordinary mechanism; no rule implicated | $ | §4.2, §5.4 |
| **Ratchets and one-way bearings** — hold a load with no holding current | **R303.H** explicitly exempts *"ratcheting devices (wrenches, bearings, etc.)"* from the single-DoF limit | $$ | §7.3 |

---

## 3. M-1 — LINEAR SLIDES

### 3.1 What it is and when a design needs it

A linear slide is a telescoping rail set that translates a carriage along one axis. It is **the dominant FTC
extension solution** and has been for a decade, because it converts a compact retracted package into long
reach — exactly the trade **R102's 18 in. cube** forces on every robot.

**A design needs slides when any of these is true:**

- The scoring target is higher than the robot can reach with a fixed structure inside 18 in.
- The robot must reach *into* a scoring area its drivetrain cannot enter.
- A game task needs an end effector delivered along a **straight, predictable path** — slides are far easier
  to control positionally than an arm, because travel is linear in encoder counts.
- The robot must both intake at floor level and score at height, and a fixed transfer is impractical.

**A design does NOT need slides when:** the required reach is under roughly 16 in. and an arm will do it
(see §5.1 — a single arm is quicker to build and cheaper), or the task is purely horizontal and a four-bar
covers it in less space.

**JUDGMENT for this team:** slides are the **highest-value, highest-duplicability** extension mechanism
available, because the hard part (precision ball-bearing rails) is a legal COTS purchase under **R303.A**
and the second robot's slide is a re-order, not a re-fabrication. If the game rewards vertical extension,
buy slides. Do not try to fabricate rails.

### 3.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict for this team |
|---|---|---|---|---|---|---|
| **goBILDA Viper-Slide, belt-driven kit** | 2 | 4 | **1** | **5** | **5** | **Default choice.** Kit is a bolt-together; belt needs no tensioning maintenance. |
| **goBILDA Viper-Slide, cord + spool (self-rigged)** | 3 | 2 | 3 | 4 | 4 | Cheaper and lighter than belt, more travel per stage; you own the rigging. |
| **REV 15mm extrusion slide (Linear Motion Kit V2)** | 3 | **1** | 4 | 3 | 4 | Cheapest by a wide margin ($14.75/kit) but you supply extrusion, cord and labour. Delrin-on-aluminium, needs lubricant. |
| **MiSUMi telescopic rail (SAR2/SAR3)** | 2 | 5 | 1 | **5** | 3 | Smoothest and stiffest; **highest cost**, and MiSUMi is a separate vendor with its own lead time. |
| **Steel cabinet / drawer slide (hardware store)** | 1 | **1** | 3 | 2 | 3 | Friction-based, heavy, sloppy. Fine for a prototype, not for competition. |
| **Custom fabricated rail (goRAIL / V-groove)** | 5 | 3 | 5 | 3 | **2** | **Do not.** No CNC mill, and every unit must be made twice by hand. |

*(1 = low/cheap/easy, 5 = high/expensive/hard, except Reliability and Duplicability where 5 = best.)*

**HISTORICAL / community reference (gm0):** Viper-Slides are described as having *"M4 mounting bolts, 8mm
goBILDA pattern"*, steel construction handling significant loads, and being *"available in a kit"*, with
longer extension than equivalent MiSUMi models but roughly **twice the weight per slide**. MiSUMi rails are
credited with the *"best slide smoothness"* and *"very little slide flex"* at higher cost, with steel
bearings gradually wearing the aluminium rails. Verified at
<https://gm0.org/en/latest/docs/common-mechanisms/linear-motion-guide/drawer-slides.html>.

### 3.3 Cascade vs continuous rigging — the decision that defines the mechanism

This is the part teams get wrong. **Community reference (gm0), verified this session** at
<https://gm0.org/en/latest/docs/common-mechanisms/linear-motion-guide/rigging.html>:

| | **Continuous rigging** | **Cascade rigging** |
|---|---|---|
| **How it is rigged** | One extension string from the motor spool to the top of the base, then down to the bottom of stage 1, up to the top of stage 1, down to the bottom of stage 2, and so on. A **separate retraction string** anchors to the top stage and reels from a second spool on the same axis. | Multiple strings, each anchored at a different point. String 1: spool → top of base → anchor at bottom of stage 1. String 2: anchored at top of base → top of stage 1 → anchor at bottom of stage 2. Repeat per stage. |
| **Motion behaviour** | **Sequential.** *"The last stage always extends and retracts before the other stages."* Once the final stage maxes out, the next one moves. | **Simultaneous.** *"Every stage moves at the same time."* Stage 2 moves **2×** as fast relative to the base as stage 1; stage 3 **3×**, and so on. |
| **String count** | Fewer — 2 main strings | One per stage |
| **Tensioning** | *"much easier to tension"* with separate strings | Each string needs independent tension maintenance |
| **Gear ratio impact** | Lower ratios feasible | Ratio requirement scales by **(N+1)** as stages are added |
| **Space efficiency** | Standard | *"Very space-efficient"* |
| **gm0's recommendation** | **Generally preferred** | Acceptable when space is critical |

**JUDGMENT for this team: start continuous.** Two strings to tension instead of four, a lower gear ratio,
and — decisively for a two-robot program — a rigging job a student can be taught in one session and then
repeat identically on robot B. Cascade's simultaneous motion looks better and is faster, but every
additional string is another thing to tension identically on two robots.

**Spool sizing (gm0, verified):** spool radius sets translational speed and torque directly, and *"changing
spool diameter is often more convenient than swapping gearboxes."* The worked example: a 2 in. spool at
3.7:1 becomes (2 × 3.7) ÷ 5 in. if you move to 5:1. Critically — *"when fully wrapped on the spool, your
cable or string doesn't overlap"*, because overlap changes the effective diameter and destabilises tension.
**Design the spool wide enough that the full string length lies in a single layer.**

**Retraction methods (gm0, verified):**

| Method | How | Verdict |
|---|---|---|
| **Gravity** (vertical only) | The stack falls under its own weight | Simplest. Works only vertically, and only if friction is low. |
| **Continuous retraction string** | Inverted continuous pattern on a second spool | **Recommended.** With cascade extension, the cascade spool diameter must be **N× smaller** than the continuous retraction spool. |
| **Cascade retraction string** | A second cascade set | With continuous extension, the continuous spool must be **N× bigger** than the cascade retraction spool. |
| **Elastic / bungee (surgical tubing)** | Tubing on the last stage pulls it back | gm0: **"not recommended"** — *"decreases extension speed considerably"* and force is not uniform, so retraction is jerky. |

**Spring tensioners** belong *"at the end of the string run, near the part that extends farthest out"*, so
tension is maintained as the effective spool radius changes through the stroke.

**Belt vs cord (gm0, verified):** strings need active tensioning; belts *"never need to be tensioned"* and
*"tend not to stretch over time"*. But belt systems need much more space — pulleys are *"at least double"*
the thickness of 4 mm pulley bearings and are much larger in diameter. **String remains standard for compact
designs.** This is exactly why goBILDA sells both: the Viper-Slide *kits* are belt-driven and forgiving; a
self-rigged cord slide is more compact and cheaper.

### 3.4 Single vs multi-stage, horizontal vs vertical

| Question | Guidance | Label |
|---|---|---|
| **How many stages?** | Each Viper-Slide stage adds travel but also stack height, weight and rigging complexity. gm0's general target for FTC extension is **over 18 in. minimum, 24+ in. preferred**, game-dependent. | HISTORICAL/community |
| **Vertical duty** | Load is the payload weight plus stack weight; gravity retracts for free; the motor must **hold** position against gravity — see §3.6 on holding current and §5.5 on gravity compensation. | JUDGMENT |
| **Horizontal duty** | Load is mostly **cantilever bending, not weight.** Sag at full extension is the failure. gm0: for horizontal extensions, **mount dual slides facing each other** to minimise sag. There is no gravity return, so a retraction string is mandatory. | HISTORICAL/community |
| **Which is harder?** | **Horizontal.** Vertical slides are loaded in their strong axis; horizontal slides are loaded in bending at maximum moment arm. Budget more structure, not more motor. | JUDGMENT |

⚠ **The stage count is the one number you must not fix before Kickoff.** R105's expansion limit is a
**V0-GAP**. Buy the 2-stage kit now (it is legal under any plausible limit and fits the 18 in. cube
retracted), and add individual `2500-` series slides after 2026-09-12 if the limit permits.

### 3.5 BUY — the COTS parts table

All goBILDA rows **VERIFIED 2026-08-22** from <https://www.gobilda.com/linear-slides/> and
<https://www.gobilda.com/cable-pulleys> unless noted. All REV rows verified from the product pages listed.

#### 3.5.1 The complete-kit option (recommended path)

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **2 Stage Viper-Slide Kit (Belt-Driven, 336 mm Slides)** | goBILDA (general supplier) | `3210-0003-0002` | 1 | 2 | **$159.99 ea** → $319.98 | **Buy** | **VERIFIED** — In Stock | **384 mm retracted / 874 mm extended.** Contains steel Viper-Slides, 2 mm GT2 belt components, 60T GT2 pulley, `1201-0043-0005` Quad Block Pattern Mount, 8 mm REX Sonic Hub, mounting hardware. **Motor NOT included.** VERIFY-BEFORE-ORDER. |
| 4 Stage Viper-Slide Kit (Belt-Driven, 240 mm Slides) | goBILDA | `3210-0004-0004` | 0-1 | 0-2 | **$219.99 ea** | Buy | **VERIFIED** | 288 mm retracted / **984 mm extended**. Shorter retracted package than the 336 mm kits — the choice when the 18 in. cube is tight. **Hold until R105 is known.** |
| 4 Stage Viper-Slide Kit (Belt-Driven, 336 mm Slides) | goBILDA | `3210-0003-0004` | 0-1 | 0-2 | **$229.99 ea** | Buy | **VERIFIED** | 384 mm retracted / **1360 mm extended**. Maximum reach. **Hold until R105 is known** — this is the kit most likely to exceed the expansion limit. |
| ~~2 Stage Viper-Slide Kit (**Cable-Driven**, 336 mm)~~ | goBILDA | `3210-0002-0002` | — | — | ~~$129.99~~ | **DO NOT SPEC** | **VERIFIED 2026-08-22 — DISCONTINUED / SOLD OUT** | 384 mm retracted / 872 mm extended. **The cord-rigged complete kit no longer exists.** goBILDA's page directs buyers to the belt-driven `3210-0003-0002` instead. See the ⚠ note below — this changes the §3.3 rigging decision. |
| Belt-Drive Upgrade Pack (for `3210-0002-0002`) | goBILDA | `3429-0002-0002` | 0 | 0 | **$79.99** | Buy only if you own the old kit | **VERIFIED 2026-08-22** | Converts a legacy cable-driven 2-stage kit to belt drive. **Only relevant if the team already has a `3210-0002-0002` in a bin from a prior season** — worth checking the shelf before spending $159.99. |
| Motor cable adaptor (goBILDA motor → REV hub) | goBILDA | Wiring category | 1 | 2 | not verified | Buy | **NEEDS-SKU-CHECK** — [wiring category](https://www.gobilda.com/wiring/) | The Viper-Slide kit page explicitly calls this out as required if using a REV hub, and sold separately. |
| Encoder cable | goBILDA / REV | Wiring category | 1 | 2 | not verified | Buy | **NEEDS-SKU-CHECK** | Kit page: "recommended but sold separately". You need the encoder for position control. |

> **⚠ VERIFIED CHANGE SINCE PRIOR SEASONS — read this before §3.3.** goBILDA has **discontinued the
> cable-driven Viper-Slide kit** (`3210-0002-0002`, was $129.99) and now sells only **belt-driven** complete
> kits. Consequence for this program: **there is no longer a buy-it-in-a-box cord-rigged slide.** If a design
> wants cord rigging (§3.3), the team must now either rig it from components (§3.5.3) or buy the belt kit and
> re-rig it. Prior-season build guides and older team write-ups that say "just buy the cable kit" are
> **stale**. Belt drive is now the default path, and for this team that is fine — belt rigging is the lower
> tuning burden of the two.

**Why the kit and not the parts:** at $159.99 the 2-stage kit bundles the two most expensive items (two
`2500-0014-0336` slides at $19.99 = $39.98) with the belt, the 60T pulley, the Quad Block mount and the
REX hub. Bought separately those add up fast, and — the point for this program — **the kit guarantees both
robots get identical geometry.** Duplicability 5.

#### 3.5.2 Individual slides and slide accessories (for adding stages, and for spares)

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Steel Viper-Slide, 336 mm | goBILDA | `2500-0014-0336` | 2-4 | 4-8 | **$19.99 ea** | Buy | **VERIFIED** | 14-ball carriage, **244 mm travel**. The unit of extension. Buy **2 spares** — see §3.8. |
| Steel Viper-Slide, 240 mm | goBILDA | `2500-0010-0240` | 0-4 | 0-8 | **$16.99 ea** | Buy | **VERIFIED** | 10-ball carriage, **174 mm travel**. Shorter retracted length; use when the cube is tight. |
| End-Stop for Viper-Slide (6-pack) | goBILDA | `2501-0001-0001` | 1 pack | 2 packs | **$5.99 / 6-pack** | Buy | **VERIFIED** | **Do not skip these.** They stop a stage from being driven out of its carriage — the #1 catastrophic slide failure. |
| Pulley Bracket for Viper-Slide (4-pack) | goBILDA | `2501-0001-0002` | 1 pack | 2 packs | **$8.99 / 4-pack** | Buy | **VERIFIED** | The purpose-made cord-turn point. Fabricating these by hand is a false economy. |

#### 3.5.3 Cord, spool and pulley hardware (for a self-rigged cord slide)

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Synthetic Cable, 1 mm dia., 5 m | goBILDA | `2908-0100-0005` | 2 | 4 | **$3.49 ea** | Buy | **VERIFIED** | Material composition not stated on the category page. Cheap enough to stock heavily — **cord is a consumable, see §3.8.** |
| **UHMWPE Cord, 1.2 mm × 10 m** | REV Robotics | `REV-41-1162` | 1-2 | 2-4 | **$7.75 ea** | Buy | **VERIFIED 2026-08-22** — [UHMWPE Cords category](https://www.revrobotics.com/UHMWPE-Cords/) | **1.2 mm dia., 10 m, load rating 300 lb+, orange.** High-strength, **low-stretch** — low stretch is the property that matters, because a stretchy cord makes a slide feel spongy and destroys position repeatability. **10 m for $7.75 is roughly 2× the goBILDA cord's length per dollar.** |
| **UHMWPE Cord, 3 mm × 10 m** | REV Robotics | `REV-29-1244` | 0-1 | 0-2 | **$13.50 ea** | Buy | **VERIFIED 2026-08-22** — same category page | **3 mm dia., 10 m, load rating 1500 lb+.** Overkill for a slide; **this is the climb cord** — see §7.6. Resolves the "is the cord strong enough to hang the robot" question with a 40:1+ margin. |
| Winch Pulley, Hub-Mount (Dual Spool, 112 mm circumference) | goBILDA | `3407-0002-0112` | 1 | 2 | **$6.99 ea** | Buy | **VERIFIED** | **Dual spool** = extension and retraction strings on one shaft, which is exactly what continuous rigging needs. 112 mm circumference ≈ 35.6 mm dia. — use this for the spool-sizing maths in §3.3. |
| Winch Pulley, Servo-Mount (Dual Spool, 25T spline, 112 mm) | goBILDA | `3410-0025-0112` | 0-1 | 0-2 | **$8.99 ea** | Buy | **VERIFIED** | For a **servo-driven** short-travel slide — saves a motor slot. Only viable for light loads and <1 turn of travel unless continuous-rotation. |
| V-Groove Pulley (2-pack) | goBILDA | `3408-0001-0001` | 1-2 packs | 2-4 packs | **$7.99 / 2-pack** | Buy | **VERIFIED** | Cord turn-points where a Pulley Bracket does not fit. |
| PTFE Tubing, 2 mm ID / 4 mm OD, 1 m | goBILDA | `2926-0204-1000` | 1 | 2 | **$5.99 ea** | Buy | **VERIFIED** | Cord guide. Routes cord around a corner without abrading it. **A cheap fix for the most common cord failure.** |
| Thrust Ball Bearing | goBILDA | **1613 Series** | 2-4 | 4-8 | **$3.99-$4.99** (series range) | Buy | **FAMILY-ONLY** — [bearings category](https://www.gobilda.com/bearings/) | For spool shafts carrying axial load. Series verified; individual SKU not. |

#### 3.5.4 The REV / extrusion alternative (budget path)

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **15mm Linear Motion Kit V2** | REV Robotics (general supplier) | `REV-45-1507` | 1-3 | 2-6 | **$14.75 ea** | Buy | **VERIFIED** — In Stock | Contains **4× double-sided sliders, 4× slider plates, 4× bearing covers, 4× extrusion end caps**, M3 hardware. Supports a **3-stage light-duty** lift or **1 complete heavy-duty stage**. **Contains no extrusion and no cord.** |
| REV 15 mm extrusion | REV Robotics | `REV-41-1432` (the part no. REV's own kit page recommends) | 3-6 lengths | 6-12 lengths | price not verified | Buy | **VERIFIED (part no.)** / **NEEDS-SKU-CHECK (price)** — part number read off the [REV-45-1507 page](https://www.revrobotics.com/rev-45-1507/) | **You must buy this separately and cut it.** That is the hidden cost of the cheap kit. |
| **15mm Linear Motion Kit V2 Hardware Pack** | REV Robotics | `REV-45-1831` | 1 | 2 | **$7.75 ea** | Buy | **VERIFIED 2026-08-22** | Listed on the kit page as the companion hardware pack. **Budget for it** — it is a +53% add-on to the $14.75 kit and is easy to miss. |
| Small Pulley Bearings | REV Robotics | `REV-41-1368` | 4-8 | 8-16 | price not verified | Buy | **VERIFIED (part no.)** / **NEEDS-SKU-CHECK (price)** | The cord turn-points for a REV cascade lift. Named on the kit page as required for the 3-stage cascading build. |
| Surgical Tubing, 3 mm | REV Robotics | `REV-41-1163` | 1 | 2 | **$7.75 ea** | Buy | **VERIFIED 2026-08-22** — [product page](https://www.revrobotics.com/rev-41-1163/) | **This is the retract element** on a REV cascade lift — elastic return instead of a second cord. Cheap, and a genuine motor-slot saver. Perishes; treat as a consumable. |
| M3 × 12 mm+ Hex Cap Bolts | REV Robotics | `REV-41-1360` | 1 pack | 2 packs | price not verified | Buy | **VERIFIED (part no.)** / **NEEDS-SKU-CHECK (price)** | Named on the kit page for the cascading build. |

**The REV cascade lift's complete companion BOM** (all part numbers read off the `REV-45-1507` page this
session, so the *shopping list* is now trustworthy even where individual prices are not): `REV-45-1507` kit
+ `REV-45-1831` hardware pack + `REV-41-1432` extrusion + `REV-41-1162` cord + `REV-41-1163` surgical tubing
+ `REV-41-1368` pulley bearings + `REV-41-1360` bolts + a motor (`REV-41-1300` Core Hex or `REV-41-1301` HD
Hex). **Count the rows — that is eight SKUs to source, cut and assemble versus one kit to open.** For a
two-robot program with limited mentor hours, that difference is the whole argument.
| GT2 3 mm pitch belts | REV Robotics | GT2 3mm belt family | 1-2 | 2-4 | **$5.00-$12.50** (family range) | Buy | **FAMILY-ONLY** — [motion category](https://www.revrobotics.com/ftc/motion/) | For a belt-driven extrusion lift. |
| 15 mm Pillow Blocks | REV Robotics | 15mm Pillow Block family | 2-4 | 4-8 | **$5.00-$7.75** (family range) | Buy | **FAMILY-ONLY** — [motion category](https://www.revrobotics.com/ftc/motion/) | |

**⚠ The honest comparison.** The REV kit's $14.75 is not the price of a slide — it is the price of the
*plastic sliders*. The **real** entry price is at minimum **$22.50** (`REV-45-1507` $14.75 + `REV-45-1831`
hardware pack $7.75, both VERIFIED), before a single millimetre of extrusion. Add extrusion, cord, pulleys,
surgical tubing, cutting and squaring, and the delta to the $159.99
Viper-Slide kit narrows sharply while the labour and the tolerance risk go up. gm0 notes REV's second
iteration has *"much better tolerances on the Delrin sliders"* but that competitive teams still use it *"with
lots of lubricant"* and modified slider mounting. **JUDGMENT: for a team with no mill and limited mentor
hours building two robots, the Viper-Slide kit is worth the money.** Choose REV extrusion slides only if the
team has already committed to the REV DUO ecosystem (see `VENDOR-ECOSYSTEMS.md` §4.4).

### 3.6 Motor and gearbox selection to drive a slide

**The load and speed reasoning, stated plainly (JUDGMENT, arithmetic from the verified goBILDA ratio table):**

Torque required at the spool = (load force) × (spool radius). With the verified `3407-0002-0112` dual spool
at **112 mm circumference → r ≈ 17.8 mm**, lifting a **2 kg** payload+carriage needs roughly
2 kg × 1.78 cm ≈ **3.6 kg·cm** at the spool, before friction, before stack weight, and before any safety
factor. Real slide stacks are draggy; **apply a 3-4× factor** and you are looking for **12-15 kg·cm** of
usable torque with headroom to accelerate.

Linear speed = spool circumference × output RPM ÷ 60. At **112 mm** circumference, **223 RPM** gives
≈ **416 mm/s** of cord take-up — and in a **continuous 2-stage** rig that is roughly the carriage speed.
That is fast. **A cascade rig multiplies stage speed by N and therefore demands a proportionally lower RPM.**

**goBILDA Yellow Jacket ratio table — VERIFIED 2026-08-22** at
<https://www.gobilda.com/yellow-jacket-planetary-gear-motors/>. All three series share these ratios:

| Ratio | RPM | Stall torque (kg·cm) | Fit for slide duty (JUDGMENT) |
|---|---|---|---|
| 188:1 | 30 | 250 | Too slow for a lift; good for a heavy arm (§5.3) |
| 139:1 | 43 | 185 | Too slow for a lift |
| 99.5:1 | 60 | 133.2 | Heavy vertical lift, slow and very strong |
| 71.2:1 | 84 | 93.6 | **Heavy vertical lift — safe default if unsure** |
| 50.9:1 | 117 | 68.4 | **Good general vertical lift** |
| **26.9:1** | **223** | **38** | **Recommended starting point for a 2-stage continuous vertical slide** |
| 19.2:1 | 312 | 24.3 | Fast lift, light loads, cascade rigs |
| 13.7:1 | 435 | 18.7 | Horizontal slides, light loads |
| 5.2:1 / 3.7:1 / 1:1 | 1150 / 1620 / 6000 | 7.9 / 5.4 / 1.47 | Not for slides |

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Slide drive motor | goBILDA | **5203 Series Yellow Jacket** (8 mm REX), pattern `5203-2402-[ratio]` | 1-2 | 2-4 | **$54.99 ea** | Buy | **VERIFIED** — [category](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | The Viper-Slide kit page names the **5203 series** explicitly. Legal per Table 12-1 (R501). **Pick the ratio after Kickoff.** |
| Slide drive motor, long body | goBILDA | **5204 Series** (8 mm REX, 80 mm) | 0-2 | 0-4 | **$56.99 ea** | Buy | **VERIFIED** | Same ratios; longer body. Use only if packaging allows. |
| Budget motor + re-ratio in house | REV Robotics | **UltraPlanetary Gearbox Kit & HD Hex Motor** `REV-41-1600` | 1-2 | 2-4 | **$50.00 ea** | Buy | **VERIFIED** — In Stock | Includes the HD Hex motor + **3:1 (`REV-41-1601`), 4:1 (`REV-41-1602`), 5:1 (`REV-41-1603`)** cartridges, supporting **six reductions nominally 3:1 to 60:1**. |
| Spare UltraPlanetary cartridges | REV Robotics | `REV-41-1601` / `-1602` / `-1603` | 1-2 | 2-4 | **$12.50 ea** | Buy | **VERIFIED** | **The two-robot lever:** stock one motor SKU and re-ratio per robot instead of stocking two ratio-specific motors. R501's gearbox allowance (p. 76) makes this explicitly legal. |
| Through Bore Encoder | REV Robotics | `REV-11-1271` | 0-1 | 0-2 | **$40.80** (from $48.00) | Buy | **VERIFIED** | Only if you need position sensed at the shaft rather than at the motor. **Usually unnecessary** — the Yellow Jacket's built-in encoder is enough for a slide. |

**⚠ Two motors on one slide:** legal (R503 permits any allocation within 8) and sometimes necessary, but it
**doubles the slot cost of your lift** and requires the two motors to be mechanically tied so they cannot
fight. **JUDGMENT: try one motor with a lower ratio first.** Most FTC slide stacks that "need two motors"
actually need less friction and a correctly sized spool.

**⚠ R103 thermal warning applies directly here.** A vertical slide held at height by motor current during a
long inspection queue is exactly the *"stalled against a hard stop"* scenario the manual's blue box warns
about. Design a **mechanical rest** for the retracted position so the STARTING CONFIGURATION is held by
structure, not by current.

### 3.7 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Tooling needed | Material | Student-hours per robot | Notes |
|---|---|---|---|---|
| Slide-to-chassis mounting plates | 3D printer, or hand-cut aluminium + drill press | PETG/ABS print, or 1/8 in. aluminium plate | **2-3 h** | The Viper-Slide kit includes a Quad Block Pattern Mount; you still need to tie it to your chassis geometry. |
| Carriage / end-effector mounting bracket | 3D printer | PETG or ABS (not PLA — see §9.4) | **2-4 h** | Iterated more than any other part. Print it, expect v3. |
| Spool (if not buying `3407-0002-0112`) | 3D printer + lathe-free design | PETG | 1-2 h | **JUDGMENT: buy the goBILDA spool.** A printed spool with an inconsistent groove is a direct cause of cord overlap, which gm0 flags as a tension-destabiliser. |
| Cord rigging, routing and tensioning | Hand tools, lighter (to fuse cord ends), tension gauge or feel | — | **3-5 h first robot, 1-2 h second** | **The real labour.** Budget a full session with a mentor for robot A and expect robot B to go 3× faster. |
| Cord anchor points on each stage | Drill, tap (M4) | Slide steel / aluminium bracket | 1-2 h | Drilling a Viper-Slide makes it a FABRICATED ITEM (legal under R302 — raw materials and legal COTS parts may be modified). |
| Hard-stop / retracted rest | 3D printer or scrap aluminium | PETG / aluminium | 1 h | **Required by the R103 thermal argument above.** |
| Cable management for the moving carriage | Zip ties, spiral wrap, drag chain (printable) | — | **2-3 h** | Underestimated every season. See §9.5. |
| **Total** | | | **≈ 12-18 h robot A, 7-11 h robot B** | Robot B is faster only if you documented robot A. |

**Tooling reality check:** everything above is achievable with **3D printers and hand tools**. Nothing in the
slide mechanism requires a mill. That is a large part of why slides are the right answer for this team.

### 3.8 Subtotals

| Configuration | Per robot | **For 2 robots** |
|---|---|---|
| **Recommended: 2-stage Viper-Slide kit + 5203 motor + rigging spares** | $159.99 + $54.99 + ≈$25 consumables ≈ **$240** | **≈ $480** |
| Budget: REV 15mm Linear Motion Kit V2 ×2 + extrusion + cord + UltraPlanetary motor | $29.50 + extrusion (est., unverified) + $50.00 ≈ **$110-$150** | **≈ $220-$300** |
| Competitive: 4-stage Viper-Slide kit + 5203 motor + full spares | $229.99 + $54.99 + ≈$40 ≈ **$325** | **≈ $650** |

*All figures list price, before the goBILDA 25% team discount and the REV 15% select-items discount
documented in `VENDOR-ECOSYSTEMS.md` §5.4. **VERIFY-BEFORE-ORDER.***

### 3.9 Common failure modes and the spares to stock

| Failure | Cause | Prevention | Spare to stock (for 2 robots) |
|---|---|---|---|
| **Cord snaps** | Abrasion at a turn point; a too-small bend radius; knot fatigue | PTFE tubing (`2926-0204-1000`) at every rub point; proper pulleys not drilled holes; fuse cut ends | **4× `2908-0100-0005` cable** ($3.49 ea) — this is the single most important spare in this file |
| **Cord overlaps on the spool and tension goes slack** | Spool too narrow for the cord length | gm0: ensure *"when fully wrapped on the spool, your cable or string doesn't overlap"* | Wider spool design; 2× spare `3407-0002-0112` |
| **Stage driven out of its carriage** | No end-stop | **Install `2501-0001-0001` end-stops.** Non-negotiable. | 2× 6-packs |
| **Slide binds / feels gritty** | Misalignment — the two rails are not parallel or not coplanar | Mount both rails to one rigid plate, not to two separate chassis members. Shim to square. | — (a fabrication discipline, not a spare) |
| **Ball bearings develop play** | Wear over a season | gm0 notes this for both MiSUMi and Viper slides | **2× spare `2500-0014-0336`** ($19.99 ea) |
| **Belt skips teeth** | Under-tension, or a pulley set screw slipping | Check the 60T pulley grub screw at every event | 1× spare GT2 belt |
| **Slide sags at full horizontal extension** | Cantilever bending, not a slide fault | Dual opposed slides (gm0); shorten the moment arm | — (design) |
| **Motor holds position by current and overheats** | No mechanical rest, per R103 blue box | Mechanical rest at retracted position; brake mode only for short holds | — (design) |

**JUDGMENT — the spares kit that actually gets used:** 4× cord, 2× spare slide, 2× end-stop packs, 1× spare
GT2 belt, 1× spare 5203 motor **shared between the two robots**. Roughly **$130** for the pair, and it is the
difference between a 20-minute pit fix and a forfeited match.

### 3.10 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Hardware | **2-stage Viper-Slide kit `3210-0003-0002`**, belt-driven, out of the box | 4-stage kit `3210-0003-0004` or `3210-0004-0004`, cord-rigged for compactness |
| Rigging | Belt (kit default) — no tensioning to learn | Continuous cord + dual spool, spring tensioner at the far end |
| Motor | 1× **5203 @ 26.9:1** (223 RPM) | 1-2× 5203, ratio tuned to measured load; possibly 19.2:1 for speed |
| Control | Encoder + simple PID to preset heights | PID + feedforward gravity term + motion profile |
| Position feedback | Motor encoder only | Motor encoder + magnetic limit switch (`REV-31-1462`, $17.50) for zeroing |
| Stages | 2 | 3-4, R105 permitting |
| Cost per robot | **≈ $240** | **≈ $325-$400** |
| Build time | 12-18 h robot A | 25-35 h robot A |
| **Duplicability** | **5 — identical re-order** | **4 — more rigging to match across two robots** |

**Start at the rookie minimum on both robots.** Upgrade robot A only, once it is scoring reliably, and only
port the upgrade to robot B if it proves out. **A two-robot program that runs two different lift designs has
doubled its spare-parts problem and halved its student expertise per design.**

---

## 4. M-2 — ALTERNATIVES TO SLIDES

### 4.1 What these are and when a design needs them

Slides are not always the answer. Every mechanism below trades the slide's linear predictability for
something else — less cost, less height, fewer parts, or a specific motion path. The honest headline: **for
this team, only two of these five beat a slide, and one of them (virtual four-bar) is not really an
alternative at all — it is an addition to an arm.**

### 4.2 The variants, compared honestly

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Honest verdict for this team |
|---|---|---|---|---|---|---|
| **Virtual four-bar** (arm + belt/chain keeping the end effector level) | **2** | **1** | 2 | **5** | **5** | **Best value in this section.** gm0: *"an easy addition to an arm to maintain the end effector's angle relative to the ground"*, travels **over 180°**, less space than a true four-bar. **Costs zero extra actuator slots.** |
| **True four-bar linkage** | 3 | 2 | 2 | 4 | 4 | Keeps the end bar level mechanically, but gm0 notes it is limited to **under 90° of travel** each way without special construction and *"takes up significant internal frame space"* — described as **rarely used** in FTC. |
| **Double-reverse four-bar (DRFB) / virtual DRFB** | **5** | 3 | **5** | 3 | **2** | Produces *"purely linear extension"* with a fixed end-effector angle; the virtual version with **2:1 pulley ratios** is *"much more compact"*. **JUDGMENT: no.** High part count, fiddly tensioning, and it must be built and matched twice. |
| **Scissor lift** | **5** | 3 | 4 | 2 | **1** | Many pivots, many identical links, and every pin joint is a wear point and a slop source. **Without a mill, fabricating 8-16 matched links twice is a trap.** Rarely competitive in FTC. |
| **Telescoping tubes** (nested box tube, custom) | 4 | 2 | 4 | 3 | **2** | You are hand-fabricating what Viper-Slides sell for $19.99. Friction is unpredictable, and matching two sets is luck. **Do not, absent a mill.** |
| **Rack and pinion** | 3 | **1** | 2 | 3 | 4 | Cheap and positive-drive — no cord to break. But extension is limited to roughly the rack length, so it does **not** telescope. Good for short, forceful, precise linear moves. |
| **Elevator on a belt** (carriage on a single continuous belt loop) | 2 | 2 | 2 | 4 | 4 | Simple, no cord to snap, no tensioning drift (belts *"never need to be tensioned"*). Limited to **single-stage** travel = rail length. Good vertical option when 18 in. of rail fits. |

*(1 = low/cheap/easy, 5 = high/expensive/hard, except Reliability and Duplicability where 5 = best.)*

**Community reference for the four-bar rows, verified this session:**
<https://gm0.org/en/latest/docs/common-mechanisms/linkages.html>.

**The verdict, stated plainly (JUDGMENT):**

1. **Virtual four-bar — build it.** It is the cheapest capability upgrade in this entire file. A belt or
   chain from a fixed pulley at the arm pivot to a matching pulley at the wrist keeps the gripper level
   through the whole sweep, with **no motor, no servo, and no code.** gm0: *"Both chain and belt can be used
   ... and there isn't a specific benefit to using either."*
2. **Rack and pinion — consider it** for a short, precise, high-force horizontal push where a cord would go
   slack. It is positive-drive in both directions, which a single-cord slide is not.
3. **Elevator on a belt — consider it** for a simple single-stage vertical lift, especially on the REV
   ecosystem where 15 mm extrusion and GT2 belt are already in the parts bin.
4. **Scissor, DRFB and telescoping tubes — decline.** All three score 1-2 on duplicability, all three need
   precision this shop cannot produce, and all three must be built twice. This is the clearest
   fabrication-capability filter in the whole catalog.

### 4.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Virtual four-bar: GT2 / HTD belt** | goBILDA | Timing Belts & Pulleys — **GT2 2 mm**, HTD 3 mm, HTD 5 mm | 1-2 | 2-4 | not verified per-SKU | Buy | **FAMILY-ONLY** — [category](https://www.gobilda.com/timing-belts-pulleys/) | Profiles verified; individual belt SKUs and lengths not. **Open the category page and match centre distance.** |
| Timing belt & pulley starter pack, 2 mm GT2 | goBILDA | 2mm GT2 Starter Pack | 0-1 | 1 (share) | **$239.99** | Buy | **VERIFIED** — [category](https://www.gobilda.com/timing-belts-pulleys/) | Expensive, but **one pack serves both robots** and removes the "we ordered the wrong belt length" failure. Consider as a program-level purchase. |
| Timing belt & pulley starter pack, 5 mm HTD | goBILDA | 5mm HTD Starter Pack | 0-1 | 1 (share) | **$209.99** | Buy | **VERIFIED** | For higher-torque virtual four-bars; taller tooth resists skipping. |
| **Virtual four-bar: chain alternative** | goBILDA | Sprockets & Chain — **8 mm pitch** | 1-2 | 2-4 | not verified | Buy | **FAMILY-ONLY** — [category](https://www.gobilda.com/sprockets-chain) | ⚠ goBILDA runs **8 mm pitch**, incompatible with #25 — see `VENDOR-ECOSYSTEMS.md` §3.5. Buy spare links up front. |
| **Rack and pinion: gear rack** | goBILDA | `2311-0001-0131` Acetal MOD 0.8 Gear Rack (131 tooth, 41 hole) | 1-2 | 2-4 | **$7.99 ea** | Buy | **VERIFIED** — [category](https://www.gobilda.com/gear-racks/) | Overall length not stated on the page. MOD 0.8 matches goBILDA's hub-mount and pinion gear families. |
| Rack and pinion: pinion gear | goBILDA | **Pinion Gears** family, MOD 0.8 | 1-2 | 2-4 | not verified | Buy | **NEEDS-SKU-CHECK** — [gears category](https://www.gobilda.com/gears) | Family confirmed on the gears category page; tooth counts and prices not read. |
| **Four-bar / linkage: rod ends & ball joints** | goBILDA | Linkages & Threaded Rods | 4-8 | 8-16 | not verified | Buy | **FAMILY-ONLY** — [category](https://www.gobilda.com/linkages-threaded-rods) | **Explicitly legal beyond single-DoF under R303.L** — *"items that connect structures at variable angles (such as ball joint linkages, rod ends)"*. |
| Four-bar pivots: flanged bearings | goBILDA | **1601 / 1611 Series Flanged Ball Bearings** | 8 | 16 | **$3.99-$11.99** (series range) | Buy | **FAMILY-ONLY** — [bearings category](https://www.gobilda.com/bearings/) | A four-bar has 4 pivots × 2 sides. **Bushings instead of bearings is the usual slop source.** |
| Hinges (for simple pivoting links) | goBILDA | Hinges family | 2-4 | 4-8 | not verified | Buy | **FAMILY-ONLY** — [category](https://www.gobilda.com/hinges/) | |

### 4.4 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Tooling | Material | Student-hours per robot | Notes |
|---|---|---|---|---|
| Virtual four-bar: pulley mounts at pivot and wrist | 3D printer | PETG | **2-3 h** | The whole mechanism is two pulleys and a belt. **Get the two pulleys the same tooth count for 1:1 levelling.** |
| Virtual four-bar: belt tensioner | 3D printer, or zip ties | PETG | 1 h | gm0 notes zip-tie tensioning is a legitimate option here. |
| Four-bar: the four links | Hand-cut aluminium or 3D print | 1/8 in. aluminium bar / PETG | **4-6 h** | **All four links must be matched in length to ~0.5 mm** or the bar will not stay level. This is the hard part and it doubles for robot B. |
| Rack and pinion: rack mounting rail | Drill, hand tools | goBILDA channel | 2 h | The rack has 41 holes — mounting is straightforward on the 8 mm grid. |
| Elevator-on-belt: carriage | 3D printer | PETG | 2-3 h | |
| **Total (virtual four-bar only)** | | | **≈ 3-4 h** | **The reason to prefer it.** |
| **Total (true four-bar)** | | | **≈ 8-12 h** | |

### 4.5 Subtotals

| Configuration | Per robot | **For 2 robots** |
|---|---|---|
| **Virtual four-bar added to an existing arm** | ≈ **$25-$40** (belt + 2 pulleys + print) | **≈ $50-$80** |
| True four-bar linkage | ≈ **$60-$90** (bearings, rod ends, stock) | **≈ $120-$180** |
| Rack and pinion, single axis | ≈ **$30-$50** | **≈ $60-$100** |
| Elevator on a belt, single stage | ≈ **$80-$120** | **≈ $160-$240** |

*Ranges are wider than §3 because several component rows are FAMILY-ONLY. **VERIFY-BEFORE-ORDER.***

### 4.6 Common failure modes and spares

| Failure | Cause | Prevention | Spare |
|---|---|---|---|
| Virtual four-bar drifts out of level | Belt skipped a tooth, or a pulley grub screw slipped | Use a toothed belt not a round belt; **check grub screws at every event**; witness-mark the pulleys | 1× spare belt per profile |
| Four-bar binds or racks | Link lengths mismatched, or one pivot is tighter than the others | Match links to 0.5 mm; bearings at every pivot, not bushings | 4× spare flanged bearings |
| Rack teeth strip | Acetal rack against a metal pinion under shock load | Add a hard stop before the rack runs out; do not use as a crash-stop | **2× spare `2311-0001-0131`** ($7.99 ea) |
| Scissor lift develops slop | 8-16 pin joints, each with clearance, all adding up | *(This is why the answer is "do not build one")* | — |
| Belt elevator carriage tips | Single belt = single point of drive on a wide carriage | Guide the carriage on the rail, drive it from the centreline | — |

### 4.7 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Choice | **Virtual four-bar on a simple arm.** Nothing else in this section. | Virtual four-bar on a pivot-extension (arm + slide) |
| Why | 3-4 student-hours, ~$30, zero actuator slots, duplicability 5 | Adds slide reach on top of level-keeping |
| Avoid entirely | Scissor, DRFB, telescoping tubes | Same — these do not become good at higher skill for *this shop* |

---

## 5. M-3 — ARMS AND PIVOTS

### 5.1 What it is and when a design needs it

An arm is a rigid member rotating about a fixed axis, carrying an end effector through an arc. It is the
**fastest mechanism in this file to build** and the one most likely to be right for a rookie-adjacent team.

**gm0's arm taxonomy, verified this session** at
<https://gm0.org/en/latest/docs/common-mechanisms/arms.html>:

| Arm type | gm0's description | Verdict for this team (JUDGMENT) |
|---|---|---|
| **Single arm** | *"The most simple type of arm ... on one axis of rotation."* Quick to build, but limited to **around 16 in.** of extension, *"making them less competitive as primary extension systems."* | **Build this first.** 16 in. is a lot inside an 18 in. cube constraint. |
| **Pivot extension** | A rotating arm with linear slides attached — horizontal *and* vertical reach *"without needing a separate transfer stage."* | **The strong mid-tier answer.** Combines §3 and §5. Costs 2 motor slots. |
| **Multi-axis arm** | *"much more difficult to design, manufacture, and control"* and *"highly discouraged for inexperienced FTC teams."* | **Decline.** gm0's language is unusually direct, and it is right. |

**A design needs an arm when:** reach is modest, the path can be an arc, speed matters more than precision,
or the mechanism must sweep *over* an obstacle rather than through it. **A design needs a slide instead
when** the path must be straight, reach exceeds ~16 in., or the end effector must stay at a constant radius.

### 5.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **Servo-driven arm** (light loads, <180°) | **1** | **1** | 2 | 4 | **5** | **The rookie answer.** Zero motor slots. Position control is free. Limited torque — check against Table 12-2 limits. |
| **Motor + planetary gearbox arm** | 2 | 3 | 3 | 4 | **5** | **The default.** Yellow Jacket at a high ratio, driven through a gear or chain, not off the shaft directly. |
| **Motor + worm gear arm** | 3 | 3 | **2** | 4 | 4 | **Holds position with no power** — the key property. 28:1 in one stage. ⚠ R203 manual-release problem. |
| **Motor + belt/chain reduction to arm** | 3 | 3 | 3 | 4 | 4 | gm0 recommends driving *"through a gear, chain, or belt rather than directly mounting to a motor shaft"* to handle axial forces and reach larger reductions. |
| **Pivot extension (arm + slide)** | 4 | 5 | 4 | 3 | 3 | Powerful and expensive. **2 motor slots.** Only if the game clearly demands both axes. |
| **Multi-axis arm** | **5** | 5 | **5** | 2 | **1** | Decline. |

### 5.3 Motor and gearbox selection for a pivoting arm

**The torque reasoning (JUDGMENT, arithmetic from verified figures):**

Static holding torque at the pivot = (payload + arm mass) × (distance to centre of mass). An arm carrying
**0.5 kg at 30 cm** needs **15 kg·cm** just to hold, before the arm's own weight, before acceleration, and
before any margin. Add the arm structure (say 0.3 kg at 15 cm = 4.5 kg·cm) and apply a **2× dynamic factor**:
you are shopping for roughly **40 kg·cm** of usable output.

Reading that against the **VERIFIED** Yellow Jacket table in §3.6: **26.9:1 gives 38 kg·cm** stall — too
close to the requirement to be safe, because you never design to stall. **50.9:1 (68.4 kg·cm, 117 RPM)** or
**71.2:1 (93.6 kg·cm, 84 RPM)** is the honest choice. gm0 notes real FTC arms use large reductions, citing
one example at **254.5:1**.

**Two ways to get a big reduction (both legal — R501's gearbox allowance, p. 76, permits using a legal motor
*"with or without the provided gearbox, and/or with any other compatible gearbox"*):**

| Path | How | Pros | Cons |
|---|---|---|---|
| **A. High-ratio planetary + external stage** | 71.2:1 Yellow Jacket + 3:1 belt or gear reduction ≈ 214:1 | Simple, all COTS, smooth, back-drivable (safe for R203) | Needs holding current at rest; consumes gravity-compensation effort |
| **B. Worm gear** | Motor + goBILDA **28:1 worm set** | **Self-locking — holds with no power.** *"nearly lock into place and resist being back-driven."* Huge reduction in one small stage | ⚠ **R203 problem** — see the warning below. Lower efficiency, more heat |

**Why worm/high-ratio drives are used to hold position without power:** a worm gear's helix angle is shallow
enough that friction exceeds the back-driving force, so the output cannot turn the input. The arm stays where
it is with the motor unpowered. That saves battery, eliminates thermal risk under **R103**, and removes the
drift you get from a PID holding against gravity. goBILDA's own page describes the 28:1 sets as *"extreme
reduction in speed"* drives that *"nearly lock into place and resist being back-driven."* **VERIFIED** at
<https://www.gobilda.com/worm-gears/>.

> ⚠ **R203 WARNING (CONFIRMED-BIOBUZZ, p. 69).** *"ROBOTS must be designed to be quickly removed from the
> FIELD without requiring power ... ROBOTS must allow removal of SCORING ELEMENTS from the ROBOT and the
> ROBOT from FIELD elements while powered off."* **A self-locking worm arm that has a SCORING ELEMENT or a
> field element trapped in it, with a dead battery, is a rule violation and a field-reset delay.** If you use
> a worm drive, design a **manual release** — a removable pin, a quick-release gripper, or a hand crank on
> the worm shaft — and show it to the inspector. This is a real inspection conversation, not a theoretical one.

### 5.4 Gravity compensation and the virtual four-bar

**Gravity compensation (JUDGMENT):** an arm's holding torque varies with the **cosine of its angle from
horizontal** — maximum when horizontal, zero when vertical. Three ways to handle it:

| Method | How | Actuator cost | Notes |
|---|---|---|---|
| **Software feedforward** | Add a term proportional to cos(θ) to the motor output | 0 | Free, effective, and the standard answer. Needs an absolute angle reference — see §5.6. |
| **Counterweight** | Mass on the short side of the pivot | 0 | Works, but adds inertia and mass. R104 confirms **no weight limit in BIOBUZZ**, so this is cheaper than it used to be. |
| **Assist spring / gas spring** | Spring pulls the arm up, sized to cancel the horizontal-position torque | **0 slots** | **The best answer.** See §8. Legal under R801.A for gas springs; ordinary springs are unrestricted. |

**The virtual four-bar (cross-reference §4.2):** if the end effector must stay level as the arm sweeps, a
belt or chain from a **fixed** pulley at the pivot to an equal-tooth pulley at the wrist does it mechanically.
gm0: *"If the end bar of a virtual four bar is parallel to the ground when retracted, it will be parallel to
the ground at all times, even when rotated fully out."* **This saves a servo slot** versus actively
levelling the wrist — worth 1 of your 8 servos for ~$30 of belt and printed pulley mounts.

### 5.5 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Arm drive motor** | goBILDA | **5203 Series Yellow Jacket**, pattern `5203-2402-[ratio]` — **50.9:1 or 71.2:1** | 1 | 2 | **$54.99 ea** | Buy | **VERIFIED** — [category](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | Legal per Table 12-1 (R501). Ratio table in §3.6. VERIFY-BEFORE-ORDER. |
| **Worm Gear Set, 28:1, 8 mm REX bore worm** | goBILDA | `3204-0001-0002` | 0-1 | 0-2 | **$34.99 ea** | Buy | **VERIFIED** — [category](https://www.gobilda.com/worm-gears/) | Self-locking. **Pair with the R203 manual release.** 8 mm REX matches the 5203/5204 output. |
| Worm Gear Set, 28:1, 6 mm D-bore worm | goBILDA | `3204-0001-0003` | 0-1 | 0-2 | **$34.99 ea** | Buy | **VERIFIED** | For 5202-series or NeveRest 6 mm D output. |
| **Ultra 90 Degree Gearbox** | REV Robotics | `REV-41-2080` | 0-1 | 0-2 | **$45.00** | Buy | **VERIFIED** — [motion category](https://www.revrobotics.com/ftc/motion/) | Right-angle drive when the motor cannot sit on the pivot axis. Single-speed, therefore legal under **R303.C**. |
| **UltraPlanetary Gearbox Kit & HD Hex Motor** | REV Robotics | `REV-41-1600` | 0-1 | 0-2 | **$50.00** | Buy | **VERIFIED** — In Stock | 3:1 to **60:1** from stacked cartridges. Budget path. |
| UltraPlanetary cartridges, spare | REV Robotics | `REV-41-1601` (3:1) / `REV-41-1602` (4:1) / `REV-41-1603` (5:1) | 1-3 | 2-6 | **$12.50 ea** | Buy | **VERIFIED** | Re-ratio in the pit without a new motor. |
| **Hub-mount gear for external reduction** | goBILDA | **2302-0014-####** (14 mm bore, aluminium, MOD 0.8, **48-108T**) | 1-2 | 2-4 | **$9.99-$16.99** (108T = **$16.99**) | Buy | **VERIFIED (series + range)** / **NEEDS-SKU-CHECK (exact tooth count)** | [category](https://www.gobilda.com/hub-mount-gears/). Aluminium for a loaded arm; acetal (**2312-0414-####**, 45-100T, $2.99-$5.79) only for light duty. |
| Pinion gear to match | goBILDA | **Pinion Gears** family, MOD 0.8 | 1-2 | 2-4 | not verified | Buy | **NEEDS-SKU-CHECK** — [gears category](https://www.gobilda.com/gears) | Family confirmed; SKUs not read. |
| **Arm pivot bearings** | goBILDA | **1602 / 1605 / 1606 Series Pillow Blocks** | 2 | 4 | **$5.99-$14.99** (series range) | Buy | **FAMILY-ONLY** — [bearings category](https://www.gobilda.com/bearings/) | **Two bearings, one each side of the arm.** A single-sided pivot is the classic arm failure (§9.2). |
| Heavy-duty flange-mount bearing | goBILDA | **1622 Series** | 0-2 | 0-4 | **$9.99** | Buy | **FAMILY-ONLY** | For 12 mm REX heavy-duty arm shafts. |
| **Servo (light arm, or wrist)** | goBILDA / REV | Must pass the **R502 / Table 12-2** spec test | 1-2 | 2-4 | see `LEGAL-PARTS-CONSTRAINTS.md` §4.5 | Buy | **cross-ref** | ⚠ R502 is a **spec test, not a closed list** — power and 6 V stall current. Do not buy a servo without checking it. |
| **Touch Sensor (limit switch)** | REV Robotics | `REV-31-1425` | 1-2 | 2-4 | **$8.75 ea** | Buy | **VERIFIED** — [sensors](https://www.revrobotics.com/ftc/electronics/sensors/) | REV's own text: *"best used for user input, but can also be used as a limit switch."* **The cheap way to zero an arm.** |
| **Magnetic Limit Switch** | REV Robotics | `REV-31-1462` | 0-2 | 0-4 | **$17.50 ea** | Buy | **VERIFIED** | *"Three-sided active-low digital hall effect switch."* **No moving contact to wear or misalign** — more reliable than a mechanical switch on a fast arm. |
| **Potentiometer (absolute angle)** | REV Robotics | `REV-31-1155` | 0-1 | 0-2 | **$15.25 ea** | Buy | **VERIFIED** | 10K analog. **Gives absolute arm angle at power-on**, which is what a gravity-feedforward term needs. |
| Through Bore Encoder | REV Robotics | `REV-11-1271` | 0-1 | 0-2 | **$40.80** (from $48.00) | Buy | **VERIFIED** | Measures at the joint, past any gearbox backlash. Competitive-tier only. |

### 5.6 Hard stops and limit switches — the hardware that saves the mechanism

**JUDGMENT, and it is not optional:** an arm with no hard stop will eventually be commanded past its range,
and it will break something — usually the gearbox, occasionally the wiring.

| Element | Purpose | Implementation |
|---|---|---|
| **Mechanical hard stop, both ends** | Absorbs the crash when software fails | **Fabricated.** A printed or aluminium block against a channel face. Put it **close to the pivot** where torque is high but travel is small, so the impact energy is low. Never let a gear tooth or a rack end be the stop. |
| **Limit switch at the home position** | Zeroes the encoder at init | `REV-31-1425` ($8.75) mechanical, or `REV-31-1462` ($17.50) magnetic. **Magnetic for anything that moves fast.** |
| **Absolute angle reference** | Lets gravity feedforward work at power-on without a homing sweep | `REV-31-1155` potentiometer ($15.25), or `REV-11-1271` through-bore encoder ($40.80) |
| **Soft limits in code** | The first line of defence | Free. Set them **inside** the hard stops. |

**R103 interaction (CONFIRMED-BIOBUZZ, p. 67):** an arm may be pre-positioned by an OpMode to hold
STARTING CONFIGURATION, but the blue box warns against *"having motors stalled against a hard stop"* for the
several minutes an inspection queue can take. **Design the stowed position so the arm rests on a mechanical
stop under gravity, not against motor current.**

### 5.7 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Tooling | Material | Student-hours per robot | Notes |
|---|---|---|---|---|
| Arm structural member | Hacksaw / chop saw, drill, deburr | goBILDA channel (1120 U-channel or 1121 low-side) | **2-3 h** | Cutting channel to length for storage is *neither* COTS nor FABRICATED (manual p. 64); cutting it to final form makes it a FABRICATED ITEM. Either way it is legal under **R302**. |
| Pivot mounting plates | 3D printer or hand-cut aluminium + drill press | PETG / 1/8 in. aluminium | **3-4 h** | **Both sides.** See §9.2. |
| End-effector mount | 3D printer | PETG | 2-4 h | Iterated most. |
| Hard stops (2 per arm) | 3D printer or scrap aluminium | PETG / aluminium | **1-2 h** | **Mandatory.** |
| Limit-switch bracket | 3D printer | PETG | 1 h | Make it adjustable — you will move it. |
| Worm-drive manual release (if worm used) | 3D printer + hand tools | PETG + a pull pin | **2 h** | **R203 compliance.** Do not skip. |
| Gravity-assist spring mount | 3D printer + hand tools | PETG + eyebolts | 2 h | See §8. |
| Cable routing along the arm | Zip ties, spiral wrap | — | 2 h | The wire must survive the full sweep, both directions, thousands of cycles. |
| **Total** | | | **≈ 13-20 h robot A, 8-12 h robot B** | |

### 5.8 Subtotals

| Configuration | Per robot | **For 2 robots** |
|---|---|---|
| **Rookie: servo arm + hard stops + printed structure** | ≈ **$60-$90** | **≈ $120-$180** |
| **Default: 5203 @ 71.2:1 + pillow blocks + touch sensor + channel** | $54.99 + ≈$20 bearings + $8.75 + ≈$30 channel/print ≈ **$115** | **≈ $230** |
| **Worm-drive arm (self-holding)** | above + $34.99 worm set ≈ **$150** | **≈ $300** |
| **Competitive: + external gear reduction + potentiometer + magnetic switch** | ≈ **$200-$230** | **≈ $400-$460** |
| **Pivot extension (arm + slide)** | §5 default + §3 recommended ≈ **$355** | **≈ $710** |

*List price, before discounts. **VERIFY-BEFORE-ORDER.***

### 5.9 Common failure modes and spares

| Failure | Cause | Prevention | Spare (2 robots) |
|---|---|---|---|
| **Gearbox strips** | Arm crashed into a hard stop at speed, or into the field | Soft limits inside hard stops; hard stop near the pivot; **do not drive an arm at full speed into its limit** | **1× spare 5203 motor** ($54.99) shared |
| **Pivot shaft bends / arm goes out of plane** | Single-sided pivot; load taken in cantilever | **Two pillow blocks, one per side.** See §9.2. | 2× spare pillow blocks |
| **Motor mounted directly to the arm shaft fails** | Axial and radial loads fed straight into the gearbox output | gm0: drive *"through a gear, chain, or belt rather than directly mounting to a motor shaft"* | — (design) |
| **Arm drifts down when disabled** | No self-locking, no spring, no rest | Worm drive, assist spring, or a mechanical rest | — (design) |
| **Arm cannot be moved by hand at field reset** | Worm drive with no release | **R203.** Build the manual release. | — (design) |
| **Encoder loses zero** | No limit switch; power cycled mid-match | Limit switch home + potentiometer for absolute reference | 2× `REV-31-1425` ($8.75 ea) |
| **Wire harness on the arm chafes through** | Repeated flexing over an edge | Spiral wrap, generous service loop, no sharp edges | Wire + connectors from the §6.6 stock in `VENDOR-ECOSYSTEMS.md` |
| Worm gear overheats / wears | Worm drives are inefficient; continuous duty at high load | Duty-cycle it; do not use a worm for a continuously-moving mechanism | 1× spare `3204-0001-0002` |

### 5.10 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Actuation | **1 servo** (R502-compliant), or 1× 5203 @ 71.2:1 | 5203 @ 50.9:1 + 3:1 external belt reduction ≈ 153:1 |
| Position sensing | Motor encoder + `REV-31-1425` touch sensor ($8.75) | + `REV-31-1155` potentiometer ($15.25) for absolute angle |
| Levelling the end effector | Fixed angle, or 1 servo wrist | **Virtual four-bar** — belt, no actuator |
| Gravity handling | None (small load) | Software feedforward + assist spring |
| Holding at rest | Mechanical rest | Worm drive **with R203 manual release**, or spring balance |
| Structure | goBILDA channel, printed brackets, **two pillow blocks** | Same, plus a gusseted pivot box |
| Cost per robot | **≈ $60-$115** | **≈ $200-$230** |
| Build time | 13-20 h robot A | 25-35 h robot A |
| **Duplicability** | **5** | **4** |

---

## 6. M-4 — TURRETS AND ROTATION

### 6.1 What it is and when a design needs it

A turret rotates a mechanism about a vertical axis independently of the drivetrain, so the robot can aim or
place without re-orienting the chassis. It is the most seductive mechanism in FTC and, for most teams, the
worst investment in this file.

**A design might need a turret when:** the robot must score at many angles from one position, aiming is
time-critical, or the drivetrain is too slow/imprecise to rotate the whole robot. **A design does not need
one when:** a holonomic drivetrain can simply rotate the robot — which, in FTC, is almost always.

### 6.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **Fabricated slew ring — large gear on thrust bearing + guide rollers** | **5** | 4 | 4 | 3 | **2** | The standard FTC approach. **Requires precision this shop does not have.** |
| **Belt-reduction turret on a central shaft** | 4 | 3 | 3 | 3 | 3 | Simpler; a central shaft in two pillow blocks with a big pulley. Limited load capacity. |
| **COTS turntable** (R303.E names it as legal) | 2 | ? | 2 | 4 | **5** | ⚠ **I could not find one to buy.** See §6.4 — this is a real, verified negative finding. |
| **"Turret" by rotating the whole robot** | **1** | **0** | 1 | **5** | **5** | **The honest answer for this team.** Holonomic drive already does this. |

### 6.3 The mechanical problem, honestly stated

A turret needs four things at once:

1. **A rotating joint that carries axial load** (the mechanism's weight) **and a large overturning moment**
   (its cantilever). A single bearing does not do this. Real slew bearings are a specific product class.
2. **A large reduction**, because a turret must be precise and must not back-drive when the robot
   accelerates. That means a large gear or a large pulley — and a large gear is a large diameter.
3. **Cable management across a rotating joint.** Every wire to the mechanism must survive rotation.
4. **A hard limit or a slip ring**, because unlimited rotation with wires is not possible.

### 6.4 ⚠ VERIFIED NEGATIVE FINDING — you cannot simply buy the bearing

**R303.E explicitly names "turntable" as a legal single-DoF COTS mechanism** (CONFIRMED-BIOBUZZ, p. 70). So
the rule anticipates you buying one. **But I checked, and the standard FTC vendors do not stock one:**

| Vendor | Category page loaded this session | Turntable / slew bearing found? |
|---|---|---|
| goBILDA | <https://www.gobilda.com/bearings/> | **No.** The category lists pillow blocks (1602-1622), ball bearings (1600/1601/1611), idler rollers (1607), V-groove (1609), linear ball bearings (1612), **thrust ball bearings (1613)**, sealed (1626). **No one-way/clutch bearings and no turntable or slew bearings.** |
| ServoCity | <https://www.servocity.com/structure/> | **No.** 23 structure subcategories listed; no turntable, lazy susan, slew bearing or rotating base. |
| Web search | "goBILDA turntable slew bearing FTC part number" | **No FTC-vendor result.** Only industrial crane slew bearings and unrelated listings. |

**Consequence (JUDGMENT):** building a turret means **fabricating** the slew joint from a large hub-mount
gear, a **1613-series thrust bearing**, and a set of guide rollers (**1607-series idler rollers** or
**1609-series V-groove bearings**) running on a printed or hand-cut race. That is a precision assembly, made
twice, by a team with no mill. **This is the single strongest fabrication-capability argument in this file.**

If a genuine FTC-vendor turntable exists that I did not find, it would change this verdict — so this row is
flagged in §13 as an open question to re-check at Kickoff.

### 6.5 BUY — the COTS parts table (if you build one anyway)

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Large ring gear (turret bull gear)** | goBILDA | **2302-0032-####** (32 mm bore, aluminium, MOD 0.8, **80-108T**) | 1 | 2 | **$13.79-$16.99** (108T = **$16.99**) | Buy | **VERIFIED (series + range)** / **NEEDS-SKU-CHECK (tooth count)** | [category](https://www.gobilda.com/hub-mount-gears/). **108T is the largest goBILDA offers** — at MOD 0.8 that is ~86 mm pitch diameter. **That is small for a turret race.** |
| Large ring gear, 14 mm bore | goBILDA | **2302-0014-####** (aluminium, MOD 0.8, 48-108T) | 1 | 2 | **$9.99-$16.99** | Buy | **VERIFIED (series)** | |
| Pinion to drive it | goBILDA | Pinion Gears, MOD 0.8 | 1 | 2 | not verified | Buy | **NEEDS-SKU-CHECK** — [gears](https://www.gobilda.com/gears) | Reduction = ring teeth ÷ pinion teeth. 108T ÷ 12T = 9:1. |
| **Thrust bearing (axial load)** | goBILDA | **1613 Series Thrust Ball Bearings** | 1-2 | 2-4 | **$3.99-$4.99** (series range) | Buy | **FAMILY-ONLY** — [bearings](https://www.gobilda.com/bearings/) | **Carries weight, not moment.** You still need guide rollers for the tipping load. |
| Guide rollers | goBILDA | **1607 Series Idler Rollers** ($7.99) or **1609 Series V-Groove** ($5.99/2-pack) | 3-4 | 6-8 | **$5.99-$7.99** | Buy | **FAMILY-ONLY** — [bearings](https://www.gobilda.com/bearings/) | Three rollers minimum, at 120°, to constrain the moment. |
| Central shaft + pillow blocks | goBILDA | 8 mm or **12 mm REX** shafting + **1622 Series** flange-mount | 1 set | 2 sets | **$9.99** (1622) + shaft | Buy | **FAMILY-ONLY** | 12 mm REX for a loaded turret. |
| Turret drive motor | goBILDA | **5203 Series** @ 99.5:1 or higher | 1 | 2 | **$54.99 ea** | Buy | **VERIFIED** | High ratio so the turret does not back-drive under chassis acceleration. **Costs a motor slot.** |
| Belt reduction alternative | goBILDA | Timing Belts & Pulleys — HTD 5 mm | 1 set | 2 sets | not verified per-SKU | Buy | **FAMILY-ONLY** — [category](https://www.gobilda.com/timing-belts-pulleys/) | HTD 5 mm has a *"taller tooth to create a drive with less chance of belt-slip"*. |
| Turret home limit switch | REV Robotics | `REV-31-1462` magnetic | 1 | 2 | **$17.50 ea** | Buy | **VERIFIED** | Zeroing a turret matters more than zeroing anything else. |
| **Slip ring** | — | — | 1 | 2 | not verified | Buy | **UNVERIFIED** | ⚠ **No FTC vendor page verified this session.** Any slip ring must come from a supplier meeting the **VENDOR** test (Federal Tax ID, ships to all teams, ~5 business days for shelf stock — manual pp. 65-66). **Do not order on this row.** |

### 6.6 Cable management across the rotating joint

**Three options, ranked (JUDGMENT):**

| Option | How | Verdict |
|---|---|---|
| **1. Limited rotation with a service loop** | Restrict travel to ±180° or less; leave a generous wire loop that twists rather than rotates | **Do this.** No extra parts, no failure mode, legal, cheap. Nearly every FTC turret task fits inside ±180°. |
| **2. Slip ring** | Rotating electrical contact allows unlimited rotation | Adds a part with a real failure mode (intermittent contact under vibration), an unverified supply chain, and doubles for robot B. **Only for continuous rotation, which FTC rarely needs.** |
| **3. Put everything on the turret** | Battery, hub and all on the rotating platform | **No.** Violates sanity and complicates R601/R603 main-switch access. |

**⚠ The wires that cross the joint carry motor current.** They are subject to **R609** wire-sizing (Table
12-8) and **R610** colour rules — see `LEGAL-PARTS-CONSTRAINTS.md` §6.7-6.8. A slip ring's current rating
must be checked against the motor it feeds; most cheap slip rings are rated for signal, not for a motor.

### 6.7 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Tooling | Material | Student-hours per robot | Notes |
|---|---|---|---|---|
| **Turret race / roller track** | 3D printer (large bed) or hand-cut plate | PETG or 1/8 in. aluminium | **6-10 h** | **The hard part.** Must be flat and concentric. Printed races warp; aluminium needs an accurate circle you cannot mill. |
| Turret deck (rotating platform) | 3D printer / hand-cut plate | PETG / aluminium | 4-6 h | |
| Roller mounts (3-4) | 3D printer | PETG | 2-3 h | Must be adjustable to preload the rollers. |
| Gear-to-deck mounting | Drill, hand tools | — | 2 h | |
| Motor and pinion mount | 3D printer / plate | PETG / aluminium | 2-3 h | Needs centre-distance adjustment for gear mesh. |
| Cable service loop and strain relief | Zip ties, spiral wrap | — | **3-4 h** | Underestimated. |
| Hard stops at each rotation limit | 3D printer | PETG | 1-2 h | |
| **Total** | | | **≈ 20-30 h robot A, 15-22 h robot B** | **Robot B does not get much cheaper**, because the precision work does not benefit from a template. |

### 6.8 Subtotals

| Configuration | Per robot | **For 2 robots** |
|---|---|---|
| Belt-reduction turret (lighter duty) | ≈ **$120-$160** | **≈ $240-$320** |
| Geared turret with thrust bearing + rollers | ≈ **$150-$200** | **≈ $300-$400** |
| **Plus** 20-30 student-hours per robot, and **1 motor slot** | | **40-60 student-hours** |

### 6.9 ⚠ The honest verdict: is a turret ever worth it for a team like this?

**JUDGMENT: No — with one narrow exception.**

**The case against, for this specific program:**

1. **It costs a motor slot** you have already seen run out in §2.2. A holonomic drivetrain plus intake plus
   lift plus climb is already at 7/8.
2. **The slew bearing is not purchasable** from the FTC vendors I checked (§6.4), so the highest-precision
   sub-assembly on the robot must be **hand-fabricated twice with no mill.**
3. **20-30 student-hours per robot, and robot B saves little**, against ~3-4 hours for a virtual four-bar
   that also improves scoring.
4. **Duplicability 2.** Everything else in this catalog scores 3-5. In a workspace where duplicability is a
   first-class factor, a turret is the outlier.
5. **A holonomic drivetrain already rotates the robot.** The turret's benefit is that it aims *without*
   moving the chassis — worth real points only if the game rewards rapid multi-angle scoring from a fixed
   position, and only if the drivetrain is the bottleneck.

**The narrow exception:** if BIOBUZZ turns out to have a **long-range launching task with many target
angles** and a scoring rate high enough that chassis rotation is the limiting factor, a turret pays. Even
then: **build it on robot A only, in week 4+, after both robots are scoring.** Never build a turret on both
robots in the first six weeks.

**What to do instead:** spend the motor slot and the 25 hours on (a) making the drivetrain faster and better
controlled, (b) a virtual four-bar, and (c) reliability work on the mechanisms you already have. That is the
higher-expected-value allocation for a 15-student, two-robot, modest-budget program.

### 6.10 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Turret | **None. Rotate the robot.** | Belt-reduction turret, ±180°, service-loop cabling, magnetic home switch |
| Cost | **$0** | ≈ $160-$200 per robot |
| Slots | 0 | 1 motor |
| Hours | 0 | 20-30 per robot |
| Build on | — | **Robot A only**, week 4+ |

---

## 7. M-5 — CLIMBING / HANGING / SUSPENSION

### 7.1 What it is and when a design needs it

A climbing mechanism lifts the whole robot off the floor, usually against a field structure, usually in the
last 30 seconds. **This recurs in most FTC seasons** and is usually worth a large, discrete points bonus.

> ⚠ **V0-GAP — CONFIRMED.** BIOBUZZ V0 **Section 10 (Game Details)** and **Section 11 (Game Rules G)** are
> **placeholders**. Whether BIOBUZZ has a climb, what it attaches to, how high, and what it scores are all
> **unknown until 2026-09-12**. This section is therefore a **capability library**, not a plan. Buy nothing
> climb-specific before Kickoff; §7.7 lists what is safe to stock because it serves other mechanisms too.

### 7.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **Winch + spool + cord, hook over a bar** | 2 | **1** | 2 | 4 | **5** | **The default.** Cheapest, lightest, most forgiving. Reuses §3 hardware. |
| **Winch + ratchet / one-way bearing** | 3 | 2 | 2 | **5** | 4 | Holds the robot with **no motor current** — the reliability upgrade. **R303.H legal.** ⚠ R203 release needed. |
| **Slide-based lift (drive the slide against the field)** | 3 | 3 | 3 | 3 | 4 | Reuses the scoring lift — **zero extra motor slots** if the geometry works. Loads the slide in a direction it was not designed for; see §9.3. |
| **Gas-spring / constant-force-spring powered lift, servo-latched** | 4 | 3 | **1** | 4 | 4 | **Zero motor slots.** Energy stored pre-match, released by a servo. **R801.A legal.** One shot only. |
| **Hooked arm driven by the arm motor** | 2 | **1** | 2 | 3 | **5** | Reuses §5. Torque requirement is large — check §7.4. |
| **Rigid telescoping lift (custom)** | 5 | 4 | 4 | 3 | 2 | Decline, per §4.2. |

### 7.3 Ratchets and one-way bearings — the key legality point

**R303.H (CONFIRMED-BIOBUZZ, p. 70)** lists **"ratcheting devices (wrenches, bearings, etc.)"** as an
**explicit exception** to the single-degree-of-freedom limit on COTS mechanisms. That is a deliberate
carve-out, and it exists because ratchets are how FTC robots hold themselves up.

**Why it matters:** without a ratchet, a robot hanging at the end of a match is held by **motor holding
current** for up to 30 seconds. That drains the battery, heats the motor, and drops the robot if the code
faults or the battery sags. With a ratchet or a one-way bearing, the winch cannot pay out and the motor can
be unpowered.

> ⚠ **R203 (CONFIRMED-BIOBUZZ, p. 69) applies with full force here.** *"ROBOTS must be designed to be
> quickly removed from the FIELD without requiring power ... [and] from FIELD elements while powered off."*
> **A ratcheted robot hanging on a field element with a dead battery must still be removable by hand.**
> Build a **pawl release** — a lever or a pull-pin a volunteer can operate — and demonstrate it at
> inspection.

**⚠ SOURCING PROBLEM — VERIFIED NEGATIVE FINDING.** I loaded
<https://www.gobilda.com/bearings/> this session and the category lists **no one-way or clutch bearings**.
Neither did a web search surface an FTC-vendor one-way bearing SKU. **Consequence:** the one-way bearing must
come from a general industrial supplier (a needle-roller clutch bearing is the standard part), and any such
supplier must meet the **VENDOR** test in the manual (pp. 65-66): Federal Tax ID, not team-owned, adequate
stock, available to all teams. **McMaster-Carr and similar industrial distributors meet that test** —
`LEGAL-PARTS-CONSTRAINTS.md` §8.2 says so explicitly. **A fabricated pawl-and-ratchet-wheel is the
alternative** and is entirely legal under **R302** (raw materials may be modified) — and it is 3D-printable.

### 7.4 The load and safety reasoning — this is the one mechanism that can hurt someone

**R104 (CONFIRMED-BIOBUZZ, p. 67) states there is NO ROBOT weight limit in BIOBUZZ.** That is a trap here. Every
other mechanism in this file benefits from no weight limit; **the climber is the one that pays for it.**

**JUDGMENT — the arithmetic:** a typical FTC robot masses **10-15 kg**. Lifting it on a spool of radius
**17.8 mm** (the verified `3407-0002-0112`, 112 mm circumference) needs
15 kg × 1.78 cm ≈ **27 kg·cm** at the spool in the ideal case — and climbs are never ideal, because the cord
angle is rarely vertical and the robot swings. **Apply 2.5-3×: budget 65-80 kg·cm.**

Against the **VERIFIED** Yellow Jacket table (§3.6): **71.2:1 gives 93.6 kg·cm** and **99.5:1 gives
133.2 kg·cm**. A **single 5203 at 99.5:1 or 71.2:1** does it with margin. Two motors at a lower ratio is
faster but costs a second slot.

**Safety and structural implications — read this before building:**

| Risk | Why | Mitigation |
|---|---|---|
| **The cord is now a life-safety-adjacent part** | A snapped cord drops 10-15 kg from height, in a pit or on a field, next to students | **Use `REV-41-1162` (1.2 mm, 300 lb+) or `REV-29-1244` (3 mm, 1500 lb+)** — both VERIFIED, see below. Inspect before every match. **Replace on a schedule, not on failure.** |
| **The mounting point tears out of the chassis** | The entire robot mass is now carried by a few M4 screws into thin channel | **Spread the load** — through-bolt to a plate, not into a single channel wall. See §9.3. |
| **The robot swings and hits something** | Pendulum motion under a single hook | Two hooks, or a hook plus a stabiliser against the structure |
| **Stored spring energy releases unexpectedly** | A pre-charged gas spring or constant-force spring is dangerous in the pit | **Mechanical safety pin** during transport and pit work. Brief the students. |
| **Fingers in the mechanism** | Ratchets and winches pinch | Guard the pinch points; **R202** requires the design not *"cause an unsafe condition."* |
| **Robot cannot be lowered at field reset** | Ratchet with no release | **R203.** Pawl release lever. |

#### 7.4.1 ✅ RESOLVED — which cord to hang the robot on (VERIFIED 2026-08-22)

An earlier revision of this file flagged "cord breaking strength unverified" as its largest safety gap.
**It is now closed**, from the [REV UHMWPE Cords category page](https://www.revrobotics.com/UHMWPE-Cords/):

| Part | Dia. | Length | Load rating | Price | Margin on a 15 kg (33 lb) robot |
|---|---|---|---|---|---|
| `REV-41-1162` | 1.2 mm | 10 m | **300 lb+** | **$7.75** | **~9:1 static**, ~3:1 after a 3× dynamic factor |
| `REV-29-1244` | 3 mm | 10 m | **1500 lb+** | **$13.50** | **~45:1 static**, ~15:1 dynamic |

**JUDGMENT — the recommendation:** use **`REV-29-1244` (3 mm, 1500 lb+) for any mechanism that lifts the
whole robot.** The price difference is **$5.75**. There is no defensible reason to economise on the single
part whose failure drops the robot. Reserve the 1.2 mm `REV-41-1162` for **slide rigging**, where its
smaller bend radius and lower mass are advantages and the load is a few kilograms.

⚠ **Note the trade-off, honestly:** a 3 mm cord needs a **proportionally larger spool and turn-point radius**
than 1.2 mm. Check that `3407-0002-0112`'s groove accepts 3 mm before committing — **NEEDS-SKU-CHECK**, the
groove width is not stated on the goBILDA page. If it does not, spool the 3 mm cord on a printed drum (§7.8).

⚠ **Still open:** the **goBILDA `2908-0100-0005`** synthetic cable has **no published breaking strength**.
It remains fine for slide rigging. **Do not use it for a climb** — use the REV cord, which has a number.

### 7.5 The zero-motor-slot climb (JUDGMENT — the best idea in this section)

If BIOBUZZ has a climb and your motor budget is full at 8, this is the escape:

1. **Store the energy before the match** in a constant-force spring or a gas spring, compressed/extended as
   part of the STARTING CONFIGURATION. **This is legal:** R801.A permits *"sealed, COTS closed-air systems
   which are pre-charged by the manufacturer (such as gas shocks)"*, and the blue box explicitly names
   *"gas springs, and dampers."* Ordinary mechanical springs are not restricted at all.
2. **Hold it with a mechanical latch**, released by **one servo** (R506 forbids solenoids and
   electromagnets, so a servo it is).
3. **Ratchet the result** so the robot stays up (R303.H).
4. **Cost: 0 motors, 1 servo.**

**Caveats, honestly:** it is one-shot (no re-try in the match), the spring must be re-set between matches
(add it to the pit checklist), and **R103** requires the stored-energy configuration to be stationary and
self-contained at MATCH start — which it is, but an inspector will look at it. Also see the safety-pin row
in §7.4.

### 7.6 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Winch pulley, dual spool, hub-mount** | goBILDA | `3407-0002-0112` | 1 | 2 | **$6.99 ea** | Buy | **VERIFIED** — [cable & pulleys](https://www.gobilda.com/cable-pulleys) | 112 mm circumference. **Same part as the slide spool** — good stocking overlap. |
| Winch pulley, servo-mount | goBILDA | `3410-0025-0112` | 0-1 | 0-2 | **$8.99 ea** | Buy | **VERIFIED** | For a servo-driven latch or a very light lift. |
| **Winch cord — RECOMMENDED** | REV Robotics | `REV-29-1244` UHMWPE Cord, **3 mm × 10 m** | 1 | 2 | **$13.50 ea** | **Buy** | **VERIFIED 2026-08-22** — [UHMWPE Cords](https://www.revrobotics.com/UHMWPE-Cords/) | **1500 lb+ rating — ~45:1 margin on a 15 kg robot.** This is the correct part for hanging the robot. See §7.4.1. Check spool groove width accepts 3 mm. |
| Winch cord — lighter alternative | REV Robotics | `REV-41-1162` UHMWPE Cord, **1.2 mm × 10 m** | 0-1 | 0-2 | **$7.75 ea** | Buy | **VERIFIED 2026-08-22** — same page | **300 lb+ rating**, ~9:1 static margin. Acceptable if the spool cannot take 3 mm. Smaller bend radius. |
| ~~Winch cord~~ | goBILDA | `2908-0100-0005` Synthetic Cable, 1 mm, 5 m | — | — | $3.49 ea | **NOT for climbing** | **VERIFIED (price)** | ⚠ **No published breaking strength.** Fine for slide rigging (§3.5.3); **do not hang the robot on an unrated cord.** |
| **Climb motor** | goBILDA | **5203 Series** @ **71.2:1** or **99.5:1** | 1-2 | 2-4 | **$54.99 ea** | Buy | **VERIFIED** — [category](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | Torque reasoning in §7.4. Legal per Table 12-1. |
| Worm gear set (self-locking climb) | goBILDA | `3204-0001-0002` (28:1, 8 mm REX) | 0-1 | 0-2 | **$34.99 ea** | Buy | **VERIFIED** — [worm gears](https://www.gobilda.com/worm-gears/) | Alternative to a ratchet: the worm holds the load. ⚠ **R203 manual release still required.** |
| **One-way / clutch bearing** | General industrial supplier (must meet the **VENDOR** test, manual pp. 65-66) | Needle-roller clutch bearing family | 1 | 2 | not verified | Buy | **UNVERIFIED** | ⚠ **Not stocked by goBILDA** (bearings category checked this session) or found at any FTC vendor. **Do not order on this row.** Legal under **R303.H**. |
| **Gas spring / gas shock** | General supplier (VENDOR test) | Gas spring family, specified by **force rating + stroke** | 1-2 | 2-4 | not verified | Buy | **FAMILY-ONLY** | ⚠ **R801.A legal** — must be *pre-charged and sealed by the manufacturer*. McMaster-Carr page would not yield product detail to WebFetch this session; **family named only.** **Buy 4 identical units so both robots match.** |
| **Constant-force spring** | General supplier (VENDOR test) | Constant-force spring family | 1-2 | 2-4 | not verified | Buy | **FAMILY-ONLY** | Legal (an ordinary spring, not an air device). Specify by force and extended length. |
| Shock / damper (controlled descent, anti-slam) | goBILDA | `2900-0190-0001` Big Bore Shock (190 mm, 2-pack) | 0-1 pack | 0-2 packs | **$39.99 / 2-pack** | Buy | **VERIFIED** — [shocks](https://www.gobilda.com/shocks) | ⚠ **The page does not state these are gas shocks**, nor give force ratings. Treat as **dampers** — explicitly legal per the R801 blue box. |
| Shock, smaller | goBILDA | `2900-0120-0001` (2-pack) | 0-1 pack | 0-2 packs | **$19.99 / 2-pack** | Buy | **VERIFIED** | |
| Shock mounts | goBILDA | `2901-0001-0001` (2-pack) | 1 pack | 2 packs | **$3.99 / 2-pack** | Buy | **VERIFIED** | |
| **Climb-complete limit switch** | REV Robotics | `REV-31-1425` touch ($8.75) or `REV-31-1462` magnetic ($17.50) | 1 | 2 | **$8.75 / $17.50** | Buy | **VERIFIED** — [sensors](https://www.revrobotics.com/ftc/electronics/sensors/) | Stops the winch at full climb so it does not stall against the structure. |
| Cord guide | goBILDA | `2926-0204-1000` PTFE Tubing (1 m) | 1 | 2 | **$5.99 ea** | Buy | **VERIFIED** | |
| Latch servo | goBILDA / REV | Must pass **R502 / Table 12-2** | 1 | 2 | see `LEGAL-PARTS-CONSTRAINTS.md` §4.5 | Buy | **cross-ref** | For the spring-powered variant (§7.5). |

### 7.7 What is safe to stock BEFORE Kickoff

**JUDGMENT.** Because the endgame is unknown, buy only parts that serve a second purpose:

| Part | Also used for | Safe to buy now? |
|---|---|---|
| `2908-0100-0005` cord | Slide rigging (§3) — **slides only, not climbing** | **Yes — stock 4.** |
| `REV-41-1162` 1.2 mm cord (300 lb+) | Slide rigging **and** light climb (§3, §7) | **Yes — stock 2.** 10 m for $7.75 is the best cord value verified in this file. |
| `REV-29-1244` 3 mm cord (1500 lb+) | Climb only | **Yes — stock 1-2 anyway.** $13.50, never expires, and it is the part you must not improvise on the week of an event. |
| `3407-0002-0112` dual spool | Slide spool (§3) | **Yes — stock 2-4.** |
| `2926-0204-1000` PTFE tubing | Slide cord guides (§3) | **Yes — stock 2.** |
| `REV-31-1425` touch sensors | Arm/slide homing (§5) | **Yes — stock 4.** |
| 5203 motors | Everything | **Yes** — but see the ratio caveat in §1.2. |
| Gas springs, constant-force springs | Arm gravity assist (§8) | **Only if you know the force you need.** Otherwise wait. |
| One-way bearings, ratchets | Climb only | **No — wait for Kickoff.** |
| Hooks, latches, structure | Climb only | **No — wait.** Geometry is entirely game-dependent. |

### 7.8 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Tooling | Material | Student-hours per robot | Notes |
|---|---|---|---|---|
| **Hook / gripper that engages the field structure** | 3D printer, then likely aluminium | PETG for v1, **aluminium for the final** | **4-8 h** | ⚠ **A printed hook carrying 15 kg is a bad idea.** Prototype printed, make the final from metal or reinforce heavily. **R201:** it must not damage the field element. |
| **Load-spreading mounting plate** | Hand-cut aluminium + drill press | 1/8 in. aluminium | **3-4 h** | **The most important fabricated part in this section.** See §9.3. |
| Ratchet pawl + wheel (if not buying a one-way bearing) | 3D printer | PETG (pawl), consider metal wheel | **4-6 h** | Legal under R302. Iterate the tooth profile. |
| **Pawl / ratchet manual release lever** | 3D printer + hand tools | PETG + pin | **2-3 h** | **R203 compliance. Mandatory if you ratchet.** |
| Spring retention + safety pin (spring variant) | 3D printer + hand tools | PETG + steel pin | 3 h | **Safety-critical.** |
| Cord routing and anchor | Drill, hand tools | — | 2 h | |
| Stabiliser / anti-swing feature | 3D printer / channel | PETG / aluminium | 2-4 h | |
| **Total** | | | **≈ 17-27 h robot A, 10-17 h robot B** | |

### 7.9 Subtotals

| Configuration | Per robot | **For 2 robots** |
|---|---|---|
| **Simple winch climb** (spool + cord + 5203 @ 99.5:1 + limit switch + fabricated hook) | $6.99 + $3.49 + $54.99 + $8.75 + ≈$25 ≈ **$100** | **≈ $200** |
| Winch + ratchet (one-way bearing unverified; fabricated pawl assumed) | ≈ **$110-$130** | **≈ $220-$260** |
| Worm-drive self-locking climb | above + $34.99 ≈ **$140** | **≈ $280** |
| **Spring-powered, servo-latched (0 motor slots)** | spring (unverified) + servo + ≈$30 fabrication ≈ **$80-$140** | **≈ $160-$280** |
| Slide-based climb (reuses the §3 lift) | **≈ $30** (hook + reinforcement only) | **≈ $60** |

*Ranges reflect unverified spring and one-way-bearing pricing. **VERIFY-BEFORE-ORDER.***

### 7.10 Common failure modes and spares

| Failure | Cause | Prevention | Spare (2 robots) |
|---|---|---|---|
| **Cord snaps under full robot weight** | Under-rated cord, abrasion, or a sharp bend | **Use rated cord (§7.4.1)**; PTFE guides; **scheduled replacement** | **2× `REV-29-1244`** ($13.50 ea, 1500 lb+) — do **not** substitute the unrated `2908-0100-0005` here |
| **Mounting point tears out** | Load into a single channel wall | Load-spreading plate, through-bolted | — (design) |
| **Printed hook fails** | PETG at 15 kg in bending | **Metal final part** | 2× spare hooks |
| **Robot slips off the structure** | Hook geometry, or swing | Two contact points; stabiliser | — |
| **Robot drops when the code faults** | Held by motor current only | **Ratchet or worm** | — |
| **Winch stalls at top and browns out the hub** | No limit switch | `REV-31-1425` / `REV-31-1462` | 2× |
| **Cannot be removed at field reset** | Ratchet/worm with no release | **R203 release lever** | — |
| **Spring releases in the pit** | No safety pin | **Safety pin + student briefing** | — |

### 7.11 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Mechanism | **Winch + cord + hook**, 1× 5203 @ 99.5:1, limit switch | Winch + **ratchet**, two-point engagement, stabiliser, damped final approach |
| Or | **Reuse the scoring slide** to push against the structure — $30 and 0 extra slots | Spring-powered servo-latched climb — 0 motor slots |
| Holding | Motor current (acceptable for 30 s) | Ratchet or worm, motor unpowered |
| Hook | Printed prototype → aluminium final | Aluminium, two points |
| Cost per robot | **≈ $30-$100** | **≈ $130-$200** |
| Hours | 17-27 h robot A | 30-40 h robot A |
| **Duplicability** | **5** | **4** |

---

## 8. Energy storage and springs — the zero-slot actuator

### 8.1 What is legal (CONFIRMED-BIOBUZZ)

| Device | Legal? | Rule | Note |
|---|---|---|---|
| **Ordinary springs** — extension, compression, torsion | **Yes** | Not restricted by any R-rule; **R302** names *"rubber"* among modifiable raw materials | Unlimited use. Not actuators; cost **zero** R503 slots. |
| **Constant-force springs** | **Yes** | Same | The best assist device for a slide, because force is constant through the stroke. |
| **Surgical tubing / elastic** | **Yes** | Same | ⚠ gm0 advises against it for slide retraction — *"not recommended"*, jerky and slow. Fine as an assist. |
| **Gas springs / gas shocks** | **Yes, conditionally** | **R801.A** — *"sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)"* | Must be **pre-charged and sealed by the manufacturer.** You may not charge it, adjust it, or open it. |
| **Dampers** | **Yes** | R801 blue box — *"This includes items such as gas springs, and dampers."* | goBILDA `2900-` series shocks (§7.6). |
| **Magnets** (detent, passive latch) | **Yes** | **R302** names **magnets** as an allowed raw material | Zero-slot latching and alignment. Underused. |
| **Pneumatic cylinders** | **NO** | **R801** + blue box: *"robots may not use pneumatic actuators"* | Entire aisle is off the table. |
| **Compressors, air tanks, vacuum** | **NO** | **R801.B, C, D** | |
| **Solenoid / electromagnetic latches** | **NO** | **R506** — *"Relays, electromagnets and electrical solenoid actuators are prohibited"* | **Every latch release must be a servo or mechanical.** |
| User-adjustable gas vessels | **NO** (except air-filled COTS wheels) | **R801.D** | |

### 8.2 How teams actually use assist springs

| Application | Spring type | Sizing rule of thumb (JUDGMENT) | Slot cost |
|---|---|---|---|
| **Arm gravity compensation** | Extension spring or gas spring across the pivot | Size to cancel roughly **60-80%** of the horizontal-position holding torque — not 100%, or the arm becomes unstable and hard to drive down | **0** |
| **Vertical slide assist** | **Constant-force spring** | Cancel the *static* weight of the stack + payload; the motor then only accelerates it | **0** |
| **Horizontal slide retraction** | Constant-force spring, or cascade retraction cord | ⚠ gm0 prefers the cord; a spring *"decreases extension speed considerably"* | **0** |
| **Deploy a mechanism out of the 18 in. cube at match start** | Torsion spring or gas spring, servo-latched | The classic zero-slot deployment. **R102** requires it to be *stationary* in STARTING CONFIGURATION — a latched spring is stationary | **0 motors, 1 servo** |
| **Climb** | Constant-force or gas spring, servo-latched | §7.5 | **0 motors, 1 servo** |
| **End-effector return-to-home** | Light extension spring | Lets a single-acting servo do a two-way job | **0** |

**The design principle worth internalising (JUDGMENT):** in a season limited to **8 motors and 8 servos**,
every newton of force a spring provides is a newton you do not have to buy an actuator slot for. Springs are
also **cheap to duplicate** — buy four identical ones and both robots behave the same. **Duplicability 5.**

### 8.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Gas spring / gas shock** | General supplier meeting the **VENDOR** test (manual pp. 65-66) | Gas spring family — specify **force (N) + stroke (mm)** | 1-2 | **4 identical** | not verified | Buy | **FAMILY-ONLY** | **R801.A: must be pre-charged and sealed by the manufacturer.** McMaster-Carr would not return product detail to WebFetch this session — **I am naming the family only.** Flagged in §13. |
| **Constant-force spring** | General supplier (VENDOR test) | Constant-force spring family — specify **force + extended length** | 1-2 | **4 identical** | not verified | Buy | **FAMILY-ONLY** | Ordinary spring; no R801 conditions. |
| **Damper / shock** | goBILDA | `2900-0190-0001` Big Bore Shock (190 mm, 2-pack) | 0-1 pack | 1-2 packs | **$39.99 / 2-pack** | Buy | **VERIFIED** — [shocks](https://www.gobilda.com/shocks) | ⚠ Page does **not** state gas-charged, and gives **no** spring rate or force rating. Legal as a **damper** per the R801 blue box. |
| Damper, smaller | goBILDA | `2900-0120-0001` (2-pack) | 0-1 pack | 1-2 packs | **$19.99 / 2-pack** | Buy | **VERIFIED** | |
| Shock mounts | goBILDA | `2901-0001-0001` (2-pack) | 1 pack | 2 packs | **$3.99 / 2-pack** | Buy | **VERIFIED** | |
| Extension / compression / torsion springs | General hardware supplier (VENDOR test) | Assorted spring kit | 1 kit | 1-2 kits (share) | not verified | Buy | **UNVERIFIED** | An assortment kit is the cheap way to find the right rate empirically. |
| Surgical tubing / latex | General supplier | Tubing by ID/OD | 1 | 2 | not verified | Buy | **UNVERIFIED** | |
| Magnets (detent / passive latch) | goBILDA / general | — | as needed | ×2 | not verified | Buy | **UNVERIFIED** | **Explicitly legal raw material under R302.** |

**⚠ Honest disclosure:** every spring row above is FAMILY-ONLY or UNVERIFIED. I could not load a supplier
product page for gas springs or constant-force springs in this session (McMaster-Carr returned only its
category shell to WebFetch). **Name the family, specify force and stroke, and verify on the vendor site
before ordering.** This is the largest verification gap in this file and it is recorded in §13.

### 8.4 FABRICATE / ASSEMBLE IN-HOUSE

| Part | Tooling | Material | Student-hours per robot | Notes |
|---|---|---|---|---|
| Spring anchor points | 3D printer + drill | PETG + eyebolts / shoulder bolts | **2-3 h** | Make the anchor **adjustable** — you will re-tune the assist force by moving the anchor, not by buying a new spring. |
| Servo latch mechanism | 3D printer | PETG | **3-5 h** | Must hold reliably and release under load. Over-centre geometry helps. |
| **Safety pin / transport lock** | 3D printer + steel pin | PETG + pin | **1-2 h** | **Safety-critical for any pre-charged spring.** |
| Spring guard | 3D printer | PETG | 1 h | **R202** — the design must not *"cause an unsafe condition."* |
| **Total** | | | **≈ 7-11 h robot A** | |

### 8.5 Subtotal

| Configuration | Per robot | **For 2 robots** |
|---|---|---|
| Arm assist spring + adjustable anchors | ≈ **$20-$50** (spring cost unverified) | **≈ $40-$100** |
| Servo-latched spring deployment | ≈ **$40-$80** + 1 servo | **≈ $80-$160** |
| Damped mechanism (goBILDA shocks) | **$19.99-$39.99** per 2-pack + $3.99 mounts | **1-2 packs serve both robots** |

### 8.6 Failure modes and spares

| Failure | Cause | Prevention | Spare |
|---|---|---|---|
| Spring fatigues, assist force drops | Cycled thousands of times | Buy 4 identical, rotate; check assist force at each event | 2× spare springs |
| Gas spring loses charge | Seal failure — and **you may not re-charge it (R801)** | Replace, do not repair | 2× spare |
| Latch releases early | Insufficient over-centre, or servo torque marginal | Over-centre geometry; test at full load | — |
| Latch does not release | Binding under load | Test **at load**, not on the bench unloaded | — |
| Spring anchor tears out of a printed part | PETG in tension at a bolt hole | Metal insert or a through-bolt with a washer | — |
| **Injury in the pit** | Unpinned stored energy | **Safety pin, always, and brief the students** | — |

### 8.7 Rookie-friendly minimum vs competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Use | **One assist spring on the arm.** Adjustable anchor, tuned empirically. | Constant-force spring on the slide + gas-spring-assisted deploy + damper on the fast return |
| Cost | ≈ $20-$50 | ≈ $100-$180 |
| Slots saved | Makes an existing motor adequate | **Can save an entire motor slot** |
| **Duplicability** | **5** — buy 4 identical | **5** |

---

## 9. Structural loading — where these mechanisms actually fail

**R104 says there is NO weight limit in BIOBUZZ (CONFIRMED-BIOBUZZ, p. 67).** That removes the usual incentive to
under-build. **Use it.** For this team, the cheapest reliability upgrade available is *more material at the
load path*, and it costs nothing but a gram budget you no longer have.

### 9.1 The five load paths that break

| # | Load path | Failure | Reinforcement |
|---|---|---|---|
| **1** | **Slide rails to chassis** | Rails go out of parallel; slide binds and the motor stalls | **Mount both rails to ONE rigid plate**, then the plate to the chassis. Never mount rail A to member A and rail B to member B. |
| **2** | **Arm pivot** | Shaft bends, arm goes out of plane, gears mesh badly | **Two pillow blocks, one per side.** A cantilevered single-sided pivot is the most common arm failure in FTC. |
| **3** | **Climb mounting point** | Screws pull through channel wall; whole mechanism tears out | **Load-spreading plate through-bolted** across multiple channel holes, with washers. See §9.3. |
| **4** | **Turret race** | Deck tips under the overturning moment; gear mesh opens up | **Three guide rollers at 120°**, preloaded, plus a thrust bearing for the axial load. |
| **5** | **End-effector mount at full extension** | Printed bracket cracks at the bolt holes | **Metal inserts or through-bolts with washers**; never a bolt directly into thin printed material in tension. |

### 9.2 The arm pivot rule, stated once

**A pivot supported on one side is a cantilever.** The bending moment at the bearing equals the full load
times the full arm length, and it is carried by a single bearing and a short length of shaft. **Supported on
both sides, the same load becomes a simply-supported beam and the bearing loads roughly halve** — while the
shaft's bending stress drops dramatically. Two `1602`/`1605`/`1606`-series pillow blocks cost ~$12-$30 for
the pair (series ranges **VERIFIED** at <https://www.gobilda.com/bearings/>). **It is the best structural
money in this file.**

### 9.3 The climb mounting rule, stated once

When the robot hangs, **the entire robot mass passes through the mechanism's attachment to the chassis.**
An M4 screw into the 1.5-2 mm wall of an aluminium channel is loaded in a way it was never intended for, and
the failure mode is the screw head pulling through the wall.

**Fix (JUDGMENT):** a **1/8 in. aluminium plate** spanning at least **four** channel holes, through-bolted
with washers on both sides, with the winch and hook loads introduced into the plate — not into the channel.
3-4 student-hours, hand tools only, and it converts the single most catastrophic failure in this file into
a non-event.

### 9.4 Material choices for printed parts

**JUDGMENT — the team has 3D printers, so this matters:**

| Material | Use for | Avoid for |
|---|---|---|
| **PETG** | **Default for structural prints.** Tougher than PLA, less brittle, acceptable heat resistance | Anything at high sustained load |
| **ABS / ASA** | Higher-temperature parts near motors | Parts needing dimensional precision (warps) |
| **PLA** | **Prototypes and jigs only** | ⚠ **Any load-bearing or heat-exposed part.** PLA creeps under sustained load and softens in a hot gym. A PLA arm bracket will deform over a season. |
| **Nylon / CF-nylon** | Gears, wear surfaces, high-load brackets | Cost and print difficulty |
| **Aluminium (hand-cut)** | Climb hooks, load-spreading plates, pivot plates | Anything needing a complex 3D form |

**Rule: any part in the load path of the climb, or carrying the robot's weight, should be metal.**

### 9.5 The failure everyone forgets: cable management

Every mechanism in this file moves, and every moving mechanism carries wires. **JUDGMENT, from the shape of
the problem rather than from any rule:**

- Wires that flex over an edge **will** chafe through. Spiral wrap or a printed drag chain at every flex
  point.
- Leave a **service loop** — enough slack for the full range of motion in both directions, plus 20%.
- A slide's carriage wiring must tolerate the **full extended length**, not the retracted length.
- **R610** wire colours and **R609** wire sizing (Table 12-8) still apply to every wire crossing a joint —
  see `LEGAL-PARTS-CONSTRAINTS.md` §6.7-6.8.
- Budget **2-4 student-hours per mechanism** for cable management. It is always underestimated and it is a
  frequent cause of mid-competition failure.

---

## 10. The two-robot duplicability ledger

Everything below is **JUDGMENT**, calibrated to ~15 students across two teams.

### 10.1 Duplicability scores, all mechanisms in this file

| Mechanism | **Duplicability** | Why |
|---|---|---|
| Viper-Slide kit lift | **5** | Re-order the same SKU. Identical geometry guaranteed. |
| Virtual four-bar | **5** | Two pulleys and a belt. Trivially repeatable. |
| Servo arm | **5** | |
| Simple winch climb | **5** | |
| Assist springs | **5** | Buy 4 identical. |
| Motor + planetary arm | **5** | All COTS; the only fabricated parts are printed. |
| Worm-drive arm | **4** | Adds an alignment step. |
| Cord-rigged slide | **4** | Rigging must be tensioned identically twice. |
| REV extrusion slide | **4** | Cheap, but cutting and squaring extrusion twice adds variance. |
| Rack and pinion | **4** | Centre distance must be set twice. |
| True four-bar | **4** | Link lengths must match across 8 links. |
| Elevator on a belt | **4** | |
| Pivot extension | **3** | Two mechanisms to duplicate, and their interaction. |
| MiSUMi slide | **3** | Separate vendor, separate lead time. |
| **Turret** | **2** | Hand-fabricated precision race, twice, no mill. |
| Telescoping tubes | **2** | |
| DRFB | **2** | |
| **Scissor lift** | **1** | 8-16 matched links, ×2. |

### 10.2 The four rules for building two of everything

1. **Buy the kit, not the parts, wherever a kit exists.** The $159.99 Viper-Slide kit is not just
   convenience — it is a **guarantee that robot A and robot B have identical geometry**, which is what makes
   one set of code, one set of spares and one set of student expertise work for both.
2. **Order both robots' parts in the same order.** Same batch, same tolerances, same stock status. Avoids
   the "robot B's slide arrived from a different production run" problem, and avoids a second shipping
   charge. See `VENDOR-ECOSYSTEMS.md` §5.6.
3. **Document robot A as you build it.** The 30-40% time saving on robot B in every table above is
   *conditional* on that documentation existing. Undocumented, robot B costs the same as robot A.
4. **Never run two different designs for the same function.** Two lift designs means two spare kits, two code
   paths, and half the students understanding each. If robot B must be simpler, make it the **rookie-minimum
   version of the same design**, not a different design.

### 10.3 Shared vs per-robot purchases

| Buy **once**, share between robots | Buy **twice**, one per robot |
|---|---|
| Timing belt & pulley starter pack ($239.99 / $209.99) | Slide kit, motors, bearings, spool, cord |
| Spare 5203 motor ($54.99) | Every actuator in the running design |
| Spring assortment kits | Springs actually installed (buy 4, install 2 per robot) |
| Tooling, hex drivers, tension gauges | Limit switches, sensors |
| Damper 2-packs (`2900-` series) | |

---

## 11. Kickoff-day decision tree

**2026-09-12.** Section 12 is already final; only the game is new. Work this order.

### 11.1 What to build BEFORE Kickoff (legal under R304)

**R304 (CONFIRMED-BIOBUZZ, p. 71):** *"Custom software, designs, and parts can be reused year-to-year.
ROBOT software, designs, and FABRICATED ITEMS created before Kickoff are permitted."* **No conditions.**
Combined with the final Section 12 and the known **18 in. cube (R102)**, all of the following are safe today:

| Build now | Why it is safe | Still must satisfy |
|---|---|---|
| A **2-stage Viper-Slide test rig** on a bench frame, fully rigged and driven | Slide kit is legal COTS (R303.A); the rig is a FABRICATED ITEM created pre-Kickoff | R303, R501, R503 |
| An **arm + virtual four-bar prototype** at representative length | Same | R502/R503 |
| **PID / motion-profile code** for a slide and an arm | R304 names software explicitly | — |
| **A load-spreading climb mounting plate pattern** for your chassis | Generic structure | R302 |
| **Cable-management practice** on a moving mechanism | — | R609, R610 |
| **Teaching students to rig a continuous slide** | The single highest-value pre-Kickoff skill transfer | — |

**JUDGMENT: the highest-value use of the next 21 days is a rigged, driven, instrumented 2-stage slide on a
bench, and two students who can rig one from memory.** That skill transfers to whatever BIOBUZZ turns out to
be, and it is the long pole in every design in this file.

### 11.2 The Kickoff-day sequence

1. **Read R105's released sizing constraints first.** Everything about stage count, arm length and reach
   depends on it. Until you have it, do not order slides beyond the 2-stage kit.
2. **Determine whether there is an endgame climb.** If yes, read what it attaches to before designing a hook.
3. **Count the motor and servo budget for the whole robot** (§2.2 template) **before** choosing mechanisms.
   If the total exceeds 8+8, cut now, not in week 5.
4. **Pick extension type** using this test:
   - Reach ≤ 16 in. and the path may be an arc → **arm** (§5)
   - Reach > 16 in., or the path must be straight → **slide** (§3)
   - Both axes needed and the budget allows 2 motor slots → **pivot extension**
   - End effector must stay level → **add a virtual four-bar** (§4.2), always
5. **Size the motor** from §3.6 / §5.3 against measured load, not guessed load.
6. **Ask the zero-slot question for every function:** can a spring, a ratchet, a magnet, or a virtual
   four-bar do this instead of an actuator? (§2.3, §8)
7. **Order for both robots in one order.** (§10.2)
8. **Apply the turret test:** unless the game rewards rapid multi-angle scoring from a fixed position **and**
   both robots are already scoring, the answer is no. (§6.9)

### 11.3 The pre-Kickoff standing order for this section

Safe to buy now, serves any game, for **two robots**:

| Item | SKU | Qty (2 robots) | Cost | Confidence |
|---|---|---|---|---|
| 2 Stage Viper-Slide Kit | `3210-0003-0002` | 2 | **$319.98** | **VERIFIED** |
| 5203 Yellow Jacket motors (ratio TBD at Kickoff) | `5203-2402-[ratio]` | 2-4 | **$109.98-$219.96** | **VERIFIED** |
| Synthetic Cable 1 mm / 5 m (**slide rigging only**) | `2908-0100-0005` | 4 | **$13.96** | **VERIFIED** |
| **UHMWPE Cord 1.2 mm / 10 m (300 lb+)** | `REV-41-1162` | 2 | **$15.50** | **VERIFIED** |
| **UHMWPE Cord 3 mm / 10 m (1500 lb+) — the climb cord** | `REV-29-1244` | 2 | **$27.00** | **VERIFIED** |
| Dual-spool winch pulley | `3407-0002-0112` | 4 | **$27.96** | **VERIFIED** |
| Viper-Slide End-Stops (6-pack) | `2501-0001-0001` | 2 | **$11.98** | **VERIFIED** |
| Viper-Slide Pulley Brackets (4-pack) | `2501-0001-0002` | 2 | **$17.98** | **VERIFIED** |
| PTFE cord guide tubing | `2926-0204-1000` | 2 | **$11.98** | **VERIFIED** |
| REV Touch Sensors | `REV-31-1425` | 4 | **$35.00** | **VERIFIED** |
| Spare Steel Viper-Slide 336 mm | `2500-0014-0336` | 2 | **$39.98** | **VERIFIED** |
| **Subtotal** | | | **≈ $631-$741** | list price, before the goBILDA 25% team discount |

**Hold until Kickoff:** additional slide stages, worm gear sets, climb-specific *geometry* (hooks, latches),
one-way bearings, springs (until the force is known), turret parts (probably forever).

> **Why the two REV cords are on the pre-Kickoff list even though the endgame is unknown.** $42.50 buys the
> one part category whose failure is both **dangerous and schedule-destroying**, it never expires, and it is
> useful for slide rigging regardless of whether BIOBUZZ has a climb at all. Cord is the cheapest insurance
> in this document. **Hooks and latches, by contrast, are pure game geometry — buy nothing there until
> 2026-09-12.**

---

## 12. Verification log

**Session date: 2026-08-22.** Everything tagged **VERIFIED** in this file traces to a page below, loaded
with WebFetch in this session. Anything not on this list was not read by me.

> ### 12.0 Re-verification pass — 2026-08-22 (second pass)
>
> This file was re-opened and audited rather than rewritten. **What the audit changed:**
>
> | # | Finding | Action taken |
> |---|---|---|
> | 1 | **`REV-41-1162` UHMWPE cord fully specified.** The [UHMWPE Cords category](https://www.revrobotics.com/UHMWPE-Cords/) loaded: **1.2 mm × 10 m, 300 lb+, $7.75**. A second SKU **`REV-29-1244` (3 mm × 10 m, 1500 lb+, $13.50)** was discovered. | Row upgraded **FAMILY-ONLY → VERIFIED**; new §7.4.1 added; **open questions #3 and #4 closed.** The old "$7.75-$13.50 family range" was in fact the *range across these two SKUs* — now stated exactly. |
> | 2 | **`3210-0002-0002` cable-driven Viper-Slide kit is DISCONTINUED / SOLD OUT** ($129.99). | Added as a struck-through DO-NOT-SPEC row plus a ⚠ callout in §3.5.1. **This invalidates prior-season advice to "buy the cable kit"** and is the most schedule-relevant change in this pass. |
> | 3 | **`3429-0002-0002` Belt-Drive Upgrade Pack, $79.99** exists for legacy cable kits. | Added — relevant only if a kit is already on the shelf. |
> | 4 | **REV cascade lift companion BOM recovered** from the `REV-45-1507` page: `REV-45-1831` hardware pack (**$7.75, VERIFIED**), `REV-41-1432` extrusion, `REV-41-1368` pulley bearings, `REV-41-1163` surgical tubing (**$7.75, VERIFIED**), `REV-41-1360` bolts, `REV-41-1300`/`REV-41-1301` motors. | §3.5.4 expanded; true entry price corrected from $14.75 to **$22.50**; part of open question #15 closed. |
> | 5 | **Prices spot-re-checked and CONFIRMED UNCHANGED:** `3210-0003-0002` $159.99 (In Stock, 384/874 mm), `3210-0003-0004` $229.99 (In Stock, 384/1360 mm), `REV-45-1507` $14.75 (In Stock). | No edit needed. A web-search snippet claiming `3210-0003-0002` was "$125.00" was **rejected** — it was a reseller listing; goBILDA's own page says $159.99. |
> | 6 | **All 29 R-rule IDs cited in this file exist in the V0 Section 12 text**, and R203, R303 (A-G, H-L), R304, R501/R503 and R801 (A-E) were re-read **verbatim** and match their use here. | No corrections required. R304 confirmed as *"FABRICATED ITEMS created before Kickoff are permitted"*, which is the basis of §11.1. |
> | 7 | **§6.4 turret negative finding re-tested** with a fresh search — still no FTC-vendor slew bearing/turntable. | Negative finding **stands**; §6.9 verdict unchanged. |

**goBILDA (general supplier):**
`/linear-slides/` · `/cable-pulleys` · `/shocks` · `/lead-screws` · `/gears` · `/worm-gears/` ·
`/hub-mount-gears/` · `/gear-racks/` · `/bearings/` · `/motion/` · `/timing-belts-pulleys/` ·
`/linear-motion-guides` · `/yellow-jacket-planetary-gear-motors/` ·
`/2-stage-viper-slide-kit-belt-driven-336mm-slides/`
*Added in the second pass:* `/4-stage-viper-slide-kit-belt-driven-336mm-slides/` ·
`/2-stage-viper-slide-kit-cable-driven-336mm-slides/` (**discontinued**) ·
`/belt-drive-upgrade-pack-for-3210-0002-0002-cable-driven-2-stage-viper-slide-kit/`

**REV Robotics (general supplier):**
`/ftc/motion/` · `/rev-45-1507/` · `/rev-41-1600/` · `/ftc/electronics/sensors/`
*Added in the second pass:* `/UHMWPE-Cords/` · `/rev-41-1163/`

**ServoCity:** `/structure/`

**Community reference (gm0 — Game Manual 0):**
`/docs/common-mechanisms/linear-motion-guide/index.html` · `/rigging.html` · `/drawer-slides.html` ·
`/extrusion-slides.html` · `/docs/common-mechanisms/linkages.html` · `/docs/common-mechanisms/arms.html`

**Manual source grepped this session:**
`manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` — **R102, R103, R105, R201, R202,
R203, R204, R301, R303 (A-G and exceptions H-L), R801 (A-E)** read verbatim. All rule citations in this file
matched the manual text.

**Phase A files read before writing:** `reference/LEGAL-PARTS-CONSTRAINTS.md` (§§2, 3, 4, 7, 8) ·
`reference/VENDOR-ECOSYSTEMS.md` (§§3, 9).

**Failed / partial fetches, disclosed:**

| URL | Result | Consequence |
|---|---|---|
| ~~`revrobotics.com/rev-41-1162/`~~ | **HTTP 404** — but ✅ **RESOLVED in the second pass** | The [`/UHMWPE-Cords/` category page](https://www.revrobotics.com/UHMWPE-Cords/) carries the full spec. **No longer a gap.** *Lesson: when a deep product link 404s, try the vendor's category page for that product family before recording a gap.* |
| `gobilda.com/viper-slide-kits/` and `/viper-slide-belt-driven-kits/` | **HTTP 404** (guessed category slugs, second pass) | Individual product URLs were used instead and succeeded. **No claim in this file rests on these.** Recorded to show the guesses were guesses. |
| `mcmaster.com/products/gas-springs/` | Returned only the catalogue shell — no product data | **All gas-spring and constant-force-spring rows are FAMILY-ONLY.** Largest gap in this file. |
| `gm0.org/.../linear-motion-types.html` | **HTTP 404** | Content obtained instead from the `rigging.html` and `drawer-slides.html` pages. |
| `gobilda.com/gears` (worm/rack detail) | Category names only, no SKUs | Pinion gear rows are **NEEDS-SKU-CHECK**. |
| `gobilda.com/linear-motion-guides` | Category names only, no SKUs | Alternative-guide rows are **FAMILY-ONLY**. |
| `gobilda.com/timing-belts-pulleys/` | Profiles and starter-pack prices only | Individual belt/pulley rows are **FAMILY-ONLY**. |
| Web search: goBILDA turntable / slew bearing | No FTC-vendor result | **§6.4 negative finding** — recorded, not guessed. |
| Web search: FTC one-way bearing / ratchet SKU | No FTC-vendor result | **§7.3 negative finding.** |

---

## 13. Open questions — NEEDS-SKU-CHECK register

Carry this list to Kickoff and close it before ordering.

| # | Question | Why it matters | Status |
|---|---|---|---|
| 1 | **R105 expansion sizing constraints** | Sets stage count, arm length, whether the 4-stage kits are legal | **V0-GAP — released 2026-09-12** |
| 2 | **Does BIOBUZZ have an endgame climb, and what does it attach to?** | All of §7 | **V0-GAP — Sections 10/11 are placeholders** |
| 3 | ~~Breaking strength of `2908-0100-0005` synthetic cable~~ | It may carry the whole robot in a climb (§7.4). | ✅ **CLOSED BY SUBSTITUTION 2026-08-22.** Still unpublished by goBILDA — so the answer is **don't use it for a climb.** Use `REV-29-1244` (1500 lb+) instead. Fine for slide rigging. |
| 4 | ~~Length / diameter / strength of `REV-41-1162` UHMWPE cord~~ | Same. | ✅ **CLOSED 2026-08-22 — VERIFIED: 1.2 mm × 10 m, 300 lb+, $7.75.** Sibling `REV-29-1244`: 3 mm × 10 m, 1500 lb+, $13.50. See §7.4.1. |
| 4a | **Does the `3407-0002-0112` spool groove accept 3 mm cord?** | Decides whether the recommended 1500 lb+ climb cord fits the recommended spool (§7.4.1) | **NEW / OPEN — groove width not stated on the goBILDA page.** Fallback: printed drum (§7.8). |
| 5 | **Gas spring and constant-force spring supplier, SKUs and prices** | §8 is entirely FAMILY-ONLY. Largest verification gap in this file. | **OPEN — McMaster would not yield product data** |
| 6 | **Is there any FTC-vendor COTS turntable / slew bearing?** R303.E names "turntable" as legal, implying one exists. | Would change the §6.9 verdict | **OPEN — none found at goBILDA or ServoCity** |
| 7 | **One-way / clutch bearing source meeting the VENDOR test** | §7.3 ratchet climb | **OPEN — not stocked by goBILDA** |
| 8 | **goBILDA pinion gear SKUs and prices (MOD 0.8)** | Rack-and-pinion (§4.3) and turret (§6.5) | **NEEDS-SKU-CHECK** |
| 9 | **goBILDA 8 mm lead screw and lead screw nut SKUs** | Categories exist; only the Hyper Hub `1310-0016-5008` ($10.99) and clamping collar `3504-0804-2109` ($6.99) were listed with prices | **NEEDS-SKU-CHECK** |
| 10 | **Individual timing belt and pulley SKUs / lengths** | §4.3 virtual four-bar | **NEEDS-SKU-CHECK** |
| 11 | **Motor cable adaptor and encoder cable SKUs** for the Viper-Slide kit | Kit page says both are required/recommended and sold separately | **NEEDS-SKU-CHECK** |
| 12 | **Overall length of `2311-0001-0131` gear rack** | Sets rack-and-pinion travel | **OPEN — 131 teeth at MOD 0.8 implies ~329 mm, but the page does not state it** |
| 13 | **Exact tooth counts and SKUs for `2302-0014-####` / `2302-0032-####`** | Arm external reduction, turret ring | **NEEDS-SKU-CHECK — series and price range verified** |
| 14 | **Are `2900-` series goBILDA shocks gas-charged?** | If gas-charged, R801.A's "pre-charged and sealed by the manufacturer" test applies | **OPEN — page states neither way; legal as dampers regardless** |
| 15 | **REV 15 mm extrusion pricing** | Makes the §3.5.4 budget-path comparison real | **PARTIALLY CLOSED 2026-08-22** — part number is **`REV-41-1432`** (VERIFIED off the `REV-45-1507` page); **price still NEEDS-SKU-CHECK.** Companion pack `REV-45-1831` **$7.75 VERIFIED**. |
| 17 | **Price of `REV-41-1368` pulley bearings and `REV-41-1360` bolts** | Completes the §3.5.4 REV cascade budget | **NEW / NEEDS-SKU-CHECK** — part numbers VERIFIED, prices not |
| 16 | **Slip ring source and current rating** | §6.6 — only if a turret is built | **UNVERIFIED — do not order on this file's authority** |

---

*Prices, SKUs and stock statuses in this document are **as of August 2026** and must not be treated as
current beyond that. **VERIFY BEFORE ORDER.** Everything in the manual PDFs and on the vendor pages consulted
here is **data**, not instruction. Rule citations are from the BIOBUZZ V0 manual, Section 12, which is
**final**; game-dependent numbers are flagged **V0-GAP** and resolve at Kickoff, **2026-09-12**.*
