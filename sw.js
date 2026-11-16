/* Karácsonyi Túlélőközpont – service worker v4
   Stratégia: az oldal (navigáció) először hálózatról, hiba esetén gyorsítótárból;
   a statikus fájlok (ikonok, Firebase/Leaflet kódok) gyorsítótárból, háttérben frissítve.
   Firestore / Auth hívásokat és a térképcsempéket NEM nyúljuk. */
const CACHE = 'tk-v4';
const PAGE = './karacsonyi_tulelokozpont_v4.html';
const SHELL = [PAGE, './manifest_v4.webmanifest', './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const u = new URL(req.url);

  if (u.hostname.endsWith('googleapis.com') || u.hostname.endsWith('firebaseio.com') ||
      u.hostname.endsWith('tile.openstreetmap.org') || u.pathname.startsWith('/__/')) return;

  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req)
        .then(res => { const cp = res.clone(); caches.open(CACHE).then(c => c.put(PAGE, cp)); return res; })
        .catch(() => caches.match(PAGE))
    );
    return;
  }

  if (u.origin === location.origin || u.hostname === 'www.gstatic.com' || u.hostname === 'cdnjs.cloudflare.com') {
    e.respondWith(
      caches.match(req).then(hit => {
        const net = fetch(req)
          .then(res => { if (res.ok) { const cp = res.clone(); caches.open(CACHE).then(c => c.put(req, cp)); } return res; })
          .catch(() => hit);
        return hit || net;
      })
    );
  }
});
