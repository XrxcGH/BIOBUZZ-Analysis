# LAUNCHERS AND FEEDING — mechanism catalog

### Flywheel shooters, catapults, elastic launchers, the no-launch alternatives, and the feed systems that actually decide whether any of them work

**Workspace:** `reference/mechanisms/LAUNCHERS-AND-FEEDING.md`
**Written:** 2026-08-22 · **Season:** FIRST Tech Challenge 2026-27 **BIOBUZZ** presented by RTX
**Legality source of truth:** BIOBUZZ Competition Manual **V0**, Section 12 ROBOT Construction Rules (R) — **final for this season**
**Calibration target:** ~15 students, **two registered teams (A and B), two robots**, modest budget, 3D printers + hand tools, **no CNC mill**, limited mentor hours

---

> ## ⚠ READ THIS BEFORE READING ANYTHING ELSE
>
> **It is not known whether BIOBUZZ has a launchable SCORING ELEMENT.** Section 8 (Game Overview),
> Section 9 (ARENA), Section 10 (Game Details) and Section 11 (Game Rules G) are all **V0 PLACEHOLDERS**.
> The game is published at **Kickoff, 12 September 2026**.
>
> **This file is a capability library, not a recommendation.** It exists so that if — and only if — the
> kickoff point table rewards launching, this program can produce an accurate two-robot bill of materials in
> hours instead of weeks. If BIOBUZZ turns out to have no launchable element, or pays the same for a
> low-effort deposit as for a shot, **the correct number of launchers to build is zero**, and this file's
> §8 (Ramps and Deposits) and §14 (Blunt Assessment) are the sections that matter.
>
> **A second, sharper warning.** I searched the **entire V0 manual text** for `launch`, `projectile`,
> `eject`, `shoot` and `catapult`. The only hit is the word "ejection" in a behavioral context.
> **There is currently no rule anywhere in V0 that restricts launching SCORING ELEMENTS.** That is *not*
> permission — it is a **V0-GAP**. Historically, launch restrictions (elements leaving the FIELD, launch
> height/trajectory limits, "do not launch at other ROBOTS") live in the **Game Rules (G)** section, and
> **Section 11 G-rules is a placeholder**. Assume launch constraints are coming and design margin for
> them. See §1.3.

---

## Revision note — re-verification pass, 2026-08-22

This file was re-checked against live vendor pages after its first draft. **Nothing about the legality
analysis changed** — every R-rule citation was re-grepped against the V0 Section 12 text and all of them
hold. Five substantive corrections were made to the **parts and cost** content:

| # | Correction | Where |
|---|---|---|
| 1 | 🔴 **The `3628` steel flywheels have NO bore.** They bolt to a square hub-mount pattern (**82 mm → 32 mm pattern**, **60 mm → 16 mm pattern**), so a **matching hub is a mandatory extra purchase**, and the `-0014-` field does **not** mean a 14 mm pattern | §3.3 |
| 2 | **Servo `2000-0025-0003` = $36.99**, not the ≈ $25 previously assumed. The old estimate came from `REV-41-1097`, which is **discontinued**. Every servo-bearing subtotal was rebuilt | §5.5, §6.5, §8.5, §9.3, §10.3, §16 |
| 3 | **Servo Power Injector `3125-0001-0001` = $69.99**, more than **double** the ≈ $30 previously assumed | §9.3, §16.1 |
| 4 | 🔴 **RPM ceiling conflict:** REV's DUO compliant wheel is rated **5,500 RPM**, below the **6000 RPM** free speed of the recommended 1:1 flywheel motors. A software velocity cap is now required, not optional | §3.3, §3.6 |
| 5 | Register items **11, 12 and 13 are now CLOSED**; the first pass's 404'd flywheel URL was a wrong guessed slug and the correct pages resolved | §17, §18.2 |

Prices re-confirmed **unchanged**: `5203-2402-0001` $54.99 · `5204-8002-0003` $56.99 · `3628-0032-0082`
$15.99 · `3628-0014-0060` $12.99 · `am-3462` $6.20 · `am-3945` $8.40 · `am-4537` $8.70 · `am-3480`
$11.00 · `REV-41-2034/2035-PK4` $19.50/4-pk · `REV-41-1291` $22.00 · `3102-0001-0001` $12.99.
**All still VERIFY-BEFORE-ORDER.**

---

## Contents

| § | Section |
|---|---|
| 0 | How to read this file |
| 1 | The legality envelope for launchers — what Section 12 already settles |
| 2 | Launcher physics you must be able to compute before you buy anything |
| 3 | **L1 — Single-flywheel shooter with a hood** |
| 4 | **L2 — Dual-flywheel (counter-rotating) shooter** |
| 5 | **L3 — Linear puncher / spring catapult** |
| 6 | **L4 — Elastic / slingshot launcher** |
| 7 | **L5 — Pneumatic launcher — ILLEGAL IN BIOBUZZ** |
| 8 | **L6 — Ramps, chutes and deposits — the no-launch alternative** |
| 9 | **FEED SYSTEMS — F1 hopper + agitator, F2 single-file indexer, F3 kicker/gate** |
| 10 | **AIMING — A1 fixed, A2 adjustable hood, A3 turret** |
| 11 | Fabrication guide — materials, printers, hand tools, student-hours |
| 12 | The tuning burden, quantified — what a launcher demands of your programmer |
| 13 | The duplicability problem — two flywheels that behave identically |
| 14 | Blunt assessment for a ~15-student two-robot program |
| 15 | Worked R503 actuator budgets for launcher robots |
| 16 | Cost rollups |
| 17 | Verification log — every page loaded this session |
| 18 | Open questions / NEEDS-SKU-CHECK register |

---

## 0. How to read this file

### 0.1 Claim labels (matched to `LEGAL-PARTS-CONSTRAINTS.md` §0.1)

| Label | Meaning |
|---|---|
| **CONFIRMED-BIOBUZZ** | Read directly from the BIOBUZZ V0 Section 12 text this session. Rule ID cited and re-grepped. |
| **HISTORICAL** | Prior season (DECODE 25-26, ITD 24-25, and older). Calibration only, **never binding**. |
| **JUDGMENT** | My engineering recommendation or calculation for this specific team. Not a rule. |
| **V0-DEFERRED** | The manual explicitly says the number arrives at Kickoff. |
| **V0-GAP** | Silently absent from V0 where a prior season had a rule. Assume it may return. |

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

| Tag | Meaning |
|---|---|
| **VERIFIED** | I loaded the vendor page with WebFetch **on 2026-08-22** and read the SKU and price off it. |
| **FAMILY-ONLY** | I verified the vendor *category* page but not this exact SKU/price. The family is real; treat the SKU as **NEEDS-SKU-CHECK**. |
| **MANUAL-SOURCED** | SKU comes from a BIOBUZZ V0 rule table (highest authority for *legality*), but no vendor page loaded → **no price given**. |
| **CROSS-REF** | Verified in Phase A (`VENDOR-ECOSYSTEMS.md` / `LEGAL-PARTS-CONSTRAINTS.md`), not re-fetched here. |
| **UNVERIFIED** | Neither. **Do not order from this row.** |

**Every price in this file is "as of August 2026" and is marked VERIFY-BEFORE-ORDER.**
Prices, stock and vendor catalogs move. A part being legal does not mean it is in stock.

### 0.3 Scoring polarity in the variant tables — read this or you will misread every table

| Column | 1 means | 5 means |
|---|---|---|
| **Complexity** | trivial to build | very hard to build |
| **Cost** | cheap | expensive |
| **Tuning burden** | works when bolted on | eats your season |
| **Reliability** | fails often | fails rarely |
| **Duplicability** | agony to build twice | copies to robot B cleanly |

**Complexity, Cost and Tuning burden are BAD-HIGH. Reliability and Duplicability are GOOD-HIGH.**

### 0.4 Where this file sits

- `reference/LEGAL-PARTS-CONSTRAINTS.md` — the purchasing legality envelope. **Read first.** This file
  cites it rather than repeating it.
- `reference/VENDOR-ECOSYSTEMS.md` — vendor profiles, the interoperability map, the pre-kickoff standing
  order. Shafting, bearings, hubs, fasteners and belts are specified there and **cross-referenced, not
  duplicated,** here.
- `reference/ROBOT-ARCHETYPE-LIBRARY.md` §3.3 — the launcher/shooter **archetype** at strategy altitude
  (scored 2.63; duplicability 3; programming load 4). This file is the **mechanism and BOM** altitude beneath it.
- `reference/ACHIEVABILITY-FACTORS.md` — the factor model, including duplicability.

---

## 1. The legality envelope for launchers — what Section 12 already settles

Section 12 is **FINAL for BIOBUZZ**. Everything below is knowable today, before kickoff.

### 1.1 The single most important sentence for this entire file

**CONFIRMED-BIOBUZZ — R801 blue box (Section 12.8):**

> *"High-speed flywheels or rollers used for manipulating SCORING ELEMENTS would not on their own be
> considered a high-speed airflow device."*

**Flywheel launchers and roller intakes are explicitly, deliberately carved out as legal.** The rule
writers anticipated exactly this mechanism and protected it from the airflow ban in the same breath as
banning blowers. You do not need a Q&A on this point.

### 1.2 The rules that shape every launcher on this page

