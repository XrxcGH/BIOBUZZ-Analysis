# ELECTRONICS AND SENSING

### The control system, power, wiring and sensing catalog for a TWO-ROBOT BIOBUZZ program — what must be bought, what must be built, what is illegal, and what it costs twice

> **Season:** FIRST Tech Challenge 2026-2027 **BIOBUZZ** presented by RTX
> **Legality source:** BIOBUZZ Competition Manual **V0** (2026-07-31), **Section 12 ROBOT Construction Rules (R)** —
> **FINAL for this season**, plus **Section 5 Event Rules (E)** for charging.
> **Written:** 2026-08-22. **Kickoff:** 2026-09-12. **Game Q&A opens:** 2026-09-28, 12:00 p.m. ET.
> **All prices are as of August 2026 and are `VERIFY-BEFORE-ORDER`.**

> **⚡ WHY THIS FILE IS DIFFERENT FROM EVERY OTHER MECHANISM FILE.**
> Every other mechanism in this catalog is *game-dependent* — you cannot know whether you need an intake until
> 12 September. **The electronics are not.** Section 12.5 through 12.9 is final, the 18-inch STARTING CONFIGURATION
> cube (R102) is final, and **every legal BIOBUZZ robot contains the same mandated control-system core no matter what
> the game turns out to be.** That makes this the one mechanism file you can act on today — and the one where a wrong
> purchase is most expensive, because the rules name legal parts *by part number* and everything else is illegal
> regardless of how correct its specifications are.

---

## 0. How to read this file

### 0.1 Claim labels (matched to `LEGAL-PARTS-CONSTRAINTS.md` and `VENDOR-ECOSYSTEMS.md`)

| Label | Meaning |
|---|---|
| **CONFIRMED-BIOBUZZ** `[C]` | Stated in the BIOBUZZ V0 text. Rule ID and page cited. Grep-verified this session. |
| **HISTORICAL** `[H]` | From a prior season (DECODE, INTO THE DEEP) or a prior-season FIRST document. **Planning input only — not law for BIOBUZZ.** |
| **JUDGMENT** `[J]` | My recommendation for *this* program. Not a rule. Argue with it. |
| **V0-GAP** | The V0 manual is silent where a prior season had a rule. Expect it to return at Kickoff. |
| **V0-ERRATA** | The V0 text contains an internal inconsistency or a broken cross-reference. |

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

| Tag | Meaning |
|---|---|
| **VERIFIED** | I loaded the vendor page with WebFetch **in this session (2026-08-22)** and read the name, SKU and price off it. |
| **MANUAL-SOURCED** | The part number comes from a BIOBUZZ V0 rule table (12-1 … 12-9). Legality is certain; **price and stock are not asserted.** |
| **FAMILY-ONLY** | I verified the vendor **category page** but not this specific product. The family is real; the SKU is not asserted. |
| **NEEDS-SKU-CHECK** | Buy the family, confirm the exact SKU on the vendor page before ordering. |
| **UNVERIFIED** | Neither page nor price loaded. Treat as a placeholder. |

**No SKU or price appears in this file unless it carries VERIFIED or MANUAL-SOURCED.** Where a vendor blocked or
failed to render, I say so (§14).

### 0.3 Where this file sits

- `reference/LEGAL-PARTS-CONSTRAINTS.md` — **the legality envelope.** Full rule text, Tables 12-1 … 12-9, the
  do-not-buy list, motors and servos as *actuators*. **Read that first.** This file does not repeat it; it
  cross-references it and extends it into the parts that are *purely electrical*.
- `reference/VENDOR-ECOSYSTEMS.md` — **the buyer's map.** Vendor profiles, the FIRST storefront limit-one-per-team
  arithmetic, the procurement calendar, the pre-kickoff standing order.
- `reference/CONSTRUCTION-RULES-R.md` — R-rule analysis.
- **This file** — the *mechanism-level* electronics catalog: what a control system, a power system, a harness, a
  sensor suite and a vision system each cost to build **twice**, what fails, and what to stock.

### 0.4 The verdict, in one paragraph

**CONFIRMED-BIOBUZZ + JUDGMENT.** BIOBUZZ mandates exactly one control-system topology (R701), exactly one battery
chemistry and a closed allowlist of battery part numbers (R601), exactly one main power switch off a closed
allowlist (R603), and a hard **8 motors + 8 servos** cap across all mechanisms (R503). The whole 8+8 budget fits on
a **single Control Hub** — 4 motor ports × 2 motors/port and 6 servo ports × 2 servos/port (Table 12-3). So the
Expansion Hub is a *convenience* purchase, not a legality purchase, and for a two-robot program on a modest budget
**you should design not to need it and save $550.** Buy the control system through the **FIRST storefront**, twice,
because the Electronics Kit and Driver Kit are **limit one per registered team** and you have two registrations.
Budget **≈ $2,200 for the mandatory electrical core of two robots** and **≈ $2,600 for two complete,
competition-ready, sparred, sensing-equipped packages** (§9) — and **about 56% of that is four storefront kits**,
i.e. two purchase decisions.

---

## 1. The two-robot electronics bill, in one page

**JUDGMENT + VERIFIED prices.** Three tiers. Pick one and stop deliberating.

| Tier | What it is | Two-robot cost | When it's right |
|---|---|---|---|
| **Rookie-minimum** | 2× storefront Electronics Kit + 2× storefront Driver Kit + 2 extra batteries + 1 extra charger + 1 shared REV Cable Bundle | **≈ $1,565** | B team's first robot; almost no spares, one event on the calendar |
| **Program-standard** `[J] RECOMMENDED` | The above + 5 batteries + 2 chargers + 2× REV Cable Bundle + console/wiring spares + 1× REV Sensor Bundle + through-bore encoder + OTOS + a cased camera on the A robot | **≈ $2,620** (§9.3) | Two robots, a practice field, a season with league play |
| **Competitive** | The above + 2× Limelight 3A + 2× goBILDA odometry pack + a spare Control Hub + a spare Driver Hub | **≈ $4,210** | You intend to win autonomous and you can afford redundancy |

### 1.1 The five decisions that set the number

| # | Decision | The answer, and why |
|---|---|---|
| **1** | Control Hub or phone + Expansion Hub? | **Control Hub.** R701.A. R701's blue box: *"the REV Control Hub is the only officially supported ROBOT CONTROLLER device."* `[C]` The phone path is still legal but it makes you the vendor of your own support. |
| **2** | Buy retail or through the FIRST storefront? | **Storefront, twice.** Electronics Kit + Driver Kit = **$610/team [H]** versus **$650 retail for the two hubs alone**, before the servo, two sensors, cable pack, grounding strap, switch and two gamepads. **[D]** |
| **3** | Second hub (Expansion Hub) — yes or no? | **Design so the answer is no.** §E1.3. The 8+8 budget fits on one Control Hub. **$275 × 2 = $550 saved.** |
| **4** | How many batteries? | **4–6 for the program.** Not 2. §E3. Batteries in rotation, not in sequence, is what keeps two robots on a practice field. |
| **5** | Vision: webcam or Limelight 3A? | **Webcam first, Limelight only on the A robot, and only if autonomous scoring is the strategy.** §E8. |

### 1.2 The two-robot multiplier, stated honestly

**The control system is the least duplicable thing in FTC.** A 3D-printed bracket costs $1.40 to make twice. A
Control Hub costs $375 to make twice, and there is no legal substitute, no cheaper equivalent and no way to share
one between two robots that are both on a practice field. **Roughly 45–55% of a two-robot electronics budget is
fixed, non-negotiable, doubled cost.** Plan the money before you plan the mechanisms.

---

## 2. The R-rule envelope for electronics — the compact citation table

All **CONFIRMED-BIOBUZZ**, all grep-verified against
`manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` this session.

| Rule | p. | What it decides for this file |
|---|---|---|
| **R102** * | 66 | STARTING CONFIGURATION ≤ **18 × 18 × 18 in.** — the volume your electronics must pack into. |
| **R104** * | — | **No robot weight limit in BIOBUZZ.** Electronics packaging can favour serviceability over mass. |
| **R105** | — | Expansion limits are **game-dependent → DEFERRED TO KICKOFF.** Affects wire lengths across extending mechanisms only. |
| **R501** * | 74-76 | Motor allowlist (Table 12-1). **Carve-out:** vibration/autofocus motors in COTS computing devices, and **motors integral to a COTS sensor (e.g. LIDAR, scanning sonar)** — *"These motors do not count toward the limit in R503."* |
| **R502** * | 76 | Servo allowlist test (Table 12-2). **Blue box, load-bearing for wiring:** *"The REV Control Hub and REV Expansion Hub provide **5V** to servos, and the goBILDA Servo Power Injector, REV Servo Power Module, Studica Servo Power Block, and REV Servo Hub provide **6V** to servos."* |
| **R503** * | 76-77 | **8 motors + 8 servos total, across all MECHANISMS in all configurations.** `[H] DECODE allowed 10 servos — this is a reduction.` |
| **R504** * | 77 | Actuators may not be modified — **except** leads may be trimmed and connectorised (per R609), insulation added to terminals, labels applied. |
| **R505** * | 77 | **Table 12-3** — the only legal power-regulating devices for actuators, with per-device load limits. |
| **R506** * | 77 | **Relays, electromagnets and electrical solenoid actuators are PROHIBITED.** |
| **R601** * | 78 | **Exactly 1 approved 12V NiMH main battery** (Table 12-4, closed allowlist by part number). Fuse → COTS 20A ATM mini blade. Connectors → Anderson Powerpole, XT30, or comparable rating. |
| **R602** * | 78-79 | COTS USB battery packs ≤ 100 Wh for **self-contained peripherals and LEDs only**; electrically isolated. *"Any device receiving signals from a REV Control or Expansion Hub must be powered by the main ROBOT battery."* |
| **R603** * | 79 | **Exactly one main power switch** from Table 12-5, accessible, clear of pinch hazards. Secondary switches allowed downstream. |
| **R604** * | 79 | Fuses used as directed. **No higher trip points, no self-resetting replacements.** |
| **R605** * | 79-80 | **Frame must not carry current.** Grounding only via a Table 12-6 resistive strap, to a fully COTS component with an XT30 connector. |
| **R606** * | 80 | Power-regulating devices, wiring and fuses must be **made visible for inspection**; RC diagnostic lights/screen visible. |
| **R607** * | 80 | CUSTOM CIRCUITS must not output regulated power **above 5V** except solely for LEDs. Unregulated battery voltage may pass through. |
| **R608** * | 80-81 | **Table 12-7** — how each power regulator must be powered (XT30 / screw terminals / JST-VH, main battery only). |
| **R609** * | 81 | **Table 12-8** wire sizing. Manufacturer-integral wires are **exempt**. **No paralleling small wires** to fake a larger gauge. |
| **R610** * | 82 | **Wire colours** on the 12V main bus and +5V aux bus, along the entire length. Does **not** apply to motor, signal, servo or manufacturer wiring. |
| **R611** * | 82 | Powered USB hubs may draw only from an **R602 USB pack** or the **5V aux port** on a REV hub. |
| **R612** * | 82 | **Do not modify critical power paths.** **Boost and buck converters in a power path are explicitly prohibited.** Blue box names the **goBILDA Servo Travel Tuner**. |
| **R613** * | 82-83 | **No mixing power.** Sensors powered solely by the regulator they connect to; **no cross-wiring ports, no combining ports into a bus**; 6V servo power → **servos only**; +5V Aux may power devices not connected to other regulators except via USB. |
| **R701** * | 84 | **ROBOT CONTROLLER = (A) REV Control Hub REV-31-1595, or (B) Android smartphone + REV Expansion Hub REV-31-1153. Plus (C) no more than one additional Expansion Hub.** |
| **R702** * | 84-85 | Coprocessor software may not be altered. **Exception: programmable vision coprocessors in Table 12-9 — which contains exactly one device, the Limelight 3A (LL_3A).** Example 6 names the **Limelight 3G, OpenMV Cam and Luxonis OAK-1 as prohibited**. |
| **R703** * | 85 | Smartphone RC must connect to the Expansion Hub via **USB** (OTG cables/hubs permitted). |
| **R704** * | 85 | Wi-Fi/bandwidth. **D: FTC Dashboard, FTControl Panels and similar are PROHIBITED on the RC network. No continuous video stream.** C: programming laptops off the RC network during matches. |
| **R705** * | 85 | Device naming `<team#>-RC` / `<team#>-DS`, spares `<team#>-<letter>-RC/DS`. **Two teams ⇒ four names minimum.** |
| **R706** * | 85 | Only listed modifications to DS device, Android RC, switches, regulators, fuses, batteries. **No custom enclosures.** **K: power switch mounting brackets may be modified or replaced.** **H: devices except batteries may be repaired.** |
| **R707** * | 85-86 | **USB is for vision.** Only (A) webcams/optical vision sensors per R708, (B) a USB hub or switch, (C) a REV Expansion Hub. |
| **R708** * | 86 | **Single image sensor** devices natively supported by the RC app. **Stereoscopic cameras not allowed.** (A) all UVC-compatible USB webcams *"(Logitech C270, and related)"*; (B) R702 coprocessors. **UVC stream/data only.** |
| **R709** * | 86 | Self-contained video recorders (GoPro-style) allowed for **non-functional post-MATCH viewing**, wireless off. |
| **R710** * | 86 | **Lasers** only if part of a sensor, **IEC/EN 60825-1 Class I or Exempt**, and **non-visible spectrum**. |
| **R711** * | 86 | Control Hub Wi-Fi password **must** be changed; smartphones in Airplane Mode; **Bluetooth disabled** on RC and DS; DS purged of all remembered Wi-Fi connections except the RC. |
| **R901** * | 87 | DS = **REV Driver Hub REV-31-1596**, or any Android device + USB cables/hubs for gamepads. **Only one DS connected and powered at a time.** Spare DS permitted. |
| **R902** * | 87 | DS touch screen **accessible and visible**, usable without a mouse. |
| **R903** * | 87-88 | OPERATOR CONSOLE **including power banks** ≤ **36 × 18 × 24 in.** (91.4 × 45.7 × 61.0 cm). No hard weight limit; **>20 lb invites scrutiny.** Spare USB hub allowed, one connected. |
| **R904** * | 88 | **No wireless to/from/within the OPERATOR CONSOLE** other than the RC↔DS app link. *"active wireless network cards and Bluetooth devices"* named. |
| **E511** * | 39 (§5) | Charging: safe rate per manufacturer; **never a charger exceeding 3-amp average channel current**; polarised connector matching the battery — **never alligator clips**. |

**V0-ERRATA carried forward from `LEGAL-PARTS-CONSTRAINTS.md` §16, re-confirmed this session:** Table 12-8 writes the
Core Hex as `REV-14-1300` while Table 12-1 says `REV-41-1300` (the latter is the real REV SKU); R601.A points at R610
(wire colours) for fuse installation; R612.C points at R607 instead of R505.
**⚠ Extraction warning:** in the sectioned plain-text dump, **Tables 12-3, 12-4 and 12-7 are row-shifted** — the
`.txt` dump silently mis-pairs cells with their rows. **Re-extracted from the PDF with PyMuPDF this session and
reproduced verbatim here:** Table 12-3 in **E1.3**, Table 12-4 (batteries) / 12-5 (switches) / 12-6 (grounding
straps) in **E3.2**. Two shifts confirmed and corrected on 2026-08-22:
> - The `.txt` gives **Servo Hub `REV-11-1855` = "2 Motors per Device"** and **SPARKmini `REV-31-1230` = "2 Servos
>   per Port"**. The PDF says the opposite — **Servo Hub = 2 Servos per Port, SPARKmini = 2 Motors per Device.**
> - In Table 12-4 the **notes column is shifted up one row**: *"May be labeled as ‘Modern Robotics’"* belongs to
>   **Matrix `14-0014`** (not goBILDA), and *"Formerly 739023"* belongs to **TETRIX MAX `W39057`** (not Matrix).

**Read the PDF, not the .txt, before an inspection argument.** `LEGAL-PARTS-CONSTRAINTS.md` §5.2 / §6.6 agrees
with the PDF reading of the port limits.

---

# E1 · THE CONTROL SYSTEM

## E1.1 What it is and when a design needs it

**Always. There is no design that does not need it.** The ROBOT CONTROLLER is the single legal source of control for
every actuator on the robot (R701) and the only legal path from the driver's thumbs to a motor. It is also the most
expensive single object on the robot, has no legal substitute, and must be bought **twice** for a two-team program.

**What the mechanism actually comprises:**

1. A **ROBOT CONTROLLER** — a REV Control Hub, or an Android smartphone tethered by USB to a REV Expansion Hub (R701.A/B, R703).
2. Optionally **one** additional REV Expansion Hub (R701.C — *"no more than one"*).
3. A **DRIVER STATION** — a REV Driver Hub or another Android device (R901); covered in **E2**.
4. Optionally, **actuator expansion**: a REV SPARKmini (motors, open-loop) or a REV Servo Hub / goBILDA Servo Power
   Injector (servos, 6V) — all from Table 12-3 (R505).

**Verified Control Hub port budget (VERIFIED — `revrobotics.com/rev-31-1595/` and `docs.revrobotics.com` loaded 2026-08-22):**

| Resource | Count | Note |
|---|---|---|
| DC motor ports | **4** | JST VH 2-pin, **with built-in encoder ports** |
| Servo ports | **6** | 0.1 in. header |
| Digital I/O ports | **8** | |
| Analog input ports | **4** | |
| I2C buses | **4** | independent |
| RS485 ports | **2** | daisy-chain to an Expansion Hub |
| USB | **1 × USB-C, 1 × USB 2.0-A, 1 × USB 3.0-A** | R707 limits what may be plugged in |
| Internal IMU | **1 × 6-axis** | free odometry heading source — **do not buy a separate IMU for a Control Hub build** |
| Input voltage | **8–15 V** | XT30, main battery only (Table 12-7) |
| Motor port current | **10 A continuous, 20 A absolute max** | |
| +5V auxiliary | **5 A total, shared across servo and power ports** | |
| Per servo port pair | **2 A max** | **the number that causes servo brownouts — see E5** |
| Processors | RK3328 quad-core Cortex-A53 + TI Cortex-M4 | |
| In the box | Control Hub, XT30 extension 30 cm, 3-pin JST PH 30 cm, USB-A→USB-C cable | |

## E1.2 The main variants

| # | Variant | What it is | Legality |
|---|---|---|---|
| **A** | **Control Hub alone** | REV-31-1595 only. 4 motor / 6 servo / 8 DIO / 4 analog / 4 I2C. | R701.A `[C]` |
| **B** | **Control Hub + Expansion Hub** | Adds 4 motor / 6 servo / 8 DIO / 4 analog / 4 I2C over RS485. | R701.A + C `[C]` |
| **C** | **Control Hub + SPARKmini(s)** | Adds 2 open-loop motors per $35 device. **No encoder feedback.** | R505 Table 12-3 `[C]` |
| **D** | **Control Hub + Servo Hub / Servo Power Injector** | Adds servo *channels* and raises servo voltage 5V → 6V. **Does not raise the R503 cap of 8.** | R505 Table 12-3, R502 blue box `[C]` |
| **E** | **Android phone + Expansion Hub** | The legacy path. Legal, cheaper if you already own the phone, unsupported by FIRST. | R701.B, R703 `[C]` |

