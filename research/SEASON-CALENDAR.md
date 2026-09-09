# FTC 2026-2027 BIOBUZZ — Season Calendar

**Compiled:** 2026-08-22 · **T-21 days to Kickoff**
**Season:** BIOBUZZ&trade; presented by RTX — part of the **FIRST&reg; CANOPY&trade;** 2026-27 season brand
**Kickoff:** Saturday **September 12, 2026, 12:00 p.m. ET**

> **Verification status of this document.** Every date below was re-checked on 2026-08-22 against a primary source. The local Key Season Dates PDF was confirmed **byte-identical (MD5 `e960e6fb…c3fc`)** to the file served live at `ftc-resources.firstinspires.org` — our copy is current, not stale. The live 2027 event page independently reports the same revision stamp: *"Important Season Dates — Version 26-27.1 (updated Jun 24, 2026)"*.

---

## 0. How to read this document

| Label | Meaning |
|---|---|
| **CONFIRMED** | Stated in an official 2026-27 BIOBUZZ source (V0 manual, Key Season Dates V26-27.1, or a firstinspires.org page). Safe to act on. |
| **DERIVED** | Arithmetic applied to a CONFIRMED rule (e.g. counting Thursdays). The rule is confirmed; the date is my calculation. |
| **HISTORICAL-PATTERN** | Not stated for BIOBUZZ. Inferred from DECODE (2025-26) / INTO THE DEEP (2024-25). Planning assumption only. |
| **TBA** | FIRST has explicitly not announced this, or prints "TBD". Do **not** substitute a prior-season number. |
| **UNVERIFIED** | Could not be confirmed from a primary source. |

### Source keys

| Key | Source | Note |
|---|---|---|
| `[DATES]` | `manuals/archive/supplemental/2026-27_BIOBUZZ_ImportantSeasonDates.pdf` | Rev **V26-27.1, June 24, 2026**. Verified identical to live `https://ftc-resources.firstinspires.org/ftc/archive/2027/event/season-dates`. |
| `[V0]` | `manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` | Pre-season V0. Verified identical to live `…/archive/2027/game/manual` (MD5 `6044b5b0…b005`). Sections 8-11, 13 and 15 are Kickoff placeholders (§14 League Play is NOT). |
| `[WEB]` | firstinspires.org program / resource pages | Cited inline. |
| `[COMM]` | community.firstinspires.org — official FIRST blog | Primary, but marketing-voice; its dates drift vs `[DATES]` (see §7). |

> **Precedence:** `[DATES]` outranks `[COMM]`. It is newer, versioned and change-controlled; the blogs are not.

---

## 1. Master calendar

Dates are as published. "What the team must do" is operational interpretation, not FIRST text.

### 1.1 Pre-Kickoff (elapsed — for audit / context)

| Date | T | Event | Status | Src |
|---|---|---|---|---|
| Sat May 2, 2026 | T-133 | Game Set pre-orders open via AndyMark | CONFIRMED | `[DATES]` |
| Sun May 3, 2026 | T-132 | **Game preview blog** — scoring element named **"Pollen"**, ~3 in. plastic balls | CONFIRMED | `[COMM]` game-preview-field-elements |
| Mon May 4, 2026 | T-131 | StarterBot resource guides published (all four vendors, rev 26-27.2) | CONFIRMED | `[WEB]` 2027 team page version stamps |
| Sun May 17, 2026 | T-118 | DECODE "Unlocked" software release | CONFIRMED | `[DATES]` |
| Wed Jun 17, 2026 | T-87 | 2026-27 team registration opens (FIRST Dashboard) | CONFIRMED | `[WEB]` cost-and-registration |
| Thu Jun 18, 2026 | T-86 | ROBOT SIGN printables published (rev 26-27.1) | CONFIRMED | `[WEB]` 2027 team page |
| Wed Jun 24, 2026 | T-80 | **Key Season Dates V26-27.1 published** — the document this calendar is built on | CONFIRMED | `[DATES]` |
| Fri Jul 10, 2026 | T-64 | Game Set pre-order ship deadline for PDP kickoffs · FTC Scoring Event Requests open | CONFIRMED | `[DATES]` |
| Mid Jul 2026 | ~T-60 | FTC Events 2026-27 event pages live · FTC SDK Summer Release | CONFIRMED | `[DATES]` |
| Thu Jul 23, 2026 | T-51 | Official Event Request Guide V26-27.1 published | CONFIRMED | `[WEB]` 2027 event page |
| Wed Jul 29, 2026 | T-45 | FTC Events site defaults to BIOBUZZ season · Robot Transport Letter 26-27.1 | CONFIRMED | `[COMM]`, `[WEB]` |
| Fri Jul 31, 2026 | T-43 | **Competition Manual Preview (V0) published** · inspection docs stubbed "Coming Soon" | CONFIRMED | `[V0]`, `[WEB]` |
| Mon Aug 17, 2026 | T-26 | Game Set shipments start (estimated) · **last date for regions to be counted for FCMP/Premier capacity-based advancement** | CONFIRMED | `[DATES]` |

