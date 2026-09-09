# FTC VENDOR ECOSYSTEMS

### The buyer's map of the FTC parts world — profiles, the interoperability map, the ecosystem-commitment decision, procurement reality, and a pre-kickoff standing order for a two-robot program

**Built:** 2026-08-21 (pre-kickoff) | **Target season:** 2026-27 BIOBUZZ presented by RTX | **Kickoff:** 2026-09-12
**Corpus root:** ``
**Calibration target:** ~15 students, TWO registered FTC teams (A team + B team), **two robots**, modest budget, 3D printers and hand tools only (no CNC mill), limited mentor hours.

> **THE BIOBUZZ GAME IS NOT PUBLIC.** Nothing here describes BIOBUZZ game play. Sections 8, 9, 10, 11, 13 and 15
> of the V0 pre-season manual are placeholders deferred to Kickoff. **Section 12 (ROBOT Construction Rules, R) is
> FINAL** — so *what is legal to bolt to the robot is knowable right now*, and that is exactly what a vendor map
> needs. Every legality claim below cites a rule ID from
> `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`.

---

## 0. How to read this file

### 0.1 Evidence labels (matched to `ROBOT-ARCHETYPE-LIBRARY.md` / `SCORING-PATTERNS.md`)

| Label | Meaning |
|---|---|
| **[C]** CONFIRMED-BIOBUZZ | Text present in the BIOBUZZ V0 manual's already-final sections (Section 12 unless noted) |
| **[H]** HISTORICAL | From a prior season's manual or a prior season's published vendor/FIRST document. A pattern, never a BIOBUZZ fact |
| **[D]** DERIVED | Arithmetic or logic on stated values. Inputs cited, the conclusion is mine |
| **[J]** JUDGMENT | Engineering/procurement opinion calibrated to this specific two-team program. Not a fact |
| **UNVERIFIED** | Could not be established. Treat as unknown |

### 0.2 Parts-row confidence tags (the anti-hallucination contract)

| Tag | What it guarantees |
|---|---|
| **VERIFIED** | I loaded that vendor page (or that FIRST PDF) **in this session** and read the name, SKU and price off it |
| **FAMILY-ONLY** | I verified the *product family* and the *category URL*, but **not** the specific SKU. Marked **NEEDS-SKU-CHECK** |
| **MANUAL-SKU** | The part number comes from a **BIOBUZZ V0 manual table** (12-1/12-2/12-3/12-9) that I grepped. The *price* is separately tagged |
| **UNVERIFIED** | Named from context only. Do not order against this row without checking |

**Every price in this file is "as of 2026-08-21" and is marked VERIFY-BEFORE-ORDER.** FTC vendors reprice at
season turnover. Prices are US list, pre-discount, pre-tax, pre-shipping.

**No SKU appears in this document unless it came off a page I actually loaded, or out of a V0 manual table I
actually grepped.** Where I only know the family, the row says so and links the category page I *did* load.
Section 9 is the full verification log of URLs opened this session.

### 0.3 Where this file sits

| File | What it gives you |
|---|---|
| `reference/CONSTRUCTION-RULES-R.md` | Full Section 12 R-rule detail — the legality source of truth |
| `reference/ROBOT-ARCHETYPE-LIBRARY.md` | Which mechanisms you might build; this file tells you where to buy them |
| `reference/ACHIEVABILITY-FACTORS.md` | The weighted factor model incl. **duplicability**, which this file operationalises as "can I buy two?" |
| `research/SMALL-TEAM-ECONOMICS.md` | Whole-program dollars and hours. This file is the parts half of that |

---

## 1. The decision in one page

**[J] Recommendation for this program: commit to goBILDA as the single structural + motion ecosystem, and to
REV as the single electrical/control ecosystem. Buy the control system through the FIRST storefront. Do not mix
structural systems between the A robot and the B robot.**

Four reasons, in order of weight for a two-robot program:

1. **Duplicability is a buying problem before it is a design problem.** Two robots means every BOM line is
   ordered twice. A single ecosystem means one part number, one order, one CAD library, one hex key size, and a
   B-team student can walk to the A-team's parts bin and find the identical part. Two ecosystems doubles the
   inventory taxonomy on a program that already doubles the inventory count.
