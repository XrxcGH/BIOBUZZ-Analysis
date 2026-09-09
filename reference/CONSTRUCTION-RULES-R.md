# BIOBUZZ (2026-27) ROBOT Construction Rules (Section 12 / R-rules) — Design & Inspection Reference

**Status: Section 12 is ALREADY FINAL in the BIOBUZZ Pre-Season V0 manual.** Unlike Sections 8-11, 13 and 15
(which are Kickoff placeholders), Section 12 is fully written. Everything below is actionable **now**, before
the 12 September 2026 Kickoff — with exactly one deferred rule (R105) and a short list of documented gaps.

**Primary source:** `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf`
(pp. 64-88; text extract at `.../sections/12_RobotConstruction_R_p64-88.txt`).
**Diff baseline:** `.../manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf` §12, pp. 119-152 (V6, post-TU32).

---

## 0. How to read this document

| Label | Meaning |
|---|---|
| **[V0-FINAL]** | Present and complete in BIOBUZZ V0 Section 12. Treat as a BIOBUZZ number/rule. |
| **[V0-DEFERRED]** | V0 explicitly says the detail is released at Kickoff. |
| **[V0-GAP]** | Present in DECODE, absent from V0, with no explanation. May be a deliberate deletion or a Kickoff insertion. **UNVERIFIED** which. |
| **[V0-ERRATA]** | Apparent defect in V0 (missing value, bad cross-reference). Verify against the Kickoff manual / Team Update 00. |
| **[PRIOR]** | Prior-season fact (DECODE / ITD / prior Q&A). **Not** a BIOBUZZ number unless separately confirmed. |
| **[INFER]** | My inference. Not a rule. |

### 0.1 The single most useful structural fact in Section 12

FIRST marks **"Evergreen" rules** — rules expected to recur every season with only details changing — with a
**leading asterisk and a green headline**; all other (game-specific) headlines are orange
(BIOBUZZ V0 §1.7.1, p. 18).

I checked the span colours of every headline on pp. 64-88 of the V0 PDF:

> **51 of the 52 R-rules in BIOBUZZ Section 12 are green/Evergreen. The single orange (game-specific) rule is R105 — the expansion rule — and it is exactly the one FIRST deferred to Kickoff.**

**[INFER]** Practical consequence: everything in Section 12 except R105 is now effectively frozen for the
season. You can commit to motor counts, electronics architecture, wiring, signs and OPERATOR CONSOLE design
**today**. The only structural unknown is *how far your robot may expand*.

---

## 1. Executive summary — what changed vs DECODE, ranked by design impact

| # | Change | BIOBUZZ | DECODE (2025-26) | Why it matters |
|---|---|---|---|---|
| 1 | **Servo limit cut** | **8 motors + 8 servos** (R503) | 8 motors + **10** servos | You lose 2 servos. ITD 2024-25 was 12 → 10 → 8. Re-plan any 9-10 servo architecture *now*. |
| 2 | **Gas springs / gas shocks are now LEGAL** | R801.A allows "sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)"; orange box names *gas springs and dampers* | DECODE R207.A explicitly banned gas springs, and the Inspection Quick Reference listed them as illegal | Huge for hang/lift/counterbalance mechanisms. Constant-force lifting without burning a motor. |
| 3 | **Expansion numbers deferred** | R105: "Sizing Constraints and more details will be released at Kickoff" | 18 in. horizontal square, 18 in. vertical (default), 38 in. vertical under G415 | Cannot finalize extension/lift geometry. Design *adjustable* hard stops. |
| 4 | **FTC Dashboard & third-party telemetry explicitly banned** | R704.D names "FTC Dashboard, FTControl Panels, and others" as prohibited | DECODE R706 banned continuous video streams but did **not** name Dashboard-class tools | Many teams tune PID/paths over Dashboard. Legal in the pit, **not** on the ROBOT network during play. Read R704.D verbatim before your first event. |
| 5 | **Gamepad allowlist removed from §12** | No gamepad table anywhere in V0. R901.B: "for connecting one or more gamepads" — no model list, no count cap | DECODE R903 + Table 12-12: max **2** gamepads from a 7-item allowlist | **[V0-GAP]** Do **not** assume any gamepad is legal or that >2 are allowed. Highest-probability Kickoff re-insertion. |
| 6 | **Android smartphone allowlist removed** | R701.B: "a smartphone Android device"; R901.B "Any Android Device". No model table, no Android-7 minimum | DECODE R704 + Table 12-10 (6 Motorola models, Android 7+) | Old phones are no longer model-gated, but FIRST states only the Control Hub / Driver Hub are *supported*. |
| 6b | **Control-system software version table removed** | R701 orange box → "FIRST Tech Challenge Firmware Update Page (**Coming Soon**)" | DECODE R713 + Table 12-11 (Control Hub OS 1.1.2, Hub FW 1.8.2, RC/DS App 11.0, Driver Hub OS 1.2.0, Servo Hub FW 25.0.2) | **[V0-DEFERRED]** SDK/firmware targets are a Kickoff-day item. |
| 7 | **Nothing may be moving at the start** | R102 adds "**all parts of the ROBOT must be fully stationary**" in STARTING CONFIGURATION | DECODE R101 had no such clause | Kills pre-spun flywheels / pre-wound energy in motion at T=0. New in FTC — not present in DECODE or ITD. |
| 8 | **OPERATOR CONSOLE got 4 in. deeper** | R903: 3 ft W × **1 ft 6 in** D × 2 ft H (91.4 × **45.7** × 61.0 cm) | R904: 3 ft × **1 ft 2 in** × 2 ft (91.4 × **35.5** × 61.0 cm) | 14 in → 18 in depth. Also now explicitly includes "all power sources (e.g., power banks)". |
| 9 | **OPERATOR CONSOLE may use USB hubs** | R901.B allows "any combination of USB cables (including USB OTG cables) and/or USB hubs (powered or unpowered…)" | DECODE R901.B: "one OTG cable and COTS USB cable" only | Cleaner console wiring, spare-hub swap now explicit (R903 orange box: only one hub connected at a time). |
| 10 | **Stored-energy whitelist deleted** | No BIOBUZZ equivalent of DECODE R608 | DECODE R608 limited non-electrical stored energy to (a) change in COG altitude, (b) deformation of parts (springs, rubber bands, surgical tubing) | **[V0-GAP]** Energy sourcing is now policed only by R506 (no solenoids/electromagnets/relays), R601 (one battery) and R801 (air). Verify at Kickoff before designing an exotic energy store. |
| 11 | **Wire-colour rule narrowed** | R610 applies only to "**the 12V main power bus and +5V auxiliary bus**"; explicitly exempts motor wiring, signal wiring, servo cables and extensions | DECODE R616 applied to **all** non-SIGNAL-LEVEL constant-polarity wiring | Materially easier to pass electrical inspection. Also: DECODE's "insulated **copper** wire" requirement (R615) is gone — BIOBUZZ R609 says only "insulated wire". |
| 12 | **FIRST logo no longer allowed on ROBOT SIGNS** | R402 allowance list omits the logo | DECODE R402.B allowed "solid white FIRST logos no larger than 1.5 in." | The new 2026-27 sign template carries no logo — cross-checked below. |
| 13 | **New +5V Aux / port-power discipline** | R613.B "power from a specific port may only power devices plugged into that exact port"; R613.D +5V Aux may power devices "not connected to other power regulation devices except via USB" | DECODE R619.B explicitly permitted +5V Aux power to be used "in conjunction with any Analog, Digital, or I2C port on that device" | **Tightening.** The old trick of powering a hungry I2C/analog sensor from +5V Aux while its signal lines sit on a hub port now reads as illegal. |
| 14 | **Flashing-light threshold relaxed** | R202.J: >**5 Hz** invites scrutiny | DECODE R203 orange box: >**2 Hz** | Minor, but the E-rules mirror it (**E108.G**: no items flashing faster than ~5×/sec — note this is E108 in BIOBUZZ V0; it was E109 in DECODE). |
| 15 | **New motor added** | **WATTOS Stingray 12V DC (WDM12)** added to Table 12-1 | Not present | 13 legal motor families (was 12). No motors removed. |

---

## 2. Master R-rule table (all 52 BIOBUZZ rules)

All rules **[V0-FINAL]** unless noted. "E" = Evergreen (green/asterisked headline). Page = V0 PDF page.

### 12.1 General ROBOT Design (pp. 66-68)

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R101** | ✔ | Team must build the ROBOT and its MAJOR MECHANISMS. Defines MAJOR MECHANISM = assembly addressing ≥1 game challenge (movement, SCORING ELEMENT manipulation, FIELD element manipulation, scorable task without another ROBOT). Gearboxes, sub-mechanisms and COTS items are **not** MAJOR MECHANISMS. | — | Judged/asked verbally. **Moved from DECODE I301 into §12.** Cross-refs R301, R303. |
| **R102** | ✔ | STARTING CONFIGURATION ≤ 18-inch cube; **all parts fully stationary**; ROBOT fully self-contained. | **18 × 18 × 18 in. (45.70 cm each)** | Sizing-tool check. Pre-loaded SCORING ELEMENTS may protrude. Must comply in *every* configuration used per §3.3. |
| **R103** | ✔ | ROBOT must hold STARTING CONFIGURATION self-supported — no force on the sizing tool's sides/top. May use (a) mechanical means unpowered and/or (b) an OpMode pre-positioning servos/motors. | — | Robot may be live during sizing; **tell the inspector**. Beware thermal failure from motors stalled against hard stops for minutes. |
| **R104** | ✔ | **No weight limit** ("for FIRST Tech Challenge ROBOTS playing BIOBUZZ"). | none | Nothing to check. Orange box still warns about TILE damage, battery drain, transport, performance. |
| **R105** | ✗ (**only game-specific rule in §12**) | One assembly — **may not be designed to intentionally detach COMPONENTS**. May expand after MATCH start, "still subject to sizing constraints relative to the ROBOT, based on the initial STARTING CONFIGURATION." | **[V0-DEFERRED]** — *"Sizing Constraints and more details will be released at Kickoff"* (p. 68) | The **entire** expansion envelope is unknown. See §3 below. |

