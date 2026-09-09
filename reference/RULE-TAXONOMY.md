# FTC Rule-Numbering Taxonomy — BIOBUZZ 2026-27 Reference

**Purpose:** everything needed to read, cite, grep and diff FTC rule IDs on kickoff day (2026-09-12).
**Built from:** BIOBUZZ Pre-Season V0 (`BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf`, 93 pp.), DECODE 2025-26 (TU32 / Section 11 V15), INTO THE DEEP 2024-25 (V14), and the 2015-16 → 2023-24 Game Manual Part 1 / Part 2 archive.
**Verified:** 2026-08-21 against the local corpus.

### Confidence legend

| Tag | Meaning |
|---|---|
| **[V0]** | CONFIRMED-FOR-BIOBUZZ — present in the BIOBUZZ V0 PDF. Safe to cite. |
| **[HIST]** | HISTORICAL-PATTERN — true in DECODE and/or ITD, **not** yet confirmed for BIOBUZZ. |
| **[SPEC]** | SPECULATION — inference only. Do not cite to a REFEREE. |
| UNVERIFIED | Could not confirm from the corpus. |

---

## 0. Executive corrections — read these first

| # | Claim you may be carrying | Reality |
|---|---|---|
| 1 | "V0 has 113 rules." | **V0 has exactly 109 numbered rules.** Verified three independent ways (regex sweep of `v0_pymupdf.txt`; PDF span+colour extraction via pymupdf; the awk recogniser in §5.3 — all return 109). `C270` in `R708.A` is a **Logitech webcam model**, not a rule; naive `\b[A-Z][0-9]{3}\b` sweeps report 110 and silently count it. **[V0]** |
| 2 | "Evergreen = asterisk *after* the rule id." | Half-right, and the ingest script's regex is broken (§5). The manual's own definition: headline presented in "bold green text with a leading asterisk" — the marker is a **leading asterisk on the *headline*** plus **bold green `#06844B`**. The asterisk is frequently typeset in a **separate black non-bold span**, so colour-only *or* span-only detection both miss rules. And `BIOBUZZ_V0_layout.txt` (`pdftotext -layout`) **mis-pairs rule IDs with rule text** — do not use it for this. **[V0]** V0 p.18, §1.7.1 |
| 3 | "Section 14 League Play (L) is a placeholder." | **False.** V0 p.90 §14 is fully written prose. It contains **zero L-rules** — and neither DECODE nor ITD ever had a single `L###` rule. **[V0]** |
| 4 | "Placeholder sections are 8, 9, 10, 11, 13, 14." | The correct list is **8, 9, 10, 11, 13, 15**. Section 15 *FIRST* Championship (C) *is* a placeholder (V0 p.91); Section 14 is not. **[V0]** |
| 5 | "Evergreen rules keep their numbers, so DECODE numbers still apply." | **36 evergreen rules were renumbered between DECODE and BIOBUZZ V0**, and several moved across sections entirely (§7). Every DECODE-era citation — veteran memory, forum post, last year's Q&A — is presumed stale until checked. |
| 6 | "V0's rules are almost all evergreen, so the manual is settled." | **108 of 109 V0 rules are marked evergreen; exactly one (`R105`) is game-specific.** That ratio is an artefact: every genuinely game-specific rule lives in Sections 8–11 / 13 / 15, which are still placeholders. |
| 7 | "V0 tells you the penalty vocabulary." | It does not. V0 contains **zero `Violation:` lines**, and the strings `MINOR FOUL`, `MAJOR FOUL`, `YELLOW CARD`, `DISQUALIFIED`, `MOMENTARY`, `CONTINUOUS`, `EGREGIOUS` appear **nowhere** in it (§8). All of that arrives on 2026-09-12. **[V0]** |

---

## 1. Prefix taxonomy — the letter *is* the section

The manual states it outright: the letter indicates the section the rule is published in; the following digit is
the subsection; the final digits are the rule's position within that subsection. **[V0]** V0 p.17, §1.7.1,
"Figure 1-3 Rule numbering method". (Identical wording in ITD V14 p.10 and DECODE. **[HIST]**)

| Prefix | Section | Domain | In BIOBUZZ V0? | V0 count |
|---|---|---|---|---|
| **I** | 3 Competition Eligibility and Inspection (I) | Registration, event check-in, ROBOT inspection & re-inspection | Yes — final | 7 |
| **E** | 5 Event Rules (E) | Conduct at the venue: safety, pits, wireless, carts, ceremonies | Yes — final | 35 |
| **A** | 6 Awards (A) | PORTFOLIO, judging interviews, award eligibility | Yes — final | 15 |
| **G** | 11 Game Rules (G) | Gameplay: conduct, pre-MATCH, AUTO/TELEOP, ROBOT & human interaction | **No — placeholder** | 0 |
| **R** | 12 ROBOT Construction Rules (R) | Legal parts, sizing, actuators, power, control, OPERATOR CONSOLE | Yes — final | 52 |
| **T** | 13 Tournament (T) | REFEREE authority, replays, Question Box, qualification, playoffs, dual division | **No — placeholder** | 0 |
| **L** | 14 League Play Tournaments (L) | League Meets, League Tournament ranking & advancement | Section written, **no rules** | 0 |
| **C** | 15 *FIRST* Championship (C) | Championship-only modifications (awards, 3-ROBOT ALLIANCES, da Vinci) | **No — placeholder** | 0 |

**Total confirmed for BIOBUZZ: 109. [V0]**

> **The `L` anomaly.** `L` is declared in the legend in V0, DECODE *and* ITD, yet **no `L###` rule exists in any of
> the three** (`grep -E '\bL[0-9]{3}\b'` returns nothing across all three manuals). Section 14 governs League Play
> entirely through prose that cross-references §13.6, Table 13-1 and §10.6.1. **[V0][HIST]**
> Expect **zero L-rules at kickoff. [SPEC]**

> **Note the forward references in V0 §14** (p.90): it cites "Section 13.6 Qualification MATCHES",
> "Table 13-1" and "Section 10.6.1 YELLOW and RED CARDS" — all of which are inside placeholder sections. Those
> citations are already written against **DECODE's exact subsection numbering**, which is strong evidence that
> BIOBUZZ Sections 10 and 13 will reuse DECODE's subsection layout, and therefore DECODE's T-blocks. **[SPEC]**

> **False-positive traps when sweeping `[A-Z][0-9]{3}`:** `C270` and `C920` (Logitech webcams), `F310`
> (Logitech gamepad, pre-2024 manuals), `Z87` (safety-glasses standard), `G5` / `E4` / `E5` (Motorola phone
> models). Always anchor to `^` **and** restrict the class to `[IEARGTLC]`.

---

## 2. Hundreds-block structure — the block **is** the subsection number

`R6`**07** = Section 12, sub**section 12.6**, **7th** rule in it. The mapping is mechanical, not thematic, and it
has a sharp consequence: **inserting or deleting a subsection shifts an entire hundreds-block, even for evergreen
rules.**

Proof from the corpus: ITD §13.5 was *Qualification MATCHES* (`T501`). DECODE inserted a new §13.5 *Practice
MATCHES*, pushing Qualification to §13.6 — so ITD `T501` → DECODE `T601`, ITD's playoff `T6xx` → DECODE `T7xx`,
and ITD's dual-division `T7xx` → DECODE `T8xx`. Nothing about those rules changed; the *heading above them* did.
**[HIST]**

### 2.1 BIOBUZZ V0 blocks (confirmed)

