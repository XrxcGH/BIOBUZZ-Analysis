#!/usr/bin/env python3
"""extract-tables.py -- recover the manual's TABLES by geometry, not by flattened text.

WHY THIS EXISTS  (this is a measured failure, not a theoretical one)
    The single most important artifact in a kickoff manual is the point-values table in
    Section 10. `pdftotext -layout` mangles it. Measured on the 2025-26 DECODE manual,
    Table 10-2 came out of `pdftotext -layout` with the row labels and the numbers on
    DIFFERENT lines -- "Fully returned to BASE" had no number beside it and the values
    5 / 10 / 10 floated free at the bottom of the block. An AI handed that text builds a
    WRONG scoring model, which then poisons every downstream strategy decision.

    `pymupdf`'s table finder reads the same page by ruling lines and cell geometry and
    recovers the rows correctly (verified on that same DECODE page, 2026-08-22).

    The same applies to Table 12-1 (legal motors), 12-2 (servo spec test), 12-7/12-8
    (power and wire sizing), Table 6-1 (awards per event) and the RP-threshold table.

USAGE
    python tools/extract-tables.py <manual.pdf> [--pages 79-94] [--sections 9,10,13]
                                   [--out DIR] [--min-rows 2]

    # kickoff default: every table in the whole manual
    python tools/extract-tables.py manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V1.pdf

    # just the game-details pages
    python tools/extract-tables.py <manual.pdf> --sections 10

OUTPUT  (in <out>, default <manual-dir>/tables_<stem>/)
    TABLES.md          every table as GitHub markdown, captioned with the nearest
                       "Table N-M:" caption found on the page, in page order
    tables.tsv         one row per table cell-row, tab separated, for grep/awk
    INDEX.txt          page / caption / rows / cols, so you can find one fast

VERIFY BEFORE YOU TRUST
    Table finders fail on borderless tables and on tables split across a page break.
    INDEX.txt flags any table whose first column is empty (a likely split) with SPLIT?.
    For anything you are about to base a scoring model on, also look at the rendered page:
        python tools/render-pages.py <manual.pdf> --sections 10
"""
import argparse, io, os, re, sys

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required:  python -m pip install pymupdf")

CAPTION = re.compile(r"(Table\s+\d+-\d+\s*:?[^\n]{0,90})")


def clean(s):
    if not s:
        return ""
    s = (s.replace("\n", " ").replace("−", "-").replace("–", "-").replace("—", "--")
          .replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
          .replace("�", "-").replace("|", "/"))
    return re.sub(r"\s+", " ", s).strip()


def section_ranges(doc):
    tops = [(lvl, t, pg) for lvl, t, pg in doc.get_toc() if lvl == 1]
    out = {}
    for i, (_, t, pg) in enumerate(tops):
        m = re.match(r"\s*(\d+)\s+(.*)", t)
        if not m:
            continue
        end = (tops[i + 1][2] - 1) if i + 1 < len(tops) else doc.page_count
        out[int(m.group(1))] = (m.group(2).strip(), pg, max(pg, end))
    return out


def parse_pages(spec, maxpage):
    pages = []
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            a, b = chunk.split("-", 1)
            pages += list(range(int(a), int(b) + 1))
        else:
            pages.append(int(chunk))
    return [p for p in pages if 1 <= p <= maxpage]


def captions_on(page):
    """Every 'Table N-M: ...' caption on the page with its y position, so a page holding
    several tables gets each one labelled with the caption physically nearest it rather
    than all three inheriting the first caption on the page."""
    out = []
    for b in page.get_text("blocks"):
        x0, y0, x1, y1, txt = b[0], b[1], b[2], b[3], b[4]
        for m in CAPTION.finditer(txt or ""):
            out.append((y0, clean(m.group(1))))
    out.sort()
    return out