### 12.2 Fair Play & Damage Prevention (pp. 68-69)

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R201** | ✔ | No damage / no mess in the ARENA. Named risks: TILE-damaging traction devices; exposed sharp edges/protrusions; abrasive surfaces. Named mess risks: excess lubricant, unsecured ballast (sand, coffee beans, kitty litter, glitter, ball bearings), liquids/gels, tire sealant, graphite powder. Gouging/tearing/repeatedly marking SCORING ELEMENTS violates this rule **and G### (placeholder)**. | — | The classic "run your hand over every edge" check. Consolidates DECODE R201+R202+R205+R206. |
| **R202** | ✔ | Safety & fair play for **ROBOT *and* OPERATOR CONSOLE**. Prohibited: A vision-blocking shields/curtains; B distracting or MATCH-mimicking audio; C anti-sensor devices incl. imagery mimicking **36h11 AprilTags**; D flammable gas / flames / pyrotechnics; E hazardous materials "like liquid mercury or lead"; F high-intensity lights (brief targeting use only, LRI/Head Ref may order disable); G animal-based materials; H devices designed to damage or flip robots; I entanglement risks; J lighting flashing **> 5 Hz** invites scrutiny; K anything else against the spirit. | **5 Hz** | Note **E**: DECODE's explicit carve-out permitting *painted/encapsulated/sealed* lead ballast is **gone**. Assume lead ballast is now disallowed until clarified. |
| **R203** | ✔ | ROBOT must release SCORING ELEMENTS and detach from FIELD elements **while powered off**. | — | Inspector will power down and pull an element out. Design manual release into intakes/grippers. |
| **R204** | ✔ | No mechanism designed to increase downforce by grabbing the FIELD surface or by generated-airflow suction. | — | Visual + questioning. |

### 12.3 Fabrication (pp. 69-71)

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R301** | ✔ | COTS **MAJOR MECHANISMS** purpose-built to complete a game task are prohibited. Exceptions: (A) COTS drive CHASSIS, (B) COTS MAJOR MECHANISMS from official FIRST **StarterBots**. New sentence: "A vendor selling *'build to print'* manufacturing of publicly available, purpose-built solutions is against the spirit of this rule." | — | Judgement call; the new build-to-print sentence closes the "have a vendor CNC the open-source scoring arm" loophole. |
| **R302** | ✔ | Legal COTS parts and raw materials may be modified (drilled, cut, painted). Raw materials = sheet stock, extruded shapes, metals/plastic/rubber/wood, magnets. | — | — |
| **R303** | ✔ | COTS COMPONENTS/MECHANISMS ≤ **1 degree of mechanical freedom**. Allowed 1-DoF examples: linear slide kit, linear actuator kit, non-shifting gearbox, pulley, turntable, lead screw, single-DoF gripper. Exempt: ratcheting devices, holonomic wheels (omni/mecanum), dead-wheel odometry kits, misalignment couplers (U-joints, flex couplers), variable-angle connectors (ball joints, rod ends). | **1 DoF** | Common failure: a COTS gripper with an added wrist/twist actuator = multi-DoF = illegal. Also bans "highly specialized individual COMPONENTS only designed to assemble into a multiple-DoF COTS COMPONENT." |
| **R304** | ✔ | **Software, designs AND fabricated items created before Kickoff are permitted.** (DECODE split this across R304 + R305.) | — | Off-season prototyping is explicitly fine. |
| **R305** | ✔ | Current-season SCORING ELEMENTS or replicas may not be used in ROBOT construction. | — | DECODE's trailing clause "…or for any other team supplied SCORING ELEMENTS" was **dropped**. |

### 12.4 ROBOT SIGN Rules (pp. 71-74) — see §4 for the deep dive

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R401** | ✔ | **Minimum of two** ROBOT SIGNS, on opposite **or adjacent (90° apart)** surfaces. Top of ROBOT counts. Must be (A) robust material, (B) ≥ 6.5 in. wide, (C) ≥ 2.5 in. tall, (D) supported by ROBOT structure/frame. | **≥ 6.5 in. (16.5 cm) × ≥ 2.5 in. (6.4 cm)**; readable from **12 ft (3.65 m)** | Measured with a ruler. "Robust" is deliberately undefined — good-faith effort. Note "**Minimum of** two" (was "Two") — more than 2 is explicitly fine. |
| **R402** | ✔ | Each sign must contain a **solid, opaque red or blue rectangle** ≥ 6.5 × 2.5 in. (16.50 × 6.35 cm). Only these other markings are allowed: A the R403 numbers; B small hook-and-loop/fasteners; C narrow differing colours at corners/folds/cutouts; D narrow template markings; E **no power may be used to illuminate/reveal ALLIANCE colour**. Reversible/configurable signs must never show the opposite colour. | **6.5 × 2.5 in.** | Figure 12-2 shows a non-rectangular (oval) sign is legal **only if a full 6.5 × 2.5 in. rectangle of solid ALLIANCE colour fits inside it**. |
| **R403** | ✔ | Team numbers: A solid opaque **white** Arabic numerals **approximately 2.25 in. (5.70 cm)** tall; B **approximately ≥ 0.25 in. (0.60 cm)** of background around the numbers; C **not vertically stacked**; D robust material; E **not powered/illuminated**. | **2.25 in.**, **0.25 in.** | Figure 12-4: a sign rotated 90° so the number reads bottom-to-top is **OK**; digits stacked vertically or mirrored is **NOT OK**. Prohibited: edge-lit engraved plastic, LED displays. If no colour printer at the event, the **Head REFEREE may approve a substitute** — handwritten on plain paper is explicitly acceptable as a fallback. |

### 12.5 Motors & Actuators (pp. 75-78) — see §5

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R501** | ✔ | Closed list of legal motors (Table 12-1, 13 families). Plus: factory vibration/autofocus motors inside COTS computing devices, and motors integral to COTS sensors (LIDAR, scanning sonar) — **neither counts toward R503**. | 13 families | Orange box: "Many legal gearmotors are sold with labeling based on the entire assembly. These motors may be used **with or without the provided gearbox, and/or with any other compatible gearbox**." |
| **R502** | ✔ | Servo legality gate: mechanical output power **and** stall current, both at 6 V. Power formula: `P = 0.25 × (stall torque N·m) × (no-load speed rad/s)`. | Servo: **≤ 8 W @6V**, stall current **≤ ___ A @6V** — **[V0-ERRATA]** value missing in V0 PDF; DECODE was **≤ 4 A @6V**. Linear servo: power **N/A**, **≤ 1 A @6V** | Must show datasheet or be on the pre-verified list in the Inspection Quick Reference. If the manufacturer gives no 6 V spec, specs at >6 V may be used. Stall current means *maximum possible*, ignoring software limits. |
| **R503** | ✔ | **Total actuator cap across ALL configurations used at an event.** | **8 motors + 8 servos** | Summed over every swappable mechanism (see I302), not per-match. DECODE's helpful orange box about the hub's 5 V/5 A servo budget (2 A per port pair, 10 W per pair, 25 W total) was **deleted** — the electrical limit still exists physically. |
| **R504** | ✔ | No motor/servo modification except: A mounting brackets and output shaft/interface (incl. pinion gears); B lead trimming + connectors/splices (per R609) and functionally-equivalent electrical enclosure substitution; C manufacturer-specified servo mods (**"setting soft limits"** or continuous-rotation conversion); D non-obstructing labels; E terminal insulation; F repairs with unchanged performance; G manufacturer-recommended maintenance. | — | Highest-Q&A-volume rule after R105. See §9 for the prior-season rulings (encoder removal, rear-cap removal, 4th-wire additions). |
| **R505** | ✔ | Actuator control signals must originate from an approved power-regulating device (Table 12-3). Exceptions: servos, fans, and motors integral to COTS sensors/computing devices per R501. | Table 12-3 (below) | Any signal-generating/altering device between hub and servo is illegal. |
| **R506** | ✔ | **No relays, electromagnets, or electrical solenoid actuators**, or related systems. | — | Visual/questioning. |

**Table 12-1 — Legal motors [V0-FINAL]** (V0 p. 75)

| Motor | Part numbers | Notes |
|---|---|---|
| AndyMark NeveRest 12V DC | am-3104, am-3104b | |
| AndyMark NeveRest Hex 12V DC | am-3104c | |
| goBILDA Yellow Jacket 520x Series 12V DC | 5201-0002-0026, etc. | 5201, 5202, 5203, 5204 series |
| goBILDA 5000 Series 12V DC | 5000-0002-4008, etc. | |
| Modern Robotics / MATRIX 12V DC | 5000-0002-0001 | Discontinued |
| NFR Products Yuksel 12V DC | NFR-600-100-000 | |
| REV Robotics HD Hex 12V DC | REV-41-1291 | |
| REV Robotics Core Hex 12V DC | REV-41-1300 | |
| Studica Robotics Maverick 12V DC | 75001 | |
| SWYFT Robotics SWYFT Spike Motor | SR-MOTOR-DC-01 | |
| TETRIX MAX 12V DC | 739530, 39530 | Discontinued |
| TETRIX MAX TorqueNADO 12V DC | W44260 | |
| **WATTOS Stingray 12V DC** | **WDM12** | **NEW for BIOBUZZ** |

**Table 12-2 — Servo requirements at 6 V [V0-FINAL, one value missing]** (V0 p. 76)

