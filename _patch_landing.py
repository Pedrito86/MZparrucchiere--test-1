#!/usr/bin/env python3
"""Patch minime sulle 6 nuove landing. NON tocca index.html o file preesistenti."""
import os
ROOT = "/Users/pietro/Desktop/ultima versione sito web zucchini/app"
NEW_SLUGS = ["chi-siamo","make-up","prodotti","sposa","bridal","dove-siamo"]

old = 'onclick="navigateTo(\'cookie-policy\')"'
new = 'href="../index.html?skipintro=1#cookie-policy" style="color:inherit;cursor:pointer;text-decoration:none"'
for s in NEW_SLUGS:
    p = os.path.join(ROOT,s,"index.html")
    with open(p,"r",encoding="utf-8") as f: t=f.read()
    t2 = t.replace(old,new)
    # Sistemazione anche residuo del form privacy (se esiste)
    old2 = 'onclick="navigateTo(\'cookie-policy\')"'
    t2 = t2.replace(old2, new)
    if t2 != t:
        with open(p,"w",encoding="utf-8") as f: f.write(t2)
        print(f"PATCH navigateTo -> href: {s}/")

# === SOLO bridal: cookie banner EN ===
bridal = os.path.join(ROOT,"bridal","index.html")
with open(bridal,"r",encoding="utf-8") as f: t=f.read()
IT_COOKIE = '<p>Questo sito utilizza solo <strong>cookie tecnici</strong> per garantirti la migliore esperienza di navigazione, nessun cookie di profilazione. Puoi accettare o rifiutare: la tua scelta sara\' ricordata. <a href="../index.html?skipintro=1#cookie-policy" style="color:inherit;cursor:pointer;text-decoration:none">Leggi la Cookie Policy</a></p>'
EN_COOKIE = '<p>This website uses only <strong>technical cookies</strong> to guarantee you the best browsing experience — no profiling cookies. You can accept or decline: your choice will be remembered. <a href="../index-en.html?skipintro=1#cookie-policy" style="color:inherit;cursor:pointer;text-decoration:none">Read the Cookie Policy</a></p>'
if IT_COOKIE in t:
    t = t.replace(IT_COOKIE, EN_COOKIE)
    # Anche i pulsanti
    t = t.replace('Rifiuta', 'Decline')
    t = t.replace('Accetta', 'Accept')
    with open(bridal,"w",encoding="utf-8") as f: f.write(t)
    print("PATCH cookie banner EN: bridal/")

print("Patching completato. Nessun file preesistente modificato.")