def caption_for(caps, bbox, used):
    """Nearest unused caption above the table; fall back to nearest below, then any."""
    if not caps:
        return "(no caption on page)"
    top = bbox[1]
    above = [(top - y, i) for i, (y, _) in enumerate(caps) if y <= top + 6 and i not in used]
    below = [(y - top, i) for i, (y, _) in enumerate(caps) if y > top + 6 and i not in used]
    pick = min(above or below or [(0, i) for i in range(len(caps))])[1]
    used.add(pick)
    return caps[pick][1]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--pages", default=None)
    ap.add_argument("--sections", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--min-rows", type=int, default=2)
    a = ap.parse_args()

    if not os.path.exists(a.pdf):
        sys.exit("no such file: " + a.pdf)
    doc = pymupdf.open(a.pdf)
    stem = os.path.splitext(os.path.basename(a.pdf))[0]
    outdir = a.out or os.path.join(os.path.dirname(os.path.abspath(a.pdf)), "tables_" + stem)
    os.makedirs(outdir, exist_ok=True)

    if a.pages:
        pages = parse_pages(a.pages, doc.page_count)
    elif a.sections:
        ranges = section_ranges(doc)
        pages = []
        for tok in a.sections.split(","):
            sec = int(tok.strip())
            if sec in ranges:
                _, s, e = ranges[sec]
                pages += list(range(s, e + 1))
            else:
                print("   ! section %s not in the PDF outline -- skipped" % sec)
        pages = sorted(set(pages))
    else:
        pages = list(range(1, doc.page_count + 1))

    md = io.open(os.path.join(outdir, "TABLES.md"), "w", encoding="utf-8", newline="\n")
    tsv = io.open(os.path.join(outdir, "tables.tsv"), "w", encoding="utf-8", newline="\n")
    idx = io.open(os.path.join(outdir, "INDEX.txt"), "w", encoding="utf-8", newline="\n")
    md.write("# %s - tables recovered by geometry\n\n" % stem)
    md.write("Extracted with `tools/extract-tables.py` (pymupdf `find_tables`). "
             "Use these, not the `pdftotext -layout` text, for anything numeric.\n\n")
    tsv.write("page\ttable_no\tcaption\trow_no\tcells\n")
    idx.write("page  table  rows x cols  flags  caption\n")

    n_tables = 0
    for p in pages:
        page = doc[p - 1]
        try:
            found = page.find_tables()
        except Exception as e:                       # noqa: BLE001 - report, never abort a run
            idx.write("%4d  ERROR  %s\n" % (p, str(e)[:60]))
            continue
        caps, used = captions_on(page), set()
        for ti, t in enumerate(found.tables):
            rows = [[clean(c) for c in r] for r in t.extract()]
            rows = [r for r in rows if any(c for c in r)]
            if len(rows) < a.min_rows:
                continue
            n_tables += 1
            cap = caption_for(caps, t.bbox, used)
            # Only flag a genuine continuation: an empty first cell is normal for a merged
            # header, so also require the table to start high on the page (no caption above
            # it) -- otherwise every awards-criteria table gets a false SPLIT? and the flag
            # stops meaning anything.
            split = "SPLIT?" if (rows and not rows[0][0] and t.bbox[1] < 130) else "      "
            idx.write("%4d  %5d  %3d x %-3d  %s %s\n"
                      % (p, ti + 1, len(rows), max(len(r) for r in rows), split, cap))
            md.write("## p.%d - %s\n\n" % (p, cap))
            if split.strip():
                md.write("> First cell empty - this table may be a continuation of one on the "
                         "previous page, or have a merged header. Check the rendered page.\n\n")
            width = max(len(r) for r in rows)
            for r in rows:
                r += [""] * (width - len(r))
            md.write("| " + " | ".join(rows[0]) + " |\n")
            md.write("|" + "---|" * width + "\n")
            for r in rows[1:]:
                md.write("| " + " | ".join(r) + " |\n")
            md.write("\n")
            for ri, r in enumerate(rows):
                tsv.write("%d\t%d\t%s\t%d\t%s\n" % (p, ti + 1, cap, ri, "\t".join(r)))

    md.close()
    tsv.close()
    idx.close()
    doc.close()
    print("== %s: %d tables from %d page(s) -> %s" % (stem, n_tables, len(pages), outdir))
    print("     TABLES.md / tables.tsv / INDEX.txt")
    if n_tables == 0:
        print("   !! No tables found. Either the pages have none, or FIRST changed how tables")
        print("   !! are drawn. Render the pages instead: python tools/render-pages.py <pdf>")


if __name__ == "__main__":
    main()