### 1.2 Kickoff window — the next three weeks

| Date | T | Event | What the team must do | Status | Src |
|---|---|---|---|---|---|
| **Sat Aug 22, 2026** | **T-21** | *Today* | Finish V0 Sections 1-7, 12, 14 and 16 — already final, will not change at Kickoff | — | — |
| Fri Sep 4, 2026 | T-8 | **Early Game Preview Information** — *privacy agreements required for all viewers* | If your PDP offers access, sign early. Content is embargoed — do not redistribute | CONFIRMED | `[DATES]` |
| Fri Sep 11, 2026 | T-1 | Last 2025-26 DECODE off-season event | Clear the workspace; dry-run the ingest harness | CONFIRMED | `[DATES]` |
| **Sat Sep 12, 2026, 12:00 p.m. ET** | **T+0** | **KICKOFF.** Game reveal streams on the FTC YouTube channel. **The full Competition Manual publishes *after* the broadcast airs.** FTC Scoring Event Configuration opens | Watch reveal → run `tools/ingest-manual.sh` → execute the `SOURCES.md` §9 download plan | CONFIRMED | `[DATES]`, `[WEB]`, `[COMM]` |
| Sep 12-18, 2026 | T+0…T+6 | **FTC SDK release** · **FTC Live Preview (Beta)** | Pull the new `FtcRobotController` release. Do **not** run league events on the Beta | CONFIRMED | `[DATES]` |
| Mon Sep 14, 2026 | T+2 | FIRST Leadership Award nominations **open** | Identify your nominee now — the deadline is a hard Dec 15 | CONFIRMED | `[DATES]` |
| Thu Sep 17, 2026 | T+5 | Volunteer training available · **first regular Thursday Team Update** | Assign one student to read every Team Update, every week | CONFIRMED (training) / DERIVED (TU) | `[DATES]`, `[V0]` §1.7.3 |
| **Mon Sep 28, 2026, 12:00 p.m. ET** | **T+16** | **Team Q&A opens** (Volunteer Q&A too) | Access is via **Lead Coach 1/2 dashboard account only** — verify your LC can log in *before* this date | CONFIRMED | `[V0]` §1.7.4; `[DATES]` |

> ⚠️ **The 16-day blackout.** Kickoff is Sep 12 but the Q&A does not open until Sep 28. For **more than two weeks** you will hold game rules you cannot get official clarification on. **This is the same gap DECODE had, and it is the norm, not an anomaly** — DECODE kicked off **Sat Sep 6, 2025** (DECODE Team Update 00 is dated Sep 6, 2025 and describes changes "from the V0 Preview Release") and its Q&A opened **Sep 22, 2025**, also **T+16**. The season before that was shorter: INTO THE DEEP kicked off Sep 7, 2024 and its Q&A opened **Sep 16, 2024** (T+9, per the ITD kickoff manual §1.9). So the gap has been 9 days once and 16 days twice — plan for 16. Budget for it: draft questions during the blackout and submit the moment the queue opens.

### 1.3 Competition season