| Class | Mech. output power | Stall current | Named example servos |
|---|---|---|---|
| Servo | **≤ 8 W @6V** | **≤ ___ A @6V** ← blank in V0; DECODE = ≤ 4 A **[V0-ERRATA]** | AndyMark High-Torque (am-4954); Axon MAX+; DSSERVO 35KG Coreless (DS3235MG); FEETECH FT5335M-FB; goBILDA Dual Mode (2000-0025-0003); REV Smart Servo (REV-41-1097); Studica Multi-Mode Smart Servo (75002) |
| Linear Servo | N/A | **≤ 1 A @6V** | Actuonix Micro Linear (P8-100-252-12-R); Hitec HLS12-3050-6V; Studica Linear Servo RC Actuator (75014) |

Voltage note (R502 orange box): **Control Hub / Expansion Hub servo ports supply 5 V**; goBILDA Servo Power
Injector, REV Servo Power Module, Studica Servo Power Block and REV Servo Hub supply **6 V**. A 6-8.4 V servo
may misbehave on 5 V.

**Table 12-3 — Power regulators and load limits [V0-FINAL, identical to DECODE]** (V0 p. 77)

| Device | Part number | Load limit |
|---|---|---|
| goBILDA 6V Servo Power Injector | 3125-0001-0001 | 2 servos per port |
| REV Control/Expansion Hub — **motor** ports | REV-31-1153 / REV-31-1595 | 2 motors per port |
| REV Control/Expansion Hub — **servo** ports | REV-31-1153 / REV-31-1595 | 2 servos per port |
| REV Servo Power Module | REV-11-1144 | 2 servos per port |
| REV Robotics Servo Hub | REV-11-1855 | 2 servos per port |
| REV SPARKmini | REV-31-1230 | 2 motors per device |
| Studica Servo Power Block | 75005 | 2 servos per port |

### 12.6 Power Distribution (pp. 78-83)

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R601** | ✔ | Exactly **one** approved 12 V NiMH main battery; only legal electrical energy source for control + actuation; must be unaltered except (A) fuse may be replaced with a COTS equivalent **in-line 20 A ATM mini blade fuse** "installed per **R610**" ← **[V0-ERRATA]**, R610 is the wire-colour rule; (B) connectors may be swapped for Anderson Powerpole, XT30 or comparable. | **1 battery, 12 V NiMH, 20 A ATM mini blade fuse** | Table 12-4, 7 approved packs. Note DECODE *required* the 20 A fuse; BIOBUZZ frames it as an allowed replacement of the factory fuse — same practical outcome. |
| **R602** | ✔ | Other batteries only for self-contained peripherals/LEDs: COTS USB battery packs **≤ 100 Wh (27,000 mAh @3.7 V)**, **5 V/5 A** or **12 V/5 A max output using USB-PD per port**; plus batteries integral to self-contained devices (e.g., GoPro-style camera). Conditions: (A) must not power any ROBOT actuator; (B) must not power any device receiving control signals from the ROBOT control system — **exceptions: powered USB hubs, and ROBOT CONTROLLER smartphones**. | **100 Wh / 27,000 mAh / 5 A** | "Any device receiving signals from a REV Control or Expansion Hub must be powered by the main ROBOT battery." DECODE's extra conditions (unmodified COTS cables, charged per manufacturer, securely fastened) were **dropped**. |
| **R603** | ✔ | **Exactly one** main power switch controlling all battery power to all power-regulating devices (except R602 items). (A) must be from Table 12-5; (B) accessible to the team, away from high-speed moving parts and pinch hazards; (C) secondary switches allowed downstream on the 12 V line. | 6 approved switches | **Relaxed vs DECODE**: DECODE required accessibility "to the team **and FIELD STAFF**" and its orange box called switches behind an access panel not acceptable. BIOBUZZ explicitly permits mounting **behind removable panels**. |
| **R604** | ✔ | Fuses must be used as the device manufacturer directs; no modifying, no higher trip point, no self-resetting fuses. | — | Intent-based wording; DECODE's explicit "must not exceed the rating of those closer to the battery / may be replaced with a smaller rating" language is gone but the intent survives. Cross-check E510 (no thermally cooling fuses to delay tripping). |
| **R605** | ✔ | **Frame is not a conductor.** All wiring/devices electrically isolated from the frame. Frame grounding permitted only if: (A) strap from Table 12-6; (B) strap connects directly to a fully-COTS component with an **XT30** connector **and** directly to the frame via the resistive terminal; (C) nothing designed to ground the frame to the FIELD. | 3 approved straps | DECODE's numeric compliance test (**>120 Ω** measured from the switch input terminals to any point on the ROBOT) and its warning about conductive-enclosure cameras/lights/encoders were **deleted**. **[PRIOR]** — still the right way to self-test. Points to the ROBOT Wiring Guide. |
| **R606** | ✔ | All power-regulating devices, wiring and fuses must be **able to be made visible** for inspection; ROBOT CONTROLLER mounted so diagnostic lights / screen can be made visible. | — | "Visible for inspection" ≠ visible during a MATCH. Merges DECODE R612 + R711. Strong encouragement to keep LEDs visible in match config so FIELD STAFF can help you. |
| **R607** | ✔ | CUSTOM CIRCUIT = any active electrical item that isn't an R501 actuator or an R505 power-regulating device. CUSTOM CIRCUITS must not output **regulated voltage > 5 V**, except solely for powering LEDs. May pass through unregulated battery voltage. | **5 V** | — |
| **R608** | ✔ | Each power-regulating device may only be energized as Table 12-7 specifies, from the ROBOT main battery. | Table 12-7 | Hub/Injector = XT30; Servo Power Module = screw terminals; Servo Hub = power terminals; SPARKmini = Power input; Studica Servo Power Block = JST-VH. |
| **R609** | ✔ | Minimum wire gauge by application (Table 12-8). Integrated/manufacturer-supplied wires are exempt. | **18 / 22 / 28 AWG** | Combining small wires in parallel is explicitly not allowed. **BIOBUZZ dropped DECODE's "copper" requirement.** |
| **R610** | ✔ | Colour-code **only** the 12 V main power bus and +5 V aux bus, full length: (A) positive = red, yellow, white, brown, or black-with-stripe; (B) negative = black or blue. Explicitly does **not** apply to motor wiring, signal-level wiring, servo cables/extensions, or manufacturer-attached wires. | — | **Materially narrower than DECODE R616.** DECODE's multi-conductor re-identification requirement is gone. |
| **R611** | ✔ | Powered USB hubs may only be powered by (A) an R602-approved COTS USB battery pack, or (B) the 5 V auxiliary port on a REV Expansion/Control Hub. | — | — |
| **R612** | ✔ | CUSTOM CIRCUITS must not alter power/control paths between: A battery↔main switch; B main switch↔power-regulating device (per **R603**); C any two power-regulating devices (per **R607** ← **[V0-ERRATA]**, R607 is the custom-circuit rule; DECODE had the same style of bad ref); D power-regulating device↔actuator. High-impedance voltage / low-impedance current monitoring is OK if inconsequential. | — | Buck/boost converters in the battery path are explicitly banned. Named illegal device: **goBILDA Servo Travel Tuner**. |
| **R613** | ✔ | Don't mix power across ports/devices: A sensors/encoders/devices powered **solely** by the regulating device they're connected to (no custom circuits, no second hub); B a port's power may only feed devices plugged into **that exact port** — no cross-wiring, no combining ports into a bus; C 6 V from servo power modules/injectors may only power **servos**; D the +5 V Aux port on a REV hub may power devices **not connected to other power regulation devices except via USB**. | — | **Tighter than DECODE R619.** DECODE explicitly allowed +5 V Aux to be used "in conjunction with any Analog, Digital, or I2C port on that device"; BIOBUZZ removed that sentence. |

**Table 12-4 — Legal main batteries [V0-FINAL, identical to DECODE]** (V0 p. 78)

| Battery | Part number | Notes |
|---|---|---|
| AndyMark Flat Pack Battery DC 12V | am-5290 | |
| goBILDA 12V NiMH Nested Battery | 3100-0012-0020 | |
| Matrix 12V 3000mAh NiMH | 14-0014 | May be labeled "Modern Robotics" |
| REV 12V Slim Battery | REV-31-1302 | |
| Studica 12V 3000mAh NiMH | 70025 | |
| TETRIX MAX 12V 3000mAh NiMH | W39057 | Formerly 739023 |
| WATTOS 12V Battery | WT-NMH1230 | |

**Table 12-5 — Legal power switches [V0-FINAL, identical to DECODE]**: AndyMark am-4969 · goBILDA Floodgate
3103-0005-0001 · REV Switch Cable & Bracket REV-31-1387 · Studica 70182 · TETRIX R/C Switch Kit W39129 ·
WATTOS WTS-SW1220.

**Table 12-6 — Legal grounding straps [V0-FINAL, identical to DECODE]**: AndyMark am-4648a · REV REV-31-1269 ·
Swyft SR-Ground-01.

**Table 12-8 — Wire sizing [V0-FINAL]** (V0 p. 81; verified against the PDF's table cell geometry, because
naive text extraction mis-aligns this table)

| Minimum wire size | Applications |
|---|---|
| **18 AWG** (19 SWG / 1 mm²) | 12 V main battery power · Motor power (unless listed below) · 11-20 A fuse-protected circuit |
| **22 AWG** (22 SWG / 0.5 mm²) | Motor power for **TETRIX MAX 12V DC** and **REV Core Hex (listed as "REV-14-1300")** · PWM/servo · LEDs (5 V/12 V) · ≤10 A fuse-protected circuit |
| **28 AWG** (29 SWG / 0.08 mm²) | Signal-level circuits (≤1 A continuous from a source incapable of >1 A: I2C, DIO, analog, encoder, RS485) |

