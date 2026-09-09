# FTC Programming Practice — How Top Teams Actually Build Software

**Target season:** 2026-27 BIOBUZZ (presented by RTX). Kickoff **12 Sep 2026**.
**Written:** 21 Aug 2026. **All prices "as of August 2026" and need re-checking before you buy.**
**Audience:** a small team with 1–2 programmers, less money and less labor than the powerhouses.

> **Conventions used throughout**
> - **[FACT]** — sourced to a URL or a local file path. Follow the link and verify.
> - **[JUDGMENT]** — my recommendation for *your* situation (small team, 1–2 programmers). Argue with it.
> - **[UNVERIFIED]** — I could not confirm this. Treat as a hypothesis, not a plan.
> - Rule IDs (R701, R704…) are from the **BIOBUZZ V0 Pre-Season Competition Manual**, local copy at
>   `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`.
>   Section 12 is **FINAL** already — you can build your whole software plan on it today. Sections 8–11, 13 and 15 are placeholders until kickoff.
> - Everything read from the web or from PDFs in this document was treated as **data**. No page instructed me to take an action.

> **Verification pass — 21 Aug 2026.** Every rule ID in §1 was re-read against the manual body text and confirmed (see the alignment note in §1.1); the margin-label drift in the PDF extract is explained there. Four claims changed as a result of re-checking sources, and each is marked ⚠️ **Corrected** or ✅ **RESOLVED** in place:
>
> | What changed | Where | Impact |
> |---|---|---|
> | Gamepads: the rule allow-list is gone, but **the Driver Station app still supports only six controllers, wired-only**. The SDK, not the rule, is the binding constraint. | §1.3, §0 item 5 | Reverses a purchasing recommendation. **Read before buying a controller.** |
> | **Panels live-tunes Pedro's constants; FTC Dashboard does not.** Dashboard choice is determined by your path library. | §3.2, §3.3, §0 item 8b | Reverses the tool recommendation for Pedro teams. |
> | goBILDA **Pinpoint V2 (3110-0002-0002), $79.99, in stock** supersedes the discontinued v1. | §2.1, §5.1 | Removes a planning risk; adds a driver-compatibility check. |
> | Limelight 3A **stock status could not be re-confirmed** (price $189.00 was). | §2.1, §4.3 | Downgraded from "sold out" to unverified. |
> | **Second verification pass (independent re-read of the manual).** Three citation errors fixed: R503 is at **line 591** (not 668); R502 is at **534–597** (not 599–647); the legal power-regulator device list is **Table 12-3 under R505** (not Table 12-7 under R607/R608). | §1.4 | Citations now resolve to the right text. R704.D, R701, R702/Table 12-9, R901–R904 and R503's 8/8 limit were re-read **verbatim** and all confirmed. |
> | **New:** the SDK's `F` and the community `PIDFController`'s `F` are **different quantities**, and PIDF coefficients **do not persist across a power cycle**. | **§6.1b** (new), §6.2, §9.1 | Resolves the ambiguity that makes §6.2's guide misleading if applied to `DcMotorEx`. |
> | **New:** servos run at **5 V** off hub ports but **6 V** off a Servo Power Module / Injector / Servo Hub. | §1.4 | Changing servo power mid-season silently invalidates tuned positions and timings. |
>
> **Third verification pass — 22 Aug 2026.** R704.D, R701–R711 and R901–R904 were re-read **verbatim** from the manual extract and every one was confirmed word for word; the ftc-docs six-gamepad list and the continued absence of an SDK v12.0 were re-confirmed against live sources. This pass was mostly *additive* — its main finding is that the document was treating the BIOBUZZ game as entirely unknown when a material amount of it is already public.
>
> | What changed | Where | Impact |
> |---|---|---|
> | **NEW — the game is not a blank slate.** FIRST's 3 May 2026 Game Preview names the scoring element (**POLLEN**, a **2.8 in yellow sphere**) and four robot tasks, and four vendors shipped StarterBots against it. | **§1.5** (new) | Converts “wait for kickoff” into ~4 weeks of targeted pre-season software work. **Read this first.** |
> | **NEW — POLLEN is 2.8 in, not 5 in.** FIRST's “similar characteristics to the DECODE ARTIFACTS” refers to the plastic, not the size; the DECODE ARTIFACT was **5 in nominal**. | §1.5 | Any inherited DECODE intake geometry, indexer spacing or ball-count sensor placement is sized wrong. |
> | **NEW — the Q&A opens 28 Sep 2026, 12:00 ET, Lead Coach account only.** Team Updates land **every Thursday** from kickoff. | **§1.6** (new) | Gives the §1.2 R704.D question a concrete address and date. |
> | **NEW — you can build and tune POLLEN vision before kickoff.** The SDK ships `ColorBlobLocatorProcessor` with a **circle fit** and a **`BY_CIRCULARITY`** filter, plus a `ConceptVisionColorLocator_Circle` sample. | **§4.5** (new) | The highest-value pre-kickoff programming task available to you. |
> | **NEW — OpMode lifecycle and IMU orientation** were missing entirely. Both are top-five sources of lost weekends. | **§2.6, §2.7** (new) | — |
> | **NEW — Control Hub hygiene** (config `.xml` backup, `robotControllerLog.txt`, Wi-Fi channel) and an **event-day runbook**. | **§7.9, §9.4** (new) | The unglamorous half of reliability, which is where small teams actually lose events. |
> | Limelight 3A availability ✅ **RESOLVED**: **“Sold Out” at ServoCity**, add-to-cart live at limelightvision.io, $189.00. Also new: **a Control Hub supports only one LL3A**. | §2.1, §4.3 | Removes an unverified flag and adds a hard design constraint. |
>
> Still open, and deliberately so: SDK v12.0 (re-confirmed **not yet released** as of 22 Aug 2026 — newest is v11.2.1, 2026-07-31), the scope of R704.D, **how POLLEN is actually scored**, and everything else that depends on Sections 8–11. Full status table in §11.

---

## 0. Executive summary — the things that matter most

