<!--
  ============================================================================
  PRE-EVENT SELF-INSPECTION CHECKLIST — BIOBUZZ 2026-27
  ============================================================================
  SOURCE OF EVERY LINE:
    Section 12 ROBOT Construction Rules (R101-R904)  — FINAL in the V0 manual
    Section 3  Competition Eligibility and Inspection (I101-I304) — FINAL in V0
    File:  manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf
    Rule-by-rule analysis: reference/CONSTRUCTION-RULES-R.md

  WHY YOU SELF-INSPECT (BIOBUZZ section 3.3.1, verbatim):
    "An Inspection Checklist is available to help teams self-inspect their
     ROBOT. Teams are strongly encouraged to self-inspect before every event."
    and
    "Inspection is not comprehensive. Teams are expected to adhere to the spirit
     of the rules in Section 12 ROBOT Construction Rules (R), even if INSPECTORS
     do not check every part of the ROBOT."

  THIS IS NOT THE OFFICIAL CHECKLIST.
    As of 2026-08-22 FIRST has NOT published the 2026-27 Inspection Checklist or
    the 2026-27 Inspection Quick Reference. DOWNLOAD BOTH THE MOMENT THEY POST
    (Kickoff, 12 September 2026) and reconcile this file against them. The Quick
    Reference in particular carries the pre-verified servo list, the KNOWN-ILLEGAL
    servo list, illegal servo signal/power adapters, illegal traction devices,
    and the RC/DS wiring diagrams — it is the second-most-important kickoff
    download after the manual.
    (reference/CONSTRUCTION-RULES-R.md section 10.4)

  GAME-SPECIFIC ITEMS ARRIVE AT KICKOFF.
    Section 12 is final, but it contains exactly ONE game-specific rule: R105,
    and its numbers are DEFERRED. The V0 manual says, on p. 68:
        "Sizing Constraints and more details will be released at Kickoff"
    So every dimension in section D below is a BLANK until 12 September 2026.
    Sections 8-11 (Game Overview / ARENA / Game Details / Game Rules) and 13-14
    are also placeholders in V0. Anything in this checklist that depends on the
    game itself is marked  [KICKOFF].

  COVERAGE AUDIT — re-verified 2026-08-22 against the extracted manual text.
    The V0 PDF contains exactly 52 R-rule IDs. Extracted with:
        grep -oE "R[0-9]{3}" manuals/2026-27_BIOBUZZ/v0_pymupdf.txt | sort -u -V
    They are:
        R101-R105  R201-R204  R301-R305  R401-R403  R501-R506
        R601-R613  R701-R711  R801       R901-R904
    Every one of those 52 is checked somewhere below, plus I101-I103 and
    I301-I304. If you re-run the grep after a Team Update and get an ID that is
    not in the list above, that rule is NEW and this file does not cover it.

  ⚠ DISCREPANCY TO BE AWARE OF (2026-08-22).
    reference/CONSTRUCTION-RULES-R.md enumerates additional IDs — R205-R208,
    R306-R307, R614-R619, R712-R718, R905-R906 — that do NOT appear anywhere in
    the BIOBUZZ V0 PDF text. Do not add checklist rows for them on that basis.
    Treat the PDF as ground truth; treat that file's extra IDs as UNVERIFIED
    until you can point at a page number in a released manual or Team Update.

  HOW TO USE
    - Run the whole thing the WEEK BEFORE an event, not the night before. Half
      the failures below need a part order or a reprint.
    - Run sections A, D and H again the MORNING of the event, after transport.
    - Two people. One reads, one checks. Never the person who built it, alone.
    - Print it. Tick it with a pen. Date it. File it in  meetings/ .
  ============================================================================
-->

# Pre-Event Self-Inspection — Team <NNNNN>

