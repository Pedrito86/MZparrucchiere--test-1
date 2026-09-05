#!/usr/bin/env python3
import re, pathlib
files = list(pathlib.Path("/Users/pietro/Desktop/ultima versione sito web zucchini/app").glob("**/index-en.html"))
for fp in files:
    h = fp.read_text(encoding="utf-8")
    n = h.count("function pageSetLang(l)")
    it_active = 'class="lang-btn active" onclick="pageSetLang(\'it\')"' in h
    en_active = 'class="lang-btn active" onclick="pageSetLang(\'en\')"' in h
    m = re.search(r"function pageSetLang\(l\)\s*\{([^}]+)\}", h, flags=re.S)
    src = m.group(1) if m else "NONE"
    has_swap = ("window.location.href = 'index.html'" in src) and ("window.location.href = 'index-en.html'" in src)
    print(f"{fp.name:32s} parent={fp.parent.name:36s} | setLang(n={n})  IT={int(it_active)}/EN={int(en_active)} swapOK={int(has_swap)}")
