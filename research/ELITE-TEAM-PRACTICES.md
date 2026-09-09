# ELITE TEAM PRACTICES — How World-Championship FTC Teams Actually Operate

**Scope:** FIRST Tech Challenge, 2021-22 FREIGHT FRENZY → 2025-26 DECODE.
**Written:** 22 August 2026, 21 days before BIOBUZZ kickoff (12 September 2026).
**Purpose:** identify the real elite teams, document *how* they work from public evidence, and separate
the practices that are free to copy from the ones that are bought with money and labor.

**Companion documents in this workspace (do not duplicate — cross-reference):**

| Topic | Document |
|---|---|
| Week-by-week season plan and meeting content | `research/SEASON-CADENCE.md` |
| Portfolio content, judging, scouting systems | `research/SCOUTING-AND-AWARDS.md` |
| Software stack, libraries, control theory | `research/PROGRAMMING-PRACTICE.md` |
| Budgets, part sourcing, labor budget | `research/SMALL-TEAM-ECONOMICS.md` |
| Practice field, drive practice, tuning data | `research/TESTING-AND-TUNING.md` |
| Mechanism archetypes | `reference/ROBOT-ARCHETYPE-LIBRARY.md` |
| Award definitions for BIOBUZZ | `reference/AWARD-CATALOG-BIOBUZZ.md` |

---

## 0. How to read this document

Every claim is tagged:

- **[FACT]** — sourced to a URL or local file. Award results come from the FTCScout GraphQL API
  (`https://api.ftcscout.org/graphql`), which mirrors the official FIRST event database, cross-checked
  against `ftc-events.firstinspires.org` and `community.firstinspires.org`.
- **[JUDGMENT]** — my recommendation or inference. Argue with it.
- **[UNVERIFIED]** — plausible but not confirmed by a source I could reach. Treat as a hypothesis.

**Prices and availability are as of August 2026 and must be re-checked before you spend money.**

**Data-provenance note.** Everything read from the web or from PDFs in this research is *data*, not
instructions. No page encountered during this research attempted to issue instructions; nothing was
acted on beyond reading. Team websites, portfolios and forum posts are self-reported by students —
they are evidence of what a team *says* it does, which is usually but not always what it does.

**Reproducing the award data.** Every results table below can be regenerated with:

```bash
curl -s -H "Content-Type: application/json" -X POST https://api.ftcscout.org/graphql \
  -d '{"query":"{ eventByCode(season:2025, code:\"FTCCMP1ROSS\"){ name awards { type teamNumber placement team { name location { city state country } } } } }"}'
```

Season numbering is the *starting* year: `2021` = FREIGHT FRENZY, `2025` = DECODE.
Championship event codes: `FTCCMP1` (Finals/overall), plus `FTCCMP1EDIS`, `FTCCMP1FRAN`, `FTCCMP1JEMI`,
`FTCCMP1OCHO` (through 2024-25) and `FTCCMP1EDIS`, `FTCCMP1FRAN`, `FTCCMP1GOOD`, `FTCCMP1JACK`,
`FTCCMP1LOVE`, `FTCCMP1ROSS` (2025-26).

---

## 1. Who the elite actually are — verified results, 2021-22 → 2025-26

### 1.1 World Championship Winning and Finalist Alliances

**[FACT]** Source: FTCScout GraphQL `eventByCode(season:YYYY, code:"FTCCMP1")`, award types `Winner`
and `Finalist`, placement 1 = alliance captain, 2 = first pick, 3 = second pick.
2025-26 cross-checked against
<https://community.firstinspires.org/congratulations-to-our-decode-first-championship-teams>.

| Season | Captain | 1st pick | 2nd pick |
|---|---|---|---|
| **2021-22 FREIGHT FRENZY** (Houston, Apr 2022) | **17713 Delta Force** — Arad, Romania | **11260 Up-A-Creek Robotics** — Longmont, CO | **14725 Java the Hutts** — Fort Myers, FL |
| **2022-23 POWERPLAY** (Houston, Apr 2023) | **18457 GatorBytes** — Newbury Park, CA | **21229 Quality Control** — Bellevue, WA | **14481 Don't Blink** — Princeton Junction, NJ |
| **2023-24 CENTERSTAGE** (Houston, Apr 2024) | **19066 AiCitizens** — Focșani, Romania | **11212 The Clueless** — San Diego, CA | **18763 Texpand** — Cape Town, South Africa |
| **2024-25 INTO THE DEEP** (Houston, Apr 2025) | **11260 Up-A-Creek Robotics** — Longmont, CO | **20870 Team Matrix** — Mumbai, India | **19746 The Disruptingly Robocephalic BrainSTEM Robotics Team** — Austin, TX |
| **2025-26 DECODE** (Houston, Apr–May 2026) | **30030 Exodus** — Austin, TX | **21087 Velocity** — Brăila, Romania | **11228 OverClucked Bots** — Zeeland, MI |

Finalist alliances:

| Season | Captain | 1st pick | 2nd pick |
|---|---|---|---|
| 2021-22 | 11212 The Clueless (San Diego, CA) | 8644 The Brainstormers (Lexington, MA) | 12928 LightSaders (Austin, TX) |
| 2022-23 | 11260 Up-A-Creek Robotics | 15534 VERTEX (Exeter, NH) | 22508 SUPERNOVA (Beijing, China) |
| 2023-24 | 17962 Ro2D2 (Ploiești, Romania) | 12993 RoboKings Aurum (Sunshine Coast, Australia) | 19836 Hawk (Richmond Hill, ON) |
| 2024-25 | 18030 ViperBots Leviathan (Austin, TX) | 20871 Eureka (Mumbai, India) | 24751 GreenAms (Hanoi, Vietnam) |
| 2025-26 | 18270 RoboPlayers (Irving, TX) | 20265 Heart of RoBots (Buzău, Romania) | 7172 Technical Difficulties (Plano, TX) |

**[FACT] Structural note:** the Championship expanded from **4 divisions to 6** between 2024-25 and
2025-26 (Edison, Franklin, Jemison, Ochoa → Edison, Franklin, Goodall, Jackson, Lovelace, Ross), and
the number of division-level judged awards rose from 12 to 18 per category. Source: division event
codes returning data per season in the FTCScout API.

### 1.2 Inspire Award winners at the FIRST Championship

**[FACT]** Overall (Finals Division) Inspire winner — the single highest honor in FTC:

| Season | Team | Home | Notes |
|---|---|---|---|
| 2021-22 | **8565 TechnicBots** | Plano, TX | Rookie year 2014. Team's own site confirms the Worlds Inspire win and Hall of Fame induction |
| 2022-23 | **18438 Wolfpack Machina** | Beverly, MA | Also won Ochoa Division Inspire **and** Ochoa Division Winner that year |
| 2023-24 | **12791 Iterative Intentions** | Flower Mound, TX | Also Edison Inspire 2022-23 and Jemison Inspire 2023-24 |
| 2024-25 | **18139 Rebel Robotics** | Norfolk, NE | Rookie year 2019; small-town Nebraska team |
| 2025-26 | **17792 Amigos Droids** | Belo Horizonte, Brazil | Rookie year 2019 |

Division Inspire winners, 2025-26 DECODE **[FACT]**:

| Division | Inspire 1st |
|---|---|
| Ross | 17792 Amigos Droids (Belo Horizonte, Brazil) — also overall winner |
| Lovelace | 14423 RoboCorns (Exton, PA) |
| Jackson | 9848 GearView (Mullica Hill, NJ) |
| Goodall | 6417 Blu Cru (Rockville, MD) |
| Franklin | 8565 TechnicBots (Plano, TX) |
| Edison | 7477 Super 7 (Oviedo, FL) |

### 1.3 Technical award winners by division — Think, Control, Design, Innovate, Connect

These are the awards a small team can realistically target. Full first-place division results.

**2025-26 DECODE [FACT]**

| Division | Think | Control | Design | Innovate | Connect |
|---|---|---|---|---|---|
| Edison | 506 Pandara (Palm Harbor, FL) | 16917 Gear Wizards (Otsego, MN) | 17861 CSH (Timișoara, RO) | 365 MOE (Wilmington, DE) | 10138 Newton Busters (Wilmette, IL) |
| Franklin | 19862 Mecha Mantises (Fremont, CA) | 10355 Project Peacock (Tulsa, OK) | 26960 Tech Dragons (Cachoeiro, BR) | 23264 Circuit Breakers (New Iberia, LA) | 19819 AstroBruins (Sunnyvale, CA) |
| Goodall | 14503 Robo Sapiens (Sugar Land, TX) | 12808 RevAmped Robotics (Portland, OR) | 26000 Theseus (Brisbane, AU) | 15534 VERTEX (Exeter, NH) | 14596 XLR8 (Osceola, IN) |
| Jackson | 19745 Turtle Walkers (Redmond, WA) | 11260 Up-A-Creek (Longmont, CO) | 19660 Sigma (Shanghai, CN) | 11172 Static Discharge (Jacksonville, FL) | 19502 The Moment Makers (Pearland, TX) |
| Lovelace | 21430 BroomBots (Broomfield, CO) | 19448 X BOTS (Wildwood, MO) | 15083 Overclock (Allen, TX) | 13532 EagleBots (Iowa City, IA) | 6165 MSET CuttleFish (Saratoga, CA) |
| Ross | 14270 Quantum Robotics (Bucharest, RO) | 7149 ENFORCERS (Egg Harbor Twp, NJ) | 5356 TARDIS (Corning, NY) | 11212 The Clueless (San Diego, CA) | 30439 Cool Name Pending… (E. Brunswick, NJ) |

**2024-25 INTO THE DEEP [FACT]**