| Date | T | Event | What the team must do | Status | Src |
|---|---|---|---|---|---|
| Fri-Sun Oct 2-4, 2026 *(proposed)* | T+20 | Preseason Testing Event — **date and location TBD** | Watch for announcement | TBA | `[DATES]` |
| **Thu Oct 15, 2026** | **T+33** | **FTC Live official release** (minimum version for advancing events) · **earliest date for League Meets / Qualifying Tournaments** | First day you can legally compete at an advancing event — robot must be inspection-legal | CONFIRMED | `[DATES]` |
| Mon Oct 19, 2026 | T+37 | PDP deadline: request Regional Championship events + set up Region Advancement in FTC Scoring | Ask your PDP to publish the region's advancement plan | CONFIRMED | `[DATES]` |
| Mon Nov 16, 2026 | T+65 | **Region Size Snapshot** for FCMP advancement calculation · deadline for Event Variance requests (Dual Division / extra RCMP matches) | — | CONFIRMED | `[DATES]` |
| Tue Nov 17, 2026 | T+66 | *Manual states this as the region registration cutoff — conflicts with Nov 16, see §7 #1* | — | **CONFLICT** | `[V0]` §4.2 |
| Thu Nov 19, 2026 | T+68 | FTC Live Dual Division release · **FCMP + Premier Event advancement allocations released** | Learn how many slots your region actually gets | CONFIRMED | `[DATES]` |
| Mon Nov 30, 2026 | T+79 | **Earliest Regional Championship (RCMP) events** · earliest Dual Division events | — | CONFIRMED | `[DATES]` |
| Early Dec 2026 | ~T+80 | Regional advancement slot allocations published on FTC-Events | Check `ftc-events.firstinspires.org/2027` for your region | CONFIRMED | `[V0]` §4.2 |
| **Tue Dec 15, 2026** | **T+94** | **FIRST Leadership Award nominations DUE** · interview event dates set in FTC Scoring | The only hard, FIRST-wide award deadline all season | CONFIRMED | `[DATES]` |
| Fri Dec 18, 2026 | T+97 | Leadership Award semi-finalist confirmation emails sent | — | CONFIRMED | `[DATES]` |
| Mon Feb 15, 2027 | T+156 | Leadership Award **finalists due to FIRST**. Earlier RCMPs may announce earlier; FIRST keeps later RCMP finalists confidential | — | CONFIRMED | `[DATES]` |
| **Sun Mar 21, 2027** | **T+190** | **Last RCMP date to receive FCMP/Premier advancement** — FIRST must receive final event data by EOD | Last realistic path to Houston | CONFIRMED | `[DATES]` |
| Fri Apr 9, 2027 | T+209 | Teams not paid **and** hotels not secured are **dropped**; slots reallocated regardless of original region | Pay and book hotels early | CONFIRMED | `[DATES]` |
| Thu Apr 15, 2027 | T+215 | **Projected final Team Update** | Freeze rule interpretations after this | DERIVED — see §2 | `[V0]` §1.7.3 + FCMP date |
| **Wed Apr 28 – Sat May 1, 2027** | T+228…T+231 | **FIRST Championship** — **George R. Brown Convention Center, Houston, TX** | — | CONFIRMED (dates + venue) | `[DATES]`; `[COMM]` update-future-of-first-championship |

### 1.4 Post-season

| Date | T | Event | Status | Src |
|---|---|---|---|---|
| Thu May 20, 2027 | T+250 | FTC **BIOBUZZ "Unlocked"** software release (off-season play) | CONFIRMED | `[DATES]` |
| Late May 2027 | ~T+255 | 2027-28 season registration opens | CONFIRMED | `[DATES]` |
| Sat Jul 31, 2027 | T+322 | **End of FIRST support for BIOBUZZ** | CONFIRMED | `[DATES]` |
| TBD | — | Registration and Storefront closed · last day to use grant funds or secure a team number for current-season events | **TBA** | `[DATES]` |
| TBD | — | **Last date to order BIOBUZZ-specific field elements from AndyMark** | **TBA** — watch this; it gates spare game pieces | `[DATES]` |
| TBD (5:00 p.m. ET) | — | FIRST Championship **final payment deadline** | **TBA** (time known, date not) | `[DATES]` |

