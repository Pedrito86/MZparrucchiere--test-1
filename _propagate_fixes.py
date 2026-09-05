#!/usr/bin/env python3
import re, os

FILES = [
    'salone-villanova-castenaso/index.html',
    'salone-villanova-castenaso/index-en.html',
    'salone-villafontana-medicina/index.html',
    'salone-villafontana-medicina/index-en.html',
    'salone-imola/index.html',
    'salone-imola/index-en.html',
    'barber-shop/index.html',
    'barber-shop/index-en.html',
]

# Fix 1: SyntaxError function name mangled
FIX1_OLD = '    var started = false;\n    function  {\n        if (started && !force) return;'
FIX1_NEW = '    var started = false;\n    function startVideo(force) {\n        if (started && !force) return;'

# Fix 2: tryMobileKick missing startVideo(true)
FIX2_OLD = "    var tryMobileKick = function() {  try { window.removeEventListener('touchstart', tryMobileKick, { once:true }); } catch(e){} try { window.removeEventListener('click', tryMobileKick, { once:true }); } catch(e){} try { window.removeEventListener('scroll', tryMobileKick, { once:true }); } catch(e){} };"
FIX2_NEW = "    var tryMobileKick = function() { startVideo(true); try { window.removeEventListener('touchstart', tryMobileKick, { once:true }); } catch(e){} try { window.removeEventListener('click', tryMobileKick, { once:true }); } catch(e){} try { window.removeEventListener('scroll', tryMobileKick, { once:true }); } catch(e){} };"

# Fix 3: SVG onerror inline removal
SVG_ONERROR_RE = re.compile(r' onerror="[^"]*"', re.DOTALL)

# Fix 4: Guardia INTRO dopo dichiarazioni const + let finished
INTRO_HEADER_PATTERN = re.compile(
    r"    const overlay = document\.getElementById\('introOverlay'\);\s*\n"
    r"    const video = document\.getElementById\('introVideo'\);\s*\n"
    r"    const skipBtn = document\.getElementById\('introSkip'\);\s*\n"
    r"    const soundBtn = document\.getElementById\('introSound'\);\s*\n"
    r"    const soundIcon = document\.getElementById\('introSoundIcon'\);\s*\n"
    r"    let finished = false;\s*\n",
    re.MULTILINE,
)
INTRO_GUARD = (
    "    const overlay = document.getElementById('introOverlay');\n"
    "    const video = document.getElementById('introVideo');\n"
    "    const skipBtn = document.getElementById('introSkip');\n"
    "    const soundBtn = document.getElementById('introSound');\n"
    "    const soundIcon = document.getElementById('introSoundIcon');\n"
    "    let finished = false;\n"
    "    if (!overlay || !video) { return; }\n"
)

# Fix 5: gallery let → var
GALLERY_LET_OLD = (
    "let galleryItems = [];\n"
    "let galleryIndex = 0;\n"
    "let galleryToken = 0;"
)
GALLERY_VAR_NEW = (
    "var galleryItems = [];\n"
    "var galleryIndex = 0;\n"
    "var galleryToken = 0;"
)

# Fix 6: revealObserver const → var
REVEAL_CONST_OLD = (
    "// ===== REVEAL ON SCROLL =====\n"
    "const revealObserver = new IntersectionObserver((entries) => {\n"
    "    entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); } });\n"
    "}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });\n"
    "document.querySelectorAll('.reveal, .g-reveal').forEach(el => revealObserver.observe(el));"
)
REVEAL_VAR_NEW = (
    "// ===== REVEAL ON SCROLL =====\n"
    "var revealObserver = new IntersectionObserver((entries) => {\n"
    "    entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); } });\n"
    "}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });\n"
    "document.querySelectorAll('.reveal, .g-reveal').forEach(el => revealObserver.observe(el));"
)

for f in FILES:
    if not os.path.exists(f):
        print(f"SKIP {f} (non esiste)")
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    orig_len = len(c)
    changes = []

    if FIX1_OLD in c:
        c = c.replace(FIX1_OLD, FIX1_NEW)
        changes.append('fix1(function startVideo)')

    if FIX2_OLD in c:
        c = c.replace(FIX2_OLD, FIX2_NEW)
        changes.append('fix2(tryMobileKick)')

    new_c, n_onerror = SVG_ONERROR_RE.subn('', c)
    if n_onerror > 0:
        c = new_c
        changes.append(f'fix3(SVG onerror x{n_onerror})')

    c, n_guard = INTRO_HEADER_PATTERN.subn(INTRO_GUARD, c)
    if n_guard > 0:
        changes.append(f'fix4(intro guardia x{n_guard})')

    if GALLERY_LET_OLD in c:
        cnt = c.count(GALLERY_LET_OLD)
        c = c.replace(GALLERY_LET_OLD, GALLERY_VAR_NEW)
        changes.append(f'fix5(gallery let→var x{cnt})')

    if REVEAL_CONST_OLD in c:
        cnt = c.count(REVEAL_CONST_OLD)
        c = c.replace(REVEAL_CONST_OLD, REVEAL_VAR_NEW)
        changes.append(f'fix6(reveal const→var x{cnt})')

    if len(c) == orig_len and not changes:
        print(f"-- {f}: NESSUNA MODIFICA")
        continue

    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
    print(f"OK {f}: {', '.join(changes)}")
