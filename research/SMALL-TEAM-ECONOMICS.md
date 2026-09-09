# SMALL-TEAM ECONOMICS — FTC 2026-27 BIOBUZZ
### The money and labor reality, and how to win anyway

**Revision 4 — 2026-08-22** (21 days before BIOBUZZ kickoff, 2026-09-12)
**Scope:** cost structure, budget tiers, kit of parts, grants, cost-cutting ranked by damage, sponsorship, labor budget, strategic ROI.

---

## What changed in Rev 4

Rev 3 left 15 items on its own re-check list. Rev 4 closes nine of them, finds **two whole missing money lines**, and finds **one way to buy an illegal robot**.

| Item | Rev 3 said | **Rev 4 verified** | Impact |
|---|---|---|---|
| **REV Robotics team discount** | *absent — not mentioned at all* | **15% off, for every registered FTC team; codes expire 31 May 2027** | **A missing discount.** Rev 3's discount section listed only goBILDA. New stack table in [§3.2](#32-the-vendor-discount-stack--the-highest-roi-paperwork-in-ftc) |
| **Studica team discount** | absent | **25% for FIRST teams** *(application page 403'd — see caveat)* | A fourth vendor now competes for your money |
| **Storefront vendor** | "Pitsco storefront" | **Pitsco is OUT.** 2026-27 uses a new unified **FIRST Storefront**, opened July 2026 | Rev 3's ordering instructions were wrong |
| **Financial guarantor** | absent | **New 2026-27 requirement** for purchase orders / tax exemption | School-affiliated teams must set this up *before* ordering |
| **goBILDA 5203 cross-ratio price parity** | **UNVERIFIED**, a strategy conclusion hung on it | **VERIFIED — $54.99 for all 11 ratios (1:1 / 6000 RPM through 188:1 / 30 RPM)** | Re-gearing genuinely costs nothing but the motor |
| **goBILDA 20V chassis kits** | absent | **⚠️ ILLEGAL.** R501 Table 12-1 lists **12V motors only**. The Overlander-4 at **$599.99** looks cheaper than a $699.99 Strafer and **cannot pass inspection** | A cost cut that ends your season |
| **Claude plan pricing** | UNVERIFIED, third-party summary | **VERIFIED: Pro $20/mo, or $200/yr ($17/mo). Max from $100/mo** | 8 months × $20 = **$160 beats the $200 annual plan** |
| **FTC SIM 2026-27 field** | UNVERIFIED | **Confirmed absent** — DECODE is still the newest field listed | Don't plan September programming around a BIOBUZZ sim |
| **StarterBot** | one line | **4 official vendors** (AndyMark, goBILDA, REV, Studica); *Base* published now, **full StarterBot at kickoff**; goBILDA **Upgrade Pack $249.99** for last-year's-kit teams | New [§3.5](#35-the-starterbot-path--the-cheapest-way-to-own-a-working-robot-in-week-2-new-in-rev-4) |
| **BAE Systems FTC grant** | absent | Added to the grants table | One more named program |
| **Chassis kit prices** | 5 kits | 9 legal 12V kits refreshed; **Bravo Bare-Bones $399.99** is the new cheap entry | Cheaper legal COTS chassis exists |
| **Generic EVA floor tiles** | absent | **$1.25–1.95/sq ft** vs AndyMark's **$2.03/sq ft**, but **½" not ⅝" thick** | New ranked cut, with an honest verdict |
| **"Tier B/C gap narrows"** | asserted | **Half true.** Absolute gap halves ($7,040 → $3,500); the *ratio* slightly widens (1.97× → 2.17×) | Corrected and reframed in [§2.3](#23-three-year-cost-of-ownership-and-cost-per-student-new-in-rev-4) |
| **GM0's $4,000 startup figure** | cited flat | **Built on a $295 registration** — pre-2025 pricing | GM0's total understates today by ~$55 on that line alone |
| **DRIVE TEAM composition** | not stated | **Up to 4 people; max 1 DRIVE COACH (may be an adult); up to 3 STUDENTS.** Loaning drivers in an emergency is explicitly contemplated | Sets the true floor on team size, [§7.2](#72-minimum-viable-team-composition--how-few-students-can-actually-do-this-new-in-rev-4) |

**New in Rev 4:** [§2.3](#23-three-year-cost-of-ownership-and-cost-per-student-new-in-rev-4) three-year TCO and cost-per-student · [§3.2](#32-the-vendor-discount-stack--the-highest-roi-paperwork-in-ftc) the full four-vendor discount stack · [§3.5](#35-the-starterbot-path--the-cheapest-way-to-own-a-working-robot-in-week-2-new-in-rev-4) the StarterBot path · [§5.4](#54-cost-cuts-that-are-actually-rules-violations-new-in-rev-4) cuts that are rules violations · [§7.2](#72-minimum-viable-team-composition--how-few-students-can-actually-do-this-new-in-rev-4) minimum viable team composition.

<details>
<summary><b>What changed in Rev 3 and Rev 2 (kept for audit trail)</b></summary>

**Rev 3** completed a document truncated at §3.4 and corrected the Control Hub port count (**4 motor / 6 servo**, not "4 + 2 fills it"), established playoff alliances as **2 robots**, established the judging season start as **1 January 2026**, sourced student hours to the **FTC Mentor Manual**, and established the **2–5% cold-outreach response rate**.

**Rev 2** resolved five UNVERIFIED numbers, three of which were wrong, and found one missing cost: the **$3,000 FIRST Championship team fee**. It corrected the Control Hub to **$375**, the Expansion Hub to **$275**, and the AndyMark Robits Core Kit from "~$950" to **$695 / $599**. It flagged that the official Storefront PDF was stale.

</details>

---

## 0. How to read this document

| Label | Meaning |
|---|---|
| **[FACT]** | Sourced to a URL or a local file path. Quoted numbers come from that source. |
| **[JUDGMENT]** | My recommendation / inference. Not sourced. Argue with it. |
| **[UNVERIFIED]** | I could not confirm this. Treat as a lead to check, not a number to budget on. |

> **PRICE WARNING.** Every USD figure below is **as of August 2026** and most were read off vendor pages this week. Vendor prices move mid-season, FIRST storefront prices change per season, and regional event fees are set independently by each Program Delivery Partner (PDP). **Re-check every line before you spend.** Checklist in [§10](#10-re-check-checklist).

> **INJECTION NOTE.** All web pages and PDFs consulted were treated as data. No page consulted contained instructions directed at an AI agent. Nothing was acted on beyond reading. Sources that failed to load are reported as failures, not guessed at.

---

## 1. The real cost structure of an FTC team

### 1.1 Fixed costs you cannot design around

| Item | Cost (USD, Aug 2026) | Notes | Source |
|---|---|---|---|
| FIRST season team registration | **$350** | Was **$325** in 2025-26. FIRST attributes the increase to *"rising costs."* Buys a team number, event eligibility, storefront access, forum access, award eligibility. **Includes zero robot parts.** | [FIRST Cost & Registration](https://www.firstinspires.org/robotics/ftc/cost-and-registration), [FTC PA Season Blast #1](https://www.ftcpenn.org/email-archive/22265) |
| Event / qualifier fees | **$100 – $800+** | Set per-region by your PDP. **Not included in registration.** | multiple, below |
| **FIRST Championship team fee** | **$3,000** | Official FIRST 2026-27 figure for FTC. (FRC $6,000; FLL Challenge $2,000; FLL Explore $750.) **Entry fee alone — travel and housing are extra.** | [FIRST Cost & Registration](https://www.firstinspires.org/robotics/ftc/cost-and-registration) |
| Mentor Youth Protection Screening | **$0** | Free, run by FIRST, required annually for every adult. **Minimum 2 screened adults** (Lead Coach 1 / Lead Coach 2). | [FTC Mentor Manual](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-mentor-manual.pdf); V0 manual line 847 |

**[FACT] What the $350 actually buys, per FIRST:** an official team number; the ability to register for and compete at official events; access to the community forums for control-system support; eligibility for team awards and *FIRST* Leadership Award nominations; and participant/alumni access to scholarships and career-discovery. It explicitly **does not** include event participation (*"event availability varies by region and fees are set by local FIRST Program Delivery Partners"*) and **does not** include robot build kits or control-system hardware. ([FIRST Cost & Registration](https://www.firstinspires.org/robotics/ftc/cost-and-registration))

**[FACT] FIRST's own headline startup number:** *"You can start your FIRST Tech Challenge team for around $1,800, which includes the yearly registration fee and initial robotics set investment."* The same page states local events *"are not included with the registration fee."* ([FIRST — Get Started](https://www.firstinspires.org/programs/ftc/get-started))

> **[JUDGMENT] That $1,800 is honest but incomplete.** It is registration + storefront kits, i.e. $350 + ~$1,305, rounded up. It excludes event fees, batteries beyond the one in a kit, any practice field, any tool, any spare, and all travel. Treat $1,800 as *the cost of owning a legal robot*, not the cost of competing with it. The real floor is ~$2,600 (see [§2](#2-three-budget-tiers)).

**Regional event fee reality [FACT]** — real published figures, showing a ~5× spread:

| Region | Structure | Fee |
|---|---|---|
| New Jersey | Flat season fee, required before competing | **$100** |
| Arizona | 2 events / 3 events | **$225 / $300** (+ separate region championship fee) |
| Southern California | Up to 4 League events + 1 Qualifier, **single payment** | **$300** (+$100 if invited to Wildcard) |
| Minnesota (High Tech Kids) | League Play / Qualifier / State Championship | **$480 / $355 / $485** |
| FIRST Chesapeake | 2 qualifiers | **$500** |

Sources: [NJ FTC](https://www.newjerseyftc.com/event-registration-and-acceptance-criteria.html), [AZ FTC calendar](https://azfll.engineering.asu.edu/events/calendar/ftc-calendar/), [SoCal FTC League Information](https://socalftc.org/leagues/league-information/), [High Tech Kids](https://hightechkids.org/ftc-overview/how-much-does-ftc-cost/), [FIRST Chesapeake](https://www.firstchesapeake.org/post/september-ftc-link-decode-season-registration-and-qualifiers)

> **[JUDGMENT] Your single biggest uncontrolled cost variable is your region, and you cannot change it.** Before building a budget, email your PDP for the 2026-27 fee schedule **in writing**. A $100 flat-fee region and a $500 two-qualifier region differ by more than your entire spares budget. Also ask, in the same email, two questions almost nobody asks: *"Is there a waitlist, and what is your acceptance criterion?"* and *"Can you nominate us for the Hardship Grant?"* ([§3.3](#33-grants--named-programs-real-numbers))

> **[JUDGMENT] The $3,000 Championship fee changes the shape of the whole budget.** It is larger than a Tier A team's *entire season*. Qualifying for Houston is not a reward that pays for itself — it is a $3,000 invoice due fast. FIRST's championship planning guidance states teams are *"not guaranteed their spot at FIRST Championship until they secure both their event registration fee with FIRST and their lodging with ConferenceDirect,"* with a hard payment deadline (April 9, 5:00 PM ET in the 2025 cycle). ([FIRST — Planning for FIRST Championship](https://community.firstinspires.org/2025-planning-for-first-championship)) Plan the fundraiser in November; do not carry the money in your baseline. See [§1.8](#18-travel-and-soft-costs--the-line-that-eats-small-teams).

---

### 1.2 The control system — and whether the cheap path is still legal

**[FACT — LOCAL SOURCE]** The BIOBUZZ **V0 Competition Manual Section 12 (ROBOT Construction Rules) is FINAL already** — it will not change at kickoff. R-rules read directly from
`C:/Users/ericj/Documents/BIOBUZZ Analysis/manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt`

**R701 — ROBOT CONTROLLER.** Must be:
> A. a REV Control Hub (REV-31-1595), **or**
> B. a smartphone Android device connected to a REV Expansion Hub (REV-31-1153).
> In addition to A or B, a ROBOT may also contain: C. no more than one additional REV Expansion Hub (REV-31-1153).

**R901 — DRIVER STATION.** The OPERATOR CONSOLE must have at least one of:
> A. REV Driver Hub (REV-31-1596), **or**
> B. Any Android Device with or without any combination of USB cables … for connecting one or more gamepads.

**So: YES, the phone-based path is still legal in 2026-27 — on both ends.** But the manual prints this warning under *both* rules:

> "Due to unpredictable variations in Android software across different manufacturers and updates, the REV Control Hub is the only officially supported ROBOT CONTROLLER device. Teams choosing to use any other unsupported device (e.g., smartphones) are responsible for testing and verifying its compatibility, functionality, and performance."

**Control system pricing [FACT — verified at REV, Aug 2026]:**

| Item | SKU | REV retail | Via FIRST Storefront | Source |
|---|---|---|---|---|
| REV Control Hub | REV-31-1595 | **$375.00** (incl. XT30 ext. cable, 3-pin JST PH cable, USB-A→C) | **Electronics / Control set $350** | [REV](https://www.revrobotics.com/rev-31-1595/), [FIRST](https://www.firstinspires.org/robotics/ftc/cost-and-registration) |
| REV Driver Hub | REV-31-1596 | **$275.00** (incl. 5040 mAh Li-ion, wall charger, cable) | **Driver Kit $295** (Driver Hub + 2 FTC-legal gamepads + FTC-legal webcam) | [REV](https://www.revrobotics.com/rev-31-1596/), [FIRST](https://www.firstinspires.org/robotics/ftc/cost-and-registration) |
| REV Expansion Hub | REV-31-1153 | **$275.00** (incl. XT30 ext. cable, 3-pin JST PH cable) | not bundled | [REV](https://www.revrobotics.com/rev-31-1153/) |

> **⚠️ [FACT — NEW IN REV 4] The REV 15% FTC team discount does NOT cover the control system.** The REV FTC discount category contains structure (15mm extrusion $6.00–29.75, 45mm U-channel $2.50–44.00, 45mm flat plate $2.50–12.50), motion (DUO traction wheels $12.50–20.00, DUO omni $27.00–31.00, 5 mm hex shaft $12.50–23.25, #25 chain turnbuckle $11.00), hardware (M3 nuts $6.00–8.75, 5.5 mm wrenches $11.00–14.75) and accessories (PS4-compatible gamepad $26.00, Color Sensor V3 $20.75, Driver Hub battery $21.75). It **does not** include the Control Hub, the Expansion Hub, or the 12V main batteries. ([REV FTC Discounts](https://www.revrobotics.com/ftc/discounts/))

> **[FACT] The Storefront Electronics/Control set at $350 contains a $375 Control Hub plus other parts.** Buying the Hub retail is strictly worse, and no discount closes the gap.

> **[JUDGMENT] Do NOT take the phone path. It is the most expensive-looking cheap decision available to you.** The saving is roughly $200–350. The cost is that you own the entire Android compatibility surface: OS updates that break the app mid-season, USB-OTG flakiness, Wi-Fi Direct pairing failures at events, and — critically — **no support from the FTC forums, from REV, or from the FTA at your event**, because the manual says in writing that you are on your own. A small team's scarcest resource is debugging hours. Spend $350 to never spend those hours.

**Port budget [FACT — verified at REV, Aug 2026].** The Control Hub has **4 DC motor ports (with built-in encoder ports), 6 servo ports, 8 digital I/O, 4 analog, 4 I2C, 2 RS485, 1 internal 6-axis IMU.** ([REV-31-1595](https://www.revrobotics.com/rev-31-1595/)) **R503 [FACT — LOCAL SOURCE]** caps the whole ROBOT at **8 motors and 8 servos**.

> **⚠️ Four ports is four ports. A 4-wheel-drive robot consumes 100% of the Control Hub's motor ports before a single mechanism exists.** Any motor-driven mechanism on a 4-motor drivetrain forces the **$275 Expansion Hub**.

> **[JUDGMENT] This is the cheapest architectural decision on the robot, and almost nobody costs it out.** Your three legal ways to avoid $275:
>
> | Architecture | Motors used | Expansion Hub needed? |
> |---|---|---|
> | 4-motor drivetrain + all-servo mechanisms | 4 motors, ≤6 servos | **No — $0** |
> | 2-motor (tank) drivetrain + 2-motor mechanism | 4 motors | **No — $0** |
> | 4-motor drivetrain + any motor mechanism | 5–8 motors | **Yes — +$275** |
>
> Servos are cheaper than motors *and* cheaper than the port they don't consume. A goBILDA 2000-Series torque servo is **$27.74 discounted** vs a 5203 motor at **$41.24 discounted**; swapping one mechanism motor for a servo can save **$14 on the actuator and $275 on the Hub**. Decide this in CAD, before you order.

---

### 1.3 Power — batteries and chargers

**[FACT — LOCAL SOURCE] R601** restricts you to **exactly one** approved 12V NiMH main battery, from a closed list (V0 Table 12-4):

| Approved main battery pack | Part number | Notes |
|---|---|---|
| AndyMark Flat Pack Battery DC 12V | `am-5290` | |
| goBILDA 12V NiMH Nested Battery | `3100-0012-0020` | May be labeled "Modern Robotics" |
| Matrix 12V 3000 mAh NiMH | `14-0014` | Formerly 739023 |
| REV 12V Slim Battery | `REV-31-1302` | |
| Studica 12V 3000 mAh NiMH | `70025` | |
| TETRIX MAX 12V 3000 mAh NiMH | `W39057` | |
| WATTOS 12V Battery | `WT-NMH1230` | |

**Seven packs, not four.** This is the complete Table 12-4 list, read from `sections/12_RobotConstruction_R_p64-88.txt` ll. 663–675. R601 also permits exactly two alterations to a pack: **A.** the fuse may be replaced with a COTS equivalent in-line **20 A ATM mini blade** fuse installed per R610, and **B.** installed connectors may be replaced with "other popular connectors such as Anderson Powerpole, XT30, or any connector with a comparable power rating."

**R602** additionally allows COTS USB battery packs of **≤100 Wh (27,000 mAh at 3.7V), 5V/5A or 12V/5A max output**, for coprocessors only — and they **must remain electrically isolated from the ROBOT power systems.**

**Charging rule [FACT — LOCAL SOURCE] — this is E511, an EVENT rule, not an R-rule:** *"Never charge batteries on a battery charger that exceeds a **3-amp average channel current**,"* and *"Safe connectors are those with a polarized connector corresponding to the connector on the battery itself. Batteries must never be charged using alligator clips or similar."* (`sections/05_EventRules_E_p33-42.txt`, **E511**, ll. 362–372 — Section 5 Event Rules, *not* Section 12.)

| Item | SKU | Cost | Source |
|---|---|---|---|
| REV 12V Slim Battery, 10-cell 3000 mAh, XT30 + inline 20A ATM fuse | REV-31-1302 | **$55.00** | [REV](https://www.revrobotics.com/rev-31-1302/) |
| REV charger for Slim Battery (XT30 output) | — | **$36.50** | [REV](https://www.revrobotics.com/rev-31-1302/) |
| AndyMark Flat Pack Battery, 3000 mAh, XT30(F), 20A fuse | am-5290 | **$54.00** | [AndyMark](https://andymark.com/products/am-flat-pack-battery) |
| AndyMark RDX2 200 2-port XT30 charger, 100 W/port, **with battery resistance meter** | am-5619_XT30 | **$154.00** | [AndyMark](https://andymark.com/products/rdx2-200-2-port-xt30-ftc-battery-charger) |

> **[JUDGMENT] Budget three batteries and a two-port charger — roughly $319.** One on the robot, one charging, one cooled and resting. Two channels because a single 3A-limited channel cannot turn a pack around inside a qualifier's match cadence. See [§5.2](#52-the-three-false-economies) for why cheapness here is the #1 self-inflicted competitive wound.

---

### 1.4 Starter kits, structure and motion

The four official *FIRST* vendor kits, priced Aug 2026:

| Kit | SKU | List | FTC-team price | Source |
|---|---|---|---|---|
| **FIRST Storefront Build Kit** (REV FTC Competition Set V3.1) | — | **$660** (2026-27; was $650) | storefront, limit 1/team/season | [FIRST](https://www.firstinspires.org/robotics/ftc/cost-and-registration) |
| **goBILDA FTC Starter Kit 2026-27** | 3200-4008-2627 | **$899.99** | **$674.99** (25% team discount) | [goBILDA](https://www.gobilda.com/ftc-starter-kit-2026-2027-season/) |
| **goBILDA FTC Starter Kit Upgrade Pack** *(new in Rev 4)* | — | **$249.99** | **~$187** (25%) | [goBILDA StarterBot guide](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/) |
| **REV FTC Starter Kit V3.1** | REV-45-3529 | **$695.00** | 15% off *(if in the discount category — verify)* | [REV](https://www.revrobotics.com/competition/ftc-starter-bot/) |
| **AndyMark Robits Core Kit — with electronics** | am-5000a | **$695.00** | — | [AndyMark](https://andymark.com/products/robits-core-kit) |
| **AndyMark Robits Core Kit — no electronics** | am-5000a_NE | **$599.00** | — | [AndyMark](https://andymark.com/products/robits-core-kit) |
| **Studica FTC starter kit** | — | **[UNVERIFIED]** — product page returned HTTP 403 | 25% claimed | [Studica FTC](https://www.studica.com/first-tech-challenge) |

> **[JUDGMENT — NEW IN REV 4] The goBILDA Upgrade Pack at $249.99 ($187 discounted) is the cheapest legitimate route to a current-season kit if you already own last year's.** It is not advertised anywhere near as loudly as the $899.99 full kit. If your team competed in DECODE, check what the Upgrade Pack contains against your existing inventory before paying five times as much.

**What's in the goBILDA 2026-27 Starter Kit [FACT]:** 3× Yellow Jacket 19.2:1 (312 RPM) + 1× 50.9:1 (117 RPM) motors with encoders; 4× dual-mode servos (2 torque, 2 speed) + servo programmer; U-channel and polycarbonate grid plates; 7× 48 mm + 2× 72 mm GripForce Gecko wheels, 2× omni, hogback traction, intake rollers; sprockets/chain/gears; **12V NiMH battery and charger**; hex keys and nut driver. ([goBILDA](https://www.gobilda.com/ftc-starter-kit-2026-2027-season/))

**What's in the AndyMark Robits Core Kit (am-5000a) [FACT]:** 2 NeveRest motors, 2 programmable torque servos, 2 programmable speed servos, power switch, **battery and charger**, motor encoder cables, polycarbonate/aluminium structure on a 0.5" grid, HTD pulleys, gears, timing belts, hex shafts, 4 wheels (compliant + omni), fasteners, spacers, assembly tools, ruler, cable ties, and an organizer tote. ([AndyMark](https://andymark.com/products/robits-core-kit))

**Motors and servos [FACT]:**

| Part | SKU | List | With 25% goBILDA team discount |
|---|---|---|---|
| goBILDA 5203 Yellow Jacket planetary gearmotor, 19.2:1 / 312 RPM, encoder | 5203-2402-0019 | **$54.99** | **$41.24** |
| goBILDA 2000 Series Dual Mode Servo (25-2, Torque), 300 oz-in stall @ 6V, 60 g | 2000-0025-0002 | **$36.99** | **$27.74** |

> **✅ [FACT — RESOLVED IN REV 4] All eleven Yellow Jacket 5203 gear ratios cost the same $54.99.** Verified across the family page: 1:1 (6000 RPM), 3.7:1 (1620), 5.2:1 (1150), 13.7:1 (435), 19.2:1 (312), 26.9:1 (223), 50.9:1 (117), 71.2:1 (84), 99.5:1 (60), 139:1 (43), 188:1 (30). *"The pricing is uniform across all gear ratio options at $54.99 per unit."* ([goBILDA Yellow Jacket family](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/))
>
> **[JUDGMENT] This was UNVERIFIED in Rev 3 and a real strategy conclusion hung on it. It holds.** Changing your mind about a gear ratio costs the price of a motor and nothing else — no premium for extreme ratios. Practically: **do not agonise over gear ratio in CAD.** Pick a plausible one, build it, measure it, and if it is wrong buy the right one for $41.24 discounted. A team that treats gear ratio as a cheap empirical question will out-iterate a team that treats it as an expensive analytical one. Also note R501's own remark that legal gearmotors *"may be used with or without the provided gearbox, and/or with any other compatible gearbox"* — you may legally swap gearboxes between motors you already own.

> **[JUDGMENT] Standardize entirely on one motor family and one servo family.** The saving is not per-part, it is *inventory*: one spare motor covers every position on the robot, one spare servo covers every joint, one encoder-cable type, one mounting pattern, one set of CAD. Mixing families to save $8 doubles your spares bill and your failure modes. Rank 5 in [§5.1](#51-cost-cuts-ranked-by-savings-per-unit-of-performance-lost).

---

### 1.5 The field, and its substitutes

| Item | SKU | Cost | Source |
|---|---|---|---|
| **Official FTC Perimeter Kit** — 11'9"×11'9", 12.3" tall, 80 lb, tool-free hinged corners | am-0481b | **$740.00** | [AndyMark](https://andymark.com/products/first-tech-challenge-perimeter-kit) |
| **Official FIRST DIY Low-Cost Perimeter** — ½" PVC pipe + tees + elbows, ⅛" hardboard panels, #8 screws, PVC cement; Home Depot SKUs listed in the guide | — | **$159.90 est. before tax** — *guide's costs date to 2020-10-06; expect materials inflation* | [FIRST Low-Cost Field Perimeter Guide](https://ftc-resources.firstinspires.org/ftc/archive/2025/game/diy-perimeter) |
| Field Soft Tiles (24"×24"×**⅝"** EVA; **36 tiles = full field**) | am-2499 | **1 = $9.70 · 4-pk = $38 · 18-pk = $147 · 36-pk = $293** (= **$2.03/sq ft**) | [AndyMark](https://andymark.com/products/first-tech-challenge-field-soft-tiles) |
| *Generic EVA gym tiles, 24"×24"×**½"*** *(new in Rev 4)* | various | **$1.25 – $1.95/sq ft** → ~**$180–281** for 144 sq ft | [Home Depot](https://www.homedepot.com/), [Walmart foam tiles](https://www.walmart.com/c/kp/foam-tiles-flooring) |
| **BIOBUZZ Full Game Set** | — | **$599.00** | [AndyMark](https://andymark.com/products/ftc-2026-27-preorders) |
| **BIOBUZZ Partial Game Set** (Red or Blue) | — | **$399.00 each** | [AndyMark](https://andymark.com/products/ftc-2026-27-preorders) |
| **BIOBUZZ POLLEN Game Preview Pack** — 3 elements, yellow, 2.8"±0.1", 0.055 lb | am-5851_preview | **$5.50** (≈ $1.83/ball) | [AndyMark](https://andymark.com/products/ftc-2026-27-game-preview-pack) |

**Critical logistics [FACT]:** *"Orders received by 7-August-2026 will begin shipping after kickoff, beginning Monday, 14-September, 2026."* and *"Team orders will be fulfilled in the order received."* Game sets **exclude** the perimeter (am-0481b) and soft tiles (am-2499). Pre-orders opened **2 May 2026**. AndyMark publishes **no second wave** after the 7 Aug cutoff. ([AndyMark pre-orders](https://andymark.com/products/ftc-2026-27-preorders), [FIRST Game Preview](https://community.firstinspires.org/game-preview-field-elements))

> **[JUDGMENT] You have missed the 7 Aug wave, and orders ship in the order received — so you are behind teams that ordered in May.** Assume you will not have official game elements in September. Plan the first month around the $5.50 preview pack as a dimensional reference plus printed or substituted balls, and **phone AndyMark** to ask when an order placed today would actually ship. Do not build a schedule that assumes a field in week 1.

**[FACT] FIRST confirms POLLEN are** *"plastic balls approximately 3 in. in diameter"* that function similarly to DECODE's artifacts. ([FIRST Game Preview](https://community.firstinspires.org/game-preview-field-elements))

**[FACT] A community 3D-print model of the BIOBUZZ Pollen exists** on MakerWorld (`https://makerworld.com/en/models/2755231-ftc-2026-2027-biobuzz-pollen-game-element`). **[UNVERIFIED]** — the page returned HTTP 403 to fetch; print settings, dimensional accuracy and mass fidelity are unconfirmed. Verify against the official 0.055 lb / 2.8" spec before tuning any mechanism against printed balls.

> **[JUDGMENT] Highest-leverage practice-space decision:** **DIY perimeter (~$160) + 18 official tiles ($147) = ~$307 half-field** versus **$740 + $293 = $1,033 full official field** — a **$726 saving**, more than an entire Tier A structure budget. The performance cost is real but small: hardboard/PVC walls differ in bounce and friction from official polycarbonate-and-extrusion, **and BIOBUZZ is a ball game (2.8" POLLEN)**, so wall interaction matters more this season than it did in a game about clipping specimens. Mitigation: DIY for volume practice, then beg 2–3 sessions on a real field before your first event.

> **[JUDGMENT — NEW IN REV 4] On generic ½" foam tiles: save the $113, but not on your main practice area.** The official tile is **⅝"**; generic gym tiles are typically **½"**. That ⅛" changes how far your wheels sink, which changes effective ride height, ground clearance under the frame, and the compression your traction wheels see. Those are exactly the variables your drivetrain and any ground-intake are tuned against. **Use official ⅝" tiles for the area where the robot actually runs; use cheap generic tiles for a separate programming/odometry bench area, for the pit floor, and to protect a garage floor.** Saving $113 by tuning against the wrong surface is a false economy in the same family as the battery one.

---

### 1.6 Tools, 3D printing, fabrication

| Item | Cost | Source |
|---|---|---|
| Bambu Lab A1 mini | **$299** | [Bambu Lab US](https://us.store.bambulab.com/products/a1-mini) via [price tracker](https://originalpricing.com/bambu-lab-printer-prices/) |
| Bambu Lab A1 mini Combo (with AMS Lite) | **$649** | same |
| Bambu Lab P1S (enclosed) | **$399 on sale / $699 MSRP** — *"has hit $399 repeatedly on sale"* | same |
| PLA filament | **~$25/kg** (Bambu own-brand) | same |
| Benchtop drill press (home center) | **~$150** | [FTC 9929 toolbox](https://ftc9929.com/2020/06/22/whats-in-our-toolbox/) |
| Tap Magic cutting fluid | **~$8**, lasts multiple seasons | same |
| Core hand-tool set — nut drivers, drill bits, hacksaw, hex keys (ball-end **and** T-handle), tap & drill set, files, combination + ratcheting wrenches, chain tool, rivets + riveter | **$250–450** for a real set | [REV Building Your Toolbox](https://www.revrobotics.com/blog/tech-tool-tip-tuesdays-building-your-toolbox/) |

> **[JUDGMENT] An enclosed printer is a want; an A1 mini is a need.** At $299 + $25/kg, a printer pays for itself the first time it replaces a $60 custom bracket order plus a week of shipping. For a small team the *schedule* saving dwarfs the *dollar* saving: same-day iteration is how you get 6 design cycles instead of 2. Buy PLA for prototypes and one spool of PETG or ASA for parts that see load or heat. Do not buy the enclosed P1S unless you are already printing ABS routinely. **Before buying anything: your school library, public library and local makerspace probably already own a printer.** A Tier A team should exhaust that before spending $299.

---

### 1.7 Software and digital tooling — the $0 column

**[FACT] Essentially the entire software stack an FTC team needs is free, and most of it is free *specifically because you are a FIRST team*.**

| Tool | Cost to an FTC team | What it replaces | Source |
|---|---|---|---|
| **Onshape** — cloud CAD + PDM, with FTC Parts Library and 2026 FTC Field Model | **$0** — *"Onshape is proud to provide free access to our CAD platform and resources for FRC and FTC Teams."* Free Education account for **every student and mentor** | A commercial CAD seat | [Onshape for FIRST](https://www.onshape.com/en/education/first-robotics), [FTC Docs — PTC CAD Resources](https://ftc-docs.firstinspires.org/en/latest/cad_resources/ptc/ptc.html) |
| **PTC Creo, Mathcad, Windchill, Vuforia** | **$0** to FTC teams via the PTC *FIRST* student download page | Desktop CAD, engineering math | [FTC Docs — PTC](https://ftc-docs.firstinspires.org/en/latest/cad_resources/ptc/ptc.html) |
| **FIRST Tech Challenge Skill Builders** *(new in Rev 4)* — activities, challenges and robot mini-games on FIRST Training | **$0** | Paid pre-season curriculum | [FIRST — Introducing Skill Builders](https://community.firstinspires.org/introducing-first-tech-challenge-skill-builders) |
| **Vendor StarterBot resource guides** *(new in Rev 4)* — assembly PDFs, example code, STEP files, interactive 3D models from all four vendors | **$0** (the *guide*; the kit is not) | A paid build curriculum | [goBILDA](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/), [Studica](https://www.studica.com/ftc-starter-bot-resource-guide-2026-2027) |
| **FTC SIM** (FIRST Robotics Canada) — browser robot simulator with a competition field | **$0**, supported by CanCode | **A practice field, for programming** | [ftcsim.org](https://ftcsim.org/) |
| **Android Studio / FtcRobotController / OnBot Java / Blocks** | $0 | Commercial IDE | official FTC toolchain |
| **GM0 (Game Manual 0)** — the community engineering reference | $0 | A paid curriculum | [gm0.org](https://gm0.org/en/latest/docs/being-a-team/starting-a-team.html) |
| **ftcscout.org, ftc-events API** | $0 | Paid scouting software | see `research/SCOUTING-AND-AWARDS.md` |

> **[JUDGMENT] Read that table as a strategic statement, not a shopping list.** CAD, simulation, match data, training curriculum, and the entire programming toolchain — the things that most differentiate a good robot from a mediocre one — **cost a well-funded team exactly the same as they cost you: nothing.** Money buys machining, spares depth, a second robot, and travel. It does not buy better CAD, better code, better strategy, or better data. Every hour you move from fundraising into those four things is an hour spent in the part of the game where your budget is irrelevant.

> **⚠️ [FACT — RESOLVED IN REV 4] FTC SIM does NOT yet have a BIOBUZZ field.** As of 2026-08-22 the site still lists *"2025-26 Competition Field: DECODE presented by RTX"* as its current field, with no 2026-27 mention. ([ftcsim.org](https://ftcsim.org/))
> **[JUDGMENT] So do not plan September programming around a BIOBUZZ simulator.** Plan it around: (a) the DECODE sim, for drivetrain/odometry/state-machine practice that transfers regardless of game; (b) the **free Skill Builders** on FIRST Training; and (c) the **free StarterBot Base build guides and example code**, which exist *today* and are built around a drop-center 6WD chassis with a Gecko-wheel intake — i.e. exactly the mechanism family a ball game will need.

**The AI line item [FACT — verified in Rev 4 + JUDGMENT].** This team uses Claude Code. Budget it explicitly rather than pretending it is free:

| Plan | Verified price | [JUDGMENT] Fit |
|---|---|---|
| Free | **$0** | Enough to try it; not enough for daily work |
| **Claude Pro** | **$20/month billed monthly**, or **$200/year billed annually (≈$17/mo)** | Adequate for one mentor + light student use |
| Claude Max | **from $100/month** (5× and 20× usage tiers) | Only if a student is doing heavy daily code work |

Source: [claude.com/pricing](https://claude.com/pricing) — *"$17 Per month with annual subscription discount ($200 billed up front). $20 if billed monthly."* Anthropic publishes no standard student discount for consumer plans.

> **[JUDGMENT — corrected in Rev 4] Pay monthly, not annually.** An FTC season is roughly eight active months (September–April). **8 × $20 = $160**, which is **$40 cheaper than the $200 annual plan**, and you can cancel in May. Rev 3 quoted $160/season from an unverified third-party summary and happened to land on the right number for the wrong reason; the reason is that you should not buy twelve months of a service you use for eight.
>
> That $160 is roughly four discounted motors. It is worth it **only if it is spent on clerical displacement, not on engineering displacement** — see [§7.6](#77-where-ai-displaces-labor--and-where-it-must-not). Note **A201** permits AI use in portfolios *provided you credit it*.

---

### 1.8 Travel and soft costs — the line that eats small teams

| Item | Realistic range | Notes |
|---|---|---|
| Local events (carpool, no hotel) | **$0 – $150** | fuel only |
| Regional / State Championship, 1 night, 8 people | **$800 – $1,800** | 2–3 hotel rooms + food |
| **FIRST Championship (Houston), 8 people** | **$3,000 fee [FACT]** + **$6,000–$9,000 travel [JUDGMENT — estimate]** = **~$9,000–$12,000** | Flights + 4 nights of ConferenceDirect-booked lodging + food. **This one line can exceed your entire robot budget by 3×.** |
| Team shirts / pit banner / portfolio printing | **$200 – $500** | |

> **[JUDGMENT] Do not budget for FIRST Championship in your baseline.** Budget it as a *contingent* campaign you launch the week you qualify. Teams that pre-reserve championship money and do not qualify have starved their robot for nothing; teams that qualify without a plan panic against a two-week clock and a hard April deadline. **Write the emergency-fundraiser email in November and leave it in drafts.** With the fee confirmed at $3,000, the ask you are drafting is for roughly $10,000 — a scale that needs a named local corporate sponsor lined up in advance, not a bake sale.

---

### 1.9 The invisible lines: shipping, tax, and organizational overhead

**[FACT]** The FIRST cost page states plainly that *"applicable sales tax and shipping not included"* in its listed prices. ([FIRST Cost & Registration](https://www.firstinspires.org/robotics/ftc/cost-and-registration))

**[FACT — NEW IN REV 4] Two 2026-27 process changes with money consequences:**

1. **Sales tax now applies to registrations without physical items in certain jurisdictions.** Previously a registration with no goods attached often escaped tax. ([FIRST — 2026-2027 Season Pricing and Registration Updates](https://community.firstinspires.org/2026-2027-season-pricing-and-registration-updates))
2. **A "financial guarantor" profile is now required** for any team using a purchase order or a tax-exemption certificate — set up under the **Team/Account Finances** tab using the organization's EIN or international equivalent. ([FIRST — Key Changes to Registration](https://community.firstinspires.org/key-changes-to-first-tech-challenge-registration-whats-new))

> **[JUDGMENT] If you are school-affiliated, the financial guarantor step is a hard blocker with a slow clock.** It requires the school's EIN and, in practice, a business-office signature. Start it **before** you try to order, not the night you discover the storefront won't accept your PO. Districts also had to *"add FIRST as a payor"* now that Pitsco is no longer the vendor — if nobody in your business office has done that, your first order will fail.

| Hidden line | Realistic figure | Notes |
|---|---|---|
| Shipping + sales tax on parts | **~10% of goods spend** **[JUDGMENT]** | On Tier B goods (~$4,900) that is **~$490** — more than a battery set. goBILDA offers **$50 flat-rate international** shipping to FTC team accounts; **no published domestic free-shipping threshold** at goBILDA or REV. ([goBILDA FTC](https://www.gobilda.com/ftc/)) |
| Getting 501(c)(3) / tax-deductible status | **$275 – $575 first year** | See [§3.4](#34-becoming-tax-deductible-the-unlock-for-real-sponsorship). Optional, but it gates most corporate money. |
| Consumables — filament, zip ties, Loctite, tape, gamepad batteries | **$100 – $250/season** **[JUDGMENT]** | Never budgeted, always spent. |
| Pit setup — table cover, power strip, tote bins, extension cord | **$100 – $200** **[JUDGMENT]** | One-time, reusable for years. |

> **[JUDGMENT] Add 10% to every goods number in this document before you present a budget to a school or a sponsor.** The tier totals in [§2](#2-three-budget-tiers) include this.

---

## 2. Three budget tiers

All figures **USD, as of Aug 2026**, **first-year (rookie) all-in**, **including ~10% shipping and sales tax on goods**. Assumes the cheaper end of regional event fees. **FIRST Championship is excluded and shown separately as a contingency.**

### 2.1 The tier table

| Line | **Tier A — Bare minimum** | **Tier B — Mid / genuinely competitive** | **Tier C — Well-funded** |
|---|---|---|---|
| FIRST registration | 350 | 350 | 350 |
| Event fees | 250 (1 league) | 500 (league + qualifier + regional champ) | 1,200 (3 entry-level + state + off-season) |
| Storefront Driver Kit | 295 | 295 | 295 |
| Storefront Electronics / Control set (Control Hub) | 350 | 350 | 350 |
| Storefront Build Kit | 660 | 660 | 660 |
| goBILDA Starter Kit (25% off) | — *(skip; Build Kit covers it)* | 675 | 675 |
| Additional structure / motion parts | — | 300 | 1,500 |
| Extra motors (5203 @ $41.24 disc.) | — | 165 (4) | 330 (8) |
| Servos / sensors / spares | 50 | 300 | 700 |
| Second control system (practice/spare bot) | — | — | 650 |
| Batteries + chargers | 92 (1 + 1) | 238 (3 + 2) | 440 (6 + 3) |
| Field perimeter | 160 (DIY) | 160 (DIY) | 740 (official am-0481b) |
| Soft tiles | 147 (18 official, half field) | 293 (36 official, full) | 293 (36 official, full) |
| Game set | 22 (preview pack + printed POLLEN) | 399 (partial) | 599 (full) |
| 3D printer + filament | — *(school / library / makerspace)* | 399 (A1 mini + 4 kg) | 900 (P1S + AMS + 10 kg) |
| Tools | 0 (school / borrowed) | 400 | 1,200 (+ pit setup) |
| Software / AI | 0 (all free tier) | 160 (Claude Pro × 8 mo) | 800 (Max 5× × 8 mo) |
| Travel (local / regional only) | 0 (carpool) | 800 | 800 |
| Branding / shirts / portfolio print | 60 | 300 | 800 |
| *Subtotal* | *2,436* | *6,744* | *13,282* |
| **+ shipping & sales tax (~10% of goods)** | **+184** | **+493** | **+1,000** |
| **TOTAL (first year, no Championship)** | **≈ $2,620** | **≈ $7,240** | **≈ $14,280** |
| *Contingent: FIRST Championship (fee + travel)* | *n/a* | *+$9,000 – $12,000* | *+$9,000 – $12,000* |
| **Recurring (year 2+, no Championship)** | **≈ $915** | **≈ $3,085** | **≈ $6,500** |

> **[JUDGMENT] Championship is deliberately below the line for all three tiers.** At **$3,000 fee + ~$6,000–9,000 travel**, Houston costs **more than a Tier B team's entire season** and roughly **4× a Tier A season**. It is not a tier; it is a separate fundraising event.

### 2.2 What each tier actually buys

| | Tier A | Tier B | Tier C |
|---|---|---|---|
| Legal, inspectable robot | ✅ | ✅ | ✅ |
| Reliable autonomous | ✅ *(software is free)* | ✅ | ✅ |
| Practice-space realism | half field, DIY walls | full official tiles, DIY walls | official field |
| Iteration speed | slow (order-and-wait) | fast (print same day) | fastest (print + machine) |
| Second robot for driver practice while you fix the first | ❌ | ❌ | ✅ |
| Spares depth to survive a mid-event failure | thin | adequate | deep |
| Free CAD / simulator / training / scouting data | ✅ **identical** | ✅ **identical** | ✅ **identical** |
| Competing for judged awards | ✅ **fully** | ✅ | ✅ |
| Competing for Inspire | ✅ **fully** | ✅ | ✅ |

> **[JUDGMENT] Note the last three rows.** Tier A and Tier C have *identical* access to the free digital toolchain and to the highest-value advancement points in the game. That is the entire thesis of [§8](#8-the-strategic-core-where-a-small-team-should-concentrate).

### 2.3 Three-year cost of ownership and cost per student (NEW in Rev 4)

**[JUDGMENT] The first-year number is misleading, in both directions.** Much of Tier B and C's year-1 spend is *capital* — a control system, a field, a printer, tools — which does not recur. Here is the honest three-year picture, assuming no Championship and no catastrophic loss:

| | Tier A | Tier B | Tier C |
|---|---|---|---|
| Year 1 | $2,620 | $7,240 | $14,280 |
| Year 2 | $915 | $3,085 | $6,500 |
| Year 3 | $915 | $3,085 | $6,500 |
| **3-year total** | **$4,450** | **$13,410** | **$27,280** |
| *of which one-time capital (Y1)* | *~$1,610* | *~$3,900* | *~$6,600* |
| **3-year cost per student, 5-student team** | **$890** | **$2,682** | **$5,456** |
| **3-year cost per student, 12-student team** | **$371** | **$1,118** | **$2,273** |

> **⚠️ [JUDGMENT — CORRECTION TO REV 3] Rev 3 said "the gap between Tier B and Tier C narrows every year you survive." That is half true and worth stating precisely.** The **absolute** gap halves — $7,040 in year 1, $3,500 in year 2. The **ratio** slightly widens — 1.97× in year 1, 2.17× in year 2. Both facts matter, but only one is actionable.
>
> **The actionable one: your second season is the cheap season, and the marginal cost of buying Tier C capability is $3,500, not $7,040.** In year 2 your control system, field, printer, tools and most structure already exist. A Tier A team entering year 2 has a **$915 floor** and *everything above it is discretionary*. That is the single best moment in a small team's life to run one focused fundraising campaign and buy the one thing that was actually limiting you — the third battery, the official tiles, the printer, the COTS chassis — rather than spreading money thin across a rookie shopping list.

> **[JUDGMENT] The cost-per-student row is the number to put in a sponsorship letter, not the total.** *"$890 per student over three years"* reads as a bargain to a local business. *"$4,450"* reads as a big ask. Both are the same Tier A team. It is also the number that makes the case to a school board: FTC at Tier A is cheaper per student per year than most varsity sports.

### 2.4 Sanity check against published third-party budgets

| Source | Rookie first-year estimate | Caveat |
|---|---|---|
| FIRST (official) | **~$1,800** | Registration + robot set only; excludes events, field, tools, travel |
| Colorado FIRST | ~$2,500 | |
| ORTOP (Oregon) | $3,800 – $5,500 | |
| GM0 | **~$4,000 startup + ~$2,500/yr recurring** | **⚠️ [FACT — NEW IN REV 4] GM0's breakdown uses a $295 registration** — that is pre-2025 pricing; it is $350 now. Its Expansion Hub line ($250) is also stale ($275). Treat GM0's total as a **floor**, not a current number. |

GM0's itemization, for comparison: registration $295 · competition costs $250–800 · game set $450/season · field $659 *("it will cost you additional money to replace every 2-3 years")* · control and communication set $265 · electronics set $282 · Expansion Hub $250 · goBILDA starter kit $600 with discount · sensors and servos ~$500. It adds: *"Don't underpitch your budget needs!"* ([GM0 — Starting a Team](https://gm0.org/en/latest/docs/being-a-team/starting-a-team.html))

Sources: [FIRST Get Started](https://www.firstinspires.org/programs/ftc/get-started), [Colorado FIRST](https://coloradofirst.org/ftc/), [ORTOP](https://ortop.org/programs/ftc/), [GM0](https://gm0.org/en/latest/docs/being-a-team/starting-a-team.html)

> **[JUDGMENT] My Tier A ($2,620) sits between FIRST's $1,800 and Colorado's $2,500**, and it is achievable — but only because it assumes DIY perimeter, half field, borrowed tools, no printer, no travel, no AI spend, and a cheap region. Every one of those is a constraint you will feel. **Treat Tier A as the floor you can survive on, not the plan.** Tier B (~$7,240) is the honest number for a team that intends to advance.

**Note on Chief Delphi budget threads [FACT + CAUTION]:** Chief Delphi's "Team Budget Per Season" threads quote $7,000–$15,000 minimums with "$5,000–$6,000 for registration." **Those are FRC numbers, not FTC** — FRC registration is $6,500 versus FTC's $350, confirmed on the same FIRST cost page. Do not import them. ([CD thread](https://www.chiefdelphi.com/t/team-budget-per-season/145475)) The one FTC-transferable line: teams cut costs by *carpooling, avoiding hotels, not over-ordering parts, treating parts well, and sourcing used parts from the community.*

---

## 3. What FIRST provides, and the grant landscape

### 3.1 The FIRST Storefront — the closest thing to a "kit of parts"

**[FACT] FTC has no free kit of parts.** Registration buys *access to a discounted storefront*, nothing physical.

> **⚠️ [FACT — MAJOR PROCESS CHANGE, NEW IN REV 4] Pitsco is no longer the FTC vendor.** For 2026-27, *"all FIRST Tech Challenge teams registering through the FIRST Dashboard will purchase their season registration and materials through the new FIRST Storefront."* The refreshed Dashboard launched **17 June 2026**; the new Storefront opened **mid-July 2026**. Teams managing multiple rosters can *"order for all teams at the same time."* Organizations that had PITSCO set up as a vendor must **add FIRST as a payor**. Rev 3's ordering instructions ("Pitsco storefront") were wrong. ([FIRST — Key Changes to Registration](https://community.firstinspires.org/key-changes-to-first-tech-challenge-registration-whats-new), [FTC PA Season Blast #1](https://www.ftcpenn.org/email-archive/22265))

| Step | Item | 2025-26 price *(storefront PDF)* | **2026-27 price** *(FIRST website)* |
|---|---|---|---|
| 1 | Season registration | $325 | **$350** |
| 2 | **Driver Kit** — REV Driver Hub ×1, FTC-legal gamepads ×2, FTC-legal webcam ×1 | $285 | **$295** |
| 3 | **Electronics / Control set** — REV Control Hub, Smart Robot Servo, switch cable + bracket, Color Sensor V3 + cable, Touch Sensor + cable, resistive grounding strap, Control Hub cable pack, M3×16 screws + nylocks | $325 | **$350** |
| 4 | **Build Kit** — **REV *or* TETRIX Competition Set** *(the TETRIX option is new/newly surfaced)* | $650 | **$660** |
| 5 | Game Set (optional) — AndyMark BIOBUZZ set, soft tiles, perimeter | — | see [§1.5](#15-the-field-and-its-substitutes) |
| | **Estimated total robot kit** | ~$1,260 | **~$1,305** |

**[FACT]** FIRST states the Storefront offers *"either a REV or TETRIX Competition set,"* with details in *"the REV and TETRIX Bill of Materials,"* plus *"an Electronics Modules and Sensors Set and a Control Communications Set."* **Limit one per item per registered team per season.**

> **⚠️ [FACT — DISCREPANCY, still open in Rev 4] The official Storefront PDF is stale.** As of 2026-08-22 the [FTC Storefront Kit & Price Options PDF](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf) is still **Revision 25-26.4, dated Feb 18, 2026**, and lists **2025-26 prices and the DECODE game set**. The [FIRST Cost & Registration page](https://www.firstinspires.org/robotics/ftc/cost-and-registration) lists the higher 2026-27 prices. **Budget from the website, not the PDF.**

> **[FACT — CRITICAL PROCESS NOTE, verbatim from the storefront PDF]:** *"If you are waiting for a grant, please DO NOT check out until after that grant has been awarded. FIRST will not be able to make changes to orders after checkout."* **Sequence your grant applications before your storefront order.**

### 3.2 The vendor discount stack — the highest-ROI paperwork in FTC

**⚠️ [FACT — NEW IN REV 4] Rev 3 listed only goBILDA. There are at least four separate discounts, and they cover different, largely non-overlapping parts of the robot.**

| Vendor | Discount | What it covers | Terms / expiry | How to get it |
|---|---|---|---|---|
| **goBILDA** | **25% off** | *"covers nearly every product storewide,"* a few unspecified exclusions | **"for the life of the team"**; **$50 flat-rate international shipping** for FTC team accounts; no published domestic free-shipping threshold | Create a team account → FIRST Team Discount form → confirmation *"typically within one business day."* [gobilda.com/ftc](https://www.gobilda.com/ftc/) |
| **REV Robotics** ⭐ *new* | **15% off select items** | Structure (15mm extrusion, 45mm U-channel, flat plate), motion (DUO traction/omni wheels, hex shaft, chain turnbuckle), hardware (M3 nuts, wrenches), accessories (gamepad $26.00, Color Sensor V3 $20.75, Driver Hub battery $21.75). **NOT the Control Hub, Expansion Hub, or 12V batteries.** | *"Discount codes expire May 31, 2027"* | *"Log in to your FIRST Dashboard and check for your unique Discount Code,"* or fill in REV's Team Registration Form. [revrobotics.com/ftc/discounts](https://www.revrobotics.com/ftc/discounts/) |
| **Studica Robotics** ⭐ *new* | **25% claimed** for all *FIRST* teams, on most kits and parts | *"some exclusions may apply"*; applications *"subject for review"* | **[UNVERIFIED]** — the application page returned HTTP 403 to automated fetch. **Open it in a browser and confirm before relying on it.** | [studica.com/studica-robotics-team-discount](https://www.studica.com/studica-robotics-team-discount) |
| **FIRST Storefront** | Discounted control system, electronics, build kit | See [§3.1](#31-the-first-storefront--the-closest-thing-to-a-kit-of-parts) | 1 purchase per item per season | FIRST Dashboard → Storefront |
| **PTC / Onshape** | **100% off** CAD | See [§1.7](#17-software-and-digital-tooling--the-0-column) | Free to all FIRST teams, always | [PTC FIRST student downloads](https://www.ptc.com/en/education/student/first) |
| *AndyMark Product Donation Voucher* | *$450 / $125* | **Not applicable to FTC** — the PDV is an **FRC** Kickoff Kit opt-out credit, redeemed from a lead mentor's TIMS account | — | [andymark.com/pages/pdv](https://andymark.com/pages/pdv) |

> **[JUDGMENT] Do all three vendor forms this week. Total effort ≈ 45 minutes. Total value ≈ $700–900 in year 1 and every year after.** On a Tier B parts spend the goBILDA 25% alone is **~$600/yr, forever**. The REV 15% is smaller but it is free and it stacks on a different product set — REV is where your extrusion, wheels and spare gamepads come from, and 15% off those is real money you are otherwise leaving on the table.

> **[JUDGMENT] The discount structure quietly tells you which vendor to standardize on.** goBILDA discounts *everything* including motors and servos; REV discounts structure and accessories but **not** the control system or batteries. If you standardize actuators on goBILDA and structure on whichever is cheaper post-discount, you capture both. What you must not do is assume "REV team discount" means the Control Hub is cheaper — it is not, and the Storefront set at $350 remains the cheapest legal route to a Control Hub.

### 3.3 Grants — named programs, real numbers

| Program | Sponsor | Amount | Eligibility | Deadline (last known) | URL |
|---|---|---|---|---|---|
| **FTC Hardship Grant** | FIRST HQ | **$350** to storefront (registration + storefront products only) | Rookie & veteran teams in US/Mexico/Canada with financial barriers; **must be nominated by your region's PDP** | 09/30/2025 (25-26 cycle); **26-27 expected similar** | [FIRST Team Grants](https://www.firstinspires.org/programs/team-grant-opportunities) |
| **FTC SIM Argosy Rookie Team Grant** | Argosy Foundation via FTC SIM | **$1,000**, one-time, via HCB — **usable only for FTC season registration and products** | **North American rookie teams only**, who have **not already paid registration**; both Lead Mentors screened. Not combinable with the FIRST need-based rookie grant | 10/31/2025 (25-26); **26-27 TBA** | [FIRST Team Grants](https://www.firstinspires.org/programs/team-grant-opportunities), [FIRST WI announcement](https://www.firstinspireswi.org/post/ftc-sim-argosy-rookie-grant-now-open) |
| **Boeing FTC Grant** | Boeing | not published | Teams with a Boeing employee mentor; rookie & veteran | 10/03/2025 (25-26); 26-27 TBA | [FIRST Team Grants](https://www.firstinspires.org/programs/team-grant-opportunities) |
| **John Deere FTC Grant** | John Deere | varies by need | Teams in John Deere communities or with a John Deere employee mentor | 09/27/2025 (25-26); 26-27 TBA | [FIRST Team Grants](https://www.firstinspires.org/programs/team-grant-opportunities) |
| **BAE Systems FTC Grant** ⭐ *new in Rev 4* | BAE Systems | not published | Teams **within 75 miles of a BAE site**, or with a BAE employee mentor | **07/08/2026** *(2026-27 cycle — passed)* | [FIRST Team Grants](https://www.firstinspires.org/programs/team-grant-opportunities) |
| **Dow FLL & FTC Grant** | Dow | not published | Dow employee mentor and/or team in a Dow community (US/Canada) | **06/30/2026** *(2026-27 cycle — passed)* | [Submittable](https://usfirst.submittable.com/submit/7ef618be-1d7f-4d06-b588-19b0583b33aa/2026-2027-dow-first-fll-ftc-grant-application) |
| **Arconic Foundation Grant** | Arconic | **$750** | Rookie & veteran in specified counties (PA, TN, NY, GA, AR, IA, IL) | 10/31/2025 (25-26); 26-27 TBA | [FIRST Team Grants](https://www.firstinspires.org/programs/team-grant-opportunities), [ftcpenn.org](https://www.ftcpenn.org/team-grants) |
| **Gene Haas Foundation Student Competition Teams Grant** | Gene Haas Foundation | **stated preference $500–$2,500 per student** | Public school, or private school / team with **501(c)(3)**; project must involve **CNC machining**. Cannot buy Haas products. | **Opens after 1 May 2026; due 1 Sept 2026** — **10 days away** | [ghaasfoundation.org/apply-now](https://www.ghaasfoundation.org/apply-now) |
| **Digital Citizen Fund Grant** | DCF | **up to five × $5,000** | US-based **rookie** teams, all- or majority-female | 06/01/2026 for 26-27 *(passed)* | via [FIRST Team Grants](https://www.firstinspires.org/programs/team-grant-opportunities) |
| **Google.org Grant (via PA FIRST)** | Google.org | **$4,000 + up to $1,200 PD** (initial); **$1,500 + up to $600** (renewal) | ≥50% middle-school students AND diversity/underserved criteria | 25-26 closed; 26-27 TBA | [ftcpenn.org](https://www.ftcpenn.org/team-grants) |
| **Google Team Support Grant (Georgia)** | Google via GeorgiaFIRST | not published | Rookie or veteran; **must include middle-school-age students**; priority to under-resourced/underrepresented | **2026-27 cycle open** | [gafirst.org/ftc](https://gafirst.org/ftc) |
| **Panasonic Foundation Grant (SoCal)** | Panasonic | **$300** × 40 teams — league meet registration | SoCal FTC teams | **30 Sept 2026** | [socalftc.org/grants](https://socalftc.org/grants/) |
| **NASA KSC FTC Rookie Team Grant** | NASA Kennedy Space Center | equipment + partial registration | New teams in Brevard, Volusia, Orange or Seminole County FL | see site | [public.ksc.nasa.gov](https://public.ksc.nasa.gov/kscsma/first-tech-challenge-ftc-grants/) |
| **DonorsChoose + 3M** | 3M | project-based, **materials only — NOT registration** | Educators at public / charter / Head Start / BIE schools | rolling | [socalftc.org/grants](https://socalftc.org/grants/) |
| **PA Dept. of Education Grant** | PA DoE | **$1,000–$1,500 per FTC team** | Philadelphia public-school FTC teams | 26-27 TBA | [ftcpenn.org](https://www.ftcpenn.org/team-grants) |
| *California Argosy Foundation Grant* | *Argosy* | *$3,000 unrestricted* | **⚠️ FRC rookie teams only — not FTC.** Final date to apply 11 Sept 2026 | — | [cafirst.org/grants](https://cafirst.org/grants/) |
| Master list — **check weekly** | FIRST | — | — | rolling | [firstinspires.org/programs/team-grant-opportunities](https://www.firstinspires.org/programs/team-grant-opportunities) |

> **⚠️ [FACT — CONFIRMED AGAIN IN REV 4] As of 2026-08-22 the FIRST national grants page still shows NO open 2026-27 FTC grants that a team could apply to today.** The only two 2026-27-labelled FTC listings (Dow, 06/30/2026; BAE Systems, 07/08/2026) have already closed. Everything else on the page is a 2025-26 cycle. The page says *"Check back frequently for new or modified opportunities"* and *"New grant opportunities will be posted throughout the year."*

> **[JUDGMENT] The national 2026-27 window has not opened. Set a weekly recurring reminder on that page from now through December.** Argosy ($1,000), Boeing, John Deere and Arconic all opened between August and December last cycle. Argosy specifically requires that you have **not yet paid registration** — so *checking that page is worth $1,000 and checking it late is worth $0.*

> **[JUDGMENT] Priority order for a small team, by probability × amount ÷ effort:**
> 1. **FTC SIM Argosy Rookie Grant ($1,000)** — if you are a rookie, the single largest easy grant, and **forfeited the moment you pay registration**. Check whether the 26-27 cycle is open *before you register.* Highest-urgency item on this page.
> 2. **Your PDP's hardship-grant nomination ($350)** — literally your registration back, for one email. Chronically under-claimed because teams don't know to ask.
> 3. **Gene Haas ($500–$2,500/student)** — huge, but **due 1 Sept 2026, ten days away**, and needs 501(c)(3) or public-school status plus a CNC-machining nexus. If you have a school sponsor, scramble this week. If not, note it for next year and fix your tax status in the off-season ([§3.4](#34-becoming-tax-deductible-the-unlock-for-real-sponsorship)).
> 4. **Your regional PDP's own page** — PA, SoCal, Georgia, California and Florida all run programs invisible from the national list. Find yours and read it end to end. **Check whether your region's grant is FTC or FRC before you spend an evening on it** — California's Argosy grant is FRC-only, and it is easy to misread.
> 5. **DonorsChoose** if your coach is a public-school teacher — close to free money for materials, chronically underused by robotics teams.

### 3.4 Becoming tax-deductible: the unlock for real sponsorship

**[FACT] Most corporate giving programs, and several grants above (notably Gene Haas), require the recipient to be a 501(c)(3) or a public school.** Four real paths:

| Path | First-year cost | Ongoing | Time to status | Notes |
|---|---|---|---|---|
| **Ride your school's existing status** | **$0** | $0 | immediate | Simplest by far. Donations go to a school activity account. **Cost: you don't control the money, and purchases go through district procurement** — and you now also need the **financial guarantor** setup ([§1.9](#19-the-invisible-lines-shipping-tax-and-organizational-overhead)). |
| **Parent Booster USA group exemption** | **$575** (excl. state filing fees) | **$450/yr renewal** | Immediate on approval — **no IRS Form 1023, no IRS filing fee** | 501(c)(3) under PBUSA's group exemption ruling. Status maintained only while you stay a paying member. Early-bird discount typically Sept 1 – Dec 31; memberships renew Jan 1. ([PBUSA pricing](https://parentbooster.org/pricing), [group exemption letter](https://parentbooster.org/resources/group-exemption-letter)) |
| **File your own IRS Form 1023-EZ** | **$275 IRS user fee** + state incorporation fees | annual Form 990-N | weeks to months | Available only to organizations projecting **under $50,000/year** revenue — which describes essentially every FTC team. Paid at pay.gov; the IRS does not process until the fee clears. ([IRS FAQ](https://www.irs.gov/charities-non-profits/frequently-asked-questions-about-form-1023)) |
| **Fiscal sponsorship** by an existing 501(c)(3) | typically **a % cut of donations** | ongoing % | fast | An umbrella nonprofit holds your funds and issues receipts. FIRST names **4-H, Boys and Girls Clubs, and Hack Club Bank** as options. ([Chief Delphi discussion](https://www.chiefdelphi.com/t/501c3-organizations-first-and-robotics-teams/473881)) |

> **[JUDGMENT] If you are school-affiliated, use the school's status and stop reading this section — you are done for $0.** If you are an independent community team, **1023-EZ at $275 is the cheapest permanent answer**; PBUSA at $575/$450 is the cheapest *fast and administratively supported* answer. Decision rule: if you expect to raise **more than about $1,500/yr from businesses**, the tax-deductible receipt pays for itself immediately, because "we can give you a receipt" converts a meaningful fraction of maybes into yeses. If less, skip it and take in-kind donations instead ([§6.2](#62-the-in-kind-ask-is-the-small-teams-superpower)) — **in-kind gifts do not require you to be a 501(c)(3) for the donor to treat it as a business expense.**

### 3.5 The StarterBot path — the cheapest way to own a working robot in week 2 (NEW in Rev 4)

**[FACT]** For 2026-27, **four vendors — AndyMark, goBILDA, REV Robotics and Studica — each publish a StarterBot.** Each has already released a **StarterBot *Base*** (*"a drivetrain and intake which will be used as part of the full StarterBot builds"*), with the **complete StarterBot released at Kickoff, 12 September 2026**. ([FIRST — Game Preview 2027](https://community.firstinspires.org/game-preview-field-elements))

**[FACT] The 2026-27 StarterBot Base is a drop-center 6WD chassis with a GripForce Gecko wheel intake.** goBILDA's resource guide bundles: assembly instructions (PDF), **example code (ZIP)**, STEP files, an interactive 3D model, and schematics. It requires the **2026-27 goBILDA FTC Starter Kit ($899.99 list / ~$675 discounted) plus a REV Hub**, or the **$249.99 Upgrade Pack** if you own last year's kit. ([goBILDA StarterBot Base Resource Guide](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/))

**[FACT] The guides are explicitly training tools, not a competition answer:** *"It is not a guide to build an official competition robot for the 2026-27 BIOBUZZ season, but a training tool to help teams enter the season with stronger fundamentals."* ([Studica StarterBot guide](https://www.studica.com/blog/ftc-starter-bot-build-guide-2026-2027/))

**[FACT — RULES] R301 explicitly permits StarterBot mechanisms.** R301 prohibits COTS MAJOR MECHANISMS purpose-built to complete a game task, **with explicit exceptions for "COTS drive CHASSIS" and for StarterBot mechanisms.** (`sections/12_RobotConstruction_R_p64-88.txt`, R301)

> **[JUDGMENT] For a 3–5 student team this is the single most underrated schedule decision available.** The classic small-team failure is spending September and October building a chassis that does not work, arriving at a December qualifier with an untested robot, and never getting driver practice. The StarterBot path inverts that: **you have a driving, intaking robot in week 2**, which means driver practice, autonomous development, and mechanism iteration all start in October instead of January.
>
> The counter-argument is real: judges want *your* engineering, and "we built the StarterBot" is not a Design Award story. **The resolution is the same as for a COTS chassis ([§5.2](#52-the-three-false-economies)): document the build-vs-buy trade study, then document every modification you made to the StarterBot and why.** R302 lets you cut, drill and modify legal COTS parts freely. A StarterBot base that you measurably improved, with data, is better Design Award content than a mediocre original chassis you ran out of time to test.
>
> **Practical shape:** build the StarterBot Base *now*, before kickoff, from whichever vendor kit you own. On 12 September, throw away the game-specific half and keep the drivetrain. You will have spent the pre-season learning your own toolchain on a robot that works.

---

## 4. Where cheap parts actually come from

### 4.1 The used and donated market — thin, but real

**[FACT — RULES CHECK] Used parts are legal.** The V0 R-rules define COTS as a standard part commonly available from a VENDOR, and state that parts *"functionally equivalent to the original condition as delivered from the VENDOR are considered COTS."* A second-hand goBILDA channel or a three-year-old Control Hub is still a COTS item. (`sections/12_RobotConstruction_R_p64-88.txt`, §12 preamble)

**[FACT — RULES CHECK] Other teams may legally give you parts and labor.** R101 requires the ROBOT and its MAJOR MECHANISMS be built by your team, but explicitly says the rule *"is not intended to prohibit or discourage assistance from other teams (e.g., fabricating elements, supporting construction, writing software, developing game strategy, contributing COMPONENTS, and/or MECHANISMS)."* (same file, R101)

> **[JUDGMENT] Read R101 again — it is the single most under-exploited sentence in the manual for a resource-poor team.** FIRST has written down, in the construction rules, that another team may machine your parts, help you build, write software with you, and *hand you components and mechanisms*. What you may not do is have an outside organization deliver a complete purpose-built solution. That leaves an enormous legal space: a veteran team in your league can water-jet your side plates, and it is not a rules problem. **Ask.**

| Channel | Typical yield | Effort | Notes / source |
|---|---|---|---|
| **Your PDP / regional partner** | Highest — folded teams donate whole inventories | One email | Regional partners often know which teams disbanded and hold or broker their parts. **[JUDGMENT] Start here.** |
| **A veteran team in your league** | Parts, machining, mentoring, field time | One conversation | Legal per R101. Also generates Connect/Motivate portfolio content. |
| **Chief Delphi** | Occasional control-system and structure lots | Moderate — watch threads | [Buying used FTC control systems](https://www.chiefdelphi.com/t/buying-used-ftc-control-systems/518828), [FRC/FTC Marketplace](https://www.chiefdelphi.com/t/frc-ftc-marketplace/480331) |
| **FTC Forum "teams helping teams"** | Occasional | Low | [FTC Forum thread](https://ftcforum.firstinspires.org/forum/first-tech-challenge-community-forum-this-is-an-open-forum/teams-helping-teams-programming/82095-where-can-i-buy-used-robot-parts) |
| **eBay** | Motors, hubs, structure — no robotics-specific search | High (sifting) | **Verify R501 legality of any actuator before buying** — see [§5.4](#54-cost-cuts-that-are-actually-rules-violations-new-in-rev-4). |
| **AndyMark Sale & Clearance** | Discontinued SKUs at a discount | Low | [andymark.com/collections/sale-clearance](https://andymark.com/collections/sale-clearance) — check R501 legality; Table 12-1 marks some motors *"Discontinued"* but still legal |
| **BotSwapShop.com** | **Likely defunct** | — | **[FACT] `https://botswapshop.com` fails to load: "certificate has expired"** (checked 2026-08-21). Do not plan around it. |
| **School / district surplus** | Tools, benches, storage, a drill press | Low | Ask facilities and the CTE/shop teacher, not just your principal. |

> **[JUDGMENT] What to buy used, and what never to buy used:**
>
> | Buy used without hesitation | Buy used carefully | **Never buy used** |
> |---|---|---|
> | Structure (channel, plates, brackets), shafts, spacers, hardware, hubs, gears, sprockets, chain, tools, field tiles, perimeter | Motors (check gearbox slop and encoder function), servos (check for dead spots), Driver Hub, gamepads | **Batteries.** **Anything whose failure mid-match costs you a match.** |
>
> Structure is inert: it has no wear-out mode you can't see. Batteries are a consumable with an invisible state of health and a hard rules constraint (R601). The line between the two columns is *"can I inspect it in five minutes?"*

### 4.2 Borrowing a field instead of owning one

**[FACT]** The Mentor Manual lists **scrimmages, workshops and practice days** as unofficial event types, *"usually held early in the season to practice against real competitors with the season's new game,"* *"often conducted by local Affiliate Partners or experienced teams,"* and notes that *"if a practice day is held in a team's area, it is a good opportunity to obtain assistance from veteran teams and mentors, especially if the team is facing significant challenges."* ([FTC Mentor Manual](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-mentor-manual.pdf))

| Field access option | Cost | Realism | [JUDGMENT] Use it for |
|---|---|---|---|
| Own official field (perimeter + 36 tiles + full game set) | **~$1,632** | 100% | Nothing a small team needs before December |
| Own DIY perimeter + 18 official tiles + partial set | **~$706** | ~80% | Everything except final wall-interaction tuning |
| Official tiles only, taped field lines, no walls | **~$293** | ~55% | Drivetrain tuning, odometry, cycle-path practice |
| Generic ½" tiles only | **~$180** | ~45% | Programming bench, pit floor — **not** drivetrain tuning ([§1.5](#15-the-field-and-its-substitutes)) |
| **Borrowed field at a veteran team / league host** | **$0 + fuel** | 100% | The 2–3 sessions before your first event that actually matter |
| **Scrimmage / practice day** | **$0–$50** | 100% + real opponents | Defense, alliance behaviour, pit-crew rehearsal |
| **FTC SIM** ([ftcsim.org](https://ftcsim.org/)) | **$0** | Autonomous logic only; **DECODE field only as of Aug 2026** | September, before the robot exists |

> **[JUDGMENT] The single highest-value $0 line in this entire document is "ask another team in your league if you can practice on their field for two hours."** It is worth more than any $700 purchase, it is available to you today, it costs a text message, and it simultaneously generates Connect-award content. Small teams systematically fail to ask because asking feels like an imposition. It is not — FTC's entire culture is built on the opposite assumption, and the Mentor Manual says so in writing.

### 4.3 Print instead of buy, and what not to print

| Print it | Buy it | Have it machined (in-kind) |
|---|---|---|
| Brackets, mounts, spacers, standoffs, cable guides, sensor housings, gamepad/battery mounts, intake rollers and compliant surfaces, prototype geometry, portfolio props, pit organizers, **game-element replicas before the real ones ship** | Anything rotating under load at speed, anything carrying drivetrain torque, gears, bearings, shafts, wheels, structure that defines chassis squareness | Flat load-bearing plates, side plates, anything you would otherwise buy as an expensive custom part — this is the **best in-kind ask** ([§6.2](#62-the-in-kind-ask-is-the-small-teams-superpower)) |

> **[JUDGMENT] The printer's real payoff is schedule, not dollars.** At $299 for an A1 mini and ~$25/kg of PLA, the cash saving on any single bracket is a few dollars. The saving that matters is **the 5–10 days you don't spend waiting for an order**, multiplied across a season. Six design iterations beat two, and iteration count is the one competitive variable a small team can actually max out.

> **[JUDGMENT] Print the game elements.** With the AndyMark pre-order wave closed (7 Aug 2026) and orders filled in the sequence received, printed POLLEN is likely your only September practice element. Buy the **$5.50 Game Preview Pack (am-5851_preview)** as your dimensional ground truth — 2.8" ± 0.1", 0.055 lb — and iterate printed copies against it. **Mass and surface friction are what your intake actually cares about**; a printed shell that matches diameter but weighs half as much will teach your intake the wrong lesson. **Weigh your prints and add ballast until they match 0.055 lb.**

---

## 5. Cost-cutting, ranked by damage

### 5.1 Cost cuts ranked by savings-per-unit-of-performance-lost

**Rank 1 = free money. Rank 16 = the last thing you should cut.** Savings are first-year, Tier B baseline, USD as of Aug 2026.

| # | Cut | Saves | Performance cost | Verdict |
|---|---|---|---|---|
| **1** | **goBILDA 25% FTC team discount** | **~$600/yr, forever** | **Zero** | Do it today. 15 minutes. No downside exists. |
| **2** | **REV 15% + Studica 25% team discounts** ⭐ *new* | **~$100–250/yr** on structure, wheels, accessories | **Zero** | Two more forms, ~30 min total. Rev 3 missed these entirely. |
| **3** | **Free software stack** — Onshape, PTC, Skill Builders, StarterBot guides, FTC SIM, GM0, ftcscout | **$0 vs. thousands** | **Zero — identical to what a rich team uses** | Already free. The cut is *not buying paid alternatives.* |
| **4** | **Ask your PDP to nominate you for the Hardship Grant** | **$350** | Zero | One email. Registration back. |
| **5** | **Borrow field time instead of owning a field** | **$0 spent; up to $1,632 avoided** | Slightly less volume practice | Highest-value ask in FTC. |
| **6** | **DIY perimeter + half field instead of official field** | **~$726** | Small: wall bounce/friction differ; matters more in a ball game | Mitigate with 2 real-field sessions pre-event. |
| **7** | **Servo-first mechanism architecture to stay on one Hub** | **$275 + $14/actuator** | Zero if the mechanism suits a servo; large if you force it | A CAD decision, not a purchasing decision. |
| **8** | **Standardize on one motor + one servo family** | **~$150–300/yr in spares**, plus inventory sanity | **Negative cost — it improves reliability** | Mixing families to save $8/part doubles your spares bill. |
| **9** | **StarterBot Base instead of an original chassis** ⭐ *new* | ~$0 cash; **30–60 student-hours** | Design-story risk only, and only if undocumented | See [§3.5](#35-the-starterbot-path--the-cheapest-way-to-own-a-working-robot-in-week-2-new-in-rev-4). Buys schedule, which a small team needs more than cash. |
| **10** | **Reuse your own prior-season drivetrain** | **~$400–600** | Zero on the field; small judging risk | See the rules note below. |
| **11** | **Print instead of buying custom brackets** | **~$100–300/yr + weeks of schedule** | Zero for non-load parts | The schedule saving dominates. |
| **12** | **Buy structure and tools used; take in-kind machining** | **~$200–500** | Zero if inspectable | Never batteries. |
| **13** | **Carpool, no hotels, drive to the nearest events** | **$800–1,800/event weekend** | Zero on robot; some fatigue cost | Chief Delphi's teams name this as their #1 cut. |
| **14** | **Skip the second Expansion Hub, skip a second robot** | **$275 / $650+** | Real but survivable: no parallel driver practice | Tier C luxuries, not Tier B needs. |
| **15** | **Buy spares by failure probability, not by category** | **~$200–400 of wrong spares avoided** | Zero if you pick right; catastrophic if you pick wrong | See the spares table below. |
| **16** | **Cut battery count, control system quality, or drivetrain quality** | $50–350 | **Match-losing** | **DO NOT. See [§5.2](#52-the-three-false-economies).** |
| **✗** | **Generic ½" foam tiles for the main practice area** | $113 | **Wrong ride height, wrong compression** | Use them for the pit floor and programming bench, not where the robot is tuned. |
| **✗✗** | **20V chassis kits, non-listed motors, wrong servos** | $100–300 | **You fail inspection and do not compete** | **Not a cut. See [§5.4](#54-cost-cuts-that-are-actually-rules-violations-new-in-rev-4).** |

**Rules note on #10 [FACT + CAUTION].** A keyword search of the full V0 manual text (`manuals/2026-27_BIOBUZZ/v0_pymupdf.txt`) for "previous season", "prior season", "past season" and "last season" returns **no rule prohibiting reuse of a robot or mechanism your own team built in a prior season**; R101 requires only that the ROBOT and its MAJOR MECHANISMS *"were built by the FIRST Tech Challenge team that has registered for the event."* **But** A201.E requires the PORTFOLIO to *"only include progress, challenges, and accomplishments which have taken place since January 1, 2026,"* and judges are *"strictly instructed to only consider information from the current event and the current season."*

> **[JUDGMENT] So: reuse the hardware, but you get no judging credit for last year's design work.** If you reuse a drivetrain, document the *2026-27 decision to reuse it* — the evaluation, the modifications, the trade study that justified it. That is current-season engineering and it is exactly what the Design Award rewards.

**Spares triage [JUDGMENT]** — what actually fails at an FTC event, ranked:

| Buy spares of | Why | Approx. cost |
|---|---|---|
| **Fuses (20A ATM)** | Blow silently; a $1 part disables the robot. REV: *"12V Slim Battery fuses are common 20A fuses that can be purchased in auto stores or online."* ([REV battery docs](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/12v-battery-best-practices-and-troubleshooting)) | **<$10 for a pack** |
| **Motor/encoder cables, servo cables, XT30 pigtails** | Highest-frequency failure. Flex, vibration, pinch. | **$30–50** |
| **One spare motor, one spare servo** *(of your standard family)* | Covers every position on the robot because you standardized | **~$70 discounted** |
| **Zip ties, Loctite, heat shrink, electrical tape** | Consumed constantly | **$25** |
| **A spare gamepad** | REV PS4-compatible gamepad **$26.00** in the 15% discount category; a dead gamepad in queue is a lost match | **$26** |
| Wheels / tread | Wear is visible and predictable — buy when worn, not in advance | $0 pre-event |
| **A whole spare Control Hub** | ~$350 sitting idle. **[JUDGMENT] Not for a Tier A/B team** — borrow from a neighbouring team if yours dies; that is exactly what pits are for. | skip |

### 5.2 The three false economies

#### False economy #1 — batteries

**[FACT] The rules already prevent you from buying junk.** R601 limits you to **exactly one** main battery on the ROBOT, from a closed list of four approved packs. There is no legal cheap generic option. (`sections/12_RobotConstruction_R_p64-88.txt`, R601)

**So the false economy isn't buying a bad battery — it's owning too few, and running them too long.**

| Verified fact | Source |
|---|---|
| *"Discharging the battery past 9.0V can reduce the lifespan of the battery and can permanently damage the cells,"* though *"periodic dips below 9.0V when under load is expected and okay."* | [REV 12V Battery Best Practices](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/12v-battery-best-practices-and-troubleshooting) |
| A brownout indicator is *"the voltage on the Driver Station showing 9 volts or lower when running code."* | [REV Control Hub Troubleshooting](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting) |
| *"All rechargeable batteries have a finite lifespan"*; replace when the pack *"isn't holding a charge as well as it used to."* | [REV 12V Slim Battery](https://www.revrobotics.com/rev-31-1302/) |
| Manual charging rule: *"Never charge batteries on a battery charger that exceeds a 3-amp average channel current"*; charge only via the battery's own connector, **never alligator clips.** | `sections/12_RobotConstruction_R_p64-88.txt` |
| AndyMark advises cycling a new Flat Pack **3–5 times** to reach peak performance. | [AndyMark am-5290](https://andymark.com/products/am-flat-pack-battery) |

> **[JUDGMENT] Three batteries and a dual-port charger is the correct floor — roughly $319.** The arithmetic: at a qualifier you may play 5–7 qualification matches plus playoffs across ~6 hours. A 3000 mAh pack that has been through inspection, a practice match and two qual matches is not the same pack you started with. With one battery you are choosing between playing brown-out matches and scratching. With three you always have a rested, cooled, fully-charged pack.
>
> **[JUDGMENT] The RDX2's battery resistance meter is the sleeper buy.** Internal resistance is the only cheap way to tell a dying NiMH pack from a good one *before* it costs you a match. $154 for a 2-port charger that also diagnoses your packs beats two $36.50 chargers, and it removes the most common invisible failure in FTC. **[UNVERIFIED]** — confirm the RDX2's **per-channel average current complies with the manual's 3 A rule** before using it in the pit; the product page advertises 100 W per port, which is a power rating, not the average channel current the rule specifies.

> **[JUDGMENT] The cost of the false economy, quantified.** One brown-out in a qualification match costs roughly 1 of ~5 matches → several rank positions → several Qualification Phase Performance points (at a 28-team event: rank 1 = 16, rank 13 = 10, rank 28 = 4). It also costs you the pick. **A $110 second and third battery is cheaper than one lost match.**

#### False economy #2 — the control system

| Option | Cash | Hidden cost |
|---|---|---|
| **Storefront Electronics/Control set** ($350, includes a $375 Control Hub + other parts) | **$350** | None. Cheapest and best simultaneously. |
| Retail Control Hub | $375 | +$25 for less stuff. **The REV 15% team discount does not apply to it.** |
| **Phone + Expansion Hub** | ~$275 + a phone | **You own the entire Android compatibility surface**, and the manual states in writing that unsupported devices are the team's own responsibility to test and verify. No FTA support, no forum support, no REV support. |
| **Used Control Hub of unknown age** | $150–250? | Unknown firmware/eMMC history, no warranty, and you cannot inspect it. **[JUDGMENT] Acceptable only as a *spare*, never as your primary.** |

> **[JUDGMENT] The debugging-hours argument is the whole argument.** A 5-student team has maybe 500–1,000 student-hours in the season ([§7](#7-the-labor-budget)). Spending 40 of them on Wi-Fi Direct pairing failures is a 4–8% tax on your entire program to save $200. No cut in this document has a worse ratio.

#### False economy #3 — drivetrain quality

**[FACT] Alliances in FTC playoffs are two robots.** At the end of qualification, the top-ranked teams become ALLIANCE leads and *"each ALLIANCE lead chooses 1 other team to join their ALLIANCE."* The number of alliances scales with event size: **2 alliances at a 4–10 team event, 4 at 11–20, 6 at 21–40, 8 at 41–64.** (2025-26 DECODE Competition Manual §13.7.1–13.7.2, Table 13-2 — `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf`. **BIOBUZZ §13 is a placeholder until kickoff; re-check.**)

> **[JUDGMENT] Do that arithmetic.** At a 30-team qualifier, 6 alliances × 2 robots = **12 of 30 teams reach the playoffs (40%)**, and **your robot is 50% of your alliance's output.** In a 3-robot alliance you can hide behind partners. In a 2-robot alliance you cannot. That is why drivetrain quality is not a comfort purchase — it is the thing that determines whether anyone picks you.

**What "cheap drivetrain" actually costs:**

| Cheap choice | Failure mode | Competitive consequence |
|---|---|---|
| Unsupported / plain-bore wheels, no bearings | Binding, uneven drag, motor heat | Slow cycles, brownouts, dead motors |
| Flexible or non-square frame | Wheel scrub, drift, unrepeatable odometry | Autonomous doesn't repeat; you lose AUTO points every match |
| Mismatched motor family / wrong gear ratio | Stall, thermal shutdown, no pushing power | You get shoved off scoring positions and can't defend |
| Chain/belt without proper tensioning | Skipped teeth mid-match | Random, unfixable-in-90-seconds failures |

**COTS chassis is explicitly legal [FACT].** R301 prohibits COTS MAJOR MECHANISMS purpose-built to complete a game task, **with an explicit exception for "COTS drive CHASSIS, provided none of the individual parts violate any other rules"** and for StarterBot mechanisms. (`sections/12_RobotConstruction_R_p64-88.txt`, R301)

**Legal 12V COTS chassis options [FACT — goBILDA, Aug 2026]:**

| Chassis kit | SKU | List | With 25% team discount |
|---|---|---|---|
| **Bravo (Bare-Bones)** ⭐ *cheapest entry* | — | **$399.99** | **~$300** |
| Recon | 3209-0004-0001 | **$349.99** | **~$262** |
| Hammerhead | 3209-0003-0001 | **$449.99** | **~$337** |
| BeeLine V2 | 3209-0002-0002 | **$649.99** | **~$487** |
| Strafer (Ø104 mm GripForce mecanum) | 3209-0001-0007 | **$699.99** | **~$525** |
| Strafer (Ø140 mm mecanum) | 3209-0012-0002 | **$799.99** | **~$600** |
| Outlaw | 3209-0005-0001 | **$799.99** | **~$600** |
| Bravo (Grouser Paddles / Rubber Tread) | — | **$1,049.99** | **~$787** |

Source: [goBILDA Chassis Kits](https://www.gobilda.com/chassis-kits). **Prices as of Aug 2026 — re-check.**

> **⚠️ [FACT — NEW IN REV 4] The same page also sells 20V "Overlander" chassis kits at $539.99–$699.99. These are NOT FTC-legal.** See [§5.4](#54-cost-cuts-that-are-actually-rules-violations-new-in-rev-4).

> **[JUDGMENT] For a team with fewer than ~6 students, buying a COTS chassis is not cheating and not a cop-out — it is correct resource allocation.** R301 makes it legal. It converts 30–60 student-hours of chassis fabrication and debugging into 30–60 hours on the mechanism that actually scores, which is where your differentiation lives. The counter-argument is real: judges for the Design Award want evidence of *your* engineering. **The resolution is to document the trade study** — why a COTS chassis, what you evaluated, what you modified (R302 lets you drill, cut and modify legal COTS parts freely), and what you spent the reclaimed hours on. A well-argued build-vs-buy decision is *better* Design Award content than a mediocre home-built chassis.

### 5.3 Dollars per advancement point

**[FACT — LOCAL SOURCE, V0 §4.1, Table 4-1]** (`sections/04_Advancement_p27-32.txt`):

| Source of points | Points |
|---|---|
| Qualification Phase Performance | **2 – 16** (inverse-error-function normal distribution across ranks, α = 1.07) |
| ALLIANCE lead | **21 − ALLIANCE lead number** (ALLIANCE #1 = 20, #3 = 18) |
| Draft Order Acceptance | **21 − draft position** (3rd draft position = 18) |
| Playoff: Winners / Finalists / 3rd / 4th | **40 / 20 / 10 / 5** |
| **Inspire Award 1st / 2nd / 3rd** | **60 / 30 / 15** |
| All other 1st / 2nd / 3rd place awards | **12 / 6 / 3** |

**Tiebreakers, in order (Table 4-2):** total advancement points → **Judged Team Award points** → playoff advancement → alliance selection results → qualification phase performance → **average qualification match points (excl. fouls)** → **average qualification AUTO points** → highest individual match → second-highest → random.

**[JUDGMENT] Cost per advancement point — the most important table in this document:**

| Investment | Cost | Realistic points it buys | **$/point** |
|---|---|---|---|
| **A 15-page portfolio + rehearsed 5-minute interview** | **~$20 printing + ~60 student-hours** | Inspire 1st = **60**; a single non-Inspire 1st = **12** | **$0.33 – $1.67** |
| Two more judged-award categories prepared (e.g. Connect + Control) | ~30 student-hours | **12–24** | **~$0** |
| Third battery + dual-port charger | $265 | Maybe **2–5** (avoided brownout → rank) | **~$50–130** |
| Reliable drivetrain upgrade (COTS chassis, cheapest legal) | ~$300 | **5–20** (rank + getting picked) | **~$15–60** |
| Second Expansion Hub | $275 | 0–3 | **~$90+** |
| Official field instead of DIY | +$726 | 2–5 | **~$145–360** |
| Second complete robot | ~$1,500 | 3–8 | **~$190–500** |
| FIRST Championship attendance | ~$10,000 | 0 *(it is the destination, not a source)* | **∞** |

> **[JUDGMENT] The portfolio is the cheapest advancement point in FIRST Tech Challenge by two orders of magnitude, and it is the one line where a 4-student team competes on exactly equal footing with a 30-student team.** Inspire 1st (60 pts) is worth more than winning the event outright (40 pts). A team that wins the event as the #1 alliance lead from rank 1 collects 16 + 20 + 40 = **76**. A team that wins Inspire and finishes mid-pack collects 60 + ~10 = **70** — and beats the event winner on the *second* tiebreaker if it comes to that, because **Judged Team Award points sort above playoff points**. **You do not need to out-build anyone to advance. You need a good-enough robot and an excellent portfolio.**

> **[JUDGMENT] Note tiebreakers 7 and 8: average qualification match points, then average qualification AUTO points.** Both reward *consistency*, not peak. A robot that scores the same modest amount every match outranks a robot that scores double in two matches and zero in three. **Consistency is free; peak scoring is expensive.** This is the same conclusion the alliance-selection argument reaches by a different route.

### 5.4 Cost cuts that are actually rules violations (NEW in Rev 4)

**[JUDGMENT] These look like savings on a vendor page and end your season at the inspection table. Every one is a real product a real small team could plausibly buy this week.**

| Tempting purchase | Real price | Why it fails | Rule |
|---|---|---|---|
| **goBILDA 20V "Overlander" chassis kits** — Overlander-4 **$599.99**, Overlander-6 **$639.99–699.99**, Overlander-T **$629.99** | Looks **$100 cheaper** than a Strafer | **R501 Table 12-1 lists only 12V motors.** The legal list is: AndyMark NeveRest 12V (am-3104/b/c), goBILDA Yellow Jacket 520x 12V, goBILDA 5000 Series 12V, Modern Robotics/MATRIX 12V, NFR Yuksel 12V, REV HD Hex 12V (REV-41-1291), REV Core Hex 12V (REV-41-1300), Studica Maverick 12V (75001), SWYFT Spike, TETRIX MAX 12V, TETRIX TorqueNADO 12V, WATTOS Stingray 12V. **No 20V motor is on it.** | R501, `sections/12_RobotConstruction_R_p64-88.txt` |
| A cheap generic hobby servo off eBay | $8–15 vs $27.74 | **R502** caps servos at **8 W mechanical output @ 6V** (P ≈ 0.25 × stall torque N·m × no-load speed rad/s) and a stall-current limit. You must *"provide documentation verifying servo specifications"* if it isn't on the pre-approved list. | R502, Table 12-2 |
| A generic 12V NiMH pack that "looks the same" | $25 vs $55 | **R601** is a **closed list of four packs.** Nothing else is legal, at any price. | R601 |
| A cheap high-current charger | $20 vs $36.50 | **"Never charge batteries on a battery charger that exceeds a 3-amp average channel current."** Also: charge via the battery's own connector, **never alligator clips.** | §12 charging rule |
| A non-REV robot controller | any | **R701** allows only a REV Control Hub, or an Android phone + REV Expansion Hub. There is no third option. | R701 |
| A 9th motor or 9th servo | ~$41 | **R503** caps the ROBOT at **8 motors and 8 servos.** | R503 |

> **[JUDGMENT] The 20V chassis trap is the dangerous one, because it is on the *same vendor page* as the legal kits, from a vendor whose entire brand is FTC.** goBILDA sells to more than FTC. A student browsing `gobilda.com/chassis-kits` sees nine 12V kits and five 20V kits in one grid, sorted by price, and the cheapest complete-looking option in the whole grid is a 20V Overlander. **Write "12V ONLY — R501" on the top of your parts spreadsheet and check every actuator SKU against Table 12-1 before ordering.** R501 also notes that *"additional motors may be added to the legal motor list in future competition manual updates"* — so re-check after each Team Update, but never assume forward.

> **[JUDGMENT] One genuine flexibility hidden in R501 that is worth money:** *"Many legal gearmotors are sold with labeling based on the entire assembly. These motors may be used with or without the provided gearbox, and/or with any other compatible gearbox."* Combined with the verified **$54.99-across-all-ratios** finding ([§1.4](#14-starter-kits-structure-and-motion)), this means you may legally cannibalise gearboxes between motors you already own. A team with two wrong-ratio motors can sometimes make one right-ratio motor for $0.

---

## 6. Sponsorship and fundraising that actually works for a small team

Primary source: the **FIRST Robotics Competition Fundraising Guide, Rev. July 2026**, created by FRC Team 6328 *Mechanical Advantage* with FIRST HQ. It states it *"was created for FIRST Robotics Competition teams based in the United States but most of the content is also applicable to … FIRST Tech Challenge teams."* ([PDF](https://www.firstinspires.org/hubfs/web/program/frc/resources/fundraising-guide.pdf?hsLang=en)) **Ignore its dollar figures — they are FRC-scale ($33,000 sample budget). Use its mechanics.**

### 6.1 The numbers that decide where you spend your effort

| Fact | Number | Source |
|---|---|---|
| Cold-outreach positive response rate to companies that haven't approached you | **2–5%** — *"That will likely be higher among parent and mentor employers and previous sponsors."* | FIRST Fundraising Guide (Jul 2026) |
| Sponsorship tier structure recommended | **3–5 tiers**, e.g. *"$100-$499; $500-$999; $1,000-$1,999; $2,000+"* | same |
| Sponsorships and grants renewal | *"Sponsorships and grants generally do not automatically renew. You must reapply for funding each season."* | same |
| Sponsor retention | *"It's more efficient and effective to keep an existing sponsor year after year than find a new one."* | same |
| Who must not accept donations | *"Mentors and parents should not directly accept donations for a team, school, or nonprofit organization. Doing so can have personal tax implications in the U.S."* | same |

> **[JUDGMENT] A 2–5% cold response rate is the whole strategy in one number.** To land 3 sponsors cold you must contact roughly 60–150 businesses. A 5-student team cannot do that and also build a robot. **Therefore a small team must not run a cold campaign.** Run a *warm* campaign: parent and mentor employers, previous sponsors, and businesses that already sponsor other youth groups in your town. The guide's own advice for finding those: *"What are the local business names on the back of the local youth sports league shirts? Who sponsors local PTA or PTO events? … Who advertises in the high school theater playbill?"* That is a list of 10–20 pre-qualified prospects, gettable in one evening, at maybe 20–30% conversion instead of 2–5%.

### 6.2 The in-kind ask is the small team's superpower

**[FACT]** The guide: *"A donation of money is not the only type of sponsorship available. Sometimes, a company may have an easier time donating goods or services instead of trying to free up money in their monthly cash flow."* Its own worked example is an in-kind ask: *"We are asking if your print shop would be willing to donate services to create and produce our team banners this year or maybe charge for materials only."*

**[JUDGMENT] Why in-kind beats cash for a team like yours:**

1. **It clears a lower approval bar.** A shop foreman can approve 40 minutes of water-jet time on scrap. A cash donation goes to whoever controls the budget.
2. **It does not require you to be a 501(c)(3).** A business donating goods or services out of inventory is generally handling a business expense, not a charitable deduction. **[JUDGMENT — not tax advice; the donor's accountant decides.]**
3. **It buys the thing you actually can't buy: capability.** $300 cash buys structure. 3 hours of a machinist's time buys parts you cannot make at all.
4. **It creates a relationship with an engineer**, which converts into a technical mentor — the scarcest resource in this document.

**The in-kind ask list, ranked by value to a small team [JUDGMENT]:**

| Ask | Typical donor | Cash-equivalent value | Also delivers |
|---|---|---|---|
| **Water-jet / laser / CNC time on flat plate** | Local machine shop, sign shop, fab shop | **$150–600/season** | Parts you literally cannot make — **and the CNC nexus Gene Haas requires** ([§3.3](#33-grants--named-programs-real-numbers)) |
| **A technical mentor for 2 h/week** | Any local engineering employer | **priceless** | Fills the mentor gap in [§7.6](#76-mentor-time-realities) |
| **Meeting/build space with power and a workbench** | Library, church, makerspace, employer | **$500–2,000/season** | Removes the "we meet in a garage" ceiling |
| **3D printer access** | School library, public library, makerspace | **$299 + filament** | Lets a Tier A team skip the printer line entirely |
| **T-shirt screen printing / banner printing** | Local print shop | **$200–500** | Pit presence, judge impression |
| **Portfolio printing and binding** | Any print shop, or a parent's office | **$20–60** | Direct Inspire-award input |
| **Transport — a van for event day** | Church, employer, dealership | **$150–400/event** | Solves the logistics that kill small teams |
| **Filament, fasteners, tape, consumables** | Hardware store, maker shop | **$100–250** | Never budgeted, always needed |
| **Used tooling** (drill press, bench vise, hand tools) | Retiring tradesperson, employer surplus | **$250–450** | One-time, permanent |

### 6.3 Money you already have and aren't claiming

**[FACT] Corporate matching gifts and volunteer-hour grants.** The guide: *"Take advantage of corporate donation matching programs where the company will match (double) donations made by employees to nonprofit organizations or schools. Additionally, many employers have volunteer hour programs and will donate at a per hour rate for employees who volunteer with an organization. This means that parents and mentors who volunteer their time with the team can submit their volunteer hours, and the team would receive a donation for those hours."*

> **[JUDGMENT] This is the highest dollar-per-minute fundraising action available to a small team, and it is almost universally missed.** Your mentors are already volunteering 160–200 hours ([§7.6](#76-mentor-time-realities)). If one mentor works for a company with a volunteer-hour program at a common $10–25/hour rate, that is **$1,600–5,000 of "fundraising" for filling in a form you can complete in an evening.** It requires no new relationship, no pitch, and no rejection risk. **[UNVERIFIED]** — per-hour rates vary enormously and many programs cap annual totals; the mentor must confirm with their own HR. **Ask every parent and mentor: *"Does your employer have a matching gift or volunteer grant program?"***

**Other money already in reach [FACT, from the same guide]:**

| Source | Mechanism | Effort |
|---|---|---|
| School district / booster club account | Already tax-exempt; may cover registration outright | One conversation |
| FIRST Dashboard donations | Paid directly to FIRST using FIRST's 501(c)(3); **restricted to FIRST expenses** unless regranted | Low |
| Fiscal sponsors named by FIRST | **4-H, Boys and Girls Clubs, Hack Club Bank** | Low–moderate |
| Cash-back / loyalty programs | e.g. **Kroger Community Rewards**; requires nonprofit documentation | Low, recurring, small |
| Restaurant / shopping nights | Percentage of an evening's sales; *"usually only require reaching out to the manager"* | Low; payoff depends on publicity |
| Local service organizations | **Rotary Club, Lions Club, United Way** chapters; local bank community foundations; workforce development groups | Moderate |

### 6.4 Sponsorship tiers sized for a small team

**[JUDGMENT] Scale the guide's FRC tiers down by ~2×, and promise only what 5 students can actually deliver.**

| Tier | Ask | Benefits you can genuinely deliver |
|---|---|---|
| **Friend** | **$50–199** or any in-kind | Name on team website + one social post + a student-signed thank-you card |
| **Bronze** | **$200–499** | The above + logo on the pit banner + logo in the portfolio sponsor page |
| **Silver** | **$500–999** | The above + logo on the team shirt + a written season-end impact report |
| **Gold** | **$1,000+** | The above + **logo on the robot** + a robot demo at their site + an invitation to a competition |

> **[JUDGMENT] Reserve the robot logo and the on-site demo for the top tier only** — the guide's explicit advice is to *"reserve the benefits that are the most appealing to organizations (name on the robot, for example) or require the most work to follow through to higher level tiers."* And do not promise a demo you can't staff. A broken promise costs you next season's renewal, which the guide identifies as far more valuable than a new sponsor.

### 6.5 The ask — a short template

The guide's recommended story structure is **HOOK → PROBLEM → SOLUTION → BRAG → CALL TO ACTION**, with the caution: *"Keep emails as short as possible while making the point. Most emails aren't read past the first paragraph."* It also warns against insider language: *"'FIRST Impact Award' is meaningless to anyone without the context."*

**[JUDGMENT] A small-team email that follows that structure. Replace every bracket. Keep it under 200 words. Send it from a team account, signed by a student.**

> **Subject: Local high-school robotics team — asking [COMPANY] for help with [SPECIFIC THING]**
>
> Dear [NAME],
>
> I'm [FIRST NAME], a [GRADE]th-grader at [SCHOOL] and one of [N] students on [TEAM NAME], FIRST Tech Challenge team #[NUMBER] in [TOWN].
>
> There are [N] of us. We design, build and program a robot from scratch every year to compete against teams several times our size, and we do our own budgeting, machining and software. This year's season runs September through [MONTH], and our season budget is $[X] — about $[X/N] per student.
>
> I saw that [COMPANY] [SPECIFIC REASON — sponsors the youth soccer league / does precision machining a mile from our school / employs [PARENT NAME]]. That's why I'm writing to you rather than sending this everywhere.
>
> **We're asking for [ONE SPECIFIC THING]: [e.g. "about two hours of water-jet time on 1/8" aluminium, from our files"] or a sponsorship of $[AMOUNT], which would cover [CONCRETE ITEM].** If neither works, we'd still be grateful for [ALTERNATIVE — a shop tour, an engineer to answer questions for an hour].
>
> Either way, thank you for reading. Our one-page sponsor sheet is attached.
>
> [FIRST NAME] [LAST INITIAL], [TEAM NAME] #[NUMBER]
> [team email] · [website/QR]

**Why each part is there [JUDGMENT]:** a student signature (the guide: *"potential sponsors can be more receptive to receiving an ask from students than from the team's adults"*); one specific ask with a fallback (the guide: give specifics *"while also leaving room for them to offer something else"*); a named reason for contacting *them* specifically (this is what separates a 20–30% warm ask from a 2–5% cold one); the **per-student cost** from [§2.3](#23-three-year-cost-of-ownership-and-cost-per-student-new-in-rev-4), which reframes the number as small; no jargon; and the team's small size stated as the *hook*, not hidden — being 5 kids who do everything themselves is a better story than 30 kids with a machine shop, and you should lead with it.

**Follow-through [FACT]:** track every contact in a shared spreadsheet with *"company name, contact info, priority, what to ask for, dates and methods of contact, and outcome"* — the guide names this as the record-keeping that survives student graduation. Take a no gracefully; keep the contact for next season.

### 6.6 What a small team should *not* spend fundraising effort on

| Skip | Why [JUDGMENT] |
|---|---|
| **Cold-emailing 100 businesses** | 2–5% response × your labor budget = negative return. Warm list only. |
| **Raffles** | The guide devotes a full page to state charitable-gaming law: permits, a **5% gaming tax** and 30-day filings in its Massachusetts example, plus reporting thresholds. Legal exposure and adult-hours cost, for modest money. |
| **A big fundraising event (pasta dinner, car wash)** | *"takes effort, planning, and a group of committed people"* — a labor cost a 5-student team pays out of build hours. Do this only if a parent group runs it *for* you. |
| **Repeat crowdfunding** | The guide: *"Asking your community and network to contribute to campaigns like this more than once a year is rarely successful."* Save your one shot for a Championship-qualification campaign. |
| **Long grant applications with low hit rates** | Apply only where you clearly meet stated criteria (region, rookie status, demographic, 501(c)(3), FTC-vs-FRC). Reuse boilerplate answers — the guide recommends maintaining short- and long-form standard answers. |

---

## 7. The labor budget

### 7.1 What FIRST officially expects

**[FACT — FTC Mentor Manual, official]:**

| Guideline | Number |
|---|---|
| Official team size limits | **"no less than two and no more than fifteen student team members"**, grades 7–12 |
| Recommended team size | *"For most programs the ideal team size is between 6-12 students."* |
| Required adults | *"Each team must have two adults who are screened coaches/mentors"* (Lead Coach 1 / Lead Coach 2, Youth Protection Screening — **$0**) |
| **Minimum student commitment** | **26 hours per season**, *"not including the competitions themselves"* — ~2 meetings/week × 1–1.5 h × 9–12 weeks |
| **Average student** | **~37 hours per season** |
| **Intense end** | **up to 12 hours/week over 15 weeks = 180 hours** |
| Meeting length | *"Sessions lasting 1-2 hours are the most productive."* |
| Mentor overhead | *"As a mentor, additional time will be needed each week, beyond team meetings, to prepare and coordinate the team's tasks."* |

Source: [FTC Mentor Manual](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-mentor-manual.pdf). Confirmed locally: the V0 manual requires *"2 adults must be assigned in the Lead Coach 1/Lead Coach 2 roles and have passed"* screening (`v0_pymupdf.txt` line 847).

> **⚠️ [JUDGMENT] The 26/37-hour figures describe participation, not competitiveness.** They are FIRST's floor for a student getting value from the program. **A team that intends to win awards and advance operates at or above the 180-hour "intense" end.** Do not plan a competitive season against the 37-hour number; plan against **150–250 student-hours each**, and be honest with families in September about which one you are doing.

### 7.2 Minimum viable team composition — how few students can actually do this? (NEW in Rev 4)

**[FACT — the hard constraints]:**

| Constraint | Number | Source |
|---|---|---|
| Minimum registered students | **2** | Mentor Manual |
| Minimum screened adults | **2** | V0 manual, Mentor Manual |
| **DRIVE TEAM at a match** | **up to 4 people**; **max 1 DRIVE COACH** *(may be an adult, wears a "DRIVE COACH" badge)*; **up to 3 STUDENTS** filling DRIVER and HUMAN PLAYER roles, wearing "DRIVE TEAM" badges | 2025-26 DECODE Manual, Table 10-1 — **BIOBUZZ §13 is a placeholder; re-check at kickoff** |
| Judged Initial Interview | *"all teams must participate"* (A203); team may present uninterrupted **up to ~5 minutes** (A205) | V0 §6 |
| Adults during judging | *"may not interact or actively coach"* | V0 §6 |

> **[FACT] The DRIVE TEAM definition explicitly contemplates emergencies:** the manual gives as an example of acceptable flexibility *"a bus is delayed, a DRIVE COACH has no DRIVERS, and their pit neighbors agree to help by loaning DRIVERS as temporary members of the team until their bus arrives."* It also states the intent is **not** to let teams "adopt" stronger drivers from other teams for strategic advantage.

**[JUDGMENT] The honest answer to "how few?":**

| Team size | Viable? | What it looks like | Fails when |
|---|---|---|---|
| **2 students** | **Legal, not competitive** | Both drive. One programs, one builds. No portfolio depth, no scouting, no backup anything. The adult must be the DRIVE COACH. | Any absence. Any judged award beyond participation. |
| **3 students** | **The true competitive floor** | ① Driver + lead builder ② Operator + programmer ③ Portfolio + strategy + scouting. Mentor is DRIVE COACH. | One student sick on event day. Nobody is redundant. |
| **4–5 students** | **The small-team sweet spot** | Adds a **backup driver** and a second builder. Portfolio owner is not also on the drive team, so they can be in the pit reading the feedback form. | Two simultaneous absences. |
| **6–12 students** | FIRST's recommendation | Roles start to be genuinely separable | — |

**[JUDGMENT] The four roles that MUST exist, in priority order — if any is missing you have a structural failure, not a staffing inconvenience:**

1. **Someone who can deploy code at an event.** Not write features — *deploy the version that worked yesterday.* This is the most common single point of failure in small-team FTC.
2. **A driver and a robot operator.** One student can do both, but it is a real handicap in a game with a scoring mechanism. Two is the target; a **backup driver** is the first redundancy you buy.
3. **A portfolio owner.** One person whose name is on the 15 pages, who owns the deadline. Committees do not finish portfolios.
4. **Two screened adults.** Legally mandatory, and the second one is what stops the first from burning out ([§7.6](#76-mentor-time-realities)).

Everything else — scouting, outreach, marketing, pit crew, hardware management — is a *task* that a checklist can carry, not a person you must have.

### 7.3 The official role list vs. the recommended team size

**[FACT] The Mentor Manual's role appendix lists these minimum staffing levels:**

| Role | Manual's stated minimum |
|---|---|
| Mentor | 2+ adults |
| Future Mentor | 1+ |
| Team Captain | 1+ student |
| Strategy | 2+ students |
| Build Team | 2+ students |
| Programming Team | 2+ students |
| Hardware/Tools Management | 2+ students |
| Pit Crew | 2+ students |
| Driver | 2+ students **and 1 backup driver** |
| Driver Coach | 1+ student or adult |
| Speaking Representative | 2+ students |
| Team Coopertition | whole team, 3+ specialists |
| Documentation | whole team, 2+ specialists |
| Marketing | 1+ student |
| Fundraising | 2+ students |
| Recruitment | 2+ students |
| **Total student role-slots** | **≈ 27** |

The same manual recommends **6–12 students**. It resolves the contradiction itself: *"An individual can take on multiple roles; however, be sure that a single individual does not take on too many."*

> **[JUDGMENT] For a 5-student team, that is 27 role-slots ÷ 5 = 5.4 roles per student.** This is *the* structural fact of small-team FTC and every recommendation in [§8](#8-the-strategic-core-where-a-small-team-should-concentrate) follows from it. You cannot staff the official model. **You must decide, explicitly and in writing, which roles you are *not* filling** — because the alternative is filling all of them badly, which is what most small teams do by accident.

### 7.4 Honest hours per week by role, for a competitive season

**[JUDGMENT — estimates, not sourced. Calibrated to the Mentor Manual's 180-hour "intense" figure over ~26 weeks, Sept 12 kickoff → mid-March regional.]** Hours are per person in that role.

| Role | Sep (pre-kickoff / kickoff) | Oct–Nov (design & build) | Dec–Jan (iterate & compete) | Feb–Mar (peak/champs) | Season total |
|---|---|---|---|---|---|
| **Lead builder / mechanism owner** | 3 | **10–12** | 8–10 | 8–10 | **210–260 h** |
| **Programmer** | 4 *(toolchain, sim, StarterBot example code)* | 6–8 | **10–12** *(auto tuning is a January job)* | 8 | **190–230 h** |
| **Driver** | 1 | 2 | **6–8** *(driver practice is a discipline, not a warm-up)* | 8–10 | **120–160 h** |
| **Portfolio / documentation lead** | 3 | 4–5 | 6–8 *(deadline compression before first event)* | 4 | **120–150 h** |
| **Strategy / scouting** | 2 *(manual + prior-season analysis)* | 3 | 5 *(pre-event scouting prep)* | 6 | **100–130 h** |
| **Pit crew / hardware manager** | 1 | 3 | 5 | 6 *(all event-day)* | **90–120 h** |
| **Outreach / sponsorship** | 4 *(the ask window is Aug–Oct)* | 3 | 2 | 2 | **70–90 h** |
| **Team captain (overhead on top of another role)** | +2 | +2 | +3 | +3 | **+65 h** |
| **Lead mentor (adult)** | 4 | **6–8** | 6–8 | 8–10 | **160–200 h** |
| **Second mentor (adult)** | 1 | 2–3 | 3 | 5 | **70–90 h** |

**[JUDGMENT] The arithmetic that matters for a 5-student team:** those role totals sum to roughly **900–1,140 student-hours** for a competitive season. Divide by 5 students and you get **180–230 hours each** — precisely the Mentor Manual's "intense" figure. **A 5-student team running one competitive season is running every student at the ceiling of what FIRST describes as maximum participation.** There is no slack. That is not a reason to quit; it is a reason to be ruthless about [§8.3](#83-excellent-versus-adequate--the-concentration-table).

**Event days are separate and brutal [JUDGMENT]:** a qualifier is a **10–14 hour day** including load-in, inspection, judging, 5–7 qualification matches, alliance selection, playoffs and awards, plus 1–3 h of travel each way. Budget **1.5 event-days of recovery**. A season with 3 events costs roughly **45 person-hours per attending student** on top of the table above.

### 7.5 Covering roles when a student is out

**[FACT] The Mentor Manual builds redundancy into exactly one role and says why:** Driver is *"2+ students and 1 backup driver"*, with the note *"Backup robot operators should be trained and prepared to take part in the competition, in case of illness or nerves. Practice time should include both groups, so everyone is prepared to play in front of a loud, enthusiastic audience."*

**[FACT] And the manual provides one emergency escape hatch:** loaning DRIVERS from a neighbouring team is explicitly named as an acceptable Gracious Professionalism scenario when a team arrives short-handed ([§7.2](#72-minimum-viable-team-composition--how-few-students-can-actually-do-this-new-in-rev-4)) — **but not as a strategic upgrade.**

> **[JUDGMENT] Extend redundancy to exactly three roles — and no further.** Redundancy is expensive in a 5-person team; buy it only where a single absence is fatal on event day.

| Role | Single-point-of-failure risk | Mitigation | Cost of mitigation |
|---|---|---|---|
| **Driver** | **Fatal on event day** | Train a backup; both practice. *In a genuine emergency, pit neighbours may loan drivers.* | ~40 h of the backup's time |
| **Programmer** | **Fatal** — nobody else can deploy a fix | **Everything in git, README with build/deploy steps, one other student who can pull, build and deploy** *(not write features — just deploy)* | ~10 h of cross-training |
| **Robot assembly knowledge** | **Fatal** — nobody can reassemble after a failure | Photograph every subassembly; a one-page wiring/pinout map taped inside the pit box | ~6 h |
| Portfolio lead | Recoverable — it's a document | Shared cloud doc, never a local file; a written outline early | ~0 |
| Strategy / scouting | Recoverable | Templates and a written scouting sheet anyone can fill in | ~0 |
| Outreach / sponsorship | Recoverable | Shared contact spreadsheet | ~0 |
| Pit crew | Recoverable | Written pre-match checklist any team member can execute | ~2 h |

**The four artifacts that make absences survivable [JUDGMENT]** — build these in October, not March:

1. **A written pre-match checklist** (battery swapped & logged, fuse check, fasteners, wire strain relief, opmode selected, starting configuration verified). The Mentor Manual assigns exactly this to Pit Crew: *"Creates safety and robot functionality checklists throughout the build season."*
2. **A wiring/pinout map** — one page, laminated, in the pit box. Which motor is in which port, which servo, which sensor.
3. **A deploy runbook** — how to get code onto the robot, in numbered steps, **tested by someone who is not the programmer.**
4. **A shared drive, never a personal laptop.** Every portfolio, CAD document, scouting sheet and photo. Onshape is cloud-native, which is one more reason to use it.

> **[JUDGMENT] The most common small-team catastrophe is not a broken robot. It is that the one student who understands the code has the flu on event day, and nobody else can even deploy the working version that was on the robot yesterday.** The mitigation costs ten hours in October.

### 7.6 Mentor time realities

**[FACT]** Two Youth-Protection-screened adults are mandatory (screening is free). The Mentor Manual is explicit about the boundary: mentoring means *"allowing students to do as much of the work as possible"* and *"Mentors should not complete the team's work if the team's commitment is low."* Mentor work happens *"each week, beyond team meetings."*

**[JUDGMENT] What the two mentors actually spend time on, and what to do about it:**

| Mentor task | Weekly cost | Can it be delegated? |
|---|---|---|
| Being physically present at every meeting (an adult must supervise) | **= meeting hours, non-negotiable** | Only to a second screened adult. **This is why you need two.** |
| Ordering, receiving, reconciling parts; **financial guarantor / PO setup** | 1–2 h | To a parent volunteer (no screening needed to place orders) |
| Event registration, forms, rosters, consent | 1 h | Partly — to a parent |
| Transport and logistics | 2–4 h on event weeks | To a parent driver pool |
| Technical unblocking | 2–4 h | To an in-kind technical mentor ([§6.2](#62-the-in-kind-ask-is-the-small-teams-superpower)) |
| Fundraising and sponsor relations | 1–2 h | **Should be students** — the guide says sponsors respond better to students |

> **[JUDGMENT] The realistic ask for a lead mentor of a competitive small team is 160–200 hours/season — a demanding part-time commitment.** Two mentors at that level is the thing that fails first in small programs, and it fails silently: the second mentor drifts to "shows up sometimes", the first absorbs the difference, and by February the adult is doing the students' work — which is both a mentoring failure and, in judging terms, a story the judges will notice. **Recruit the second adult in August, give them a defined job (logistics, ordering, transport — not engineering), and protect the lead mentor's hours.** A parent who owns ordering and driving is worth more than a parent who "helps out."

### 7.7 Where AI displaces labor — and where it must not

**[FACT] A201 permits AI in the portfolio**, verbatim: *"Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a footnote or endnote credit. Example Credit: 'Portfolio created by Team XXXXX and ChatGPT'."* (`sections/06_Awards_A_p43-58.txt`, A201)

**[JUDGMENT] Draw the line at "clerical vs. engineering", and hold it.** The team's stated goal is *more* hands-on student time, and the failure mode is subtle: AI that writes your design rationale doesn't just risk a rules problem, it hollows out the exact evidence judges are looking for — and judges interview students about their own work.

| Use AI for (clerical — reclaims hours) | Do not use AI for (engineering — destroys the deliverable) |
|---|---|
| Drafting sponsor emails from your template, then a student edits and signs | Making the design decision, or writing the design rationale as if it were the team's |
| Turning meeting notes and photos into portfolio *draft* prose the students rewrite | Producing the trade study the students never did |
| Parsing manuals, diffing Team Updates, building rule checklists (e.g. the R501 legality check in [§5.4](#54-cost-cuts-that-are-actually-rules-violations-new-in-rev-4)) | Answering judges' questions (obviously, and it will be visible) |
| Boilerplate for grant applications you customize | Fabricating outreach or impact numbers |
| Scouting-data munging, event-schedule parsing, ftc-events API work | Writing autonomous code no student on the team understands |
| Price/BOM checking against vendor pages — this document's own re-check list | Being the only entity that knows how the code works ([§7.5](#75-covering-roles-when-a-student-is-out)) |

> **[JUDGMENT] The honest test:** *if a judge asked the student who owns this to explain it, unprompted, for two minutes — could they?* If yes, the AI was a tool. If no, you have traded a 12-point award for a few saved hours, and the credit footnote won't save you. Budget **$160/season for Claude Pro** ([§1.7](#17-software-and-digital-tooling--the-0-column)) and spend it on the left-hand column.

---

## 8. The strategic core: where a small team should concentrate

### 8.1 How matches and advancement are actually won

**Chain of facts [FACT — V0 §4 and DECODE §13]:**

1. Advancement is scored on **four independent inputs**: qualification rank (2–16), alliance selection (up to 20), playoff finish (up to 40), and **judged awards (up to 60 for Inspire 1st, 12 for any other 1st place)**.
2. Playoff alliances are **two robots**, and only **6 of ~30 teams lead an alliance** at a 21–40 team event — **12 of 30 play in the playoffs at all**.
3. Alliance selection explicitly rewards being *pickable*, not just being ranked: FIRST's commentary says the points *"support come-from-behind teams"* and *"recognize teams employing a unique strategy"* — *"Teams with unique or divergent ROBOT capabilities that complement the strengths of other ALLIANCE members may be selected to fill a strategic niche."*
4. Ties are broken by **Judged Team Award points before playoff points**, then by **average match points**, then **average AUTO points** — three consecutive consistency measures.

> **[JUDGMENT] What that structure rewards, in priority order, for a team with 5 students and $3,000:**
>
> | Priority | What it is | Why the structure rewards it |
> |---|---|---|
> | **1** | **Be pickable** — do one thing consistently and predictably, every match | Your robot is 50% of a 2-robot alliance. Alliance captains pick reliability over peak scoring, because they can plan around a robot that always does X. |
> | **2** | **Win judged awards** | 60 points for Inspire, 12 for each other 1st place, and they outrank playoff points on the tiebreak. Costs $20 and student-hours, not dollars. |
> | **3** | **Score in autonomous, every time** | AUTO is the most repeatable phase (no defence, no opponent interaction), it is where disciplined tuning beats money, and **average AUTO points is tiebreaker #7**. |
> | **4** | **Finish every match mobile** | A dead robot scores zero, drags your average match points down (tiebreaker #6), and gets remembered by every scout in the room. |
> | **5** | Peak scoring rate | Matters, but a high-variance high-ceiling robot loses to a boring reliable one across 5–7 quals *and* on three separate tiebreakers. |

### 8.2 How awards are actually judged

**[FACT — V0 §6]:**

| Mechanic | Detail |
|---|---|
| Portfolio limits (**A201**) | Cover page + **no more than 15 pages of content**; US Letter or A4; digital submission **< 15 MB**; content **only from since 1 January 2026** |
| Judges will **not** click links | *"JUDGES will not click on links, websites, or videos in a PORTFOLIO."* They also *"cannot take extra printed papers from an interview back to their judging room."* |
| Initial Interview | Team may present **uninterrupted for up to about 5 minutes** (A205); may be in a room, in the pits, or virtual; **all teams must participate** (A203) |
| Judges' scope | *"strictly instructed to only consider information from the current event and the current season"*; **the current season begins 1 January 2026** |
| Feedback | **Every team gets a written feedback form** from the Initial Interview (A212) |
| Award count scales with event size (**A211**) | At a **21–40 team event**: Inspire 1st/2nd/3rd, Think 1st/2nd, and 1st (often 2nd) place in Connect, Reach, Sustain, Design, Innovate, Control, plus Judges' Choice |
| Inspire restrictions | Only winnable **in your HOME REGION** (A213), and **only once per season** from any Qualifying or League Tournament (A214) |
| Coaches may not coach | Adults may observe outside the Initial Interview but *"may not interact or actively coach"* during judge interactions |
| AI is permitted, with credit | A201 — see [§7.7](#77-where-ai-displaces-labor--and-where-it-must-not) |

> **[JUDGMENT] Six consequences a small team should act on immediately:**
> 1. **The season already started on 1 January 2026.** Anything your team did this spring and summer — outreach, a demo at a library, a summer build, the StarterBot Base you assembled in August, a rookie team you helped start — is *current-season* content. **Go inventory it this week**; most small teams throw away eight months of free portfolio material because they think the season starts at kickoff.
> 2. **15 pages is a small-team advantage.** A 30-student team has more to say than fits. You do not. The constraint is binding on them and free for you.
> 3. **Everything must be *in* the portfolio.** No QR codes to a website, no "see our YouTube." Judges won't click, and can't take handouts back to the room.
> 4. **Rehearse 5 minutes, not 10.** It is the only guaranteed uninterrupted judge contact you get all season. For a 5-student team that means every student speaks — which is also what judges want to see.
> 5. **At a 30-team event there are roughly 8–10 award categories in play, most with 1st and 2nd place.** With 30 teams and ~14 award slots, the odds of *some* award are far better than the odds of a playoff win, and each 1st place is 12 points.
> 6. **Read your feedback form.** Every team gets one and most teams never act on it. It is a free, judge-written specification for winning the same award at the next event.

### 8.3 Excellent versus adequate — the concentration table

**[JUDGMENT] This is the core recommendation of this document.**

| **Be genuinely excellent at** | Why | What it costs you |
|---|---|---|
| **One scoring mechanism, executed reliably** | It is what makes you pickable; it is the whole robot for a small team | Most of your build hours — deliberately |
| **A repeatable autonomous** | Highest points-per-hour on the field; testable without opponents; **tiebreaker #7** | Programmer hours in Dec–Jan |
| **Drivetrain reliability** *(not sophistication)* | A robot that never dies gets picked; a robot that dies never does | ~$300 COTS chassis, the StarterBot base, or a careful build |
| **The portfolio and the 5-minute interview** | 60/12 points at ~$0.33/point; the only arena where you are equal to the biggest team in the room | ~60–90 student-hours, front-loaded |
| **Documentation discipline** *(photos, decisions, dates, from day 1)* | Raw material for the portfolio, the interview, *and* the deploy runbook; cannot be retrofitted in March | 15 min at the end of every meeting |
| **Battery and pre-match discipline** | Removes the highest-frequency cause of losing a match you should have won | $319 + a checklist |
| **Rules literacy on R501/R502/R601** | Prevents the one failure mode that is 100% fatal and 100% avoidable | 2 hours, once, with the parts spreadsheet open |

| **Be deliberately merely adequate at** | Why it's safe to be adequate | The trap |
|---|---|---|
| Robot aesthetics / wire tidiness beyond safe-and-inspectable | No points, low judging weight relative to cost | Perfectionism eats build hours |
| A second scoring mechanism | Doubles mechanism risk, halves your iteration count on the first one, and often forces the +$275 Expansion Hub | "We need to do everything the top teams do" |
| Advanced localization / vision beyond what your auto actually needs | Enormous hour sink, small point yield if the basic auto is already reliable | Chasing what looks impressive on Chief Delphi |
| Peak cycle speed | Reliability beats speed across 5–7 quals **and on three tiebreakers** | Optimizing a mechanism that isn't finished |
| CAD completeness (full-robot assembly of every part) | CAD the interfaces and the mechanism; sketch the rest | CAD as procrastination |
| Custom machined parts | Print, buy, or take machining as in-kind | Buying a mill |
| Elaborate scouting software | A shared sheet + [ftcscout.org](https://ftcscout.org) covers a small team's needs | Building an app instead of a robot |
| Social media presence | Not a judged criterion in itself | Confusing marketing with outreach |
| Attending many events | 3 entry-level events max are advancement-eligible; each costs money and ~45 person-hours | Over-scheduling a 5-person team |

| **Be deliberately bad at / simply not do** | Why |
|---|---|
| Cold-call fundraising campaigns | 2–5% response × scarce labor |
| Raffles and large fundraising events | Legal overhead and adult-hours; let a parent group own them or skip |
| Building a second/practice robot | Tier C item; buy driver practice with borrowed field time instead |
| A machine shop of your own | In-kind ask, or print |
| Chasing every award category | Pick 3: **Inspire + one MCI award (Design/Innovate/Control) + one TA award (Connect/Reach/Sustain)** and prepare those properly |

### 8.4 The one-paragraph version

> **[JUDGMENT]** For a team with 4–6 students and a Tier A/B budget, the winning shape is: **a boring, reliable, single-mechanism robot with a drivetrain that never fails and an autonomous that always works, presented by a team with an excellent 15-page portfolio and a rehearsed 5-minute interview.** That team is pickable at 30-team events, collects 10–14 qualification points, is a plausible second pick into a 2-robot alliance, and competes on level terms for a 60-point Inspire Award and a 12-point category award — using free CAD, free training content, free StarterBot guides, free match data, a $20 print job, and a $350 control system that costs the richest team in the room exactly the same. **The money buys spares, travel and iteration speed. It does not buy the four things that decide advancement: strategy, code, documentation and discipline.** Concentrate there.

---

## 9. The money-and-labor calendar, Aug 2026 → Apr 2027

**[JUDGMENT] Dated actions, in order. Deadlines marked [FACT] are sourced above.**

| When | Money action | Labor action |
|---|---|---|
| **This week (22–31 Aug 2026)** | **Three vendor discount forms: goBILDA 25%, REV 15%, Studica 25%** ([§3.2](#32-the-vendor-discount-stack--the-highest-roi-paperwork-in-ftc)) · check FIRST grants page for an open Argosy rookie cycle **before paying registration** · ask PDP for hardship-grant nomination + written 2026-27 event fee schedule + waitlist criteria · **school teams: start the financial-guarantor / EIN setup and confirm FIRST is added as a payor** | Both mentors complete Youth Protection Screening ($0) · recruit the second adult and give them a defined job · **inventory everything done since 1 Jan 2026** for the portfolio · **build the StarterBot Base** from whatever kit you own ([§3.5](#35-the-starterbot-path--the-cheapest-way-to-own-a-working-robot-in-week-2-new-in-rev-4)) |
| **By 1 Sept 2026** | **[FACT] Gene Haas Foundation deadline** — only if you have 501(c)(3)/public-school status and a CNC nexus | Ask every parent/mentor: matching gifts? volunteer-hour grants? ([§6.3](#63-money-you-already-have-and-arent-claiming)) |
| **Early Sept, pre-kickoff** | Register ($350) **after** grant sequencing · order storefront kits · order 3 batteries + dual-port charger · buy the **$5.50 POLLEN preview pack** · **check every actuator SKU against R501 Table 12-1 before ordering** | Warm sponsor list built (10–20 pre-qualified names) · student-signed asks sent · Onshape accounts created · FIRST Training Skill Builders started |
| **12 Sept 2026 — Kickoff [FACT]** | Hold parts spend until strategy is decided | Read §§8–11, 13 and 15 of the released manual · run `tools/ingest-manual.sh` · full vendor StarterBots release today · **decide the one mechanism** |
| **Sept–Oct** | DIY perimeter + 18 official tiles (~$307) · structure and motion parts **after** CAD, not before | Peak build hours (10–12 h/wk for builders) · **build the four absence-proofing artifacts** ([§7.5](#75-covering-roles-when-a-student-is-out)) · portfolio outline exists by 31 Oct |
| **Nov** | Order spares by failure probability ([§5.1](#51-cost-cuts-ranked-by-savings-per-unit-of-performance-lost)) | **Write the Championship emergency-fundraiser email and leave it in drafts** · beg 2–3 sessions on a real field |
| **Dec–Jan** | Event fees due per your PDP's schedule | Autonomous tuning is a January job · driver practice becomes 6–8 h/wk · portfolio drafted, printed, proofed · rehearse the 5-minute interview until every student speaks |
| **First event** | Travel = fuel only; carpool | **Read the judge feedback form the day you get it** and act on it before the next event |
| **Feb–Mar** | Regional championship fees · shirts/banner if funded | Peak driver and pit-crew hours |
| **If you qualify for Houston** | **[FACT] $3,000 team fee** + ~$6,000–9,000 travel; FIRST requires both the fee and ConferenceDirect lodging secured, on a hard deadline | Launch the drafted campaign the same day |
| **April–May (off-season)** | **This is the cheap year-2 window** ([§2.3](#23-three-year-cost-of-ownership-and-cost-per-student-new-in-rev-4)) — fix your tax status, buy the one thing that limited you · thank every sponsor with a written impact report · **REV discount codes expire 31 May 2027 — re-request** | Recruit next season's students · write the season retro while it's fresh |

---

## 10. Re-check checklist

**Everything below was read in August 2026 and will drift. Verify before spending.** ✅ = resolved in Rev 4.

| # | Item | Where to check | Status / why it moves |
|---|---|---|---|
| 1 | **Your PDP's 2026-27 event fee schedule** | Email your Program Delivery Partner | **OPEN — largest uncontrolled variable**, ~5× regional spread |
| 2 | FIRST registration + storefront kit prices | [firstinspires.org/robotics/ftc/cost-and-registration](https://www.firstinspires.org/robotics/ftc/cost-and-registration) | Re-confirmed $350 / $295 / $350 / $660 on 2026-08-22 |
| 3 | **Storefront PDF revision** | [ftc-storefront-options.pdf](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf) | **STILL rev 25-26.4 (Feb 2026)** with 2025-26 prices — **trust the website** |
| 4 | **Open 2026-27 grants — weekly until December** | [firstinspires.org/programs/team-grant-opportunities](https://www.firstinspires.org/programs/team-grant-opportunities) | **STILL no open 26-27 FTC grant.** Argosy $1,000 is forfeited once you pay registration |
| 5 | REV prices: Control Hub $375, Driver Hub $275, Expansion Hub $275, Slim Battery $55, charger $36.50 | [revrobotics.com](https://www.revrobotics.com/) | Vendor pricing moves mid-season |
| 6 | goBILDA 25% discount terms | [gobilda.com/ftc](https://www.gobilda.com/ftc/) | Re-confirmed. *"a few exclusions apply"* — unspecified; ask which |
| 7 | **goBILDA 5203 cross-ratio price parity** | [Yellow Jacket family page](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) | ✅ **RESOLVED — $54.99 across all 11 ratios** |
| 8 | **Chassis kit availability and prices** | [gobilda.com/chassis-kits](https://www.gobilda.com/chassis-kits) | ✅ Refreshed. **⚠️ 20V Overlander kits on the same page are R501-illegal** |
| 9 | **AndyMark BIOBUZZ game-set shipping** after the 7 Aug wave | [andymark.com FTC 26-27 pre-orders](https://andymark.com/products/ftc-2026-27-preorders) | **OPEN — no second wave published; orders fill in the order received. Phone them.** |
| 10 | AndyMark battery/charger: am-5290 $54, am-5619_XT30 $154 | [andymark.com](https://andymark.com/) | **OPEN — confirm the RDX2's average channel current ≤ 3 A** per the manual's charging rule |
| 11 | **BIOBUZZ Sections 8–11, 13 and 15** | Manual release at kickoff, 12 Sept 2026 | **OPEN — §5.2, §7.2 and §8.1 cite DECODE's §13/Table 10-1 and 13-2 as proxies. Re-verify.** |
| 12 | **FTC SIM 2026-27 field availability** | [ftcsim.org](https://ftcsim.org/) | ✅ **Confirmed absent** as of 2026-08-22 — DECODE only |
| 13 | Claude plan pricing | [claude.com/pricing](https://claude.com/pricing) | ✅ **RESOLVED — Pro $20/mo or $200/yr; Max from $100/mo** |
| 14 | Parent Booster USA ($575/$450) and IRS 1023-EZ ($275) fees | [parentbooster.org/pricing](https://parentbooster.org/pricing), [IRS](https://www.irs.gov/charities-non-profits/frequently-asked-questions-about-form-1023) | **OPEN** — fees and early-bird windows change annually |
| 15 | **Team Updates, every week after kickoff** | FTC Team Updates page | **OPEN** — R-rules are final in V0, but Team Updates amend the manual all season, **including the legal motor list** |
| 16 | **REV 15% discount code** ⭐ *new* | FIRST Dashboard, or [revrobotics.com/ftc/discounts](https://www.revrobotics.com/ftc/discounts/) | **Codes expire 31 May 2027.** Confirm which SKUs are in the category before assuming a discount |
| 17 | **Studica 25% team discount** ⭐ *new* | [studica.com/studica-robotics-team-discount](https://www.studica.com/studica-robotics-team-discount) | **UNVERIFIED — page returned HTTP 403.** Open it in a browser |
| 18 | **Financial guarantor / payor setup** ⭐ *new* | FIRST Dashboard → Team/Account Finances | **Blocks ordering** for PO or tax-exempt teams. Slow. Start early |
| 19 | **goBILDA Upgrade Pack contents** ⭐ *new* | [goBILDA StarterBot guide](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/) | $249.99 vs $899.99 — confirm what it contains against your inventory |
| 20 | Sales tax on registrations without physical items ⭐ *new* | [FIRST pricing updates](https://community.firstinspires.org/2026-2027-season-pricing-and-registration-updates) | New for 26-27 in certain jurisdictions |

---

## 11. Sources

**Local (this workspace):**
`manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` (R101, R301, R302, R501 + Table 12-1, R502 + Table 12-2, R503, R601, R602, R701, R901, COTS definition, charging rule) · `.../04_Advancement_p27-32.txt` (Tables 4-1, 4-2, §4.1.1 formula) · `.../06_Awards_A_p43-58.txt` (A201, A203, A205, A211–A214, judging scope, AI credit) · `.../03_Eligibility_Inspection_I_p22-26.txt` · `.../05_EventRules_E_p33-42.txt` · `.../02_SeasonOverview_p5-21.txt` · `.../14-16_League_Glossary_p90-93.txt` · `manuals/2026-27_BIOBUZZ/v0_pymupdf.txt` · `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_INITIAL_kickoff.txt` (DRIVE TEAM definition, Table 10-1) · `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf` (§13.7.1–13.7.2, Table 13-2) · sibling docs `reference/AWARD-CATALOG-BIOBUZZ.md`, `reference/AWARD-ALIGNMENT-MATRIX.md`, `reference/LEGAL-PARTS-CONSTRAINTS.md`, `reference/VENDOR-ECOSYSTEMS.md`, `research/SCOUTING-AND-AWARDS.md`, `research/SEASON-CADENCE.md`

**Official FIRST:** [Cost & Registration](https://www.firstinspires.org/robotics/ftc/cost-and-registration) · [Get Started](https://www.firstinspires.org/programs/ftc/get-started) · [Team Grant Opportunities](https://www.firstinspires.org/programs/team-grant-opportunities) · [FTC Mentor Manual](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-mentor-manual.pdf) · [FRC Fundraising Guide, Rev. July 2026](https://www.firstinspires.org/hubfs/web/program/frc/resources/fundraising-guide.pdf?hsLang=en) · [Storefront Kit & Price Options PDF](https://info.firstinspires.org/hubfs/web/program/ftc/ftc-storefront-options.pdf) · [Low-Cost Field Perimeter Guide](https://ftc-resources.firstinspires.org/ftc/archive/2025/game/diy-perimeter) · [Planning for FIRST Championship](https://community.firstinspires.org/2025-planning-for-first-championship) · [2026-2027 Season Pricing and Registration Updates](https://community.firstinspires.org/2026-2027-season-pricing-and-registration-updates) · [Key Changes to FTC Registration](https://community.firstinspires.org/key-changes-to-first-tech-challenge-registration-whats-new) · [Game Preview 2027: StarterBots, Skill Builders, Field Elements](https://community.firstinspires.org/game-preview-field-elements) · [Introducing FTC Skill Builders](https://community.firstinspires.org/introducing-first-tech-challenge-skill-builders) · [2026 Advancement Model whitepaper](https://community.firstinspires.org/hubfs/web/program/ftc/2026-advancement-whitepaper-v1.pdf) · [FTC Docs — Team Discounts](https://ftc-docs.firstinspires.org/sponsors/discounts/discounts.html) · [FTC Docs — PTC CAD Resources](https://ftc-docs.firstinspires.org/en/latest/cad_resources/ptc/ptc.html)

**Vendors:** [REV Control Hub](https://www.revrobotics.com/rev-31-1595/) · [REV Driver Hub](https://www.revrobotics.com/rev-31-1596/) · [REV Expansion Hub](https://www.revrobotics.com/rev-31-1153/) · [REV 12V Slim Battery](https://www.revrobotics.com/rev-31-1302/) · [**REV FTC Team Discounts**](https://www.revrobotics.com/ftc/discounts/) · [REV FTC Starter Bot](https://www.revrobotics.com/competition/ftc-starter-bot/) · [REV 12V Battery Best Practices](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/12v-battery-best-practices-and-troubleshooting) · [REV Control Hub Troubleshooting](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/control-hub-troubleshooting) · [REV Building Your Toolbox](https://www.revrobotics.com/blog/tech-tool-tip-tuesdays-building-your-toolbox/) · [goBILDA FTC](https://www.gobilda.com/ftc/) · [**goBILDA Yellow Jacket family**](https://www.gobilda.com/yellow-jacket-planetary-gear-motors/) · [goBILDA Chassis Kits](https://www.gobilda.com/chassis-kits) · [goBILDA Starter Kit 2026-27](https://www.gobilda.com/ftc-starter-kit-2026-2027-season/) · [**goBILDA StarterBot Base Resource Guide**](https://www.gobilda.com/ftc-starter-bot-resource-guide-2026-2027-season/) · [AndyMark Robits Core Kit](https://andymark.com/products/robits-core-kit) · [AndyMark FTC 2026-27 pre-orders](https://andymark.com/products/ftc-2026-27-preorders) · [AndyMark Flat Pack Battery](https://andymark.com/products/am-flat-pack-battery) · [AndyMark RDX2 charger](https://andymark.com/products/rdx2-200-2-port-xt30-ftc-battery-charger) · [AndyMark FTC Perimeter Kit](https://andymark.com/products/first-tech-challenge-perimeter-kit) · [AndyMark Field Soft Tiles](https://andymark.com/products/first-tech-challenge-field-soft-tiles) · [AndyMark PDV (FRC only)](https://andymark.com/pages/pdv) · [Studica StarterBot Build Guide](https://www.studica.com/blog/ftc-starter-bot-build-guide-2026-2027/) · [Studica team discount](https://www.studica.com/studica-robotics-team-discount) · [Bambu Lab A1 mini](https://us.store.bambulab.com/products/a1-mini)

**Community & regional:** [GM0 — Starting a Team](https://gm0.org/en/latest/docs/being-a-team/starting-a-team.html) · [FTC SIM](https://ftcsim.org/) · [ftcscout.org](https://ftcscout.org) · [Chief Delphi — used FTC control systems](https://www.chiefdelphi.com/t/buying-used-ftc-control-systems/518828) · [Chief Delphi — FRC/FTC Marketplace](https://www.chiefdelphi.com/t/frc-ftc-marketplace/480331) · [Chief Delphi — 501c3 for robotics teams](https://www.chiefdelphi.com/t/501c3-organizations-first-and-robotics-teams/473881) · [Chief Delphi — team budget per season (FRC, do not import)](https://www.chiefdelphi.com/t/team-budget-per-season/145475) · [FTC 9929 toolbox](https://ftc9929.com/2020/06/22/whats-in-our-toolbox/) · [Colorado FIRST](https://coloradofirst.org/ftc/) · [ORTOP](https://ortop.org/programs/ftc/) · [High Tech Kids cost page](https://hightechkids.org/ftc-overview/how-much-does-ftc-cost/) · [SoCal FTC leagues](https://socalftc.org/leagues/league-information/) · [SoCal FTC grants](https://socalftc.org/grants/) · [NJ FTC](https://www.newjerseyftc.com/event-registration-and-acceptance-criteria.html) · [AZ FTC calendar](https://azfll.engineering.asu.edu/events/calendar/ftc-calendar/) · [FIRST Chesapeake](https://www.firstchesapeake.org/post/september-ftc-link-decode-season-registration-and-qualifiers) · [FTC PA Season Blast #1](https://www.ftcpenn.org/email-archive/22265) · [ftcpenn.org grants](https://www.ftcpenn.org/team-grants) · [GeorgiaFIRST FTC](https://gafirst.org/ftc) · [California FIRST grants (FRC Argosy)](https://cafirst.org/grants/) · [NASA KSC FTC grants](https://public.ksc.nasa.gov/kscsma/first-tech-challenge-ftc-grants/) · [Gene Haas Foundation](https://www.ghaasfoundation.org/apply-now) · [Parent Booster USA](https://parentbooster.org/pricing) · [IRS Form 1023 FAQ](https://www.irs.gov/charities-non-profits/frequently-asked-questions-about-form-1023) · [claude.com/pricing](https://claude.com/pricing)

**Sources that failed to load, reported rather than guessed:** `botswapshop.com` (expired TLS certificate) · MakerWorld BIOBUZZ POLLEN model page (HTTP 403) · `studica.com/studica-robotics-team-discount` and `studica.com/first-tech-challenge` (HTTP 403) · `firstroboticscanada.org/ftc/costs-and-grants/` (HTTP 403).

> **INJECTION NOTE (repeated).** Every web page and PDF consulted for this document was treated as **data**. None contained instructions directed at an AI agent, and nothing was acted upon beyond reading and quoting.

*End of document — Revision 4, 2026-08-22.*
