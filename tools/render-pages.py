#!/usr/bin/env python3
"""render-pages.py -- turn manual pages into PNGs you can hand to Claude as images.

WHY THIS EXISTS
    The two most valuable things in a kickoff manual -- the FIELD diagram (Section 9 ARENA)
    and the SCORING table (Section 10 Game Details) -- are the two things text extraction
    handles worst. Figures vanish entirely; multi-column scoring tables interleave. You must
    look at those pages as pictures.
    `pdfimages` is NOT installed on this machine, so this uses pymupdf's page rasteriser,
    which is better anyway: it renders the composed page (art + labels + callouts) rather
    than the disembodied embedded bitmaps.

USAGE
    python tools/render-pages.py <manual.pdf> [--sections 8,9,10,11] [--pages 60-75]
                                 [--dpi 150] [--out DIR] [--max-mb 4.5]

    # the kickoff default: renders Game Overview / ARENA / Game Details / Game Rules
    python tools/render-pages.py manuals/2026-27_BIOBUZZ/BIOBUZZ_Competition_Manual_V1.pdf

    --sections   top-level manual section numbers; page ranges are read from the PDF outline
    --pages      explicit 1-based page ranges, e.g. "60-75,88"  (overrides --sections)
    --dpi        150 is readable for tables; 200 for dense field dimensions; 100 to save size
    --max-mb     shrink DPI automatically until every page is under this size

OUTPUT
    <out>/p<NNN>_<section-slug>.png plus a MANIFEST.txt listing what to upload in what order.
"""
import argparse, os, re, sys

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required:  python -m pip install pymupdf")

DEFAULT_SECTIONS = [8, 9, 10, 11]          # Game Overview, ARENA, Game Details, Game Rules (G)


def slug(text, n=38):
    s = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return s[:n] or "page"


def section_ranges(doc):
    """Map top-level section number -> (title, first_page, last_page), 1-based inclusive."""
    tops = [(lvl, title, pg) for lvl, title, pg in doc.get_toc() if lvl == 1]
    out = {}
    for i, (_, title, pg) in enumerate(tops):
        m = re.match(r"\s*(\d+)\s+(.*)", title)
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


def main():
    ap = argparse.ArgumentParser(add_help=True, description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--sections", default=",".join(map(str, DEFAULT_SECTIONS)))
    ap.add_argument("--pages", default=None)
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--out", default=None)
    ap.add_argument("--max-mb", type=float, default=4.5)
    a = ap.parse_args()

    if not os.path.exists(a.pdf):
        sys.exit(f"no such file: {a.pdf}")
    doc = pymupdf.open(a.pdf)
    outdir = a.out or os.path.join(os.path.dirname(os.path.abspath(a.pdf)),
                                   "figures_" + os.path.splitext(os.path.basename(a.pdf))[0])
    os.makedirs(outdir, exist_ok=True)

    ranges = section_ranges(doc)
    labels = {}
    if a.pages:
        pages = parse_pages(a.pages, doc.page_count)
        for p in pages:
            labels[p] = next((slug(t) for _, (t, s, e) in ranges.items() if s <= p <= e), "page")
    else:
        pages = []
        for tok in a.sections.split(","):
            tok = tok.strip()
            if not tok:
                continue
            sec = int(tok)
            if sec not in ranges:
                print(f"   ! section {sec} not in the PDF outline -- skipped")
                continue
            title, s, e = ranges[sec]
            for p in range(s, e + 1):
                pages.append(p)
                labels[p] = f"s{sec}-{slug(title)}"
        if not pages:
            sys.exit("nothing to render: the outline has none of the requested sections.\n"
                     "Fall back to explicit pages, e.g.  --pages 60-75")

    pages = sorted(set(pages))
    print(f"== rendering {len(pages)} page(s) from {os.path.basename(a.pdf)} "
          f"({doc.page_count}pp) at {a.dpi} dpi")
    if ranges:
        print("== section map from the PDF outline:")
        for sec in sorted(ranges):
            t, s, e = ranges[sec]
            print(f"     {sec:>2}  pp.{s:>3}-{e:<3}  {t}")

    manifest, total = [], 0
    for p in pages:
        page = doc[p - 1]
        dpi = a.dpi
        while True:
            pix = page.get_pixmap(dpi=dpi)
            name = f"p{p:03d}_{labels.get(p, 'page')}.png"
            path = os.path.join(outdir, name)
            pix.save(path)
            mb = os.path.getsize(path) / 1e6
            if mb <= a.max_mb or dpi <= 72:
                break
            dpi = int(dpi * 0.75)          # too big for an upload -- step down and retry
        total += mb
        manifest.append((p, name, round(mb, 2), dpi))
        print(f"   p{p:>3}  {name}  {mb:.2f} MB @ {dpi} dpi")

    mpath = os.path.join(outdir, "MANIFEST.txt")
    with open(mpath, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"# rendered from {os.path.basename(a.pdf)} ({doc.page_count} pages)\n")
        fh.write("# Upload these to Claude in this order, alongside the text extract.\n")
        fh.write("# The ARENA pages answer field geometry; the Game Details pages carry the\n")
        fh.write("# scoring table. Read the scoring PROSE in the text extract, not off the image.\n\n")
        for p, name, mb, dpi in manifest:
            fh.write(f"page {p:>3}\t{name}\t{mb} MB\t{dpi} dpi\n")
        fh.write(f"\ntotal\t{total:.2f} MB\t{len(manifest)} images\n")
    print(f"== {len(manifest)} image(s), {total:.1f} MB total -> {outdir}")
    print(f"== manifest: {mpath}")
    if total > 25:
        print("   ! That is a lot to upload at once. Render ARENA (s9) and Game Details (s10)")
        print("   ! first, run the review on those, then add the rest.")
    doc.close()


if __name__ == "__main__":
    main()