> **[V0-ERRATA]** Table 12-8 says the Core Hex is "REV-**14**-1300"; Table 12-1 says "REV-**41**-1300". The same
> typo exists in DECODE. Assume REV-41-1300 is the real part.
> **Note:** DECODE's version of this table straddled a page break, which makes text extraction *appear* to
> place "11-20 A fuse protected circuit" in the 22 AWG group. Cell-geometry analysis shows it was 18 AWG in
> DECODE too — **this is not a real change**, just a formatting cleanup.

### 12.7 Control, Command & Signals System (pp. 83-87)

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R701** | ✔ | Exactly **1** programmable ROBOT CONTROLLER: (A) REV Control Hub **REV-31-1595**, or (B) a smartphone Android device connected to a REV Expansion Hub **REV-31-1153**. Plus optionally (C) **no more than one additional** REV Expansion Hub. | max **2 hubs total** | Orange box: only the **REV Control Hub** is *officially supported*; smartphone users own all compatibility risk. Firmware page "**Coming Soon**" **[V0-DEFERRED]**. |
| **R702** | ✔ | No modifying coprocessor software. Manufacturer binary firmware updates OK. Exception: **programmable vision coprocessors natively supported by the FTC SDK** may be reprogrammed — Table 12-9. | Table 12-9 = **Limelight 3A (LL_3A)** only | Explicit rulings carried in the orange boxes: **allowed** — Adafruit BNO055, SparkFun OTOS (do not rebuild its firmware; vendor binaries OK), Digital Chicken Labs OctoQuad FTC Edition, optical-flow sensors, DFRobot HuskyLens, Charmed Labs Pixy2. **Prohibited** — OpenMV Cam, Luxonis OAK-1, **Limelight 3G**. |
| **R703** | ✔ | Smartphone ROBOT CONTROLLER must connect to the Expansion Hub via its integrated USB port, using any combination of USB/OTG cables and/or hubs (powered or unpowered, OTG integrated or not). | — | **Relaxed vs DECODE** (which prescribed micro-USB and a specific cable/adapter pairing). |
| **R704** | ✔ | Wi-Fi & bandwidth. A no other wireless to/from/within the ROBOT; B all comms originate only from the RC or DS on the RC's Wi-Fi network, nothing else may connect/interfere; C **all programming laptops and other devices must be disconnected during MATCH play**; D software may only stream robot control data, debugging data and telemetry **using the FTC Driver Station Application** — *"Additional logging/streaming services, such as those hosted by third party plugins and tools such as **FTC Dashboard, FTControl Panels**, and others are prohibited. No continuous video stream is allowed."*; E teams must use an assigned Wi-Fi band/channel if event staff request it. | — | **Biggest software-workflow change of the season.** Consolidates DECODE R706+R708+R710 and adds the named-tool prohibition. |
| **R705** | ✔ | Device naming: `<team#>-RC`, `<team#>-DS`; spares may add a letter (`12345-A-DS`). | — | Checked on the self-inspect screen. |
| **R706** | ✔ | No tampering with DS device/software, Android RC device, main/secondary switches, power regulation devices, fuses, batteries — except A standard connection points; B fasteners/adhesives to mount; C thermal interface material; D non-obscuring labels; E jumpers/switches moved per the manual; F manufacturer firmware; G integral motor-controller and battery wires may be cut/stripped/connectorized; H repairs (not batteries) with identical performance; I insulating exposed conductors; J tape for debris protection; K power-switch mounting brackets modified/replaced. | — | DECODE's separate item "jumpers may be changed from their default location" was merged into E. |
| **R707** | ✔ | USB may only connect: A webcams/optical vision sensors per R708; B a USB hub or USB switch; C a REV Expansion Hub. | — | No USB LEDs, no USB storage, no USB microcontrollers. |
| **R708** | ✔ | USB vision must be **single image sensor** and natively supported by the RC app (**stereo cameras prohibited**): A all UVC-compatible webcams (Logitech C270 and related); B vision coprocessors allowed per R702. UVC webcams may only use the UVC stream/data. | — | — |
| **R709** | ✔ | Self-contained recording devices (GoPro or similar) allowed for **non-functional post-MATCH viewing only**, wireless **off**. | — | Inspector will ask you to show wireless is disabled. |
| **R710** | ✔ | Lasers only if: A part of a sensor; B rated **IEC/EN 60825-1 "Class I"** or **IEC/EN 62471 "Exempt"**; C **non-visible spectrum**. | — | **[V0-ERRATA]** The "62471" digits do not render in the V0 PDF text layer (shows "IEC/EN ⎵7"); DECODE reads 62471. Visible-red line lasers remain illegal. |
| **R711** | ✔ | Android device configuration: A Control Hub Wi-Fi password changed from default; B smartphones in Airplane Mode; C Wi-Fi enabled **and Bluetooth disabled** on both RC and DS; D on **DRIVER STATION** Android devices, remove all remembered Wi-Fi Direct groups and Wi-Fi connections except the RC connection. | — | D's scope changed from DECODE's "smartphones and REV Driver Hub" to "DRIVER STATION Android devices" — same practical effect. |

### 12.8 Pneumatic Systems & Airflow Devices (p. 87)

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R801** | ✔ | A **may only use sealed, COTS closed-air systems pre-charged by the manufacturer (such as gas shocks)**; B no stored-pressure components actuated by a solenoid or able to change stable state; C **may not generate pressure or vacuum**; D no user-adjustable gas storage vessels **except air-filled (pneumatic) COTS wheels**; E no device creating high-speed airflow **except cooling fans integrated into COTS computing devices**. | — | Orange box confirms: **"they may use 'closed air' systems which were sealed by their manufacturer. This includes items such as gas springs, and dampers."** Flywheels/rollers for manipulating SCORING ELEMENTS are **not** "high-speed airflow devices". |

### 12.9 OPERATOR CONSOLE (pp. 87-88)

| Rule | E | What it constrains | Hard numbers | Inspection implication |
|---|---|---|---|---|
| **R901** | ✔ | Only **one** approved Android DRIVER STATION device connected and powered on. Must have at least: (A) **REV Driver Hub REV-31-1596**, or (B) **any Android device**, with or without any combination of USB cables (incl. OTG) and/or USB hubs (powered or unpowered, OTG-integrated or not) for connecting one or more gamepads. | 1 DS device powered on | Spare DS device allowed if only one is connected/powered at a time. Only the Driver Hub is *officially supported*. |
| **R902** | ✔ | DS touch screen must be accessible, clearly visible during inspection and MATCHES, and functional without extra aids (e.g., a mouse). | — | Inspector taps the screen. |
| **R903** | ✔ | OPERATOR CONSOLE volume **including all power sources (e.g., power banks)**: **3 ft W × 1 ft 6 in D × 2 ft H (91.4 × 45.7 × 61.0 cm)**, excluding items held or worn by DRIVERS. | **91.4 × 45.7 × 61.0 cm** | Orange box: >**20 lb (~9 kg)** invites extra scrutiny (no hard weight limit). Spare external USB hub allowed if only one connected at a time. Not a robot cart. Also see R202. |
| **R904** | ✔ | No wireless to/from/within the OPERATOR CONSOLE other than the RC-app↔DS-app link. | — | Wireless NICs and Bluetooth devices named as prohibited. |

---

## 3. Sizing & expansion — exactly what is deferred

### 3.1 What IS confirmed today [V0-FINAL]

- **STARTING CONFIGURATION = 18 × 18 × 18 in. (45.70 cm) cube**, self-contained (R102).
- **All parts fully stationary** at the start (R102) — **new for BIOBUZZ**.
- **Self-supported** in the sizing tool; no leaning on the tool's walls or lid (R103). Powered holding via an
  initialised OpMode is explicitly allowed.
- **Pre-loaded SCORING ELEMENTS may extend outside** the starting cube (R102 orange box).
- **No weight limit** (R104).
- **May not be designed to intentionally detach COMPONENTS** (R105, first sentence).
- **Expansion is measured relative to the ROBOT, based on the initial STARTING CONFIGURATION** (R105, second
  sentence) — i.e., the envelope rotates with the robot; it is *not* a floor-relative box.
- Must show compliance in **all** interchangeable-mechanism configurations (R102 orange box → §3.3).

### 3.2 What is DEFERRED [V0-DEFERRED]

> V0 p. 68, verbatim: *"Sizing Constraints and more details will be released at Kickoff"*

Unknown until 12 Sep 2026:
1. The **horizontal** expansion limit (footprint at max extension).
2. Whether horizontal expansion must be **mechanically** constrained (software limits disallowed) — DECODE's
   rule; likely to recur but unstated.
3. The **vertical** expansion limit(s), and whether there is a two-tier limit (normal vs. endgame).
4. Any per-phase (AUTO / TELEOP / ENDGAME) differences and the G-rule penalties that back them.
5. Whether the limit is a square, a cylinder, or something new.

### 3.3 Prior-season numbers — reference only, DO NOT assume [PRIOR]

| Season | Horizontal expansion | Vertical expansion |
|---|---|---|
| 2024-25 ITD | R104: horizontal limit only | (no vertical rule) |
| 2025-26 DECODE | R105.A: must remain within a fixed **18 × 18 in.** square at full expansion; **must be physically constrained without software** | R105.B: **18 in.** default; R105.C: up to **38 in. (96.50 cm)** within the limits of G415 |

### 3.4 Design guidance while R105 is unknown [INFER]

- Build extension hard stops that are **relocatable** (slotted, bolt-position-selectable), not welded/riveted.
- Assume the horizontal limit will again require a **mechanical** stop. Software-only limiting has been ruled
  insufficient for horizontal in every recent season — see the Q&A precedents in §9.
- Assume vertical *may* allow a software limit (DECODE did). Design so a firmware change can retune height.
- Assume **wires, cable ties, chains and flexible extensions count** toward the envelope **[PRIOR]** — this has
  been ruled repeatedly.