| | |
|---|---|
| **Event** | <name / code> |
| **Date run** | <YYYY-MM-DD> |
| **Reader** | <First L.> |
| **Checker** | <First L.> |
| **Robot configuration(s) inspected** | <list every configuration you will bring — see I301 / I302> |
| **Manual version this was checked against** | V0 2026-07-31 + Team Updates through #<n> |

**Result:** ☐ READY  ☐ READY WITH FIXES (list at the end)  ☐ NOT READY

---

## A. Sizing and configuration

| ☐ | Rule | Check | Notes |
|---|---|---|---|
| ☐ | **R102** | Fits an **18 × 18 × 18 in. cube (45.70 cm each side)** in STARTING CONFIGURATION. Check with a real sizing tool, not a tape measure. | Pre-loaded SCORING ELEMENTS may protrude |
| ☐ | **R102** | **Every part is fully stationary** in the starting configuration. Nothing spinning, nothing creeping, no pre-tensioned mechanism in motion. | This kills pre-spun flywheels |
| ☐ | **R102** | The robot is **fully self-contained** — nothing rests on the field or a person | |
| ☐ | **R103** | Holds the starting configuration **self-supported**: no force on the sizing tool's sides or top. Unpowered restraints and/or a pre-positioning OpMode are both allowed | If you use an OpMode, **tell the inspector** |
| ☐ | **R103** | If you hold position with powered motors/servos: they can survive several minutes stalled without thermal failure | Inspection queues are long |
| ☐ | **R102/I301** | **EVERY configuration** you will use in a match has been sized, not just the one you carried in | |
| ☐ | **R105** | Single assembly — **no component is designed to intentionally detach** | No minibots, no dropped anchors |
| ☐ | **R105** `[KICKOFF]` | Maximum expansion measured at **full MECHANICAL extension** (software limits do not count for a mechanical check), against the Kickoff envelope: **<record the number here on 12 Sep 2026>** | **Historically the #1 inspection failure** |
| ☐ | **R105** `[KICKOFF]` | Two unlinked mechanisms extended **simultaneously**, measured together | The case teams always miss |
| ☐ | **R104** | No weight limit — nothing to check. But confirm you can lift and cart it, and that TILE damage risk is addressed under R201 | |

**How to pre-empt the R105 failure:** build relocatable hard stops now, so that
when the envelope number posts at Kickoff you move a stop rather than redesign.

---

## B. Safety and damage prevention

