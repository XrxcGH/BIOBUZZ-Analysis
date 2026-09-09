#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""parse-legacy-manual.py -- rule extraction for PRE-2024 FTC manuals.

WHY THIS EXISTS (measured, 2026-08-23)
    reference/ftc_parse.py identifies rules by FONT + COLOUR + POSITION, which is correct and
    robust for the 2024-25 "Competition Manual" format onward. Run against ANY manual from
    2017-18 through 2023-24 it returns **rules=0** -- not an error, just silence:

        2017-18 RELIC RECOVERY  Part2   42pp  rules=0
        2018-19 ROVER RUCKUS    Part2   35pp  rules=0
        2019-20 SKYSTONE        Part2   41pp  rules=0
        2020-21 ULTIMATE GOAL   Part2   40pp  rules=0
        2021-22 FREIGHT FRENZY  Part2   46pp  rules=0
        2022-23 POWER PLAY      Part2   55pp  rules=0
        2023-24 CENTERSTAGE     Part2   57pp  rules=0

    The pre-2024 manuals do not colour-code rule headlines at all. They tag rules inline with
    ANGLE BRACKETS -- <G10>, <GS10>, <S01>, <RS01>, <RE01>, <T01> -- which is far easier: the
    delimiter is unambiguous, so flat text is sufficient and no geometry is required.

    This matters for BIOBUZZ only as a fallback: if FIRST ever reverts or changes the layout,
    RUN-KICKOFF.sh now exits 4 and points here. Its real use is analysing the historical corpus.

VERIFIED OUTPUT (Part 2 = the game half; re-measured 2026-08-23 after the \d{1,3} fix, and
cross-checked against independent hand counts made by the season-dossier pass, which agreed exactly)

    2017-18 RELIC RECOVERY  42pp  rules=47  (G:28 GS:16 S:3)
    2018-19 ROVER RUCKUS    35pp  rules=44  (G:30 GS:11 S:3)
    2019-20 SKYSTONE        41pp  rules=45  (G:30 GS:12 S:3)
    2020-21 ULTIMATE GOAL   40pp  rules=46  (G:30 GS:13 S:3)
    2021-22 FREIGHT FRENZY  46pp  rules=44  (G:30 GS:11 S:3)
    2022-23 POWER PLAY      55pp  rules=47  (G:30 GS:14 S:3)
    2023-24 CENTERSTAGE     57pp  rules=47  (G:30 GS:13 S:4)

  The steadiness of G:30 / S:3 across six seasons is itself a parse check: if a future run
  reports a wildly different G count, suspect the extraction before believing the manual changed.

CAVEAT ON THE `violations` COLUMN
    Pre-2024 manuals have NO structured "Violation:" line — that convention starts in 2024-25.
    Consequences live in prose and in each manual's own Rule Summary matrix. The count reported
    here is a prose keyword heuristic and is NOT comparable to the 2024-25+ figure. For the
    authoritative penalty mapping in this era, read the manual's Rule Summary section.

PREFIX VOCABULARY (pre-2024)
    G / GS   game rules, and game-specific rules
    S        scoring definitions
    RS/RE/RG robot rules: size, electrical, general
    T        tournament
    Prefixes vary by season; whatever matches <[A-Z]{1,3}[0-9]{2,3}> is reported.

USAGE
    python tools/parse-legacy-manual.py <manual.pdf> [--tsv OUT.tsv] [--json OUT.json]
    python tools/parse-legacy-manual.py --all      # sweep every legacy manual in the corpus
