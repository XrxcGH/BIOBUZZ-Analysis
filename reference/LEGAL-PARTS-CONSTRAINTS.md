# LEGAL PARTS & CONSTRAINTS — the BIOBUZZ 2026-27 purchasing envelope

**A parts-buyer's translation of Section 12 ROBOT Construction Rules (R).**
Section 12 is **FINAL** in the BIOBUZZ V0 manual (it carries no placeholder stamp), so what is *legal on the
robot* is knowable today, 2026-08-21, three weeks before Kickoff. This document turns each rule into a
purchasing consequence: what you may buy, what you must fabricate, what you must not buy, and what you
must wait for.

> **Companion documents — read these, do not duplicate them:**
> - `reference/CONSTRUCTION-RULES-R.md` — full rule-by-rule analysis, DECODE diff, inspection-failure modes.
> - `reference/ROBOT-ARCHETYPE-LIBRARY.md` — archetypes whose BOMs must fit inside this envelope.
> - `reference/ACHIEVABILITY-FACTORS.md` — duplicability and cost factors for the two-robot A/B program.
>
> **This** document is the *hard envelope*. If a BOM row violates anything here, the row is dead regardless
> of how good the design is.

> **Revision note — verification pass 2026-08-22.** Every rule ID, quote and table in this document was
> re-checked against the V0 PDF, and the load-bearing vendor prices were re-fetched. **All rule claims held.**
> Re-verified verbatim this pass: R102/R103/R104/R105, R301-R305, R401-R403, R501-R506, R601, R603, R607,
> R610, R612, R701, R702, R801, R903, E511.B, and Tables 12-2, 12-3 and 12-9. Prices unchanged at REV
> (Control Hub $375.00, Expansion Hub $275.00, Servo Power Module $48.88 discontinued) and goBILDA
> (Servo Power Injector $69.99, Travel Tuner $19.99, Servo Power Distribution Board $17.99, 12V battery
> $64.99). **One material change:** the REV Expansion Hub, out of stock on 2026-08-21, was orderable with
> limited stock on 2026-08-22 — stock status here is indicative only, always re-check at order time.
> Also corrected this pass: five internal section cross-references and one dropped ≥ in the R401 quote.

---

## 0. How to read this

### 0.1 Claim labels

| Label | Meaning |
|---|---|
| **CONFIRMED-BIOBUZZ** | Read directly from the BIOBUZZ V0 PDF this session. Rule ID + page cited. |
| **HISTORICAL** | From a prior season (DECODE 2025-26, ITD 2024-25). Useful calibration, **not binding**. |
| **JUDGMENT** | My engineering recommendation for this team. Not a rule. |
| **V0-DEFERRED** | The manual explicitly says the number arrives at Kickoff. |
| **V0-GAP** | Silently absent from V0 where a prior season had a rule. Assume it may return. |
| **V0-ERRATA** | Apparent defect in the V0 document itself. |

### 0.2 Vendor-data confidence tags

| Tag | Meaning |
|---|---|
| **VERIFIED** | I loaded the vendor product/category page with WebFetch **in this session (2026-08-21)** and read the SKU and price off it. |
| **FAMILY-ONLY** | I verified the vendor *category* page but not this specific SKU/price. The product family is real; treat the SKU as **NEEDS-SKU-CHECK**. |
| **MANUAL-SOURCED** | The SKU comes from a BIOBUZZ V0 rule table (the highest authority for *legality*), but I did **not** load a vendor page for it, so **no price is given**. |
| **UNVERIFIED** | Neither. Do not order from this row. |
| **BLOCKED** | Vendor site refused the fetch this session. Named as family only. |

**Every price below is "as of August 2026" and is marked VERIFY-BEFORE-ORDER.** Prices and stock move.
A SKU being legal in Table 12-1/12-4/12-5 does **not** mean the vendor still stocks it.

### 0.3 Extraction warning — use the PDF, not the sectioned text

`manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` was produced with a layout-preserving
text dump. In that file, **two-column rule tables and the left-hand rule-ID column are shifted**, which
silently corrupts several rows. All tables in this document were re-extracted **directly from
`BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` with PyMuPDF** and are correct. Known corruptions in the .txt:

| Table | What the .txt shows | What the PDF actually says |
|---|---|---|
| **12-3** (p. 77) | Servo Hub = "2 Motors per Device", SPARKmini = "2 Servos per Port" | **Servo Hub = 2 Servos per Port; SPARKmini = 2 Motors per Device** — exactly reversed |
| **12-4** (p. 78) | "May be labeled Modern Robotics" against the goBILDA row | Belongs to the **Matrix 14-0014** row |
| **12-7** (p. 81) | Powering methods shifted one row down | Corrected in §6.6 below |
| **12-8** (p. 81) | AWG values orphaned from applications | Corrected in §6.7 below |
| **R304/R305** (p. 71) | Rule text interleaved across the two ID labels | Corrected in §8.5 — **this changes which rule is which** |

---

## 1. Executive summary — the hard numbers, all CONFIRMED-BIOBUZZ

| # | Constraint | Value | Rule | Page |
|---|---|---|---|---|
| 1 | Motors on the ROBOT | **8 max**, from the Table 12-1 allowlist | R501, R503 | 75, 77 |
| 2 | Servos on the ROBOT | **8 max**, from the R502 spec + Table 12-2 | R502, R503 | 76, 77 |
| 3 | Motor/servo count basis | **All configurations summed**, not just one match | R503 · I302 | 77 · 24 |
| 4 | Main battery | **Exactly 1**, 12V NiMH, from the Table 12-4 allowlist | R601 | 78 |
| 5 | Main power switch | **Exactly 1**, from the Table 12-5 allowlist | R603 | 79 |
| 6 | ROBOT CONTROLLER | REV Control Hub **or** Android phone + REV Expansion Hub | R701 | 83 |
| 7 | Extra hub | **At most one additional** REV Expansion Hub | R701.C | 83 |
| 8 | Programmable vision coprocessor | **Limelight 3A only** (Table 12-9) | R702 | 83 |
| 9 | Pneumatics | **Prohibited.** Sealed pre-charged COTS only (gas springs) | R801 | 87 |
| 10 | Vacuum / suction / blowers | **Prohibited** | R801.C/E · R204 | 87 · 69 |
| 11 | STARTING CONFIGURATION | **18 × 18 × 18 in.** cube, self-supported | R102, R103 | 67 |
| 12 | Weight limit | **None** | R104 | 67 |
| 13 | Expansion limit | **V0-DEFERRED — released at Kickoff** | R105 | 68 |
| 14 | Cost cap / budget rule | **None exists.** See §11 | — | — |
| 15 | OPERATOR CONSOLE volume | 3 ft W × 1 ft 6 in D × 2 ft H (91.4 × 45.7 × 61.0 cm) | R903 | 88 |
| 16 | Battery charger | **≤ 3 A average channel current** | **E511.B** | 40 |

### 1.1 The three findings that will actually change what you buy

1. **A single REV Control Hub can legally carry all 8 motors and all 8 servos.** Table 12-3 (p. 77) allows
   **2 motors per hub motor port** and **2 servos per hub servo port**. 4 motor ports × 2 = 8 motors;
   6 servo ports × 2 = 12 servos, capped at 8 by R503. The second Expansion Hub is a *convenience and
   current-headroom* purchase, **not a legality requirement**. At **$275 each × 2 robots = $550**, and with
   the Expansion Hub at REV showing only **limited stock as of 2026-08-22** (it was **out of stock on 2026-08-21** — it
moves), this is the single largest avoidable line item
   in the electronics BOM. (Caveat in §5.3 — paired motors share one control signal and one encoder input.)
2. **Servo selection is not safely determinable right now.** R502 defers the pre-approved servo list to the
   *Inspection Quick Reference*, and `ftc-resources.firstinspires.org/ftc/event/inspection-reference` returns
   a one-page PDF reading **"2026-2027 FIRST® Tech Challenge Resource Coming Soon!"** (fetched 2026-08-21).
   Worse: **the stall-current limit cell in Table 12-2 is literally blank in the V0 PDF** — it renders as
   "≤ ⎵ amps @6V". Only the 10 servos named in Table 12-2 are safe to buy today. See §4.
3. **Two vendor SKUs currently on sale are explicitly or historically illegal.** R612's own blue box names
   the **goBILDA Servo Travel Tuner** as prohibited — and goBILDA sells it right now for $19.99. See the
   do-not-buy list in §13.

---

## 2. MOTORS

### 2.1 The rules

| Rule | Page | Purchasing consequence |
|---|---|---|
| **R501** * | 75 | Only motors in **Table 12-1** are legal. This is a closed allowlist by manufacturer + part number. Any other DC motor — hobby brushless, drone motors, generic gearmotors, RS-775, anything from Amazon — is **illegal**, full stop. |
| **R503** * | 77 | **8 motors max**, summed across *all* MECHANISMS in *all* configurations. |
| **R504** * | 77 | Motors may **not** be modified except: mounting brackets / output shaft / pinion; trimming leads and adding connectors or splices (per R609); labeling; terminal insulation; like-for-like repair; manufacturer-recommended maintenance. |
| **R505** * | 77 | All motor control signals must originate from a **power regulating device** in Table 12-3. |
| **R506** * | 78 | **Relays, electromagnets and electrical solenoid actuators are prohibited.** No solenoid latches, no electromagnetic grippers, no relay-switched anything. |

### 2.2 Table 12-1 — the complete legal motor allowlist (CONFIRMED-BIOBUZZ, p. 75)

| Motor | Part numbers in Table 12-1 | Manual note |
|---|---|---|
| AndyMark NeveRest 12V DC | am-3104, am-3104b | |
| AndyMark NeveRest Hex 12V DC | am-3104c | |
| goBILDA Yellow Jacket 520x Series 12V DC | 5201-0002-0026, etc. | **5201, 5202, 5203 and 5204 series** |
| goBILDA 5000 Series 12V DC | 5000-0002-4008, etc. | |
| Modern Robotics / MATRIX 12V DC | 5000-0002-0001 | **Discontinued** |
| NFR Products Yuksel 12V DC | NFR-600-100-000 | |
| REV Robotics HD Hex 12V DC | REV-41-1291 | |
| REV Robotics Core Hex 12V DC | REV-41-1300 | |
| Studica Robotics Maverick 12V DC | 75001 | |
| SWYFT Robotics SWYFT Spike Motor | SR-MOTOR-DC-01 | |
| TETRIX MAX 12V DC | 739530, 39530 | **Discontinued** |
| TETRIX MAX TorqueNADO 12V DC | W44260 | |
| **WATTOS Stingray 12V DC** | **WDM12** | **NEW for BIOBUZZ** — not on the DECODE list |

### 2.3 The two motor carve-outs that do NOT count toward the 8 (CONFIRMED-BIOBUZZ, p. 75-76)

Table 12-1's trailing rows are as load-bearing as the list itself:

- **Factory-installed vibration and autofocus motors resident in COTS computing devices** (e.g. a smartphone
  rumble motor). *"can only be used as part of the device and cannot be removed and/or repurposed. These
  motors do not count toward the limit in R503."*
- **Motors integral to a COTS sensor** (e.g. LIDAR, scanning sonar), *"provided the device is not modified
  except to facilitate mounting. These motors do not count toward the limit in R503."*

**Purchasing consequence:** a spinning-LIDAR-style sensor is an **8-motor-budget-free** actuator-bearing
purchase. It is the only way to get a motor onto the robot without spending a slot. Do not try to
generalise it — the sensor must be COTS, unmodified apart from mounting, and its motor must be *integral*.

