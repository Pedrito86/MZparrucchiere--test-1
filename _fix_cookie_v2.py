import re

FILE = 'dove-siamo/index-en.html'
with open(FILE) as f:
    c = f.read()

NEW_CONTENT = '''                <h3>What are <span>cookies</span></h3>
                <p>Cookies are small text files that websites save on your device during browsing. They are used to ensure the proper functioning of the site, to remember your preferences and, in some cases, to collect statistical information or profiling data.</p>

                <h3>Cookies used by <span>this site</span></h3>
                <p>The <strong>MZ Parrucchieri</strong> site uses exclusively <strong>technical cookies</strong>, essential for the operation of the pages and which do not require your prior consent:</p>
                <ul>
                    <li><strong>Browsing cookies:</strong> they allow the correct display of the pages and the site's functionalities.</li>
                    <li><strong>Consent preference:</strong> your choice in the cookie banner (accept or decline) is stored locally on your device, so you will not be shown the banner again on every visit.</li>
                </ul>
                <p><strong>No profiling or tracking cookies</strong> are installed by this site: we do not collect statistical browsing data nor do we create user profiles.</p>

                <h3>Services &amp; <span>third-party</span> content</h3>
                <p>To offer you a complete experience, the site connects to some external services that may install their own cookies according to their respective policies:</p>
                <ul>
                    <li><strong>Google Fonts and Font Awesome:</strong> for the typographic characters and icons of the site.</li>
                    <li><strong>Instagram and Facebook:</strong> through the links to our official profiles in the footer.</li>
                    <li><strong>WhatsApp and Google Maps:</strong> through the contact buttons and the directions to reach our salons.</li>
                </ul>
                <p>We invite you to consult the privacy policies of these services for more details on their respective processing.</p>

                <h3>How to manage <span>cookies</span></h3>
                <p>You can at any time change your preferences or delete cookies directly from your browser settings:</p>
                <ul>
                    <li><strong>Chrome:</strong> Settings &gt; Privacy and security &gt; Cookies</li>
                    <li><strong>Safari:</strong> Preferences &gt; Privacy</li>
                    <li><strong>Firefox:</strong> Settings &gt; Privacy &amp; Security</li>
                    <li><strong>Edge:</strong> Settings &gt; Cookies and site permissions</li>
                </ul>
                <p>Disabling technical cookies may impair some functionalities of the site.</p>

                <h3>Data <span>Controller</span></h3>
                <p>The data controller is <strong>MZ Parrucchieri</strong>, with salons in Villanova di Castenaso (Via Cesare Battisti 6), Villafontana di Medicina (Piazza G. Bersani 17), Imola and Barber Shop Medicina (Via O. Argentesi 22). For any information you can contact us using the details indicated on the Contact page.</p>

                <h3>Changes to this <span>Notice</span></h3>
                <p>This Cookie Policy may be updated periodically. We invite you to consult this page to check for any changes.</p>'''

# Strategia: trova l'inizio di cookie-content e sostituisci TUTTO il contenuto interno
# Pattern: <div class="cookie-content reveal">[....]</div>  (prossimo </div> è la chiusura)
PAT_START = '<div class="cookie-content reveal">\n'
idx_start = c.find(PAT_START)
print(f'idx_start = {idx_start}')
if idx_start < 0:
    print('ERRORE PAT_START non trovato')
    exit(1)
# Trova il prossimo </div> DOPO idx_start che corrisponde alla chiusura di cookie-content
# Dobbiamo bilanciare i div. Apriamo 1 (cookie-content), poi contiamo quanti div aperti ci sono nel contenuto.
# Metodo semplice: iteriamo dalla fine di PAT_START, contiamo aperture/chiusure, quando il conto torna a 0 abbiamo la chiusura.
pos = idx_start + len(PAT_START)
depth = 1
while depth > 0 and pos < len(c):
    next_open = c.find('<div', pos)
    next_close = c.find('</div>', pos)
    if next_close < 0:
        print('ERRORE chiusura div non trovata')
        exit(1)
    if next_open >= 0 and next_open < next_close:
        depth += 1
        pos = next_open + 4
    else:
        depth -= 1
        pos = next_close + 6
# Ora pos si trova DOPO il </div> che chiude cookie-content
idx_end_div = pos - 6  # inizio di </div>

# Costruisci nuovo file
c_new = c[:idx_start + len(PAT_START)] + NEW_CONTENT + '\n            ' + c[idx_end_div:]

with open(FILE, 'w') as f:
    f.write(c_new)

print('OK: Sezione Cookie Policy EN tradotta con successo')
print(f'  Vecchia lunghezza: {len(c)}  Nuova lunghezza: {len(c_new)}')
