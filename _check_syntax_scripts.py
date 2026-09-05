import re, os, subprocess, tempfile

def extract_scripts(filepath):
    with open(filepath, encoding='utf-8') as f:
        html = f.read()
    # matches <script>...</script> (non-greedy)
    pattern = re.compile(r'<script[^>]*>(.*?)</script>', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(html)
    return matches

FILE_IT = 'dove-siamo/index.html'
FILE_EN = 'dove-siamo/index-en.html'

scripts_it = extract_scripts(FILE_IT)
scripts_en = extract_scripts(FILE_EN)

print(f'=== {FILE_IT}: {len(scripts_it)} blocchi script ===')
for i, s in enumerate(scripts_it):
    print(f'  blocco {i+1}: {len(s)} chars  first 80: {repr(s[:80])}')

print(f'\n=== {FILE_EN}: {len(scripts_en)} blocchi script ===')
for i, s in enumerate(scripts_en):
    print(f'  blocco {i+1}: {len(s)} chars  first 80: {repr(s[:80])}')

# Verifica node disponibile
HAS_NODE = False
try:
    r = subprocess.run(['node', '--version'], capture_output=True, text=True, timeout=5)
    HAS_NODE = r.returncode == 0
    print(f'\nNode disponibile: {r.stdout.strip()}')
except Exception as e:
    print(f'\nNode NON disponibile: {e}')

if HAS_NODE:
    for fname, scripts in [(FILE_IT, scripts_it), (FILE_EN, scripts_en)]:
        print(f'\n--- node --check su {fname} ---')
        for i, s in enumerate(scripts):
            if not s.strip():
                print(f'  blocco {i+1}: VUOTO, skip')
                continue
            with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as tf:
                tf.write(s)
                tf_path = tf.name
            try:
                r = subprocess.run(['node', '--check', tf_path], capture_output=True, text=True, timeout=10)
                if r.returncode == 0:
                    print(f'  blocco {i+1}: OK')
                else:
                    print(f'  blocco {i+1}: ❌ SYNTAX ERROR')
                    lines = r.stderr.splitlines()
                    for ln in lines[:8]:
                        print(f'       {ln}')
            finally:
                try: os.unlink(tf_path)
                except: pass
else:
    # Fallback: conta {}, (), [] per blocco
    def count_balance(s, op, cl):
        return s.count(op) - s.count(cl)
    for fname, scripts in [(FILE_IT, scripts_it), (FILE_EN, scripts_en)]:
        print(f'\n--- Bilanciamento simboli su {fname} ---')
        for i, s in enumerate(scripts):
            b = count_balance(s, '{', '}')
            p = count_balance(s, '(', ')')
            br = count_balance(s, '[', ']')
            status = 'OK' if (b==0 and p==0 and br==0) else '⚠️ '
            print(f'  blocco {i+1}: {status}  {{}}: {b:+d}  (): {p:+d}  []: {br:+d}  len: {len(s)}')
