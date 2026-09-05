import re

FILES = [
    'dove-siamo/index.html',
    'dove-siamo/index-en.html',
]

# ==== 1) SVG: rimuovi completamente attributo onerror (inline SVG non fa richieste di rete, non serve) ====
# Pattern: ` onerror="this.onerror=...."`  (non-greedy fino a " dopo onerror=)
SVG_ONERROR_RE = re.compile(r' onerror="[^"]*"', re.DOTALL)

# ==== 2) INTRO IIFE: aggiungi guardia early return DOPO le dichiarazioni ====
# Il blocco inizia SEMPRE con:
INTRO_HEADER = """\
    const overlay = document.getElementById('introOverlay');
    const video = document.getElementById('introVideo');
    const skipBtn = document.getElementById('introSkip');
    const soundBtn = document.getElementById('introSound');
    const soundIcon = document.getElementById('introSoundIcon');
    let finished = false;
"""

INTRO_HEADER_GUARD = """\
    const overlay = document.getElementById('introOverlay');
    const video = document.getElementById('introVideo');
    const skipBtn = document.getElementById('introSkip');
    const soundBtn = document.getElementById('introSound');
    const soundIcon = document.getElementById('introSoundIcon');
    let finished = false;
    if (!overlay || !video) {
        return;
    }
"""

for f in FILES:
    with open(f, encoding='utf-8') as fp:
        c = fp.read()

    before = len(c)

    # ---- Fix 1: Rimuovi onerror inline da SVG salon-icon-original o qualsiasi SVG ----
    c_new = SVG_ONERROR_RE.sub('', c)
    removed = c.count('onerror=') - c_new.count('onerror=')
    c = c_new

    # ---- Fix 2: Aggiungi guardia early return in TUTTI i blocchi INTRO ----
    # replace_all: header con 5 const + finished => header + guardia
    n = c.count(INTRO_HEADER)
    c = c.replace(INTRO_HEADER, INTRO_HEADER_GUARD)

    print(f'{f}:')
    print(f'  Fix 1 (rimossi onerror inline SVG): {removed}')
    print(f'  Fix 2 (guardia early return intro): {n} occorrenze trovate e sostituite')
    print(f'  Lunghezza prima: {before} / dopo: {len(c)} / delta: {len(c)-before:+d}')

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)

print('\nOK.')