- Assume **two independent (non-linked) mechanisms will be measured extended simultaneously** at inspection
  **[PRIOR]**. If you want a 4-in. extension out of each side, mechanically interlock them.
- **R105 is the only non-Evergreen rule in Section 12.** Budget your kickoff-day review time accordingly:
  read R105 and the associated G-rules first, then diff the rest of Section 12 against this document.

---

## 4. ROBOT SIGN deep dive (12.4) + supplemental template cross-check

### 4.1 Cross-check against `2026-27_BIOBUZZ_RobotSign_USLetter.pdf`

I opened the official 2026-27 template (`manuals/archive/supplemental/2026-27_BIOBUZZ_RobotSign_USLetter.pdf`,
version stamp **"US Letter V26-27.1"**). Findings:

- **Geometry matches R401/R402 exactly.** Each sign rectangle is **468 × 180 pt = 6.5 × 2.5 in.** — the
  *minimum* legal size, with zero margin. Printing at anything less than 100% scale makes the sign illegal.
- **Layout:** 4 signs per US Letter sheet — **2 red + 2 blue**, five digit positions each. (Enough for the
  R401 minimum of two signs in both alliance colours from one sheet.)
- **New fill-in-the-segments design.** The template prints seven-segment-style outlines; printed instruction:
  *"Use a red or blue marker to fill in the white spaces to reveal the digits of your team number. Cut out each
  ROBOT SIGN and display them on your robot. Laminate or place behind clear plastic for a more rugged solution."*
  This means a **mono/greyscale printer plus a red and a blue marker is sufficient** — a genuinely useful fact
  when you're at an event without a colour printer.
- **No FIRST logo anywhere on the template** — consistent with R402 having dropped DECODE's
  "solid white FIRST logos ≤ 1.5 in." allowance. **Do not add a logo to your sign this season.**
- **Consistency:** no discrepancy found between the template and R401-R403.

### 4.2 Sign rules that quietly constrain the ROBOT's exterior

- **Two signs, on opposite *or* 90°-adjacent faces, supported by the ROBOT's structure/frame.** A sign zip-tied
  to a floppy plate or hanging off a mechanism is a re-inspection risk (R401.D). The top face is legal — useful
  if two side faces are consumed by intakes.
- **6.5 × 2.5 in. of *contiguous, solid, opaque* alliance colour.** If your side panel is a lattice of lightening
  holes, you need a solid backer. Figure 12-2 explicitly fails an oval whose inscribed rectangle is short.
- **Nothing else visible on the sign.** Sponsor logos, team names and mascots on the *sign area* are prohibited
  (R402). Put them elsewhere on the robot.
- **Nothing powered.** No edge-lit acrylic, no LED matrix numbers (R402.E, R403.E).
- **Reversible/configurable signs must never leak the other colour** (R402 orange box) — magnetic flip-plates
  and sliding covers need a positive latch.
- **Cheap failure mode:** DECODE's explicit examples of robust materials (acrylic, laminated paper, wood, metal)
  and of robust numbers (mailbox/vinyl numbers, laminated printouts) were removed from BIOBUZZ; both R401 and
  R403 now say only "make a good faith effort". **[INFER]** This reads as intentional leniency, not a new
  standard — the DECODE examples remain the safe choices.

---

## 5. Actuator budget — the quiet strategic constraint

### 5.1 The trend line

| Season | Motors | Servos | Source |
|---|---|---|---|
| 2024-25 ITD | 8 | **12** | ITD R503 |
| 2025-26 DECODE | 8 | **10** | DECODE R503 |
| **2026-27 BIOBUZZ** | **8** | **8** | **BIOBUZZ R503 [V0-FINAL]** |

**[INFER]** Servo count has been cut by 2 in each of the last two seasons while motors held at 8. Plan for 8/8
as a firm ceiling; do not expect a Team Update to restore servos.

### 5.2 What counts, and what doesn't

- **Counts:** every motor from Table 12-1 and every servo meeting R502, **summed across every configuration you
  bring to an event**, whether used simultaneously or not (R503 + I302). A swappable "specialist" mechanism does
  not get its own budget.
- **Does not count:** factory vibration/autofocus motors inside a COTS computing device; motors integral to a
  COTS sensor such as LIDAR or scanning sonar (R501, both explicitly exempted from R503).

### 5.3 Electrical budget that R503 no longer warns you about

DECODE's R503 orange box carried a warning that BIOBUZZ **deleted**: each REV Control/Expansion Hub supplies
**5 V limited to 5 A total shared across all servo ports plus the +5 V aux port, with a 2 A max across paired
servo ports (10 W per port pair, 25 W total)**. **[PRIOR]** The hardware limit is unchanged — the *warning* is
gone, not the physics. With 8 high-torque servos you will exceed a single hub's servo budget; plan on a REV
Servo Hub, Servo Power Module, goBILDA Injector or Studica Servo Power Block (all Table 12-3 legal, all 6 V).

### 5.4 Motor/servo modification — the most-litigated rule after R105

R504 text is essentially unchanged from DECODE (only R504.C's example changed from *"re-programming"* to
*"setting soft limits"*, and R504.B's broken cross-reference was fixed from R503 → **R609**). The prior-season
official rulings therefore very likely still apply — see §9.

---

## 6. Complete DIFF: BIOBUZZ V0 §12 vs DECODE (TU32, V6) §12

### 6.1 Renumbering crosswalk

| DECODE | BIOBUZZ | Change |
|---|---|---|
| I301 (Section 3) | **R101** | **Moved into §12.** Text unchanged except cross-ref now "R301 and R303" (was "R301"). |
| R101 | R102 | **+ "all parts of the ROBOT must be fully stationary"**; I304 cross-ref → §3.3. |
| R102 | R103 | Orange box softened: "Teams **must** also be especially cautious…taking every precaution" → "Teams **should** be especially cautious…please notify the INSPECTOR". |
| R103 | R104 | + "playing BIOBUZZ". |
| R104 (keep it together) | merged into **R105** sentence 1 | DECODE's "Violations…handled by G209" note dropped. |
| R105 (expansion, full numbers) | **R105** | **All numbers, figures, inspection guidance and G-rule cross-refs deleted → "released at Kickoff".** |
| R201 (TILE damage, named wheels) | folded into R201 orange box | Named examples (am-2256 HiGrip, am-3309 Roughtop) **deleted from the manual**. |
| R202 (sharp edges) | folded into R201 | |
| R203 (safety/fair play) | **R202** | Scope **+OPERATOR CONSOLE**; 2 Hz → **5 Hz**; audio now also covers "mimic match sounds"; hazardous-material list compressed and the **encapsulated-lead-ballast carve-out deleted**; hydraulics moved to R801 territory; light-shrouding language → "disable or modify at LRI/Head REF discretion". |
| R204 | R203 | Retitled; adds "Some events may allow…ROBOT power during FIELD reset, but ROBOTS should be designed such that this is not required." |
| R205 (mess) | folded into R201 | "glitter" added to the ballast list. |
| R206 (damage scoring elements) | folded into R201 orange box | + "routinely **and repeatedly**"; cross-ref now **G###** placeholder. |
| R207 (air) | **R801** (moved to §12.8) | **LOOSENED — see §6.2.** |
| R208 | R204 | Unchanged. |
| R301 | R301 | MAJOR MECHANISM def now via R101 (was I301); "purpose-built complete bolt-on out-of-the-box solution" → "purpose-built solutions"; **+ new build-to-print sentence**. |
| R302 | R302 | Unchanged (list reformatted A-D). |
| R303 | R303 | Unchanged. |
| R304 + R305 | **R304** (merged) | "Custom software, designs, and parts can be reused year-to-year." |
| R306 | R305 | Trailing clause "…or for any other team supplied SCORING ELEMENTS" **deleted**. |
| R307 (work outside pit hours) | **[V0-GAP] — no equivalent found anywhere in V0** | BIOBUZZ instead has restrictive E-rules: practice only in pit/practice area/Practice MATCH, and E107 limits where FABRICATED ITEMS may be produced. |
| R401-R403 | R401-R403 | See §6.3. |
| R501-R506 | R501-R506 | See §6.4. |
| R601 | R601 | Restructured; fuse now "may be replaced" rather than "must have installed". |
| R602 | R602 | Conditions A (unmodified COTS cables), B (charged per manufacturer), C (securely fastened) **deleted**; "self-contained camera" → "self-contained devices such as camera"; REV Blinkin example deleted. |
| R603 (charger connectors) | **moved to E511.C** | |
| R604 (3 A charge rate) | **moved to E511.B** | Same 3 A number. |
| R605 (batteries are not ballast) | **[V0-GAP] — deleted** | |
| R606 (battery securely mounted) | **[V0-GAP] — deleted** | R201 ("any component not secured sufficiently") arguably still covers it. |
| R607 (robust/insulated connections, slip rings) | **[V0-GAP] — deleted** | The explicit blessing of COTS slip rings / rolling contacts is gone. |
| R608 (non-battery stored energy whitelist) | **[V0-GAP] — deleted** | See §6.5. |
| R609 (main power switch) | **R603** | (B) "accessible to the team **and FIELD STAFF**" → "accessible to the team, **away from high-speed moving parts and pinch hazards**"; **behind removable panels now explicitly permitted**. |
| R610 (fuse ratings) | **R604** (condensed) | Explicit "must not exceed the rating of those closer to the battery", "may be replaced with a smaller rating", "self-resetting fuses (breakers) are not allowed" → single intent statement retaining the self-resetting ban. |
| R611 (frame not a wire) | **R605** | **>120 Ω compliance test deleted**; anodize-scratching note deleted; conductive-enclosure-device warning deleted; XT30 device examples deleted. |
| R612 (inspectable) + R711 (RC visible) | **R606** (merged) | "must be **visible**" → "must be **able to be made visible**". |
| R613 | **R607** | Unchanged substance. |
| R614 (energize regulators) | **R608** | Table 12-7 unchanged. |
| R615 (wire size) | **R609** | **"copper" requirement dropped**; "SIGNAL LEVEL" → "Signal level"; table now on one page. |
| R616 (wire colours) | **R610** | **Scope narrowed to the 12 V main bus and +5 V aux bus only**; multi-conductor re-identification requirement deleted. |
| R617 | **R611** | Unchanged. |
| R618 | **R612** | Cross-refs re-pointed (R609→R603, R613→R607). |
| R619 | **R613** | Rewritten & tightened — see §6.6. |
| R701 + R702 | **R701 / R702** | R701 keeps 1 RC + ≤1 extra Expansion Hub. "an **allowed** smartphone Android device" → "a smartphone Android device" (**allowlist gone**). |
| R703 (programmable vision coprocessors) | merged into **R702** | Table 12-9 unchanged (Limelight 3A only). Examples 4-6 folded in. |
| R704 (Android smartphone allowlist, Table 12-10) | **[V0-GAP] — deleted** | 6 Motorola models + Android 7 minimum + the international-exception email process all gone. |
| R705/R706/R707 | **R703** + **R705** | Micro-USB/cable prescription generalised. |
| R706 (bandwidth) + R708 (network) + R710 (assigned channel) | **R704** (merged) | **+ named prohibition of FTC Dashboard / FTControl Panels / third-party streaming plugins**; + explicit "disconnect laptops during MATCH play". |
| R709 (no other wireless on ROBOT) | folded into **R704.A** | DECODE's clarifying note (cameras and non-RF sensors aren't wireless comms) **deleted**. |
| R712 | **R706** | DECODE items E ("jumpers may be changed from their default location") and F merged into one. |
| R713 + Table 12-11 (software versions) | **[V0-DEFERRED]** | Replaced by R701's orange box → "FIRST Tech Challenge Firmware Update Page (Coming Soon)". |
| R714/R715 | **R707 / R708** | Unchanged. |
| R716 | **R709** | Unchanged. |
| R717 (lasers) | **R710** | Unchanged criteria. |
| R718 (Android config) | **R711** | Item D scope reworded. |
| R801 (no pneumatics) | **R801** (rewritten) | See §6.2. |
| R901 | **R901** | (B) "Approved Android Device from rule R704 with one OTG cable and COTS USB cable" → "**Any Android Device** with…any combination of USB cables…and/or **USB hubs**…for connecting one or more gamepads." |
| R902 | **R902** | Unchanged. |
| R903 + Table 12-12 (gamepads, max 2) | **[V0-GAP] — deleted** | See §6.7. |
| R904 | **R903** | **Depth 1 ft 2 in → 1 ft 6 in (35.5 → 45.7 cm)**; "+ (e.g., power banks)"; "likely to **present unsafe circumstances**" → "likely to **disrupt normal ARENA operations**"; absorbs DECODE R906's "not a robot cart" orange box. |
| R905 | **R904** | Line-of-sight/metal-shielding note deleted. |
| R906 (unsafe/unfair OPERATOR CONSOLES) | folded into **R202** | |