### Comparison table (1 = worst / hardest, 5 = best / easiest)

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability (2nd robot)** | Verdict |
|---|---|---|---|---|---|---|
| **A. Control Hub alone** | **5** | **4** | **5** | **5** | **5** | **`[J]` THE ANSWER for both robots.** |
| B. + Expansion Hub | 3 | 2 | 4 | 4 | **2** | $550 for the pair, and it was out of stock a day ago. Last resort. |
| C. + SPARKmini | 4 | **5** | 3 | 4 | **5** | $35 × 2. Brilliant for a dumb roller. Useless for anything closed-loop. |
| D. + Servo Hub / Injector | 4 | 3 | 4 | **5** | 4 | Buy **only** if you have 6V-rated servos or ≥7 servos. |
| E. Phone + Expansion Hub | **2** | 3 | **2** | **2** | **2** | Legal `[C]`, but "responsible for testing and verifying its compatibility" is you. Two phones = two support problems. |

## E1.3 The port math that saves this program $550 — read before you add an Expansion Hub

**CONFIRMED-BIOBUZZ.** Table 12-3 (R505) gives **2 motors per hub motor port** and **2 servos per hub servo port**.
A lone Control Hub therefore supports **4 × 2 = 8 motors** and **6 × 2 = 12 servo positions**, capped at 8 by R503.

Port counts **VERIFIED** off `revrobotics.com/rev-31-1595/` this session: **4 DC motor ports, 6 servo ports**,
8 digital I/O, 4 analog, 4 I2C, 2 RS485, **1 internal 6-axis IMU**.

**Table 12-3: Power Regulators and Limits** — reproduced **verbatim from the V0 PDF, printed p. 77**
(re-extracted with PyMuPDF this session; **this is the authoritative de-shifted version** — see the extraction
warning in §2, which specifically scrambles the Servo Hub and SPARKmini load limits in the `.txt` dump):

| Power Regulating Device | Part Number | **Load Limit per Device** |
|---|---|---|
| goBILDA 6V Servo Power Injector | `3125-0001-0001` | 2 Servos per Port |
| REV Control Hub or Expansion Hub **Motor** Ports | `REV-31-1153` / `REV-31-1595` | **2 Motors per Port** |
| REV Control Hub or Expansion Hub **Servo** Ports | `REV-31-1153` / `REV-31-1595` | **2 Servos per Port** |
| REV Servo Power Module | `REV-11-1144` | 2 Servos per Port — ⚠ **DISCONTINUED**, see E1.4 |
| REV Robotics Servo Hub | `REV-11-1855` | **2 Servos per Port** |
| REV SPARKmini | `REV-31-1230` | **2 Motors per Device** |
| Studica Servo Power Block | `75005` | 2 Servos per Port |

**This table is a closed list (R505).** A motor or servo controller that is not on it is illegal no matter how well
it works — which is why the do-not-buy list in §11 exists.

> **The entire legal 8-motor + 8-servo budget fits on ONE Control Hub. An Expansion Hub buys you convenience,
> current headroom and independent encoder channels — never legality.**

**The catch `[J]`:** two motors on one port share **one control signal and one encoder input**. They must be commanded
identically. That is correct for a mechanically coupled pair (two motors on a common lift shaft; two motors on one
side of a tank drive) and **wrong for two independent mechanisms**.

| Situation | Cheapest legal answer | Cost for 2 robots |
|---|---|---|
| Coupled pair (lift, tank side, dual-roller intake) | **Pair them on one hub port.** | **$0** |
| 5+ *independent, closed-loop* motors | Expansion Hub | $550 |
| An independent, *open-loop* motor (duck spinner, dumb roller) | **SPARKmini REV-31-1230** | **$70** |
| 7–8 servos, or servos needing 6V | **Servo Hub REV-11-1855** or **goBILDA Injector 3125-0001-0001** | $180 / $140 |

**`[J]` Design rule for this program: keep independent closed-loop motors ≤ 4 per robot.** Write that constraint into
every archetype BOM alongside the R503 8+8 budget. It is worth $550 and it removes a part with a live stock risk.

## E1.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Electronics Kit** (Control Hub, Smart Robot Servo, Switch Cable & Bracket, Color Sensor V3 + cable, Touch Sensor + cable, Resistive Grounding Strap, Control Hub Cable Pack, M3×16 screws + nylocks) | **FIRST storefront (Pitsco)** | "Electronics Modules and Sensors Kit V1.1" | **1** | **2** | **$325 ea = $650** | Buy | **VERIFIED** page, price `[H]` rev 25-26.4 | 🕐 **LIMIT ONE PER REGISTERED TEAM.** You have two registrations — that is the whole reason the two-team structure pays for itself. Satisfies R701.A, R603, R605 in one order. |
| **Control Hub** (retail fallback) | REV Robotics | **`REV-31-1595`** | 1 | 2 | **$375.00 ea = $750** | Buy | **VERIFIED** — In Stock 2026-08-22 | R701.A `[C]`. Only if the storefront limit is exhausted or you want a spare. |
| **Expansion Hub** (optional 2nd hub) | REV Robotics | **`REV-31-1153`** | **0–1** | **0–2** | **$275.00 ea** | Buy | **VERIFIED** — ⚠ **still OUT OF STOCK on 2026-08-22** (re-checked; page structured data reads `OutOfStock`). Out of stock two days running — **treat availability as a real schedule risk, not a footnote** | R701.C `[C]` allows **at most one** extra. **See E1.3 — design so you don't need it.** |
| **SPARKmini motor controller** | REV Robotics | **`REV-31-1230`** | 0–2 | 0–4 | **$35.00 ea** | Buy | **VERIFIED** — In Stock | 2 **motors** per device (Table 12-3) `[C]`. Powered only via its Power input from the main battery (Table 12-7) `[C]`. **Open-loop — no encoder.** |
| **Servo Hub** | REV Robotics | **`REV-11-1855`** | 0–1 | 0–2 | **$90.00 ea** | Buy | **VERIFIED** | Table 12-3 `[C]`. Delivers **6V** to servos (R502 blue box) `[C]`. Does **not** raise the R503 cap. |
| **Servo Power Injector** | goBILDA | **`3125-0001-0001`** (8–15 V in, 6 V out) | 0–1 | 0–2 | **$69.99 ea** | Buy | **VERIFIED** | Table 12-3 `[C]`. XT30 from main battery **only** (Table 12-7) `[C]`. **R613.C: its 6V may power servos only — not LEDs.** |
| ~~Servo Power Module~~ | ~~REV~~ | ~~`REV-11-1144`~~ | — | — | ~~$48.88~~ | — | **VERIFIED: DISCONTINUED** | Legal (Tables 12-3, 12-7) `[C]` but end-of-life. **Never design two robots around an EOL part.** |
| **Control & Power Bundle** (Control Hub + 12V Slim Battery + Battery Charger `REV-31-1299` + PS4 gamepad + Switch Cable & Bracket + **Driver Hub**) | REV Robotics | **`REV-35-1906`** | 0–1 | 0–2 | **$750.00 ea** | Buy | **VERIFIED** contents + price + In Stock | **The one-SKU whole-robot-electronics answer** if the storefront is unavailable. Compare: storefront Electronics + Driver Kit = $610 `[H]`. **Storefront still wins.** |
| DUO Control Bundle | REV Robotics | `REV-35-2709` | 0–1 | 0–2 | **$650.00 ea** | Buy | **VERIFIED** price; **contents NOT verified** | NEEDS-SKU-CHECK on contents against R701/R601/R603 before assuming completeness. |
| Control Hub repair service | REV Robotics | `REV-31-1595-RFB` | as needed | as needed | **$165.00** | Buy | **VERIFIED** — In Stock | R706.H permits repair `[C]` — **but not of batteries.** Less than half the price of replacement. |
| USB-A → USB-C cable (RC↔laptop) | REV Robotics | `REV-11-1232` | 1 | 2 | **$10.50–$11.00** | Buy | **VERIFIED** | One comes in the Control Hub box. A second lives in the pit kit. |
| ❌ 3D-printed Control Hub enclosure | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R706 forbids "removing enclosures and replacing with custom enclosures."** Print *mounts*, never *enclosures*. |

## E1.5 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Method | Material / tooling | Per robot | For 2 | Student-hours (both robots) |
|---|---|---|---|---|---|
| **Control Hub mounting tray** | 3D print, or cut 3 mm polycarbonate + hand-drill | Printer or hand tools; M3 hardware | 1 | 2 | **2–3 h** |
| **Serviceability cut-outs / removable access panel** | Design into the chassis plate | CAD + hand tools | 1 | 2 | **1–2 h** — this is an **R606** requirement, not a nicety |
| **Diagnostic-LED sight window** | Slot or hole in a guard | hand tools | 1 | 2 | **0.5 h** — R606.B; and FIELD STAFF cannot help you if they can't see the lights |
| **Cable strain-relief anchors** | 3D print + zip tie / Cinch-Strap | printer | 6–12 | 12–24 | **2 h** |
| **Wiring diagram for YOUR robot** | Draw it, laminate it, tape it inside the pit toolbox | paper | 1 | **2 — one per robot, not one per program** | **2 h** — the single highest-value hour in this list |

**Total fabrication: ≈ 8–10 student-hours for both robots.** Print every bracket **qty 2 on the first run**.

## E1.6 Approximate subtotals

| Configuration | Per robot | **For 2 robots** |
|---|---|---|
| Storefront Electronics Kit only (Control Hub path) | **$325** `[H]` | **$650** |
| Retail Control Hub only | $375 | $750 |
| Control Hub + SPARKmini ×1 | $410 | $820 |
| Control Hub + Expansion Hub | $650 | **$1,300** ← the expensive branch |
| Control & Power Bundle (incl. Driver Hub, battery, charger, gamepad, switch) | $750 | $1,500 |

## E1.7 Common failure modes and the spares to stock

| Failure | Symptom | Cause | Prevention / spare |
|---|---|---|---|
| **Control Hub reboots mid-match** | Robot dies, comes back ~15 s later | **ESD through the frame**, or battery sag below ~8 V (R605; Control Hub minimum input 8 V) | **Fit the resistive grounding strap (R605, Table 12-6).** Highest reliability-per-dollar part in the whole BOM. |
| **XT30 pulled out of the hub** | Total power loss | No strain relief on the battery lead | Cinch-Strap the battery; anchor the XT30 lead within 50 mm of the hub |
| **Motor port dead** | One motor stops, others fine | Port MOSFET failed after a stall | **`REV-31-1595-RFB` $165 repair**, or **move the motor to a free port** — this is why you keep a port spare |
| **Encoder count drifts / reverses** | Autonomous walks off | JST PH sensor cable partly unseated | JST joiner boards + a cable that is **routed, not stretched** |
| **RS485 link drops the Expansion Hub** | Half the robot dead | RS485 cable or connector | A second **JST PH 3-pin comms cable** in the kit (in the Cable Bundle) |
| **Wrong firmware after an update** | DS won't connect | Mismatched hub firmware | Update all four devices (2 RC, 2 DS) on the **same day**, from the **same laptop** |