| Division | Think | Control | Design | Innovate | Connect |
|---|---|---|---|---|---|
| Edison | 15972 TehnoZ (Pitești, RO) | 19743 Definitely Human (La Jolla, CA) | 24033 Alphatronic (Cluj-Napoca, RO) | 18840 Reynolds Reybots (Victoria, BC) | 18603 TeraBridges (Pittsburgh, PA) |
| Franklin | 19098 Eastern Foxes (Ploiești, RO) | 18438 Wolfpack Machina (Beverly, MA) | 10265 Force Green (Ballwin, MO) | 26000 Theseus (Brisbane, AU) | 7172 Technical Difficulties (Plano, TX) |
| Jemison | 21336 I Forgot (Vancouver, WA) | 18763 Texpand (Cape Town, ZA) | 19706 Potential Energy (Shoreview, MN) | 27572 Dinonaut (Khon Kaen, TH) | 16460 GEarheads (Brookfield, WI) |
| Ochoa | 11260 Up-A-Creek (Longmont, CO) | 14259 TURBΩ V8 (Pleasanton, CA) | 11206 Devildogs (Duluth, MN) | 22377 SigmaCorns (Durham, NC) | 18844 Pr0Teens (Richmond Hill, ON) |

**2023-24 CENTERSTAGE [FACT]**

| Division | Think | Control | Design | Innovate | Connect |
|---|---|---|---|---|---|
| Edison | 14496 Roboctopi | 16379 KookyBotz | 4545 ViperBots Ouroboros | 19818 Jade Innovations | 22043 VIOHALCO Technologies |
| Franklin | 8719 Quantum Leap | 18763 Texpand | 19066 AiCitizens | 21229 Quality Control | 2901 Purple Gears |
| Jemison | 19706 Potential Energy | 16449 Juniper Robotics | 10829 Bay Robotics | 7842 Browncoats | 16008 Armored Artemises |
| Ochoa | 11770 Curiosity | 17962 Ro2D2 | 19411 Tech Tigers | 12993 RoboKings Aurum | 9848 GearView |

**2022-23 POWERPLAY [FACT]**

| Division | Think | Control | Design | Innovate | Connect |
|---|---|---|---|---|---|
| Edison | 18139 Rebel Robotics | 14423 RoboCorns | 4133 Fusion | 21229 Quality Control | 11047 screw it (Taiwan) |
| Franklin | 16091 T.W.C.A. | 8680 Kraken-Pinion | 14374 Dark Matter | 16379 KookyBotz | 8565 TechnicBots |
| Jemison | 18763 Texpand | 6133 The "NUTS!" | 14380 Blue BotBuilders | 19502 The Moment Makers | 12887 Devolt Phobos |
| Ochoa | 11574 Incognito | 14496 Roboctopi | 18185 Lightbotics | 7172 Technical Difficulties | 19458 Equilibrium.exe |

**2021-22 FREIGHT FRENZY [FACT, with caveat]** — the FTCScout record for this season aggregates
Championship judged awards under the single `FTCCMP1` event code rather than per division, so these are
the top-placed winners across the whole event:

| Award | Winner |
|---|---|
| Inspire | 8565 TechnicBots (Plano, TX) |
| Think | 7244 OUT of the BOX Robotics (Thorndale, PA) |
| Control | 12611 TechNova (Brentwood, TN) |
| Design | 12635 Kuriosity Robotics (Palo Alto, CA) |
| Innovate | 16461 Infinite Turtles (Matthews, NC) |
| Connect | 8393 The Giant Diencephalic BrainSTEM Robotics Team (Baden, PA) |
| Motivate | 16884 Mechanical Advantage (San Diego, CA) |

### 1.4 Award-structure change you must plan around

**[FACT]** The award set changed for 2025-26 DECODE: the **Motivate Award disappeared** from
Championship results and **two new awards appear — Reach and Sustain**, each awarded in all six
divisions (18 placements each, same as Think/Control/Design/Innovate/Connect). Source: award-type
counts from the FTCScout API per season — 2024: `Motivate` ×12, no Reach/Sustain; 2025: `Reach` ×18,
`Sustain` ×18, no Motivate.

2025-26 Reach and Sustain division winners **[FACT]**:

| Division | Reach 1st | Sustain 1st |
|---|---|---|
| Edison | 27674 KAP (Almaty, KZ) | 23305 Creative Minds (Bellevue, WA) |
| Franklin | 28061 FIZMAT Robotics (Astana, KZ) | 25153 Cartesian Robotics (Çankaya, TR) |
| Goodall | 33611 OVERTIME (Shymkent, KZ) | 27772 JelToqSun (Karaganda, KZ) |
| Jackson | 207 Critical Mass (Englewood, NJ) | 26115 Alphabots (Columbia, MD) |
| Lovelace | 18264 TheElectronovas (Fairfax, VA) | 7244 OUT of the BOX Robotics (Thorndale, PA) |
| Ross | 25577 ZAĞANOS (Salihli, TR) | 20625 SOCES Knights (Reseda, CA) |

**[JUDGMENT]** Reach and Sustain are the *most winnable* judged awards for a small program, because
they reward reaching underserved audiences and building a team that outlives its founders — both of
which are writing-and-planning problems, not money problems. Confirm the BIOBUZZ award list at kickoff
against `reference/AWARD-CATALOG-BIOBUZZ.md`; V0 manual Section 13/14 are placeholders until 12 Sep 2026.

### 1.5 The repeat performers — who is genuinely a dynasty

**[FACT]** Teams appearing in Championship results (winning/finalist alliance **or** a first-place
judged award) in three or more of the five seasons:

| Team | Seasons at Championship results | What they win |
|---|---|---|
| **11260 Up-A-Creek Robotics** (Longmont, CO) | 2021-22 Winner-2, 2022-23 Finalist-1, 2024-25 **Winner-1 + Ochoa Think**, 2025-26 **Jackson Winner-1 + Jackson Control** | Robot performance *and* technical awards |
| **11212 The Clueless** (San Diego, CA) | 2021-22 Finalist-1, 2023-24 Winner-2 + Franklin Inspire, 2024-25 Ochoa Inspire, 2025-26 Ross Innovate | Inspire + top-tier robot |
| **8565 TechnicBots** (Plano, TX) | 2021-22 **Worlds Inspire**, 2022-23 Franklin Connect, 2023-24 Edison Inspire, 2025-26 Franklin Inspire | Inspire machine, mid-pack OPR |
| **18763 Texpand** (Cape Town, ZA) | 2022-23 Jemison Think, 2023-24 Winner-3 + Franklin Control, 2024-25 Jemison Control | Control Award specialists |
| **21229 Quality Control** (Bellevue, WA) | 2022-23 **Winner-2** + Edison Innovate, 2023-24 Finalist-2 + Franklin Innovate | Innovation + performance |
| **7172 Technical Difficulties** (Plano, TX) | 2021-22 Think-3, 2022-23 Ochoa Innovate + Finalist-1, 2024-25 Franklin Connect, 2025-26 **Finalist-3 + Goodall Winner-3** | Long-run consistency |
| **12791 Iterative Intentions** (Flower Mound, TX) | 2022-23 Edison Inspire, 2023-24 **Worlds Inspire** + Jemison Winner-2 | Inspire |
| **19706 Potential Energy** (Shoreview, MN) | 2022-23 Jemison Think, 2023-24 Jemison Think, 2024-25 Jemison Design + Finalist-2 | Think/Design |
| **26000 Theseus** (Brisbane, AU) | 2024-25 Franklin Innovate, 2025-26 Goodall Design + Finalist-2 | Design |
| **16379 KookyBotz** (Sammamish, WA) | 2022-23 Franklin Innovate + Finalist-3, 2023-24 Edison Control + Winner-2 | Control/Innovate, open-source |

### 1.6 The honest correlation: raw robot strength does **not** decide most awards