**Net:** DECODE §12 had ~73 numbered rules; BIOBUZZ §12 has **52**. Section 12 lost 4 tables
(Android smartphones, software versions, gamepads, and DECODE's split wire table) and gained none.

### 6.2 Pneumatics / airflow — the biggest *permissive* change

| | DECODE R207/R801 | BIOBUZZ R801 |
|---|---|---|
| Gas springs / gas shocks | **Explicitly prohibited** ("pneumatic solenoids or cylinders, gas storage vessels, **gas springs**, compressors, or vacuum generating devices"); Inspection Quick Reference listed gas springs as an illegal closed-air device | **Explicitly ALLOWED** — "sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)"; orange box: "includes items such as **gas springs, and dampers**" |
| Solenoid-actuated / bistable pressure devices | prohibited | prohibited (R801.B) |
| Generating pressure or vacuum | prohibited | prohibited (R801.C) |
| User-adjustable gas vessels | prohibited | prohibited **except air-filled (pneumatic) COTS wheels** (R801.D) |
| High-speed airflow | prohibited except integrated COTS computing-device cooling fans | same (R801.E) |
| Hydraulics | banned via R203.F | **[V0-GAP]** no explicit hydraulic ban in V0 §12; R202 general-safety and R801 would be the hooks |
| Section preamble | "these rules apply at all times while at the event, not just on the FIELD" | **preamble deleted** (from both §12.6 and §12.8) |

**[INFER] Design consequence:** a COTS gas spring is now the cheapest way to get large, constant, motor-free
force. Obvious BIOBUZZ applications: counterbalancing a heavy arm/lift so a single motor can hold it,
one-shot deploys, and damped endgame mechanisms. The catch: R801.B forbids anything that "change[s] their
stable state" under actuation — a gas spring that a solenoid or latch toggles between two pressure states is
still illegal; a plain sealed gas spring is not. And R102's new "fully stationary" clause means a pre-compressed
gas spring must be mechanically latched, not merely held by a motor that's already moving.

### 6.3 ROBOT SIGN diff

| Item | DECODE | BIOBUZZ |
|---|---|---|
| Headline | "Two ROBOT SIGNS per ROBOT" | "**Minimum of two** ROBOT SIGNS per ROBOT" |
| Robust-material examples | acrylic, plastic-laminated paper, wood, metal; "must be designed to withstand vigorous game play" | **deleted**; "no specific guidance on what is robust enough…good faith effort" |
| FIRST logo on sign | **allowed**, solid white ≤ 1.5 in. (R402.B) | **removed from the allowance list** |
| Template markings | "**dark** narrow markings on background solely for template purposes" | "**narrow** markings on background solely for template purposes" |
| Number height | "**2.25 in. +/- 0.5 in.** (5.70 cm +/- 1.25 cm)" | "**approximately** 2.25 in. (5.70 cm)" |
| Background margin | "minimum of 0.25 in. (0.60 cm)" | "minimum of **approximately** 0.25 in. (0.60 cm)" |
| Robust-number examples | self-adhesive mailbox/vinyl numbers; laminated printed numbers | **deleted**; + explicit fallback "**substitute ROBOT SIGNS may be simply handwritten on plain paper**" |
| Figures | 12-3, 12-4, 12-5 (incl. logo example), 12-6, 12-7 | 12-1, 12-2, 12-3, 12-4 (logo figure removed) |

**[INFER]** The tolerance language went from a hard band (±0.5 in.) to "approximately". This is a *relaxation*
and reduces sign-related inspection friction, but it also removes your ability to argue a precise number back
at an inspector. Print the official template at 100% and the question never comes up.

### 6.4 Motors & actuators diff

| Item | DECODE | BIOBUZZ |
|---|---|---|
| R501 headline | "Allowable motors" | "Only specific motors are allowed" |
| Motor list | 12 families | **13** — **+ WATTOS Stingray 12V DC (WDM12)**. Nothing removed. |
| R502 headline | "Allowable servos" | "Servo usage is restricted" |
| Servo power limit | ≤ 8 W @6V | ≤ 8 W @6V (unchanged) |
| Servo stall current | **≤ 4 A @6V** | **≤ ___ A @6V — value missing in V0 [V0-ERRATA]** |
| Linear servo | N/A power, ≤ 1 amp**s** @6V | N/A power, ≤ 1 amp @6V |
| Example servo lists | identical | identical |
| **R503 limit** | **8 motors + 10 servos** | **8 motors + 8 servos** |
| R503 orange boxes | + hub 5 V/5 A servo-budget warning; + total-battery-power/brownout warning | **both deleted** |
| R504.B cross-ref | "(per R503)" — wrong rule | "(per **R609**)" — correct (wire sizing) |
| R504.C example | "re-programming or modification for continuous rotation" | "**setting soft limits** or modification for continuous rotation" |
| R504.D | "**minimal** labeling may be applied" | "labeling may be applied" |
| Table 12-3 | 7 rows | identical 7 rows |
| R506 headline | "No relays or alternative electrical actuation" | "The use of relays, electromagnets, and electrical solenoid actuators is prohibited" |

### 6.5 The deleted stored-energy rule

DECODE **R608** read (paraphrased): non-electrical energy stored at the start of a MATCH may come **only** from
(A) a change in the altitude of the ROBOT's centre of gravity, or (B) deformation of ROBOT parts (springs,
rubber bands, surgical tubing, etc.).

BIOBUZZ V0 has **no equivalent rule**. I searched the full V0 text for "surgical", "altitude", "center of
gravity", "rubber band", "deformation" and "non-battery" — zero hits outside the R303 odometry example and the
R801 gas-spring text.

**[INFER] Reading:** with gas springs now legal (R801.A), the DECODE whitelist would have been
self-contradictory, so FIRST appears to have deleted the whitelist and let R506 (no solenoids/electromagnets/
relays), R601 (one battery), R602 (peripheral batteries only) and R801 (air) do the policing. **UNVERIFIED**
whether this was intentional. Practical rule of thumb until Kickoff: if your stored energy is a spring, a raised
mass, or a manufacturer-sealed gas spring, you are on solid ground; anything more exotic (flywheel energy banks,
chemical, combustion) should go to the Q&A on day one.

### 6.6 Power-mixing rule (R619 → R613) — read this if you run sensors