| Block | Subsection | Topic | V0 rules in block | n |
|---|---|---|---|---|
| **I1xx** | 3.1 | Team Eligibility Rules | I101–I103 | 3 |
| *I2xx* | 3.2 | Awards Eligibility Rules | *prose only — points at A201 / A203 / A213 / A214* | 0 |
| **I3xx** | 3.3 | MATCH Eligibility Rules (inspection) | I301–I304 | 4 |
| **E1xx** | 5.1 | General Rules | E101–E118 | 18 |
| *E2xx* | 5.2 | Machine Shops & Host Team Build Spaces | *prose only* | 0 |
| **E3xx** | 5.3 | Wireless Rules | E301–E302 | 2 |
| *E4xx* | 5.4 | Load-In | *prose only* | 0 |
| **E5xx** | 5.5 | Pits | E501–E511 | 11 |
| **E6xx** | 5.6 | ROBOT Carts | E601 | 1 |
| **E7xx** | 5.7 | Ceremonies | E701–E703 | 3 |
| *A1xx* | 6.1 | Team Judged Awards Overview & Schedule | *prose + tables only* | 0 |
| **A2xx** | 6.2 | Team Judged Award Rules | A201–A215 | 15 |
| *A3xx–A6xx* | 6.3–6.6 | Award descriptions; ALLIANCE / Individual / Global awards | *prose only* | 0 |
| **R1xx** | 12.1 | General ROBOT Design — ownership, 18-in cube, weight, expansion | R101–R105 | 5 |
| **R2xx** | 12.2 | Fair Play & Damage Prevention | R201–R204 | 4 |
| **R3xx** | 12.3 | Fabrication — COTS, raw materials, DoF, year-to-year reuse | R301–R305 | 5 |
| **R4xx** | 12.4 | ROBOT SIGN Rules | R401–R403 | 3 |
| **R5xx** | 12.5 | Motors & Actuators | R501–R506 | 6 |
| **R6xx** | 12.6 | Power Distribution | R601–R613 | 13 |
| **R7xx** | 12.7 | Control, Command & Signals System | R701–R711 | 11 |
| **R8xx** | 12.8 | Pneumatic Systems & Airflow Devices | R801 | 1 |
| **R9xx** | 12.9 | OPERATOR CONSOLE | R901–R904 | 4 |

**[V0]** Subsection titles from V0 Contents pp.2–3 and the orange `Roboto-Bold 13 pt #ED7D31` headings.
Sections 3.2, 5.2, 5.4 and 6.1/6.3–6.6 are deliberately rule-free prose — a **gap in the numbering is not a
missing rule**.

### 2.2 G / T / C blocks — DECODE's map, as the kickoff baseline

| Block | DECODE subsection | Topic | DECODE rules | n |
|---|---|---|---|---|
| G1xx | 11.1 | Personal Safety | G101–G102 | 2 |
| G2xx | 11.2 | Conduct (GP, throwing MATCHES, egregious violations) | G201–G212 | 12 |
| G3xx | 11.3 | Pre-MATCH (be prompt, FIELD setup, OpMode selection) | G301–G305 | 5 |
| G4xx | 11.4 | In-MATCH — 11.4.1 AUTO → 11.4.6 Human, **all one block** | G401–G434 | 34 |
| *G5xx* | *(ITD §11.5 Post-MATCH — deleted in DECODE)* | Post-MATCH | ITD G501–G502 | 0 |
| T2xx | 13.2 | General Tournament Rules | T201–T207 | 7 |
| T3xx | 13.3 | MATCH Replays | T301–T302 | 2 |
| T4xx | 13.4 | Question Box | T401–T403 | 3 |
| *T5xx* | 13.5 Practice MATCHES | — | *none* | 0 |
| T6xx | 13.6 | Qualification MATCHES | T601 | 1 |
| T7xx | 13.7 | Playoff MATCHES | T701–T705 | 5 |
| T8xx | 13.8 | Dual Division Events | T801–T803 | 3 |
| C3xx | 15.3 | 3-ROBOT ALLIANCES | C301 | 1 |
| C5xx | 15.5 | *FIRST* Championship Playoffs | C501 | 1 |

**[HIST]** DECODE Contents pp.4–5 + PDF extraction. Note `G1xx` is *Personal Safety*, **not** a general block:
`G101` is "humans stay off the FIELD", not a catch-all conduct rule. The **entire in-MATCH rulebook is one flat
`G4xx` block of ~34 rules**, subdivided only by 11.4.x headings — so `G4xx` numbers are the least stable in the
manual and the most likely to shift under Team Updates.

---

## 3. What is ABSENT from V0 and therefore lands at kickoff

| Prefix | V0 | DECODE | ITD | Kickoff prediction |
|---|---|---|---|---|
| **G** | **0** | 53 | 53 | **~50–55 rules**, blocks `G1xx`–`G4xx` (a `G5xx` Post-MATCH block returns only if §11.5 is reinstated). Expect ~30 % game-specific/orange: DECODE 16/53, ITD 15/53. **[SPEC]** |
| **T** | **0** | 21 | 20 | **~20 rules**, blocks `T2xx`–`T8xx`, essentially all evergreen (DECODE 21/21). **[SPEC]** |
| **C** | **0** | **2** (`C301`, `C501`) | **1** (`C301`) | **2–3 rules** in `C3xx` / `C5xx`. **[SPEC]** |
| **L** | 0 | 0 | 0 | **0.** **[SPEC]** |
| **I** | 7 | 11 | 10 | V0 already consolidated DECODE's 11 into 7 (§7). Small chance an inspection rule returns once the game exists. |
| **E / A / R** | 35 / 15 / 52 | 39 / 15 / 73 | 39 / 14 / **72** (a naive sweep of ITD V14 returns 73 because the manual contains a typo, `R418`, in a recap-video pointer on p.≈101 — no such rule exists) | R shrank 21 vs DECODE by **consolidation, not deletion** (§7). At kickoff expect only `R105`-style expansion detail to change. |

**Rough total at kickoff: 109 + ~75 ≈ 185 rules. [SPEC]** (DECODE shipped 214, ITD 209; the BIOBUZZ R-section
consolidation explains the gap.)

### 3.1 The one explicit placeholder cross-reference in V0

V0 p.68, inside the orange note attached to `R201`, contains the literal token **`GXXX`** where a game-rule
number will be filled in at kickoff. It is styled as a live cross-reference (`Consolas`, `#4472C4`) — i.e. FIRST's
own editing placeholder. **[V0]**

```bash
grep -n 'GXXX\|TXXX\|LXXX' "manuals/2026-27_BIOBUZZ/v0_pymupdf.txt"
#  -> 1 hit: line 2697,  "violations of this rule and GXXX."
```

On kickoff day re-run that grep against the new manual: **any surviving `XXX` token is an unresolved editing
error and a legitimate day-one Q&A question.**
---

## 4. The "evergreen" convention — what it actually is

### 4.1 FIRST's own definition

V0 §1.7.1 (p.18) defines two headline formats. Evergreen rules — those "expected to be present each season with
only their specific details changing" — get a headline in **bold green text with a leading asterisk**. All other
rule headlines use **bold orange text** (no asterisk). The manual also notes evergreen rules "start their
respective section, so their rule number is less likely to change from season to season" — a claim §7 shows is
only loosely true. Identical wording appears in ITD V14 p.10 and DECODE. **[V0][HIST]**

Critically, evergreen means **the rule's subject survives**, not that its text is frozen: FIRST explicitly
reserves the right to change game terms and numeric details inside an evergreen rule (their own examples:
changing ROBOT expansion specifics, or the allowed motor count). **An evergreen rule is not a rule you can skip
reading.**

### 4.2 The actual marker in the PDF — three signals, only one of them reliable alone

| Signal | Value in V0 & DECODE | Reliable alone? |
|---|---|---|
| **Headline font colour** | `#06844B` (green) for evergreen; `#ED7D31` (orange) for game-specific | **Yes** — the ground truth |
| Headline font | `Roboto-Bold`, 11 pt, starting at x ≈ 72 pt (rule id sits at x ≈ 36 pt) | Yes, combined with colour |
| **Leading `*`** | Present on every evergreen headline in the extracted text stream | **Yes in extracted text**, but see the trap below |

**The trap:** the asterisk is *sometimes* its own span in `Roboto-Regular`, **black**, not part of the green bold
run. In V0 this happens for `R201` and `R501`; in ITD for `T203` and `T204`. A colour-based extractor that
concatenates only green spans therefore drops the `*` — and any code that keys on "green span begins with `*`"
will misclassify those rules. Conversely, a text-only extractor works fine, because the asterisk lands in the
text stream regardless of which span carries it.

