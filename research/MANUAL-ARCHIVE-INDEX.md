# FTC Game Manual Archive — Index, Link Status & Recovery Guide

**Compiled:** 2026-08-22 · **Every URL in this document was live-probed on this date.**
**Scope:** the historical FTC manual corpus (2005-06 → 2026-27), where each document still exists online, and what we hold locally.
**Companion doc:** `research/SOURCES.md` covers *current-season BIOBUZZ* links. This doc covers *history*. Section 10 lists corrections this pass made to SOURCES.md.

---

## 0. The five findings that matter

| # | Finding | Evidence |
|---|---|---|
| 1 | **`usfirst.org` is completely dead — DNS does not resolve.** Not a 404: the domain itself is gone, including `archive.usfirst.org` and `www3.usfirst.org`. Every pre-2016 FTC document is **Wayback-only**. | `curl` returns exit 35 / HTTP `000` for `http://archive.usfirst.org/`, `https://www.usfirst.org/` (probed 2026-08-22) |
| 2 | **The entire `firstinspires.org/sites/default/files/uploads/resource_library/ftc/…` tree now 404s.** All 21 manual URLs probed returned `404 text/html`. This killed *every* official manual link for **2015-16 → 2023-24** — nine seasons. | 21/21 probes returned 404; see §2 |
| 3 | **The modern `ftc-resources.firstinspires.org` archive only reaches back to 2024-25.** `…/ftc/archive/<Y>/game/manual` returns a PDF for Y=2025, 2026, 2027 and **404 for Y=2016…2024**. | 12-year probe sweep, §2 |
| 4 | **`gamemanual0.com` is dead; the live host is `gm0.org`.** SOURCES.md §10 cited the dead domain. | `gamemanual0.com` → DNS fail; `gm0.org` → 200 |
| 5 | **`ftcforum.firstinspires.org` now redirects to `ftc-community.firstinspires.org`** (Discourse), which has **no Game Q&A category**. The old vBulletin Q&A threads appear **not** to have been carried over. Official Q&A now lives in the separate `ftc-qa.firstinspires.org` app. | redirect chain + category listing, §8 |

> **Net effect:** for 2005-06 through 2023-24 — twenty seasons — the Wayback Machine is the *only* surviving route to the game manuals. Our local mirror is therefore the primary asset, not a convenience copy.

---

## 1. Season-by-season master index

**Legend — Document set:** `GM 1+2` = Game Manual Part 1 (rules/tournament) + Part 2 (game-specific). `CM` = single Competition Manual. `Sectioned` = manual published as separate section PDFs.
**Legend — Live URL:** ✅ live today · ⛔ dead, Wayback-only.