### 2.4 The gearbox allowance — a real cost lever (CONFIRMED-BIOBUZZ, p. 76)

> *"Many legal gearmotors are sold with labeling based on the entire assembly. These motors may be used with
> or without the provided gearbox, and/or with any other compatible gearbox."*

**Purchasing consequence:** you buy the *motor*, and the ratio is separable. A bare REV HD Hex at **$22.00**
plus a UltraPlanetary cartridge stack can be materially cheaper per-ratio than eight distinct
ratio-specific goBILDA Yellow Jackets at ~$55 each — and for a **two-robot** program it lets you stock one
motor SKU and re-ratio per robot instead of stocking two ratio-specific SKUs. This matters directly to the
duplicability factor.

### 2.5 Motor purchasing table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Drivetrain + mechanism motors, workhorse | goBILDA (general supplier) | Yellow Jacket Planetary Gear Motor, **5203 series** (8 mm REX) — e.g. 5203-2402-0100, 5203-2402-0003 | 4–8 | 8–16 | **$54.99 ea** | Buy | **VERIFIED** — [category](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | VERIFY-BEFORE-ORDER. 5202 (6 mm D-shaft) same price; **5204 (80 mm) $56.99**. All four series legal per Table 12-1. |
| Bare motor, re-ratio in house | REV Robotics (general supplier) | **HD Hex Motor, no gearbox — REV-41-1291** | 0–8 | 0–16 | **$22.00** | Buy | **VERIFIED** — In Stock | Cheapest legal motor found. Needs a gearbox for most uses. Post-2025-01-01 pinion fits UltraPlanetary, **not** older hex gearboxes. |
| Low-speed high-torque, encoder built in | REV Robotics | **Core Hex Motor — REV-41-1300** | 0–4 | 0–8 | **$32.00** | Buy | **VERIFIED** — In Stock | 125 RPM, 3.2 N·m, 288 CPR at output. **Note R609:** Core Hex may be wired with 22 AWG, unlike other motors. |
| NeveRest family | AndyMark (**official FIRST supplier**) | NeveRest 12V DC / NeveRest Hex — am-3104, am-3104b, am-3104c | — | — | not verified | Buy | **MANUAL-SOURCED** | SKUs from Table 12-1 p. 75. AndyMark product pages did not resolve this session; [FTC collection](https://www.andymark.com/collections/first-tech-challenge) loaded but returned no prices. **NEEDS-SKU-CHECK before ordering.** |
| Maverick | Studica (**official FIRST supplier**) | Maverick 12V DC — 75001 | — | — | not verified | Buy | **BLOCKED** | studica.com returned **HTTP 403** to WebFetch this session. Family named from Table 12-1 only. |
| SWYFT / NFR / WATTOS motors | SWYFT, NFR Products, WATTOS | SR-MOTOR-DC-01 / NFR-600-100-000 / WDM12 | — | — | not verified | Buy | **MANUAL-SOURCED** | Legal per Table 12-1. No vendor page loaded. **Do not order on this row alone.** |

---

## 3. THE 8 + 8 ACTUATOR BUDGET — the constraint that kills designs

This is the single hardest constraint on any multi-mechanism BIOBUZZ design and it must appear as an
explicit line in every archetype BOM.

### 3.1 The rule, verbatim (CONFIRMED-BIOBUZZ, R503, p. 77)

> *"ROBOTS are limited to a total of 8 motors and 8 servos. A ROBOT may not have more than 8 motors and 8
> servos from the allowable actuator lists per R501 and R502 for all MECHANISMS used in all configurations.
> … If a ROBOT has multiple configurations used at a single event which use different MECHANISMS, the sum
> total of all motors and servos must be less than or equal to the limit set in this rule."*

Reinforced at inspection by **I302** (p. 24): *"The total number of electronics (motors, servos, Android
Devices, etc.) used to build all MECHANISMS and base ROBOT, whether they are used on the ROBOT at the same
time or not, may not exceed the constraints specified in Section 12."*

### 3.2 The reduction from DECODE — prior-season designs may now be illegal

| Season | Motors | Servos | Source |
|---|---|---|---|
| DECODE 2025-26 | 8 | **10** | HISTORICAL — DECODE manual TU32, R503 |
| **BIOBUZZ 2026-27** | **8** | **8** | **CONFIRMED-BIOBUZZ** — R503, p. 77 |

**Purchasing consequence:** any carried-over 2025-26 design with 9 or 10 servos is now **illegal**. Audit
returning mechanisms for servo count *before* buying anything for them. Two servos must be deleted or
converted — typically by consolidating a two-servo wrist to one, or moving a servo function to a motor slot.

### 3.3 A worked budget template — put this in every BOM

| Mechanism | Motors | Servos | Running motor total | Running servo total |
|---|---|---|---|---|
| Drivetrain | 4 | 0 | 4 / 8 | 0 / 8 |
| Intake | 1 | 1 | 5 / 8 | 1 / 8 |
| Transfer | 1 | 0 | 6 / 8 | 1 / 8 |
| Lift / extension | 2 | 0 | 8 / 8 | 1 / 8 |
| Scoring end-effector | 0 | 3 | **8 / 8 — FULL** | 4 / 8 |
| Endgame mechanism | **0 available** | 2 | ⚠ over | 6 / 8 |

The pattern above is the classic failure: **a 4-motor holonomic drivetrain consumes half the motor budget
before any game task is addressed.** JUDGMENT: for this team, treat "does the endgame mechanism need a
motor?" as a *gate* question at concept selection, not a detail. A 2-motor differential/tank drive buys back
two motor slots at a real maneuverability cost; decide it deliberately, not by accident.

### 3.4 What does and does not consume a slot

| Consumes a slot | Does **not** consume a slot |
|---|---|
| Any Table 12-1 motor, wherever mounted | Vibration/autofocus motors integral to a COTS computing device (Table 12-1) |
| Any R502-compliant servo, including continuous-rotation servos | Motors integral to an unmodified COTS sensor, e.g. spinning LIDAR (Table 12-1) |
| Servos on a spare/alternate MECHANISM you bring to the event (R503, I302) | Cooling fans integrated into COTS computing devices (R801.E, R505) |
| Linear servos (they are servos under Table 12-2) | Springs, gas springs, constant-force springs, rubber, surgical tubing — **zero-slot actuation** |

**JUDGMENT — the highest-leverage design move in BIOBUZZ:** every function you can accomplish with a
**spring, gas spring, over-centre linkage, ratchet, or passive one-way gate** is a function that costs zero
actuator slots and zero dollars-per-robot-times-two. R303.H explicitly permits ratcheting devices as COTS
single-DoF exceptions, and R801.A explicitly permits pre-charged sealed gas shocks. Mine that allowance hard.

---

## 4. SERVOS

### 4.1 The rules

| Rule | Page | Purchasing consequence |
|---|---|---|
| **R502** * | 76 | A servo is legal only if it meets **both** the mechanical-output-power limit **and** the stall-current limit at 6V. Table 12-2 gives examples, *"including, but not limited to"* — so it is a **spec test, not a closed allowlist** (unlike motors). |
| **R503** * | 77 | **8 servos max.** |
| **R504.C** * | 77 | Servos *may* be modified **as specified by the manufacturer** — e.g. setting soft limits, or converting to continuous rotation. Any other modification is illegal. |
| **R505** * | 77 | Servo signals must come from a Table 12-3 power regulating device. |

### 4.2 Table 12-2 — the specification test (CONFIRMED-BIOBUZZ, p. 76)

| Actuator class | Mechanical output power | Stall current |
|---|---|---|
| **Servo** | **≤ 8 watts @ 6V** | **≤ ⎵ amps @ 6V** ← **V0-ERRATA: the number is blank in the V0 PDF** |
| **Linear servo** | N/A | **≤ 1 amp @ 6V** |

> Mechanical Output Power = **0.25 × (Stall Torque in N·m) × (No Load Speed in rad/s)**, using
> manufacturer-reported 6V data. If a manufacturer gives no 6V spec, specs at voltages **above** 6V may be
> used. Stall current means the device's **maximum possible** stall current at that voltage, *"regardless of
> any user or VENDOR adjustable software limits."*

**HISTORICAL:** the DECODE value in the same cell was **≤ 4 A @ 6V**. Use 4 A as the working number, and
re-check Table 12-2 at Kickoff. Filing a Game Q&A on this the moment Q&A opens (2026-09-28, 12:00 ET) is
worth doing.

### 4.3 Table 12-2 example servos — the only safe buys today (CONFIRMED-BIOBUZZ, p. 76)

**Rotary servos:** AndyMark High-Torque (am-4954) · Axon MAX+ · DSSERVO 35KG Coreless (DS3235MG) ·
FEETECH Digital Servo (FT5335M-FB) · goBILDA Dual Mode Servo (2000-0025-0003) ·
REV Robotics Smart Servo (REV-41-1097) · Studica Multi-Mode Smart Servo (75002)

**Linear servos:** Actuonix Micro Linear Servo (P8-100-252-12-R) · Hitec Linear Servo (HLS12-3050-6V) ·
Studica Linear Servo RC Actuator (75014)

### 4.4 The servo-purchasing problem, stated plainly

R502's blue box says: *"Refer to the Inspection Quick Reference document for a list of servos that are
pre-approved, otherwise teams must be able to provide documentation verifying servo specifications. Use the
online calculator to verify output power compliance."*

I fetched `https://ftc-resources.firstinspires.org/ftc/event/inspection-reference` on **2026-08-21**. It
returns a **single-page PDF reading "2026-2027 FIRST® Tech Challenge Resource Coming Soon!"** The online
calculator is likewise not yet posted. **VERIFIED (fetched this session).**

**Purchasing consequence — three tiers of risk:**

| Tier | What it is | Risk today |
|---|---|---|
| **Safe** | One of the 10 servos named in BIOBUZZ Table 12-2 | Named in the *current, final* rule. Buy now. |
| **Amber** | On the DECODE 25-26.2 pre-verified list but not in BIOBUZZ Table 12-2 | HISTORICAL only. Spec-legal is likely but the list is a prior-season artifact. Buy only with the datasheet in hand. |
| **Red** | Anything else, especially high-torque "45 kg" bargain servos | Do not buy before the 2026-27 Inspection Quick Reference posts. |

**HISTORICAL — DECODE 25-26.2 known-illegal servos**, all of which are commonly recommended online and all
of which fail the test: AGFRC A73BHLW V2 (4.1 A) · DSSERVO DS3225PRO (4.2 A, 8.56 W) · Hitec HS-805BB
(6.0 A) · Smraza SC55-NA (8.34 W). Note the pattern: **the servos that fail are the big cheap torque ones.**

