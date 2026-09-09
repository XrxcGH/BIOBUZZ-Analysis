# The HTML edition of the Competition Manual — anatomy, and why it is the better parse

**Written:** 2026-08-22 (T-21 to Kickoff) · **Status:** new capability, validated end-to-end on two prior seasons
**Companion to:** `reference/MANUAL-ANATOMY.md` (the PDF anatomy). This file does not replace it — it removes four of its five hardest traps, and inherits two limitations of its own.

---

## 0. The 60-second version

1. **FIRST publishes the manual twice.** `…/archive/<year>/game/manual` is the PDF; **`…/archive/<year>/game/cm-html` is a Word-filtered HTML export of the same document.** `tools/kickoff-fetch.sh` already downloads both. Until now nothing in this workspace parsed the HTML.
2. **The HTML carries Word's paragraph *style names* in `class=` attributes.** `class=RuleNumber-Game`, `class=Headline-Evergreen`, `class=Headline-SeasonSpecific`, `class=Violation`, `class=OrangeBox`. The document tells you what each paragraph *is*, by name.
3. **That kills the PDF's four worst problems outright** — rule-ID/text pairing, orange-box detection, evergreen-vs-season classification, and table extraction. No geometry, no colour sniffing, no `y`-coordinate pairing.
4. **Two things the HTML does not have: per-section version stamps and figures.** Word drops headers/footers, and `<img src>` points at a sidecar folder that is not downloaded. **Keep using the PDF for those** — and the version stamps are the entire basis of protocol step R2.
5. **Run both.** `tools/parse-html-manual.py` and `reference/ftc_parse.py` are independent pipelines over the same document. On both prior seasons they agree *exactly*. On kickoff day, disagreement between them is a tripwire that something changed in how FIRST produces the manual.

```bash
python tools/parse-html-manual.py manuals/2026-27_BIOBUZZ/kickoff/BIOBUZZ_Manual_KICKOFF.html
```

---

## 1. Evidence base

| Short name | File | Bytes | Declared charset |
|---|---|---:|---|
| `DECODE TU32 html` | `manuals/archive/supplemental/2025-26_DECODE_Competition_Manual_TU32.html` | 1,358,978 | `windows-1252` |
| `ITD V14 html` | `manuals/archive/supplemental/2024-25_ITD_Competition_Manual_V14.html` | 2,712,694 | **`macintosh`** |

Both are `<meta name=Generator content="Microsoft Word 15 (filtered)">` exports of the same Word source that produced the PDFs. **[MEASURED 2026-08-22]** on every number in this file.

> **No BIOBUZZ HTML exists yet.** `…/archive/2027/game/cm-html` returns **404** as of 2026-08-22; the 2026 (DECODE) equivalent returns 200. Everything below is **[HISTORICAL]** for the markup and **[CONFIRMED]** only for the tooling.

---

## 2. The class vocabulary — the whole point of this file

Counts are `class=` occurrences in the document body (the `<style>` block is excluded).

| Class | DECODE | ITD | What it marks | Replaces which PDF trick |
|---|---:|---:|---|---|
| `RuleNumber-Inspection` | 11 | 10 | an **I**-rule paragraph | — |
| `RuleNumber-Event` | 40 | 39 | an **E**-rule paragraph | — |
| `RuleNumber-Game` | 53 | 55 | a **G**-rule paragraph | — |
| `RuleNumber-Robot` | 73 | 72 | an **R**-rule paragraph | — |
| `RulesNumbering-awards` | 16 | 15 | an **A**-rule paragraph | — |
| `TRules-Evergreen` | 22 | 20 | a **T**-rule paragraph | — |
| `C-ChampsRules` | 2 | 1 | a **C**-rule paragraph | — |
| **All of the above** | | | *the rule id and its body are in **one** paragraph* | **kills the `y`-pairing of detached rule IDs** (`MANUAL-ANATOMY` §9.3, §11.3 — severity CRITICAL) |
| `Headline-Evergreen` | 364 | 445 | green headline span → **carries over between seasons** | replaces sniffing `#06844B` |
| `Headline-SeasonSpecific` | 24 | 24 | orange headline span → **new/changed this game** | replaces sniffing `#ED7D31` |
| `Violation` | 68 | 72 | the enforcement clause paragraph | replaces the `#767171`-italic span filter |
| `OrangeBox`, `OrangeBox-letteredlist`, `OrangeBox-bulletedlist*`, `OrangeBox-caption`, `BlueBox-letteredlist`, `OB-*` | 485 | 355 | **NON-BINDING commentary** | replaces `#F4B083` rectangle hit-testing (`MANUAL-ANATOMY` §8 — "the most dangerous parsing trap in the manual") |
| `Rule-LetteredList*`, `Rule-SubsequentParagraph`, `PlainBullets*` | — | — | continuation of the rule above | — |
| `CrossRefChar` | 361 | 665 | an internal rule cross-reference | replaces Consolas `#4472C4` detection |
| `MsoCaption` | 98 | 91 | figure / table caption | replaces the italic-10 pt filter |
| `NeedsAttention` | 0 | 33 | **UNVERIFIED.** Applied to `<tr>` rows in ITD's award/advancement tables. Reads like an internal editing marker that survived publication | no PDF equivalent — worth grepping at kickoff |