| DECODE R619 | BIOBUZZ R613 |
|---|---|
| A. no outside power on devices connected to a regulating device, except communication connections (RS485/USB/PWM) | A. "sensors, encoders, and other devices must be powered **solely** by the power regulation device they are connected to. Do not use outside power sources (e.g., custom circuits or a second hub) to power them" |
| B. port power only for devices on that port — **"The only exception to this is +5V power from the +5V power port on the REV Control Hub or Expansion Hub may be used in conjunction with any Analog, Digital, or I2C port on that device."** | B. "power from a specific port may only power devices plugged into that exact port. Do not cross-wire power to other ports, and do not combine power from multiple ports into a single power bus/line" — **the +5 V/port-combination exception is gone** |
| C. 6 V from servo power modules only for servos | C. same |
| — | **D. (new)** "the +5V Aux port on a REV hub may be used to power devices **not connected to other power regulation devices except via USB**" |

**[INFER] Practical effect:** the common trick of feeding a power-hungry I2C sensor or LED driver from the
+5 V Aux port while its signal lines sit on a hub I2C/digital port now appears **illegal** under R613.B/D as
written. +5 V Aux remains legal for a powered USB hub (R611.B) and for standalone devices. Verify at Kickoff or
via Q&A before committing to a wiring harness that depends on the old exception.

### 6.7 The missing gamepad rule

DECODE R903 + Table 12-12 limited the OPERATOR CONSOLE to **no more than 2** electrically-unmodified gamepads
from a closed list: Logitech F310 (940-00010); Xbox 360 Controller for Windows (52A-00004, wired mode only);
Sony DualShock 4 for PS4 (explicitly **not** the DualSense Edge); Sony DualSense for PS5; Etpark Wired
Controller for PS4 (REV-39-1865 / REV-31-2983); REV Robotics USB PS4-Compatible Gamepad; Quadstick in
Xbox 360 emulation mode. Plus: back-paddle-style non-electronic enhancements legal; ferrite clip recommended;
different colours OK if the same model; spare gamepads OK if ≤2 connected.

**BIOBUZZ V0 has none of this.** The only mention of "gamepad" in the entire manual is R901.B's phrase
"for connecting one or more gamepads."

**[V0-GAP] — treat as the single highest-probability Kickoff insertion.** Do not buy an off-list controller on
the theory that the allowlist is gone, and do not design a 3-gamepad console.

---

## 7. Rules that historically cause inspection failures

Ranked from the DECODE Inspection Checklist (`manuals/archive/supplemental/2025-26_DECODE_InspectionChecklist.pdf`,
rev 25-26.2), the DECODE Inspection Quick Reference (rev 25-26.2), and Q&A volume. **[PRIOR]** for the failure
frequency; **[V0-FINAL]** for the BIOBUZZ rule numbers.