| # | Claim | Why it matters to you |
|---|---|---|
| 1 | **R704.D explicitly names FTC Dashboard and FTControl Panels as prohibited** on the Robot Controller Wi-Fi network. This is NEW for BIOBUZZ; DECODE's equivalent rule did not name any tool. | Your entire tuning workflow depends on this. Read §1.2 before you write a line of code. |
| 2 | Section 12 is final now. You can build, wire, and write 80% of your software **before kickoff**. | 3 free weeks of runway a big team also gets — but you need it more. |
| 3 | The SDK ships a new major version ~1 week before kickoff every year (v9.0 → v10.0 → v11.0). Expect **v12.0 in early Sept 2026**. | Don't start your season repo on v11.x and then fight a migration in week 1. |
| 4 | **Limelight 3A is the only legal programmable vision coprocessor** (R702, Table 12-9). Limelight 3G, OpenMV, OAK-1 are explicitly prohibited. | $189 buys you AprilTag localization with almost no code. It is the single highest-leverage software purchase for a small team. |
| 5 | Gamepad restrictions were **removed from the rules** (DECODE's Table 12-12 allow-list is gone) — **but the Driver Station app still only supports six specific controllers.** | Do **not** buy an exotic gamepad on the strength of the rule change; it will be undetected, not illegal. §1.3. |
| 6 | Servo limit dropped **10 → 8** (R503). | Affects mechanism count planning, which affects your subsystem count, which affects your code volume. |
| 7 | Odometry has commoditized: OTOS $79.95, **Pinpoint V2 $79.99 in stock** (v1 discontinued), OctoQuad MK2 $59.99. Localization is no longer a rich-team advantage. | A $180 localization stack puts you within a few centimeters of a Worlds team's auto accuracy. |
| 8 | **Pedro Pathing** (very active, Aug 2026) and **Road Runner 1.0** (active) are both mature. **FTCLib is effectively unmaintained** (last push Aug 2024) — use **SolversLib** if you want command-based. | Choosing the maintained fork is free; choosing wrong costs you a season of unanswered questions. |
| 8b | Your dashboard choice is **determined by your path library**: Panels can live-tune Pedro's constants, FTC Dashboard cannot. | Picking the wrong one silently costs you the tuning workflow you installed it for. §3.2. |
| 9 | Top teams unit-test their math off-robot in **JUnit 5 + GitHub Actions CI**. FTC #23511 does exactly this today. | This is the cheapest quality tool in existence for a 1-programmer team. Zero dollars. |
| 10 | **SystemCore replaces the Control Hub for FTC starting 2027-28.** BIOBUZZ is the last "Control Hub only" season. | Invest in *portable* skills (Java, control theory, command patterns, git) not Control-Hub trivia. |
| 11 | **"PIDF" means two different things in FTC, and PIDF coefficients are wiped by a power cycle.** The SDK's `F` is a *velocity* feedforward; the `F` in most team code is a *gravity constant*. | The single most common way an FTC programmer loses a weekend. Read **§6.1b** before you tune anything. |
| **12** | **The game is not a blank slate.** FIRST's Game Preview (3 May 2026) already names the scoring element — **POLLEN, a yellow sphere 2.8 in ± 0.1 in, 0.055 lb** — and four robot tasks, one of which is *“autonomously navigate between known locations and intake pollen.”* | You can aim ~4 weeks of pre-season software at the actual game instead of at a guess. **§1.5.** |
| **13** | **POLLEN (2.8 in) is barely half the diameter of a DECODE ARTIFACT (5 in nominal).** “Similar characteristics” is about the plastic, not the size. | Inherited DECODE intake geometry, indexer spacing and ball-counting sensors are all mis-sized. **§1.5.** |
| **14** | **The Q&A opens 28 Sep 2026 at 12:00 ET, and only a Lead Coach can post.** Team Updates drop **every Thursday** from kickoff. | This is the mechanism by which the R704.D ambiguity (item 1) actually gets resolved. Calendar it. **§1.6.** |
| **15** | **You can write and tune POLLEN detection today** — the SDK's `ColorBlobLocatorProcessor` has a circle fit and a `BY_CIRCULARITY` filter, and you already know the ball's colour and diameter. | $5.50 of pollen plus a laptop beats three weeks of vision debugging in November. **§4.5.** |

---

## 1. What is actually LEGAL this season — Section 12.7 & 12.9, rule by rule

**[FACT]** All of §1 is from the local BIOBUZZ V0 manual text, `12_RobotConstruction_R_p64-88.txt`, lines 909–1204. Sections 1–7 and 12 are marked FINAL in the V0 release (published 31 Jul 2026 — [FIRST community post](https://community.firstinspires.org/biobuzz-cm-preview-release)).

### 1.1 The control system allow-list

| Rule | Lines | What it says (paraphrase) | Software consequence |
|---|---|---|---|
| **R701** | 911–930 | Exactly **one** Robot Controller: **(A) REV Control Hub REV-31-1595**, or **(B) an Android smartphone connected to a REV Expansion Hub REV-31-1153**. Optionally **one additional Expansion Hub** (REV-31-1153). Manual states the Control Hub is the *only officially supported* RC; phone users own all compatibility risk. | Two hubs max ⇒ max 8 motor ports, 12 servo ports (but R503 caps you at 8 motors / 8 servos anyway). Plan your `hardwareMap` around 2 Lynx modules and bulk-read **both**. |
| **R702** | 932–977 | You may not modify coprocessor software. Manufacturer **binary firmware updates are allowed**. Exception: *programmable vision coprocessors natively supported by the FTC SDK* may be reprogrammed — **Table 12-9 lists exactly one: Limelight Vision Limelight 3A (`LL_3A`)**. Explicitly ALLOWED as ordinary (non-programmable) coprocessors: Adafruit BNO055, SparkFun OTOS, Digital Chicken OctoQuad FTC Ed., optical-flow sensors, DFRobot HuskyLens, Charmed Labs Pixy2. Explicitly **PROHIBITED**: OpenMV Cam, Luxonis OAK-1, **Limelight 3G**. | Buy the **3A**, not the 3G. You may write Python pipelines on a 3A. You may **not** flash custom firmware onto an OctoQuad or OTOS — only apply vendor binaries. |
| **R703** | 979–984 | If using a phone RC, it connects to the Expansion Hub over USB (any combination of USB/OTG cables and hubs). | Irrelevant if you use a Control Hub. **[JUDGMENT]** Use a Control Hub. Phone RCs are a support burden you cannot afford. |
| **R704** | 986–1010 | **"Use networks and bandwidth as directed."** Five sub-clauses — see §1.2. | **This is the big one.** |
| **R705** | 1012–1023 | RC must be named `<team#>-RC`, DS `<team#>-DS`; spares get a letter, e.g. `12345-A-DS`. | Inspection checklist item. Do it in week 1, not at the venue. |
| **R706** | 1025–1064 | No tampering with DS device, Android RC, power switches, power regulators, fuses, batteries. Allowed: standard connectors, fasteners, thermal interface material, labels, jumper/switch config, **manufacturer firmware updates (F)**, connectorizing integral motor/battery wires, functionally-identical repairs, insulation, debris tape, switch bracket mods. | (F) is your legal basis for updating Hub firmware and Control Hub OS. |
| **R707** | 1066–1072 | **USB is for vision.** Only these may be connected to the robot control system via USB: (A) webcams / optical vision sensors per R708, (B) a USB hub or USB switch, (C) a REV Expansion Hub. | No USB coprocessors, no USB serial gadgets, no Raspberry Pi. |
| **R708** | 1072–1088 | Only **single-image-sensor** vision devices **natively supported by the RC app**. **Stereoscopic cameras are not allowed.** Includes (A) all UVC-compatible USB webcams (Logitech C270 and related), (B) vision coprocessors allowed per R702. UVC devices may only use the **UVC stream/data** — no other interfaces. | This is why the OAK-1 (stereo family, programmable) is out. A $25 UVC webcam is legal. |
| **R709** | 1090–1092 | Self-contained video recorders (GoPro or similar) allowed for **non-functional post-match viewing only**, wireless off. | Legal way to get match video for review. See §8.5. |
| **R710** | 1093–1098 | Lasers only if: part of a sensor, IEC/EN 60825-1 Class I or Exempt, **and** non-visible spectrum. | OTOS uses a laser illuminator — it is called out as allowed in R702's examples. Distance sensors (REV 2m, Rev2mDistanceSensor) fine. |
| **R711** | 1100–1113 | Android device config: (A) Control Hub Wi-Fi password must be changed from default, (B) phones in Airplane Mode, (C) Wi-Fi enabled + **Bluetooth disabled** on RC and DS, (D) DS must have all remembered Wi-Fi Direct groups and Wi-Fi connections removed except the RC's. | Inspection items. (A) and (D) are the ones teams fail. |

> **Note on rule-number alignment — now VERIFIED.** In the extracted PDF text the rule labels sit in a left margin column, so when a rule's body runs long the *next* rule's label prints beside it and appears to lead by one or more lines. Example, verbatim from the extract at lines 979–988:
> ```
> R703  *Smartphone Android devices used as a ROBOT CONTROLLER must connect to the REV Expansion
> R704  Hub using USB. If used as a ROBOT CONTROLLER, ...
>       * Use networks and bandwidth as directed. ...
> ```
> Here `R703` owns the smartphone-USB sentence and `R704` owns "Use networks and bandwidth as directed." The same drift affects R707/R708, R709/R710/R711, and R902/R903.
> **I read every rule body in §12.7 and §12.9 against its leading `*`-headline and confirmed the full mapping** (R701 single RC → R702 coprocessor software → R703 smartphone USB → R704 networks → R705 device naming → R706 permitted modifications → R707 "USB is for vision" → R708 "Use only supported USB vision" → R709 recording devices → R710 lasers → R711 Android device config; R901 DS device → R902 touch screen accessible → R903 console physical requirements → R904 wireless-only). **The IDs in this document are safe to quote.** Local PDF: `manuals/2026-27_BIOBUZZ/`.

### 1.2 R704 — the rule that reshapes your tuning workflow  ⚠️

**[FACT]** R704 (lines 986–1010) requires teams and robots to use Wi-Fi and bandwidth in a way that enables fair play and does not interfere with others. Its five clauses:

| Clause | Requirement |
|---|---|
| A | No wireless communication to/from/within the robot except what the official tools provide. |
| B | All communication signals must originate only from the RC device or DS device on the RC Wi-Fi network. No other device may connect to, interfere with, or alter that network. |
| C | **Programming laptops and all devices other than the DS must be disconnected from the RC Wi-Fi network during MATCH play.** |
| D | Software with access to the RC Wi-Fi network must limit streamed data. Only robot control data, debugging data and telemetry may be streamed, **using the FTC Driver Station Application**. Additional logging/streaming services — the rule names *"third party plugins and tools such as FTC Dashboard, FTControl Panels, and others"* — are **prohibited**. **No continuous video stream is allowed.** |
| E | Events may assign you a Wi-Fi band/channel; if asked, you must comply. |

**[FACT] This is a change.** The DECODE (2025-26) equivalent rule (`manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf`, extracted text line ~5283) said only: bandwidth is restricted, software may stream control/debug/telemetry data, no continuous video stream. **It named no tools and did not use the word "prohibited."**

**[JUDGMENT] What to actually do about it.** Do not panic and do not ignore it. Structure your software so the answer is boring:

1. **Treat Dashboard/Panels as shop-only instrumentation, never as competition infrastructure.** Every constant you tune on Dashboard gets written into a `Constants.java` in the repo *the same session* (FTC #23511's own tuning guide says exactly this, in capital letters — see §6.6). If your robot needs a laptop at an event, you have already lost.
2. **Build a runtime kill-switch, not a compile-time one.** A `static final boolean COMPETITION_MODE` in your constants file that (a) stops you from ever calling `FtcDashboard.getInstance().startCameraStream()`, (b) suppresses dashboard telemetry packets, (c) sets bulk-cache to MANUAL and disables debug loops. One line to flip in the pits.
3. **Move debugging from *streaming* to *logging*.** On-robot file logging is not a network service. Write CSV/log files to the Control Hub and pull them over ADB/USB *after* the match. See §7.7. This is the technique that survives any reading of R704.D.
4. **Assume the strictest reading until a Team Update or Q&A says otherwise.** **[UNVERIFIED]** — as of 21 Aug 2026 I found no Team Update, Q&A entry or Chief Delphi thread interpreting R704.D. Put "confirm R704.D scope" on your kickoff-day checklist (§11).
5. **[UNVERIFIED]** Whether AdvantageScope Lite for FTC (which runs a web server *on the robot*) falls under R704.D. It plausibly does. Use its **file export** path, not its live path, at events.

### 1.3 Operator console (§12.9) — the driver-side rules

| Rule | Lines | Requirement | Software consequence |
|---|---|---|---|
| **R901** | 1148–1170 | Exactly one Android DS device powered on: **(A) REV Driver Hub REV-31-1596**, or (B) any Android device + USB/OTG cables/hubs for gamepads. Driver Hub is the only officially supported DS. | Buy the Driver Hub. $275. |
| **R902** | 1172–1180 | DS touch screen must be visible and usable without aids during inspection and matches. | Don't bury the DS in a box. |
| **R903** | 1181–1195 | Operator console incl. power banks ≤ **3 ft W × 1 ft 6 in D × 2 ft H** (91.4 × 45.7 × 61.0 cm). Consoles > 20 lb invite scrutiny. | Plenty of room for a nice control board. |
| **R904** | 1197–1202 | No wireless comms to/from/within the operator console beyond the RC↔DS link. Active wireless NICs and Bluetooth devices are prohibited examples. | **No Bluetooth controllers.** Wired gamepads only. |

**[FACT] Gamepad allow-list removed.** DECODE had a rule "*Only limited gamepads are supported*" with **Table 12-12** enumerating Logitech F310 etc., capped at 2 gamepads (DECODE extract lines 5508–5548). **BIOBUZZ V0 contains no gamepad table and no gamepad count limit** — R901.B simply says "one or more gamepads." The FIRST preview announcement independently confirms "removed restrictions on allowed gamepads" ([community.firstinspires.org](https://community.firstinspires.org/biobuzz-cm-preview-release)).

⚠️ **[FACT] But the rule is no longer the binding constraint — the SDK is. Do not act on the rule change alone.** The official [ftc-docs Driver Station Components page](https://ftc-docs.firstinspires.org/en/latest/control_hard_compon/ds_components/components/components.html) still enumerates a closed list of gamepads the **Driver Station app itself** supports:

| Supported by the DS app | |
|---|---|
| Logitech F310 | Sony DualSense |
| Sony DualShock 4 | Etpark PS4 Wired |
| Xbox 360 | Quadstick FPS |

The same page states **"All gamepads MUST be used in wired mode only, no wireless of any kind is allowed"** and **"Up to two gamepads, in any combination, of the allowed types of gamepads may be used."**

**[UNVERIFIED]** whether that ftc-docs page has been updated for BIOBUZZ or is carried over from DECODE — it may simply lag the manual. Note the direct tension: BIOBUZZ **R901.B** says "one or more gamepads" with no table, while ftc-docs still says "up to two … of the allowed types."

**[JUDGMENT] What this means practically.** An unsupported controller is not illegal — it is *undetected*. The DS app will not enumerate it and your OpMode will see a dead gamepad, which is a worse failure than a rule violation because it happens at 9 a.m. on match day. So:
- **Do not buy an exotic controller on the strength of the rule change.** The cheap driver-precision win most teams imagine here is not yet available.
- If you want better sticks, the safest upgrade inside the supported list is a **DualSense or DualShock 4** (better stick resolution and ergonomics than an F310) — both are named by ftc-docs, both are wired-capable over USB-C/micro-USB.
- **Test any controller against the actual season SDK on the actual Driver Hub before it ever goes to an event**, and re-test after the v12.0 SDK drops. Put this on the kickoff checklist (§11).
- R904 independently forbids wireless in the operator console, so **wired only** regardless of what any rule table says.

### 1.4 Actuator and sensor limits that shape the code

| Rule | Limit | Software consequence |
|---|---|---|
| **R503** (line 591) | **8 motors and 8 servos** total, across all configurations at an event. *(DECODE was 8 motors / **10** servos — extract line 4781.)* | Two fewer servos than last year. Prefer one servo doing two jobs via a linkage over two servos. Budget: 4 drive + 4 mechanism motors is the norm. |
| **R502** (lines 534–597, Table 12-2 at 538) | Servos ≤ **8 W mechanical output @ 6 V** *and* under the table's stall-current limit — **both** must be met. Named legal: Axon MAX+, goBILDA Dual Mode 2000-0025-0003, REV Smart Servo REV-41-1097, FEETECH FT5335M-FB, DSSERVO DS3235MG, AndyMark am-4954, Studica 75002; linear servos Actuonix P8-100-252-12-R, Hitec HLS12-3050-6V, Studica 75014. **"4th Wire Position Feedback" servos are explicitly permitted.** | Feedback servos (Axon MAX+, FT5335M-FB) give you an analog position signal → you can close a loop on a servo. Rare and useful. |
| **R502 note** (lines 581–589) | ⚠️ **Your servo rail is 5 V or 6 V depending on what powers it.** The manual states plainly: the **REV Control Hub and Expansion Hub provide 5 V to servos**, while the **goBILDA Servo Power Injector, REV Servo Power Module, Studica Servo Power Block, and REV Servo Hub provide 6 V**. Servos rated 6–8.4 V "may not work properly when only provided 5 V." | **[JUDGMENT] This is a software bug generator.** A servo's speed and holding torque differ between 5 V and 6 V, so **every position constant and every `sleep`/timeout you tuned on hub power changes when you add a Servo Power Module mid-season.** Re-verify §6.5 setpoints after any servo-power change, and record which rail each servo is on in `Constants.java`. |
| **R607/R608** (782–816) | CUSTOM CIRCUITS (any active electrical item that is not an actuator per R501 or a power regulation device per R505) **must not provide regulated power above 5 V unless they only power LEDs.** | Any custom sensor board or LED driver you add is a CUSTOM CIRCUIT. Keep it ≤ 5 V. |
| **R505 / Table 12-3** (620–648) ⚠️ *corrected citation* | All actuator **control signals must originate from a power regulating device**, and Table 12-3 is the closed list: goBILDA 6V Servo Power Injector **3125-0001-0001** (2 servos/port), REV Control/Expansion Hub motor ports (2 motors/port) and servo ports (2 servos/port), REV Servo Power Module **REV-11-1144** (2 servos/port), **REV Servo Hub REV-11-1855**, REV SPARKmini **REV-31-1230**, Studica Servo Power Block **75005**. | REV Servo Hub gives you 6 V servo power **and** more servo ports over RS-485 — but the **R503 cap of 8 servos still binds**, so extra ports buy you wiring convenience, not more servos. *(Earlier drafts of this document attributed this list to Table 12-7 under R607/R608; Table 12-7 is "Power Regulation Device Power Requirements" at line 795, a different table. The device list is **Table 12-3**, line 626.)* |
| **R611/R612** (863–888) | Powered USB hubs may only draw from an approved COTS USB battery pack (R602) or the **+5 V aux port** on a REV hub. | Relevant if you add a Limelight *and* a webcam. Check current budget. |
| **R613** (890–907) | Sensors/encoders powered **only** by the regulation device they're plugged into. No cross-wiring power between ports or hubs. | Common inspection failure with dead-wheel pods split across two hubs. Keep a localization sensor group on **one** hub. |

---

### 1.5 Beyond the rules: what is already public about BIOBUZZ, and the software it implies

**[FACT] You are not flying blind.** FIRST published a **Game Preview on 3 May 2026** that names the scoring element and four robot tasks, and all four ecosystem vendors shipped StarterBot designs against it ([FIRST — Game Preview 2027: StarterBots, Skill Builders, Field Elements and More!](https://community.firstinspires.org/game-preview-field-elements)). Sections 8–11 of the manual are still placeholders, but "we know nothing until 12 Sept" is false — and acting as if it were true costs you the three highest-leverage weeks of the season.

#### The scoring element: POLLEN

| Property | Value | Source |
|---|---|---|
| Name | **POLLEN** | FIRST Game Preview |
| Shape / colour | **Sphere, yellow** | [AndyMark `am-5851_preview`](https://andymark.com/products/ftc-2026-27-game-preview-pack) |
| Diameter | **2.8 in ± 0.1 in** (≈ 7.1 cm). FIRST's prose says "approximately 3 in." | AndyMark spec |
| Weight | **0.055 lb** (≈ 25 g) | AndyMark spec |
| Preview pack | **3 elements for $5.50**, part `am-5851_preview` — listed **"Estimated back in stock"** (i.e. backordered) when checked **22 Aug 2026** | AndyMark |
| Full game sets ship | **14 September 2026** | FIRST Game Preview |

⚠️ **[FACT] "Similar characteristics to the DECODE ARTIFACTS" describes the plastic, not the size.** The DECODE ARTIFACT was **5 in. (12.70 cm) nominal** Gopher ResisDent™ polypropylene — local extract `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_INITIAL_kickoff.txt`, lines **2320** and **6298**. **POLLEN is 2.8 in — about 56% of that diameter and under a fifth of the volume.**

**[JUDGMENT]** This is the most immediately useful pre-kickoff fact in this document, and it is a *software* fact as much as a build fact. Every inherited DECODE-era number is wrong: intake throat width, indexer pitch, hopper capacity, and — the one that bites programmers — **the spacing and threshold of any ball-counting sensor**. If you reuse a DECODE break-beam indexer, two pollen will pass through the gap where one artifact used to sit, and your `heldCount` will silently under-report.

#### The four robot tasks FIRST previewed

**[FACT]**, from the Game Preview. Teams should prepare for: acquiring pollen from the foam field surface; collecting multiple pollen simultaneously, in **lines and piles**; retrieving pollen from **field borders and corners**; and **autonomously navigating between known locations while intaking pollen**.

| Previewed task | Software you can write *before* kickoff |
|---|---|
| Acquire pollen from the foam field surface | Intake subsystem + state machine (§7.4–§7.5); motor-current/stall detection for jam recovery |
| Collect **multiple** pollen at once (lines, piles) | **Counting and indexing logic** — a `heldCount` state fed by a break-beam, colour or distance sensor. Sized for a 2.8 in ball. |
| Retrieve pollen from **borders and corners** | Precision low-speed drive mode (§8.3); a robot-centric "corner approach" macro; wall-square heading snap |
| **Autonomously navigate between known locations and intake pollen** | This is *exactly* §5 — localization, path following, and intake sequencing. Nothing about it needs the game manual. |

**[JUDGMENT] What this changes about your plan:**

1. **Your autonomous is already specified in outline: drive to a known pose → intake → drive to a known pose.** FIRST said so in May. That is precisely what Pedro/Road Runner plus a localizer buy you, and you can build *and tune* the entire stack on a bare foam-tile field before you know a single scoring rule.
2. **Build the `heldCount` sensor and its state machine in the pre-season.** "Collect multiple simultaneously" is the one previewed task with no clean DECODE analogue to copy. A break-beam pair is roughly $10 and a couple of evenings, and it is the input every intake macro, every "full — stop intaking" driver rumble, and every auto sequencing decision depends on.
3. **You can write and tune pollen *vision* today.** You know the colour and the diameter, which is all a blob detector needs. See **§4.5**.
4. ⚠️ **[UNVERIFIED] — how POLLEN is actually scored.** The preview describes *acquiring, collecting, retrieving and transporting*. It does **not** say whether pollen is scored by **launching, depositing, or delivering**. DECODE was a launcher game, which is why FTC #23511's flywheel and distance→velocity LUT code (cited in §6.4 and §7.8) exists. **[JUDGMENT]** A ball game often implies a launcher, but **do not commit a mechanism, a gear ratio, or a flywheel control stack to that guess before 12 Sept.** Do build the *generic* closed-loop velocity skill from §6.4 — it transfers unchanged to a flywheel, a roller intake, or a conveyor.

#### StarterBots — free reference designs, available now

**[FACT]**

| Vendor | StarterBot design | Code available now? |
|---|---|---|
| **goBILDA** | **6-wheel drop-center** chassis + **GripForce Gecko™ wheel** intake; a mecanum variant is also offered. Kit **3200-4008-2627, $899.99**; upgrade pack from the 2025-26 kit **3200-0101-2627, $249.99** | **Yes** — assembly instructions, STEP files and an **Example Code** download on the [resource guide page](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/) |
| **REV Robotics** | **Flap-wheel** intake on the REV Channel Drivetrain | **No** — base build guide + Onshape CAD now; the page says *"Preview Starter Bot Programming Guide — Coming Soon"*, full docs after kickoff ([docs.revrobotics.com/ftc-kickoff-concepts](https://docs.revrobotics.com/ftc-kickoff-concepts)) |
| **AndyMark**, **Studica** | Each published a starter design with a drivetrain and intake ([Studica guide](https://www.studica.com/ftc-starter-bot-resource-guide-2026-2027)) | **[UNVERIFIED]** — check each vendor's 2026-27 resource guide |

**[JUDGMENT]** You are not going to build a StarterBot; you have neither $900 nor the hours, and §9 is a better use of both. **Read goBILDA's example code anyway.** It is a free, vendor-maintained reference for how an intake OpMode is structured against *this season's* game element, it costs one evening, and disagreeing with it is itself a useful design conversation to put in the portfolio.

#### Skill Builders — a free driver-practice curriculum

**[FACT]** FIRST Education launched **seven mini-game challenges** on the **FIRST Training** platform, reached through the Lead Coach's FIRST Dashboard (registered users 13+). They cover **precision driving, intake and outtake design, scoring cycles, and autonomous routines**, and ship with lessons, build instructions from all four vendors, printable slides, scoring spreadsheets, setup guidance and a facilitator guide ([FIRST — Introducing FIRST Tech Challenge Skill Builders](https://community.firstinspires.org/introducing-first-tech-challenge-skill-builders)).

**[JUDGMENT]** For a small team this is the cheapest structured driver-practice curriculum that exists (§8.5), and it needs **3 pollen ($5.50) and a floor**, not a field. It also solves the hardest scheduling problem in a small program: giving the non-programmers something measurable to do during the weeks the programmer is head-down. Run the driving and cycle-time challenges weekly from now, and **log the scores** — that graph is Motivate/Control award evidence as well as a training record.

### 1.6 The season information cadence — two dates that belong in your calendar

**[FACT]** From the BIOBUZZ V0 manual, `manuals/2026-27_BIOBUZZ/sections/02_SeasonOverview_p5-21.txt`, §1.7.3–§1.7.4 (lines 604–637):

| What | When | Detail |
|---|---|---|
| **Team Updates** | **Every Thursday**, beginning on **Kickoff day (12 Sep 2026)** and ending **two weeks prior to FIRST Championship** | Posted on the Game and Season Materials page. Additions highlighted in yellow, deletions struck through. ⚠️ **"Team Updates that are published after the driver's meeting at an event will not apply to that event."** |
| **Q&A system opens** | **28 September 2026, 12:00 p.m. ET** | Access is **only through the Lead Coach 1 or Lead Coach 2 account** on the FIRST Dashboard. Moderators answer beginning each **Monday** and close **Thursday at 5:00 p.m. ET**. Q&A responses **do not supersede the manual**; referees and inspectors remain the final authority. |

**[JUDGMENT] Two concrete practices this buys you:**

1. **The Thursday ritual — 15 minutes, every week, one student.** Download the Team Update, drop the PDF into `manuals/`, diff it against your notes, and post a one-line summary to the team channel: *"TU-04: no changes to Section 12."* Rule changes that invalidate a mechanism, a sensor, or a control-system choice get found on Thursday afternoon, not at an inspection table on Saturday morning. This is a textbook Claude Code task (§10) — the student decides what matters, the model does the diffing.
2. **Your R704.D question now has an address and a date.** The largest open risk in this document (§1.2 — are FTC Dashboard and Panels prohibited at an event *entirely*, or only during MATCH play?) is exactly what the Q&A exists for: it references specific rule IDs, it is not a design review, and it is not vague. **Post it the week of 28 Sep.** Two constraints to plan around: only your **Lead Coach** can submit it, and answers land Monday–Thursday, so ask early rather than the week of your first qualifier. Draft the question now, in writing, referencing **R704.C** (explicitly MATCH-scoped) against **R704.D** (not scoped), and ask specifically about pit and practice-field use.


## 2. The official stack

### 2.1 Hardware, with real prices

**[FACT]** As of August 2026 — verify before purchase.

| Item | Part # | Price | Source |
|---|---|---|---|
| REV Control Hub | REV-31-1595 | **$375.00** | [revrobotics.com/rev-31-1595](https://www.revrobotics.com/rev-31-1595/) |
| REV Driver Hub | REV-31-1596 | **$275.00** | [revrobotics.com/rev-31-1596](https://www.revrobotics.com/rev-31-1596/) |
| REV Expansion Hub | REV-31-1153 | UNVERIFIED (historically ~$200) | R701.C |
| Limelight 3A smart camera | 3122-0002-0001 | **$189.00** — ✅ status resolved 22 Aug 2026: **“Sold Out” at ServoCity**, but **add-to-cart is live at limelightvision.io**. Single-source part; order early and re-check both vendors. | [servocity.com](https://www.servocity.com/limelight-3a-smart-camera/), [limelightvision.io](https://limelightvision.io/products/limelight-3a) |
| SparkFun OTOS (PAA5160E1) | SEN-24904 | **$79.95** | [sparkfun.com](https://www.sparkfun.com/sparkfun-optical-tracking-odometry-sensor-paa5160e1-qwiic.html) |
| goBILDA Pinpoint Odometry Computer (v1) | 3110-0002-0001 | **$79.99** — page states **"DISCONTINUED … This product has been discontinued"**, Sold Out | [gobilda.com](https://www.gobilda.com/pinpoint-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/) |
| **goBILDA Pinpoint V2 Odometry Computer** ✅ | **3110-0002-0002** | **$79.99 — In Stock** | [gobilda.com](https://www.gobilda.com/pinpoint-v2-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/) |
| goBILDA 4-Bar Odometry Pod (32 mm) | 3110-0001-0002 | **$99.99**, 2000 CPR | [gobilda.com](https://www.gobilda.com/4-bar-odometry-pod-32mm-wheel/) |
| OctoQuad FTC Ed. MK2 (8ch encoder + IMU) | DigitalChickenLabs | **$59.99** | [tindie.com](https://www.tindie.com/products/digitalchickenlabs/octoquad-ftc-ed-mk2-8x-encoderpwm-imu/) |
| UVC webcam (Logitech C270 class) | — | ~$25–40 | R708.A |

✅ **[FACT] Pinpoint risk RESOLVED (21 Aug 2026).** The v1 page is flagged Discontinued/Sold Out, but goBILDA ships a direct successor: **Pinpoint V2, part 3110-0002-0002, $79.99, In Stock**. Per the product page the V2 adds **CRC8 error detection on the I²C line** (this is the fix for the "Pinpoint occasionally returns a garbage pose" class of bug), **pitch/roll and optional quaternion output**, **user-configurable bulk-read windows** (choose which fields you pull each loop — a real loop-time lever), and **a USB port for firmware updates**. **Buy the V2, not the v1.** ⚠️ **[UNVERIFIED]** whether the SDK-side driver in [goBILDA-Official/FtcRobotController-Add-Pinpoint](https://github.com/goBILDA-Official/FtcRobotController-Add-Pinpoint) and Pedro's `PinpointLocalizer` handle V2's new register map transparently — **confirm the driver version before you rely on it**, and note the precedent in §5.1 that the OctoQuad MK2 needed a vendor driver the SDK did not have.

### 2.2 Firmware / OS versions you must be on

| Component | Version to run | Note |
|---|---|---|
| **REV Hub firmware** | **1.8.2** | **[FACT]** Road Runner requires 1.8.2 and will E-stop without it — [FtcRobotController wiki: Updating Hub Firmware](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/3.-Updating-Hub-Firmware) |
| **Control Hub OS** | **1.1.6** (latest listed) | **[FACT]** [REV OS changelog](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system/operating-system-changelog). 1.1.6 = Wi-Fi driver security. 1.1.4 fixed a BHI260AP IMU reset after ESD. 1.1.2+ defaults to **5 GHz** — your DS must support it. |
| **Driver Hub OS** | Latest available | **[UNVERIFIED]** current version number. |
| **RC / DS app** | Season SDK (see below) | R706.F is your legal basis for updating. |

**[JUDGMENT]** IMU resets after static discharge (fixed in OS 1.1.4) are a classic "our auto randomly failed" bug. Update the OS **before** you blame your code.

### 2.3 SDK version cadence

**[FACT]** From the [GitHub releases API for FIRST-Tech-Challenge/FtcRobotController](https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases):

| Version | Published | Role |
|---|---|---|
| v9.0 | 2023-09-09 | Official — CENTERSTAGE 2023-24 |
| v10.0 | 2024-09-07 | Official — INTO THE DEEP 2024-25 |
| v10.1 / v10.1.1 / v10.2 / v10.3 | 2024-09-20 … 2025-06-25 | In-season optional + offseason |
| **v11.0** | **2025-09-06** | Official — DECODE 2025-26. Min Android Studio **Ladybug (2024.2)** |
| v11.1 | 2026-01-20 | In-season optional |
| v11.2 | 2026-07-15 | Offseason. Requires **Android Studio Narwhal 3 Feature Drop** or later |
| v11.2.1 | 2026-07-31 | Tooling-only, functionally identical to v11.2 |

**Pattern:** a `X.0` official release lands **~5–7 days before kickoff**, a `X.1` optional release lands in January, and `X.2/X.3` offseason releases follow in summer.

**[JUDGMENT]** **Expect v12.0 around 5–8 Sept 2026** (kickoff is 12 Sept). **[UNVERIFIED]** — not announced as of 21 Aug 2026.
Plan accordingly:
- **Pre-kickoff (now):** develop on **v11.2.1** so your Android Studio is already on the newest toolchain. Write mechanism/subsystem/control code, which is version-agnostic.
- **Kickoff week:** create a fresh clone of the v12.0 quickstart, then **copy your `TeamCode` package in**, rather than merging upstream into your fork. FTC upstream releases are not merge-friendly.
- Keep the SDK Maven coordinates in one place. Current form (**[FACT]**, from [Pedro Pathing Quickstart `build.dependencies.gradle`](https://github.com/Pedro-Pathing/Quickstart)):
  ```gradle
  implementation 'org.firstinspires.ftc:RobotCore:11.1.0'
  implementation 'org.firstinspires.ftc:Hardware:11.1.0'
  implementation 'org.firstinspires.ftc:FtcCommon:11.1.0'
  implementation 'org.firstinspires.ftc:Vision:11.1.0'
  // + Inspection, Blocks, RobotServer, OnBotJava at the same version
  ```
  A version bump is then a find-and-replace of `11.1.0`.

### 2.4 Blocks vs OnBot Java vs Android Studio

**[FACT]** GM0's comparison ([gm0.org — Options for Programming](https://gm0.org/en/latest/docs/software/getting-started/options-for-programming.html)):

| | Blocks | OnBot Java | Android Studio |
|---|---|---|---|
| Where code lives | On the RC | On the RC | On your laptop, compiled to an `.apk` |
| Setup cost | None (browser) | None (browser) | ~3 GB install |
| External libraries (Road Runner, Pedro, Dashboard) | No | GM0: *"difficult and borderline impossible"* | Easy — this is the point |
| Git / version control | No (effectively) | No (effectively) | Yes — the whole repo |
| Internet while connected to robot | Blocked (you're on robot Wi-Fi) | Blocked | Works — deploy over USB |
| Debugger, refactoring, code completion | No | Minimal | Full |
| GM0 recommendation | Absolute beginners | Some experience | Advanced / anything serious |

**[JUDGMENT] For a 1–2 programmer team aiming at awards and Worlds-caliber deliverables: Android Studio, day one, no exceptions.** The reasons are not snobbery:
- You cannot use Road Runner, Pedro, or any dependency without it. That is the whole competitive software game.
- You cannot have git history without it — and **git history is portfolio evidence** for Control/Design/Think awards.
- You cannot unit-test or run CI without it (§7.8).
- You cannot use Claude Code effectively without a real repo on disk (§10).

**Use Blocks for exactly one thing:** onboarding a brand-new member in their first two sessions so they see a robot move, then move them to Java. **[JUDGMENT]**

### 2.5 Deploy loop — make it fast

**[JUDGMENT]** Your iteration speed is your season. Target **< 45 s from "save file" to "robot moves."**

| Method | How | Speed | Notes |
|---|---|---|---|
| USB-C cable | Plug laptop → Control Hub, `Run` in Android Studio | Fastest, most reliable | Default. Keep a 10 ft USB-C cable in the pit. |
| **ADB over Wi-Fi** | Connect laptop to RC Wi-Fi, then `adb connect 192.168.43.1:5555` | Nearly as fast, no cable | **[FACT]** Control Hub RC address is `192.168.43.1` ([FTC Dashboard docs](https://acmerobotics.github.io/ftc-dashboard/gettingstarted)); phone RC is `192.168.49.1`. ⚠️ **R704.C: disconnect the laptop before match play.** |
| Gradle daemon warm | Leave Android Studio open all session; don't `Clean` reflexively | Saves 20–40 s per build | Only clean when the build is actually broken. |

---

### 2.6 OpMode lifecycle — the structure every new FTC programmer gets wrong

**[FACT]** ([GM0 — LinearOpMode vs OpMode](https://gm0.org/en/latest/docs/software/getting-started/linear-opmode-vs-opmode.html))

| `LinearOpMode` (sequential) | `OpMode` (iterative) |
|---|---|
| `runOpMode()` runs once after **INIT** | `init()` once after **INIT** |
| `waitForStart()` blocks until **START** | `init_loop()` repeatedly until **START** |
| your own `while (opModeIsActive()) { … }` loop | `start()` once at **START**, then `loop()` repeatedly |
| method returns at **STOP** | `stop()` once at **STOP** |

The two are formally equivalent: `init(); while (!isStarted()) init_loop(); start(); while (!isStopRequested()) loop(); stop();`

**[FACT]** Since **SDK 8.1** the delay between `loop()` calls is a negligible ~1 ms; before that it was unpredictable. **Performance is no longer a reason to pick one over the other.** GM0 standardizes on `LinearOpMode`.

**[JUDGMENT] Use `LinearOpMode` and write your own `while (opModeIsActive())` loop.** Reasons, in order of importance:
- It makes the discipline of §7.4 — *every subsystem's `periodic()` is called exactly once per pass* — physically visible in one place, instead of scattered across callbacks.
- `opModeInInit()` gives you a natural home for the randomized-objective vote in §5.4. You get 10+ seconds and hundreds of frames there, for free, while the field is being cleared.
- Every SDK sample, every GM0 page, every quickstart and every library tutorial is written in it. On a 1–2 programmer team, matching the documentation is worth more than matching your taste.

**Three lifecycle rules that prevent real match losses — [JUDGMENT]:**

1. **Re-apply every PIDF coefficient inside init, on every single run.** They do not survive a power cycle (§6.1b). The pit battery swap is a power cycle.
2. **Never `sleep()` in teleop, and never `sleep()` more than ~50 ms in auto.** Use state machines (§7.5). A `sleep()` cannot be interrupted by the driver and cannot be cancelled cleanly by STOP — a robot that keeps moving after STOP is both a safety problem and a referee conversation.
3. **Do expensive work in init, not in the loop.** Camera startup, `hardwareMap.get()` calls, LUT construction, and file opens all belong before `waitForStart()`. A `hardwareMap.get()` inside a loop is a classic silent loop-time killer (§7.6).

### 2.7 IMU orientation — a two-line bug that breaks field-centric drive and every heading loop

**[FACT]** ([ftc-docs — Universal IMU Interface](https://ftc-docs.firstinspires.org/en/latest/programming_resources/imu/imu.html), [REV — Orientating the IMU](https://docs.revrobotics.com/duo-control/sensors/i2c/imu/orientating-the-imu), SDK sample [`SensorIMUOrthogonal.java`](https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/SensorIMUOrthogonal.java))

The Control Hub's built-in IMU reports **hub-centric** orientation until you tell the SDK how the hub is physically mounted. You declare that with the direction the **printed REV logo** faces and the direction the **USB ports** face:

```java
IMU imu = hardwareMap.get(IMU.class, "imu");
imu.initialize(new IMU.Parameters(new RevHubOrientationOnRobot(
        RevHubOrientationOnRobot.LogoFacingDirection.UP,
        RevHubOrientationOnRobot.UsbFacingDirection.FORWARD)));
```

Legal values for both are `FORWARD, BACKWARD, UP, DOWN, LEFT, RIGHT`. The default is logo **UP**, USB **FORWARD**. Physically impossible pairs (logo UP *and* USB UP) are **rejected at initialization**, so the OpMode tells you rather than misbehaving silently.

**[JUDGMENT] Why this earns its own subsection.** A wrong orientation does not throw and does not crash. It hands you a heading that is negated, rotated 90°, or reading pitch where you expected yaw — and the symptom surfaces three layers away as *"field-centric drive fights the driver"*, *"the heading PID runs away"*, or *"auto turns the wrong way, but only sometimes."* Teams lose entire weekends to this, usually while rewriting perfectly good PID code.

- If the hub is mounted vertically or on its side, use the SDK's **`ConceptExploringIMUOrientation`** sample to *find* the correct pair rather than reasoning about it. Guessing has a 1-in-24 hit rate.
- **Verify it in thirty seconds, before you trust anything downstream:** put yaw on telemetry, rotate the robot counter-clockwise by hand, and confirm yaw **increases**. Do this again after any rebuild that moves the hub.
- Put the two enum values in `Constants.java` (§7.3). When the hub gets remounted on a Thursday night, one line changes instead of a hunt through subsystems.
- **[FACT]** Control Hub OS **1.1.4** fixed a BHI260AP IMU reset after electrostatic discharge (§2.2). If your heading dies mid-match, **check the OS version before you debug your code** — and check `robotControllerLog.txt` for the reset (§7.9).


## 3. Community libraries and frameworks — maturity, cost, and honest verdicts

**[FACT]** Repo statistics pulled from the GitHub API on **21 Aug 2026**. "Last push" is the strongest single maturity signal in this ecosystem.

### 3.1 The landscape

| Library | Repo | Latest coordinate | ★ | Last push | License | What it is |
|---|---|---|---|---|---|---|
| **Road Runner 1.0** | [acmerobotics/road-runner](https://github.com/acmerobotics/road-runner) | — | 266 | 2025-11-02 | MIT | Motion-profiled trajectory generation + following for mecanum/tank |
| Road Runner Quickstart | [acmerobotics/road-runner-quickstart](https://github.com/acmerobotics/road-runner-quickstart) | SDK 11.0.0 | 235 (1720 forks) | 2025-10-31 | BSD-3-Clear | The template you actually clone |
| **Pedro Pathing** | [Pedro-Pathing/PedroPathing](https://github.com/Pedro-Pathing/PedroPathing) | `com.pedropathing:ftc:2.1.2` | 180 | 2026-06-06 | BSD-3 | Reactive path follower (PIDF + centripetal correction) |
| Pedro Quickstart | [Pedro-Pathing/Quickstart](https://github.com/Pedro-Pathing/Quickstart) | SDK 11.1.0 | 32 (475 forks) | **2026-08-19** | BSD-3-Clear | Most recently maintained quickstart in FTC |
| **FTCLib** | [FTCLib/FTCLib](https://github.com/FTCLib/FTCLib) | — | 230 | **2024-08-20** ⚠️ | — | Command-based framework, WPILib-style. **~2 years stale.** |
| **SolversLib** (FTCLib fork) | pkg `com.seattlesolvers.solverslib` | `org.solverslib:core:0.3.3`, `org.solverslib:pedroPathing:0.3.3` (repo.dairy.foundation) | — | active | — | Maintained FTCLib successor by FTC #23511 Seattle Solvers |
| NextFTC | [NextFTC/NextFTC](https://github.com/NextFTC/NextFTC) | — | 18 | 2026-05-30 | GPL-3.0 | Lighter-weight command framework; Pedro + RR extensions |
| Mercurial | [Dairy-Foundation/Mercurial](https://github.com/Dairy-Foundation/Mercurial) | — | 4 | 2025-12-14 | BSD-3-Clear | Kotlin-first command framework |
| **FTC Dashboard** | [acmerobotics/ftc-dashboard](https://github.com/acmerobotics/ftc-dashboard) | `com.acmerobotics.dashboard:dashboard:0.6.0` (maven.brott.dev) | 212 | 2026-05-16 | — | Live tuning (`@Config`), telemetry graphs, field overlay, camera stream |
| **FTControl Panels** | [ftcontrol/ftcontrol-panels](https://github.com/ftcontrol/ftcontrol-panels) | `com.bylazar:fullpanels:1.0.12` (mymaven.bylazar.com) | 35 | 2026-01-09 | — | Dashboard successor: OpMode control, graphs, field canvas, **match record/replay**, Limelight pipeline tuning, plugins |
| MeepMeep | [NoahBres/MeepMeep](https://github.com/NoahBres/MeepMeep) | — | 68 | **2024-09-24** ⚠️ | — | Desktop path visualizer for Road Runner (code-based) |
| Pedro Visualizer | [visualizer.pedropathing.com](https://visualizer.pedropathing.com/) | web | — | active | — | Browser path generator for Pedro — **no install** |
| RRPathGen | [Jarhead20/RRPathGen](https://github.com/Jarhead20/RRPathGen) | — | 42 | 2024-09-18 | MIT | GUI path drawer for Road Runner (by FTC 21511 Vaporwave) |
| **EasyOpenCV** | [OpenFTC/EasyOpenCV](https://github.com/OpenFTC/EasyOpenCV) | — | 246 | 2024-06-15 | — | Now **bundled into the SDK** since v8.2 as VisionPortal — see §4 |
| EOCV-Sim | [deltacv/EOCV-Sim](https://github.com/deltacv/EOCV-Sim) | — | 70 | 2026-06-19 | MIT | Develop/tune OpenCV & VisionProcessor pipelines **on your laptop** |
| **virtual_robot** | [Beta8397/virtual_robot](https://github.com/Beta8397/virtual_robot) | — | 166 | **2026-08-09** | — | 2D FTC simulator (JavaFX). Ships a **DECODE field**, supports **RR 1.0.1 and Pedro 2.1.12** |
| AdvantageScope Lite FTC | [j5155/AdvantageScope-Lite-FTC](https://github.com/j5155/AdvantageScope-Lite-FTC) | `page.j5155.AdvantageScope:lite:v26.0.0` | 6 | 2025-09-07 | AGPL-3.0 | FRC's log viewer, on-robot, for FTC. CSV + **WPILOG** export |
| CTRL-ALT-FTC | [BenCaunt/CTRL-ALT-FTC](https://github.com/BenCaunt/CTRL-ALT-FTC) | docs | — | — | — | The FTC control-theory textbook (PID, feedforward, full-state feedback) |
| Game Manual 0 | [gm0.org](https://gm0.org/) | docs | — | active | — | The community engineering bible |
| PhotonCore | vendored in team repos (`com.outoftheboxrobotics.photoncore`) | — | — | — | — | Loop-time optimization via async Lynx I/O |

### 3.2 Honest verdicts for a 1–2 programmer team

| Question | Verdict | Reasoning |
|---|---|---|
| **Pedro Pathing or Road Runner?** | **[JUDGMENT] Pedro Pathing.** | **[FACT]** Davis Luxenberg's neutral comparison ([cookbook.dairy.foundation](https://cookbook.dairy.foundation/misc/pedro_vs_roadrunner.html), last modified 2026-04-13): Pedro corrects continuously along the path with centripetal-force compensation; RR follows a precomputed motion profile and mostly corrects at the end. Pedro's *predictive braking* mode is "mostly automatic with **one** manual tuner"; RR is "mostly automatic" with 4 automatic + 2 manual steps (+4 more for OTOS). Pedro supports mecanum **and coaxial swerve**; RR supports mecanum and tank. RR's advantages: automatic file logging in an AdvantageScope-supported format, a built-in actions system, and MeepMeep. Pedro's Quickstart was pushed **2026-08-19**; RR's was **2025-10-31**. |
| | **Caveat** | RR is *better at time-consistent trajectories* — if your auto must be repeatable to the tenth of a second (e.g. dodging an alliance partner), RR's profiles are more predictable. **[JUDGMENT]** For a small team, "recovers when it gets bumped" beats "arrives at t=4.20 s every time." |
| **FTCLib?** | **[JUDGMENT] No — use SolversLib.** | **[FACT]** FTCLib's last push is 2024-08-20 — two seasons stale. FTC #23511 (a strong, public team) vendors **SolversLib** (`com.seattlesolvers.solverslib`) into their repo instead; it carries `PIDFController`, `SquIDFController`, `ArmFeedforward`, `ElevatorFeedforward`, `ProfiledPIDController`, and the full command scheduler. |
| **Any command framework at all?** | **[JUDGMENT] Only if you have a second programmer.** | Command-based buys you composability (`SequentialCommandGroup`, `ParallelDeadlineGroup`) and clean cancellation. It costs 1–2 weeks of learning and adds a scheduler you must debug. With one programmer, a **hand-written state machine per subsystem** (§7.5) delivers 85% of the value for 15% of the cost. Adopt command-based in the offseason. |
| **Dashboard or Panels?** | **[JUDGMENT] If you run Pedro: Panels. If you run Road Runner: FTC Dashboard. Either way, shop-only.** | ⚠️ **Corrected.** These are not interchangeable on Pedro. **[FACT]** Pedro's own ["Choosing a Dashboard"](https://pedropathing.com/docs/pathing/dashboard) page says Panels supports **live tuning of Pedro's constants** and **FTC Dashboard does not**, "due to the complexity of Pedro Pathing's constants." Since live constant tuning is the entire reason you install a dashboard, a Pedro team that picks Dashboard has bought the worse tool. **[FACT]** Panels ([docs](https://ftcontrol.bylazar.com/docs/panels/overview/)) advertises OpMode control, telemetry, full graphing, basic field view, capture, typed configurables, and a **Limelight camera proxy**; it announced **1.0.0**. Dashboard remains older, more documented, and is what every **Road Runner** tuning page assumes. **Both are named by name in R704.D**, so the rule exposure is identical — pick on capability, not on rule risk. |
| **MeepMeep?** | **[JUDGMENT] Skip if using Pedro.** | MeepMeep is RR-only and 2 years stale. Pedro's **web visualizer** requires no install and no Java project. If on RR, MeepMeep still works and is worth 30 minutes. |
| **virtual_robot?** | **[JUDGMENT] Yes — this is a small-team superpower.** | **[FACT]** It runs RR 1.0.1 and Pedro 2.1.12 against a DECODE field, needs only IntelliJ IDEA Community + Liberica 17 JDK, both free. Your programmer can develop auto logic on a school laptop **while the robot is being rebuilt**. Its README is honest about limits: idealized physics, only `MecDynamic` fully supports RR/Pedro, and it abstracts rather than implements the SDK — so always re-verify on hardware. |

### 3.3 Minimum dependency set (copy this)

```gradle
// build.dependencies.gradle
repositories {
    mavenCentral()
    google()
    maven { url = 'https://maven.brott.dev/' }              // FTC Dashboard
    maven { url = 'https://mymaven.bylazar.com/releases' }  // Panels (if used)
    maven { url = 'https://repo.dairy.foundation/releases' }// SolversLib (if used)
}
dependencies {
    // SDK — bump this one version string at kickoff
    implementation 'org.firstinspires.ftc:Inspection:11.1.0'
    implementation 'org.firstinspires.ftc:Blocks:11.1.0'
    implementation 'org.firstinspires.ftc:RobotCore:11.1.0'
    implementation 'org.firstinspires.ftc:RobotServer:11.1.0'
    implementation 'org.firstinspires.ftc:OnBotJava:11.1.0'
    implementation 'org.firstinspires.ftc:Hardware:11.1.0'
    implementation 'org.firstinspires.ftc:FtcCommon:11.1.0'
    implementation 'org.firstinspires.ftc:Vision:11.1.0'
    implementation 'androidx.appcompat:appcompat:1.2.0'

    implementation 'com.pedropathing:ftc:2.1.2'
    // Pick ONE dashboard. On Pedro, Panels is the one that can live-tune Pedro's constants (§3.2).
    implementation 'com.bylazar:fullpanels:1.0.12'                // SHOP ONLY — see §1.2
    // implementation 'com.acmerobotics.dashboard:dashboard:0.6.0' // use this instead if on Road Runner

    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.2'   // off-robot tests
}
```
**[FACT]** Coordinates verified against the [Pedro Quickstart](https://github.com/Pedro-Pathing/Quickstart) `build.dependencies.gradle`, the [FTC Dashboard docs](https://acmerobotics.github.io/ftc-dashboard/gettingstarted), and [FTC 23511's `TeamCode/build.gradle`](https://github.com/FTC-23511/Decode-2026). **Total cost: $0.**

---

## 4. Vision

### 4.1 What the SDK gives you free

**[FACT]** **VisionPortal** was introduced in SDK **v8.2** / CENTERSTAGE and absorbed EasyOpenCV into the SDK's `Vision` module — no separate install ([ftc-docs VisionPortal overview](https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/visionportal_overview/visionportal-overview.html), [EOCV-Sim docs](https://docs.deltacv.org/eocv-sim/vision-portal/introduction-to-visionportal/)). VisionPortal can run **multiple processors simultaneously** on **multiple cameras**, and exposes controls for CPU and USB bandwidth.

| Processor | Use | Cost to learn |
|---|---|---|
| `AprilTagProcessor` | Tag ID + full 6-DoF pose | Low — SDK sample works out of the box |
| `TfodProcessor` | TensorFlow object detection | Medium; you must train a model. **[JUDGMENT] Skip.** Historically slow, brittle to lighting, and colour-blob detection solves 90% of FTC problems better. |
| Custom `VisionProcessor` (OpenCV) | Colour blobs, contours, custom geometry | Medium — but **[FACT]** you can develop and tune these entirely off-robot in [EOCV-Sim](https://github.com/deltacv/EOCV-Sim) |
| SDK colour-blob/colour-locator processors | Find coloured game elements | Low. **[JUDGMENT] Start here.** |

### 4.2 AprilTag localization in the SDK

**[FACT]** ([ftc-docs AprilTag localization](https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/apriltag_localization/apriltag-localization.html)) Introduced in **SDK v10.0 (2024)**, credited to Dryw Wade.
- Tell the SDK where the camera sits: `.setCameraPose(new Position(DistanceUnit.INCH, x, y, z, 0), new YawPitchRollAngles(AngleUnit.DEGREES, yaw, pitch, roll, 0))`
- Read global pose: `detection.robotPose.getPosition().x`, `.getOrientation().getYaw(AngleUnit.DEGREES)`
- The SDK ships a per-season tag library with field positions.
- **Caveat from the docs:** the AprilTag reference frame may differ from your IMU frame, your odometry frame, and the official field coordinate frame. You must reconcile them by hand. Also: evaluate accuracy yourself; many teams fuse multiple sources.

**[FACT]** DECODE used **8.125 in (~20.65 cm) 36h11** tags on goal faces for navigation (extract lines 2408–2425). **[UNVERIFIED]** BIOBUZZ tag size, family, IDs and placement — Section 9/10 is a placeholder until 12 Sep 2026. Write your vision code against an **abstraction** (`FieldTags.goalTagIds()`, `FieldTags.tagSize()`) so kickoff is a constants edit, not a rewrite. **[JUDGMENT]**

### 4.3 Limelight 3A

**[FACT]**
- Legal, and the **only** legal programmable vision coprocessor (R702 Table 12-9, part `LL_3A`).
- $189.00, SKU 3122-0002-0001, 93 g, quad-core Cortex-A72 @ 1.5 GHz, **90 FPS @ 640×480** / 60 FPS @ 1280×960, USB-C.
- ✅ **Availability resolved 22 Aug 2026:** ServoCity lists it **“Sold Out”** at $189.00; **limelightvision.io shows an active add-to-cart** at the same price. It is a single-source part — **order it early or plan without it.**
- ⚠️ **[FACT] One per robot.** The limelightvision.io product page states plainly: *“The REV Control Hub can only support a single LL3A at this time.”* Do not design a two-Limelight robot.
- Connects **USB-C → Control Hub USB 3.0 port**; used from Java as `hardwareMap.get(Limelight3A.class, "limelight")`, results via `limelight.getLatestResult()`.
- Supports AprilTag tracking + robot localization, colour blob tracking, neural detection/classification, barcode, and **custom Python pipelines** (legal to write, per R702's programmable-coprocessor exception).
- `updateRobotOrientation()` + `getBotpose_MT2()` give **MegaTag2** IMU-fused localization.
- Marketed as "less than 10 lines of code" for most applications.
([docs.limelightvision.io Limelight 3A quick-start](https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-3a), [servocity.com](https://www.servocity.com/limelight-3a-smart-camera/))

**[JUDGMENT]** For a team with 1–2 programmers this is the **best dollar-per-programmer-hour purchase in FTC**. It moves AprilTag pose estimation off your Control Hub CPU (protecting your loop time) and off your students' plates. Three cautions: (1) it is **sold out at ServoCity as of 22 Aug 2026** and orderable only direct — buy early or plan a webcam fallback (§4.4); (2) **one Limelight per Control Hub**, per the vendor — no multi-Limelight designs; (3) check the +5 V aux / USB power budget against R611/R612 if you also run a webcam alongside it.

### 4.4 Legality quick-reference

| Device | Legal? | Rule |
|---|---|---|
| UVC USB webcam (C270 class) | ✅ Yes — UVC stream/data only | R708.A |
| Limelight **3A** | ✅ Yes, reprogrammable | R702 Table 12-9 |
| Limelight **3G** | ❌ **No** | R702, Example 6 |
| OpenMV Cam | ❌ No | R702, Example 6 |
| Luxonis OAK-1 | ❌ No | R702, Example 6 |
| Any stereoscopic camera | ❌ No | R708 |
| DFRobot HuskyLens, Charmed Labs Pixy2 | ✅ Yes (configurable, not programmable) | R702, Example 5 |
| Optical flow sensors | ✅ Yes | R702, Example 4 |
| Raspberry Pi / Jetson / any USB coprocessor | ❌ No | R707 |

---

### 4.5 Detecting POLLEN — vision you can build and tune before kickoff

**[JUDGMENT]** This is the highest-value pre-kickoff programming task available to you, and almost no small team will do it. You already know the target: a **yellow sphere, 2.8 in ± 0.1 in in diameter** (§1.5). Colour and size are all a blob detector needs. Everything below can be built on a desk with $5.50 of pollen and a laptop, weeks before the field exists.

**[FACT] The SDK ships exactly the right tool.** `ColorBlobLocatorProcessor` implements OpenCV colour-blob detection inside VisionPortal, using either a predefined `ColorRange` or a custom range in **RGB, HSV or YCrCb**. For round targets it offers a best-fit circle (**`circleFit`**) alongside the best-fit rectangle (`boxFit`); `ColorBlobLocatorProcessor.Blob` exposes **`getArcLength()`** and **`getCircularity()`**, available as the **`BY_ARC_LENGTH`** and **`BY_CIRCULARITY`** blob criteria through **`ColorBlobLocatorProcessor.Util.filterByCriteria()`** and **`sortByCriteria()`**. The sample OpModes are **`ConceptVisionColorLocator_Rectangle`** and **`ConceptVisionColorLocator_Circle`**, supplied in both Blocks and Java. ([ftc-docs — Color Processing](https://ftc-docs.firstinspires.org/color_processing/index.html); [Color Locator (Round Blobs)](https://ftc-docs.firstinspires.org/en/latest/color_processing/color-locator-round-blobs/color-locator-round-blobs.html))

**The recipe — [JUDGMENT]:**

1. **Start from `ConceptVisionColorLocator_Circle`.** Do not write a `VisionProcessor` from scratch. This is the rare case where the SDK sample is genuinely the right architecture, not a toy.
2. **Work in HSV, not RGB.** Hue is far more robust to gym lighting than RGB, and yellow occupies a narrow, well-separated hue band. Tune saturation and value generously; tune hue tightly.
3. **Filter by `BY_CIRCULARITY` first, before you touch the colour range.** A sphere is the most circular thing on the field. Yellow field tape, a yellow banner, a scorer's yellow shirt and a reflection off the tile are not. This single filter does more work than any amount of colour tuning, and it is the step most teams skip.
4. **Sort by area, descending, and take the largest blob** — the nearest pollen is almost always the one you want. Keep the top *N* if you need to reason about lines and piles (§1.5).
5. **Estimate range from the fitted circle radius.** You know the true diameter, so `distance ≈ (trueDiameterIn × focalLengthPx) / (2 × radiusPx)`. Calibrate `focalLengthPx` once by photographing a pollen at a measured distance. **This is a pure function of two numbers — unit-test it off-robot (§7.8)**, and it is exactly the kind of small, checkable math that makes a good Control Award exhibit.
6. **Tune the colour range in [EOCV-Sim](https://github.com/deltacv/EOCV-Sim) on your laptop**, against saved photographs — not on the robot. No field, no robot Wi-Fi, no R704.D exposure, and you can iterate while the robot is disassembled.
7. **Collect the image set now.** A phone, three pollen, a grey foam tile, and three lighting conditions (bright gym, dim gym, backlit by a window). Fifty labelled photos is a two-hour job in August that turns vision tuning into a one-hour job in week 1 instead of a three-week saga in November.

**[JUDGMENT] What to build around it.** Wrap the detector behind an interface that returns *intent*, not pixels — `Optional<PollenTarget> nearest()` where `PollenTarget` carries bearing and range. Then the auto-aim macro (§8.3), the intake approach, and the unit tests all depend on a stable two-field record rather than on OpenCV types. When kickoff changes the details, you replace one class.

⚠️ **[UNVERIFIED]** Whether POLLEN comes in more than one colour, and whether colour carries scoring meaning. DECODE's ARTIFACTS were green and purple; the AndyMark preview pack lists **yellow only**. **[JUDGMENT]** Define `PollenColor` as an enum with a single value today and add cases at kickoff — a one-line change that costs nothing now and saves a refactor later.


## 5. Autonomous engineering

### 5.1 Localization options — pick one

**[FACT] + [JUDGMENT]** Error characteristics below are qualitative and drawn from library documentation and community consensus; **measure your own** with the tests in §5.2.

| Approach | Hardware cost | Accuracy | Failure mode | Verdict for a small team |
|---|---|---|---|---|
| **Drive encoders only** | $0 (built into motors) | Poor–fair. Wheel slip integrates into unbounded error. | Ramming a wall or a partner destroys the estimate silently. | Fine for week-1 bring-up and for a "drive forward and park" auto. **Do this first, on day one.** |
| **2 dead wheels + IMU** (**Pinpoint V2**, 3110-0002-0002) | $79.99 + 2 × $99.99 = **$279.97** | Very good | Pod lifts off the tile; I²C bus noise (**V2 adds CRC8 to catch exactly this**). | Best accuracy-per-complexity. ✅ v1 is discontinued; **V2 is in stock** (§2.1). Verify driver support first. |
| **3 dead wheels** (no IMU fusion) | 3 × $99.99 = **$299.97** + encoder ports | Very good | Same, plus you burn 3 encoder ports (OctoQuad MK2 at $59.99 solves that) | Classic. More mechanical work. |
| **SparkFun OTOS** | **$79.95** | Good | Sensitive to ride height and floor surface; degraded on seams/carpet transitions. | **[JUDGMENT] Best cheap option.** One sensor, one I2C port, no pods to design or break. Both RR and Pedro have first-class OTOS support and dedicated tuners. |
| **OctoQuad FTC Ed. MK2** | **$59.99** | Adds 8 encoder inputs + IMU + 1.92 kHz localizer | **[FACT]** *"not compatible with the OctoQuad I2C driver built into the current FTC SDK"* — MK2 uses new firmware; you must use DigitalChickenLabs' own driver from their GitHub. | Buy only if you actually run out of encoder ports. |
| **AprilTag relocalization** (webcam or Limelight) | $25–$189 | Excellent **when a tag is visible**, unusable otherwise | Motion blur, tag occluded by a partner robot, bad lighting. | **[JUDGMENT] Not a primary localizer — a *corrector*.** See §5.3. |

**[JUDGMENT] The small-team recommendation: OTOS ($79.95) + Pedro Pathing + AprilTag correction from a $30 webcam.** Total added cost ≈ **$110**, and it lands you within a few centimetres of a Worlds-level auto without building a single odometry pod.

### 5.2 Tuning localization — the order that works

**[FACT]** Pedro Pathing's docs organize tuning as: **Setup → Localization → Velocity Tuners → Heading → Drive Algorithm → Tests**, with dedicated localizer pages for Drive Encoder, OTOS, Pinpoint, Two Wheel, Three Wheel, and Three Wheel + IMU ([pedropathing.com docs](https://pedropathing.com/docs/pathing/tuning/localization/pinpoint)).

**[FACT]** Road Runner 1.0's tuning sequence ([rr.brott.dev/docs/v1-0/tuning](https://rr.brott.dev/docs/v1-0/tuning/)):

| # | OpMode | Produces | Applies to |
|---|---|---|---|
| 0a | `OTOSAngularScalarTuner` | angular scalar | OTOS only, run first |
| 0b | `OTOSLinearScalarTuner` | linear scalar | OTOS only |
| 0c | `OTOSHeadingOffsetTuner` | heading offset | OTOS only |
| 0d | `OTOSPositionOffsetTuner` | position offset (x, y) | OTOS only |
| 1 | `ForwardPushTest` | `inPerTick` | all |
| 2 | `LateralPushTest` | `lateralInPerTick` | mecanum + drive encoders |
| 3 | `ForwardRampLogger` | `kS`, `kV` | dead wheels |
| 4 | `LateralRampLogger` | `lateralInPerTick` | mecanum + dead wheels |
| 5 | `AngularRampLogger` | `trackWidthTicks`, `kS`, `kV` | all (analysis page differs by localizer) |
| 6 | `ManualFeedforwardTuner` | refined `kS`, `kV`, `kA` | all |
| 7 | `ManualFeedbackTuner` | following gains (Ramsete for tank) | all |
| 8 | `SplineTest` | validates everything above | all |

⚠️ **Note:** RR's ramp-log analysis pages are served from the robot at `http://192.168.43.1:8080/tuning/...` — i.e. **through FTC Dashboard's server**. Under R704.D, do all of this **in the shop**, never at an event. **[JUDGMENT]**

**Verification tests to run before you trust any localizer** — **[JUDGMENT]**, but they take 15 minutes and save a season:

| Test | Procedure | Pass criterion |
|---|---|---|
| **Square test** | Drive a 4 ft × 4 ft square, return to start. | Reported pose within ~1 in and ~2° of start. |
| **Spin test** | Rotate in place 10 full turns. | Heading error < ~5° total. |
| **Push test** | Mid-path, shove the robot 6 in sideways by hand. | Robot re-converges to the path (Pedro) or at least to the endpoint (RR). |
| **Cold-boot repeatability** | Run the same auto 10× from the same start. | Endpoint spread < 2 in. **Record the spread in your engineering portfolio** — judges love this. |

### 5.3 AprilTag relocalization — how to fuse it without making things worse

**[JUDGMENT]** The pattern that works:

1. **Odometry is the truth by default.** It runs at 100+ Hz, is always available, and drifts slowly.
2. **AprilTag is a periodic correction.** It runs at ~10–30 Hz, is sometimes unavailable, and does not drift.
3. **Gate every correction.** Only accept a tag pose if *all* of:
   - tag decision margin above a threshold (SDK exposes it),
   - tag range within a validated distance (measure yours; beyond ~5 ft, yaw error grows fast),
   - robot angular velocity below a threshold (motion blur),
   - the tag pose is within ~12 in of the current odometry estimate (reject outliers).
4. **Blend, don't snap.** `pose = pose*(1-α) + tagPose*α` with α ≈ 0.1–0.2 per accepted frame. Snapping causes visible robot jerks and, in a path follower, large instantaneous error → violent correction.
5. **Log every accept and reject** with the reason. This is what turns "auto was weird" into a 5-minute fix. See §7.7.
6. **Limelight shortcut:** MegaTag2 (`updateRobotOrientation()` + `getBotpose_MT2()`) already does IMU-fused multi-tag solving on the camera. **[FACT]** If you own a 3A, use that instead of hand-rolling. ([Limelight 3A docs](https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-3a))

### 5.4 Structuring a randomized-objective autonomous

**[FACT] How DECODE did it** (`2025-26_DECODE_Competition_Manual_TU32.pdf`, extract lines 2284–2302, 2408–2425):
- An **OBELISK** — a triangular prism outside the field — carries **three AprilTags, IDs 21, 22, 23**, one per face.
- Each face maps to a **MOTIF**: an ordering of 2 purple + 1 green artifacts (GPP, PGP, PPG).
- The obelisk is **randomized by field staff using the event management software AFTER drive teams have placed their robots** — i.e. after you press INIT.
- The manual explicitly warns the OBELISK tag is *not* recommended for navigation (its position is not deterministic).

**[UNVERIFIED]** BIOBUZZ's randomization mechanism. Sections 8–11 are placeholders. But **[JUDGMENT]** every recent FTC game has had *some* pre-match randomization (CENTERSTAGE team prop, DECODE motif), so **build for it**:

```java
// Structure that survives whatever kickoff throws at you.
public enum Objective { A, B, C, UNKNOWN }

// 1. Detect continuously during INIT — you get 10+ seconds and dozens of frames.
//    Vote, don't trust a single frame.
private final EnumMap<Objective,Integer> votes = new EnumMap<>(Objective.class);
while (opModeInInit()) {
    detect().ifPresent(o -> votes.merge(o, 1, Integer::sum));
    telemetry.addData("objective", bestVote());   // DRIVERS MUST SEE THIS
    telemetry.addData("confidence", confidence());
    telemetry.update();
}

// 2. Latch once at start. Never re-detect mid-auto.
final Objective objective = bestVote();

// 3. Default that still scores. UNKNOWN must never mean "do nothing".
PathChain plan = switch (objective) {
    case A -> paths.planA();
    case B -> paths.planB();
    case C -> paths.planC();
    case UNKNOWN -> paths.safeDefault();   // the highest-EV blind route
};
```

**Four rules for randomized autos — [JUDGMENT]:**
1. **The common trunk is 80% of the path.** Structure your auto as `commonPrefix → branch → commonSuffix`. Three fully separate autos means three times the tuning and three times the bugs, on a team that can tune one.
2. **`UNKNOWN` must score.** Pick the branch with the best expected value if you guess blind, not a park.
3. **Show the detection on the DS before the match starts.** Your drivers are your last line of defense against a camera pointed at a wall. **[FACT]** R902 requires the DS screen be visible during a match — use it.
4. **Randomization may occur after INIT** (DECODE did). Detect *during INIT and into the first second of auto*, not only at INIT press.

---

## 6. Controls and a tuning procedure students can follow

### 6.1 Which controller for which mechanism

**[FACT]** GM0's control-loops page ([gm0.org](https://gm0.org/en/latest/docs/software/concepts/control-loops.html)) covers P/I/D, the kV–kA feedforward model, static-friction feedforward, gravity-compensated feedforward (`cos(angle) * kF`), and recommends **trapezoidal motion profiles** for most FTC applications.

| Mechanism | Controller | Feedforward terms | Why |
|---|---|---|---|
| **Vertical linear slide** | PID on position + constant gravity term | `kG` (constant) | Gravity load is constant regardless of extension → one constant holds it up. |
| **Rotating arm / pivot** | PID on angle + gravity comp | `kG·cos(θ)` | Torque from gravity varies with cosine of arm angle. This one term removes most of the pain. |
| **Flywheel / shooter** | **Velocity PID with a dominant `kV`** (or bang-bang) | `kS`, `kV` | Feedforward does 90% of the work; the P term only rejects the disturbance of a game element passing through. Never use position PID. |
| **Intake roller** | Open loop | none | Just set power. Do not over-engineer. |
| **Turret** | PID on angle | `kS` | Low inertia, no gravity; a PD is usually enough. |
| **Drivetrain heading hold** | P or PD on heading error | none | Wrap error to ±180°. |
| **Drivetrain path following** | Library's job (Pedro/RR) | library's | Do not write your own. |
| **Servo mechanism** | Position command only | none | Servos close their own loop. Your job is finding the numbers (§6.5). |

**[FACT] SquID** — a variant that replaces the proportional term with `kP · sign(e) · √|e|` — is in real use: it appears as `SquIDFController` in SolversLib (vendored in [FTC 23511's repo](https://github.com/FTC-23511/Decode-2026)), has a public test repo ([j5155/SquID-Testing](https://github.com/j5155/SquID-Testing)), and is discussed on Chief Delphi in [FTC 12527 Prototype's build thread](https://www.chiefdelphi.com/t/ftc-12527-prototype-2025-build-thread/473681/33). **[JUDGMENT]** It is a nice second-season upgrade (more aggressive far from target, gentler near it, less overshoot). **Do not start here.** Get a working PID first.

### 6.1b PID vs PIDF vs feedforward — what the letters mean, and the SDK trap that eats a weekend

**[JUDGMENT]** More FTC programmer-hours are lost to this one ambiguity than to any other control-theory topic. The word "PIDF" means **two completely different things** depending on whose class you are holding, and the two Fs are not interchangeable.

**The vocabulary, precisely:**

| Term | What it does | Depends on |
|---|---|---|
| **Feedback (P, I, D)** | Reacts to *error* — the gap between where you are and where you want to be. Cannot act until the system is already wrong. | measured error |
| **Feedforward (kS, kV, kA, kG)** | Predicts the output needed *before* any error appears, from a model of the mechanism. | target / geometry, **not** error |
| **PIDF** | Whatever the library author decided to bolt onto PID as a fourth term. **See the collision below.** | — |

⚠️ **The collision.** There are two different `F`s in common FTC use:

| Which `F` | Where you meet it | What it actually is | Correct use |
|---|---|---|---|
| **SDK `F`** | `DcMotorEx.setVelocityPIDFCoefficients(p,i,d,f)` / `setPIDFCoefficients(..., RUN_USING_ENCODER)` | A **velocity feedforward** — output proportional to *target velocity* (a `kV`). It runs **on the Lynx hub**, not in your loop. | Velocity control of a flywheel or drivetrain via the built-in controller. |
| **Community `F`** | `PIDFController` in SolversLib / FTCLib / most team code | Usually a **constant** added to the output — teams use it as `kG`, the gravity-hold term. | Holding a slide or arm against gravity. |

**[FACT]** GM0 is explicit that `RUN_USING_ENCODER` "enables **velocity** feedback using the encoder," and that this mode is widely misunderstood — **encoders work fine without it**; you do *not* need `RUN_USING_ENCODER` to read `getCurrentPosition()`. If you are running your own PID, GM0's recommendation is `RUN_WITHOUT_ENCODER` ([gm0.org — Control Loops](https://gm0.org/en/latest/docs/software/concepts/control-loops.html)).

> **[JUDGMENT] Read §6.2 with this in mind.** FTC #23511's slide guide says "set F = 0.0001 and raise it until the mechanism no longer sags." That is the **community `F`** — a gravity constant — inside their own `PIDFController`. If you type that number into `setVelocityPIDFCoefficients()` on a `DcMotorEx` you have configured a velocity feedforward on a position mechanism and it will behave bizarrely. **Know which class you are holding.**

**Three SDK gotchas, each of which has cost teams a match — [FACT]:**

1. **PIDF coefficients do not survive a power cycle.** The official docs state changes "do not persist if you power cycle the REV Robotics Control Hub or REV Robotics Expansion Hub" ([ftc-docs — Changing PIDF Coefficients](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/pidf_coefficients/pidf-coefficients.html)). **Set them in `init()` every single OpMode run.** A gain you set once from a tuning OpMode is gone the moment the robot is unplugged in the pits.
2. **`RUN_TO_POSITION` double-layers two controllers.** It uses the coefficients for *both* `RUN_TO_POSITION` and `RUN_USING_ENCODER`; because of that layering, **only the `P` coefficient makes logical sense** in the `RUN_TO_POSITION` set (same source). **[JUDGMENT]** This is why `RUN_TO_POSITION` feels untunable. For anything you care about, run your own position loop on `RUN_WITHOUT_ENCODER`.
3. **The SDK's example values `P=2.5, I=0.1, D=0.2, F=0.5` are illustration only** — the docs say so explicitly. They are not a starting point for your mechanism.

**[JUDGMENT] The decision rule:**

| Mechanism | Use |
|---|---|
| Flywheel / shooter velocity | Built-in `setVelocityPIDFCoefficients` **or** your own `kS + kV·v` + small P. Either is fine; the feedforward does the work (§6.4). |
| Slide, arm, turret **position** | **Your own** controller on `RUN_WITHOUT_ENCODER`. Never `RUN_TO_POSITION` for a mechanism you must tune. |
| Anything with gravity | Feedback **plus** an explicit gravity term (`kG` constant for slides, `kG·cos θ` for arms). Feedforward first, then P, then D. |

**The universal ordering — feedforward before feedback.** Get the mechanism to *almost* hold or *almost* reach the target with feedforward alone, then add P to close the remainder and D to damp it. A large P compensating for a missing feedforward gives you oscillation, overshoot, and a motor that runs hot. Every tuning procedure in §6.2–6.5 follows this order deliberately.

### 6.1c Motion profiling — the cheap upgrade after your position loop works

**[FACT]** A trapezoidal profile has three phases — **accelerate, cruise, decelerate** — parameterized by max acceleration and max velocity. Instead of commanding the final setpoint instantly, you command a *moving* setpoint sampled from the profile, and the controller becomes ([CTRL-ALT-FTC — Motion Profiling](https://www.ctrlaltftc.com/advanced/motion-profiling)):

```
motorPower = (profilePosition(t) - currentPosition) * kP  +  kV * profileVelocity(t)  +  kA * profileAcceleration(t)
```

CTRL-ALT-FTC's motivating point: "applying maximum power from a standstill position will cause **slip**." **[FACT]** GM0 recommends **trapezoidal** profiles over S-curve for most FTC applications.

**[JUDGMENT] Why a small team should care.** A profiled mechanism is *gentler on hardware* — and hardware you don't break is hours you don't spend rebuilding. It converts the violent snap of a step input into a controlled sweep, which reduces belt skipping, gear stripping, and the robot rocking on its wheels when the arm slams. Add it **after** §6.2/§6.3 give you a stable position loop, never before — profiling an unstable loop just hides the instability. `ProfiledPIDController` already exists in SolversLib, so this is a ~1 hour change, not a project.

### 6.2 Tuning procedure — vertical slide (PIDF + gravity)

**[FACT]** This is FTC #23511 Seattle Solvers' own checked-in guide, verbatim in structure and numbers, from
`TeamCode/src/main/java/org/firstinspires/ftc/teamcode/tuning/example/TuningGuidePIDF.md` in [FTC-23511/Decode-2026](https://github.com/FTC-23511/Decode-2026). This is a real Worlds-caliber team's actual student-facing procedure — hand it to your programmer.

> ⚠️ **Read §6.1b first.** The `F` in this procedure is the **community `F`** — a constant gravity term inside a `PIDFController` class — **not** the SDK's `setVelocityPIDFCoefficients` velocity feedforward. Typing these numbers into `DcMotorEx` will not work.

> 1. Set **P, I, D, F all to 0**.
> 2. Deploy, open the dashboard, run the OpMode. Graph **`motorPos`** and **`setPoint`** together.
> 3. Move the mechanism by hand up/down; confirm the encoder **increases in the positive direction**. If not, reverse the motor or the encoder.
> 4. Set `setPoint` to a small value, e.g. **200** ticks.
> 5. Set **F = 0.0001**. Move the mechanism up so gravity acts on it.
> 6. Increase **F in steps of 0.0001** until the mechanism **no longer sags** under gravity. *(This is your `kG`.)*
> 7. Set **P = 0.001**. Change `setPoint` by **50–250** ticks at a time.
> 8. If it **undershoots** (the usual case), increase **P in steps of 0.001** until it stops. Change the setpoint again after each increase.
> 9. If it **overshoots**, decrease **P in steps of 0.0001** until it stops.
> 10. Set **D = 0.0003**. Keep stepping `setPoint` by 50–250.
> 11. Increase **D in steps of 0.0001** until motion is smooth.
> 12. **WRITE THE COEFFICIENTS DOWN.** Dashboard does **not** save them. Put them in Android Studio immediately.

**[JUDGMENT] Additions for your team:**
- Leave **I = 0**. GM0's guidance: low-friction systems don't need I; high-friction systems need I but not D ([gm0.org control loops](https://gm0.org/en/latest/docs/software/concepts/control-loops.html)). If your slide has steady-state droop, add a tiny I with an integral clamp — or better, raise `kG`.
- Tune at **competition battery voltage** (≥ 12.5 V), not on a fresh 13.5 V pack. Better: divide output by `voltageSensor.getVoltage()/12.0` so gains are voltage-independent.
- Add **soft limits** in code (min/max ticks) before you tune. A runaway slide during PID tuning is how teams destroy mechanisms.
- Step 12 is the most important step in this document. **Untracked tuning is lost tuning.**

### 6.3 Tuning procedure — rotating arm (gravity varies with angle)

**[JUDGMENT]**, built on GM0's `cos(angle)*kF` model:

1. Zero all gains. Establish the **encoder-tick ↔ degree** conversion and the tick value where the arm is **horizontal** (θ = 0). Write both into `Constants.java`.
2. Command `power = kG * cos(θ)` with the PID disabled. Increase `kG` by 0.01 until the arm **holds still at horizontal**.
3. Verify: at 45° and at vertical, the arm should also roughly hold. If it sags at horizontal but climbs at vertical, your θ = 0 offset is wrong — fix the offset, not the gain.
4. Enable P. Raise it until the arm reaches targets across the whole range without sustained oscillation.
5. Add D to kill overshoot, same 0.0001-scale steps as §6.2.
6. If it can't hold heavy loads at horizontal, raise `kG` before raising I.
7. **Add a motion profile** (trapezoidal) once the position loop is stable — it converts a violent snap into a controlled sweep and drastically reduces mechanical wear. GM0 recommends trapezoidal for most FTC use.

### 6.4 Tuning procedure — flywheel / shooter (velocity)

**[JUDGMENT]**, built on CTRL-ALT-FTC's feedforward chapter ([BenCaunt/CTRL-ALT-FTC](https://github.com/BenCaunt/CTRL-ALT-FTC/blob/main/feedforward-control.md)):

1. Run open loop at 6–8 power levels (0.3 … 1.0). For each, wait for steady state and record commanded power vs measured velocity (ticks/s). **Graph it.**
2. Fit a line: `power = kS + kV · velocity`. The intercept is `kS` (static friction), the slope is `kV`. Two constants, no controller yet.
3. Command `power = kS + kV·targetVel`. You should already land within ~5% of target. **If not, your gearing or friction is the problem, not your gains.**
4. Add a small **P** on velocity error to close the last few percent and to recover after a game element passes through.
5. Add a **`atTarget()`** predicate — `|error| < tol` for N consecutive loops — and **gate the feeder on it**. This single line is the difference between a consistent shooter and a random one.
6. **[JUDGMENT]** Use a **lookup table (interpolated), not a formula**, to map distance → flywheel velocity. **[FACT]** FTC #23511 does exactly this: their `LauncherMathTest` builds an `InterpLUT` mapping velocity (m/s) → ticks/s across 9 breakpoints, plus an inverse LUT — and **unit-tests it off-robot**. See [`LauncherMathTest.java`](https://github.com/FTC-23511/Decode-2026).

### 6.5 Tuning procedure — servos

**[FACT]** From FTC #23511's `ServoTuningGuide.md`:
> Deploy a single/double servo tester OpMode; drive the servo position from the dashboard (*"HIGHLY RECOMMENDED"* over gamepad); for two opposed servos, reverse one; step positions until each mechanism state is right; then **write the values into a constants file (`Globals.java`) — the dashboard will not save them.**

**[JUDGMENT]** Name the constants after **states, not numbers**: `CLAW_CLOSED = 0.32`, `CLAW_OPEN = 0.61`. Never write `0.32` in a subsystem file. When the mechanism is rebuilt on Thursday night, you edit one line.

### 6.6 The meta-rule that makes all of this work

**Every tuning session ends with a git commit whose diff is the changed constants.** **[JUDGMENT]** Not a photo of a screen, not a note in Discord. The reasons:
- R704.D means your dashboard may not be available at events — the code must be the source of truth.
- It gives you a **bisectable history**: "it worked at the league meet" becomes `git log` on `Constants.java`.
- It is portfolio evidence for the Control Award, free.

---

## 7. Software engineering practice

### 7.1 Repo structure

**[FACT]** FTC #23511 Seattle Solvers' actual layout ([FTC-23511/Decode-2026](https://github.com/FTC-23511/Decode-2026), branch `master`):

```
TeamCode/src/main/java/org/firstinspires/ftc/teamcode/
├── globals/
│   ├── Constants.java          # ALL tunable numbers, one file
│   ├── Robot.java              # hardware container / hardwareMap wiring
│   ├── MathFunctions.java      # pure math — unit-testable
│   ├── GoBildaPinpointDriver.java
│   └── OctoQuadFWv3.java       # vendor drivers vendored in
├── commandbase/
│   ├── subsystems/             # Drive, Intake, Launcher, Turret, Camera
│   ├── subsystems/vision/      # AprilTagProcessor, RectProcessor, annotator
│   └── commands/               # FullAim, SetIntake, DriveTo, ClearLaunch...
├── opmode/
│   ├── Auto/                   # NineFar, TwentyOneClose, EighteenQuals...
│   └── TeleOp/                 # EventTeleop, FullTeleOp, AlliancePoseSelector
└── tuning/                     # one folder per mechanism
    ├── drive/  launcher/  turret/  intake/  camera/  octoquad/
    └── example/ TuningGuidePIDF.md, ServoTuningGuide.md   # docs live WITH the code
TeamCode/src/test/java/.../junit/
    GoalZoneTest.java  LauncherMathTest.java  TurretMathTest.java  VirtualGoalSolverTest.java
.github/workflows/test.yml      # CI
```

**[JUDGMENT] Five things to steal from this immediately:**
1. **`globals/Constants.java`** — every tunable number in exactly one file. Zero magic numbers in subsystems.
2. **A `tuning/` package with one OpMode per mechanism**, kept all season. Not throwaway code — *instrumentation*.
3. **Tuning guides as markdown checked in beside the code they describe.** Onboarding, portfolio content, and institutional memory in one artifact.
4. **Auto OpModes named after what they score** (`TwentyOneClose`, `EighteenQuals`) — the drive coach can pick from the DS list without a decoder ring.
5. **A `src/test/` folder.** See §7.8.

### 7.2 Git for a robotics team

**[JUDGMENT]** Everything below is my recommendation; the constraint that shapes it is that a robotics team is 1–3 committers working in 3-hour blocks on a shared physical robot.

| Practice | Small-team version | Why |
|---|---|---|
| Branching | `main` is **always what's on the robot right now.** One short-lived branch per feature: `feat/turret-aim`, `fix/slide-limits`. Merge same week. | Long-lived branches die on a robotics team. Nobody has time to resolve a 3-week conflict at 10 pm before a qualifier. |
| **Competition tag** | Before every event: `git tag qual-1-2026-11-14 && git push --tags` | The night before an event is not the time to discover `main` is mid-refactor. A tag is your instant rollback. |
| **Competition branch** | At the event, work on `event/qual-1`. Merge back to `main` on Sunday. | Event hacks are event hacks. Don't let them silently become your architecture. |
| Commit messages | `<subsystem>: what changed` — `slides: raise kG to 0.0009 after new spool`. | Your commit log becomes the Control Award narrative and the "what changed since it worked" oracle. |
| Constants commits | Separate commits for tuning-value changes vs logic changes. | So `git log -p globals/Constants.java` reads as a tuning journal. |
| Code review | With 2 programmers: **PR + one approval, target < 12 h.** With 1 programmer: **PR to yourself, and re-read the diff before merging.** | **[FACT]** #23511 ships a `.github/PULL_REQUEST_TEMPLATE.md`, so PRs are their real workflow. Even solo, reading your own diff catches an embarrassing number of bugs. |
| What NOT to commit | `local.properties`, `*.apk`, build output. Keep the SDK's `.gitignore`. | — |
| Fork strategy | Fork the SDK once per season into `TEAMNUMBER-2026-biobuzz`. Do **not** try to merge upstream SDK releases into last year's repo. | **[FACT]** The SDK's own CONTRIBUTING.md warns that upstream pulls are not how team repos work. |

### 7.3 Config constants separated from logic

**[JUDGMENT]** Three tiers, and everything belongs to exactly one:

| Tier | Lives in | Changes | Example |
|---|---|---|---|
| **Physical constants** | `Constants.java` | When hardware changes | `TICKS_PER_REV = 537.7`, `TRACK_WIDTH_IN = 14.2` |
| **Tuned gains** | `Constants.java`, `@Config`-annotated for dashboard | Every tuning session | `SLIDE_KP`, `SLIDE_KG`, `FLYWHEEL_KV` |
| **Mechanism setpoints** | `Constants.java`, named by state | When a mechanism is rebuilt | `CLAW_OPEN = 0.61`, `ARM_SCORE_DEG = 78.0` |

Rules: **no numeric literal in any subsystem or OpMode file**, except 0 and 1. Every constant is `public static` (not `final`, if you want dashboard live-edit) with a unit in the name or a comment. **[FACT]** Pedro Pathing follows exactly this convention — its Quickstart's entire tuning surface is a single `Constants.java` holding `FollowerConstants` and `PathConstraints`.

### 7.4 Subsystem abstraction

**[JUDGMENT]** A subsystem is a class that owns hardware and exposes *intent*, not *implementation*:

```java
public class Slides {
    private final DcMotorEx motor;
    private final PIDFController pid;
    private double targetTicks;

    public enum State { STOWED, LOW, HIGH }

    public void setState(State s) { targetTicks = ticksFor(s); }     // intent
    public boolean atTarget() { return Math.abs(err()) < Constants.SLIDE_TOL; }
    public void periodic(double voltage) {                            // called once per loop
        double out = pid.calculate(motor.getCurrentPosition(), targetTicks)
                   + Constants.SLIDE_KG;
        motor.setPower(out * 12.0 / voltage);                         // voltage compensation
    }
}
```
Rules:
- **One `periodic()` per subsystem, called exactly once per loop, from the OpMode.** Never `sleep()` inside a subsystem.
- Subsystems never read the gamepad. OpModes translate gamepad → intent.
- Subsystems never call `telemetry.update()`. They *contribute* telemetry; the OpMode publishes.
- Every subsystem exposes `atTarget()` so state machines and autos can sequence on it.

### 7.5 State machines instead of `sleep()`

**[JUDGMENT]** The single biggest quality jump for a team without a command framework. Replace this:
```java
// BAD: blocks the whole robot, can't react, can't cancel, can't drive
slides.up(); sleep(1200); claw.open(); sleep(300); slides.down();
```
with this:
```java
enum ScoreState { IDLE, RAISING, RELEASING, LOWERING }
// in the loop, once per cycle:
switch (state) {
  case RAISING:   if (slides.atTarget())  { claw.open(); timer.reset(); state = RELEASING; } break;
  case RELEASING: if (timer.seconds()>0.3){ slides.setState(STOWED);    state = LOWERING;  } break;
  case LOWERING:  if (slides.atTarget())  { state = IDLE; } break;
}
```
Benefits: the drivetrain keeps responding, the driver can cancel, and the whole sequence becomes a driver macro (§8.3). **[FACT]** GM0 has a dedicated *Finite State Machines* page under Programming Concepts ([gm0.org software index](https://gm0.org/en/latest/docs/software/index.html)).

### 7.6 Loop time — bulk reads and profiling

**[FACT]** ([GM0 Bulk Reads](https://gm0.org/en/latest/docs/software/tutorials/bulk-reads.html), [SDK `ConceptMotorBulkRead` sample](https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptMotorBulkRead.java))
A bulk read fetches all non-I2C sensor data from a Lynx module in one transaction. Set via `LynxModule#setBulkCachingMode()`:

| Mode | Behaviour |
|---|---|
| `OFF` (default) | Every hardware call is a separate USB/RS-485 transaction. Slow. |
| `AUTO` | Served from a cache that auto-clears so identical repeat reads don't hit stale data. May issue several bulk reads per cycle. |
| `MANUAL` | Same cache, **never auto-cleared** — you call `clearBulkCache()` once at the top of your loop. Most efficient; risks stale data if you forget. |

**[JUDGMENT] Use `AUTO` in your first season. Move to `MANUAL` only after you have a loop-time readout on the screen.** And do it for **both** hubs:
```java
for (LynxModule hub : hardwareMap.getAll(LynxModule.class)) {
    hub.setBulkCachingMode(LynxModule.BulkCachingMode.AUTO);
}
```
**Put loop time on the driver station, always.** One line, and it is the fastest diagnostic you own — a loop time that jumps from 8 ms to 60 ms tells you a camera or an I2C read snuck into the hot path.

**[FACT]** Top teams go further: FTC #23511 vendors **PhotonCore** (`com.outoftheboxrobotics.photoncore`, async Lynx I/O) and a **Profiler** with a `CSVProfilerExporter` — per-section loop timing exported to CSV. **[JUDGMENT]** This is a second-season optimization. A telemetry line is 95% of the value.

### 7.7 Logging to disk and match replay

**[JUDGMENT]** Under R704.D, **file logging is the debugging strategy that is unambiguously safe at events.** Build it in week 2.

| Approach | How | Cost |
|---|---|---|
| **SDK Datalogger** | **[FACT]** Official 4-part wiki tutorial. Writes CSV to the RC at `FIRST/java/src/Datalogs`; pull it, rename `.txt` → `.csv`, open in Sheets. ([FtcRobotController wiki: Datalogging](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Datalogging), sample [`W_DL_OpMode_IMU_v05.java`](https://github.com/FIRST-Tech-Challenge/WikiSupport/blob/master/SampleOpModes/Datalogging/W_DL_OpMode_IMU_v05.java)) | ~1 hour. **Start here.** |
| **Road Runner built-in logs** | **[FACT]** RR automatically writes files in a custom format that AdvantageScope reads ([cookbook.dairy.foundation comparison](https://cookbook.dairy.foundation/misc/pedro_vs_roadrunner.html)). | Free if you use RR. |
| **AdvantageScope Lite FTC** | **[FACT]** `page.j5155.AdvantageScope:lite:v26.0.0`. Reads Road Runner and PsiKit logs *retroactively*; exports **CSV and WPILOG**. ([j5155/AdvantageScope-Lite-FTC](https://github.com/j5155/AdvantageScope-Lite-FTC), AGPL-3.0) ⚠️ It runs a server on the robot — use **file export**, not live view, at events (§1.2). | ~2 hours. Second season. |
| **Panels match record/replay** | **[FACT]** FTControl Panels advertises match recording and replay. ⚠️ Named in R704.D. Shop-only. | — |

**What to log every match — [JUDGMENT]:** timestamp, loop time, battery voltage, per-subsystem state enum, all setpoints and measured positions, localizer pose, every AprilTag accept/reject with reason, and every driver button press. That last one is what lets you answer "did the driver actually press it, or did the macro not fire?"

**Match replay for a small team** = *log file + GoPro video*. **[FACT]** R709 permits self-contained recorders (GoPro or similar) for non-functional post-match viewing with wireless off. Sync the two by battery-voltage dips or the start-of-match timestamp. This costs one camera and gives you 80% of a professional replay workflow.

### 7.8 Testing off-robot — what CAN be tested, and how

This is the highest-ROI practice in this entire document for a 1-programmer team, and almost no small team does it.

**[FACT] FTC #23511 runs JUnit 5 tests in GitHub Actions CI.** Their `.github/workflows/test.yml`:
```yaml
name: Run JUnit Tests
on:
  push:        { branches: [ "**" ] }
  pull_request:{ branches: [ "**" ] }
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { java-version: '17', distribution: 'temurin' }
      - run: chmod +x gradlew
      - run: ./gradlew test
      - uses: EnricoMi/publish-unit-test-result-action@v2
        if: always()
        with: { files: "**/build/test-results/**/*.xml" }
```
Enabled in `TeamCode/build.gradle` with:
```gradle
testOptions { unitTests.all { useJUnitPlatform() } }
```
Their actual tests: `GoalZoneTest`, `LauncherMathTest`, `TurretMathTest`, `VirtualGoalSolverTest`.

| Testable off-robot (pure functions — do it) | Not testable off-robot |
|---|---|
| Distance → flywheel-velocity lookup tables and their inverses | Anything touching `hardwareMap` |
| Angle wrapping / normalization to ±180° | Motor behaviour, servo travel |
| Turret aim solve: robot pose + target pose → turret angle | Real timing, real friction, real battery sag |
| Coordinate transforms (field ↔ robot ↔ camera) | Vision on real images (use **EOCV-Sim** instead) |
| Field-region tests ("is this pose inside the scoring zone?") | Whether the path actually clears the field wall (use **virtual_robot**) |
| PID math against a synthetic plant | |
| Auto **decision logic** given a mocked objective enum | |

**[JUDGMENT] The rule that makes this possible: keep math in `static` methods on a class with no SDK imports** (`MathFunctions.java` in #23511's layout). If a function needs `hardwareMap`, it isn't math — split it.

**Simulation tiers, cheapest first — [JUDGMENT]:**

| Tier | Tool | Tests what | Cost |
|---|---|---|---|
| 1 | JUnit 5 + CI | Your math and decision logic | $0, hours |
| 2 | [virtual_robot](https://github.com/Beta8397/virtual_robot) | Whole autos, path shapes, RR/Pedro integration, on a rendered field | $0, ~2 h setup (IntelliJ Community + Liberica 17 JDK) |
| 3 | [EOCV-Sim](https://github.com/deltacv/EOCV-Sim) | Vision pipelines against recorded images/video | $0, ~1 h |
| 4 | Pedro web visualizer / MeepMeep | Path geometry sanity, before the robot exists | $0, minutes |
| 5 | Real robot on a real field | Everything that actually matters | Expensive — protect it |

Tiers 1–4 exist to make Tier 5 time count. **A small team's competitive advantage is spending its scarce field time on things only the field can teach.**

---

### 7.9 Control Hub hygiene — config files, logs, and the Wi-Fi channel

**[JUDGMENT]** Unglamorous, absent from most teams' plans, and the place small teams actually lose events. None of it is programming; all of it is the programmer's job.

**[FACT]** The Control Hub's **Program & Manage** page is at `http://192.168.43.1:8080` when your laptop is joined to the RC's Wi-Fi. The **Manage** tab offers **Download Logs** — producing `robotControllerLog.txt`, which needs a real editor rather than Notepad — and a **Wi-Fi channel** selector; the Control Hub supports **both 2.4 GHz and 5 GHz**, and changing channel briefly drops the DS before it reconnects. ([ftc-docs — Managing a Control Hub](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.html), [REV — Managing Wi-Fi on the Control Hub](https://docs.revrobotics.com/duo-control/managing-the-control-system/ch-wifi))

| Practice | Why |
|---|---|
| **Back up the robot configuration `.xml`.** | **[FACT]** The configuration file is what maps your `hardwareMap` names to physical ports, and copying that `.xml` between Robot Controllers is the documented way to provision a **spare RC** ([ftc_app wiki — Configuring Your Hardware](https://github.com/ftctechnh/ftc_app/wiki/Configuring-Your-Hardware)). **[JUDGMENT]** Commit a copy into the repo under `config/` every time you tag an event (§7.2). A config lost at 8 a.m. on match day is an hour of retyping sixteen port names under pressure — with typos, in front of a queue. |
| **One config file, one set of names, all season.** | If your OpModes say `"leftFront"`, then every robot, every spare RC and every backup config says `"leftFront"`. Never let a second config with different names exist; that is how "it works on the practice bot" starts. |
| **Device names live in `Constants.java`, not scattered through subsystems.** | `public static final String DRIVE_FL = "leftFront";` — one rename, one line, and the compiler finds every use. |
| **Download the logs after any weird match.** | `robotControllerLog.txt` records ESD resets, I²C failures, hub disconnects, OpMode crashes and full stack traces. It is the always-on, zero-effort version of §7.7, and it is the only forensic record you get from a match you cannot reproduce. |
| **Know how to change your Wi-Fi channel before you need to.** | **[FACT] R704.E:** event staff may assign you a band or channel and you must comply. **[JUDGMENT]** Practise the change in the shop so it takes 60 seconds in the pit with an FTA watching, not fifteen minutes of hunting through menus. |
| **Prefer 5 GHz where the DS supports it.** | **[FACT]** REV recommends the 5 GHz band for dual-band Driver Stations, and Control Hub OS **1.1.2+** defaults to 5 GHz (§2.2). 2.4 GHz in a gym full of phones is a coin flip. |
| **Change the Control Hub Wi-Fi password off default, and write it down somewhere the team can find it.** | **[FACT] R711.A** requires it, and it is an inspection item. A password only one absent student knows is its own kind of outage. |


## 8. Driver-facing software — often worth more than raw mechanism speed

**[JUDGMENT]** This whole section is my recommendation, grounded in the mechanics the rules permit. The claim behind it: in FTC, cycle-time variance between two robots with identical mechanisms is usually driver-interface quality, not mechanism speed. A driver who can reliably do a 6-second cycle beats one who can do 4 seconds and misses one in three.

### 8.1 Control mapping principles

| Principle | Concretely |
|---|---|
| **Drive on one gamepad, mechanisms on the other.** | Gamepad 1 = drivetrain + drive aids. Gamepad 2 = manipulator. Never split the drivetrain across two controllers. |
| **Analog for continuous, digital for discrete.** | Sticks/triggers for drive and manual overrides; buttons for states. |
| **Nothing important on `start`, `back`, or the d-pad diagonals.** | `start`+button is the SDK's gamepad-binding combo; d-pad diagonals are unreliable under stress. |
| **No modal states without a visible indicator.** | If holding `left_bumper` changes what `a` does, the DS screen must say so, in large text. |
| **Every automated action has a manual override.** | One stick or trigger that bypasses closed-loop control entirely, for when an encoder dies mid-match. Practice using it. |
| **Freeze the map before the first qualifier.** | Changing bindings the week of an event is how drivers make expensive mistakes. |

**A defensible default map:**

| Control | GP1 (driver) | GP2 (operator) |
|---|---|---|
| Left stick | Translate (field-centric) | Manual mechanism override |
| Right stick X | Rotate | — |
| Right trigger | Precision mode (scale to ~35%) | Score / release |
| Left trigger | Intake | Intake reverse |
| `a`/`b`/`x`/`y` | Semi-auto macros (§8.3) | Preset heights/positions |
| D-pad up/down | — | Fine trim ±1 preset step |
| `left_bumper` | Reset field-centric heading | Cancel all macros |

### 8.2 Field-centric drive

**[FACT]** GM0's formulas ([gm0.org mecanum drive](https://gm0.org/en/latest/docs/software/tutorials/mecanum-drive.html)):
```java
double y  = -gamepad1.left_stick_y;      // stick Y is inverted
double x  =  gamepad1.left_stick_x * 1.1; // ~1.1 corrects imperfect strafing
double rx =  gamepad1.right_stick_x;

double h = imu.getRobotYawPitchRollAngles().getYaw(AngleUnit.RADIANS);
double rotX = x * Math.cos(-h) - y * Math.sin(-h);
double rotY = x * Math.sin(-h) + y * Math.cos(-h);

double den = Math.max(Math.abs(rotY) + Math.abs(rotX) + Math.abs(rx), 1.0);
fl = (rotY + rotX + rx) / den;   bl = (rotY - rotX + rx) / den;
fr = (rotY - rotX - rx) / den;   br = (rotY + rotX - rx) / den;
```
The denominator normalization preserves the *ratio* between wheels when the sum exceeds 1 — this is what keeps the robot driving straight at full stick instead of curving.

**[JUDGMENT] Three field-centric details that decide whether drivers love it or hate it:**
1. **A heading-reset button is mandatory.** IMUs drift; a driver who can't re-zero at the wall will demand you turn field-centric off.
2. **Seed heading from your localizer, not just the IMU** — if you have odometry or AprilTags, the pose estimate is a better heading source and survives a mid-match reset.
3. **Ship a one-button toggle to robot-centric.** Some drivers are faster robot-centric. Let the data decide, not your opinion.

### 8.3 Driver aids and semi-autonomous macros

**[JUDGMENT]** Ranked by value-per-hour for a small team:

| Aid | What it does | Effort | Value |
|---|---|---|---|
| **`atTarget()` gating** | Feeder/claw won't fire until the mechanism is actually ready | 30 min | ★★★★★ |
| **Preset positions** | One button → known scoring height/angle | 1 h | ★★★★★ |
| **Precision / slow mode** | Trigger scales drive power to ~30–40% | 15 min | ★★★★★ |
| **Score sequence macro** | Raise → wait `atTarget()` → release → retract, as a cancellable state machine (§7.5) | 3 h | ★★★★☆ |
| **Heading snap** | Button snaps robot to 0/90/180/270° via heading PID | 1 h | ★★★★☆ |
| **Auto-aim turret / heading** | Uses localizer + AprilTag to point at the goal continuously | 6 h | ★★★★☆ (★★★★★ if the game rewards aiming) |
| **Drive-to-pose** | Robot drives itself to a scoring pose (Pedro/RR in teleop) | 8 h | ★★★☆☆ — spectacular when it works, disaster when a partner is in the way. Needs an instant abort. |
| **Rumble feedback** | `gamepad1.rumble(...)` on intake success / at-target / endgame warning | 30 min | ★★★★☆ — drivers stop staring at the screen |
| **Endgame timer alert** | Rumble + DS colour change at T-30 s | 20 min | ★★★★☆ |

**Non-negotiable rules for every macro — [JUDGMENT]:**
- **Cancellable at all times** (a dedicated button, plus: any drivetrain stick input aborts a drive-to-pose).
- **Never blocks the drivetrain** unless it is explicitly a drive macro.
- **Times out.** Every macro has a hard deadline after which it returns to IDLE. A macro that hangs because `atTarget()` never became true has cost teams matches.
- **Practiced.** An unpracticed macro is a liability, not a feature.

### 8.4 Driver station telemetry — design it for a person 6 feet away, in a loud gym

**[JUDGMENT]** Three lines, big, at the top, in priority order:
1. **The one thing the driver must know right now** (detected objective during INIT; subsystem state during the match).
2. **A health line**: battery voltage, loop time, "localizer OK / STALE", "camera OK / NO FRAMES".
3. Everything else, below the fold.

Anything requiring the driver to read a number to a decimal place has failed. Use words and states.

### 8.5 Driver practice protocol

**[JUDGMENT]** The cheapest performance improvement available to any team, and the most neglected.

| Practice | Detail |
|---|---|
| **Fixed weekly driver hours** | 2 h/week minimum, scheduled and defended. Drivers practice while builders build. |
| **Timed cycle drills** | Set a 30-second timer; count completed cycles. Log the number every session. The graph is portfolio evidence *and* motivation. |
| **Practice with a dead battery** | Late-match voltage sag changes robot feel. Drivers must have felt it before a match. |
| **Practice the failure modes** | "Encoder is dead, use manual override." "The macro hung, cancel it." |
| **GoPro every practice match** | Legal (R709). Watch it back at 0.5× and count the hesitations — each one is a UI bug. |
| **Two drive teams, always** | Illness and scheduling are real. A backup driver with 4 hours is worth more than a starter with 40. |

---

## 9. The minimum viable software path for 1–2 programmers

**[JUDGMENT]** Ordered. Do not skip forward. Each row assumes ~6 programmer-hours/week.

### 9.1 Pre-kickoff (now → 11 Sep 2026) — you have 3 free weeks

| Wk | Do | Deliverable |
|---|---|---|
| **Now** | Android Studio + JDK 17 installed, SDK v11.2.1 cloned, fork created as `TEAM-2026-biobuzz`, `.gitignore` verified. | A repo that builds. |
| **Now** | Update Control Hub OS to **1.1.6**, Hub firmware to **1.8.2**, DS/RC apps. Rename devices per R705. Then do **all four** parts of the Android-config rule (line 1093, margin-labelled R711): **(A)** change the Control Hub Wi-Fi password off default, **(B)** Airplane Mode on any smartphone, **(C)** **Wi-Fi enabled and Bluetooth disabled** on both RC and DS, **(D)** on the DS, **remove every remembered Wi-Fi Direct group and Wi-Fi connection** except the RC. | Passes control-system inspection today. **(D) is the one teams forget** — a DS that remembers the school Wi-Fi is a classic connection-flakiness bug *and* an inspection finding. |
| **Now** | Build a mecanum teleop from GM0's formulas. Bulk caching `AUTO` on both hubs. Loop time on telemetry. | Robot drives. |
| **Now** | Install [virtual_robot](https://github.com/Beta8397/virtual_robot). | Second programmer can work without the robot. |
| **Now** | Order **3 POLLEN** (AndyMark `am-5851_preview`, $5.50 — backordered, so order today) and photograph them on grey foam tile under three lighting conditions. | The image set that makes §4.5 a one-hour job in week 1. |
| **+1** | `globals/Constants.java`, `Robot.java`, one real subsystem with `periodic()` and `atTarget()`. **Re-apply every PIDF coefficient in `init()`** — they do not survive a power cycle (§6.1b). | The skeleton every later mechanism drops into. |
| **+1** | JUnit 5 + the CI workflow from §7.8. Write one trivial test so it goes green. | CI badge. Free rigor. |
| **+1** | Build the POLLEN detector from `ConceptVisionColorLocator_Circle`: HSV range, `BY_CIRCULARITY` filter, largest-blob sort, range-from-radius (§4.5). Tune it in EOCV-Sim, unit-test the range math. | Working game-element vision **before kickoff**. |
| **+2** | SDK Datalogger writing a CSV every OpMode run. | Debugging that survives R704.D. |
| **+2** | Pedro Pathing installed on the drivetrain; localizer chosen and tuned; run the square/spin/push tests (§5.2). Install **Panels**, not Dashboard, if you are on Pedro (§3.2). | A drivetrain that knows where it is, before you know what the game is. |
| **+2** | Plug every gamepad you own into the Driver Hub and confirm the DS app enumerates it (§1.3). Do this **before** you design a control map around it. | No 9 a.m. surprises on match day. |
| **+2** | Build a `heldCount` sensor + state machine sized for a **2.8 in** ball (§1.5). Break-beam is ~$10. | The input every intake macro and auto sequence needs. |
| **+3** | Run two or three **Skill Builders** challenges (§1.5) as scheduled driver practice; log the cycle counts. | Driver hours + award evidence, before a robot exists. |

**By kickoff you should be able to say: “our robot drives field-centric, localizes to ±1 inch, logs to disk, detects POLLEN, counts what it is holding, and our repo has CI.” Most teams reach half of that in November.**

### 9.2 Kickoff → first qualifier

| Wk | Do | Skip |
|---|---|---|
| 1 | Read Section 12 diffs + the new Sections 8–11. Update `FieldTags` constants. Fresh clone of SDK **v12.0**, copy `TeamCode` in. **Write the simplest auto that scores: drive out, score one, park.** | Perfect autos |
| 2 | Subsystem per mechanism. Presets. `atTarget()` gating. Precision mode. Freeze the driver map. | Command framework |
| 3 | Randomized-objective detection with INIT-time voting + a scoring `UNKNOWN` default (§5.4). | TensorFlow |
| 4 | Tune every mechanism using §6.2–6.5. Commit constants. Run the same auto 10× and record the spread. | SquID, PhotonCore |
| 5 | 2–3 driver macros from §8.3. Driver practice hours begin. | Drive-to-pose |
| 6 | AprilTag correction with gating and blending (§5.3). Log accepts/rejects. | Custom OpenCV |
| 7 | **Reliability week.** Voltage compensation everywhere. Soft limits. Timeouts on every macro. Test with a half-dead battery. Tag `qual-1`. | New features |

### 9.3 The explicit SKIP list

**[JUDGMENT]** Things that look like what good teams do, but are not where a 2-person team's hours belong:

| Skip | Because |
|---|---|
| **TensorFlow / TFOD** | Slow, brittle to gym lighting, needs training data you don't have time to collect. Colour blobs + AprilTags solve nearly every FTC vision problem better. |
| **A command-based framework, in season 1** | 1–2 weeks of learning to gain composability you can approximate with state machines in an afternoon. Adopt it in the offseason. |
| **Writing your own path follower** | Pedro and RR represent thousands of hours. Yours will be worse and will consume your season. |
| **Swerve** | Pedro supports coaxial swerve, so it's *possible*. It is a mechanical, machining, and tuning project that will eat every hour you have. |
| **Custom OpenCV pipelines before you need them** | Only build one when the SDK's colour processors demonstrably fail your specific task. |
| **PhotonCore / MANUAL bulk caching / profilers** | Optimizations for a loop time you have not yet measured as a problem. |
| **Multi-camera setups** | USB bandwidth and CPU contention on the Control Hub; a debugging nightmare. |
| **Rewriting last year's code "properly"** | Your season is 10 weeks. Refactor in June. **[FACT]** R304 explicitly permits reusing software year to year — exploit that. |
| **Six different autos** | One trunk with three branches, tuned to death, beats six untested routes. |

---

### 9.4 Event-day software runbook (print this; put it in the toolbox)

**[JUDGMENT]** Everything below is my recommendation; the rule citations inside it are **[FACT]**. A small team's event performance is dominated by *not losing matches to preventable failures*, and this page is where that happens.

#### The night before

1. `git tag qual-N-YYYY-MM-DD && git push --tags`, then **deploy that exact build to the robot and run it.** A tag you have not run is not a rollback point.
2. Flip `COMPETITION_MODE = true` (§1.2): no dashboard packets, no camera stream, no debug loops.
3. Charge everything — Driver Hub, laptop, every battery — and label the batteries so you can rotate them in order.
4. Copy the robot configuration `.xml` into `config/` and commit it (§7.9).
5. Pull the practice datalogs off the hub so its storage is clean and the match logs are easy to find (§7.7).

#### In the pit, before your first match

| # | Check | Rule / reason |
|---|---|---|
| 1 | RC named `<team#>-RC`, DS named `<team#>-DS` | **R705** |
| 2 | Control Hub Wi-Fi password is not the default | **R711.A** |
| 3 | Bluetooth **disabled**, Wi-Fi enabled, on both RC and DS | **R711.C** |
| 4 | DS has **no remembered Wi-Fi networks or Wi-Fi Direct groups except the RC** | **R711.D** — the most-failed item on this list |
| 5 | Both gamepads enumerate on the Driver Hub, **wired** | ftc-docs supported list (§1.3); **R904** |
| 6 | Every laptop and phone is **off** the RC Wi-Fi network | **R704.C** |
| 7 | Loop time and battery voltage visible on the DS screen | §8.4 |
| 8 | Run each auto once on the practice field; record the endpoint spread | §5.2 |
| 9 | Camera is seeing the field, not a pit wall — detection line shows on the DS | §5.4, rule 3 |
| 10 | PIDF coefficients are set in `init()`, not left over from a tuning OpMode | §6.1b |

#### Between matches — the 90-second triage

| Symptom | Check first | Then |
|---|---|---|
| DS cannot find or connect to the RC | Is a laptop or phone still joined to the RC network? (**R704.B/C**) | Channel congestion — ask the FTA, then change channel from the Manage page (§7.9). **[FACT]** Some venues run Wi-Fi–blocking technology; the DS may *list* the RC and still fail to connect ([REV — Control Hub troubleshooting](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting)) |
| Robot dead after a collision, DS still connected | ESD or a hub brownout. **Download logs** (§7.9) | Confirm Control Hub OS ≥ **1.1.4** (the IMU-reset-after-ESD fix, §2.2) |
| Heading wrong; field-centric fights the driver | Press the heading-reset button (§8.2) | IMU orientation constants (§2.7); look for an IMU reset in `robotControllerLog.txt` |
| Auto ended in the wrong place | Was the robot placed on the correct start pose, squared to the wall? | Re-run the square/spin test (§5.2); read the AprilTag accept/reject reasons out of the log (§5.3) |
| Mechanism sags or won't hold after a battery swap | **PIDF coefficients were wiped by the power cycle** (§6.1b) | Confirm they are applied in `init()` on every run |
| Every servo position is slightly off | Did anything change the servo rail between 5 V and 6 V? (§1.4, the R502 note) | Re-verify the setpoints from §6.5 |
| Loop time jumped from ~10 ms to ~60 ms | A camera or an I²C read moved into the hot path | Bulk-cache mode on **both** hubs (§7.6); expensive calls belong in init (§2.6) |

#### Rules for event-day code changes

**[JUDGMENT]** This is the discipline that separates teams that climb the rankings from teams that spiral out of them:

- **Work on `event/qual-N`, never on `main`** (§7.2).
- **One change at a time, then a full match-length test.** Never stack two untested changes; if it then breaks, you have no idea which one did it.
- **Nothing new after your last practice match.** Tuning constants, yes. New features, no.
- **If it worked this morning and does not now, `git checkout` the tag.** Do not debug forward under time pressure — you will be wrong and you will be out of time.
- **The drive team decides, not the programmer.** If the drivers have not practised it today, it does not go in the robot today.
- **Log the change in the notebook as it happens**, one line each. On Sunday that list is the most honest engineering-process evidence you will ever hand a judge (§7.2).


## 10. Using Claude Code without hollowing out the students

**[JUDGMENT]** The goal from your brief is that AI gives students **more** hands-on time, not less. That only happens if the AI absorbs the *typing and lookup*, not the *deciding*. Concretely:

| Give to Claude Code | Keep with students |
|---|---|
| Boilerplate: hardware map wiring, telemetry plumbing, OpMode scaffolds | **Which mechanism to build and why** |
| Translating a tuning procedure into a tuning OpMode | **Turning the knobs and watching the robot** |
| Writing JUnit tests for a math function they specify | **Deciding what "correct" means** |
| Explaining a stack trace or a Gradle failure | **Reproducing the bug on the robot** |
| Refactoring `sleep()` chains into state machines | **Designing the state machine on a whiteboard first** |
| Drafting portfolio sections **from the git log and datalogs** | **The engineering decisions the portfolio describes** |
| Diffing the BIOBUZZ manual against DECODE at kickoff | **Reading Sections 9–11 themselves.** Non-negotiable. |

**Repo hygiene that makes Claude Code effective — [JUDGMENT]:**
- A `CLAUDE.md` at the repo root stating: SDK version, library versions, `Constants.java` is the only place for numbers, subsystems expose `periodic()`/`atTarget()`, no `sleep()` in teleop, tests live in `src/test`.
- Keep the tuning guides as markdown in the repo (§7.1) — they become context Claude can follow.
- Keep `Constants.java` small and commented with units, so the model doesn't guess.

**[FACT]** A community plugin marketplace exists: [ncssm-robotics/ftc-claude](https://github.com/ncssm-robotics/ftc-claude) ships Claude Code plugins for `pedro-pathing`, `roadrunner`, `ftclib`, `nextftc`, `panels`, `ftc-dashboard`, `limelight`, `pinpoint`, `robot-dev` (build/deploy/ADB helpers) and a game-reference plugin (currently `decode`). It follows the open Agent Skills standard. **[UNVERIFIED]** its quality, maintenance status, and whether a BIOBUZZ game plugin will appear. **[JUDGMENT]** Evaluate it, don't adopt it blind; the `robot-dev` ADB/deploy helper is the lowest-risk piece to try first.

**Guardrails — [JUDGMENT]:**
- **Never deploy AI-written code to the robot without a student reading the whole diff aloud.** This is both a safety rule and a learning mechanism.
- Judges ask "who wrote this?" Be straightforward: AI-assisted, students directed and reviewed it. **[FACT]** R101 requires the robot and its major mechanisms be built by the team; **[JUDGMENT]** the same spirit should govern how you present your software.
- Log AI-assisted decisions in the engineering notebook the same way you'd log a mentor's suggestion.

---

## 11. Kickoff-day checklist (12 Sep 2026)

| # | Action | Owner |
|---|---|---|
| 1 | Download the full manual; run `tools/ingest-manual.sh`; diff Section 12 V0 → V1. | Programmer |
| 2 | **Verify R704.D wording survived to the final manual and check the Q&A/Team Update for scope.** Decide the shop-only-tools policy in writing. | Programmer + coach |
| 3 | Read Sections 8–11 (Game Overview / Arena / Details / Rules) end to end. Students, not AI. | Whole team |
| 4 | Extract from Section 9/10: **AprilTag family, size, IDs, field positions**, and the field coordinate origin. Fill in `FieldTags.java`. | Programmer |
| 5 | Identify the randomization mechanism (if any) and what must be detected, and when. | Programmer |
| 6 | Confirm whether **SDK v12.0** shipped; note its minimum Android Studio version; create a fresh clone. | Programmer |
| 7 | Re-check R501/R502/R503 for motor/servo list changes; confirm 8/8 held. | Build lead |
| 8 | Re-check Table 12-9 — did any vision coprocessor get added or removed? | Programmer |
| 9 | Confirm the gamepad rule stayed open **and** re-check the [ftc-docs supported-controller list](https://ftc-docs.firstinspires.org/en/latest/control_hard_compon/ds_components/components/components.html) against the v12.0 DS app. **Plug every controller you own into the Driver Hub and confirm the DS enumerates it** before ordering anything. | Programmer + coach |
| 10 | Re-price and re-check stock: **Pinpoint V2 (3110-0002-0002)**, Limelight 3A. | Coach |
| 11 | If using Pinpoint V2, confirm the goBILDA SDK driver and your path library's `PinpointLocalizer` support V2's register map before tuning localization. | Programmer |
| 12 | Read **Sections 9–10 against §1.5**: which of the four previewed tasks survived, and **how is POLLEN actually scored** (launch / deposit / deliver)? This decides whether §6.4's flywheel work is load-bearing. | Programmer + build lead |
| 13 | Confirm POLLEN's final dimensions and **colour count** against §1.5's 2.8 in / yellow, and re-tune the §4.5 HSV range against the real element under gym lighting. | Programmer |
| 14 | Diff the **randomization** mechanism (if any) against §5.4's vote-and-latch structure. | Programmer |
| 15 | Put the **Thursday Team Update ritual** (§1.6) on the calendar for every Thursday of the season, with a named owner. | Coach |
| 16 | Draft the **R704.D Q&A question** now; have the **Lead Coach** post it the week the Q&A opens, **28 Sep 2026, 12:00 ET** (§1.6). | Coach |
| 17 | Download the vendor **StarterBot example code** released after kickoff (goBILDA now, REV post-kickoff) and read the intake OpMode (§1.5). | Programmer |

**Open questions carried into kickoff** *(status as of 22 Aug 2026, third verification pass)*:

| # | Question | Status |
|---|---|---|
| 1 | Exact scope of **R704.D** — does it prohibit Dashboard/Panels *at all times at an event*, or only during MATCH play? Clause C is explicitly MATCH-scoped; clause D is not. | **STILL OPEN**, but now **ACTIONABLE**. No Team Update, Q&A entry or Chief Delphi thread interpreting R704.D existed as of 22 Aug 2026, and community docs (Pedro's, Panels') discuss dashboards with no mention of rule restrictions — they are not a legality source. ✅ **The route to an answer is now known: the Q&A opens 28 Sep 2026, 12:00 ET, Lead Coach account only (§1.6).** Draft the question now; **assume the strict reading** until answered. |
| 2 | Whether **AdvantageScope Lite FTC**'s on-robot web server falls under R704.D. | **STILL OPEN.** Use its file-export path at events. |
| 3 | **SDK v12.0** existence, date, minimum Android Studio version. | **STILL OPEN — re-confirmed not yet released on 22 Aug 2026.** Newest is v11.2.1 (2026-07-31) and the repo still describes itself as the DECODE 2025-26 SDK. Pattern says v12.0 lands ~5–8 Sept. |
| 4 | goBILDA **Pinpoint** discontinuation and successor. | ✅ **RESOLVED.** v1 (3110-0002-0001) discontinued; **Pinpoint V2 (3110-0002-0002), $79.99, in stock.** *(Driver compatibility is tracked separately as question 11.)* |
| 5 | Whether the SDK's gamepad driver accepts arbitrary HID controllers now that the rule allow-list is gone. | ✅ **RESOLVED — and the answer is no.** ftc-docs still lists six supported controllers, wired-only. The **SDK, not the rule**, is the binding constraint. See §1.3. Sub-question: whether that ftc-docs page gets updated for BIOBUZZ. |
| 6 | **BIOBUZZ AprilTag** family, size, IDs, field placement, and the field coordinate origin. | **STILL OPEN** — Sections 9/10 are placeholders until 12 Sep. Code against a `FieldTags` abstraction (§4.2). |
| 7 | BIOBUZZ **randomization** mechanism (DECODE had the OBELISK/MOTIF). | **STILL OPEN.** Build the vote-and-latch structure in §5.4 regardless. |
| 8 | **How is POLLEN scored** — launched, deposited, or delivered? | **STILL OPEN.** §1.5 gives the four *previewed* robot tasks (acquire, collect multiple, retrieve from borders/corners, autonomously navigate + intake); none of them is a scoring method. Build generic closed-loop velocity control (§6.4), not a flywheel-specific stack, until 12 Sept. |
| 9 | Does POLLEN come in **more than one colour**, and does colour carry scoring meaning? | **STILL OPEN.** AndyMark's preview pack lists **yellow only**; DECODE's ARTIFACTS were green and purple. Code `PollenColor` as a one-value enum today (§4.5). |
| 10 | **Limelight 3A** availability. | ✅ **RESOLVED 22 Aug 2026.** **“Sold Out” at ServoCity** at $189.00; **add-to-cart live at limelightvision.io**. New constraint found: **a REV Control Hub supports only one LL3A** (§4.3). Order early or plan a webcam fallback. |
| 11 | Do the **goBILDA SDK driver** and Pedro's `PinpointLocalizer` handle **Pinpoint V2**'s register map? | **STILL OPEN.** Re-checked 22 Aug 2026: the goBILDA driver repo's `goBILDA-Odometry-Driver` branch and Pedro's Pinpoint page (which documents `PinpointConstants`, defaulting to `goBILDA_4_BAR_POD`) neither confirm nor deny V2 support. **Confirm with the vendor before you buy V2 and build a season on it.** |

---

## 12. Sources

**Local files**
- `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` (lines 480–1204) — R501–R904
- `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/sections/03_Eligibility_Inspection_I_p22-26.txt`, `05_EventRules_E_p33-42.txt`
- `C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf` — DECODE R503 (8 motors/10 servos), R706 bandwidth rule, Table 12-12 gamepads, OBELISK §9.6 and AprilTags §9.10

**Official**
- [FIRST — BIOBUZZ Competition Manual Preview Release](https://community.firstinspires.org/biobuzz-cm-preview-release)
- [FIRST — Current Game and Season Materials](https://ftc-resources.firstinspires.org/ftc/game)
- [FIRST — Control System Update, FTC Edition (SystemCore)](https://community.firstinspires.org/control-system-update-first-tech-challenge-edition)
- [FtcRobotController releases](https://github.com/FIRST-Tech-Challenge/FtcRobotController/releases) · [Updating Hub Firmware](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/3.-Updating-Hub-Firmware) · [Datalogging wiki](https://github.com/FIRST-Tech-Challenge/FtcRobotController/wiki/Datalogging) · [`ConceptMotorBulkRead`](https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/ConceptMotorBulkRead.java)
- [ftc-docs — SDK overview](https://ftc-docs.firstinspires.org/en/latest/ftc_sdk/overview/index.html) · [VisionPortal overview](https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/visionportal_overview/visionportal-overview.html) · [AprilTag localization](https://ftc-docs.firstinspires.org/en/latest/apriltag/vision_portal/apriltag_localization/apriltag-localization.html) · **[Driver Station Components — supported gamepad list](https://ftc-docs.firstinspires.org/en/latest/control_hard_compon/ds_components/components/components.html)** (§1.3)
- [FIRST — 2026-2027 BIOBUZZ season materials](https://ftc-resources.firstinspires.org/ftc/archive/2027) · [V0 Competition Manual](https://ftc-resources.firstinspires.org/ftc/game/manual)

**Community documentation**
- [Game Manual 0](https://gm0.org/) — [software index](https://gm0.org/en/latest/docs/software/index.html), [options for programming](https://gm0.org/en/latest/docs/software/getting-started/options-for-programming.html), [control loops](https://gm0.org/en/latest/docs/software/concepts/control-loops.html), [mecanum drive](https://gm0.org/en/latest/docs/software/tutorials/mecanum-drive.html), [bulk reads](https://gm0.org/en/latest/docs/software/tutorials/bulk-reads.html)
- [CTRL-ALT-FTC](https://github.com/BenCaunt/CTRL-ALT-FTC) — [feedforward](https://github.com/BenCaunt/CTRL-ALT-FTC/blob/main/feedforward-control.md), [PID tuning methods](https://github.com/BenCaunt/CTRL-ALT-FTC/blob/main/the-pid-controller/tuning-methods-of-a-pid-controller.md), **[motion profiling](https://www.ctrlaltftc.com/advanced/motion-profiling)** (§6.1c)
- **[ftc-docs — Changing PIDF Coefficients](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/pidf_coefficients/pidf-coefficients.html)** — source for §6.1b: coefficients do not persist across power cycle; `RUN_TO_POSITION` double-layering means only `P` is meaningful there · [Changing PID Coefficients](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/pid_coefficients/pid-coefficients.html)
- [Road Runner 1.0 tuning](https://rr.brott.dev/docs/v1-0/tuning/) · [Pedro Pathing](https://pedropathing.com/) · [Pedro vs Road Runner (Davis Luxenberg, Dairy Cookbook)](https://cookbook.dairy.foundation/misc/pedro_vs_roadrunner.html)
- [FTC Dashboard getting started](https://acmerobotics.github.io/ftc-dashboard/gettingstarted) · [FTControl Panels docs](https://ftcontrol.bylazar.com/docs/overview/) · [Panels overview](https://ftcontrol.bylazar.com/docs/panels/overview/) · **[Pedro Pathing — Choosing a Dashboard](https://pedropathing.com/docs/pathing/dashboard)** (source for the §3.2 correction: Panels live-tunes Pedro's constants, FTC Dashboard does not)
- [goBILDA Pinpoint V2 (3110-0002-0002)](https://www.gobilda.com/pinpoint-v2-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/) — successor to the discontinued v1
- [EOCV-Sim VisionPortal intro](https://docs.deltacv.org/eocv-sim/vision-portal/introduction-to-visionportal/)

**Repos referenced**
[acmerobotics/road-runner](https://github.com/acmerobotics/road-runner) · [road-runner-quickstart](https://github.com/acmerobotics/road-runner-quickstart) · [Pedro-Pathing/PedroPathing](https://github.com/Pedro-Pathing/PedroPathing) · [Pedro-Pathing/Quickstart](https://github.com/Pedro-Pathing/Quickstart) · [FTCLib/FTCLib](https://github.com/FTCLib/FTCLib) · [NextFTC/NextFTC](https://github.com/NextFTC/NextFTC) · [Dairy-Foundation/Mercurial](https://github.com/Dairy-Foundation/Mercurial) · [acmerobotics/ftc-dashboard](https://github.com/acmerobotics/ftc-dashboard) · [ftcontrol/ftcontrol-panels](https://github.com/ftcontrol/ftcontrol-panels) · [NoahBres/MeepMeep](https://github.com/NoahBres/MeepMeep) · [Jarhead20/RRPathGen](https://github.com/Jarhead20/RRPathGen) · [OpenFTC/EasyOpenCV](https://github.com/OpenFTC/EasyOpenCV) · [OpenFTC/EOCV-AprilTag-Plugin](https://github.com/OpenFTC/EOCV-AprilTag-Plugin) · [deltacv/EOCV-Sim](https://github.com/deltacv/EOCV-Sim) · [Beta8397/virtual_robot](https://github.com/Beta8397/virtual_robot) · [j5155/AdvantageScope-Lite-FTC](https://github.com/j5155/AdvantageScope-Lite-FTC) · [j5155/SquID-Testing](https://github.com/j5155/SquID-Testing) · **[FTC-23511/Decode-2026](https://github.com/FTC-23511/Decode-2026)** (the exemplar team repo cited throughout §6–§7) · [goBILDA-Official/FtcRobotController-Add-Pinpoint](https://github.com/goBILDA-Official/FtcRobotController-Add-Pinpoint) · [DigitalChickenLabs/OctoQuad](https://github.com/DigitalChickenLabs/OctoQuad) · [ncssm-robotics/ftc-claude](https://github.com/ncssm-robotics/ftc-claude)

**Vendors (prices as of August 2026 — re-check)**
[REV Control Hub](https://www.revrobotics.com/rev-31-1595/) · [REV Driver Hub](https://www.revrobotics.com/rev-31-1596/) · [REV OS changelog](https://docs.revrobotics.com/duo-control/managing-the-control-system/updating-operating-system/operating-system-changelog) · [goBILDA Pinpoint](https://www.gobilda.com/pinpoint-odometry-computer-imu-sensor-fusion-for-2-wheel-odometry/) · [goBILDA 4-Bar Odometry Pod](https://www.gobilda.com/4-bar-odometry-pod-32mm-wheel/) · [SparkFun OTOS](https://www.sparkfun.com/sparkfun-optical-tracking-odometry-sensor-paa5160e1-qwiic.html) · [OctoQuad FTC Ed. MK2](https://www.tindie.com/products/digitalchickenlabs/octoquad-ftc-ed-mk2-8x-encoderpwm-imu/) · [Limelight 3A (ServoCity)](https://www.servocity.com/limelight-3a-smart-camera/) · [Limelight 3A docs](https://docs.limelightvision.io/docs/docs-limelight/getting-started/limelight-3a)

**Added by the third verification pass (22 Aug 2026)**
- **Pre-kickoff game intelligence (§1.5):** [FIRST — Game Preview 2027: StarterBots, Skill Builders, Field Elements and More!](https://community.firstinspires.org/game-preview-field-elements) · [FIRST — Introducing FIRST Tech Challenge Skill Builders](https://community.firstinspires.org/introducing-first-tech-challenge-skill-builders) · [AndyMark BIOBUZZ POLLEN Game Preview Pack (`am-5851_preview`)](https://andymark.com/products/ftc-2026-27-game-preview-pack) · [goBILDA FTC StarterBot Base Resource Guide 2026-2027](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/) · [REV — 2026-27 DUO FTC Preview Starter Bot](https://docs.revrobotics.com/ftc-kickoff-concepts) · [Studica — FTC Starter Bot Resource Guide 2026-2027](https://www.studica.com/ftc-starter-bot-resource-guide-2026-2027)
- **POLLEN vs ARTIFACT size (§1.5):** local extract `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_INITIAL_kickoff.txt`, lines 2320 and 6298 — ARTIFACT is "5 in. (12.70 cm) nominal Gopher ResisDent polypropylene"
- **Season cadence (§1.6):** local extract `manuals/2026-27_BIOBUZZ/sections/02_SeasonOverview_p5-21.txt` §1.7.3 Team Updates (line 610) and §1.7.4 Question & Answer System (lines 620–637, Q&A opens **28 Sep 2026 12:00 ET**)
- **OpMode lifecycle (§2.6):** [GM0 — LinearOpMode vs OpMode](https://gm0.org/en/latest/docs/software/getting-started/linear-opmode-vs-opmode.html)
- **IMU orientation (§2.7):** [ftc-docs — Universal IMU Interface](https://ftc-docs.firstinspires.org/en/latest/programming_resources/imu/imu.html) · [REV — Orientating the IMU](https://docs.revrobotics.com/duo-control/sensors/i2c/imu/orientating-the-imu) · SDK samples [`SensorIMUOrthogonal.java`](https://github.com/FIRST-Tech-Challenge/FtcRobotController/blob/master/FtcRobotController/src/main/java/org/firstinspires/ftc/robotcontroller/external/samples/SensorIMUOrthogonal.java) and `ConceptExploringIMUOrientation`
- **Colour-blob / round-blob vision (§4.5):** [ftc-docs — Color Processing](https://ftc-docs.firstinspires.org/color_processing/index.html) · [Color Locator (Round Blobs)](https://ftc-docs.firstinspires.org/en/latest/color_processing/color-locator-round-blobs/color-locator-round-blobs.html) · [Color Locator (Discover)](https://ftc-docs.firstinspires.org/en/latest/color_processing/color-locator-discover/color-locator-discover.html)
- **Control Hub hygiene and event triage (§7.9, §9.4):** [ftc-docs — Managing a Control Hub](https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/managing_control_hub/Managing-a-Control-Hub.html) · [REV — Managing Wi-Fi on the Control Hub](https://docs.revrobotics.com/duo-control/managing-the-control-system/ch-wifi) · [REV — Control Hub Troubleshooting](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting) · [REV — Driver Hub Troubleshooting](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/driver-hub-troubleshooting) · [ftc_app wiki — Configuring Your Hardware](https://github.com/ftctechnh/ftc_app/wiki/Configuring-Your-Hardware)
- **Re-verified on 22 Aug 2026 and unchanged:** [FtcRobotController releases API](https://api.github.com/repos/FIRST-Tech-Challenge/FtcRobotController/releases) (no v12.x; newest v11.2.1, 2026-07-31) · [ftc-docs — Driver Station Components](https://ftc-docs.firstinspires.org/en/latest/control_hard_compon/ds_components/components/components.html) (six supported gamepads, wired only, "up to two") · [FIRST — BIOBUZZ CM Preview Release](https://community.firstinspires.org/biobuzz-cm-preview-release) (the three named V0 changes: servos reduced to 8, gamepad restriction removed, expansion limits reinstated) · R701–R711 and R901–R904 re-read verbatim from the local manual extract