| Rule | What it says | Consequence for a launcher |
|---|---|---|
| **R801.A–E** * | Only **sealed COTS closed-air systems pre-charged by the manufacturer** (gas shocks). No pressure or vacuum generation, no compressors, no blowers. | **No pneumatic launcher exists in BIOBUZZ.** See §7. Gas springs remain legal as a stored-energy element. |
| **R506** * | *"The use of relays, electromagnets, and electrical solenoid actuators is prohibited."* | 🔴 **Your catapult release cannot be a solenoid.** Releases must be servo-driven sears, motor-driven cams, or slipping/ratcheting gears. This rule kills the obvious catapult trigger. |
| **R503** * | **8 motors + 8 servos total**, summed across **all MECHANISMS in all configurations**. | A launcher robot spends 1–2 motors on the flywheel, 1 on intake, 1 on transfer, plus servos on hood/kicker — **on top of** a drivetrain. See §15. |
| **R501** * / Table 12-1 | Closed motor allowlist by manufacturer and part number. | Your flywheel motor **must** come from Table 12-1. There is **no legal brushless flywheel motor** in FTC. |
| **R502** * / Table 12-2 | Servo spec test: **≤ 8 W mechanical output @ 6V** and a stall-current cap (**the cap is blank in the V0 PDF — V0-ERRATA**; DECODE's value was 4 A). | Hood servos and kicker servos must pass the spec test. Big cheap "45 kg" servos generally **fail**. |
| **R303** * | COTS COMPONENTS/MECHANISMS must not exceed a **single degree of freedom**. Exceptions include **(H) ratcheting devices**, (I) holonomic wheels, (J) dead-wheel odometry, (K) misaligned-motion couplers, (L) variable-angle linkages. | A **bought** two-axis turret assembly is illegal. A **fabricated** one is fine. Ratchets are explicitly available for catapult winches. |
| **R301** * | **COTS MAJOR MECHANISMS purposefully designed to complete a game task are prohibited** (exceptions: COTS drive chassis, official StarterBots). | You may not buy a "shooter kit," and no vendor sells a legal one. **The launcher is, by rule, a fabricated mechanism.** |
| **R302** * | Legal COTS parts and raw materials may be drilled, cut, painted. Raw materials explicitly include **sheet stock, extruded shapes, metals, plastic, rubber, wood, magnets**. | Your polycarbonate hood, printed side plates and hopper walls are all explicitly sanctioned. |
| **R102** * | **STARTING CONFIGURATION ≤ 18 in. cube** (45.70 cm per side), fully self-contained and **stationary**. | A tall hood + hopper stack fights the 18-inch cube hard. See §1.4. |
| **R105** | ROBOTS stay one assembly; expansion beyond STARTING CONFIGURATION is limited — *"Sizing Constraints and more details will be released at Kickoff."* | **V0-DEFERRED.** Do not finalize a deploying-hood or rising-hopper geometry until kickoff. |
| **R201** * | No damaging the ARENA, no making a mess. *"Gouging, tearing off pieces, or routinely and repeatedly marking SCORING ELEMENTS are violations of this rule…"* | 🔴 **A flywheel is an abrasion machine.** A hard wheel at high surface speed slipping on an element will mark it. Inspectable and penalizable. See §3.6. |
| **R202** * | Safety and fair play. **(F)** *"high intensity light sources used on the ROBOT should only be illuminated for a brief time while targeting"*; **(I)** entanglement risk; **(C)** nothing mimicking 36h11 AprilTags. | Constrains vision-aiming illumination (§10.4) and open-flywheel guarding. |
| **R203** * | ROBOTS must allow removal of **SCORING ELEMENTS from the ROBOT** and the ROBOT from FIELD elements **while powered off**. | 🔴 **This rule constrains hopper design directly.** A magazine that traps elements behind a powered kicker with no manual egress is an **inspection failure**. See §9.1. |
| **R204** * | No downforce by grabbing the floor or by generated airflow suction. | Reinforces the vacuum ban; no suction-assisted intake. |
| **R702** * / Table 12-9 | Programmable vision coprocessors natively supported by the FTC SDK may be reprogrammed. **Table 12-9 lists exactly one device: Limelight Vision Limelight 3A, part number `LL_3A`.** | If you want a smart camera for range-finding, **the Limelight 3A is the only device on the table**. See §10.4. |
| **R704** * | **(C)** *"Ensure all programming laptops and other devices … are disconnected from the ROBOT CONTROLLER Wi-Fi network during MATCH play."* | 🔴 **You cannot live-tune or watch flywheel telemetry during a match.** All shot calibration happens in the pit or in practice. This is the rule that makes launcher tuning expensive. See §12.4. |

### 1.3 The V0-GAP you must plan around

**V0-GAP — there is no launch-restriction rule in V0 today.** Grepping the full V0 text for
`launch|projectile|eject|shoot|catapult` returns only a behavioral use of "ejection."

Prior seasons placed launch constraints in the **G-rules** (Section 11), which is a **placeholder**. The
constraints that have historically appeared, and that you should carry as design margin:

| Likely constraint (HISTORICAL, not binding) | Design margin to carry now |
|---|---|
| SCORING ELEMENTS must not leave the FIELD | Do not design for maximum range. Design for **the shortest range that scores**, with a hard velocity ceiling in software. |
| Restrictions on launching at or into other ROBOTS | Keep the muzzle elevation **upward**; avoid flat, fast trajectories at robot height. |
| Height or trajectory limits above the FIELD | Keep the arc as low as the target geometry allows. |
| Element damage from repeated high-energy shots | **Already binding today** via R201. |

**JUDGMENT:** build the launcher with a **software velocity-cap constant** from day one, so that a kickoff
G-rule or a Thursday Team Update can be complied with by changing one number rather than rebuilding a hood.

### 1.4 The 18-inch cube is the real geometric enemy

**CONFIRMED-BIOBUZZ — R102**: 18 × 18 × 18 in. (45.70 cm), fully self-contained, **stationary** at MATCH start.

A launcher stack is naturally tall: hopper on top → indexer → flywheel → hood exit. Add a drivetrain
underneath and the 18-inch height disappears fast. The blunt arithmetic:

| Layer | Realistic vertical budget |
|---|---|
| Drivetrain, wheels, chassis rails | 4–5 in. |
| Electronics shelf (Control Hub, battery) | 2–3 in. |
| Flywheel + hood assembly | 4–6 in. |
| Hopper volume above the indexer | **whatever is left — often only 3–5 in.** |
| **Total** | **must be ≤ 18 in.** |

**Two escapes, both CONFIRMED-BIOBUZZ:**

1. **R102 explicitly permits pre-loads to stick out:** *"Any pre-loaded SCORING ELEMENTS may extend
   outside the starting size constraint."* A pre-loaded element sitting proud of the hopper is legal at
   MATCH start. This is a real and frequently missed allowance.
2. **R105 permits expansion after the MATCH starts** — but **the amount is V0-DEFERRED to Kickoff.** A
   hopper that unfolds upward in the first second is a legitimate pattern; **do not commit to it until
   kickoff publishes the expansion envelope.**

---

## 2. Launcher physics you must be able to compute before you buy anything

**JUDGMENT — this entire section is engineering calculation, not rules.** But it is the difference between
buying the right motor once and buying the wrong motor twice, which for a two-robot program means buying
the wrong motor four times.

### 2.1 Surface speed is the number you actually control

Wheel surface speed: **v_s = π · D · (RPM / 60)**, with D in metres.

Using the **VERIFIED** goBILDA Yellow Jacket ratios and common wheel diameters:

| Wheel Ø | @ 1150 RPM | @ 1620 RPM | @ 6000 RPM (1:1) |
|---|---|---|---|
| 48 mm | 2.9 m/s | 4.1 m/s | 15.1 m/s |
| 72 mm | 4.3 m/s | 6.1 m/s | 22.6 m/s |
| 96 mm | 5.8 m/s | 8.1 m/s | **30.2 m/s** |
| 4 in (101.6 mm) | 6.1 m/s | 8.6 m/s | 31.9 m/s |

### 2.2 How much of that reaches the element

| Configuration | Approximate element exit speed | Spin imparted |
|---|---|---|
| **Single flywheel against a fixed hood** | **≈ v_s / 2** | Heavy **backspin** (the hood scrubs one side) |
| **Dual counter-rotating flywheels, equal speed** | **≈ v_s** | Near zero |
| **Dual flywheels, deliberately mismatched** | between the two | Tunable top- or backspin |

**JUDGMENT — the design consequence.** A single flywheel throws away roughly half its surface speed and
converts it into backspin. That is not pure waste: backspin stabilizes the trajectory and, on many target
geometries, makes a shot that hits the back of a goal drop in rather than bounce out. But it means a
**single flywheel needs roughly double the surface speed of a dual flywheel** for the same range.

### 2.3 Ballistics sanity check

Flat-ground range at 45°: **R = v² / g**.

| Desired range | Required exit speed | Single-flywheel v_s | Dual-flywheel v_s |
|---|---|---|---|
| 2 m | 4.4 m/s | 8.9 m/s | 4.4 m/s |
| 3 m | 5.4 m/s | 10.8 m/s | 5.4 m/s |
| 4 m | 6.3 m/s | 12.5 m/s | 6.3 m/s |

Shooting **upward into an elevated target** raises all of these — budget **+30–50 %** over the flat-ground
figure. **JUDGMENT: a realistic FTC shot needs 5–9 m/s of element exit speed**, which means:

- **Dual flywheel:** a 96 mm wheel at **1150–1620 RPM** is in range. Both are stock Yellow Jacket ratios.
- **Single flywheel:** you need **10–18 m/s** surface speed → a 96 mm wheel at **2000–3600 RPM**, which is
  **not a stock Yellow Jacket ratio.** You either run the **6000 RPM 1:1** motor at 35–60 % throttle, gear
  up from 1620 RPM, or use a smaller wheel at 6000 RPM.

🔴 **This is the most common launcher purchasing mistake:** buying a 1150 RPM motor for a single-flywheel
shooter and discovering in week 4 that it physically cannot reach the target.

### 2.4 Flywheel inertia and recovery time — the metric nobody budgets for

Every shot **steals energy from the flywheel.** Energy delivered to a 70 g element at 7 m/s:

**E_shot = ½ · m · v² = ½ · 0.070 · 49 ≈ 1.7 J**

*(70 g is an **illustrative placeholder — the BIOBUZZ element mass is unknown until Kickoff.** Recompute
this table on kickoff day; it is the first calculation you should run.)*

goBILDA publishes moment of inertia on its steel flywheels — **VERIFIED this session:**

| Flywheel | J | Stored energy @ 3000 RPM (314 rad/s) | Speed drop from one 1.7 J shot |
|---|---|---|---|
| `3628-0014-0060` (60 mm, 115 g) | 551 g·cm² = 5.51 × 10⁻⁵ kg·m² | ½·J·ω² ≈ **2.7 J** | ⚠ **~37 % energy → ~21 % RPM drop** |
| `3628-0032-0082` (82 mm, 152 g) | 1651 g·cm² = 1.651 × 10⁻⁴ kg·m² | ≈ **8.1 J** | **~21 % energy → ~11 % RPM drop** |
| Either, plus motor rotor and compliant wheel inertia | higher | higher | lower drop |

**The lesson, stated plainly:** a light flywheel sags hard on every shot, and **shot 2 goes somewhere
different from shot 1** unless the software waits for recovery. Adding rotational mass costs almost nothing
(**$12.99–$15.99, VERIFIED**) and is the cheapest reliability upgrade on the entire robot.

**Recovery time — JUDGMENT:** restoring ~1.7 J with perhaps 10–20 W of usable motor power at speed gives a
**theoretical floor near 0.1 s**, but settling back inside a ±1 % velocity band realistically takes
**0.3–0.8 s**. That caps a well-tuned flywheel at roughly **1.5–3 shots per second**, and an *untuned* one
at **one shot every 3–4 seconds**, because the programmer ends up padding the wait to be safe.

> **Cross-ref:** `ROBOT-ARCHETYPE-LIBRARY.md` §3.3 records exactly this failure mode — *"teams build a
> beautiful flywheel and a bad feeder, then discover mid-season that they can shoot one element every four
> seconds."*

### 2.5 Compliance and compression — the grip budget

The element must be **squeezed** to transfer momentum. Too little compression → slip, inconsistent shots,
and **R201 marking**. Too much → the motor bogs on entry and the element deforms.

| Parameter | Practical starting point (JUDGMENT) | Notes |
|---|---|---|
| **Compression** | **3–8 mm** of element diameter | The most sensitive geometric variable on the mechanism. Make it **adjustable** — slotted holes, never round ones. |
| **Wheel durometer** | **30A–50A** | Softer grips better and marks less; harder survives more and holds RPM. AndyMark ships **35A green / 40A orange / 50A blue / 60A black** (VERIFIED); goBILDA Boot-Wheels are **30A** (VERIFIED); REV DUO compliant wheels are **30A soft / 40A medium** (VERIFIED). |
| **Contact arc** | 30–60° of wrap | More wrap = more transfer, more scrub, more marking risk. |
| **Hood gap** | element Ø + 1–3 mm | Too tight jams; too loose loses backspin. |

**JUDGMENT — buy three durometers, not one.** At $6.20–$11.00 per AndyMark compliant wheel, buying 35A,
40A and 50A to test costs under $35 and saves a fortnight. Durometer is not a spec you can compute; it is
a spec you discover empirically **with the actual element, which you do not have until kickoff.**

---

## 3. L1 — Single-flywheel shooter with a hood

### 3.1 What it is and when a design needs it

One powered compliant wheel spinning against a fixed curved surface (the **hood**). The element enters the
gap, is pinched between wheel and hood, and is flung out with heavy backspin. It is the **default FTC
shooter** and the cheapest way to put a scoring element somewhere the robot cannot drive.

**A design needs it when:**

- The kickoff point table pays for delivering elements to a target the robot **cannot reach or climb to**.
- The target is **far enough that driving there costs more time than shooting**.
- The element is **compressible and reasonably uniform** (foam ball, disc, ring). Rigid or irregular
  elements shoot badly and abrade.

**A design does NOT need it when:** the target is reachable by driving; the game pays per element and
cycle rate dominates (a launcher is then just a cycler with worse odds); or scoring is a low-forgiveness
target where a 60 % hit rate is worse than a 100 % deposit. See §8 and §14.

### 3.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Single compliant wheel + printed hood, fixed angle** | **2** | **2** | **4** | 3 | **4** | The rookie-friendly baseline. One motor, one wheel, one printed hood. |
| Single compliant wheel + **added steel flywheel** on the same shaft | 2 | 2 | **3** | **4** | **4** | 🟢 **Best value on this page.** ~$15 buys a large drop in shot-to-shot variance (§2.4). |
| Single wheel, **geared up** from 1620 RPM via belt/pulley | 3 | 3 | 4 | 3 | 3 | Adds a belt stage to reach single-flywheel surface speed. More parts to duplicate. |
| Single wheel, **6000 RPM 1:1 motor, throttled** | 2 | 2 | **4** | 3 | **4** | Simplest way to reach speed. Runs the motor well below its torque peak; velocity control does the work. |
| **Stacked twin wheels on one shaft** (one motor, two contact points) | 3 | 3 | 4 | **4** | 3 | Wider, more even grip on a large element. Still one motor — **does not** cost a second R503 slot. |

**JUDGMENT — recommended starting point for this program:** *single compliant wheel + steel flywheel on a
6000 RPM 1:1 motor, fixed hood.* It is one motor, one R503 slot, two cheap VERIFIED parts, and it has the
best duplicability score available in a launcher.

### 3.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Flywheel motor, high free speed** | goBILDA (general supplier) | **Yellow Jacket 5203 Series, 6000 RPM 1:1 — `5203-2402-0001`** (8 mm REX, 1.47 kg·cm) | 1 | **2** | **$54.99 ea = $110** | Buy | **VERIFIED** — [category](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | 🔴 The **only stock ratio** that reaches single-flywheel surface speed without a gear-up stage (§2.3). Built-in encoder. VERIFY-BEFORE-ORDER. |
| Flywheel motor, alternative | goBILDA | Yellow Jacket **1620 RPM — `5203-2402-0003`** (8 mm REX) / `5202-2402-0003` (6 mm D) / `5204-8002-0003` ($56.99) | 1 | 2 | **$54.99 ea** | Buy | **VERIFIED** | 5.4 kg·cm. Needs a **gear-up stage** for a single flywheel; fine as-is for **dual** flywheel (§4). |
| Flywheel motor, budget | REV Robotics (general supplier) | **HD Hex Motor, bare — `REV-41-1291`** | 1 | 2 | **$22.00 ea = $44** | Buy | **CROSS-REF** (VERIFIED in `LEGAL-PARTS-CONSTRAINTS.md` §2.5) | Cheapest legal motor. **R504 permits use with or without the supplied gearbox** — bare HD Hex is a natural direct-drive flywheel motor. Encoder is separate. |
| **Compliant contact wheel** | AndyMark (**official FIRST supplier**) | **Compliant Wheel 3 in., 5 mm hex — `am-4537`** (35A / 40A / 60A) | 1–2 | **2–4** | **$8.70 ea ≈ $17–$35** | Buy | **VERIFIED** — [product page](https://andymark.com/products/compliant-wheels) | 5 mm hex suits REV/goBILDA hex shafting. **Buy multiple durometers** (§2.5). |
| Compliant contact wheel, larger | AndyMark | **Compliant Wheel 4 in. — `am-3480`** (1/2 in hex) / `am-3562` (3/8 in hex) / `am-4538` (5 mm hex) / `am-3563` (nub bore) | 1–2 | 2–4 | **$11.00 ea** | Buy | **VERIFIED** | All four bores $11.00. 35A/40A/50A/60A available (5 mm hex is 40A/50A/60A only). |
| Compliant contact wheel, small | AndyMark | 2 in. `am-3462` / `am-3571` / `am-3572` — **$6.20**; 2.25 in. `am-3949` / `am-3950` / `am-4536` — **$7.20**; 3 in. `am-3945` / `am-3946` — **$8.40** | as needed | ×2 | **$6.20–$8.70** | Buy | **VERIFIED** | The cheapest durometer-test kit in FTC. |
| Compliant wheel, goBILDA ecosystem | goBILDA | **3615 Series Boot-Wheel, 30A, 8 mm REX** — `3615-4008-0096` (96 mm) **$8.99** · `3615-4008-0072` (72 mm) **$6.99** · `3615-4008-0048` (48 mm) **$4.99** | 1–2 | **2–4** | **$10–$18** | Buy | **VERIFIED** — [intake wheels](https://www.gobilda.com/intake-wheels/) | 🟢 **Stays inside the goBILDA 8 mm REX standard** — no adapter, no hub. See `VENDOR-ECOSYSTEMS.md` §3.3. |
| Compliant wheel, REV ecosystem | REV Robotics | **DUO Compliant Wheel 2 in., 5 mm hex, 4-pack** — Soft 30A `REV-41-2035-PK4` · Medium 40A `REV-41-2034-PK4` | 1 pk | **1–2 pk** | **$19.50 / 4-pk** | Buy | **VERIFIED** — [DUO compliant wheels](https://www.revrobotics.com/duo-compliant-wheels/) — **In Stock** | 4-pack economics are good for a two-robot program: one pack can serve both robots. 🔴 **RPM CEILING — added 2026-08-22: REV publishes a 5,500 RPM rating for this wheel.** That is **below the 6000 RPM free speed** of both `5203-2402-0001` and `REV-41-1291`. On a 1:1 direct-drive flywheel you must **cap commanded velocity below 5,500 RPM in software** (easy — you are running closed-loop anyway, §12.1) or choose a different contact wheel. Spinning a compliant wheel past its rating risks the moulded hub letting go, which is an **R201** safety problem at flywheel energies. |
| 🟢 **Steel flywheel (inertia mass)** | goBILDA | **`3628-0032-0082`** — 82 mm, 152 g, **1651 g·cm²** | 1 | **2** | **$15.99 ea = $32** | Buy | **VERIFIED** — [flywheels](https://www.gobilda.com/flywheels/) | 🔴 **Buy this.** Cuts shot-to-shot RPM sag roughly in half vs. the 60 mm (§2.4). Published J is the only such spec in the FTC catalog. |
| Steel flywheel, smaller | goBILDA | **`3628-0014-0060`** — 60 mm, 115 g, **551 g·cm²** | 1 | 2 | **$12.99 ea = $26** | Buy | **VERIFIED** | Use when the 82 mm will not fit inside the 18-inch cube. |
| Shafting (8 mm REX) | goBILDA | Stainless REX Shafting 8 mm w/ E-Clip | 1–2 | 2–4 | $3.69–$17.99 ea | Buy | **CROSS-REF** — `VENDOR-ECOSYSTEMS.md` §6.4 | **NEEDS-SKU-CHECK per length.** |
| Bearings / pillow blocks | goBILDA | `1611` Series (8 mm REX ID) · `1602` / `1605` / `1606` pillow blocks | 2–4 | **4–8** | ≈ $25–$50 | Buy | **CROSS-REF** — `VENDOR-ECOSYSTEMS.md` §6.4 | 🔴 **The flywheel shaft must be supported on BOTH sides.** A cantilevered flywheel wobbles and the shot wanders. |
| Hubs (flywheel → shaft) | goBILDA | Clamping / Sonic / Hyper hub, 8 mm REX bore, with a **16 mm or 32 mm square hub-mount face** to match the flywheel | 1–2 | 2–4 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** — [hubs](https://www.gobilda.com/hubs/) | 🔴 **CORRECTED 2026-08-22 — the `3628` flywheels have NO BORE.** They are flat steel plates that bolt to a hub-mount pattern, so a hub is a **mandatory** separate purchase. **VERIFIED:** `3628-0032-0082` (82 mm) = four 4 mm holes with hex counterbores on the goBILDA **32 mm square pattern**, plus eight holes on a **48 mm square pattern** (matches the 96 mm Hogback Traction Wheel). `3628-0014-0060` (60 mm) = four 4 mm holes on the **16 mm square pattern**, plus four on a **32 mm** pattern (matches the 72 mm Hogback). ⚠ **The `-0014-` field does NOT mean a 14 mm pattern.** Order the hub to the *pattern*, not to the part number. |
| Belt/pulley gear-up (only if geared) | goBILDA | 5 mm HTD Starter Pack (8 mm REX bore) **$209.99** | 0–1 shared | **0–1 shared** | $210 | Buy | **CROSS-REF** — `VENDOR-ECOSYSTEMS.md` §6.4 | Only needed for the geared-up variant. One pack serves both robots. |

**No complete-kit option exists.** **CONFIRMED-BIOBUZZ — R301** prohibits COTS MAJOR MECHANISMS
purpose-built for a game task, and no FTC vendor sells a shooter kit. **The launcher is necessarily a
fabricated mechanism.** This is a rule, not a market gap.

### 3.4 FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours (per robot) |
|---|---|---|---|---|---|
| **Hood (curved guide surface)** | 3D print in sections, **or** heat-bend polycarbonate over a printed form | **PETG or ABS** print; or **1/16–1/8 in. polycarbonate** sheet | 1 | 2 | **4–8 h** (design-iteration heavy) |
| **Side plates** (hold shaft, hood, and set compression) | 3D print, or cut from polycarbonate / 1/8 in. aluminium with hand tools | PETG print or polycarb sheet | 2 | 4 | **3–5 h** |
| **Compression adjustment slots** | Slot the side plates | — | — | — | included above |
| Entry throat / feed ramp into the wheel | 3D print | PETG | 1 | 2 | **2–4 h** |
| Flywheel guard (R202.I entanglement, safety) | Print or polycarb | PETG / polycarb | 1 | 2 | **1–2 h** |
| Motor mount plate | Print or drill goBILDA/REV plate | PETG / aluminium | 1 | 2 | **1–2 h** |
| **Total** | | | | | **≈ 11–21 h per robot** |

**Material guidance (JUDGMENT):**

- **PETG** is the right default for hoods and side plates: tougher and more impact-tolerant than PLA,
  prints on any FTC-team printer, and does not creep as badly near a warm motor.
- **PLA is a trap for the hood.** It is stiff and prints beautifully, then goes brittle and cracks at the
  fastener bosses after a few hundred shots. Acceptable for **prototype iteration only**.
- **ABS/ASA** if you have an enclosure — better heat tolerance next to a motor running at 6000 RPM.
- **TPU** for the entry throat and any element-contacting lip: it will not mark elements (**R201**).
- **Polycarbonate sheet** for the hood if you can heat-bend it — a single smooth continuous curve
  outperforms a printed one with layer lines, and layer lines are exactly what scuffs elements.
- 🔴 **Print the hood in ≥ 3 versions before committing.** Hood curvature is the variable you cannot
  calculate accurately; you iterate it. Budget the filament, not the certainty.

### 3.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Flywheel motor (`5203-2402-0001`) | $54.99 | $109.98 |
| Steel flywheel (`3628-0032-0082`) | $15.99 | $31.98 |
| Compliant wheels (2, mixed durometer) | ≈ $18 | ≈ $36 |
| Shaft, 2 bearings/pillow blocks, hub | ≈ $35 | ≈ $70 |
| Fasteners, spacers, guard hardware | ≈ $10 | ≈ $20 |
| **COTS subtotal** | **≈ $135** | **≈ $268** |
| Filament / polycarb (incl. iteration) | ≈ $25 | ≈ $50 |
| **Total materials** | **≈ $160** | **≈ $318** |
| **Student-hours** | **11–21 h** | **16–30 h** (second copy is faster) |

**VERIFY-BEFORE-ORDER — all prices as of August 2026.**

### 3.6 Common failure modes and the spares to stock

| Failure | Cause | Fix | Spare to stock |
|---|---|---|---|
| 🔴 **Shot-to-shot scatter** | Flywheel RPM sag between shots; no velocity feedback (§2.4) | Add inertia mass; add closed-loop velocity + a "ready" gate | — (software) |
| 🔴 **First shot short, rest fine** | Firing before spin-up completes | Spin up during approach; gate on measured velocity | — |
| **Compliant wheel wears flat / glazes** | High slip at the contact patch | Reduce compression; softer durometer | **2 spare compliant wheels per robot** |
| **Element marking / scuffing** (**R201 risk**) | Hard wheel + high slip + layer-line hood | Softer wheel, TPU throat, smooth/sand the hood | Sandpaper; TPU throat spare |
| **Hood cracks at fastener bosses** | PLA hood, vibration | Reprint in PETG; add washers | **1 spare printed hood per robot** |
| **Shaft wobble / precession** | Cantilevered flywheel, single bearing | Support both ends | **2 spare bearings** |
| **Set screws back out** | Vibration at 6000 RPM | **Clamping hubs**, blue threadlocker | Threadlocker; spare set screws |
| 🔴 **Compliant wheel hub fails / wheel disintegrates** | **Running the wheel past its RPM rating.** REV's DUO compliant wheel is rated **5,500 RPM** (VERIFIED) while the 1:1 motors free-spin at **6000 RPM** | **Software velocity cap below the wheel's rating.** Confirm the rating for whichever wheel you pick — AndyMark does not publish one for its compliant wheels, so treat 5,500 RPM as the working ceiling unless the vendor says otherwise | Spare compliant wheels |
| **Motor overheats** | Sustained high-RPM running all match | Spin down between cycles; do not idle at full speed | **1 spare flywheel motor per program** |
| **Encoder cable fatigue** | Vibration | Strain-relieve at the motor | **2 spare encoder cables** |

**JUDGMENT — minimum spares for a two-robot program:** 4 compliant wheels, 2 printed hoods, 4 bearings,
1 complete spare flywheel motor, 2 encoder cables, threadlocker. Approximately **$100**.

### 3.7 Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Motor | 1 × HD Hex `REV-41-1291` ($22) or 1 × `5203-2402-0001` | 1 × `5203-2402-0001`, encoder wired and trusted |
| Inertia | Compliant wheel only | **+ `3628-0032-0082` steel flywheel** |
| Hood | Single printed PETG hood, fixed angle | Heat-bent polycarbonate, iterated 3+ times, TPU throat |
| Compression | Fixed holes | **Slotted, adjustable, marked with a witness line** |
| Control | Open-loop power, fixed wait | **PIDF velocity control + ready-gate + distance→RPM lookup** (§12) |
| Aiming | Drive to a taped floor spot | Limelight 3A + heading alignment (§10) |
| Shots/sec | ~0.3 (one per 3–4 s) | 1.5–3 |
| Build hours | 8–12 h | 25–40 h + programming |
| Cost per robot | ≈ $90 | ≈ $160 (+ $189 if Limelight) |

---

## 4. L2 — Dual-flywheel (counter-rotating) shooter

### 4.1 What it is and when a design needs it

Two powered wheels facing each other, spinning in opposite directions, with the element passing through
the nip between them. Both surfaces drive the element, so **exit speed approaches full surface speed**
(§2.2) and spin is controllable by mismatching the two wheel speeds.

**A design needs it when:** you need **spin control** (a game where the element must not bounce out, or
must curve); when you want **lower RPM for the same range** (quieter, less wear, less marking); or when
the element is heavy enough that single-sided grip slips.

### 4.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Two motors, independent velocity control** | 4 | **4** | **5** | 3 | **2** | 🔴 Maximum control, maximum cost. **Two R503 motor slots.** Two PIDF loops per robot = **four** across the program. |
| Two wheels, **one motor**, belt/gear coupled to counter-rotate | **4** | 3 | 3 | 3 | 3 | Saves an R503 slot. Mechanically harder; a reversing idler or crossed belt is needed. |
| **Two motors, same commanded speed** (no spin control) | 3 | 4 | 4 | **4** | 3 | Simpler software than independent control; still two motor slots. |
| Vertical stack (over/under) vs. horizontal (side/side) | — | — | — | — | — | Over/under imparts back/topspin; side-by-side imparts sidespin. **Over/under is the usual FTC choice.** |

### 4.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Flywheel motors ×2** | goBILDA | Yellow Jacket **1620 RPM — `5203-2402-0003`** (8 mm REX) | **2** | **4** | **$54.99 ea = $220** | Buy | **VERIFIED** | 🟢 At dual-flywheel efficiency, **1620 RPM on a 96 mm wheel (8.1 m/s) is already in the useful band** (§2.3) — no gear-up needed. |
| Flywheel motors, higher torque | goBILDA | Yellow Jacket **1150 RPM — `5203-2402-0005`** (7.9 kg·cm) | 2 | 4 | **$54.99 ea = $220** | Buy | **VERIFIED** | Better recovery torque, lower top speed. Good if the element is heavy. |
| Flywheel motors, budget | REV | **HD Hex bare — `REV-41-1291`** | 2 | 4 | **$22.00 ea = $88** | Buy | **CROSS-REF** | 🟢 **Halves the motor cost across two robots** ($88 vs $220). Needs external encoders or a gearbox with one. |
| **Compliant wheels ×2** | AndyMark | `am-4537` 3 in. 5 mm hex **$8.70** / `am-3480` 4 in. **$11.00** | **2–4** | **4–8** | **$35–$88** | Buy | **VERIFIED** | Both wheels must be the **same diameter and durometer** or the shot skews. |
| Compliant wheels, goBILDA | goBILDA | Boot-Wheel `3615-4008-0096` **$8.99** / `3615-4008-0072` **$6.99** | 2–4 | 4–8 | **$28–$72** | Buy | **VERIFIED** | 30A. 8 mm REX bore — no adapter needed. |
| Steel flywheels ×2 | goBILDA | `3628-0032-0082` **$15.99** / `3628-0014-0060` **$12.99** | 2 | **4** | **$52–$64** | Buy | **VERIFIED** | Both sides need inertia, or the weaker side sags and the shot skews. |
| Shafts, bearings, pillow blocks, hubs | goBILDA | 8 mm REX shafting; `1611` bearings; `1602`/`1605`/`1606` pillow blocks | 2 sets | **4 sets** | ≈ $60–$100 | Buy | **CROSS-REF** — `VENDOR-ECOSYSTEMS.md` §6.4 | Four bearing supports minimum. |
| Reversing idler / crossed belt (1-motor variant only) | goBILDA | 5 mm HTD Starter Pack **$209.99**; sprockets `3311-…` $2.29–$4.79 | 1 shared | 1 shared | $210 | Buy | **CROSS-REF** | Only for the single-motor coupled variant. |

### 4.4 FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours |
|---|---|---|---|---|---|
| **Side plates (2), holding both shafts at a fixed nip gap** | 3D print or cut polycarb/aluminium | PETG / polycarb | 2 | 4 | **5–8 h** — 🔴 the hard part; **both shafts must stay parallel** |
| Nip-gap adjustment slots | Slot one shaft's mounts | — | — | — | included |
| Entry throat guiding the element into the nip | 3D print | PETG + TPU lip | 1 | 2 | **3–5 h** |
| Exit guide / short hood | 3D print or polycarb | PETG / polycarb | 1 | 2 | **2–4 h** |
| Guards over both wheels (R202.I) | Print or polycarb | PETG | 2 | 4 | **1–2 h** |
| **Total** | | | | | **≈ 11–19 h per robot** |

🔴 **The fabrication risk specific to dual flywheels:** the two shafts must be **parallel and equidistant
from the element path.** With hand tools and 3D-printed plates, a 1° skew or 1 mm offset sends every shot
sideways. **This is why duplicability scores 2.** Robot B's plates must be printed from the same file,
on the same printer, with the same slicer settings — and even then, verify the nip gap with feeler
gauges on both robots.

### 4.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| 2 × motors (`5203-2402-0003`) | $109.98 | $219.96 |
| *(budget alt: 2 × `REV-41-1291`)* | *$44.00* | *$88.00* |
| 2 × compliant wheels | ≈ $18–$22 | ≈ $36–$44 |
| 2 × steel flywheels | $31.98 | $63.96 |
| Shafts, 4 bearings, hubs | ≈ $60 | ≈ $120 |
| Fasteners, guards | ≈ $15 | ≈ $30 |
| **COTS subtotal** | **≈ $235** | **≈ $470** |
| *(budget path)* | *≈ $170* | *≈ $340* |
| Filament / polycarb | ≈ $30 | ≈ $60 |
| **Total materials** | **≈ $265** | **≈ $530** |
| **Student-hours** | **11–19 h** | **18–30 h** |

### 4.6 Common failure modes and spares

| Failure | Cause | Fix | Spare |
|---|---|---|---|
| 🔴 **Shot skews left/right consistently** | Wheels at different speeds, different durometers, or shafts not parallel | Match wheels; verify parallelism; equalize velocity setpoints | Matched wheel pairs |
| 🔴 **The two robots shoot differently** | Nip gap or plate tolerance differs | Feeler-gauge both; use the same print file and printer | — |
| One wheel sags more than the other | Unequal inertia or unequal load | Same flywheel on both sides | Spare steel flywheel |
| Element stalls in the nip | Nip gap too tight, or entry misaligned | Widen gap; fix the throat | Spare throat print |
| Doubles the motor budget cost | Design choice | Consider the 1-motor coupled variant | — |

**Spares for two robots:** 4 matched compliant wheels, 2 spare throats, 4 bearings, 1 spare motor. ≈ **$120**.

### 4.7 Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Motors | 2 × `REV-41-1291` at the same commanded power | 2 × `5203-2402-0003`, independent PIDF velocity |
| Spin | Uncontrolled | Deliberately mismatched for shot shaping |
| Nip gap | Fixed, printed | Slotted, feeler-gauge set, recorded per robot |
| Software | Same power to both, fixed wait | Two velocity loops, both ready-gated, distance→RPM table |
| Cost per robot | ≈ $170 | ≈ $265 |
| **R503 cost** | **2 motor slots** | **2 motor slots** |

**JUDGMENT for this program:** dual flywheel is the **A-team-only** option. It costs **two of eight motor
slots**, doubles the tuning work, and is the hardest mechanism in this file to duplicate. Choose it only
if kickoff proves spin control is genuinely required.

---

## 5. L3 — Linear puncher / spring catapult

### 5.1 What it is and when a design needs it

Energy is stored slowly in a **spring, elastic, or gas spring**, held by a mechanical latch, and released
all at once into the element. Two families:

- **Linear puncher:** a spring-loaded plunger strikes the element along a straight guide.
- **Rotary catapult:** a spring-loaded arm sweeps up and releases the element at a fixed angle.

**A design needs it when:** the game asks for a **repeatable one-shot** rather than sustained fire; when
the element is **rigid, irregular, or non-compressible** (flywheels handle these badly); when you want
**zero standby power** (no spin-up, no idle current); or when **motor slots are exhausted** and the launch
can be driven off a slow winch motor you already have.

🔴 **The R506 constraint that shapes every catapult in BIOBUZZ.**
**CONFIRMED-BIOBUZZ — R506:** *"The use of relays, electromagnets, and electrical solenoid actuators is
prohibited."* The intuitive catapult trigger — a solenoid pulling a sear — is **illegal**. Your release
must be one of:

| Legal release mechanism | How it works | R503 cost |
|---|---|---|
| **Servo-driven sear/latch** | A servo rotates a hook out of engagement | 1 servo |
| **Motor-driven cam** | A cam lifts and drops the arm once per revolution | shares the winch motor — **0 extra** |
| **Slipping-gear / gap-tooth gear** | A gear with missing teeth winds then releases automatically | shares the winch motor — **0 extra** |
| **Ratcheting winch + servo pawl release** | **R303.H explicitly permits COTS ratcheting devices** | 1 servo |

**JUDGMENT:** the **gap-tooth gear** is the elegant answer — one motor winds and fires with no separate
trigger, and it costs **zero** additional R503 slots. It is also the hardest to fabricate without a mill.
The **servo sear** is the realistic answer for this team.

### 5.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Rotary catapult, surgical tubing, servo sear** | 3 | **1** | **2** | 3 | **4** | 🟢 Cheapest launcher on this page. Energy set by tubing count/stretch — a *physical*, copyable number. |
| Rotary catapult, **gas spring** | 3 | 3 | 2 | **4** | **4** | **R801.A** explicitly permits sealed pre-charged COTS gas shocks. Very consistent; force does not decay like rubber. |
| **Linear puncher, compression spring** | 4 | 2 | 3 | 3 | 3 | Straight-line guide needed; more precise fabrication. |
| Catapult with **adjustable draw** (variable range) | **5** | 3 | **4** | 2 | **2** | Adds a DoF and most of the flywheel's tuning burden. **JUDGMENT: not worth it for this team.** |
| **Constant-force spring** wind-up | 3 | 2 | 2 | 4 | 4 | Force stays flat across the stroke — the most repeatable spring type. |

🟢 **The catapult's structural advantage over the flywheel:** its energy is set by **geometry and spring
choice**, both of which are *physically measurable and physically copyable*. A flywheel's energy is set by
a **software number that depends on battery voltage, motor temperature and wheel wear**. That is why
catapult duplicability scores 4 and dual-flywheel scores 2.

### 5.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Latex surgical tubing** | goBILDA | **`2907-0305-0002`** — 3 mm ID × 5 mm OD, 2 m | 1–2 | **2–4** | **$4.99 ea = $10–$20** | Buy | **VERIFIED** — [intake wheels cat.](https://www.gobilda.com/intake-wheels/) | 🟢 The cheapest stored energy in FTC. **Latex ages and loses force — replace it every few events** and log the date. |
| Silicone cord (alternative elastic) | goBILDA | **`2928-0008-0002`** — 8 mm, 50A, 2 m | 0–1 | 0–2 | **$5.99 ea** | Buy | **VERIFIED** | More UV/age-stable than latex; less energy per unit stretch. |
| Silicone tubing | goBILDA | **`2928-0508-0002`** — 5 mm ID × 8 mm OD, 50A, 2 m | 0–1 | 0–2 | **$5.99 ea** | Buy | **VERIFIED** | |
| **Gas spring / gas shock** | goBILDA | Shocks — [motion category](https://www.gobilda.com/motion/) | 1–2 | **2–4** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🔴 **R801.A [CONFIRMED-BIOBUZZ]:** only **sealed, manufacturer-pre-charged** closed-air systems are legal. Specify by **force rating and stroke**, and **buy 4 identical units so both robots match** (`LEGAL-PARTS-CONSTRAINTS.md` §7). |
| Compression / extension / torsion springs | goBILDA | Springs — [hardware category](https://www.gobilda.com/hardware/) | as needed | ×2 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | Unrestricted by R801 (they store no gas). |
| **Winch / draw motor** | goBILDA | Yellow Jacket **1150 RPM `5203-2402-0005`** (7.9 kg·cm) | 1 | **2** | **$54.99 ea = $110** | Buy | **VERIFIED** | High torque, low speed — right for winding a spring. |
| Winch motor, high-torque budget | REV | **Core Hex `REV-41-1300`** — 125 RPM, 3.2 N·m, 288 CPR | 1 | 2 | **$32.00 ea = $64** | Buy | **CROSS-REF** (VERIFIED in `LEGAL-PARTS-CONSTRAINTS.md` §2.5) | 🟢 Excellent catapult winch: very high torque, built-in encoder for draw position. |
| **Sear / release servo** | goBILDA | **2000 Series Dual Mode Servo — `2000-0025-0003`** | 1 | **2** | **$36.99 ea = $74** | Buy | **VERIFIED** — [product page](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/) | **$36.99 VERIFIED 2026-08-22** — this is the *25-3 Speed* variant, 9.3 kg·cm @ 6.0 V, 300° range. Legal by name in Table 12-2. |
| Sear servo, alternative | REV | **Smart Robot Servo — `REV-41-1097`** | 1 | 2 | **$25.50** | Buy | **CROSS-REF** — ⚠ **DISCONTINUED at REV** | Still legal (named in Table 12-2). **If you want these for two robots, buy all of them now.** |
| **Ratchet / one-way bearing** | goBILDA | Ratcheting devices | 1 | 2 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🟢 **R303.H [CONFIRMED-BIOBUZZ]** explicitly lists *"ratcheting devices (wrenches, bearings, etc.)"* as an allowed COTS single-DoF exception. Holds the draw with **zero** motor current. |
| Cord / Dyneema for the draw | any VENDOR | braided line | 1 | 2 | ≈ $10 | Buy | **UNVERIFIED** | Any VENDOR per `LEGAL-PARTS-CONSTRAINTS.md` §8.2. |
| Shaft, bearings, pillow blocks, hubs | goBILDA | as `VENDOR-ECOSYSTEMS.md` §6.4 | 1 set | 2 sets | ≈ $40 | Buy | **CROSS-REF** | |
| Hard end-stop / bumper | goBILDA | Rubber grommets `2911-0014-0003` **$3.99** | 2 | 4 | ≈ $8–$16 | Buy | **CROSS-REF** | 🔴 **The arm stop sets the launch angle. It must not move.** |

### 5.4 FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours |
|---|---|---|---|---|---|
| **Catapult arm / plunger** | 3D print (high infill) or cut aluminium | **PETG ≥ 50 % infill**, or 1/8 in. aluminium bar | 1 | 2 | **4–6 h** |
| **Arm pivot mounts** | Print + bearings, or drilled plate | PETG / aluminium | 2 | 4 | **2–3 h** |
| **Element cup / pocket** | 3D print, TPU lining | PETG shell + TPU liner | 1 | 2 | **2–4 h** |
| **Sear / latch geometry** | 3D print, iterate | **PETG or nylon — not PLA** | 1 | 2 | 🔴 **4–8 h — the highest-iteration part** |
| **Hard stop / angle-setting bracket** | Print + rubber bumper | PETG + grommet | 1 | 2 | **1–2 h** |
| Spring anchor points | Print or drilled plate | PETG / aluminium | 2–4 | 4–8 | **1–2 h** |
| Draw-limit / arm guard | Print | PETG | 1 | 2 | **1 h** |
| **Total** | | | | | **≈ 15–26 h per robot** |

**Material guidance (JUDGMENT):**

- 🔴 **The sear is the part that breaks.** It sees the full stored energy as an impact every shot. Print it
  in **PETG or nylon at high infill**, keep the engagement face perpendicular to the load, and **print
  four spares before your first event**. A cracked sear is a dead catapult, and it always cracks at an event.
- **The arm should be stiff, not strong.** A flexy arm stores energy and releases it late, which changes
  the launch angle shot-to-shot. Aluminium bar beats a printed arm here if you can cut and drill it.
- **TPU in the element cup** protects the element (**R201**) and damps bounce-out.
- 🔴 **The hard stop defines your launch angle, and therefore your range.** Make it adjustable, then
  **lock it and mark it with a witness line**, so robot B can be set to the identical position.

### 5.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Winch motor (Core Hex `REV-41-1300`) | $32.00 | $64.00 |
| *(alt: `5203-2402-0005`)* | *$54.99* | *$109.98* |
| Sear servo (`2000-0025-0003`) | **$36.99** | **$73.98** |
| Surgical tubing / elastic | $4.99 | $9.98 |
| *(alt: gas spring)* | *NEEDS-SKU-CHECK* | *buy 4 identical* |
| Ratchet, shaft, bearings, hubs, stops | ≈ $55 | ≈ $110 |
| **COTS subtotal** | **≈ $129** | **≈ $258** |
| Filament (incl. sear iteration + spares) | ≈ $25 | ≈ $50 |
| **Total materials** | **≈ $154** | **≈ $308** |
| **Student-hours** | **15–26 h** | **22–38 h** |
| **R503 cost** | **1 motor + 1 servo** | |

🟢 **Note the R503 economy:** a catapult costs **one motor slot and one servo slot** — the same as a
single flywheel, and **one motor slot cheaper than a dual flywheel.**

### 5.6 Common failure modes and spares

| Failure | Cause | Fix | Spare |
|---|---|---|---|
| 🔴 **Sear cracks or wears round** | Impact loading every shot | PETG/nylon, high infill, perpendicular engagement | **4 spare sears per program** |
| 🔴 **Range decays over the day** | Latex tubing fatigues and takes a set | Replace tubing on a schedule; log install date | **Spare tubing, always** |
| Arm bounces off the stop, angle varies | Hard stop, no damping | Rubber grommet bumper | Spare grommets |
| Element bounces out of the cup before release | Cup too shallow / no retention | Deepen cup; add TPU lip | Spare cup print |
| **Winch stalls at full draw** | Motor too fast/weak | Use Core Hex or 1150 RPM | — |
| Draw position drifts | No encoder or no ratchet | Encoder + hard limit, or **R303.H ratchet** | — |
| Arm flexes, shot goes long/short | Printed arm too compliant | Aluminium arm | Spare arm |
| **Robot A and B shoot different distances** | Different tubing age/stretch, different stop position | **Log tubing install date and stop witness mark per robot** | — |

**Spares for two robots:** 4 sears, 2 arms, 2 cups, 2 m spare tubing, 4 grommets. ≈ **$40.**

### 5.7 Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Energy | 2 loops surgical tubing, fixed | Gas spring, or constant-force spring |
| Draw | Core Hex winch to a hard limit | Core Hex + encoder + **R303.H ratchet** hold |
| Release | Printed servo sear | Hardened/nylon sear, or gap-tooth gear (0 servo slots) |
| Angle | Fixed hard stop | Fixed hard stop, witness-marked, identical on both robots |
| Range control | **None — drive to a spot** | None — *still* drive to a spot. 🟢 **This is a feature.** |
| Cost per robot | ≈ $90 | ≈ $145 |
| Shots/sec | 0.3–0.5 (draw time dominates) | 0.5–1.0 |

🔴 **The catapult's real limitation is cycle rate, not accuracy.** Winding a spring takes 1–3 seconds. If
the kickoff game pays **per element** and expects sustained fire, a catapult loses badly to a flywheel. If
it pays for **a few accurate shots**, the catapult is the better engineering choice for this team.

---

## 6. L4 — Elastic / slingshot launcher

### 6.1 What it is and when a design needs it

The element is held against a stretched elastic band and released directly — no arm, no plunger. The
element is the projectile *and* the moving mass. Effectively a catapult with the arm deleted.

**A design needs it when:** the element is light and aerodynamically stable; the shot is short-range; and
you want the **absolute minimum part count**. This is a legitimate **B-team / rookie** pattern.

**JUDGMENT:** treat this as a **prototype-grade** mechanism. It is fast to build and hard to make precise,
because the elastic contacts the element directly and any asymmetry becomes a tumbling shot.

### 6.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Fixed-draw slingshot, servo release** | **1** | **1** | 2 | 2 | **4** | Simplest launcher that exists. One servo, some tubing. |
| Servo-drawn slingshot (servo does the pull) | 2 | 1 | 2 | 2 | 4 | Only viable if draw force is within servo torque — **check R502 8 W limit**. |
| Motor-drawn slingshot | 3 | 2 | 3 | 3 | 3 | Converges on the catapult (§5). |

### 6.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Latex surgical tubing** | goBILDA | **`2907-0305-0002`** — 3 mm ID × 5 mm OD, 2 m | 1 | **2** | **$4.99 ea = $10** | Buy | **VERIFIED** | The whole energy system. |
| Silicone cord | goBILDA | **`2928-0008-0002`** — 8 mm, 50A, 2 m | 0–1 | 0–2 | **$5.99 ea** | Buy | **VERIFIED** | More age-stable than latex. |
| **Release servo** | goBILDA | 2000 Series Dual Mode Servo — `2000-0025-0003` | 1 | **2** | **$36.99 ea = $74** | Buy | **VERIFIED** — [product page](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/) | **$36.99 VERIFIED 2026-08-22** — *25-3 Speed*, 9.3 kg·cm @ 6.0 V, 300° range. |
| Draw motor (drawn variants only) | REV | Core Hex `REV-41-1300` | 0–1 | 0–2 | **$32.00** | Buy | **CROSS-REF** | |
| Anchors, standoffs, fasteners | goBILDA | M4 Hardware Starter Pack `3201-0010-0001` **$139.99** (shared) | — | 1 shared | — | Buy | **CROSS-REF** — `VENDOR-ECOSYSTEMS.md` §6.5 | Already in the standing order. |

### 6.4 FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours |
|---|---|---|---|---|---|
| Frame / fork holding the elastic | 3D print or cut extrusion | PETG / goBILDA channel | 1 | 2 | **2–4 h** |
| Element pocket / pouch | 3D print + TPU | PETG + TPU | 1 | 2 | **2–3 h** |
| Release hook | 3D print | PETG/nylon | 1 | 2 | **2–4 h** |
| Guide rails (keep the element straight) | Print or polycarb | PETG / polycarb | 2 | 4 | **1–2 h** |
| **Total** | | | | | **≈ 7–13 h per robot** |

### 6.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Servo (`2000-0025-0003`) | **$36.99** | **$73.98** |
| Tubing | $4.99 | $9.98 |
| Hardware, anchors | ≈ $10 | ≈ $20 |
| **COTS subtotal** | **≈ $52** | **≈ $104** |
| Filament | ≈ $12 | ≈ $24 |
| **Total materials** | **≈ $64** | **≈ $128** |
| **Student-hours** | **7–13 h** | **10–18 h** |
| **R503 cost** | **0 motors + 1 servo** | 🟢 **the cheapest actuator footprint of any launcher here** |

### 6.6 Common failure modes and spares

| Failure | Cause | Fix | Spare |
|---|---|---|---|
| 🔴 **Element tumbles in flight** | Asymmetric release; pouch not centred | Symmetrical pouch; guide rails | Spare pouch |
| Range decays through the day | Latex fatigue | Scheduled replacement; log date | **Spare tubing** |
| Release hook wears | Repeated load | Nylon/PETG high infill | **3 spare hooks** |
| Servo stalls trying to release under load | Draw force exceeds servo torque | Over-centre release geometry so the servo only *trips* the latch | — |
| Only one range works | No adjustment by design | Accept it; drive to a spot | — |

### 6.7 Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Everything | Printed fork, tubing, servo hook | 🔴 **There isn't really a competitive version.** Once you add draw control and range adjustment you have built a worse catapult (§5). |

**JUDGMENT:** build this in **week 1 as a prototype** to measure how the actual BIOBUZZ element flies —
it is the fastest way to gather ballistic data — then decide between a flywheel and a catapult with real
numbers instead of guesses. **Its value is as an experiment, not as a competition mechanism.**

---

## 7. L5 — Pneumatic launcher — ILLEGAL IN BIOBUZZ

### 7.1 The ruling

🔴 **CONFIRMED-BIOBUZZ — R801 (Section 12.8). Do not design, propose, or buy this.**

> **A.** *"ROBOTS may only use sealed, COTS closed-air systems which are pre-charged by the manufacturer
> (such as gas shocks),"*
> **B.** no stored-pressure components actuated by a device like a solenoid or able to change stable state,
> **C.** *"ROBOTS may not generate pressure or vacuum,"*
> **D.** no user-adjustable gas storage vessels, **except air-filled (pneumatic) COTS wheels**,
> **E.** no device creating high-speed airflow, **except cooling fans integrated into COTS computing devices**.

Blue box: *"robots may not use pneumatic actuators, pressure or vacuum storage devices, compressors,
vacuum generators, or air blowers, but they may use 'closed air' systems which were sealed by their
manufacturer. This includes items such as **gas springs, and dampers**."*

Reinforced by **R506** (no solenoid actuators — so even a legally-stored-air system could not be valved)
and **R204** (no airflow-generated downforce).

### 7.2 What this rules out, concretely

| ❌ Illegal — do not buy, do not propose | Rule |
|---|---|
| Pneumatic cylinder launchers of any kind | R801.A, R801.B |
| Air tanks, accumulators, user-charged reservoirs | R801.C, R801.D |
| Compressors, hand pumps to charge an on-board vessel | R801.C |
| Solenoid valves (also independently banned) | R801.B, **R506** |
| CO₂ cartridges / compressed-gas launchers | R801.C, R801.D |
| Blower or ducted-fan launchers | R801.E |
| Vacuum or suction pick-up on the feed | R801.C, R204 |

### 7.3 What remains legal, and is the correct substitute

| ✅ Legal | Rule | Use it for |
|---|---|---|
| **COTS gas springs / gas shocks / dampers**, sealed and pre-charged by the manufacturer | **R801.A** + blue box | Catapult energy storage (§5) — this is the sanctioned "pneumatic-feeling" option |
| Coil, extension, torsion and **constant-force springs** | unrestricted | Catapult and puncher energy |
| Surgical tubing, silicone cord | unrestricted | Elastic energy (§5, §6) |
| **High-speed flywheels and rollers** | **R801 blue box, explicit** | Flywheel shooters (§3, §4) |

🟢 **Purchasing consequence for this program:** the entire pneumatics aisle at every FTC vendor is off the
table — **and that is good news for a two-robot team.** Pneumatics duplicate badly (tubing routing, leak
chasing, and per-robot charge state are all bespoke). See `LEGAL-PARTS-CONSTRAINTS.md` §7.

**BOM impact: $0. There is nothing to buy in this section.**

---

## 8. L6 — Ramps, chutes and deposits — the no-launch alternative

### 8.1 What it is and when a design needs it

The robot **drives to the target** and releases elements under gravity down a ramp, chute or tipping
hopper. **No launching at all.** It is included in a launcher catalog because it is the most frequently
correct answer, and the one most often skipped past on the way to building something exciting.

**A design needs it when:** the target is **reachable by driving**; the game pays **per element** so
throughput beats range; or the target is **low and forgiving**. It is also the right **B-team** mechanism
in almost every launcher-friendly game.

> **Cross-ref — `ROBOT-ARCHETYPE-LIBRARY.md`** records the calibration case directly: in VELOCITY VORTEX,
> *"a dump bot and a flywheel bot earned the same teleop rate"* because a corner deposit paid the same 5
> points as the launcher-required centre target. **Read the point table before you read this section's
> neighbours.**

### 8.2 The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Fixed gravity chute + servo gate** | **1** | **1** | **1** | **5** | **5** | 🟢 **The highest reliability and duplicability scores in this entire file.** |
| **Tipping / dumping hopper** (servo or motor) | 2 | 2 | **1** | **4** | **5** | One actuator dumps everything at once. |
| Powered belt/roller ejector | 3 | 2 | 2 | 4 | 4 | Controlled release rate; shares parts with the intake. |
| Chute with **passive one-way gate** | 2 | **1** | **1** | 4 | **5** | 🟢 **Zero actuator slots.** A sprung flap that elements push past but cannot return through. |

### 8.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Gate / dump servo** | goBILDA | 2000 Series Dual Mode Servo — `2000-0025-0003` | 1 | **2** | **$36.99 ea = $74** | Buy | **VERIFIED** — [product page](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/) | **$36.99 VERIFIED 2026-08-22** — *25-3 Speed*, 9.3 kg·cm @ 6.0 V, 300° range. Only actuator required. |
| Dump motor (large hoppers) | REV | Core Hex `REV-41-1300` | 0–1 | 0–2 | **$32.00 ea** | Buy | **CROSS-REF** | High torque for tipping a loaded hopper. |
| Servo horn / hub | goBILDA | Servo hubs (H25T 25-tooth) | 1 | 2 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** — [hubs](https://www.gobilda.com/hubs/) | |
| Hinge hardware / pivot | goBILDA | Ball joint linkages, rod ends | 2 | 4 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **R303.L [CONFIRMED-BIOBUZZ]** permits variable-angle linkage COTS items. |
| **Springs for a passive gate** | goBILDA | Springs — [hardware](https://www.gobilda.com/hardware/) | 1–2 | **2–4** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🟢 **Zero R503 slots.** |
| Polycarbonate sheet | any VENDOR (McMaster, local plastics) | 1/16–1/8 in. polycarbonate | 1 sheet shared | 1–2 sheets | ≈ $25–$60 | Buy (raw material) | **UNVERIFIED** | **R302** explicitly permits sheet stock as raw material. Any VENDOR per §8.2 of `LEGAL-PARTS-CONSTRAINTS.md`. |

### 8.4 FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours |
|---|---|---|---|---|---|
| Chute / ramp surface | Cut + bend polycarbonate, or 3D print | **Polycarb 1/16 in.** or PETG | 1 | 2 | **3–5 h** |
| Hopper walls | Cut polycarb; rivet/bolt to frame | Polycarb | 3–4 | 6–8 | **3–5 h** |
| Gate flap + pivot | 3D print | PETG + TPU seal lip | 1 | 2 | **2–3 h** |
| Element-friendly liner | TPU print or adhesive foam | TPU / foam | 1 | 2 | **1–2 h** |
| **Total** | | | | | **≈ 9–15 h per robot** |

**Material guidance (JUDGMENT):** **polycarbonate, not acrylic.** Acrylic is cheaper and clearer and it
**shatters** on the first hard contact — an R201 mess risk and a safety problem. Polycarbonate bends cold,
drills without cracking if you back it up, and survives being driven into a wall. Buy one 24 × 48 in.
sheet and it will supply both robots' hoppers, chutes and guards for the whole season.

### 8.5 Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Gate servo (`2000-0025-0003`) | **$36.99** | **$73.98** |
| Hinges, springs, hardware | ≈ $15 | ≈ $30 |
| Polycarbonate (share of one sheet) | ≈ $20 | ≈ $40 |
| **COTS subtotal** | **≈ $72** | **≈ $144** |
| Filament | ≈ $10 | ≈ $20 |
| **Total materials** | **≈ $82** | **≈ $164** |
| **Student-hours** | **9–15 h** | **13–22 h** |
| **R503 cost** | **0 motors + 1 servo** (or **0 + 0** with a passive gate) | |

### 8.6 Common failure modes and spares

| Failure | Cause | Fix | Spare |
|---|---|---|---|
| Elements bridge and stop flowing | Chute too narrow or too shallow | Widen; steepen to **> 30°**; add a vibration source or agitator (§9.1) | — |
| Elements dribble out early | Gate does not seal | TPU lip on the gate | Spare gate print |
| Dump servo stalls under a full load | Torque underestimated | Move to Core Hex motor, or split the dump | — |
| Chute cracks | Acrylic used instead of polycarbonate | **Use polycarbonate** | Spare sheet offcut |
| 🔴 **Elements trapped, cannot be removed powered-off** | Gate holds them mechanically | **R203 violation.** Add a manual release or make the gate gravity-openable | — |

### 8.7 Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Structure | Printed chute, servo gate | Polycarb chute, TPU-sealed gate, passive one-way inlet |
| Control | Servo open/close on a button | Timed staged release to avoid target jams |
| Cost per robot | ≈ $45 | ≈ $70 |
| Reliability | **Already excellent** | Excellent |

🟢 **JUDGMENT — the honest recommendation.** If kickoff shows the target is drivable-to, **build this on
both robots and spend the saved 40+ student-hours and $300 on drivetrain quality and driver practice.**
It scores as well as a launcher in many games and it will never miss.

---

## 9. FEED SYSTEMS — where launcher seasons are actually lost

> 🔴 **The thesis of this file.** The launcher is the part students want to build and the part that gets
> built first. **The feed system is the part that decides your score.** A flywheel that is perfectly tuned
> and fed by a hopper that jams every fourth element is a **0.25-elements-per-second robot**, which is
> worse than a dump bot.
>
> **`ROBOT-ARCHETYPE-LIBRARY.md` §3.3 states the rule of thumb directly: *"Budget the feeder at twice the
> launcher's build hours."* Every hour estimate in this section assumes you took that seriously.**

### 9.0 The feed chain, and the three places it breaks

```
FIELD → intake → hopper (bulk storage) → agitator → indexer (single-file) → kicker/gate → launcher
                     ↑ bridging           ↑ starving      ↑ double-feed        ↑ mistiming
```

| Failure | Where | Symptom | Section |
|---|---|---|---|
| **Bridging / arching** | Hopper | Elements form a stable arch and stop flowing even though the hopper is full | §9.1 |
| **Double-feed** | Indexer | Two elements enter the launcher together; both go nowhere useful, and the flywheel stalls | §9.2 |
| **Mistimed feed** | Kicker | Element arrives before the flywheel has recovered → short shot | §9.3, §12 |

### 9.1 F1 — Hopper and agitator

#### What it is and when a design needs it

A bulk container holding several elements, with something to keep them moving toward the exit. You need it
whenever the robot carries **more than 2–3 elements**. Below that count, feed them single-file from the
intake (§9.2) and **skip the hopper entirely** — a real and underused simplification.

#### 🔴 The R203 constraint that must shape your hopper on day one

**CONFIRMED-BIOBUZZ — R203:** *"ROBOTS must allow removal of SCORING ELEMENTS from the ROBOT and the ROBOT
from FIELD elements while powered off."*

A hopper whose only exit is past a powered kicker or a servo-held gate is an **inspection failure**. Design
one of these in from the start:

- A gravity-openable gate (spring-return, not servo-held closed).
- A hinged or removable hopper wall/lid.
- An open top wide enough to reach in and lift elements out.

**JUDGMENT:** the open-top hopper solves R203 for free and is also the easiest to load in the pit. Prefer it.

#### The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Passive sloped hopper, no agitator** | **1** | **1** | 2 | 2 | **5** | 🟢 Free, and works **only if walls are steep enough**. See the geometry table below. |
| Sloped hopper + **compliant-wheel agitator** (motor) | 3 | 3 | 3 | **4** | 3 | The standard reliable answer. **Costs 1 motor slot.** |
| Sloped hopper + **agitator sharing the intake motor** | **4** | 2 | 3 | 4 | 3 | 🟢 **Zero extra R503 slots** — belt the agitator off the intake shaft. Best value; harder to route. |
| **Vibrating / oscillating floor** (servo) | 2 | 2 | **4** | 2 | 3 | Cheap but fiddly; helps bridging only marginally. |
| **Funnel with a moving wall** (servo paddle) | 2 | 2 | 3 | 3 | 4 | Sweeps elements to the exit. **Costs 1 servo.** |
| **Narrow "no-hopper" serpentine magazine** | 2 | **1** | **1** | **5** | **5** | 🟢🟢 **The best answer when element count is low.** Elements sit single-file in a tube. **Cannot bridge — there is nowhere to bridge.** |

#### 🔴 Anti-bridging geometry — the numbers that matter

**JUDGMENT — these are the design rules that prevent most hopper failures. Apply them before you buy anything.**

| Parameter | Rule of thumb | Why |
|---|---|---|
| **Wall angle from horizontal** | **≥ 35°**, prefer **45°+** | Below ~30° elements sit still. This is the number one hopper mistake. |
| **Exit width** | **≥ 1.5 × element diameter**, ideally **2×** | An exit under 1.5× is a bridge generator. |
| **Hopper walls converging to the exit** | Converge on **only two** sides, not four | Four-sided convergence is a classic arch former. Two-sided funnels flow far better. |
| **Any internal corner** | **Radius or chamfer it** | Sharp internal corners trap elements. |
| **Wall surface** | **Smooth and slippery** — sanded PETG, or polycarbonate | Layer lines are friction. |
| **Element count above the exit** | Keep the stack shallow | Deep stacks generate high wall pressure and lock the arch in place. |

🔴 **The single most valuable hopper design move: make one wall clear polycarbonate.** You cannot debug a
jam you cannot see. This costs nothing and saves whole practice sessions.

#### BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Agitator motor** | goBILDA | Yellow Jacket **1150 RPM `5203-2402-0005`** (7.9 kg·cm) | 0–1 | **0–2** | **$54.99 ea** | Buy | **VERIFIED** | Slow and torquey is right — a fast agitator throws elements out. **Costs 1 R503 motor slot.** |
| Agitator motor, budget | REV | **Core Hex `REV-41-1300`** — 125 RPM | 0–1 | 0–2 | **$32.00 ea** | Buy | **CROSS-REF** | 🟢 125 RPM is nearly ideal for an agitator with no extra reduction. |
| **Agitator wheels (soft, forgiving)** | goBILDA | **3615 Boot-Wheel 30A, 8 mm REX** — `3615-4008-0096` **$8.99** · `3615-4008-0072` **$6.99** · `3615-4008-0048` **$4.99** | 2–4 | **4–8** | **$20–$36** | Buy | **VERIFIED** — [intake wheels](https://www.gobilda.com/intake-wheels/) | 30A is soft enough not to mark elements (**R201**). |
| Agitator rollers, small | goBILDA | **Intake Roller Wheel 8-pack, 30A, 8 mm REX** — `3618-4008-0016` (16 mm) **$12.99** · `3618-4008-0012` (12 mm) **$12.99** | 1 pk | **1–2 pk** | **$13–$26** | Buy | **VERIFIED** | 🟢 8 wheels per pack — **one pack can serve both robots.** Excellent value for building a roller array. |
| **Compliant agitator wheels** | AndyMark (official FIRST supplier) | Compliant Wheel **35A** (softest) — `am-3462` 2 in. **$6.20** · `am-3945` 3 in. **$8.40** | 2–4 | 4–8 | **$25–$50** | Buy | **VERIFIED** — [product page](https://andymark.com/products/compliant-wheels) | **35A green is the softest AndyMark offers** — best for agitating without marking. |
| Compliant agitator wheels, REV | REV | **DUO Compliant Wheel 2 in., 30A Soft, 4-pk — `REV-41-2035-PK4`** | 1 pk | **1 pk** | **$19.50** | Buy | **VERIFIED** — **In Stock** | 4-pack covers both robots. |
| **Surgical tubing "fingers"** | goBILDA | `2907-0305-0002` — latex, 2 m | 1 | **2** | **$4.99 ea** | Buy | **VERIFIED** | 🟢 Cheapest agitator possible: tubing loops on a slow shaft sweep elements without gripping hard. |
| Silicone cord agitator | goBILDA | `2928-0008-0002` — 8 mm, 50A, 2 m | 0–1 | 0–2 | **$5.99 ea** | Buy | **VERIFIED** | More durable than latex. |
| Paddle servo (funnel variant) | goBILDA | 2000 Series Dual Mode Servo — `2000-0025-0003` | 0–1 | 0–2 | **$36.99 ea** | Buy | **VERIFIED** — [product page](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/) | **$36.99 VERIFIED 2026-08-22** — *25-3 Speed*, 9.3 kg·cm @ 6.0 V, 300° range. |
| Shaft / bearings / hubs | goBILDA | 8 mm REX shafting, `1611` bearings, `1602`/`1605` pillow blocks | 1 set | 2 sets | ≈ $30–$50 | Buy | **CROSS-REF** — `VENDOR-ECOSYSTEMS.md` §6.4 | |
| **Polycarbonate sheet (hopper walls)** | any VENDOR | 1/16 in. clear polycarbonate, 24 × 48 in. | share | **1 sheet** | ≈ $25–$60 | Buy (raw material) | **UNVERIFIED** | 🟢 **R302** permits sheet stock. **Make at least one wall clear.** |

#### FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours |
|---|---|---|---|---|---|
| **Hopper walls (3–4)** | Cut + cold-bend polycarbonate; bolt to frame | **Polycarb 1/16 in.** (≥1 clear) | 3–4 | 6–8 | **4–6 h** |
| **Sloped floor / funnel** | 3D print in sections, or bent polycarb | PETG (sanded smooth) | 1 | 2 | **3–5 h** |
| Corner fillets / anti-bridge inserts | 3D print | PETG | 2–4 | 4–8 | **2–3 h** |
| Agitator shaft mounts | 3D print or drilled plate | PETG / aluminium | 2 | 4 | **1–2 h** |
| **Open-top lip / R203 access** | Print or bend | PETG / polycarb | 1 | 2 | **1 h** |
| Element-friendly liner (if marking appears) | TPU or adhesive foam | TPU | 1 | 2 | **1–2 h** |
| **Total** | | | | | **≈ 12–19 h per robot** |

**Material guidance (JUDGMENT):** **polycarbonate for walls, never acrylic** (§8.4). **Sand printed funnel
surfaces** — layer lines running across the flow direction are a bridging cause you can remove with
five minutes of 220-grit. Print funnel sections **with the layer lines running along the flow**, not across.

#### Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Agitator motor (Core Hex) | $32.00 | $64.00 |
| Agitator wheels / tubing | ≈ $20 | ≈ $40 |
| Shaft, bearings, hubs | ≈ $40 | ≈ $80 |
| Polycarb (share of a sheet) | ≈ $20 | ≈ $40 |
| **COTS subtotal** | **≈ $112** | **≈ $224** |
| Filament | ≈ $20 | ≈ $40 |
| **Total materials** | **≈ $132** | **≈ $264** |
| **Student-hours** | **12–19 h** | **18–28 h** |
| **R503 cost** | **1 motor** (0 if belted off the intake) | |

#### Common failure modes and spares

| Failure | Cause | Fix | Spare |
|---|---|---|---|
| 🔴 **Bridging with a full hopper** | Walls too shallow, exit too narrow, 4-sided convergence | Apply the §9.1 geometry table; add agitator | — |
| 🔴 **Agitator throws elements out of the hopper** | Agitator too fast / too grippy | Slow it (Core Hex 125 RPM); softer 30A wheels; tubing fingers | Spare soft wheels |
| Elements wedge in a corner | Sharp internal corner | Print fillet inserts | Fillet inserts |
| Agitator stalls under a full load | Motor too fast/weak | Core Hex or 1150 RPM | — |
| Elements marked/scuffed (**R201**) | Hard agitator surface, high slip | 30A/35A wheels; TPU liner | TPU liner |
| 🔴 **Cannot remove elements powered off** | **R203 violation** | Open top or spring-return gate | — |
| Cannot diagnose a jam | Opaque walls | **Clear polycarb wall** | — |

**Spares for two robots:** 4 soft wheels, 2 m tubing, 2 sets fillet inserts, TPU liner stock. ≈ **$50.**

#### Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Storage | 🟢 **No hopper — 2–3 element serpentine magazine** | Sloped hopper, 45° walls, clear front |
| Agitation | None needed | Soft-wheel agitator belted off the intake motor (**0 extra slots**) |
| Capacity | 2–3 elements | 5+ elements |
| R203 | Open tube, trivially compliant | Open top + spring-return gate |
| Cost per robot | ≈ $30 | ≈ $132 |
| **Reliability** | 🟢 **Higher** | Lower, but higher capacity |

🔴 **JUDGMENT for this program: start with no hopper.** A 3-element serpentine magazine cannot bridge,
cannot double-feed, needs no agitator motor, and costs almost nothing to duplicate. Add a hopper **only if
the kickoff point table proves that carrying 5+ elements beats cycling faster with 3.**

---

### 9.2 F2 — Single-file indexer (the anti-double-feed mechanism)

#### What it is and when a design needs it

A geometry that accepts elements in bulk and presents them to the launcher **exactly one at a time**. This
is the highest-value, most-skipped mechanism on the robot. **Any launcher that draws from a hopper needs
one.** Without it, two elements arrive together, the flywheel bogs, and both shots are lost.

#### The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Serpentine / S-tube magazine** | **1** | **1** | **1** | **5** | **5** | 🟢🟢 **Best in class.** A tube one element wide. Physically cannot double-feed. Zero actuators. |
| **Star wheel / paddle indexer** (motor) | 3 | 3 | 3 | **4** | 3 | A rotating wheel with element-sized pockets. One pocket = one element, guaranteed by geometry. |
| **Belt/chain indexer with flights** | 4 | 3 | 3 | 4 | 3 | Conveyor with dividers. Good for long paths. |
| **Escapement (two alternating gates)** | 3 | 2 | **4** | 3 | 3 | Two servos alternate: upper holds while lower releases. Precise; timing-sensitive. |
| **Gravity stack + single kicker** | 2 | **1** | 2 | 3 | **4** | Elements stack vertically; kicker takes the bottom one. Simple; can jam if the stack binds. |

🟢 **JUDGMENT — pick the serpentine tube unless you have a reason not to.** It converts a *timing* problem
(hard, software, per-robot) into a *geometry* problem (easy, physical, identically copyable). This is the
single best duplicability decision available in the whole feed chain.

#### 🔴 The geometry that prevents double-feeds

| Parameter | Rule | Why |
|---|---|---|
| **Tube/channel width** | element Ø **+ 2–4 mm**, and **< 1.8 × element Ø** | Wider than 1.8× and two elements can sit side by side. This is *the* double-feed rule. |
| **Tube depth** | element Ø + 2–4 mm | Same reason in the other axis. |
| **Star-wheel pocket depth** | **≥ 0.6 × element Ø** | Shallow pockets let a second element ride along. |
| **Star-wheel shroud clearance** | **< 0.5 × element Ø** | The shroud must physically block a second element from entering a pocket. |
| **Entry throat** | Taper from hopper width to single-file over **≥ 2 × element Ø** of length | An abrupt necking is a jam. |
| **Bend radius in a serpentine** | **≥ 2 × element Ø** | Tight bends bind. |

#### BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Indexer motor** (star-wheel / belt variants) | REV | **Core Hex `REV-41-1300`** — 125 RPM, 288 CPR at output | 0–1 | **0–2** | **$32.00 ea = $64** | Buy | **CROSS-REF** | 🟢 **Built-in encoder at 288 CPR makes precise pocket indexing easy.** Best indexer motor in FTC for the money. |
| Indexer motor, alternative | goBILDA | Yellow Jacket **1150 RPM `5203-2402-0005`** | 0–1 | 0–2 | **$54.99 ea** | Buy | **VERIFIED** | Needs more reduction for pocket indexing. |
| **Indexer rollers (soft)** | goBILDA | Intake Roller Wheel 8-pk 30A — `3618-4008-0016` (16 mm) / `3618-4008-0012` (12 mm) | 1 pk | **1 pk** | **$12.99** | Buy | **VERIFIED** | 🟢 8 per pack covers both robots. Ideal for lining a single-file channel. |
| Indexer belt wheels | goBILDA | Boot-Wheel 30A `3615-4008-0048` (48 mm) **$4.99** | 2–4 | 4–8 | **$20–$40** | Buy | **VERIFIED** | |
| **Belt / pulley for belt indexer** | goBILDA | 5 mm HTD Starter Pack (8 mm REX) **$209.99** | 0–1 shared | **0–1 shared** | $210 | Buy | **CROSS-REF** — `VENDOR-ECOSYSTEMS.md` §6.4 | One pack serves both robots and the whole robot's belt needs. |
| Chain + sprockets (belt alternative) | goBILDA | Chain `3308-0008-1000` **$11.99**; sprockets `3311-0014-0016/-0020` **$2.29–$4.79** | 1 set | 2 sets | ≈ $40 | Buy | **CROSS-REF** | |
| **Element-presence sensor** | REV | Through-bore / distance sensors — see `LEGAL-PARTS-CONSTRAINTS.md` §5.4 | 1–2 | **2–4** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🔴 **The highest-value sensor on a launcher robot.** Lets software know an element is staged. See §12.3. |
| Shaft / bearings / hubs | goBILDA | 8 mm REX, `1611`, pillow blocks | 1 set | 2 sets | ≈ $35 | Buy | **CROSS-REF** | |
| Polycarbonate / PETG for the channel | any VENDOR | sheet stock | share | share | ≈ $15 | Buy (raw material) | **UNVERIFIED** | **R302** raw material. |

#### FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours |
|---|---|---|---|---|---|
| 🟢 **Serpentine tube / single-file channel** | 3D print in sections, bolt together | **PETG**, sanded inside | 1 | 2 | **4–7 h** (iterate width!) |
| **Star wheel with element pockets** | 3D print, high infill | PETG / nylon | 0–1 | 0–2 | **3–5 h** |
| **Shroud around the star wheel** | 3D print or bent polycarb | PETG / polycarb | 0–1 | 0–2 | **2–3 h** |
| **Entry taper (hopper → single file)** | 3D print | PETG | 1 | 2 | 🔴 **3–5 h — highest-iteration part** |
| Channel lid (clear, for debugging) | Cut polycarbonate | **Clear polycarb** | 1 | 2 | **1–2 h** |
| Sensor mounts | 3D print | PETG | 1–2 | 2–4 | **1 h** |
| **Total** | | | | | **≈ 14–23 h per robot** |

🔴 **Print the channel in at least three widths.** The correct internal width depends on the actual element,
which you will not have until kickoff. Design the channel as a **parametric model with width as a variable**
before kickoff, so on kickoff evening you change one number and start three prints. **This is the single
most useful pre-kickoff CAD task in this entire file.**

#### Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Indexer motor (Core Hex) | $32.00 | $64.00 |
| Rollers (share of one 8-pk) | ≈ $7 | $12.99 |
| Shaft, bearings, hubs | ≈ $35 | ≈ $70 |
| Presence sensor | ≈ $25 | ≈ $50 |
| Sheet stock | ≈ $15 | ≈ $30 |
| **COTS subtotal** | **≈ $114** | **≈ $227** |
| Filament (incl. 3 channel iterations) | ≈ $30 | ≈ $55 |
| **Total materials** | **≈ $144** | **≈ $282** |
| **Student-hours** | **14–23 h** | **20–34 h** |
| **R503 cost** | **1 motor** (**0** for a pure serpentine gravity tube) | |

#### Common failure modes and spares

| Failure | Cause | Fix | Spare |
|---|---|---|---|
| 🔴 **Double-feed** | Channel wider than **1.8 × element Ø**; shallow star pockets | Narrow the channel; deepen pockets; tighten the shroud | Narrower channel print |
| 🔴 **Jam at the entry taper** | Taper too abrupt | Lengthen the taper to ≥ 2× element Ø | Alternate taper print |
| Element sticks in the tube | Layer-line friction, tight bend | Sand; increase bend radius | Spare tube section |
| Star wheel loses position | No encoder, or set screws slipping | Core Hex encoder; **clamping hubs**; blue threadlocker | Spare hub |
| Indexer runs but launcher is not ready | No handshake between indexer and flywheel | **Gate the indexer on measured flywheel velocity** (§12.3) | — |
| Cannot see the jam | Opaque channel | **Clear polycarb lid** | — |
| Element retained powered-off (**R203**) | Closed channel with a servo gate | Gravity-openable path or removable lid | — |

**Spares for two robots:** 2 spare channel sections, 2 tapers, 1 star wheel, 4 rollers, 2 sensors. ≈ **$90.**

#### Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Mechanism | 🟢 **Gravity serpentine tube, no actuator** | Star-wheel indexer, Core Hex encoder, closed-loop pocket positioning |
| Capacity | 2–3 elements | 5+ |
| Sensing | None (driver watches) | Presence sensor + flywheel-ready handshake |
| Rate | ~0.5/s | 1.5–3/s |
| Cost per robot | ≈ $25 | ≈ $144 |
| **R503 cost** | 🟢 **0 motors, 0 servos** | 1 motor |

---

### 9.3 F3 — Kicker servo and gate (the final release)

#### What it is and when a design needs it

The last element in the chain: a servo-driven paddle, plunger or gate that pushes **one** staged element
into the launcher at a commanded instant. Needed whenever you want **shot-by-shot timing control** — which
is any flywheel launcher, because the element must not arrive until the wheel is at speed (§2.4, §12).

#### The main variants

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Notes |
|---|---|---|---|---|---|---|
| **Servo paddle kicker** | **2** | **2** | 2 | **4** | **4** | 🟢 The standard. Rotate in, rotate out. **1 servo slot.** |
| **Servo linear plunger** | 3 | 2 | 3 | 3 | 3 | Pushes straight; needs a linkage or linear servo. |
| **Linear servo** | 2 | 3 | 2 | 3 | 4 | Table 12-2 permits linear servos (**≤ 1 A @ 6V**). Clean but slow. |
| **Gate + gravity drop** | **1** | **1** | **1** | **4** | **5** | 🟢 Servo opens a gate, gravity does the work. Fewest moving parts. |
| **Continuous-rotation servo roller** | 2 | 2 | 3 | 3 | 4 | **R504.C** permits manufacturer-specified CR conversion. Meters elements by run time — less precise. |

#### 🔴 The power detail that makes kickers reliable

**CONFIRMED-BIOBUZZ — R502 blue box (V0 p. 76):**

> *"The REV Control Hub and REV Expansion Hub provide 5V to servos, and the goBILDA Servo Power Injector,
> REV Servo Power Module, Studica Servo Power Block, and REV Servo Hub provide 6V to servos. While
> virtually all servos are compatible with 6V, servos with an operating voltage range of 6-8.4 DCV, for
> example, may not work properly when only provided 5V."*

A kicker must move **fast and decisively**. A servo run at 5 V from the Hub is meaningfully slower and
weaker than the same servo at 6 V. **JUDGMENT: if your kicker feels sluggish, the fix is usually a 6 V
power injector, not a bigger servo** — and a bigger servo may fail the R502 8 W test anyway.

**Table 12-3 (CONFIRMED-BIOBUZZ, R505) — approved power regulating devices and per-port limits:**

| Power Regulating Device | Part Number | Load Limit per Device |
|---|---|---|
| goBILDA 6V Servo Power Injector | `3125-0001-0001` | 2 Servos per Port |
| REV Control Hub / Expansion Hub **motor** ports | `REV-31-1595` / `REV-31-1153` | 2 Motors per Port |
| REV Control Hub / Expansion Hub **servo** ports | `REV-31-1595` / `REV-31-1153` | 2 Servos per Port |
| REV Servo Power Module | `REV-11-1144` | 2 Servos per Port |
| REV Robotics Servo Hub | `REV-11-1855` | ⚠ text reads "2 Motors per Device" |
| REV SPARKmini | `REV-31-1230` | 2 Servos per Port |
| Studica Servo Power Block | `75005` | ⚠ no limit shown in the extracted text |

⚠ **EXTRACTION WARNING.** The two flagged rows are almost certainly **column-shift artifacts** in the
layout-preserving text dump — the same defect `LEGAL-PARTS-CONSTRAINTS.md` §0.3 warns about. A "Servo Hub"
with a *motor* limit is implausible. **Re-read Table 12-3 in the PDF before relying on those two rows.**

#### BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Kicker servo** | goBILDA | **2000 Series Dual Mode Servo — `2000-0025-0003`** | 1 | **2** | **$36.99 ea = $74** | Buy | **VERIFIED** — [product page](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/) | **$36.99 VERIFIED 2026-08-22** — this is the *25-3 Speed* variant, 9.3 kg·cm @ 6.0 V, 300° range. Legal by name. HISTORICAL DECODE specs 2.5 A / 2.65 W — comfortably inside R502. |
| Kicker servo, alternative | REV | **Smart Robot Servo — `REV-41-1097`** | 1 | 2 | **$25.50** | Buy | **CROSS-REF** — ⚠ **DISCONTINUED at REV** | Legal (Table 12-2). 13.5 kg·cm, 2 A stall. **Buy both robots' worth now if you want them.** |
| Kicker servo, high torque | AndyMark (official FIRST supplier) | **High-Torque Servo — `am-4954`** | 1 | 2 | not verified | Buy | **MANUAL-SOURCED** (Table 12-2) | AndyMark product pages did not resolve this session. **NEEDS-SKU-CHECK.** |
| Linear servo | Actuonix | **Micro Linear Servo — `P8-100-252-12-R`** | 0–1 | 0–2 | not verified | Buy | **MANUAL-SOURCED** (Table 12-2) | **≤ 1 A @ 6V class per Table 12-2.** Consumes a **servo** slot. |
| **6V servo power injector** | goBILDA | **6V Servo Power Injector — `3125-0001-0001`** (6-channel, 8–15 V in) | 0–1 | **0–2** | **$69.99 ea** | Buy | **VERIFIED** — [servo electronics](https://www.gobilda.com/servo-electronics/) | 🟢 **2 servos per port.** The fix for a sluggish kicker. |
| Servo power module | REV | **Servo Power Module — `REV-11-1144`** | 0–1 | 0–2 | NEEDS-SKU-CHECK | Buy | **MANUAL-SOURCED** (Table 12-3) | 2 servos per port. |
| **Servo programmer (bench tool, NOT on the robot)** | goBILDA | **2000 Series Servo Programmer — `3102-0001-0001`** | — | **1 per program** | **$12.99** | Buy | **CROSS-REF** (VERIFIED in `LEGAL-PARTS-CONSTRAINTS.md` §4.5) | 🟢 **R504.C** permits manufacturer-specified servo modification — setting soft limits and CR conversion. **Buy one for the whole program, not one per robot.** |
| Servo horns / hubs | goBILDA | Servo hubs (H25T 25-tooth) | 1–2 | 2–4 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** — [hubs](https://www.gobilda.com/hubs/) | |
| **Servo connector clips (6-pk)** | goBILDA | **`2917-0001-0001`** | 1 | **2** | **$5.99 ea = $12** | Buy | **CROSS-REF** — VERIFIED | 🟢 **Stops the #1 cause of "the servo just stopped working."** Buy these. |
| Servo extension cables (TJC8) | goBILDA | Wiring → TJC8 Servo category | 2 | 4 | NEEDS-SKU-CHECK | Buy | **CROSS-REF** — VERIFIED category | |

#### FABRICATE / ASSEMBLE IN-HOUSE

| Fabricated item | Method | Material | Per robot | For 2 | Student-hours |
|---|---|---|---|---|---|
| **Kicker paddle / plunger face** | 3D print, **TPU contact face** | PETG body + **TPU face** | 1 | 2 | **2–4 h** |
| Kicker mount / servo bracket | 3D print or drilled plate | PETG / aluminium | 1 | 2 | **1–2 h** |
| **Staging pocket** (holds exactly one element in place) | 3D print | PETG | 1 | 2 | 🔴 **3–5 h — geometry-critical** |
| Gate flap (gate variant) | 3D print + TPU lip | PETG + TPU | 0–1 | 0–2 | **2–3 h** |
| Linkage (plunger variant) | Print + ball links | PETG + **R303.L** COTS rod ends | 0–1 | 0–2 | **2–3 h** |
| **Total** | | | | | **≈ 6–14 h per robot** |

**Material guidance (JUDGMENT):** put **TPU on every surface that touches an element** — it grips gently,
does not mark (**R201**), and absorbs the impact that would otherwise crack a PETG paddle. The kicker
paddle is a **high-cycle** part: it moves once per shot, thousands of times per season. Print it solid
(≥ 60 % infill) and **keep two spares per robot in the pit kit**.

#### Approximate subtotal

| Line | Per robot | For 2 robots |
|---|---|---|
| Kicker servo (`2000-0025-0003`) | **$36.99** | **$73.98** |
| Servo horn/hub, clips, cable | ≈ $15 | ≈ $30 |
| 6V injector (optional) | **$69.99** | **$139.98** |
| Servo programmer | — | **$12.99 (program-wide)** |
| **COTS subtotal** | **≈ $52–$122** | **≈ $117–$257** |
| Filament | ≈ $10 | ≈ $20 |
| **Total materials** | **≈ $62–$132** | **≈ $137–$277** |
| **Student-hours** | **6–14 h** | **9–20 h** |
| **R503 cost** | **0 motors + 1 servo** | |

#### Common failure modes and spares

| Failure | Cause | Fix | Spare |
|---|---|---|---|
| 🔴 **Kicker fires before the flywheel is ready** | No velocity handshake | **Gate the kick on measured RPM within tolerance** (§12.3) | — (software) |
| 🔴 **Kicker pushes two elements** | Staging pocket holds more than one | Tighten the pocket to element Ø + 2–3 mm | Alternate pocket print |
| Servo too slow, element dribbles in | 5 V supply; servo undersized | **6 V injector**; faster servo within R502 | Injector |
| Paddle cracks | High-cycle PETG at low infill | ≥ 60 % infill; TPU face | **2 spare paddles per robot** |
| Servo horn slips on the spline | Loose horn screw | Threadlocker; correct horn | Spare horns |
| **Servo disconnects mid-match** | Connector vibration | 🟢 **Servo connector clips `2917-0001-0001`** | Clips |
| Servo drifts out of calibration | Soft limits lost | Re-set with the programmer (**R504.C**) | Programmer |
| Element retained powered-off (**R203**) | Kicker blocks the only exit | Design a gravity or manual egress path | — |

**Spares for two robots:** 4 paddles, 2 pockets, 2 horns, 1 spare servo, clips. ≈ **$60.**

#### Rookie-friendly minimum vs. competitive version

| | **Rookie-friendly minimum** | **Competitive version** |
|---|---|---|
| Mechanism | Servo paddle, PETG, on a button | Servo paddle, TPU face, 6 V injector |
| Timing | Driver presses when it sounds right | **Automatic: velocity-gated, sensor-confirmed, one press = one shot** |
| Sensing | None | Element-presence sensor + flywheel ready flag |
| Rate | ~0.3/s | 1.5–3/s |
| Cost per robot | ≈ $40 | ≈ $80 |

---

## 10. AIMING — fixed, adjustable hood, or turret

### 10.1 The three strategies compared

| Strategy | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | R503 cost |
|---|---|---|---|---|---|---|
| 🟢 **A1 — Fixed angle, drive to a position** | **1** | **1** | **2** | **5** | **5** | **0 + 0** |
| **A2 — Adjustable hood (variable angle)** | 3 | 2 | **4** | 3 | 3 | **0 + 1 servo** |
| **A3 — Turret (rotating launcher)** | **5** | **5** | **5** | 2 | **1** | **1 motor** (+ often 1 servo) |

### 10.2 A1 — Fixed angle and drive to position

**What it is:** the launcher geometry never changes. The robot drives to a known spot on the FIELD and
shoots. Range is set by *where you park*, not by what you tune.

🟢 **JUDGMENT — this is the correct choice for this program, and it is not a compromise.**
`ROBOT-ARCHETYPE-LIBRARY.md` §3.3 reaches the same conclusion independently, listing the launcher as
A-team-suitable **"with one exception — a fixed-geometry, drive-to-a-spot launcher with no turret"** being
the B-team-viable form.

**Why it wins for a two-robot program:**

- **One shot solution to tune, not a continuous function.** You calibrate one RPM at one distance. A
  variable-range launcher requires a whole distance→RPM curve (§12.2).
- **It duplicates perfectly.** The geometry is fixed and physical; robot B gets the same printed parts and
  the same single number.
- **It costs zero R503 slots.** In a season where 8 motors disappear fast (§15), this matters enormously.
- **The driver skill transfers.** Parking on a spot is a learnable, practisable skill — and driver practice
  is the cheapest performance available to a 15-student program.

**Sensing it implies:** essentially none. A floor mark, a wall, or a physical alignment feature is enough.
If you want repeatability, add **odometry or an AprilTag pose fix** to drive to the spot automatically.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Dead-wheel odometry (optional) | goBILDA | Odometry pods — **R303.J** explicitly permits COTS dead-wheel odometry kits | 0–1 set | 0–2 sets | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🔴 `3624-4008-0032` (32 mm omni, the classic pod wheel) was **OUT OF STOCK** in the Phase A check — verify. |
| Alignment feature (physical) | — | — | 1 | 2 | ~$0 | **Fab** | **JUDGMENT** | A printed bumper stop that indexes off a FIELD wall is free, legal under R302, and beats sensors. |

**Fabrication:** essentially none beyond the launcher itself. **0–2 student-hours.**

### 10.3 A2 — Adjustable hood

**What it is:** a servo tilts the hood (or the whole launcher) to change launch angle, letting one RPM
serve several distances — or letting you trade angle against speed.

**When a design needs it:** when the game forces shooting from a **range of distances** you cannot control,
and where driving to a fixed spot is contested or too slow.

🔴 **The tuning cost is the real price.** An adjustable hood converts one calibration point into a
**two-variable surface** (angle × RPM → range). You must characterize it, and you must characterize it
**twice, once per robot.** See §12.2.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Hood servo** | goBILDA | 2000 Series Dual Mode Servo — `2000-0025-0003` | 1 | **2** | **$36.99 ea = $74** | Buy | **VERIFIED** — [product page](https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/) | **$36.99 VERIFIED 2026-08-22** — *25-3 Speed*, 9.3 kg·cm @ 6.0 V, 300° range. Must hold position against the hood load. |
| Hood servo, alternative | REV | Smart Robot Servo — `REV-41-1097` | 1 | 2 | **$25.50** | Buy | **CROSS-REF** — ⚠ DISCONTINUED | |
| Linear servo (fine angle control) | Actuonix | `P8-100-252-12-R` | 0–1 | 0–2 | not verified | Buy | **MANUAL-SOURCED** (Table 12-2) | ≤ 1 A @ 6V. |
| **Ball-joint linkage / rod ends** | goBILDA | Ball joint linkages | 2 | 4 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🟢 **R303.L** explicitly permits COTS *"items that connect structures at variable angles (such as ball joint linkages, rod ends…)"*. |
| Hood pivot bearings | goBILDA | `1601` / `1611` flanged bearings | 2 | 4 | ≈ $8–$24 | Buy | **CROSS-REF** | |
| 6V servo power injector | goBILDA | `3125-0001-0001` (6-channel, 8–15 V in) | 0–1 | 0–2 | **$69.99 ea** | Buy | **VERIFIED** — [servo electronics](https://www.gobilda.com/servo-electronics/) | Helps the servo hold under load. |

**FABRICATE:** pivoting hood (**4–7 h**), pivot mounts (**2–3 h**), servo linkage bracket (**1–2 h**),
**angle witness scale printed onto the side plate** (**1 h** — 🟢 do this; it is how robot B gets set to
match robot A). **Total ≈ 8–13 h per robot.**

**Subtotal:** COTS ≈ **$72/robot, $144 for two**; +filament ≈ $15/robot. **R503 cost: 1 servo.**

**Failure modes:** servo cannot hold angle under recoil (add a linkage with mechanical advantage, or a
detent); angle drifts between matches (add a hard stop at each used position); **the two robots' angle
scales disagree** (🔴 witness-mark both, and record angle in *encoder counts*, not degrees).

### 10.4 A3 — Turret

**What it is:** the launcher rotates independently of the chassis, so the robot can shoot while moving or
without aiming the whole drivetrain.

🔴 **JUDGMENT — do not build a turret in this program.** Stated bluntly because it is the most seductive
mechanism in FTC and the one most reliably fatal to a small team's season. The reasons:

1. **It costs an R503 motor slot** you almost certainly need elsewhere (§15).
2. **It requires continuous closed-loop position control** *plus* the flywheel's velocity control *plus*
   vision, all working together, all the time.
3. **Wire management across a rotating joint** is a hard mechanical problem (slip rings are not on the
   legal parts list; you end up with a limited-rotation cable service loop and a software rotation limit).
4. 🔴 **It scores duplicability 1.** Two turrets, each with its own zero offset, backlash, and vision
   calibration, is not "build it twice" — it is **build two different robots**.
5. **R303 forbids buying one.** *"COTS COMPONENTS and MECHANISMS must not exceed a single degree of
   mechanical freedom"* — a bought pan-tilt assembly is illegal. A COTS **turntable** is explicitly allowed
   (R303.E) as a single-DoF item, but you fabricate everything above it.
6. **R202.I** — a rotating mechanism with a cable loop is an entanglement-risk review item.

If a turret is genuinely required by the kickoff game, it belongs on **one robot (the A team's) only**, and
the B team should run the fixed-angle version (§10.2). **Do not attempt two.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Turret motor** | REV | **Core Hex `REV-41-1300`** — 125 RPM, 3.2 N·m, 288 CPR | 1 | 2 | **$32.00 ea** | Buy | **CROSS-REF** | High reduction + encoder = the right turret motor. **Costs 1 R503 motor slot.** |
| **Turntable / lazy susan bearing** | goBILDA | Turntable products | 1 | 2 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🟢 **R303.E** explicitly names "turntable" as an allowed single-DoF COTS mechanism. |
| Drive ring / large sprocket | goBILDA | `3310-0032-0070` 70 T aluminium hub-mount **$18.99** | 1 | 2 | **$38** | Buy | **CROSS-REF** — VERIFIED | Large reduction to the turret ring. |
| Pinion sprocket | goBILDA | `3312-4008-0008` 8 T press-fit 8 mm REX **$4.99/2-pk** | 1 | 1 pk | **$4.99** | Buy | **CROSS-REF** — VERIFIED | |
| Chain | goBILDA | `3308-0008-1000` **$11.99** | share | 1 | **$12** | Buy | **CROSS-REF** — VERIFIED | |
| Cable carrier chain | goBILDA | `2924-1015-1000` (1 m) **$19.99** | 1 | 2 | **$40** | Buy | **CROSS-REF** — VERIFIED | For the rotating service loop. |
| Absolute position sensor / limit switch | REV | see `LEGAL-PARTS-CONSTRAINTS.md` §5.4 | 1–2 | 2–4 | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🔴 A turret **must** know its zero at init. |

**FABRICATE:** turret deck (**5–8 h**), bearing/ring mounts (**3–5 h**), cable service loop guide
(**2–4 h**), hard rotation stops (**1–2 h**). **Total ≈ 11–19 h per robot** — *plus* everything in §3 or §4
riding on top of it.

**Subtotal:** COTS ≈ **$150/robot, $300 for two**. **R503 cost: 1 motor** (+1 servo if the hood also adjusts).

### 10.5 The sensing each strategy implies

> **Cross-reference the electronics catalog** for full sensor coverage and legality:
> `reference/LEGAL-PARTS-CONSTRAINTS.md` §5.4 (Sensors, cameras and coprocessors — R702, R707, R708).

| Aiming strategy | Minimum sensing | Better sensing | Notes |
|---|---|---|---|
| **A1 Fixed** | 🟢 **None** — a floor mark | IMU heading + odometry to auto-drive to the spot | The reason A1 is cheap in *every* dimension |
| **A2 Adjustable hood** | Servo position (open-loop) | Distance estimate (vision or range sensor) → angle lookup | Needs a distance measurement to be worth anything |
| **A3 Turret** | Encoder + zero limit switch | **Vision target tracking, closed-loop** | Cannot work well without vision |

#### 🔴 The vision constraint you must know before designing any of this

**CONFIRMED-BIOBUZZ — R702 and Table 12-9.** Programmable vision coprocessors may be reprogrammed only if
natively supported by the FTC SDK, and **Table 12-9 lists exactly one device:**

| Device | Part Number |
|---|---|
| **Limelight Vision Limelight 3A** | **`LL_3A`** |

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Limelight 3A smart camera** | Limelight Vision (general supplier); also stocked by AndyMark (**official FIRST supplier**) | **Limelight 3A — `LL_3A`** | 0–1 | **0–2** | **$189.00 ea = $378** | Buy | **VERIFIED** — [product page](https://limelightvision.io/products/limelight-3a) | 🔴 **The only device in Table 12-9.** Has **REV and goBILDA threaded mounting**. ⚠ Vendor page states: *"The REV Control Hub can only support a single LL3A at this time."* VERIFY-BEFORE-ORDER. |
| Webcam (SDK-supported UVC) | various | standard UVC webcam | 0–1 | 0–2 | ≈ $30–$70 | Buy | **CROSS-REF** — see `LEGAL-PARTS-CONSTRAINTS.md` §5.4 | 🟢 A plain webcam running AprilTag detection **on the Control Hub** avoids R702 entirely and costs a fifth as much. |

🔴 **$378 for two Limelights is a serious line item for a modest budget** — roughly the cost of an entire
fixed-angle launcher on both robots (§3.5). **JUDGMENT: for this program, try the webcam + Control Hub
AprilTag path first.** Buy Limelights only if you have measured that on-Hub vision is too slow for your
aiming loop, and even then consider **one** for the A team.

**R202.F caution:** *"high intensity light sources used on the ROBOT should only be illuminated for a brief
time while targeting and may invite additional scrutiny."* If you use active illumination for vision,
**strobe it only during targeting**, not continuously. Also **R202.C** — no imagery on the robot that
mimics 36h11 AprilTags.

---

## 11. Fabrication guide — materials, tooling, student-hours

**CONFIRMED-BIOBUZZ — R302:** *"Allowed raw materials and legal COTS parts can be modified (drilled, cut,
painted, etc.) as long as no other rules are violated."* Raw materials explicitly include **sheet stock,
extruded shapes, metals, plastic, rubber, wood, and magnets.** Everything in this section is sanctioned.

**CONFIRMED-BIOBUZZ — R301:** you may **not** buy a COTS MAJOR MECHANISM purpose-built for a game task.
**A launcher is therefore, by rule, a fabricated mechanism.** There is no shortcut to buy your way out of
this section.

### 11.1 Material selection matrix

| Part | First choice | Acceptable | 🔴 Avoid | Why |
|---|---|---|---|---|
| **Hood / guide surface** | Heat-bent **polycarbonate** 1/16 in. | **PETG** print, sanded | **PLA** | Smooth continuous curve; layer lines scuff elements (**R201**) |
| **Side plates** | **Polycarbonate** or 1/8 in. aluminium | PETG print ≥ 40 % infill | PLA, acrylic | Must hold shaft alignment under vibration |
| **Hopper walls** | **Polycarbonate** (≥ 1 wall **clear**) | PETG print | 🔴 **Acrylic — shatters** | Impact survival + jam visibility |
| **Serpentine / indexer channel** | **PETG**, sanded inside | Polycarb + printed ends | PLA | Low friction, tough |
| **Catapult sear / latch** | **Nylon** or PETG ≥ 80 % infill | — | 🔴 **PLA — cracks** | Full stored energy as impact, every shot |
| **Catapult arm** | **Aluminium bar** | PETG ≥ 60 % infill | PLA | Stiffness sets launch-angle repeatability |
| **Kicker paddle** | **PETG ≥ 60 %** + **TPU face** | — | PLA | High-cycle impact part |
| **Any element-contacting surface** | 🟢 **TPU** | Adhesive foam | Bare printed PETG | Protects elements (**R201**), grips gently |
| **Guards / covers** | Polycarbonate | PETG | Acrylic | **R202.I** entanglement |
| **Spacers, brackets, mounts** | PETG | PLA (low-load only) | — | |

🔴 **Acrylic is banned by good sense, not by rule.** It shatters into fragments on FIELD contact — an
**R201** "making a mess" risk and a safety problem. **Polycarbonate costs slightly more and never does this.**

### 11.2 Tooling required (matches this program's stated capability)

| Tool | Have it? | Used for |
|---|---|---|
| **3D printer(s)** | ✅ assumed | Hoods, side plates, channels, pockets, paddles, sears |
| **Hand drill + step bits** | ✅ assumed | Polycarb and aluminium holes |
| **Jigsaw / coping saw / shears** | ✅ assumed | Cutting polycarbonate sheet |
| **Heat gun** | ⚠ **buy one if absent (~$25)** | 🟢 Bending polycarbonate hoods — the single best fabrication upgrade for this mechanism family |
| **Feeler gauges** | ⚠ **buy (~$10)** | 🔴 **Setting identical nip gaps / compression on BOTH robots** (§13) |
| **Digital calipers** | ⚠ **buy (~$25)** | Measuring the element on kickoff day; every channel width decision |
| **Tachometer or encoder telemetry** | ✅ (encoders) | Verifying flywheel RPM |
| **CNC mill** | ❌ **not available** | Not required by anything in this file — **by design** |

🟢 **Nothing in this catalog requires a mill.** Every mechanism here is achievable with printers, a heat
gun, a drill and hand tools. That is deliberate.

### 11.3 The two-robot printing discipline

> **`VENDOR-ECOSYSTEMS.md` §6.7 states the rule this program should already be following:**
> *"every print job runs qty 2, immediately. A part printed once is a part robot B doesn't have."*

For launchers specifically, extend it:

| Rule | Why |
|---|---|
| 🔴 **Print qty 2 of every part, same printer, same filament spool, same slicer profile** | Different printers give different tolerances; a 0.3 mm difference in a nip gap is a different shooter |
| 🔴 **Print qty 4 of sears, paddles and channel sections** | These are the consumables; 2 for the robots, 2 for the pit kits |
| **Record the slicer profile in the build log** | So a mid-season reprint matches the original |
| **Never "just tweak" one robot's part** | If you change robot A's hood, reprint robot B's the same day, or you now maintain two designs |

### 11.4 Student-hour rollup by mechanism

| Mechanism | Hours, robot A | Hours, robot B | **Program total** |
|---|---|---|---|
| §3 Single flywheel | 11–21 | 5–9 | **16–30** |
| §4 Dual flywheel | 11–19 | 7–11 | **18–30** |
| §5 Catapult | 15–26 | 7–12 | **22–38** |
| §6 Slingshot | 7–13 | 3–5 | **10–18** |
| §8 Ramp / deposit | 9–15 | 4–7 | **13–22** |
| §9.1 Hopper + agitator | 12–19 | 6–9 | **18–28** |
| §9.2 Indexer | 14–23 | 6–11 | **20–34** |
| §9.3 Kicker | 6–14 | 3–6 | **9–20** |
| §10.2 Fixed aiming | 0–2 | 0–1 | **0–3** |
| §10.3 Adjustable hood | 8–13 | 4–6 | **12–19** |
| §10.4 Turret | 11–19 | 🔴 *don't* | **11–19 (one robot only)** |

🔴 **The number that should stop you:** a **complete flywheel launcher robot** — flywheel + hopper +
indexer + kicker + fixed aiming — is **63–108 student-hours across two robots**, *excluding* the
drivetrain, electronics, programming, and the portfolio. Add the programming in §12 and it is the
**dominant cost of your season.**

---

## 12. The tuning burden, quantified — what a launcher demands of your programmer

> 🔴 **The headline, stated as bluntly as the brief demands: a flywheel shooter is CHEAP TO BUILD and
> EXPENSIVE TO MAKE REPEATABLE.** The parts in §3 total about **$135 per robot**. The software and
> calibration that turn those parts into points cost **40–80 programmer-hours** and are the reason
> `ROBOT-ARCHETYPE-LIBRARY.md` §3.3 scores this archetype **programming load 4** and **tuning burden 5**.

### 12.1 What "velocity control" actually requires

Open-loop power (`motor.setPower(0.7)`) **does not work** for a launcher. Here is why, concretely:

| Disturbance | Effect on shot | Magnitude |
|---|---|---|
| **Battery voltage sag** over a match (12.5 V fresh → ~11.5 V late) | Same power command → **lower RPM → shorter shot** | 🔴 **~8 % RPM, easily a miss** |
| **Shot-to-shot energy loss** | Each shot drains the flywheel (§2.4) | **11–21 % RPM drop per shot** |
| **Motor warming** over a match | Resistance rises, torque falls | few % |
| **Compliant wheel wear** over a season | Effective radius shrinks, grip changes | few %, drifting |
| **Different battery between matches** | Different starting voltage | several % |

**The fix is closed-loop velocity control:**

1. Read the encoder velocity (Yellow Jacket and Core Hex both have built-in encoders).
2. Run **PIDF** — and note that **F (feedforward) does most of the work** on a flywheel. A well-chosen F
   term gets you to roughly the right speed; PID only rejects the disturbance.
3. **Gate firing on measured velocity being inside a tolerance band** (§12.3).

🔴 **The single most common software mistake:** tuning PID with a large P and no F. A flywheel is a
high-inertia, low-friction integrator — large P causes oscillation that never settles, and the shot
scatters worse than open-loop. **Tune F first, with P = I = D = 0.**

### 12.2 The calibration work, in hours

| Task | Hours (robot A) | Hours (robot B) | Notes |
|---|---|---|---|
| Wire encoder, verify counts and direction | 2 | 1 | |
| Get velocity telemetry readable and logged | 3 | 1 | Shared code |
| **Tune F, then P/I/D to a stable setpoint** | **6–12** | **3–6** | 🔴 Not shared — **each robot's mechanism differs** |
| Determine ready-band tolerance + recovery wait | 3–5 | 2–3 | |
| **Build the distance→RPM table** (fixed angle: 1 point; variable: a curve) | **4–20** | **3–15** | 🔴 The range that separates A1 from A2/A3 aiming |
| Integrate kicker/indexer handshake | 4–8 | 2–4 | |
| Venue re-calibration (per event) | 1–2 **per event** | 1–2 **per event** | §12.4 |
| **Total, season** | **22–50 h** | **12–30 h** | **🔴 34–80 programmer-hours across the program** |

**JUDGMENT:** with ~15 students across two teams, you likely have **1–3 capable programmers total**. A
launcher will consume **most of one programmer's season.** That programmer will then not be writing your
autonomous. Decide that trade deliberately.

🟢 **The A1 (fixed-angle) saving is enormous and worth restating:** a fixed-angle launcher needs **one**
calibration point. An adjustable-hood or turret launcher needs a **curve or surface**, measured at 5–10
distances, **twice** (once per robot), and **re-measured whenever anything changes.** That is the entire
difference between the 4-hour and 20-hour rows above.

### 12.3 The three software gates that make a launcher work

Implement all three or the mechanism will disappoint:

| Gate | Rule | Why |
|---|---|---|
| 1. **Ready gate** | Do not fire unless `\|measured_RPM − target_RPM\| < tolerance` | Prevents the classic "first shot short" (§3.6) |
| 2. **Recovery gate** | After a shot, wait until the ready gate re-satisfies before the next feed | Prevents shot 2 landing short (§2.4) |
| 3. **Presence gate** | Do not fire unless a staged element is detected | Prevents dry-fire and double-feed masking |

**JUDGMENT — set the ready tolerance to ±1 % of setpoint to start**, then widen it only if cycle time is
unacceptable. Widening the tolerance is exactly the trade of **accuracy for rate**, and you should make it
knowingly, with a number.

### 12.4 🔴 The R704 problem — why launcher tuning is expensive in a way that surprises teams

**CONFIRMED-BIOBUZZ — R704.C:** *"Ensure all programming laptops and other devices (other than the DRIVER
STATION device) are disconnected from the ROBOT CONTROLLER Wi-Fi network during MATCH play."*

**Consequences you must plan around:**

- **You cannot watch flywheel telemetry during a real match.** No live graph, no dashboard, no live PID edit.
- **You cannot tune between matches on the FIELD.** Tuning happens in the pit, on a practice FIELD if the
  venue has one, or not at all.
- **Therefore: log to the Driver Station / on-Hub storage, and review after the match.** Build this in from
  the start. A launcher without post-match logging is a launcher you cannot debug at an event.
- **Therefore: every shot parameter must be adjustable from the DRIVER STATION**, not from a laptop —
  a gamepad-adjustable RPM trim, or a small set of pre-set distances the driver selects.

🟢 **JUDGMENT — build a "shot calibration table" as a physical artifact.** A laminated card per robot
listing distance → RPM → observed hit rate, updated at every practice and event. This is also
**precisely the evidence the Control Award asks for** — `ROBOT-ARCHETYPE-LIBRARY.md` §3.3 and the award
matrix both flag *"shot-calibration table (distance vs. flywheel RPM vs. hit rate) logged per venue"* as
the Control Award artifact for this archetype. **The tuning burden and the award submission are the same work.**

### 12.5 Venue variance — the cost nobody budgets

**HISTORICAL / JUDGMENT.** The same robot shoots differently at different venues: floor flatness, tile
seams, target manufacturing tolerance, and even air temperature affect the result. Budget **1–2 hours of
re-calibration per robot per event**, and **arrive at every event expecting to re-shoot the table.**

🔴 **`ROBOT-ARCHETYPE-LIBRARY.md` §3.3 puts it in one line: *"A launcher without a practice target is not
a strategy."*** If you cannot build a full-size replica target to practise against, **do not build a
launcher.** This is a genuine gate question for this program: a practice target costs money, space and
build hours that are not in any table above.

---

## 13. The duplicability problem — two flywheels that behave identically

> **This section exists because duplicability is a first-class factor in this workspace, and because the
> launcher is the mechanism where it hurts most.**

### 13.1 The core claim, stated plainly

🔴 **Two flywheel shooters tuned to behave identically is materially harder than one — and the difficulty is
not in the building, it is in the calibrating.**

Building the second one is *easy*: print the same files, buy the same parts, bolt it together. **That is
the trap.** Two mechanically identical launchers will still shoot differently, because:

| Divergence source | Typical magnitude | Copyable? |
|---|---|---|
| **Compliant wheel durometer batch variation** | small but real | ❌ Not without measuring |
| **Compression / nip gap set by hand** | 🔴 **0.5–1 mm easily** | ⚠ Only with feeler gauges |
| **Printed hood dimensional variation** (printer, spool, temperature) | 0.2–0.5 mm | ⚠ Same printer + profile helps |
| **Motor-to-motor free speed tolerance** | few % | ❌ Absorbed by closed-loop control |
| **Battery health difference between robots** | 🔴 several % of RPM | ✅ Absorbed by closed-loop control |
| **Wheel wear rate** (different practice hours) | drifts apart all season | ❌ Diverges continuously |
| **PIDF constants** | — | ⚠ Similar, but **must be verified per robot** |

### 13.2 Duplicability scores, ranked

| Mechanism | Duplicability | Why |
|---|---|---|
| 🟢 **Ramp / deposit (§8)** | **5** | No tuning exists. Geometry is the whole mechanism. |
| 🟢 **Serpentine indexer (§9.2)** | **5** | Physical width. Copy the file, copy the behaviour. |
| 🟢 **Fixed-angle aiming (§10.2)** | **5** | One number per robot. |
| **Catapult (§5)** | **4** | Energy is spring choice + geometry — **physically measurable and copyable**. |
| **Single flywheel (§3)** | **4** | One velocity loop per robot; geometry is single-sided so alignment is easier. |
| **Kicker servo (§9.3)** | **4** | Positions are servo angles; record them. |
| **Hopper + agitator (§9.1)** | **3** | Flow behaviour is emergent and sensitive to surface finish. |
| **Adjustable hood (§10.3)** | **3** | A calibration *curve* per robot, not a point. |
| 🔴 **Dual flywheel (§4)** | **2** | Two shafts to keep parallel, two velocity loops, **four PIDF tunings across the program**. |
| 🔴 **Turret (§10.4)** | **1** | Two zero offsets, two backlash profiles, two vision calibrations. Effectively two different robots. |

### 13.3 The duplicability protocol — do these seven things or accept divergence

1. 🔴 **Feeler-gauge the compression/nip gap on both robots** and write the number in both build logs.
   This is the highest-value 10 minutes in the whole build.
2. 🔴 **Same printer, same spool, same slicer profile, printed back-to-back**, for every launcher part.
3. **Witness-mark every adjustable position** (hood angle, stop position, compression slot) with a scribed
   or printed line, so a knocked adjustment is visibly wrong.
4. **Buy compliant wheels in one order, from one batch**, and assign them in matched pairs.
5. **Tune each robot's PIDF separately, and record both sets in the build log.** Do not assume they copy.
   Start robot B from robot A's constants, then verify.
6. **Maintain one shot-calibration table per robot** (§12.4). They will not be the same table. That is
   expected and fine — what is not fine is having only one and assuming it applies to both.
7. **Rotate practice hours evenly** so the wheels wear at similar rates, or replace both wheels together.

### 13.4 The honest framing for the A/B split

| Approach | Verdict |
|---|---|
| Both robots run the **same launcher design** | 🟢 **Correct**, and the protocol above makes it work. Parts, spares and knowledge are shared. |
| Both robots run the **same launcher, differently tuned** | 🟢 **Expected.** Two calibration tables is normal, not failure. |
| A team runs a launcher, **B team runs a deposit (§8)** | 🟢 **Often the best answer.** B gets a reliable scorer; A gets the ambitious one; spares still partly shared. |
| A team runs a **turret**, B team runs a fixed launcher | ⚠ Acceptable **only** if the game demands a turret. Little sharing. |
| 🔴 **Both robots run turrets** | ❌ **Do not.** |

---

## 14. Blunt assessment — is a launcher a good choice for a ~15-student two-robot program?

**JUDGMENT throughout. The brief asked for bluntness, so here it is.**

### 14.1 The verdict

> 🔴 **A launcher is a DEFENSIBLE choice for the A team and a BAD choice for the B team, and it is only
> defensible at all if three specific conditions hold. If you cannot tick all three on kickoff day, build
> the deposit mechanism (§8) on both robots and spend the savings on drivetrain and driver practice.**

### 14.2 The three gate conditions

| # | Condition | If false |
|---|---|---|
| **1** | 🔴 **The kickoff point table pays MORE for a launched element than for one you can drive up and deposit.** | Build §8. A launcher that scores the same as a ramp is pure downside. |
| **2** | 🔴 **You can build or borrow a FULL-SIZE PRACTICE TARGET.** | Do not build a launcher. You cannot calibrate what you cannot shoot at (§12.5). |
| **3** | 🔴 **You have a programmer who can own closed-loop velocity control for the season (34–80 h).** | Build §5 (catapult) or §8. A launcher without velocity control is a random number generator. |

### 14.3 The case against, honestly stated

- **It consumes your best programmer.** 34–80 programmer-hours across two robots (§12.2), and with 1–3
  capable programmers total, that is most of one person's season. Your autonomous will suffer.
- **It consumes R503 slots you need.** A flywheel + intake + transfer + hopper agitator is **4 motors**
  before the drivetrain. A 4-motor holonomic drive then puts you at **8/8 with no endgame mechanism**
  (§15). This is the most common way a launcher design dies.
- **Duplicability 2–4, and the pain is invisible until late.** The second launcher builds fast and
  calibrates slow. Teams discover this in week 8, not week 3.
- **The feeder, not the launcher, will define your season** — and it is the part nobody is excited to
  build (§9).
- **Venue variance is real** and costs 1–2 h per robot per event, forever (§12.5).
- **`ROBOT-ARCHETYPE-LIBRARY.md` scored this archetype 2.63**, well below the ground-intake cycler at 3.63.
  That scoring was done independently of this file and reached the same conclusion.

### 14.4 The case for, honestly stated

- 🟢 **It is genuinely cheap in parts.** ~$135/robot for a single flywheel (§3.5). The cost is time, not money.
- 🟢 **R801's explicit flywheel carve-out means zero legality risk.** You will not be surprised at inspection.
- 🟢 **The fixed-angle version (A1) removes most of the tuning burden** and is legitimately B-team-viable.
- 🟢 **The tuning work IS the Control Award submission** (§12.4). You are paid twice for the same effort —
  and for a program that values judged awards, this is a real argument.
- 🟢 **`ROBOT-ARCHETYPE-LIBRARY.md` §3.3:** *"When the game pays for a repeatable one-shot, the launcher is
  correctly priced and worth building."*

### 14.5 The recommended posture on kickoff day

| Priority | Action |
|---|---|
| 1 | **Measure the element** (calipers, scale) and **recompute §2.4** with the real mass. |
| 2 | **Check gate conditions §14.2.** Be honest. All three, or build §8. |
| 3 | If launching: 🟢 **both robots build the SAME single-flywheel, fixed-angle, serpentine-fed design** (§3 + §9.2 + §9.3 + §10.2). |
| 4 | **Build the feeder first, the launcher second.** The launcher is the easy half. |
| 5 | 🔴 **Do not build a turret. Do not build two dual-flywheels.** |
| 6 | **Order compliant wheels in 3 durometers immediately** (§2.5) — under $35, and the long pole is knowing which one grips your element. |
| 7 | **Build the practice target in week 1**, before the launcher is finished. |

### 14.6 The single sentence version

> 🔴 **Build a flywheel only if the game clearly pays for it, and if you do, build the simplest possible
> one on both robots and spend your real effort on the feeder — because the flywheel is cheap to build,
> expensive to make repeatable, and the feeder is where your season is actually won or lost.**

---

## 15. Worked R503 actuator budgets for launcher robots

**CONFIRMED-BIOBUZZ — R503:** *"ROBOTS are limited to a total of 8 motors and 8 servos … for all MECHANISMS
used in all configurations."* Reinforced at inspection by **I302**.
🔴 **DECODE allowed 10 servos; BIOBUZZ allows 8. Prior-season designs may now be illegal.**

**Every launcher BOM must carry one of these tables.**

### 15.1 Budget A — Single flywheel, serpentine feed, fixed aiming 🟢 **RECOMMENDED**

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| Drivetrain (4× mecanum/holonomic) | 4 | 0 | 4 / 8 | 0 / 8 |
| Intake | 1 | 0 | 5 / 8 | 0 / 8 |
| Transfer to magazine | 1 | 0 | 6 / 8 | 0 / 8 |
| **Flywheel** | **1** | 0 | **7 / 8** | 0 / 8 |
| Kicker | 0 | 1 | 7 / 8 | 1 / 8 |
| **Remaining for endgame** | **1 motor** | **7 servos** | ✅ **headroom** | ✅ |

🟢 **This is the only launcher budget in this section that leaves a motor for an endgame mechanism.** That
is the strongest practical argument for the recommended configuration.

### 15.2 Budget B — Single flywheel with hopper agitator and adjustable hood

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| Drivetrain (4×) | 4 | 0 | 4 / 8 | 0 / 8 |
| Intake | 1 | 0 | 5 / 8 | 0 / 8 |
| Hopper agitator | 1 | 0 | 6 / 8 | 0 / 8 |
| Indexer | 1 | 0 | 7 / 8 | 0 / 8 |
| **Flywheel** | **1** | 0 | **8 / 8 — FULL** | 0 / 8 |
| Kicker | 0 | 1 | 8 / 8 | 1 / 8 |
| Adjustable hood | 0 | 1 | 8 / 8 | 2 / 8 |
| **Endgame** | 🔴 **0 available** | 6 servos | ⚠ **servo-only endgame or nothing** | |

⚠ **Viable but tight.** 🟢 **The fix:** belt the agitator off the intake motor (§9.1) to recover a slot.

### 15.3 Budget C — Dual flywheel 🔴 **THE FAILURE CASE**

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| Drivetrain (4×) | 4 | 0 | 4 / 8 | 0 / 8 |
| Intake | 1 | 0 | 5 / 8 | 0 / 8 |
| Indexer | 1 | 0 | 6 / 8 | 0 / 8 |
| **Dual flywheel** | **2** | 0 | 🔴 **8 / 8 — FULL** | 0 / 8 |
| Kicker | 0 | 1 | 8 / 8 | 1 / 8 |
| Hopper agitator | 🔴 **over** | — | ❌ | |
| Endgame | 🔴 **over** | — | ❌ | |

🔴 **A dual flywheel plus a 4-motor drivetrain leaves NOTHING.** No agitator, no endgame, no margin.
**The escape:** a **2-motor tank/differential drivetrain** buys back two slots at a real maneuverability
cost — decide that deliberately, as `LEGAL-PARTS-CONSTRAINTS.md` §3.3 urges, **not by accident in week 6.**

### 15.4 Budget D — Catapult 🟢 **the R503-efficient launcher**

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| Drivetrain (4×) | 4 | 0 | 4 / 8 | 0 / 8 |
| Intake | 1 | 0 | 5 / 8 | 0 / 8 |
| Transfer | 1 | 0 | 6 / 8 | 0 / 8 |
| **Catapult winch** | **1** | 0 | **7 / 8** | 0 / 8 |
| Sear release | 0 | 1 | 7 / 8 | 1 / 8 |
| **Remaining** | **1 motor** | **7 servos** | ✅ | ✅ |

🟢 **Same actuator cost as a single flywheel, with no velocity-control burden.** If the game rewards a
repeatable one-shot rather than sustained fire, **this is the better engineering choice for this program.**

### 15.5 Budget E — Deposit / ramp 🟢 **maximum headroom**

| Mechanism | Motors | Servos | Running motors | Running servos |
|---|---|---|---|---|
| Drivetrain (4×) | 4 | 0 | 4 / 8 | 0 / 8 |
| Intake | 1 | 0 | 5 / 8 | 0 / 8 |
| Lift / delivery | 1–2 | 0 | 6–7 / 8 | 0 / 8 |
| Gate | 0 | 1 | 6–7 / 8 | 1 / 8 |
| **Remaining** | **1–2 motors** | **7 servos** | ✅✅ | ✅ |

### 15.6 The zero-slot actuation reminder

**`LEGAL-PARTS-CONSTRAINTS.md` §3.4 — the highest-leverage move in BIOBUZZ:** springs, gas springs
(**R801.A**), over-centre linkages, and **ratcheting devices (R303.H)** cost **zero actuator slots and zero
dollars per robot times two.** For launchers specifically:

| Zero-slot opportunity | Rule |
|---|---|
| Gas spring or elastic as the catapult energy source | **R801.A** / unrestricted springs |
| **Ratchet holding the catapult draw** (no motor holding current) | **R303.H** |
| Passive one-way gate in the feed path | unrestricted |
| Gravity serpentine magazine (no indexer motor) | — |
| Gap-tooth gear release (winch motor also fires) | — |
| Agitator belted off the intake motor | — |

---

## 16. Cost rollups

**All figures list price, as of August 2026, before discounts, tax and shipping. VERIFY-BEFORE-ORDER.**

### 16.1 By mechanism

| Mechanism | COTS / robot | COTS × 2 | Materials × 2 | Student-hours × 2 | R503 cost |
|---|---|---|---|---|---|
| §3 Single flywheel | ≈ $135 | ≈ $268 | ≈ $318 | 16–30 h | 1 motor |
| §4 Dual flywheel | ≈ $235 | ≈ $470 | ≈ $530 | 18–30 h | 🔴 2 motors |
| §5 Catapult | ≈ $129 | ≈ $258 | ≈ $308 | 22–38 h | 1 motor + 1 servo |
| §6 Slingshot | ≈ $52 | ≈ $104 | ≈ $128 | 10–18 h | 🟢 1 servo |
| §7 Pneumatic | 🔴 **ILLEGAL — $0** | — | — | — | — |
| §8 Ramp / deposit | ≈ $72 | ≈ $144 | ≈ $164 | 13–22 h | 🟢 1 servo (or 0) |
| §9.1 Hopper + agitator | ≈ $112 | ≈ $224 | ≈ $264 | 18–28 h | 1 motor (0 if belted) |
| §9.2 Indexer | ≈ $114 | ≈ $227 | ≈ $282 | 20–34 h | 1 motor (0 serpentine) |
| §9.3 Kicker | ≈ $52–$122 | ≈ $117–$257 | ≈ $137–$277 | 9–20 h | 1 servo |
| §10.2 Fixed aiming | ≈ $0 | ≈ $0 | ≈ $0 | 0–3 h | 🟢 0 |
| §10.3 Adjustable hood | ≈ $72 | ≈ $144 | ≈ $174 | 12–19 h | 1 servo |
| §10.4 Turret | ≈ $150 | 🔴 *one robot only* | — | 11–19 h | 🔴 1 motor |
| Vision (Limelight 3A) | $189 | 🔴 **$378** | $378 | — | 0 |

### 16.2 Three complete launcher packages, two robots each

| Package | Contents | **COTS × 2** | **Materials × 2** | **Hours × 2** | **R503** |
|---|---|---|---|---|---|
| 🟢 **MINIMUM (rookie / B-team)** | Single flywheel + serpentine magazine + kicker + fixed aiming | **≈ $364** | **≈ $434** | **≈ 45–75 h** | 1 motor + 1 servo |
| **COMPETITIVE (A-team)** | Single flywheel + steel flywheel + hopper/agitator + star indexer + kicker + fixed aiming + webcam vision | **≈ $814** | **≈ $924** | **≈ 85–140 h** | 3 motors + 1 servo |
| 🔴 **MAXIMUM (not recommended)** | Dual flywheel + hopper + indexer + kicker + adjustable hood + 2× Limelight | **≈ $1,468** | **≈ $1,618** | **≈ 105–170 h** | 🔴 4 motors + 2 servos |

🔴 **Read the MAXIMUM row as a warning, not a menu.** It is roughly **4× the cost and 2.5× the hours** of
the MINIMUM row, consumes **half the motor budget**, and — on the evidence of `ROBOT-ARCHETYPE-LIBRARY.md`
§3.3 — will not score proportionally more.

### 16.3 Spares kit for two robots

| Item | Qty | ≈ Cost |
|---|---|---|
| Compliant wheels (mixed durometer) | 6 | ≈ $50 |
| Printed hoods / channels / tapers | 6 | ≈ $25 filament |
| Kicker paddles | 4 | ≈ $10 filament |
| Catapult sears (if applicable) | 4 | ≈ $10 filament |
| Bearings | 8 | ≈ $30 |
| Spare flywheel motor | 1 | $32–$55 |
| Spare servo | 1 | **$36.99** |
| Encoder / servo cables | 4 | ≈ $20 |
| Surgical tubing | 2 m | $4.99 |
| Servo connector clips | 2 pk | $12 |
| **Total** | | **≈ $232** |

---

## 17. Verification log — every page loaded this session (2026-08-22)

### 17.1 Primary rule source (all R-rule text, grepped directly)

- `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` — R102, R103, R105, R201, R202,
  R203, R204, R301, R302, R303, R501–R506 (incl. **Table 12-3**), R601, R701, R702 (**Table 12-9**),
  R704, R801.
- `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` — full-text search for
  `launch|projectile|eject|shoot|catapult` (result: **no launch-restriction rule exists in V0** — §1.3).

⚠ **Extraction caveat inherited from `LEGAL-PARTS-CONSTRAINTS.md` §0.3:** the sectioned `.txt` has
column-shift defects in two-column rule tables. Table 12-3 rows for the **REV Servo Hub** and **Studica
Servo Power Block** show signs of this (§9.3). **Re-read those from the PDF before relying on them.**

### 17.2 Vendor pages loaded with WebFetch this session — VERIFIED

| URL | What it verified |
|---|---|
| `https://www.gobilda.com/yellow-jacket-planetary-gear-motors/` | 6000 RPM `5203-2402-0001` $54.99; 1620 RPM `5203/5202-2402-0003` $54.99, `5204-8002-0003` $56.99; 1150 RPM `-0005` variants; torques |
| `https://www.gobilda.com/flywheels/` | **Steel Flywheels** `3628-0014-0060` (60 mm, 115 g, 551 g·cm²) **$12.99**; `3628-0032-0082` (82 mm, 152 g, 1651 g·cm²) **$15.99** |
| `https://www.gobilda.com/intake-wheels/` | Boot-Wheels `3615-4008-0096/-0072/-0048` 30A; Intake Roller Wheels `3618-4008-0016/-0012` 8-pk $12.99; Gecko `3613-…`; Silicone Cord `2928-0008-0002` $5.99; Silicone Tubing `2928-0508-0002` $5.99; **Latex Surgical Tubing `2907-0305-0002` $4.99** |
| `https://www.gobilda.com/wheels-tires/` | Confirmed **Flywheels** and **Intake Wheels** exist as catalog categories |
| `https://andymark.com/products/compliant-wheels` | Compliant wheels 2 in./2.25 in./3 in./4 in., all part numbers and prices; **durometer guide 35A green → 60A black** |
| `https://www.revrobotics.com/duo-compliant-wheels/` | `REV-41-2034-PK4` (40A) and `REV-41-2035-PK4` (30A), 2 in., 5 mm hex, **$19.50/4-pk, In Stock** |
| `https://limelightvision.io/products/limelight-3a` | **$189.00**; REV + goBILDA threaded mounting; *"The REV Control Hub can only support a single LL3A at this time."* |
| `https://www.andymark.com/collections/first-tech-challenge` | Loaded; **"Compliant & Intake" category exists**, no prices rendered |
| `https://www.gobilda.com/hubs/` | Category loaded; hub families confirmed, **individual SKUs not rendered → FAMILY-ONLY** |

**Re-verification pass, 2026-08-22 (second session) — additional pages loaded:**

| URL | What it verified |
|---|---|
| `https://www.gobilda.com/steel-flywheel-82mm-diameter-152g-1651-g-cm/` | 🔴 **`3628-0032-0082` $15.99, 152 g, 1651 g·cm² — and the mounting pattern: four 4 mm holes w/ hex counterbores on the goBILDA 32 mm square pattern + eight holes on a 48 mm square pattern.** No bore. Closed register item 11. |
| `https://www.gobilda.com/steel-flywheel-60mm-diameter-115g-551-g-cm/` | `3628-0014-0060` $12.99, 115 g, 551 g·cm²; **16 mm square pattern** (+32 mm secondary). Confirms `-0014-` is **not** a 14 mm pattern. |
| `https://www.gobilda.com/2000-series-dual-mode-servo-25-3-speed/` | **`2000-0025-0003` = $36.99**, stall 7.9/9.3/10.8 kg·cm at 4.8/6.0/7.4 V, 300° range. Closed register item 12. |
| `https://www.gobilda.com/servo-electronics/` | **`3125-0001-0001` Servo Power Injector = $69.99** (6-channel, 8–15 V in); **`3102-0001-0001` Servo Programmer = $12.99** (re-confirmed). Closed register item 13. |
| `https://www.gobilda.com/flywheels/` (re-fetch) | Prices and inertia figures **unchanged** from first pass. |
| `https://www.gobilda.com/yellow-jacket-planetary-gear-motors/` (re-fetch) | `5203-2402-0001` 6000 RPM $54.99, `5204-8002-0003` $56.99 **unchanged**. |
| `https://andymark.com/products/compliant-wheels` (re-fetch) | `am-3462` $6.20, `am-3945` $8.40, `am-4537` $8.70, `am-3480` $11.00 and the 35A-green→60A-black durometer guide **all unchanged**. |
| `https://www.revrobotics.com/duo-compliant-wheels/` (re-fetch) | `REV-41-2034-PK4` / `REV-41-2035-PK4` $19.50 per 4-pk, **In Stock**, 5 mm hex moulded hub, rated **5,500 RPM** — unchanged. |

### 17.3 Pages that did NOT resolve this session — stated explicitly

| URL | Result |
|---|---|
| `https://www.gobilda.com/3628-series-steel-flywheel-60mm-diameter-115g/` | **HTTP 404** — wrong URL slug guessed in the first pass. ✅ **Superseded 2026-08-22:** the correct product URLs resolved on the second pass (see §17.2) and the bore/hub pattern is now **VERIFIED**. |
| `https://www.revrobotics.com/rev-41-1594/` | **HTTP 404.** Speculative URL; no claim made from it. |
| `https://www.andymark.com/collections/compliant-intake` | Loaded but rendered **no product rows**. Data came from the product page instead. |
| Studica (`studica.com`) | **Not attempted this session.** Phase A recorded **HTTP 403** to WebFetch. Studica parts named from manual tables only. |

### 17.4 Cross-referenced Phase A documents (not re-fetched)

- `reference/LEGAL-PARTS-CONSTRAINTS.md` — §2 motors, §3 the 8+8 budget, §4 servos, §5.4 sensors/cameras,
  §7 pneumatics, §8 fabrication definitions.
- `reference/VENDOR-ECOSYSTEMS.md` — §3 interoperability, §6.4 motion parts, §6.5 fasteners, §6.6 wiring, §6.7 fabrication.
- `reference/ROBOT-ARCHETYPE-LIBRARY.md` — §3.3 launcher/shooter archetype (score 2.63).

### 17.5 Official FIRST supplier status (from `VENDOR-ECOSYSTEMS.md` §2.0)

| Vendor | Status |
|---|---|
| **AndyMark** | ✅ **Official FIRST supplier** |
| **Studica** | ✅ **Official FIRST supplier** |
| **FIRST storefront (Pitsco)** | ✅ **Official** |
| goBILDA | General supplier (meets the **R302/VENDOR** test) |
| REV Robotics | General supplier (but the **only** legal control-system source per R701) |
| Limelight Vision | General supplier; also stocked by AndyMark |

---

## 18. Open questions / NEEDS-SKU-CHECK register

### 18.1 Blocked on Kickoff (2026-09-12) — cannot be resolved earlier

| # | Question | Blocks |
|---|---|---|
| 1 | 🔴 **Does BIOBUZZ have a launchable SCORING ELEMENT at all?** | This entire file |
| 2 | 🔴 **Element mass, diameter, compressibility, surface** | §2.4 energy calc; §2.5 durometer; §9.2 channel width — **all of it** |
| 3 | **Target height, distance, and forgiveness** | §2.3 required velocity; §10 aiming choice |
| 4 | **Does the point table pay more for a launched element than a deposited one?** | §14.2 gate condition 1 |
| 5 | **R105 expansion envelope** (V0-DEFERRED, explicit) | §1.4 deploying hopper/hood geometry |
| 6 | **Do G-rules restrict launching?** (Section 11 is a placeholder — §1.3) | Velocity cap, trajectory design |
| 7 | **How many elements can a ROBOT possess?** | §9.1 hopper vs. serpentine decision |

### 18.2 Resolvable before Kickoff

| # | Item | Action | Owner |
|---|---|---|---|
| 8 | **Table 12-2 servo stall-current cap is BLANK in the V0 PDF (V0-ERRATA)** | 🔴 **File a Game Q&A when it opens 2026-09-28, 12:00 ET.** Use DECODE's 4 A as the working number meanwhile | Programming/electrical lead |
| 9 | **Table 12-3 rows for REV Servo Hub + Studica Servo Power Block look column-shifted** | Re-read Table 12-3 in the PDF with PyMuPDF | Whoever owns the parts list |
| 10 | **2026-27 Inspection Quick Reference + servo power calculator not yet posted** (Phase A verified "Coming Soon") | Re-check weekly; it decides which servos are pre-approved | Electrical lead |
| 11 | ✅ **CLOSED 2026-08-22.** `3628` flywheels have **no bore** — they bolt to a square hub-mount pattern: **82 mm = 32 mm pattern** (+48 mm), **60 mm = 16 mm pattern** (+32 mm). A matching hub is a **mandatory** extra purchase (§3.3). | — | Done |
| 12 | ✅ **CLOSED 2026-08-22.** `2000-0025-0003` = **$36.99** (*25-3 Speed*; 9.3 kg·cm @ 6.0 V, 300°). ⚠ **All servo subtotals were rebuilt** — the old ≈ $25 estimate came from the now-discontinued `REV-41-1097`. | — | Done |
| 13 | ✅ **CLOSED 2026-08-22.** `3125-0001-0001` = **$69.99** (6-channel, 8–15 V input). ⚠ **More than double** the ≈ $30 previously assumed — §9.3 subtotal corrected. | — | Done |
| 14 | **`REV-41-1097` Smart Servo is DISCONTINUED** | 🔴 If you want these for two robots, **buy the full quantity now** | Purchasing |
| 15 | **AndyMark motor/servo prices unresolved** (`am-3104*`, `am-4954`) | Retry AndyMark product pages | Purchasing |
| 16 | **Element-presence sensor SKU** (§9.2) | Choose from `LEGAL-PARTS-CONSTRAINTS.md` §5.4 and verify | Electrical lead |
| 17 | **Dead-wheel odometry pod wheel `3624-4008-0032` was OUT OF STOCK** in Phase A | Re-check stock | Purchasing |

### 18.3 🟢 Safe to do NOW, before Kickoff — the pre-kickoff work list

| # | Action | Why it is safe |
|---|---|---|
| 18 | **Buy AndyMark compliant wheels in 35A, 40A and 50A** (2 in. `am-3462` $6.20 / 3 in. `am-3945` $8.40) | Under $35, needed regardless of game, and durometer is the long-pole unknown (§2.5) |
| 19 | **Buy latex surgical tubing `2907-0305-0002` ($4.99)** | Cheap, universally useful for prototyping (§5, §6, §9.1) |
| 20 | 🔴 **Build a PARAMETRIC CAD model of a serpentine channel with width as a variable** | §9.2 — on kickoff evening you change one number and start three prints. **The highest-value pre-kickoff CAD task in this file.** |
| 21 | **Buy feeler gauges (~$10) and digital calipers (~$25)** | §11.2, §13.3 — the duplicability protocol depends on them |
| 22 | **Buy a heat gun (~$25) if you do not have one** | §11.2 — enables polycarbonate hoods |
| 23 | **Write and bench-test a PIDF velocity-control OpMode on any spare motor** | §12.1 — the software is game-agnostic; the learning curve is the expensive part, and it can be climbed in August |
| 24 | **Buy the goBILDA servo programmer `3102-0001-0001` ($12.99), one per program** | §9.3 — R504.C permits it; useful for every servo on both robots |
| 25 | **Design and cost a full-size practice target rig** (materials, space, hours) | §14.2 gate condition 2 — decide **before** kickoff whether you can actually do this |
| 26 | **Audit any returning 2025-26 mechanism for servo count** | 🔴 **R503 dropped from 10 servos to 8.** Prior designs may now be illegal (§15) |

---

*End of `LAUNCHERS-AND-FEEDING.md`. Written 2026-08-22 against BIOBUZZ Competition Manual V0, Section 12
(final). All prices as of August 2026 and marked **VERIFY-BEFORE-ORDER**. Game-dependent content is flagged
**V0-DEFERRED** and must be revisited on Kickoff, 12 September 2026.*