Between the rule id and the headline there is also an `Arial-BoldMT` **space** span (colour `#000000`). Naive
"first bold span after the id" logic latches onto that spacer and reports colour `0x000000` for every rule.

### 4.3 Ground truth for BIOBUZZ V0

| | Count |
|---|---|
| Rules with green (`#06844B`) headline = **evergreen** | **108** |
| Rules with orange (`#ED7D31`) headline = **game-specific** | **1** (`R105`, p.68) |
| Total | **109** |

Cross-check: exactly **112 green `Roboto-Bold` 11 pt spans** exist in V0 (some headlines split across two spans)
and exactly **one** orange bold 11 pt rule headline. The other orange bold text in V0 is the Competition
Integrity Contract headings (pp.14–16) and the phrase "bold orange text" in the §1.7.1 legend itself, which is
self-demonstratingly set in orange. **[V0]**

| Manual | Rules | Evergreen | Game-specific |
|---|---|---|---|
| BIOBUZZ V0 | 109 | 108 | **1** |
| DECODE (TU32) | 214 | 197 | 17 |
| INTO THE DEEP (V14) | 209 | 193 | 16 |

**[V0][HIST]** The BIOBUZZ 1/109 ratio is an artefact of the placeholders — 16 of DECODE's 17 game-specific rules
are `G4xx` in-MATCH rules plus `C501`; only `R105` lives outside Section 11/15.

---

## 5. Extraction recipes — and the ingest-script fix

### 5.1 Which text extraction to trust

Tested by asking each extraction "which rules carry a leading `*` on their headline?" and scoring against the
108-rule colour-based ground truth:

| Source | Evergreen found | Verdict |
|---|---|---|
| `BIOBUZZ_V0_raw.txt` (`pdftotext`, no flags) | 15 / 108 | **Useless** — collapses runs of rule ids onto one line (`E103 E104 E105`) |
| `BIOBUZZ_V0_layout.txt` (`pdftotext -layout`) | 68 / 108 | **Actively dangerous** — see 5.2 |
| `v0_pymupdf.txt` (`page.get_text()`) | 101 / 108 with a one-line regex; **109/109 with the awk in 5.3** | **Use this** |
| PDF spans + colour (pymupdf `get_text("dict")`) | 109 / 109 | Ground truth; use for the authoritative pass |

### 5.2 Why `pdftotext -layout` must not be used for rule parsing

The rule id sits in a narrow left column and the rule text in a wide right column. When a rule's text wraps,
`-layout` pairs the **next rule's id** with the **previous rule's continuation text**. Real output from
`BIOBUZZ_V0_layout.txt`:

```
1220:E103  *Children with adults, please. Children under 12 must be accompanied in the pits by an adult at
1221:E104  all times.
1222:E105
1224:E106  floors, walls, and railings, in any way. This includes littering with team giveaways including
```

`E104` is *Respect the venue*, not "all times." Any pipeline that reads a rule's text from the `-layout` file
will attribute text to the wrong rule. `-layout` remains fine for **tables** (Table 12-1 motors, Table 12-8 wire
sizes) — just not for rule/headline pairing.

### 5.3 Corrected evergreen detector

The ingest script currently uses:

```bash
grep -E '^[IEARGTLC][0-9]{3}[[:space:]]+\*' "$WORK/full_layout.txt"        # evergreen  -> finds 68 of 108
grep -E '^[IEARGTLC][0-9]{3}' "$WORK/full_layout.txt" | grep -v '\*'       # game-spec  -> 26 FALSE POSITIVES
```

Both numbers are wrong, for three reasons: (a) it reads the `-layout` file (5.2); (b) some rule ids are indented,
so `^` misses them (`A202`); (c) an id alone on a line is scored "game-specific" when the asterisk is simply on
the following line. **Replace with a pymupdf text extract plus this two-line-aware awk:**

```bash
# 1. extract text with pymupdf, not pdftotext
python -c "import pymupdf,io,sys; d=pymupdf.open(sys.argv[1]); \
io.open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(p.get_text() for p in d))" \
  "$PDF" "$WORK/full_pymupdf.txt"

# 2. classify
awk '
/^[IEARGTLC][0-9]{3}[ \t]*$/          { id=$0; sub(/[ \t]+$/,"",id); getline n;
                                        print id "\t" (n ~ /^[ \t]*\*/ ? "EVERGREEN" : "GAMESPEC"); next }
/^[IEARGTLC][0-9]{3}[ \t]+\*/         { print substr($0,1,4) "\tEVERGREEN"; next }
/^[IEARGTLC][0-9]{3}[ \t]+[A-Za-z"(]/ { print substr($0,1,4) "\tGAMESPEC" }
' "$WORK/full_pymupdf.txt" | sort -u \
| awk -F'\t' '{k=$1; if(!(k in seen) || $2=="EVERGREEN") seen[k]=$2} END{for(k in seen) print k"\t"seen[k]}' \
| sort > "$WORK/rules_CLASSIFIED.tsv"
```

Validation of exactly this recipe:

| Manual | Rules found | Evergreen | Game-specific | Errors |
|---|---|---|---|---|
| BIOBUZZ V0 | **109** | 108 | `R105` | none — `C270` correctly excluded (mid-line) |
| DECODE TU32 | 214 | 197 | 17 (matches colour truth exactly) | the final de-dup pass is what removes a `T206` cross-reference false positive |

### 5.4 Authoritative colour-based pass (use this to settle disputes)

```python
import pymupdf, re
GREEN, ORANGE = 0x06844B, 0xED7D31
pat = re.compile(r'^[IEARGTLC]\d{3}$')
doc = pymupdf.open(PDF)
for pno, page in enumerate(doc, 1):
    spans = [s for b in page.get_text("dict")["blocks"] if b["type"] == 0
               for l in b["lines"] for s in l["spans"] if s["text"].strip()]
    spans.sort(key=lambda s: (round(s["bbox"][1], 1), s["bbox"][0]))
    for i, s in enumerate(spans):
        if not (pat.match(s["text"].strip()) and "Bold" in s["font"]
                and s["bbox"][0] < 70 and s["size"] >= 10):
            continue                       # x<70 rejects in-text cross-references
        head, col = "", None
        for u in spans[i+1:i+12]:          # skip the Arial-BoldMT spacer span
            if "Bold" in u["font"] and u["color"] in (GREEN, ORANGE) and u["size"] >= 10:
                col = col or u["color"]
                if u["color"] == col: head += u["text"]
                else: break
            elif head: break
        print(s["text"].strip(), pno,
              "EVERGREEN" if col == GREEN else "GAME-SPECIFIC", head.strip())
```

### 5.5 Kickoff-day grep cookbook

```bash
PY=manuals/2026-27_BIOBUZZ/ingest_V1/full_pymupdf.txt

# every rule id actually defined (not cross-references), de-noised
awk '/^[IEARGTLC][0-9]{3}([ \t]|$)/{print substr($0,1,4)}' "$PY" | sort -u

# the new game rules only
awk '/^G[0-9]{3}([ \t]|$)/{print substr($0,1,4)}' "$PY" | sort -u | wc -l

# every enforcement clause, with its penalty
grep -nE '^Violation[s]?:' "$PY"

# the game-specific (orange) rules = highest review priority
grep GAMESPEC "$WORK/rules_CLASSIFIED.tsv"

# rules that moved: V0 id present, headline different
diff <(sort "$WORK/rules_v0_headlines.tsv") <(sort "$WORK/rules_v1_headlines.tsv")

# unresolved editing placeholders
grep -nE '\b[GTLCRIEA]XXX\b' "$PY"
```
---

## 6. Complete BIOBUZZ V0 rule inventory — all 109 rules

Paraphrases are mine, condensed from the rule body (not FIRST's headline text). **EG** = evergreen (green
headline + leading asterisk). Page = V0 PDF page. **[V0] throughout.**

### 6.1 Section 3 — Competition Eligibility and Inspection (I) · 7 rules