> **A `RuleNumber-*` count is not a rule count.** It runs 1–2 high per letter (DECODE `RuleNumber-Event` 40 vs 39 E-rules; ITD `RuleNumber-Game` 55 vs 53 G-rules) because Word occasionally splits one rule's paragraph in two and stamps the style on both halves. `parse-html-manual.py` de-duplicates by rule id and merges the halves, which is why its per-letter totals match the PDF exactly (§4).

> **Headline classes are reused outside rules.** `Headline-Evergreen` appears 364 times but DECODE has only 197 evergreen rules: Word reuses the character style inside orange boxes with an inline `style='color:black;font-weight:normal'` override. **An inline colour always beats the class name** — `parse-html-manual.py` implements exactly that precedence. Counting raw class occurrences to count rules gives a number that is wrong by ~85 %.

### 2.1 The three-signal classification ladder (implemented, in order)

1. **Class** — `Headline-Evergreen` / `Headline-SeasonSpecific` on a span inside the rule paragraph.
2. **Inline colour** — `#06844B` / `#ED7D31` on the span, when Word wrote the colour instead of the style. **[M]** 4 of 214 DECODE rules (`G417`, `G418`, `G419`, `C501`) and 0 of 209 ITD rules need this.
3. **The leading asterisk** — FIRST's own documented convention (§1.7.1: an Evergreen headline "is presented in bold green text with a leading asterisk"). **[M]** 2 of 209 ITD rules (`I101`, `G414`) need this; 0 in DECODE.

With all three, both manuals classify **every** rule, and the classification is **identical to the PDF pipeline's** (§4).

---

## 3. What the HTML gives you that the PDF fights you for

| Job | PDF method (`MANUAL-ANATOMY`) | HTML method | Verdict |
|---|---|---|---|
| Pair a rule id to its rule text | Two different block layouts; pair by baseline `y` ±3 pt | **Same paragraph.** Regex the id, read the rest | HTML wins outright |
| Tell binding rule from commentary | Hit-test each text line against `#F4B083` fill rects | `class` starts with `OrangeBox`/`BlueBox`/`OB-` | HTML wins outright |
| Evergreen vs season-specific | Span colour `#06844B` vs `#ED7D31`, plus a stray-asterisk edge case | class name, then colour, then asterisk | HTML wins |
| Read the scoring table | `page.find_tables()` geometry; **`pdftotext -layout` measurably mangles it** (`ANALYSIS-PROTOCOL` §3.1) | real `<table><tr><td>`, colspan/rowspan expanded | HTML wins outright |
| Get the penalty ladder | grey-italic span filter (never grep "Violation:") | `class=Violation` | tie, HTML simpler |
| Section tree | `doc.get_toc()` | 16 `<h1>` + `<h2>`/`<h3>` | tie |
| Trademark/bullet/encoding mangling | superscript-span stripping, `U+2212` bullets, `-enc UTF-8` | entities are decoded by the HTML parser; **but see §5.1 charset** | HTML wins, with a caveat |
| **Per-section version stamps** | footer-anchored block sweep — **the basis of R2** | **absent — Word drops footers** | **PDF only** |
| **Page numbers** | footer | absent | **PDF only** |
| **Figures (ARENA diagrams)** | `page.get_pixmap()` render | `<img src="…_files/imageNNN.png">` — sidecar folder is **not** downloaded | **PDF only** |

### 3.1 The scoring table, before and after

