#!/usr/bin/env python3
import os
R="/Users/pietro/Desktop/ultima versione sito web zucchini/app"
def c(p,pat):
    with open(os.path.join(R,p),"r",encoding="utf-8") as f: t=f.read()
    import re
    return len(re.findall(pat,t))
def first(p,n):
    with open(os.path.join(R,p),"r",encoding="utf-8") as f: return "\n".join(f.read().splitlines()[:n])
print("dove-siamo · sede-card:",        c("dove-siamo/index.html",    r"class=\"sede-card"))
print("chi-siamo · staff-sede teams:", c("chi-siamo/index.html",      r"class=\"staff-sede "))
print("prodotti  · product-brand:",    c("prodotti/index.html",       r"class=\"product-brand "))
print("make-up   · gallery items:",    c("make-up/index.html",        r"class=\"sposa-gallery-item"))
print("sposa     · award 2025:",       c("sposa/index.html",          r"award-section|wedding-awards-2025"))
print("bridal    · html lang:")
print(first("bridal/index.html", 3))
print("\nnavbar /sposa/ (links reali):")
import re
with open(os.path.join(R,"sposa/index.html")) as f: t=f.read()
navstart=t.find('<ul class="nav-links"')
navend  =t.find('</ul>', navstart)
nav=t[navstart:navend+5]
for m in re.findall(r"<li><a[^>]*>.*?</a></li>", nav): print("  ·", m)