| Rule | Sub | p. | Paraphrase | EG |
|---|---|---|---|---|
| I101 | 3.1 | 22 | Team must be registered and "competition ready" — registration, fees, 2 YPP-screened Lead Coaches (North America), all youth registered — to earn MATCH points or be award-eligible. | ✔ |
| I102 | 3.1 | 22 | An adult must check in at Pit Admin no later than 45 min before Qualification MATCHES; at least one STUDENT must be on site first. | ✔ |
| I103 | 3.1 | 23 | At least one — preferably two — responsible adults present for the entire event. | ✔ |
| I301 | 3.3 | 24 | Bring the complete ROBOT + OPERATOR CONSOLE with every COMPONENT (including decoration) that will be used in MATCHES; nothing un-inspected may be added later. | ✔ |
| I302 | 3.3 | 24 | Electronics counts (motors, servos, Android devices) are summed across **all** configurations, not per configuration. | ✔ |
| I303 | 3.3 | 25 | Request re-inspection for changes that could break compliance, or when the Head REFEREE/FTA asks; a listed set of minor changes is exempt. | ✔ |
| I304 | 3.3 | 25 | Re-inspection may not be used to circumvent any other rule. | ✔ |

### 6.2 Section 5 — Event Rules (E) · 35 rules

> Enforcement for this whole section is the **Universal Violation Note** (p.33), not per-rule Violation lines — see §8.2.

| Rule | Sub | p. | Paraphrase | EG |
|---|---|---|---|---|
| E101 | 5.1 | 33 | Personal safety practices, incl. ANSI/UL/CE/AS-NZS/CSA-rated eye protection in specified areas (10-minute grace period on entering the venue). | ✔ |
| E102 | 5.1 | 34 | Be respectful; uncivil behaviour toward any participant is not tolerated; examples enumerated. | ✔ |
| E103 | 5.1 | 34 | Children under 12 must be accompanied by an adult in the pits at all times. | ✔ |
| E104 | 5.1 | 34 | Do not damage the venue; includes littering with team giveaways (candy, flyers, stickers) or items thrown from the stands. | ✔ |
| E105 | 5.1 | 34 | Competition FIELD, practice FIELD and inspection are for teams registered at that event only, unless pre-approved. | ✔ |
| E106 | 5.1 | 34 | Practise only in your pit, designated practice areas, or a Practice MATCH; no private practice rigs set up outside the pit. | ✔ |
| E107 | 5.1 | 35 | FABRICATED ITEMS may only be produced in listed places: own pit, another team's pit with permission, in the MATCH/practice queue, or designated areas. | ✔ |
| E108 | 5.1 | 35 | Prohibited items list: skateboards, hoverboards, drones, bottled gas, noisemakers, scooters (accommodations excepted), bright-light items, etc. | ✔ |
| E109 | 5.1 | 35 | Do not arrange venue power/internet/phone service, or use event-reserved internet. | ✔ |
| E110 | 5.1 | 35 | No sales at an event (raffle tickets, food, merch, drinks) unless the Event Director allows. | ✔ |
| E111 | 5.1 | 35 | No live bands in the audience; no loud music. | ✔ |
| E112 | 5.1 | 35 | Hang banners considerately: don't cover others' signs, share space, don't block spectator views, get ED permission outside your pit. | ✔ |
| E113 | 5.1 | 36 | Flags/flagpoles used around the FIELD must be reasonable — guideline < 3 ft × 5 ft and < 2 lb. | ✔ |
| E114 | 5.1 | 36 | No firearms or weapons, including realistic props; law-enforcement and venue security exempt. | ✔ |
| E115 | 5.1 | 36 | Practice-FIELD access requires a completed initial full inspection (applies only at events without scheduled inspection times). | ✔ |
| E116 | 5.1 | 36 | Do not record anyone at the event without their consent; staff and volunteers may decline and withdraw from a recorded interaction. | ✔ |
| E117 | 5.1 | 36 | One inspected ROBOT per team per event; teams may not compete at concurrent events. | ✔ |
| E118 | 5.1 | 37 | No saving or designating seats; no banners/roping to reserve seating (event staff will remove them). | ✔ |
| E301 | 5.3 | 37 | Teams may not run their own Wi-Fi, Bluetooth, or any 2.4/5 GHz comms in the venue — cellular hotspots included. | ✔ |
| E302 | 5.3 | 37 | No interfering with, or connecting to, another team's or FIRST's wireless network without permission; report vulnerabilities to the FTA/ED. | ✔ |
| E501 | 5.5 | 38 | No pit access outside designated pit hours. | ✔ |
| E502 | 5.5 | 38 | Pit setup must be self-contained in the assigned space; no running power/internet lines elsewhere, no swapping pits. | ✔ |
| E503 | 5.5 | 38 | Keep aisles and exit pathways clear. | ✔ |
| E504 | 5.5 | 38 | Open flames and spark-throwing tools generally prohibited; the Event Director may add restrictions. | ✔ |
| E505 | 5.5 | 39 | Only small benchtop machinery (one-person liftable) in pits; floor-standing power tools prohibited. | ✔ |
| E506 | 5.5 | 39 | No brazing or welding. | ✔ |
| E507 | 5.5 | 39 | Soldering by electric iron/gun only. | ✔ |
| E508 | 5.5 | 39 | No pit structure that bears human weight or stores items overhead; must not block fire sprinklers. | ✔ |
| E509 | 5.5 | 39 | Aerosols and noxious-fume chemicals only in approved areas (some venues allow none). | ✔ |
| E510 | 5.5 | 39 | No heating or cooling ROBOT parts above/below ambient venue temperature to gain an advantage. | ✔ |
| E511 | 5.5 | 40 | Charge batteries safely: manufacturer-recommended rate, charger ≤ 3 A average channel current, safe connectors. | ✔ |
| E601 | 5.6 | 40 | Carts must be controllable, safe, fit through a 30-in door, stay in the pit when unused, and carry no sound systems. | ✔ |
| E701 | 5.7 | 41 | During non-playoff ceremonies: no power tools, no loud hand tools, no shouting in the pits. | ✔ |
| E702 | 5.7 | 41 | Max 5 team members in the pits during non-playoff ceremonies; at least 1 representative must observe. | ✔ |
| E703 | 5.7 | 41 | Remain silent and non-disruptive during national anthems; abstention from traditional observance is a right. | ✔ |

### 6.3 Section 6 — Awards (A) · 15 rules

| Rule | Sub | p. | Paraphrase | EG |
|---|---|---|---|---|
| A201 | 6.2 | 48 | The team PORTFOLIO is the **only** content JUDGES will collect for deliberations; format limits enumerated. | ✔ |
| A202 | 6.2 | 49 | PORTFOLIO must be submitted on time and as the Event Director instructs (default: 1 printed copy at check-in). | ✔ |
| A203 | 6.2 | 49 | Participation in the Initial Interview is required for **any** judged award. | ✔ |
| A204 | 6.2 | 49 | Bring ≥ 2 STUDENT representatives, a PORTFOLIO copy, and show-and-tell items to the Initial Interview. | ✔ |
| A205 | 6.2 | 49 | Every team is scheduled the same Initial Interview length — at least 10 minutes. | ✔ |
| A206 | 6.2 | 50 | The timer starts once the team begins (after JUDGE introductions); slow starts get a warning, then the clock runs regardless. | ✔ |
| A207 | 6.2 | 50 | The first 5 minutes are the team's uninterrupted prepared presentation; the team may end it early to start Q&A. | ✔ |
| A208 | 6.2 | 50 | One adult may attend the judging session as a silent observer. | ✔ |
| A209 | 6.2 | 50 | Translator / sign-language / adaptive-technology accommodations are provided on notice. | ✔ |
| A210 | 6.2 | 50 | No photo, video or audio recording during the Initial Interview — on top of E116. | ✔ |
| A211 | 6.2 | 51 | The number of awards given scales with checked-in team count (Table 6-1); only those awards are advancement-points-eligible. | ✔ |
| A212 | 6.2 | 52 | All teams receive Initial Interview feedback; the feedback form is not used in deliberations. | ✔ |
| A213 | 6.2 | 52 | Inspire Award (1st/2nd/3rd) eligibility only within the team's HOME REGION; Championship and Premier events excepted. | ✔ |
| A214 | 6.2 | 52 | 1st-place Inspire may be won only once per season across Qualifying/League Tournaments; 2nd/3rd remain possible afterwards. | ✔ |
| A215 | 6.2 | 52 | A team may win or be runner-up for only **one** team judged award per event. | ✔ |