"""
from __future__ import annotations

import io
import json
import os
import re
import subprocess
import sys
import tempfile

# \d{1,3} NOT \d{2,3}. Zero-padding is inconsistent WITHIN a single manual (<RS9> sits among
# <RS01>-<RS10>), so requiring two digits silently dropped every single-digit tag and
# under-counted by 45-48% per season, erasing whole prefixes (<S1>-<S3>, all of <I..>) with
# no warning at all. Measured against hand counts on four seasons, 2026-08-23.
RULE_TAG = re.compile(r"<([A-Z]{1,3})(\d{1,3})>")
# A rule's body runs from its tag to the next tag or a blank-line paragraph break.
VIOLATION = re.compile(r"(Violation|VIOLATION|PENALTY|Penalty)\s*:?\s*(.{0,160})")


def extract_text(pdf: str) -> str:
    """pdftotext -layout, UTF-8. Falls back to pymupdf if poppler is unavailable."""
    txt = os.path.join(tempfile.gettempdir(), "_legacy_%d.txt" % os.getpid())
    try:
        subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", pdf, txt],
                       check=True, capture_output=True)
        with io.open(txt, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except Exception:
        try:
            import pymupdf
            doc = pymupdf.open(pdf)
            return "\n".join(p.get_text() for p in doc)
        except Exception as e:  # pragma: no cover
            sys.stderr.write("cannot extract text: %s\n" % e)
            return ""
    finally:
        if os.path.exists(txt):
            try:
                os.remove(txt)
            except OSError:
                pass


def parse(pdf: str) -> dict:
    text = extract_text(pdf)
    lines = text.split("\n")
    hits = []
    for i, line in enumerate(lines):
        for m in RULE_TAG.finditer(line):
            hits.append((i, m.start(), m.group(1), m.group(2), m.group(0)))

    # Deduplicate: a tag is a DEFINITION at its first occurrence with body text following it;
    # later occurrences are cross-references. Keep the occurrence with the most following text.
    best: dict[str, tuple] = {}
    for idx, col, pfx, num, tag in hits:
        tail = lines[idx][col + len(tag):].strip()
        body = tail
        j = idx + 1
        while j < len(lines) and len(body) < 400:
            nxt = lines[j].strip()
            if not nxt or RULE_TAG.search(nxt):
                break
            body += " " + nxt
            j += 1
        body = re.sub(r"\s+", " ", body).strip()
        prev = best.get(tag)
        if prev is None or len(body) > len(prev["body"]):
            v = VIOLATION.search(body)
            best[tag] = {
                "id": tag.strip("<>"), "tag": tag, "prefix": pfx, "num": int(num),
                "line": idx + 1, "body": body[:400],
                "violation": (v.group(2).strip() if v else ""),
                "refs": 0,
            }
    for _, _, _, _, tag in hits:
        if tag in best:
            best[tag]["refs"] += 1

    rules = sorted(best.values(), key=lambda r: (r["prefix"], r["num"]))
    by_prefix: dict[str, int] = {}
    for r in rules:
        by_prefix[r["prefix"]] = by_prefix.get(r["prefix"], 0) + 1

    pages = 0
    try:
        import pymupdf
        pages = pymupdf.open(pdf).page_count
    except Exception:
        pass

    return {
        "file": os.path.basename(pdf), "pages": pages,
        "rules": rules, "total": len(rules), "by_prefix": by_prefix,
        "total_tag_occurrences": len(hits),
        "with_violation": sum(1 for r in rules if r["violation"]),
        "empty_body": [r["id"] for r in rules if len(r["body"]) < 15],
    }


def report(r: dict) -> None:
    sys.stdout.write("### %s: %dpp rules=%d (%s) violations=%d tag-occurrences=%d\n" % (
        r["file"], r["pages"], r["total"],
        " ".join("%s:%d" % kv for kv in sorted(r["by_prefix"].items())),
        r["with_violation"], r["total_tag_occurrences"]))
    if r["empty_body"]:
        sys.stdout.write("   !! %d rules extracted with no body (check by hand): %s\n" % (
            len(r["empty_body"]), " ".join(r["empty_body"][:10])))
    if r["total"] == 0:
        sys.stdout.write("   !! NO <TAG> RULES FOUND. Either this is a 2024-25+ manual (use\n"
                         "   !! reference/ftc_parse.py instead) or the text layer is broken.\n")


def main() -> int:
    argv = sys.argv[1:]
    if "-h" in argv or "--help" in argv:
        sys.stdout.write(__doc__ + "\n")
        return 0

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--all" in argv:
        argv.remove("--all")
        pats = ["archive/wayback", "archive"]
        pdfs = []
        for sub in pats:
            d = os.path.join(root, "manuals", sub)
            if not os.path.isdir(d):
                continue
            for fn in sorted(os.listdir(d)):
                if fn.endswith(".pdf") and re.match(r"20(1[7-9]|2[0-3])-", fn):
                    pdfs.append(os.path.join(d, fn))
        if not pdfs:
            sys.stdout.write("no legacy manuals found under manuals/\n")
            return 1
    else:
        pdfs = None  # resolved below, AFTER flags are stripped

    def take(flag):
        if flag not in argv:
            return None
        i = argv.index(flag)
        val = argv[i + 1] if i + 1 < len(argv) else None
        del argv[i:i + (2 if val else 1)]
        return val

    # Strip --tsv/--json BEFORE collecting input paths. Previously `pdfs` was built first, so the
    # OUTPUT path was swept up as a second input PDF: the tool reported on a file that did not
    # exist and wrote no TSV, while the per-file report line still looked perfectly correct.
    tsv_out, json_out = take("--tsv"), take("--json")
    if pdfs is None:
        pdfs = [a for a in argv if not a.startswith("-")]
        if not pdfs:
            sys.stdout.write(__doc__ + "\n")
            return 1

    rc = 0
    for pdf in pdfs:
        if not os.path.exists(pdf):
            sys.stdout.write("### MISSING %s\n" % pdf)
            rc = 1
            continue
        r = parse(pdf)
        report(r)
        if r["total"] == 0:
            rc = 1
        if tsv_out and len(pdfs) == 1:
            with io.open(tsv_out, "w", encoding="utf-8", newline="\n") as fh:
                fh.write("id\tprefix\tline\trefs\tviolation\tbody\n")
                for x in r["rules"]:
                    fh.write("%s\t%s\t%d\t%d\t%s\t%s\n" % (
                        x["id"], x["prefix"], x["line"], x["refs"],
                        x["violation"].replace("\t", " "), x["body"].replace("\t", " ")))
            sys.stdout.write("   wrote %s\n" % tsv_out)
        if json_out and len(pdfs) == 1:
            with io.open(json_out, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(r, fh, ensure_ascii=False, indent=1)
            sys.stdout.write("   wrote %s\n" % json_out)
    return rc


if __name__ == "__main__":
    sys.exit(main())
