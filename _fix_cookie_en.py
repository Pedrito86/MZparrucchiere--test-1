import re

FILE = 'dove-siamo/index-en.html'
with open(FILE) as f:
    c = f.read()

OLD = '''                <span class="section-eyebrow">Privacy &amp; Trasparenza</span>
                <h2 class="section-title">Cookie <span>Policy</span></h2>
                <p class="section-sub">Ultimo aggiornamento: Agosto 2026</p>
            </div>
            <div class="cookie-content reveal">
                <h3>Cosa sono i <span>cookie</span></h3>
                <p>I cookie sono piccoli file di testo che i siti web salvano sul tuo dispositivo durante la navigazione. Servono a garantire il corretto funzionamento del sito, a ricordare le tue preferenze e, in alcuni casi, a raccogliere informazioni statistiche o di profilazione.</p>

                <h3>Cookie utilizzati da <span>questo sito</span></h3>
                <p>Il sito di <strong>MZ Parrucchieri</strong> utilizza esclusivamente <strong>technical cookies</strong>, indispensabili per il funzionamento delle pagine e non richiedono il tuo consenso preventivo:</p>
                <ul>
                    <li><strong>Cookie di navigazione:</strong> permettono la corretta visualizzazione delle pagine e delle funzionalit\u00e0 del sito.</li>
                    <li><strong>Preferenza sul consenso:</strong> la tua scelta nel banner cookie (accetta o rifiuta) viene memorizzata localmente sul tuo dispositivo, per non riproporti il banner a ogni visita.</li>
                </ul>
                <p><strong>Nessun cookie di profilazione o tracciamento</strong> viene installato da questo sito: non raccogliamo dati statistici di navigazione n\u00e9 creiamo profili degli utenti.</p>

                <h3>Services &amp; <span>third-party</span> content</h3>
                <p>Per offrirti un'esperienza completa, il sito si collega ad alcuni servizi esterni che potrebbero installare propri cookie secondo le rispettive informative:</p>
                <ul>
                    <li><strong>Google Fonts e Font Awesome:</strong> per i caratteri tipografici e le icone del sito.</li>
                    <li><strong>Instagram e Facebook:</strong> attraverso i link ai nostri profili ufficiali nel footer.</li>
                    <li><strong>WhatsApp e Google Maps:</strong> attraverso i pulsanti di contatto e le indicazioni per raggiungere i nostri saloni.</li>
                </ul>
                <p>Ti invitiamo a consultare le informative privacy di questi servizi per maggiori dettagli sui rispettivi trattamenti.</p>

                <h3>Come gestire i <span>cookie</span></h3>
                <p>Puoi in qualsiasi momento modificare le tue preferenze o eliminare i cookie direttamente dalle impostazioni del tuo browser:</p>
                <ul>
                    <li><strong>Chrome:</strong> Impostazioni &gt; Privacy e sicurezza &gt; Cookie</li>
                    <li><strong>Safari:</strong> Preferenze &gt; Privacy</li>
                    <li><strong>Firefox:</strong> Impostazioni &gt; Privacy e sicurezza</li>
                    <li><strong>Edge:</strong> Impostazioni &gt; Cookie e autorizzazioni sito</li>
                </ul>
                <p>La disabilitazione dei technical cookies potrebbe compromettere alcune funzionalit\u00e0 del sito.</p>

                <h3>Titolare del <span>trattamento</span></h3>
                <p>Il titolare del trattamento dei dati \u00e8 <strong>MZ Parrucchieri</strong>, con saloni a Villanova di Castenaso (Via Cesare Battisti 6), Villafontana di Medicina (Piazza G. Bersani 17), Imola e Barber Shop Medicina (Via O. Argentesi 22). Per qualsiasi informazione puoi contattarci ai recapiti indicati nella pagina Contact.</p>

                <h3>Modifiche a questa <span>informativa</span></h3>
                <p>Questa Cookie Policy pu\u00f2 essere aggiornata periodicamente. Ti invitiamo a consultare questa pagina per verificare eventuali modifiche.</p>'''

NEW = '''                <span class="section-eyebrow">Privacy &amp; Transparency</span>
                <h2 class="section-title">Cookie <span>Policy</span></h2>
                <p class="section-sub">Last updated: August 2026</p>
            </div>
            <div class="cookie-content reveal">
                <h3>What are <span>cookies</span></h3>
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

if OLD in c:
    c = c.replace(OLD, NEW)
    with open(FILE, 'w') as f:
        f.write(c)
    print('OK: Sezione Cookie Policy tradotta')
else:
    print('ERRORE: pattern OLD non trovato. Verifico differenze...')
    idx = c.find('Privacy &amp; Trasparenza')
    print(f'  Privacy &amp; Trasparenza trovato a posizione: {idx}')
    if idx > 0:
        snippet = c[idx:idx+300]
        print('  PRIMI 300 CHAR DOPO IL MATCH:')
        print(repr(snippet))