2. **goBILDA's discount is the largest verified discount in the FTC world and it is nearly storewide.** goBILDA
   states **25% off "nearly every product storewide"** for all FIRST teams, **"active for the life of the team"**
   ([verified](https://www.gobilda.com/ftc/)). REV's is **15% and only on "select items"** in a specific discount
   category, with codes that **"expire May 31, 2027"** ([verified](https://www.revrobotics.com/ftc/discounts/)).
   On a structural/motion spend, 25%-storewide beats 15%-on-a-subset decisively. **[D]**
3. **The 18-inch cube (R102) plus 8 motors / 8 servos (R503) rewards dense, bolt-together mechanisms**, which is
   goBILDA's whole design language: 8mm hole grid, 14mm bearing seats built into the pattern, and REX shafting
   that runs in round-bore bearings. Packing an intake, a lift and a drivetrain into 18 in³ **[C]** with hand tools
   is a fit-and-tolerance problem, and a fine-pitch fixed pattern removes a class of "we drilled it 2 mm off" failures.
4. **The electrical side is not a choice.** R701 permits exactly two ROBOT CONTROLLER configurations, and both are
   REV: "**A. a REV Control Hub (REV-31-1595), or B. a smartphone Android device connected to a REV Expansion Hub
   (REV-31-1153)**" **[C]**. You are a REV electrical customer no matter what you decide about aluminium.

**The one condition under which REV DUO is the better structural choice:** if the team's design instinct is
*adjustability* — sliding a bracket to tension a chain instead of re-drilling — and if a mentor is already fluent
in extrusion. REV's 15 mm extrusion has "slots on all four sides that accept standard M3 hardware"
([verified](https://docs.revrobotics.com/duo-build/structure/intro)), so it has **infinite** pitch where goBILDA has
8 mm pitch. That is genuinely better for prototyping and worse for repeatability, and repeatability is what a
two-robot program is short of. See §4.4 for the full argument.

**Cost of the recommendation, with the goBILDA team discount already applied:** roughly **$4.0k–$4.5k** for the
pre-kickoff standing order across both robots (§6.9), of which about **$1.2k is control system bought through the
FIRST storefront** at prices FIRST negotiated below retail (§2.6). About **65% of that total is four purchase
decisions** — two storefront bundles and two goBILDA kits.

> **Correction, 2026-08-22:** an earlier revision of this line read "$2.6k–$3.5k, before discount," which
> contradicted the itemised rollup in §6.9. The §6.9 line-item arithmetic was re-checked and is correct
> ($3,965 low / $4,505 high); this summary figure was wrong and has been conformed to it. **[D]**

---

## 2. Vendor profiles

### 2.0 Official FIRST supply roles vs general suppliers

The phrase "official FTC vendor" gets used loosely. Here is what is actually verifiable:

| Vendor | Verified role with FIRST for 2026-27 | Evidence |
|---|---|---|
| **Pitsco** | **Operates the FIRST storefront.** The FIRST Tech Challenge Storefront PDF instructs teams to use the team Dashboard to "access the Pitsco Storefront to purchase materials" | FIRST storefront PDF, rev 25-26.4 (Feb 18, 2026) **[H]** |
| **REV Robotics** | **Supplies the control system inside the FIRST kits.** The Electronics Kit contents are REV Control Hub + REV sensors; the Driver Kit contains a REV Driver Hub; the Build Kit is the "REV FIRST Tech Challenge Competition Set V3.1" | FIRST storefront PDF **[H]**; R701 names REV hardware exclusively **[C]** |
| **AndyMark** | **Supplies the season game/field elements.** FIRST's own game-preview post directs teams to `andymark.com/ftc-2026-27` for the BIOBUZZ scoring element, stated as "available for purchase and immediate shipment from AndyMark" | FIRST community game-preview page, verified this session |
| **AndyMark, goBILDA, REV, Studica** | **All four are official StarterBot partners for 2026-27.** FIRST hosts a StarterBot Base page per vendor under `ftc-resources.firstinspires.org/ftc/archive/2027/team/` | FIRST community game-preview page, verified this session |
| **ServoCity** | Same company/catalogue lineage as goBILDA (ServoCity discontinued Actobotics in June 2023 "to focus on goBILDA"). No separate FIRST role verified | gm0 Actobotics page, verified this session |
| **Limelight Vision, Digital Chicken Labs, SparkFun, Adafruit, Actuonix, Hitec, FEETECH, DSSERVO, Axon, NFR, SWYFT, WATTOS** | **Component-only suppliers named in V0 manual tables.** Not build-system vendors. Legal because a manual table names them, not because they are "official" | Tables 12-1, 12-2, 12-9 **[C]** |

**[J] Practical read:** buy *control system* from the FIRST storefront (cheapest legal path), *game elements* from
AndyMark (sole source), and *everything mechanical* from your chosen ecosystem vendor.

---

### 2.1 goBILDA — the metric bolt-together system

- **Category URLs loaded this session:** [/structure/](https://www.gobilda.com/structure/) ·
  [/motion/](https://www.gobilda.com/motion/) · [/electronics/](https://www.gobilda.com/electronics/) ·
  [/hardware/](https://www.gobilda.com/hardware/) · [/channel/](https://www.gobilda.com/channel/) ·
  [/shafting-tubing/](https://www.gobilda.com/shafting-tubing/) · [/pattern-adaptors/](https://www.gobilda.com/pattern-adaptors/) ·
  [/ftc/](https://www.gobilda.com/ftc/) (the FIRST discount page)

**Known for:** a single, obsessively consistent metric pattern; anodised aluminium channel; the REX shaft system;
the deepest FTC-facing motion catalogue (26 motion categories verified, from *Gears* and *Sprockets & Chain* through
*Linear Slides*, *Lead Screws*, *Shocks*, *CV & Universal Joints* and *Control-Arms*).

**Structural system.** Metric, **M4** hardware. The pattern is **"4mm holes on an 8mm grid"**
([verified](https://www.gobilda.com/pattern)), with **"a 14mm hole to easily seat a bearing"** worked into the grid,
and **"clocked (rotated) the four holes closest to the bearing hole"** so components can mount at 45°. Slots
"come from joining nearby holes and give you adjustability when mounting." A secondary **32 mm square pattern** of
four thru-holes is used for hubs, spacers and pillow blocks. Structure categories verified: Channel, goRAIL®, Beams,
Shafting & Tubing, Mounts, Clamping Mounts, Grid Plates, Pattern Plates, Brackets, Baseplates, Pattern Adaptors,
Pattern Spacers, Standoffs & Spacers, Threaded Plates, Hinges, Structure Bundles.

**Channel families (verified names):** `1120 Series U-Channel` (48 mm, full-height sides), `1121 Series Low-Side
U-Channel` (12 mm sides), `1143 Series Mini Low-Side U-Channel` (12 mm tall × 32 mm wide), `Rail-Channel`, plus the
`goRAIL®` line. 1120 U-Channel comes in **27 variants from 1-hole/48 mm to 49-hole/1200 mm, $4.99–$50.99** (verified).

**Shaft standard — REX®.** goBILDA's differentiator. Their own words: **"The REX® profile is a fusion of Round and
HEX profiles which combines the best of both worlds. The six outer points of the hex are clipped to a common
diameter so you can run the shafting in a round bore bearing."** ([verified](https://www.gobilda.com/stainless-steel-rex-shafting/)).
Sizes verified: **8 mm REX** ($3.69–$17.99, 24–624 mm) and **12 mm REX** ($3.99–$19.99, 32–624 mm; "passes through
14mm goBILDA center holes", M4 threaded ends). Also stocked: stainless round, **6 mm D**, Hub-Shafts, and 25-tooth
servo shafts.

**Power transmission:** **8 mm pitch chain** (steel `3308-0008-1000` $11.99, plastic `3309-0108-0050` $7.99) — *not*
#25. Belts: **GT2 2 mm**, **HTD 3 mm**, **HTD 5 mm**.

**Strengths [J]:** highest parts-per-dollar after the 25% discount; every mechanism you can name has a bolt-together
path; the pattern makes chain/belt centre-to-center distances land on grid, which removes a whole tensioning
headache; excellent for hand-tool-only shops.

**Gaps [J]:** M4 hardware is heavier and coarser than M3 for tiny mechanisms; 8 mm chain is an ecosystem lock-in
(§3.5); the catalogue is *large enough to be a decision cost* for a rookie; goRAIL/extrusion offerings are newer and
less proven in FTC than the channel line.

**Price positioning:** mid, and **effectively the cheapest of the majors once the 25% storewide FIRST discount is
applied.** Anchors verified this session: Yellow Jacket motors **$54.99–$56.99**; Dual Mode servos **$36.99**;
Proton servos **$17.99**; 96 mm omni **$21.99**; 96 mm mecanum set **$169.99**; 2-stage 336 mm Viper-Slide kit **$159.99**.

---

### 2.2 REV Robotics — the extrusion system, and the only legal control system

- **Category URLs loaded this session:** [/ftc/](https://www.revrobotics.com/ftc/) ·
  [/duo/](https://www.revrobotics.com/duo/) · [/ion/](https://www.revrobotics.com/ion/) ·
  [/15mm-extrusions/](https://www.revrobotics.com/15mm-extrusions/) · [/ftc/discounts/](https://www.revrobotics.com/ftc/discounts/) ·
  [docs.revrobotics.com/duo-build/structure/intro](https://docs.revrobotics.com/duo-build/structure/intro) ·
  [docs.revrobotics.com/duo-build/building/compatibility](https://docs.revrobotics.com/duo-build/building/compatibility)

**Known for:** the **Control Hub / Driver Hub / Expansion Hub** control system that R701 makes mandatory **[C]**;
the **DUO** 15 mm extrusion build system; aggressive use of Delrin to hold cost down.

> **Critical naming trap: REV DUO is the FTC system. REV ION is the FRC system.** REV's own ION page describes it
> as **"a comprehensive ecosystem ... designed to integrate seamlessly with the existing FRC landscape"**
> ([verified](https://www.revrobotics.com/ion/)). ION parts (MAXSpline shafts, 2-inch bolt circles, MAXTube) will
> arrive, will be beautiful, and will bolt to **nothing** on your FTC robot. Buy from `/duo/`, never `/ion/`. **[D]**

**Structural system.** Metric, **M3** hardware. **"REV Extrusion is a rectangular structure rail with slots for M3
hardware on all four sides"**, in **15 mm** and **15 mm × 30 mm** profiles; extrusion ends have a **5 mm hole pitch**
that can be M3-tapped. **"Structural brackets have M3 holes on an 8mm pitch."** Channels: **15 mm × 45 mm C Channel**
and **45 mm × 45 mm U Channel**, with **"M3 holes on an 8mm pitch down the center of the Channel"** and **"Every 16mm
a center hole is opened up to become a 9mm bearing seat."** ([verified](https://docs.revrobotics.com/duo-build/structure/intro))

**The Motion Pattern.** REV's rotational-mounting standard is **"a circular M3 hole pattern on a 16mm diameter"**,
with an **Extended Motion Pattern** on a **32 mm diameter**. Note the 32 mm coincidence with goBILDA's 32 mm pattern —
the *diameters* match, the *hole sizes* do not (M3 vs M4). **[D]**

**Shaft standard:** **5 mm hex**, "precision ground 5 mm stainless steel (SUS303)", stocked in 75 / 90 / 135 / 400 mm,
"can be cut if needed" ([verified](https://docs.revrobotics.com/duo-build/motion/intro/shaft)); adaptable to 1/2 in
UltraHex. **Chain: #25 roller** (`REV-41-1365`), which REV explicitly frames as the interop currency —
**"#25 pitch chain ... because it's common to all systems."**

**Strengths [J]:** the slot beats the hole grid for anything you have to tune (chain tension, belt tension, sensor
placement, bumper height); lighter than channel for the same span; Delrin brackets are cheap enough to break without
grief; and the control-system half is non-optional and excellent.

**Gaps [J]:** extrusion has a real learning curve — gm0 calls it "a bit higher learning curve than most other kits";
slot-mounted joints *move* under impact if under-torqued, which is exactly the failure a rookie B-team will not
diagnose; and M3 in aluminium strips more readily than M4 under student torque.

**Price positioning:** low-to-mid on structure ("designed with affordability in mind"), **high on electronics** —
and the electronics are mandatory. Verified anchors: **Control Hub REV-31-1595 $375.00**; **Driver Hub REV-31-1596
$275.00**; **Expansion Hub REV-31-1153 $275.00** (**OUT OF STOCK** as of 2026-08-21); **Servo Hub REV-11-1855 $90.00**;
**HD Hex Motor REV-41-1291 $22.00**; **FTC Starter Kit V3.1 REV-45-3529 $695.00**; 15 mm extrusion category
**$6.00–$29.75**.

---

### 2.3 AndyMark — game elements, NeveRest motors, and the Robits imperial system

- **Category URLs loaded this session:** [/collections/first-tech-challenge](https://www.andymark.com/collections/first-tech-challenge) ·
  [/collections/robits](https://andymark.com/collections/robits) · [/pages/how-do-i-use-robits](https://andymark.com/pages/how-do-i-use-robits) ·
  [/ftc-2026-27](https://www.andymark.com/ftc-2026-27) · [/collections/first-tech-challenge-2026-2027](https://andymark.com/collections/first-tech-challenge-2026-2027)

**Known for:** **being the sole source of FTC field and game elements**, NeveRest gearmotors (in the R501 allowlist
**[C]**), FTC chassis kits, and the newer **Robits** build system.

**Structural system — Robits.** Imperial and distinctly FRC-flavoured: **"1 inch by 1 inch tube profile"** in
6061-T6 aluminium; **"Clearance holes for 10-32 screws are spaced every 0.5 inches"**; **"0.25 inch resolution of
gussets and spacers"**; **"a bushing hole every 1.5 inches"**; **3/8 hex shafts**, with 6 mm D referenced for NeveRest
motors ([verified](https://andymark.com/pages/how-do-i-use-robits)). Also listed: an **S3 Extrusion** line.

**Strengths [J]:** the 1×1 box tube is stiff and forgiving, 10-32 hardware is available at any hardware store, and
3/8 hex is a robust shaft for a drivetrain. If your mentors come from FRC, Robits will feel native.

**Gaps [J]:** imperial in a metric-dominant FTC world; 0.5 in hole pitch is coarse compared with goBILDA's 8 mm
(≈0.315 in), which costs you packaging density inside an 18-inch cube **[C] R102**; the FTC-facing motion catalogue is
thinner than goBILDA's.

**Where AndyMark is unavoidable (BIOBUZZ-specific, verified 2026-08-21):**

| AndyMark BIOBUZZ item | Price | Notes |
|---|---|---|
| FTC 2026-27 BIOBUZZ Full Game Set | **$599.00** | Pre-order. **"Orders received by 7-August-2026 will begin shipping after kickoff, beginning Monday, 14-September, 2026"** |
| Blue Partial Game Set | **$399.00** | |
| Red Partial Game Set | **$399.00** | |
| Field Perimeter `am-0481b` | UNVERIFIED price | **Not included** in game sets |
| Soft Tiles `am-2499` | UNVERIFIED price | **Not included** in game sets |
| Tape Set `am-5850_tape`, Tool Set `am-5850_tool`, Game Preview Pack `am-5851_preview`, Premium Set `am-3145a` | UNVERIFIED prices | Named on the same page |

> **"Returns are not accepted for this product. All sales are final."** (AndyMark BIOBUZZ pre-order page, verified).
> The scoring element itself is stated by FIRST as already shipping. **[H/verified]**

---

### 2.4 ServoCity / Actobotics — one live catalogue, one dead standard

- **Category URL loaded this session:** [servocity.com/structure/](https://www.servocity.com/structure/)

**Status.** ServoCity is alive and sells a structure catalogue whose category list is essentially identical to
goBILDA's (Channel, Grid Plates, Pattern Plates, Brackets, T-Slot Extrusion, Beams, Tubing, Clamping Mounts, Block
Mounts, Motor Mounts, Servo Mounts, Linear Actuator Mounts, Baseplates, Standoffs & Spacers, Hinges, Structure
Bundles — verified). It also sells the goBILDA 6 V Servo Power Injector under its own domain.

**Actobotics is discontinued.** gm0 states: **"As of June 2023, ServoCity is discontinuing the Actobotics line to
focus on goBILDA."** Actobotics was **imperial**, built on a **1.5 in C-channel**, a **1/4 in steel D-shaft**, and a
bolt circle that goBILDA's own adaptor names as **1.50 in** (see the `1206 Series Pattern Adaptor (16-4)` — "1.50"
Actobotics to 16mm goBILDA", verified). Actobotics **"can interface with other kits such as REV through a variety of
Pattern Adapters"** and is **"compatible with the 5mm hex used by REV with their adaptable hubs."**

**[J] Buying guidance:** treat ServoCity as *a second storefront for the goBILDA catalogue* (useful when goBILDA is
out of stock on a part — check both). **Do not start a new subsystem on Actobotics.** If the school already owns a
box of Actobotics channel, §3.7 lists the two adaptor part numbers that let you bolt it into a goBILDA robot; harvest
it, don't build on it.

---

### 2.5 Studica — legal parts, an unreachable website

**Studica appears four times in the final BIOBUZZ rules, so its parts are unambiguously legal:**

| Studica part | Where it is named | Rule |
|---|---|---|
| **Maverick 12V DC motor, `75001`** | Table 12-1 Motor allowances | R501 **[C]** |
| **Multi-Mode Smart Servo, `75002`** | Table 12-2 example servos | R502 **[C]** |
| **Linear Servo RC Actuator, `75014`** | Table 12-2 example linear servos | R502 **[C]** |
| **Servo Power Block, `75005`** | Table 12-3 Power Regulators and Limits | R505 **[C]** |
| Studica Servo Power Block (6 V) | R502 blue-box note: named among the regulators that "provide 6V to servos" | R502 **[C]** |

> **FETCH FAILURE, STATED PLAINLY: `studica.com` returned HTTP 403 Forbidden to every request I made this session**
> (`/first-tech-challenge`, `/studica-robotics`, `/blog/ftc-starter-bot-build-guide-2026-2027/`, and the site root).
> **I therefore have no verified Studica price, no verified stock status, and no verified structural-system
> documentation.** The part numbers above are **MANUAL-SKU** — read out of V0 manual tables, which is a stronger
> source than a vendor page anyway. Everything else about Studica in this file is UNVERIFIED. Someone with browser
> access should fill this in before kickoff.

**[J] What is known without the site:** Studica is one of the four official 2026-27 StarterBot partners (verified from
FIRST's own game-preview page), and it is the only vendor whose servo power regulator is named in Table 12-3 without
a stated per-port load limit in the extracted text (§3.9). For a small US team, Studica is a *component* supplier
(one legal motor, two legal servos, one legal servo power block), not a plausible primary ecosystem — you would be
betting the season on a catalogue you cannot browse.

---

### 2.6 The FIRST storefront (Pitsco) — the cheapest legal control system, with hard limits

**Source: `FIRST Tech Challenge Storefront — Kit and Price Options`, revision 25-26.4, dated Feb 18, 2026**, fetched
and text-extracted this session from `info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf`.
**[H] — this is the 2025-26 (DECODE) revision. A 26-27 revision is expected at or before kickoff. Prices below are
last season's published numbers and are the best available today.**

Access path (quoted): team Dashboard → *team options* → *Payment and Product* → *Order Products* → **"the Pitsco
Storefront."**

> **⚠️ Prices corrected 2026-08-22 — the table below was 2025-26 storefront pricing.** `research/SMALL-TEAM-ECONOMICS.md` §2 has the 2026-27 figures from *FIRST* Cost & Registration: registration **$350** (was $325), Driver Kit **$295** (was $285), Electronics/Control set **$350** (was $325), Build Kit **$660** (was $650). The 2026-27 prices below are the ones to budget from.

| Step | Item | Price (2026-27) | Limit | Contents as published |
|---|---|---|---|---|
| 1 | Season team registration | **$350** *(was $325 in 25-26)* | per team | Includes "Access to the FIRST storefront for discounted control system components and robot kit of parts" |
| 2 | **Driver Kit** | **$295** *(was $285)* | **"Limit one per register team per season"** | FTC Legal Gamepad (2), REV Driver Hub (1), FTC Legal Webcam |
| 3 | **Electronics Kit** (Electronics Modules and Sensors Kit V1.1) | **$350** *(was $325)* | **"Limit one per register team per season"** | REV Control Hub, Smart Robot Servo, Switch Cable and Bracket, Color Sensor V3 w/ cable, Touch Sensor w/ cable, Resistive Grounding Strap, FTC Control Hub Cable Pack, M3×16 screw pack and nylock nuts |
| 4 | **Build Kit** | **$660** *(was $650)* | **"Limit one per registered team per season"** | "REV FIRST Tech Challenge Competition Set V3.1" |
| 5 | Game Set (optional) | not stated | — | AndyMark game sets, full / half / soft tiles / perimeter |

> **THE SINGLE MOST IMPORTANT PROCUREMENT FACT IN THIS FILE, FOR THIS PROGRAM.** The Driver Kit and Electronics Kit
> are limited to **one per registered team per season** — and **you have two registered teams**. That is the
> mechanical reason the two-team structure pays for itself on the control system: **two registrations = two
> Electronics Kits + two Driver Kits at storefront prices.** **[D] on [H] prices**
>
> Arithmetic, at 25-26 prices: storefront Electronics + Driver = **$610 per team**. Buying the same core at REV
> retail = Control Hub **$375.00** + Driver Hub **$275.00** = **$650.00** *before* the servo, the two sensors, the
> cable pack, the grounding strap, the switch and the two gamepads. **Buy through the storefront. Both times.**
> **[D]**

**[J] Caveat:** the storefront PDF warns *"If you are waiting for a grant, please DO NOT check out until after that
grant has been awarded. FIRST will not be able to make changes to orders after checkout."* Sequence any grant money
before you place these two orders.

**FIRST Choice / Virtual Kit of Parts:** FIRST runs a Product Donation Voucher programme with a **Round 1 pre-kickoff**
and a **Round 2 launching at Kickoff** that "may be game specific." I could **not** load the FIRST Kit of Parts page
this session (`firstinspires.org/resources/library/ftc/kit-of-parts` returned HTTP 404). **Round dates, item lists and
voucher values for 26-27: UNVERIFIED.** Check the team Dashboard in the week of kickoff. **[H] on the programme's
existence, UNVERIFIED on this season's terms.**

**Vendor discounts listed on FIRST's own docs site.** `ftc-docs.firstinspires.org/sponsors/discounts/discounts.html`
(loaded this session) lists only **two** entries — *Team Grant Opportunities* and the *FIRST Storefront* ("All FIRST
Tech Challenge Teams are eligible for discounts on control equipment, electronics, and starter kits", limit "one
purchase per item per category each season", promo code "N/A"). **The goBILDA and REV discounts are NOT listed there
— they are run by the vendors directly** (§5.4). Do not conclude from that page that no vendor discounts exist. **[D]**

---

### 2.7 Component-only suppliers worth knowing

| Supplier | Why it matters | Rule basis |
|---|---|---|
| **Limelight Vision** | **The only** programmable vision coprocessor teams may reprogram. Table 12-9 lists exactly one device: **"Limelight Vision Limelight 3A — LL_3A"**. R702 explicitly names the **Limelight 3G** as *prohibited*. **Limelight 3A verified at $189.00** ([limelightvision.io](https://limelightvision.io/products/limelight-3a)) | R702, Table 12-9 **[C]** |
| **Digital Chicken Labs** | OctoQuad FTC Edition (8-channel encoder/PWM) — R702 Example 3 states it **"is allowed"** | R702 **[C]** |
| **SparkFun** | Optical Tracking Odometry Sensor — R702 Example 2 states **"This device is allowed"** (firmware updates OK, source modification not) | R702 **[C]** |
| **Adafruit** | BNO055 IMU — R702 Example 1: **"This device is allowed"** | R702 **[C]** |
| **DFRobot / Charmed Labs** | HuskyLens, Pixy2 — R702 Example 5: **"These devices are allowed"** (configurable, not programmable) | R702 **[C]** |
| **Hitec, FEETECH, DSSERVO, Axon, Actuonix** | Named as example legal servos in Table 12-2 | R502 **[C]** |
| **NFR Products, SWYFT Robotics, WATTOS, TETRIX (Pitsco), Modern Robotics/MATRIX** | Named in the Table 12-1 motor allowlist | R501 **[C]** |

---

## 3. THE INTEROPERABILITY MAP

This is the section to print and tape to the parts cabinet.

### 3.1 The four-and-a-half competing standards, side by side

| | **goBILDA** | **REV DUO** | **TETRIX (Pitsco)** | **AndyMark Robits** | **Actobotics (dead)** |
|---|---|---|---|---|---|
| Units | Metric | Metric | Metric channel, **Imperial fasteners** | **Imperial** | **Imperial** |
| Fastener | **M4** | **M3** | **SAE / Imperial bolts** | **10-32** | Imperial |
| Hole grid | **4 mm holes on an 8 mm grid** | Bracket **M3 holes on 8 mm pitch**; extrusion **slots** (infinite pitch); channel M3 @ 8 mm centre line | **16 mm bolt circle, on 16 mm spacing** | **10-32 clearance every 0.5 in**; gusset resolution 0.25 in | Fixed pitch, **1.50 in** bolt circle |
| Secondary/rotational pattern | **32 mm square** 4-hole pattern | **Motion Pattern: M3 circle on 16 mm dia.**; Extended: **32 mm dia.** | 16 mm bolt circle | 1.875 in bolt circle referenced for FRC wheels | 1.50 in |
| Bearing seat in structure | **14 mm hole** built into the grid | **9 mm bearing seat every 16 mm** in channel | n/a verified | **bushing hole every 1.5 in** | n/a verified |
| Primary channel | 48 mm U-Channel (1120); Low-Side (1121, 12 mm); Mini Low-Side (1143, 12×32 mm) | **15×45 mm C**, **45×45 mm U**; 15 mm & 15×30 mm extrusion | **32 mm C-channel** | **1 in × 1 in box tube** | **1.5 in C-channel** |
| Shaft | **8 mm REX**, **12 mm REX**, 6 mm D, round | **5 mm hex** (SUS303) | **6 mm or 4.7 mm round, set-screw drive** | **3/8 in hex**; 6 mm D for NeveRest | **1/4 in D** |
| Chain | **8 mm pitch** | **#25 roller (imperial)** | Imperial chain | Imperial | Imperial |
| Belt | GT2 2 mm, HTD 3 mm, HTD 5 mm | UNVERIFIED this session | UNVERIFIED | UNVERIFIED | UNVERIFIED |
| Status | Active, expanding | Active | Active but ageing | Active, newer | **Discontinued Jun 2023** |

Sources for every cell above are the vendor/gm0 pages listed in §9. Cells marked UNVERIFIED were not confirmed this
session and must not be treated as fact.

---

### 3.2 The single most important sentence in this file

> **The 8 mm hole *spacing* is shared. The hole *diameter* is not.**

goBILDA is **4 mm holes on an 8 mm grid**. REV DUO brackets are **M3 holes on an 8 mm pitch**. TETRIX is **16 mm
spacing** — an exact multiple of 8. So three systems' hole *patterns* line up geometrically. REV says so directly:
**"The REV DUO Plastic Brackets have mounting holes on an 8mm spacing which is compatible with other building
systems"** and **"Tetrix channels also use an 8mm hole spacing so almost all REV DUO brackets can mount directly to
the channel"** ([verified](https://docs.revrobotics.com/duo-build/building/compatibility)). gm0 says goBILDA **"is
able to interface with TETRIX channel because they share some holes."**

**[D] The consequence, which no vendor page states plainly:**

- An **M3 screw passes through a goBILDA 4 mm hole** — loosely, with ~0.5 mm of slop per side. It works, it is not
  precise, and it will not carry shear the way an M4 in a 4 mm hole does.
- An **M4 screw will NOT pass through a REV M3 hole.** Period. You must drill, and drilling a Delrin bracket to
  4 mm leaves very little material.
- Therefore **goBILDA↔REV interop is one-directional in practice: REV brackets bolt onto goBILDA structure more
  easily than goBILDA parts bolt onto REV structure.**
- And **matching hole spacing is not the same as matching mechanical standard.** You can bolt a REV bracket to a
  goBILDA channel and still have no way to get a REV 5 mm hex shaft through a goBILDA 14 mm bearing seat, or a
  goBILDA 8 mm chain onto a REV #25 sprocket. **Structure interop ≠ motion interop.** That distinction is where
  teams lose weekends.

---

### 3.3 Shaft standards — what actually turns what

| Shaft | Native to | Runs in round bearings? | Direct partners | Verified adapter path off-system |
|---|---|---|---|---|
| **8 mm REX** | goBILDA | **Yes** — "the six outer points of the hex are clipped to a common diameter so you can run the shafting in a round bore bearing" (verified) | goBILDA 8 mm REX bores across hubs/sprockets/pulleys/bearings/wheels; Yellow Jacket 5203/5204 output | goBILDA `Flanged Stainless Steel Shaft for REV Motion Pattern` (8 mm REX, 29 mm) **$7.99** — a REX shaft with a REV Motion Pattern flange |
| **12 mm REX** | goBILDA | Yes; "passes through 14mm goBILDA center holes" (verified) | goBILDA heavy-duty line, 1622 flange-mount bearings | none verified |
| **6 mm D** | goBILDA / NeveRest | n/a | goBILDA 6 mm D bores; AndyMark NeveRest output | gm0: goBILDA 6 mm D clamping hubs fit TETRIX shafts, **but** you then also need a goBILDA↔TETRIX pattern adaptor |
| **5 mm hex** | REV DUO | No | REV DUO everything; Actobotics via REV "adaptable hubs" (gm0) | REV **High Strength Hex Hub `REV-41-1147`** and **Universal Hex Hub `REV-41-1833`** — REV's own words: "specifically designed to help teams use the parts they already have with the reliability and convenience of a hex drive shaft" |
| **3/8 in hex** | AndyMark Robits | No | Robits gussets/bushings | goBILDA `Thru-Hole AndyMark Robits to Threaded goBILDA®` **$5.99** (pattern only, not shaft) |
| **1/4 in D** | Actobotics | n/a | Actobotics | via REV adaptable hubs (gm0) |
| **6 / 4.7 mm round, set screw** | TETRIX | n/a | TETRIX | gm0 warns set screws "are notorious for coming loose under load" |
| **MAXSpline** | **REV ION — FRC ONLY** | — | — | **None. Do not buy.** |

**[J] Reading of the table:** REX is the most forgiving shaft standard in FTC because it eats both hex-bore and
round-bore parts, which means a REX-based robot can absorb a mis-ordered bearing. 5 mm hex is the most *available*
because REV DUO is the FIRST Build Kit. Set-screw round shafts (TETRIX) are the ones that will fail at a competition
you drove three hours to.

---

### 3.4 Fasteners — the quiet incompatibility

| System | Fastener | Practical note **[J]** |
|---|---|---|
| goBILDA | **M4** (socket head, button head, low-profile, hex head, thread-locking, thread-forming; also M3 and M5 in catalogue) | 2.5 mm and 3 mm ball-end hex, 7 mm nut driver. Verified in the goBILDA Starter Kit tool list |
| REV DUO | **M3**, incl. **M3 hex-head screws slid along the extrusion slot** — REV: "Rather than using a T-nut, slide a M3 hex head screw along the slot" | 2.5 mm hex driver. Different driver from goBILDA's M4 |
| TETRIX | **SAE/Imperial** | A separate imperial driver set on the same robot |
| Robits | **10-32** | Available at any hardware store — a genuine advantage |

**[D] Mixing systems means mixing driver sizes at the pit table.** With two robots, a 15-student roster and an
inspection queue, "which hex key is this" is a real time cost, not a joke. One ecosystem ⇒ one driver set ⇒ one
spare-hardware bin ⇒ students can fix either robot.

---

### 3.5 Chain and belt — the hard wall

**This is the incompatibility with no adapter.**

- goBILDA runs **8 mm pitch chain**. gm0, plainly: goBILDA **"utilizes 8mm pitch chain, as opposed to the FTC
  standard #25 Imperial chain. This means that other kits' chain and sprockets won't work with goBILDA."**
- REV runs **#25 roller chain** (`REV-41-1365`) and calls it out **"because it's common to all systems."**
- TETRIX, Robits and Actobotics are all imperial chain.

**[D] Therefore:** goBILDA is the *only* major system whose chain is a closed island. If you standardise on goBILDA,
your chain, sprockets, and every spare master link are 8 mm and nothing else in the building fits. If you standardise
on REV/TETRIX/Robits, #25 is a commodity you can buy from three vendors and a bearing shop.

**[J] Is that a reason to reject goBILDA? No** — but it *is* a reason to buy your goBILDA chain and sprockets in
usable spare quantity up front (§6.4), because the failure mode "we broke a chain at 9 pm and there is no #25 in the
county that fits" is real and specific to this choice.

**Belts sidestep it.** GT2/HTD belts are commodity profiles from many suppliers, and goBILDA's own pattern makes
belt centre-to-centre distances land on the 8 mm grid. **[J] For a small team, belt-driven mechanisms are the lower-
risk choice over chain wherever the load allows** — quieter, no lubrication, no master link to lose, no stretch
re-tension between matches.

---

### 3.6 What bolts to what — the verdict matrix

Legend: **✅ direct** (bolts together as sold) · **🔩 adapter** (a named, purchasable adaptor exists) ·
**⚠️ trap** (looks compatible, isn't, or costs more than it saves) · **⛔ no** (no path)

| From ↓ / To → | goBILDA structure | REV DUO structure | TETRIX channel | Robits tube | Actobotics channel |
|---|---|---|---|---|---|
| **goBILDA structure** | ✅ | 🔩 `Thru-Hole REV to Threaded goBILDA` / `Threaded REV to Thru-Hole goBILDA` **$5.99 ea** | 🔩 `Thru-Hole Tetrix to Threaded goBILDA` / `Threaded Tetrix to Thru-Hole goBILDA` **$5.99 ea**; gm0: "share some holes" | 🔩 `Thru-Hole AndyMark Robits to Threaded goBILDA` **$5.99** | 🔩 `Thru-Hole Actobotics to Threaded goBILDA Pattern Adaptor` **$5.99**; `1206 Series Pattern Adaptor (16-4)` 1.50 in → 16 mm **$5.99** |
| **REV DUO brackets** | ⚠️ *M3 in a 4 mm hole — spacing matches, fit is sloppy* **[D]** | ✅ | ✅ REV: "almost all REV DUO brackets can mount directly to the channel" | ⛔ no verified path | ✅ REV: "will also work with Actobotics channel" |
| **goBILDA 8 mm chain / sprockets** | ✅ | ⛔ | ⛔ | ⛔ | ⛔ |
| **#25 chain** | ⛔ | ✅ | ✅ | ✅ | ✅ |
| **8 mm / 12 mm REX shaft** | ✅ (+ round-bore bearings) | 🔩 goBILDA `Flanged SS Shaft for REV Motion Pattern` **$7.99** | ⛔ | ⛔ | ⛔ |
| **5 mm hex shaft** | ⚠️ *needs a 5 mm hex-bore goBILDA hub; goBILDA lists 5 mm hex bores* | ✅ | 🔩 via REV `REV-41-1147` / `REV-41-1833` hubs | ⛔ | 🔩 gm0: "compatible with the 5mm hex used by REV with their adaptable hubs" |
| **REV ION / MAXSpline** | ⛔ | ⛔ **different REV system** | ⛔ | ⛔ | ⛔ |
| **VEX / Nexus wheels** | 🔩 goBILDA lists wheel adaptors for both (prices not shown) | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED |
| **LEGO axle** | 🔩 `3900 Series Bearing Adaptor for LEGO Axle` **$2.99/12 pk** | ⛔ | ⛔ | ⛔ | ⛔ |

---

### 3.7 The adapter catalogue you can actually buy

All rows below were read off [gobilda.com/pattern-adaptors](https://www.gobilda.com/pattern-adaptors/) this session.
goBILDA is, by a wide margin, the vendor that invests most in cross-system adaptors — which is itself an argument
for making goBILDA the *hub* of a mixed shop.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Thru-Hole REV → Threaded goBILDA adaptor | goBILDA | Pattern Adaptors — NEEDS-SKU-CHECK | 2 | 4 | $5.99 ea ≈ **$24** | Buy | **VERIFIED** (name+price on category page; SKU not shown) | Only buy if you are deliberately mixing |
| Threaded REV → Thru-Hole goBILDA adaptor | goBILDA | Pattern Adaptors — NEEDS-SKU-CHECK | 2 | 4 | $5.99 ea ≈ **$24** | Buy | **VERIFIED** | Opposite handedness of the above |
| Flanged SS Shaft for REV Motion Pattern (8 mm REX, 29 mm) | goBILDA | Pattern Adaptors — NEEDS-SKU-CHECK | 1 | 2 | $7.99 ea ≈ **$16** | Buy | **VERIFIED** | The one true REX↔REV motion bridge |
| Thru-Hole Actobotics → Threaded goBILDA adaptor | goBILDA | Pattern Adaptors — NEEDS-SKU-CHECK | as needed | as needed | $5.99 ea | Buy | **VERIFIED** | Only to harvest legacy stock |
| 1206 Series Pattern Adaptor (16-4), 1.50 in Actobotics → 16 mm goBILDA | goBILDA | **`1206` series** | as needed | as needed | $5.99 ea | Buy | **VERIFIED** (series number shown) | Also the proof that Actobotics is a 1.50 in pattern |
| Thru-Hole TETRIX → Threaded goBILDA / Threaded TETRIX → Thru-Hole goBILDA | goBILDA | Pattern Adaptors — NEEDS-SKU-CHECK | as needed | as needed | $5.99 ea | Buy | **VERIFIED** | For school-owned TETRIX stock |
| Thru-Hole AndyMark Robits → Threaded goBILDA | goBILDA | Pattern Adaptors — NEEDS-SKU-CHECK | as needed | as needed | $5.99 ea | Buy | **VERIFIED** | |
| High Strength Hex Hub | REV | **`REV-41-1147`** | as needed | as needed | UNVERIFIED | Buy | **VERIFIED** SKU (REV docs); price UNVERIFIED | Converts non-hex parts (incl. AndyMark Stealth Wheels) to 5 mm hex |
| Universal Hex Hub | REV | **`REV-41-1833`** | as needed | as needed | UNVERIFIED | Buy | **VERIFIED** SKU (REV docs); price UNVERIFIED | REV: "designed to help teams use the parts they already have" |
| 3900 Series Bearing Adaptor for LEGO Axle | goBILDA | **`3900` series** | 0 | 0 | $2.99 / 12 pk | Buy | **VERIFIED** | Listed for completeness; no competition use |

*All prices as of **August 2026** — **VERIFY BEFORE ORDER**.*

---

### 3.8 The traps, named

1. **REV ION is not REV DUO.** ION is FRC (MAXSpline, 2 in bolt circle). Ordering from `/ion/` for an FTC robot
   wastes money and a week. **[D]**
2. **"8 mm spacing is compatible" ≠ "M4 fits."** REV holes are M3. See §3.2. **[D]**
3. **goBILDA 8 mm chain has no adapter to anything.** Not one. §3.5.
4. **TETRIX set-screw hubs on round shafts.** gm0: they "are notorious for coming loose under load," and TETRIX
   channel "ha[s] a tendency to flex and bend under load." gm0 also calls TETRIX "the most expensive kit on average
   while providing the most limited build options." **[H]**
5. **Actobotics looks like a bargain on clearance.** It has been discontinued since June 2023; you are buying into a
   dead pattern with no restock path. **[H]**
6. **The REV Servo Power Module `REV-11-1144` is legal but DISCONTINUED.** It is named in Table 12-3 **[C]**, and
   REV's own page shows **"Discontinued"** at $48.88 (was $57.50), verified 2026-08-21. **Do not design around it.**
   Use the **REV Servo Hub `REV-11-1855` ($90.00, in stock, 6 channels)** or the **goBILDA 6 V Servo Power Injector
   `3125-0001-0001` ($69.99, in stock, 6 channels, 8–15 V in, 6 V out up to 24 A)**. **[D]**
7. **The 5 V vs 6 V servo trap, straight out of R502.** The manual's own note: *"The REV Control Hub and REV
   Expansion Hub provide 5V to servos, and the goBILDA Servo Power Injector, REV Servo Power Module, Studica Servo
   Power Block, and REV Servo Hub provide 6V to servos. While virtually all servos are compatible with 6V, servos
   with an operating voltage range of 6-8.4 DCV, for example, may not work properly when only provided 5V."*
   **[C]** — buy the servo and the power path together, or the servo will underperform and you will blame the code.
8. **Buying a "COTS mechanism" that does the game task.** R301: *"COTS MAJOR MECHANISMS purposefully designed to
   complete a game task are prohibited,"* with only two exceptions — **COTS drive CHASSIS**, and **COTS MAJOR
   MECHANISMS created as part of the official FIRST Tech Challenge StarterBots** **[C]**. A vendor "build to print"
   of a purpose-built solution is called out as *"against the spirit of this rule."* So: a bought chassis is fine,
   a bought "BIOBUZZ scorer" is not.
9. **Buying a multi-DoF COTS mechanism.** R303: COTS parts must be **single degree of freedom**, with a named allow
   list (linear slide kit, linear actuator kit, non-shifting gearbox, pulley, turntable, lead screw, single-DoF
   gripper) and named exceptions (ratchets, omni/mecanum wheels, dead-wheel odometry kits, U-joints/flex couplers,
   ball joints/rod ends) **[C]**. A COTS gripper with an added wrist is explicitly out.
10. **Anything pneumatic or suction.** R801 bans pneumatic actuators, pressure/vacuum generation and high-speed
    blowers; only manufacturer-sealed closed-air systems (gas shocks/springs, dampers) are allowed, plus air-filled
    COTS wheels **[C]**. Do not put a vacuum intake or a cylinder on any shopping list. Gas springs and constant-
    force springs remain available — goBILDA lists a **Shocks** category and a **Springs** category (verified).
11. **Relays, electromagnets and electrical solenoids are prohibited outright** (R506) **[C]**. This kills a
    surprising number of "clever latch" ideas at the parts-order stage.
12. **Ordering game elements late.** AndyMark's own pre-order page: **"Orders received by 7-August-2026 will begin
    shipping after kickoff, beginning Monday, 14-September, 2026"** and **"All sales are final."** That date has
    already passed as of today (2026-08-21). See §5.5.

---

### 3.9 Two documented gaps in my own source extraction — read the PDF before you rely on these

I am flagging these rather than papering over them.

| Gap | What the extracted text shows | What to do |
|---|---|---|
| **Table 12-2 servo stall-current limit** | The row extracts as `Servo   8 watts @6V  amps @6V   FEETECH ...` — **the numeric stall-current value is missing from the text layer.** The mechanical-output-power limit (**8 W @ 6 V**, via `Mechanical Output Power = 0.25 × Stall Torque(N-m) × No Load Speed(rad/s)`) *is* legible | Open the V0 PDF and read Table 12-2 visually, and use the FTC **online calculator** and **Inspection Quick Reference** that R502 points to. **Servos must meet BOTH requirements.** **[C]** |
| **Table 12-3 load limits** | The table misaligns in extraction: `REV Robotics Servo Hub REV-11-1855 — 2 Motors per Device` is almost certainly a column shift (the Servo Hub is a **6-channel servo** device per REV's own verified spec page), and **Studica Servo Power Block `75005` has no load limit shown at all** | Read Table 12-3 visually before finalising any servo-expansion plan. Do not quote my extraction to an inspector |

**[J] This matters commercially:** the servo rules are the ones that decide whether a $99.99 Axon or a $17.99 Proton
goes on the robot, and R503's **8 servo** ceiling makes each slot expensive.

---

## 4. The ecosystem commitment decision

### 4.1 Why a small team must pick one

**[J] The argument is about *variance*, not about which aluminium is better.** Both goBILDA and REV DUO can produce
a competitive FTC robot; thousands of teams prove that annually. What a 15-student, two-robot, low-mentor-hour
program cannot absorb is variance — the unplanned Saturday, the second order, the part that arrives and doesn't fit.

Five concrete costs of mixing, each traceable to something verified above:

| Cost of mixing | Mechanism | Evidence |
|---|---|---|
| **Two fastener systems** | M4 vs M3 vs 10-32; two driver sets; two spare-hardware bins; students can't cross-fix robots | §3.4 **[D]** |
| **Two shaft systems** | 8 mm REX vs 5 mm hex — every hub, bearing, sprocket, pulley and wheel bore is bought twice, in two standards | §3.3 **[D]** |
| **Two chain systems with no bridge** | 8 mm vs #25 — the one incompatibility with literally no adapter | §3.5, gm0 verified |
| **Two discount programs with different rules** | goBILDA 25% storewide, life of team; REV 15% on select items only, expiring 5/31/2027 | §5.4, both verified |
| **Doubled decision cost at 11 pm** | "Which bracket is this, and does it fit the other robot?" ×2 robots ×15 students | **[J]** |

**[D] The multiplier that makes this a first-class issue for *this* program:** every one of those costs is paid
**twice**, because you build **two robots**. A single-robot team pays a mixing tax; a two-robot team pays it twice
and also loses the biggest benefit of running two teams — **that the two robots share a BOM, a CAD library, a spares
bin and a repair procedure.** `ACHIEVABILITY-FACTORS.md` scores **duplicability** as a first-class factor; ecosystem
commitment is the highest-leverage single decision available for raising it, and it is free.

### 4.2 The recommendation

**[J] Standardise on goBILDA for structure and motion. Standardise on REV for control and power. Buy the control
system through the FIRST storefront, twice (once per registered team).**

The reasoning, ranked:

1. **The discount arithmetic is decisive on the mechanical spend.** 25% storewide, for the life of the team, on
   "nearly every product" (verified) vs 15% on a curated subset with an expiry (verified). On a $2,000 mechanical
   order that is roughly a **$200 delta** *plus* the fact that the goBILDA discount covers the *whole* order rather
   than the eligible slice. **[D]**
2. **The catalogue depth means fewer "we can't buy that" moments in October.** 26 motion categories, 16 structure
   categories, Viper-Slides in stock at verified prices, and the largest cross-vendor adaptor range in FTC (§3.7).
3. **The 14 mm bearing seat and the 32 mm pattern are built into the structure**, so bearings and pillow blocks
   drop into channel without fabricating a plate — which matters enormously with no mill. **[J]**
4. **REX tolerates mistakes.** A shaft that runs in *both* hex-bore and round-bore parts (verified quote, §2.1)
   forgives an ordering error at 10 pm.
5. **The 2026-27 goBILDA FTC Starter Kit is in stock today at a verified $899.99 / $674.99 with the FIRST team
   discount**, against a stated retail value "over $1,600" — while the 2025-26 kit shows **Discontinued/Sold Out**
   (both verified). Availability *now* is worth more than a marginal spec advantage in November.

### 4.3 The deliberate exception (this is not "mixing")

**Electrical is REV, always.** R701 leaves no other option **[C]**. Buying a REV Control Hub, REV Driver Hub, REV
sensors and REV cabling while building goBILDA structure is not a mixed ecosystem — it is the *only* legal
configuration, and the two ecosystems meet at exactly one interface: **mounting the hub**, which is four screws
through a plate. Budget one goBILDA plate or one 3D-printed hub tray per robot and the interface is closed.

**[J] The other sanctioned exception:** vision/odometry coprocessors (Limelight 3A, OctoQuad, SparkFun OTOS,
Adafruit BNO055) are single-vendor components with USB/I²C interfaces. They are not an ecosystem, they are a
peripheral, and R702 tells you exactly which ones are legal **[C]**.

### 4.4 When REV DUO is the better call

Commit to REV DUO instead if **two or more** of these are true for your program:

- **A mentor is already fluent in extrusion** and will be present most build nights. Extrusion's learning curve is
  real (gm0 says so) and it is the difference between "adjustable" and "everything is slightly loose."
- **The design you pick on kickoff day is tension-critical** — long chain runs, belt-driven lifts, anything where
  you expect to move a pulley 3 mm and re-test. The slot beats the grid here, decisively.
- **You need #25 chain compatibility** because the school owns a bin of it, or because you want a commodity chain
  supply rather than a goBILDA-only one (§3.5).
- **The FIRST Build Kit is your main mechanical purchase.** The Build Kit *is* the REV Competition Set V3.1
  (verified from the storefront PDF **[H]**) at $650 per team, limit one per team. If you buy two Build Kits, you
  have already bought a large REV DUO inventory and standardising on goBILDA means owning two systems anyway.
  **[D] — this is the strongest single argument for REV, and it is a budget argument, not an engineering one.**
- **Weight or packaging is tight.** gm0: "extrusion allows teams to save space as opposed to channel, and is
  lighter than aluminum channel." Note that R104 states **there is no ROBOT weight limit in BIOBUZZ** **[C]**, so
  the weight half of that argument is *worth much less this season than usual* — but the packaging half still
  matters inside the R102 18-inch cube **[C]**.

**[J] The honest tiebreaker:** if you are going to buy two FIRST Build Kits at $650 each anyway, buy them, build
Kit-first, and treat goBILDA as the *supplement* for the parts REV doesn't do well (Viper-Slides, GripForce wheels,
REX drivetrain). That is a defensible *hub-and-spoke* strategy. What is **not** defensible is deciding per-mechanism,
per-week, based on whatever is in stock. **Pick the hub before kickoff, in writing, and hold it.**

### 4.5 The commitment, written down

**[J] Draft this as a one-line team standard before September 12 and pin it in the shop:**

> *"Structure and motion: goBILDA, M4, 8 mm grid, 8 mm REX shaft, 8 mm chain, HTD 5 belt. Control and power: REV,
> through the FIRST storefront. Off-standard parts require a named adapter part number on the BOM before ordering.
> Both robots use the same BOM."*

That last sentence is the duplicability guarantee. Any deviation has to be argued for, not defaulted into.

---

## 5. Procurement reality

### 5.1 Lead time and shipping — what is verified and what is not

| Question | Status |
|---|---|
| goBILDA order processing / cutoff / carrier | **UNVERIFIED** — `gobilda.com/shipping-returns/` and `/shipping-and-returns/` both returned HTTP 404 this session |
| goBILDA international shipping | **VERIFIED**: FTC team accounts get **"a $50 Flat Rate"** on non-US orders, "no matter the size or quantity" ([/ftc/](https://www.gobilda.com/ftc/)) |
| goBILDA discount activation time | **VERIFIED**: "Most discounts are activated within the day of account activation or the next business day" |
| REV shipping policy | **UNVERIFIED** — `revrobotics.com/shipping/` returned HTTP 404. REV product pages *do* show per-item status strings such as **"In Stock & Ready To Ship!"**, **"Out of Stock"**, **"Discontinued"** — use those |
| AndyMark game-set ship date | **VERIFIED**: "Orders received by 7-August-2026 will begin shipping after kickoff, beginning **Monday, 14-September, 2026**" |
| AndyMark returns | **VERIFIED**: "Returns are not accepted for this product. All sales are final." |
| Studica anything | **UNVERIFIED — site returns HTTP 403** |

**[J] Plan against 1–2 weeks door-to-door for a normal in-stock order from a US FTC vendor, and 3–6 weeks for
anything backordered in September–October.** That is a planning assumption, not a verified vendor SLA — treat it as
**[J]** and confirm at order time.

### 5.2 The September–October demand spike is real, and I can show it to you today

I did not have to search for anecdotes. **On 2026-08-21 — three weeks *before* kickoff and before the spike properly
starts — the following were already unavailable, read directly off vendor pages:**

| Item | Vendor | Status verified 2026-08-21 | Why it matters |
|---|---|---|---|
| **Expansion Hub `REV-31-1153`** | REV | **Out of Stock** ($275.00) | This is a **rule-named** device: R701(B) and R701(C) **[C]**. If you planned a second hub for motor/servo port count, it is not available right now |
| **Servo Power Module `REV-11-1144`** | REV | **Discontinued** ($48.88, was $57.50) | Named in Table 12-3 **[C]**. Legal, unbuyable |
| **Axon MINI Servo MK2 `2004-0025-0001`** | goBILDA | **OUT OF STOCK** ($99.99) | Premium servo, common lift/arm choice |
| **M4 Socket Head Screw Assortment `3201-0004-0001`** | goBILDA | **out of stock** ($54.99, 600 pc) | *Fasteners* go out of stock. This is the least glamorous and most disabling stock-out there is |
| **32 mm Omni Wheel `3624-4008-0032`** | goBILDA | **OUT OF STOCK** ($14.99) | Small omnis are odometry-pod staples |
| **FTC Starter Kit 2025-26 `3200-4008-2526`** | goBILDA | **Discontinued / Sold Out** ($849.99) | Last season's kit is simply gone |
| **Matrix 12V 3000mAh NiMH `14-0014`** | goBILDA | **Discontinued** ($49.99) | A **battery** — an R601 item **[C]** — discontinued; successor is `3100-0012-0020` at $64.99 |

**[D] Six stock-outs and three discontinuations in a single afternoon of casual browsing, three weeks before
kickoff, is the evidence.** After September 12, when ~7,000 teams read the same manual and reach the same
conclusions about the same mechanisms, the popular items — slides, specific gear ratios, omni wheels, servo
horns, chain — go first.

**[J] And it is worse for you than for a one-robot team**, in three compounding ways:
1. You order **double quantity**, so you hit "only 6 left" limits that a single-robot team never notices.
2. If a part goes out of stock after you have built robot A, **robot B is now a different robot** — which destroys
   the shared-BOM advantage that justified running two teams.
3. A partial shipment leaves **one robot done and one blocked**, which is the worst possible state for morale on a
   B-team of newer students.

**[J] The rule that follows: for any part where the two robots must match, order BOTH robots' quantity in a SINGLE
order, plus one spare.** Never "order A now, B later."

### 5.3 Backorder discipline

**[J] Recommended policy, calibrated to this program:**

- **Never let a backorder hold a shipment.** If a vendor offers ship-complete vs ship-partial, choose **partial**
  and let the missing line follow. A blocked box helps nobody.
- **Treat "Out of Stock" as "not in the design"** during the kickoff-week decision. Design around what has a green
  status string *today*. This is the cheapest de-risking move available on kickoff day.
- **Second-source the commodity lines.** ServoCity carries a catalogue that mirrors goBILDA's (§2.4) — check both
  domains before declaring a part unavailable.
- **Keep a written "if X is out, we use Y" line for the five highest-risk parts** (slides, drive motors, drive
  wheels, servos, chain). Write it before kickoff; the substitution decision is much worse under time pressure.

### 5.4 Discounts and vouchers — verified

| Programme | Amount | Scope | Duration / expiry | How to get it | Confidence |
|---|---|---|---|---|---|
| **goBILDA FIRST team discount** | **25%** | **"nearly every product storewide"**; "a few exclusions apply" (exclusions not enumerated on the page) | **"active for the life of the team"** | Create a team account → complete application form → email confirmation; **"activated within the day of account activation or the next business day"** | **VERIFIED** ([gobilda.com/ftc](https://www.gobilda.com/ftc/)) |
| **goBILDA international shipping** | **$50 flat rate** | non-US addresses, any size/quantity | with FTC team account | same application | **VERIFIED** |
| **REV FTC team discount** | **15%** | **"select items"** only — products in REV's discount category | **"Discount codes expire May 31, 2027"**; 2026-27 programme is **active** | Code appears on the **FIRST Dashboard**, or complete REV's Team Registration Form | **VERIFIED** ([revrobotics.com/ftc/discounts](https://www.revrobotics.com/ftc/discounts/)) |
| **FIRST Storefront (Pitsco)** | Negotiated prices, not a % | "control equipment, electronics, and starter kits" | Current season; **"one purchase per item per category each season"** | Team Dashboard → Payment and Product → Order Products | **VERIFIED** (ftc-docs) + prices **[H]** from storefront PDF rev 25-26.4 |
| **FIRST Team Grants** | "Varies by grant" | — | "See each individual grant opportunity" | firstinspires.org grants list | **VERIFIED** that the programme exists; amounts UNVERIFIED |
| **FIRST Choice / Virtual Kit of Parts (Product Donation Vouchers)** | Vouchers, value unstated | Round 1 pre-kickoff; **Round 2 launches at Kickoff** and "may be game specific" | UNVERIFIED for 26-27 | Team Dashboard | **[H]** programme exists; **26-27 dates/items UNVERIFIED** (FIRST Kit of Parts page 404'd) |
| AndyMark team discount | — | — | — | — | **UNVERIFIED** — no discount statement found on AndyMark's FIRST page |
| Studica team discount | — | — | — | — | **UNVERIFIED** — site 403 |

**[D] Action, this week, both teams:** register both teams' goBILDA accounts and both REV discount codes **before**
kickoff. goBILDA activation is next-business-day; REV's code lives on the Dashboard. Discovering on September 13
that your 25% isn't active costs a day and ~$200 on a $800 order.

### 5.5 The BIOBUZZ procurement calendar (verified dates only)

| Date | Event | Source | Status |
|---|---|---|---|
| **2026-05-02, 6:00 p.m. ET** | AndyMark game-set **pre-orders opened** | FIRST game-preview page | **passed** |
| **2026-05-04** | Studica StarterBot Base released | FIRST game-preview page | **passed** |
| **2026-08-07** | **AndyMark cutoff:** "Orders received by 7-August-2026 will begin shipping after kickoff" | AndyMark BIOBUZZ page | **PASSED — 14 days ago** |
| **2026-08-21** | *Today.* Vendor stock already thinning (§5.2) | this session | — |
| **2026-09-12** | **KICKOFF.** Full Competition Manual, full StarterBot designs released. FIRST: "full StarterBot designs will not be released until Kickoff" | FIRST game-preview page | 22 days out |
| **2026-09-14** | AndyMark game sets **begin shipping** | AndyMark BIOBUZZ page | |
| **2026-09-28, 12:00 p.m. ET** | **Game Q&A opens** | workspace ground truth | |
| Every Thursday, Kickoff → 2 wks before Championship | **Team Updates** post; additions highlighted yellow, deletions struck through | workspace ground truth | Watch for R501 additions — R501's own note says *"Additional motors may be added to the legal motor list in future competition manual updates"* **[C]** |
| **2027-05-31** | REV FTC discount codes expire | REV discounts page | |

> **⚠️ ACTION FLAG:** the **August 7 AndyMark cutoff has already passed.** If the program has not ordered a game set
> or field elements, **check the AndyMark BIOBUZZ page for current ship estimates before assuming a September 14
> delivery** — and note that **"All sales are final"** on that pre-order. For a two-team program, a **full game set
> ($599) plus perimeter and tiles** is the practice-field question; **[J]** two partial sets ($399 each = $798) is
> usually the wrong buy for one shop, but may be right if the two teams practise at different sites.

### 5.6 The two-robot ordering protocol

**[J] Six rules. They are cheap and they prevent the specific failures this program is exposed to.**

1. **One BOM, two quantities.** Every line carries *qty/robot* and *qty×2*. The tables in §6 are formatted that way
   on purpose — keep that format for the kickoff BOMs.
2. **Order both robots at once, always**, plus **+1 spare** on anything that can break in a match (§5.2).
3. **One cart, one buyer, one card.** Split orders across parents/mentors is how you end up with two slightly
   different robots and no receipt trail.
4. **Buy the FIRST storefront kits per team immediately** (limit one each per registered team — that limit is the
   whole reason two registrations are financially efficient, §2.6).
5. **Anything on the critical path gets ordered in the first 48 hours after kickoff**, before the spike peaks —
   even at the cost of ordering slightly wrong. A wrong $60 motor beats a right motor that arrives in November.
6. **Keep a live stock-status column in the BOM.** Copy the vendor's own string ("In Stock & Ready To Ship!",
   "Out of Stock", "Discontinued") and the date you read it.

---

## 6. The starter standing order — parts to own before kickoff, for TWO robots

**Scope rule:** everything below is **game-agnostic**. These are parts that get used every season regardless of what
the field looks like, so buying them before September 12 is not a gamble — it is removing them from the critical path.

**Reading the tables:** *Approx cost* is the extended cost **for two robots at list price**, before the 25% goBILDA /
15% REV discounts and before tax and shipping. **Every price is as of August 2026 and is VERIFY-BEFORE-ORDER.**
**🕐 = long lead / high stock-out risk — order first.**

### 6.1 Control system and power — buy through the FIRST storefront

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Electronics Kit** (Control Hub + servo + Color V3 + Touch + cables + grounding strap + switch) | **FIRST storefront (Pitsco)** | "Electronics Modules and Sensors Kit V1.1" | 1 | **2** | **$350 ea = $700** *(25-26: $325/$650)* | Buy | **VERIFIED** page/price; 2026-27 pricing | 🕐 **Limit one per registered team.** Cheapest legal Control Hub path. R701(A) **[C]** |
| **Driver Kit** (2 gamepads + REV Driver Hub + FTC-legal webcam) | **FIRST storefront (Pitsco)** | "Driver Kit" | 1 | **2** | **$295 ea = $590** *(25-26: $285/$570)* | Buy | **VERIFIED**; 2026-27 pricing | 🕐 **Limit one per registered team.** R901 requires an approved Android DRIVER STATION **[C]** |
| Control Hub (retail fallback) | REV | **`REV-31-1595`** | — | — | **$375.00 ea** | Buy | **VERIFIED** | Only if storefront limit is exhausted. R701(A) **[C]** |
| Driver Hub (retail fallback) | REV | **`REV-31-1596`** | — | — | **$275.00 ea**, "In Stock & Ready To Ship!" | Buy | **VERIFIED** | |
| Expansion Hub (2nd hub, optional) | REV | **`REV-31-1153`** | 0–1 | 0–2 | **$275.00 ea — OUT OF STOCK 2026-08-21** | Buy | **VERIFIED** | 🕐 R701(C): "no more than one additional REV Expansion Hub" **[C]**. **Design so you do not need it** |
| **12 V NiMH main battery** | REV | **`REV-31-1302`** 12V Slim, 3000 mAh, XT30, inline 20 A ATM fuse, 16 AWG | 2 | **5** (2/robot + 1 pool spare) | **$60.00 ea = $300** | Buy | **VERIFIED** name/SKU/price; **chemistry NOT stated on the product page — NEEDS-VERIFY** | 🕐 R601: exactly **1** approved **12 V NiMH** main battery on the robot; fuse may be replaced with a COTS 20 A ATM mini blade **[C]**. **Confirm NiMH before ordering** |
| 12 V NiMH battery (alternate) | goBILDA | **`3100-0012-0020`** NiMH 3000 mAh, XT30 | — | — | **$64.99 ea** | Buy | **VERIFIED** (chemistry explicitly NiMH) | Second source. Successor to the discontinued Matrix `14-0014` |
| Battery charger | REV or goBILDA | NEEDS-SKU-CHECK — [goBILDA /batteries/](https://www.gobilda.com/batteries/) lists a *Battery Chargers* category | 1 | **2** | UNVERIFIED | Buy | **FAMILY-ONLY** | One charger per team so both pits are independent |
| **Servo Hub (servo expansion / 6 V)** | REV | **`REV-11-1855`**, 6 ch, 7–15 V in, 5–7.4 V out (6 V default), 15 A | 0–1 | 0–2 | **$90.00 ea**, "In Stock & Ready To Ship!" | Buy | **VERIFIED** | Named in Table 12-3 **[C]**. Provides **6 V** to servos per R502 note **[C]** |
| Servo Power Injector (alternate) | goBILDA | **`3125-0001-0001`**, 6 ch, 8–15 V in, 6 V out to 24 A | 0–1 | 0–2 | **$69.99 ea**, In Stock | Buy | **VERIFIED** | Named in Table 12-3 **[C]** |
| ~~Servo Power Module~~ | ~~REV~~ | ~~`REV-11-1144`~~ | — | — | ~~$48.88~~ | — | **VERIFIED: DISCONTINUED** | Legal per Table 12-3 **[C]** but unbuyable. Do not design around |
| Vision coprocessor (optional) | Limelight Vision | **Limelight 3A** (`LL_3A` in Table 12-9) | 0–1 | 0–2 | **$189.00 ea** | Buy | **VERIFIED** price; SKU from Table 12-9 **[C]** | 🕐 The **only** reprogrammable vision coprocessor allowed (R702) **[C]**. **Limelight 3G is explicitly prohibited** |
| USB webcam (2nd, for the other robot / spares) | any | FTC-legal webcam — one comes in each Driver Kit | 1 | 2 | UNVERIFIED | Buy | **FAMILY-ONLY** | R707/R708: USB is for vision **[C]** |

### 6.2 Motors and servos — and the R503 budget

> **R503 [C]: "ROBOTS are limited to a total of 8 motors and 8 servos ... for all MECHANISMS used in all
> configurations."** If the robot has multiple configurations at one event, **the sum across all of them** must
> fit. **[H] DECODE allowed 10 servos — this is a reduction, and prior-season designs may now be illegal.**
> **[C] Carve-out worth money:** vibration/autofocus motors inside COTS computing devices, and **motors integral to
> a COTS sensor (e.g. LIDAR, scanning sonar), provided the device is not modified except to facilitate mounting**,
> **"do not count toward the limit in R503."** A scanning LIDAR is therefore a *free* motor. **[C]**

**The R501 legal-motor allowlist, by vendor (MANUAL-SKU, from Table 12-1 [C]).** This list is **closed** — "The only
allowed motor actuators are" — unlike the servo list, which is open ("including, but not limited to").

| Motor | Vendor | Part numbers in Table 12-1 | Note in Table 12-1 |
|---|---|---|---|
| NeveRest 12V DC | AndyMark | `am-3104`, `am-3104b` | |
| NeveRest Hex 12V DC | AndyMark | `am-3104c` | |
| **Yellow Jacket 520x Series 12V DC** | **goBILDA** | `5201-0002-0026`, etc. | **"5201, 5202, 5203, and 5204 series"** |
| 5000 Series 12V DC | goBILDA | `5000-0002-4008`, etc. | |
| Modern Robotics / MATRIX 12V DC | MR/MATRIX | `5000-0002-0001` | **Discontinued** |
| Yuksel 12V DC | NFR Products | `NFR-600-100-000` | |
| **HD Hex 12V DC** | **REV** | `REV-41-1291` | |
| **Core Hex 12V DC** | **REV** | `REV-41-1300` | |
| Maverick 12V DC | Studica | `75001` | |
| SWYFT Spike Motor | SWYFT Robotics | `SR-MOTOR-DC-01` | |
| TETRIX MAX 12V DC | TETRIX | `739530`, `39530` | **Discontinued** |
| TETRIX MAX TorqueNADO 12V DC | TETRIX | `W44260` | |
| Stingray 12V DC | WATTOS | `WDM12` | |

> **[C] Also from Table 12-1:** *"Many legal gearmotors are sold with labeling based on the entire assembly. These
> motors may be used with or without the provided gearbox, and/or with any other compatible gearbox."* — you may
> legally re-gear a Yellow Jacket or an HD Hex. That is a real cost saver: buy one motor, change the ratio.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Drive motors** | goBILDA | **Yellow Jacket `5203` series** (8 mm REX out, 24 mm) — ratio TBD at kickoff | 4 | **8** | **$54.99 ea = $439.92** | Buy | **VERIFIED** family+price | 🕐 Ratio is game-dependent — **[J]** buy 4 now in a mid ratio for the practice chassis, 4 more after kickoff |
| Mechanism motors | goBILDA | **Yellow Jacket `5204`** (80 mm, 8 mm REX) or `5203` | 2–4 | **4–8** | $54.99–$56.99 ea | Buy | **VERIFIED** | Counts against the R503 **8-motor** ceiling **[C]** |
| Motor (low cost / spare) | REV | **`REV-41-1291`** HD Hex, no gearbox, 12 V, 6000 rpm free, 0.105 N·m stall, 28 cpr | 0 | **1–2 spare** | **$22.00 ea** | Buy | **VERIFIED** | Cheapest legal motor found this session. Legal per Table 12-1 **[C]** |
| **Workhorse servos** | goBILDA | **Dual Mode `2000-0025-0002`** (Torque) / **`-0003`** (Speed) / **`-0004`** (Super Speed) | 4 | **8** | **$36.99 ea = $295.92** | Buy | **VERIFIED** | `2000-0025-0003` is named in Table 12-2 **[C]**. Counts against R503 **8-servo** ceiling |
| Budget servos | goBILDA | **Proton `2002-0180-0002` / `-0003`** | as needed | as needed | **$17.99 ea** | Buy | **VERIFIED** | **[J]** Half the price — use for low-load jobs and prototypes. Confirm against Table 12-2's 8 W/stall-current spec **[C]** |
| Multi-turn servo | goBILDA | **5-Turn Dual Mode `2000-0025-0502/-0503/-0504`** | 0–1 | 0–2 | **$49.99 ea** | Buy | **VERIFIED** | For winch/rotate jobs that would otherwise burn a motor slot |
| Premium servo | goBILDA | **Axon MAX MK2 `2004-0025-0002`** | 0–1 | 0–2 | **$99.99 ea** | Buy | **VERIFIED** | "Axon MAX+" is named in Table 12-2 **[C]** — confirm the MK2 variant meets the spec |
| ~~Axon MINI MK2~~ | goBILDA | `2004-0025-0001` | — | — | ~~$99.99~~ | — | **VERIFIED: OUT OF STOCK** 2026-08-21 | Example of the spike (§5.2) |
| **Spare motor** | goBILDA | same SKU as drive motors | — | **+1** | ~**$55** | Buy | **VERIFIED** family | 🕐 **[J] Non-negotiable.** A dead drive motor between matches ends a two-robot day |
| **Spare servos** | goBILDA | same SKU as workhorse servos | — | **+2** | ~**$74** | Buy | **VERIFIED** family | **[J]** Servos are the most-replaced actuator in FTC |
| Servo programmer | goBILDA | included in the FTC Starter Kit; else Servo Electronics category — NEEDS-SKU-CHECK | 1 | 1 (shared) | UNVERIFIED | Buy | **FAMILY-ONLY** | R504(C) **[C]**: servos "may be modified as specified by the manufacturer (e.g., setting soft limits or modification for continuous rotation)" |

**[D] Motor/servo budget worksheet — carry this on every kickoff BOM:**

| Subsystem | Motors | Servos |
|---|---|---|
| Drivetrain | 4 | 0 |
| Intake | 1 | 0–1 |
| Lift / extension | 1–2 | 0 |
| Manipulator / wrist / gripper | 0 | 2–3 |
| Endgame mechanism | 0–1 | 0–2 |
| **Available (R503) [C]** | **8** | **8** |
| **Typical committed** | **6–8** | **2–6** |

**[J] The binding constraint is almost always motors, not servos.** A 4-motor drivetrain spends half the budget
before any scoring mechanism exists. Two levers exist: (a) a **6-motor drivetrain is a false economy** in an 8-motor
world; (b) a **5-turn servo can replace a motor** on light winch/rotate duty for $49.99 and a free motor slot.
And remember the **COTS-sensor-motor carve-out** above — a scanning sensor's motor is free **[C]**.

### 6.3 Structure — the always-used stock

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **FTC Starter Kit (2026-2027 Season)** | goBILDA | **`3200-4008-2627`** — In Stock | 1 | **2** | **$899.99 ea list; $674.99 ea with FIRST discount = $1,349.98** | Buy | **VERIFIED** | 🕐 **The single highest-value line in this document.** Stated retail value "over $1,600" per kit. Contains 3× YJ 19.2:1 + 1× YJ 50.9:1, 4× 2000-series servos, battery+charger+mount, channel, grid plates, 7 GripForce Gecko 48 mm, 2× 96 mm omni, 5× Hogback traction, chain, 600+ M4 screws, 20 flanged bearings, 8 mm REX shafts, hubs, hex keys. **Buying two = both robots start identical** |
| U-Channel, long | goBILDA | **`1120` Series U-Channel** (48 mm) — [category](https://www.gobilda.com/channel/); **bundle `3203-1120-0001`** (17 pc) **$219.99** | 4–6 pcs | **8–12 pcs** | $4.99–$50.99 by length ≈ **$150–$300**, or **$219.99** as the bundle | Buy | **VERIFIED** family+range; **bundle SKU/price/stock VERIFIED 2026-08-22** | 27 length variants, 1-hole/48 mm → 49-hole/1200 mm. R302 permits cutting legal COTS and raw stock **[C]**. **[J] Prefer the bundle for duplicability, keep 2–3 long pieces for one-offs — see §6.10.2** |
| Low-Side U-Channel | goBILDA | **`1121` Series** (12 mm sides) — bundle **`3203-1121-0001`** (17 pc) **$199.99** | 2–4 pcs | **4–8 pcs** | **$199.99** as bundle | Buy | **VERIFIED** SKU+price+stock 2026-08-22 (§6.10) | Lighter/lower profile for superstructure |
| Mini Low-Side U-Channel | goBILDA | **`1143` Series** (12 mm × 32 mm) — bundle **`3203-1143-0001`** (17 pc) **$184.99** | 2 pcs | **4 pcs** | **$184.99** as bundle | Buy | **VERIFIED** SKU+price+stock 2026-08-22 (§6.10) | For arms and light linkages |
| Grid plates / pattern plates | goBILDA | [Grid Plates](https://www.gobilda.com/structure/), Pattern Plates | 2–4 | **4–8** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | The mounting surface for hubs and coprocessors |
| Brackets, assorted | goBILDA | Brackets / Mounts / Clamping Mounts | 20+ | **40+** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **[J]** You will always want more 90° brackets than you planned |
| Standoffs & spacers | goBILDA | **`3203-1501-0001`** Standoffs Bundle (148 pc) **$139.99** · **`3203-1502-0001`** Spacers Bundle (80 pc) **$46.99** — see §6.10 | assorted | **1 of each, shared** | **$186.98** | Buy | **VERIFIED** SKU+price+stock 2026-08-22 | **Corrected 2026-08-22.** An earlier revision listed "`1504`/`1505` 32 mm OD Pattern Spacers" tagged VERIFIED on the strength of *search-result titles only* — which does not meet this file's own §0.2 contract. `/standoffs-spacers/` confirms the categories (M4 Standoffs, Spacers, Offset Standoffs, M4 Shoulder-Standoffs, Pattern Spacers, Shaft Spacers & Shims) but **shows no series numbers; treat `1504`/`1505` as UNVERIFIED.** The bundle SKUs above are read off a loaded page |
| Polycarbonate sheet | any / REV | REV lists polycarbonate sheets on [/ftc/](https://www.revrobotics.com/ftc/) | 1 sheet | **2 sheets** | UNVERIFIED | **Fab** | **FAMILY-ONLY** | R302 **[C]**: sheet stock is explicitly a legal raw material. Cuts with hand tools. Guards, hoppers, deflectors |
| 3D printer filament (PLA+/PETG/TPU) | any | — | 2–3 kg | **4–6 kg** | UNVERIFIED | **Fab** | **UNVERIFIED** | 🕐 **[J] The single biggest fabrication lever you have without a mill.** Print in duplicate; a second identical part costs filament and time only |
| Hub mounting plate for Control Hub | — | — | 1 | 2 | — | **Fab** (3D print or cut polycarb) | **[J]** | The *only* mechanical interface between the REV electrical ecosystem and the goBILDA structural one (§4.3) |
| **ROBOT SIGNS** | — | FIRST template, US Letter / A4 | **2** | **4** | ~$0 | **Fab** | **[C]** | 🕐 **R401: minimum two ROBOT SIGNS per ROBOT, in at least 2 separate locations, on opposite or adjacent surfaces.** R402: each sign must contain a rectangle with a solid red/blue field. **Inspection item — make 4 of these in August, not on the morning of the event** |

### 6.4 Motion — shaft, bearings, hubs, chain, belts, wheels

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **8 mm REX shafting** | goBILDA | **Stainless Steel REX Shafting, 8 mm w/ E-Clip** (24–624 mm) | 6–10 pcs | **12–20 pcs** | $3.69–$17.99 ea ≈ **$120–$220** | Buy | **VERIFIED** family + price range; **NEEDS-SKU-CHECK** per length | 🕐 Runs in round-bore bearings (§3.3). Buy a spread of lengths |
| 12 mm REX shafting | goBILDA | **Stainless Steel REX Shafting, 12 mm w/ E-Clip** | 0–2 pcs | **0–4 pcs** | $3.99–$19.99 ea | Buy | **VERIFIED** family+range | For high-load pivots; passes through 14 mm goBILDA centre holes |
| **Flanged ball bearings** | goBILDA | **`1601` Series Flanged** (4–32 mm ID) / **`1611` Series** (8 mm REX ID) | 20 | **40** | $3.99–$11.99 / 2-pk ≈ **$90–$150** | Buy | **VERIFIED** series+prices | 🕐 **[J] Buy far more than you think.** Bearings vanish. The Starter Kit includes 20 flanged bearings per kit |
| Pillow blocks | goBILDA | **`1602`** (1-side/2-post) $7.99–$14.99 · **`1605`** (1-side/1-post) $5.99–$6.99 · **`1606`** (2-side/1-post) $6.99–$7.99 · **`1621`** flat $7.99–$9.99/2-pk | 6–10 | **12–20** | ≈ **$100–$180** | Buy | **VERIFIED** series+prices | REX and round bores available. The reason you don't need a mill |
| Hubs (clamping / set-screw / sonic) | goBILDA | [Hubs](https://www.gobilda.com/hubs/): Classic Clamping, Set-Screw, Hyper `1310`/`1313`/`1315`, Sonic, Servo (H25T 25-tooth) | 8–12 | **16–24** | NEEDS-SKU-CHECK | Buy | **VERIFIED** families; bores incl. **8 mm/12 mm REX, 5 mm/3-8"/1-2" hex, 6 mm D, 14 mm, 32 mm** | **[J] Clamping > set-screw** every time (see the TETRIX set-screw failure mode, §3.8) |
| **8 mm chain (steel)** | goBILDA | **`3308-0008-1000`** | 1 | **2 + 1 spare** | **$11.99 ea ≈ $36** | Buy | **VERIFIED** | 🕐 **No cross-system substitute exists** (§3.5). Buy the spare |
| 8 mm chain (plastic) | goBILDA | **`3309-0108-0050`** | 1 | **2** | **$7.99 ea = $16** | Buy | **VERIFIED** | Lighter, quieter, lower load |
| Sprockets, hub-mount plastic | goBILDA | **`3311-0014-0016/-0020/-0024/-0042`** (14 mm bore, 16/20/24/42 T) | 4–8 | **8–16** | $2.29–$4.79 ea ≈ **$30–$60** | Buy | **VERIFIED** SKUs+prices | Cheapest ratio experiments in the catalogue |
| Sprockets, clamping | goBILDA | **`3302-4008-0014`** (8 mm REX, 14 T) **$12.99** · **`3302-4012-0014`** (12 mm REX, 14 T) **$12.99** | 2–4 | **4–8** | ≈ **$52–$104** | Buy | **VERIFIED** | |
| Sprockets, aluminium hub-mount | goBILDA | **`3310-0032-0028`** 28 T **$9.99** · **`3310-0032-0070`** 70 T **$18.99** | as needed | as needed | — | Buy | **VERIFIED** | 32 mm bore = the 32 mm pattern |
| Pinion / idler sprockets | goBILDA | **`3312-4008-0008`** 8 T press-fit 8 mm REX **$4.99/2-pk** · **`3312-0006-0008`** idler 6 mm bore **$4.99/2-pk** | 2 | **4** | ≈ **$20** | Buy | **VERIFIED** | |
| Chain tensioner | goBILDA | **`1524-0001-0001`** Arc-Slot Tensioner Bracket | 2 | **4** | **$5.99 ea = $24** | Buy | **VERIFIED** | 🕐 **[J] The part teams wish they'd bought.** Fixed-pitch systems need these; extrusion doesn't |
| **Timing belt + pulley starter pack** | goBILDA | **5 mm Pitch HTD Starter Pack (8 mm REX Bore)** **$209.99** · alt: **2 mm GT2 Starter Pack** **$239.99** | 1 (shared) | **1–2** | **$210–$480** | Buy | **VERIFIED** names+prices; **NEEDS-SKU-CHECK** | **[J]** Expensive up front, but belts beat chain for a low-maintenance small team (§3.5). One pack can serve both robots |
| Viper-Slide kit (2-stage 336 mm) | goBILDA | **`3210-0003-0002`** — 2 Stage Viper-Slide Kit (336 mm) | 0–1 | **0–2** | **$159.99 ea** | Buy | **VERIFIED** SKU+price+stock (2026-08-22: **In Stock**) | 🕐 **Historically the highest stock-out-risk item in FTC [J]** — but *in stock today*. Legal as a COTS **single-DoF "linear slide kit"** under R303(A) **[C]**. **[J] Hold until kickoff unless budget allows a speculative pair** |
| Viper-Slide kit (4-stage 336 mm) | goBILDA | **`3210-0003-0004`** — 4 Stage Viper-Slide Kit (336 mm) | 0–1 | 0–2 | **$229.99 ea** | Buy | **VERIFIED** SKU+price+stock (**In Stock**) | 4-stage 240 mm is **`3210-0004-0004`** at **$219.99**, also In Stock |
| Linear Actuator Kit (203 mm stroke) | goBILDA | **`3212-0001-0001`** | 0–1 | 0–2 | **$129.99 ea** | Buy | **VERIFIED** SKU+price+stock (**In Stock**) | **[C]** R303(B) names "linear actuator kit" as an allowed single-DoF COTS mechanism. A cheaper, lower-travel alternative to a slide stack |
| Viper-Slide spares | goBILDA | Individual steel slides **240 mm $16.99 / 336 mm $19.99**; End-Stops **$5.99/6-pk**; Pulley Brackets **$8.99/4-pk** | — | as needed | — | Buy | **VERIFIED** | Bent slides are a routine repair |
| **Omni wheels** | goBILDA | **`3624-0014-0096`** 96 mm **$21.99** · **`3624-0014-0072`** 72 mm **$19.99** · **`3624-4008-0048`** 48 mm **$16.99** | 2–4 | **4–8** | ≈ **$70–$180** | Buy | **VERIFIED** SKUs+prices | **`3624-4008-0032` (32 mm) is OUT OF STOCK** — the classic odometry-pod wheel. R303(I) explicitly allows holonomic wheels as a COTS exception **[C]** |
| Mecanum wheel set | goBILDA | **`3213-3606-0002`** 96 mm set **$169.99** · **`3625-0202-0104`** GripForce Ø104 mm 40A **$189.99** · **`3213-3606-0003`** 140 mm **$299.99** | 0–1 set | **0–2 sets** | **$340–$600** | Buy | **VERIFIED** SKUs+prices | 🕐 **[J] Defer until kickoff.** Mecanum vs tank is a game-dependent call, and this is a $340+ line ×2 robots |
| Traction / intake wheels | goBILDA | GripForce Gecko™, Hogback Traction, Rhino, Intake Wheels — [category](https://www.gobilda.com/wheels-tires/) | as needed | as needed | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | The Starter Kit already ships 7 Gecko 48 mm + 5 Hogback per kit |
| Collars, couplers, shims, shaft spacers | goBILDA | Collars / Couplers / Shaft Spacers & Shims | assorted | assorted | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **[J]** Buy an assortment; these are the parts that stop a build at 10 pm |
| Springs / gas shocks | goBILDA | [Springs](https://www.gobilda.com/hardware/), [Shocks](https://www.gobilda.com/motion/) | as needed | as needed | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **R801 [C]:** sealed manufacturer-charged closed-air systems (gas shocks) are the **only** legal stored-air device. Constant-force and coil springs are unrestricted |

### 6.5 Fasteners and hardware — the stock-out that stops everything

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **M4 Hardware Starter Pack (2,625 pc)** | goBILDA | **`3201-0010-0001`** | — | **1 shared** | **$139.99** | Buy | **VERIFIED** | 🕐 **[J] Buy this in August.** It is the single best hardware value found this session and fasteners *do* stock out (below) |
| M4 Button Head Screw Assortment (600 pc) | goBILDA | **`3201-0004-0002`** | — | **1–2** | **$54.99 ea** | Buy | **VERIFIED** | |
| ~~M4 Socket Head Screw Assortment (600 pc)~~ | goBILDA | `3201-0004-0001` | — | — | ~~$54.99~~ | — | **VERIFIED: out of stock 2026-08-21** | 🕐 **Proof that fasteners go first.** §5.2 |
| M5 Set-Screw Bundle (75 pc) | goBILDA | **`3203-2806-0001`** | — | **1** | **$14.99** | Buy | **VERIFIED** | |
| Nylock nuts, M4 | goBILDA | Nuts category | 200+ | **400+** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | Starter Kit includes ~200 locknuts per kit |
| Washers, M4 | goBILDA | Washers category | assorted | assorted | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | |
| Thread locker | goBILDA | Thread Locker category | 1 | **1–2** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **[J]** Blue, not red. Vibration loosens everything over a season |
| Hex keys — 2.5 mm & 3 mm ball-end, 7 mm nut driver | goBILDA | Tools category | 1 set | **2 sets + 1 pit spare** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | Sizes verified from the Starter Kit tool list. **[J] One set per robot bin, one in the pit kit** |

### 6.6 Wire, connectors and electrical consumables

R609 requires appropriately sized insulated wire; R610 requires **specified wire colours for the 12 V main power
bus and the +5 V auxiliary bus** **[C]** — read those two rules before buying spools, since colour is an
**inspection** item, not a preference.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **20 A ATM mini blade fuses** | any auto-parts / goBILDA | goBILDA **Fuses** category | 2 | **4–6** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🕐 **R601(A) [C]:** the battery fuse "may be replaced with a COTS equivalent in-line **20A ATM mini blade fuse**." Cheap, tiny, and it will blow at an event |
| XT30 connectors (pairs) | goBILDA | **Wiring → XT30** category | 4 | **8** | NEEDS-SKU-CHECK | Buy | **VERIFIED** category | R601(B) **[C]** permits replacing battery connectors with "Anderson Powerpole, XT30, or any connector with a comparable power rating" |
| Anderson Powerpole connectors | goBILDA | **Wiring → Anderson Powerpole** category | as needed | as needed | NEEDS-SKU-CHECK | Buy | **VERIFIED** category | Explicitly named in R601(B) **[C]** |
| Servo extension cables (TJC8) | goBILDA | **Wiring → TJC8 Servo** category | 8 | **16** | NEEDS-SKU-CHECK | Buy | **VERIFIED** category | One per servo, plus spares |
| Motor/encoder cables | REV | Control Hub cable pack (in the FIRST Electronics Kit) | 1 set | **2 sets** | included | Buy | **VERIFIED** **[H]** | |
| Heat shrink tubing | goBILDA | **`3201-0005-0001`** | — | **1** | **$9.99** | Buy | **VERIFIED** | R504(E) **[C]**: "insulation may be applied to electrical terminals" |
| Zip ties (100 pk) | goBILDA | **`2909-0101-0100`** | 1 | **2** | **$4.99 ea = $10** | Buy | **VERIFIED** | |
| Cinch-Straps hook & loop (4 pk) | goBILDA | **`2909-0102-0250`** | 2 | **4** | **$3.99 ea = $16** | Buy | **VERIFIED** | **[J]** Best battery retention method there is |
| Grommets (plastic 12-pk / rubber 14 mm 4-pk) | goBILDA | **`2911-0014-0001`** $3.99 · **`2911-0014-0003`** $3.99 | 1 | **2** | ≈ **$16** | Buy | **VERIFIED** | Wire through a 14 mm centre hole without chafing |
| Servo connector clips (6 pk) | goBILDA | **`2917-0001-0001`** | 1 | **2** | **$5.99 ea = $12** | Buy | **VERIFIED** | 🕐 **[J] Stops the #1 cause of "the servo just stopped working."** |
| Braided cable sleeve (3 m) | goBILDA | **`2925-0008-3000`** | 1 | **2** | **$5.99 ea = $12** | Buy | **VERIFIED** | R606 **[C]**: the electrical system must be **inspectable** — tidy wiring is a rules requirement, not vanity |
| Cable-carrier chain (1 m) | goBILDA | **`2924-1015-1000`** | 0–1 | **0–2** | **$19.99 ea** | Buy | **VERIFIED** | For wiring across an extending slide |
| Resistive grounding strap | REV | included in the FIRST Electronics Kit | 1 | **2** | included | Buy | **VERIFIED** **[H]** | Inspection item |

### 6.7 What you FABRICATE, not buy

With 3D printers and hand tools and no CNC mill, this is the honest fab list. R302 is your authority: *"Allowed raw
materials and legal COTS parts can be modified (drilled, cut, painted, etc.)"*, with raw materials explicitly
including **sheet stock, extruded shapes, metals, plastic, rubber, wood, and magnets** **[C]**.

| Fabricated item | Method | Per robot | For 2 robots | Confidence | Notes |
|---|---|---|---|---|---|
| **ROBOT SIGNS** | Print FIRST template + mount on plate | 2 | **4** | **[C]** R401/R402 | 🕐 Make these in August |
| Control Hub / Driver Hub mounting tray | 3D print or cut polycarb | 1 | 2 | **[J]** | The goBILDA↔REV interface (§4.3) |
| Intake rollers / compliant wheels | 3D print (TPU) | as needed | ×2 | **[J]** | The classic print-in-duplicate win |
| Gripper fingers / jaws | 3D print | as needed | ×2 | **[J]** | **R303 [C]**: a *bought* multi-DoF gripper is illegal; a *fabricated* one is fine |
| Sensor and camera brackets | 3D print | 3–6 | 6–12 | **[J]** | |
| Guards, hoppers, deflectors | Cut polycarbonate | 1–3 | 2–6 | **[C]** R302 sheet stock | Hand tools only; R201 **[C]** requires the robot not damage the ARENA or make a mess |
| Spacers and standoffs (odd lengths) | 3D print or cut tube | as needed | ×2 | **[J]** | Cheaper than the catalogue for one-offs |
| Battery mount / retention | 3D print + Cinch-Strap | 1 | 2 | **[J]** | |
| Cable management clips | 3D print | many | many | **[J]** | Supports R606 inspectability **[C]** |
| **A duplicate print queue** | — | — | — | **[J]** | 🕐 **The two-robot discipline: every print job runs qty 2, immediately.** A part printed once is a part robot B doesn't have |

### 6.8 Long-lead / order-first list

**[J] If the budget only clears in stages, order in this sequence:**

1. 🕐 **Two FIRST storefront Electronics Kits + two Driver Kits** — limit-one-per-team, and the control system is on
   the critical path for *everything* including programming practice. **≈$1,220 [H]**
2. 🕐 **Two goBILDA FTC Starter Kits `3200-4008-2627`** — in stock today, discontinued-and-sold-out is what happened
   to last season's. **≈$1,350 with team discount**
   - 🕐 **CHECK THE SHELF FIRST:** for each **2025-2026** Starter Kit the program already owns, the **Upgrade Pack
     `3200-0101-2627` at $249.99** brings it to 2026-27 spec instead of buying a second full kit — **[D] ~$650 saved
     per kit owned** (§6.10). Verified In Stock 2026-08-22. This is the highest-leverage single check in this list
3. 🕐 **M4 Hardware Starter Pack `3201-0010-0001`** ($139.99) + bearings + spare fasteners — fasteners and bearings
   are already stocking out (§5.2)
4. 🕐 **Batteries and 20 A ATM fuses** — R601 items **[C]**; 5 batteries across two robots
5. 🕐 **Spare motor ×1, spare servos ×2**
6. 🕐 **Filament, 4–6 kg** — your only real fabrication capacity
7. 🕐 **Chain, chain tensioners, shaft stock, hubs** — the 8 mm chain island has no substitute (§3.5)
8. 🕐 **AndyMark field/game elements** — the Aug 7 cutoff has passed; check current ship dates (§5.5)
9. Defer to kickoff: **Viper-Slides, mecanum wheels, final drive ratios, mechanism-specific motors** — all
   game-dependent, all expensive, all ×2

### 6.9 Budget rollup (list price, before discounts, before tax/shipping)

| Block | For TWO robots | Basis |
|---|---|---|
| FIRST storefront: 2× Electronics Kit + 2× Driver Kit | **$1,290** | $350+$295 per team, 2026-27 *FIRST* Cost & Registration *(was $1,220 at 25-26 prices)* |
| 2× goBILDA FTC Starter Kit `3200-4008-2627` (list) | **$1,799.98** | $899.99 ea, VERIFIED |
| ⤷ *same, with the 25% FIRST team discount* | ***$1,349.98*** | *$674.99 ea, stated on the product page, VERIFIED* |
| Batteries (5) + fuses | **≈$300–$330** | $60.00 / $64.99 ea, VERIFIED |
| Fasteners (M4 starter pack + button-head assortment) | **≈$195** | $139.99 + $54.99, VERIFIED |
| Bearings, pillow blocks, hubs, collars | **≈$250–$400** | VERIFIED price ranges, quantities **[J]** |
| Shaft stock (8 mm/12 mm REX) | **≈$150–$250** | VERIFIED ranges |
| Chain, sprockets, tensioners | **≈$150–$250** | VERIFIED SKUs |
| Wire, connectors, consumables | **≈$120–$200** | VERIFIED SKUs + FAMILY-ONLY |
| Spare motor + 2 spare servos | **≈$130** | VERIFIED |
| Filament 4–6 kg | **≈$100–$180** | UNVERIFIED |
| **Pre-kickoff subtotal (with goBILDA discount applied)** | **≈$3,965–$4,510** | **[D]** |
| *Optional now / likely at kickoff:* belt starter pack | +$210–$480 | VERIFIED |
| *Optional now / likely at kickoff:* 2× Viper-Slide kits | +$320–$460 | VERIFIED |
| *Optional now / likely at kickoff:* 2× mecanum sets | +$340–$600 | VERIFIED |
| *Optional:* AndyMark full game set | +$599 | VERIFIED |
| *Optional:* 2× Limelight 3A | +$378 | VERIFIED |
| *Excluded above:* 2× team registration | +$650 | $325 ea **[H]** |

**[J] Read of the rollup:** roughly **$4.0–4.5k of pre-kickoff parts** puts two complete, identical, legal,
practice-capable robots on the floor before the game is known — and about **65% of that is two kits and two
storefront bundles**, i.e. four purchase decisions. That is the shape a low-mentor-hour program wants: few
decisions, high coverage, everything duplicated.

### 6.10 The bundle-and-kit shortcut — full goBILDA FTC Kits category, verified 2026-08-22

**Added in the 2026-08-22 verification pass.** The entire `/ftc-kits` category was loaded and read in one page,
which resolves a number of rows that earlier revisions of this file could only mark NEEDS-SKU-CHECK. **Every row
below is VERIFIED: part number, price and stock status read off the category listing this session.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **FTC Starter Kit (2026-2027)** | goBILDA | **`3200-4008-2627`** | 1 | **2** | **$899.99** ea list / **$674.99** discounted | Buy | **VERIFIED** — In Stock | The anchor purchase (§6.3) |
| 🕐 **FTC Starter Kit Upgrade Pack (2025-26 → 2026-27)** | goBILDA | **`3200-0101-2627`** | — | **1 per kit already owned** | **$249.99** | Buy | **VERIFIED** — In Stock | 🕐 **THE MONEY-SAVER THIS FILE PREVIOUSLY MISSED.** "If your team is rocking the 2025-2026 goBILDA FTC Starter Kit ... this upgrade pack will provide you with all the contents necessary to bring your existing kit up to the current standard." **[D] $249.99 vs $899.99 = ~$650 saved per kit already owned.** Contains polycarb grid plates, U-channels, spacers, shafts, GripForce Gecko + Hogback wheels, a ServoBlock, Dual Block Mount, zip ties. **Check the shelf before buying a second full kit** |
| **8 mm REX Shaft Starter Pack** | goBILDA | **`3201-0008-0001`** | — | **1 shared** | **$199.99** | Buy | **VERIFIED** — In Stock | Resolves the §6.4 "buy a spread of lengths" row with one SKU instead of 12–20 per-length decisions |
| **goBILDA Servo Starter Pack** | goBILDA | **`3201-0007-0001`** | — | **1 shared** | **$309.99** | Buy | **VERIFIED** — In Stock | Cross-check contents against the R502 allowlist and the R503 8-servo cap before assuming every servo in it is usable (§6.2) |
| Intake Wheel Starter Pack (8 mm REX bore) | goBILDA | **`3201-0014-0001`** | 0–1 | **0–2** | **$159.99** | Buy | **VERIFIED** — In Stock | **[J] Defer to kickoff** — intake geometry is the most game-dependent choice on the robot |
| **1120 Series U-Channel Bundle (17 pcs)** | goBILDA | **`3203-1120-0001`** | — | **1 shared** | **$219.99** | Buy | **VERIFIED** — In Stock | 🕐 Resolves the §6.3 NEEDS-SKU-CHECK channel row. 17 pcs covers the 8–12 pcs two robots need, with spares |
| 1121 Series Low-Side U-Channel Bundle (17 pcs) | goBILDA | **`3203-1121-0001`** | — | **1 shared** | **$199.99** | Buy | **VERIFIED** — In Stock | Resolves the §6.3 `1121` row |
| 1143 Series Mini Low-Side U-Channel Bundle (17 pcs) | goBILDA | **`3203-1143-0001`** | — | **0–1 shared** | **$184.99** | Buy | **VERIFIED** — In Stock | Resolves the §6.3 `1143` row |
| 1109 Series goRAIL Bundle (15 pcs) | goBILDA | **`3203-1109-0001`** | — | **0–1** | **$119.99** | Buy | **VERIFIED** — In Stock | Lighter open-rail structure; not previously covered in this file |
| **1501 Series Standoffs Bundle (148 pcs)** | goBILDA | **`3203-1501-0001`** | — | **1 shared** | **$139.99** | Buy | **VERIFIED** — In Stock | Resolves the §6.3 standoffs row. **NOTE:** the verified *bundle* series are **1501** (standoffs) and **1502** (spacers). An earlier revision cited "`1504`/`1505` 32 mm OD Pattern Spacers" from search-result titles; **I could not confirm 1504/1505 on `/standoffs-spacers/` this session — treat those two series numbers as UNVERIFIED** |
| 1502 Series Spacers Bundle (80 pcs) | goBILDA | **`3203-1502-0001`** | — | **1 shared** | **$46.99** | Buy | **VERIFIED** — In Stock | Cheapest bundle in the category |
| Strafer Chassis Kit (104 mm GripForce mecanum) | goBILDA | **`3209-0001-0007`** | 0–1 | **0–2** | **$699.99** ea | Buy | **VERIFIED** — In Stock | See the legality note below |
| BeeLine Chassis Kit V2 | goBILDA | **`3209-0002-0002`** | 0–1 | **0–2** | **$649.99** ea | Buy | **VERIFIED** — In Stock | See the legality note below |
| ~~M4 Socket Head Screw Assortment (600 pc)~~ | goBILDA | `3201-0004-0001` | — | — | ~~$54.99~~ | — | **VERIFIED: still OUT OF STOCK on 2026-08-22** | 🕐 **Out of stock on two consecutive days of checking, still three weeks pre-kickoff.** The §5.2 argument is not a one-day artefact |

#### 6.10.1 A COTS drive chassis is explicitly legal — and that matters most to *this* program

**[C] R301 prohibits "COTS MAJOR MECHANISMS purposefully designed to complete a game task," but lists as its first
allowed exception: "A. COTS drive CHASSIS, provided none of the individual parts violate any other rules."**
Grepped verbatim from `12_RobotConstruction_R_p64-88.txt`.

**[J] The implication for a two-robot, no-mill, low-mentor-hour program is larger than for anyone else.** The
drivetrain is the one mechanism that is (a) required on both robots, (b) unglamorous, (c) tolerance-sensitive, and
(d) *not* where the season is won. Buying it twice converts the hardest-to-duplicate fabrication job into a
purchase order, and guarantees the A and B robots actually drive identically — which is the whole premise of a
shared BOM. Against that: **$1,300–$1,400 for two chassis kits is a large fraction of the §6.9 budget**, and R301's
exception is for a *drive chassis* only — bolting a game-task mechanism onto a COTS kit does not inherit its
legality.

**[J] Recommendation: price two chassis kits as a genuine option at kickoff, not before.** Drive geometry
(mecanum vs tank vs holonomic) is game-dependent, and §5.2's rule still applies — if you buy, buy both in one
order. Note the Strafer kit ships **104 mm GripForce mecanum wheels**, which R303(I) explicitly permits as a
holonomic-wheel exception to the single-DoF rule **[C]**.

#### 6.10.2 Bundle vs cut-to-length — the actual trade

**[D]** The §6.3 guidance was "buy long and cut," which R302 permits **[C]**. The bundles change that arithmetic:
`3203-1120-0001` delivers 17 pre-cut 1120 channels for **$219.99**, against a per-piece range of **$4.99–$50.99**.

**[J] For this program, prefer the bundle.** Pre-cut channel arrives with square ends and clean, on-pattern holes —
which is precisely what a team without a mill cannot reliably reproduce with a hacksaw, and precisely what makes
robot B match robot A. Keep two or three long channels for genuine one-offs and cut those. The bundle is the
duplicability purchase; the long stock is the prototyping purchase.

---

## 7. Rule cross-reference for buyers

Grep any of these in `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` before ordering.

| Rule | Buying consequence | Line |
|---|---|---|
| **R102*** | 18 in × 18 in × 18 in STARTING CONFIGURATION cube — packaging density drives channel/extrusion choice | 169 |
| **R104*** | **No weight limit in BIOBUZZ** — removes the usual "buy the lighter system" argument | 197 |
| **R105** | Expansion limits exist but the numbers are **game-dependent → DEFERRED TO KICKOFF.** Do not buy slide length against a guess | 211 |
| **R201*** | Robot must not damage the ARENA or make a mess — affects wheel/intake material choice | 220 |
| **R204*** | No downforce-generating floor-grabbing or airflow suction | 295 |
| **R301*** | COTS MAJOR MECHANISMS purpose-built for a game task are **prohibited**; **COTS drive CHASSIS** and **official StarterBot mechanisms** are the only exceptions | 301 |
| **R302*** | Legal COTS parts and raw materials **may be modified** — sheet stock, extruded shapes, metals, plastic, rubber, wood, magnets | ~316 |
| **R303*** | COTS parts must be **single DoF**; allow-list includes linear slide kits, linear actuator kits, non-shifting gearboxes, pulleys, turntables, lead screws, single-DoF grippers; exceptions include omni/mecanum wheels and dead-wheel odometry kits | 328 |
| **R304*** | **Pre-Kickoff FABRICATED ITEMS and designs are permitted** — legal basis for building a practice chassis in August | 381 |
| **R401/R402*** | ≥2 ROBOT SIGNS per robot, on opposite or adjacent surfaces, with a solid red/blue rectangle | 399/421 |
| **R501*** | **Closed** motor allowlist (Table 12-1). COTS-sensor motors and device vibration motors **do not count** toward R503 | 484 |
| **R502*** | **Open, spec-based** servo list (Table 12-2): **8 W @ 6 V** mechanical output power **and** a stall-current limit. **5 V vs 6 V regulator note** | 534 |
| **R503*** | **8 motors + 8 servos total, across all MECHANISMS in all configurations.** ⇐ the hardest constraint on any multi-mechanism BOM | 591 |
| **R504/R505*** | No actuator modification except the listed exceptions; **Table 12-3** lists the only legal power regulating devices and their per-port limits | 599 |
| **R506*** | **Relays, electromagnets and electrical solenoids prohibited** | 2949 (layout) |
| **R601*** | Exactly **1** approved **12 V NiMH** main battery; COTS 20 A ATM mini blade fuse and Powerpole/XT30 connector swaps allowed | 650 |
| **R602*** | Other batteries only for self-contained peripherals and LEDs (COTS USB packs) | 682 |
| **R603*** | Exactly one main power switch | 701 |
| **R607*** | Custom circuits must not provide regulated power above 5 V unless powering LEDs only | 782 |
| **R609/R610*** | Appropriately sized wire; **specified wire colours** for the 12 V main and +5 V aux buses | 817/852 |
| **R701*** | **REV Control Hub (REV-31-1595)** or **Android phone + REV Expansion Hub (REV-31-1153)**; optionally **one** additional Expansion Hub | 911 |
| **R702*** | Coprocessor software may not be altered; **Table 12-9 lists exactly one** programmable vision coprocessor: **Limelight 3A (LL_3A)**. Limelight 3G, OpenMV Cam, Luxonis OAK-1 **prohibited** | 932 |
| **R704*** | **FTC Dashboard, FTControl Panels and similar third-party streaming tools are prohibited** on the ROBOT CONTROLLER network; no continuous video stream; laptops off the network during MATCH play | 980 |
| **R707/R708*** | USB is for vision — only webcams/optical vision sensors and R702-allowed vision coprocessors | 1065 |
| **R801*** | **No pneumatics, no compressors, no vacuum, no blowers.** Only manufacturer-sealed closed-air (gas shocks/springs, dampers) and air-filled COTS wheels | 1119 |
| **R901*** | One approved Android DRIVER STATION device on the OPERATOR CONSOLE | 1148 |

---

## 8. Open questions — the NEEDS-SKU-CHECK / UNVERIFIED register

Work this list down before kickoff. Each line is something I could **not** verify this session.

| # | Question | Blocked by | Owner action |
|---|---|---|---|
| 1 | **Is `REV-31-1302` NiMH?** R601 requires NiMH **[C]**; REV's product page does not state chemistry | Vendor page silent | Confirm with REV, or buy goBILDA `3100-0012-0020` which states NiMH explicitly ($64.99) |
| 2 | **Table 12-2 stall-current number** | PDF text-layer gap (§3.9) | Read the V0 PDF table visually; use the FTC online servo calculator + Inspection Quick Reference |
| 3 | **Table 12-3 per-device load limits**, esp. Servo Hub row and the missing Studica `75005` limit | PDF column misalignment (§3.9) | Read the V0 PDF table visually before finalising servo expansion |
| 4 | **Studica prices, stock, structural system** | `studica.com` HTTP 403 on all paths | Browse manually; Studica is an official StarterBot partner and its parts are rule-legal |
| 5 | **goBILDA shipping policy, processing time, carrier** | `/shipping-returns/` and `/shipping-and-returns/` both 404 | Check at checkout or contact goBILDA |
| 6 | **REV shipping policy** | `/shipping/` 404 | Rely on per-product status strings |
| 7 | **FIRST Choice / Virtual Kit of Parts 26-27 rounds, dates, items, voucher values** | `firstinspires.org/resources/library/ftc/kit-of-parts` 404 | Check the team Dashboard at kickoff |
| 8 | **26-27 FIRST storefront revision** — prices and kit contents may change from rev 25-26.4 | Not yet published | Re-read the storefront PDF at kickoff before ordering |
| 9 | **AndyMark team discount** — exists? | No statement on `andymark.com/pages/first` | Ask AndyMark directly |
| 10 | **AndyMark BIOBUZZ ship dates now that the Aug 7 cutoff has passed** | Page states the cutoff, not the post-cutoff behaviour | Check `andymark.com/ftc-2026-27` before ordering; sales are final |
| 11 | **Prices for `REV-41-1147` / `REV-41-1833` hex hubs** | SKUs verified from REV docs; product pages not loaded | Load the product pages if mixing systems |
| 12 | Per-length SKUs for goBILDA **brackets, grid plates, hubs, traction wheels** | Category pages verified; individual SKUs not | Build the kickoff BOM off live product pages, not off this file. **[PARTIALLY CLOSED 2026-08-22:** channel, standoffs, spacers, REX shafting and the slide/actuator kits now have VERIFIED *bundle* SKUs — see §6.10**]** |
| 17 | **`1504` / `1505` "32 mm OD Pattern Spacers" series numbers** | Previously tagged VERIFIED on search-result titles alone; `/standoffs-spacers/` shows categories but **no series numbers** | **Downgraded to UNVERIFIED 2026-08-22.** Use the verified bundles `3203-1501-0001` / `3203-1502-0001` instead (§6.3, §6.10) |
| 18 | Contents of **Servo Starter Pack `3201-0007-0001`** vs the R502 allowlist | Price/stock verified; itemised contents not read | Confirm every servo in the pack is R502-legal, and that the build still fits the R503 **8-servo** cap, before relying on it |
| 19 | Whether the program already owns a **2025-2026 goBILDA Starter Kit** | Local inventory question, not a vendor one | Physically check the shelf — it decides a **~$650 per kit** purchase (§6.8, §6.10) |
| 13 | goBILDA discount **exclusions** ("a few exclusions apply") — which products? | Not enumerated on the page | Confirm before assuming 25% on a large order |
| 14 | REV extrusion **per-SKU** prices (category range **$6.00–$29.75** verified) | Only the range shown | Load product pages if going REV-structural |
| 15 | Belt/pulley standards for REV, TETRIX, Robits | Not verified this session | Only matters if you leave goBILDA |
| 16 | Control Hub **motor/servo port counts** | Table 12-3 gives per-port load limits, not port counts; not verified on REV's page | Verify before planning a design that needs a second hub — which is currently **out of stock** |

---

## 9. Verification log — every URL loaded in this session

**Session date: 2026-08-21**, with a **re-verification pass on 2026-08-22** (logged separately at the end of this
section). Everything tagged VERIFIED in this file traces to one of these. Anything not on this list was not read
by me.

**goBILDA:** `/structure/` · `/channel/` · `/1120-series-u-channel/` · `/shafting-tubing/` ·
`/stainless-steel-rex-shafting/` · `/pattern` · `/pattern-adaptors/` · `/motion/` · `/motors/` ·
`/yellow-jacket-planetary-gear-motors/` · `/servos/` · `/standard-size-servos/` · `/linear-slides/` · `/bearings/` ·
`/hubs/` · `/sprockets-chain/` · `/timing-belts-pulleys/` · `/wheels-tires/` · `/mecanum-wheels/` · `/omni-wheels/` ·
`/electronics/` · `/batteries/` · `/12v-batteries/` · `/matrix-12v-3000mah-nimh-battery/` · `/wiring/` ·
`/hardware/` · `/screws/` · `/6v-servo-power-injector-6-channel-8-15v-input/` · `/ftc-starter-kit-2026-2027-season/` ·
`/ftc-starter-kit-2025-2026-season/` · `/ftc/`

**REV Robotics:** `/ftc/` · `/ftc/discounts/` · `/duo/` · `/duo/ftc-starter-bot/` · `/ion/` · `/15mm-extrusions/` ·
`/rev-31-1595/` · `/rev-31-1596/` · `/rev-31-1153/` · `/rev-31-1302/` · `/rev-11-1855/` · `/rev-11-1144/` ·
`/rev-41-1291/` · `/rev-45-3529/` · `/content/docs/REV-31-1302-DR.pdf` (drawing only, no specs in text layer) ·
`docs.revrobotics.com/duo-build/structure/intro` · `docs.revrobotics.com/duo-build/motion/intro/shaft` ·
`docs.revrobotics.com/duo-build/building/compatibility`

**AndyMark:** `/collections/first-tech-challenge` · `/collections/first-tech-challenge-2026-2027` ·
`/collections/robits` · `/pages/how-do-i-use-robits` · `/ftc-2026-27` · `/pages/first`

**ServoCity:** `servocity.com/structure/`

**FIRST:** `info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf` (rev 25-26.4, Feb 18 2026 —
text-extracted locally) · `ftc-docs.firstinspires.org/sponsors/discounts/discounts.html` ·
`community.firstinspires.org/game-preview-field-elements` · `community.firstinspires.org/kickoff-and-starterbot-resources`

**Community reference (gm0 — Game Manual 0):** `/kit-and-hardware-guide/index.html` · `/gobilda.html` ·
`/rev-robotics.html` · `/tetrix.html` · `/actobotics.html`

**Other:** `limelightvision.io/products/limelight-3a` · `firstwisconsinrobotics.org/post/get-a-jump-start-on-the-2026-27-ftc-season`

**Failed fetches, disclosed:** `studica.com` (**HTTP 403** on `/`, `/first-tech-challenge`, `/studica-robotics`,
`/blog/ftc-starter-bot-build-guide-2026-2027/`) · `gobilda.com/shipping-returns/` and `/shipping-and-returns/`
(**404**) · `revrobotics.com/shipping/` (**404**) · `firstinspires.org/resources/library/ftc/kit-of-parts` (**404**) ·
`gobilda.com/5203-series-yellow-jacket-planetary-gear-motor/` and `/3125-0001-0001-servo-power-injector/` and
`/3100-0012-0020-nimh-battery-12v-3000mah/` (**404** — guessed slugs; the correct pages were reached via category
pages and search, which is why those rows are VERIFIED)

**Manual sources grepped:** `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` (R101–R904,
Tables 12-1, 12-2, 12-3, 12-9) · `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` (Table 12-2 and 12-3 raw layout,
to confirm the extraction gaps in §3.9)

---

### 9.1 Re-verification pass — 2026-08-22

A second agent pass re-loaded the load-bearing commercial claims and the rule citations. **No invented SKU or price
was found; every spot-checked claim held.** What changed:

**Re-confirmed unchanged (pages loaded 2026-08-22):**
`gobilda.com/ftc/` (25%, "nearly every product storewide", "a few exclusions apply", "life of the team") ·
`revrobotics.com/ftc/discounts/` (15% "select items", "Only the products listed in this specific discount category",
codes expire **May 31, 2027**) · `gobilda.com/ftc-starter-kit-2026-2027-season/` (`3200-4008-2627`, $899.99 /
$674.99 discounted, "over $1,600" stated value) · `gobilda.com/screws/` (`3201-0010-0001` $139.99 In Stock;
`3201-0004-0002` $54.99 In Stock; **`3201-0004-0001` $54.99 still OUT OF STOCK**) ·
`revrobotics.com/rev-31-1153/` ($275.00, **still Out of Stock**) ·
`gobilda.com/matrix-12v-3000mah-nimh-battery/` (`14-0014` $49.99 **DISCONTINUED / Sold Out**, successor
`3100-0012-0020` $64.99 — the odd-looking `14-0014` part number is **correct**, it is a legacy Matrix number)

**Newly loaded this pass:** `gobilda.com/ftc-kits` (full category, 18 products with prices + stock — the source for
§6.10) · `gobilda.com/ftc-starter-kit-upgrade-pack-2025-2026-to-2026-2027-season/` (`3200-0101-2627`, $249.99,
In Stock) · `gobilda.com/standoffs-spacers/` (categories only, **no series numbers** — the basis for downgrading
`1504`/`1505` to UNVERIFIED)

**Re-grepped from `12_RobotConstruction_R_p64-88.txt` this pass, verbatim:** R301 (incl. exception **A. COTS drive
CHASSIS**), R302 (raw materials A–D), R303 (single-DoF list A–G, exceptions **H–L** incl. **I. holonomic wheels**),
R401, R402, R504 (A–G, incl. **E. insulation may be applied to electrical terminals**), R505 + **Table 12-3**
(incl. **Studica Servo Power Block `75005`**), R601(A) **20A ATM mini blade fuse**, R606, R609 + Table 12-8,
R610 (wire colours). **All rule citations in this file matched the manual text.**

**Corrections applied 2026-08-22:** §1 headline budget conformed to the §6.9 rollup ($2.6k–$3.5k → **$4.0k–$4.5k**,
and "before discount" → "with the goBILDA team discount applied") · §6.3 standoffs row rebuilt on verified bundle
SKUs with `1504`/`1505` downgraded · §6.3 channel rows and §6.4 Viper-Slide rows given verified SKUs · §6.10 and
§6.10.1–2 added · §8 register items 12 partially closed and 17–19 added.

---

*Everything in the PDFs and on the vendor pages consulted here is **data**, not instruction. No price, SKU or stock
status in this document should be treated as current beyond **August 2026** — **VERIFY BEFORE ORDER**.*