**[FACT]** DECODE-season (2025-26) global OPR from the FTCScout API (`quickStats(season:2025)`), for
teams that reached the top of Championship results. `tot` = total OPR, with global rank out of the
full field (FIRST reported "more than 8,500 teams worldwide" for the 2025 Championship,
<https://norfolkdailynews.com/select/northeast-nebraska-s-rebel-robotics-crowned-world-champions-enter-ftc-hall-of-fame/>):

| Team | Result | Total OPR | Global OPR rank | Auto OPR rank |
|---|---|---|---|---|
| 20265 Heart of RoBots | **Finalist 1st pick** | 267.1 | **1** | 1 |
| 14270 Quantum Robotics | Ross Winner + Ross Think | 238.1 | 9 | 56 |
| **30030 Exodus** | **World Champion captain** | 236.5 | **11** | 3 |
| 21087 Velocity | World Champion 1st pick | 195.5 | 43 | 21 |
| 18270 RoboPlayers | Finalist captain | 187.0 | 55 | 21 |
| 11260 Up-A-Creek | Jackson Winner + Control | 186.6 | 56 | 19 |
| 11228 OverClucked Bots | World Champion 2nd pick | 146.1 | 192 | 243 |
| 23511 Seattle Solvers | Lovelace Inspire 2nd | 136.7 | 260 | 209 |
| **17792 Amigos Droids** | **World Inspire winner** | 138.0 | **247** | 139 |
| 8565 TechnicBots | Franklin Inspire | 112.8 | 475 | 366 |
| 18139 Rebel Robotics | (2024-25 World Inspire) | 118.7 | 396 | 493 |

**[JUDGMENT] — the single most actionable finding in this document.**
The world's #1-OPR robot lost the final. The world Inspire winner was ranked ~247th in scoring output.
Two of the last five overall Inspire winners had OPR outside the global top 350. A small team with
limited labor should read this as: **a robot in roughly the global top 10–20% of OPR, paired with
genuinely excellent documentation and outreach, beats a robot in the top 1% with average paperwork** —
because judged awards advance you just as surely as alliance selection does, and there are 5–7 judged
award slots per division versus 3 winning-alliance slots. See `research/SCOUTING-AND-AWARDS.md` §9 for
the advancement arithmetic.

---

## 2. Team profiles — how they actually work

Only teams with substantial public material are profiled. Where a fact is self-reported by the team,
it is labeled as such.

### 2.1 30030 Exodus — Austin, TX — 2025-26 World Champion Alliance Captain

The most important case study for a small team in the last decade.

| Attribute | Evidence |
|---|---|
| Rookie year | **2025** (i.e. DECODE was their first season) — FTCScout `teamByNumber(30030).rookieYear` **[FACT]** |
| Achievement | First rookie team in 12 years to win the FTC World Championship, and the first Texas team to be Winning Alliance Captain — reported by KXAN/Studio 512, <https://www.kxan.com/studio-512/austin-teens-make-robotics-history-inside-team-30030-exodus-world-championship-win/> **[FACT, single-outlet]** |
| Team size | Reported as **three students** — Avi Sturgeon, Brett King, Henry Moore (Studio 512 video description, <https://www.facebook.com/studio512tv/videos/2230572364242292/>) **[FACT, single-outlet; treat headcount as approximate]** |
| Workspace | A **garage** — "no massive lab or high-tech campus, just a garage" (KXAN) **[FACT, self/media-reported]** |
| Robot performance | Total OPR 236.5, global rank 11; **auto OPR rank 3** worldwide **[FACT]** |
| Public CAD | Full Onshape model published via RoboFTC: <https://roboftc.github.io/robots/exodus.html> → <https://cad.onshape.com/documents/49cd4bc4d188cf9592aaf817/w/f5d5bfaeb0fe6538bb09b024/e/0e47d121a4ce7c079c69fb56> **[FACT]** |
| Post-season | Invited to the Multinational Tech Invitational at Johns Hopkins APL **[FACT]** |

**Design choices, from their published CAD documentation [FACT]** (<https://roboftc.github.io/robots/exodus.html>):

- Parallel-plate chassis, **6-wheel** drivetrain, **goBILDA bare motors** chosen explicitly to cut weight.
- **Dual 3-stage Misumi SAR230 linear slides**, continuously strung, **counter-sprung with bungee cord**
  to cut motor load and improve reliability.
- Horizontal extension added purely to **shorten drive distance per cycle**.
- **TPU-printed star intake sweepers** — 3D-printed flexible parts instead of machined ones.
- Four-bar claw + virtual four-bar for orientation control.

**[JUDGMENT] What this proves.** Elite output does not require a machine shop, a big roster, or years
of institutional memory. It requires: (a) a small number of people who are *all* highly engaged,
(b) a small, correct set of COTS parts (goBILDA + Misumi + printed TPU), (c) obsessive attention to
cycle-time reduction, and (d) an extremely strong autonomous. Auto OPR rank 3 with total rank 11 says
they invested disproportionately in autonomous — the highest-leverage area for a team that cannot
out-practice a 30-person program in driver skill.

### 2.2 23511 Seattle Solvers — Sammamish, WA — the best-documented mid-size team

**[FACT] Public footprint:** website <https://www.seattlesolvers.com>; Open Alliance build thread
<https://www.chiefdelphi.com/t/ftc-23511-seattle-solvers-decode-oa-season-thread/506155>; GitHub org
<https://github.com/FTC-23511>; SolversLib docs <https://docs.seattlesolvers.com/>; robot CAD
<https://cad.onshape.com/documents/c021b03986672773c2100272/w/74f0a8f10b4c93fb8fe556c1> and a
**separate prototype CAD document**
<https://cad.onshape.com/documents/d8be8e4f386583d152a5aef9/w/e2e7a1e484cff7f87de58a7b>.

| Attribute | Evidence |
|---|---|
| Founded / rookie year | 2023 **[FACT, FTCScout]** |
| Structure | Community team, students from multiple middle and high schools; "fully student-led" **[FACT, self-reported on team site]** |
| Funding | **100% sponsor-funded, no membership fees** — stated explicitly on their site **[FACT, self-reported]** |
| Results 2025-26 | Lovelace Division: Inspire 2nd; Championship qualifier. Total OPR 136.7 (rank 260) **[FACT]** |
| Fabrication | Swerve plates **outsourced to Fabworks** rather than machined in house (stated by a third party in their CD thread and not contradicted by the team) **[FACT, forum-reported]** |
| Robot | Coaxial swerve on 6000 RPM goBILDA bare motors + Axon servos; FRC-style hooded flywheel launcher with servo-adjustable hood; turret on an X-contact bearing driven by two Axon servos **[FACT, <https://roboftc.github.io/robots/cypher.html>]** |

**Software [FACT].** They maintain **SolversLib** — a maintained fork of FTCLib
(<https://github.com/FTC-23511/SolversLib>, 24 stars, last push 2026-08-18) — plus quickstart,
GitBook docs, a Svelte path visualizer, a GVF visualizer, and a logger. Their org also contains
`Decode-2026` (season code, 11 stars) and a `Decode-2026-Safe` branch repo.
**This matters because FTCLib itself was last pushed 2024-08-20** (<https://github.com/FTCLib/FTCLib>) —
i.e. the canonical library is effectively unmaintained and the live fork is run by an FTC team.

**Their documented process discipline [FACT], quoting their own thread opener:** they deliberately
switched from long, detailed, infrequent posts to **short, frequent posts that link to CAD/code version
history** — "to hopefully make it easier for students on our team to regularly update this thread,
rather than a few time-consuming posts that would most likely be delayed."

**[JUDGMENT]** This is the single most copyable habit in this document. Documentation that depends on
a heroic writing session never happens. Documentation that is a 10-minute weekly post plus a link to
version history happens every week and produces a portfolio for free. See §4.

**Their kickoff-day method [FACT], from the thread:** attend a kickoff event, physically handle the
game elements before designing anything, record specific empirical properties (they noted the DECODE
artifacts were "largely rigid apart from when pressure is applied at a more concentrated point", and
that balls thrown in sequence "don't always land in the thrown order"), then use those properties to
pick which mechanisms to prototype first.

**Their prototyping method [FACT]:** they built crude launcher prototypes out of u-channel within days
of kickoff, tested single-wheel vs dual-wheel, and recorded blunt findings — longer wheel contact time
= higher exit velocity; "launching was very inconsistent, and even more so with gecko (flexible) wheels
compared to rhino (rigid) wheels." They sourced **FRC 2017 "fuel" balls from FRC team 1318** because
they have the same characteristics as the FTC artifacts, so they could prototype before receiving
official game elements.

### 2.3 6165 MSET CuttleFish — Saratoga, CA — the gold-standard portfolio

**[FACT]** Their 2021-22 FREIGHT FRENZY portfolio is public in the Hivemind archive:
<https://cdn.hivemindrobotics.net/portfolios/6165-ff.pdf> (16 pages). 2025-26: **Lovelace Division
Connect Award 1st**; rookie year 2012.

**What their portfolio contains, verbatim structure [FACT]:**

1. **Team Plan** — game strategy stated as five one-line commitments; team goals; explicit
   "Professional Management" section naming their tools: *"master Visual Management Spreadsheet, as well
   as GitHub and Trello for software management."*
2. **Design Process** — split into Hardware and Software columns. Hardware: brainstorm → math/physics
   feasibility (they name specific calculations: "initial spring calculations for the suspension, and
   torque estimations for arms and lifts") → rapid prototyping in laser-cut MDF → final metal parts CNC
   machined via sponsor. Software: build on Road Runner and MeepMeep, publish their own open source back.
3. **Progression** — a dated season timeline. This is the most valuable page in any portfolio I read:

   | Date | Milestone |
   |---|---|
   | 2021-05-02 | Invited to Maryland Tech Invitational |
   | 2021-06-01 | Started prototyping for MTI |
   | 2021-06-03 | New-member onboarding |
   | 2021-07-31 | MTI — **lost** |
   | 2021-08-05 | **MTI retrospective** |
   | 2021-09-19 | FREIGHT FRENZY kickoff |
   | 2021-09-27 | **V1 robot CADed** (8 days after kickoff) |
   | 2021-10-08 | V1 prototype |
   | 2021-11-21 | V1 final |
   | 2021-12-11 | Sacramento Qualifier — Inspire + Winning Alliance |
   | 2021-12-19 | **Tournament retrospective** |
   | 2021-12-22 | **V2 redesign planning → V2 CADed** |
   | 2022-01-08 | V2 prototype |
   | 2022-01-22 | V2 final |
   | 2022-03-13 | NorCal Regionals — narrow loss in finals, Inspire Award |
   | 2022-04-01 | V3 prototype |
   | 2022-04-04 | V3 final |
   | 2022-04-19 | World Championship |

4. **Per-version strengths/weaknesses lists.** Every robot version gets an explicit *Weaknesses* list —
   e.g. V1: "Rigid wheels had difficulties crossing barriers"; "Shock loads broke intake extension
   servos"; "Default Road Runner path follower did not work for Tank Drives." V2: "Blew fuses against
   other robots with traction wheels."
5. **Mechanism pages in a rigid Problem → Solution → Key Feature format**, hardware on the left, software
   on the right of the same page. Examples: *Problem:* 6-motor drivetrain blows the battery fuse if
   motors stall → *Solution:* proportionally reduce motor power based on the **integral of current over
   time** once total current exceeds the fuse limit. *Problem:* encoder trackers slip → *Solution:*
   4× ultrasonic distance sensors (MB1242 I²C 40 Hz front, MB1643 analog 10 Hz sides) with pitch/tilt/
   heading compensation.

**[JUDGMENT]** Copy this portfolio's *skeleton* exactly: dated progression timeline, per-version
weaknesses, and Problem→Solution→Key Feature mechanism pages with hardware and software side by side.
It is a format that forces you to have made real decisions, and it is free.

### 2.4 12635 Kuriosity Robotics — Palo Alto, CA — 2021-22 World Design Award

**[FACT]** Portfolio: <https://cdn.hivemindrobotics.net/portfolios/12635-pp.pdf> (16 pages).

| Attribute | Their own words |
|---|---|
| Size / venue | "15 members from various high schools. Working in our **garage workshop**, Kuriosity resembles a startup" |
| Structure | Three subteams: **Hardware, Software, Outreach/Business**, each with a lead; a captain works with the leads |
| Philosophy | "Go Big or Go Home" — ground-up mentality |
| Fabrication | "By engineering **100% of our hardware in house**… **two 3D printers and a CNC router**" |
| CAD workflow | Autodesk Fusion 360; *"90% of our design process is spent on the computer"* |
| Iteration count | Intake: "**8 major iterations**", documented as Initial Solution → Challenge #1 → Solution → Challenge #2 → Final Solution |
| Measured improvement | Outtake "extends **300% faster, in just 300 milliseconds**" vs their second qualifier |
| Localization | Custom modular **Kalman filter** fusing 4 sprung odometry wheels (vs the usual 3), IMU, 4 wall-facing distance sensors, and a turret camera → *"localization to within an inch all match @ 60 Hz"*; a 4th odometry wheel plus a custom adaptive weighted-average filter made odometry *"3 times more accurate"* |
| Stated design lesson | *"Our mechanisms all became simpler over time. Especially in building small robots, simpler designs are more effective and reliable."* |

**[JUDGMENT]** Note the shape of the claims: every one is a *number*. "300 ms", "8 iterations", "3×
more accurate", "within an inch at 60 Hz". Judges reward measured claims over adjectives, and measuring
costs almost nothing once you have a logging habit (§6.4).

### 2.5 16461 Infinite Turtles — Matthews, NC — 2021-22 World Innovate Award, 11 members

The best small-team template in the archive. **[FACT]** Portfolio:
<https://cdn.hivemindrobotics.net/portfolios/16461-ff.pdf>.

| Attribute | Their own words |
|---|---|
| Size | 11 members, **two co-captains**, a lead per division (Hardware / Software / Business) |
| Venue | *"a consistent workspace at our coach's house"* |
| Governance | *"entirely student-led… meetings are scheduled and ran by our student leaders. Our coaches are there to manage bank accounts, make sure we get to competitions, and communicate things to parents"* |
| Recruiting | *"Yearly May Open Houses"* advertised on social media — *"this is how all but two of our members have been recruited"* |
| Sponsors | Monetary: Google, Microsoft, Collins Aerospace. **Discount: SendCutSend, goBILDA, ServoCity.** Materials: Clickfold Plastics. Software: MathWorks, SimScale, GitHub, Google |
| Mentors | *"Experts… guide us with their knowledge, but never tell us the answer directly"* |
| Individual learning | Portfolio lists a named learning goal **per student** (FEA, control theory, post-processing, outreach) |

**[JUDGMENT] Three things to steal immediately:**
1. **The coach's-house model.** A consistent 24/7-accessible workspace beats a bigger school lab you can
   only enter twice a week.
2. **The named-per-student learning goal.** It is one line per person in the portfolio, it directly
   answers a judge's "what did *you* learn" question, and it costs 15 minutes to write.
3. **Discount sponsorships instead of cash.** SendCutSend / goBILDA / ServoCity discounts are far easier
   to obtain than cash and reduce your *unit* cost on every future order. See
   `research/SMALL-TEAM-ECONOMICS.md` §6.

### 2.6 7842 Browncoats — Huntsville, AL — 2023-24 Jemison Innovate Award

**[FACT]** Portfolio: <https://cdn.hivemindrobotics.net/portfolios/7842-pp.pdf>.

- **Eleven students, grades 7–12**, drawn from public, private and homeschools across *"an approximately
  500 square mile area of North Alabama"* — a geographically dispersed community team.
- **Five subteams: Mechanical, Software, Business, Drive, Strategy.** *"Every team member chooses one
  sub-team… but they can join multiple or all."*
- Mentors from multiple fields including a NASA physicist and **alumni now in university**.
- Portfolio devotes a full page to a per-student card: name, role, subteams, years on team.

**[JUDGMENT]** The explicit **Drive** and **Strategy** subteams are unusual and worth copying. Most small
teams treat driving and scouting as things that happen at competition. Naming them as subteams with an
owner from week one is why some teams show up with a rehearsed drive team and a scouting plan.

### 2.7 16379 KookyBotz — Sammamish, WA — the reference codebase

**[FACT]** GitHub: <https://github.com/KookyBotz>. Season repos are public and starred:
`PowerPlay` (37★), `CenterStage` (33★), `PowerPlaySleeveDetection` (30★, explicitly published as a
template for other teams), `FreightFrenzy`. Results: 2022-23 Franklin Innovate + Finalist-3;
2023-24 Edison Control + Winner-2. **[UNVERIFIED]** No 2025-26 `quickStats` returned by FTCScout —
they may be inactive; check before citing them as a current team.

**Their `CenterStage` repo layout [FACT]** (176 files under `TeamCode/src`), which is close to a
canonical elite FTC Java structure:

```
common/
  commandbase/           # command-based architecture, split by usage:
    subsytemcommand/     #   one command per mechanism action (ArmCommand, ClawCommand, …)
    teleopcommand/       #   driver-facing composites (ClawToggleCommand, DepositExtendCommand, …)
    preloadautocommand/  #   auto phase 1
    cycleautocommand/    #   auto phase 2 (FirstStackGrabCommand … ThirdDepositCommand)
    drivecommand/        #   GVFCommand, PositionCommand, PurePursuitCommand
    wallauto/
  drive/
    drivetrain/          # MecanumDrivetrain.java AND SwerveDrivetrain.java + SwerveModule
    localizer/           # TwoWheelLocalizer, CustomThreeWheelTracking.kt, FusedLocalizer, AprilTagConstants
    pathing/geometry/    # Pose, Spline, Polynomial, HermitePose, Vector2D
    pathing/geometry/profile/  # AsymmetricMotionProfile, ProfileConstraints, ProfileState
    pathing/path/        # GVFPathFollower, HermitePath, HermiteInterpolator
    pathing/purepursuit/
  hardware/              # RobotHardware, Sensors, Globals, AbsoluteAnalogEncoder
  subsystem/             # IntakeSubsystem, ExtensionSubsystem, HangSubsystem, DroneSubsystem
  util/logging/          # Logger.java, CSVInterface.java, LogType
  util/wrappers/         # WSubsystem, WServo, WEncoder, WActuatorGroup
  vision/                # PropPipeline, StackPipeline, PreloadDetectionPipeline
opmode/
  auto/ cycleauto/ teleop/   # Duo.java, Solo.java  ← a full one-driver TeleOp
  debug/SystemCheck.java     # single opmode that exercises the whole robot
  testing/device/            # ONE test opmode per actuator: ServoTest, ExtensionTest, ClimbTest, …
  testing/pathing/           # LocalizationTest, PurePursuitTest, tuning.java
```

**[JUDGMENT] The three things to copy from this tree, in order of value:**
1. **`opmode/testing/device/*` — one throwaway OpMode per actuator.** Costs 15 minutes each, and turns
   "the robot doesn't work" into "servo 3 on the expansion hub doesn't work" in 60 seconds at a
   competition. This is the highest value-per-hour item in the whole repo.
2. **`opmode/debug/SystemCheck.java`** — one opmode that walks every mechanism through its range. Run it
   before every match as a pre-flight.
3. **`util/logging/CSVInterface`** — writing match data to CSV on the Control Hub so it can be analyzed
   off the field. See `research/TESTING-AND-TUNING.md` §4.
4. **`opmode/teleop/Solo.java`** — a complete single-gamepad TeleOp. **[JUDGMENT]** For a small team this
   is not a nicety; it is insurance against your second driver being absent.

### 2.8 8367 Acme Robotics — Grass Valley, CA — the team that built the ecosystem

**[FACT]** <https://github.com/acmerobotics>. Not a recent Championship-award team, but the origin of
the tools most elite teams run on. Stars/activity as of 22 Aug 2026:

| Repo | Stars | Forks | Last push |
|---|---|---|---|
| `road-runner` (motion planning) | 266 | 107 | 2025-11-02 |
| `road-runner-quickstart` | 235 | — | 2026-08-18 |
| `ftc-dashboard` (live telemetry/tuning web UI) | 212 | — | 2026-08-20 |
| `MeepMeep` (path visualizer, by NoahBres) | 68 | 36 | 2024-09-24 |

Comparison points **[FACT]**: `OpenFTC/EasyOpenCV` 246★ (last push 2024-06-15);
`FTCLib/FTCLib` 230★ (last push **2024-08-20** — stale); `Pedro-Pathing/PedroPathing` 180★
(last push 2026-06-06); `FTC-23511/SolversLib` 24★ (last push **2026-08-18** — actively maintained).

**[JUDGMENT]** For BIOBUZZ: Road Runner + FTC Dashboard is still the safest default; Pedro Pathing is
the credible alternative; use SolversLib rather than FTCLib if you want a command framework, because
FTCLib has not been touched in two years. Detail and trade-offs in `research/PROGRAMMING-PRACTICE.md` §3.

### 2.9 8565 TechnicBots — Plano, TX — the Inspire machine

**[FACT]** <https://www.technicbots.com/>; GitHub <https://github.com/Technicbots-FTC-8565>.

- 2021-22 **World Championship Inspire Award** → FTC Hall of Fame; selected as **Team USA for the 2022
  FIRST Global Challenge in Geneva**; Edison Inspire 2023-24; Franklin Inspire 2025-26. Rookie 2014.
- Their own site's headline metrics **[FACT, self-reported]**: *"16+ Years Active; 2,000+ Hours of
  Outreach This Year; 8,000+ People Impacted This Year."*
- They run a recurring community event, the **FLYSET FIRST Workshop** — 12th annual, 15 Aug 2026, hybrid,
  with FIRST in Texas / North Texas officials and industry speakers **[FACT]** — plus a "Monthly
  Mentoring Forum" and a May Robotics Showcase.
- Their DECODE-season OPR was 112.8, global rank 475 **[FACT]**.

**[JUDGMENT]** TechnicBots is the clearest proof that Inspire is won off the field. 2,000 outreach hours
is not copyable by a small team — but *hosting one recurring event that other teams attend* is. A
half-day kickoff watch party or a single annual workshop gives you a countable, repeatable,
photographable outreach program with named beneficiaries, which is exactly what Connect/Reach judges
ask for.

### 2.10 12736 / 12737 Electric Mayhem — Buffalo, NY — the documentation-first program

**[FACT]** Build thread: <https://www.chiefdelphi.com/t/12736-electric-mayhem-green-2025-26-build-thread/506022>;
YouTube <https://www.youtube.com/@electricmayhemrobotics>.

| Practice | Detail (self-reported in thread) |
|---|---|
| Program shape | Two FTC teams (12736 Green, 12737 White) sharing one lab, **meeting three times a week after school**; 13th year in FIRST, 9th in FTC |
| Off-season onboarding | 9th annual FTC summer camp: four groups each built an FTC robot to play *that year's VEX game*, ending in a full tournament on the last day — used to onboard new students |
| Kickoff | They **host** the local kickoff at their school (9 years running) — game reveal, field tour, rule-book deconstruction, then group game analysis |
| Kickoff method (new for DECODE) | Worked with a parent who is a creativity expert to run **divergent → convergent** ideation with **delayed judgment** ("no matter how bad an idea sounds, don't shoot it down while diverging"), replacing their old "list all the ways a robot could play, pick a favorite" method |
| Artifact | A **2D bot sketch** in a public CAD document, updated as the design changes, that acts as the single shared picture of the robot |
| Cadence | Weekly build-thread post; a weekly podcast ("Weekly Dose of Mayhem", season 3) |
| Honesty | They publish failures — a ceiling collapse closing the lab for two weeks; an intake redesign forced because "the intake is too long for the turret to be correctly mounted without it hanging over our frame, and out of the 18″×18″ box" |

**[JUDGMENT]** The **public 2D bot sketch** is a cheap and extremely effective coordination device.
One drawing, always current, that everyone points at. For a small team with no full-time CAD lead,
a maintained 2D layout is worth more than a half-finished 3D assembly.

### 2.11 Cross-program reference: FRC 9280 High Altitude — sprint-based build management

**[FACT, FRC not FTC]** <https://www.chiefdelphi.com/t/high-altitude-9280-build-thread-2026-open-alliance/509708>.
Included because their management writeup is unusually explicit and transfers directly.

- They run an **"Agile-hybrid framework inspired by SCRUM"** — explicitly *not* formal SCRUM roles, but:
  "clear priorities / short feedback loops / weekly iteration / visible work".
- Season goals written down at the start, in measurable form: *"Be competitive at the Monterrey Regional,
  reach finals, and win an award; qualify for the Championship; finish top 10 at the Midwest Regional."*
- **Sprint 1 = prototypes + build the field.** Mentors assigned as leaders per prototype; students choose
  which area to work in.
- Kickoff day: split into groups to break down (a) arena and field elements, (b) match flow and scoring,
  (c) game and robot rules; build a **scoring spreadsheet**; review analogous past games for inspiration.
- A former student lead, now a mentor, wrote: documenting *"forced us to think in systems, document
  decisions, and reflect on what actually worked (and what didn't) under real build-season pressure."*

---

## 3. The composite elite season process, with gates

**[JUDGMENT]** Synthesized from §2 (especially 6165's dated progression, 23511's thread, 12736's kickoff
method, 9280's sprint model) and GM0's design-strategy guidance. Dates are mapped onto the BIOBUZZ
calendar; reconcile against `research/SEASON-CADENCE.md`, which is the authoritative calendar in this
workspace.

| Phase | When (BIOBUZZ) | What elite teams do | **Gate to exit the phase** |
|---|---|---|---|
| **P0 Pre-season** | now → 11 Sep 2026 | Onboarding, tool/CAD training, rebuild last year's drivetrain, run an off-season event, fix the workspace | Every member can use the CAD tool and deploy code; drivetrain rolls |
| **P1 Game analysis** | Kickoff day, 12 Sep | Handle game elements; build a scoring spreadsheet; enumerate every way to score; divergent → convergent ideation with delayed judgment; list rule constraints (18″ box, height limits) | A written **strategy statement** of ≤5 lines and a ranked list of robot roles |
| **P2 Prototyping** | Weeks 1–3 | Free-build crude prototypes out of u-channel/MDF/wood in *hours*, not days; test one physical question each; record blunt findings including negative results; source proxy game elements if the real ones are scarce | Each subsystem has **one** prototype with a measured result that justifies the chosen approach |
| **P3 V1 CAD + build** | Weeks 3–8 | Full CAD before cutting metal (6165: V1 CADed **8 days** after kickoff, V1 final ~9 weeks after kickoff); parallel subsystem CAD by different people in one shared document | V1 drives and scores; **a written weaknesses list exists** |
| **P4 Compete V1** | First qualifier | Compete deliberately; scout; collect match data | **Written tournament retrospective within a week** (6165 did theirs 8 days after the qualifier) |
| **P5 V2 redesign** | Post-Q1 → Jan | Redesign against the weaknesses list, not against a wish list; V2 CAD → prototype → final in ~4–6 weeks (6165: 22 Dec CAD → 8 Jan prototype → 22 Jan final) | V2 beats V1 on a **measured** metric (cycle time, auto points, reliability) |
| **P6 Refine** | Feb → March | Small V3 changes only; drive practice; auto reliability; portfolio finalization | Auto success rate and cycle time logged over ≥20 practice matches |
| **P7 Championship** | April | Same robot, more practice; judging rehearsal | — |
| **P8 Off-season** | May → Aug | Retrospective; off-season event (e.g. MTI); open-source the code/CAD; onboard | Written retrospective + published artifacts |

**[FACT]** Off-season competition is a real elite practice, not a nicety: the **Multinational Tech
Invitational** (formerly Maryland Tech Invitational), 10th edition **26–29 June 2026 at Johns Hopkins
Applied Physics Laboratory, Laurel MD**, invitation-only, **$800 registration**, applications due
**29 March 2026**, invitations earned through DECODE-season on-field performance plus a required solo
match video submission (<https://www.firstchesapeake.org/mti>). 6165 CuttleFish's portfolio shows them
prototyping for MTI in **June**, losing there in July, and running a retrospective in **August** —
before the season even started.

**[JUDGMENT]** For a small team the transferable version of "compete in the off-season" is: play a
scrimmage against one other local team in October and again in December. It costs a Saturday. It is
the only way to find the failures that only appear under match conditions.

### GM0's design-strategy guidance — the free version of elite judgment

**[FACT]** <https://gm0.org/en/latest/docs/design-skills/design-strategy.html> presents a
problem/solution table that matches what elite portfolios actually say:

| Mistake | Consequence | What to do instead |
|---|---|---|
| Do everything at once | Robot is half-baked; cannot excel anywhere | **Perfect one objective first** — highly optimized, consistently excels in one area |
| Overcomplicate | More time to iterate; less reliable | **Simplify** — best designs are usually simplest, fewer moving parts |
| Score-first design | Neglects proper principles; wildly inconsistent | **Design for consistency** — reliability > scoring ability; a big plus at alliance selection |
| Build haphazardly | Subpar materials, inadequate support | **Build for reliability** — remove unneeded moving parts, eliminate single points of failure |
| Fret about design | Wastes testing time | **Focus on execution** — make a decision and move |

GM0 also points to Karthik Kanagasabapathy's (FRC 1114 Simbotics) *Effective FIRST Strategies*
presentation as the canonical strategy talk.

---

## 4. How elite teams document decisions — and what the portfolio actually looks like

### 4.1 The formats that recur

**[FACT]** Across the four full portfolios read (6165, 12635, 16461, 7842), all were **exactly 16 pages**
— consistent with the FTC portfolio page cap. Recurring structural elements:

| Element | Seen in | What it is |
|---|---|---|
| **Dated progression timeline** | 6165 | One page: every milestone in the season with a date, including losses and retrospectives |
| **Problem → Solution → Key Feature** mechanism blocks | 6165 | Rigid three-line template per mechanism; hardware left column, software right column, same page |
| **Initial Solution → Challenge → Solution → Challenge → Final Solution** | 12635 | Iteration narrative per mechanism, with the iteration count stated ("8 major iterations") |
| **Per-version Strengths / Weaknesses** | 6165 | Explicit weaknesses per robot version — the strongest possible evidence of an engineering process |
| **Per-student learning goal** | 16461 | One line per member: what *that person* learned this year |
| **Per-student role card** | 7842 | Name, role, subteams, years on team |
| **Sponsor table split by type** | 16461 | Monetary / Discount / Materials / Software, with continuing sponsors highlighted |
| **Numbers everywhere** | 12635, 6165 | "300 ms", "3× more accurate", "within an inch at 60 Hz", "8 iterations", "±0.9 in compression" |

### 4.2 The documentation *cadence* that makes portfolios cheap

**[FACT + JUDGMENT]** The elite pattern is that the portfolio is a **by-product**, not a project:

1. **Weekly public post** (Open Alliance build thread, or a private blog if you prefer). 23511 explicitly
   redesigned theirs to be short and frequent because the long-form version kept slipping.
2. **CAD and code version history is the primary record.** 23511 tells readers to "see version
   history/branches as well" instead of writing step-by-step prose. Your Onshape version history and your
   git log already *are* a decision log — if you name versions and write commit messages.
3. **A maintained 2D layout sketch** (12736) as the always-current shared picture.
4. **Retrospective after every event, within a week** (6165: qualifier 11 Dec → retrospective 19 Dec).
5. **Photograph everything** — a portfolio is 60% images and you cannot retroactively photograph a
   prototype you threw away in October.

**[JUDGMENT] AI leverage (Claude Code).** The correct division of labor is: students produce the raw
material (photos, measurements, one-paragraph "what we tried and what happened" notes, git/Onshape
history); Claude Code turns that into portfolio prose, tables and consistent formatting, and interrogates
it for gaps ("you claim a 300 ms extension — where is the measurement?"). Students must still make and
own every engineering decision; see `research/AI-IN-FTC-POLICY.md` for the rules and disclosure
expectations before you rely on this.

---

## 5. In-house vs COTS — the fabrication ladder

**[FACT]** Observed capability levels among the profiled teams:

| Team | Fabrication capability | Consequence |
|---|---|---|
| 30030 Exodus | COTS goBILDA + Misumi slides + **3D-printed TPU** intake parts, in a garage | World champion with essentially no machine tools |
| 12635 Kuriosity | **Two 3D printers + a CNC router**, garage; "100% of our hardware in house" | Won World Design Award; ultra-compact custom packaging |
| 6165 CuttleFish | **Laser-cut MDF for prototypes**, CNC metal for final parts **via a sponsor** (Trial & Error Robotics), learned CAM from the sponsor | Fast iteration cheaply; precision only where it matters |
| 23511 Seattle Solvers | Plates **outsourced to Fabworks** | Swerve-grade precision with zero shop |
| 16461 Infinite Turtles | **SendCutSend discount sponsorship** | Laser/waterjet parts at reduced unit cost |

**[JUDGMENT] The ladder, in order of value-per-dollar for a small team:**

1. **3D printer (FDM) + TPU and PETG.** Exodus's championship intake sweepers were printed TPU. A single
   printer changes what you can design more than any other purchase.
2. **Laser-cut or hand-cut MDF/plywood for prototypes.** 6165 built prototypes in MDF specifically to
   "speed up redesign and iteration cycle". Cheap sheet goods make prototyping fast; nobody judges a
   prototype's material.
3. **Outsourced flat parts** (SendCutSend, Fabworks) for the 3–6 structural plates that actually need
   precision. This is the single best substitute for owning a mill.
4. **A drill press + hand tools + good COTS extrusion (goBILDA / REV).** The Exodus bill of materials is
   almost entirely this.
5. **CNC router / mill** — last, and only if you have a mentor who will actually run it. Otherwise it is
   an expensive shelf.

Pricing, part numbers and vendor comparisons live in `research/SMALL-TEAM-ECONOMICS.md` §4 and
`reference/VENDOR-ECOSYSTEMS.md`. **All prices need re-checking as of August 2026.**

---

## 6. Programming stack and how software is organised

### 6.1 The stack elite teams actually run

**[FACT], as of 22 Aug 2026:**

| Layer | Dominant choice | Status |
|---|---|---|
| Language / IDE | Java in Android Studio (some Kotlin) | Universal at this level |
| Path following | **Road Runner** (`acmerobotics/road-runner`, 266★) | Actively maintained (push 2025-11-02); quickstart pushed 2026-08-18 |
| Path following (alt) | **Pedro Pathing** (`Pedro-Pathing/PedroPathing`, 180★), developed by FTC 10158 Scott's Bots | Push 2026-06-06; docs at <https://pedropathing.com/> |
| Tuning / telemetry | **FTC Dashboard** (`acmerobotics/ftc-dashboard`, 212★) | Push 2026-08-20 |
| Path visualization | **MeepMeep** (68★) | Push 2024-09-24 — aging |
| Command framework | **SolversLib** (fork of FTCLib, maintained by FTC 23511) | Push 2026-08-18. **FTCLib itself last pushed 2024-08-20** |
| Vision | EasyOpenCV (246★, push 2024-06-15); increasingly **Limelight 3A** with AprilTags | 12736 used a Limelight 3A + AprilTags in DECODE |
| Control theory reference | **CTRL ALT FTC** <https://www.ctrlaltftc.com/> | Live |

### 6.2 Architecture

**[FACT]** From the KookyBotz tree (§2.7) and 6165's portfolio: **command-based architecture, subsystem
objects, finite state machines, hardware access centralized in one class** (`RobotHardware`,
`Globals`, `Sensors`), path-following code separated from mechanism code, vision pipelines isolated.
6165 states it directly: *"Splitting up tasks and classes in Android Studio by hardware components.
Finite State Machines' abstract structure allows for members to optimize a single module to fit into the
larger program's macros and automations"* and *"GitHub allows members to code their modules in version
control… while maintaining a Minimum Viable Product."*

### 6.3 Teams write their own controllers when the library does not fit

**[FACT]** 6165 wrote a **custom Ramsete controller** ported from FRC because Road Runner's default
follower did not work for their tank/traction drivetrain, then *"helped 8 other teams set up the Ramsete
algorithm, and… open-sourced our code."* KookyBotz wrote their own **GVF path follower**, Hermite spline
geometry and asymmetric motion profiles. 12635 wrote a **custom modular Kalman filter**.

**[JUDGMENT]** Do *not* copy this. Writing your own path follower is a top-1% activity that pays off only
after everything else is done. For BIOBUZZ, take Road Runner or Pedro Pathing off the shelf and spend the
saved weeks on autonomous *reliability* and driver practice. Exodus reached auto OPR rank 3 worldwide;
nothing in their public CAD suggests exotic control code.

### 6.4 Data collection habits worth copying

**[FACT]** KookyBotz ship `util/logging/CSVInterface.java` + `Logger.java` and a `LogType` enum;
12635 quantifies localization at 60 Hz and within an inch; 6165 applies a low-pass filter to a noisy IR
sensor and adds **haptic controller feedback** to tell the driver the intake has collected a game element.

**[JUDGMENT]** Minimum viable version for a two-programmer team, roughly 4 hours of work total:
log timestamp + pose + mechanism state to a CSV on the Control Hub every loop; download after practice;
plot cycle time and auto success rate. That single habit converts "the robot feels slow" into a number
you can put in the portfolio and act on. Detail in `research/TESTING-AND-TUNING.md` §4.

---

## 7. How elite teams practice and test

**[FACT] Observed practices:**

- **Build the field early and treat it as sprint-1 work.** 9280 built the HUB and TOWER as their first
  sprint deliverable *before* the robot existed, so prototypes could be tested against real geometry.
- **Source proxy game elements.** 23511 obtained FRC 2017 "fuel" balls from FRC 1318 because they match
  the DECODE artifacts, letting them prototype launchers immediately.
- **Measure the physical property, then design.** 23511 recorded artifact compressibility and stacking
  order behavior on kickoff day; 9280 set intake compression to **0.9 inches** as a tested parameter.
- **Test the negative result and write it down.** 23511: gecko (flexible) wheels launched *less*
  consistently than rhino (rigid) wheels. That single sentence saved every team who read it a week.
- **Prototype for hours, not days.** 12736: *"for a prototype we built in an hour with a broken router it
  works pretty well."*
- **Pre-flight opmodes.** KookyBotz's `SystemCheck` and per-device test opmodes.

**[JUDGMENT] For a small team, ranked:**
1. Build **the scoring element of the field first** (the goal/target), not the whole field. A full field is
   ~$500–1,500 in lumber and vinyl and a lot of storage you may not have.
2. Ten drive-practice sessions of 45 minutes beat one 8-hour session.
3. Log every practice match: cycle count, auto result, and every failure with a one-word cause. Twenty
   rows of this beats any amount of intuition.

Full treatment: `research/TESTING-AND-TUNING.md` §2–4.

---

## 8. Transferable practices, ranked by value-per-hour for a small team

**[JUDGMENT]** Ranked for a team of roughly 5–10 students with limited money. "Cost" is honest labor cost.
"Free?" means it requires no money and no additional people — only decisions.

| # | Practice | Source of evidence | Cost | Free? | Why it ranks here |
|---|---|---|---|---|---|
| 1 | **Write a ≤5-line strategy statement on kickoff day and hold to it** | 6165 portfolio p.1; GM0 "perfect one objective first" | 2 h | ✅ | Every downstream decision gets cheaper. The #1 cause of small-team failure is scope. |
| 2 | **Short weekly documentation post + rely on CAD/git version history as the decision log** | 23511 thread opener | 30 min/wk | ✅ | Produces the portfolio for free and stops the pre-deadline heroics that never happen |
| 3 | **Per-actuator test OpModes + a SystemCheck pre-flight** | KookyBotz `opmode/testing/device/*`, `opmode/debug/SystemCheck.java` | 4–6 h once | ✅ | Turns competition-day debugging from 30 minutes into 60 seconds |
| 4 | **Written weaknesses list after every event, retrospective within one week** | 6165 progression timeline (Q1 11 Dec → retro 19 Dec) | 2 h/event | ✅ | This *is* the engineering process judges are looking for, and it directs V2 |
| 5 | **Maintain one always-current 2D robot layout sketch** | 12736 public CAD 2D sketch | 1 h/wk | ✅ | Cheapest possible coordination artifact for a team with no full-time CAD lead |
| 6 | **Handle game elements and measure their properties before designing** | 23511 kickoff post; 9280 compression = 0.9 in | 2 h | ✅ | Prevents an entire wasted prototype generation |
| 7 | **Prototype in hours out of scrap MDF/wood; test exactly one question each** | 12736 ("built in an hour"), 6165 (laser-cut MDF) | ongoing | ✅ | Iteration speed dominates iteration quality early in a season |
| 8 | **Log to CSV every loop; plot cycle time and auto success** | KookyBotz `CSVInterface`; 12635's quantified claims | 4 h once | ✅ | Converts opinions into portfolio-grade numbers |
| 9 | **Problem → Solution → Key Feature portfolio template, hardware and software on one page** | 6165 portfolio | 0 (format) | ✅ | Best-in-class structure, costs nothing to adopt |
| 10 | **Name a Drive subteam and a Strategy subteam from week one** | 7842 (five subteams incl. Drive and Strategy) | 0 | ✅ | Makes driving and scouting someone's job instead of nobody's |
| 11 | **Per-student named learning goal, written down and updated** | 16461 portfolio | 15 min | ✅ | Directly answers judges' "what did you learn"; also a retention tool |
| 12 | **Publish your CAD and code (Open Alliance)** | theopenalliance.org/ftc; 23511, 12736, KookyBotz | 1 h/wk | ✅ | Forces clarity, attracts help, and is strong Connect/Innovate evidence |
| 13 | **Buy a 3D printer and design around printed TPU/PETG parts** | 30030 Exodus TPU sweepers | ~$300–600 | ❌ money | Highest-leverage single purchase; not free but cheap |
| 14 | **Counter-spring / bungee-assist every lift; add servo savers** | 30030 (bungee-assisted lift); 6165 (spring shock absorbers) | 2 h | ✅ | Reliability per hour is unbeatable; both teams cite it as a reliability fix |
| 15 | **Outsource only the 3–6 plates that need precision** | 23511 (Fabworks); 16461 (SendCutSend discount) | $50–200/order | ❌ money | Substitutes for a $10k machine shop |
| 16 | **Scrimmage against one local team in Oct and Dec** | Off-season/MTI pattern (6165) | 2 Saturdays | ✅ | Only way to surface match-condition failures early |
| 17 | **Host one recurring community event (kickoff watch party or workshop)** | 12736 (9 years hosting kickoff); 8565 (12th FLYSET workshop) | 1–2 days/yr | ✅ | The copyable core of an Inspire/Connect/Reach program |
| 18 | **Ask for discount sponsorships, not just cash** | 16461 (SendCutSend, goBILDA, ServoCity) | 4 h of emails | ✅ | Far higher hit rate than cash asks; compounds every order |
| 19 | **Divergent → convergent ideation with delayed judgment at kickoff** | 12736 (creativity-expert-guided method) | 3 h | ✅ | Cheap fix for the "first idea wins" failure mode |
| 20 | **Read three elite portfolios before writing yours** | Hivemind archive | 2 h | ✅ | Fastest possible calibration of what "good" looks like |
| 21 | **Recruit via one annual open house** | 16461 ("all but two of our members") | 1 day/yr | ✅ | Sustainability evidence for the Sustain award, and a real pipeline |
| 22 | **Weekly sprint with visible priorities and named owners** | 9280 (Agile-hybrid, sprint 1 = prototypes + field) | 30 min/wk | ✅ | Turns "we met and worked on stuff" into measurable progress |
| 23 | **Write a Solo (one-gamepad) TeleOp** | KookyBotz `opmode/teleop/Solo.java` | 3 h | ✅ | Insurance against absence — a real risk on a small team |
| 24 | **Adopt Road Runner or Pedro Pathing rather than writing a follower** | §6.3 | −3 weeks saved | ✅ | Negative cost: it *saves* time |

### What is genuinely bought, not earned

**[JUDGMENT]** Be honest about these; do not pretend process substitutes for them:

| Advantage | Who has it | Real cost | Cheapest substitute |
|---|---|---|---|
| Full permanent practice field | Most Championship teams | ~$500–1,500 materials + a room you can leave it in | Build the goal/scoring structure only; tape floor markings; borrow a field for one Saturday/month |
| CNC mill or router in-house | 12635 (router), teams with sponsors | $2k–15k + a mentor who runs it | Outsourced flat parts (SendCutSend / Fabworks) + a 3D printer |
| 20–30 students | 8565, most school programs | — | Ruthless scope: one robot role, done excellently (GM0's "perfect one objective first") |
| 2,000 outreach hours/year | 8565 | ~40 person-hours/week | One recurring event + one sustained partnership, documented with counts |
| Multiple engineer mentors | 7842 (NASA physicist + engineers + alumni) | — | One mentor who refuses to give answers (16461's model) + the FTC Discord + Open Alliance threads |
| Off-season invitationals (MTI) | Top ~100 teams | $800 + travel, invitation-only | Local scrimmage with one other team |
| Machined swerve modules | 23511 | Outsourced plates + Axon servos + 6000 RPM motors | Do not build swerve. A well-tuned mecanum or 6-wheel drivetrain won the 2026 championship |

---

## 9. Best public resources, with what specifically to take from each

**[FACT] — all URLs verified reachable on 22 August 2026 unless noted.**

### Portfolios worth reading

| Resource | URL | Take this |
|---|---|---|
| **Hivemind Portfolio Archive** | <https://portfolios.hivemindrobotics.net/> (files at `https://cdn.hivemindrobotics.net/portfolios/{team}-{season}.pdf`) | The whole archive. Season slugs seen: `ff` FREIGHT FRENZY, `pp` POWERPLAY, `ug` ULTIMATE GOAL, `itd` INTO THE DEEP |
| **6165 MSET CuttleFish, FREIGHT FRENZY** | <https://cdn.hivemindrobotics.net/portfolios/6165-ff.pdf> | The **dated progression timeline**, the per-version strengths/weaknesses lists, and the Problem→Solution→Key Feature mechanism template. The best single portfolio in this research |
| **12635 Kuriosity Robotics, POWERPLAY** | <https://cdn.hivemindrobotics.net/portfolios/12635-pp.pdf> | How to write iteration narratives with a stated iteration count, and how to quantify every claim |
| **16461 Infinite Turtles, FREIGHT FRENZY** | <https://cdn.hivemindrobotics.net/portfolios/16461-ff.pdf> | The small-team template: 11 members, coach's house, per-student learning goals, discount-sponsor table |
| **7842 Browncoats, POWERPLAY** | <https://cdn.hivemindrobotics.net/portfolios/7842-pp.pdf> | Subteam structure including explicit **Drive** and **Strategy** subteams; per-student role cards |
| **23511 Seattle Solvers, INTO THE DEEP** | <https://cdn.hivemindrobotics.net/portfolios/23511-itd.pdf> | Recent-season layout reference. **[NOTE]** Image-based PDF — no extractable text; read visually |
| **14270 Quantum Robotics, POWERPLAY** | <https://cdn.hivemindrobotics.net/portfolios/14270-pp.pdf> | Romanian national-championship portfolio; visual design reference. Image-based PDF |

### Repos worth reading

| Resource | URL | Take this |
|---|---|---|
| **KookyBotz CenterStage** | <https://github.com/KookyBotz/CenterStage> | The package layout (§2.7). Especially `opmode/testing/device/`, `opmode/debug/SystemCheck.java`, `util/logging/CSVInterface.java`, `opmode/teleop/Solo.java` |
| **KookyBotz PowerPlaySleeveDetection** | <https://github.com/KookyBotz/PowerPlaySleeveDetection> | Explicitly published as a copyable vision-pipeline template |
| **Road Runner + quickstart + FTC Dashboard** | <https://github.com/acmerobotics/road-runner>, `/road-runner-quickstart`, `/ftc-dashboard` | The default autonomous stack; Dashboard for live PID/pose tuning |
| **Pedro Pathing** | <https://github.com/Pedro-Pathing/PedroPathing>, docs <https://pedropathing.com/> | The main Road Runner alternative; developed by FTC 10158 Scott's Bots |
| **SolversLib** | <https://github.com/FTC-23511/SolversLib>, docs <https://docs.seattlesolvers.com/> | A **maintained** command-based framework (FTCLib is stale since Aug 2024). Also a model of a team open-sourcing a real library |
| **Seattle Solvers season code** | <https://github.com/FTC-23511/Decode-2026> | A current, real, competitive season codebase to read end to end |
| **EasyOpenCV** | <https://github.com/OpenFTC/EasyOpenCV> | Still the standard non-Limelight vision path (last push 2024-06-15) |

### CAD worth opening

| Resource | URL | Take this |
|---|---|---|
| **RoboFTC open-source index** | <https://roboftc.github.io/> | Curated Onshape links for named competitive robots, plus component-level CAD (dead axle, claw, active intake, swerve module, boxtube, differential wrist) |
| **30030 Exodus (world champion) CAD** | <https://roboftc.github.io/robots/exodus.html> → <https://cad.onshape.com/documents/49cd4bc4d188cf9592aaf817/w/f5d5bfaeb0fe6538bb09b024/e/0e47d121a4ce7c079c69fb56> | Parallel-plate chassis, bungee-counter-sprung Misumi SAR230 lift, printed-TPU intake sweepers |
| **23511 Cypher (DECODE swerve + hooded shooter)** | <https://roboftc.github.io/robots/cypher.html> → <https://cad.onshape.com/documents/c021b03986672773c2100272/w/74f0a8f10b4c93fb8fe556c1> | Turret on an X-contact bearing; servo-adjustable shooter hood |
| **23511 prototype CAD document** | <https://cad.onshape.com/documents/d8be8e4f386583d152a5aef9/w/e2e7a1e484cff7f87de58a7b> | The habit of keeping prototypes in a *separate* CAD document from the robot |

### Build threads and video worth following

| Resource | URL | Take this |
|---|---|---|
| **FTC Open Alliance** | <https://www.theopenalliance.org/ftc>, category <https://www.chiefdelphi.com/c/first/ftc-open-alliance/90> | Member teams publish CAD, code, media and a build thread. Registration opened at 10:00 on kickoff morning in 2025-26 — expect the same for BIOBUZZ |
| **FTC Open Alliance statistics page** | <https://www.theopenalliance.org/ftc/stats> | Aggregate view of what member teams are using: drivetrains, building materials, brands, subsystems, programming choices. Useful sanity check when picking an archetype |
| **23511 Seattle Solvers DECODE thread** | <https://www.chiefdelphi.com/t/ftc-23511-seattle-solvers-decode-oa-season-thread/506155> | Kickoff-day element characterization; launcher prototype findings; the short-post documentation policy |
| **12736 Electric Mayhem Green DECODE thread** | <https://www.chiefdelphi.com/t/12736-electric-mayhem-green-2025-26-build-thread/506022> | Kickoff ideation method; the 2D bot sketch; honest failure reporting |
| **FRC 9280 High Altitude 2026 thread** | <https://www.chiefdelphi.com/t/high-altitude-9280-build-thread-2026-open-alliance/509708> | The clearest written description of sprint-based build management in either program |
| **Behind the Bot (FTC) playlist** | <https://www.youtube.com/playlist?list=PLkZ6_Ld1x9Y8p3x74cXFLBAvVpxlIbDuX> | Per-team robot walkthroughs. Start with 30030 Exodus <https://www.youtube.com/watch?v=gaTss6W49CQ>, 14270 Quantum Robotics <https://www.youtube.com/watch?v=DiWEMH436hY>, 20265 Heart of RoBots <https://www.youtube.com/watch?v=on4jUaoD5UA>, 19066 AiCitizens <https://www.youtube.com/watch?v=T2gFdXRMm20> |
| **Championship winner interview, DECODE** | <https://www.youtube.com/watch?v=NtZWHN9pPWI> | 30030 Exodus + 21087 Velocity on how the winning alliance worked |
| **FTC Open Alliance Show** (FUN Robotics Network) | <https://funroboticsnetwork.com/> | Short visual season updates from OA teams; interview slots are first-come-first-served after OA registration |

### Reference sites

| Resource | URL | Take this |
|---|---|---|
| **Game Manual 0** | <https://gm0.org/en/latest/> | The community engineering bible. Priority pages: Design Strategy, Engineering Design Process, Team Organization, Common Mechanisms, Awards |
| **CTRL ALT FTC** | <https://www.ctrlaltftc.com/> | Control theory for FTC — PID, feedforward, PIDF. Their key practical point: run your own external PID rather than the built-in one, for a faster refresh rate and better stability |
| **Learn Road Runner** | <https://learnroadrunner.com/> | Step-by-step Road Runner tuning |
| **FTC Docs (official)** | <https://ftc-docs.firstinspires.org/en/latest/> | Authoritative on hardware, control system, inspection |
| **FTCScout** | <https://ftcscout.org/> + GraphQL API <https://api.ftcscout.org/graphql> | Team/event results, OPR quick stats. The API is scriptable — see §0 |
| **FTC Events (official)** | <https://ftc-events.firstinspires.org/> | Official event results and awards, authoritative over any third party |
| **The Orange Alliance** | <https://theorangealliance.org/> | Alternate results database, useful for cross-checking |
| **FTC Directory** | <https://directory.powercut-robotics.org/teams> | Curated index of FTC resources by category (Teams / Programming / Design / Vendors / Rules / Team Management) |
| **Chief Delphi** | <https://www.chiefdelphi.com/> | The forum. Note: it 403s automated fetchers; append `.json` to a topic URL and set a browser User-Agent to read it programmatically |

---

## 10. What to do in the 21 days before kickoff (22 Aug – 11 Sep 2026)

**[JUDGMENT]** Ordered by value-per-hour, drawn from §8. Reconcile with `research/SEASON-CADENCE.md` §3,
which is the authoritative pre-season plan.

| Days | Action | Output |
|---|---|---|
| 1–2 | Read 6165-ff, 16461-ff and 12635-pp portfolios as a team; write a one-page "what good looks like" | Calibration doc + your portfolio template |
| 2–3 | Adopt the 6165 portfolio skeleton in your tool of choice; create the empty progression timeline and start dating it *now* | Portfolio shell |
| 3–5 | Stand up the repo from a Road Runner or Pedro Pathing quickstart; write per-actuator test OpModes and a `SystemCheck` against last year's robot | Working debug tooling before you need it |
| 5–6 | Add CSV logging; log one practice session with last year's robot to prove the pipeline | A CSV you can plot |
| 6–8 | Register intent to join the **FTC Open Alliance** (registration opens kickoff morning); create the build thread skeleton and the weekly-post calendar reminder | Documentation cadence that runs itself |
| 8–10 | Assign subteams **including Drive and Strategy**; write per-student learning goals | Team structure page of the portfolio |
| 10–14 | Send 10 discount-sponsorship emails (SendCutSend, goBILDA, ServoCity, local fabricators); ask for discount codes, not cash | Lower unit cost all season |
| 14–17 | Build the field's scoring structure as soon as the BIOBUZZ field drawings publish; buy sheet goods now | Prototyping surface on day 1 |
| 17–19 | Rehearse the kickoff-day process: element handling → scoring spreadsheet → divergent/convergent ideation → ≤5-line strategy statement | A kickoff run-sheet |
| 19–21 | Confirm the BIOBUZZ award list (Reach/Sustain vs Motivate) against the released manual; pick your two target judged awards | Award targets in writing |

---

## 11. Open questions to re-verify at kickoff (12 September 2026)

1. **[UNVERIFIED]** Does BIOBUZZ retain **Reach** and **Sustain** (introduced in DECODE) or revert to
   Motivate? V0 manual Section 13 is a placeholder. Check against
   `reference/AWARD-CATALOG-BIOBUZZ.md` on kickoff day.
2. **[UNVERIFIED]** Will the 2027 Championship keep **six divisions**? This changes the number of judged
   award slots and therefore your advancement odds.
3. **[UNVERIFIED]** Whether 16379 KookyBotz are still an active team — no 2025-26 quick stats returned.
   Their repos remain valid reading regardless.
4. **[UNVERIFIED]** Team 30030 Exodus's exact roster size (three is media-reported from a single outlet)
   and how many hours per week they worked. No team publishes hours/week; treat every hours figure in
   FTC discourse as anecdote.
5. **[FACT, but volatile]** Library maintenance status — re-check push dates for Road Runner, Pedro
   Pathing, SolversLib and EasyOpenCV before committing at kickoff. FTCLib being stale since Aug 2024 is
   the kind of fact that changes.
6. **Prices** in §5 and in `research/SMALL-TEAM-ECONOMICS.md` are as of August 2026 and must be re-checked.

---

## 12. Sources

**Official / results**

- FIRST Championship DECODE results — <https://community.firstinspires.org/congratulations-to-our-decode-first-championship-teams>
- FTC Events (official results) — <https://ftc-events.firstinspires.org/> ; e.g. <https://ftc-events.firstinspires.org/2024/FTCCMP1/awards>
- FTCScout — <https://ftcscout.org/> ; GraphQL API <https://api.ftcscout.org/graphql> (all award tables and OPR figures in §1)
- The Orange Alliance — <https://theorangealliance.org/>
- FTC Docs — <https://ftc-docs.firstinspires.org/en/latest/>
- Multinational Tech Invitational — <https://www.firstchesapeake.org/mti>

**Team-published material**

- 30030 Exodus CAD — <https://roboftc.github.io/robots/exodus.html>
- 30030 Exodus press — <https://www.kxan.com/studio-512/austin-teens-make-robotics-history-inside-team-30030-exodus-world-championship-win/> ; <https://www.facebook.com/studio512tv/videos/2230572364242292/>
- 23511 Seattle Solvers — <https://www.seattlesolvers.com> ; <https://www.chiefdelphi.com/t/ftc-23511-seattle-solvers-decode-oa-season-thread/506155> ; <https://github.com/FTC-23511> ; <https://docs.seattlesolvers.com/> ; <https://roboftc.github.io/robots/cypher.html>
- 6165 MSET CuttleFish portfolio — <https://cdn.hivemindrobotics.net/portfolios/6165-ff.pdf>
- 12635 Kuriosity Robotics portfolio — <https://cdn.hivemindrobotics.net/portfolios/12635-pp.pdf>
- 16461 Infinite Turtles portfolio — <https://cdn.hivemindrobotics.net/portfolios/16461-ff.pdf>
- 7842 Browncoats portfolio — <https://cdn.hivemindrobotics.net/portfolios/7842-pp.pdf>
- 16379 KookyBotz — <https://github.com/KookyBotz> ; <https://github.com/KookyBotz/CenterStage>
- 8367 Acme Robotics — <https://github.com/acmerobotics>
- 8565 TechnicBots — <https://www.technicbots.com/> ; <https://github.com/Technicbots-FTC-8565>
- 11260 Up-A-Creek Robotics — <https://www.team11260.org/> ; <https://github.com/Team11260> ; <https://www.youtube.com/@11260Robotics>
- 12736 Electric Mayhem Green — <https://www.chiefdelphi.com/t/12736-electric-mayhem-green-2025-26-build-thread/506022> ; <https://www.youtube.com/@electricmayhemrobotics>
- FRC 9280 High Altitude — <https://www.chiefdelphi.com/t/high-altitude-9280-build-thread-2026-open-alliance/509708>
- 18139 Rebel Robotics coverage — <https://norfolkdailynews.com/select/northeast-nebraska-s-rebel-robotics-crowned-world-champions-enter-ftc-hall-of-fame/> ; <https://norfolkne.gov/government/departments/communications-office/news/rebel-robotics-proclamation.html>

**Community infrastructure**

- FTC Open Alliance — <https://www.theopenalliance.org/ftc> ; <https://www.theopenalliance.org/ftc/teams> ; <https://www.theopenalliance.org/ftc/stats> ; season thread <https://www.chiefdelphi.com/t/the-2025-26-ftc-open-alliance-season/505867>
- Chief Delphi FTC Open Alliance category — <https://www.chiefdelphi.com/c/first/ftc-open-alliance/90>
- Game Manual 0 — <https://gm0.org/en/latest/> ; design strategy <https://gm0.org/en/latest/docs/design-skills/design-strategy.html> ; team organization <https://gm0.org/en/latest/docs/being-a-team/team-organization.html>
- CTRL ALT FTC — <https://www.ctrlaltftc.com/>
- Learn Road Runner — <https://learnroadrunner.com/>
- Pedro Pathing — <https://pedropathing.com/> ; <https://github.com/Pedro-Pathing/PedroPathing>
- Hivemind Portfolio Archive — <https://portfolios.hivemindrobotics.net/> ; <https://www.hivemindrobotics.net/>
- RoboFTC — <https://roboftc.github.io/>
- FTC Directory — <https://directory.powercut-robotics.org/teams>
- FUN Robotics Network — <https://funroboticsnetwork.com/>
- Behind the Bot playlist — <https://www.youtube.com/playlist?list=PLkZ6_Ld1x9Y8p3x74cXFLBAvVpxlIbDuX>

**Local workspace cross-references**

- `research/SEASON-CADENCE.md`, `research/SCOUTING-AND-AWARDS.md`, `research/PROGRAMMING-PRACTICE.md`,
  `research/SMALL-TEAM-ECONOMICS.md`, `research/TESTING-AND-TUNING.md`, `research/AI-IN-FTC-POLICY.md`
- `reference/AWARD-CATALOG-BIOBUZZ.md`, `reference/ROBOT-ARCHETYPE-LIBRARY.md`, `reference/VENDOR-ECOSYSTEMS.md`
- `manuals/2026-27_BIOBUZZ/` (V0 manual; Sections 8–11, 13 and 15 are placeholders until 12 Sep 2026)