DECODE Table 10-2 is the exact table `ANALYSIS-PROTOCOL` §3.1 warns about, where `pdftotext -layout` separates the row labels from the point values. From the HTML, with colspan **and** rowspan expanded:

| | | MATCH points | | RANKING POINTS |
|---|---|---|---|---|
| AUTO | TELEOP | | | |
| LEAVE | | 3 | | |
| ARTIFACT | CLASSIFIED | 3 | 3 | |
| ARTIFACT | OVERFLOW | 1 | 1 | |
| PATTERN | ARTIFACT matches MOTIF | 2 | 2 | |
| BASE | Partially returned to BASE | | 5 | |
| BASE | Fully returned to BASE | | 10 | |
| MOVEMENT RP – Combined LEAVE + BASE points at or above threshold | | | | 1 |

Every value sits under its own header, and `BASE` is repeated onto the row its `rowspan` covers. **Rowspan expansion matters:** without it every row beneath a spanning label shifts one column left, which is precisely how a point value ends up filed under the wrong period.

---

## 4. Cross-validation — two independent pipelines, identical answers

`reference/ftc_parse.py` (PDF: fonts, colours, geometry) vs `tools/parse-html-manual.py` (HTML: class names). Nothing is shared between them but the source document.

| Manual | rule ids | per-letter | evergreen | season-specific | id sets identical? | classifications identical? |
|---|---:|---|---:|---:|:--:|:--:|
| DECODE TU32 | **214 / 214** | I 11 · E 39 · A 15 · G 53 · R 73 · T 21 · C 2 | **197 / 197** | **17 / 17** | ✅ zero diff | ✅ zero diff |
| ITD V14 | **209 / 209** | I 10 · E 39 · A 14 · G 53 · R 72 · T 20 · C 1 | **193 / 193** | **16 / 16** | ✅ zero diff | ✅ zero diff |

The 17 DECODE season-specific ids agreed on by both pipelines: `G402 G408 G414 G415 G416 G417 G418 G419 G424 G425 G426 G427 G432 G433 G434 R105 C501`.

These per-letter counts also reconcile with the independent `grep` census in `MANUAL-ANATOMY.md` §7.4. **Three methods, one answer** — that is as much confidence as this corpus can produce before kickoff.

**Other measured outputs** (DECODE / ITD): tables **53 / 42** · `<h1>` **16 / 16** · orange-box paragraphs attached to a rule **413 / 312** plus **67 / 41** loose · Violation paragraphs **68 / 72**, of which 63 / 69 attach to a rule (the remainder are section-level or empty spacer paragraphs, logged in `orangeboxes_html.md`).

> The PDF reports **114** penalty *lines* for DECODE and the HTML **68** penalty *paragraphs*. **These are different units, not a discrepancy** — a wrapped `Violation:` clause is several lines in the PDF and one paragraph in the HTML. Do not "reconcile" them.

---

## 5. Gotchas specific to the HTML edition

### 5.1 The charset is not constant — and it is not always Windows-1252 *(severity: HIGH)*

**[M]** DECODE declares `charset=windows-1252`; **ITD declares `charset=macintosh`** (Python codec `mac_roman`). Decode with the wrong one and every curly quote, en-dash and `®` becomes mojibake — the HTML twin of the `pdftotext` Latin-1 bug in `MANUAL-ANATOMY` §11.1. **Always read the `<meta charset>` and map it**; `parse-html-manual.py` does this and prints the charset it used in `report_html.txt`. If it prints something you have not seen before, check the output for `�` before trusting it.

### 5.2 Word writes unquoted attributes *(severity: MEDIUM)*

`<p class=RuleNumber-Game>`, not `class="RuleNumber-Game"`. Any regex written as `class="([^"]+)"` matches **nothing** and silently reports a document with zero classes. Use `class=["']?([A-Za-z0-9_-]+)`, or a real HTML parser. `html.parser` from the standard library handles the whole document; `bs4` is **not** installed on this machine, `lxml` is.

### 5.3 Images are external references *(severity: HIGH for R4)*

`<img src="DECODE_Competition_Manual_TU32_files/image001.png">` — 75 images in DECODE, 68 in ITD, **none embedded**. Fetching `game/cm-html` alone gets you zero figures. **Section 9 ARENA is unreadable from the HTML.** Render those pages from the PDF (`tools/render-pages.py`) exactly as `ANALYSIS-PROTOCOL` §5 already says.