### 6.4 Section 12 — ROBOT Construction Rules (R) · 52 rules

| Rule | Sub | p. | Paraphrase | EG |
|---|---|---|---|---|
| R101 | 12.1 | 66 | The ROBOT and its MAJOR MECHANISMS must be built by the registered team that will compete with it. | ✔ |
| R102 | 12.1 | 67 | STARTING CONFIGURATION: fully stationary and self-contained inside an 18 in. (45.70 cm) cube. | ✔ |
| R103 | 12.1 | 67 | The ROBOT may hold its STARTING CONFIGURATION by powered-off mechanical means and/or an initialized OpMode; it must be self-supporting (no leaning on the sizing tool). | ✔ |
| R104 | 12.1 | 67 | No ROBOT weight limit — but weight still affects TILE damage, battery drain, etc. | ✔ |
| **R105** | 12.1 | 68 | **GAME-SPECIFIC (the only one in V0).** ROBOT must stay one assembly — no intentional detaching; after MATCH start it may expand but stays inside sizing constraints measured against its STARTING CONFIGURATION. *Numbers deferred to kickoff.* | ✘ |
| R201 | 12.2 | 68 | ROBOT must not risk making a mess or a hazard in the ARENA. (Its orange note carries the `GXXX` placeholder.) | ✔ |
| R202 | 12.2 | 68 | No hazardous materials or unsafe conditions on the ROBOT/OPERATOR CONSOLE; no interfering with other ROBOTS or FIELD STAFF. | ✔ |
| R203 | 12.2 | 69 | The ROBOT must release SCORING ELEMENTS and detach from FIELD elements while powered off, for fast FIELD reset. | ✔ |
| R204 | 12.2 | 69 | No mechanism designed to increase downforce by gripping the floor or by generated suction. | ✔ |
| R301 | 12.3 | 69 | COTS MAJOR MECHANISMS purpose-built to complete a game task are prohibited; exceptions for COTS drive CHASSIS and official FIRST kit mechanisms. | ✔ |
| R302 | 12.3 | 70 | Legal COTS parts and allowed raw materials may be modified (drilled, cut, painted) provided no other rule breaks. | ✔ |
| R303 | 12.3 | 70 | COTS COMPONENTS/MECHANISMS may not exceed a single degree of mechanical freedom; allowed examples listed (slides, single-speed gearboxes, turntables…). | ✔ |
| R304 | 12.3 | 71 | Software, designs and FABRICATED ITEMS created before Kickoff may be reused year to year. | ✔ |
| R305 | 12.3 | 71 | Current-season SCORING ELEMENTS, or replicas of them, may not be used as ROBOT construction material. | ✔ |
| R401 | 12.4 | 71 | At least 2 ROBOT SIGNS, on separate surfaces ≥ 90° apart, visible to FIELD STAFF. | ✔ |
| R402 | 12.4 | 72 | Each ROBOT SIGN needs a solid opaque red or blue rectangle ≥ 6.5 in × 2.5 in showing the assigned ALLIANCE colour. | ✔ |
| R403 | 12.4 | 73 | Team number in solid opaque white Arabic numerals ≈ 2.25 in tall, positioned per Figures 12-1/12-3/12-4. | ✔ |
| R501 | 12.5 | 75 | Only the motors listed in Table 12-1 are legal actuators. | ✔ |
| R502 | 12.5 | 76 | Servos must meet the Table 12-2 requirements at 6 V and be compatible with their power regulating device. | ✔ |
| R503 | 12.5 | 77 | Maximum 8 motors + 8 servos, summed across **all** configurations used at an event. | ✔ |
| R504 | 12.5 | 77 | Do not modify a motor's or servo's integral mechanical/electrical system; only the listed exceptions (mounting brackets, output shaft/pinion, …). | ✔ |
| R505 | 12.5 | 77 | All actuator control signals must originate from an approved power regulating device; the approved device list is enumerated here. | ✔ |
| R506 | 12.5 | 78 | No relays, electromagnets, or electrical solenoid actuators. | ✔ |
| R601 | 12.6 | 78 | Exactly one approved 12 V NiMH main battery, unaltered except for listed exceptions (e.g. fuse). | ✔ |
| R602 | 12.6 | 78 | Other batteries only for self-contained peripherals and LEDs: COTS USB packs ≤ 100 Wh with stated 5 V/12 V output limits, and batteries integral to devices such as action cameras. | ✔ |
| R603 | 12.6 | 79 | Exactly one main power switch must control all battery power to every power regulating device (R602 excepted); approved switch list given. | ✔ |
| R604 | 12.6 | 79 | Use fuses exactly as the device manufacturer directs; no up-rating, replacing or modifying them for advantage. | ✔ |
| R605 | 12.6 | 79 | The ROBOT frame may not carry current; all wiring and devices electrically isolated from the frame. | ✔ |
| R606 | 12.6 | 80 | All power regulating devices, their wiring and fuses must be able to be made visible for inspection; the ROBOT CONTROLLER must be accessible. | ✔ |
| R607 | 12.6 | 80 | Anything active that is not an R501 actuator or R505 power regulating device is a CUSTOM CIRCUIT; regulated output above 5 V only if it powers LEDs only. | ✔ |
| R608 | 12.6 | 80 | Power regulating devices must be connected and powered through approved ports, per manufacturer instructions and the table given. | ✔ |
| R609 | 12.6 | 81 | Minimum wire gauges per Table 12-8 (e.g. 18 AWG / 1 mm² for 12 V main battery power). | ✔ |
| R610 | 12.6 | 82 | Colour-code the 12 V main and +5 V aux buses along their entire length — positive: red/yellow/white/brown/black-with-stripe; negative: black or blue. | ✔ |
| R611 | 12.6 | 82 | Powered USB hubs may draw energy only from an R602 COTS USB battery pack or the REV Expansion/Control Hub 5 V aux port. | ✔ |
| R612 | 12.6 | 82 | CUSTOM CIRCUITS may not directly alter the power or control path between battery, main switch, power regulating devices, and actuators. | ✔ |
| R613 | 12.6 | 82 | Do not mix power sources on or between power regulation devices; sensors/encoders are powered only by the device they connect to. | ✔ |
| R701 | 12.7 | 83 | Exactly one programmable ROBOT CONTROLLER — a REV Control Hub, or an Android phone connected to a REV Expansion Hub. | ✔ |
| R702 | 12.7 | 83 | Coprocessor software may not be altered; manufacturer binary firmware updates allowed; SDK-supported programmable vision coprocessors excepted. | ✔ |
| R703 | 12.7 | 84 | A smartphone acting as ROBOT CONTROLLER must connect to the REV Expansion Hub over USB (OTG cables/hubs permitted). | ✔ |
| R704 | 12.7 | 84 | Use Wi-Fi networks and bandwidth only as directed and in a way that doesn't interfere with other teams or ARENA operations; no other wireless. | ✔ |
| R705 | 12.7 | 85 | Name devices for your team number — `<team#>-RC`, `<team#>-DS`, spares included. | ✔ |
| R706 | 12.7 | 85 | No tampering with DRIVER STATION, Android ROBOT CONTROLLER, power switches, power regulation devices, fuses or batteries beyond explicitly permitted modifications. | ✔ |
| R707 | 12.7 | 86 | USB may carry only: R708 webcams/optical vision sensors, a USB hub or switch, and a REV Expansion Hub. | ✔ |
| R708 | 12.7 | 86 | Only single-image-sensor vision devices natively supported by the ROBOT CONTROLLER app — UVC webcams (e.g. Logitech C270) and approved vision coprocessors. **No stereoscopic cameras.** | ✔ |
| R709 | 12.7 | 86 | Self-contained recorders (GoPro-style) are allowed for non-functional post-MATCH review, wireless disabled. | ✔ |
| R710 | 12.7 | 86 | Lasers only if all three hold: part of a sensor, IEC/EN 60825-1 Class I or Exempt, and non-visible spectrum. | ✔ |
| R711 | 12.7 | 86 | Android device configuration: non-default Control Hub Wi-Fi password, Airplane Mode on phones, etc. | ✔ |
| R801 | 12.8 | 87 | No pneumatic actuators, high-speed blowers or vacuums; only sealed, manufacturer-pre-charged COTS closed-air items such as gas shocks. | ✔ |
| R901 | 12.9 | 87 | Exactly one approved Android DRIVER STATION device connected and powered on (REV Driver Hub or an approved Android device). | ✔ |
| R902 | 12.9 | 88 | The DRIVER STATION touch screen must remain accessible within the OPERATOR CONSOLE. | ✔ |
| R903 | 12.9 | 88 | OPERATOR CONSOLE, including power banks, must fit within 3 ft W × 1 ft 6 in D × 2 ft H, excluding items held or worn by DRIVERS. | ✔ |
| R904 | 12.9 | 88 | No wireless to, from, or within the OPERATOR CONSOLE other than the ROBOT CONTROLLER app ↔ DRIVER STATION app link. | ✔ |