| ☐ | Rule | Check |
|---|---|---|
| ☐ | **R201** | Run a bare hand over **every** exterior surface and edge. No sharp edges, burrs, exposed screw points or abrasive surfaces |
| ☐ | **R201** | No TILE-damaging traction devices. *(BIOBUZZ removed the named list; the prohibition survives. DECODE's Quick Reference named AndyMark **am-2256 HiGrip** wheels, AndyMark **am-3309 Roughtop** tread, and **Gorilla Anti-Slip Tread Tape** as illegal on tiles — treat as a strong prior until the 2026-27 Quick Reference posts.)* |
| ☐ | **R201** | No unsecured ballast. The rule names sand, coffee beans, kitty litter, glitter and ball bearings. No liquids or gels, no tire sealant, no graphite powder, no excess lubricant |
| ☐ | **R202.A** | No vision-blocking shields or curtains |
| ☐ | **R202.B** | No distracting audio, and nothing that mimics a MATCH sound |
| ☐ | **R202.C** | **No imagery that mimics 36h11 AprilTags** — check decorations, sponsor panels, bumper art, and any printed pattern |
| ☐ | **R202.D** | No flammable gas, flames or pyrotechnics |
| ☐ | **R202.E** | No hazardous materials. The rule names **liquid mercury and lead**. ⚠ **DECODE's carve-out permitting painted/encapsulated/sealed lead ballast is GONE in BIOBUZZ.** Use steel or brass |
| ☐ | **R202.F** | No high-intensity lights except brief targeting use; the LRI or Head Referee may order them disabled |
| ☐ | **R202.G** | No animal-based materials |
| ☐ | **R202.H** | Nothing designed to damage or flip another robot |
| ☐ | **R202.I** | No entanglement risks — loose straps, dangling cable, open hooks |
| ☐ | **R202.J** | No lighting flashing **faster than 5 Hz** |
| ☐ | **R203** | **Power the robot OFF, then**: a SCORING ELEMENT can be removed by hand, and the robot detaches from any field element. Ratchets, worm drives and self-locking lifts need a manual release — design it early, it is an afternoon of retrofit later |
| ☐ | **R204** | No mechanism increases downforce by gripping the field surface or by generated-airflow suction |
| ☐ | **R202/§3.3.1** | If the robot has **stored energy** in the inspection configuration (a stretched spring, a charged gas shock), **tell the inspector before they touch it** — the manual explicitly asks teams to do this |

---

## C. Fabrication and COTS legality

| ☐ | Rule | Check |
|---|---|---|
| ☐ | **R101** | **Your students built the robot and its MAJOR MECHANISMS.** A MAJOR MECHANISM = an assembly addressing at least one game challenge. Gearboxes, sub-mechanisms and COTS items are not MAJOR MECHANISMS. This is asked verbally — have the answer |
| ☐ | **R301** | No COTS MAJOR MECHANISM purpose-built to complete a game task. Exceptions: a COTS drive CHASSIS, and COTS major mechanisms from official FIRST **StarterBots** |
| ☐ | **R301** | You did not have a vendor "build to print" a publicly available purpose-built solution — new sentence in BIOBUZZ, explicitly against the spirit of the rule |
| ☐ | **R303** | **Every COTS component/mechanism has at most 1 degree of mechanical freedom.** Exempt: ratcheting devices, holonomic wheels, dead-wheel odometry kits, misalignment couplers, variable-angle connectors. ⚠ **A COTS gripper with an added wrist is multi-DoF and illegal** |
| ☐ | **R302** | Any modified COTS part / raw material is still legal after modification |
| ☐ | **R305** | **No current-season SCORING ELEMENT or replica is used in robot construction** |
| ☐ | **R304** | Pre-Kickoff software, designs and fabricated items are explicitly permitted — nothing to fix, but know this if asked |

---

## D. Robot signs

Print the official **2026-27 ROBOT SIGN template** at 100% scale.

| ☐ | Rule | Check | Number |
|---|---|---|---|
| ☐ | **R401** | **At least two** signs, on **opposite or adjacent (90° apart)** surfaces. The top of the robot counts as a surface | ≥ 2 |
| ☐ | **R401.A** | Robust material (deliberately undefined — make a good-faith effort) | |
| ☐ | **R401.B/C** | Each sign **≥ 6.5 in. wide × ≥ 2.5 in. tall** | 6.5 × 2.5 in |
| ☐ | **R401.D** | Supported by robot structure or frame, not floating on a wire | |
| ☐ | **R401** | Readable from **12 ft (3.65 m)** | 12 ft |
| ☐ | **R402** | Each sign contains a **solid, opaque red or blue rectangle** of at least 6.5 × 2.5 in. (16.50 × 6.35 cm). A non-rectangular sign is legal only if a full rectangle of that size fits inside it | |
| ☐ | **R402.E** | **No power used to illuminate or reveal the alliance colour** | |
| ☐ | **R402** | A reversible or configurable sign can never show the opposite colour | |
| ☐ | **R403.A** | Team numbers are solid opaque **white Arabic numerals, approximately 2.25 in. (5.70 cm) tall** | 2.25 in |
| ☐ | **R403.B** | **≥ 0.25 in. (0.60 cm)** of background around the numbers | 0.25 in |
| ☐ | **R403.C** | Numbers are **not vertically stacked** and not mirrored. A sign rotated 90° so the number reads bottom-to-top is fine | |
| ☐ | **R403.E** | Numbers are **not powered or illuminated**. No edge-lit engraved plastic. No LED displays | |
| ☐ | — | **Spare signs in the pit kit.** If you have no colour printer at the event, the Head Referee may approve a substitute — handwritten on plain paper is explicitly acceptable as a fallback | |

---

## E. Motors, servos and actuators

| ☐ | Rule | Check | Our number |
|---|---|---|---|
| ☐ | **R501** | Every motor is on the **Table 12-1** legal list (13 families). Motors integral to COTS sensors, and factory vibration/autofocus motors inside COTS computing devices, do not count toward R503 | |
| ☐ | **R503 + I302** | **Total ≤ 8 motors and ≤ 8 servos, summed across EVERY configuration you brought to the event** — including mechanisms sitting in the pit that are never on the robot at the same time. Count them physically, in the pit | <n>/8 motors, <n>/8 servos |
| ☐ | **R502** | Every servo: mechanical output power **≤ 8 W at 6 V**, computed as `P = 0.25 × stall torque (N·m) × no-load speed (rad/s)` | |
| ☐ | **R502** | Every servo: stall current within the cap at 6 V. ⚠ **The value is BLANK in the V0 PDF (a document defect). DECODE's value was ≤ 4 A @6V — use 4 A as the working number and confirm at Kickoff.** Linear servos: **≤ 1 A @6V** | |
| ☐ | **R502** | Datasheets printed and in the pit binder for every servo, or the servo is on the Quick Reference pre-verified list. *(DECODE's known-illegal list, as a prior: AGFRC 40KG A73BHLW V2, DSSERVO DS3225PRO, Hitec HS-805BB Monster Resin, Smraza SC55-NA 45KG Coreless.)* | |
| ☐ | **R502** | Servos rated 6–8.4 V may misbehave on the hub's **5 V** servo ports. Verify each servo actually works at the voltage it is fed | |
| ☐ | **R504** | **No motor or servo modification** beyond the allowed list: mounting brackets and output interface (incl. pinion gears), lead trimming/connectors/splices, manufacturer-specified soft-limit setting or continuous-rotation conversion, non-obstructing labels, terminal insulation, like-for-like repairs, manufacturer-recommended maintenance. ⚠ **Encoder removed, rear cap removed, or a 4th wire added = fail** | |
| ☐ | **R505** | Every actuator control signal originates from a **Table 12-3** approved power-regulating device. No signal-generating or signal-altering device between a hub and a servo. ⚠ *(DECODE's Quick Reference named the **goBILDA Servo Travel Tuner**, the **goBILDA 8-channel Servo Power Distribution Board**, and the **goBILDA 4-Channel Servo Extension via CAT6** as illegal — the Travel Tuner is named again in the BIOBUZZ R612 orange box.)* | |
| ☐ | **R505** | Per-device load limits from Table 12-3 respected: hub motor ports **2 motors/port**, hub servo ports **2 servos/port**, Servo Power Module / Servo Hub / Servo Power Injector / Servo Power Block **2 servos/port**, SPARKmini **2 motors/device** | |
| ☐ | **R506** | **No relays, electromagnets or electrical solenoid actuators**, or systems built around them | |

---

## F. Power distribution and wiring

| ☐ | Rule | Check |
|---|---|---|
| ☐ | **R601** | **Exactly one** 12 V NiMH main battery, from **Table 12-4** (am-5290 · goBILDA 3100-0012-0020 · Matrix 14-0014 · REV-31-1302 · Studica 70025 · TETRIX W39057 · WATTOS WT-NMH1230) |
| ☐ | **R601.A** | Battery unaltered, except the fuse may be replaced with a COTS-equivalent **in-line 20 A ATM mini blade fuse** |
| ☐ | **R601.B** | Connectors, if swapped, are Anderson Powerpole, XT30 or comparable |
| ☐ | **R602** | Any secondary battery is a self-contained peripheral only: COTS USB pack **≤ 100 Wh (27,000 mAh @3.7 V)**, **5 V/5 A or 12 V/5 A max per port via USB-PD**. It powers **no actuator** and **no device receiving control signals from the robot control system** — the only exceptions being powered USB hubs and RC smartphones |
| ☐ | **R603** | **Exactly one** main power switch, from **Table 12-5** (am-4969 · goBILDA Floodgate 3103-0005-0001 · REV-31-1387 · Studica 70182 · TETRIX W39129 · WATTOS WTS-SW1220) |
| ☐ | **R603.B** | Switch accessible to the team, away from high-speed moving parts and pinch hazards. BIOBUZZ explicitly permits mounting behind a removable panel |
| ☐ | **R604** | Fuses used exactly as the manufacturer directs. No modification, no higher trip point, **no self-resetting fuses** |
| ☐ | **R605** | **Frame is not a conductor.** All wiring and devices electrically isolated from the frame. **[PRIOR]** Self-test: unplug the battery and measure **> 120 Ω** from the switch input terminals to any point on the frame *(this numeric test was in DECODE and was dropped from BIOBUZZ, but it is still the right way to check)* |
| ☐ | **R605** | If a grounding strap is used, it is from **Table 12-6** (am-4648a · REV-31-1269 · Swyft SR-Ground-01), connects to a fully-COTS component with an XT30 connector, and anodizing is scratched off under its frame terminal |
| ☐ | **R606** | Every power-regulating device, all wiring and all fuses **can be made visible** for inspection. The Robot Controller is mounted so its diagnostic lights / screen can be made visible |
| ☐ | **R607** | No CUSTOM CIRCUIT outputs a regulated voltage above **5 V**, except solely to power LEDs |
| ☐ | **R608** | Every power-regulating device is energized only as **Table 12-7** specifies: Hub and Servo Power Injector = **XT30**; Servo Power Module = screw terminals; Servo Hub = power terminals; SPARKmini = Power input; Studica Servo Power Block = JST-VH |
| ☐ | **R609** | Wire gauge per **Table 12-8**: **18 AWG** for 12 V main battery power, motor power, and any 11–20 A fuse-protected circuit; **22 AWG** for TETRIX MAX 12V DC and REV Core Hex motor power, PWM/servo, LEDs, and ≤10 A circuits; **28 AWG** for signal-level circuits. Manufacturer-supplied integrated wires are exempt. **Parallelling small wires is not allowed** |
| ☐ | **R610** | Colour code **only** the 12 V main power bus and the +5 V aux bus, full length: positive = red / yellow / white / brown / black-with-stripe; negative = black or blue. This does **not** apply to motor wiring, signal wiring, servo cables or manufacturer-attached wires |
| ☐ | **R611** | Any powered USB hub is powered only by an R602-approved COTS USB battery pack, or by the +5 V auxiliary port on a REV hub |
| ☐ | **R612** | **No custom circuit alters a power or control path** between battery↔switch, switch↔regulating device, two regulating devices, or regulating device↔actuator. **No buck/boost converter anywhere in the battery path.** High-impedance voltage or low-impedance current monitoring is fine |
| ☐ | **R613** | No power mixing: sensors/encoders powered **solely** by the device they are connected to; a port's power feeds **only** devices plugged into that exact port (no bussing ports together); 6 V from servo power modules/injectors powers **servos only**; the +5 V Aux port powers devices not otherwise connected to another power-regulating device except via USB |
| ☐ | — | **[PRIOR, gap G5]** Battery securely mounted. Not in the BIOBUZZ text any more, but R201 (unsecured components) still bites, and a loose 12 V pack is the worst thing in your robot |

---

## G. Control system, wireless and vision

| ☐ | Rule | Check |
|---|---|---|
| ☐ | **R701** | Exactly **one** programmable Robot Controller: REV Control Hub **REV-31-1595**, or an Android smartphone plus a REV Expansion Hub **REV-31-1153**. At most **one additional** Expansion Hub — **two hubs total** |
| ☐ | **R702** | No modified coprocessor software. Manufacturer binary firmware updates are fine. Only programmable vision coprocessors natively supported by the SDK may be reprogrammed — **Table 12-9 lists only the Limelight 3A (LL_3A)** |
| ☐ | **R702** | Confirm nothing on the robot is on the prohibited list: **OpenMV Cam, Luxonis OAK-1, Limelight 3G**. *(Explicitly allowed in the orange boxes: Adafruit BNO055, SparkFun OTOS, Digital Chicken Labs OctoQuad FTC Edition, optical-flow sensors, DFRobot HuskyLens, Charmed Labs Pixy2.)* |
| ☐ | **R703** | *Smartphone RC only — skip if you run a Control Hub.* The phone is connected **via its own integrated USB port** to a **REV Expansion Hub**, through any combination of USB cables (OTG included) and/or USB hubs (powered or unpowered, OTG integrated or not). Nothing else may sit between the phone and the Expansion Hub |
| ☐ | **R704.A** | **No other wireless** to, from or within the robot |
| ☐ | **R704.B** | All communication originates only from the RC or the DS on the RC's Wi-Fi network |
| ☐ | **R704.C** | **All programming laptops and other devices disconnected during MATCH play.** Make this a drive-team habit now, not an event surprise |
| ☐ | **R704.D** | ⚠ **FTC Dashboard and FTControl Panels are named as PROHIBITED**, along with any other third-party logging/streaming service. **No continuous video stream.** Only the FTC Driver Station Application may carry control, debugging and telemetry data. Verify in code that every such path is gated off in competition mode |
| ☐ | **R704.E** | You can move to an assigned Wi-Fi band/channel if event staff ask |
| ☐ | **R705** | Devices named `<team#>-RC` and `<team#>-DS`. Spares may add a letter (`12345-A-DS`) |
| ☐ | **R706** | No tampering with the DS device, RC device, switches, power regulation devices, fuses or batteries beyond the allowed list (standard connection points, mounting fasteners/adhesives, thermal interface material, non-obscuring labels, manual-specified jumper positions, manufacturer firmware, cut/stripped/connectorized integral motor and battery wires, like-for-like repairs, insulation of exposed conductors, debris tape, power-switch bracket changes) |
| ☐ | **R707** | USB connects only to: a webcam/optical vision sensor per R708, a USB hub or switch, or a REV Expansion Hub. **No USB LEDs, no USB storage, no USB microcontrollers** |
| ☐ | **R708** | Every USB vision device is **single image sensor** and natively supported by the RC app. **Stereo cameras are prohibited.** UVC webcams may use only the UVC stream |
| ☐ | **R709** | Any self-contained recording device (GoPro or similar) is for non-functional post-match viewing only, with **wireless OFF** — be ready to demonstrate |
| ☐ | **R710** | Lasers only as part of a sensor, rated IEC/EN 60825-1 **Class I** or IEC/EN 62471 **Exempt**, and **non-visible spectrum**. Visible-red line lasers are illegal |
| ☐ | **R711.A** | Control Hub Wi-Fi password **changed from the default** |
| ☐ | **R711.B** | Any smartphone is in **Airplane Mode** |
| ☐ | **R711.C** | Wi-Fi enabled and **Bluetooth disabled** on both RC and DS |
| ☐ | **R711.D** | On the Driver Station Android device, **all remembered Wi-Fi Direct groups and Wi-Fi connections removed** except the RC connection |
| ☐ | — | Run the **Self Inspect** screen on both RC and DS. Zero warnings |
| ☐ | — | Record the Control Hub OS, hub firmware, RC/DS app versions and Servo Hub firmware here: <…>. *(R701's orange box points at a Firmware Update Page listed as "Coming Soon" in V0 — check it at Kickoff.)* |

---

## H. Pneumatics and airflow

| ☐ | Rule | Check |
|---|---|---|
| ☐ | **R801.A** | Any closed-air component is **COTS and sealed / pre-charged by its manufacturer** — gas springs and dampers are explicitly named as fine |
| ☐ | **R801.B** | No stored-pressure component actuated by a solenoid or able to change stable state |
| ☐ | **R801.C** | **Nothing on the robot generates pressure or vacuum** |
| ☐ | **R801.D** | No user-adjustable gas storage vessel, except air-filled (pneumatic) COTS wheels |
| ☐ | **R801.E** | No high-speed airflow device, except cooling fans integrated into COTS computing devices. *(Flywheels and rollers that manipulate scoring elements are explicitly not "airflow devices".)* |

---

## I. Operator console

| ☐ | Rule | Check | Number |
|---|---|---|---|
| ☐ | **R901** | Exactly **one** Android Driver Station device connected and powered on: REV Driver Hub **REV-31-1596**, or any Android device, plus USB cabling/hubs for gamepads. A spare is fine if only one is connected and powered at a time | 1 |
| ☐ | **R902** | Touch screen accessible, clearly visible during inspection and matches, and usable without extra aids (no mouse) | |
| ☐ | **R903** | Console volume, **including all power sources such as power banks**, fits **3 ft W × 1 ft 6 in D × 2 ft H (91.4 × 45.7 × 61.0 cm)**. Measure with the power bank inside the box. Items held or worn by drivers are excluded | 91.4 × 45.7 × 61.0 cm |
| ☐ | **R903** | Over **20 lb (~9 kg)** invites extra scrutiny (no hard limit). It is not a robot cart | |
| ☐ | **R904** | **No wireless to, from or within the console** other than the RC-app ↔ DS-app link. No wireless NICs, no Bluetooth devices, no wireless gamepads | |
| ☐ | **R202** | The console is also subject to R202 — no distracting audio, no high-intensity lights, no AprilTag-mimicking imagery | |
| ☐ | **[GAP G1]** | ⚠ **BIOBUZZ V0 has no gamepad allowlist and no 2-gamepad cap** — DECODE had both (R903 + Table 12-12). Assume the DECODE constraints still apply until Kickoff confirms, and **do not buy an off-list controller** | |

---

## J. Event eligibility and paperwork (Section 3, I-rules)

*Not about the robot, but you cannot compete without them.*

| ☐ | Rule | Check |
|---|---|---|
| ☐ | **I101** | Team is registered with FIRST and **"competition ready"**. North America: annual registration complete, fee paid, **2 adults assigned as Lead Coach 1 / Lead Coach 2 with Youth Protection Program screening passed**, any additional regional YPP screening done, and **all youth team members registered on the FIRST dashboard**. Outside North America: registration plus your Program Delivery Partner's requirements |
| ☐ | **I102** | **Check in at Pit Administration no later than 45 minutes before Qualification Matches start.** An **adult** must do the check-in, and **at least one student must be present at the venue** before check-in can complete |
| ☐ | **I102.A–D** | Bring: current team roster from the FIRST dashboard, any regional consent/registration forms, the robot built to Section 12, and the printed portfolio (optional but required for most judged awards, see A201/A202) |
| ☐ | **I103** | **At least 1, preferably 2, responsible adults present at all times** during the event. Recommended to be on the team roster |
| ☐ | **I301** | Bring the **complete robot and operator console with ALL components, including decorative parts**, that will be used in matches. Be ready to **demonstrate every configuration** the robot will use |
| ☐ | **I302** | The electronics count (motors, servos, Android devices, etc.) across **all mechanisms and the base robot, whether used simultaneously or not**, is within Section 12 limits. See section E above |
| ☐ | **I303** | The team knows what triggers **re-inspection**. Not required for: fasteners, labels/markings, sign relocation, **code revisions**, replacing a component or mechanism with an identical one, or reconfiguring with an already-inspected subset. Required for anything that could change size, legality or safety, or when the Head Referee or FTA asks |
| ☐ | **I304** | Nobody on the team is planning to use re-inspection to get around another rule |
| ☐ | **§3.3** | You may play **scheduled** practice matches before passing inspection, but **not** unscheduled or "filler line" practice matches |
| ☐ | **A202** | Portfolio submission method and deadline confirmed with the Event Director. Default if not told otherwise: **1 printed copy handed in at the Initial Interview**. Bring a spare copy for the pit |

---

## K. Fixes required before this robot competes

| # | What | Rule | Owner | By when | Done |
|---|---|---|---|---|---|
| 1 | | | <First L.> | | ☐ |
| 2 | | | | | ☐ |
| 3 | | | | | ☐ |

**Signed off by:** <First L.> and <First L.> on <YYYY-MM-DD>

---

## Appendix — the 14 failure modes, ranked

From the DECODE Inspection Checklist and Quick Reference plus Q&A volume; the
rule numbers are the BIOBUZZ ones. Full detail:
`reference/CONSTRUCTION-RULES-R.md` §7.

| # | Failure | Rule | Pre-empt it by |
|---|---|---|---|
| 1 | Over the expansion envelope at full **mechanical** extension | R105 | Relocatable hard stops; measure two mechanisms extended together |
| 2 | Wire gauge / colour wrong, or no evidence of gauge | R609, R610 | Buy labelled wire; keep a scrap sample of each gauge in the pit |
| 3 | Illegal servo (stall current or output power over cap) | R502 | Print datasheets; check against the Quick Reference list |
| 4 | Actuator count over budget across all configurations | R503, I302 | Count every motor and servo **in the pit**, not on the robot |
| 5 | Tile-damaging traction devices | R201 | Check the wheel and tread part numbers before you buy |
| 6 | Illegal servo signal/power adapter | R505, R612 | No Travel Tuner, no unapproved distribution boards |
| 7 | Sign non-compliant — too small, not solid, unsupported, only one, or on parallel faces | R401–R403 | Print the template at 100%; rigid backer bolted to frame; 90° apart |
| 8 | Frame used as a current path / uninsulated grounding | R605 | Measure > 120 Ω from switch input to frame |
| 9 | Custom circuit over 5 V or altering a power path | R607, R612 | No buck/boost anywhere in battery→hub→actuator |
| 10 | Diagnostic LEDs or RC screen not visible | R606 | Removable panel, or keep the hub visible in match config |
| 11 | Modified motor or servo | R504 | Nothing removed, nothing added, no 4th wire |
| 12 | Self-inspect warnings / device naming | R705, R711 | Rename, change the hub password, Bluetooth off, forget stale Wi-Fi groups |
| 13 | Operator console oversize or wireless enabled | R903, R904 | Measure with the power bank inside; kill Bluetooth on everything |
| 14 | Sharp edges, entanglement, loose ballast | R201, R202 | Deburr everything; secure or delete ballast |

---

## Kickoff-day update task — 12 September 2026

When the game and the supporting documents post, **update this file** before you
build anything:

1. Fill in every `[KICKOFF]` blank in section A from **R105**.
2. Download the **2026-27 Inspection Checklist** and **Inspection Quick
   Reference**; reconcile every line here against them and note the differences.
3. Fill in the **R502 servo stall-current** number (blank in the V0 PDF).
4. Check whether a **gamepad allowlist / count cap** reappeared (gap G1) and
   whether an **Android device allowlist** reappeared (gap G2).
5. Record firmware target versions from the **Firmware Update Page** (R701).
6. Add the game-specific **G-rules** that pair with R201 (the V0 text has a
   literal `GXXX` placeholder).
7. Re-run the whole checklist against the Kickoff manual and re-date it.

`tools/ai/PROMPTS-strategy.md` S1 and S7, and `tools/ai/PROMPTS-design.md` D12,
are the prompts for doing steps 1–7 with Claude. **Every finding still needs a
human with a ruler.**