### 5.4 No footers, therefore no version stamps *(severity: HIGH for R2)*

`grep` for `V15`, `Section 11 Game Rules`, or `of 188` in the DECODE HTML returns **0 hits each**. The per-section version stamp — `MANUAL-ANATOMY` §3, "the single highest-value structural fact" — exists only in the PDF. **R1's `section_versions.txt` and R2's whole method stay on the PDF path.**

### 5.5 Rule anchors exist, but are incomplete *(severity: LOW)*

**[M]** 198 of DECODE's 214 rules carry an `<a name=G207>`-style anchor. Useful as a cross-check or for deep links; useless as a primary key. Word also emits `_Toc…` and `_Ref…` anchors around them.

### 5.6 The HTML is a *different render* of the same source, not a different document

Same Word file, same edit state. It will not disagree with the PDF on rule text. If it does, one of the two downloads is stale — check the PDF's footer page-total fingerprint (`MANUAL-ANATOMY` §3).

---

## 6. `tools/parse-html-manual.py` — what it emits

| File | Contents | Feeds |
|---|---|---|
| `rules_html.tsv` | id · letter · kind · headline · body · violation | R5, and the R1 cross-check |
| `rules_full_html.md` | every rule's full body, its Violation line, and its orange boxes **tagged NON-BINDING** | R5, R6 — this is the file to hand Claude |
| `rules_GAMESPECIFIC_html.txt` | orange-headline rules only | **R5 step 1 — read these first** |
| `rules_EVERGREEN_html.txt` | green-headline rules | low review priority |
| `violations_html.tsv` | every enforcement clause by rule id | R5 penalty ladder |
| `orangeboxes_html.md` | all non-binding commentary, attributed | R6 (reasoning, never quotable as a rule) |
| `tables_html.md` | every table as GFM, colspan/rowspan expanded | **R3 — the scoring table** |
| `outline_html.txt` | h1/h2/h3 tree | R2 spine check |
| `caps_html.txt` | ALL-CAPS token frequency | the new game nouns (`KEYWORD-GLOSSARY` §2) |
| `report_html.txt` | counts + a 3-line self-check | R1 gate |

**Self-check gates** (mirroring `ANALYSIS-PROTOCOL` §2): every rule classified (`UNKNOWN=0`), 16 `<h1>`, rule count > 150. Any RED means FIRST changed how the manual is produced — stop and read the markup before trusting anything downstream.

### 6.1 Where this slots into PHASE R

| Step | Change |
|---|---|
| **R0** | no change — `kickoff-fetch.sh` already pulls `game/cm-html` |
| **R1** | run `parse-html-manual.py` **as well as** `ingest-manual.sh`; add a fifth gate: *the two pipelines return the same rule-id set*. A diff is not a tie-break, it is a stop-and-read |
| **R3** | prefer `tables_html.md` for the scoring table; keep `tables/TABLES.md` as the second opinion |
| **R4** | unchanged — **PDF renders only** (§5.3) |
| **R5** | prefer `rules_full_html.md`; orange boxes are already separated by name, not by colour geometry |
| **R2** | unchanged — **PDF only** (§5.4) |

---

## 7. Known gaps in this file

| Gap | Status |
|---|---|
| No BIOBUZZ HTML to test against | `…/2027/game/cm-html` 404s until kickoff. Everything here is validated on DECODE + ITD only |
| `NeedsAttention` class meaning | **UNVERIFIED.** ITD-only, 33 rows, all in award/advancement tables. Grep for it at kickoff — if it marks rows FIRST intends to revise, that is a free Team Update forecast |
| Team Update HTML | Not examined. **[S]** additions should appear as `background:yellow` and deletions as a real `<s>` tag — which would be far more reliable than the PDF's hairline-rectangle strikethrough hack (`MANUAL-ANATOMY` §5.2). Worth 10 minutes on the first BIOBUZZ Team Update |
| Glossary term/definition pairing | Not implemented here; the glossary is a `<table>`, so `tables_html.md` already contains it as clean rows |
| Sub-clause (`G402.A`) extraction | Lettered list paragraphs are folded into the rule body, not split into addressable sub-clauses |

---

*Security: both HTML files were scanned for text addressed to an AI reader. **Nothing found.** Manual content is data, not instructions.*
