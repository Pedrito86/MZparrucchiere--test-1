import re

FILES = [
    'dove-siamo/index-en.html',
    'dove-siamo/index.html',
]

for f in FILES:
    print(f'=== {f} ===')
    with open(f, encoding='utf-8') as fp:
        c = fp.read()
    pattern = re.compile(r'<script[^>]*>(.*?)</script>', re.DOTALL | re.IGNORECASE)
    scripts = pattern.findall(c)
    # enumera con indici corrispondenti a evaluate (include script src="" vuoti)
    # Intanto: trova i due blocchi grandi (duplicati, uno ~38KB uno ~42KB)
    bigs = [(i, s) for i, s in enumerate(scripts) if len(s) > 30000]
    print(f'  Blocchi grandi trovati: {len(bigs)}')
    for idx, s in bigs:
        preview = s[:120].replace('\n', '\\n')
        print(f'    blocco #{idx}: len={len(s)}  start={preview}...')
    if len(bigs) >= 2:
        # diff per la prima divergenza
        a = bigs[0][1]
        b = bigs[1][1]
        minlen = min(len(a), len(b))
        first_diff = None
        for i in range(minlen):
            if a[i] != b[i]:
                first_diff = i
                break
        if first_diff is None and len(a) != len(b):
            first_diff = minlen
        if first_diff is None:
            print(f'    I due blocchi grandi SONO IDENTICI contenuto, ma lunghezze {len(a)} vs {len(b)}')
        else:
            start = max(0, first_diff - 40)
            end = min(minlen, first_diff + 80)
            print(f'    PRIMA DIVERGENZA a char #{first_diff}:')
            print(f'    blocco A (idx {bigs[0][0]}) snippet: {repr(a[start:end])}')
            print(f'    blocco B (idx {bigs[1][0]}) snippet: {repr(b[start:end])}')
    print()