**Spares for a two-robot program `[J]`:** 1 × spare Control Hub *if the budget allows* (it is the only single point of
failure that ends a robot's day and cannot be improvised), otherwise 1 × spare SPARKmini ($35) and the repair-service
path pre-researched. **Never cannibalise robot B's hub for robot A at an event** — you lose two teams instead of one.

## E1.8 Rookie-minimum vs competitive

| | **Rookie-minimum (B team)** | **Competitive (A team)** |
|---|---|---|
| Controller | Storefront Electronics Kit (Control Hub) | Same |
| Second hub | **None.** ≤4 independent closed-loop motors by design | SPARKmini for any open-loop motor; Expansion Hub only if the game forces 5+ independent closed-loop motors |
| Servo power | Hub servo ports at 5V | Servo Hub at 6V if servos are 6V-rated or ≥7 servos |
| Spare | None | Spare Control Hub |
| **Cost for that robot** | **$325** `[H]` | **$450–$700** |

---

# E2 · THE OPERATOR CONSOLE AND GAMEPADS

## E2.1 What it is and when a design needs it

**Always, and it is inspected.** The OPERATOR CONSOLE is *"the set of COMPONENTS and MECHANISMS used by the DRIVE TEAM
to relay commands to the ROBOT"* (R902) — the DRIVER STATION device, the gamepads, the cables, the hub, and whatever
box it all lives in. **It is a per-TEAM purchase, not a per-robot purchase** — but with two registered teams competing
independently, you need **two complete consoles**.

## E2.2 The main variants

| # | Variant | What it is | Legality |
|---|---|---|---|
| **A** | **REV Driver Hub** | Purpose-built Android DS. 5 in. 800×480 touchscreen, 3 × USB-A, USB-C charge, user-replaceable 5040 mAh Li-ion. | R901.A `[C]`, *"the only officially supported DRIVER STATION device"* |
| **B** | **Android tablet/phone + OTG hub** | Any Android device + USB cables/hubs for gamepads. | R901.B `[C]` — legal, unsupported |
| **C** | Driver Hub + spare DS in the box | Spare permitted, **only one connected and powered on at a time**. | R901 blue box `[C]` |

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **A. Driver Hub** | **5** | 3 | **5** | **4** | **5** | **`[J]` Buy two.** Bundled into the storefront Driver Kit. |
| B. Android + OTG | 2 | **5** | 2 | 2 | 3 | Only if a working device already exists and someone owns the debugging |
| C. A + spare DS | 4 | 2 | 5 | **5** | 2 | Competitive teams only |

## E2.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per **team** | Qty for 2 teams | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Driver Kit** (FTC Legal Gamepad ×2, REV Driver Hub ×1, FTC Legal Webcam ×1) | **FIRST storefront (Pitsco)** | "Driver Kit" | **1** | **2** | **$285 ea = $570** | Buy | **VERIFIED** page, price `[H]` rev 25-26.4 | 🕐 **LIMIT ONE PER REGISTERED TEAM.** Satisfies R901 and throws in a legal webcam. **Buy this before anything else.** |
| **Driver Hub** (retail fallback) | REV Robotics | **`REV-31-1596`** | 1 | 2 | **$275.00 ea = $550** | Buy | **VERIFIED** — In Stock. Box: Driver Hub, battery, USB-A wall charger, USB-A→USB-C cable | R901.A `[C]`. 3 × USB-A, 1 × USB-C charge, 5 in. 800×480 touchscreen, 5040 mAh user-replaceable Li-ion. |
| **Driver Hub spare battery** | REV Robotics | **`REV-31-1876`** | 1 | 2 | **$21.75 ea** | Buy | **VERIFIED** | Not rule-mandated. **`[J]` A dead DS battery ends your day.** Note R903 counts power banks toward console volume. |
| **Gamepads** | REV Robotics | **`REV-31-2983`** USB PS4-compatible | **2 + 1 spare = 3** | **6** | **$26.00 ea = $156** | Buy | **VERIFIED** — In Stock | **Wired USB only — R904 bans Bluetooth** `[C]`. `[H]` DECODE capped connected gamepads at 2; V0 is silent (see E2.4). |
| **Short USB extension cables** | any | USB-A male→female, ~15 cm | 3 | 6 | UNVERIFIED | Buy | **HISTORICAL best practice** | `[H]` DECODE R903 blue box: *"Teams are strongly encouraged to use short USB cable extenders… These extenders are intended to remain forever plugged into the DRIVER STATION device"* — saves the DS ports from wear. **Cheapest reliability upgrade on the console.** |
| **Ferrite cable clips** | any | Snap-on ferrite, ~5 mm bore | 2–3 | 4–6 | UNVERIFIED | Buy | **HISTORICAL** | `[H]` DECODE: *"Adding a ferrite cable clip to gamepad cables close to the USB connector is highly recommended."* |
| USB hub (if needed) | any | Powered or unpowered, OTG optional | 0–1 | 0–2 | UNVERIFIED | Buy | **CONFIRMED-BIOBUZZ** R901.B | **A spare hub is allowed** if only one is connected at a time (R903 blue box) `[C]`. **R611 does not apply on the console** — it governs hubs on the *ROBOT*. |
| USB-A wall charger + cable | REV Robotics | included in the Driver Hub box | 1 | 2 | included | Buy | **VERIFIED** | |
| ❌ Bluetooth gamepad / wireless headset / Wi-Fi card in the console | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R904** prohibits `[C]`. |

## E2.4 ⚠ V0-GAP: there is no gamepad allowlist in BIOBUZZ V0

**CONFIRMED by exhaustive grep this session:** the string `gamepad` appears **exactly once** in the entire BIOBUZZ V0
manual — in R901.B, *"for connecting one or more gamepads."* There is **no Table of allowed gamepads and no
two-gamepad cap** in V0. DECODE carried both.

**`[H]` The DECODE allowlist (DECODE R903, Table 12-12) — planning reference only, NOT BIOBUZZ law:**

| Gamepad | Part number | DECODE note |
|---|---|---|
| Logitech F310 | 940-00010 | |
| Xbox 360 Controller for Windows | 52A-00004 | |
| Sony DualShock 4 (PS4) | N/A | **Wired mode only.** *"DOES NOT include the Sony DualSense Edge Wireless Controller in any configuration"* |
| Sony DualSense (PS5) | N/A | |
| Etpark Wired Controller for PS4 | REV-39-1865 | *"Newer versions… may not support all functionality provided by the FTC SDK"* |
| **REV Robotics USB PS4 Compatible Gamepad** | **REV-31-2983** | |
| Quadstick, Xbox 360 Emulation Mode | any model | accessibility device |

`[H]` DECODE also allowed **"enhancements to the gamepad (e.g. back paddles) that do not modify the electronics"** and
**different colours of the same model**, and capped the console at **2 connected gamepads**.

> **`[J]` PURCHASING DECISION: assume the allowlist returns at Kickoff and buy only models on the DECODE list —
> in practice, the REV `REV-31-2983` at $26.00, which is on the DECODE list AND is what the storefront Driver Kit
> ships.** Do **not** stockpile exotic controllers or build a custom control panel before 12 September. Re-grep the
> Kickoff manual for `gamepad` on day one.

## E2.5 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Method | Material / tooling | Per team | For 2 | Student-hours (both) |
|---|---|---|---|---|---|
| **Console box / tray** | Toolbox, Pelican-style case, or plywood + hinges | hand tools | 1 | **2** | **4–6 h** |
| Driver Hub cradle (screen visible & reachable) | 3D print or bent aluminium | printer / hand tools | 1 | 2 | **2 h** — **R902** requires the touchscreen be *usable without a mouse* |
| Gamepad cable routing + strain relief | Grommets, Cinch-Straps, ferrites | hand tools | 1 | 2 | **1 h** |
| Console volume check jig | Cardboard 36 × 18 × 24 in. box | free | 1 | 1 shared | **0.5 h** — **R903**; check *with* the power banks in it |

**≈ 8–10 student-hours for both consoles. This is a genuine August build — R903's dimensions are final and
game-independent.**

## E2.6 Approximate subtotals

| Configuration | Per team | **For 2 teams** |
|---|---|---|
| Storefront Driver Kit (DS + 2 gamepads + webcam) | **$285** `[H]` | **$570** |
| + spare gamepad + spare DS battery | $333 | **$666** |
| + fabricated console box (materials) | ≈ $380 | **≈ $760** |
| Retail equivalent (Driver Hub + 3 gamepads + battery) | $375 | $750 (no webcam) |

## E2.7 Common failure modes and the spares to stock

| Failure | Symptom | Cause | Prevention / spare |
|---|---|---|---|
| **Gamepad stops responding mid-match** | One driver goes dead | Cable strain at the USB connector; internal wire break | **Ferrite clip + USB extender + strain relief.** Stock **1 spare gamepad per team ($26).** |
| **Driver Hub USB port worn out** | Intermittent gamepad detection | Hundreds of plug cycles directly into the DS | **The permanently-installed USB extender.** `[H]` This is exactly the failure DECODE's blue box warns about. |
| **DS battery dies between matches** | Console won't boot | 5040 mAh and no charging outlet in the pit (§5.1: *"Power may not be available overnight"*) | **Spare `REV-31-1876` ($21.75) + charge overnight at the hotel.** |
| **DS won't connect to the RC** | Match delay, possible no-show | Remembered Wi-Fi groups, Bluetooth on, wrong device name | **R711.C/D** `[C]` — purge remembered connections, Bluetooth **off**. **R705** `[C]` — four distinct names for two teams. |
| **Console over-volume at inspection** | Fails inspection | Power bank pushed it over | **R903** counts power banks. Check with the cardboard jig **before** you leave home. |

## E2.8 Rookie-minimum vs competitive

| | **Rookie-minimum** | **Competitive** |
|---|---|---|
| DS | Storefront Driver Kit | Same + spare DS device in the box (R901 blue box permits it) |
| Gamepads | 2 (from the kit) | 2 + 1 spare, ferrites and extenders fitted |
| Console | A milk crate that fits R903 | Purpose-built case with cable management and a laminated match checklist |
| **Cost per team** | **$285** `[H]` | **$400–$650** |

---

# E3 · POWER — BATTERY, SWITCH, CHARGING, GROUNDING

## E3.1 What it is and when a design needs it

**Always, and it is the most tightly closed allowlist in the manual.** R601 permits **exactly one** approved
**12V NiMH** main battery, and it is *"the only legal source of electrical energy for the ROBOT control system and
actuation during the competition."* Table 12-4 is a **closed list by part number**. A visually identical 12V NiMH pack
from a general electronics supplier is **illegal no matter how correct its specifications are**.

> **No LiPo. No Li-ion. No LiFePO4. Not as a main battery, not ever.** `[C]` R601.
> The **only** other batteries permitted anywhere on the robot are R602 COTS USB packs (≤100 Wh, 5V/5A or 12V/5A
> via USB-PD) for **self-contained peripherals and LEDs only**, electrically isolated from the robot power system —
> *"Any device receiving signals from a REV Control or Expansion Hub must be powered by the main ROBOT battery."*

**The power system is four things, all of them mandated:**
1. **The battery** — Table 12-4 (R601)
2. **The main power switch** — exactly one, Table 12-5 (R603)
3. **The fuse** — 20A ATM mini blade, unmodified, no self-resetting substitutes (R601.A, R604)
4. **The grounding strap** — Table 12-6 (R605), the only legal way to ground electronics to the frame

## E3.2 The main variants

### Battery choice (Table 12-4 — the complete legal list, MANUAL-SOURCED `[C]`)

| Battery pack | Part number | Vendor | Price | Confidence |
|---|---|---|---|---|
| **REV 12V Slim Battery** | **`REV-31-1302`** | REV | **$60.00**, In Stock | **VERIFIED** — 3000 mAh, XT30, 16 AWG, 20A ATM replaceable fuse, 567 g, 113.5 × 90.5 × 23 mm. ⚠ **chemistry is not stated on the product page** — NEEDS-VERIFY that it is the Table 12-4 NiMH part |
| **goBILDA 12V NiMH Nested Battery** | **`3100-0012-0020`** | goBILDA | **$64.99** | **VERIFIED** — chemistry explicitly NiMH in the product name. **No note in Table 12-4.** |
| **AndyMark Flat Pack Battery DC 12V** | **`am-5290`** | AndyMark | **$54.00** | **VERIFIED** — 3000 mAh, XT30 female, 20A replaceable fuse. ⚠ *"Estimated back in stock"* — **stock risk** |
| Matrix 12V 3000 mAh NiMH | `14-0014` | Modern Robotics / MATRIX | not verified | **MANUAL-SOURCED** — Table 12-4 note: *"May be labeled as 'Modern Robotics'"* — so a battery badged **Modern Robotics** is this legal part. |
| Studica 12V 3000 mAh NiMH | `70025` | Studica | not verified | **MANUAL-SOURCED** — ⚠ studica.com returned **HTTP 403** to Phase A |
| TETRIX MAX 12V 3000 mAh NiMH | `W39057` | Pitsco / TETRIX | not verified | **MANUAL-SOURCED** — Table 12-4 note: *"Formerly 739023"*. **Do not order by the old 739023 number.** |
| WATTOS 12V Battery | `WT-NMH1230` | WATTOS | not verified | **MANUAL-SOURCED** |

**`[J]` Pick ONE model and buy them all identical, for both robots.** Identical batteries mean one charger profile,
one mounting bracket printed twice, one spare, and a rotation pool that is genuinely interchangeable between robot A
and robot B. **AndyMark `am-5290` at $54.00 is the cheapest VERIFIED legal battery**; **goBILDA `3100-0012-0020` at
$64.99 is the only one whose page explicitly states NiMH**; **REV `REV-31-1302` at $60.00 is the one bundled into the
storefront and REV kits, so you will end up owning some regardless.**

### Main power switch (Table 12-5 — closed list, MANUAL-SOURCED `[C]`)

| Power switch | Part number | Price | Confidence |
|---|---|---|---|
| **REV Switch Cable and Bracket** | **`REV-31-1387`** | **$13.00** — 20 A+ @ 12V, XT30 | **VERIFIED** (Phase A, 2026-08-21) — and **it ships inside the storefront Electronics Kit and the REV Control & Power Bundle**, so you may already own two |
| goBILDA Floodgate Power Switch | `3103-0005-0001` | not verified | **MANUAL-SOURCED** |
| AndyMark FTC Power Switch w/ Bracket | `am-4969` | not verified | **MANUAL-SOURCED** — ⚠ AndyMark collection pages did not render products this session |
| Studica On/Off Power Switch Kit | `70182` | not verified | **MANUAL-SOURCED** |
| TETRIX R/C Switch Kit | `W39129` | not verified | **MANUAL-SOURCED** |
| WATTOS Power Switch Kit | `WTS-SW1220` | not verified | **MANUAL-SOURCED** |

**R603.B** `[C]`: accessible, **away from high-speed moving parts and pinch hazards**. Mounting behind a removable
panel is permitted. **R603.C** `[C]`: secondary switches allowed **downstream** on the 12V line.
**R706.K** `[C]`: **the switch mounting bracket may be modified or replaced** — so you may 3D-print a custom bracket.
You may **not** modify the switch itself.

### Grounding strap (Table 12-6 — closed list, MANUAL-SOURCED `[C]`)

| Grounding strap | Part number | Confidence |
|---|---|---|
| **REV Resistive Grounding Strap** | **`REV-31-1269`** | **VERIFIED as a bundle line item** — ships **×2** inside the FTC Cable Bundle `REV-45-1901`, and ×1 in the storefront Electronics Kit. Standalone price not separately verified — **NEEDS-SKU-CHECK** |
| AndyMark Resistive Grounding Strap | `am-4648a` | **MANUAL-SOURCED** |
| Swyft Grounding Cable | `SR-Ground-01` | **MANUAL-SOURCED** |

**R605** `[C]`: the frame **must not carry current**; all wiring and devices electrically isolated from the frame.
Grounding electronics to the frame is permitted **only** with a Table 12-6 strap, which **must** connect directly to a
**fully COTS component with an XT30 connector** and directly to the frame **via the resistive terminal**. **R605.C:**
nothing may be designed to ground the frame to the FIELD.

> **`[J]` THE HIGHEST RELIABILITY-PER-DOLLAR PURCHASE IN THIS ENTIRE FILE.** A resistive grounding strap is a
> roughly-$10 part that prevents an ESD-induced Control Hub reboot mid-match on a dry, carpeted venue floor.
> **One per robot. Non-negotiable.** You get two free in one Cable Bundle.

### Chargers — the constraint that lives outside Section 12

**E511** (Section 5 Event Rules, p. 39) — **CONFIRMED-BIOBUZZ**, quoted verbatim:
**A.** *"Charge batteries at a safe rate, following all manufacturer recommendations,"*
**B.** *"Never charge batteries on a battery charger that exceeds a **3-amp average channel current**,"*
**C.** *"Charge batteries using safe connectors"* — *"a polarized connector corresponding to the connector on the
battery itself. Batteries must never be charged using alligator clips or similar."*

| Charger | Vendor | SKU | Price | Charge current | Confidence / E511.B verdict |
|---|---|---|---|---|---|
| **12V Slim Battery Charger** | REV | **`REV-31-1299`** (12V Slim Battery Accessories family, $6.00–$39.50) | **within $6.00–$39.50** | **switch-selectable 0.9 A or 1.8 A**; XT30 male out; IEC C13 in | **VERIFIED** (REV docs, *12V Battery Best Practices*) — ✅ **both settings are under the 3 A limit**. Ships in the REV Control & Power Bundle `REV-35-1906`. |
| **12V Battery Charger (NiCad/NiMH, XT30)** | goBILDA | **`3101-0012-0001`** | **$14.99** | **not stated on the page** | **VERIFIED** name/SKU/price; ⚠ **NEEDS-VERIFY vs E511.B before use at an event** |
| **NiMH/NiCad 12V FTC Battery Charger** | AndyMark | **`am-5473`** | **$16.00** | **not stated**; input 100–240 VAC 0.6 A; output 1.2–7.2 V (1–6S) and 8.4–18 V (7–15S); auto overcharge protection | **VERIFIED** name/SKU/price; ⚠ **NEEDS-VERIFY vs E511.B** |
| Hitec RDX2 200 AC/DC Multi-Function Smart Charger | goBILDA | `44370` | **$139.99** | **not stated; user-adjustable** | **VERIFIED** price. ⚠ **`[J]` DANGER: a programmable smart charger can be set above 3 A. If you own one, set and label the channel current and be able to show an inspector the setting.** For this program the $15 dedicated charger is the safer purchase. |
| ❌ Any 5 A "fast" NiMH charger | — | — | — | >3 A | **CONFIRMED-BIOBUZZ** — **E511.B prohibits it.** |

**`[J]` Buy the boring $15 fixed-rate chargers — two of them, one per pit, so the two teams are independent.** The
REV 0.9/1.8 A charger is the only one whose current I could verify against E511.B, so **if you want zero argument at
an event, use the REV charger.** Also note §5.1 of the manual: *"Team pits may or may not have a table and power
outlet… Power may not be available overnight for a multi-day event."* Plan charging capacity, and charge at the hotel.

## E3.3 Comparison table — power system build levels

| Build | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **Minimum legal** (1 battery, 1 switch, 1 fuse) | **5** | **5** | **5** | **2** | **5** | Passes inspection, fails a two-match block |
| **+ grounding strap** | **5** | **5** | **5** | **4** | **5** | **`[J]` The floor. R605.** |
| **+ 2 batteries/robot + 2 chargers** `[J] RECOMMENDED` | 4 | 4 | 5 | **5** | **5** | Rotation, not sequence. This is what keeps two robots practising. |
| + XT30 distribution block | 4 | 4 | 4 | 4 | 4 | ⚠ see the legality caution in E3.4 |
| + battery voltage on DS telemetry | 3 | **5** | 3 | **5** | **5** | Free (software). **Do this.** |

## E3.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **12V NiMH main battery** | AndyMark | **`am-5290`** Flat Pack | **2** | **5** (2/robot + 1 pool spare) | **$54.00 ea = $270** | Buy | **VERIFIED** — ⚠ *"estimated back in stock"* | 🕐 **R601: exactly ONE on the robot** `[C]`, but you need a rotation pool. Cheapest VERIFIED legal battery. |
| 12V NiMH main battery (alt.) | goBILDA | **`3100-0012-0020`** | 2 | 5 | **$64.99 ea = $325** | Buy | **VERIFIED** — chemistry explicitly NiMH | Second source. **Order the same model for both robots.** |
| 12V NiMH main battery (alt.) | REV | **`REV-31-1302`** 12V Slim | 2 | 5 | **$60.00 ea = $300** | Buy | **VERIFIED** — In Stock; ⚠ chemistry not stated on page | You will own some of these anyway (bundles/kits). |
| **Battery charger** | REV | **`REV-31-1299`** family | 1 | **2** | **$6.00–$39.50** | Buy | **VERIFIED** family + **0.9 A / 1.8 A** setting | ✅ **The only charger whose current I verified against E511.B.** One per pit. |
| Battery charger (alt.) | goBILDA | **`3101-0012-0001`** | 1 | 2 | **$14.99 ea = $30** | Buy | **VERIFIED** price; **NEEDS-VERIFY** current | Cheapest. Confirm ≤3 A average channel current (E511.B) `[C]` before an event. |
| Battery charger (alt.) | AndyMark | **`am-5473`** | 1 | 2 | **$16.00 ea = $32** | Buy | **VERIFIED** price; **NEEDS-VERIFY** current | Same caveat. |
| **Main power switch** | REV | **`REV-31-1387`** Switch Cable and Bracket | **1** | **2** | **$13.00 ea = $26** | Buy | **VERIFIED** | 🕐 **R603: exactly one main switch** `[C]`, from Table 12-5. **Already inside the storefront Electronics Kit and the Cable Bundle** — check the shelf first. |
| **Resistive grounding strap** | REV | **`REV-31-1269`** | **1** | **2** | ships ×2 in `REV-45-1901`; ×1 in storefront kit | Buy | **VERIFIED as a bundle line item**; standalone price **NEEDS-SKU-CHECK** | 🕐 **R605** `[C]`. **Buy one Cable Bundle and you have both.** |
| **20 A ATM mini blade fuses** | any auto-parts store, or goBILDA **Fuses** category | ATM mini blade, 20 A | 2 | **4–6** | ~$5–10 per pack | Buy | **FAMILY-ONLY** (goBILDA category verified) | 🕐 **R601.A** `[C]` permits replacement with *"a COTS equivalent in-line 20A ATM mini blade fuse."* **R604** `[C]`: **no higher trip point, no self-resetting fuses.** They blow at events. Stock a strip. |
| XT30 extension cables | REV | `REV-31-1392` (30 cm 2-pk) · `REV-31-1394` (50 cm 2-pk) | as needed | as needed | in `REV-45-1901` | Buy | **VERIFIED** as bundle contents | Battery→switch→hub runs. |
| XT30 adapters | REV | `REV-31-1385` | 0–2 | 0–4 | **$5.50–$13.50** | Buy | **VERIFIED** | |
| XT30 Power Distribution Block | REV | `REV-31-1293` | 0–1 | 0–2 | **$14.75 ea** | Buy | **VERIFIED** price; ⚠ **legality = JUDGMENT, see below** | Splits the switched 12V bus to Control Hub + SPARKmini + Servo Injector. |
| ❌ Boost / buck converter / BEC | goBILDA sells a "Voltage Regulators (BECs)" category | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R612** `[C]`: *"Altering a power pathway includes… using a boost… or buck… converter."* **That category is a trap for FTC.** Power accessories from the **+5V Aux port** (R613.D) or an isolated R602 USB pack. |
| ❌ Any 12V NiMH pack not in Table 12-4 | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R601** `[C]` is a closed allowlist **by part number**. |
| ❌ LiPo / Li-ion / LiFePO4 main battery | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R601** `[C]`. (goBILDA's 20V Li-ion charger `3101-1020-0001` $29.99 exists for their power-tool line — **not for FTC**.) |
| ❌ Relay / electromagnet / electrical solenoid | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R506** `[C]`: *"The use of relays, electromagnets, and electrical solenoid actuators is prohibited."* |

> **⚠ NEEDS-RULING — the XT30 Power Distribution Block `REV-31-1293`.** `[J]` My reading: **R608** defines a
> CUSTOM CIRCUIT as *"Any **active** electrical item that is not an actuator… or power regulation device"*; a passive
> XT30 splitting block is not an active item and does not alter voltage, so **R612** ("boost/buck… altering the
> natural variable DC voltage") does not appear to bite, and **R613.B**'s "do not combine power from multiple ports
> into a single power bus" is aimed at *regulator output ports*, not the switched main-battery bus. It is a REV part
> sold on REV's own FTC power-system page. **But V0 contains no explicit allowance.** Do **not** extend the same
> reasoning to servo-signal or servo-power distribution boards, which prior-season inspection material named as
> illegal (§E4.5). **Action: submit to Game Q&A on/after 2026-09-28 if you intend to rely on it.**

## E3.5 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Method | Material / tooling | Per robot | For 2 | Student-hours (both) |
|---|---|---|---|---|---|
| **Battery tray / retention** | 3D-printed cradle + goBILDA Cinch-Strap `2909-0102-0250` | printer, hook-and-loop strap | 1 | **2** | **2–3 h** — the battery must not move, and must come out fast between matches |
| **Power switch bracket** (if not the stock one) | 3D print | printer | 0–1 | 0–2 | **1 h** — **R706.K explicitly permits this** `[C]` |
| **Switch access cut-out + label** | hand tools, label | | 1 | 2 | **0.5 h** — R603.B accessibility |
| **Inspection access panel** | design a removable guard over the electronics bay | hand tools, M3 hardware | 1 | 2 | **2 h** — **R606** `[C]` requires regulators, wiring and fuses be *makeable visible* |
| **Battery log** (taped index card per battery: purchase date, cycle count, last capacity check) | paper + Sharpie | free | — | 5 cards | **0.5 h** — **`[J]` the cheapest way to find the one bad battery before it loses you a match** |

**≈ 6–8 student-hours for both robots.**

## E3.6 Approximate subtotals

| Line | Per robot | **For 2 robots** |
|---|---|---|
| Batteries (`am-5290` @ $54.00; 2/robot + 1 pool spare) | $108 | **$270** (5 total) |
| Charger (goBILDA `3101-0012-0001` @ $14.99) | $15 | **$30** |
| Main switch (`REV-31-1387` @ $13.00) | $13 | **$26** |
| Grounding strap | ~$10 | **~$20** (free if you buy a Cable Bundle) |
| Fuse strip (20 A ATM mini) | ~$4 | **~$8** |
| **Power subtotal** | **≈ $150** | **≈ $354** |
| *If you buy the REV charger instead* | +$25 | **+$50** |

## E3.7 Common failure modes and the spares to stock

| Failure | Symptom | Cause | Prevention / spare |
|---|---|---|---|
| **Brownout / hub reboot under load** | Robot dies when lift and drive run together | Battery internal resistance risen with age; **Control Hub input floor is 8 V** | **Rotate a fresh battery every match.** Log voltage. Retire batteries by cycle count, not by whether they "still work". |
| **Battery won't hold charge** | Fine at home, dead by match 4 | NiMH aging | REV docs, VERIFIED: *"if your 12V Slim Battery isn't holding a charge as well as it used to… it could be time to replace it."* **Budget 1 replacement battery per robot per season.** |
| **XT30 solder joints exposed** | Intermittent power, then a short | Pulling the battery out by the wire | REV docs, VERIFIED: *"Avoid pulling directly on the XT30 connector sheathing."* **Grip the connector body.** Teach this on day one. |
| **Frayed battery sheathing** | — | Abrasion against the frame | REV docs, VERIFIED: *"Do NOT use the 12V Slim Battery if the protective wire sheathing is fraying."* **Retire it.** Use grommets where wire passes through a frame hole. |
| **Blown 20 A fuse** | Total dead robot, no lights | Stall-current spike or a short | **Stock a strip of 20 A ATM mini blade fuses** and know where the fuse lives on your battery. **R604: do not substitute a bigger fuse** `[C]`. |
| **Main switch fails / wire pulls out** | Robot won't power up | Switch in a pinch zone; unsupported wiring | **R603.B** `[C]` placement. Stock **1 spare `REV-31-1387` per program ($13).** |
| **Charged the wrong way at an event** | An inspector stops you | Alligator clips, or a >3 A charger | **E511.C** `[C]`. Bring the polarised charger, not a bench supply. |

**Power spares kit for the program `[J]`:** 1 pool battery, 1 spare charger, 1 spare switch cable, 1 spare grounding
strap, 1 strip of 20 A ATM mini fuses, 2 spare XT30 pigtails.

## E3.8 Rookie-minimum vs competitive

| | **Rookie-minimum** | **Competitive** |
|---|---|---|
| Batteries | 2 per robot, 4 shared in rotation | **3 per robot, 6 in the pool**, each numbered and logged |
| Chargers | 1 shared | **2 (one per pit)** + a labelled charging station |
| Grounding | 1 strap per robot (mandatory) | Same + a documented isolation check in the pre-match routine |
| Telemetry | none | **Battery voltage on the DS screen**, plus a "swap battery" call in the drive-team checklist |
| **Cost for 2 robots** | **≈ $290** | **≈ $500** |

---

# E4 · THE WIRING HARNESS

## E4.1 What it is and when a design needs it

**Always, and it is the most under-budgeted mechanism in FTC.** The harness is everything between the battery and the
loads: gauge, colour, connectors, routing, strain relief, labelling. **It is also, empirically, the largest single
cause of mid-match failures** — a disconnect looks exactly like a code bug and costs a team two hours of the wrong
debugging.

**Three rules define the harness, and all three are inspection items:**
- **R609** `[C]` — wire **gauge** (Table 12-8)
- **R610** `[C]` — wire **colour** on the 12V main bus and +5V aux bus, **along the entire length**
- **R606** `[C]` — the harness must be **made visible for inspection**

### Table 12-8 wire sizing (R609, CONFIRMED-BIOBUZZ, p. 81)

| Application | Minimum wire size |
|---|---|
| 12V main battery power · motor power (unless listed below) · **11–20 A** fuse-protected circuit | **18 AWG** (19 SWG / 1 mm²) |
| Motor power for **TETRIX MAX 12V DC** and **REV Core Hex** · **PWM / servo** · **LEDs (5V/12V)** · ≤10 A fuse-protected circuit | **22 AWG** (22 SWG / 0.5 mm²) |
| **Signal-level circuits** (≤1 A continuous from a source incapable of >1 A: I2C, DIO, analog, encoder, RS485) | **28 AWG** (29 SWG / .08 mm²) |

Two exemptions worth money: *"Integrated wires originally attached to legal COTS devices or wires included/sold by
the manufacturer are considered part of the device and by default legal. Such wires are exempt from this rule."*
And one hard prohibition: *"Combining multiple smaller wires in parallel cannot be used to create an equivalent larger
wire."* **Buy wire with printed gauge markings** — the manual asks teams to *demonstrate* compliance for unlabeled
wire, and that is a slow, avoidable inspection argument.
**V0-ERRATA:** Table 12-8 writes the Core Hex as `REV-14-1300`; Table 12-1 says `REV-41-1300`, which is the real REV
SKU. **Do not search for REV-14-1300.**

### R610 wire colours (CONFIRMED-BIOBUZZ, p. 82)

- **Positive (+12VDC / +5V Aux):** red, yellow, white, brown, **or black-with-stripe**
- **Negative (common / GND):** black **or blue**

**Does NOT apply** to motor wiring, signal wiring, servo cables and extensions, or manufacturer-attached wires.
**Purchasing consequence: buy red and black 18 AWG for the main bus.** Do not economise with one colour plus
heat-shrink markers.

## E4.2 The main variants

| # | Variant | What it is |
|---|---|---|
| **A** | **All-bundle harness** | Buy the REV FTC Cable Bundle and use pre-made cables end to end. Zero crimping. |
| **B** | **Bundle + custom lengths** | Bundle for the standard runs; crimp your own for awkward routes. |
| **C** | **Fully custom** | Spools + connectors + crimp tools. Cheapest per foot, most skill, most failure modes. |

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **A. All-bundle** | **5** | 2 | **5** | **5** | **5** | **`[J]` THE ANSWER for the B team, and probably for both.** $220 buys a second robot's harness with no new skill. |
| **B. Bundle + custom** | 4 | 3 | 4 | 4 | 4 | The realistic A-team endpoint once slides and turrets need odd lengths |
| C. Fully custom | **1** | **5** | 2 | **2** | **2** | A crimp skill you must teach **twice** and verify **twice**. `[J]` Not for a low-mentor-hour program. |

> **`[J]` DUPLICABILITY VERDICT.** Wiring is where the build-it-twice tax is subtle: it is not the parts cost, it is
> the **skill** cost. A hand-crimped harness needs a trained student on **each** team. A bundle harness needs none.
> **For a 15-student, two-robot, low-mentor-hour program: buy the bundles.**

## E4.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **FTC Cable Bundle** `[J] BEST SINGLE BUY IN THIS SECTION` | REV | **`REV-45-1901`** | **1** | **2** | **$220.00 ea = $440** | Buy | **VERIFIED** price, In Stock, **full contents verified this session** | Contents: 2× 36 in PWM Cable 4-pk `REV-11-1130`; 1× PWM Cable Clip 10-pk `REV-11-1229`; **2× Resistive Grounding Strap `REV-31-1269`**; 1× Sensor Splitter Cable 2-pk `REV-31-1386`; **1× Switch Cable & Bracket `REV-31-1387`**; 2× JST PH 4-pin Joiner Board 4-pk `REV-31-1388`; 1× XT30 Ext 30 cm 2-pk `REV-31-1392`; 2× XT30 Ext 50 cm 2-pk `REV-31-1394`; 2× JST PH 4-pin Sensor Cable 50 cm 4-pk `REV-31-1408`; 1× JST PH 4-pin Sensor Cable 100 cm 4-pk `REV-31-1409`; 2× JST VH 2-pin Motor Cable 4-pk `REV-31-1413`; 2× JST PH 3-pin Comms Cable 50 cm 2-pk `REV-31-1418`; 2× JST VH 2-pin Joiner Board 4-pk `REV-31-1429`; 1× JST VH 2-pin Motor Cable 100 cm 4-pk `REV-31-1526`; 1× JST PH 3-pin Comms Cable 100 cm 2-pk `REV-31-1565`; 1× Zip Ties 160 mm 50-pk `REV-41-1161`. **One bundle covers the main switch AND both grounding straps.** |
| PWM / servo cables (extra) | REV | `REV-11-1130` 36 in | as needed | as needed | **$7.75–$12.50** | Buy | **VERIFIED** | 22 AWG class per Table 12-8 `[C]`. |
| JST PH 4-pin sensor cables (extra) | REV | `REV-31-1408` / `REV-31-1409` family | as needed | as needed | **$7.75–$14.75** | Buy | **VERIFIED** family | Signal-level, 28 AWG class `[C]`. |
| JST VH 2-pin motor cables (extra) | REV | `REV-31-1413` / `REV-31-1526` family | as needed | as needed | **$9.75–$22.25** | Buy | **VERIFIED** family | |
| JST joiner boards | REV | `REV-11-1277` · `REV-31-1388` · `REV-31-1429` | 1 set | 2 sets | **$6.00–$9.75** | Buy | **VERIFIED** | Extends a run **without** a crimp. **`[J]` A joiner board is a student-proof splice.** |
| Servo extension cables (TJC8) | goBILDA | **Wiring → TJC8 Servo** category | 8 | **16** | NEEDS-SKU-CHECK | Buy | **VERIFIED** category | One per servo plus spares. |
| XT30 / Anderson Powerpole connectors | goBILDA | **Wiring → XT30**, **Wiring → Anderson Powerpole** categories | 4 | **8** | NEEDS-SKU-CHECK | Buy | **VERIFIED** categories | **R601.B** `[C]` names both by name as legal battery-connector replacements. |
| 18 AWG red + black hookup wire | goBILDA **Wiring → Wire** category, or any supplier | 18 AWG stranded, **printed gauge marking** | 3 m ea colour | 6 m ea colour | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **R609 + R610** `[C]`. **Printed markings save an inspection argument.** |
| 22 AWG 3-conductor twisted (servo runs) | goBILDA | **`3806-0322-0015`** 3 conductor, 22 AWG, 15 m | 0–1 | **1 shared** | **$17.99** | Buy | **VERIFIED** | Table 12-8 PWM/servo minimum is 22 AWG `[C]`. |
| **Servo connector clips (6-pk)** | goBILDA | **`2917-0001-0001`** | **1** | **2** | **$5.99 ea = $12** | Buy | **VERIFIED** | 🕐 **`[J]` Stops the #1 cause of "the servo just stopped working."** Buy these. |
| PWM cable clips (10-pk) | REV | `REV-11-1229` | 1 | 2 | in `REV-45-1901` | Buy | **VERIFIED** as bundle content | Same job on the REV side. |
| Zip ties (100-pk) | goBILDA | **`2909-0101-0100`** | 1 | **2** | **$4.99 ea = $10** | Buy | **VERIFIED** | |
| Cinch-Straps hook & loop (4-pk) | goBILDA | **`2909-0102-0250`** | 2 | **4** | **$3.99 ea = $16** | Buy | **VERIFIED** | **`[J]` Best battery retention method there is** — and re-openable between matches. |
| Grommets | goBILDA | **`2911-0014-0001`** plastic 12-pk · **`2911-0014-0003`** rubber 14 mm 4-pk | 1 ea | **2 ea** | **$3.99 ea ≈ $16** | Buy | **VERIFIED** | Wire through a frame hole **without chafing**. Directly prevents the frayed-sheathing failure. |
| Braided cable sleeve (3 m) | goBILDA | **`2925-0008-3000`** | 1 | **2** | **$5.99 ea = $12** | Buy | **VERIFIED** | **R606** `[C]`: the electrical system must be **inspectable**. Tidy wiring is a rules requirement, not vanity. |
| Heat-shrink tubing | goBILDA | **`3201-0005-0001`** | — | **1** | **$9.99** | Buy | **VERIFIED** | **R504.E** `[C]`: *"insulation may be applied to electrical terminals."* |
| Cable-carrier chain (1 m) | goBILDA | **`2924-1015-1000`** | 0–1 | **0–2** | **$19.99 ea** | Buy | **VERIFIED** | For wiring that must cross an **extending** mechanism. **Buy after Kickoff**, once R105 expansion is known. |
| Crimp tool (variant C only) | any | Ratcheting crimper for XT30 / JST / Dupont | 0–1 | **1 shared** | UNVERIFIED | Buy | **FAMILY-ONLY** | **`[J]` A cheap non-ratcheting crimper produces exactly the failure you are trying to avoid. If you crimp, buy a ratcheting tool — or don't crimp.** |
| Wire labels / label maker | any | heat-shrink or wrap-around labels | 1 set | 2 sets | UNVERIFIED | Buy | **FAMILY-ONLY** | **R706.D** `[C]` permits labels *"as long as they do not cover labels or markings used to identify the product."* |

## E4.4 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Method | Material / tooling | Per robot | For 2 | Student-hours (both) |
|---|---|---|---|---|---|
| **Route plan + harness build** | Lay the harness out before mounting mechanisms | patience | 1 | 2 | **6–10 h** — the real number; budget it |
| **Cable-management clips** | 3D print, mount to the chassis grid | printer | 8–15 | 16–30 | **2 h** |
| **Strain-relief anchors at every connector** | Zip tie to a printed post within ~50 mm of each connector | printer, zip ties | 10–20 | 20–40 | **2–3 h** — **the single highest-value fabrication in this file** |
| **Slide / turret service loop** | Cable-carrier chain, or a deliberate loop anchored at both ends | `2924-1015-1000` | 0–1 | 0–2 | **1–2 h** |
| **Colour-coded, labelled main bus** | Red/black 18 AWG, labelled both ends | wire, labels | 1 | 2 | **1 h** — **R610** `[C]` |
| **Laminated wiring diagram of the ACTUAL robot** | Draw it; do not use a stock diagram | paper | 1 | **2** | **2 h** |

**≈ 14–20 student-hours across both robots.** **`[J]` Build robot A's and robot B's harness in the same session,
side by side, so the layouts are identical.** Identical harnesses mean a fix found on one applies to both, and a spare
cable cut for one fits the other.

## E4.5 ⚠ DO-NOT-BUY — servo signal and power "helpers"

**HISTORICAL `[H]` + CONFIRMED-BIOBUZZ `[C]`.** The DECODE **Inspection Quick Reference** (rev 25-26.2, in
`ROOT/manuals/archive/supplemental/2025-26_DECODE_InspectionQuickReference.pdf`) carries a section headed
**"Illegal Servo Power or Servo Signal Adjusters"**, stating: *"Devices that generate or alter servo signals cannot be
used to control servos, servos can only be controlled by core power regulating devices (REV Control Hub, REV Expansion
Hub, REV Servo Hub)."* It names three devices as **ILLEGAL**, and BIOBUZZ **R612**'s blue box independently names the
first one.

**All of these are on sale on goBILDA's servo-electronics page today, at prices that look like a bargain
(all prices VERIFIED on `gobilda.com/servo-electronics/` 2026-08-22):**

| Product | goBILDA SKU | Price | Status |
|---|---|---|---|
| **Servo Travel Tuner** | `3109-0002-0001` | **$19.99** | ❌ **ILLEGAL** — named in **BIOBUZZ R612 blue box** `[C]` *and* the DECODE IQR `[H]` |
| **Servo Power Distribution Board (8 Channel)** | `3108-2827-0801` | **$17.99** | ❌ **ILLEGAL** per DECODE IQR `[H]`; **not in Table 12-3** `[C]`; conflicts with **R613.B** `[C]` |
| **4 Channel Servo Extension via CAT6** | `3802-2745-4527` | **$29.99** | ❌ **ILLEGAL** per DECODE IQR `[H]` |
| Servo Speed Tuner | `3109-0009-0001` | $19.99 | ❌ **`[J]` Same class** — **R612**: *"Devices that modify actuator control signals or power (except those allowed by R505) are prohibited"* `[C]` |
| Servo Travel Reverser | `3109-0007-0001` | $13.99 | ❌ **`[J]` Same class** |
| Servo Monitor | `3109-0005-0002` | $24.99 | ⚠ **NEEDS-RULING `[J]`** — monitoring *may* fall under R612's high-impedance-monitoring allowance, but it sits in an in-line signal path. Do not rely on it. |
| Servo Commander 1 ch / 2 ch | `3109-0004-0002` $29.99 · `3109-0003-0001` $59.99 | | ❌ **`[J]`** Generates servo signals outside the RC — **R701** makes the ROBOT CONTROLLER *"the only source of control for the ROBOT actuators."* `[C]` |
| Servo Joystick (2 ch) · Servo Recorder (4 ch) | `3109-0008-0001` $79.99 · `3109-0006-0001` $119.99 | | ❌ **`[J]` Same reasoning.** |
| Signal-Boosting Servo Extension | `3116-1718-0300` | $13.99 | ⚠ **NEEDS-RULING `[J]`** — "boosting" a signal is the exact language R612 targets. Assume illegal. |

**Legal and useful from the same page:** the **Servo Power Injector `3125-0001-0001` ($69.99)** — it is in Table 12-3
`[C]` and is a **signal pass-through** device — and the **bench** programmers (**Axon Servo Programmer MK2**
`3102-0002-0001` $59.99; **goBILDA 2000-series Dual Mode Servo Programmer** `3102-0001-0001` $12.99; **Hitec DPC-11**
`44429` $25.99), which configure a servo **off the robot** and are covered by **R504.C**, *"servos may be modified as
specified by the manufacturer (e.g., setting soft limits or modification for continuous rotation)."* `[C]`
REV's equivalent bench tool is the **SRS Programmer `REV-31-1108` $25.00** (VERIFIED).

> **`[J]` This is a $100+ trap sitting inside one vendor category, in a program that has to buy everything twice.
> Print this table and tape it above the shop computer.**

## E4.6 Approximate subtotals

| Line | Per robot | **For 2 robots** |
|---|---|---|
| FTC Cable Bundle `REV-45-1901` | **$220** | **$440** |
| goBILDA consumables (zip ties, Cinch-Straps, grommets, servo clips, sleeve, heat shrink) | ≈ $30 | **≈ $60** |
| Extra servo extensions / spare cables | ≈ $25 | **≈ $50** |
| 18 AWG red/black + 22 AWG twisted | ≈ $15 | **≈ $30** (one 15 m spool covers both) |
| Cable-carrier chain (if an extending mechanism) | $20 | **$40** |
| **Wiring subtotal** | **≈ $290–$310** | **≈ $580–$620** |
| *Variant C (spools + crimper) instead* | ≈ $110 | **≈ $220, plus a ratcheting crimper, 20 student-hours and risk** |

## E4.7 Common failure modes and the spares to stock

| Failure | Symptom | Cause | Prevention / spare |
|---|---|---|---|
| **Servo "randomly stops working"** | One servo dead; comes back if you wiggle it | **PWM connector backed out of the header** | **goBILDA servo connector clips `2917-0001-0001`** / REV PWM cable clips `REV-11-1229`. **The most common single failure in FTC.** |
| **Mid-match disconnect** | Robot freezes; DS shows lost comms | Motor or battery lead pulled at the connector under vibration | **Strain relief within 50 mm of every connector.** Anchor, don't tension. |
| **Brownout when two mechanisms run together** | Hub reboots, or servos jitter | Sag on an aged battery, **or exceeding 2 A per servo port pair** | See **E5**. Rotate batteries; split heavy servos across port pairs. |
| **Wire chafed through at a frame hole** | Intermittent short, blown fuse | No grommet | **Grommets `2911-0014-0001` / `2911-0014-0003`.** |
| **Wire severed by an extending slide** | Sudden total loss of a mechanism | No service loop on a moving joint | **Cable-carrier chain `2924-1015-1000`**, or a properly anchored service loop. |
| **Failed inspection on gauge or colour** | Delay on inspection day | Unlabeled spool wire; single-colour main bus | **R609 / R610** `[C]`. Buy gauge-printed red and black. |
| **Failed inspection on accessibility** | Delay | Electronics buried under a bolted-on guard | **R606** `[C]` — design the access panel in from the start. |

**Wiring spares kit `[J]`:** 4 servo extensions, 2 PWM cables, 2 JST PH sensor cables, 2 JST VH motor cables, 1 XT30
extension, 1 pack of joiner boards, 20 A ATM fuses, zip ties, servo connector clips, heat shrink, electrical tape —
and **a spare of every cable you had to make by hand**.

## E4.8 Rookie-minimum vs competitive

| | **Rookie-minimum** | **Competitive** |
|---|---|---|
| Harness | 1 shared Cable Bundle, cables reused as-is | **1 Cable Bundle per robot**, plus custom lengths for tight routes |
| Strain relief | Zip ties | Printed anchors at every connector + connector clips on every servo |
| Labelling | None | Every cable labelled at both ends; laminated diagram in the pit |
| Documentation | — | Photo of the finished harness on a phone, so a rebuild at an event is a copy job |
| **Cost for 2 robots** | **≈ $300** | **≈ $620** |

---

# E5 · MOTORS AND SERVOS AS ELECTRICAL LOADS — CURRENT, SAG AND BROWNOUT

> This is not a purchasable mechanism; it is the **analysis that decides whether the mechanisms you did buy still work
> in match 4 on a warm afternoon.** For motor and servo *legality and part numbers*, see
> `LEGAL-PARTS-CONSTRAINTS.md` §2–§4. This section covers only their behaviour as electrical loads.

## E5.1 The four hard numbers

| Number | Value | Source | Why it matters |
|---|---|---|---|
| **Main battery** | 12V NiMH, typically **3000 mAh** | Table 12-4 `[C]`; capacities **VERIFIED** on `am-5290`, `REV-31-1302`, `3100-0012-0020` | The whole robot runs off this. There is **no second battery** for actuators (R601; R602.A) `[C]` |
| **Control Hub input range** | **8–15 V** | **VERIFIED** REV docs | Sag below ~8 V ⇒ **the hub browns out and reboots.** That is the failure. |
| **Motor port current** | **10 A continuous, 20 A absolute max** | **VERIFIED** REV docs | Two motors on one port (Table 12-3) **share this budget** `[C]` |
| **Servo power** | **+5V aux: 5 A total shared across servo and power ports; 2 A max per servo port pair** | **VERIFIED** REV docs | **The number that surprises teams.** Four high-torque servos on adjacent ports can exceed it. |

**And the rule that sets servo voltage — R502 blue box, CONFIRMED-BIOBUZZ, verbatim:**
> *"The REV Control Hub and REV Expansion Hub provide **5V** to servos, and the goBILDA Servo Power Injector,
> REV Servo Power Module, Studica Servo Power Block, and REV Servo Hub provide **6V** to servos. While virtually all
> servos are compatible with 6V, servos with an operating voltage range of 6-8.4 DCV, for example, may not work
> properly when only provided 5V."*

> **⚠ THE PURCHASE THIS CHANGES.** A servo rated **6–8.4 V** plugged into the Control Hub's **5V** servo ports may
> under-perform or not work at all. Either buy servos happy at 5V, **or** budget a **Servo Hub `REV-11-1855` ($90)**
> or **goBILDA Servo Power Injector `3125-0001-0001` ($69.99)** — **× 2 robots, i.e. $140–$180.**
> **Check the servo's voltage range BEFORE you buy it. Twice.**

## E5.2 How the 8+8 budget interacts with battery sag `[J]`

R503 caps you at **8 motors and 8 servos**. Nothing caps *simultaneous current*. The practical envelope:

| Simultaneous load | Rough draw | Effect on a healthy 12V NiMH |
|---|---|---|
| 4-motor drivetrain cruising | moderate | fine |
| 4-motor drivetrain **pushing / against a wall** | **near stall on all four** | **the classic brownout trigger** |
| Drivetrain + a 2-motor lift accelerating together | additive | brownout on an aged battery |
| 6–8 servos all commanded to a new position at once | several amps on the 5V rail | **jitter, servo reset, or the 2 A/port-pair limit hit** |

**Design rules that cost nothing `[J]`:**
1. **Never command drive and a heavy lift to full power in the same code path.** Ramp one.
2. **Current-limit in software** — the SDK exposes motor current; cap it rather than discovering that the fuse does.
3. **Spread heavy servos across different port pairs** — the 2 A limit is *per pair*, not per port.
4. **Stall detection with a timeout** on every mechanism that can hit a hard stop, so a pinned motor does not sit at
   stall current for 30 seconds.
5. **Put battery voltage on the DS telemetry screen** and make "swap the battery" a drive-team call, not a hope.
6. **A fresh battery every match** — a *procurement* decision (E3) disguised as a driving tip.

## E5.3 What is legal to do about it, and what is not

| Fix | Legal? | Rule |
|---|---|---|
| Software current limiting / ramping | ✅ Yes | no rule against it |
| Fresh battery every match | ✅ Yes | R601 permits one battery **on the robot**; the pool lives in the pit `[C]` |
| Splitting servos across port pairs | ✅ Yes | R613.B `[C]` — just do not cross-wire *power* between ports |
| Adding a 6V Servo Power Injector / Servo Hub | ✅ Yes | Tables 12-3 and 12-7 `[C]` — powered **only** from the main battery via the specified connector |
| A bulk capacitor across the 12V bus to ride out sag | ⚠ **NEEDS-RULING `[J]`** | R612 forbids custom circuits altering power pathways; a bulk cap is arguably passive but sits in the path. **Ask Q&A.** |
| **A buck / boost converter to hold 12V steady** | ❌ **NO** | **R612** `[C]` names boost and buck converters explicitly |
| **A second battery to feed the actuators** | ❌ **NO** | **R601** `[C]`; **R602.A** forbids USB packs supplying actuators |
| **A higher-rated or self-resetting fuse** | ❌ **NO** | **R604** `[C]` |
| **A relay or solenoid to latch a mechanism instead of holding it with a motor** | ❌ **NO** | **R506** `[C]` — relays, electromagnets and electrical solenoid actuators are prohibited |
| **Gas springs / constant-force springs to unload a lift motor** | ✅ **YES** | **R801.A** `[C]` permits *"sealed, COTS closed-air systems which are pre-charged by the manufacturer (such as gas shocks)"* — **`[J]` the best legal answer to a lift that browns out is to make the motor lift less** |

## E5.4 Motor / servo electrical spares `[J]`

Per **program** (not per robot): **1 spare motor**, **2 spare servos** of the models you actually used, 4 spare servo
extensions, and the matching mounting hardware. `LEGAL-PARTS-CONSTRAINTS.md` §2.5 / §4.5 carries the verified motor and
servo purchasing tables — that decision is not duplicated here.

## E5.5 Rookie-minimum vs competitive

| | **Rookie-minimum** | **Competitive** |
|---|---|---|
| Brownout strategy | Fresh battery, don't drive into walls | Software current limits, ramping, stall timeouts, voltage telemetry, gas-spring assist on the lift |
| Servo voltage | 5V hub ports, servos chosen to suit | 6V via Servo Hub / Injector where the servo spec demands it |
| Instrumentation | none | Per-motor current logged to the DS during practice |
| **Added cost for 2 robots** | **$0** | **$140–$180** (2 × servo power device) |

---

# E6 · PROPRIOCEPTIVE SENSING — ENCODERS, IMU, ODOMETRY

## E6.1 What it is and when a design needs it

**Proprioception** is the robot knowing where its own parts are and where it is on the field. Every design needs
*some* of it; the level is a strategy decision that only becomes clear after Kickoff.

| Need | Minimum sensing |
|---|---|
| A lift that must stop at a repeatable height | **Motor encoder** (built into every legal FTC gearmotor via the hub's encoder port) |
| A drivetrain that must drive a known distance in autonomous | **Motor encoders + IMU heading** |
| A drivetrain that must reach an exact pose in autonomous | **Dead-wheel odometry** or **optical tracking** |
| An arm that must know its absolute angle at power-on | **Through-bore absolute encoder** or a **limit switch homing routine** |

**The free win:** the **Control Hub contains 1 internal 6-axis IMU** (VERIFIED on `revrobotics.com/rev-31-1595/`),
and its **4 motor ports have built-in encoder ports** (VERIFIED). **A Control Hub build gets encoders and a heading
source for $0.** Do not buy a separate IMU for a Control Hub robot.

**The rule that matters most here is a permission, not a restriction.** **R501** `[C]`: *"Motors integral to a COTS
sensor (e.g., LIDAR, scanning sonar), provided the device is not modified except to facilitate mounting. **These
motors do not count toward the limit in R503.**"* So a scanning sensor's own motor is free of the 8-motor budget.
And **R702 Examples 2, 3 and 4** `[C]` explicitly allow the **SparkFun OTOS**, the **Digital Chicken Labs OctoQuad
FTC Edition**, and **optical flow sensors**.

## E6.2 The main variants

| # | Variant | What it is | Legality |
|---|---|---|---|
| **A** | **Motor encoders only** | Quadrature encoders integral to the gearmotor, read on the hub's motor port | Integral to a legal actuator `[C]` |
| **B** | **Motor encoders + Control Hub internal IMU** | Adds heading | R701.A hardware `[C]` |
| **C** | **Dead-wheel odometry pods** (2 or 3 unpowered tracking wheels + a computer) | Decouples position from wheel slip | Sensors; not actuators `[C]` |
| **D** | **Optical tracking (SparkFun OTOS)** | Laser + IMU, sees the tile surface | **R702 Example 2: *"This device is allowed"*** `[C]` — **but its software must not be modified**; binary firmware updates OK |
| **E** | **Through-bore absolute encoder** on an arm/turret shaft | Knows absolute angle at power-on | Sensor `[C]` |
| **F** | **External encoder interface (OctoQuad FTC Edition)** | 8 channels of encoder/PWM off one I2C bus | **R702 Example 3: *"This device is allowed"*** `[C]` |

### Comparison table

| Variant | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **A. Motor encoders** | **5** | **5** | 4 | **5** | **5** | **The floor. Free. Use them.** |
| **B. + internal IMU** | **5** | **5** | 4 | **4** | **5** | **`[J]` The right answer for the B team.** Free with the Control Hub. |
| **C. Dead-wheel odometry** | 2 | 2 | **2** | 4 | **3** | Best accuracy. **$280 × 2 robots and a mounting problem × 2.** A-team only. |
| **D. Optical tracking (OTOS)** | 3 | 3 | 3 | 3 | **4** | One $85 part, one bolt, one I2C cable. **`[J]` The value pick if odometry matters and the budget doesn't stretch to pods twice.** ⚠ needs a **10 mm** standoff from the tiles. |
| **E. Through-bore encoder** | 4 | 4 | 4 | **5** | **5** | **`[J]` Buy one per articulated arm/turret.** Kills the "re-home after every reboot" problem. |
| **F. OctoQuad** | 3 | 3 | 3 | 4 | 4 | Only if you run out of encoder inputs. Rare under R503's 8-motor cap. |

## E6.3 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Motor encoders** | — | **integral to every legal FTC gearmotor**; read on the Control Hub's 4 motor ports | 4–8 | 8–16 | **$0 extra** | Buy (with the motor) | **VERIFIED** — Control Hub motor ports have *"built-in encoder ports"* | 🕐 Buy motors **with** encoders. A cheaper encoder-less motor is a false economy. |
| **IMU (Control Hub build)** | REV | **built in — `1 × Internal 6-axis IMU`** | **0 to buy** | **0** | **$0** | — | **VERIFIED** on `revrobotics.com/rev-31-1595/` | 🕐 **Do NOT buy a separate IMU for a Control Hub robot.** |
| **9-Axis IMU** (phone + Expansion Hub builds, or a second reference) | REV | **`REV-31-3332`** | 0–1 | 0–2 | **$38.00 ea** | Buy | **VERIFIED** — In Stock | Only needed if you are on the R701.B path, or want an independent heading source. |
| Adafruit BNO055 IMU | Adafruit | BNO055 Absolute Orientation Sensor | 0–1 | 0–2 | not verified | Buy | **CONFIRMED-BIOBUZZ** legality — **R702 Example 1: *"This device is allowed"*** | NEEDS-SKU-CHECK on price/stock. |
| **Through Bore Encoder V1** | REV | **`REV-11-1271`** | 0–2 | 0–4 | **$40.80** (sale; was $48.00) | Buy | **VERIFIED** | **`[J]` The single best sensing purchase for any articulated arm or turret.** |
| Through Bore Encoder insert pack | REV | **`REV-25-1870`** | 0–1 | 0–2 | **$4.00 ea** | Buy | **VERIFIED** | Adapts the bore to your shaft. Buy with the encoder. |
| **Optical tracking odometry sensor** | SparkFun | **`SEN-24904`** OTOS (PAA5160E1, Qwiic/I2C) | 0–1 | 0–2 | **$84.95 ea = $170** | Buy | **VERIFIED** — In Stock; FTC Java library published | 🕐 **R702 Example 2** `[C]`: allowed, **but *"SparkFun does provide the source code and toolchain… which is not permitted by this rule."* Use it; do not recompile its firmware.** ⚠ must sit **exactly 10 mm** from the tiles — that's a fabricated bracket, ×2. |
| **Odometry computer** | goBILDA | **`3110-0002-0002`** Pinpoint V2 | 0–1 | 0–2 | **$79.99 ea** | Buy | **VERIFIED** | Fuses two pods + IMU into a pose. Sensor, not actuator. |
| **Odometry pack** (2 pods + 1 computer) | goBILDA | **`3203-3110-0002`** 4-Bar · **`3203-3110-0001`** Swingarm | 0–1 | **0–2** | **$279.99 ea = $560** | Buy | **VERIFIED** | 🕐 **The single most expensive optional sensing purchase, and it doubles.** A-team only. |
| Odometry pod (individual) | goBILDA | **`3110-0001-0002`** 4-Bar · **`3110-0001-0001`** Swingarm | 0–3 | 0–6 | **$99.99 ea** | Buy | **VERIFIED** | Cheaper to buy the pack than 2 pods + a computer separately. |
| **Potentiometer** (cheap absolute angle) | REV | **`REV-31-1155`** | 0–2 | 0–4 | **$15.25 ea** | Buy | **VERIFIED** | **`[J]` The $15 rookie alternative to a $41 through-bore encoder.** Lower resolution, limited travel, perfectly adequate for a 4-position arm. |
| OctoQuad FTC Edition | Digital Chicken Labs | OctoQuad FTC Edition | 0–1 | 0–2 | not verified | Buy | **CONFIRMED-BIOBUZZ** legality — **R702 Example 3: *"This device is allowed"*** | NEEDS-SKU-CHECK. Rarely needed under an 8-motor cap. |
| JST PH 4-pin sensor cables | REV | `REV-31-1408` / `REV-31-1409` | 1 set | 2 sets | in `REV-45-1901` | Buy | **VERIFIED** | **R609** signal-level 28 AWG class `[C]`. |
| ❌ A second hub used only to power a sensor | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R613.A** `[C]`: *"sensors, encoders, and other devices must be powered solely by the power regulation device they are connected to."* |

## E6.4 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Method | Material / tooling | Per robot | For 2 | Student-hours (both) |
|---|---|---|---|---|---|
| **Sensor brackets** (IMU, encoder, potentiometer) | 3D print | printer | 2–4 | 4–8 | **2–3 h** |
| **OTOS 10 mm standoff bracket** | 3D print to a measured height, sprung or rigid | printer, calipers | 0–1 | 0–2 | **2–3 h** — ⚠ **the height is the whole accuracy story; measure it, don't eyeball it** |
| **Odometry pod mounts** | 3D print or cut plate; must hold the pod square and sprung to the tile | printer / hand tools | 0–2 | 0–4 | **4–6 h** — **the real cost of odometry is this bracket, twice** |
| **Through-bore encoder shaft adapter** | Printed insert or the REV insert pack | printer | 0–2 | 0–4 | **1–2 h** |
| **Limit-switch homing hard stops** | Printed or cut tabs | printer / hand tools | 2–4 | 4–8 | **2 h** — see E7 |
| **Sensor calibration procedure** (written down) | Doc | free | 1 | **1 shared** | **2 h** — **`[J]` write it once, run it on both robots** |

**≈ 8–16 student-hours across both robots**, dominated by odometry-pod mounting if you take that path.

## E6.5 Approximate subtotals

| Level | Per robot | **For 2 robots** |
|---|---|---|
| **Encoders + internal IMU only** | **$0** | **$0** |
| + 1 through-bore encoder + insert | $45 | **$90** |
| + potentiometer instead | $15 | **$30** |
| + SparkFun OTOS | $130 | **$260** |
| + goBILDA odometry pack | $325 | **$650** |
| **`[J]` Recommended: B team encoders+IMU, A team + OTOS + 1 through-bore** | A: $130 / B: $0 | **≈ $175 for the program** |

## E6.6 Common failure modes and the spares to stock

| Failure | Symptom | Cause | Prevention / spare |
|---|---|---|---|
| **Encoder counts drift or invert** | Autonomous walks off course | JST cable partly unseated; motor rewired with reversed polarity | Cable clips; **label motor leads at both ends**; a "verify encoder direction" step in the pre-match checklist |
| **IMU heading drifts over a match** | Field-centric drive rotates slowly | Integration drift; hub not mounted rigidly | Re-zero at a known heading in autonomous; **mount the hub rigidly, not on a compliant plate** |
| **Odometry pod bounces off the tile** | Position error that grows with aggressive driving | Insufficient spring preload; bracket flex | Sprung mount; verify with a push test on the practice field |
| **OTOS reads garbage** | Position freezes or jumps | Height not 10 mm; dust on the lens; over a field seam | **Measure the standoff with calipers.** Keep a lens wipe in the pit kit. |
| **Absolute encoder loses its zero** | Arm goes to the wrong preset after a reboot | Encoder is incremental, not absolute; or the coupling slipped | Through-bore absolute encoder, **or** a limit-switch homing routine on every power-up |
| **I2C bus lockup** | One sensor takes out several | Two devices sharing an address, or a long unshielded run | The Control Hub has **4 independent I2C buses** (VERIFIED) — **spread devices across them.** |

**Sensing spares `[J]`:** 1 spare through-bore encoder *or* potentiometer, 4 spare JST PH sensor cables, 1 spare
odometry pod if you run pods (they are the part that gets hit).

## E6.7 Rookie-minimum vs competitive

| | **Rookie-minimum (B team)** | **Competitive (A team)** |
|---|---|---|
| Localisation | Motor encoders + Control Hub internal IMU, with time-based autonomous fallbacks | OTOS or dead-wheel pods; encoder + IMU fusion |
| Arm position | Encoder + limit-switch homing on power-up | Through-bore absolute encoder |
| Cost | **$0** | **$130–$325** per robot |
| **Honest verdict `[J]`** | **Free sensing plus a reliable 10-second autonomous beats expensive sensing plus an unfinished one.** Do not buy odometry for the B robot. | Odometry pays only if someone owns the tuning and the practice field time to prove it |

---

# E7 · EXTEROCEPTIVE SENSING — DISTANCE, COLOUR, TOUCH, MAGNETIC

## E7.1 What it is and when a design needs it

Sensing the **world**, not the robot: how far away a wall is, what colour a game element is, whether a mechanism has
reached its end of travel. These are cheap, small, low-risk parts — and the **touch/limit switch is the single
highest-value sensor in FTC** because it turns "hope the arm stops" into "the arm stops".

**One rule constrains what you may buy — R710** `[C]`: **lasers are only allowed if they are (A) part of a sensor,
(B) rated IEC/EN 60825-1 Class I or Exempt, and (C) non-visible spectrum.** A **time-of-flight distance sensor**
(REV 2m Distance Sensor, goBILDA Laser Distance Sensor) satisfies all three as sold. **A visible-red laser pointer
used as a driver aiming aid does not** — it fails (A) and (C).

**And R613.A** `[C]`: *"sensors, encoders, and other devices must be powered solely by the power regulation device
they are connected to."* You may not run a sensor from a separate supply.

## E7.2 The main variants and what each is for

| Sensor | What it answers | Typical use | Legality |
|---|---|---|---|
| **Touch / limit switch** | "Has it reached the end?" | Lift zeroing, arm homing, intake occupancy | Sensor, digital `[C]` |
| **Magnetic limit switch** | Same, without physical contact | Where a lever would be crushed or fouled | Sensor, digital `[C]` |
| **Time-of-flight distance** | "How far to that wall/element?" | Wall alignment, element detection, autonomous approach | Sensor; **R710 satisfied as sold** `[C]` |
| **Colour / RGB + proximity** | "What colour is this element?" | Alliance-element sorting, line detection on tiles | Sensor, I2C `[C]` |
| **Potentiometer** | "What angle is this joint at?" | Cheap absolute arm angle | Sensor, analog `[C]` |
| **Digital LED indicator** | Human-readable state on the robot | "Ready to score" signalling to the driver | Output; see the LED note below |

**LED note `[C]`:** LEDs are the one place **R607** relaxes — CUSTOM CIRCUITS *"shall not provide regulated output
voltages exceeding 5V, **except if solely used for powering LEDs**."* But **R613.C** is the trap: **6V from a servo
power module or injector may power servos ONLY — not LEDs.** And **R609/Table 12-8** puts LEDs in the **22 AWG**
class `[C]`.

## E7.3 Comparison table

| Sensor | Complexity | Cost | Tuning burden | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **Touch sensor** | **5** | **5** | **5** | **5** | **5** | **`[J]` Buy 4 per robot. Best value in the catalog.** |
| Magnetic limit switch | 4 | 3 | 4 | **5** | **5** | For crushed/fouled positions |
| **2m distance sensor** | 4 | 3 | 3 | 4 | **5** | Great for wall alignment; **poor at long range on dark or shiny surfaces** |
| Colour sensor V3 | 4 | 4 | **2** | 3 | **5** | **`[J]` Tuning burden is the real cost** — venue lighting changes the reading. Shroud it. |
| Colour sensor V2 | 4 | **5** | 2 | 3 | **5** | Half the price, older part. Fine for line detection. |
| Potentiometer | **5** | 4 | 4 | 4 | **5** | Cheap absolute angle |
| Digital LED indicator | **5** | 4 | **5** | **5** | **5** | Driver feedback for $3.70 a channel |

## E7.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **FTC Sensor Bundle** `[J] BEST VALUE HERE` | REV | **`REV-45-1885`** | **1** | **2** | **$180.00 ea = $360** | Buy | **VERIFIED** price, In Stock, **full contents verified** | Contents: **2× 2m Distance Sensor `REV-31-1505`**, **2× Color Sensor V3 `REV-31-1557`**, **2× Touch Sensor `REV-31-1425`**, 1× JST PH 4-pin Joiner Board 4-pk `REV-31-1388`, 1× JST PH 4-pin Sensor Cable 100 cm 4-pk `REV-31-1409`, **2× Magnetic Limit Switch `REV-31-1462`**, 1× Digital LED Indicator 4-pk `REV-31-2010`. **À-la-carte the same contents ≈ $190** — the bundle is a small saving **plus** the cables, so buy the bundle. |
| **Touch sensor** | REV | **`REV-31-1425`** | **2–4** | **4–8** | **$8.75 ea** | Buy | **VERIFIED** | 🕐 **`[J]` The highest-value sensor in FTC.** Every lift and arm should home against one. |
| **Magnetic limit switch** | REV | **`REV-31-1462`** | 0–2 | 0–4 | **$17.50 ea** | Buy | **VERIFIED** | Non-contact end-stop. |
| **2m distance sensor** | REV | **`REV-31-1505`** | 1–2 | 2–4 | **$31.50 ea** | Buy | **VERIFIED** | Time-of-flight; **R710 satisfied as sold** `[C]`. |
| Laser distance sensor (1 m, digital or analog) | goBILDA | **`3124-0001-0001`** | 0–2 | 0–4 | **$29.99 ea** | Buy | **VERIFIED** | 3.3–5V. Alternative to the REV part; check the interface you need. |
| **Colour sensor V3** | REV | **`REV-31-1557`** | 1 | 2 | **$20.75 ea** | Buy | **VERIFIED** | RGB + proximity. **Also ships in the storefront Electronics Kit.** |
| Colour sensor V2 (budget) | REV | **`REV-31-1537`** | 1 | 2 | **$13.50 ea** | Buy | **VERIFIED** | Older, cheaper, adequate for line detection. |
| **Potentiometer** | REV | **`REV-31-1155`** | 0–2 | 0–4 | **$15.25 ea** | Buy | **VERIFIED** | Cheap absolute joint angle. |
| Digital LED indicator (4-pk) | REV | **`REV-31-2010-PK4`** | 0–1 | 0–2 | **$14.75 ea** | Buy | **VERIFIED** | Driver-facing state. Also in the Sensor Bundle. |
| 5V addressable LED strip, 1 m | REV | **`REV-11-1198`** | 0–1 | 0–2 | **$26.00 ea** | Buy | **VERIFIED** | **R607** `[C]` permits >5V regulated **only** for LEDs; **R613.C** forbids feeding LEDs from 6V servo power; Table 12-8 puts LEDs at **22 AWG** `[C]`. |
| 12V RGB LED strip, 5 m | REV | **`REV-11-1197`** | 0–1 | 0–2 | **$28.75 ea** | Buy | **VERIFIED** | Same rule set. |
| Blinkin LED driver | REV | **`REV-11-1105`** | 0–1 | 0–2 | **$49.68 ea** | Buy | **VERIFIED** price | ⚠ **NEEDS-RULING `[J]`** — it is an LED *controller* driven from a PWM/servo port. It is **not in Table 12-3**, and it is not an actuator power regulator, so it is arguably a CUSTOM CIRCUIT under R608 driving LEDs (which R607 expressly permits). **Ask Q&A before relying on it.** Blinkin LED cable adapter `REV-11-1196` $4.00 (VERIFIED). |
| JST PH 4-pin sensor cables | REV | `REV-31-1408` (50 cm) / `REV-31-1409` (100 cm) | 1 set | 2 sets | **$7.75–$14.75** | Buy | **VERIFIED** | In both bundles. |
| Sensor splitter cable (2-pk) | REV | `REV-31-1386` | 1 | 2 | in `REV-45-1901` | Buy | **VERIFIED** as bundle content | Two sensors on one hub port where the bus allows. |
| ❌ Visible-spectrum laser pointer as a driver aid | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R710** `[C]` — fails "part of a sensor" and "non-visible spectrum". |
| ❌ Sensor powered from a USB pack or a second hub | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R613.A** and **R602.B** `[C]`. |

## E7.5 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Method | Material / tooling | Per robot | For 2 | Student-hours (both) |
|---|---|---|---|---|---|
| **Limit-switch actuation tabs and hard stops** | 3D print or cut aluminium | printer / hand tools | 2–4 | 4–8 | **2–3 h** — **the switch is useless without a repeatable striker** |
| **Colour-sensor shroud** | 3D print an opaque hood | printer | 0–1 | 0–2 | **1–2 h** — **`[J]` this is what makes a colour sensor survive a change of venue lighting** |
| **Distance-sensor bracket** (square to the target, clear of the frame) | 3D print | printer | 1–2 | 2–4 | **1–2 h** |
| **Sensor cable routing + service loops** | Clips, sleeve, grommets | printer + goBILDA consumables | — | — | included in E4 |
| **A "sensor map" card** (port → device → what it does) taped in the pit | paper | free | 1 | **2** | **1 h** |

**≈ 5–9 student-hours across both robots.**

## E7.6 Approximate subtotals

| Level | Per robot | **For 2 robots** |
|---|---|---|
| **Minimum useful** (2 touch sensors) | **$17.50** | **$35** |
| Practical (2 touch + 1 distance + 1 colour) | ≈ $70 | **≈ $140** |
| **REV Sensor Bundle** (2 distance + 2 colour + 2 touch + 2 magnetic + LED + cables) | **$180** | **$360** |
| **`[J]` Recommended** | Bundle on the A robot; à-la-carte touch + distance on the B robot | **≈ $250** |

## E7.7 Common failure modes and the spares to stock

| Failure | Symptom | Cause | Prevention / spare |
|---|---|---|---|
| **Colour sensor reads differently at the venue** | Sorting logic misfires | Ambient light | **Shroud it.** Calibrate at the event, not at home. Prefer *relative* thresholds over absolute. |
| **Distance sensor reads max range** | Autonomous drives into a wall | Dark, matte or angled target; out of range | Test against the **actual** field element after Kickoff. Have a timeout fallback. |
| **Limit switch never triggers** | Mechanism runs into a hard stop and stalls | Striker missed the lever; lever bent | Printed striker with margin; **stall timeout in software as a second line of defence** |
| **Limit switch triggers constantly** | Mechanism won't move | Debris, or the lever fouled | Magnetic limit switch `REV-31-1462` in dirty positions |
| **I2C sensor drops off the bus** | Sensor reads stale values | Address clash, or a long run | Spread across the **4 independent I2C buses** (VERIFIED); shorten runs |
| **Sensor cable cut by a mechanism** | Sudden loss | No service loop | E4 routing discipline |

**Spares `[J]`:** 2 touch sensors ($17.50), 1 distance sensor, 4 JST PH cables. Touch sensors are cheap enough that
running out of them at an event is inexcusable.

## E7.8 Rookie-minimum vs competitive

| | **Rookie-minimum** | **Competitive** |
|---|---|---|
| Sensors | **2 touch sensors** for lift/arm homing, and nothing else | Full Sensor Bundle, shrouded colour sensor, distance-based wall alignment |
| Software | Stall timeouts everywhere | Sensor fusion, calibrated thresholds, graceful degradation when a sensor fails |
| **Cost per robot** | **$17.50** | **$180–$220** |

---

# E8 · VISION

## E8.1 What it is and when a design needs it

Vision is how a BIOBUZZ robot will most likely locate itself and identify game elements in **AUTONOMOUS**. The game
is unknown, but the *infrastructure* is not: **AprilTags have appeared in each of the recent FTC seasons** — the
DECODE resource in `ROOT/manuals/archive/supplemental/2025-26_DECODE_AprilTags_USLetter.pdf` shows tags printed with
a **6.5 in. (16.50 cm) black square area**, mounted on the OBELISK and GOAL faces `[H]`. **Assume some form of tag or
target exists in BIOBUZZ and design a camera mount that can be aimed after Kickoff.**

**The FTC SDK does the hard part for free (VERIFIED, `ftc-docs.firstinspires.org`):** the **VisionPortal** offers
*"key capabilities of AprilTag, EasyOpenCV and the Color Processors – at the same time"*, gives AprilTag detections
as *"tag location and orientation, relative to the camera,"* supports **webcams and phone cameras**, and states
*"Multiple cameras can operate at the same time."* It also ships tools to manage **CPU resources and USB bandwidth**.
**A $75 webcam plus the SDK is a complete, legal, competitive vision system.**

## E8.2 The legality envelope — read this before you buy any camera

| Rule | Text | Consequence |
|---|---|---|
| **R707** `[C]` | *"USB is for vision."* Only (A) webcams/optical vision sensors per R708, (B) a USB hub or USB switch, (C) a REV Expansion Hub. | **No USB serial devices, no USB microcontrollers, no USB drives.** |
| **R708** `[C]` | *"Only **single image sensor** vision devices that are natively supported by the ROBOT CONTROLLER app… (**stereoscopic cameras are not allowed**)."* Covers **(A) all UVC compatible USB webcams (Logitech C270, and related)** and **(B) vision coprocessors allowed per R702**. *"UVC compatible USB webcams may only use the UVC provided stream / data."* | **No depth cameras. No stereo cameras. No using a webcam's non-UVC features.** |
| **R702 + Table 12-9** `[C]` | Programmable vision coprocessors natively supported by the FTC SDK may be reprogrammed. **Table 12-9 contains exactly one device: `Limelight Vision Limelight 3A — LL_3A`.** | **The 3A is the ONLY reprogrammable smart camera.** |
| **R702 Example 6** `[C]` | *"The OpenMV Cam, Luxonis OAK-1, and **LimeLight Vision Limelight 3G** are examples of programmable vision coprocessors that are **prohibited**."* | ⚠ **The 3A/3G distinction is a genuine money trap.** Two 3Gs for two robots is a total loss. |
| **R702 Example 5** `[C]` | *"The DFRobot HuskyLens and the Charmed Labs Pixy2 are examples of vision coprocessors that are **configurable but not programmable** and are treated no differently than other coprocessors… **These devices are allowed**."* | HuskyLens is legal — **but you may not reprogram it.** |
| **R704.D** `[C]` | *"**No continuous video stream is allowed.**"* Third-party streaming tools (**FTC Dashboard, FTControl Panels**) prohibited on the RC network. | **You cannot debug vision by streaming video over Wi-Fi at an event.** Tune tethered by USB in the pit. **This is new BIOBUZZ language — DECODE's text has zero hits for "Dashboard".** |
| **R709** `[C]` | Self-contained recorders (GoPro-style) allowed **for non-functional post-MATCH viewing**, wireless off. | A match-review camera is legal. It may not feed the robot. |
| **R710** `[C]` | Lasers only if part of a sensor, Class I/Exempt, **non-visible**. | Constrains active-illumination tricks. |

## E8.3 The main variants

| # | Variant | What it is | Legality |
|---|---|---|---|
| **A** | **UVC USB webcam + SDK VisionPortal** | Camera streams to the Control Hub; AprilTag/colour pipelines run on the hub's CPU | **R708.A** `[C]` — *"Logitech C270, and related"* |
| **B** | **goBILDA cased USB camera + SDK** | Same, but in an FTC-mountable enclosure | **R708.A** `[C]` |
| **C** | **Limelight 3A** | Smart camera; runs its own pipelines; you may reprogram it | **R702 + Table 12-9** `[C]` — the only one |
| **D** | **HuskyLens** | Configurable AI camera, on-device training | **R702 Example 5** `[C]` — allowed, **not** reprogrammable |
| **E** | **Phone camera (R701.B builds)** | The RC phone's own camera | **VERIFIED** SDK supports *"phone camera and/or webcam"* |

### Comparison table

| Variant | Complexity | Cost | **Programming burden** | Reliability | **Duplicability** | Verdict |
|---|---|---|---|---|---|---|
| **A. USB webcam + SDK** | 4 | **5** | 3 | 4 | **5** | **`[J]` START HERE — and one comes free in each storefront Driver Kit.** |
| **B. goBILDA cased camera** | **5** | 4 | 3 | **5** | **5** | **`[J]` Worth the ~$75** — the case is the mounting problem solved, twice. Global-shutter version for fast motion. |
| **C. Limelight 3A** | 3 | 2 | **4** (offloads CPU; own tuning UI) | **5** | 3 | A-team only. **$189 × 2 = $378.** ⚠ **VERIFIED:** *"The REV Control Hub can only support a single LL3A at this time."* |
| **D. HuskyLens** | 4 | 3 | **4** | 3 | 4 | Easy on-device training, weaker for pose estimation |
| **E. Phone camera** | 2 | **5** | 2 | 2 | 2 | Only on the R701.B path |

## E8.4 BUY — the COTS parts table

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **FTC-legal webcam** | **FIRST storefront (Pitsco)** | included in the **Driver Kit** ($285) | **1** | **2** | **included** | Buy | **VERIFIED** kit contents `[H]` rev 25-26.4 | 🕐 **You already bought two by buying two Driver Kits.** Cheapest legal vision on the field. |
| UVC USB webcam (retail) | Logitech and others | **C270 and related** — named in **R708.A** | 0–1 | 0–2 | **price not verified** | Buy | **MANUAL-SOURCED** legality; price **UNVERIFIED** (logitech.com did not render a price this session) | **Any UVC webcam is legal** if single-image-sensor. **No stereo.** NEEDS-SKU-CHECK on price. |
| **Rolling-shutter USB camera with goBILDA case (30 FPS)** | goBILDA | **`3122-0003-0001`** | 0–1 | 0–2 | **$74.99 ea** | Buy | **VERIFIED** | **`[J]` The mounting problem solved.** Fine for static AprilTag reads. |
| **Global-shutter USB camera with goBILDA case (100 FPS)** | goBILDA | **`3122-0004-0001`** | 0–1 | 0–2 | **$74.99 ea = $150** | Buy | **VERIFIED** | **`[J]` Same price, no motion blur — buy this one if you will read tags while moving.** |
| **Limelight 3A** | Limelight Vision | **`LL_3A`** (Table 12-9) — direct | 0–1 | 0–2 | **$189.00 ea = $378** | Buy | **VERIFIED** on limelightvision.io | 🕐 **The ONLY reprogrammable vision coprocessor (R702, Table 12-9)** `[C]`. USB-C flash & comms; **REV and goBILDA threaded mounting**; quad-core Cortex-A72 @1.5 GHz; 90 FPS @640×480. ⚠ **VERIFIED:** *"The REV Control Hub can only support a single LL3A at this time."* |
| Limelight 3A (alternate source) | goBILDA | **`3122-0002-0001`** | 0–1 | 0–2 | **$189.00 ea** — **currently OUT OF STOCK** | Buy | **VERIFIED** | Same price, second source. **Stock risk for a two-robot order.** |
| HuskyLens AI camera with goBILDA case | goBILDA | **`3122-0001-0001`** | 0–1 | 0–2 | **$79.99 ea** | Buy | **VERIFIED** | **R702 Example 5: allowed** `[C]` — **configurable, not reprogrammable.** |
| USB extension / short USB-A cable to the camera | REV or any | `REV-11-1232` USB-A→USB-C, or a short USB-A extension | 1 | 2 | **$10.50–$11.00** | Buy | **VERIFIED** (REV part) | Keep camera USB runs **short**; USB bandwidth and connector strain are both real. |
| USB hub (only if 2 cameras) | any | USB hub or switch | 0–1 | 0–2 | UNVERIFIED | Buy | **CONFIRMED-BIOBUZZ** R707.B | **R611** `[C]`: a **powered** hub on the ROBOT may draw only from an R602 USB pack or the hub's **+5V aux** port. |
| ❌ **Limelight 3G** | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R702 Example 6 names it PROHIBITED.** ⚠ **Adjacent model, same vendor. Check the letter.** |
| ❌ OpenMV Cam · Luxonis OAK-1 | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R702 Example 6** `[C]`. |
| ❌ Any stereo / depth camera (RealSense, OAK-D, ZED…) | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R708** `[C]`: *"stereoscopic cameras are not allowed."* |
| ❌ FTC Dashboard / FTControl Panels for camera tuning over Wi-Fi | — | — | **0** | **0** | — | — | **CONFIRMED-BIOBUZZ** | **R704.D** `[C]` names them. **This changes your workflow, not your BOM — plan for it now.** |

## E8.5 FABRICATE / ASSEMBLE IN-HOUSE

| Item | Method | Material / tooling | Per robot | For 2 | Student-hours (both) |
|---|---|---|---|---|---|
| **Camera mount, adjustable in pitch** | 3D print with a slotted pivot and a lockable angle | printer | 1–2 | 2–4 | **3–4 h** — **`[J]` make it ADJUSTABLE: the tag height is unknown until 12 September** |
| **Camera position jig / repeatability marks** | Scribed lines + a printed shim set | printer, calipers | 1 | 2 | **1–2 h** — **the camera must go back to the same place after a repair, or your calibration dies** |
| **Lens shade / glare hood** | 3D print | printer | 0–1 | 0–2 | **1 h** — venue spotlights are real |
| **USB strain relief at the camera and the hub** | Printed clip + zip tie | printer | 2 | 4 | **1 h** |
| **Camera calibration + tag-pose test routine** | OpMode + a printed test target | free | 1 | **1 shared** | **4–6 h** — the bulk of the vision effort |
| **A printed AprilTag test target** | Print at **ACTUAL SIZE / 100% scale** and verify the black square with a ruler | printer/paper | 1 | 1 shared | **0.5 h** — `[H]` the DECODE sheet's own instruction: verify the *"non-dotted black square area… should measure 6.5 in. (16.50 cm)"*. **Scale errors silently corrupt pose estimates.** |

**≈ 10–15 student-hours across both robots**, almost all of it software and calibration rather than parts.

## E8.6 Approximate subtotals

| Level | Per robot | **For 2 robots** |
|---|---|---|
| **Storefront Driver Kit webcam** | **$0 extra** | **$0 extra** |
| goBILDA cased global-shutter camera | $74.99 | **$150** |
| HuskyLens | $79.99 | **$160** |
| **Limelight 3A** | **$189.00** | **$378** |
| **`[J]` Recommended: kit webcam on both robots; add one goBILDA global-shutter camera to the A robot** | A: $75 / B: $0 | **≈ $75 for the program** |

## E8.7 Common failure modes and the spares to stock

| Failure | Symptom | Cause | Prevention / spare |
|---|---|---|---|
| **Tag detection works at home, fails at the venue** | Autonomous does nothing | Different lighting, different tag print, different mounting height | Test against the **official** printed target at **100% scale**. Build in a time-based fallback autonomous. |
| **Camera USB disconnects mid-match** | Vision dies, autonomous aborts | Connector strain; long USB run | **Short cable + strain relief at both ends.** Stock a spare USB cable. |
| **Pose estimate is subtly wrong** | Robot consistently misses by a few cm | Camera moved after a repair; scale error in the printed tag; uncalibrated intrinsics | Position marks on the mount; verify tag size with a ruler; recalibrate after any camera remount |
| **Frame rate collapses** | Loop time balloons, drive feels laggy | Vision pipeline eating the hub CPU | SDK's CPU/USB-bandwidth controls (VERIFIED as documented); reduce resolution; or move to a Limelight 3A |
| **You cannot debug it at the event** | Blind troubleshooting | **R704.D bans continuous video streams and FTC Dashboard on the RC network** `[C]` | **Build a USB-tethered pit workflow BEFORE the first event.** This is the biggest process consequence in this file. |
| **Motion blur ruins reads while moving** | Detections only when stopped | Rolling-shutter camera | goBILDA **global-shutter** `3122-0004-0001` ($74.99), or stop to look |

**Vision spares `[J]`:** 1 spare webcam (you have two from the Driver Kits — keep one as the spare until both robots
need one), 2 USB cables, a laminated printed tag target, and the calibration procedure on paper.

## E8.8 Rookie-minimum vs competitive

| | **Rookie-minimum (B team)** | **Competitive (A team)** |
|---|---|---|
| Camera | Driver-Kit webcam, mounted on an adjustable printed bracket | goBILDA global-shutter cased camera, or a Limelight 3A |
| Pipeline | SDK AprilTag processor, one tag, one action | AprilTag pose fused with odometry; colour processor for element ID |
| Fallback | **Time-based autonomous that scores something without vision** | Vision-primary with a time-based fallback |
| Debug workflow | USB tether in the pit | Same, plus a rehearsed calibration routine |
| **Cost** | **$0 extra** | **$75–$189 per robot** |

> **`[J]` THE HONEST VISION VERDICT FOR THIS PROGRAM.** Two Driver Kits already bought you two legal webcams. The
> SDK already does AprilTags for free. **Spend the vision budget on student-hours and a printed test target, not on
> a $378 pair of smart cameras** — until the A team has a working vision autonomous on a webcam and is genuinely
> CPU-limited. Then, and only then, buy one Limelight 3A for the A robot (and remember: **3A, not 3G**).

---

# 9 · THE COMPLETE ELECTRONICS KIT — PER ROBOT AND FOR TWO ROBOTS

**This is the deliverable table.** It is the **program-standard** tier from §1: two complete, legal, sparred,
practice-capable electronics packages. All prices **VERIFIED this session (2026-08-22)** unless the Confidence column
says otherwise. **All prices are as of August 2026 and are VERIFY-BEFORE-ORDER.**

## 9.1 Per robot / per team — the mandatory core

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost (2 robots) | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Electronics Kit** (Control Hub, servo, main switch, Color V3, Touch, grounding strap, Control Hub cable pack, M3 hardware) | FIRST storefront (Pitsco) | "Electronics Modules and Sensors Kit V1.1" | 1 | **2** | **$650** | Buy | **VERIFIED** page, price `[H]` | 🕐 **LIMIT 1 PER REGISTERED TEAM.** R701.A, R603, R605 `[C]` |
| **Driver Kit** (Driver Hub, 2 gamepads, FTC-legal webcam) | FIRST storefront (Pitsco) | "Driver Kit" | 1 | **2** | **$570** | Buy | **VERIFIED** page, price `[H]` | 🕐 **LIMIT 1 PER REGISTERED TEAM.** R901 `[C]` |
| **12V NiMH main battery** | AndyMark | `am-5290` | 2 | **5** (incl. 1 pool spare) | **$270** | Buy | **VERIFIED** $54.00 | R601 Table 12-4 `[C]`. ⚠ stock risk |
| **Battery charger** | goBILDA | `3101-0012-0001` | 1 | **2** | **$30** | Buy | **VERIFIED** $14.99; **current NEEDS-VERIFY vs E511.B** | Or REV `REV-31-1299` (0.9/1.8 A **verified compliant**) |
| **FTC Cable Bundle** | REV | `REV-45-1901` | 1 | **2** | **$440** | Buy | **VERIFIED** $220.00, contents verified | Contains the **main switch** and **2 grounding straps** — R603, R605 `[C]` |
| Wiring consumables (zip ties, Cinch-Straps, grommets, servo clips, sleeve, heat shrink) | goBILDA | `2909-0101-0100` · `2909-0102-0250` · `2911-0014-0001` · `2911-0014-0003` · `2917-0001-0001` · `2925-0008-3000` · `3201-0005-0001` | 1 set | **2 sets** | **$60** | Buy | **VERIFIED** | R606 inspectability `[C]` |
| Servo extensions + spare cables | goBILDA / REV | TJC8 Servo category · `REV-11-1130` | 1 set | 2 sets | **$50** | Buy | **VERIFIED** category / part | NEEDS-SKU-CHECK on the goBILDA SKUs |
| 20 A ATM mini blade fuses | any | ATM mini, 20 A | 2 | **4–6** | **$8** | Buy | **FAMILY-ONLY** | R601.A, R604 `[C]` |
| Spare gamepad | REV | `REV-31-2983` | 1 | **2** | **$52** | Buy | **VERIFIED** $26.00 | R904 wired only `[C]` |
| Driver Hub spare battery | REV | `REV-31-1876` | 1 | **2** | **$44** | Buy | **VERIFIED** $21.75 | |
| USB extenders + ferrite clips | any | short USB-A M/F; snap-on ferrites | 3 + 3 | 6 + 6 | **~$25** | Buy | **HISTORICAL** best practice `[H]` | Protects the DS ports |
| **SUBTOTAL — mandatory core** | | | | | **≈ $2,199** | | | |

## 9.2 Sensing and vision — the recommended addition

| Item | Vendor | SKU | Qty per robot | Qty for 2 robots | Approx cost (2 robots) | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **FTC Sensor Bundle** (A robot) | REV | `REV-45-1885` | 1 (A only) | **1** | **$180** | Buy | **VERIFIED**, contents verified | 2 distance + 2 colour + 2 touch + 2 magnetic + LED + cables |
| Touch sensors (B robot) | REV | `REV-31-1425` | 4 (B only) | **4** | **$35** | Buy | **VERIFIED** $8.75 | **`[J]` The floor for the B robot** |
| Through Bore Encoder + insert pack (A robot) | REV | `REV-11-1271` + `REV-25-1870` | 1 (A only) | **1** | **$45** | Buy | **VERIFIED** $40.80 + $4.00 | For an articulated arm/turret |
| Optical tracking odometry (A robot) | SparkFun | `SEN-24904` | 1 (A only) | **1** | **$85** | Buy | **VERIFIED** $84.95 | **R702 Example 2: allowed** `[C]` |
| Global-shutter cased camera (A robot) | goBILDA | `3122-0004-0001` | 1 (A only) | **1** | **$75** | Buy | **VERIFIED** $74.99 | Driver-Kit webcams cover the rest |
| **SUBTOTAL — sensing & vision** | | | | | **≈ $420** | | | |

## 9.3 The two-robot rollup

| Block | **For TWO robots** | Basis |
|---|---|---|
| FIRST storefront: 2 × Electronics Kit + 2 × Driver Kit | **$1,220** | $325 + $285 per team, **VERIFIED** page, `[H]` rev 25-26.4 |
| Batteries (5) + fuses | **$278** | $54.00 ea **VERIFIED** |
| Chargers (2) | **$30** | $14.99 ea **VERIFIED** |
| Cable bundles (2) + consumables + extensions | **$550** | $220.00 ea **VERIFIED** |
| Console spares (2 gamepads, 2 DS batteries, extenders, ferrites) | **$121** | **VERIFIED** where SKU'd |
| **Mandatory-core total** | **≈ $2,199** | |
| Sensing & vision (recommended) | **+$420** | |
| **PROGRAM-STANDARD TOTAL** | **≈ $2,620** | |
| *Optional: 2 × Limelight 3A* | +$378 | **VERIFIED** $189.00 ea; ⚠ **3A only, R702 Example 6 bans the 3G** `[C]` |
| *Optional: 2 × goBILDA odometry pack* | +$560 | **VERIFIED** $279.99 ea |
| *Optional: spare Control Hub + spare Driver Hub* | +$650 | **VERIFIED** $375.00 + $275.00 |
| *Optional: 2 × Expansion Hub (avoid — see E1.3)* | +$550 | **VERIFIED** $275.00 ea; ⚠ limited stock |
| *Excluded above: 2 × team registration* | +$650 | $325 ea `[H]` — **and it is what unlocks the storefront limits** |

> **Read of the rollup `[J]`:** the **mandatory** electronics for two robots is **≈ $2,200** and about **56% of it is
> four storefront kits** — i.e. **two purchase decisions**. That is exactly the shape a low-mentor-hour program wants.
> Everything above $2,620 is optional and can wait until after Kickoff. **The two storefront orders cannot wait**, and
> they are gated on registration, so **register both teams first.**

## 9.4 What is FABRICATED, program-wide

| Fabricated item | Method | For 2 robots | Student-hours (both) |
|---|---|---|---|
| Control Hub / Driver Hub mounting trays | 3D print or cut polycarb | 4 | 3 h |
| Inspection access panels (R606) | Chassis design + hand tools | 2 | 2 h |
| Battery trays + retention | 3D print + Cinch-Strap | 2 | 3 h |
| Power switch brackets (R706.K permits) | 3D print | 0–2 | 1 h |
| Strain-relief anchors + cable clips | 3D print | 30–50 | 5 h |
| Sensor / camera brackets (camera bracket **must be pitch-adjustable**) | 3D print | 8–16 | 6 h |
| Limit-switch strikers and hard stops | 3D print / hand tools | 4–8 | 3 h |
| Colour-sensor shrouds, lens hoods | 3D print | 2–4 | 2 h |
| OPERATOR CONSOLE boxes (R903 volume) | Toolbox / plywood | 2 | 6 h |
| Wiring harnesses (build both side by side) | Assembly | 2 | 12 h |
| Laminated wiring diagram + sensor map, per robot | Paper | 4 | 4 h |
| Printed AprilTag test target at 100% scale | Printer/paper | 1 shared | 0.5 h |
| Calibration + homing procedures, written | Doc | 1 shared | 6 h |
| **TOTAL FABRICATION** | | | **≈ 53–55 student-hours** |

**`[J]` Two-robot discipline: every printed bracket runs qty 2 on the first job.** A part printed once is a part the
B robot does not have, and re-slicing it three weeks later costs more than the filament ever did.

---

# 10 · THE COMPETITION SPARES KIT

**`[J]` One kit, shared by both teams, living in a labelled box that goes to every event.** R901/R903 permit spare DS
devices and spare USB hubs *in* the console as long as only one is connected — everything else here lives in the pit.

| Item | SKU | Qty | Cost | Why |
|---|---|---|---|---|
| **12V NiMH battery (pool spare)** | `am-5290` | **1** | $54.00 | The most likely part to be the problem |
| **20 A ATM mini blade fuses** | — | **strip of 5** | ~$5 | R601.A / R604 `[C]`. Blows at events. |
| **Gamepad** | `REV-31-2983` | **2** (one per team) | $52.00 | Cable strain failure is routine |
| **Driver Hub battery** | `REV-31-1876` | **1** | $21.75 | A dead DS ends the day |
| **Main switch cable + bracket** | `REV-31-1387` | **1** | $13.00 | R603 `[C]` — no switch, no match |
| **Resistive grounding strap** | `REV-31-1269` | **1** | in Cable Bundle | R605 `[C]` |
| **Touch sensors** | `REV-31-1425` | **2** | $17.50 | Cheapest thing that stops an arm |
| **Servo extensions** | goBILDA TJC8 | **4** | NEEDS-SKU-CHECK | #1 signal failure |
| **Servo connector clips** | `2917-0001-0001` | **1 pack** | $5.99 | Prevents the #1 signal failure |
| **PWM cables** | `REV-11-1130` | **2** | $7.75–$12.50 | |
| **JST PH 4-pin sensor cables** | `REV-31-1408` | **4** | $7.75–$14.75 | |
| **JST VH 2-pin motor cables** | `REV-31-1413` | **2** | $9.75–$22.25 | |
| **XT30 extension cable** | `REV-31-1394` | **1** | in Cable Bundle | |
| **JST joiner boards** | `REV-31-1388` / `REV-31-1429` | **1 pack ea** | $6.00–$9.75 | A student-proof splice |
| **USB-A → USB-C cable** | `REV-11-1232` | **2** | $10.50–$11.00 | RC tether + camera |
| **Spare motor** | per `LEGAL-PARTS-CONSTRAINTS.md` §2.5 | **1** | ~$55 | |
| **Spare servos** | per `LEGAL-PARTS-CONSTRAINTS.md` §4.5 | **2** | ~$50 | |
| **SPARKmini** (emergency motor port) | `REV-31-1230` | **1** | $35.00 | **`[J]` $35 buys you back a dead motor port mid-event** |
| Zip ties, electrical tape, heat shrink | goBILDA | 1 ea | ~$20 | |
| **Laminated wiring diagram (per robot) + sensor map + battery log** | — | 2 + 2 + 1 | $0 | **`[J]` The most useful object in the box** |
| **Printed AprilTag target at 100% scale + a ruler to verify it** | — | 1 | $0 | `[H]` DECODE instruction: verify the black square measures **6.5 in. (16.50 cm)** |
| **A copy of Section 12 + the Inspection Quick Reference** | — | 1 | $0 | Wins arguments; **the 26-27 IQR publishes at Kickoff** |
| **SPARES KIT TOTAL** | | | **≈ $380–$420** | |

**`[J]` Not in the kit, deliberately:** a spare Control Hub or Driver Hub. At **$375 / $275**, those are a *tier*
decision (§1 competitive), not a spares-kit line. If you buy one, buy **one for the program**, not one per robot, and
**never cannibalise robot B's hub for robot A** — that turns one team's bad day into two.

---

# 11 · CONSOLIDATED DO-NOT-BUY LIST (ELECTRONICS)

Everything here is **for sale right now** from a vendor you will otherwise buy from. That is what makes it dangerous.

| Item | Why it is illegal | Rule |
|---|---|---|
| **Limelight 3G** | Programmable vision coprocessor **not** in Table 12-9; **named as prohibited** | **R702 Example 6** `[C]` |
| **OpenMV Cam · Luxonis OAK-1** | Same | **R702 Example 6** `[C]` |
| **Any stereo / depth camera** (OAK-D, RealSense, ZED…) | *"stereoscopic cameras are not allowed"* | **R708** `[C]` |
| **goBILDA Servo Travel Tuner** `3109-0002-0001` $19.99 | Modifies actuator control signals | **R612 blue box names it** `[C]`; DECODE IQR `[H]` |
| **goBILDA Servo Power Distribution Board (8 ch)** `3108-2827-0801` $17.99 | Not in Table 12-3; combines port power | DECODE IQR `[H]`; **R613.B** `[C]` |
| **goBILDA 4-Channel Servo Extension via CAT6** `3802-2745-4527` $29.99 | Named illegal | DECODE IQR `[H]` |
| goBILDA Servo Speed Tuner / Travel Reverser / Signal-Boosting Extension | Modify actuator control signals | **R612** `[C]` + `[J]` |
| goBILDA Servo Commander / Joystick / Recorder | Generate actuator control signals outside the RC | **R701** `[C]` + `[J]` |
| **Any buck / boost converter or BEC in a power path** | *"Altering a power pathway includes… a boost… or buck… converter"* | **R612** `[C]` |
| **Any 12V NiMH battery not in Table 12-4** | Closed allowlist **by part number** | **R601** `[C]` |
| **LiPo / Li-ion / LiFePO4 as the main battery** | Must be 12V NiMH | **R601** `[C]` |
| **A second battery powering actuators** | One battery only; USB packs may not power actuators | **R601, R602.A** `[C]` |
| **A higher-rated or self-resetting fuse** | | **R604** `[C]` |
| **Any power switch not in Table 12-5**, or a modified switch | Closed allowlist; only the *bracket* may be modified | **R603, R706.K** `[C]` |
| **Any grounding strap not in Table 12-6** | Closed allowlist | **R605** `[C]` |
| **A battery charger exceeding 3 A average channel current** | | **E511.B** `[C]` |
| **Charging with alligator clips** | | **E511.C** `[C]` |
| **A 3D-printed replacement Control Hub / Driver Hub enclosure** | *"removing enclosures and replacing with custom enclosures"* | **R706** `[C]` |
| **A repaired battery** | Repairs allowed for devices **except batteries** | **R706.H** `[C]` |
| **Relays, electromagnets, electrical solenoid actuators** | | **R506** `[C]` |
| **Bluetooth gamepads, wireless headsets, Wi-Fi cards in the console** | | **R904** `[C]` |
| **Bluetooth / LoRa / ESP32 telemetry links on the robot** | No other wireless to, from or within the robot | **R704.A** `[C]` |
| **FTC Dashboard / FTControl Panels on the RC Wi-Fi network** | Named; and no continuous video stream | **R704.D** `[C]` |
| **USB serial devices, USB microcontrollers, USB drives on the robot** | *"USB is for vision"* | **R707** `[C]` |
| **A visible-light laser as a driver aiming aid** | Must be part of a sensor, Class I/Exempt, non-visible | **R710** `[C]` |
| **Sensors powered from a second hub or a custom circuit** | | **R613.A** `[C]` |
| **A third hub** (Control Hub + 2 Expansion Hubs) | *"no more than one additional REV Expansion Hub"* | **R701.C** `[C]` |
| **A second DRIVER STATION powered on simultaneously** | Only one connected and powered at a time | **R901** `[C]` |

---

# 12 · INSPECTION AND EVENT-DAY ELECTRICAL CHECKLIST

**`[J]` Run this on both robots, at home, before the first event. Print it. Two copies.**

**Before you leave home**
- [ ] Exactly **one** 12V NiMH main battery on the robot, and it is on the **Table 12-4** list **(R601)**
- [ ] Battery fuse is a **20 A ATM mini blade**, unmodified, not self-resetting **(R601.A, R604)**
- [ ] Exactly **one** main power switch, from **Table 12-5**, accessible and clear of pinch hazards **(R603)**
- [ ] **Resistive grounding strap** fitted, from **Table 12-6**, to a fully-COTS XT30 component and to the frame **(R605)**
- [ ] No electrical device is grounded to the frame any other way; frame carries no current **(R605)**
- [ ] Every power-regulating device is powered by the method **Table 12-7** specifies, **from the main battery only (R608)**
- [ ] Main bus is **red/black** (or another R610-legal pair) along its **entire length (R610)**
- [ ] Wire gauges meet **Table 12-8**; wire is **gauge-marked** or you can demonstrate it **(R609)**
- [ ] **No boost/buck converters, no relays, no solenoids, no second battery for actuators (R612, R506, R601)**
- [ ] Regulators, wiring and fuses **can be made visible** without disassembly; RC diagnostic lights visible **(R606)**
- [ ] Motor count ≤ 8, servo count ≤ 8, **summed across every configuration you might use (R503)** — attach the budget table
- [ ] Every motor and servo is on the **Table 12-1 / 12-2** lists **(R501, R502)**
- [ ] Only R707-legal devices on USB; **camera is single-image-sensor, not stereo (R707, R708)**
- [ ] Any smart camera is a **Limelight 3A**, not a 3G **(R702, Table 12-9)**
- [ ] Any laser on the robot is part of a sensor, Class I/Exempt, non-visible **(R710)**
- [ ] **RC named `<team#>-RC`; DS named `<team#>-DS`; four distinct names across two teams (R705)**
- [ ] Control Hub Wi-Fi password **changed from default**; **Bluetooth off** on RC and DS; DS purged of all remembered
      Wi-Fi connections except the RC **(R711)**
- [ ] OPERATOR CONSOLE fits **36 × 18 × 24 in. including power banks**; touchscreen visible and usable **(R902, R903)**
- [ ] Only **one** DS device connected and powered on; only **one** USB hub connected **(R901, R903)**
- [ ] Gamepads are **wired**; no Bluetooth, no wireless cards in the console **(R904)**
- [ ] **No FTC Dashboard / FTControl Panels / continuous video stream** in your event code path **(R704.D)**
- [ ] Charger is **≤3 A average channel current** and uses a **polarised** connector **(E511)**

**In the pit, every match**
- [ ] Fresh battery, logged
- [ ] Battery **Cinch-Strapped**, XT30 seated, strain-relieved
- [ ] Every servo connector has its clip on
- [ ] Programming laptop **disconnected from the RC Wi-Fi network (R704.C)**
- [ ] Diagnostic lights visible and green before the robot leaves the pit

---

# 13 · OPEN QUESTIONS — THE NEEDS-SKU-CHECK / NEEDS-RULING REGISTER

| # | Item | Status | Resolution path |
|---|---|---|---|
| **Q1** | **REV 12V Slim Battery `REV-31-1302` chemistry not stated on the product page** | NEEDS-VERIFY | It is named in Table 12-4 so it is **legal** `[C]`; confirm NiMH with REV before a bulk order |
| **Q2** | **goBILDA `3101-0012-0001` and AndyMark `am-5473` charger current not published** | NEEDS-VERIFY vs **E511.B** (3 A) | Ask the vendor, or buy the REV charger (`REV-31-1299`, **0.9/1.8 A verified**) |
| **Q3** | **XT30 Power Distribution Block `REV-31-1293`** | **NEEDS-RULING** | `[J]` Arguably legal (passive, not a CUSTOM CIRCUIT under R608). **Submit to Game Q&A from 2026-09-28** if you will rely on it |
| **Q4** | **Blinkin LED Driver `REV-11-1105`** | **NEEDS-RULING** | Not in Table 12-3; R607 permits >5V *solely for LEDs*. Ask Q&A |
| **Q5** | **Bulk capacitor across the 12V bus for sag** | **NEEDS-RULING** | R612 vs "inconsequential effect on power pathways". Ask Q&A |
| **Q6** | **goBILDA Servo Monitor `3109-0005-0002` and Signal-Boosting Servo Extension `3116-1718-0300`** | **NEEDS-RULING**; assume illegal | R612. Ask Q&A only if you truly need them |
| **Q7** | **No gamepad allowlist in BIOBUZZ V0** (**V0-GAP**; DECODE had one) | Open | **Re-grep the Kickoff manual for `gamepad` on 2026-09-12.** Buy only DECODE-listed models until then |
| **Q8** | **No minimum Android OS version in V0** (**V0-GAP**; DECODE required Android 7) | Open | Re-grep for `Android` at Kickoff. Do not buy old phones |
| **Q9** | **2026-27 Inspection Quick Reference not yet published** — `ftc-resources.firstinspires.org/.../inspection-reference` returned *"Resource Coming Soon!"* | Open | **Download on Kickoff day.** It carries the pre-verified servo list, the illegal-electronics list, and the official RC/DS wiring diagrams |
| **Q10** | **AndyMark `am-4969` power switch and `am-4648a` grounding strap prices** | NEEDS-SKU-CHECK | AndyMark collection pages did not render products this session; the parts are **legal** (Tables 12-5, 12-6) `[C]` |
| **Q11** | **Studica `70025` battery, `70182` switch, `75005` Servo Power Block** | UNVERIFIED | studica.com returned **HTTP 403**. Legal `[C]`; no price asserted |
| **Q12** | **Logitech C270 price** | UNVERIFIED | logitech.com did not render a price. **Legality is explicit in R708.A** `[C]`. Two webcams arrive free in the two Driver Kits |
| **Q13** | **REV Resistive Grounding Strap `REV-31-1269` standalone price** | NEEDS-SKU-CHECK | Verified as a **bundle line item** ×2 in `REV-45-1901` |
| **Q14** | **`REV-35-2709` DUO Control Bundle contents** | NEEDS-SKU-CHECK | Price verified ($650.00); contents not. Check against R701/R601/R603 |
| **Q15** | **goBILDA XT30 / Powerpole / TJC8 / wire SKUs** | NEEDS-SKU-CHECK | Categories verified on `gobilda.com/wiring/`; individual SKUs did not render |
| **Q16** | **FIRST storefront 26-27 revision** | `[H]` prices are rev 25-26.4 (Feb 18, 2026) | **A 26-27 revision is expected at or before Kickoff.** Re-check the team Dashboard before ordering |
| **Q17** | **R105 expansion limit** | DEFERRED TO KICKOFF | Affects only cable-carrier and service-loop lengths in this file |
| **Q18** | **Whether BIOBUZZ uses AprilTags at all** | DEFERRED TO KICKOFF | `[H]` They recur in recent seasons. **Build an adjustable camera mount now; commit to a pipeline on 12 September** |

---

# 14 · VERIFICATION LOG — every source loaded in this session (2026-08-22)

### 14.1 Primary — BIOBUZZ V0, grep-verified locally

| File | What it verified |
|---|---|
| `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` | Full text of R501–R506, R601–R613, R701–R711, R801, R901–R904 and Tables 12-1 through 12-9, incl. R502's 5V/6V blue box, R501's LIDAR/sensor-motor carve-out, and R702 Examples 1–6 |
| `manuals/2026-27_BIOBUZZ/sections/05_EventRules_E_p33-42.txt` | **E511** charging rules verbatim (3-amp average channel current; polarised connectors) |
| `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` | **`gamepad` appears exactly once** in the whole manual (R901.B) — confirms the V0-GAP |
| `manuals/archive/supplemental/2025-26_DECODE_Competition_Manual_TU32.html` | `[H]` DECODE R903 **Table 12-12 gamepad allowlist**, ferrite-clip and USB-extender guidance, 2-gamepad cap |
| `manuals/archive/supplemental/2025-26_DECODE_InspectionQuickReference.pdf` | `[H]` **"Illegal Servo Power or Servo Signal Adjusters"** — the three named-illegal goBILDA devices; RC and DS wiring-diagram sections |
| `manuals/archive/supplemental/2025-26_DECODE_AprilTags_USLetter.pdf` | `[H]` AprilTag print instructions; **black square = 6.5 in. (16.50 cm)**; OBELISK/GOAL placement |

### 14.2 Vendor pages loaded with WebFetch this session

| URL | What it verified |
|---|---|
| `revrobotics.com/rev-31-1595/` | **Control Hub $375.00, In Stock**; 4 motor (w/ encoder), 6 servo, 8 digital I/O, 4 analog, 4 I2C, 2 RS485, **1 internal 6-axis IMU**; box contents |
| `docs.revrobotics.com/duo-control/control-system-overview/control-hub-basics` | **8–15 V input; motor port 10 A cont. / 20 A max; +5V aux 5 A total; 2 A max per servo port pair**; RK3328 + Cortex-M4 |
| `revrobotics.com/rev-31-1596/` | **Driver Hub $275.00, In Stock**; 3 × USB-A + USB-C; 5040 mAh Li-ion; 5 in. 800×480; box contents |
| `revrobotics.com/ftc/electronics/` | Driver Hub $275.00 · Driver Hub Battery $21.75 · Control Hub Repair $165.00 · Driver Hub Repair $125.00 · Control & Power Bundle $750.00 · DUO Control Bundle $650.00 · Cable Bundle $220.00 · Sensor Bundle $180.00 · Servo Hub $90.00 · 9-Axis IMU $38.00 · Gamepad `REV-31-2983` $26.00 · JST Joiner Boards $6.00–$9.75 · USB-A/C cables $10.50–$11.00 · XT30 Adapters $5.50–$13.50 · PWM Cables $7.75–$12.50 |
| `revrobotics.com/ftc/electronics/sensors/` | 9-Axis IMU `REV-31-3332` $38.00 · Color V3 `REV-31-1557` $20.75 · Color V2 `REV-31-1537` $13.50 · 2m Distance `REV-31-1505` $31.50 · Touch `REV-31-1425` $8.75 · Potentiometer `REV-31-1155` $15.25 · Through Bore Encoder V1 `REV-11-1271` $40.80 (was $48.00) · Insert Pack `REV-25-1870` $4.00 · Magnetic Limit Switch `REV-31-1462` $17.50 · Digital LED Indicator 4-pk `REV-31-2010-PK4` $14.75 · 5V LED strip `REV-11-1198` $26.00 · 12V RGB strip `REV-11-1197` $28.75 · Blinkin `REV-11-1105` $49.68 · Blinkin adapter `REV-11-1196` $4.00 |
| `revrobotics.com/ftc/electronics/power-system/` | XT30 Power Distribution Block `REV-31-1293` $14.75 · 12V Slim Battery Accessories `REV-31-1299` $6.00–$39.50 · SRS Programmer `REV-31-1108` $25.00 · JST VH motor cables $9.75–$22.25 · JST PH sensor cables $7.75–$14.75 |
| `revrobotics.com/rev-31-1302/` | **12V Slim Battery $60.00, In Stock**; 3000 mAh, XT30, 16 AWG, 20 A ATM fuse, 567 g; **chemistry not stated** |
| `revrobotics.com/rev-45-1885/` | **FTC Sensor Bundle $180.00, In Stock — full contents** |
| `revrobotics.com/rev-45-1901/` | **FTC Cable Bundle $220.00, In Stock — full contents (16 line items)** |
| `revrobotics.com/rev-35-1906/` | **Control & Power Bundle $750.00, In Stock — full contents** (Control Hub, 12V Slim Battery, Battery Charger `REV-31-1299`, gamepad, switch cable, Driver Hub) |
| `docs.revrobotics.com/duo-control/troubleshooting-the-control-system/12v-battery-best-practices-and-troubleshooting` | **Charger switch 0.9 A / 1.8 A**; XT30 male out; IEC C13 in; battery-care and retirement guidance |
| `gobilda.com/electronics/` | Full subcategory map (motor controllers, servo electronics, sensors, cameras, odometry, batteries, **voltage regulators (BECs)**, wiring, switches, lights, fuses) |
| `gobilda.com/servo-electronics/` | Servo Power Injector `3125-0001-0001` $69.99 · **Travel Tuner $19.99 · Power Distribution Board $17.99 · CAT6 Extension $29.99 (ALL ILLEGAL)** · Speed Tuner $19.99 · Travel Reverser $13.99 · Monitor $24.99 · Commander 1ch $29.99 / 2ch $59.99 · Joystick $79.99 · Recorder $119.99 · Axon MK2 programmer $59.99 · goBILDA programmer $12.99 · Hitec DPC-11 $25.99 · 22 AWG twisted wire 15 m `3806-0322-0015` $17.99 · servo connector clips $5.99 |
| `gobilda.com/wiring/` | Consumables with SKUs and prices (Cinch-Strap, zip ties, grommets, servo clips, heat shrink, cable-carrier chain, braided sleeve) + connector **category** list (XT30, Anderson Powerpole, TJC8, JST VH/PH/XH…) |
| `gobilda.com/battery-chargers/` | **12V NiCad/NiMH XT30 charger `3101-0012-0001` $14.99** · 6V `3101-0006-0001` $14.99 · Hitec RDX2 200 `44370` $139.99 · 20V Li-ion `3101-1020-0001` $29.99 — **no charge currents published** |
| `gobilda.com/cameras/` | HuskyLens w/ case `3122-0001-0001` $79.99 · **Global-shutter USB camera `3122-0004-0001` $74.99** · Rolling-shutter `3122-0003-0001` $74.99 · **Limelight 3A `3122-0002-0001` $189.00 — OUT OF STOCK** |
| `gobilda.com/odometry/` | Pinpoint V2 `3110-0002-0002` $79.99 · 4-Bar pack `3203-3110-0002` $279.99 · Swingarm pack `3203-3110-0001` $279.99 · pods `3110-0001-0002` / `3110-0001-0001` $99.99 |
| `gobilda.com/sensors/` | Laser Distance Sensor 1 m `3124-0001-0001` $29.99 (only product rendered) |
| `andymark.com/products/am-flat-pack-battery` | **`am-5290` $54.00**; 3000 mAh, XT30 female, 20 A replaceable fuse; *"estimated back in stock"* |
| `andymark.com/products/nimh-flat-pack-charger` | **`am-5473` $16.00**; 100–240 VAC 0.6 A in; 1.2–7.2 V (1–6S) / 8.4–18 V (7–15S) out; **charge current not published** |
| `limelightvision.io/products/limelight-3a` | **Limelight 3A $189.00**; USB-C flash/comms; **REV and goBILDA threaded mounting**; quad-core Cortex-A72 @1.5 GHz; 90 FPS @640×480; ⚠ *"The REV Control Hub can only support a single LL3A at this time"* |
| `sparkfun.com/sparkfun-optical-tracking-odometry-sensor-paa5160e1-qwiic.html` | **OTOS `SEN-24904` $84.95, In stock**; Qwiic/I2C; **must be 10 mm from the field tiles**; FTC Java library |
| `ftc-docs.firstinspires.org/.../visionportal-overview.html` | **VisionPortal**: AprilTag + EasyOpenCV + Color Processors simultaneously; webcam and phone camera; multiple cameras; CPU/USB-bandwidth management |

### 14.2a Re-verification pass — 2026-08-22 (audit of this file's highest-risk claims)

Every row below was **re-loaded from the live vendor page or re-extracted from the V0 PDF** in the audit pass, to
confirm the claims this file was already making. **One error was found and corrected** (Table 12-4 notes).

| Claim re-checked | Result |
|---|---|
| Control Hub `REV-31-1595` — **$375.00, "In Stock & Ready To Ship!"** | ✅ **CONFIRMED** — and **4 motor / 6 servo / 8 digital / 4 analog / 4 I2C / 2 RS485 ports, 6-axis IMU**, which is the basis of the E1.3 port math |
| Expansion Hub `REV-31-1153` — $275.00 | ✅ price confirmed; ⚠ **still OUT OF STOCK 2026-08-22** |
| SPARKmini `REV-31-1230` — $35.00 | ✅ **CONFIRMED In Stock**; 15 A continuous, 6–20 V, XT30 in / JST-VH out / servo-PWM signal |
| Servo Power Module `REV-11-1144` — **DISCONTINUED** | ✅ **CONFIRMED on the product page: "Availability: Discontinued"**, $48.88 (from $57.50), listed under *Discontinued & Discounted Products*. **The do-not-design-around-it call in E1.4 stands.** |
| Driver Hub `REV-31-1596` $275.00 · Driver Hub Battery `REV-31-1876` $21.75 · Control Hub Repair `REV-31-1595-RFB` $165.00 · Driver Hub Repair `REV-31-1596-RFB` $125.00 · Control & Power Bundle `REV-35-1906` $750.00 · DUO Control Bundle `REV-35-2709` $650.00 · Cable Bundle `REV-45-1901` $220.00 · Sensor Bundle `REV-45-1885` $180.00 · Servo Hub `REV-11-1855` $90.00 · 9-Axis IMU `REV-31-3332` $38.00 · Gamepad `REV-31-2983` $26.00 | ✅ **ALL CONFIRMED** unchanged on `revrobotics.com/ftc/electronics/` |
| 12V Slim Battery `REV-31-1302` — $60.00, In Stock | ✅ **CONFIRMED**; 3000 mAh, XT30 female, 16 AWG, 20 A replaceable ATM fuse. **Chemistry still NOT stated on the page** — the NEEDS-VERIFY flag in E3.2 is correct and stays. (Page does say *"10-cell, 12V 3000mAh"*, consistent with 10×1.2 V NiMH, but the page never writes "NiMH".) |
| Limelight 3A `3122-0002-0001` — $189.00 | ✅ price confirmed; ⚠ **still OUT OF STOCK at goBILDA 2026-08-22.** goBILDA cameras `3122-0001-0001` / `3122-0003-0001` / `3122-0004-0001` all **In stock** |
| **R503** 8 motors + 8 servos · **R601** 1 battery + 20A ATM · **R603**/Table 12-5 · **R605**/Table 12-6 · **R701** A/B/C · **R702**/Table 12-9 · **R901** · **R903** console volume · **R102** 18-in. cube · **R104** no weight limit · **E511** 3-amp charger | ✅ **ALL re-grepped verbatim against the V0 text and confirmed exactly as cited in §2** |
| **Table 12-3** (power regulators) | ✅ **re-extracted from PDF p. 77 and now reproduced inline in E1.3.** The `.txt` dump was row-shifted; the PDF confirms **SPARKmini = 2 Motors per Device** as E1.4 states |
| **Table 12-4** (batteries) | ⚠ **ERROR FOUND AND CORRECTED.** All 7 part numbers were right, but the **notes column was shifted up one row**. Fixed in E3.2: *"May be labeled as ‘Modern Robotics’"* → **Matrix `14-0014`**; *"Formerly 739023"* → **TETRIX MAX `W39057`** |
| **Tables 12-5 / 12-6** | ✅ **re-extracted from PDF pp. 79–80 — match E3.2 exactly**, all 6 switches and all 3 grounding straps |

### 14.3 Sources that FAILED to load or render this session — stated for the record

| Source | Result |
|---|---|
| `andymark.com/collections/ftc-electronics` | **HTTP 404** |
| `andymark.com/collections/ftc-control-system` | Loaded, but **no products, part numbers or prices rendered** |
| `gobilda.com/batteries/` | **HTTP 499** |
| `revrobotics.com/rev-31-1299/` | **HTTP 404** (the accessories family is reachable from the category page) |
| `logitech.com` C270 product page | **No price rendered** |
| `studica.com` | **HTTP 403** (Phase A) — official FIRST supplier, unreachable |
| `ftc-resources.firstinspires.org/ftc/event/inspection-reference` | *"2026-2027 FIRST Tech Challenge Resource Coming Soon!"* (Phase A) |

### 14.4 Vendor status for the record

| Vendor | Role | Fetchable this session |
|---|---|---|
| **REV Robotics** | General supplier; **sole source of the mandated ROBOT CONTROLLER and DRIVER STATION hardware (R701, R901)** | **Yes — full product-level detail** |
| **goBILDA** | General supplier, deeply integrated with FTC | Yes — most categories priced |
| **AndyMark** | **Official FIRST supplier** | Partially — product pages yes, collection pages no |
| **Studica** | **Official FIRST supplier** | **No — HTTP 403** |
| **FIRST storefront (Pitsco)** | Official — **the cheapest legal control system, limit one kit per registered team** | Via the storefront PDF `[H]` rev 25-26.4 |
| **Limelight Vision** | Component supplier; **the only Table 12-9 vision coprocessor** | Yes |
| **SparkFun** | Component supplier; **R702 Example 2 device** | Yes |

---

*Document generated **2026-08-22** against BIOBUZZ Competition Manual **V0** (2026-07-31). **Section 12 is FINAL**, so
every legality claim here is actionable today; **R105 expansion limits and the game itself are not** and are flagged
DEFERRED TO KICKOFF. **All prices are as of August 2026 and are VERIFY-BEFORE-ORDER.** Nothing in this file asserts a
SKU or price that was not read off a vendor page or a BIOBUZZ rule table in the session that produced it.*