| Season | Game | Document set | Trad/Remote split | Live official URL | Held locally |
|---|---|---|---|---|---|
| 2005-06 | Half-Pipe Hustle *(FVC pilot)* | Single manual + one-pager | — | ⛔ | ✅ manual (image-only, see §5) + 2 one-pagers |
| 2006-07 | Hangin-A-Round *(FVC)* | Single manual **+ Sectioned 1-8 + App. 1-4** | — | ⛔ | ✅ complete manual, coaches handbook, App. 1/3/4, tips |
| 2007-08 | Quad Quandary | Single manual | — | ⛔ | ✅ manual + one-pager |
| 2008-09 | Face Off | Complete manual **+ Sectioned** | — | ⛔ | ✅ complete, Coach manual, §4 Robot, §5 Notebook |
| 2009-10 | Hot Shot | Single manual, **revised to Rev 7** | — | ⛔ | ✅ **Rev 5, Rev 6, Rev 7 (final)** + Coach manual |
| 2010-11 | Get Over It | Single manual | — | ⛔ | ✅ manual, Coaches Rev 3, **Game Hints** |
| 2011-12 | Bowled Over | Single manual (Rev 5) | — | ⛔ | ✅ manual + Forum Q&A |
| 2012-13 | Ring It Up | **GM 1+2** *(first split year)* | — | ⛔ | ✅ Part 1, Part 2, Q&A |
| 2013-14 | Block Party | GM 1+2 | — | ⛔ | ✅ Part 1, Part 2, Q&A, 2 inspection checklists |
| 2014-15 | Cascade Effect | GM 1+2 | — | ⛔ | ✅ Part 1, Part 2 |
| 2015-16 | RES-Q | GM 1+2 | — | ⛔ | ✅ Part I, Part II, early rev, Q&A |
| 2016-17 | Velocity Vortex | GM 1+2 | — | ⛔ | ✅ Part 1, Part 2, Q&A |
| 2017-18 | Relic Recovery | GM 1+2 | — | ⛔ | ✅ Part 1, Part 2, Q&A |
| 2018-19 | Rover Ruckus | GM 1+2 | — | ⛔ | ✅ Part 1, Part 2, Q&A |
| 2019-20 | SKYSTONE | GM 1+2 | — | ⛔ | ✅ Part 1, Part 2, Q&A, GM2 §4 |
| 2020-21 | ULTIMATE GOAL | GM 1+2 | ✅ **split begins** | ⛔ | ✅ all 4 variants, Q&A (Remote), Judge manual |
| 2021-22 | Freight Frenzy | GM 1+2 | ✅ | ⛔ | ✅ all 4 variants, Q&A (Trad) |
| 2022-23 | POWERPLAY | GM 1+2 | ✅ | ⛔ | ✅ all 4 variants, Q&A |
| 2023-24 | CENTERSTAGE | GM 1+2 *(last GM 1+2 year)* | ✅ **split ends** | ⛔ | ✅ all 4 variants, Q&A, Robot Inspection manual |
| 2024-25 | INTO THE DEEP | **CM** *(single manual begins)* | — | ✅ `…/archive/2025/game/manual` | ✅ V14 + kickoff V1 + §11 + Q&A + updates + Referee manual |
| 2025-26 | DECODE | CM | — | ✅ `…/archive/2026/game/manual` | ✅ TU32 + kickoff + §11 + Q&A + updates + field docs |
| 2026-27 | **BIOBUZZ** | CM | — | ✅ `…/archive/2027/game/manual` | ✅ V0 pre-season (§8-11, 13, 15 are placeholders) |

