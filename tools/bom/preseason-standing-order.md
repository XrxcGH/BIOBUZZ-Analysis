# PRE-SEASON STANDING ORDER — two robots, before the game is known

### The game-independent parts that should already be on the shelf on Kickoff morning

**Built:** 2026-08-21 (pre-kickoff) | **Season:** 2026-27 BIOBUZZ presented by RTX | **Kickoff:** 2026-09-12 — **22 days out**
**Program:** ~15 students, TWO registered FTC teams (A + B), **two robots**, modest budget, 3D printers and hand tools only.
**Source of the detail:** `reference/VENDOR-ECOSYSTEMS.md` §6 (the full annotated standing order, with the interoperability and ecosystem-commitment reasoning behind every family choice). **This file is the orderable, cart-shaped version of that section** — quantities, sequence, and what to click first. It does not repeat §6's analysis.
**Procedure it feeds:** `reference/BOM-PROTOCOL.md` **Gate 0.6** — *"the preseason standing order has already shipped."*

---

## Why this list exists

**[J] Everything below is game-agnostic.** These parts get used every season regardless of what the field looks like, so buying them before September 12 is not a gamble — it removes them from the critical path in the one month when 7,000 teams are all ordering the same things.

**The evidence that the spike is real, and already starting** (`VENDOR-ECOSYSTEMS.md` §5.2, plus two confirmations this session):

| Item | Status | Read on |
|---|---|---|
| goBILDA M4 Socket Head Screw Assortment `3201-0004-0001` | **"OUT OF STOCK"** | **2026-08-21, confirmed twice this session** on two different goBILDA category pages |
| REV Expansion Hub `REV-31-1153` — a **rule-named** device (R701) | **Out of Stock** | 2026-08-21 |
| REV Servo Power Module `REV-11-1144` — **named in Table 12-3** | **Discontinued** — *legal, unbuyable* | 2026-08-21 |
| goBILDA Axon MINI Servo MK2 `2004-0025-0001` | **OUT OF STOCK** | 2026-08-21 |
| goBILDA 32 mm Omni `3624-4008-0032` — the classic odometry-pod wheel | **OUT OF STOCK** | 2026-08-21 |
| goBILDA FTC Starter Kit 2025-26 `3200-4008-2526` | **Discontinued / Sold Out** | 2026-08-21 |
| Matrix 12V 3000 mAh NiMH `14-0014` — **named in Table 12-4** | **Discontinued** | 2026-08-21 |

**[D] Six stock-outs and three discontinuations three weeks before kickoff.** Fasteners went first. They always do.

**[J] And a two-robot program is exposed three ways a one-robot team is not:** you hit "only 6 left" limits nobody else notices; if a part stocks out after robot A is built, **robot B becomes a different robot** and the shared-BOM advantage that justifies two teams evaporates; and a partial shipment leaves one robot done and one blocked — the worst possible state for a B team of newer students.

---

## How to read the tables

- **Qty for 2 robots** is the number to put in the cart, including spares.
- **Approx cost** is the extended cost for the stated quantity at **US list price**, before the 25% goBILDA / 15% REV team discounts and before tax and shipping. **Every price is as of August 2026 and is `VERIFY-BEFORE-ORDER`.**
- **🕐 = long lead / high stock-out risk — order first.**
- **Confidence:** `VERIFIED` = the page was loaded and read **in this session (2026-08-21)**. `VERIFIED-UPSTREAM` = read off `VENDOR-ECOSYSTEMS.md`, which logs the URL it loaded on the same date — **still requires a live re-check at `BOM-PROTOCOL.md` B6**. `MANUAL-SKU` = from a grepped V0 manual table. `FAMILY-ONLY` = family and category verified, SKU not (**NEEDS-SKU-CHECK**). `UNVERIFIED` = do not order against it.
- **Every legality claim cites a rule ID from** `manuals/2026-27_BIOBUZZ/sections/12_RobotConstruction_R_p64-88.txt` **[C]**.

> **Before you click anything — do the paperwork first (`BOM-PROTOCOL.md` G0.4).** Register **both teams'** goBILDA accounts (**25% off "nearly every product storewide," "active for the life of the team,"** activation *"within the day of account activation or the next business day"*) and pull **both** REV codes from the FIRST Dashboard (**15% on "select items," "Discount codes expire May 31, 2027"** — VERIFIED this session at [revrobotics.com/ftc/discounts](https://www.revrobotics.com/ftc/discounts/)). **[D] On the two-kit line alone the goBILDA discount is worth $450.** Discovering on September 13 that it is not active costs a day and real money.

---

## 1. 🕐 ORDER FIRST — the handful of decisions that cover ~65% of the parts