| Rank | Failure mode | BIOBUZZ rule | How to pre-empt it |
|---|---|---|---|
| 1 | **Robot exceeds the expansion envelope at maximum *mechanical* extension** (software limits don't count for horizontal) | R105 | Build relocatable hard stops. At self-inspection, extend every mechanism to its physical limit — including two unlinked mechanisms **simultaneously** — and measure. |
| 2 | **Wire gauge / colour** — 22 AWG on a motor lead, unlabeled wire with no evidence | R609, R610 | Buy labelled wire. Keep a scrap sample of each gauge in the pit. Note BIOBUZZ only colour-codes the 12 V and +5 V aux buses now. |
| 3 | **Illegal servo** (stall current or output power over the cap) | R502 | Check against the Inspection Quick Reference pre-verified list. **[PRIOR]** DECODE's known-illegal list: AGFRC 40KG A73BHLW V2 (4.1 A / 6.05 W), DSSERVO DS3225PRO (4.2 A / 8.56 W), Hitec HS-805BB Monster Resin (6.0 A / 4.53 W), Smraza SC55-NA 45KG Coreless (2.4 A / 8.34 W). |
| 4 | **Actuator count over budget across all configurations** | R503 + I302 | Count every motor and servo in the pit, not just the ones bolted on. New ceiling is **8/8**. |
| 5 | **TILE-damaging traction devices** | R201 | **[PRIOR]** Named illegal-on-tiles in DECODE's Quick Reference: AndyMark **am-2256 HiGrip** wheels, AndyMark **am-3309 Roughtop** tread, **Gorilla Anti-Slip Tread Tape**. BIOBUZZ removed the names from the manual but not the prohibition. |
| 6 | **Illegal servo signal/power adapters** | R505, R612 | **[PRIOR]** Named illegal in DECODE's Quick Reference: **goBILDA Servo Travel Tuner** (also named in BIOBUZZ R612 orange box), **goBILDA Servo Power Distribution Board (8-channel)**, **goBILDA 4-Channel Servo Extension via CAT6**. |
| 7 | **Sign non-compliance** — too small, not solid, unsupported, only one, or on parallel faces | R401-R403 | Print the official template at 100%, mount on a rigid backer bolted to frame, put them 90° apart. |
| 8 | **Frame used as a current path / uninsulated grounding** | R605 | **[PRIOR]** Self-test: unplug the battery and measure >120 Ω from the switch input terminals to any point on the frame. Anodizing must be scratched off under the grounding strap terminal. |
| 9 | **Custom circuit over 5 V or altering a power path** | R607, R612 | No buck/boost converters anywhere in the battery→hub→actuator chain. |
| 10 | **Diagnostic LEDs / RC screen not visible** | R606 | Mount the hub so a panel can be removed, or keep it visible in match config so the FTA can actually help you. |
| 11 | **Modified motor or servo** — encoder removed, rear cap removed, 4th wire added | R504 | See §9 for the exact prior rulings. |
| 12 | **Self-inspect screen warnings / device naming** | R705, R711 | Name devices `#####-RC`/`#####-DS`, change the Control Hub Wi-Fi password, Bluetooth off, forget stale Wi-Fi Direct groups on the DS. |
| 13 | **OPERATOR CONSOLE oversize or wireless-enabled** | R903, R904 | New depth is 18 in. — measure with the power bank *inside* the box. Kill Bluetooth on everything. |
| 14 | **Sharp edges / entanglement / loose ballast** | R201, R202 | Deburr everything; secure or delete ballast. |

---

## 8. The quiet design constraints (rules that shape strategy, not just legality)

1. **8 motors / 8 servos across all configurations (R503).** With a holonomic drive (4 motors) you have **4**
   motors left for the entire game mechanism set. Servos are the scarce resource this season — down 33% from
   ITD. Budget them on paper before CAD.
2. **Max two hubs (R701).** One Control Hub + one Expansion Hub = 8 motor ports and 12 servo ports. Motor ports
   are the binding constraint, servo ports are not — the servo constraint is R503 and the 5 V/5 A hub budget.
3. **No weight limit (R104), but expansion is limited (R105).** In a no-weight-limit game, mass is cheap and
   *reach* is expensive. Historically this pushes teams toward heavy, low, stable bases with tightly-constrained
   extensions.
4. **"Fully stationary" at the start (R102).** Any strategy that relied on pre-spinning a flywheel, pre-tensioning
   in motion, or a mechanism creeping into position during the pre-match hold is dead. Holding *position* with
   powered motors/servos is still fine (R103.B).
5. **COTS single-DoF ceiling (R303).** You may not buy a 2-DoF wrist. Every added DoF past the first must be
   your own fabrication — which is itself the R101 "your team's robot" test.
6. **No detachable components (R105).** No deployable minibots, no dropped anchors, no shed covers.
7. **Robot must be removable from the FIELD unpowered, and elements must come out unpowered (R203).** Ratchets,
   worm drives and self-locking lifts need a manual release. Design it early; it's an afternoon of retrofit later.
8. **No downforce mechanisms (R204).** No suction, no tile-grabbing. Traction is limited by weight and legal
   wheel compounds only.
9. **No cost cap.** I searched the entire V0 manual: FTC has **no** ROBOT bill-of-materials cost limit
   (the only "cost" mention is the VENDOR definition's reference to "any applicable cost accounting rules").
   Cost is not a rule constraint — sourcing and the VENDOR/COTS definitions are.
10. **Gas springs are the new free lunch (R801.A).** Constant force, zero motor budget, zero servo budget,
    zero electrical budget. **[INFER]** Expect this to be the defining mechanical trend of BIOBUZZ.
11. **No third-party telemetry over the robot network (R704.D).** Your tuning workflow must move to
    OnBotJava/Android Studio + the Driver Station app, or to a wired/off-network workflow in the pit.
12. **AprilTag-mimicking imagery is banned (R202.C).** Applies to decorations, bumper art and sponsor panels.

---

## 9. Prior-season official Q&A rulings that still bind (rule text unchanged)

**[PRIOR]** — from `manuals/archive/supplemental/2025-26_DECODE_Complete_QA.html`. The underlying BIOBUZZ rule
text is materially identical, so these are strong indicators, **not** BIOBUZZ rulings. R105 rulings are the
exception — BIOBUZZ R105 has no numbers yet, so treat those as *framework* precedent only.

| Topic | DECODE rule | Ruling |
|---|---|---|
| Expansion envelope orientation (Q9, Q54, Q67) | R105 | Sizing constraints are **relative to the ROBOT** based on its STARTING CONFIGURATION — "if a ROBOT rotates itself relative to the STARTING CONFIGURATION the expansion limits also rotate with the ROBOT." **BIOBUZZ R105 retains this exact framing sentence.** |
| Mechanical capability vs. actual behaviour (Q11, TU03) | R105 | "The ROBOT at no time may be **physically capable** of extending beyond the expansion limit… This rule defines the ROBOT's legal mechanical limits **as it is built**, not only what it does at any given instant." Two non-linked mechanisms are measured extended together. |
| Servo as a physical stop (Q16) | R105 | **No** — "using software to limit the position of a servo does [not]" satisfy a physical-constraint requirement. |
| Flexible extensions, wires (Q20, Q122) | R105 | "R105 includes all parts of a ROBOT, including **wires, cable ties, chains**, and other flexible extensions." |
| Vertical limit demonstration (Q94) | R105 | Robots must show **all** mechanical extensions at inspection, vertical included. |
| Turrets (Q170) | R105 | A turret rotating the chassis outside the envelope counts as expansion, intended or not. |
| Removing a motor encoder (Q79) | R504 | **Not allowed.** |
| Removing the goBILDA Yellow Jacket rear cap (Q211) | R504.B | Only with a **functionally equivalent** enclosure replacement; electrical tape is not equivalent. |
| Gearbox changes / shaft length (Q29, Q218) | R501, R504 | Any gearbox may be used with any legal motor; modifying the **gearbox** (incl. output shaft length) is generally fine as long as the **motor** itself is untouched. |
| Adding a 4th-wire encoder to a 3-wire servo (Q92) | R504 | **Not allowed** unless the manufacturer endorses it and publishes explicit modification documentation. |

---

## 10. Every "released at Kickoff" gap and errata in Section 12

### 10.1 Explicit deferrals [V0-DEFERRED]

| # | Location | What's missing | Design decisions it blocks |
|---|---|---|---|
| D1 | **R105**, p. 68 | *"Sizing Constraints and more details will be released at Kickoff"* — the entire expansion envelope, horizontal and vertical, plus whether software limits suffice, plus inspection demonstration procedure. | Lift height, arm reach, extension travel, turret radius, intake overhang, endgame climb geometry. **The single biggest blocker.** |
| D2 | **R201** orange box, p. 68 | Cross-reference to the SCORING-ELEMENT-damage game rule is a literal placeholder: "violations of this rule and **GXXX**". | Nothing structural; tells you a G-rule will pair with R201. |
| D3 | **R701** orange box, p. 83 | "Check the FIRST Tech Challenge **Firmware Update Page (Coming Soon)**" — DECODE's Table 12-11 of recommended Control Hub OS / Hub firmware / RC & DS app / Driver Hub OS / Servo Hub firmware versions is gone with no replacement. | Which SDK and firmware to target for off-season code. Nothing stops you writing code now; expect a version bump at Kickoff. |

### 10.2 Unexplained gaps — verify at Kickoff [V0-GAP]

| # | Missing from V0 | DECODE equivalent | Risk if you assume it's gone |
|---|---|---|---|
| G1 | **Gamepad allowlist and 2-gamepad cap** | R903 + Table 12-12 | **High.** Buying an off-list controller or building a 3-gamepad console. |
| G2 | **Android smartphone allowlist / Android 7 minimum** | R704 + Table 12-10 | Medium. Using an unsupported phone as RC or DS. |
| G3 | **Non-battery stored-energy whitelist** | R608 | Medium. Designing an exotic energy store. |
| G4 | **"Batteries are not ballast"** | R605 | Low, but don't use spare batteries as weight. |
| G5 | **"Battery must be securely mounted"** | R606 | Low — R201 (unsecured components) still applies. Mount it properly regardless. |
| G6 | **"Electrical connections robust and insulated"; explicit blessing of COTS slip rings / rolling contacts** | R607 | Medium if you were planning a slip ring on a turret. Nothing now explicitly permits *or* forbids them. |
| G7 | **Explicit hydraulic ban** | R203.F | Low. |
| G8 | **Encapsulated/painted lead ballast carve-out** | R203.H | Medium. BIOBUZZ R202.E bans "hazardous materials like liquid mercury or lead" with no carve-out. Use steel or brass. |
| G9 | **Named TILE-damaging traction devices** (am-2256, am-3309) | R201 orange box | Low. The prohibition survives; only the names left the manual. |
| G10 | **>120 Ω frame-isolation compliance test** | R611 orange box | Low. Still the right self-test. |
| G11 | **"Work outside pit hours is allowed"** | R307 | Medium at events. BIOBUZZ instead has restrictive E-rules on where you may practice and fabricate. |
| G12 | **Hub 5 V/5 A servo power-budget warning** | R503 orange box | Medium. The hardware limit is unchanged; only the warning is gone. |
| G13 | **DECODE's clarifier that cameras and non-RF sensors aren't "wireless communication"** | R709 orange box | Low. |

### 10.3 Apparent document defects [V0-ERRATA] — check Team Update 00

| # | Location | Defect |
|---|---|---|
| E1 | **R502, Table 12-2**, p. 76 | **The servo stall-current limit value is missing.** The cell renders as "≤ ⎵ amps @6V". DECODE's value was **≤ 4 A @6V**. Until corrected, use 4 A as your working number and confirm at Kickoff. |
| E2 | **R601.A**, p. 78 | Fuse replacement is "installed per **R610**" — but R610 is the wire-colour rule. Almost certainly meant to point at a wiring/installation rule. |
| E3 | **R612.C**, p. 82 | "any two power regulating devices (per **R607**)" — R607 is the CUSTOM CIRCUIT rule; power-regulating devices are defined in **R505**. (DECODE had the same class of error.) |
| E4 | **Table 12-8**, p. 81 | REV Core Hex listed as "**REV-14-1300**"; Table 12-1 says "**REV-41-1300**". |
| E5 | **R710.B**, p. 86 | The second standard number does not render in the PDF text layer ("IEC/EN ⎵7"). DECODE reads **IEC/EN 62471**. |

### 10.4 Supporting documents not yet published for 2026-27

- **2026-27 Inspection Checklist** — R-rule-mapped; the DECODE version is the best proxy.
- **2026-27 Inspection Quick Reference** — referenced by name in R502 for the pre-verified servo list, the
  known-illegal servo list, illegal servo signal/power adapters, illegal traction devices, and the RC/DS wiring
  diagrams. **This is the second-most-important kickoff-day download after the manual itself.**
- **Online servo mechanical-power calculator** — referenced in R502.
- **ROBOT Wiring Guide** — referenced in R605.
- **FIRST Tech Challenge Firmware Update Page** — referenced in R701 ("Coming Soon").
- **DRIVER STATION / ROBOT CONTROLLER naming instructions** — referenced in R705.

*(Already published: the **2026-27 ROBOT SIGN template**, US Letter and A4 — cross-checked in §4.1.)*

---

## 11. Kickoff-day Section 12 review checklist

Work this list in order on 12 September 2026; it takes ~30 minutes and covers everything this document can't.

1. **R105 first.** Read it and every figure. Record: horizontal limit, vertical limit(s), whether horizontal
   must be mechanically constrained, whether vertical may be software-limited, and the paired G-rules.
2. **Diff R503.** Confirm 8 motors / 8 servos held. (Team Updates have changed actuator counts mid-season before.)
3. **Fill E1:** find the servo stall-current number in Table 12-2. If it's still blank, file a Q&A on day one.
4. **Search the manual for "gamepad".** If a gamepad table reappeared, capture the allowlist and the count cap.
5. **Search for "Android" / "smartphone".** Check whether a device allowlist reappeared.
6. **Check R701's orange box** for the live Firmware Update Page; record target Control Hub OS, hub firmware,
   RC/DS app and Servo Hub firmware versions.
7. **Re-read R704.D** word for word and decide your telemetry workflow before writing any tuning code.
8. **Confirm R801.A still permits pre-charged sealed gas springs.** This is a big enough reversal that a Team
   Update walk-back is conceivable.
9. **Diff Table 12-1 and Table 12-2** for added/removed motors and servos.
10. **Download the Inspection Checklist and Inspection Quick Reference** the moment they post; re-check the
    known-illegal servo, traction-device and servo-adapter lists against your BOM.
11. **Check whether DECODE's R605/R606/R607/R608 (ballast, battery mounting, connection robustness, stored
    energy) reappear** anywhere in the Kickoff manual.
12. **Re-verify R903's OPERATOR CONSOLE depth** (18 in. in V0) — measure your box.

---

## 12. Sources

| Claim class | File |
|---|---|
| All BIOBUZZ rule text, tables, figures | `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf`, pp. 64-88 (§12); p. 18 (§1.7.1 conventions); pp. 23-24 (I301-I303); p. 39 (E510-E511); pp. 34-35 (E106-E109) |
| Text extract used for search | `.../manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`, `.../BIOBUZZ_V0_layout.txt` |
| DECODE baseline (V6 §12, post-TU32) | `.../manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf`, pp. 119-152; pp. 18-20 (I301-I307) |
| ITD servo count trend | `.../manuals/archive/2024-25_ITD_layout.txt`, R503 |
| ROBOT SIGN template cross-check | `.../manuals/archive/supplemental/2026-27_BIOBUZZ_RobotSign_USLetter.pdf` (stamped "US Letter V26-27.1") |
| Inspection failure modes | `.../manuals/archive/supplemental/2025-26_DECODE_InspectionChecklist.pdf` (rev 25-26.2) |
| Known-illegal servos / traction devices / servo adapters | `.../manuals/archive/supplemental/2025-26_DECODE_InspectionQuickReference.pdf` (rev 25-26.2), pp. 6, 9, 10 |
| Prior-season official rulings | `.../manuals/archive/supplemental/2025-26_DECODE_Complete_QA.html` (Q9, Q11, Q16, Q20, Q54, Q67, Q79, Q92, Q94, Q122, Q170, Q211, Q218) |

**Method notes.** Several tables in both manuals mis-extract with plain text tools because of merged and
page-split cells (notably Table 12-2, Table 12-3, Table 12-4, Table 12-7 and Table 12-8). Every table value in
this document was re-derived from the PDF's own cell geometry using PyMuPDF `find_tables()` plus span
coordinates, and the DECODE↔BIOBUZZ wire-table difference was checked against cell rectangles specifically to
avoid reporting a page-break artifact as a rule change. Evergreen/non-Evergreen classification was determined
by reading headline span colours (green `#06844b` = Evergreen, orange `#ed7d31` = game-specific) on every page
of §12.

**Security note.** No prompt-injection or instruction-like content addressed to an AI system was found in any
of the PDFs, HTML files or templates examined for this document.