**Section totals: I 7 · E 35 · A 15 · R 52 = 109.**
---

## 7. Numbering stability — why last season's rule numbers are a trap

Of the 109 V0 rules, only **41** kept the exact number they had in DECODE for an equivalent headline. **36 were
renumbered**, and the rest are new or rewritten. Matching was done by normalised-headline comparison between the
V0 and DECODE PDF extractions.

### 7.1 Renumbered evergreen rules — DECODE → BIOBUZZ V0

| BIOBUZZ V0 | was DECODE | Rule subject |
|---|---|---|
| E105 | E106 | Event resources are for competing teams only |
| E106 | E107 | Practise only when/where permitted |
| E107 | E108 | Work in designated areas only |
| E108 | E109 | Prohibited items at events |
| E109 | E110 | Don't arrange extra services/utilities |
| E110 | E111 | No selling |
| E112 | E113 | Hang banners with care |
| E113 | E114 | Flag/flagpole size limits |
| E114 | E115 | No firearms/weapons |
| E115 | E116 | Inspection required for practice FIELD |
| E116 | E117 | No recording without consent |
| E509 | E510 | Aerosols/noxious fumes in approved areas only |
| I301 | I304 | Bring the complete ROBOT to inspection |
| I304 | I306 | Do not exploit re-inspection |
| R102 | R101 | 18-inch cube STARTING CONFIGURATION |
| R103 | R102 | ROBOT may assist holding STARTING CONFIGURATION |
| R104 | R103 | No weight limit |
| R204 | R208 | No grabbing the floor |
| R304 | R305 | Reuse software/designs/parts year to year |
| R305 | R306 | SCORING ELEMENTS not for ROBOT construction |
| R603 | R609 | Battery through the main power switch |
| R605 | R611 | Frame is not a current path |
| R606 | R612 / R711 | Electrical system + ROBOT CONTROLLER inspectable *(merged)* |
| R609 | R615 | Wire sizing |
| R610 | R616 | Wire colours |
| R611 | R617 | Powered USB hub sources |
| R612 | R618 | Don't modify critical power paths |
| R613 | R619 | Don't mix power on/between regulators |
| R703 | R705 | Smartphone RC connects to Expansion Hub via USB |
| R705 | R707 | Configure devices for your team number |
| R706 | R712 | Only specified control-system modifications |
| R707 | R714 | USB is for vision |
| R708 | R715 | Only supported USB vision |
| R709 | R716 | Recording devices are okay |
| R711 | R718 | Configure Android devices appropriately |
| R903 | R904 | OPERATOR CONSOLE physical requirements |
| R904 | R905 | ROBOT app wireless only |

**[V0] vs [HIST]** — every left-hand id is confirmed in V0; every right-hand id is confirmed in DECODE TU32.

### 7.2 Rules that changed **section**, not just number

| BIOBUZZ V0 | was DECODE | Move | Why it matters |
|---|---|---|---|
| **R101** "It is your team's ROBOT" | **I301** | Inspection → ROBOT Construction | A build-legality question is now an R-rule; INSPECTORS still enforce it, but it is cited differently. |
| **E117** "Enter only 1 ROBOT in the tournament" | **I302** | Inspection → Event Rules | Now covered by the E-section Universal Violation Note (VERBAL WARNING) rather than an inspection Violation line. |
| **E118** "No saving seats" | **E801** | §5.8 *In the Stands* deleted; folded into §5.1 | The whole `E8xx` block disappeared. DECODE `E802` "no throwing items from the stands" has **no V0 successor** — UNVERIFIED whether it returns. |
| **E511** "Charge batteries in a safe and fair manner" | **R603 + R604** | ROBOT Construction → Pits *(merged)* | Battery charging is now an **event** rule, not a ROBOT rule. Consequence: it is no longer an inspection item, and its enforcement is the E-section VERBAL WARNING. |

### 7.3 Consolidation — rules that became bullet points

The R-section shrank from 73 (DECODE) to 52 (V0) mostly by **absorbing standalone rules into example lists inside
broader rules**. Verified cases, all now inside V0 **`R201`** (p.68) — *not* `R202`; `R201` is the mess/damage rule that
carries the `GXXX` placeholder, `R202` is the separate safety/fair-play rule with lettered items A–K:

| DECODE standalone rule | Where it lives in V0 |
|---|---|
| R201 "Do not damage the TILE floor" | **R201** "damage risk" example list — "traction devices with features that are known to damage the TILE floor" |
| R202 "No exposed sharp edges" | **R201** "damage risk" example list — "components with exposed sharp edges or sharp protrusions" |
| R205 "Do not make a mess" / R206 "Do not damage SCORING ELEMENTS" | **R201** body + its "at risk of making a mess" list and the wear-and-tear orange box |
| R605 "Batteries are not ballast" | ⚠️ **Not** absorbed into an example list. V0 `R201`'s "loose ballast such as sand, coffee beans, kitty litter, glitter, or ball bearings" bullet is about **unsecured** components, not batteries. The operative constraint is now **`R602`**, whose headline reads "Other batteries are **only** allowed for self-contained peripheral devices and LEDs only" — which excludes a battery carried purely as dead weight, but does so by implication rather than by an explicit prohibition. `research/BIOBUZZ-V0-STRUCTURE.md` §5.8 calls this a **deletion and a gap**; both readings are defensible. **Q&A candidate for 28 Sep.** |

**This is the single most important structural change for a reviewer.** Those specifics are now introduced by
"examples … include, but are not limited to" — i.e. they moved from **closed enumerations** to a
**non-exhaustive illustrative list under a broad standard**. That widens INSPECTOR/REFEREE discretion and removes
the "it isn't listed, so it's legal" argument. Assume the same pattern applies to other DECODE rules with no V0
successor (`R204` SCORING ELEMENTS stay with the FIELD, `R606` secure battery mounting, `R607` robust insulated
connections, `R608` limit non-battery energy, `R307` work outside pit hours, `E602`–`E605` cart specifics,
`I307`/`I308` inspection procedure) before concluding a rule was deleted. **UNVERIFIED** case by case —
check the absorbing rule's example list.

### 7.4 Practical rule for kickoff day

> Never cite a rule number from memory, a forum, or a prior-season Q&A. Search the **headline text**, then read
> the number off the current manual. Build the V0→V1 id map from `rules_CLASSIFIED.tsv` before doing any rule
> analysis.

---

## 8. The grammar of rule text

### 8.1 Anatomy of a rule

```
R607   *Custom Circuits must not provide regulated power above 5V unless they are only powering LEDs.
└id┘   └────────────────── headline (green+asterisk = evergreen) ────────────────────────────────────┘
       Any active electrical item that is not an actuator (specified in R501) …          ← rule body
           A. …  B. …  C. …                                                              ← sub-items
       [orange box]  intent / best practice — persuasive, NOT binding                     ← see below
       Violation: MAJOR FOUL.                                                             ← enforcement (G/T/I only)
```

Fixed conventions, all confirmed in V0 unless noted:

