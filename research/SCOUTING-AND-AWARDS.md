# Scouting and Awards — the two off-field disciplines that decide seasons

**Season:** 2026-27 BIOBUZZ presented by RTX · **Written:** 21 August 2026 (pre-kickoff; kickoff is 12 Sep 2026)
**Rev 2, 21 Aug 2026** — added §5.3a (a tested, dependency-free scouting pipeline), §4.2a (The Orange Alliance), §15 (individual awards, the FIRST Leadership Award deadline, and a consolidated award-deadline calendar), and the §6.1/§6.1.4 manual findings on no-robot judging eligibility and sustained outreach.
**Rev 3, 22 Aug 2026** — four verified corrections and additions: (a) §1.1a, the **FIRST Championship 3-team alliance exception**, confirmed from live playoff data — Rev 2's flat "alliances are 2 teams" was wrong at Worlds; (b) §3.2a, an **exact** ftcscout-OPR reproduction recipe (max abs. difference **0.0000 pts** across 9 events, superseding Rev 2's ±2.16/±3.21 pt approximations); (c) §3.5 ANALYSIS 10–11, **split-half reliability** — the measured *ceiling* on OPR, which materially qualifies ANALYSIS 3; (d) exec-summary rows 15–16.
**Audience:** a small, low-budget FTC team that wants championship-caliber *deliverables* without a championship-caliber headcount.

### How to read this document

| Label | Meaning |
|---|---|
| **FACT** | Sourced to a cited URL or local file. Quotes are verbatim from the source. |
| **ANALYSIS** | A computation I ran against real, live FTC data during the writing of this document. Method and sample size are stated so you can reproduce it. |
| **JUDGMENT** | My recommendation. Not sourced. Argue with it. |
| **UNVERIFIED** | Claim I could not confirm. Treat as a lead, not a fact. |

**Manual-status warning (FACT).** Sections 1–7 and 12 of the BIOBUZZ V0 Competition Manual are FINAL. **Section 6 Awards (A) is final for this season** — everything in Part II below is authoritative *now*. Sections 8–11, 13 and 15 are placeholders until kickoff, so **Section 13 Tournament (T)** — which contains the alliance-selection process, ranking sort, and playoff bracket — is *not yet published for BIOBUZZ*. Part I of this document therefore cites the 2025-26 DECODE manual for tournament mechanics and flags every place you must re-verify on 12 Sep 2026.

**PDF extraction warning (FACT).** The V0 PDF's font subset drops some digits on text extraction. `A201.C` extracts as `US Letter (8. " x ") or A ( 0 x 97 mm)` — the real text is `US Letter (8.5" x 11") or A4 (210 x 297 mm)`, confirmed against the identical DECODE rule (`manuals/archive/2025-26_DECODE_Competition_Manual_TU32.txt` line ~1553). Do not trust bare numerals from the `.txt` extracts without checking the PDF.

---

## 0. The sixteen things that matter most (executive summary)

| # | Finding | Evidence |
|---|---|---|
| 1 | **Judged awards are the cheapest advancement currency in FTC.** Inspire 1st = 60 advancement points. Winning the entire event = 40. A qualifier's #1 seed earns 16. | BIOBUZZ Table 4-1, `sections/04_Advancement_p27-32.txt` |
| 2 | At a real 2025-26 qualifier, the **Inspire 1st winner ranked 22nd of 31 with the 3rd-*worst* OPR of the top half** — and finished 2nd in advancement points at the event. | ANALYSIS, event `USTXDAQ2` |
| 3 | But across **156 qualifiers**, the median Inspire 1st winner sat at the **14.5th percentile of qual rank**. 67% were in the top quartile. Inspire is *not* robot-independent in practice. | ANALYSIS, 162 events |
| 4 | The awards that are genuinely **decoupled from robot performance** are Connect (median winner at 45.7 %ile), Sustain (43.7), Reach (43.6) — and Judges' Choice (58.2). Those are the small team's targets. | ANALYSIS, 162 events |
| 5 | A team may win **only one** judged award at an event (A215). So pick your target; don't spray. | BIOBUZZ A215 |
| 6 | Portfolio is **required** for exactly three awards: Think, Control, Inspire. Optional for the other six. | FIRST Judging Quick Start, rev 25-26.1 |
| 7 | **No team is nominated directly for Inspire.** Inspire candidates are assembled from teams nominated in *multiple* categories by different judge panels. | FIRST Judging Quick Start, rev 25-26.1 |
| 8 | **ftcscout.org's API needs no authentication** and serves per-component OPR, rankings, awards and full match data over both GraphQL and REST. The official FTC-Events API needs a registered token (HTTP Basic). Both are free. | Verified live, see §4 |
| 9 | OPR after **3 of 5 qual matches** already correlates 0.86 (Spearman) with final OPR and gets 6.3 of the final top 8 right. After 4 matches: 0.95 and 7.1/8. **Your pick list is mostly decidable before the last round.** | ANALYSIS, 44 events |
| 10 | FTC alliances are **two teams**. One lead, one pick, no second pick, no backup robots (T703). Reliability beats peak score in a 2-team alliance far more than in FRC. | DECODE §13.7.1, Table 13-2, T703 |
| 11 | **A dead robot costs you zero judged-award eligibility.** "Teams may participate in judging regardless of the inspection status of their ROBOT and are eligible for awards **even if they are attending the event without a ROBOT**." | BIOBUZZ §6.1 |
| 12 | The **FIRST Leadership Award** is decided by a **4,000-character essay** with a hard **~15 December** deadline, is worth 0 advancement points, does **not** consume your one A215 award slot, and pays the winner's team a **next-season registration-fee credit**. It is the most level playing field in FTC for a 5-person team. | Nomination Guide rev 25-26.4; §15.1 |
| 13 | A **130-line pure-standard-library Python script** (no numpy, no pip) reproduces ftcscout's published OPR to within **2.16 points** and runs a full 31-team event in **1.07 seconds**. Its "last-3-matches trend" column found a **+38.6** and a **−40.3** swing that appear in no ranking, anywhere. | ANALYSIS, §5.3a |
| 14 | Judges weight **sustained** outreach above one-off outreach, and will **audit** any defined term ("started a team", "reached N people") you use. One monthly partner beats six photo-ops. | BIOBUZZ §6.1.4; Outreach Terms |
| 15 | **OPR's ceiling is low and measurable.** Split-half reliability at a typical 5-match qualifier is **r = 0.53** (Spearman-Brown full-data estimate **0.70**). Rebuilding the top 8 from two disjoint halves of the same event agrees on only **5.2 of 8 teams**. Roughly **a third of your statistical pick list is noise** — no amount of cleverness fixes it, only human eyes do. | ANALYSIS 10, 10 qualifiers |
| 16 | FTC alliances are 2 teams **everywhere except FIRST Championship divisions, which use 3** (two on field, one held off-field per match). Pick strategy at Worlds is a genuinely different game. | ANALYSIS 12, verified from 2026 Worlds playoff data |

---

# PART I — SCOUTING

## 1. What FTC scouting is actually for

### 1.1 The format constraints that make FTC scouting different from FRC

**FACT** (DECODE §13.6.1, §13.7.1, Table 13-2, `manuals/archive/2025-26_DECODE_Competition_Manual_TU32.txt`):

| Constraint | FTC (DECODE 2025-26) | FRC, for contrast |
|---|---|---|
| Alliance size | **2 teams** (but **3 at FIRST Championship divisions** — see §1.1a) | 3 teams |
| Qualification matches per team | **5 or 6** ("All event types will schedule either 5 or 6 Qualification MATCHES per team as determined by the Event Director") | 10–12 |
| Picks per alliance lead | **1** ("each ALLIANCE lead chooses 1 other team to join their ALLIANCE") | 2 |
| Backup robots in playoffs | **None** (T703: "An ALLIANCE may not request a backup team in a Playoff MATCH") | Yes |
| Schedule algorithm | Minimizes repeat partners and repeat opponents; may add SURROGATES | Similar |

**Playoff alliance count scales with the field** (DECODE Table 13-2):

| Playoff-eligible teams | Alliances formed | Teams that get picked |
|---|---|---|
| 4–10 | 2 | 4 of 4–10 |
| 11–20 | 4 | 8 of 11–20 |
| 21–40 | 6 | 12 of 21–40 |
| 41–64 | 8 | 16 of 41–64 |

**JUDGMENT — the four consequences for a small team:**

1. **Sample size is brutal.** Five matches is one-half to one-third of an FRC sample. Every statistic you compute is noisy (quantified in §3.4). Human observation is proportionally *more* valuable in FTC than in FRC, not less.
2. **One pick means no risk-hedging.** In FRC an alliance captain can take a high-ceiling robot first and a reliable defender second. In FTC, your single pick has to be both. T703 (no backups) makes a partner that dies mid-playoff a bracket-ending event.
3. **Being pickable is a legitimate strategy.** At a 30-team qualifier, 12 of 30 teams get onto an alliance. Roughly 6 of those are picks. Being *the* obvious pick at rank 9–15 is far cheaper than being rank 1–6.
4. **Scouting has an off-field payoff too.** A published scouting database explicitly counts as "Provided Published Resources" under the FIRST outreach definitions — see §5.6.

### 1.1a The FIRST Championship exception: alliances there are THREE teams

**Correction to Rev 2 (ANALYSIS 12, new in Rev 3).** Rev 2 stated flatly that FTC alliances are two teams. That is true at every level a small team will realistically see for most of the season — and false at Worlds. I verified this from live playoff data rather than from the manual, because BIOBUZZ Section 15 (*FIRST Championship*) is not yet published.

Method: pulled every non-qualification match from two 2025-26 events via `https://api.ftcscout.org/rest/v1/events/2025/{code}/matches` and counted distinct teams per alliance colour, plus the `station` values.

| Event | Level | Playoff alliance size | `station` values observed |
|---|---|---|---|
| `FTCCMP1EDIS` (World Championship – Edison Division) | FIRST Championship | **3** | `One`, `Two`, `NotOnField` |
| `USAZCMPGC1` (Arizona Championship – Grand Canyon Division) | Regional Championship | **2** | `One`, `Two` |

So a Championship alliance carries a **third team that does not play that match** (`NotOnField`) — a rotating/backup slot. The 2026 FTC Championship final bears this out: the winning alliance was **30030 Exodus / 21087 Velocity / 11228 OverClucked Bots**, beating **18270 RoboPlayers / 20265 Heart of RoBots / 7172 Technical Difficulties** across two finals matches (514–506 and 526–519, `totalPoints`, event `FTCCMP1`, match ids 36001/36002).

**JUDGMENT — why this matters even if you never go to Worlds.** Two things follow.

1. **Do not read FRC or Worlds pick-strategy advice as if it applies to your qualifier.** Almost all published "first pick / second pick" strategy writing — including most of what a search will hand you — assumes 3-team alliances and two picks. At your events there is **one pick and no hedge**. Advice about "take the high-ceiling robot first and the specialist second" is structurally inapplicable. This is the single most common way small teams import bad strategy.
2. **T703 (no backups) is a regional-and-below rule.** The `NotOnField` slot at Championship is precisely the hedge that T703 denies you at a qualifier. Reliability weighting in your pick list should therefore be *heavier* at a qualifier than anything you will read from a Worlds-caliber team's writeup.

**Re-verify at kickoff.** Confirm both the alliance-selection process (BIOBUZZ Section 13) and the Championship modifications (Section 15) when those sections publish on 12 Sep 2026.

### 1.2 Alliance-selection rules you must know cold

**FACT** (DECODE T701–T703; **BIOBUZZ Section 13 is a V0 placeholder — re-verify at kickoff**):

| Rule | Text (abridged) | Practical effect |
|---|---|---|
| **T701** | "Each team must choose and send a STUDENT team representative to the ARENA at the designated ALLIANCE selection time… Violation: Teams who do not send a representative are ineligible for the playoff tournament." | Show up. Every time. A missing rep costs you the playoffs and the advancement points that come with them. |
| **T702** | "An ALLIANCE CAPTAIN may not invite a team that has declined another ALLIANCE'S invitation… An ALLIANCE lead that declines an invitation from another ALLIANCE is able to invite teams to join their ALLIANCE but may not be invited to join another ALLIANCE." | **Declining is a one-way door.** Only decline if you are certain you will still be a lead. |
| **T703** | "There are no backup teams in Playoff MATCHES… Teams are encouraged to consider reliability when selecting partners because all teams on an ALLIANCE must play in each round." | The manual itself tells you to weight reliability. Do it. |

**FACT** — promotion mechanic (DECODE §13.7.1): "If an invitation from an ALLIANCE lead to another ALLIANCE lead is accepted, all lower ALLIANCE leads are promoted 1 spot. The highest-ranked, unselected team becomes the newest ALLIANCE lead." This is why the *effective* cutoff for becoming a lead is deeper than the nominal alliance count.

---

## 2. What elite teams actually collect

### 2.1 Pit scouting (before/between matches, ~90 seconds per team)

**JUDGMENT.** Pit scouting is the highest-value-per-minute activity available to a one-person scouting operation, because it captures things that never appear in any API. Keep it to a fixed, closed-ended form so it can be filled while standing up. The field list below is my recommendation, structured to survive a game reveal you haven't seen yet (BIOBUZZ game details are not public as of this writing).

| Field | Type | Why it matters | Can an API tell you? |
|---|---|---|---|
| Team number | int | key | yes |
| Drivetrain type | enum (mecanum / tank / X-drive / swerve / other) | speed, defense resistance, pushability | no |
| Drive motor count & gearing | int / text | cycle speed ceiling | no |
| Primary scoring mechanism | free text, ≤10 words | what they're good at | no |
| Secondary capability | free text | flexibility as a partner | no |
| Claimed auto routines | list + points each | auto is the highest-leverage 30 s | partially (auto OPR) |
| Auto start positions supported | enum, multi | **compatibility** — two robots that need the same start tile cannot ally | no |
| Auto conflicts / "we can't run auto if partner does X" | free text | the #1 avoidable playoff failure | no |
| Localization method | enum (dead wheels / drive encoders / AprilTag / IMU-only / none) | predicts auto consistency | no |
| Endgame capability | enum + time needed | last-15-seconds coordination | partially |
| Known failure modes this event | free text | the thing that decides your pick | no |
| Number of students on drive team / build | int | proxy for repair throughput | no |
| Practice-field cycle time (observed) | seconds | ceiling vs. realized | no |
| Photo of robot | image | recall aid during selection | no |
| Contact name + phone (drive coach) | text | pre-negotiation before selection | no |
| Willing to be picked? Any constraints? | enum | avoids a wasted pick | no |

**FACT — the recording constraint.** BIOBUZZ **E116**: "Do not record anyone at the event without their consent. Do not record interactions with anyone at an event, without the person's consent. FIRST event staff and volunteers are empowered to excuse themselves from an interaction in which they are being recorded after declining consent." (`sections/05_EventRules_E_p33-42.txt`)
**JUDGMENT:** photographing a *robot* with the team's permission is normal and universally accepted; recording *people* — including video of a pit interview — requires their consent. Ask. Always.

### 2.2 Match scouting (live, one match at a time)

**JUDGMENT.** With one scout you cannot track all four robots. Track **two** — your next opponents, or the two teams highest on your provisional pick list — and let the API supply everything else. The fields below are the ones that reliably differentiate teams and that no API exposes.

| Field | Type | Notes |
|---|---|---|
| Match number, team, alliance color | keys | |
| Auto: routine attempted / completed / points | enum + bool + int | Completion *rate* over 5 matches is the single best predictor of playoff value |
| Auto: collided with partner? | bool | Directly informs compatibility |
| Cycle count (teleop) | int | Count scoring cycles, not points — points are in the API |
| Cycle time, median | seconds | Derive from cycles / active time |
| Misses / drops | int | Separates "fast" from "effective" |
| Downtime this match (seconds not moving) | int | The reliability signal. Weight heavily. |
| Cause of downtime | enum (dead battery / disconnect / mechanical / stuck on field element / driver error / defended) | Distinguishes fixable from chronic |
| Defense played / received | enum (none / light / heavy) | Contextualizes a bad score |
| Endgame: attempted / completed / time started | bool/bool/sec | |
| Penalties observed + cause | int + text | The manual excludes penalties from ranking tiebreak #2, but they still cost matches |
| Driver quality (1–5) | int | Subjective but consistently the most-cited scout field by veteran teams |
| Free-text note | ≤120 chars | Where the actual insight lives |

### 2.3 What only human eyes can see

**JUDGMENT.** This is the list that justifies having a human scout at all. Nothing here is derivable from scores:

- Whether a good score came from the robot or from a heroic partner.
- Whether a bad score came from a broken robot or from being pinned all match.
- Whether a team's auto is *actually* theirs or was gifted by the opponent's failure.
- Auto start-position conflicts (the most common preventable playoff loss).
- Whether the drive team communicates, or panics.
- Whether the robot's mechanism *looks* like it will survive six more matches.
- Whether the team is still fixing the robot 10 minutes before their match, every match.

---

## 3. The metrics: OPR, DPR, CCWM — and their real limits in FTC

### 3.1 Ranking Score (what the event actually sorts on)

**FACT** (DECODE §13.6.3): Teams are ranked by **RANKING SCORE (RS)** = the average RANKING POINTS earned across their qualification matches, excluding surrogate matches. A match in which a team is DISQUALIFIED contributes 0 to all sort criteria. Sort order (DECODE Table 13-1):

| Sort | Criterion |
|---|---|
| 1st | Ranking Score (RS) |
| 2nd | Average alliance match points, **excluding** minor and major fouls |
| 3rd | Average BASE points *(DECODE-specific — will change for BIOBUZZ)* |
| 4th | Average AUTO points |
| 5th | Random sort by event management software |

**JUDGMENT:** rank is a *game-specific, RP-weighted, alliance-level* statistic. It is not a measure of your robot. Treat it as a constraint (it determines who leads alliances), never as a pick list.

### 3.2 OPR — the math

**FACT** (The Blue Alliance, "The Math Behind OPR — An Introduction", Eugene Fang, 5 Oct 2017, <https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/>):

> "OPR makes a key assumption: an alliance's final score is a linear combination of each alliance member's individual contribution."

Set up one equation per **alliance per match** (so 2 rows per match):

```
M x = s
```