> *Page 2 of `[DATES]` is a table that text extraction scrambles — the date column and label column are emitted separately, producing false pairings. Rows above were reconstructed from PDF word geometry. If a §1.4 date becomes load-bearing, eyeball page 2 of the PDF directly (§7 #6).*

### 1.5 Future seasons (multi-year planning)

| Season | Kickoff | Last RCMP for FCMP advancement | FCMP load-in |
|---|---|---|---|
| 2027-28 | Sat Sep 11, 2027 | Mon Mar 13, 2028 | Wed Apr 19, 2028 |
| 2028-29 | Sat Sep 9, 2028 | Mon Mar 19, 2029 | Wed Apr 25, 2029 |

*`[DATES]` p.2, labelled by FIRST as **projected**. Houston / GRB is committed **through 2034** (`[COMM]`, Jan 22, 2026), so the venue is stable for both.*

---

## 2. Team Update cadence — the rule that actually bites

**CONFIRMED** `[V0]` §1.7.3:

- Team Updates post **every Thursday, beginning on Kickoff day and ending two weeks prior to FIRST Championship.**
- Additions highlighted yellow; deletions struck through.
- **A Team Update published after the driver's meeting at an event does not apply to that event.**

> ⚠️ **The trap most teams miss.** That last clause cuts both ways. A Thursday-evening update does **not** govern a Saturday event whose driver's meeting already happened — but at a **Friday-load-in / Saturday-compete** event, the Thursday update **is** in force. Always record which manual version and Team Update number you competed under, and re-read the newest update on the drive to the venue.

### Projected Thursday schedule (DERIVED)

| # | Date | # | Date | # | Date |
|---|---|---|---|---|---|
| TU00 | **Sat Sep 12, 2026** (Kickoff) | TU11 | Nov 26 | TU22 | Feb 11, 2027 |
| TU01 | Sep 17 | TU12 | Dec 3 | TU23 | Feb 18 |
| TU02 | Sep 24 | TU13 | Dec 10 | TU24 | Feb 25 |
| TU03 | Oct 1 | TU14 | Dec 17 | TU25 | Mar 4 |
| TU04 | Oct 8 | TU15 | Dec 24 | TU26 | Mar 11 |
| TU05 | Oct 15 | TU16 | Dec 31 | TU27 | Mar 18 |
| TU06 | Oct 22 | TU17 | Jan 7, 2027 | TU28 | Mar 25 |
| TU07 | Oct 29 | TU18 | Jan 14 | TU29 | Apr 1 |
| TU08 | Nov 5 | TU19 | Jan 21 | TU30 | Apr 8 |
| TU09 | Nov 12 | TU20 | Jan 28 | **TU31** | **Apr 15 (projected final)** |
| TU10 | Nov 19 | TU21 | Feb 4 | | |

**Calibration.** BIOBUZZ has exactly **31 Thursdays** between Kickoff (Sat Sep 12, 2026) and FCMP-minus-two-weeks. DECODE had **32** (Thu Sep 11, 2025 → Thu Apr 16, 2026) because its Kickoff fell a week earlier in the month (**Sat Sep 6, 2025**), leaving a Thursday inside the same week as Kickoff. DECODE's final update was **TU32**, dated Thu Apr 16, 2026 — which lines up **exactly**: TU00 on Kickoff day (Sat Sep 6), then TU01–TU32 on 32 consecutive Thursdays. Verified against `manuals/_reference_prior_seasons/2025-26_DECODE_TeamUpdates_Combined.pdf` (every TU header date, Sep 6 2025 → Apr 16 2026) and `manuals/archive/supplemental/2025-26_DECODE_TeamUpdate_Latest.pdf`. **There was no off-cycle release** — the numbering is exactly one per Thursday plus TU00.

> **Conclusion: trust the *dates*, not the *numbers*.** On the DECODE pattern, expect **32 documents** for BIOBUZZ — TU00 on Sat Sep 12, 2026 plus TU01–TU31 on the 31 Thursdays through Apr 15, 2027. FIRST has also issued same-day and next-day re-releases (ITD TU04 patched TU03 the *same day*, 2024-10-17; DECODE re-issued TU10 as **TU10 v2** the next day, 2025-11-14), so the document count can exceed the Thursday count without the schedule slipping. Do not read "TU31" as meaning the season is over — read the **date** (mid-April, two weeks before Houston). Note also that "two weeks prior" is applied loosely: FCMP 2026 opened Apr 29 and the final update was Apr 16 — 13 days prior, not 14. FIRST rounds to the nearest Thursday rather than counting strictly, which is why Apr 15, 2027 (13 days before Apr 28) is the projection here rather than Apr 8.

**TU00 at Kickoff** is HISTORICAL-PATTERN (DECODE and ITD both did it), but a very strong one — DECODE's TU00 is a "notable changes from last season" summary. Expect BIOBUZZ's TU00 to be the fastest available diff of V0 against the Kickoff manual.

---

## 3. Q&A system

| Item | Value | Status | Src |
|---|---|---|---|
| Opens | **Mon Sep 28, 2026, 12:00 p.m. ET** | CONFIRMED | `[V0]` §1.7.4, `[DATES]` |
| Access | **Lead Coach 1 or Lead Coach 2's FIRST dashboard account** — no one else | CONFIRMED | `[V0]` §1.7.4 |
| Answer cycle | Moderators answer beginning each **Monday**; questions **close Thursday 5:00 p.m. ET** | CONFIRMED | `[V0]` §1.7.4 |
| **Close date** | **TBA** — neither `[V0]` nor `[DATES]` publishes one | TBA | — |
| Authority | Q&A responses **do not supersede** the manual. **REFEREES and INSPECTORS are the ultimate authority on rules** | CONFIRMED | `[V0]` §1.7.4 |
| Portal | `https://ftc-qa.firstinspires.org/` — live now, opens for BIOBUZZ Sep 28 | CONFIRMED | probed 2026-08-22 |

**On the close date:** DECODE's manual used identical wording and also never published a close date. "No published close date" is the norm, not a BIOBUZZ omission. Do not assume it closes with the last Team Update.

**Weekly rhythm to exploit:** the queue closes Thursday 5:00 p.m. ET and moderation begins Monday. **Submit Monday–Wednesday** so your question lands in the batch being worked rather than sitting a week. Q&A answers feed Team Updates (`[V0]` §1.7.4 → §1.7.3), so an early, well-formed question can change the manual text for everyone.

**Questions FIRST will not answer** (`[V0]` §1.7.4): rulings on vague situations; challenges to past-event decisions; **design-legality reviews of your ROBOT**; overly broad questions with no rule reference; "how should the referee have ruled"; duplicates; and anything clearly addressed in the manual. Good questions cite one or more specific rule numbers and ask generically about a feature, part, or gameplay scenario.

---

## 4. Award deadlines

> ⚠️ **The most important calendar fact about awards: with one exception, there are no FIRST-wide award submission deadlines.** `[V0]` §6 puts submissions on "the deadline established by the **Event Director** or local Program Delivery Partner," and PORTFOLIOs are submitted as instructed by the Event Director. **Your real deadlines arrive by email from your PDP, not from FIRST HQ.** Nothing in this calendar can supply them — set a recurring reminder to chase them.

| Award item | Deadline | Status | Src |
|---|---|---|---|
| FIRST Leadership Award — nominations open | Mon Sep 14, 2026 | CONFIRMED | `[DATES]` |
| **FIRST Leadership Award — nominations DUE** | **Tue Dec 15, 2026** | CONFIRMED | `[DATES]` |
| Leadership Award — semi-finalist emails | Fri Dec 18, 2026 | CONFIRMED | `[DATES]` |
| Leadership Award — finalists due to FIRST | Mon Feb 15, 2027 | CONFIRMED | `[DATES]` |
| Engineering PORTFOLIO / all judged awards | **Set per-event by Event Director / PDP** | CONFIRMED (that it is local) | `[V0]` §6 |
| Judged-work eligibility window | Work from **January 1, 2026** onward counts | CONFIRMED | `[V0]` §6 |

> **Sleeper advantage.** `[V0]` §6 opens the judging window at **January 1, 2026 — eight months before Kickoff.** Outreach, business-plan, fundraising and sustainability work done in spring and summer 2026 is fully documentable in the BIOBUZZ portfolio. Most teams write portfolios as if the season began in September and silently discard two semesters of evidence. (DECODE used the same construction with a Jan 1, 2025 window, so this is stable FIRST practice, not a one-off.)

**Award ordering lead times** if you host an event (`[DATES]` p.2): trophies **5-6 weeks** via `firstinspiresawards.com`; banners **8 weeks** via `shopsli.com/ftc_banners`. Banners are manually reviewed and approved **on the 1st of the month** — submitting on the 2nd costs roughly 30 extra days.

---

## 5. Registration & payment

| Item | Value | Status | Src |
|---|---|---|---|
| Season registration fee | **$350 / season** | CONFIRMED | `[WEB]` cost-and-registration |
| Registration window | Opened Jun 17, 2026; open "through the end of the season (April)" | CONFIRMED | `[WEB]` |
| Purchasing | Via the **FIRST Storefront**; hardware **not** included in the registration fee | CONFIRMED | `[WEB]` |
| Est. additional hardware | ~**$1,500** — Driver Kit $295, **Electronics / Control set** (REV Control Hub + sensors, *not* a bare Control Hub) $350, Build Kit $660, plus optional BIOBUZZ Game / Field sets. These are the **2026-27** website prices; the downloadable storefront PDF is still stamped Rev 25-26.4 and shows the older $285 / $325 / $650 — budget from the website (`research/SMALL-TEAM-ECONOMICS.md` §3.1) | CONFIRMED | `[WEB]` |
| "Competition ready" requirements | Register + pay + **2 adults in Lead Coach 1/2 with YPP screening passed** + all youth registered on the dashboard | CONFIRMED | `[V0]` I101/I102 |
| Event participation fees | **Vary by region, set by local PDP** | CONFIRMED | `[WEB]` |
| FCMP payment due | **2 weeks after preferencing assignment** | CONFIRMED | `[DATES]` |
| FCMP final payment deadline | **TBD** (time known: 5:00 p.m. ET) | TBA | `[DATES]` |
| FCMP drop date | Fri Apr 9, 2027 | CONFIRMED | `[DATES]` |
| Registration / Storefront close | **TBD** | TBA | `[DATES]` |

> **Do this before Sep 28.** The Q&A is gated on **Lead Coach 1/2 dashboard accounts** (`[V0]` §1.7.4), and "competition ready" status requires **two YPP-screened adults in those roles** (`[V0]` I102). YPP screening is not instant. A team that leaves LC2 unfilled loses Q&A access *and* competition eligibility. This is the highest-leverage 20 minutes available to you today.

---

## 6. What we legitimately know about the game before Kickoff

**CONFIRMED** — `[COMM]` *Game Preview 2027: StarterBots, Skill Builders, Field Elements and More!* (May 3, 2026):

- The BIOBUZZ scoring element is **"Pollen"** — plastic balls **approximately 3 in. in diameter**, with handling similar to DECODE's ARTIFACTS.
- FIRST named four tasks explicitly worth prototyping now:
  1. Intake Pollen off the **foam field surface**
  2. Acquire **multiple Pollen at once**, including from lines and piles
  3. Intake **off field walls and out of field corners** (Pollen naturally rolls to the border and into corners)
  4. **Autonomously navigate between known locations and intake Pollen**

**CONFIRMED** `[V0]` **R304** (2nd sentence): **FABRICATED ITEMS created before Kickoff are permitted.**  
> **NB — citation corrected 2026-08-22.** The pre-Kickoff allowance is the **second sentence of R304**, not R305. `pdftotext` detaches rule IDs from their bodies and pairs that sentence with the next ID; **R305 is "SCORING ELEMENTS are not allowed for ROBOT construction."** Verified with `reference/ftc_parse.py`. The permission is real — only the citation was wrong. There is no build-season restriction — a ball intake/indexer prototyped in August is legal on your Kickoff robot.

**CONFIRMED** `[V0]` placeholders — **six** sections: **8** (Game Overview), **9** (ARENA), **10** (Game Details), **11** (Game Rules G), **13** (Tournament T) and **15** (*FIRST* Championship C) each carry only the line *"This section will be updated with the Kickoff Competition Manual release on September 12, 2026"* (V0 pp. 60, 61, 62, 63, 89, 91). Everything else — Introduction, Season Overview, Eligibility & Inspection (I), Advancement, Event Rules (E), Awards (A), ROBOT Construction Rules (R), **§14 League Play Tournaments (L)** and Glossary — is **already final**. ⚠️ **§14 is a common trap: it is fully written, but it cross-references §13.6, Table 13-1 and §10.6.1, which do not exist yet.**

> This is first-party FIRST material, not leak or fan content. **Anything beyond the above** — scoring values, field dimensions, endgame, alliance structure — circulating before Sept 12 is **SPECULATION**, however confident the source sounds.

---

## 7. Conflicts, ambiguities and things to double-check

| # | Conflict | Detail | Recommendation |
|---|---|---|---|
| 1 | **Region cutoff: Nov 16 vs Nov 17** | `[DATES]` lists **Nov 16, 2026** "Region Size Snapshot for FIRST Championship Advancement Calculation". `[V0]` §4.2 says the cutoff is **"November 17th, 2026 for the BIOBUZZ season"**. | Plan to the **earlier** date (Nov 16). This is exactly the sort of inconsistency the Q&A exists to resolve — file it after Sep 28 and it will likely be corrected by Team Update. |
| 2 | **Two different "region counting" dates** | `[DATES]` also has **Aug 17, 2026** — "last date for regions to be counted for FCMP/FPE **capacity-based** advancement." A *different mechanism* from the Nov 16 **size snapshot**. | Do not conflate. Aug 17 = whether a region counts at all; Nov 16/17 = how big it counts as. |
| 3 | **CM Preview date: Jul 29 vs Aug 1 vs Jul 31** | `[COMM]` (Aug 10) says Jul 29; `[DATES]` says Aug 1; the live page version stamp and the PDF itself say **Jul 31, 2026**. | Immaterial in itself, but calibrating: `[COMM]` dates are loose. Trust file stamps and page version strings. |
| 4 | **Game set shipment start: Aug 17 vs Sep 14** | `[DATES]` (Jun 24) says shipments start **Aug 17, 2026 (estimated)**; the May 3 `[COMM]` preview said Sep 14, 2026. | `[DATES]` is newer and itself says "confirm directly with AndyMark". **Call AndyMark.** |
| 5 | **FIRST Championship venue — now RESOLVED** | Previously UNVERIFIED. Confirmed by `[COMM]` *Update: Future of FIRST Championship* (Jan 22, 2026): the **George R. Brown Convention Center in Houston**, committed **through 2034**. | Note that `firstinspires.org/programs/first-championship` still showed **2026** content when checked on 2026-08-22 — the page lags. Do not read its silence on 2027 as a change of plan. |
| 6 | **Page 2 of `[DATES]` is a broken table** | Text extraction emits the date column and label column separately, producing false pairings (e.g. "TBD / July 31, 2027 / Late May / May 20, 2027" as one run). §1.4 rows were reconstructed from PDF word geometry. | Low risk, but verify visually if a §1.4 date becomes load-bearing. |
| 7 | **Preseason Testing Event** | "October 2-4, 2026 (proposed)", location TBD. | Treat as TBA. |
| 8 | **Team Update numbering drifts** | DECODE had 31 Thursdays but ended at TU**32**. | Track dates, not numbers (§2). |

---

## 8. TBA register — do not let anyone fill these in

If someone hands you a number for one of these before FIRST publishes it, it is a prior-season figure or a guess.

1. **Q&A close date** — never published, this season or prior ones.
2. **Last date to order BIOBUZZ-specific field elements from AndyMark.**
3. **FIRST Championship final payment deadline** (time known — 5:00 p.m. ET; date TBD).
4. **Registration / Storefront close date**, and last day to use grant funds.
5. **Preseason Testing Event** date and location.
6. **Your region's qualifier and league-meet dates** — set by your PDP on `ftc-events.firstinspires.org`, not by FIRST HQ. Earliest possible is Oct 15, 2026.
7. **Your region's advancement slot counts** — published early December.
8. **All judged-award submission deadlines** except the FIRST Leadership Award.
9. **Everything in manual Sections 8-11, 13 and 15** — game, ARENA, scoring, Game Rules, Tournament and *FIRST* Championship structure. (§14 League Play is already final in V0.)

---

## 9. T-minus countdown

### 9.1 The next three weeks (T-21 → T-0)

| T | Date | Milestone | Prep action |
|---|---|---|---|
| **T-21** | **Sat Aug 22, 2026** | *Today* | Finish V0 Sections 1-7, 12, 14 and 16 — final now, unchanged at Kickoff. |
| T-20 | Sun Aug 23 | — | **Verify Lead Coach 1 *and* 2 exist, are YPP-screened, and can log into the FIRST dashboard.** Gates both Q&A access and competition eligibility (§5). |
| T-19…T-9 | Aug 24 – Sep 3 | — | Prototype a ~3 in. ball intake per §6. Call AndyMark about the game-set ship date (§7 #4). Grab the already-live 2027 files in `SOURCES.md` §9 Tier 0. |
| **T-8** | **Fri Sep 4** | Early Game Preview — **privacy agreement required** | Sign it if your PDP offers access. Treat contents as embargoed. |
| T-7…T-2 | Sep 5 – Sep 10 | — | Dry-run `tools/ingest-manual.sh` against the V0 PDF. Pre-write your first three Q&A questions. |
| **T-1** | **Fri Sep 11** | Last DECODE off-season event | Clear the bench. Re-read `SOURCES.md` §9 so the download sweep is muscle memory. |

### 9.2 Kickoff onward

| T | Date | Milestone |
|---|---|---|
| **T+0** | **Sat Sep 12, 12:00 p.m. ET** | **KICKOFF** — manual publishes *after* the broadcast. Run ingest + download sweep. |
| T+0…T+6 | Sep 12-18 | SDK release; FTC Live Preview (Beta). |
| T+2 | Mon Sep 14 | Leadership Award nominations open. |
| T+5 | Thu Sep 17 | First regular Thursday Team Update. |
| **T+16** | **Mon Sep 28, 12:00 p.m. ET** | **Team Q&A opens** — end of the 16-day blackout. Submit pre-drafted questions. |
| T+20 | Oct 2-4 | Preseason Testing Event *(proposed)*. |
| **T+33** | **Thu Oct 15** | FTC Live official release · **earliest league meet / qualifier**. Robot must be inspection-legal. |
| T+37 | Mon Oct 19 | PDP deadline to set up region advancement. |
| T+65 | Mon Nov 16 | Region size snapshot *(see §7 #1)*. |
| T+68 | Thu Nov 19 | **Advancement allocations released** — your region's slot count. |
| T+79 | Mon Nov 30 | Earliest Regional Championships. |
| **T+94** | **Tue Dec 15** | **Leadership Award nominations DUE.** |
| T+156 | Mon Feb 15, 2027 | Leadership Award finalists due to FIRST. |
| **T+190** | **Sun Mar 21, 2027** | **Last RCMP for FCMP / Premier advancement.** |
| T+209 | Fri Apr 9, 2027 | FCMP unpaid / unhoteled teams dropped. |
| T+215 | Thu Apr 15, 2027 | Projected final Team Update (DERIVED). |
| **T+228…T+231** | **Wed Apr 28 – Sat May 1, 2027** | **FIRST Championship**, Houston. |
| T+250 | Thu May 20, 2027 | BIOBUZZ "Unlocked" release. |
| T+322 | Sat Jul 31, 2027 | End of FIRST support for BIOBUZZ. |

### 9.3 The five dates that actually change your season

1. **Sep 12** — everything unknown becomes known. Your ingest pipeline either works or you lose the weekend.
2. **Sep 28** — Q&A opens after a 16-day blackout. First-mover advantage on rule ambiguities is real and short-lived.
3. **Oct 15** — earliest advancing event; your "must be competition-legal" date, whether or not your region uses it.
4. **Dec 15** — the only hard, FIRST-wide, non-negotiable award deadline.
5. **Mar 21** — after this, there is no path to Houston.

### 9.4 Three deadlines that are earlier than they look

| Looks like | Actually |
|---|---|
| "Awards are a spring problem" | Portfolio-eligible work started **Jan 1, 2026**. You are already eight months into the window (§4). |
| "Leadership Award is a December thing" | Nominations open **Sep 14** and the nominee needs a documented body of work. December is a *submission* date, not a *start* date. |
| "Banners and trophies can be ordered late" | Banners take **8 weeks** *and* are approved only **on the 1st of the month** — effectively ~9 weeks worst case (§4). |

---

*Compiled 2026-08-22 (T-21). All dates re-verified against live sources on this date; local `[DATES]` and `[V0]` confirmed byte-identical to the files FIRST is currently serving. Re-verify §1.2-1.3 against the Kickoff Competition Manual and any re-issued Key Season Dates PDF (ours is **V26-27.1 / June 24, 2026** — check the stamp) on September 12, 2026.*
