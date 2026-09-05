#!/usr/bin/env python3
import re, sys, difflib
from html import unescape

files = ['dove-siamo/index-en.html', 'dove-siamo/index.html']

for f in files:
    print(f"\n=== {f} ===")
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    scripts = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.DOTALL)
    bigs = [(i, s) for i, s in enumerate(scripts) if len(s) > 30000]
    print(f"  Blocchi grandi trovati: {len(bigs)}")
    for i, s in bigs:
        print(f"    idx={i} len={len(s)}")
    if len(bigs) < 2:
        continue
    a_idx, a = bigs[0]
    b_idx, b = bigs[1]
    a_lines = a.splitlines(keepends=True)
    b_lines = b.splitlines(keepends=True)
    diff = list(difflib.unified_diff(a_lines, b_lines, fromfile=f'blocco_{a_idx}_buggy(len{len(a)})', tofile=f'blocco_{b_idx}_buono(len{len(b)})', n=3))
    print(f"\n  Diff prime 150 righe (non mostro le uguali, solo +/- ):")
    out = []
    for line in diff:
        if line.startswith('+') or line.startswith('-') or line.startswith('@@'):
            out.append(line.rstrip())
    for l in out[:150]:
        print("    " + l)
    if len(out) > 150:
        print(f"    ... [altre {len(out)-150} righe di diff omesse]")
