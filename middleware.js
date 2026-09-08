// Vercel Edge Middleware
// Scopo: restituire HTTP 410 Gone per /pagamenti e /pagamenti/
// Posizione: root del progetto (stesso livello di vercel.json)

// Configurazione matcher Vercel: intercetta solo queste due rotte precise
export const config = {
  matcher: [
    '/pagamenti',
    '/pagamenti/'
  ]
};

// Funzione middleware eseguita sull'Edge Runtime di Vercel
export function middleware() {
  // Ritorna HTTP 410 Gone utilizzando la Web API standard Response
  // Compatibile nativamente con Vercel Edge Runtime anche per progetti statici
  return new Response(
    '410 Gone - Questa pagina e\' stata rimossa definitivamente.',
    {
      status: 410,
      statusText: 'Gone',
      headers: {
        'Content-Type': 'text/plain; charset=utf-8',
        'Cache-Control': 'public, s-maxage=0, max-age=0, must-revalidate',
        'X-Robots-Tag': 'noindex, noarchive'
      }
    }
  );
}