| Element | Convention | Grep |
|---|---|---|
| Rule id | `Roboto-Bold` 11 pt, black, left margin x ≈ 36 pt | `^[IEARGTLC][0-9]{3}` |
| Headline | Bold, green `#06844B` + `*` (evergreen) or orange `#ED7D31` (game-specific) | §5.3 |
| Sub-items | Capital letters `A.` `B.` `C.`, then lower-case roman `i.` `ii.` `iii.` | — |
| Sub-item citation | Dotted — `G102.C`, `R505.B` **[HIST]** | `\b[IEARGTLC][0-9]{3}\.[A-Z]\b` |
| Cross-reference | `Consolas` 11 pt, blue `#4472C4` — a live hyperlink. **93 in V0** | colour test |
| Orange box | Warning/caution/note. **Explicitly does not carry the weight of the rule**; if it conflicts with the rule, the rule wins (V0 p.17) | — |
| Defined term | ALL CAPS, defined in §16 Glossary | `\b[A-Z]{3,}\b` |
| Units | Imperial first, metric in parentheses; **imperial governs** — metric is convenience only, rounded to 0.05 cm in BIOBUZZ (ITD rounded to tenths) | — |
| Headline authority | If headline and rule body disagree, **the body wins** (V0 p.18) | — |

### 8.2 The enforcement sentence

**In BIOBUZZ V0 there are ZERO `Violation:` lines.** All of them live in Sections 11/13/15, which are
placeholders. **[V0]**

Enforcement in V0 is carried by one blanket clause, the **Universal Violation Note** (p.33, `Roboto-Italic`
`#767171`), which changed wording from DECODE:

| Manual | Universal Violation Note for Event Rules (E) |
|---|---|
| **BIOBUZZ V0** | A violation of any Event Rule results in a **VERBAL WARNING**; egregious or subsequent violations escalate to FIRST HQ and/or disqualification from MATCHES and awards. |
| DECODE | A violation results in a **warning from event volunteers**; *egregious or repeated* violations get a VERBAL WARNING from the Head REFEREE/LRI/Event Director; subsequent violations escalate. |

**BIOBUZZ compressed the ladder by one step** — what was an informal volunteer warning in DECODE is a formal
VERBAL WARNING in BIOBUZZ. **[V0]** V0 p.33 vs DECODE p.29. Both versions close with "Additional rule specific
violations, if applicable, are listed with their corresponding rule."

#### Enforcement pattern, from DECODE **[HIST]** — expect this back on 2026-09-12

Style: `Roboto-Italic`, grey `#767171`, on its own line, beginning `Violation:`. Distribution in DECODE: **all 53
G-rules carry exactly one**, plus `I302`, `I303`, `I305`, `I308`, `E105`, `T205`, `T401`, `T701`, `T702`.

Observed DECODE forms, most→least common:

| Form | Count |
|---|---|
| `Violation: VERBAL WARNING.` | 12 |
| `Violation: MINOR FOUL.` | 8 |
| `Violation: MAJOR FOUL.` | 2 |
| `Violation: MAJOR FOUL per SCORING ELEMENT.` | 2 |
| `Violation: MAJOR FOUL and YELLOW CARD.` | 2 |
| `Violation: The MATCH will not start until all requirements are met if there is a quick remedy.` | 2 |
| `Violation: MATCH will not start until the situation is remedied.` | 2 |
| `Violation: YELLOW CARD.` / `RED CARD.` / `YELLOW or RED CARD.` | 1 each |
| `Violation: DISQUALIFIED from the current MATCH.` / `DISABLED and VERBAL WARNING.` | 1 each |

**Composition grammar — this is where loopholes live.** Penalties compose along four axes:

1. **Multiplier:** `per SCORING ELEMENT` · `per ARTIFACT` · `per instance` · `per occurrence` · `per LAUNCHED
   SCORING ELEMENT` · `per SCORING ELEMENT over the limit` · *(ITD)* `plus MINOR FOUL for every 5 seconds the
   violation continues`.
2. **Escalation trigger:** `plus YELLOW CARD if REPEATED` · `if greater-than-MOMENTARY` · `plus RED CARD if
   CONTINUOUS` · `if subsequent violations occur during the event`.
3. **Conditional branch on another rule:** `MAJOR FOUL plus YELLOW CARD if G431` · `MAJOR FOUL per instance of
   ROBOT contact in G402`.
4. **Non-foul consequence:** the ALLIANCE is **ineligible for a Ranking Point**; the opposing ALLIANCE is
   **awarded** an RP or a scoring credit; the MATCH will not start; the ROBOT is DISABLED.

**Read every `Violation:` line as its own mini-rule.** Axis 1 turns a 5-point foul into an unbounded one; axis 4
can hand an opponent a Ranking Point — which is often worth far more than the foul points. On kickoff day,
`grep -n '^Violation' | sort | uniq -c` on the new manual and read the *outliers* first.

### 8.3 Penalty vocabulary **[HIST]** — none of it is in V0