**Nothing exists before 2005-06.** Half-Pipe Hustle was the first official FIRST Vex Challenge game; the program ran as FVC for two seasons and was renamed FIRST Tech Challenge in summer 2007 ([Wikipedia: Half-Pipe Hustle](https://en.wikipedia.org/wiki/Half-Pipe_Hustle); [Wikipedia: FIRST Tech Challenge](https://en.wikipedia.org/wiki/FIRST_Tech_Challenge) — community-sourced, but consistent with the FIRST-hosted `05_fvcpilot_game.pdf` we hold). Our corpus therefore reaches the true origin of the program.

---

## 2. The three URL regimes (and which is dead)

FTC manuals have lived at three successive URL schemes. Knowing which regime a season belongs to tells you instantly where to look.

| Regime | Years covered | URL shape | Status 2026-08-22 |
|---|---|---|---|
| **A. usfirst.org** | 2005-06 → ~2015 | `usfirst.org/uploadedFiles/…/FTC/Game_Info/<year>/<file>.pdf`; later `…/sites/default/files/uploadedFiles/…`; hosts `www.`, `www3.`, `archive.` | ⛔ **DNS dead** — domain no longer resolves at all |
| **B. firstinspires.org resource_library** | 2015-16 → 2023-24 | `firstinspires.org/sites/default/files/uploads/resource_library/ftc/[<season>/]<slug>.pdf` | ⛔ **All 404** (21/21 probed) |
| **C. ftc-resources.firstinspires.org** | 2024-25 → present | `ftc-resources.firstinspires.org/ftc/archive/<springYear>/<category>/<slug>` | ✅ live, **but only Y ≥ 2025** |

### Regime C reach test (probed 2026-08-22)

| Y | `…/archive/Y/game/manual` |
|---|---|
| 2016–2024 | `404 text/html` (9 consecutive years) |
| 2025 | `200 application/pdf` 4,659,851 B — INTO THE DEEP |
| 2026 | `200 application/pdf` 6,414,570 B — DECODE |
| 2027 | `200 application/pdf` 1,704,884 B — BIOBUZZ V0 |

Note the season-root landing pages (`…/archive/2024`) *do* return 200 — but they are empty shells listing only a "Game and Season Materials" link that itself 404s. **A 200 on a landing page is not evidence the documents survive.**

### Regime B slug vocabulary (all dead, all Wayback-recoverable)

Useful because the Wayback CDX index is keyed on these exact strings:

```
resource_library/ftc/game-manual-part-1.pdf                     (2017-18, 2018-19 — unversioned, overwritten each year)
resource_library/ftc/game-manual-part-2.pdf
resource_library/ftc/game-manual-part-1-traditional-events.pdf  (2020-21)
resource_library/ftc/game-manual-part-1-remote-events.pdf
resource_library/ftc/game-manual-part-1-traditional.pdf         (2021-22+)
resource_library/ftc/game-manual-part-2-remote.pdf
resource_library/ftc/first-res-q/game-manual-part-I.pdf         (2015-16, season-foldered)
resource_library/ftc/2016-2017/velocity-vortex-game-manual-part-1.pdf
resource_library/ftc/2017-2018/game-manual-part-1.pdf
resource_library/ftc/2018-2019/game-manual-part-1.pdf
resource_library/ftc/2019-2020/skystone-game-manual-part-1.pdf
resource_library/ftc/2020-2021/ultimate-goal-game-manual-part-1-traditional-events.pdf
resource_library/ftc/freight-frenzy-game-manual-part-1-traditional-events.pdf
resource_library/ftc/forum-answered-questions[-traditional|-remote].pdf
resource_library/ftc/referee-and-head-referee-manual.pdf
resource_library/ftc/robot-inspection-manual.pdf
resource_library/ftc/judge-and-judge-advisor-manual.pdf
resource_library/ftc/game-manual-part1-traditional-chinese.pdf  (translations)
resource_library/ftc/romanian-game-manual-part-1-*.pdf
```

⚠️ **Unversioned-slug trap.** `game-manual-part-1.pdf` and `forum-answered-questions.pdf` were *overwritten in place* every season. A Wayback snapshot of that URL is only identifiable by its **capture date**, not its filename. Always verify the season string inside the PDF after fetching — this pass caught one file misfiled by three seasons that way (§4.4).

---

## 3. Document-set eras — which variant should an analyst read?

| Era | Seasons | What to read |
|---|---|---|
| **Single manual** | 2005-06 → 2011-12 | One PDF holds everything. Watch revision numbers — Hot Shot reached **Rev 7**. |
| **Game Manual Part 1 + Part 2** | 2012-13 → 2023-24 | **Part 1** = season-invariant: robot construction, inspection, tournament, awards. **Part 2** = the game itself: field, scoring, `<G>` rules. **For game-strategy work read Part 2; for build-legality work read Part 1.** |
| **Single Competition Manual** | 2024-25 → present *(incl. BIOBUZZ)* | Part 1 and Part 2 merged into 16 numbered sections. Game rules are **§11 (G)**; robot rules **§12 (R)**. |

### Traditional vs Remote (2020-21 → 2023-24)

COVID-era FIRST published **two parallel manuals per part** — four PDFs per season. Verified by md5: the Remote and Traditional PDFs are **genuinely different documents** in all four seasons, not duplicates:

| Season | Part 1 Remote vs Traditional |
|---|---|
| 2020-21 ULTIMATE GOAL | DIFFERENT — 944,053 vs 1,163,725 B |
| 2021-22 Freight Frenzy | DIFFERENT — 1,260,861 vs 1,498,342 B |
| 2022-23 POWERPLAY | DIFFERENT — 1,247,462 vs 1,494,241 B |
| 2023-24 CENTERSTAGE | DIFFERENT — 1,309,189 vs 1,586,750 B |

**Which to read:** the **Traditional** manual describes a normal 2-alliance, 4-team field and is the correct lineage ancestor of the modern Competition Manual. Read Remote only when studying how FIRST restructured scoring for solo play. *(Analyst note: the Remote variants are a rich and under-used source of scoring-system edge cases, because FIRST had to re-derive every scoring rule for a 1-robot field.)*

---

## 4. New acquisitions this pass

All fetched from the Wayback Machine using raw-byte (`id_`) replay, validated as real PDFs, and text-extracted with `pdftotext -layout`.

### 4.1 Into `manuals/archive/wayback/` — pre-2015 gap fill

| File | Wayback snapshot | Why it matters |
|---|---|---|
| `2005-06_FVC_PilotGameDescription_RevJan2006.pdf` | `20060912192535` | Revised pilot-game description; **differs** from the original one-pager we already held |
| `2006-07_HANGINAROUND_FVC_CoachesHandbook.pdf` | `20070713204237` | 175 KB of extracted text — richest surviving 2006-07 document |
| `2006-07_HANGINAROUND_FVC_Appendix1_RobotInspectionGuidelines.pdf` | `20070713204321` | Earliest surviving FTC/FVC inspection rules |
| `2006-07_HANGINAROUND_FVC_Appendix3_JudgingAwardsRubrics.pdf` | `20070713203921` | Earliest surviving **awards rubrics** — direct ancestor of §6 (A) rules |
| `2006-07_HANGINAROUND_FVC_Appendix4_InspectionChecklist.pdf` | `20070713203951` | Image-heavy; thin text layer |
| `2006-07_HANGINAROUND_FVC_CompetitionTipsAndBestPractices.pdf` | `20070713204334` | FIRST own strategy advice |
| `2008-09_FACEOFF_GameManual_Section4_TheRobot.pdf` | `20081010065352` | Sectioned-manual era robot rules |
| `2008-09_FACEOFF_GameManual_Section5_EngineeringNotebook.pdf` | `20121224152818` | Ancestor of the Portfolio requirements |
| `2009-10_HOTSHOT_GameManual_Complete_Rev5.pdf` | `20120226082941` | Rev 5 |
| `2009-10_HOTSHOT_GameManual_Rev6.pdf` | `20101227070314` | Rev 6 |
| `2010-11_GETOVERIT_GameHints.pdf` | `20161223232823` | **FIRST-authored "Game Hints"** — an official strategy document, a format FIRST no longer publishes |
| `2013-14_BLOCKPARTY_HardwareInspectionChecklist.pdf` | `20141127005956` | Inspection checklist lineage |
| `2013-14_BLOCKPARTY_RobotInspectionChecklist.pdf` | `20140401205221` | Inspection checklist lineage |

**Base URLs** (prefix with `https://web.archive.org/web/<snapshot>id_/`):
- FVC 2006-07: `http://www.usfirst.org/uploadedFiles/Community/FVC/FVC_Documents_and_Updates/2006_FVC_*.pdf`
- FVC pilot: `http://www.usfirst.org:80/vex/FVCresourcectr/facts/05_fvcpilot_game_revjan06.pdf`
- FTC 2008: `http://usfirst.org:80/uploadedFiles/Community/FTC/FTC_Documents_and_Updates/2008/…`
- FTC 2009-2013: `http://{www,www3,archive}.usfirst.org/sites/default/files/uploadedFiles/Robotics_Programs/FTC/Game_Info/<year>/…`

### 4.2 Into `manuals/archive/supplemental/` — Q&A archives, gap years filled

The official Q&A archive slug (`…/game/q-a`) only reaches back to **2022-23**. Everything earlier was recovered from the overwritten `forum-answered-questions*.pdf` slug by picking snapshots by date:

| File | Snapshot | Pages | Note |
|---|---|---|---|
| `2015-16_RESQ_Complete_QA.pdf` | `20151210202616` | 119 | verified "RES-Q" inside |
| `2016-17_VELOCITYVORTEX_Complete_QA.pdf` | `20170105004318` | 101 | season-foldered slug |
| `2017-18_RELICRECOVERY_Complete_QA.pdf` | `20180605052510` | 132 | post-season = final |
| `2018-19_ROVERRUCKUS_Complete_QA.pdf` | `20190507083801` | 123 | post-season = final |
| `2019-20_SKYSTONE_Complete_QA.pdf` | `20200202192358` | 75 | |
| `2020-21_ULTIMATEGOAL_Complete_QA_Remote.pdf` | `20210123010959` | 48 | **Remote only** — see §5 |
| `2021-22_FREIGHTFRENZY_Complete_QA_Traditional.pdf` | `20211222153818` | 48 | ⚠️ **mid-season (2021-12-16)**, not final |

**Coverage after this pass:** every season 2011-12 → 2025-26 now has a Q&A archive locally, except 2014-15 (never found) and 2020-21 Traditional (§5).

### 4.3 Into `manuals/archive/supplemental/` — rule-interpretation manuals

These are how *officials* are trained to apply the rules — the highest-value non-manual source for loophole work, because they show where FIRST expects judgement calls.

| File | Season verified inside | Snapshot |
|---|---|---|
| `2024-25_ITD_RefereeAndHeadReferee_Manual.pdf` | 2024-2025 INTO THE DEEP | `20250915061621` |
| `2023-24_CENTERSTAGE_RobotInspection_Manual.pdf` | 2023-2024 CENTERSTAGE | `20240419193431` |
| `2020-21_ULTIMATEGOAL_JudgeAndJudgeAdvisor_Manual.pdf` | 2020-2021 | `20201111235950` |
| `2019-20_SKYSTONE_GM2_Section4_TheGame.pdf` | 2019-2020 SKYSTONE | `20200202192405` |

> The Referee manual is the **most recent** of these (captured Sep 2025) and is the closest available proxy for how BIOBUZZ officiating will be trained. **Label: HISTORICAL-PATTERN**, not confirmed for BIOBUZZ.

### 4.4 Corrections made to existing local files

| Action | Detail |
|---|---|
| **Deleted duplicate** | `2005-06_FVC_PilotGameDescription_Original.pdf` was **byte-identical** (md5 `7cd629161a35c1…`) to the existing `2005-06_OnePageGameDescription.pdf`. Removed. |
| **Renamed — wrong season by 3 years** | A file fetched as `2022-23_POWERPLAY_GM2_Section4_TheGame.pdf` proved to be **SKYSTONE 2019-20** on content inspection (unversioned-slug trap). Renamed `2019-20_SKYSTONE_GM2_Section4_TheGame.pdf`. |
| **Renamed — revision mislabel** | Our long-held `2009-10_HOTSHOT_GameManual.pdf` is actually **Rev 7**, i.e. *newer* than the "Rev 6" fetched believing it final. Renamed to `…_Rev7_FINAL.pdf`; the fetched file is now `…_Rev6.pdf`. **Three distinct md5s confirm three genuine revisions.** |

---

## 5. Genuinely gone, or degraded

| Item | Status | Detail |
|---|---|---|
| **2020-21 ULTIMATE GOAL Q&A — *Traditional*** | ❌ **Unrecoverable** | Exactly **one** capture exists (`20201124002440`) and it is **truncated at exactly 1,048,576 B (1 MiB)**. Yields 0 parseable pages. Retried across `id_`, `if_`, `im_` and bare replay — identical truncation every time, so the defect is in Wayback stored record. **Mitigation:** the *Remote* variant for the same season is complete (48 pp) and shares all robot/build Q&A. |
| **2014-15 Cascade Effect Q&A** | ❌ Not found | No `FTC_Forum_Answered_Questions.pdf` snapshot for the 2014 season surfaced in CDX. Q&A exists for 2011-12, 2012-13, 2013-14 then resumes 2015-16. |
| **2005-06 Half-Pipe Hustle manual** | ⚠️ **No text layer** | Scanned-image PDF; `pdftotext` yields nothing. **OCR required** before any text analysis. The one-pagers for the season *are* text-bearing and carry the scoring summary. |
| `2005-06_…RobotDesignTipsAndBestPractices` | ⚠️ No text layer | 6-byte extraction. Image-only. |
| `2007-08_OnePageGameDescription` | ⚠️ No text layer | 1-byte extraction. Image-only. |
| `2006-07_…Appendix4_InspectionChecklist` | ⚠️ Thin text | 636 B extracted; largely a scanned form. |
| **2006-07 FVC Manual "Sections 1-8" combined** | ❌ Snapshot is not a PDF | Wayback returned a 10,602 B non-PDF for that slug. **No loss** — we hold the complete 2006-07 manual plus the appendices separately. |
| **Pre-2005 anything** | ❌ Does not exist | The program began with the 2005-06 FVC pilot. |

---

## 6. Q&A archive index

| Season | Local file | Source |
|---|---|---|
| 2011-12 → 2013-14 | `*_ForumAnsweredQuestions.pdf` | usfirst.org `Game_Info/<yr>/FTC_Forum_Answered_Questions.pdf` (Wayback) |
| 2014-15 | ❌ missing | — |
| 2015-16 → 2021-22 | `*_Complete_QA*.pdf` | firstinspires `forum-answered-questions*.pdf` (Wayback, date-selected) |
| 2022-23 → 2025-26 | `*_Complete_QA.{html,pdf}` | ✅ **live**: `ftc-resources.firstinspires.org/ftc/archive/<Y>/game/q-a` |
| 2026-27 BIOBUZZ | ❌ 404 until kickoff | Q&A opens **2026-09-28, 12:00 ET** (per SOURCES.md §5) |

**Live `q-a` slug reach (probed):** 2021 ❌ · 2022 ❌ · 2023 ✅ 388,073 B · 2024 ✅ 1,072,659 B · 2025 ✅ 284,482 B · 2026 ✅ 201,377 B · 2027 ❌.
All four live sizes are **byte-identical to our local copies** — our 2022-23 → 2025-26 Q&A mirror is confirmed current.

---

## 7. Local corpus after this pass

| Location | Contents | Count |
|---|---|---|
| `manuals/archive/wayback/` | 2005-06 → 2019-20 manuals, coach manuals, one-pagers, checklists | **51 PDF + 51 .txt** |
| `manuals/archive/` | 2020-21 → 2023-24 (all 4 Trad/Remote variants each) + 2024-25 / 2025-26 / 2026-27 CM | 19 PDF + .txt |
| `manuals/archive/supplemental/` | Q&A archives, referee/inspection/judge manuals, field guides, Team Updates | **28 PDF** + HTML/zip |
| `manuals/_reference_prior_seasons/` | ITD + DECODE kickoff vs final manuals, §11 extracts, Team Updates | 12 files |
| `manuals/2026-27_BIOBUZZ/` | V0 manual, layout/raw text, per-section splits | — |

Only 5 `.txt` files remain under 2 KB, all accounted for in §5.

---

## 8. Community & official-adjacent sources

| Source | URL | Status | Assessment |
|---|---|---|---|
| **Game Manual 0** | `https://gm0.org/` | ✅ **200** | Community-written design/strategy reference. Source repo `github.com/gamemanual0/gm0` (✅ 200). Sections: Being a Team · Design Skills · Hardware Components · Common Mechanisms · Custom Manufacturing · Electronics & Motion · Software · Awards · Appendix. **Community-sourced — never cite as rule authority.** *Maintainer identity and license: UNVERIFIED (no reachable About/License page).* |
| ~~gamemanual0.com~~ | — | ⛔ DNS dead | Superseded by `gm0.org`. Fix any stored bookmark. |
| **FTC Community forum** | `https://ftc-community.firstinspires.org/` | ✅ 200 | Discourse. Categories: Announcements, Software, Hardware, Machine Learning, In The Pits, Events, Bug Reports. **No Game Q&A category.** |
| ~~ftcforum.firstinspires.org~~ | redirects → above | ⚠️ | Old vBulletin Q&A threads appear **not** migrated. `…/forum/game-q-a` → **404**. |
| **Official Team Q&A app** | `https://ftc-qa.firstinspires.org/` | ✅ 200 | A rule authority alongside the manual + Team Updates. Opens for BIOBUZZ 2026-09-28. |
| **ftc-docs** | `https://ftc-docs.firstinspires.org/` | ✅ 200 | Official technical documentation. |
| Chief Delphi | `chiefdelphi.com` | ✅ | Community. |
| r/FTC | `reddit.com/r/FTC` | ⚠️ 403 to `curl` | Bot-blocked; fine in a browser. Community. |

---

## 9. Recipe: pulling a manual out of the Wayback Machine

Two steps — find a good snapshot, then fetch **raw bytes**.

```bash
# 1. List distinct 200-status captures of a dead URL
U='http://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/game-manual-part-1.pdf'
ENC=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1],safe=''))" "$U")
curl -s "http://web.archive.org/cdx/search/cdx?url=$ENC&output=text\
&fl=timestamp,statuscode,length&filter=statuscode:200&collapse=digest"

# 2. Fetch RAW bytes with the id_ modifier (no Wayback banner injected)
curl -L -o out.pdf "https://web.archive.org/web/<TIMESTAMP>id_/$U"
```

**Non-obvious gotchas, all hit during this pass:**
- **Use `id_`.** Without it Wayback injects its toolbar and corrupts binaries.
- **`collapse=digest` deduplicates.** Distinct digests = genuinely different documents = usually different seasons for an overwritten slug.
- **CDX `length` is the *compressed* WARC record size**, not the file size. Do not use it to detect truncation.
- **Always validate.** `head -c 5` must equal `%PDF-`; then open with pymupdf and assert `page_count > 0`. A 200 response can still be an HTML error page or a truncated record.
- **A file size of exactly 1048576 / 2097152 means truncation**, not a small document.
- **Verify the season string inside the PDF** for any unversioned slug before trusting the filename.
- Retry transient `000`/empty responses once — Wayback rate-limits; one SKYSTONE fetch failed then succeeded unchanged.

---

## 10. Corrections to `research/SOURCES.md`

| SOURCES.md | Claim | Correction |
|---|---|---|
| §1 line 56 | "Historical manuals 2020-21 → 2025-26 · `…/ftc/archive/<year>/game/manual` · ✅" | ❌ **Wrong.** Only 2024-25, 2025-26, 2026-27 resolve. 2020-21 → 2023-24 return **404** and are Wayback-only. |
| §1 line 54 | ITD manual URL "✅ (assumed, same scheme)" | ✅ **Now verified** — `…/archive/2025/game/manual` returns 4,659,851 B PDF. |
| §10 line 347 | Game Manual 0 at `https://gamemanual0.com/` | ❌ **Dead domain.** Use `https://gm0.org/`. |
| §10 | `ftcforum.firstinspires.org` listed as official Q&A forum | ⚠️ Now redirects to `ftc-community.firstinspires.org`; **no Game Q&A there**. Q&A is at `ftc-qa.firstinspires.org`. |
| §11 line 362 | wayback dir "2005-06 → 2019-20" | Still true; contents grew from 38 to **51** PDFs this pass. |

---

## 11. Analyst notes — what this archive is actually good for

Labelled per the project convention.

- **HISTORICAL-PATTERN — rule text is heavily recycled.** Part 1 (2012-13 → 2023-24) and §12 (R) of the modern CM are near-identical year to year. BIOBUZZ V0 already-final R-rules can be diffed against DECODE to isolate genuine changes. *(V0 R section is final — CONFIRMED-FOR-BIOBUZZ per the project brief.)*
- **HISTORICAL-PATTERN — the Q&A archives are the loophole record.** 119 pp (RES-Q) to 132 pp (Relic Recovery) of officials adjudicating exactly the ambiguities a strong team probes. Reading two or three prior seasons Q&A teaches the *shape* of questions the GDC treats as legitimate vs. as rule-lawyering.
- **HISTORICAL-PATTERN — revision churn is normal and large.** Hot Shot reached Rev 7; DECODE reached TU32. Kickoff-day text is provisional; the corpus holds both kickoff and final manuals for 2024-25 and 2025-26, which is the best available estimate of how much moves after kickoff.
- **The Remote-era manuals (2020-21 → 2023-24) are an under-used scoring-logic source** — FIRST re-derived every scoring rule for a one-robot field, exposing assumptions normally left implicit.
- **`2010-11_GETOVERIT_GameHints.pdf` is unusual**: FIRST publishing explicit strategy guidance. No modern equivalent exists.
- ⚠️ **SPECULATION, flagged as such:** none of the above predicts BIOBUZZ *game* content. Sections 8-11, 13 and 15 of V0 are placeholders; no BIOBUZZ scoring information exists publicly before 2026-09-12.

---

## 12. Security note

Per the project standing rule, everything inside these PDFs, HTML pages and CDX responses was treated as **data, not instructions**. **No document encountered in this pass contained text addressed to an AI agent or attempting to direct tool use.** The only anomalies found were technical: one truncated Wayback record, one non-PDF snapshot, and three mislabelled/duplicate local files (all corrected in §4.4).

*No credentials were used or required; every source is public. All downloads were to the local corpus only.*