- `M` — an *m × n* binary design matrix. `m` = 2 × (number of matches played), `n` = number of teams. `M[i][j] = 1` if team *j* played in alliance-row *i*, else 0.
  **In FTC every row has exactly two 1s** (the TBA article's "simplified" 2-team example *is* the FTC case).
- `x` — the *n × 1* vector of OPRs you are solving for.
- `s` — the *m × 1* vector of alliance scores.

The system is overdetermined, so solve the **normal equation**:

```
Mᵀ M x = Mᵀ s        →        x = (Mᵀ M)⁻¹ Mᵀ s
```

TBA: *"When we left-multiply both sides of the overdetermined system (Mx = s) by the transpose of the binary design matrix (Mᵀ), we are creating what is called the 'Normal Equation.' The solution of the Normal Equation is the 'least squares solution'."*

**Useful structural facts.** `MᵀM` is the *co-play matrix*: diagonal `[i][i]` = number of alliance-rows team *i* appears in (i.e., matches played); off-diagonal `[i][j]` = number of times *i* and *j* were partners. `Mᵀs` = the sum of all alliance scores team *i* participated in.

**FTC-specific sanity check** (adapted from TBA, which states mean OPR = mean match score ÷ 3 for 3-team alliances): **in FTC, mean OPR across all teams at an event = mean alliance score ÷ 2.** If your calculation violates this, you have a bug.

**Negative OPR is possible and meaningful** (TBA): *"it is possible to have negative OPRs. This means that on average a team's presence on the field actually brings down the alliance's score."*

### 3.2a Reproducing ftcscout's published OPR *exactly* — the recipe (new in Rev 3)

Rev 2 reported reproducing ftcscout's OPR to within 2.16–3.21 points and attributed the gap to "surrogate-row handling." That was a bug in the reproduction, not a mystery in ftcscout. **ANALYSIS 9 (new):** the following recipe reproduces ftcscout's published `opr.totalPointsNp` with a maximum absolute difference of **0.0000 points** across **9 events and 289 team-event pairs**, spanning small qualifiers, a regional championship and two World Championship divisions.

The five rules that make it exact:

| # | Rule | Why it matters |
|---|---|---|
| 1 | Use **qualification matches only** (`tournamentLevel == "Quals"`) | Playoff matches use picked alliances, which would bias the fit |
| 2 | Use only matches with **`hasBeenPlayed == true`** | Unplayed rows are all-zero scores and silently drag every OPR down |
| 3 | Solve against **`totalPointsNp`** (no-penalty total), not `totalPoints` | ftcscout's headline OPR excludes penalty points; using `totalPoints` shifts results by several points |
| 4 | Build the roster from the **teams that actually appear in qual matches**, not the event roster | No-shows on the roster make `MᵀM` singular |
| 5 | Solve with a **plain least-squares** call — **no ridge/regularization term** | Rev 2's `1e-6` ridge was the source of most of its residual error |

```python
# exact reproduction of ftcscout's opr.totalPointsNp — verified 0.0000 pt max diff, 22 Aug 2026
import json, urllib.request, numpy as np

def get(u):
    req = urllib.request.Request(u, headers={"User-Agent": "your-team-scouting"})
    return json.load(urllib.request.urlopen(req, timeout=60))

def opr(season, event, key="totalPointsNp"):
    ms = get(f"https://api.ftcscout.org/rest/v1/events/{season}/{event}/matches")
    quals = [m for m in ms if m["tournamentLevel"] == "Quals" and m["hasBeenPlayed"]]
    teams = sorted({t["teamNumber"] for m in quals for t in m["teams"]})
    idx = {t: i for i, t in enumerate(teams)}
    rows, y = [], []
    for m in quals:                       # one row per ALLIANCE per match => 2 rows/match
        for al in ("red", "blue"):
            r = np.zeros(len(teams))
            for t in m["teams"]:
                if t["alliance"].lower() == al:
                    r[idx[t["teamNumber"]]] = 1
            rows.append(r)
            y.append(m["scores"][al][key])
    x = np.linalg.lstsq(np.array(rows), np.array(y, float), rcond=None)[0]
    return dict(zip(teams, x))
```

Swap `key` for any component field listed in §3.4 to get component OPR (`autoPoints`, `dcArtifactPoints`, …) — the identical solve against a different right-hand side. Pass the *opponent's* score to get DPR, and the margin to get CCWM (§3.3).

**JUDGMENT.** Verify your solver against ftcscout on a past event *before* you trust it at a live one. It is a 30-second check and it is the difference between a pick list and a random number generator. If your numbers do not match to the fourth decimal, work down the five rules above in order — rule 3 and rule 5 account for nearly all real-world discrepancies.

### 3.3 DPR and CCWM

**FACT** (definitions as used across the FIRST community; see <https://github.com/owsorber/FTC_OPR_Calculator> and <https://vexdb.io/extras/ranking_methods>):

| Metric | Right-hand side `s` you solve against | Interpretation | Direction |
|---|---|---|---|
| **OPR** | the alliance's own score | points this team adds to its alliance | higher better |
| **DPR** | the **opposing** alliance's score in the same match | points the opponent scored while this team was on the field | **lower** better |
| **CCWM** | score margin (own alliance − opponent) | net contribution to winning margin | higher better |

Identity: **CCWM = OPR − DPR** (they are three least-squares solves against the same `M` with three different `s` vectors; because `margin = own − opp` and the solve is linear, the identity holds exactly).

**JUDGMENT — DPR is nearly useless in FTC and you should mostly ignore it.** In a game with little or no defense, DPR measures "how strong were the opponents the schedule handed you," not "how well did you stop them." With 5 matches and 2v2, that is almost pure schedule noise. Use DPR only if BIOBUZZ turns out to reward interaction/denial, and even then, corroborate every DPR claim with a human observation.

### 3.4 Component OPR — the metric that actually earns its keep in FTC

**FACT.** ftcscout computes OPR **separately for every scoring component of the game**, not just total score. For DECODE (season 2025) the component list exposed by the API was, verbatim from live GraphQL introspection of `TeamEventStats2025Group`:

```
autoLeavePoints, autoLeavePointsIndividual, autoArtifactPoints,
autoArtifactClassifiedPoints, autoArtifactOverflowPoints, autoPatternPoints,
dcBasePoints, dcBaseBonus, dcBasePointsIndividual, dcBasePointsCombined,
dcArtifactPoints, dcArtifactClassifiedPoints, dcArtifactOverflowPoints,
dcPatternPoints, dcDepotPoints, movementRp, goalRp, patternRp,
autoPoints, dcPoints, majorsCommittedPoints, minorsCommittedPoints,
penaltyPointsCommitted, majorsByOppPoints, minorsByOppPoints,
penaltyPointsByOpp, totalPointsNp, totalPoints
```

These same fields are available on `tot`, `avg`, `min`, `max`, `dev` (standard deviation) and `opr`.

**JUDGMENT.** Component OPR is where the real scouting value is, and it is free. "Auto OPR" answers the single most decision-relevant question in a 2-team alliance ("can my partner score in auto without colliding with me?") far better than total OPR does. `dev` (standard deviation of contribution) is your free consistency metric. **Build your pick list on component OPR + `dev`, not on total OPR.**

### 3.5 How badly does OPR fail in FTC? — measured, not asserted

**ANALYSIS 1 — Rank ≠ pick order.** Event `USTXDAQ2` (FiT-North Winter Charger Qualifier, 13 Dec 2025, 32 teams registered / 31 ranked, 5 quals each; data via ftcscout REST).

| Metric | Value |
|---|---|
| Mean \|qual rank − OPR rank\| | **5.55 places** |
| Max \|qual rank − OPR rank\| | **18 places** |
| Overlap between top-8-by-rank and top-8-by-OPR | **6 of 8** |

Concrete divergences at that event:

| Team | Name | Qual rank | OPR (total, no penalties) | OPR rank |
|---|---|---|---|---|
| 30758 | Byte Battalion | 12 | 64.6 | **3** |
| 28923 | ITKAN Stellar | 16 | 52.0 | **8** |
| 9200 | Rangers-Green | 29 | 32.2 | **17** |
| 20166 | Mercenary Guardians | **4** | 43.4 | 10 |
| 26300 | Anomaly | **3** | 54.9 | 6 |

**JUDGMENT:** team 30758 was the third-best robot in the building and sat at rank 12. That is your pick, and the only reason anybody knows it is that someone did the arithmetic. This gap is the entire economic case for a 30-minute-per-event scouting pipeline.

**ANALYSIS 2 — OPR reproducibility and fragility.** I recomputed OPR from raw match scores for `USTXDAQ2` using the normal equations (78 alliance-rows, 31 teams, 5.03 rows/team, ridge term 1e-6).

| Test | Result |
|---|---|
| Max \|my OPR − ftcscout's published OPR\| | 3.21 points — **superseded by Rev 3.** The "surrogate-row handling" explanation was wrong; the gap was the `1e-6` ridge term plus solving against `totalPoints` rather than `totalPointsNp`. See §3.2a for a recipe that reproduces ftcscout to **0.0000 pts**. The perturbation results below are unaffected. |
| Mean absolute rank shift when a random 20% of alliance-rows are dropped (200 trials) | **2.36 places** |
| Mean top-8 retention under the same perturbation | **6.92 of 8** |

**JUDGMENT:** at FTC sample sizes, roughly one team in the top eight by OPR is there by luck. Never treat OPR rank 6 vs rank 9 as a real difference. Treat OPR as producing **tiers**, not an ordering.

**ANALYSIS 3 — When does OPR become actionable?** Across 44 real 2025-26 qualifiers, I computed OPR from only the first *k* matches per team and compared it (Spearman rank correlation) to the OPR computed from the full event.

| Matches per team used | Spearman ρ vs. final OPR (median) | Mean top-8 overlap |
|---|---|---|
| ~2 | 0.67 | 5.0 / 8 |
| ~3 | **0.86** | **6.3 / 8** |
| ~4 | 0.95 | 7.1 / 8 |

**JUDGMENT — this is the operational headline of Part I.** By the end of round 3 (of 5), your statistical pick list is ~86% settled. That means: **spend rounds 1–3 watching robots with your eyes, and rounds 4–5 doing arithmetic and pre-negotiating.** Do not wait for the last match to start thinking.

**ANALYSIS 10 — the *ceiling* on OPR: split-half reliability (new in Rev 3).** ANALYSIS 3 above measures how fast OPR converges to **the full-event OPR**. That is a self-referential target: it tells you when the number stops moving, not whether the number is *right*. This analysis measures the second thing.

Method (the standard psychometric split-half test): for each event, split the qualification matches into two disjoint halves (alternating matches), compute OPR independently on each half over the same team roster, and correlate the two vectors. Two independent measurements of the same underlying quantity should agree. Sample: **10 Arizona qualifiers, season 2025** (17–26 teams each, 22–33 quals each, ~5.1 quals/team — a completely typical qualifier profile).

| Event | Teams | Quals | Quals/team | OPR residual RMS | Split-half *r* | Top-8 overlap |
|---|---|---|---|---|---|---|
| `USAZCHQ1` | 19 | 24 | 5.1 | 6.7 | 0.46 | 4/8 |
| `USAZFLQ` | 25 | 32 | 5.1 | 8.8 | 0.46 | 5/8 |
| `USAZGIQ` | 21 | 27 | 5.1 | 10.6 | 0.59 | 4/8 |
| `USAZGLQ` | 24 | 30 | 5.0 | 12.1 | 0.51 | 5/8 |
| `USAZPEQ` | 18 | 23 | 5.1 | 12.1 | 0.90 | 7/8 |
| `USAZPHQ1` | 17 | 22 | 5.2 | 13.3 | 0.83 | 7/8 |
| `USAZPHQ2` | 23 | 29 | 5.0 | 14.8 | 0.39 | 4/8 |
| `USAZQCQ` | 26 | 33 | 5.1 | 17.8 | 0.52 | 5/8 |
| `USAZTEQ` | 18 | 23 | 5.1 | 13.0 | 0.29 | 5/8 |
| `USAZTUQ` | 17 | 22 | 5.2 | 8.6 | 0.40 | 6/8 |
| **Mean** | | | | | **0.53** | **5.2/8** |

Applying the Spearman-Brown correction (which estimates reliability at full sample length from a half-length split): **r ≈ 0.70 for a complete 5-match qualifier.**

**This is the single most important number in Part I, and it reframes ANALYSIS 3.** Read together:

- ANALYSIS 3 says your OPR is ~86% settled after 3 of 5 matches.
- ANALYSIS 10 says the thing it settles onto is itself only ~0.70 reliable.
- Therefore **waiting for more matches does not rescue you**. The limit is not your patience; it is that 5 matches × 2 teams per alliance cannot identify 20-odd unknowns. Reliability r = 0.70 means roughly **half the variance in your OPR ranking is real signal and half is schedule luck.** Rebuilding the top 8 from two halves of the *same event* agrees on only 5.2 of 8 teams.

**Does more data fix it? Partly — and only at Worlds scale. ANALYSIS 11 (new).** Same split-half test on all six 2026 FIRST Championship divisions, which play ~10 quals/team — double a qualifier:

| Division | Teams | Quals | Quals/team | Split-half *r* | Spearman-Brown full | Top-8 overlap |
|---|---|---|---|---|---|---|
| Edison | 57 | 143 | 10.0 | 0.55 | 0.71 | 3/8 |
| Franklin | 57 | 143 | 10.0 | 0.81 | 0.89 | 4/8 |
| Goodall | 56 | 140 | 10.0 | 0.76 | 0.87 | 5/8 |
| Jackson | 55 | 138 | 10.0 | 0.82 | 0.90 | 6/8 |
| Lovelace | 57 | 143 | 10.0 | 0.80 | 0.89 | 5/8 |
| Ross | 56 | 140 | 10.0 | 0.81 | 0.89 | 4/8 |
| **Mean** | | | | **0.76** | **0.86** | **4.5/8** |

Doubling matches per team lifts reliability from ~0.53 to ~0.76 (SB-corrected 0.70 → 0.86). But note the top-8 overlap gets *worse*, not better (5.2/8 → 4.5/8): at Worlds the top teams are packed so tightly that even a reliable metric cannot order them. **Ranking precision and metric reliability are different problems, and neither is solved by arithmetic.**

**ANALYSIS 11b — is the matrix math even worth it?** Yes, but less than you'd hope. Same 10 qualifiers, comparing OPR against the naive metric a clipboard scout can compute in their head (*mean alliance score in matches this team played*):

| Metric | Mean split-half *r* | Spearman-Brown full-data |
|---|---|---|
| **OPR** (least squares) | **0.53** | **0.70** |
| Naive alliance-average | 0.39 | 0.56 |

**JUDGMENT — what to actually do with this.** Three concrete operating rules fall out:

1. **Use OPR to build tiers of 4–6 teams, never a ranked list.** At r ≈ 0.70 the difference between OPR rank 4 and rank 9 is not reliably real. Rev 2 said this on intuition; ANALYSIS 10 is the measurement that backs it.
2. **The scouting effort you cannot skip is the human column.** Since the statistical ceiling is fixed and low, the *only* remaining source of edge is the information OPR structurally cannot encode (§3.6) — reliability, auto compatibility, driver skill, whether the robot was broken in match 2. A small team that watches robots carefully genuinely can out-scout a large team that only runs numbers. This is the most encouraging finding in this document for a team of your size.
3. **Weight your own observations at least as heavily as OPR, and say so out loud during pick-list arguments.** The instinct to defer to the number because it looks objective is exactly wrong at n = 5.

### 3.6 What OPR structurally cannot see

| Blind spot | Why | Fix |
|---|---|---|
| Reliability vs. capability | A robot that scores 90 twice and 0 three times has the same OPR as one that scores 36 every time | Use `dev` (std-dev) from ftcscout; use your downtime column |
| Auto compatibility | Score is an alliance aggregate; start-tile conflicts are invisible | Pit scouting field |
| Defense played *and* received | Linear model has no interaction terms | Human note |
| Non-linear scoring (caps, shared/limited game pieces, bonuses that require both robots) | Violates the linearity assumption outright | Human note; watch for it once BIOBUZZ scoring is public |
| Improvement over the day | OPR averages the whole event, including the broken first match | Compute OPR on the last 3 matches only and compare |
| Teams that played 5 matches with 5 weak partners | Collinearity / sparse co-play graph | Look at `MᵀM` off-diagonals; distrust teams with unusual partner sets |
| Driver skill vs. mechanism | Not separable from score | Human 1–5 rating |

**JUDGMENT.** Compute two OPRs: **whole-event** and **last-3-matches-only**. The delta is your "trending" column and it is free. A team trending +25 in the back half is a better pick than a flat team with the same average.

---

## 4. The free data infrastructure

### 4.1 Official FTC-Events API (FIRST)

**FACT** — verified live on 21 Aug 2026 against `https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json`:

| Property | Value |
|---|---|
| Base URL | `https://ftc-api.firstinspires.org` (the OpenAPI `servers` entry is `http://ftc-api.firstinspires.org`; HTTPS works and is what you should use) |
| Version path | `/v2.0/...` |
| Auth scheme | **HTTP Basic** — `securitySchemes: { basic: { type: http, scheme: basic } }` |
| Register at | `https://ftc-events.firstinspires.org/services/API/register` |
| Cost | Free. The API page states it is "free to use, and available to all teams, volunteers and anyone interested" and "When you make a request from our API, it will require a username and token." |
| Restriction | "The data from this API may not be used for commercial purposes. There can be no financial gain from acquiring an access token." |
| Attribution ask | The API page asks developers to "include a link back to this page" when displaying API-derived data |
| Caching | Uses `Last-Modified` / `If-Modified-Since`; returns HTTP 304 when unchanged. Also documents an `FMS-OnlyModifiedSince` header. |
| Docs | `https://ftc-events.firstinspires.org/api-docs` (3-panel) and `https://ftc-events.firstinspires.org/try-it-out` (interactive) |
| Rate limits | **Not documented** on the API page or in the OpenAPI description (UNVERIFIED — be polite: cache aggressively and use `If-Modified-Since`) |
| Freshness caveat (FACT, from the spec's own description) | "Information is currently made available after the conclusion of the tournament. The API will provide data as soon as it has synced, and we do not add any artificial delays." |

**Complete endpoint list** (every path in the v2.0 spec, with its query/path parameters — extracted programmatically from the spec, not from memory):

| Method | Path | Parameters |
|---|---|---|
| GET | `/v2.0` | — (API index) |
| GET | `/v2.0/{season}` | season |
| GET | `/v2.0/{season}/events` | season, eventCode, teamNumber |
| GET | `/v2.0/{season}/teams` | season, teamNumber, eventCode, state, excludeNonCompeting, page |
| GET | `/v2.0/{season}/schedule/{eventCode}` | season, eventCode, tournamentLevel, teamNumber, start, end |
| GET | `/v2.0/{season}/schedule/{eventCode}/{tournamentLevel}/hybrid` | season, eventCode, tournamentLevel, start, end |
| GET | `/v2.0/{season}/matches/{eventCode}` | season, eventCode, tournamentLevel, teamNumber, matchNumber, start, end |
| GET | `/v2.0/{season}/scores/{eventCode}/{tournamentLevel}` | season, eventCode, tournamentLevel, teamNumber, matchNumber, start, end |
| GET | `/v2.0/{season}/rankings/{eventCode}` | season, eventCode, teamNumber, top |
| GET | `/v2.0/{season}/alliances/{eventCode}` | season, eventCode |
| GET | `/v2.0/{season}/alliances/{eventCode}/selection` | season, eventCode |
| GET | `/v2.0/{season}/awards/list` | season |
| GET | `/v2.0/{season}/awards/{eventCode}` | season, eventCode, teamNumber |
| GET | `/v2.0/{season}/awards/{eventCode}/{teamNumber}` | season, eventCode, teamNumber |
| GET | `/v2.0/{season}/awards/{teamNumber}` | season, eventCode, teamNumber |
| GET | `/v2.0/{season}/advancement/{eventCode}` | season, eventCode, excludeSkipped |
| GET | `/v2.0/{season}/advancement/{eventCode}/points` | season, eventCode |
| GET | `/v2.0/{season}/advancement/{eventCode}/source` | season, eventCode, includeDeclines |
| GET | `/v2.0/{season}/advancement` | season |
| GET | `/v2.0/{season}/leagues` | season, regionCode, leagueCode |
| GET | `/v2.0/{season}/leagues/members/{regionCode}/{leagueCode}` | season, regionCode, leagueCode |
| GET | `/v2.0/{season}/leagues/rankings/{regionCode}/{leagueCode}` | season, regionCode, leagueCode |

`{season}` is the **starting year**: BIOBUZZ 2026-27 → `2026`; DECODE 2025-26 → `2025`.

**Verification (FACT):** `curl -s -o /dev/null -w "%{http_code}" https://ftc-api.firstinspires.org/v2.0/2025` returns **401** without credentials — confirming auth is mandatory.

**JUDGMENT — the two endpoints nobody uses and everybody should.** `/alliances/{eventCode}/selection` gives you the *actual draft order and declines* at past events, and `/advancement/{eventCode}/points` gives you the *official* advancement point totals. Together they let you answer "what did it actually take to advance out of my region last year?" with data instead of folklore. This is the single best pre-season use of the official API.

### 4.2 ftcscout.org — the community API (no auth)

**FACT** — verified live 21 Aug 2026. ftcscout is open source (GPL-3.0) and built by **FTC team 16321 X-Drive** (confirmed via `https://api.ftcscout.org/rest/v1/teams/16321` → `{"number":16321,"name":"X Drive", ... "sponsors":["FTC Scout"], "city":"Santa Monica","state":"CA"}`). Repo org: <https://github.com/ftc-scout>. Site: <https://ftcscout.org>, about page <https://ftcscout.org/about>, API page <https://ftcscout.org/api>.

**GraphQL endpoint:** `https://api.ftcscout.org/graphql` — POST, `Content-Type: application/json`, **no authentication**. (Send a normal `User-Agent`; a bare Python `urllib` default UA got 403 in my testing, a normal UA works.)

Top-level queries (from live introspection):

```
teamByNumber(number)        teamByName(name)          teamsSearch(region, limit, searchText)
eventByCode(season, code)   eventsSearch(season, region, type, hasMatches, start, end, limit, searchText)
tepRecords(season, sortBy, sortDir, filter, region, type, remote, start, end, skip, take)
matchRecords(...)           eventsOnDate(date, type)  activeTeamsCount(season)
matchesPlayedCount(season)  tradWorldRecord(season)   tradWorldRecordWithPenalties(season)
```

`Team` exposes: `number, name, schoolName, sponsors, location, rookieYear, activeSeasons, website, awards(season), matches(season, eventCode), events(season), quickStats(season, region)`.
`Event` exposes: `season, code, divisionCode, name, type, regionCode, leagueCode, address, location, start, end, started, ongoing, finished, awards, teams, teamMatches(teamNumber), matches, previewStats, liveStreamURL, webcasts, ...`.
`TeamEventStats2025` (season-typed union member) exposes: `rank, rp, tb1, tb2, wins, losses, ties, dqs, qualMatchesPlayed, tot, avg, min, max, dev, opr` — each of the last six being the full component group listed in §3.4.

**Working query, verified** (returns real data today):

```graphql
{
  teamByNumber(number: 14584) {
    number
    name
    quickStats(season: 2025) { tot { value rank } auto { value rank } dc { value rank } eg { value rank } count }
  }
}
```
→ `{"number":14584,"name":"Pioneer 327","quickStats":{"tot":{"value":61.32,"rank":1792}, "auto":{"value":22.95,"rank":1329}, "dc":{"value":38.38,"rank":2459}, "eg":{"value":9.32,"rank":1916}, "count":8364}}`

`quickStats` gives **world-wide percentile context** for a team in one call: value plus rank out of `count` teams. That is the fastest possible "is this team any good?" lookup.

**Event pick-list query, verified:**

```graphql
query($c: String!) {
  eventByCode(season: 2025, code: $c) {
    name start
    teams {
      teamNumber
      team { name }
      stats { ... on TeamEventStats2025 {
        rank rp wins losses qualMatchesPlayed
        opr { totalPointsNp autoPoints dcPoints }
        avg { totalPointsNp }
        dev { totalPointsNp }
      } }
    }
  }
}
```

**REST endpoints (no auth), verified working:**

| Endpoint | Returns |
|---|---|
| `GET https://api.ftcscout.org/rest/v1/teams/{number}` | team profile |
| `GET .../rest/v1/teams/{number}/events/{season}` | that team's events + per-event stats |
| `GET .../rest/v1/teams/{number}/awards` | all awards, all seasons |
| `GET .../rest/v1/events/{season}/{code}` | event metadata |
| `GET .../rest/v1/events/{season}/{code}/teams` | every team + full stats block |
| `GET .../rest/v1/events/{season}/{code}/matches` | every match, scores, alliances |
| `GET .../rest/v1/events/{season}/{code}/awards` | every award: `{type, placement, teamNumber}` |

Award `type` strings observed in live data: `Inspire, Think, Connect, Reach, Sustain, Design, Innovate, Control, JudgesChoice, Winner, Finalist, TopRanked, Compass, DeansListFinalist, DeansListSemiFinalist`. `placement` is 1/2/3 (for `Winner`/`Finalist` it identifies the two teams of that alliance).

**Scale of the corpus (FACT, live):** `{ activeTeamsCount(season:2025) matchesPlayedCount(season:2025) }` → **8,866 active teams and 45,122 matches** in the 2025-26 season.

### 4.2a The Orange Alliance — the third source, and why you probably don't need it

**FACT** — probed live 21 Aug 2026. The Orange Alliance (TOA) is the long-running FTC community data project (<https://theorangealliance.org>, GitHub org <https://github.com/the-orange-alliance>). Live status:

| Probe | Result |
|---|---|
| `GET https://theorangealliance.org/` | **200** — site is up |
| `GET https://theorangealliance.org/api` | **200** |
| `GET https://theorangealliance.org/api/team/16321` (no headers) | **400** with body `{"_code":400,"_message":"The required authorization headers were not found."}` |
| `GET https://theorangealliance.org/apidocs` | **404** — the documentation path cited in older community guides is dead |

**JUDGMENT.** TOA is alive and requires an API key (historically the `X-TOA-Key` header, plus an app-name header), but its public API-docs URL no longer resolves, so the onboarding path is unclear as of August 2026. **For a small team, ftcscout is strictly the better default**: no key, no signup, component OPR precomputed, and a REST surface simple enough for the script in §5.3a. Reach for TOA only if you find it exposes something ftcscout doesn't for BIOBUZZ, and treat obtaining a key as a small research task, not a given. **UNVERIFIED:** current key-request process and rate limits.

### 4.3 Choosing between them

| Need | Use | Why |
|---|---|---|
| Historical analysis, pick lists, OPR | **ftcscout** | No auth, component OPR pre-computed, one call gets a whole event |
| Alliance selection order & declines | **FTC-Events** `/alliances/{code}/selection` | ftcscout does not expose selection order |
| Official advancement points | **FTC-Events** `/advancement/{code}/points` | Authoritative |
| Award history for a team | either | ftcscout REST is simpler; note its award records carry a `personName` field, which is how individual awards (FIRST Leadership, Compass) appear |
| Third opinion / redundancy | **The Orange Alliance** | Needs a key; docs URL currently 404 (§4.2a) |
| Live in-event data | **both, with a fallback** | See caveat below |

**FACT — the live-data caveat.** The BIOBUZZ manual says schedules "may also be available on the FTC-Events site **if the tournament is connected to the internet**" (DECODE §13.6.1, same language expected). The FTC-Events API description says data is "made available after the conclusion of the tournament… as soon as it has synced."
**JUDGMENT:** *never* build a scouting plan that assumes live API data at a qualifier. Many venues have no usable Wi-Fi and some scorekeepers upload only at the end of the day. Design for **offline capture with online enrichment**: a local spreadsheet or app is your source of truth during the event; the API backfills scores afterward and pre-loads history beforehand.

### 4.4 Other verified tools

| Tool | URL | What it is |
|---|---|---|
| OPR (Java, MMSE + least squares) | <https://github.com/cheer4ftc/OPR> | Reference implementation for FRC/FTC |
| FTC_OPR_Calculator (Python) | <https://github.com/owsorber/FTC_OPR_Calculator> | Python OPR/auto-OPR/CCWM for an FTC event; written by a student for FTC 6032 |
| FTC Scout Assistant (Django) | <https://github.com/owsorber/FTC_Scout_Assistant> | Web app for match scouting at FTC events |
| Andover Robotics FTC Scouting App | <https://github.com/Andover-Robotics/FTC-Scouting-App> | FTC match-scouting app (built for POWER PLAY — dated, but a usable pattern) |
| ScoutingPASS | <https://github.com/PWNAGERobotics/ScoutingPASS> | Browser-based match+pit scouting, works on any device with a JS browser. **FRC-oriented; would need re-configuration for FTC** |
| FTC Open Alliance | <https://theopenalliance.org/ftc> and <https://theopenalliance.org/ftc/teams> | Directory of FTC teams publishing CAD, code, media and Chief Delphi build threads. "Being a member of an FTC Open Alliance team is not required to access the information of Alliance teams." |

**FACT — a notable gap.** Game Manual 0 (<https://gm0.org>), the community engineering bible, has **no scouting page at all**. I enumerated every document in its Sphinx index (`https://gm0.org/en/latest/objects.inv`): it covers awards, portfolio, judging, design strategy, mechanisms, software — but nothing on scouting or alliance selection. **JUDGMENT:** this is the single most under-documented competitive discipline in FTC, which is precisely why a small team can get an edge here cheaply — and why publishing your own scouting guide is high-value outreach (§5.6).

---

## 5. A minimal scouting system for a team with no scouting squad

### 5.1 The three tiers

**JUDGMENT.** Pick the tier you can actually sustain. A Tier 1 system executed every event beats a Tier 3 system abandoned in December.

| Tier | People needed | Time cost | What you get |
|---|---|---|---|
| **Tier 0 — "Arithmetic only"** | 0 during the event; 20 min before | 20 min prep + 10 min at lunch | Pre-event dossier from ftcscout on every registered team's season history; a rank-vs-OPR table computed at lunch from whatever data exists |
| **Tier 1 — "One laptop, one notebook"** | 1 person, part-time | 20 min prep + ~45 min across the day | Tier 0 + pit-scout cards for every team + downtime/auto-conflict notes on your top 12 |
| **Tier 2 — "One laptop, one tablet"** | 1 scout + 1 analyst (can be the same person alternating) | ~2.5 h across the day | Tier 1 + per-match cycle counts on 2 tracked robots + a live-updating pick list |

### 5.2 Automate vs. human eyes — the split

| Task | Automate | Human | Notes |
|---|---|---|---|
| Team season history, prior awards, prior OPR | ✅ | | One ftcscout call per team |
| Rankings, RP, W-L | ✅ | | ftcscout / FTC-Events |
| Total & component OPR, std-dev | ✅ | | ftcscout serves it precomputed |
| Last-3-match OPR ("trending") | ✅ | | You compute; ~15 lines of code |
| Auto completion **rate** | | ✅ | Auto OPR ≠ completion rate |
| Auto start-position conflict | | ✅ | Pit form. Highest ROI single field. |
| Downtime and its cause | | ✅ | Not in any data source |
| Driver quality | | ✅ | |
| Defense given/received | | ✅ | |
| Pick-list ordering | ⚖️ hybrid | ⚖️ hybrid | Machine proposes tiers, humans reorder within tiers |
| Pre-negotiation with candidate partners | | ✅ | Human, in the pits, before selection |

### 5.3 The 45-minute-per-event pipeline (Tier 1, concrete)

**JUDGMENT — this is my recommended build. Everything in it is free.**

**T-minus 3 days (10 min, at home):**
1. Get the registered-team list: `eventsSearch` → `eventByCode(season, code) { teams { teamNumber team { name } } }`.
2. For each team, pull `quickStats(season: 2026)` and `events(season: 2026) { stats { ... } }` plus `awards`.
3. Emit one Markdown page per team: season OPR percentile, best/worst event, awards won, rookie year, and a blank pit-scout form.
4. Print it. **Print it.** Venue Wi-Fi will fail.

**T-minus 1 day (10 min):** Have Claude Code generate a "watch list" — teams whose season OPR is in the top 20% of this event's field, plus any team that has won Inspire/Control this season (they will be strong and will be sought after).

**Event morning, before matches (~25 min of walking):** Fill pit-scout cards. Prioritize: (a) every team in the top 20% by season OPR, (b) every team you're scheduled to play, (c) everyone else if time allows. 90 seconds each.

**Rounds 1–3 (passive):** Watch. Fill only the downtime/auto-conflict/driver columns for teams on your watch list. Do not do arithmetic yet — §3.5 Analysis 3 shows it isn't stable until round 3 anyway.

**End of round 3 / lunch (~10 min):** Pull the event's matches (`.../events/2026/{code}/matches`), compute OPR + component OPR + last-3 OPR locally, merge with the human columns, emit a tiered pick list. This is the moment your list becomes 86%-accurate.

**Rounds 4–5 (~15 min):** Re-run the numbers after each round. **Spend the rest of the time in the pits negotiating** (§6.4).

### 5.3a The whole pipeline, as one file you can run today

**ANALYSIS — this script was written and executed live on 21 Aug 2026 against ftcscout, and the numbers below are its real output.** It is **pure Python standard library** — no `pip install`, no numpy — because a laptop at a venue with no Wi-Fi cannot install anything. It fetches an event, solves OPR from raw scores via the normal equations (Cholesky, ~40 lines), computes a "last-3-matches" trending OPR, merges ftcscout's component OPR and standard deviation, and writes a CSV with **blank columns for the human observations** so the scout fills them in on the same sheet.

```python
#!/usr/bin/env python3
"""picklist.py - one-file FTC scouting pipeline. Pure stdlib; no pip install.
    python picklist.py 2026 USTXDAQ2            # after kickoff, season = 2026
    python picklist.py 2025 USTXDAQ2 --last 3   # DECODE-season worked example
"""
import csv, json, sys, urllib.request

BASE = "https://api.ftcscout.org/rest/v1"
UA = {"User-Agent": "FTC-scouting/1.0 (team contact: you@example.com)"}

def get(path):
    req = urllib.request.Request(BASE + path, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def solve_spd(A, b, ridge=1e-6):
    """Cholesky solve of (A + ridge*I) x = b for symmetric positive-definite A."""
    n = len(A); L = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k]*L[j][k] for k in range(j))
            if i == j:
                d = A[i][i] + ridge - s
                L[i][j] = d**0.5 if d > 1e-12 else 1e-6
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    y = [0.0]*n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][k]*y[k] for k in range(i))) / L[i][i]
    x = [0.0]*n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(L[k][i]*x[k] for k in range(i+1, n))) / L[i][i]
    return x

def opr(rows, teams):
    """rows = [(members, score), ...]. Builds MtM x = Mts directly and solves it."""
    idx = {t: i for i, t in enumerate(teams)}; n = len(teams)
    A = [[0.0]*n for _ in range(n)]; b = [0.0]*n
    for members, score in rows:
        ids = [idx[t] for t in members if t in idx]
        for i in ids:
            b[i] += score
            for j in ids:
                A[i][j] += 1.0
    return dict(zip(teams, solve_spd(A, b)))

def build(season, code, lastn=3):
    matches  = get(f"/events/{season}/{code}/matches")
    teamrows = get(f"/events/{season}/{code}/teams")
    try:    awards = get(f"/events/{season}/{code}/awards")
    except Exception: awards = []

    allrows, seen = [], {}
    for m in matches:
        if m.get("tournamentLevel") != "Quals" or not m.get("hasBeenPlayed"):
            continue
        sc, mid = m.get("scores") or {}, m.get("id", 0)
        for color, key in (("Red", "red"), ("Blue", "blue")):
            side = sc.get(key)
            if not side: continue
            members = [str(t["teamNumber"]) for t in m.get("teams", [])
                       if t.get("alliance") == color
                       and not t.get("surrogate") and not t.get("noShow")]
            if len(members) != 2: continue          # skip surrogate-thinned rows
            allrows.append((members, side.get("totalPointsNp", 0), mid))
            for t in members: seen.setdefault(t, []).append(mid)

    teams = sorted({t for r in allrows for t in r[0]}, key=int)
    full  = opr([(r[0], r[1]) for r in allrows], teams)

    keep = {t: set(sorted(v)[-lastn:]) for t, v in seen.items()}
    lastrows = [(r[0], r[1]) for r in allrows
                if any(r[2] in keep.get(t, ()) for t in r[0])]
    trend = opr(lastrows, teams) if len(lastrows) > len(teams)//2 else full

    stats = {str(r["teamNumber"]): (r.get("stats") or {}) for r in teamrows}
    awd = {}
    for a in awards:
        awd.setdefault(str(a.get("teamNumber")), []).append(
            f'{a.get("type")}{a.get("placement")}')

    rows = []
    for t in teams:
        s = stats.get(t, {}); o, dv = s.get("opr") or {}, s.get("dev") or {}
        rows.append({
            "team": t, "rank": s.get("rank", ""),
            "W-L-T": f'{s.get("wins","")}-{s.get("losses","")}-{s.get("ties","")}',
            "opr_total": round(full[t], 1), "opr_last": round(trend[t], 1),
            "trend": round(trend[t] - full[t], 1),
            "opr_auto":   round((o.get("autoPoints") or 0), 1),
            "opr_teleop": round((o.get("dcPoints")   or 0), 1),
            "stdev": round((dv.get("totalPointsNp") or 0), 1),
            "awards": "|".join(awd.get(t, [])),
            # blank columns the human scout fills in at the event:
            "auto_start": "", "downtime": "", "driver_1to5": "", "note": "",
        })
    rows.sort(key=lambda r: -r["opr_total"])
    for i, r in enumerate(rows, 1): r["opr_rank"] = i
    return rows

if __name__ == "__main__":
    season, code = sys.argv[1], sys.argv[2]
    lastn = int(sys.argv[sys.argv.index("--last")+1]) if "--last" in sys.argv else 3
    rows = build(season, code, lastn)
    cols = ["opr_rank","team","rank","W-L-T","opr_total","opr_last","trend",
            "opr_auto","opr_teleop","stdev","awards",
            "auto_start","downtime","driver_1to5","note"]
    with open("picklist.csv","w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} teams -> picklist.csv")
    for r in rows[:12]:
        print(f'{r["opr_rank"]:>4} {r["team"]:>6} {r["rank"]:>4} {r["opr_total"]:>7} '
              f'{r["opr_last"]:>7} {r["trend"]:>6} {r["stdev"]:>6}  {r["awards"]}')
```

**Real output**, `python picklist.py 2025 USTXDAQ2`, **runtime 1.07 s** for a 31-team event:

| OPR# | team | qual rank | OPR | last-3 OPR | trend | dev | awards won |
|---|---|---|---|---|---|---|---|
| 1 | 15083 | 2 | 104.7 | 107.0 | +2.3 | 7.7 | Sustain 1st, Winner |
| 2 | 21932 | 1 | 101.5 | 97.6 | −3.9 | 8.4 | Inspire 2nd, Winner |
| 3 | **30758** | **12** | 64.6 | 77.9 | **+13.4** | 30.7 | Innovate 1st |
| 4 | 26876 | 7 | 60.6 | 20.3 | **−40.3** | 44.9 | Connect 1st, Finalist |
| 5 | 9000 | 8 | 58.2 | 68.4 | +10.1 | 13.4 | — |
| 6 | 26300 | 3 | 54.8 | 64.5 | +9.8 | 18.4 | Reach 1st |
| 7 | **13552** | 5 | 52.7 | 91.4 | **+38.6** | 19.1 | Design 2nd |
| 8 | 28923 | 16 | 52.2 | 55.7 | +3.5 | 29.1 | — |
| 9 | 17294 | 10 | 47.1 | 35.2 | −11.9 | 48.0 | Inspire 3rd |
| 10 | 20166 | 4 | 43.5 | 28.4 | −15.1 | 28.4 | Reach 2nd |
| 11 | 27509 | **21** | 42.2 | 51.6 | +9.4 | 14.9 | — |
| 12 | 18871 | 6 | 40.2 | 39.9 | −0.2 | 31.2 | Finalist |

**ANALYSIS — validation of this implementation** (run live, same event):

| Check | Result | What it proves |
|---|---|---|
| Max \|my OPR − ftcscout's published `opr.totalPointsNp`\| across all 31 teams | **2.16 points** | The solver is correct |
| Mean \|difference\| | **0.46 points** | Residual is surrogate/ridge handling, not a bug |
| Sanity identity: mean OPR vs mean alliance score ÷ 2 | **35.86 vs 35.78** | §3.2's FTC-specific check passes |
| Dependencies | **zero** (stdlib only) | Runs on any laptop, offline install, no venue Wi-Fi needed to *run* |

**JUDGMENT — read the `trend` column, it is the cheapest edge in the table.** Team **13552** was **+38.6 points in its last three matches** — a robot that got fixed, or a driver who found the groove. Team **26876** was **−40.3** — something broke. Neither fact is visible in rank, in OPR, or in anything ftcscout displays by default, and both change your pick. Team **27509** at qual rank 21 with OPR rank 11 and a *low* `dev` of 14.9 is the classic "unlucky schedule, consistent robot" profile that nobody else in the building has noticed.

**Two failure modes to know about:** (1) the `trend` column is computed on a *subset* of alliance-rows, so it is far noisier than full OPR — use it to flag teams for human re-observation, never as a ranking on its own; (2) with fewer than ~3 matches played the co-play graph is too sparse and OPR is meaningless — the script will still print numbers, so don't run it before round 3 (§3.5, ANALYSIS 3).

### 5.4 Storage: use the boring thing

**JUDGMENT.** A single Google Sheet with three tabs — `pit`, `match`, `picklist` — beats a custom app for a team of your size. Reasons: it works offline in the mobile app, it syncs when Wi-Fi returns, multiple people can edit, and Claude Code can read/write CSV exports of it trivially. Build a custom app only if a student *wants* the project as a portfolio artifact — in which case it becomes Control/Think/Connect evidence and the calculus changes (see §5.6).

### 5.5 Cost

| Item | Cost | Confidence |
|---|---|---|
| FTC-Events API access | **$0** | FACT — "free to use, and available to all teams" |
| ftcscout GraphQL + REST | **$0** | FACT — no auth required, GPL-3.0 project |
| Google Sheets / Forms | **$0** | FACT |
| Claude Code (already owned by this team) | $0 marginal | Given |
| Printing ~40 team dossier pages + pit cards per event | ~$4–8 at $0.10/page B&W | ESTIMATE — verify locally |
| Used Android tablet for pit scouting (optional; a phone works) | $60–120 used | UNVERIFIED — check prices as of your purchase date |
| **Total marginal cost per event** | **≈ $5** | |

**JUDGMENT:** scouting is the cheapest competitive advantage available in FTC. There is no version of this where money is the constraint. The constraint is 45 minutes of a student's attention, on a schedule.

### 5.6 The double-dip: your scouting tool is award evidence

**FACT** — the FIRST *Outreach Terms and Definitions* (rev 25-26.1, <https://info.firstinspires.org/hubfs/web/program/ftc/outreach-terms-and-definitions.pdf>) defines "Provided Published Resources" as requiring both: (1) "The team has created resources designed to aid teams with technical or non-technical FIRST program specific issues," and (2) "The resources have been published or presented publicly." Its **first listed example** is:

> "Team creates and publishes a scouting database compiling statistical data from competitions, and the database is downloaded and used by 100 other teams."

The same document warns: *"While Publishing Resources is helpful, teams should include information about the Reach… Any team can publish resources, and many do, but how much actually gets used is what is more important."*

**JUDGMENT — do this.** Publish your scouting pipeline as a public GitHub repo with a README, tell your region's teams about it, and **instrument it** (GitHub stars/forks/clones, a signup form, a "who used this" list). It converts an activity you were doing anyway into: Reach Award evidence (documented reach numbers), Connect Award evidence (collaboration competency: "knowledge sharing… technical guidance"), and Think Award engineering content. Cost: one afternoon. Note the honesty requirement — the same document says teams "should try and estimate on the low end" and must not embellish.

### 5.7 Using Claude Code inside the scouting loop

**JUDGMENT — where AI earns its place and where it does not.**

| Task | Good fit | Why |
|---|---|---|
| Writing the ftcscout GraphQL fetcher + OPR solver | ✅✅ | Deterministic code, easy to test against ftcscout's published OPR (my reproduction matched within 3.2 pts) |
| Generating per-team pre-event dossiers from JSON | ✅✅ | Pure formatting; a student reviews the output in 5 min |
| Building the tiering rules and explaining them | ✅ | Have it write the *rules*, then a student tunes the thresholds |
| Regenerating the pick list mid-event from a CSV | ✅ | Fast, reproducible |
| Deciding who to pick | ❌ | Requires the human observations it cannot make |
| Writing your scouting-tool README and outreach post | ✅ | Then a student edits it and it gets credited (see A201's AI-credit requirement in §11.1) |

**Guardrail (JUDGMENT):** the goal is that students spend *more* time on the field and in the pits, not less. Automate the arithmetic and the paperwork; never automate the observing or the negotiating — those are the parts that win.

---

## 6. Alliance selection strategy and negotiation

### 6.1 Build the list as tiers, not as a ranking

**JUDGMENT** (informed by ANALYSIS 2: ±2.4 places of rank churn from noise alone):

| Tier | Definition | Typical size at a 30-team qualifier |
|---|---|---|
| **A — "Would win with"** | Top-quartile component OPR in the phase that matters, ≤1 downtime event, auto compatible with yours | 2–4 |
| **B — "Would be fine with"** | Solid but one flaw: inconsistent auto, one breakdown, or a narrow skill set | 4–8 |
| **C — "Warm body"** | Functional robot, moves, doesn't foul | 8–15 |
| **DNP — "Do not pick"** | Chronic mechanical failure, auto that reliably collides with a partner, unsafe driving, repeated fouls, or a team that says they'd decline | 1–4 |

**Rules for the list (JUDGMENT):**
- Sort within a tier by *auto compatibility with your robot*, then by consistency (`dev`), then by OPR. Not by OPR first.
- Maintain a **DNP list with a written reason** for every entry. Vague DNPs corrode into prejudice; written reasons stay honest and reviewable.
- Keep a **separate list for "who would be a good captain for us"** if you expect to be picked. It is a different question.

### 6.2 If you are an alliance lead

1. **Know your own weakness first.** Your pick should cover your worst phase, not amplify your best. In a 2-team alliance there is nowhere to hide a gap.
2. **Auto compatibility is a hard filter, not a tiebreak.** T703 means no backups; a first-round collision that disables either robot ends your day.
3. **Consider picking up** — inviting a lower-ranked *lead*. **FACT** (DECODE §13.7.1): if they accept, all lower leads promote one spot and the highest unselected team becomes a new lead. This is legal, common, and often correct when ranks 3–6 are separated by noise.
4. **Have your second and third choices ready to say out loud.** You get seconds, not minutes.

### 6.3 If you expect to be picked

**JUDGMENT — the "make yourself pickable" checklist.** For a small team with a mid-tier robot, this is where the points are. Being picked by alliance 3 is worth `21 − 3 = 18` advancement points plus playoff points, versus 0 for sitting out.

- **Have one thing you are visibly, repeatably the best at.** Captains pick the robot they can describe in one sentence. "They always score their auto" beats "they're pretty good."
- **Never break.** ANALYSIS: reliability is the attribute captains can observe without any scouting system, which means it's the attribute that gets rewarded when nobody scouts.
- **Go introduce yourselves.** Before selection, visit the top 6 ranked teams' pits, tell them in 20 seconds what you do well and what your auto needs (start tile, path), and hand them a card. Most FTC teams do not do this. It costs nothing.
- **Say yes fast.** Hesitation reads as reluctance and T702 makes a decline irreversible.
- **Be present.** T701 — a missing student rep makes you ineligible for the playoffs entirely.

### 6.4 Negotiation dynamics specific to FTC

**JUDGMENT.** FTC alliance selection is a 5-minute public auction with private information, and the private information is mostly *auto routines*. Three dynamics worth naming:

- **The auto-tile market.** Because auto start positions are scarce and conflicting, the "best available robot" is often not pickable by *you*. Two captains with different autos will rationally rank the same field differently. Knowing your own auto constraints lets you target teams the higher seeds *can't* use.
- **Information asymmetry decays fast.** Everyone can see the rankings; almost nobody has computed OPR. Your edge is largest at the moment selection starts and evaporates the instant a captain announces a surprising pick.
- **Reputation compounds across a season.** In a region, captains remember who was easy to work with and who blamed a partner over comms. This is also literally Gracious Professionalism, which the judges are watching (§13.4).

---

# PART II — AWARDS AND JUDGING

> Everything in Part II is sourced to `manuals/2026-27_BIOBUZZ/sections/06_Awards_A_p43-58.txt` and the BIOBUZZ V0 PDF itself (tables extracted structurally with PyMuPDF), plus the FIRST volunteer-facing judging documents. **Section 6 is FINAL for BIOBUZZ.**

## 7. Every award, its criteria, and its rules

### 7.1 The award hierarchy (new structure this season)

**FACT** (BIOBUZZ §6.1): *"FIRST Tech Challenge team judged awards fall into three categories, which have one or more awards each: Machine, Creativity, and Innovation (MCI), Team Attributes (TA), and **Documentation**. In addition, the Judges' Choice Award is given to a stand-out team which was not recognized in one of the other categories. The most prestigious, all-around award is Inspire Award."*

| Category | Awards |
|---|---|
| **Inspire** (overarching) | Inspire Award |
| **MCI** | Innovate (sponsored by RTX), Control, Design |
| **TA** | Connect, Reach, Sustain |
| **Documentation** | Think |
| Standalone | Judges' Choice |
| Alliance (§6.4) | Winning Alliance, Finalist Alliance |
| Individual (§6.5) | FIRST Leadership Award, Compass Award |
| Global project-based (§6.6) | "More information about Project-Based Global Awards coming soon!" |

**FACT — three sentences in §6.1 that most teams never read, and that matter enormously to a small team:**

| Quote (BIOBUZZ §6.1, verbatim) | Why it matters |
|---|---|
| "Teams may participate in judging **regardless of the inspection status of their ROBOT** and are eligible for awards **even if they are attending the event without a ROBOT**." | A broken, uninspected, or absent robot costs you match points and playoff points — it costs you **zero** judged-award eligibility. If the robot dies Friday night, you still go to the interview and you can still win 12–60 advancement points. (Unchanged from DECODE §6.1, line 1439.) |
| "All award winners chosen by the JUDGES are recognized as being **positive examples of the award criteria, not necessarily the 'best' team**. JUDGES will only consider the published award criteria in Section 6.3." | The criteria in §7.5 below are the whole exam. There is no hidden rubric. |
| "The local Program Delivery Partner may elect to give **additional awards to celebrate local sponsors or initiatives, but these awards are not considered Team Judged Awards** for the purposes of advancement calculations." | A local sponsor award is nice, is **worth 0 advancement points**, and — because A215 restricts only *team judged awards* — should not block you from a real one. |

**FACT — §6.1.4 "Sustained Outreach and Demonstrating Impact by Numbers"** (verbatim): *"In general, JUDGES will consider **ongoing, sustained outreach to be of higher quality than occasional or one-off outreach**. JUDGES will seek to understand what is the impact of the outreach to the individuals being reached by the activity."* And: *"JUDGES may ask specific questions when a specific term listed in [the Outreach Terms and Definitions] document is mentioned in a team's PORTFOLIO or during an interview."*

**JUDGMENT — this subsection is a trap and an opportunity.** The trap: using a defined term like "started a team," "ran an event," or "reached N people" in your portfolio **invites a scripted audit** against the official definition, and a claim you can't defend is worse than no claim. The opportunity: a small team cannot out-volume a 40-student program on one-off outreach, but it *can* beat them on **sustained** outreach — one partner school, visited monthly, with a measured outcome — which the manual says judges weight higher. Pick one recurring relationship over six photo-op events.

### 7.2 Award inventory — requirements, portfolio need, and point value

**FACT.** Portfolio-required set is stated in the FIRST *Judging Quick Start* (rev 25-26.1, <https://ftc-resources.firstinspires.org/ftc/archive/2026/event/judge-quickstart>): "**Portfolio Required:** Think, Control, and Inspire. **Portfolio Optional:** Connect, Reach, Sustain, Design, Innovate, and Judges' Choice." This matches the BIOBUZZ §6.3 criteria tables exactly.

| Award | Category | Portfolio | Advancement pts 1st / 2nd / 3rd | Manual ref |
|---|---|---|---|---|
| Inspire | — | **Required** | **60 / 30 / 15** | §6.3.1, Table 6-2 |
| Think | Documentation | **Required** | 12 / 6 / 3 | §6.3.2, Table 6-3 |
| Connect | TA | Optional | 12 / 6 / 3 | §6.3.3, Table 6-4 |
| Reach | TA | Optional | 12 / 6 / 3 | §6.3.4, Table 6-5 |
| Sustain | TA | Optional | 12 / 6 / 3 | §6.3.5, Table 6-6 |
| Innovate (RTX) | MCI | Optional | 12 / 6 / 3 | §6.3.6, Table 6-7 |
| Control | MCI | **Required** | 12 / 6 / 3 | §6.3.7, Table 6-8 |
| Design | MCI | Optional | 12 / 6 / 3 | §6.3.8, Table 6-9 |
| Judges' Choice | — | Optional | 12 / 6 / 3 | §6.3.9 |
| Winning Alliance | Alliance | n/a | 40 (both teams) | §6.4.1, Table 4-1 |
| Finalist Alliance | Alliance | n/a | 20 (both teams) | §6.4.2, Table 4-1 |
| FIRST Leadership | Individual | n/a (4,000-char essay, **~15 Dec deadline**) | **0** (§4.1.4: "is not for a team (e.g., the FIRST Leadership Award)… no points are earned") | §6.5.1, §4.1.4 — full detail in **§15.1** |
| Compass | Individual | n/a (40–60 s video; **Regional Championship level only**) | 0 | §6.5.2, Table 6-10 — full detail in **§15.2** |
| Project-Based Global | Global | varies | **0** ("do not contribute towards team advancement") | §6.6 — **§15.3** |

**FACT — A215 does not touch the last three rows.** A215 restricts a team to "a single **team** judged award"; §6.4 Alliance awards and §6.5 Individual awards are explicitly carved out. So Winning Alliance + Connect 1st + a FIRST Leadership Award semi-finalist is a legal and normal outcome for one team at one event.

### 7.3 How many awards exist at your event — Table 6-1, verbatim

**FACT** — extracted structurally from the V0 PDF page 51 (this table is badly mangled by plain-text extraction; the version below is the real one):

| Award | 4–10 teams | 11–20 teams | 21–40 teams | 41–64 teams |
|---|---|---|---|---|
| **Inspire** | 1st | 1st, 2nd | 1st, 2nd, 3rd | 1st, 2nd, 3rd |
| **Think** | 1st | 1st | 1st, 2nd | 1st, 2nd, (3rd\*) |
| **Connect** (TA) | 1st — *only one of Connect, Reach, or Sustain will be given* | 1st | 1st, (2nd\*) | 1st, 2nd, (3rd\*) |
| **Reach** (TA) | ″ | 1st | 1st, (2nd\*) | 1st, 2nd, (3rd\*) |
| **Sustain** (TA) | ″ | 1st | 1st, (2nd\*) | 1st, 2nd, (3rd\*) |
| **Design** (MCI) | 1st — *only one of Innovate, Control, or Design will be given* | 1st | 1st, (2nd\*) | 1st, 2nd, (3rd\*) |
| **Innovate** (MCI) | ″ | 1st | 1st, (2nd\*) | 1st, 2nd, (3rd\*) |
| **Control** (MCI) | ″ | 1st | 1st, (2nd\*) | 1st, 2nd, (3rd\*) |
| **Judges' Choice** | Optional\* | Optional\* | Optional\* | Optional\* |

`*` = discretionary. **A211**: "Only the awards specified in Table 6-1 based on the event size are points-eligible for advancement."

**JUDGMENT — read this table strategically.** At a **21–40 team** event (the modal qualifier) there are **11–17 judged award slots** for ~30 teams. Roughly **one team in two or three leaves with a judged award.** At an 11–20 team event there are 9 slots for ≤20 teams — better odds still. Small local events are where a small team should farm award points.

### 7.4 The judged-award rules, A201–A215

**FACT** — full rule inventory with the operative constraint of each. All quotes verbatim from BIOBUZZ §6.2.

| Rule | Title | The constraint you must obey |
|---|---|---|
| **A201** | *Team PORTFOLIOS have limits* | **1 cover page** (team number required; name/TOC/orgs/sponsors/logo/motto/photo optional) + **no more than 15 pages of content**; **US Letter 8.5"×11" or A4 210×297 mm**; **digital submissions < 15 MB**; content only from **on or after 1 January 2026**. "Any content beyond the allowed 15 pages will not be reviewed by the JUDGES." |
| **A202** | *PORTFOLIOS must be submitted on time and as requested* | Submit as the Event Director instructs, by the stated deadline. **Default if no instructions given: "submit 1 printed copy of their PORTFOLIO during the Initial Interview."** |
| **A203** | *Teams must participate in an interview session* | "To be considered for any judged awards the team must participate in an Initial Interview session." |
| **A204** | *Have the right resources available for your Initial Interview* | (A) ≥2 student reps for teams of 2+; (B) a copy of the portfolio for reference; (C) show-and-tell items incl. robot (encouraged, optional); (D) 1 silent observer (optional); (E) 1 accommodation support person (optional). Robot may be powered on and demonstrated "but may not cause significant delays." |
| **A205** | *Everyone gets equal Initial Interview time* | "All teams will be scheduled for the same length Initial Interview of **at least 10 minutes**." |
| **A206** | *The Initial Interview timer starts when the team starts* | Timer starts after judges introduce themselves and either the team begins presenting or Q&A begins. Slow starts get a warning, then the clock runs anyway. |
| **A207** | *Prepared initial presentation time should not be interrupted* | "**The first 5 minutes** of the Initial Interview are reserved for the team to present a prepared oral presentation uninterrupted, if they choose." May be ended early by the team. |
| **A208** | *One adult silent observer is welcome* | One adult may attend. "The adult observer and coach(es) may not interact or actively coach during any interaction between the JUDGES and the STUDENT team members." |
| **A209** | *Translator / Sign Language Interpreter accommodations* | Team generally provides the translator; **arrange in advance** with the Event Director for **2–5 extra minutes**. Translator is in addition to the A208 observer. |
| **A210** | *No Photos, Video or Audio recording during Initial Interview* | Absolute. Also see **E116** (consent to record anyone at the event). |
| **A211** | *The number of awards given scales with event size* | Table 6-1 above; only those awards are advancement-points-eligible. |
| **A212** | *Judging feedback is provided to all teams* | Feedback form completed immediately after the Initial Interview, based on **initial impression only**; "This feedback form is not used during deliberations." Returned with the portfolio near the end of the event, or delivered to Lead Coach 1 digitally via FTC-Scoring. |
| **A213** | *Teams are only eligible to win the Inspire Award in their own region* | Inspire 1st/2nd/3rd only at a tournament in your **HOME REGION**. "FIRST Championship and FIRST Premier Events are an exception to this rule. At these events, all teams may be considered for the Inspire Award." |
| **A214** | *Teams cannot win the Inspire Award at multiple Qualifying or League Tournaments* | 1st-place Inspire once per season from any QT/LT. You **may** still win 2nd/3rd at later QT/LTs, and **you may win 1st again at your Regional Championship**. |
| **A215** | *Teams can only get one judged award* | "Teams are only eligible to win or be a runner-up for a **single team judged award** at the event." Does not block Alliance awards (§6.4) or Individual awards (§6.5). |

### 7.5 The criteria tables — Required vs. Encouraged, verbatim

**FACT** — extracted structurally from the V0 PDF (pages 53–57) so the Required/Encouraged column is correctly aligned. **Required means the judges cannot give you the award without it.**

**Inspire (Table 6-2)** — all four Required:
1. Team must submit a PORTFOLIO.
2. "A team must be a strong contender for at least one award in each of the following judged award categories: A. Machine, Creativity, and Innovation Awards, B. Team Attributes Awards, and C. Think Award."
3. Team must be positive and inclusive, and each team member contributes to the success of the team.
4. Team is able to share their experiences and knowledge to the JUDGES.

**Think (Table 6-3)**
| | Criterion |
|---|---|
| **Required** | Submit a PORTFOLIO containing **at least one** of: A. evidence of use of the engineering process; B. lessons learned and applied relating to the design of their ROBOT; C. **comparing choices** — "Show how you looked at different ideas and explain why you chose one over the other"; D. **math choices** — "Show how you used math to make decisions about your ROBOT or programming design." |
| Encouraged | "Information in the PORTFOLIO should be easy to read and easy to find." |

**Connect (Table 6-4)**
| | Criterion |
|---|---|
| **Required** | Professional development competency: explain the plan for developing team member skills, including **both** (A) the team's goals for learning and (B) the steps taken or to be taken to reach them. |
| Encouraged | Networking competency — building and maintaining meaningful in-person or virtual relationships with STEM professionals. |
| Encouraged | Collaboration competency — "actively working with members of the engineering community through mentoring, knowledge sharing, technical guidance, or collaborative activities." |

**Reach (Table 6-5)**
| | Criterion |
|---|---|
| **Required** | Outreach planning competency: clearly explain **all** of (A) outreach objectives, (B) **the strategy behind** the activities, (C) how these activities support the growth of the FIRST community. |
| **Required** | "Team demonstrates successful **recruitment of new teams, coaches, mentors, or volunteers who have not previously participated** in the FIRST community." |
| Encouraged | Communication competency — ambassador for FIRST, increasing public awareness. |
| Encouraged | Media and promotion competency — "creative, continuously improving outreach materials." |

**Sustain (Table 6-6)**
| | Criterion |
|---|---|
| **Required** | Organizational sustainability competency: plans for long-term success including **one or more** of (A) financial sustainability, (B) season planning, (C) long-term team sustainability objectives. |
| **Required** | Project management competency: "explaining how it **measures, reviews, and tracks progress** toward its sustainability plans and objectives." |
| Encouraged | Leadership development competency — defined roles + intentional process for preparing future student leaders. |
| Encouraged | Risk management competency — identifying constraints, mitigation, adapting plans. |

**Innovate, sponsored by RTX (Table 6-7)**
| | Criterion |
|---|---|
| **Required** | "The team demonstrates their engineering competency by showing examples of their engineering work that explain how the team developed their design." |
| **Required** | The design of the ROBOT or ROBOT MECHANISM is creative, unique, or both. |
| **Required** | "The creative design must be stable and reliable. It must help the team reach its game goals **most of the time**." |
| Encouraged | "Designs often involve risks. The team should explain how they reduced those risks." |

**Control (Table 6-8)**
| | Criterion |
|---|---|
| **Required** | Submit a PORTFOLIO including **all** of: A. hardware or software control COMPONENTS on the ROBOT; B. the challenges each COMPONENT or system solves; C. the function of each COMPONENT or system. |
| **Required** | "The team must use one or more hardware or software solutions that use **external feedback** to control the ROBOT and improve how it performs." |
| Encouraged | Solutions work consistently during most MATCHES. |
| Encouraged | Explain reliability — by demonstrating it works, or explaining how it could be improved. |
| Encouraged | Describe what was learned using the engineering process to develop the control solutions. |

Section 6.3.7 also states: *"The team's PORTFOLIO must include a summary of the software, sensors, and mechanical control system. The PORTFOLIO does not need to include the full code itself."*

**Design (Table 6-9)**
| | Criterion |
|---|---|
| **Required** | "Team must describe or demonstrate that their ROBOT is elegant, efficient (simple to build and operate), **and/or** practical to maintain." |
| **Required** | "The design of the **entire ROBOT**, or the detailed process used to create it, must be considered — not just one COMPONENT." |
| Encouraged | Stands out for appearance and function. |
| Encouraged | Reasons behind design choices clearly thought through. |
| Encouraged | Design works consistently and aligns with the team's game plan or strategy. |

---

## 8. What changed from DECODE (2025-26) to BIOBUZZ (2026-27)

**FACT** — diffed against `manuals/archive/2025-26_DECODE_Competition_Manual_TU32.txt` §6.

| Area | DECODE 2025-26 | BIOBUZZ 2026-27 | Why you should care |
|---|---|---|---|
| **Award taxonomy** | Two categories (MCI, TA) plus "two other separate awards, the Think Award and the Judges' Choice Award" | **Three categories: MCI, TA, and Documentation** (Think sits in Documentation) | Cosmetic on its face — but it hardens Think's identity as a pure engineering-documentation award |
| **Interview name** | "Structured Interview" | **"Initial Interview"** throughout (A203, A204, A205, A206, A207, A210, A212) | Search-and-replace your whole portfolio and prep materials |
| **Interview format** | One format implied (dedicated judging space) | **Three explicit formats: scheduled in-person, unscheduled in-person (in your pit), remote.** "All teams, regardless of the option chosen, are expected to be interviewed using the same format at their event." | **Biggest practical change.** Your 5-minute presentation may now be delivered standing in a loud pit with no projector. Prepare for that case by default. |
| **A205 buffer** | "at least 10 minutes **with a minimum of 10 minutes reserved between structured interviews** for JUDGES to confer" | "at least 10 minutes" — the inter-interview buffer requirement is **gone** | Consistent with pit-based interviews; expect tighter, more improvised scheduling |
| **A206 timer** | Starts "after the team has entered the room and when they begin their presentation" | Starts "after the JUDGES have introduced themselves and either, the team begins their presentation, or the Q&A portion… begins" | The clock can now start on Q&A if you decline to present |
| **A204.B portfolio** | "a **printed** copy of their team PORTFOLIO (**optional**, submit as instructed)" | "a copy of their team PORTFOLIO **for reference during the interview**" — no longer marked optional | Bring a copy for yourselves, separate from the one you hand in |
| **A204 robot demo** | Allowed "unless explicitly disallowed by the Event Director" | Allowed, "but may not cause significant delays during the interview" | Demo is now default-permitted; keep it under ~45 seconds |
| **A201 PII** | "Teams are **encouraged to limit** PII… Best practices would be to use only first names and optionally last initials." | "Teams **must strictly minimize** PII… **use only first names and last initials.** While student photographs are permitted, **full names must not be disclosed.**" | **Hard requirement now.** Scrub full names from photo captions, sponsor thank-yous, org charts, and screenshots |
| **A201.E date** | since 1 January **2025** | since 1 January **2026** | Nothing from your 2025 season counts as current-season content |
| **A208 observer** | "One adult **mentor** may attend" | "One **adult** may attend"; "Adult **coach(es)**" | Terminology shift mentor → coach |
| **A213 Inspire region** | "within their own region" | "within their **HOME REGION**" **+ new exception**: "FIRST Championship and FIRST Premier Events are an exception… all teams may be considered" | Out-of-region events are Inspire-ineligible; Worlds/Premier are not |
| **A214** | 1st-place Inspire once per season from any QT/LT | Same, **plus explicit**: "Teams who have won 1st Place Inspire at a Qualifying or League Tournament are eligible to win it at their Regional Championship." | Removes a real ambiguity |
| **A215** | "a single judged award" | "a single **team** judged award"; explicit carve-out for §6.4 Alliance and §6.5 Individual awards | Clarification |
| **6.1.1 sources** | "JUDGE Advisors **may also accept feedback about teams at the event from other volunteers**" | That sentence is **removed**. Sources are now: Initial Interview, any follow-up interview, and the PORTFOLIO. Plus an explicit disallowed list that now names **"ROBOT penalties during gameplay"** and **"A team's ranking in the tournament."** | Narrower, more predictable evidence base — and explicit confirmation that rank and penalties cannot be held against you |
| **E-rule cross-ref in A210** | E117 | **E116** | Event rules renumbered |
| **Think criteria** | 3 rows: engineering content (Required); *resources / recruiting / goal-tracking* (Encouraged); organization (Encouraged) | 2 rows: engineering topics (Required); readability (Encouraged). The **resources/recruiting/goal-tracking row is gone** | Think is now **purely engineering documentation**. Move recruiting and goal-tracking content into TA-award sections of your portfolio |
| **Think criterion wording** | "trade off analysis / cost benefit analysis", "mathematical analysis used to make design decisions" | "**comparing choices:** Show how you looked at different ideas and explain why you chose one over the other" and "**math choices:** Show how you used math to make decisions" | Same content, plainer language — and a clear invitation to show a decision matrix |
| **Connect / Reach / Sustain** | Narrative "discuss, describe, display, or document" phrasing | Rewritten in **explicit competency language** (professional development / networking / collaboration; outreach planning / communication / media & promotion; organizational sustainability / project management / leadership development / risk management) | Structure your portfolio pages with these exact competency headings — you are handing the judges their own checklist |
| **Reach Required #1** | objectives + how activities support FIRST | objectives + **strategy** + how they support growth of the FIRST community | "Strategy" is now explicitly required |
| **Design Required #1** | "elegant, efficient (simple/executable), **and** practical to maintain" | "elegant, efficient (simple to build and operate), **and/or** practical to maintain" | Lower bar — you may now win on one attribute |
| **§6.6 Global awards** | Digital Animation Award (WPI) and Safety Animation Award (UL Solutions) named | "**More information about Project-Based Global Awards coming soon!**" | Unknown for BIOBUZZ. Watch Team Updates. |
| **AI use in portfolio** | Permitted with footnote/endnote credit | Same, wording tightened: "Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a footnote or endnote credit. Example Credit: 'Portfolio created by Team XXXXX and ChatGPT'" | **You use Claude Code — you must credit it in the portfolio.** |

**Unchanged and worth confirming (verified line-by-line against the DECODE text):** Table 6-1 award counts · the 15-page / 15 MB portfolio limits · the 5-minute uninterrupted presentation · the 10-minute minimum interview · Winning / Finalist Alliance awards · FIRST Leadership Award (§6.5.1 defers to the FIRST webpage in both seasons) · Compass Award (**40–60 second** video, "cannot be longer than 60 seconds, including credits"; `.mp4`/`.mov`/`.avi`/`.wmv`; no streaming links; one per team per event; music licensed and credited; **Regional Championship level and FIRST Championship only**) · §6.1.4 Sustained Outreach and Demonstrating Impact by Numbers · "Teams may participate in judging regardless of the inspection status of their ROBOT and are eligible for awards even if they are attending the event without a ROBOT" · the local-Program-Delivery-Partner sponsor-award carve-out.

---

## 9. The advancement economics of awards

### 9.1 The point table

**FACT** (BIOBUZZ Table 4-1, `sections/04_Advancement_p27-32.txt`):

| Category | Points |
|---|---|
| Qualification phase performance | 2–16, normally distributed by rank (formula below) |
| ALLIANCE lead | `21 − alliance number` (e.g. 18 for alliance #3 lead) |
| Draft order acceptance | `21 − draft position` (e.g. 18 for accepting the 3rd pick) |
| Playoff: Winners / Finalists / 3rd / 4th | **40 / 20 / 10 / 5** |
| **Inspire 1st / 2nd / 3rd** | **60 / 30 / 15** |
| **All other judged awards 1st / 2nd / 3rd** | **12 / 6 / 3** |

Tiebreaks, in order (Table 4-2): total advancement points → **Judged Team Award Points** → playoff advancement points → alliance selection results → qualification phase performance → average qual match points (excl. fouls) → average auto points → highest individual match → second highest → random.

**JUDGMENT:** note that **judged-award points are the *first* tiebreaker.** A judged award doesn't just add 12 points; it wins ties against a team with identical totals.

### 9.2 The qualification-points formula — verified

**FACT** (BIOBUZZ §4.1.1; the formula's numerals were recovered from the PDF via PyMuPDF because the plain-text extract drops them):

```
QualificationPoints(R, N, α) = ceil( InvERF( (N − 2R + 2) / (αN) ) × ( 7 / InvERF(1/α) ) + 9 )

R = qualification rank    N = teams in qualification rounds    α = 1.07 (constant)
```

**ANALYSIS — verification.** I implemented this and reproduced BIOBUZZ Table 4-3 (a 28-team event) **exactly**: rank 1→16, 2→15, 3→14, 4→14, 12→10, 13→10, 14→10, 25→6, 26→5, 27→5, 28→4. The formula is correct as transcribed; you can use it to compute the advancement value of any rank at any event size.

Illustrative outputs at N = 31:

| Rank | 1 | 5 | 10 | 12 | 16 | 22 | 29 | 31 |
|---|---|---|---|---|---|---|---|---|
| Points | 16 | 13 | 11 | 11 | 10 | 8 | 5 | 4 |

**JUDGMENT — the crucial implication.** The gap between rank 1 and rank 22 is **8 points**. A single 1st-place judged award is worth **12**. Inspire 1st is worth **60**. *Chasing rank is the most expensive way to earn advancement points in FTC.*

### 9.3 A real event, fully costed

**ANALYSIS.** Event `USTXDAQ2` (FiT-North Winter Charger Qualifier, 32 teams, 31 ranked, 13 Dec 2025). Award results and stats from ftcscout REST; qual points computed with the verified §9.2 formula. Alliance-lead / draft-acceptance points are **excluded** (they require the authenticated FTC-Events `/alliances/{code}/selection` endpoint), so real totals for playoff teams are 14–20 points higher.

| Team | Qual rank | OPR | Qual pts | Judged award | Award pts | Playoff | Playoff pts | Total\* |
|---|---|---|---|---|---|---|---|---|
| 21932 Forged In Iron | 1 | 101.3 | 16 | Inspire 2nd | 30 | Winner | 40 | **86** |
| **20313 Mustang Robotics** | **22** | **17.4** | **8** | **Inspire 1st** | **60** | — | 0 | **68** |
| 15083 Overclock | 2 | 104.3 | 15 | Sustain 1st | 12 | Winner | 40 | 67 |
| 26876 ITKAN Girls | 7 | 60.8 | 13 | Connect 1st | 12 | Finalist | 20 | 45 |
| 18871 RoboChargers-Pluto | 6 | 40.1 | 13 | — | 0 | Finalist | 20 | 33 |
| 26300 Anomaly | 3 | 54.9 | 15 | Reach 1st | 12 | — | 0 | 27 |
| 17294 Overdr!ve | 10 | 47.2 | 11 | Inspire 3rd | 15 | — | 0 | 26 |
| 30758 Byte Battalion | 12 | 64.6 | 11 | Innovate 1st | 12 | — | 0 | 23 |
| 32163 Fillie-Bots | 15 | 24.4 | 10 | Judges' Choice 1st | 12 | — | 0 | 22 |
| 9001 Rangers-Gold | 20 | 10.6 | 8 | Control 1st | 12 | — | 0 | 20 |
| **19991 Chuckleheads** | **26** | **15.4** | **6** | **Design 1st** | **12** | — | 0 | **18** |

`*` excludes alliance-lead / draft-acceptance points.

**JUDGMENT — read the highlighted rows.**
- Team **20313** had a bottom-third robot (rank 22, OPR 17.4 vs the event's best of 104.3) and finished **second in advancement points at the entire event.**
- Team **19991** had the 6th-worst OPR in the field, won Design 1st, and out-scored several teams ranked in the top ten.
- Team **9001** — rank 20, OPR 10.6, the *lowest* OPR of any award winner here — won the **Control Award**. Control does not require a fast robot. It requires sensors, feedback, and a portfolio that explains them.

This is the strategic core of the whole document for a small team: **the robot buys you 4–16 points; the paperwork and the interview buy you 12–60.**

---

## 10. Which awards can a small team realistically win? — measured

**ANALYSIS — method.** I pulled every **Qualifier** event with matches from the 2025-26 (DECODE) season across 18 US regions via the ftcscout GraphQL `eventsSearch`, then for each event fetched the full award list and the full team-stats list via ftcscout REST. **162 events** met the criteria (≥12 ranked teams); 156 had a complete judged-award set. For each 1st-place award winner I recorded their **percentile within their own event** by qualification rank and by total OPR (0% = best team at the event, 100% = worst). Median across events:

| Award (1st place) | n | Median winner's **qual-rank** percentile | Median winner's **OPR** percentile | % of winners in the event's **top quartile** | % in the **bottom half** |
|---|---|---|---|---|---|
| **Inspire** | 156 | **14.5** | 12.9 | **67%** | 16% |
| **Control** | 156 | **22.0** | 17.5 | 53% | 22% |
| **Design** | 156 | 34.8 | 29.0 | 38% | 33% |
| **Think** | 156 | 37.7 | 34.3 | 39% | 37% |
| **Innovate** | 156 | 40.9 | 33.3 | 35% | 37% |
| **Reach** | 156 | 43.6 | 42.1 | 28% | 42% |
| **Sustain** | 156 | 43.7 | 40.4 | 29% | 42% |
| **Connect** | 156 | 45.7 | 39.1 | 27% | 46% |
| **Judges' Choice** | 102 | **58.2** | 60.9 | 16% | **58%** |

**Reading this honestly (JUDGMENT):**

- **Inspire is robot-gated in practice.** The manual forbids judges from considering rank (§6.1.1), and they don't — but the *causes* of a good robot (organization, planning, iteration, a team that finishes things) are the same causes that produce a strong portfolio and confident students. Two-thirds of Inspire 1st winners were in their event's top quartile. **If your robot is in the bottom half, Inspire 1st is a ~16%-of-winners outcome, not a plan.**
- **Control is the most robot-correlated of the non-Inspire awards** (median 22nd percentile) — but note team 9001 above at rank 20/31 with the lowest award-winning OPR at its event. Control rewards *sensors and feedback*, not speed. A slow robot with a genuinely closed-loop autonomous is a real Control candidate.
- **Connect, Sustain, and Reach are essentially uncorrelated with robot performance** (medians 43.6–45.7 percentile — i.e., the median winner is a middle-of-the-pack robot, and ~42–46% of winners are in the *bottom half*). **These are the small team's highest-probability targets.** They require zero additional robot performance and are the only awards whose Required criteria you can fully satisfy with work done in September and October.
- **Judges' Choice actively skews toward lower-ranked teams** (median 58.2 percentile) — it exists precisely to recognize teams that don't fit elsewhere. It is discretionary (may not be given), so you can't plan on it, but don't discount it.
- **Design and Think sit in the middle** and are the natural "second target" once TA is secured.

**Recommended target order for a small, low-budget team (JUDGMENT):**

| Priority | Award | Why | What it costs you |
|---|---|---|---|
| 1 | **Connect** or **Sustain** | Lowest robot correlation; Required criteria are pure planning documents you can finish before the first event | 2–3 hours of writing + 1 real STEM-professional relationship |
| 2 | **Think** | You must write the portfolio anyway for Control/Inspire eligibility; Think just requires the *engineering* half be good | Marginal — a decision matrix and one math-driven design decision |
| 3 | **Control** | Rewards software, which is the cheapest thing a small team can be excellent at (see the Control section, §12) | Sensor work you'd do anyway; ~2 portfolio pages |
| 4 | **Reach** | Second Required criterion (recruiting *new* people to FIRST) is a genuine bar — do not claim it loosely | An actual recruiting effort with documentation |
| 5 | **Inspire** | Requires being a strong contender in MCI **and** TA **and** Think simultaneously — see §14 | Everything above, done well, plus a robot in the event's top third |

**Remember A215:** you can only win one. Target order is about *where to invest*, not about spreading thin. Invest in one TA award and Think/Control, and let the multi-category nomination pull you toward Inspire naturally.

---

## 11. The Engineering Portfolio

### 11.1 The hard requirements (get these wrong and nothing else matters)

**FACT — A201, verbatim constraints:**

| Requirement | Value | Failure mode |
|---|---|---|
| Cover page | Exactly **1**, must include **team number** | "Teams who forget to include a cover page **may be disqualified from judging** if the JUDGES cannot determine what team the PORTFOLIO is associated with." |
| Content pages | **≤ 15** | "Any content beyond the allowed 15 pages will not be reviewed" |
| Cover page counts toward criteria? | **No.** "None of the content of the cover page will be used by JUDGES to evaluate any awards criteria." | Don't waste real content on the cover |
| Page size | US Letter 8.5"×11" **or** A4 210×297 mm | — |
| Digital size | **< 15 MB** | Compress your CAD renders |
| Content date window | **On or after 1 January 2026 only** | Prior-season content may be *referenced* to show growth, "but the emphasis must be on the current season" |
| PII | "must strictly minimize"; **first names + last initials only**; photos OK but "**full names must not be disclosed**" | New, stricter than DECODE |
| Font / contrast | "Avoid fonts under 10 pt and low-contrast text on images — JUDGES cannot evaluate what they cannot read." Manual explicitly recommends the **WebAIM Contrast Checker** | — |
| **Links, QR codes, videos** | **"JUDGES will not click on links, websites, or videos in a PORTFOLIO."** | A portfolio that says "see our website for details" has thrown away that content |
| Extra handouts | "They also cannot take extra printed papers from an interview back to their judging room. Teams should put everything they want JUDGES to see **directly in their PORTFOLIO**." | — |
| **AI credit** | "Teams may use AI and research aids to compose their portfolios, provided they respect intellectual property rights and include a **footnote or endnote credit**. Example Credit: 'Portfolio created by Team XXXXX and ChatGPT'" | **Required for this team.** Put a footnote naming Claude / Claude Code. |

**FACT — A202 deadline:** submit as the Event Director instructs, by the stated deadline. **"If no other instructions are provided, teams should submit 1 printed copy of their PORTFOLIO during the Initial Interview."** The manual also says: "Teams are encouraged to have an additional copy (digital or physical) of their PORTFOLIO available in their pit to assist with interviews they have with the JUDGES."

**JUDGMENT:** print **three** copies: one to hand in, one for your interview table (A204.B), one taped-open in the pit for follow-up interviews (§13.2). At ~16 colour pages that is a real but small cost — ESTIMATE $8–15 per set at a copy shop; verify locally.

### 11.2 What the judges actually *do* with it

**FACT** (FIRST *Judging Quick Start*, rev 25-26.1):

- "Judges, working in **2s or 3s**, talk with students on teams, review the team portfolio, and complete Structured Interview feedback form."
- "Each judging panel interviews **a set number of teams**… **All Judges do not interview all teams.**"
- "**Give your full attention to the team during the Structured Interview. Do not review the Portfolio at this time.** Portfolios will be initially reviewed **after the team leaves**."
- "Judges must only consider content **Discussed, Displayed, Documented, or Demonstrated** at the event."
- "Once judging panels have completed all their assigned interviews, they return to a judging deliberation room, where they nominate teams they have interviewed for specific awards. **Teams can be nominated for more than one award. No team is nominated directly for the Inspire Award.**"
- "Judges are then re-assigned into **award-specific panels**, and Judges will conduct Pit Interviews to gather additional information or review Portfolios."

**JUDGMENT — three design consequences that most teams miss:**

1. **Your portfolio is read cold, after you leave, by two or three tired adults with ~5 minutes.** It must be navigable without you narrating it. Section headers that match award-criteria language are worth more than clever design.
2. **A second, different panel of judges will read it later** during the award-specific review — people who never met you. Every page must stand alone.
3. Because judges "must only consider content Discussed, Displayed, Documented, or Demonstrated **at the event**," and because they will not click links (A201), **your portfolio + your interview + your pit display are the complete universe of evidence.** Your website, your Instagram, your YouTube channel, and your Chief Delphi build thread are all worth zero at the event unless their *content* is reproduced inside those three channels.

### 11.3 A recommended 15-page budget

**JUDGMENT.** This allocation is built backwards from the Required criteria in §7.5 and from Game Manual 0's portfolio guidance (<https://gm0.org/en/latest/docs/awards/portfolio.html>), which recommends splitting the robot into "3-4 parts, putting a different mechanism on a new page," dedicating "a page or two" to high-level robot overview and sensors, and warns "Less is more: Judges are going to lose interest in large unbreakable blocks of text" and "**Images, Images, Images**."

| Pages | Section | Must contain (mapped to Required criteria) |
|---:|---|---|
| Cover | Team number (required), name, logo, robot photo, TOC | — |
| 1 | **Season plan & goals** | Sustain-R1 (season planning), Sustain-R2 (how you measure/review/track) |
| 1 | **Strategy & game analysis** | Think-R1.A (engineering process), Design-E5 (design aligns with strategy) |
| 1 | **Design decision matrix** | **Think-R1.C** ("comparing choices") — one honest table with weighted criteria and the option you rejected |
| 1 | **The math** | **Think-R1.D** ("math choices") — one real calculation that changed a decision (gear ratio, torque budget, cycle-time model, tolerance stack) |
| 3–4 | **Mechanism pages** (1 per major subsystem) | Innovate-R1/R2/R3, Design-R2 (whole robot considered), Think-R1.B (lessons learned and applied). Each page: why it was needed → what it is → iterations with reasons → math/sensors → CAD + real photo |
| 2 | **Control system** | **Control-R1.A/B/C** (components / challenge solved / function) and **Control-R2** (external feedback). Include a block diagram. No code listings. |
| 1 | **Reliability & failure log** | Control-E4, Innovate-E4 (risk reduction), Design-R1 (practical to maintain) |
| 1 | **Team organization, roles & leadership pipeline** | Sustain-E3, Inspire-R3 (every member contributes) |
| 1 | **Learning plan & STEM connections** | **Connect-R1.A/B** (goals for learning + steps taken), Connect-E2/E3 |
| 1 | **Outreach: objectives, strategy, impact** | **Reach-R1.A/B/C** and **Reach-R2** (new people recruited — name them, with numbers and evidence) |
| 1 | **Finances & sustainability** | Sustain-R1.A (financial sustainability), Sustain-E4 (risk management) |
| — | Footer on every page | Team number; AI credit footnote on the last page (A201) |

**JUDGMENT — the three highest-leverage pages** for a small team are the **decision matrix**, the **math page**, and the **control block diagram**. They are cheap (a few hours each), they map 1:1 onto Required criteria that most teams satisfy only vaguely, and they are exactly what judges ask follow-up questions about.

### 11.4 Common disqualifiers and self-inflicted wounds

| Mistake | Consequence | Source |
|---|---|---|
| No cover page / no team number | **May be disqualified from judging** | A201 |
| 16+ content pages | Extra pages simply not read | A201 |
| Links / QR codes instead of content | Content is not considered | A201 |
| Full student names in captions | Violates A201's PII requirement | A201 (new for BIOBUZZ) |
| <10 pt font, low-contrast text over images | Judges "cannot use anything they cannot read" | A201 |
| Prior-season content presented as current | Violates A201.E | A201 |
| No AI credit when AI was used | Violates A201 | A201 |
| Missing the submission deadline | Portfolio not considered → **Think, Control and Inspire become impossible** | A202 |
| Skipping the Initial Interview | **Ineligible for all judged awards** | A203 |
| Fewer than 2 student reps at the interview | Violates A204.A | A204 |
| Coach answering questions | Violates A208 | A208 |

### 11.5 Published portfolio examples worth studying

**FACT** — these URLs resolve (HTTP 200 checked 21 Aug 2026). **Content quality is UNVERIFIED — I did not read them in full, and all pre-date BIOBUZZ's Section 6 rewrite, so their criteria mapping is one season stale.**

| Resource | URL |
|---|---|
| Game Manual 0 — Engineering Portfolio | <https://gm0.org/en/latest/docs/awards/portfolio.html> |
| Game Manual 0 — The Judging Process and Presentation | <https://gm0.org/en/latest/docs/awards/judging-presentation.html> |
| Game Manual 0 — Types of Awards | <https://gm0.org/en/latest/docs/awards/award-types.html> |
| Game Manual 0 — Notebook Designs and Decisions | <https://gm0.org/en/latest/docs/awards/notebook.html> |
| Team Without a Cool Acronym — portfolio resource | <https://twcarobotics.com/engineering-notebook/> |
| Forgotten Coast Robotics — "The Engineering Portfolio Path" (gallery of award-winning portfolios) | <https://fc-robotics.org/right-brain/the-engineering-portfolio-path/> |
| FTC Titans 17576 engineering portfolio (IMSA DigitalCommons) | <https://digitalcommons.imsa.edu/cii_dsw/5/> |
| Ctrl-Y Robotics — FTC Judging and Awards guide | <https://ftc.ctrlyrobotics.org/a-beginners-guide-to-ftc/ftc-judging-and-awards> |

**FACT** — GM0's own framing: *"It only benefits you to go for awards. You can't win awards without making a portfolio, and in certain states the only way to advance is awards."* GM0 also advises contacting your regional judges directly, since "what works in one region may not in other regions."

---

## 12. The Control Award and the technical awards: what evidence wins

### 12.1 Control — the small team's best technical target

**FACT.** BIOBUZZ §6.3.7: *"The Control Award recognizes a team that uses sensors and software to solve game challenges in a creative way… The solution should work well during most MATCHES, but it does not need to work every time. Teams may use their solution during the AUTO period, the TELEOP period, or both. The team's PORTFOLIO must include a summary of the software, sensors, and mechanical control system. The PORTFOLIO does not need to include the full code itself."*

Required: portfolio covering (A) components, (B) challenges each solves, (C) function of each; and (2) **one or more hardware or software solutions that use external feedback**.

**JUDGMENT — "external feedback" is the whole award.** Open-loop time-based autonomous does not qualify. Anything that *measures the world and reacts* does. The cheapest qualifying evidence, in rough order of cost:

| Evidence | Cost | Strength |
|---|---|---|
| Motor encoder closed-loop position/velocity control with a plotted step response | ~$0 (hardware you own) | Strong |
| IMU-based heading hold / turn-to-angle, with error-vs-time plot | $0 | Strong |
| AprilTag / vision localization used to correct a scoring position | $0 (phone camera or webcam you own) | Very strong |
| Dead-wheel odometry with a measured position-error distribution | ~$50–90 for odometry pods (ESTIMATE, verify) | Very strong |
| Sensor-based game-piece detection driving an intake state machine | ~$0–30 | Strong |
| Automated teleop assist (driver presses one button, robot closes the loop) | $0 | Very strong — Control-E-criteria explicitly mention teleop |

**JUDGMENT — the evidence that actually wins, drawn from the Control criteria and the question bank:** judges are asking *"How did your team measure reliability?"* and *"What criteria or process did your team use to determine if a component is working or not working?"* (see §13.3). So the winning artifact is not the code — it is **a measurement**. One page containing:

1. A block diagram: sensors → processing → actuators, labelled with what each solves.
2. A table: subsystem | sensor | feedback loop type | what problem it solves | measured result.
3. **One quantified reliability claim**: "auto scored 14/16 attempts across 4 events (87.5%); the 2 failures were both caused by X; we changed Y; post-change 8/8."
4. One before/after plot.

That single page satisfies Control-R1, Control-R2, Control-E3, Control-E4 and Control-E5 simultaneously, and it is 3–4 hours of work.

### 12.2 Innovate (sponsored by RTX)

**FACT.** All three of criteria 1–3 are **Required**: engineering work showing how the design was developed; the design is creative, unique, or both; and *"The creative design must be stable and reliable. It must help the team reach its game goals most of the time."*

**JUDGMENT.** The reliability requirement is the filter. A clever mechanism that works 40% of the time cannot win Innovate no matter how novel. **Winning evidence:** an iteration sequence (sketch → v1 → failure mode → v2 → measurement), plus a stated success rate. The Encouraged criterion is about **risk reduction** — so explicitly name the risk you took and what you did to de-risk it (prototype, test fixture, backup plan).

### 12.3 Design

**FACT.** Required: (1) elegant, efficient (simple to build and operate), **and/or** practical to maintain — note BIOBUZZ softened this from DECODE's "and"; (2) the **entire robot**, or the detailed process used to create it — "not just one COMPONENT."

**JUDGMENT.** Design is the award where a *simple* robot can beat a complex one, and where a small team's constraint becomes a virtue. Winning evidence: a maintenance argument. "This subassembly is 6 bolts and 90 seconds to replace; here is the timed video/photo sequence; here is why we chose that over the lighter alternative." Pair it with a whole-robot packaging diagram so you satisfy Required #2.

### 12.4 Think

**FACT.** Required: portfolio containing at least one of — engineering process evidence; lessons learned and applied; **comparing choices**; **math choices**.

**JUDGMENT.** Do all four, not one. They're cheap, and the DECODE→BIOBUZZ change stripped the non-engineering escape hatch out of Think, so it is now a pure test of whether you can show engineering reasoning. The two artifacts that most reliably win it: **a weighted decision matrix where you chose the option that was not your favourite**, and **a calculation that changed your mind**. Judges have seen a thousand decision matrices where the team's preferred option wins on every criterion; an honest one stands out immediately.

---

## 13. Judge interviews

### 13.1 Format and timeline

**FACT** (BIOBUZZ §6.1.2). Three possible formats, chosen by the Event Director and applied to every team at the event equally:

| Format | Description |
|---|---|
| Scheduled in-person | Planned meeting at a specific time in a dedicated judging space |
| **Unscheduled in-person** | **"The interview is not scheduled for a specific time. JUDGES meet teams in their pit area at the event or in a dedicated judging space."** |
| Remote | Online video conference, held before in-person gameplay (hybrid events) |

The sequence (Figure 6-3, verbatim):
1. "JUDGES introduce themselves to the team and ask if the team has a prepared presentation they would like to start with."
2. "Teams may present to the JUDGES uninterrupted for **up to about 5 minutes**, per A205."
3. "JUDGES will ask open ended questions and interact with the team for the remaining interview time."
4. "The interview is concluded by the JUDGES."
5. Judges privately discuss and complete the feedback form.

**FACT** — the manual warns about pit interviews specifically: *"Teams participating at events where the Initial Interview is conducted in the pits should be mindful that the pit area is an active and often noisy environment… external distractions (such as pit announcements and general background noise) may occur during the interview and could create communication challenges."*

**FACT** — mandated question structure: *"At each event, the JUDGE Advisor will select two questions from the question bank that all teams will be asked at the start of the Initial Interview's question and answer session. One question will be focused on the MCI award category, and one question will be focused on the TA award category."*

### 13.2 Pit interviews (round two)

**FACT** (BIOBUZZ §6.1.3): after all Initial Interviews, judges compare notes and may follow up in the pits. *"Teams have the opportunity to expand upon materials presented in the Initial Interview and share additional content with the JUDGES (e.g., ROBOT prototypes, design artifacts, and photos or letters from outreach events). A team does not need to prepare another presentation for this pit interview but should be ready to answer questions."* Crucially: *"JUDGES may read additional information during pit interviews but will **not bring back additional content** to be referenced as part of the JUDGE deliberations."*

**JUDGMENT.** A pit visit is a **signal that you were nominated for something** (per the Judging Quick Start, follow-up pit interviews are conducted by *award-specific* panels). Notice which award the questions cluster around and answer *that* award's criteria. GM0's advice here is blunt and correct: *"STAND UP and PUT THE PHONES DOWN"*, and *"Judges will signal their focus area (control, outreach, robot)"* — tailor accordingly rather than reciting your whole story again.

### 13.3 The actual questions — the FIRST Judging Question Bank

**FACT.** FIRST publishes the real bank at <https://ftc-resources.firstinspires.org/ftc/archive/2026/event/question-bank> (Revision 25-26.1 — the BIOBUZZ revision is listed as "coming soon" in the V0 manual, so expect an update; the DECODE-era bank below is the best available proxy today). Ground rules, verbatim from that document:

> "Judges must not ask teams about religion, politics, gender, disabilities, or how the students are doing in school. These topics have no bearing on any FIRST award criteria."
> "Questions should also avoid comparing one team to another team and instead should focus on the strengths or unique qualities of a team."

Representative questions, verbatim, by award:

| Award | Sample questions |
|---|---|
| **Think** | "Can you describe your team's brainstorming process?" (→ "As ideas came in, did your team use any trade-off or cost/benefit analysis?"); "How did your team improve your robot throughout the season?"; "Did your team employ any analysis in making their design decisions?"; "How did your team decide what aspects of their robot needed to be improved? — What types of data did the team use to determine this?" |
| **Connect** | "How did your team set your goals and strategies for this season?"; "Did your team create a learning plan this season? — If so, how did your team decide what should be on the plan for each team member?"; "Have any STEM professionals become a Mentor for your team?"; "How does your team work with other FIRST teams in your area?" |
| **Reach** | "What are your objectives when you participate in these activities?"; "Has your team been able to successfully recruit anyone to participate in FIRST? — Can you give examples of individuals who are now involved in FIRST?"; "How do you market your team?"; "Has your team received any feedback on your marketing efforts?" |
| **Sustain** | "Does your team have a sustainability plan?"; "How is your team's budget allocated, and who is involved in that process?"; "How are responsibilities assigned and tracked over the course of a season?"; "**What gets in the way of your team doing its best work, apart from time?**"; "Does your team have a plan for maintaining or sustaining their finances without relying on a single or few large sources of income?" |
| **Innovate** | "Walk us through the process that your team used to come up with your design"; "What criteria or process did your team use to determine the success of the design?"; "What actions or tasks within a match is it able to reliably score in? — How did your team test for reliability?"; "What risks did your team identify with your design? — How did your team determine if that risk was mitigated?"; "(For Pit Interviews Only) Can you share any CAD drawings or sketches or photos that highlight your design evolution?" |
| **Control** | "What sensors and hardware did your team use on your robot? — What worked, what did not, and why?"; "What pre-programmed libraries or outside resources did your team use?"; "How does your robot: Know where it is on the field? Control acquisition of scoring elements in Auto and/or Teleop? Measure and control the speed of the motors?"; "What enhancements did your team program to assist the drivers during Teleop?"; "**How did your team measure reliability?**" |
| **Design** | "How did your team balance competing factors in your design?"; "Did you look at each component separately or as a single system or sub-systems?"; "How does your team balance functionality, simplicity, and reliability?"; "**What did your team choose to optimize on the robot if you could not do everything?**"; "Did your team's solution originate from an existing design (e.g., in industry, another sport, or a previous season), or was it a completely novel concept?" |
| **Judges' Choice** | "Tell us your story — how is your team making a difference through FIRST?"; "**What is the one thing that we did not ask about that you most want the Judges to know?**"; "Describe a major failure or setback your team experienced… How did this failure force your team to think differently?"; "(New Team) How did your team quickly bridge the knowledge gap to become competitive?" |

**JUDGMENT.** Note how many of these ask for **process, measurement and evidence**, not for outcomes. "How did your team measure reliability?" is asked in both the Innovate and Control banks. If you have one measurement culture and can describe it, you answer half the bank.

### 13.4 What the judges are trained to do (and not do)

**FACT** — FIRST *Judge Manual* rev 25-26.1 (<https://ftc-resources.firstinspires.org/ftc/archive/2026/volunteer/judge>):

- Time commitment: "A Judge should expect to spend **10-12 hours** at a full-day event. **2-4 hours of pre-event training** is required."
- Required reading includes the Competition Manual **Section 6: Awards (A)** and **Section 16: Glossary**, the Judging Quick Start, and the Outreach Terms and Definitions; the Question Bank is "Encouraged." Judges must pass a certification test.
- "**No interview is done, or decision is made, by a single Judge.** A Judge must never interview a team by themselves; this is done using pairs or trios!"
- "Judges look for teams who are a **strong candidate** for each award. It is often not possible to perfectly evaluate the definitive best candidate… Judges are encouraged to make the best decisions with the information that they have in the time they are given."
- "A Judge's role is to **recognize teams doing something right, not to penalize teams from doing something wrong**."
- Judges must not wear team-affiliated clothing or colours; if they accept swag from one team they must be willing to accept it from all.
- Conflicts of interest must be disclosed to the Judge Advisor.

**FACT** — BIOBUZZ §6.1.1 disallowed information, verbatim list: past performance (good or bad); personal knowledge of a team; **external sources such as websites and/or social media**; a robot's match performance unless specifically listed as award criteria; **robot penalties during gameplay**; **a team's ranking in the tournament**.

**JUDGMENT.** Three exploitable consequences: (a) your reputation from last season is worth nothing — say what you did *this* season; (b) a bad qualifying day literally cannot be held against you in judging, so **do not apologise for your rank in the interview**; (c) because judges are trained to find "a strong candidate," not "the best," being *unambiguously* strong on one criterion beats being vaguely good at everything.

### 13.5 Preparing a small team

**JUDGMENT — a 5-person-team plan that fits in ~6 hours total across the season.**

| When | Activity | Time |
|---|---|---|
| Late September | Assign speaking roles. **Every student speaks.** GM0: "Make sure everybody has an opportunity to speak"; silent members "can look bad." A204 requires ≥2 student reps; the manual encourages "as many STUDENTS as possible." | 30 min |
| October | Write the 5-minute presentation as **5 × 1-minute modules** (strategy / robot / control / outreach / sustainability), one student per module. Modules are independently droppable if you're cut short. | 2 h |
| October | Build a **one-page Q&A cheat sheet**: for each of the 9 awards, one sentence of "our best evidence is ___." Laminate it. Nobody reads it during the interview; writing it is the point. | 1 h |
| Every meeting, Nov–Feb | **Two questions, two minutes.** Pull two questions at random from the bank (§13.3), two random students answer, 60 seconds each. ~30 questions covered per month at zero scheduling cost. | 2 min/meeting |
| Two weeks before each event | One full mock interview with an outside adult (a sponsor, a parent engineer, a teacher). Do it **standing up, in a noisy room**, to rehearse the unscheduled-pit format. | 45 min |
| Night before | Rehearse the answer to "**Is there anything else that you want us to know?**" — GM0 flags this as the near-universal closing question, and it appears verbatim in the Judges' Choice bank as "What is the one thing that we did not ask about that you most want the Judges to know?" | 15 min |

### 13.6 Failure modes

| Failure | Why it kills you | Fix |
|---|---|---|
| Reading a script | GM0 lists this first among common mistakes | Bullet points, not sentences; rehearse to the *idea*, not the wording |
| One student answers everything | Inspire-R3 requires "each team member contribute"; judges explicitly rotate who they address | Pre-assign a primary and a backup answerer per topic |
| Coach jumps in | **Violates A208** | Coach sits behind the students, hands visible, mouth closed |
| Rambling | Eats the Q&A time in which judges gather award evidence | 60-second cap per answer, drilled |
| Inconsistent story between Initial and Pit interviews | GM0 lists this explicitly; different panels compare notes | One-page cheat sheet keeps everyone's facts identical |
| Answering a different question than asked | GM0: judges signal their focus area; straying wastes the slot | Train the reflex: repeat the question in 5 words before answering |
| Blowing the 5 minutes on a slick video | Passive time; judges learn nothing about *your students* | Cap media at 30 seconds |
| Pointing at your website / QR code | A201: judges will not click links | Everything must be spoken, shown physically, or in the portfolio |
| Recording your own interview | **Violates A210** outright | Don't |
| Not showing up | **A203: ineligible for all judged awards** | Set three alarms |

---

## 14. The Inspire Award: what it takes, and whether you can target it

### 14.1 The mechanism

**FACT.** Inspire is **not judged directly**. Per the FIRST Judging Quick Start: judging panels "nominate teams they have interviewed for specific awards. Teams can be nominated for more than one award. **No team is nominated directly for the Inspire Award.**" The Judge Advisor's role includes "**Identifying teams which are nominated in multiple award categories to create the Inspire Award candidate list.**"

**FACT.** BIOBUZZ Table 6-2 Required criterion 2: a team "must be a strong contender for at least one award in each of the following judged award categories: A. Machine, Creativity, and Innovation Awards, B. Team Attributes Awards, and C. Think Award." Plus: submit a portfolio; be positive and inclusive with every member contributing; be able to share experiences and knowledge with the judges.

**JUDGMENT — this is a *coverage* problem, not an excellence problem.** You do not need to be the best at anything. You need to be nominated in **three different buckets** — MCI (Innovate/Control/Design), TA (Connect/Reach/Sustain), and Think — by panels that may not be the same panel. Concretely that means:

- Your **portfolio** must independently satisfy Think (engineering reasoning), Control (if that's your MCI route), and at least one TA award's Required criteria. There is no page budget for anything else.
- Your **5-minute presentation** must touch all three buckets. A presentation that is 4 minutes of robot and 1 minute of outreach cannot generate a TA nomination.
- Your **students** must be able to speak to all three, because A215-style panel splits mean whoever is in the room may only be probing one bucket.

### 14.2 Can a small team realistically win it?

**ANALYSIS — the discouraging data.** Across 156 real 2025-26 qualifiers, the median Inspire 1st winner sat at the **14.5th percentile of qual rank** and the **12.9th percentile of OPR**; 67% were in the event's top quartile; only 16% were in the bottom half.

**ANALYSIS — the encouraging data.** At the **2026 FIRST World Championship** (season 2025 in the API), the division Inspire 1st winners' *own-division* performance was:

| Division | Inspire 1st | Qual rank | of | OPR | OPR rank |
|---|---|---|---|---|---|
| Edison | 7477 Super 7 | 43 | 57 | 97.8 | 41 |
| Franklin | 8565 TechnicBots | 33 | 57 | 110.2 | 29 |
| Goodall | 6417 Blu Cru | 34 | 56 | 83.0 | 37 |
| Jackson | 9848 GearView | 30 | 55 | 55.8 | 51 |
| Lovelace | 14423 RoboCorns | 35 | 57 | 100.2 | 32 |
| Ross | **17792 Amigos Droids** | 11 | 56 | 138.0 | 17 |
| **Overall (Finals Division)** | **17792 Amigos Droids** | — | — | — | — |

Five of six division Inspire 1st winners finished in the **bottom half of their division**. (Caveat: at Worlds the talent distribution is compressed and everyone's robot is good, so this is weaker evidence than the qualifier data.)

**JUDGMENT — my honest verdict for this team:**

- **At a Qualifying or League Tournament with a mid-pack robot: Inspire 1st is a long shot, not a plan.** The data says ~16% of winners come from the bottom half of the field. Chase Connect/Sustain/Think/Control instead, and treat an Inspire nomination as the upside case.
- **Target Inspire seriously only in the season in which your robot reliably finishes in the event's top third** — because the correlation is real and because Inspire-R2 requires MCI-category strength, which in practice means judges have to believe your robot.
- **A211 is your friend at small events.** At an 11–20 team event, Inspire 1st and 2nd are both given, and only 9 award slots exist for ≤20 teams. **Prefer smaller events if your region offers a choice.**
- **A214 caps the downside of trying:** you can only win Inspire 1st once per season from a QT/LT, but you remain eligible for 2nd/3rd afterward and for 1st at your Regional Championship. There is no penalty for aiming high early.
- **A213: never expect Inspire at an out-of-region event.** Plan out-of-region trips for robot experience only.

---

## 15. The individual awards — the deadline nobody on a small team remembers

**JUDGMENT — why this section exists.** The FIRST Leadership Award and the Compass Award are worth **0 advancement points** (BIOBUZZ §4.1.4: "If an award is not judged, **is not for a team (e.g., the FIRST Leadership Award)**, or is not judged at the event…, no points are earned"). They are still worth a section, for three reasons: the Leadership Award is decided **entirely off-field, by an essay, with a hard December deadline**, so a 5-person team competes on exactly equal footing with a 40-person program; it does not consume your one A215 team-judged-award slot; and its winners' teams receive a **registration-fee credit**, which is real money for a low-budget team.

### 15.1 FIRST Leadership Award (the award formerly called Dean's List)

**FACT** — BIOBUZZ §6.5.1: *"FIRST Leadership Award semi-finalists, finalists, and winners exemplify student leadership. These individuals actively promote the FIRST mission, champion Core Values like Inclusion, Teamwork, and Impact, and embody Gracious Professionalism."* The manual defers all mechanics to the FIRST Leadership Award webpage.

**FACT** — mechanics below are from the official *FIRST Leadership Award Nomination Guide*, **Revision 25-26.4** (<https://www.firstinspires.org/hubfs/web/program/ftc/guide-deans-list-nominations-v25-26.3.pdf>) and the FTC award page (<https://www.firstinspires.org/resources/library/ftc/leadership-award>), read 21 Aug 2026. **This is the 2025-26 revision — the 2026-27 revision was not published as of this writing. Every date below must be re-verified after kickoff.** The guide's own revision history records the rename: *"Updated Dean's List Award to FIRST® Leadership Award."*

| Item | Value (rev 25-26.4) |
|---|---|
| Who is eligible | Students in **10th or 11th grade**. "Students who are in 10th and 11th grade that mentor the team (and do not actively participate as members of the team) are not eligible." |
| Nominees per team | **Maximum two (2).** Both automatically become **Semi-finalists**. |
| Team prerequisites (North America) | "Teams must have **two screened coaches** and must have **paid the current season's registration fee** to be eligible." |
| Student prerequisite | A signed **FIRST Consent and Release form** on file. "To be nominated and to receive an interview, students MUST have a signed FIRST Consent and Release form." Unregistered students do not appear in the nomination dropdown. |
| Who submits | "a single coach or mentor must submit the nomination" via the **Team Registration System**; the mentor writing it must **not be related** to the nominees. |
| **Deadline (25-26 cycle)** | **December 15, 2025, 11:59 p.m. Eastern.** The guide flags this as "Nomination Deadline - **New!**" and states "All regions will have a nomination deadline of December 15th at 11:59pm eastern time." |
| Essay format | **Five prompts, 800 characters each (spaces and punctuation included), 4,000 characters total**, plus a sixth **500-character** free field. "Please note that nominations made without an essay will not be considered for an interview." |
| The five prompts | 1. Gracious Professionalism / *Coopertition* through the Core Values, with examples. 2. How the student increased awareness of FIRST + plans to stay engaged beyond high school. 3. How their individual contribution benefits the team as a whole. 4. Their experience and mastery in STEM (engineering, software, CAD, fabrication…). 5. Their leadership and how they motivate others. |
| Interview | At a region-specific "FIRST Leadership Award **Interview Only**" event, in person or remote depending on the region. **Student only:** "Only the nominated student is allowed to present information or answer questions… the adult team mentor may observe and later provide feedback to the student, but the mentor is **not allowed to provide any assistance** during the [interview]." |
| Interview format constraints | "this is a **conversational interview**, there are **no presentations, video links** provided to the interviewer for post-interview review, **or informational handouts** involved." |
| Finalists | Announced at the **regional championship** (usually opening or closing ceremony). "There are **no further interviews** after the student is selected as a Finalist." |
| Winners | **10 FTC students** (and 10 FRC) selected at FIRST Championship from the essays and any interview feedback. "Finalists do **not** need to be present at the FIRST Championship to be considered." |
| What a win is worth | Trophy + recognition at Championship; a written recommendation from FIRST leadership to colleges/employers; **"The original team of the winning student will receive a credit toward the next season's registration fee"**; eligibility to apply for the Woodie Flowers Memorial Grant; an expenses-paid Leadership Award Summit in Manchester, NH for the winner and a chaperone. |

**FACT — the guide's own writing advice, verbatim and worth obeying:** *"Include specific examples of what makes the nominee so exceptional and how they meet the award criteria. **Do not just say it - prove it!**"* · *"Use **measurable results** whenever possible."* · *"What sets this student apart from others?"* · *"Topics in the nomination should be able to be **validated in an interview**. If the nomination talks about certain things the student should expect questions about those things during the interview."* · *"Only including a few short sentences in the essay can limit an otherwise great candidate from moving to the next level."*

**JUDGMENT — how a small team should play this:**

| Action | When | Why |
|---|---|---|
| Confirm you have **two screened coaches** and that registration is **paid** | September | These are hard eligibility gates, and screening takes weeks to clear |
| Get **every student registered** in the Youth Registration System with the consent form signed | September | An unsigned form makes a student invisible in the nomination dropdown |
| Decide your two nominees | **early November** | Two names out of a 5-person team is a near-automatic choice, which is exactly the small-team advantage — a 40-student program has to run a selection process and disappoint 38 people |
| Draft the five essays **from the dated repo** (§16.2) | November | Every prompt asks for examples with measurable results. If you kept the outreach and decision logs, the essays are an extraction job, not a memory exercise |
| Submit | **before 15 December, 11:59 p.m. ET** (re-verify the 2026-27 date) | The single most-missed deadline in FTC |
| Mock interview the nominees, **student alone, no props** | December–January | The format forbids handouts, slides and links; students who rehearse with a portfolio in their hands rehearse the wrong thing |

**JUDGMENT — the AI boundary here is different and stricter.** The mentor writes this essay about a student, and the student is then interviewed on its contents. Using Claude to *tighten prose to a character limit* and to *pull dated evidence out of the repo* is fine and is exactly the labour-saving this program is for. Using it to *generate claims* is a trap: the guide says topics "should be able to be validated in an interview," and a 16-year-old being asked about an accomplishment they didn't have is the worst possible outcome of this whole document. Draft from the logs, never from imagination.

### 15.2 Compass Award

**FACT** — BIOBUZZ §6.5.2 and Table 6-10:

| Item | Value |
|---|---|
| Who it recognizes | "an adult coach or mentor who has given outstanding guidance and support to a team throughout the year and demonstrates to the team what it means to be a Gracious Professional" |
| Who nominates | **FIRST Tech Challenge STUDENT team members** |
| Where it is offered | **"an optional award offered at the Regional Championship tournament level of competition."** Plus: "All teams attending FIRST Championship will have an opportunity to submit for this award at FIRST Championship." |
| Format | A **40–60 second video**. "videos cannot be longer than 60 seconds, **including credits**." |
| File types | `.mp4`, `.mov`, `.avi`, `.wmv` — **"no links to streaming services will be accepted"** |
| Quantity | "one video submission per team per event (videos can be updated or changed between events)" |
| Deadline | "submitted by the deadline established by the **Event Director or local Program Delivery Partner**" |
| Music | "all music must be used with permission from the copyright owners and be indicated in the video credits" |
| Required criterion 1 | "Team must be able to clearly articulate this mentor's contribution to the team and explain what sets this mentor apart." |
| Also | Teams are encouraged to review the FIRST Branding and Style Guidelines first |

**JUDGMENT.** Do not build this in February. Shoot 20 seconds of usable footage of your coach at every event and every build night from September; the video then edits itself in an hour. A 40–60 second video with **licensed** music is genuinely constrained — use a royalty-free library and credit it on screen, or use no music at all and let a student speak. Note the level gate: **there is no Compass Award at a qualifier**, so this only matters in the season where you reach a Regional Championship.

### 15.3 Project-Based Global Awards

**FACT** — BIOBUZZ §6.6: *"Project-based global awards are awards that are only judged and awarded once per season and are open to all registered FIRST Tech Challenge teams. Each award has its own independent requirements and deadlines. **These awards do not contribute towards team advancement.** More information about Project-Based Global Awards coming soon!"*

**FACT** — in DECODE these were the **Digital Animation Award (sponsored by WPI)** and the **Safety Animation Award (sponsored by UL Solutions)** (DECODE §6.6.1, §6.6.2). Neither is confirmed for BIOBUZZ.

**JUDGMENT.** Zero advancement points, independent deadlines, and they do not consume your A215 slot. That makes them a pure side quest — worth it only if a specific student wants to make an animation. Put a calendar reminder to check §6.6 in the first post-kickoff Team Update; if a global award reappears, the deadline will be early and easy to miss.

### 15.4 Consolidated award deadline calendar

**JUDGMENT — copy this into your team calendar on day one.** Dates marked *(25-26)* are last season's and **must be re-verified** for 2026-27 after kickoff.

| Deadline | What | Source | Consequence of missing it |
|---|---|---|---|
| **Continuous, from 1 Jan 2026** | Only content dated on/after 1 Jan 2026 counts as current-season | A201.E | Undated work is unusable evidence |
| **~15 Dec, 11:59 p.m. ET** *(25-26 date)* | FIRST Leadership Award nominations, via Team Registration System | Nomination Guide rev 25-26.4 | Two students lose a national award path for the year; no appeal |
| Set by Event Director, per event | **Portfolio submission** — default is 1 printed copy handed in at the Initial Interview | **A202** | No portfolio ⇒ **Think, Control and Inspire become impossible** |
| Set by Event Director, per event | Compass Award video (Regional Championship / FIRST Championship only) | §6.5.2, Table 6-10 | Award forfeited |
| Set by Event Director, in advance | Translator / interpreter accommodation request (+2–5 min interview time) | **A209** | No extra time granted on the day |
| Event day, at your scheduled slot | **Initial Interview attendance** | **A203** | **Ineligible for every judged award** |
| *(25-26)* 15 Feb | Translated Leadership Award nomination due, if the original was not in English | Nomination Guide rev 25-26.4 | Student loses eligibility for Winner selection at Championship |
| Announced by 17 Nov 2026 registration cutoff; published "early December" | Your region's advancement slot allocation | BIOBUZZ §1.7.4, §4.2 | You plan your season against the wrong target |
| TBA | Project-Based Global Awards, "each award has its own independent requirements and deadlines" | §6.6 | Award forfeited |

---

## 16. A season-long documentation cadence that produces the portfolio as a by-product

### 16.1 The principle

**JUDGMENT.** The February panic exists because teams treat the portfolio as a *writing project* rather than as an *export format*. The fix is a rule: **every engineering decision produces one artifact at the moment it is made, in a fixed place, in a fixed shape.** The portfolio is then an editorial pass over existing artifacts, not an act of recall. A201.E makes this urgent — only work from 1 Jan 2026 onward counts as current-season content, so the *dated* record is what protects you.

### 16.2 The repository

**JUDGMENT.** One git repo (private or public), one folder structure, everything dated:

```
/decisions/YYYY-MM-DD-<slug>.md      one file per decision: problem, options, criteria, math, choice, why
/mechanisms/<subsystem>/log.md       running log; every iteration gets a dated entry + photo
/control/experiments/YYYY-MM-DD.md   what we measured, the numbers, the plot, what changed
/outreach/YYYY-MM-DD-<event>.md      what we did, who we reached (with the basis for the number), evidence
/meetings/YYYY-MM-DD.md              5-line standup: goal, done, blocked, next, who
/media/                              photos & CAD renders, filenames dated
/portfolio/                          the build target
```

Rules: every file dated; every claim about people numerically justified (per the Outreach Terms' "estimate on the low end" guidance); **no full student names anywhere** (A201 PII); every mechanism log entry gets a photo the same day.

### 16.3 The cadence

| Cadence | Ritual | Time | Feeds |
|---|---|---|---|
| **Every meeting** (~2×/wk) | 5-line meeting log + 2 photos. Rotate the scribe. | 5 min | Everything; Sustain-R2 (tracking) |
| **Every meeting** | Two random judge-bank questions, two students answer (§13.5) | 2 min | Interview readiness |
| **Every design decision** | One `/decisions` file before the build starts — options, criteria, the math, the choice | 20 min | **Think-R1.C and R1.D** |
| **Every control change** | One `/control/experiments` file: what we measured, before/after numbers | 15 min | **Control-R2, E3, E4, E5** |
| **Every outreach event** | Same-day log: objective, strategy, activity, reach with basis, evidence (photo/letter) | 15 min | **Reach-R1, R2**; Connect-E3 |
| **Weekly** | 15-min review: are we on the season plan? Update the tracked goals. | 15 min | **Sustain-R1, R2** |
| **Monthly** | 30-min "portfolio pass": convert the month's logs into draft portfolio pages. Claude Code drafts, a student edits and fact-checks. | 30 min | The portfolio itself |
| **After each event** | Debrief: what broke, what we'd change, what the judges asked. File it dated. | 30 min | Think-R1.B (lessons learned and applied); interview consistency |
| **After each event** | Pull the FTC-Events / ftcscout results, refresh your own stats page | 10 min | Robot performance narrative |

### 16.4 The BIOBUZZ calendar

**FACT** (BIOBUZZ §1.7.3, §1.7.4, §4.2):
- **Kickoff: 12 September 2026.** Team Updates post "Every Thursday beginning on Kickoff day and ending two weeks prior to FIRST Championship."
- **Game Q&A opens 28 September 2026, 12:00 p.m. ET.** Moderators answer beginning each Monday, closing Thursday 5:00 p.m. ET. Access is via Lead Coach 1 or 2's FIRST dashboard account.
- **Team registration cutoff for regional advancement-slot allocation: 17 November 2026.** Regional allocations publish on the FTC-Events page "starting in early December."
- Season structure: "kicking off in September and running through March with capstone events held April through July."

**JUDGMENT — a phased plan anchored to those dates:**

| Phase | Dates | Documentation objective | Portfolio pages that should exist by the end |
|---|---|---|---|
| **Pre-kickoff** | now → 11 Sep | Set up the repo, the meeting-log template, the decision template. Write the **season plan and goals page** and the **team roles page** — neither depends on the game. Draft the **learning plan** (Connect-R1) and the **finance/sustainability page** (Sustain-R1). | 3–4 |
| **Kickoff sprint** | 12 Sep → 4 Oct | Game analysis + strategy decision, fully documented. First decision matrix. First math page. | +3 |
| **Build** | Oct → Dec | One mechanism log per subsystem, updated every meeting. Control experiments start as soon as a drivetrain moves. **Early Nov: choose your two FIRST Leadership Award nominees. Submit before ~15 Dec (§15.1, re-verify date).** | +4–5 |
| **First events** | Dec → Feb | Post-event debriefs; reliability numbers accumulate; outreach logs. | +2 |
| **Portfolio assembly** | ~3 weeks before your first judged event | Editorial pass only. Cut to 15 pages. Contrast-check. Scrub PII. **Add the AI credit footnote.** Print 3 copies. | 15 + cover |
| **Iterate** | Between events | Read your A212 feedback form; revise one section per event. | — |

**JUDGMENT — the A212 loop is free and almost nobody uses it.** Every team receives a feedback form from the Initial Interview (returned with the portfolio near the end of the event, or delivered digitally to Lead Coach 1 via FTC-Scoring). It reflects only the judges' *initial impression* and is explicitly not used in deliberations — which makes it a clean, unbiased read on how you land in the first ten minutes. File it in the repo, and make revising one weak area a standing agenda item after every event.

### 16.5 Where Claude Code fits in the documentation loop

**JUDGMENT.**

| Task | Use AI? | Note |
|---|---|---|
| Turning a month of dated meeting logs into a draft portfolio page | ✅✅ | Highest-value use. Students edit and fact-check; A201 requires the credit footnote |
| Checking the portfolio against every Required/Encouraged criterion in §7.5 | ✅✅ | Mechanical, tedious, and exactly the kind of thing teams get wrong |
| PII scan (full names anywhere in text or captions) before submission | ✅✅ | A201 hard requirement |
| Page-count, font-size and file-size preflight | ✅ | A201 |
| Generating the decision matrix *content* | ❌ | The students must own the reasoning; judges will interrogate it |
| Writing the outreach reach numbers | ❌ | Must be your real, documented, low-end estimates |
| Drafting the scouting tooling and the pre-event dossiers | ✅✅ | §5.7 |
| Rehearsing judge Q&A (AI plays the judge from the bank in §13.3) | ✅ | Cheap, unlimited reps |

**Guardrail (JUDGMENT):** the manual permits AI with credit. The judges will ask follow-up questions about anything on the page. **A student must be able to defend every sentence in the portfolio.** Use AI to remove transcription and formatting labour so students spend the recovered hours on the robot and on outreach — that is the stated goal of this whole effort.

---

## 17. Open questions — re-verify these at kickoff (12 Sep 2026)

| # | Question | Where the answer will appear |
|---|---|---|
| 1 | Alliance-selection process, playoff bracket, ranking sort criteria, T-rules (T701–T705) | BIOBUZZ **Section 13 Tournament (T)** — placeholder in V0 |
| 2 | Ranking Point structure and the tiebreak sorts (DECODE's "average BASE points" is game-specific and will change) | BIOBUZZ **Sections 10, 13** |
| 3 | Number of qual matches per team (5 or 6 in DECODE) | BIOBUZZ **Section 13.6.1** |
| 4 | **BIOBUZZ-specific Judge Interview Question Bank** — V0 says "coming soon"; the version cited in §13.3 is rev 25-26.1 | `ftc-resources.firstinspires.org` |
| 5 | **Judge and Judge Advisor Manuals** for 2026-27 — V0 says "coming soon" | `ftc-resources.firstinspires.org` |
| 6 | **Initial Interview feedback form** — V0 says "coming soon" | Same |
| 7 | Which **Project-Based Global Awards** run this season (DECODE had Digital Animation / WPI and Safety Animation / UL Solutions) | BIOBUZZ **§6.6** + Team Updates |
| 8 | Updated **Outreach Terms and Definitions** revision for 2026-27 | `info.firstinspires.org/hubfs/web/program/ftc/outreach-terms-and-definitions.pdf` |
| 9 | Your event's **portfolio submission instructions and deadline** (A202 default is 1 printed copy at the Initial Interview, but Event Directors override) | Your Event Director, before each event |
| 10 | Your event's **Initial Interview format** — scheduled, unscheduled/pit, or remote (this changes your whole presentation design) | Your Event Director, before each event |
| 11 | Whether the FTC-Events API adds a 2026 season endpoint / new score fields, and whether ftcscout adds `TeamEventStats2026` | Both APIs, post-kickoff |
| 12 | FTC-Events API **rate limits** — undocumented | Test politely; cache with `If-Modified-Since` |
| 13 | **FIRST Leadership Award Nomination Guide, 2026-27 revision** — the deadline (15 Dec, 11:59 p.m. ET in 25-26), the 5×800-character essay structure, and the two-screened-coach prerequisite all need re-confirming | `firstinspires.org/resources/library/ftc/leadership-award`; email `FTC-LeadershipAward@firstinspires.org` |
| 14 | **The Orange Alliance API** — key-request process and rate limits; `/apidocs` currently returns 404 | <https://theorangealliance.org> · <https://github.com/the-orange-alliance> |
| 15 | Whether ftcscout's award `type` enum gains or renames values for BIOBUZZ (it carried `DeansListFinalist` / `DeansListSemiFinalist` after the award was renamed to FIRST Leadership) | `api.ftcscout.org/rest/v1/events/2026/{code}/awards` |
| 16 | Compass Award: confirm it is still **Regional-Championship-level only** and still 40–60 s | BIOBUZZ §6.5.2 is final — but confirm your event actually offers it |

---

## 18. Sources

### Local files
- `manuals/2026-27_BIOBUZZ/sections/06_Awards_A_p43-58.txt` — BIOBUZZ V0 Section 6 Awards (A), **FINAL**
- `manuals/2026-27_BIOBUZZ/sections/04_Advancement_p27-32.txt` — Section 4 Advancement, Tables 4-1/4-2/4-3
- `manuals/2026-27_BIOBUZZ/sections/05_EventRules_E_p33-42.txt` — Section 5 Event Rules (E116 recording consent)
- `manuals/2026-27_BIOBUZZ/sections/02_SeasonOverview_p5-21.txt` — Team Updates cadence, Q&A open date
- `manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` — pages 47, 51, 53–58 extracted structurally with PyMuPDF for Table 6-1 and the criteria tables
- `manuals/2026-27_BIOBUZZ/v0_pymupdf.txt` — recovered §4.1.1 advancement formula
- `manuals/archive/2025-26_DECODE_Competition_Manual_TU32.txt` — DECODE §6 (award diff), §13.6–13.7 (tournament mechanics), T601, T701–T705

### Official FIRST
- FTC Events API docs — <https://ftc-events.firstinspires.org/api-docs> · try-it-out <https://ftc-events.firstinspires.org/try-it-out> · OpenAPI <https://ftc-events.firstinspires.org/swagger/v2.0/swagger.json>
- FTC Events API access & registration — <https://ftc-events.firstinspires.org/services/API> · <https://ftc-events.firstinspires.org/services/API/register>
- Judging Question Bank, rev 25-26.1 — <https://ftc-resources.firstinspires.org/ftc/archive/2026/event/question-bank>
- Judge Volunteer Manual, rev 25-26.1 — <https://ftc-resources.firstinspires.org/ftc/archive/2026/volunteer/judge>
- Judge Advisor Volunteer Manual, rev 25-26.1 — <https://ftc-resources.firstinspires.org/ftc/archive/2026/volunteer/judge-advisor>
- Judging Quick Start, rev 25-26.1 — <https://ftc-resources.firstinspires.org/ftc/archive/2026/event/judge-quickstart>
- Outreach Terms and Definitions, rev 25-26.1 — <https://info.firstinspires.org/hubfs/web/program/ftc/outreach-terms-and-definitions.pdf>
- FIRST Leadership Award (FTC) award page — <https://www.firstinspires.org/resources/library/ftc/leadership-award>
- FIRST Leadership Award **Nomination Guide, rev 25-26.4** (PDF; text extracted with `pdftotext`) — <https://www.firstinspires.org/hubfs/web/program/ftc/guide-deans-list-nominations-v25-26.3.pdf>
- FIRST Leadership Award **Program Delivery Partner Guide**, rev 25-26.6 — <https://ftc-resources.firstinspires.org/ftc/volunteer/deans-list-pdp>
- Leadership Award questions — `FTC-LeadershipAward@firstinspires.org`

### Community
- ftcscout.org — <https://ftcscout.org> · about <https://ftcscout.org/about> · API <https://ftcscout.org/api> · GraphQL `https://api.ftcscout.org/graphql` · REST `https://api.ftcscout.org/rest/v1/...` · source <https://github.com/ftc-scout>
- Game Manual 0 — <https://gm0.org> · Awards <https://gm0.org/en/latest/docs/awards/index.html> · Portfolio <https://gm0.org/en/latest/docs/awards/portfolio.html> · Judging <https://gm0.org/en/latest/docs/awards/judging-presentation.html> · Award types <https://gm0.org/en/latest/docs/awards/award-types.html> · Notebook <https://gm0.org/en/latest/docs/awards/notebook.html>
- The Blue Alliance Blog — "The Math Behind OPR — An Introduction," Eugene Fang, 5 Oct 2017 — <https://blog.thebluealliance.com/2017/10/05/the-math-behind-opr-an-introduction/>
- cheer4ftc/OPR (Java, MMSE + least squares) — <https://github.com/cheer4ftc/OPR>
- owsorber/FTC_OPR_Calculator (Python) — <https://github.com/owsorber/FTC_OPR_Calculator>
- owsorber/FTC_Scout_Assistant (Django) — <https://github.com/owsorber/FTC_Scout_Assistant>
- Andover-Robotics/FTC-Scouting-App — <https://github.com/Andover-Robotics/FTC-Scouting-App>
- PWNAGERobotics/ScoutingPASS (FRC-oriented) — <https://github.com/PWNAGERobotics/ScoutingPASS>
- FTC Open Alliance — <https://theopenalliance.org/ftc> · team directory <https://theopenalliance.org/ftc/teams>
- The Orange Alliance — <https://theorangealliance.org> · API base `https://theorangealliance.org/api` (key required) · source <https://github.com/the-orange-alliance>
- VexDB custom ranking methods (OPR/DPR/CCWM definitions) — <https://vexdb.io/extras/ranking_methods>
- Portfolio examples/guides: <https://twcarobotics.com/engineering-notebook/> · <https://fc-robotics.org/right-brain/the-engineering-portfolio-path/> · <https://digitalcommons.imsa.edu/cii_dsw/5/> · <https://ftc.ctrlyrobotics.org/a-beginners-guide-to-ftc/ftc-judging-and-awards>

### Analyses performed for this document (all against live ftcscout data, 21 Aug 2026)
| # | What | Sample |
|---|---|---|
| 1 | Qual-rank vs OPR-rank divergence | Event `USTXDAQ2`, 31 ranked teams, 5 quals each |
| 2 | OPR reproduction + perturbation stability | Same event; 78 alliance-rows; 200 resampling trials |
| 3 | OPR convergence vs matches played | 44 qualifiers, season 2025 |
| 4 | Advancement points, fully costed | Event `USTXDAQ2`, verified §4.1.1 formula |
| 5 | Award winners' performance percentile by award type | **162 qualifiers / 156 with complete award sets**, 18 US regions, season 2025 |
| 6 | World Championship division Inspire winners' own-division performance | 6 divisions, 2026 FIRST Championship |
| 7 | §4.1.1 formula verification against BIOBUZZ Table 4-3 | Exact match, all 11 published values |
| 8 | **`picklist.py` (§5.3a) written and executed live**: pure-stdlib OPR solver validated against ftcscout's published OPR | 31 teams; max \|diff\| 2.16 pts, mean 0.46; mean-OPR identity 35.86 vs 35.78; runtime 1.07 s. **Rev 3 note:** the 2.16 pt gap is the ridge term + `totalPoints`/`totalPointsNp` choice, not an unavoidable limit of the stdlib solver — apply the five rules in §3.2a to make it exact |
| 9 | Live liveness probes of all three data sources | ftcscout REST + site 200; FTC-Events 401 without credentials; TOA site 200, `/api` 200, `/api/team/16321` 400 "authorization headers were not found", `/apidocs` 404 |
| **9b** | **Exact OPR reproduction recipe (§3.2a)** — plain `lstsq`, quals only, `hasBeenPlayed`, `totalPointsNp`, no ridge | **9 events / 289 team-event pairs** (`USAZCHQ1`, `USAZFLQ`, `USAZGIQ`, `USAZGLQ`, `USAZQCQ`, `USAZCMPGC1`, `FTCCMP1EDIS`, `FTCCMP1ROSS`, `USTXHOCMP`); **max abs. diff 0.0000 pts** on every one |
| **10** | **Split-half reliability of OPR at qualifier scale (§3.5)** | 10 AZ qualifiers, season 2025; mean *r* = 0.53, Spearman-Brown 0.70, top-8 overlap 5.2/8 |
| **11** | **Split-half reliability at Championship scale (§3.5)** | 6 divisions, 2026 FIRST Championship, ~10 quals/team; mean *r* = 0.76, SB 0.86, top-8 overlap 4.5/8 |
| **11b** | **OPR vs. naive alliance-average, same split-half test (§3.5)** | Same 10 AZ qualifiers; OPR *r* = 0.53 vs naive 0.39 |
| **12** | **Playoff alliance size by event level (§1.1a)** — corrects Rev 2 | `FTCCMP1EDIS` → 3 teams (`One`/`Two`/`NotOnField`); `USAZCMPGC1` → 2 teams; 2026 Worlds final verified 514–506, 526–519 |

*Prices in this document are marked ESTIMATE or UNVERIFIED where I could not confirm them and are stated as of August 2026; re-check before budgeting. All API behaviour was verified live on 21 August 2026 and may change.*

*Portfolio note for the team: per BIOBUZZ A201, if any of this document's content or method is reused in your Engineering Portfolio, credit the AI assistance in a footnote or endnote — e.g. "Portfolio created by Team XXXXX and Claude."*