| Term | DECODE definition | ITD |
|---|---|---|
| MINOR FOUL | credit of **5 points** to the opponent's MATCH point total | same |
| MAJOR FOUL | credit of **15 points** to the opponent's MATCH point total | same |
| YELLOW CARD | warning from the Head REFEREE for egregious ROBOT or team-member behaviour | same |
| RED CARD | DISQUALIFICATION from the MATCH | same |
| VERBAL WARNING | *(the only one defined in V0's glossary)* a warning issued by event staff or the Head REFEREE | — |

Qualifier vocabulary to watch (all DECODE glossary terms, absent from V0): **MOMENTARY**, **CONTINUOUS**,
**REPEATED**, **EGREGIOUS**, **DISABLED**, **DISQUALIFIED**. These are the tuning knobs FIRST uses to make an
otherwise-identical rule strict or lenient. **Do not assume BIOBUZZ reuses DECODE's 5/15 point values — verify on
kickoff day.**

### 8.4 Modal verbs

FIRST is disciplined but not perfect about modals. Counts (word-boundary, case-insensitive):

| Modal | V0 whole manual | DECODE §11 only | Reading |
|---|---|---|---|
| `may` | 206 | 62 | permission — grants an option |
| `may not` | 40 | 32 | **prohibition** — the strongest negative form used |
| `must` | 149 | 31 | **binding requirement** |
| `will` | 122 | 21 | statement of what FIRST/volunteers do — usually not a team obligation |
| `should` | 86 | 15 | **recommendation, not binding** |
| `shall` | 7 | 1 | legacy synonym for *must*; survives mainly in R-rules |

**The `should` trap.** `should` is advisory. V0 examples: `I301` — teams *should* present the complete ROBOT;
`I303` — a team *should* request re-inspection; `E502` — pit setups *should* be self-contained; `R201` — ROBOTS
*should* be designed so they don't damage anything. A rule whose operative verb is *should* cannot by itself
carry a penalty; the enforceable hook is usually a **different** rule (`I304` "do not exploit re-inspection" is
the enforceable partner of the advisory `I303`). Note also `R201`'s headline uses *should* while its body says
"The ROBOT **must not** pose a risk" — **when headline and body disagree, the body governs** (V0 p.18).

### 8.5 The ALL-CAPS defined-term convention

V0 §16 (p.92): defined terms are in ALL CAPITAL LETTERS throughout the manual; "Competition rules mean what they
plainly say. If a word is not given a game definition, then you should use its common conversational meaning."
**[V0]**

Practical consequences:

* **ALL CAPS narrows a rule.** `R305` bans *SCORING ELEMENTS* — the defined game pieces — not "anything that looks
  like a game piece."
* **lower case broadens it.** A word left un-capitalised is read conversationally, which is often *wider* than a
  defined term. Watch for a rule that switches between `ROBOT` and "robot", or `MATCH` and "match".
* **A term used in ALL CAPS but not in the glossary is an ambiguity to file in the Q&A.**

**V0's glossary has only 22 entries:** ALLIANCE, ARENA, CHASSIS, COMPONENT, COTS, HOME REGION, INSPECTOR, JUDGE,
LRI, MAJOR MECHANISM, MECHANISM, OPERATOR CONSOLE, PORTFOLIO, REFEREE, ROBOT, ROBOT CONTROLLER, ROBOT SIGN,
STARTING CONFIGURATION, STUDENT, TILE, VENDOR, VERBAL WARNING. **[V0]**

**Terms V0 already uses in ALL CAPS inside binding rules but does *not* define** (frequency in V0):

`MATCH` (75 incl. MATCHES) · `FIELD` (24) · `DRIVER STATION` (21) · `SCORING ELEMENT` (10) · `FIELD STAFF` (9) ·
`FABRICATED ITEM` (7) · `DRIVE TEAM` (3) · `CUSTOM CIRCUIT` (3) · `FOULS` (3, in the §4 Advancement tables:
"Average Qualification MATCH Points (excluding FOULS)").

Every one of those definitions arrives at kickoff — and **each is a place where a definition change silently
rewrites an already-"final" rule.** Example: `R305` bans building with SCORING ELEMENTS, but SCORING ELEMENT is
undefined in V0; the BIOBUZZ definition (single game piece? a set? a field-supplied assembly?) decides how wide
`R305` actually is. **Diff the glossary first on kickoff day — before reading a single G-rule.**

---

## 9. The pre-2024 scheme and the renumbering event

### 9.1 When and how it changed

| Season | Document(s) | Scheme |
|---|---|---|
| 2015-16 RES-Q → 2023-24 CENTERSTAGE | **Game Manual Part 1** (season-agnostic) + **Part 2** (game) — and, 2020-21 to 2023-24, separate *Traditional* and *Remote* editions | `<XX##>` — angle-bracketed, 1–2 letter prefix, **2 digits**, title in Title Case followed by a dash |
| **2024-25 INTO THE DEEP onward** | **one Competition Manual** | `X###` — bare, 1 letter, **3 digits**, colloquial headline, evergreen colour coding |

The renumbering was a **clean break at the 2024-25 season**, executed as part of merging Part 1 + Part 2 into a
single *Competition Manual* and dropping the Traditional/Remote split. There is **no crosswalk table** in any
manual in this corpus; ITD V14 simply presents the new scheme in §1.6 with the same "Figure 1-2 Rule numbering
method" legend BIOBUZZ still uses. **[HIST]**

### 9.2 The old prefixes

**Game Manual Part 1** (competition/robot/inspection, season-agnostic):

| Prefix | Section (CENTERSTAGE Part 1) | Domain | Modern equivalent |
|---|---|---|---|
| `C##` | 3.5 Competition Rules | Conduct, eligibility, egregious behaviour (`C01`–`C29`) | split across `G2xx` + `E1xx` |
| `RG##` | 7.3.1 General Robot Rules | Illegal parts, general legality | `R1xx` / `R3xx` |
| `RM##` | 7.3.2 Robot Mechanical Parts & Materials | Allowed materials, COTS | `R3xx` |
| `RE##` | 7.3.3 Robot Electrical Parts & Materials | Power switch, batteries, wiring | `R5xx` / `R6xx` |
| `DS##` | 7.3.4 Driver Station Rules | OPERATOR CONSOLE / DRIVER STATION | `R9xx` |
| `RS##` | 7.3.5 Robot Software Rules | Device naming, app config | `R7xx` |
| `DR##` | 7.4 Team Game Element Construction | CENTERSTAGE-only (Drone) | *(none — game-specific)* |
| `I##` | 8.4 Inspection Rules | Inspection (`I01`–`I10`) | `I3xx` |
| `T##` | 4.9 Tournament Rules | Tournament conduct (`T10`–`T27` observed) | `T2xx`–`T8xx` |

**Game Manual Part 2** (the game):

| Prefix | Section (CENTERSTAGE Part 2) | Domain | Modern equivalent |
|---|---|---|---|
| `S##` | 4.5.1 Safety Rules | `S01`–`S04` | `G1xx` |
| `G##` | 4.5.2 General Game Rules | `G01`–`G30` | evergreen `G2xx`–`G4xx` |
| `GS##` | 4.5.3 Game-Specific Rules | `GS01`–`GS13` | the orange/game-specific `G4xx` rules |

Notes: `RS` meant **Robot Software** in this era, not "robot safety". `DS` and `DR` appear only from ~2021-22 and
2023-24 respectively — the old scheme grew prefixes ad hoc, which is precisely what the 2024-25 renumbering fixed.
The old `<GS##>` "Game-Specific" prefix is the direct ancestor of today's **orange, non-asterisked** headline: the
distinction survived, but moved from the *prefix* into *typography*. **[HIST]**

### 9.3 Old-scheme formatting

`<RG01> Illegal Parts - The following types of mechanisms and parts are not allowed:`

Angle brackets around the id, Title-Case short title, hyphen, then rule text. Sub-item citations appended the
letter directly to the bracketed id (`<RG01>a`). Grep for the old scheme with:

```bash
grep -oE '<[A-Z]{1,2}[0-9]{2}>[a-z]?' manuals/archive/wayback/*.txt
```

---

## 10. Kickoff-day checklist (5 minutes, in order)

1. `pdftotext`-free extract with pymupdf, then run the §5.3 awk → `rules_CLASSIFIED.tsv`. Sanity-check the total
   (expect ~185) and the game-specific count (expect ~17).
2. **Diff the glossary first.** New/changed ALL-CAPS definitions silently rewrite the 109 already-"final" rules —
   especially `SCORING ELEMENT` (`R305`), `MATCH`, `FIELD`, `FABRICATED ITEM` (`E107`), `CUSTOM CIRCUIT` (`R607`).
3. `grep -n '^Violation'` → sort by rarity. Read the **outliers** (RP awards/forfeits, "per X" multipliers,
   conditional branches) before the common `MINOR FOUL.` lines.
4. Read every **orange/game-specific** rule end to end. In V0 that is a single rule (`R105`); at kickoff expect
   ~17, and they are where the game actually lives.
5. Build the **V0 → V1 id map** by headline text. Do not trust any inherited rule number, including your own
   notes from this document (§7).
6. `grep -nE '\b[GTLCRIEA]XXX\b'` → any hit is an unresolved FIRST editing placeholder and a free day-one Q&A.
7. Check `R105`'s replacement text specifically — it is the one rule V0 flagged as game-specific, i.e. FIRST has
   already told you the expansion limits are changing.

---

## 11. Source index

| File | Used for |
|---|---|
| `manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V0_2026-07-31.pdf` | All **[V0]** claims: rule ids, headlines, colours, pages, §1.7.1 legend (p.17-18), Universal Violation Note (p.33), §14 League Play (p.90), glossary (p.92) |
| `manuals/2026-27_BIOBUZZ/v0_pymupdf.txt` | Text-mode greps; the trustworthy text extraction |
| `manuals/2026-27_BIOBUZZ/BIOBUZZ_V0_layout.txt` | **Do not use for rule parsing** (§5.2); fine for tables |
| `manuals/_reference_prior_seasons/2025-26_DECODE_Competition_Manual_TU32.pdf` | DECODE rule inventory, G/T/C blocks, renumbering baseline |
| `manuals/_reference_prior_seasons/2025-26_DECODE_Section11_text.txt` | `Violation:` pattern census |
| `manuals/_reference_prior_seasons/2024-25_ITD_Section11_text.txt` | ITD `Violation:` forms; `G5xx` Post-MATCH block |
| `manuals/archive/2024-25_INTO_THE_DEEP_Competition_Manual_V14.txt` | First season of the modern scheme; `A1xx`-era awards numbering |
| `manuals/archive/2023-24_CENTERSTAGE_GameManual_Part{1,2}_Traditional.txt` | Last season of the `<XX##>` scheme; Part 1/Part 2 prefix map |
| `manuals/archive/wayback/2015-16_RESQ_GameManual_Part{I,II}.txt` | Earliest confirmed `<XX##>` usage; `T10`–`T12` |
| `tools/ingest-manual.sh` | The evergreen/game-specific greps corrected in §5.3 |

**Security note:** no file in this corpus contained text addressed to an AI agent or attempting to instruct one.
The only prompt-shaped strings encountered were FIRST's own editing placeholder `GXXX` (V0 p.68) and a PORTFOLIO
credit example naming an AI tool (V0 p.48, inside `A201`) — both ordinary manual content, not injection.
