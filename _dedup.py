#!/usr/bin/env python3
# Rimuovi duplicato pageSetLang da 4 saloni EN
import os
APP = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"
DUP = """
<script>
function pageSetLang(l) {
    try { localStorage.setItem('mz_lang', l); } catch(e) {}
    if (l === 'it') window.location.href = 'index.html';
    else if (l === 'en') window.location.href = 'index-en.html';
    else window.location.href = 'index.html';
}
</script>

</body>"""
OK_ONLY = """

</body>"""
for folder in ['salone-villanova-castenaso', 'salone-villafontana-medicina', 'salone-imola', 'barber-shop']:
    p = os.path.join(APP, folder, 'index-en.html')
    with open(p, 'r', encoding='utf-8') as f: h = f.read()
    c_before = h.count('function pageSetLang')
    if DUP in h:
        h2 = h.replace(DUP, OK_ONLY, 1)
        print(f"dedup OK: {folder}/index-en.html  {c_before} -> {h2.count('function pageSetLang')}")
    else:
        h2 = h
        print(f"pattern not found, check: {folder} count still {c_before}")
    with open(p, 'w', encoding='utf-8') as f: f.write(h2)