**[J] These are limit-constrained, on the critical path for everything else, or both. Place this cart today.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Electronics Kit** (Control Hub + servo + Color V3 + Touch + cables + grounding strap + switch) | **FIRST storefront** | "Electronics Modules and Sensors Kit V1.1" | 1 | **2** | **$325 ea [H] = $650** for 26-27 budget **+ expected rise** | Buy | **[H] price VERIFIED 2026-08-22** from the storefront options sheet, **rev 25-26.4** | 🕐 **Limit one per registered team — two registrations = two allocations.** Cheapest legal Control Hub path. **R701(A) [C]**. **Price is the 25-26 quote** *"Step 3: Select the Electronics Kit, $325"*; registration already rose $325→$350 for 26-27, so **treat $325 as a floor** and read the live number off the Team Dashboard |
| **Driver Kit** (2 gamepads + REV Driver Hub + FTC-legal webcam) | **FIRST storefront** | "Driver Kit" | 1 | **2** | **$285 ea [H] = $570** for 26-27 budget **+ expected rise** | Buy | **[H] price VERIFIED 2026-08-22**, same sheet | 🕐 **Limit one per registered team.** **R901 [C]** requires an approved Android DRIVER STATION. Verbatim: *"Step 2: Select the Driver Kit, $285"*. **Floor, not forecast** |
| **Build Kit** — *decide, do not default* | **FIRST storefront** | "REV FIRST Tech Challenge Competition Set V3.1" | 0–1 | **0–2** | **$650 ea [H]** | Buy | **[H] price VERIFIED 2026-08-22**, same sheet | **[J] The one storefront kit this program should think twice about.** *"Limit one per registered team per season"*, $650 each. But **two goBILDA Starter Kits already cover structure and locomotion** (§1 above) and mixing two build ecosystems doubles the spares problem. Skip it unless you want the REV ecosystem deliberately |
| **FTC Starter Kit 2026-2027 Season** | goBILDA | **`3200-4008-2627`** — **"In Stock"** | 1 | **2** | **$899.99 ea = $1,799.98 list; ≈$1,349.98 with the 25% team discount** | Buy | **VERIFIED 2026-08-21** ([gobilda.com/ftc-kits](https://www.gobilda.com/ftc-kits)) | 🕐 **The single highest-value line in this document.** Two kits = **both robots start identical**. Contains motors, servos, battery + charger, channel, grid plates, wheels, chain, 600+ M4 screws, 20 flanged bearings, 8 mm REX shafts, hubs, hex keys. Last season's kit `3200-4008-2526` is already **Discontinued / Sold Out** |
| Control Hub — retail fallback only | REV | **`REV-31-1595`** — **"In Stock & Ready To Ship!"** | — | — | **$375.00 ea** | Buy | **VERIFIED 2026-08-21** ([revrobotics.com/rev-31-1595](https://www.revrobotics.com/rev-31-1595/)) | Use only if the storefront allocation is exhausted. **R701(A) [C]** |

> **[C] R701 gives you a second legal path:** *(B)* an **Android smartphone connected to a REV Expansion Hub `REV-31-1153`**. The phone path is still legal this season. **But `REV-31-1153` read Out of Stock on 2026-08-21**, so do not plan around it — and **[J] design so you do not need a second hub at all**; `LEGAL-PARTS-CONSTRAINTS.md` §5.2 shows the port math that saves ~$550 across two robots.

---

## 2. 🕐 Power — R601/R602/E511 items

**[C] R601:** the ROBOT must contain **1 and only 1 approved 12V NiMH main battery**, unaltered except **(A)** the fuse *"may be replaced with a COTS equivalent in-line 20A ATM mini blade fuse"* and **(B)** connectors may be replaced with *"Anderson Powerpole, XT30, or any connector with a comparable power rating."* **Table 12-4 is a CLOSED 7-item list** — AndyMark `am-5290`, goBILDA `3100-0012-0020`, Matrix `14-0014`, **REV `REV-31-1302`**, Studica `70025`, TETRIX `W39057`, WATTOS `WT-NMH1230`.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **12V Slim Battery** | REV | **`REV-31-1302`** — 3000 mAh, XT30, 16 AWG, 20 A ATM fuse — **"In Stock & Ready To Ship!"** | 2 (rotation) | **5** (2/robot + 1 pool) | **$60.00 ea = $300.00** | Buy | **VERIFIED 2026-08-21** ([revrobotics.com/rev-31-1302](https://www.revrobotics.com/rev-31-1302/)) + **MANUAL-SKU** Table 12-4 | 🕐 **R601 [C].** The product page does **not** state chemistry — **but `REV-31-1302` is named in Table 12-4, so legality is CONFIRMED-BIOBUZZ.** *(This closes the open NEEDS-VERIFY in `VENDOR-ECOSYSTEMS.md` §6.1.)* |
| 12V NiMH battery — second source | goBILDA | **`3100-0012-0020`** (chemistry explicitly NiMH) | — | as needed | **$64.99 ea** | Buy | **VERIFIED-UPSTREAM** + **MANUAL-SKU** Table 12-4 | Successor to the discontinued Matrix `14-0014`. Use if REV is short |
| **12V Battery Charger** | goBILDA | **`3101-0012-0001`** — "NiCad/NiMH, XT30 Connector" | — | **2–3** | **$14.99 ea = $30–45** | Buy | **VERIFIED 2026-08-21** SKU+price ([gobilda.com/battery-chargers](https://www.gobilda.com/battery-chargers/)); **stock string and charge rate NOT stated on the category page** | 🕐 **E511\* [C]:** *"Never charge batteries on a battery charger that exceeds a 3-amp average channel current."* **Confirm the rating at the cart.** **[J] One charger per pit + 1** — two robots at one event cannot share one charger |
| Multi-function smart charger (alternative) | goBILDA | **`44370`** Hitec RDX2 200 AC/DC | — | 0–1 | **$139.99** | Buy | **VERIFIED 2026-08-21** SKU+price | Only if you want per-channel control. **Must still satisfy E511's 3 A average channel current [C]** |
| **20 A ATM mini blade fuses** | any auto-parts / goBILDA | Fuses category | 2 | **4–6** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | 🕐 **R601(A) [C].** Cheap, tiny, and it *will* blow at an event |

---

## 3. 🕐 Fasteners and hardware — the stock-out that stops everything

**[J] This is the least glamorous section and the highest-regret one.** A build stops at 10 p.m. over a $0.40 screw, and as of 2026-08-21 the emergency reorder may not even be possible.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **M4 Hardware Starter Pack (2,625 pcs)** | goBILDA | **`3201-0010-0001`** — in stock, "Staff Pick" | — | **1 shared** | **$139.99** | Buy | **VERIFIED 2026-08-21** ([gobilda.com/hardware-bundles](https://www.gobilda.com/hardware-bundles/)) | 🕐 **[J] Buy this in August.** Best hardware value found in two sessions of looking. Shared bench stock — `qty_per_robot = 0` |
| M4 Button Head Screw Assortment (600 pcs) | goBILDA | **`3201-0004-0002`** — in stock | — | **1–2** | **$54.99 ea** | Buy | **VERIFIED 2026-08-21** | |
| ~~M4 Socket Head Screw Assortment (600 pcs)~~ | goBILDA | ~~`3201-0004-0001`~~ | — | — | ~~$54.99~~ | — | **VERIFIED 2026-08-21: "OUT OF STOCK"** | 🕐 **The proof.** Confirmed on two separate goBILDA category pages this session |
| M5 Set-Screw Bundle (75 pcs) | goBILDA | **`3203-2806-0001`** — in stock | — | **1** | **$14.99** | Buy | **VERIFIED 2026-08-21** | |
| 2807 Series Shims Bundle (108 pcs) | goBILDA | **`3203-2807-0001`** — in stock | — | **1** | **$14.99** | Buy | **VERIFIED 2026-08-21** | **[J]** Shims are the parts that stop a build at 10 p.m. |
| 1502 Series Spacers Bundle (80 pcs) | goBILDA | **`3203-1502-0001`** — in stock | — | **1** | **$46.99** | Buy | **VERIFIED 2026-08-21** | |
| 1501 Series Standoffs Bundle (148 pcs) | goBILDA | **`3203-1501-0001`** — in stock | — | **1** | **$139.99** | Buy | **VERIFIED 2026-08-21** | **[J]** Optional if the Starter Kits cover your standoff needs — check the kit BOM first |
| 2803 Series Threaded Plates Bundle (70 pcs) | goBILDA | **`3203-2803-0001`** — in stock | — | **0–1** | **$54.99** | Buy | **VERIFIED 2026-08-21** | |
| **12-Piece Tool Set for M4 Hardware** | goBILDA | **`3201-0015-0001`** — in stock | 1 set | **2 sets** | **$69.99 ea = $139.98** | Buy | **VERIFIED 2026-08-21** | 🕐 **[J] One set per robot bin.** Sharing one hex-key set across two teams is a daily friction tax |
| Nylock nuts M4 / washers M4 | goBILDA | Nuts / Washers categories | 200+ | **400+** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** ([gobilda.com/hardware](https://www.gobilda.com/hardware/) subcategories verified 2026-08-21) | Starter Kits include ~200 locknuts per kit |
| Thread locker (blue, not red) | goBILDA | Thread Locker category | — | **1–2** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** (subcategory verified 2026-08-21) | **[J]** Vibration loosens everything over a season |

---

## 4. 🕐 Motion — shafting, bearings, hubs, chain, sprockets

**[C] R303** makes the COTS single-DoF families here explicitly legal: **A** linear slide kit, **B** linear actuator kit, **C** non-shifting gearbox, **D** pulley, **E** turntable, **F** lead screw, **G** single-DoF gripper; plus exceptions **H** ratchets, **I** holonomic wheels, **J** dead-wheel odometry kits.

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **8 mm REX Shaft Starter Pack** | goBILDA | **`3201-0008-0001`** — in stock | — | **1 shared** | **$199.99** | Buy | **VERIFIED 2026-08-21** ([gobilda.com/ftc-kits](https://www.gobilda.com/ftc-kits)) | 🕐 **[J] One pack covers a spread of lengths for both robots** — better than guessing individual lengths pre-kickoff |
| 8 mm / 12 mm REX shafting, individual lengths | goBILDA | Stainless Steel REX Shafting w/ E-Clip | 6–10 pcs | **12–20 pcs** | $3.69–$19.99 ea | Buy | **VERIFIED-UPSTREAM** family + range; **NEEDS-SKU-CHECK** per length | Top up the starter pack after kickoff when lengths are known |
| **8 mm REX Standoff Bundle (104 pcs)** | goBILDA | **`3203-1516-0001`** — in stock | — | **0–1** | **$119.99** | Buy | **VERIFIED 2026-08-21** | |
| **Flanged ball bearings** | goBILDA | `1601` Series (4–32 mm ID) / `1611` Series (8 mm REX ID) | 20 | **40** | ≈**$90–$150** | Buy | **VERIFIED-UPSTREAM** series+prices; **NEEDS-SKU-CHECK** per bore | 🕐 **[J] Buy far more than you think.** Bearings vanish. Kits include 20 flanged bearings each |
| Pillow blocks | goBILDA | `1602` / `1605` / `1606` / `1621` Series | 6–10 | **12–20** | ≈**$100–$180** | Buy | **VERIFIED-UPSTREAM** series+prices | **[J] The reason you don't need a mill** |
| Hubs — **clamping**, not set-screw | goBILDA | Classic Clamping, Hyper `1310`/`1313`/`1315`, Sonic, Servo (H25T) | 8–12 | **16–24** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **[J] Clamping beats set-screw every time** — see the set-screw failure mode in `VENDOR-ECOSYSTEMS.md` §3.8 |
| **8 mm chain (steel)** | goBILDA | **`3308-0008-1000`** | 1 | **2 + 1 spare** | **$11.99 ea ≈ $36** | Buy | **VERIFIED-UPSTREAM** | 🕐 **No cross-system substitute exists** (`VENDOR-ECOSYSTEMS.md` §3.5, "the hard wall"). Buy the spare |
| 8 mm chain (plastic) | goBILDA | **`3309-0108-0050`** | 1 | **2** | **$7.99 ea = $16** | Buy | **VERIFIED-UPSTREAM** | Lighter, quieter, lower load |
| **Chain tensioner** | goBILDA | **`1524-0001-0001`** Arc-Slot Tensioner Bracket | 2 | **4** | **$5.99 ea = $24** | Buy | **VERIFIED-UPSTREAM** | 🕐 **[J] The part teams wish they'd bought** |
| Sprockets, hub-mount plastic | goBILDA | `3311-0014-0016/-0020/-0024/-0042` (14 mm bore) | 4–8 | **8–16** | ≈**$30–$60** | Buy | **VERIFIED-UPSTREAM** SKUs+prices | Cheapest ratio experiments in the catalogue |
| Sprockets, clamping | goBILDA | `3302-4008-0014` (8 mm REX, 14T) / `3302-4012-0014` (12 mm REX) | 2–4 | **4–8** | **$12.99 ea** | Buy | **VERIFIED-UPSTREAM** | |
| Collars, couplers, shims, shaft spacers | goBILDA | Collars / Couplers / Shaft Spacers & Shims | assorted | assorted | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **[J]** Buy an assortment |
| Springs / gas shocks | goBILDA | Springs; Shocks | as needed | as needed | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **R801 [C]:** manufacturer-pre-charged sealed gas shocks are the **only** legal stored-air device. **[J] Springs cost zero R503 actuator slots — the highest-leverage allowance in the manual** |

---

## 5. Structure — the always-used stock

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **1120 Series U-Channel Bundle (17 pcs)** | goBILDA | **`3203-1120-0001`** — in stock | — | **1–2 shared** | **$219.99 ea** | Buy | **VERIFIED 2026-08-21** | 🕐 **[J] Buy long and cut** — **R302 [C]** permits modifying legal COTS and raw stock. A bundle beats guessing 27 individual length SKUs pre-kickoff |
| 1121 Series Low-Side U-Channel Bundle | goBILDA | **`3203-1121-0001`** — in stock | — | **0–1** | **$199.99** | Buy | **VERIFIED 2026-08-21** | Lighter/lower-profile superstructure |
| 1143 Series Mini Low-Side U-Channel Bundle (17 pcs) | goBILDA | **`3203-1143-0001`** — in stock | — | **0–1** | **$184.99** | Buy | **VERIFIED 2026-08-21** | For arms and light linkages |
| 1109 Series goRAIL Bundle (15 pcs) | goBILDA | **`3203-1109-0001`** — in stock | — | **0–1** | **$119.99** | Buy | **VERIFIED 2026-08-21** | |
| goRAIL Bracket Assortment (202 pcs) | goBILDA | **`3201-0003-0001`** — in stock | — | **0–1** | **$159.99** | Buy | **VERIFIED 2026-08-21** | **[J] You will always want more brackets than you planned** |
| Grid plates / pattern plates | goBILDA | Structure → Grid Plates, Pattern Plates | 2–4 | **4–8** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | The mounting surface for hubs and coprocessors |
| **Polycarbonate sheet** | any / REV | Polycarbonate sheet stock | 1 sheet | **2 sheets** | UNVERIFIED | **Fab stock** | **FAMILY-ONLY** | **R302 [C]** explicitly names *sheet stock* as a legal raw material. Cuts with hand tools. Guards, hoppers, deflectors |
| **3D printer filament (PLA+ / PETG / TPU)** | any | — | 2–3 kg | **4–6 kg** | ≈**$100–$180** | **Fab stock** | **UNVERIFIED** | 🕐 **[J] The single biggest fabrication lever you have without a mill.** Print in duplicate; a second identical part costs filament and time only |

---

## 6. Wire, connectors and electrical consumables

**[C] R609** requires appropriately sized insulated wire (Table 12-8) and **R610** mandates **specific wire colours** for the 12 V main power bus and the +5 V auxiliary bus. **Colour is an inspection item, not a preference — read both rules before buying spools.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Heat shrink tubing | goBILDA | **`3201-0005-0001`** | — | **1** | **$9.99** | Buy | **VERIFIED-UPSTREAM** | **R504(E) [C]**: insulation may be applied to electrical terminals |
| Zip ties (100 pk) | goBILDA | **`2909-0101-0100`** | 1 | **2** | **$4.99 ea = $10** | Buy | **VERIFIED-UPSTREAM** | |
| **Cinch-Straps hook & loop (4 pk)** | goBILDA | **`2909-0102-0250`** | 2 | **4** | **$3.99 ea = $16** | Buy | **VERIFIED-UPSTREAM** | **[J] Best battery retention method there is** |
| **Servo connector clips (6 pk)** | goBILDA | **`2917-0001-0001`** | 1 | **2** | **$5.99 ea = $12** | Buy | **VERIFIED-UPSTREAM** | 🕐 **[J] Stops the #1 cause of "the servo just stopped working"** |
| Braided cable sleeve (3 m) | goBILDA | **`2925-0008-3000`** | 1 | **2** | **$5.99 ea = $12** | Buy | **VERIFIED-UPSTREAM** | **R606 [C]:** the electrical system must be **inspectable** — tidy wiring is a rules requirement |
| Grommets (plastic 12-pk / rubber 14 mm 4-pk) | goBILDA | **`2911-0014-0001`** / **`2911-0014-0003`** | 1 | **2** | **$3.99 ea ≈ $16** | Buy | **VERIFIED-UPSTREAM** | Wire through a 14 mm centre hole without chafing |
| XT30 connector pairs | goBILDA | Wiring → XT30 category | 4 | **8** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** (category verified upstream) | **R601(B) [C]** permits XT30 and Anderson Powerpole |
| Servo extension cables (TJC8) | goBILDA | Wiring → TJC8 Servo category | 8 | **16** | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | One per servo, plus spares |
| Cable-carrier chain (1 m) | goBILDA | **`2924-1015-1000`** | 0–1 | **0–2** | **$19.99 ea** | Buy | **VERIFIED-UPSTREAM** | For wiring across an extending slide |

---

## 7. Actuator spares — and the R503 8+8 ceiling

> **[C] R503:** *"ROBOTS are limited to a total of 8 motors and 8 servos… for all MECHANISMS used in all configurations."* **[H] DECODE allowed 10 servos — this is a reduction, and prior-season designs may now be illegal.**
> **[C] The carve-out worth money:** vibration/autofocus motors inside COTS computing devices, and **motors integral to an unmodified COTS sensor (e.g. LIDAR, scanning sonar)**, *"do not count toward the limit in R503."*
> **[C] The other lever, from Table 12-1:** *"These motors may be used with or without the provided gearbox, and/or with any other compatible gearbox"* — **re-gear rather than re-buy.**

**[J] Do NOT buy mechanism-specific motors, servos, wheels or slide kits before kickoff.** Ratios, wheel type and reach are all game-dependent. **Buy spares of the families the Starter Kits already commit you to, and nothing else.**

| Item | Vendor | Product family / SKU | Qty per robot | Qty for 2 robots | Approx cost | Buy or Fab | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| **Spare drive motor** | goBILDA | Yellow Jacket `5203` series (8 mm REX) — match the ratio in your Starter Kits | — | **+1** | ≈**$55** | Buy | **VERIFIED-UPSTREAM** family+price; **NEEDS-SKU-CHECK** per ratio | 🕐 **[J] Non-negotiable.** A dead drive motor between matches ends a two-robot day. **MANUAL-SKU:** the 5201/5202/5203/5204 series is named in Table 12-1 **[C]** |
| Cheapest legal spare motor | REV | **`REV-41-1291`** HD Hex, 12 V | — | **1–2** | **$22.00 ea** | Buy | **VERIFIED-UPSTREAM**; **MANUAL-SKU** Table 12-1 | Cheapest motor on the legal list |
| **Spare servos** | goBILDA | Dual Mode `2000-0025-0002/-0003/-0004` — match your Starter Kits | — | **+2** | ≈**$74** | Buy | **VERIFIED-UPSTREAM**; `2000-0025-0003` is **MANUAL-SKU** in Table 12-2 **[C]** | **[J] Servos are the most-replaced actuator in FTC** |
| goBILDA Servo Starter Pack | goBILDA | **`3201-0007-0001`** — in stock | — | **0–1** | **$309.99** | Buy | **VERIFIED 2026-08-21** | **[J] Only if the two Starter Kits' servo complement is short.** Otherwise defer — servo *type* is game-dependent |
| Servo programmer | goBILDA | Servo Electronics category (one ships in the FTC Starter Kit) | — | 1 shared | NEEDS-SKU-CHECK | Buy | **FAMILY-ONLY** | **R504(C) [C]:** servos *"may be modified as specified by the manufacturer (e.g., setting soft limits or modification for continuous rotation)"* |
| ~~Servo Power Module~~ | ~~REV~~ | ~~`REV-11-1144`~~ | — | — | — | — | **VERIFIED-UPSTREAM: DISCONTINUED** | Named in Table 12-3 **[C]** — **legal, unbuyable.** Do not design around it |
| Servo Hub (if you need 6 V servo expansion) | REV | **`REV-11-1855`** — 6 ch, 7–15 V in, 5–7.4 V out, 15 A | 0–1 | **0–2** | **$90.00 ea** | Buy | **VERIFIED-UPSTREAM**; **MANUAL-SKU** Table 12-3 | Verify per-port limits against Table 12-3 before ordering |
| Servo Power Injector (alternative) | goBILDA | **`3125-0001-0001`** — 6 ch, 8–15 V in, 6 V out to 24 A | 0–1 | **0–2** | **$69.99 ea** | Buy | **VERIFIED-UPSTREAM**; **MANUAL-SKU** Table 12-3 | |

---

## 8. Fabricate now — no purchase order required

**[C] R304\*** permits pre-Kickoff fabricated items and reused designs. **[C] R302\*** permits modifying legal COTS parts and raw materials (*"sheet stock, extruded shapes, metals, plastic, rubber, and wood, and magnets"*). **[J] Everything here can be finished before September 12 and none of it depends on the game.**

| Fabricated item | Method | Per robot | For 2 robots | Confidence | Notes |
|---|---|---|---|---|---|
| **ROBOT SIGNS** | Print the FIRST template on robust backing | 2 | **4+ (both alliance colours)** | **[C]** R401/R402 | 🕐 **Make these in August, not on event morning.** R401: ≥2 per ROBOT, in ≥2 separate locations on opposite or adjacent surfaces **90° apart**, min **6.5 in wide × 2.5 in tall**, robust material, **supported by the frame**. R402: solid red **or** blue opaque rectangle, and **"cannot be powered"** |
| Control Hub / Driver Hub mounting tray | 3D print or cut polycarb | 1 | **2** | **[J]** | The one deliberate goBILDA↔REV interface (`VENDOR-ECOSYSTEMS.md` §4.3) |
| Battery mount / retention | 3D print + Cinch-Strap | 1 | **2** | **[J]** | |
| Cable-management clips | 3D print | many | **many** | **[J]** | Supports **R606 [C]** inspectability |
| Sensor and camera brackets | 3D print | 3–6 | **6–12** | **[J]** | |
| Practice chassis (both robots) | Assemble from the Starter Kits | 1 | **2** | **[C]** R304 | 🕐 **[J] The whole point of buying two kits in August.** Drivetrain CAD, SDK setup and driver practice all start before kickoff |
| **A duplicate print queue** | — | — | — | **[J]** | 🕐 **The two-robot discipline: every print job runs qty 2 immediately, and a third set as spares.** A part printed once is a part robot B does not have |

---

## 9. Deliberately NOT on this list — hold until kickoff

**[J] Every one of these is expensive, doubled, and game-dependent. Buying them now is a bet, not a hedge.**

| Item | Why it waits | What to do instead |
|---|---|---|
| **Viper-Slide / linear slide kits** | Stage count and travel depend on the expansion limits. **R105 [C] states the sizing constraints *"will be released at Kickoff."*** **Stamp `DEFERRED-R105`** | Know the SKUs and prices now so you can order in the first 48 h. **VERIFIED 2026-08-21:** 2-Stage 336 mm `3210-0003-0002` **$159.99**; 4-Stage 240 mm `3210-0004-0004` **$219.99**; 4-Stage 336 mm `3210-0003-0004` **$229.99**; Linear Actuator Kit 203 mm `3212-0001-0001` **$129.99** — all **In Stock** |
| **Mecanum wheel sets** | Strafing vs tank is a game call, and this is a **$340–600 line × 2 robots** — and it costs 2 R503 motor slots | Two Starter Kits already ship omni + traction wheels. Decide at kickoff |
| **Mechanism-specific motor ratios** | Ratio is game-dependent — and **Table 12-1 [C] lets you re-gear a motor you already own** | Buy spares in the ratio your Starter Kits use |
| **Intake Wheel Starter Pack** `3201-0014-0001` **$159.99** (VERIFIED 2026-08-21, In Stock) | Intake geometry depends entirely on the game element | Note the SKU; order in the first 48 h if the game needs a roller intake |
| **COTS drive chassis kits** — Strafer `3209-0001-0007` **$699.99**, BeeLine V2 `3209-0002-0002` **$649.99** (both VERIFIED 2026-08-21, In Stock) | **Legal** — **R301(A) [C]** explicitly exempts COTS drive CHASSIS. But **[J] $1,300–1,400 for two** duplicates what two Starter Kits already give you | Build the chassis from the Starter Kits. Revisit only if build hours, not dollars, are the binding constraint |
| **Vision coprocessor** (Limelight 3A, `LL_3A`) | ~$189 × 2, and the AUTO requirement is unknown | A webcam ships in each Driver Kit. **[C] R702 + Table 12-9, re-verified from the PDF 2026-08-22:** Table 12-9 *"Supported programmable vision coprocessors"* has **exactly one row — Limelight Vision Limelight 3A, `LL_3A`**. That is the *only* programmable vision coprocessor you may reprogram. **R702 Example 6 names three that are PROHIBITED: the OpenMV Cam, the Luxonis OAK-1, and the Limelight 3G** — note the **3G is banned while the 3A is allowed**, a one-character mistake that costs ~$400 across two robots. **Allowed** (treated as ordinary non-programmable coprocessors, per Examples 1–5): Adafruit BNO055 IMU, SparkFun OTOS, Digital Chicken Labs OctoQuad FTC Edition, optical-flow sensors, DFRobot HuskyLens, Charmed Labs Pixy2 |
| **Second REV Expansion Hub** `REV-31-1153` | **$275.00 ea — price VERIFIED 2026-08-22** ([revrobotics.com/rev-31-1153](https://www.revrobotics.com/rev-31-1153/)); page schema still reads **`OutOfStock`**. **$550 across two robots**, confirming the earlier estimate | **[J] Design so you do not need one** — see the port math in `LEGAL-PARTS-CONSTRAINTS.md` §5.2. **[C] R701(C)** permits *"no more than one additional REV Expansion Hub"*, so one per robot is the legal ceiling anyway |
| **Belt/pulley starter pack** ($210–240) | Only needed if the design uses belts | If bought, **buy ONE for both robots** — it is bench stock |

> **⚠️ One exception that is already late: field and game elements.** **[H]** AndyMark's pre-order cutoff — *"Orders received by 7-August-2026 will begin shipping after kickoff, beginning Monday, 14-September, 2026"* — **passed 14 days ago**, and *"All sales are final."* **Call AndyMark for a real ship date before assuming September 14.** For a two-team program sharing one shop, **[J]** one full game set beats two partial sets — unless the two teams practise at different sites.

---

## 10. Rollup and order sequence

### Cost rollup — list price, before discounts, before tax and shipping

| Block | For TWO robots | Basis |
|---|---|---|
| FIRST storefront: 2× Electronics Kit + 2× Driver Kit | **$1,220 at [H] 25-26 prices — budget ≈$1,220–$1,350 for 26-27** | 2×$325 + 2×$285, both **quoted verbatim** from the storefront options sheet **rev 25-26.4 (Feb 18 2026)**, **VERIFIED 2026-08-22**. Registration rose $325→$350 for 26-27, so **carry ~10% headroom**. Build Kit ($650 ea) deliberately excluded — see §1 |
| 2× goBILDA FTC Starter Kit `3200-4008-2627` | **$1,799.98 list → ≈$1,349.98 with the 25% team discount** | **VERIFIED 2026-08-21**, re-confirmed **2026-08-22** |
| Power: 5 batteries + 2–3 chargers + fuses | **≈$340–$360** | **VERIFIED 2026-08-21** ($60.00, $14.99) + FAMILY-ONLY fuses |
| Fasteners and hardware bundles + 2 tool sets | **≈$400–$540** | **VERIFIED 2026-08-21** ($139.99 + $54.99 + $14.99 + $14.99 + $46.99 + $139.98) |
| Motion: shaft pack, bearings, pillow blocks, hubs, chain, sprockets, tensioners | **≈$550–$800** | $199.99 **VERIFIED**; the rest VERIFIED-UPSTREAM ranges |
| Structure bundles (channel) | **≈$220–$440** | **VERIFIED 2026-08-21** |
| Wire, connectors, consumables | **≈$120–$200** | VERIFIED-UPSTREAM SKUs + FAMILY-ONLY |
| Actuator spares (+1 motor, +2 servos) | **≈$130** | VERIFIED-UPSTREAM |
| Filament 4–6 kg + polycarbonate sheet | **≈$120–$220** | UNVERIFIED |
| **PRE-KICKOFF SUBTOTAL (goBILDA discount applied, before tax/shipping)** | **≈ $4,050–$4,750** | **[D]** |
| *Excluded: 2× team registration* | *+$700* | *$350 ea — **[O-FTC] VERIFIED 2026-08-22**, firstinspires.org: "$350/season registration". Not a parts cost, **but it gates both storefront allocations**, so it is the first money that must move* |
| *Excluded and deliberately skipped: 2× storefront Build Kit* | *+$1,300* | *$650 ea **[H]**. Covered by the two goBILDA Starter Kits — see §1* |
| *Excluded and already late: AndyMark game set* | *+$599* | *VERIFIED-UPSTREAM* |

**[J] Read of the rollup:** roughly **$4.0–4.8k of pre-kickoff parts** puts two complete, identical, legal, practice-capable robots on the floor **before the game is known** — and about **65% of it is four purchase decisions** (two storefront bundles, two goBILDA kits). That is exactly the shape a low-mentor-hour program wants: few decisions, high coverage, everything duplicated. Cross-check the whole-program figure against the tiers in `research/SMALL-TEAM-ECONOMICS.md` §2 (**Tier B ≈ $7,240 all-in** is the honest number for a program that intends to advance — and that is a *one-team* figure; registration and the limit-one storefront kits are **per registered team**).

### If the budget clears in stages, order in this sequence

1. 🕐 **2× FIRST storefront Electronics Kits + 2× Driver Kits** — limit-one-per-team, and the control system blocks *everything*, including programming practice.
2. 🕐 **2× goBILDA FTC Starter Kit `3200-4008-2627`** — in stock today; last season's kit is already **Discontinued / Sold Out**.
3. 🕐 **M4 Hardware Starter Pack `3201-0010-0001` + bearings + tool sets** — fasteners are *already* stocking out.
4. 🕐 **Batteries (5), chargers (2–3), 20 A ATM fuses** — R601/E511 items **[C]**.
5. 🕐 **Spare motor ×1, spare servos ×2** — the parts that break.
6. 🕐 **Filament 4–6 kg + polycarbonate sheet** — your only real fabrication capacity.
7. 🕐 **Shaft starter pack, chain, tensioners, hubs** — the 8 mm chain island has no substitute.
8. **Structure bundles (channel)** — buy long, cut to fit under R302 **[C]**.
9. **Call AndyMark** about game elements — the cutoff has passed.
10. **Defer to kickoff:** slide kits, mecanum, final ratios, intake wheels, vision coprocessor.

### The ordering protocol (from `VENDOR-ECOSYSTEMS.md` §5.6 — [J], and it is cheap)

1. **One BOM, two quantities** — every line carries qty/robot and qty×2.
2. **Order both robots at once, always**, plus +1 spare on anything that can break in a match.
3. **One cart, one buyer, one card.**
4. **Buy the storefront kits per registered team immediately** — the limit-one rule is the whole financial reason two registrations pay.
5. **Anything on the critical path ships in the first 48 hours after kickoff**, even at the cost of ordering slightly wrong. *A wrong $60 motor beats a right motor that arrives in November.*
6. **Keep a live stock-status column** — copy the vendor's own string and the date you read it. Choose **ship-partial**, never ship-complete.

---

## 11. Before you order — the mandatory re-check

> **Every price and SKU above is "as of August 2026" and is `VERIFY-BEFORE-ORDER`.** Rows tagged **VERIFIED-UPSTREAM**, **FAMILY-ONLY** or **UNVERIFIED** have **not** been read off a live page in this session, and rows tagged **VERIFIED** were read on **2026-08-21** — which will be stale within weeks.
>
> **Run `reference/BOM-PROTOCOL.md` Step B6 on this entire list before placing any cart.** The copy-paste prompt is **P6** in `tools/bom/PROMPTS-bom.md`. Track the result in `tools/bom/BOM.template.csv`.

**The open register — what is still unresolved on this list:**

| Item | Status | Who resolves it |
|---|---|---|
| **2026-27 FIRST storefront prices** (Electronics Kit, Driver Kit, Build Kit) | **PARTLY RESOLVED 2026-08-22.** The workspace disagreement is settled against a primary source: storefront options sheet **rev 25-26.4, Feb 18 2026** — Driver **$285**, Electronics **$325**, Build **$650**, each *"limit one per registered team per season"*, registration **$325**. Those are **[H] 25-26**. For **26-27**, only registration is published: **$350** + supporting materials *"$1,500/estimated"* (**[O-FTC]**, firstinspires.org). **The 26-27 per-kit prices remain [U]** | Log in to the **FIRST Team Dashboard** (login-gated, not fetchable by an agent) and read the three kit prices. **Budget the [H] figures + ~10%** until you do |
| 20 A ATM fuses, nylock nuts, washers, thread locker, grid plates, hubs, collars, XT30/TJC8 wiring, springs/shocks | **FAMILY-ONLY / NEEDS-SKU-CHECK** | B6 fetch, per SKU |
| Bearing and pillow-block SKUs per bore | **VERIFIED-UPSTREAM** series and price ranges; **NEEDS-SKU-CHECK** per bore | B6 fetch |
| goBILDA charger `3101-0012-0001` charge rate vs **E511's 3 A average channel current [C]** | SKU and price **VERIFIED**; **rate not stated on the category page** | Read the product page at the cart |
| goBILDA / REV shipping policy and lead times | **UNVERIFIED** — both vendors' shipping pages returned **HTTP 404** | **[J] Plan 1–2 weeks in stock, 3–6 weeks backordered in Sep–Oct.** Confirm at order time |
| Studica catalogue | **UNVERIFIED** — site returned **HTTP 403** | Phone or email Studica if you need their parts |
| AndyMark game-set ship date after the passed Aug 7 cutoff | **UNVERIFIED** | Phone AndyMark |

---

*Detail and reasoning: `reference/VENDOR-ECOSYSTEMS.md` §6. Procedure: `reference/BOM-PROTOCOL.md`. Prompts: `tools/bom/PROMPTS-bom.md`. Tracking sheet: `tools/bom/BOM.template.csv`.*