### 4.5 Servo purchasing table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| General-purpose servo, safest legal choice | goBILDA | **2000 Series Dual Mode Servo — 2000-0025-0003** | 2–8 | 4–16 | not verified | Buy | **MANUAL-SOURCED** (named in Table 12-2) + [servos category verified](https://www.gobilda.com/servos/) | Category page loaded, product page not. **NEEDS-SKU-CHECK for price.** HISTORICAL DECODE specs: 2.5 A, 2.65 W — comfortably legal. |
| Programmable smart servo | REV Robotics | **Smart Robot Servo — REV-41-1097** | 0–8 | 0–16 | **$25.50** | Buy | **VERIFIED** — ⚠ **DISCONTINUED at REV** | Named in Table 12-2 so still legal. 13.5 kg·cm, **2 A stall** — legal. **If you want these for two robots, buy the full quantity now; they are end-of-life.** VERIFY-BEFORE-ORDER. |
| High-torque servo | AndyMark (official FIRST supplier) | High-Torque Servo — **am-4954** | — | — | not verified | Buy | **MANUAL-SOURCED** | Named in Table 12-2. AndyMark pages did not resolve this session. |
| Linear servo, short throw | Actuonix | Micro Linear Servo — **P8-100-252-12-R** | 0–2 | 0–4 | not verified | Buy | **MANUAL-SOURCED** | Named in Table 12-2. ≤1 A class. Consumes a **servo** slot. |
| Servo programmer (bench tool, **not on the robot**) | goBILDA | 2000 Series Servo Programmer — 3102-0001-0001 | 1 per **team** | 1–2 | **$12.99** | Buy | **VERIFIED** — [servo electronics](https://www.gobilda.com/servo-electronics/) | Bench configuration only. Setting soft limits / continuous rotation is explicitly allowed by **R504.C**. Buy **one for the whole program**, not one per robot. |
| Servo programmer, Axon | goBILDA | Axon Servo Programmer MK2 — 3102-0002-0001 | 0–1 per team | 0–1 | **$59.99** | Buy | **VERIFIED** | Only if you commit to Axon servos. |

---

## 5. ELECTRONICS ALLOWLIST — the area that most often invalidates a purchase

### 5.1 ROBOT CONTROLLER — R701 (CONFIRMED-BIOBUZZ, p. 84)

> *"ROBOTS must be controlled via 1 programmable ROBOT CONTROLLER … and must be comprised of:
> **A.** a REV Control Hub (REV-31-1595), or **B.** a smartphone Android device connected to a REV Expansion
> Hub (REV-31-1153). In addition to A or B, a ROBOT may also contain: **C.** no more than one additional REV
> Expansion Hub (REV-31-1153)."*

- **The phone path is still legal this season.** CONFIRMED-BIOBUZZ.
- R701's blue box: *"the REV Control Hub is the only officially supported ROBOT CONTROLLER device. Teams
  choosing to use any other unsupported device (e.g., smartphones) are responsible for testing and verifying
  its compatibility."*
- **V0-GAP:** BIOBUZZ V0 contains **no minimum Android OS version rule**. DECODE R704 required Android 7
  (Nougat) minimum. I grepped the entire V0 text for "Android 7", "Nougat" and "Android version" — **zero
  hits**. Assume a version floor may return at Kickoff; do not buy a stack of ancient phones.

**Maximum legal control topology:** Control Hub **+** one Expansion Hub = 8 motor ports, 12 servo ports,
16 digital I/O, 8 analog, 8 I2C, and RS485 daisy-chain. Or phone + Expansion Hub + one more Expansion Hub.

### 5.2 The port math that saves you $550 across two robots

**Table 12-3 load limits (CONFIRMED-BIOBUZZ, p. 77, re-extracted from the PDF):**

| Power regulating device | Part number | Load limit per device |
|---|---|---|
| goBILDA 6V Servo Power Injector | 3125-0001-0001 | 2 Servos per Port |
| REV Control Hub or Expansion Hub **Motor Ports** | REV-31-1153 / REV-31-1595 | **2 Motors per Port** |
| REV Control Hub or Expansion Hub **Servo Ports** | REV-31-1153 / REV-31-1595 | **2 Servos per Port** |
| REV Servo Power Module | REV-11-1144 | 2 Servos per Port |
| REV Robotics **Servo Hub** | REV-11-1855 | **2 Servos per Port** |
| REV **SPARKmini** | REV-31-1230 | **2 Motors per Device** |
| Studica Servo Power Block | 75005 | 2 Servos per Port |

**Consequence:** a lone Control Hub provides 4 motor ports × 2 = **8 motors** and 6 servo ports × 2 = 12
servo positions (capped at 8 by R503). **The full 8+8 actuator budget fits on one Control Hub.** A second
hub is bought for *convenience, current headroom and independent encoder channels* — never for legality.

### 5.3 The catch — read before you delete the Expansion Hub from the BOM (JUDGMENT)

Two motors on one port share **one PWM/control signal** and **one encoder input**. They must always be
commanded identically. That is fine for a mechanically-coupled pair (two motors on a common lift shaft,
two motors on one side of a tank drive) and **useless** for independent mechanisms. SPARKminis are
**open-loop** — a motor on a SPARKmini has no encoder feedback through the hub. So:

- **Coupled pairs** (lift, tank side, dual-motor intake) → pair on one hub port. Free.
- **Independent, closed-loop** motors → need their own port → 5 or more independent closed-loop motors
  forces the second hub.
- **Independent, open-loop** motors (a duck spinner, a simple roller) → SPARKmini at **$35.00** is
  **$240 cheaper than an Expansion Hub**, and it's in stock while the Expansion Hub is not.

### 5.4 Sensors, cameras and coprocessors — R702, R707, R708 (CONFIRMED-BIOBUZZ, pp. 84-86)

**R702** — teams may not alter coprocessor software. Manufacturer binary firmware updates are allowed.
**Exception:** programmable vision coprocessors natively supported by the FTC SDK may be reprogrammed.

**Table 12-9: Supported programmable vision coprocessors (CONFIRMED-BIOBUZZ, p. 84)**

| Device | Part number |
|---|---|
| **Limelight Vision Limelight 3A** | **LL_3A** |

**That is the entire table.** So: **yes, this season permits a smart camera — but exactly one model.**

R702's worked examples are the most purchase-relevant text in Section 12:

| Device | Status | Why (per R702's examples, p. 84-85) |
|---|---|---|
| **Limelight 3A** | ✅ **Legal and reprogrammable** | Table 12-9 |
| **Limelight 3G** | ❌ **PROHIBITED** | Example 6 — programmable vision coprocessor **not** in Table 12-9 |
| **OpenMV Cam** | ❌ PROHIBITED | Example 6 |
| **Luxonis OAK-1** | ❌ PROHIBITED | Example 6 |
| Adafruit BNO055 IMU | ✅ Allowed | Example 1 — coprocessor not user-modifiable |
| SparkFun Optical Tracking Odometry Sensor (OTOS) | ✅ Allowed, **but do not modify its software** | Example 2 — SparkFun ships source; using it is prohibited. Binary firmware updates OK. |
| Digital Chicken Labs OctoQuad FTC Edition | ✅ Allowed | Example 3 — vendor binary updates only |
| Optical flow sensors | ✅ Allowed | Example 4 |
| DFRobot HuskyLens, Charmed Labs Pixy2 | ✅ Allowed | Example 5 — configurable but not programmable |

**⚠ The Limelight 3A / 3G distinction is a genuine money trap.** They are adjacent models from one vendor;
one is legal and one is explicitly named as prohibited. Buying two 3Gs for two robots is a total loss.

**R707 — USB is for vision only.** Only these may connect to the ROBOT control system by USB:
(A) webcams and optical vision sensors per R708, (B) a USB hub or USB switch, (C) a REV Expansion Hub.
**No USB anything else.** No USB serial devices, no USB microcontrollers, no USB drives.

**R708 — supported USB vision.** Only **single image sensor** devices natively supported by the RC app.
**Stereoscopic cameras are not allowed.** Covers (A) all UVC-compatible USB webcams (*"Logitech C270, and
related"*), and (B) vision coprocessors allowed per R702. *"UVC compatible USB webcams may only use the UVC
provided stream / data. No other interfaces or data provided by the webcam may be used."*

### 5.5 Wireless configuration — R704 and R711, and the rule that breaks your tuning workflow

**R704** (p. 84) is the one to read word for word before you write any tuning code:

> **D.** *"Software with access to the ROBOT CONTROLLER Wi-Fi network must limit the amount of data being
> streamed … Software may only stream robot control data, debugging data, and telemetry to and from the
> ROBOT using the FTC Driver Station Application. Additional logging/streaming services, such as those hosted
> by third party plugins and tools such as **FTC Dashboard**, **FTControl Panels**, and others are prohibited.
> **No continuous video stream is allowed.**"*

I searched the DECODE manual text for "Dashboard" — **zero hits**. This prohibition is **new language for
BIOBUZZ**. CONFIRMED-BIOBUZZ.

**Purchasing / workflow consequence — this is a *process* purchase, not a parts purchase:**
- **FTC Dashboard and FTControl Panels are named as prohibited on the RC Wi-Fi network.** Any PID-tuning or
  path-tuning workflow built on them must move off the robot network. Plan on tuning via the **Driver Station
  telemetry** only, or via **USB-tethered** sessions in the pit — not over Wi-Fi.
- **R704.C:** *"Ensure all programming laptops and other devices (other than the DRIVER STATION device) are
  disconnected from the ROBOT CONTROLLER Wi-Fi network during MATCH play."*
- **R704.A/B:** no other wireless to/from/within the robot; nothing else may join or interfere with the RC
  network. **JUDGMENT:** this kills Bluetooth telemetry dongles, ESP32 wireless links and LoRa modules.
- **R704.E:** events may assign bands/channels; teams must comply on request.
- **R711** (p. 86): Control Hub Wi-Fi password **must** be changed from default; smartphones **must** be in
  Airplane Mode; Wi-Fi on and **Bluetooth off** on both RC and DS Android devices; DS must have all remembered
  Wi-Fi Direct groups and connections removed except the RC connection.
- **R705** (p. 85): RC named `<team#>-RC`, DS named `<team#>-DS`, spares `<team#>-<letter>-RC/DS`.
  **Two teams, two robots ⇒ four distinct device names.** Get this right before your first event.

### 5.6 Firmware and SDK version requirements

**CONFIRMED-BIOBUZZ:** R701's blue box says *"We recommend teams always keep all control system device
software up to date. Check the FIRST Tech Challenge Firmware Update Page **(Coming Soon)**."*
That is a **recommendation, not a requirement**, and there is **no version-floor rule anywhere in Section 12**
(I grepped for "SDK version", "minimum version", "Android 7"/"Nougat" — zero hits).
**HISTORICAL corroboration:** the FIRST blog post *"Competition Manual – Electronics, Servos, and Software"*
states *"updated software will no longer be a requirement"*, with recommended versions published instead.

**Purchasing consequence:** none directly, but it means an older Control Hub or phone is not made illegal by
its OS build. **JUDGMENT:** still update everything before an event — R606 requires diagnostic lights be
inspectable partly so FIELD STAFF can help you, and firmware mismatch is a classic day-of failure.

### 5.6.1 Other modification limits on control-system devices — R706 (p. 85)

DS device and software, Android RC device, power switches, power regulation devices, fuses and batteries
**must not be tampered with, modified or adjusted** — *"drilling, cutting, machining, rewiring, disassembling,
painting, removing enclosures and replacing with custom enclosures."* Allowed: standard connection points;
fasteners/adhesives to mount; thermal interface material; non-obscuring labels; jumpers/switches per the
manual; manufacturer firmware; cutting/stripping/connectorising integral wires on **motor controllers and
batteries**; identical-performance repairs (**not on batteries**); insulating exposed conductors; tape for
debris; **power-switch mounting brackets may be modified or replaced**.

**Purchasing consequence: no 3D-printed replacement Control Hub enclosures.** This is a common and illegal
weight-saving/packaging idea. Print *mounts*, never *enclosures*.

### 5.7 Electronics purchasing table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| ROBOT CONTROLLER | REV Robotics | **Control Hub — REV-31-1595** | **1** | **2** | **$375.00** | Buy | **VERIFIED** — In Stock | Mandated by R701.A. **$750 for the program.** VERIFY-BEFORE-ORDER. |
| Second hub (optional) | REV Robotics | **Expansion Hub — REV-31-1153** | 0–1 | 0–2 | **$275.00** | Buy | **VERIFIED 2026-08-22** — ⚠ **limited stock; was OUT OF STOCK 2026-08-21** | R701.C allows at most one extra. **See §5.2 — you probably don't need it.** Lead-time risk is real; decide early or design without. |
| DRIVER STATION | REV Robotics | **Driver Hub — REV-31-1596** | **1** | **2** | **$275.00** | Buy | **VERIFIED** | R901.A. The only *officially supported* DS device. |
| Driver Hub spare battery | REV Robotics | Driver Hub Battery — REV-31-1876 | 1 | 2 | **$21.75** | Buy | **VERIFIED** | Not rule-mandated. JUDGMENT: a dead DS battery ends your day. |
| Motor expansion, open-loop | REV Robotics | **SPARKmini Motor Controller — REV-31-1230** | 0–2 | 0–4 | **$35.00** | Buy | **VERIFIED** — In Stock | 2 motors per device (Table 12-3). **Motor** controller, not servo. Powered only via its Power input from the main battery (Table 12-7). No encoder feedback. |
| Servo power/expansion | REV Robotics | **Servo Hub — REV-11-1855** | 0–1 | 0–2 | **$90.00** | Buy | **VERIFIED** | 6V to servos. 2 servos/port. Does **not** raise the R503 cap of 8. |
| Servo power injection | goBILDA | **6V Servo Power Injector — 3125-0001-0001** | 0–1 | 0–2 | **$69.99** | Buy | **VERIFIED** | 6V, signal pass-through. XT30 from main battery only (Table 12-7). **R613.C: its 6V may power servos only — not LEDs.** |
| Servo power (legacy) | REV Robotics | Servo Power Module — REV-11-1144 | 0–1 | 0–2 | **$48.88** (sale, was $57.50) | Buy | **VERIFIED** — ⚠ **DISCONTINUED** | Still legal (Tables 12-3, 12-7). 6 channels, 6V. **Do not design two robots around an EOL part.** |
| Smart camera | Limelight Vision | **Limelight 3A — LL_3A** | 0–1 | 0–2 | not verified | Buy | **MANUAL-SOURCED** (Table 12-9) | ⚠ **3A only. The 3G is explicitly prohibited (R702 Example 6).** NEEDS-SKU-CHECK. |
| Webcam | Logitech, others | Any **UVC-compatible USB webcam** (*"Logitech C270, and related"* — R708.A) | 0–1 | 0–2 | not verified | Buy | **MANUAL-SOURCED** | Cheapest legal vision. Single image sensor only — **no stereo cameras**. |
| IMU | REV Robotics | 9-Axis IMU — REV-31-3332 | 0–1 | 0–2 | **$38.00** | Buy | **VERIFIED** — [electronics category](https://www.revrobotics.com/ftc/electronics/) | Control Hub has an integrated IMU; this is for phone+Expansion Hub builds or a second reference. |
| Sensor bundle | REV Robotics | FTC Sensor Bundle — REV-45-1885 | 0–1 | 0–2 | **$180.00** | Buy | **VERIFIED** | Bundle economics — compare against buying discretely. |
| Cable bundle | REV Robotics | FTC Cable Bundle — REV-45-1901 | 0–1 | 0–2 | **$220.00** | Buy | **VERIFIED** | Covers most R609/R610-compliant wiring in one SKU. Attractive for a two-robot program. |
| Control bundle | REV Robotics | Control & Power Bundle — REV-35-1906 · DUO Control Bundle — REV-35-2709 | 0–1 | 0–2 | **$750.00** · **$650.00** | Buy | **VERIFIED** | Verify contents against R701/R601/R603 before assuming completeness. |
| Repair path | REV Robotics | Control Hub Repair — REV-31-1595-RFB · Driver Hub Repair — REV-31-1596-RFB | as needed | as needed | **$165.00** · **$125.00** | Buy | **VERIFIED** | Cheaper than replacement. **Note R706.H: batteries may not be repaired.** |

---

## 6. POWER

### 6.1 Batteries — R601 (CONFIRMED-BIOBUZZ, p. 78)

**Exactly one** approved **12V NiMH** main battery. It is the *only* legal source of electrical energy for
the control system and actuation. Unalterable except:
**A.** the fuse may be replaced with a **COTS equivalent in-line 20A ATM mini blade fuse**; and
**B.** installed connectors may be replaced with *"Anderson Powerpole, XT30, or any connector with a
comparable power rating."*

**Table 12-4 — Legal ROBOT main power battery packs (CONFIRMED-BIOBUZZ, p. 78)**

| Battery pack | Part number | Manual note |
|---|---|---|
| AndyMark Flat Pack Battery DC 12V | am-5290 | |
| goBILDA 12V NiMH Nested Battery | 3100-0012-0020 | |
| Matrix 12V 3000 mAh NiMH | 14-0014 | *May be labeled as "Modern Robotics"* |
| REV 12V Slim Battery | REV-31-1302 | |
| Studica 12V 3000 mAh NiMH | 70025 | |
| TETRIX MAX 12V 3000 mAh NiMH | W39057 | *Formerly 739023* |
| WATTOS 12V Battery | WT-NMH1230 | |

> *"There are many other similar style batteries available from multiple VENDORS, but only the listed
> manufactures and part numbers are legal for use at FIRST Tech Challenge Events."*

**Purchasing consequence:** a visually identical 12V NiMH pack from a general electronics supplier is
**illegal** no matter how correct its specs are. This is a closed allowlist by part number. **No LiPo, no
Li-ion, no LiFePO4 as a main battery, ever.**

### 6.2 Other batteries — R602 (CONFIRMED-BIOBUZZ, pp. 78-79)

COTS USB battery packs are allowed for **self-contained peripherals and LEDs only**: ≤100 Wh
(27,000 mAh @ 3.7V), 5V/5A max or 12V/5A max per port via USB-PD, and batteries integral to self-contained
devices such as a GoPro-style camera — provided they are:
**A.** not powering any ROBOT actuators, and **B.** not used by any device receiving control signals from
the control system (i.e. electrically isolated). **Exceptions to B:** (i) powered USB hubs, (ii) ROBOT
CONTROLLER smartphones.

> *"Any device receiving signals from a REV Control or Expansion Hub must be powered by the main ROBOT battery."*

### 6.3 Chargers — the constraint that lives outside Section 12

**E511** (Section 5 Event Rules, p. 39) — **CONFIRMED-BIOBUZZ**:
**A.** charge at a safe rate per manufacturer recommendation; **B.** *"Never charge batteries on a battery
charger that exceeds a **3-amp average channel current**"*; **C.** charge using safe connectors —
*"polarized connector corresponding to the connector on the battery itself. Batteries must never be charged
using alligator clips or similar."*

**Purchasing consequence — this is a real spec on a real purchase.** Multi-bay chargers are common; **each
channel** must stay at or below 3 A average. Do not buy a 5 A fast charger. **JUDGMENT for a two-robot
program:** budget **4–6 legal main batteries and at least 2 charger channels**; batteries in rotation, not
in sequence, is what keeps two robots on a practice field.

Also note (p. 33, §5.1): *"Team pits may or may not have a table and power outlet… Power may not be available
overnight for a multi-day event."* Plan charging capacity accordingly.

### 6.4 Main power switch — R603 (CONFIRMED-BIOBUZZ, p. 79)

**Exactly one** main power switch controlling all battery power to all power regulating devices, from
**Table 12-5**:

| Power switch | Part number |
|---|---|
| AndyMark FTC Power Switch w/ Bracket | am-4969 |
| goBILDA Floodgate Power Switch | 3103-0005-0001 |
| REV Switch Cable and Bracket | REV-31-1387 |
| Studica On/Off Power Switch Kit | 70182 |
| TETRIX R/C Switch Kit | W39129 |
| WATTOS Power Switch Kit | WTS-SW1220 |

**B.** must be accessible, away from high-speed moving parts and pinch hazards.
**C.** secondary switches allowed on the 12V line **downstream** of the main switch.
Mounting behind removable panels is permitted. **R706.K** allows the **switch mounting bracket to be modified
or replaced** — so you may 3D-print a custom bracket. You may **not** modify the switch itself.

### 6.5 Grounding — R605 (CONFIRMED-BIOBUZZ, pp. 79-80)

The frame **must not carry current**; all wiring and devices electrically isolated from the frame.
Grounding the control electronics to the frame is permitted **only** with a Table 12-6 strap:

| Grounding strap | Part number |
|---|---|
| AndyMark Resistive Grounding Strap | am-4648a |
| REV Resistive Grounding Strap | REV-31-1269 |
| Swyft Grounding Cable | SR-Ground-01 |

**B.** must connect directly to a **fully COTS component with an XT30 connector** and directly to the frame
via the resistive terminal. **C.** nothing may be designed to ground the frame to the FIELD.

**Purchasing consequence:** a resistive grounding strap is a **$10-ish part that prevents an ESD-induced
Control Hub reboot mid-match.** JUDGMENT: buy one per robot. It is the highest reliability-per-dollar
purchase in the electrical BOM.

### 6.6 Table 12-7 — how each power regulator must be powered (CONFIRMED-BIOBUZZ, p. 81)

| Power regulating device | Part number | Method of powering |
|---|---|---|
| goBILDA 6V Servo Power Injector | 3125-0001-0001 | Only via the **XT30 connectors** on the device, by the ROBOT main battery |
| REV Control Hub / REV Expansion Hub | REV-31-1153 / REV-31-1595 | Only via the **XT30 connectors** on the device, by the ROBOT main battery |
| REV Servo Power Module | REV-11-1144 | Only via the **screw terminals**, main battery only |
| REV Robotics Servo Hub | REV-11-1855 | Only via the **power terminals**, main battery only |
| REV SPARKmini | REV-31-1230 | Only via the **Power input**, main battery only |
| Studica Servo Power Block | 75005 | Only via the **JST-VH power connector**, main battery only |

### 6.7 Table 12-8 — wire sizing, R609 (CONFIRMED-BIOBUZZ, p. 81)

| Application | Minimum wire size |
|---|---|
| 12V main battery power · Motor power (unless listed below) · 11–20 A fuse-protected circuit | **18 AWG** (19 SWG / 1 mm²) |
| Motor power for **TETRIX MAX 12V DC** and **REV Core Hex** · PWM / servo · LEDs (5V/12V) · ≤10 A fuse-protected circuit | **22 AWG** (22 SWG / 0.5 mm²) |
| Signal-level circuits (≤1 A continuous from a source incapable of >1 A: I2C, DIO, analog, encoder, RS485) | **28 AWG** (29 SWG / .08 mm²) |

- *"Integrated wires originally attached to legal COTS devices or wires included/sold by the manufacturer are
  considered part of the device and by default legal. Such wires are exempt from this rule."*
- *"Combining multiple smaller wires in parallel cannot be used to create an equivalent larger wire."*
- **Buy wire with printed gauge markings.** The manual asks teams to *demonstrate* compliance for unlabeled
  wire. Unmarked spool wire is a slow, avoidable inspection argument.
- **V0-ERRATA:** Table 12-8 writes the Core Hex as **REV-14-1300**; Table 12-1 says **REV-41-1300**. The
  Table 12-1 number is the real REV SKU (verified on the vendor page). Do not search for REV-14-1300.

### 6.8 Wire colours — R610 (CONFIRMED-BIOBUZZ, p. 82)

The **12V main power bus and +5V auxiliary bus** must be colour-coded **along their entire length**:
- **Positive (+12VDC / +5V Aux):** red, yellow, white, brown, or black-with-stripe.
- **Negative (common/GND):** black or blue.

Does **not** apply to motor wiring, signal wiring, servo cables/extensions, or manufacturer-attached wires.

**Purchasing consequence:** buy **red and black** 18 AWG for the main bus. Do not economise with a single
colour and heat-shrink markers.

### 6.9 Custom circuits and the rules that ban common shop fixes

| Rule | Page | What it bans that people try to buy |
|---|---|---|
| **R607** | 80 | CUSTOM CIRCUITS must not output **regulated voltage above 5V**, *except solely for powering LEDs*. Unregulated battery voltage may pass through. |
| **R611** | 82 | Powered USB hubs may draw power **only** from an approved COTS USB battery pack (R602) or the **5V aux port** on a REV hub. |
| **R612** | 82 | CUSTOM CIRCUITS must not alter power/control paths between battery↔switch, switch↔regulator, regulator↔regulator, or regulator↔actuator. **Boost and buck converters in a power path are explicitly prohibited.** Blue box names the **goBILDA Servo Travel Tuner** as a prohibited device. |
| **R613** | 82-83 | **A.** sensors/encoders powered solely by the regulator they connect to — no second hub, no custom circuit. **B.** power from a port may only feed that port; **no cross-wiring, no combining ports into a bus.** **C.** 6V from servo power modules/injectors **may power servos only**. **D.** the +5V Aux port may power devices not connected to other regulators except via USB. |
| **R604** | 79 | Fuses used as directed; **no higher-trip-point or self-resetting replacements**. |
| **R606** | 80 | All power regulating devices, wiring and fuses must be **made visible for inspection**; RC diagnostic lights/screen must be visible. Not required during a match, but you must be able to expose them. |

**Purchasing consequence:** **do not buy a BEC / buck converter / voltage regulator to run a 12V LED strip or
a 5V accessory off the main bus.** goBILDA sells a "Voltage Regulators (BECs)" category
([electronics index verified](https://www.gobilda.com/electronics/)); that category is a **trap** for FTC —
R612 prohibits altering a power path with a boost or buck converter. Power accessories from the hub's
**+5V Aux** port (R613.D) or from an isolated R602 USB pack instead. And **design panel access into the
chassis** so R606 can be satisfied without disassembly.

---

## 7. PNEUMATICS AND AIRFLOW DEVICES — R801 (CONFIRMED-BIOBUZZ, p. 87)

> **A.** *"ROBOTS may only use sealed, COTS closed-air systems which are pre-charged by the manufacturer
> (such as gas shocks),"*
> **B.** no stored-pressure components actuated by a device like a solenoid or able to change stable state,
> **C.** *"ROBOTS may not generate pressure or vacuum,"*
> **D.** no user-adjustable gas storage vessels, **except air-filled (pneumatic) COTS wheels**,
> **E.** no device creating high-speed airflow, **except cooling fans integrated into COTS computing devices**.
>
> Blue box: *"robots may not use pneumatic actuators, pressure or vacuum storage devices, compressors,
> vacuum generators, or air blowers, but they may use 'closed air' systems which were sealed by their
> manufacturer. This includes items such as **gas springs, and dampers**."* Also: *"High-speed flywheels or
> rollers used for manipulating SCORING ELEMENTS would not on their own be considered a high-speed airflow
> device."*

Reinforced by **R204** (p. 69): *"No grabbing the floor. ROBOTS may not use any mechanism which is designed
to increase downforce by either grabbing FIELD surfaces or by using some form of generated airflow to provide
downward suction."*

| ❌ Do not buy / do not propose | ✅ Legal and available |
|---|---|
| Pneumatic cylinders, air tanks, compressors, solenoid valves, tubing/fittings kits | **COTS gas springs / gas shocks / dampers** — pre-charged and sealed by the manufacturer (R801.A) |
| Vacuum pumps, venturi generators, suction cups | Constant-force springs, extension/compression/torsion springs, surgical tubing |
| Blower fans, ducted fans, EDF units for moving game elements | **Cooling fans integrated into COTS computing devices** (R801.E) |
| Vacuum-assisted downforce ("wheelie" suction skirts) | **Air-filled COTS pneumatic wheels** (R801.D exception) |
| — | **High-speed flywheels/rollers** for element manipulation (blue box, explicitly not airflow devices) |

**Purchasing consequence for a modest-budget two-robot program:** the entire pneumatics aisle at every FTC
vendor is off the table. This is *good news* for duplicability — pneumatics doubles poorly. **Gas springs are
the sanctioned zero-actuator-slot energy store; specify them by force rating and stroke, and buy four
identical ones so both robots match.**

---

## 8. FABRICATION vs COTS — the definitions that decide what you may build now

### 8.1 The three defined categories (CONFIRMED-BIOBUZZ, pp. 64-66)

| Term | Manual definition (abridged) | Buying consequence |
|---|---|---|
| **COTS item** | *"a standard (i.e., not custom order) part commonly available from a VENDOR for all teams for purchase … in an unaltered, unmodified state (with the exception of installation or modification of any software)."* Discontinued items that remain functionally equivalent to as-delivered still count as COTS. | The moment you drill it, it stops being COTS. |
| **FABRICATED ITEM** | *"any COMPONENT or MECHANISM that has been altered, built, cast, constructed, concocted, created, cut, heat treated, machined, manufactured, modified, painted, produced, surface coated, or conjured partially or completely into the final form in which it will be used."* | Anything your team makes, or has made to your drawing. |
| **Neither** (raw material) | *"a 20 ft. length of aluminium which has been cut into 5 ft. pieces by the team for storage or transport is neither COTS … nor a FABRICATED ITEM (the cuts were not made to advance the part towards its final form)."* | Stock cut only for storage/transport stays raw material. |

The manual's five worked examples are the practical test (p. 64-65): a drilled panel becomes a FABRICATED
ITEM while its undrilled twin stays COTS; a machine shop copying published drawings does **not** produce a
COTS part *"because it is not commonly carried as part of the standard stock"*; drawings themselves are COTS
and usable as raw material, but the gearbox you build from them is a FABRICATED ITEM; **non-functional label
markings keep a part COTS, but adding device-specific mounting holes makes it a FABRICATED ITEM**; a
discontinued-but-functionally-equivalent COTS gearbox is still usable.

### 8.2 VENDOR — who you may buy from (CONFIRMED-BIOBUZZ, pp. 65-66)

A VENDOR must: **A.** have a Federal Tax ID (or equivalent national business registration);
**B.** not be a wholly owned subsidiary of a FIRST team or collection of teams;
**C.** maintain sufficient stock/production capability to ship general product timely — the manual's own
example uses **5 business days** for shelf stock; **D.** make products available to **all** FTC teams.

Worked example (p. 65): a vendor cutting and welding belting to a custom length produces a **FABRICATED
ITEM** and a 2-week lead time is acceptable; if instead they ship a raw length from shelf stock (a COTS
item) it must arrive within 5 business days and the team does the welding.

**Purchasing consequence:** buying from a hobby shop, McMaster-Carr, a local metal supplier or a general
industrial distributor is fine — they all meet the VENDOR test. Buying a purpose-built mechanism from a
one-team-affiliated micro-business does **not**.

### 8.3 What may be modified — R302 (CONFIRMED-BIOBUZZ, p. 70)

> *"Allowed raw materials and legal COTS parts can be modified (drilled, cut, painted, etc.) as long as no
> other rules are violated."* Raw materials include **sheet stock, extruded shapes, metals, plastic, rubber,
> wood, and magnets.**

**But R504 and R706 override this for actuators and control-system devices.** You may drill a goBILDA
channel; you may not drill a Control Hub. **Magnets are explicitly a legal raw material** — useful for
detent, alignment and passive-latch designs that cost zero actuator slots.

### 8.4 COTS MECHANISM limits — R301 and R303 (CONFIRMED-BIOBUZZ, pp. 69-71)

**R301:** *"COTS MAJOR MECHANISMS purposefully designed to complete a game task are prohibited."* Exceptions:
**A.** COTS drive CHASSIS, and **B.** COTS MAJOR MECHANISMS created as part of the official FIRST Tech
Challenge **StarterBots**. Blue box: *"A vendor selling 'build to print' manufacturing of publicly available,
purpose-built solutions is against the spirit of this rule."*

**R303:** COTS components and mechanisms **must not exceed a single degree of mechanical freedom.**
Explicitly allowed single-DoF COTS items: **linear slide kit · linear actuator kit · single-speed
(non-shifting) gearboxes · pulley · turntable · lead screw · single-DoF gripper.**
Explicit exceptions to the single-DoF limit: **ratcheting devices (wrenches, bearings, etc.) · holonomic
wheels (omni or mecanum) · dead-wheel odometry kits · items transferring motion between misaligned
components (universal joints, flexible shaft couplers) · items connecting structures at variable angles
(ball joint linkages, rod ends).**

Blue box: *"grippers that incorporate additional actuators providing additional twisting and/or bending
actions (like a wrist) add degrees of freedom that are prohibited in COTS MECHANISMS."*

**Purchasing consequence — this is the key COTS shopping map:**

| ✅ You may buy this as a kit | ❌ You must build this yourself |
|---|---|
| **Linear slide kits** (viper-slide-style) — [goBILDA](https://www.gobilda.com/electronics/) is the usual family; **NEEDS-SKU-CHECK** | A multi-jointed arm-with-wrist assembly sold as one product |
| **Linear actuator kits, lead screws, pulleys, turntables** | A purpose-built game-task mechanism from any vendor |
| **Single-speed gearboxes** | A shifting/two-speed gearbox |
| **Single-DoF grippers** | A gripper with an added wrist or twist actuator |
| **Dead-wheel odometry kits** (explicit exception) | — |
| **Omni and mecanum wheels** (explicit exception) | — |
| **A complete COTS drive chassis** (R301.A) | Any other COTS MAJOR MECHANISM |
| **Official FIRST StarterBot mechanisms** (R301.B) | — |

**R101** (p. 66) sits behind all of this: the ROBOT and its **MAJOR MECHANISMS** must be built by the
registered team. Gearbox assemblies, sub-mechanisms of a major mechanism, and COTS items are explicitly **not**
subject to R101 — so buying a slide kit and building your lift around it is squarely legal.

### 8.5 ⚠ R304 vs R305 — a correction to the workflow brief

**The pre-Kickoff allowance is R304, not R305.** Verified by direct PDF extraction of **page 71**:

> **R304** \*Custom software, designs, and parts can be reused year-to-year. ROBOT software, designs, and
> FABRICATED ITEMS created before Kickoff are permitted.
>
> **R305** \*SCORING ELEMENTS are not allowed for ROBOT construction. Current season SCORING ELEMENTS or
> replicas of SCORING ELEMENTS are not allowed to be used as part of ROBOT construction.

(The layout-preserved text dump interleaves the two rule-ID labels above the two rule texts, which is what
makes the .txt look as though R305 carries the pre-Kickoff clause. It does not. **Cite R304.**)

### 8.6 What R304 legitimately lets you build **right now**, before 12 September 2026

This is the most actionable rule in Section 12 for a team standing 22 days from Kickoff. R304 has **no
"only if"** conditions attached — software, designs and FABRICATED ITEMS created before Kickoff are
permitted. Combined with the fact that **Section 12 is final** and **R102's 18-inch cube is known**, the
following are all safe to build today:

| Build now under R304 | Why it's safe | Rules it must still satisfy |
|---|---|---|
| **A complete drivetrain, both robots** | R102's 18 in. cube is final; no expansion rule applies to a drivetrain that stays inside the starting envelope | R102, R201 (non-damaging traction), R303.I (mecanum/omni OK), R503 motor budget |
| **The full electrical harness and control-system layout** | Every electrical rule in §12.6/12.7 is final | R601, R603, R605, R606, R609, R610, R613 |
| **A wiring/battery/switch "electrical plate" sub-assembly ×2** | Fabrication now, bolt-on later | R606 inspectability |
| **ROBOT SIGNS ×4** (2 per robot) | R401-R403 are final; the official template is already published | R401, R402, R403 |
| **OPERATOR CONSOLE boxes ×2** | R901-R903 are final, including the volume | R902, R903 |
| **Odometry pods / dead-wheel mounts** | R303.J is an explicit exception | R303.J |
| **Software: drive base, odometry, autonomous framework, vision pipeline, telemetry** | R304 covers software explicitly | R702 (don't reprogram non-Table-12-9 coprocessors), R704.D (no Dashboard on the RC network) |
| **Test rigs, jigs, print fixtures, spare-part inventory** | Not robot parts at all | — |
| **A parameterised CAD library of brackets/mounts** | Designs are explicitly covered | — |

**What you must NOT build yet:**
- Anything whose geometry depends on **R105 expansion limits** — lift heights, extension reach, arm lengths.
- Anything sized to a **SCORING ELEMENT** — intakes, grippers, hoppers, magazines.
- Anything sized to a **FIELD element** — the ARENA section is a placeholder.
- Anything using **current-season SCORING ELEMENTS or replicas** as robot structure — **R305 forbids it
  outright**. Buy game pieces for *practice*; they are a practice consumable, never a BOM row.

**Duplicability note (JUDGMENT):** R304 is worth roughly three weeks of build season to a two-robot program,
because the doubled work — two drivetrains, two harnesses, two consoles, four signs — is precisely the work
that is **game-independent**. Front-load the doubling now, and Kickoff week is spent on the one mechanism
that actually depends on the game.

---

## 9. ROBOT SIGNS — Section 12.4

### 9.1 The rules (CONFIRMED-BIOBUZZ, pp. 71-74)

**R401** — **minimum two ROBOT SIGNS per ROBOT**, in at least 2 separate locations, *"on opposite or adjacent
surfaces of the ROBOT, ≥90 degrees apart."* Any surface visible to FIELD STAFF may be used, including the top.
Each sign must:
**A.** be made of a **robust material**, **B.** minimally **6.5 in. (16.5 cm) wide**,
**C.** minimally **2.5 in. (6.4 cm) tall**, **D.** be **supported by the structure/frame of the ROBOT**.
Intent: legible *"from at least 12 feet (3.65 meters) away."*

**R402** — each sign must contain a rectangle with a **solid red or blue opaque background at least
6.5 in. × 2.5 in. (16.50 cm × 6.35 cm)** indicating alliance colour as assigned in the match schedule.
Only these other markings are permitted: those required by R403; small amounts of hook-and-loop tape, hard
fasteners or equivalents; narrow differing-colour areas at corners/folds/cutouts; narrow template markings;
and **E. the sign cannot be powered or rely on power to illuminate/reveal the alliance colour.** Reversible
or configurable signs must not let the opposite colour show.

**R403** — team numbers must be: **A.** solid opaque **white Arabic numerals approximately 2.25 in.
(5.70 cm) tall**, **B.** with a minimum of approximately **0.25 in. (0.60 cm) of background surrounding**
them, **C.** **not vertically stacked**, **D.** robust material, **E.** **not powered or reliant on power.**
Prohibited examples given: *"team numbers only visible by edge lit engraved plastic"* and *"LED Display
numbers."* If no legal sign and no colour printer is available at an event, the Head REFEREE may approve a
substitute; handwritten-on-plain-paper is explicitly acceptable as a fallback.

### 9.2 Cross-check against the official template — VERIFIED this session

I opened `manuals/archive/supplemental/2026-27_BIOBUZZ_RobotSign_USLetter.pdf` with PyMuPDF and measured its
vector geometry directly:

- **1 page, US Letter (612 × 792 pt = 8.50 × 11.00 in).**
- **Four filled rectangles, each exactly 6.50 in. × 2.50 in.** — **two pure blue (RGB 0,0,255)** and
  **two pure red (RGB 255,0,0)**.
- **No text layer** — the numerals are yours to add.

**This exactly matches R401.B/C and R402's minimum rectangle.** One printed sheet yields a **complete set for
one robot in both alliance colours** (2 red + 2 blue). **Two robots ⇒ 2 sheets minimum**; print spares.

### 9.3 The sign requirement designers forget

R401.D — signs must be **supported by the structure/frame of the ROBOT** — and R401's 90-degree placement
rule together mean **two 6.5 × 2.5 in. flat, unobstructed, frame-backed mounting areas on perpendicular faces
must be reserved in the 18-inch cube from the first CAD session.** Discovering at inspection that both
candidate faces are occupied by a mechanism is a classic and entirely avoidable failure.

### 9.4 ROBOT SIGN purchasing table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Official sign template | FIRST | `2026-27_BIOBUZZ_RobotSign_USLetter.pdf` (A4 also published) | 1 file | 1 file | **free** | — | **VERIFIED** (measured this session) | Already on disk at `manuals/archive/supplemental/`. 4 rectangles, 6.50 × 2.50 in, 2 red + 2 blue. |
| Colour printing | any | Colour laser/inkjet on card stock or photo paper | 1 sheet | **2+ sheets** | ~$1 | **Fab** | JUDGMENT | R403's fallback allowance shows FIRST expects printed signs. Print spares — signs get destroyed. |
| Sign substrate | any (raw material per R302) | 1/16 in. polycarbonate, ABS, or 3D-printed plate | 2 | **4** | ~$2–5 ea | **Fab** | JUDGMENT | R401.A "robust material" is deliberately vague. Laminate + rigid backer is the reliable answer. |
| Reversible red/blue mount | any | Hook-and-loop tape or hard fasteners | 2 sets | 4 sets | ~$5 | **Fab** | **CONFIRMED-BIOBUZZ** — R402.B explicitly permits *"small amounts of hook-and-loop tape, hard fasteners, or functional equivalents"* | A flip/swap mount is legal **provided the opposite colour is never visible** (R402). |
| ❌ Backlit / LED / edge-lit numbers | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **Explicitly prohibited by R402.E and R403.E.** Named examples: edge-lit engraved plastic, LED display numbers. |

---

## 10. OPERATOR CONSOLE — Section 12.9

### 10.1 The rules (CONFIRMED-BIOBUZZ, pp. 87-88)

**R901** — the OPERATOR CONSOLE may have **only one approved Android-based DRIVER STATION device connected
and powered on**, and must have at least one of:
**A.** **REV Driver Hub (REV-31-1596)**, or
**B.** *"Any Android Device with or without any combination of USB cables (including USB OTG cables) and/or
USB hubs (powered or unpowered, with or without OTG integrated into the hub) for connecting one or more
gamepads."*
Blue box: the **REV Driver Hub is the only officially supported DS device.** A **spare DS device is allowed**
as long as only one is connected and powered on at a time.

**R902** — the DS **touch screen must be accessible**, clearly visible during inspection and in a match, and
*"functional without the requirement of additional aides (e.g., mouse)."*

**R903** — the OPERATOR CONSOLE, **including all power sources (e.g. power banks)**, must not exceed
**3 ft wide × 1 ft 6 in deep × 2 ft tall (91.4 × 45.7 × 61.0 cm)**, excluding items held or worn by drivers.
Blue box: **no hard weight limit, but over 20 lbs (~9 kg) invites extra scrutiny.** A **spare external USB hub
is allowed** if only one is connected at a time. Intent: *"to allow teams to use a container to store,
organize, and transport the DRIVER STATION device and support electronics. The OPERATOR CONSOLE rules are not
intended to allow systems that function as a ROBOT cart."*

**R904** — no wireless communication to/from/within the OPERATOR CONSOLE other than the RC↔DS app connection.
*"Examples of prohibited wireless systems include… active wireless network cards and Bluetooth devices."*

Also applies: **R202** (p. 68) — consoles must not use hazardous materials, be unsafe, or interfere with
other robots or FIELD STAFF; explicitly bans *"shields, curtains, or any other devices solely designed or
used to limit the vision of any DRIVE TEAM members"* and distracting audio devices.

### 10.2 Gamepads — a V0-GAP worth knowing about

**BIOBUZZ V0 contains no gamepad allowlist.** The only mention of gamepads in the whole manual is R901.B's
*"for connecting one or more gamepads."* I grepped the full V0 text — one hit. Prior seasons carried a
gamepad table.

**Purchasing consequence:** V0 imposes **no restriction on gamepad make/model or count** beyond R904 (must be
**wired**, not Bluetooth) and R903 (must fit the console volume). **JUDGMENT: assume the allowlist returns at
Kickoff and buy conservatively** — a USB-wired, historically-allowed controller. Do not stockpile exotic
custom control panels before 12 September.

### 10.3 OPERATOR CONSOLE purchasing table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| DRIVER STATION | REV Robotics | **Driver Hub — REV-31-1596** | **1** | **2** | **$275.00** | Buy | **VERIFIED** | R901.A. Only officially supported DS. **$550 for the program.** |
| DS battery (spare) | REV Robotics | Driver Hub Battery — REV-31-1876 | 1 | 2 | **$21.75** | Buy | **VERIFIED** | R903 counts power banks toward console volume. |
| Gamepad | REV Robotics | **USB PS4-Compatible Gamepad — REV-31-2983** | **2** | **4** | **$26.00** | Buy | **VERIFIED** | **Wired USB — R904 bans Bluetooth.** Two drivers per team. Buy spares; gamepads fail. |
| USB hub | any | Powered or unpowered USB hub, OTG optional | 0–1 | 0–2 | not verified | Buy | **CONFIRMED-BIOBUZZ** (R901.B) | A **spare hub is allowed** if only one is connected (R903 blue box). If powered on the **robot**, R611 applies — on the console it does not. |
| Console enclosure | — | Toolbox / Pelican-style case / plywood box | 1 | **2** | ~$30–80 | **Fab** | JUDGMENT + **R903** | Must fit **36 × 18 × 24 in**, keep the touchscreen visible and usable (R902), and stay under ~20 lb to avoid scrutiny. **Build both now under R304.** |
| ❌ Bluetooth gamepad / wireless headset / Wi-Fi card | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R904** prohibits. |

---

## 11. COST CAP AND BUDGET RULES — there are none

**CONFIRMED-BIOBUZZ (by exhaustive search):** I grepped the entire BIOBUZZ V0 manual text for
`cost accounting`, `BUDGET`, `cost limit`, `total cost`, `individual COMPONENT cost`, `$` and `price`.

**Results:** exactly two hits, both inside the VENDOR definition's commentary on pp. 65-66 —
*"circumvent any applicable **cost accounting** rules"* and *"best **prices** and level of service available."*
**There is no cost cap rule, no per-component price limit, no total-robot budget rule, and no cost-accounting
worksheet anywhere in the BIOBUZZ V0 manual.** The phrase "any applicable cost accounting rules" is
aspirational language inherited from FRC; **no such rule exists in FTC BIOBUZZ**.

**Purchasing consequence:** the constraint on this program is **your actual money and your actual mentor
hours**, not a rule. Nothing stops a wealthier team from outspending you, and nothing requires you to
document part costs for inspection. Conversely, **there is no rule-based reason to avoid a cheaper part** —
if it satisfies R501/R502/R601/R603 and the COTS definition, price is irrelevant to legality.

**JUDGMENT — the real budget model for two robots:** the *mandatory* electronics floor is roughly
**$375 (Control Hub) + $275 (Driver Hub) + battery + switch ≈ $730 per robot ≈ $1,460 for the program**,
before a single motor, servo or piece of structure. Add 8 motors and 8 servos per robot and the actuator
line alone is several hundred dollars more per robot. **Every actuator slot you *don't* spend is money you
don't spend twice.** That is why §3.4's spring-and-ratchet advice is a budget strategy, not just a design one.

---

## 12. SIZE AND WEIGHT — what is known, and what must wait

### 12.1 What V0 says, precisely (CONFIRMED-BIOBUZZ)

| Rule | Page | Text |
|---|---|---|
| **R102** * | 67 | *"STARTING CONFIGURATION is limited to an 18-inch Cube. … all parts of the ROBOT must be fully stationary, and the ROBOT must be fully self-contained within an 18 in. (45.70 cm) wide, by 18 in. (45.70 cm) long, by 18 in. (45.70 cm) high volume."* Pre-loaded SCORING ELEMENTS may extend outside. Interchangeable mechanisms must comply **in all configurations**. |
| **R103** * | 67 | ROBOTS must be **fully self-supported** in STARTING CONFIGURATION — *"does not exert force on the sides or top of a sizing tool."* Allowed: **A.** mechanical means while powered off, and/or **B.** initialising an OpMode that pre-positions servos and motors. |
| **R104** * | 67 | *"**There is no ROBOT weight limit.** There is no explicit weight limit for FIRST Tech Challenge ROBOTS playing BIOBUZZ."* Still consider tile damage, battery consumption, transportation, performance. |
| **R105** | 68 | ROBOTS must stay as one assembly, may not intentionally detach components, may expand after the match starts — *"but are still subject to sizing constraints relative to the ROBOT, based on the initial STARTING CONFIGURATION."* → **"Sizing Constraints and more details will be released at Kickoff."** |

### 12.2 ⚠ SIZING CONSTRAINTS ARE DEFERRED TO KICKOFF

**R105 is the only R-rule in Section 12 that is explicitly incomplete.** The expansion limit — how far beyond
the 18-inch cube the robot may grow, whether the limit is horizontal, vertical or both, and whether it may be
enforced in software or must be mechanical — **is not knowable today**. Do not infer it from DECODE or ITD;
this number has moved between seasons.

### 12.3 Purchasing decisions that MUST wait for Kickoff

| Purchase | Why it must wait |
|---|---|
| **Linear slide kits — stage count and length** | The number of stages and the extended length are set entirely by R105's vertical/horizontal limit and by scoring geometry. Buying 4-stage kits ×2 robots before you know either is the most expensive guess available. |
| **Arm/boom tube lengths and pivot geometry** | Reach is bounded by R105. |
| **Any intake geometry, roller spacing, compliant wheel durometer** | Sized to the SCORING ELEMENT, which is in placeholder Section 10. |
| **Grippers, claws, hoppers, magazines** | Sized to the SCORING ELEMENT. |
| **Endgame / climbing hardware** | Sized to FIELD elements in placeholder Section 9. |
| **Gas spring force rating and stroke** | Force depends on the mass and travel of a mechanism you cannot dimension yet. |
| **Motor gear ratios for game mechanisms** | Load and speed unknown. (Ratios for the *drivetrain* are a different question — see below.) |

### 12.4 Purchasing decisions that safely CANNOT wait

Everything on this list is fixed by rules that are final today, and every one of them has to be bought
**twice**. Ordering now is the correct call; lead time is the enemy of a two-robot program.

| Purchase | Locked by | Two-robot qty |
|---|---|---|
| **Control Hubs** | R701.A | **2** |
| **Driver Hubs** | R901.A | **2** |
| **Main batteries** (+ spares for practice rotation) | R601 Table 12-4 | **4–6** |
| **Battery charger(s), ≤3 A per channel** | E511.B | **1–2 multi-bay** |
| **Main power switches** | R603 Table 12-5 | **2** |
| **Resistive grounding straps** | R605 Table 12-6 | **2** |
| **Wire: 18 AWG red/black, 22 AWG, 28 AWG signal** | R609, R610 | 1 program lot |
| **20 A ATM mini blade fuses** | R601.A | pack |
| **Drivetrain motors and wheels** | R102 (18 in. cube is final), R503 | 8 motors, 8 wheels |
| **Gamepads** (wired USB) | R901.B, R904 | **4 + spares** |
| **ROBOT SIGN stock and printing** | R401-R403 (final) | **4 signs** |
| **OPERATOR CONSOLE enclosures** | R903 (final) | **2** |
| **Structure stock** — extrusion/channel, hardware, bearings, shafts | R302 raw materials | 1 program lot |
| **Odometry pods** | R303.J | 2 sets |

**The 18-inch cube is final. That is enough to design and build both complete drivetrains, both full
electrical systems, both operator consoles and all four signs before Kickoff, under R304.** Do it.

### 12.5 One more size fact that is final

**R903's OPERATOR CONSOLE volume — 36 × 18 × 24 in — is final and is not deferred.** Measure the box you
intend to use *now*; it is the only dimensional constraint besides the 18-inch cube that you can design
against today.

---

## 13. DO-NOT-BUY LIST — parts that are for sale right now and are not legal

Every row here is something a team could plausibly add to a cart. Sources: the BIOBUZZ V0 rules
(CONFIRMED-BIOBUZZ) plus the DECODE 25-26.2 *Inspection Quick Reference* (**HISTORICAL** — the 2026-27
edition is not yet published).

| ❌ Item | Vendor / SKU | Price seen | Why illegal | Rule |
|---|---|---|---|---|
| **goBILDA Servo Travel Tuner** | goBILDA **3109-0002-0001** | **$19.99** — VERIFIED on sale 2026-08-21 | **Named by name in R612's blue box** as a prohibited device that modifies actuator control signals | **R612** (CONFIRMED-BIOBUZZ, p. 82) |
| **goBILDA Servo Power Distribution Board (8 Channel)** | goBILDA **3108-2827-0801** | **$17.99** — VERIFIED on sale | Listed under "Illegal Servo Power or Servo Signal Adjusters"; not a Table 12-3 device | R505 · **HISTORICAL** DECODE IQR p. 9 |
| **goBILDA 4-Channel Servo Extension via CAT6** | goBILDA **3802-2745-4527** | **$29.99** — VERIFIED on sale | Same list | R505 · **HISTORICAL** DECODE IQR p. 9 |
| **goBILDA Servo Speed Tuner / Servo Travel Reverser** | 3109-0009-0001 / 3109-0007-0001 | $19.99 / $13.99 — VERIFIED on sale | Same *class* of device as the Travel Tuner: alters servo control signals | R612 · **JUDGMENT** — confirm against the 2026-27 IQR |
| **Limelight 3G** | Limelight Vision | — | **Explicitly named as a prohibited programmable vision coprocessor.** Only the **3A** is in Table 12-9 | **R702 Example 6** (CONFIRMED-BIOBUZZ, p. 85) |
| **OpenMV Cam · Luxonis OAK-1** | — | — | Same example | **R702 Example 6** |
| **Any stereoscopic / depth camera** | — | — | *"stereoscopic cameras are not allowed"* | **R708** (p. 86) |
| **Any BEC / buck / boost converter in a power path** | goBILDA "Voltage Regulators (BECs)" category, others | — | R612 explicitly names boost/buck converters as altering a power pathway | **R612** (p. 82) |
| **Pneumatic cylinders, compressors, solenoid valves, air tanks, vacuum generators, suction cups, blowers** | all FTC vendors | — | *"ROBOTS may not generate pressure or vacuum"*; no pneumatic actuators | **R801** (p. 87) |
| **Relays, electromagnets, electrical solenoid actuators** | — | — | *"the use of relays and electromagnets is also prohibited"* | **R506** (p. 78) |
| **Any 12V NiMH pack not in Table 12-4; any LiPo/Li-ion main battery** | general suppliers | — | Closed allowlist by part number | **R601** (p. 78) |
| **Battery chargers exceeding 3 A average channel current** | general suppliers | — | *"Never charge batteries on a battery charger that exceeds a 3-amp average channel current"* | **E511.B** (p. 39) |
| **AndyMark am-2256 HiGrip wheels · am-3309 Roughtop tread · Gorilla Anti-Slip Tread Tape** | AndyMark, general | — | Known FIELD-TILE-damaging traction devices — **illegal on any surface touching the tiles** (the parts themselves are not wholly illegal) | R201 · **HISTORICAL** DECODE IQR p. 10 |
| **High-torque bargain servos** — e.g. AGFRC A73BHLW V2, DSSERVO DS3225PRO, Hitec HS-805BB, Smraza SC55-NA | general suppliers | — | Exceed the stall-current or 8 W mechanical-power limit | R502 · **HISTORICAL** DECODE IQR p. 6 |
| **Custom 3D-printed Control Hub / Driver Hub enclosures** | — | — | *"removing enclosures and replacing with custom enclosures"* is explicitly listed as prohibited tampering | **R706** (p. 85) |
| **LED / edge-lit / powered ROBOT SIGN numbers** | — | — | Signs *"cannot be powered or rely on power"* | **R402.E, R403.E** (pp. 72-73) |
| **Bluetooth gamepads, wireless headsets, Wi-Fi cards in the console** | — | — | No wireless other than the RC↔DS app connection | **R904** (p. 88) |
| **FTC Dashboard / FTControl Panels as a match-day tuning workflow** | free software | — | *"third party plugins and tools such as FTC Dashboard, FTControl Panels, and others are prohibited"* on the RC Wi-Fi network | **R704.D** (p. 85) |

---

## 14. PRE-PURCHASE LEGALITY CHECKLIST

Run this before **any** part enters a cart. Ten questions, each mapped to the rule that answers it.
If a question can't be answered from a vendor page or a datasheet, **don't buy it yet**.

### 14.1 The ten questions

| # | Question | Check against | Fail consequence |
|---|---|---|---|
| **1** | **Is it a motor?** If yes — is the exact manufacturer + part number in **Table 12-1**? | **R501**, p. 75 | Closed allowlist. Not on it ⇒ illegal, no appeal. |
| **2** | **Is it a servo?** If yes — is it one of the 10 named in **Table 12-2**? If not, do I have a manufacturer datasheet showing **≤8 W** mechanical output at 6V *and* stall current within the (currently blank) limit? Linear servo ⇒ **≤1 A @6V**. | **R502**, p. 76 | Spec test, not a list. **No datasheet ⇒ no purchase.** Working stall-current number: **4 A (HISTORICAL)**. |
| **3** | **Does it add to the actuator count?** Recount **all** motors and servos across **all** configurations and spare mechanisms. Still ≤ **8 and 8**? | **R503**, p. 77 · **I302**, p. 24 | Over budget ⇒ redesign, not re-buy. |
| **4** | **Is it electrical and not an actuator?** Then: is it a **power regulating device in Table 12-3**? Is it powered the way **Table 12-7** demands (main battery, correct connector)? Does it stay within **R607** (≤5V regulated, except LEDs) and **R612** (no boost/buck in a power path)? Does it avoid **R613** (no cross-port power, 6V for servos only)? | **R505, R607, R608, R612, R613**, pp. 77-83 | The single most common invalid purchase category. |
| **5** | **Does it connect by USB?** Only **webcams/optical vision per R708**, a **USB hub or switch**, or a **REV Expansion Hub** may. Is it a **single image sensor**? Is it in **Table 12-9** if it's a programmable vision coprocessor? | **R707, R708, R702**, pp. 84-86 | **Limelight 3A yes, 3G no.** Stereo cameras no. |
| **6** | **Is it a battery, charger or power switch?** Main battery ⇒ **Table 12-4** by part number. Switch ⇒ **Table 12-5** by part number. Charger ⇒ **≤3 A average channel current**. Aux battery ⇒ **R602** limits and isolation. | **R601, R603**, pp. 78-79 · **E511**, p. 39 | Closed allowlists. |
| **7** | **Is it a COTS MECHANISM?** Does it exceed **one degree of freedom**? Is it a **COTS MAJOR MECHANISM purpose-built for a game task**? | **R303, R301**, pp. 69-71 | Slide kits, lead screws, turntables, single-DoF grippers, odometry pods, omni/mecanum wheels are fine. Wristed grippers and shifting gearboxes are not. |
| **8** | **Will I modify it?** Motor/servo ⇒ only the **R504.A-G** list. Control-system device, switch, fuse or battery ⇒ only the **R706.A-K** list. Raw material or ordinary COTS part ⇒ **R302** allows drilling/cutting/painting. | **R504, R706, R302**, pp. 70, 77, 85 | Modifying a hub, a battery or a servo beyond the manufacturer's own allowance is an instant inspection failure. |
| **9** | **Does it touch the FIELD TILES, shed material, or create a hazard?** Abrasive tread? Loose ballast? Lubricants? Exposed sharp edges? Entanglement risk? Lighting over 5 Hz or high-intensity? AprilTag-like imagery? | **R201, R202**, pp. 68-69 | R202 also bans flame/pyrotechnics, hazardous materials, animal-based materials, and anything designed to damage or flip other robots. |
| **10** | **Does it move air, store pressure, or pull vacuum?** Anything not a **manufacturer-sealed pre-charged closed-air device** (gas spring/damper), a **COTS pneumatic wheel**, or a **cooling fan integral to a COTS computing device**. | **R801**, p. 87 · **R204**, p. 69 | Whole product categories are out. |

### 14.2 Two-robot cross-checks (JUDGMENT — specific to this program)

- **11. Can I buy two?** Check stock, not just legality. The **REV Expansion Hub** was **out of stock on 2026-08-21**
  and showed **limited stock on 2026-08-22** — a one-day swing, so re-check at order time rather than trusting
  any status in this document. The **REV Servo Power Module** and **REV Smart Robot Servo** are **discontinued**. A part that
  is legal but unobtainable in quantity 2 is not a part you can design both robots around.
- **12. Is it end-of-life?** Table 12-1 already flags **Modern Robotics/MATRIX (5000-0002-0001)** and
  **TETRIX MAX (739530/39530)** as discontinued. The COTS definition (p. 64) says discontinued-but-
  functionally-equivalent parts remain legal — so an EOL part is legal to *use*, just not to *plan around*.
- **13. Does it double cleanly?** If the part needs individual tuning, shimming or hand-fitting, you will do
  that work twice with limited mentor hours. Prefer the part that bolts on identically to both robots.
- **14. Have I priced the *pair*?** Every line in a BIOBUZZ BOM is ×2. $375 Control Hub is a $750 decision.
  $275 Expansion Hub is a $550 decision — see §5.2 before spending it.

### 14.3 Kickoff-day (2026-09-12) purchasing actions

1. **Read R105 first** — record the expansion limit. Every deferred purchase in §12.3 unblocks from that
   one number.
2. **Diff Table 12-2** — find the servo stall-current value. If still blank, **file a Q&A when Game Q&A opens
   2026-09-28, 12:00 p.m. ET**.
3. **Diff Table 12-1 and Table 12-9** for added/removed motors and vision coprocessors.
4. **Confirm R503 still reads 8 and 8.** Team Updates have changed actuator counts mid-season before.
5. **Download the 2026-27 Inspection Quick Reference and Inspection Checklist the moment they post**, and
   re-run §14.1 questions 2, 4 and 9 against your entire servo, electronics and traction BOM.
6. **Search the Kickoff manual for "gamepad"** — if the allowlist returned, re-check what you bought.
7. **Re-read R704.D** and lock the tuning workflow before writing tuning code.
8. Order the deferred long-lead items (slide kits, gas springs) **the same day**.

---

## 15. Sources

### 15.1 Primary — BIOBUZZ V0 (all rule text, tables and page numbers above)

- `manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf`
  — §12 pp. 64-88 (re-extracted with PyMuPDF for every table); I301-I302 p. 24; E511 p. 40; §5.1 p. 33;
  Glossary p. 92.
- `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` — used for
  full-manual keyword searches (cost/budget, Android version, gamepad, charger).
- `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`
  — ⚠ column-shifted in five places; see §0.3.
- `manuals/archive/supplemental/2026-27_BIOBUZZ_RobotSign_USLetter.pdf`
  — vector geometry measured directly this session; see §9.2.

### 15.2 Prior season — HISTORICAL only

- `manuals/archive/supplemental/2025-26_DECODE_Competition_Manual_TU32.html`
  — R503 servo count (10), Table 12-2 stall current (≤4 A), Tables 12-1/12-3/12-4/12-9 for the diff.
- `manuals/archive/supplemental/2025-26_DECODE_InspectionQuickReference.pdf`
  — pre-verified servos (pp. 4-5), known-illegal servos (p. 6), illegal servo signal/power adapters (p. 9),
  illegal traction devices (p. 10).

### 15.3 Vendor pages loaded with WebFetch on 2026-08-21 — VERIFIED

| URL | What it verified |
|---|---|
| https://www.revrobotics.com/ftc/electronics/ | Servo Hub $90 · Driver Hub $275 · Driver Hub Battery $21.75 · 9-Axis IMU $38 · Gamepad REV-31-2983 $26 · bundles · repair services |
| https://www.revrobotics.com/rev-31-1595/ | **Control Hub $375.00, In Stock** |
| https://www.revrobotics.com/rev-31-1153/ | **Expansion Hub $275.00** — OUT OF STOCK 2026-08-21; **re-checked 2026-08-22: orderable, limited stock** |
| https://www.revrobotics.com/rev-31-1230/ | SPARKmini $35.00, In Stock, motor controller |
| https://www.revrobotics.com/rev-11-1144/ | Servo Power Module $48.88 (was $57.50), **Discontinued**, 6 ch, 6V |
| https://www.revrobotics.com/rev-41-1291/ | HD Hex Motor $22.00, In Stock |
| https://www.revrobotics.com/rev-41-1300/ | Core Hex Motor $32.00, In Stock |
| https://www.revrobotics.com/rev-41-1097/ | Smart Robot Servo $25.50, **Discontinued**, 13.5 kg·cm, 2 A stall |
| https://www.revrobotics.com/rev-31-1302/ | 12V Slim Battery $60.00, In Stock |
| https://www.revrobotics.com/rev-31-1387/ | Switch Cable & Bracket $13.00, In Stock, 20 A+ @12V, XT30 |
| https://www.gobilda.com/servo-electronics/ | Servo Power Injector 3125-0001-0001 **$69.99**; Travel Tuner $19.99; Servo Power Distribution Board $17.99; 4-Ch CAT6 Extension $29.99; programmers |
| https://www.gobilda.com/12v-batteries/ | 12V Battery 3100-0012-0020 **$64.99** |
| https://www.gobilda.com/yellow-jacket-planetary-gear-motors/ | 5202/5203 $54.99; 5204 $56.99 |
| https://www.gobilda.com/electronics/ · /motors/ · /servos/ · /batteries/ · /switches/ | Category structure only — **no prices rendered**; FAMILY-ONLY |
| https://ftc-resources.firstinspires.org/ftc/event/inspection-reference | **"2026-2027 FIRST® Tech Challenge Resource Coming Soon!"** — 1 page, no content |
| https://www.andymark.com/collections/first-tech-challenge | Page loads; BIOBUZZ season section present; **no part numbers or prices extracted** |
| https://www.studica.com/studica-robotics | **HTTP 403 Forbidden — BLOCKED this session** |

### 15.4 Vendor status for the record

| Vendor | Status | Fetchable this session |
|---|---|---|
| **AndyMark** | **Official FIRST supplier** | Partially — category page only, no prices |
| **goBILDA** | General supplier, deeply integrated with FTC | Yes — product-level prices on some categories |
| **REV Robotics** | General supplier; **sole source of the mandated ROBOT CONTROLLER and DRIVER STATION hardware** | Yes — full product-level detail |
| **Studica** | **Official FIRST supplier** | **No — HTTP 403** |
| **ServoCity / Actobotics** | General supplier (same parent as goBILDA) | Not fetched this session |
| **FIRST Tech Challenge storefront** | Official — apparel/season materials, not robot parts | Fetched, returned no usable content |

---

## 16. Known gaps in this document

| # | Gap | Resolution |
|---|---|---|
| G1 | **Servo stall-current limit is blank in V0 Table 12-2.** | Working number **4 A** (HISTORICAL). Confirm at Kickoff; Q&A on 2026-09-28 if still blank. |
| G2 | **2026-27 Inspection Quick Reference not published.** | Download on Kickoff day; it carries the pre-verified servo list, known-illegal servos, illegal servo adapters, illegal traction devices, and RC/DS wiring diagrams. |
| G3 | **AndyMark and Studica prices unverified.** | Their motors, servos, batteries and switches are **legal** (Table 12-1/12-2/12-4/12-5) but no price or stock is asserted here. Re-verify before ordering. |
| G4 | **No SKU asserted for linear slide kits, gas springs, wheels, extrusion or structural hardware.** | Deliberate — these are the §12.3 deferred purchases. Families named, SKUs left as NEEDS-SKU-CHECK. |
| G5 | **R105 expansion limit unknown.** | Kickoff, 2026-09-12. |
| G6 | **No gamepad allowlist in V0** (V0-GAP). | Re-search the Kickoff manual for "gamepad". |
| G7 | **No minimum Android OS version in V0** (V0-GAP; DECODE required Android 7). | Re-search for "Android"/"smartphone" at Kickoff. |
| G8 | **V0-ERRATA carried forward:** blank servo stall current (Table 12-2); Core Hex written **REV-14-1300** in Table 12-8 vs **REV-41-1300** in Table 12-1; R710.B's second IEC/EN standard number does not render; R601.A points at R610 (wire colours) for fuse installation; R612.C points at R607 instead of R505 (R607 is the ≤5V CUSTOM CIRCUIT rule; the device list is R505) — **both mis-pointers re-confirmed 2026-08-22**; and R401.C gives the sign height as 2.5 in. (**6.4 cm**) while R402 gives the same dimension as **6.35 cm**. | Check **Team Update 00** on the first Thursday after Kickoff. |

---

*Document generated 2026-08-21 against BIOBUZZ Competition Manual **V0** (2026-07-31); **rules, tables and
headline prices re-verified 2026-08-22** (see the revision note at the top). Section 12 is FINAL;
sizing constraints (R105) are not. **All prices are as of August 2026 and are VERIFY-BEFORE-ORDER.***
