import json,os,html
import os
OUT=os.environ.get('OUT','/home/claude/landing'); BASE='https://bela23ah.github.io/mariahrmageddon/'
os.makedirs(OUT,exist_ok=True)
FB='https://www.facebook.com/Kaefte'
FBG='https://www.facebook.com/mariahrmageddon'
REG=[]  # automatikus oldallista (sitemap)
KWHU='Mariahrmageddon, Whamageddon, Feliznavidageddon, karácsonyi kihívás, Last Christmas kerülése, Mariah Carey karácsonyi dal, Wham'+"'"+'d, Carey'+"'"+'d Away, Feliminated, karácsonyi túlélőjáték, dalmentes karácsonyi filmek, Kecskeméti Fiatalok Társasága, Káefte'
KWEN='Whamageddon, Mariahgeddon, Mariahpocalypse, Mariah Carey Christmas challenge, Last Christmas game, Wham'+"'"+'d, Carey'+"'"+'d Away, Feliminated, Feliz Navidad challenge, Christmas survival game, Wham-safe Christmas films'
CSS='''<style>
:root{--bg:#eef6fc;--card:#fff;--ink:#16324f;--mut:#5f7a93;--blue:#2c6fa8;--red:#d7263d;--gold:#e0932b;--line:#d3e3f1}
@media(prefers-color-scheme:dark){:root{--bg:#0f2742;--card:#16314f;--ink:#e8f2fb;--mut:#9db6cc;--line:#2a4a6b}}
*{box-sizing:border-box}body{margin:0;background:linear-gradient(var(--bg),var(--bg));color:var(--ink);font:17px/1.6 system-ui,Segoe UI,Roboto,sans-serif}
header{max-width:760px;margin:auto;padding:14px 16px 0;display:flex;gap:12px;align-items:center;justify-content:space-between;flex-wrap:wrap}
header a.brand{font-weight:800;color:var(--ink);text-decoration:none;letter-spacing:.02em}
nav.sub{max-width:760px;margin:auto;padding:6px 16px;display:flex;gap:8px;flex-wrap:wrap}nav.sub a{font-size:.8rem;text-transform:uppercase;letter-spacing:.05em;font-weight:700;color:var(--blue);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:5px 11px;background:var(--card)}
main{max-width:760px;margin:auto;padding:8px 16px 40px}h1{font-size:2rem;line-height:1.15;margin:.6em 0 .3em;text-wrap:balance}h2{font-size:1.25rem;margin:1.6em 0 .4em}
.lead{font-size:1.1rem;color:var(--mut);margin:.2em 0 1em}.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin:12px 0}
.cta{display:inline-block;background:var(--red);color:#fff;text-decoration:none;font-weight:700;border-radius:14px;padding:12px 20px;margin:8px 8px 8px 0}.cta.alt{background:var(--blue)}
ul,ol{padding-left:1.2em}li{margin:.25em 0}table{border-collapse:collapse;width:100%;font-size:.95rem}td,th{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
.kw{display:flex;flex-wrap:wrap;gap:6px;margin:.6em 0}.kw span{background:var(--card);border:1px solid var(--line);border-radius:999px;padding:3px 10px;font-size:.78rem;color:var(--mut)}
footer{max-width:760px;margin:auto;padding:0 16px 40px;color:var(--mut);font-size:.85rem;text-align:center}footer a{color:var(--blue);margin:0 6px}
.src{font-size:.85rem;color:var(--mut)}a{color:var(--blue)}.share a,.share button{display:inline-block;margin:4px 6px 4px 0;padding:8px 12px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--ink);font:inherit;font-size:.9rem;text-decoration:none;cursor:pointer}
</style>'''
HUNAV=[('funkciok.html','Funkciók'),('filmek.html','Filmek'),('szlengszotar.html','Szótár'),('index.html','Az app'),('mariahrmageddon.html','Mariahrmageddon'),('whamageddon.html','Whamageddon'),('feliznavidageddon.html','Feliznavidageddon'),('jatekmodok.html','Játékmódok'),('versenyek.html','Versenyek'),('minijatekok.html','Mini játékok'),('tortenet.html','Története'),('en.html','English')]
def page(slug,title,desc,og,body,lang='hu',faq=None,extra_head='',kw=None,alt=None):
    url=BASE+slug; REG.append(slug)
    extra_head=(f'<meta name="keywords" content="{html.escape(kw or (KWHU if lang=="hu" else KWEN))}">'+(f'<link rel="alternate" hreflang="{alt[0]}" href="{BASE}{alt[1]}"><link rel="alternate" hreflang="{lang}" href="{url}">' if alt else '')+extra_head)
    ld=[{"@context":"https://schema.org","@type":"WebPage","name":title,"url":url,"inLanguage":lang,"description":desc,"isPartOf":{"@type":"WebSite","name":"Karácsonyi Túlélőközpont","url":BASE}}]
    if faq: ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
    nav=''.join(f'<a href="{h}">{t}</a>' for h,t in (HUNAV if lang=='hu' else [('index.html?lang=en','App'),('christmas-movies.html','Christmas movies'),('features.html','Features'),('en.html','Home')]))
    brand='Karácsonyi Túlélőközpont' if lang=='hu' else 'Christmas Survival Center'
    foot='<a href="adatkezeles.html">Adatkezelés</a>·<a href="aszf.html">ÁSZF</a>·<a href="impresszum.html">Impresszum</a>·<a href="%s">Facebook (játék)</a>·<a href="%s">Káefte</a>·<a href="https://www.reddit.com/r/Mariahrmageddon/" rel="noopener">Reddit</a>'%(FBG,FB) if lang=='hu' else '<a href="privacy.html">Privacy</a>·<a href="terms.html">Terms</a>·<a href="imprint.html">Imprint</a>·<a href="%s">Facebook</a>·<a href="https://www.reddit.com/r/Mariahrmageddon/" rel="noopener">r/Mariahrmageddon</a>·<a href="features.html">Features</a>·<a href="index.html">Play the Hungarian app</a>'%FBG
    h=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{brand}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="{BASE}og/{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{html.escape(title)}"><meta name="twitter:description" content="{html.escape(desc)}"><meta name="twitter:image" content="{BASE}og/{og}">
{extra_head}<link rel="icon" href="icons/icon-192.png">{CSS}
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head><body>
<header><a class="brand" href="{'index.html' if lang=='hu' else 'en.html'}">❄ {brand}</a></header><nav class="sub">{nav}</nav>
<main>{body}</main><footer>{foot}</footer></body></html>'''
    open(f'{OUT}/{slug}','w').write(h)
CTA='<p><a class="cta" href="index.html">Belépek és játszom</a><a class="cta alt" href="szabalyok-link">Szabályok az appban</a></p>'.replace('szabalyok-link','index.html#rules')
KW='<div class="kw"><span>karácsonyi kihívás</span><span>challenge</span><span>túlélőközpont</span><span>ingyenes program</span><span>ünnepek</span></div><div class="card" style="margin:.6em 0"><b>Kerüld el!</b> A cél nem csak az, hogy ne <i>hallgasd meg</i> a dalt, hanem hogy véletlenül se <i>halld meg</i>. Készülj fel: fülhallgató, némított videók, óvatos bevásárlás.</div>'

# ---------- HU ----------
page('mariahrmageddon.html','Mariahrmageddon – a Mariah Carey-kihívás szabályai','Ingyenes karácsonyi kihívás: december 24-ig ne hallgasd meg Mariah Carey „All I Want for Christmas Is You” eredeti felvételét. Szabályok, tippek, kiesés-bejelentés.','l-mariah.png',f'''
<h1>Mariahrmageddon</h1><p class="lead">Karácsonyi challenge egyetlen szabállyal: ne hallgasd meg Mariah Carey „All I Want for Christmas Is You” című dalát december 24-ig.</p>{KW}
<h2>Hogyan működik?</h2><ol><li><b>Regisztrálsz</b> az appban, és kiválasztod a játékmódot.</li><li><b>December 1-jétől</b> kerülöd a dalt, bárhol és bármikor.</li><li><b>Ha felismered</b>, kiestél. Akár egyetlen taktusból is. Az app kiesés-bejelentő gombjával jelented, és megoszthatod.</li><li><b>Karácsonyig bent maradók</b> a túlélők.</li></ol>
<h2>Mi számít kiesésnek?</h2><p>Csak az eredeti, 1994-es felvétel. A feldolgozás, a remix és a gyerekkórus nem számít, azokat nyugodtan hallgathatod. Az számít, hogy felismerted, nem az, hogy végighallgattad.</p>
<h2>Össznépi cél</h2><p>Ha a regisztráltak legalább 10%-a karácsonyig bent marad, kollektíve túléltük. Csak a Mariahrmageddon kiesései számítanak, és december 24-ig az új meghívottak megmenthetnek mindenkit.</p>
<h2>Túlélési tippek</h2><ul><li>Fülhallgató a plázában és a karácsonyi vásáron.</li><li>Kerüld a rádiót és a háttérzenés üzleteket.</li><li>Az appban a biztonságos helyek térképén Mariah-mentes zónákat találsz.</li></ul>
{CTA}<p class="src">A kihívás ingyenes. A szervező a Kecskeméti Fiatalok Társasága (<a href="{FB}">Káefte</a>). A játék nemzetközi „testvére” a Whamageddon és a Mariahpocalypse néven is ismert változat. <a href="tortenet.html">A története</a>.</p>''',faq=[('Mi az a Mariahrmageddon?','Ingyenes karácsonyi kihívás: december 24-ig nem hallgathatod meg Mariah Carey All I Want for Christmas Is You című dalának eredeti felvételét.'),('Mi számít kiesésnek?','Ha felismered az eredeti felvételt, akár egyetlen taktusból. A feldolgozás és a remix nem számít.'),('Mikor kezdődik és ér véget?','December 1-jén kezdődik, és december 24-én éjfélkor ér véget.')])

page('whamageddon.html','Whamageddon – ne hallgasd meg a Last Christmas-t','A Whamageddon a Wham! „Last Christmas” kerülése karácsonyig. Ingyenes challenge: szabályok, kiesés-bejelentés, túlélési tippek.','l-wham.png',f'''
<h1>Whamageddon</h1><p class="lead">Wham!: „Last Christmas” (1984). A cél: december 24-ig ne hallgasd meg az eredeti felvételt.</p>{KW}
<h2>Szabályok</h2><ul><li>Csak az eredeti Wham!-felvétel számít. A feldolgozások nem.</li><li>Ha felismered, kiestél. Elég egyetlen taktus is.</li><li>Az időszak december 1-jétől december 24-ig tart (éjfélkor ér véget).</li></ul>
<h2>Honnan jön?</h2><p>A Whamageddon dán barátok ötlete, a CBS News beszámolója szerint a 2000-es évek közepén találták ki, a Facebook-oldala 2016-ban indult el. A játék azóta nemzetközi lett. <a href="tortenet.html">Részletek</a>.</p>
<h2>A mi változatunk</h2><p>A Karácsonyi Túlélőközpontban a Whamageddon a második front. Hagyományos módban a Mariahrmageddon után, Die Hard módban egyszerre indul a másik két fronttal.</p>
<h2>Mit jelent, ha valakit „megwhamtak”?</h2><p>Azt, hogy elkapta a Last Christmas, és kiesett. Ilyenkor a legjobb, amit tehetsz: bejelented, és megosztod.</p>
{CTA}''',faq=[('Mi az a Whamageddon?','Karácsonyi kihívás: december 24-ig nem szabad meghallgatni a Wham! Last Christmas című dalának eredeti felvételét.'),('A feldolgozás számít?','Nem, csak az eredeti Wham!-felvétel.')])

page('feliznavidageddon.html','Feliznavidageddon – a harmadik karácsonyi front','A Feliznavidageddon a Feliz Navidad kerülése karácsonyig. A kihívást a Kecskeméti Fiatalok Társasága találta ki, ingyenes challenge.','l-feliz.png',f'''
<h1>Feliznavidageddon</h1><p class="lead">José Feliciano: „Feliz Navidad” (1970). A harmadik front: ne hallgasd meg az eredeti felvételt december 24-ig.</p>{KW}
<h2>Mi ez?</h2><p>A Feliznavidageddon a Mariahrmageddon és a Whamageddon mellé kitalált harmadik kihívás. Az ötlet a Kecskeméti Fiatalok Társaságától jön.</p>
<h2>Szabályok</h2><ul><li>Csak az eredeti felvétel számít, a feldolgozás nem.</li><li>Ha felismerted, kiestél, akár egyetlen taktusból.</li><li>Hagyományos módban a Whamageddon után jön, Die Hard módban mindhárom egyszerre.</li></ul>
{CTA}''',faq=[('Mi az a Feliznavidageddon?','A Feliz Navidad eredeti felvételének kerülése december 24-ig. A kihívást a Kecskeméti Fiatalok Társasága találta ki.')])

page('jatekmodok.html','Játékmódok: Hagyományos és Die Hard','Két játékmód a három karácsonyi kihíváshoz: a láncolt Hagyományos és az egyszerre induló Die Hard.','l-modes.png',f'''
<h1>Játékmódok</h1><p class="lead">Két mód a három fronthoz. Válassz, ami illik a vérmérsékletedhez.</p>{KW}
<table><tr><th></th><th>Hagyományos</th><th>Die Hard</th></tr><tr><td>Menete</td><td>Egymás után: Mariahrmageddon, Whamageddon, Feliznavidageddon</td><td>Mindhárom egyszerre indul</td></tr><tr><td>Kiesés</td><td>Az egyik elbukásával jön a következő front</td><td>Bármelyik bukása a végét jelenti</td></tr><tr><td>Neked való, ha</td><td>szereted a fokozatosságot</td><td>mindent vagy semmit akarsz</td></tr></table>
<h2>Átválthatok?</h2><p>Hagyományosból Die Hard módra addig, amíg nem estél ki sehol.</p>{CTA}''')

page('versenyek.html','Versenyek: össznépi cél, települések, baráti csapatok','Az össznépi 10%-os cél, a települések versenye és a baráti csapatok: ki éli túl karácsonyig? Ingyenes karácsonyi challenge.','l-contests.png',f'''
<h1>Versenyek</h1><p class="lead">Nem csak magadnak játszol. Három közösségi verseny is megy a kihívás alatt.</p>{KW}
<h2>Össznépi cél</h2><p>Ha a regisztráltak legalább 10%-a karácsonyig bent marad, kollektíve túléltük. December 24-ig bármikor kicsúszhatunk, de az új meghívottak megmenthetnek mindenkit. Csak a Mariahrmageddon kiesései számítanak.</p>
<h2>Települések versenye</h2><p>Az számít, hányan élték túl az adott településről (ezért érdemes sokaknak jelentkezni). Mellette az arány is látszik.</p>
<h2>Baráti csapatok</h2><p>Hozz létre csapatot a barátaiddal vagy a munkatársaiddal, és nézzétek, ki bírja tovább. Egy játékos több csapatnak is tagja lehet.</p>
<h2>XP-ranglista</h2><p>A játék közben XP-t gyűjthetsz, és szintet léphetsz. A ranglista a játékosok vidám versenye.</p>{CTA}''')

page('minijatekok.html','Mini játékok a karácsonyi kihíváshoz','Fülvédő futam, Betörők ellen, Toronyépítő és karácsonyi bingó: rövid játékok XP-ért a Karácsonyi Túlélőközpontban.','l-mini.png',f'''
<h1>Mini játékok</h1><p class="lead">Rövid játékok a várakozáshoz. Belépve XP-t és helyet kapsz a ranglistán, és értesítést is, ha valaki megdönti a rekordod.</p>{KW}
<ul><li><b>Fülvédő futam:</b> éld túl a 24 napot, 1 perc játék = 1 nap. Ugorj és bújj le a hanghullámok elől.</li><li><b>Betörők ellen:</b> idle clicker. Építs csapdákat, és védd meg a nagy házat két betörőtől.</li><li><b>Toronyépítő:</b> rakd egymásra az emeleteket. A menetnek előre megadott emeletszáma van (20, 27, 34…), a megnyert torony tetejére felirat kerül.</li><li><b>Karácsonyi bingó:</b> pipáld, amit az ünnepeken megélsz, a családi vitáktól a hírekig.</li></ul>{CTA}''')

page('tortenet.html','A Mariahrmageddon és társai története','Honnan jön a Whamageddon, mi a Mariahpocalypse, és hogyan lett Magyarországon Mariahrmageddon és Feliznavidageddon.','l-history.png',f'''
<h1>A története</h1><p class="lead">Három dal, egy játék. Honnan jön, és hol tartunk?</p>{KW}
<h2>Whamageddon: az eredeti</h2><p>Világszerte a Whamageddon a legismertebb: dán barátok ötlete, a CBS News beszámolója szerint Thomas Mertz és barátai találták ki a 2000-es évek közepén. A Facebook-oldal 2016-ban indult, ekkor lett széles körben ismert. Ők kezdték, a hivatalos oldaluk a <a href="https://whamageddon.com/" rel="noopener">whamageddon.com</a>. A szabály egyszerű: december 1-től karácsonyig nem szabad meghallani a Wham!-féle Last Christmas eredeti felvételét.</p>
<h2>Mariah Carey: Mariahpocalypse és Mariahgeddon</h2><p>A Mariah Carey-dal kerülése külföldön is él, több helyen Mariahpocalypse vagy Mariahgeddon néven. A saját leírása szerint a Whamageddon „elhidegült unokatestvére”, és Black Fridaytől december 26-ig tart. Magyarországon Mariahrmageddon néven ismert, és a szervezése főleg a Kecskeméti Fiatalok Társaságához (Káefte) kötődik.</p>
<h2>Feliznavidageddon</h2><p>A harmadik frontot a Káefte találta ki, teljesen saját ötlet, hogy a láncolt „túlélősorozat” kerek legyen: Mariahrmageddon, Whamageddon, Feliznavidageddon.</p>
<h2>Miért Mariahrmageddon, és nem Mariahpocalypse?</h2><p>A Mariahpocalypse angolul tökéletes, de magyarul (Mariahpokalipszis) nyelvtörő. A Mariahrmageddon rövidebb, könnyebben megy a szánkon, és természetesen a Whamageddont tükrözi. Nemzetközi ikertestvérének a Mariahpocalypse-t (és a Mariahgeddont) tekintjük.</p><h2>Miért a Feliz Navidad a harmadik dal?</h2><p>Magyarországon is jellemzően a Rockin' Around the Christmas Tree áll feljebb a karácsonyi listákon (nagyjából az 5. hely körül), a Feliz Navidad inkább a 15. környékén. Mivel ez az utolsó vigaszág, miután Mariah és a Wham! kiejtett, nem akartunk a végére még egy szinte lehetetlen top 5-ös slágert, így igazságosabb esélye van valakinek karácsonyig túlélni. Ráadásul magyar nyelvű országban a kétnyelvű (spanyol–angol) dal külön vicces, amikor lesből támad egy plázában vagy a rádióban. Ha ez túl kegyes, ott a Die Hard mód, ahol mind a hármat egyszerre kerülöd.</p><h2>Szlengszótár</h2><p>Ezeket a kifejezéseket nem fordítjuk, így él a nemzetközi játékban: <b>Wham'd</b> (elkapott a Last Christmas), <b>Carey'd Away</b> (elkapott Mariah), <b>Whamhalla</b> (a kiesettek mennyországa; a barátaidat tilos direkt oda küldeni), <b>un-Whamly</b> (a játék szellemével ellentétes, szemét viselkedés).</p>
<h2>Miért érdemes?</h2><p>Mert ingyenes, nevetséges, és karácsony közben mégis összehoz embereket: baráti csapatokat, településeket, az egész országot.</p>
<p class="src">Források: <a href="https://www.cbsnews.com/amp/news/what-is-whamageddon-wham-last-christmas-game-denmark-who-created-viral-trend-thomas-mertz">CBS News a Whamageddonról</a>, <a href="https://sites.google.com/view/Mariahpocalypse">Mariahpocalypse</a>, <a href="https://whamageddon.com/">whamageddon.com</a>.</p>{CTA}''')

# ---------- EN ----------
EN=f'''
<h1>Mariahrmageddon · Whamageddon · Feliznavidageddon</h1><p class="lead">The free Christmas song survival challenge. Don't hear them until midnight on December 24.</p>
<div class="kw"><span>christmas challenge</span><span>whamageddon</span><span>mariah carey</span><span>free game</span><span>holidays</span></div>
<div class="card"><p style="font-size:1.15rem;margin:0"><b>Have fun dodging the sultry voice of Mariah, but don't get “Carey'd Away.”</b></p></div>
<div class="card"><b>Dodge it!</b> The goal is not just to avoid listening: you must not even hear it by accident. Earbuds in, videos muted, shop carefully.</div>
<h2>What does it mean to get Wham'd?</h2><p>You heard the original “Last Christmas” by Wham! after December 1. You're out. Same goes for Mariah Carey's “All I Want for Christmas Is You” (you got Carey'd Away) and José Feliciano's “Feliz Navidad”.</p>
<h2>The three fronts</h2><ul><li><b>Mariahrmageddon:</b> Mariah Carey, “All I Want for Christmas Is You” (1994).</li><li><b>Whamageddon:</b> Wham!, “Last Christmas” (1984).</li><li><b>Feliznavidageddon:</b> José Feliciano, “Feliz Navidad” (1970). Invented by the Kecskemét Youth Society.</li></ul>
<h2>Rules</h2><ol><li>Only the original recordings count. Covers and remixes are fine.</li><li>The game runs from December 1 to midnight on December 24.</li><li>Recognise it, even from one bar, and you are out. Own up and share it.</li><li>Two modes: Traditional (one front after another) or Die Hard (all three at once).</li></ol>
<h2>Why “Mariahrmageddon” and not Mariahpocalypse?</h2><p>Mariahpocalypse makes total sense in English, but in Hungarian (Mariahpokalipszis) it is a tongue-twister. Mariahrmageddon is shorter, rolls off the tongue more easily and mirrors Whamageddon. We consider Mariahpocalypse (and Mariahgeddon) its international twin.</p><h2>Why Feliz Navidad as the third song?</h2><p>Even in Hungary, Rockin' Around the Christmas Tree usually sits higher on the holiday charts (around #5), while Feliz Navidad hovers closer to #15. As the final consolation round after falling to Mariah and Wham!, we did not want another near-impossible top-5 mega-hit at the very end, which gives people a fairer fighting chance to survive until Christmas. Plus, in a Hungarian-speaking country a bilingual Spanish–English track has a uniquely funny vibe when it ambushes you in a mall or on the radio. If that sounds too merciful, there is always Die Hard mode, where you dodge all three at once.</p><h2>Slang</h2><p><b>Wham'd</b>: you got hit by Last Christmas. <b>Carey'd Away</b>: you got hit by Mariah. <b>Whamhalla</b>: where the fallen go; sending friends there on purpose is not allowed. <b>Un-Whamly</b>: against the spirit of the game.</p>
<h2>Where does it come from?</h2><p>Whamageddon is the original and by far the best known: it was started by Danish friends in the mid-2000s and took off after its Facebook page launched in 2016, according to <a href="https://www.cbsnews.com/amp/news/what-is-whamageddon-wham-last-christmas-game-denmark-who-created-viral-trend-thomas-mertz">CBS News</a>. The official site is <a href="https://whamageddon.com/">whamageddon.com</a>. The Mariah variant is also played abroad as <a href="https://sites.google.com/view/Mariahpocalypse">Mariahpocalypse</a> or Mariahgeddon; in Hungary the Kecskemét Youth Society runs it as Mariahrmageddon, and Feliznavidageddon is entirely its own invention.</p>
<p><a class="cta" href="index.html?lang=en">Open the app (English)</a></p><p class="src">The app has a HU/EN switch in the header.</p>
<div class="share"><h2>Share it</h2>
<a href="https://twitter.com/intent/tweet?text=Have%20fun%20dodging%20the%20sultry%20voice%20of%20Mariah%2C%20but%20don%27t%20get%20%22Carey%27d%20Away.%22%20%23Mariahrmageddon%20%23Whamageddon&url={BASE}en.html" rel="noopener">Share on X</a>
<a href="https://www.reddit.com/submit?url={BASE}en.html&title=Mariahrmageddon%20%7C%20Whamageddon%20%7C%20Feliznavidageddon%3A%20don%27t%20get%20Carey%27d%20Away" rel="noopener">Reddit</a>
<a href="https://www.threads.net/intent/post?text=Have%20fun%20dodging%20the%20sultry%20voice%20of%20Mariah%2C%20but%20don%27t%20get%20%22Carey%27d%20Away.%22%20{BASE}en.html" rel="noopener">Threads</a>
<a href="https://www.facebook.com/sharer/sharer.php?u={BASE}en.html" rel="noopener">Facebook</a>
<button type="button" id="cp">Copy text for 9GAG, TikTok, etc.</button></div>
'''
SCR='''<script>document.getElementById('cp').onclick=function(){var t="Have fun dodging the sultry voice of Mariah, but don't get \\"Carey'd Away.\\" #Mariahrmageddon #Whamageddon @@en.html";if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){document.getElementById('cp').textContent='Copied!'}).catch(function(){prompt('Copy:',t)});else prompt('Copy:',t)}</script>'''.replace('@@',BASE)
EN+=SCR

page('en.html',"Mariahrmageddon, Whamageddon, Feliznavidageddon: don't get Carey'd Away","Free Christmas song survival challenge. Dodge Mariah Carey, Wham! and Feliz Navidad until midnight on December 24, or get Wham'd.",'l-en.png',EN,lang='en',faq=[("What does it mean to get Wham'd?","You heard the original Last Christmas by Wham! after December 1, so you are out of the game."),("What is Mariahrmageddon?","A Christmas challenge: avoid Mariah Carey's All I Want for Christmas Is You until December 24.")],alt=('hu',''))


# ---------- AUTOMATA ALOLDAL-ÉPÍTŐ: a filmek az app adataiból (FILMS), így az újraépítés mindig szinkronban van ----------
import re
APP='/home/claude/karacsonyi_tulelokozpont_v26.html'
FILMS=json.loads(re.search(r'const FILMS=(\[.*?\]);\nlet filmTab',open(APP).read(),re.S).group(1))
def tbl(fs,en):
    rows=''.join("<tr><td>%s%s</td><td>%s</td><td>%s</td></tr>"%(html.escape(f[0]),'' if en or not f[2] or f[2]==f[0] else ' ('+html.escape(f[2])+')',f[1],html.escape(f[5] if en else f[4])) for f in fs)
    return '<table><tr><th>Film</th><th>%s</th><th>%s</th></tr>%s</table>'%('Year' if en else 'Év','Note' if en else 'Megjegyzés',rows)
ok=[f for f in FILMS if f[3] in('ok','cm','cf')]; orig=[f for f in FILMS if f[3] in('of','ow')]; unk=[f for f in FILMS if f[3]=='unk']
cov=[f for f in FILMS if f[3] in('cm','cf')]
def lis(fs,en): return ''.join("<li><b>%s</b> (%s): %s</li>"%(html.escape(f[0]),f[1],html.escape(f[5] if en else f[4])) for f in fs)
page('filmek.html','Karácsonyi filmek Mariah-, Wham!- és Feliz-dal nélkül','Dalmentes karácsonyi filmek a Mariahrmageddon, Whamageddon és Feliznavidageddon kihívásokhoz: %d film, plusz a Suicide list.'%len(ok),'l-mini.png',f'''
<h1>Karácsonyi filmek dalmentesen</h1><p class="lead">Melyik karácsonyi filmet nézheted meg anélkül, hogy kiesnél? A lista a whamageddon.com „Wham-Safe Viewing” listájára és az IMDb/Tunefind zenei adataira épül. {len(ok)} film, amelyben az eredeti Mariah-, Wham!- és Feliz Navidad-felvétel nem hallható.</p>
<div class="card"><b>Fontos:</b> csak az eredeti előadó eredeti felvétele számít, a feldolgozás nem. Az adatok szerkeszthetők és hiányosak lehetnek, ezért hibák előfordulhatnak. Nézz csak olyat, amit ismersz.</div>
<h2>Feldolgozások (nem számítanak)</h2><ul>{lis(cov,False)}</ul>
<h2>Dalmentes filmek ({len(ok)})</h2>{tbl(ok,False)}
<h2>Suicide list: ahol az eredeti elhangzik</h2><p>Hazardíroknak. Csak olyan film, amelynek zenei adatai szerint az egyik dal eredetije hallható.</p>{tbl(orig,False)}
<h2>Nincs elég adat</h2><p>Ezekről nincs elég megbízható zenei adat, ezért sehova nem soroltuk őket.</p>{tbl(unk,False)}
<p class="src">Források: <a href="https://whamageddon.com/">whamageddon.com</a>, IMDb Soundtracks, Tunefind, stlyrics.org. Plakátok és streaming: TMDB, JustWatch (az appban).</p>{CTA}''',alt=('en','christmas-movies.html'))
page('christmas-movies.html','Christmas movies without Mariah, Wham! or Feliz Navidad','Wham-safe, Mariah-safe and Feliz-safe Christmas movies for the Mariahrmageddon, Whamageddon and Feliznavidageddon challenges.','l-en.png',f'''
<h1>Song-free Christmas movies</h1><p class="lead">Which Christmas movie can you watch without getting Wham'd? {len(ok)} movies without the original Mariah Carey, Wham! or José Feliciano recording, based on the official Wham-Safe Viewing list of whamageddon.com and IMDb/Tunefind music credits.</p>
<div class="card"><b>Note:</b> only the original artist's original recording counts; covers do not. The data can be incomplete, so mistakes can happen. Only watch movies you know.</div>
<h2>Covers (do not count)</h2><ul>{lis(cov,True)}</ul>
<h2>Song-free movies ({len(ok)})</h2>{tbl(ok,True)}
<h2>Suicide list: the original is heard</h2>{tbl(orig,True)}
<h2>Not enough data</h2>{tbl(unk,True)}
<p><a class="cta" href="index.html?lang=en">Open the app (English)</a></p>''',lang='en',alt=('hu','filmek.html'))
GL='''<h1>Szlengszótár</h1><p class="lead">Ezeket a kifejezéseket nem fordítjuk, így él a nemzetközi játékban.</p>
<dl><dt><b>Wham'd</b></dt><dd>Elkapott a Last Christmas.</dd><dt><b>Carey'd Away</b></dt><dd>Elkapott Mariah.</dd><dt><b>Feliminated</b></dt><dd>Elkapott a Feliz Navidad (Feliz + eliminated). Tréfás változatai: <b>Navidamned</b> (Navidad + damned), <b>Felici-NO!</b></dd><dt><b>Whamhalla</b></dt><dd>A kiesettek mennyországa. A barátaidat tilos direkt oda küldeni.</dd><dt><b>un-Whamly</b></dt><dd>A játék szellemével ellentétes, szemét viselkedés.</dd></dl>
<p>Közösség: <a href="https://www.reddit.com/r/Mariahrmageddon/" rel="noopener">r/Mariahrmageddon</a> · <a href="https://www.facebook.com/mariahrmageddon">Facebook-oldal</a>.</p>'''
page('szlengszotar.html',"Szlengszótár: Wham'd, Carey'd Away, Feliminated","A Mariahrmageddon, Whamageddon és Feliznavidageddon nemzetközi szlengje: Wham'd, Carey'd Away, Feliminated, Whamhalla, un-Whamly.",'l-history.png',GL+CTA,faq=[("Mit jelent a Feliminated?","Elkapott a Feliz Navidad: Feliz + eliminated."),("Mit jelent a Carey'd Away?","Elkapott Mariah Carey dala."),("Mit jelent a Wham'd?","Elkapott a Last Christmas.")])


# ---------- FUNKCIÓ-ALOLDALAK (adatvezérelt): minden funkciónak saját, indexelhető oldala + hub ----------
FEAT=[
('fulvedo-futam','Fülvédő futam','Earmuff Run','Mini játék: éld túl a 24 napot a hanghullámok között.','Mini game: survive 24 days among the sound waves.',
 ['Egy perc játék egy napnak felel meg: a teljes 24 nap végigjátszása 24 perc.','Ugorj és bújj le a hanghullámok elől, miközben a fülhallgatós figura fut.','Belépve XP-t kapsz, és felkerülsz a ranglistára; ha valaki megdönti a rekordod, mézeskalács-értesítést kapsz.'],
 ['One minute of play equals one day: the full 24 days take 24 minutes.','Jump and duck under the sound waves while the headphone hero runs.','Logged in, you earn XP and a leaderboard place; if someone beats your record, a gingerbread notification tells you.']),
('betorok-ellen','Betörők ellen','Burglar Defence','Idle clicker: védd meg a nagy házat két betörőtől karácsonyi csapdákkal.','Idle clicker: defend a big house from two burglars with Christmas traps.',
 ['Építs csapdákat és vásárolj egyre több karácsonyi díszt.','A kisfiú a tetőn figyel, a magas vékony és az alacsony zömök betörő pedig próbálkozik.','Ranglista és XP jár hozzá.'],
 ['Build traps and buy more and more Christmas decorations.','The boy watches from the roof while a tall thin and a short stocky burglar try their luck.','Comes with a leaderboard and XP.']),
('toronyepito','Toronyépítő','Tower Builder','Rakd egymásra az emeleteket: a megnyert torony tetejére felirat kerül.','Stack the floors: a won tower gets a sign on top.',
 ['Minden menetnek előre megadott emeletszáma van (20, 27, 34…).','A megnyert menetek XP-t adnak.','A megnyert torony tetején NAKATOMI felirat látszik, a Die Hard előtt tisztelegve.'],
 ['Every round has a set number of floors (20, 27, 34…).','Won rounds give XP.','A won tower shows a NAKATOMI sign on top, a nod to Die Hard.']),
('karacsonyi-bingo','Karácsonyi bingó','Christmas Bingo','Pipáld ki, amit az ünnepeken megélsz: családi vitáktól a hírekig.','Tick off what you live through over the holidays, from family arguments to the news.',
 ['5×5-ös tábla, mobilon is kényelmesen elfér.','Magyar nyelven a hazai, angolul a nemzetközi ünnepi helyzetek szerepelnek.','Vidám, nem komoly: saját szövegekkel, a műfaj stílusában.'],
 ['A 5×5 board that fits comfortably on a phone.','Hungarian shows local, English shows international holiday situations.','Light-hearted and not serious, with original texts in the style of the genre.']),
('kerulendo-helyek','Kerülendő és biztonságos helyek','Places to avoid and safe places','Térkép arról, hol szól valószínűleg a karácsonyi zene, és hol nyugodt a hely.','A map of where Christmas music is likely playing and where it is calm.',
 ['A játékosok címmel és hangossággal ajánlanak helyeket.','Látszik a feltételezett és a valódi hallótávolság.','A biztonságos helyek külön rétegen jelennek meg, hogy tervezhesd a bevásárlást.'],
 ['Players suggest places with an address and a volume level.','Assumed and real audible range are shown.','Safe places have their own layer so you can plan your shopping.']),
('barati-csapatok','Baráti csapatok','Friend teams','Hozz létre csapatot barátokkal vagy kollégákkal, és nézzétek, ki bírja tovább.','Create a team with friends or colleagues and see who lasts longer.',
 ['Egy játékos több csapatnak is tagja lehet.','A csapatok versenyén az arány számít: a 4/5 jobb, mint az 5/10, így a nagy csapatoknak sincs előnyük.','Egyenlő aránynál a legtovább játékban lévő tag csapata győz.','A csapaton belül a több élő front számít.'],
 ['A player can be in several teams.','Teams are ranked by ratio: 4/5 beats 5/10, so big teams get no advantage.','On equal ratio, the team of the longest-surviving member wins.','Inside a team, more live fronts count.']),
('telepulesek-versenye','Települések versenye','Town contest','Melyik településről élték túl többen?','Which town has the most survivors?',
 ['Az számít, hányan élték túl az adott településről.','Mellette az arány is látszik.','A főoldalon az első település, a statisztikában az összes látszik.'],
 ['What counts is how many survivors come from a town.','The ratio is shown alongside.','The home page shows the leading town; statistics show all of them.']),
('osszneppi-cel','Össznépi cél','Collective goal','Ha a regisztráltak 10%-a karácsonyig bent marad, mindenki nyert.','If 10% of registered players are still in by Christmas, everyone wins.',
 ['Csak a Mariahrmageddon kiesései számítanak.','December 24-ig bármikor kicsúszhatunk, de az új meghívottak megmenthetnek mindenkit.','Csúszkán látszik, hol tart a közösség.'],
 ['Only Mariahrmageddon eliminations count.','We can slip until December 24, but new invitees can save everyone.','A slider shows where the community stands.']),
('adventi-naptar','Adventi naptár és ünnepi kellékek','Advent calendar and holiday props','Napi ablak, adventi koszorú és ajándékfa gyűjthető kellékekkel.','A daily door, an advent wreath and a gift tree with collectible props.',
 ['A napi ablak felugró ablakban nyílik, és XP-t ad.','Adventi vasárnapokon gyertya gyűjthető; a meg nem gyújtott gyertya a hét végén magától ég tovább, halványabban.','Az ajándékfa kellékeit (maci, labda, Mikulás-sapka) a felületen elrejtve találod meg.'],
 ['The daily door opens in a pop-up and gives XP.','On advent Sundays you can collect a candle; an unlit candle burns on by itself at the end of the week, more dimly.','Props for the gift tree (teddy, ball, Santa hat) are hidden around the interface.']),
('xp-es-jelvenyek','XP, szintek és jelvények','XP, levels and badges','A túlélés napjai jelvényt érnek, a játék közben XP gyűlik.','Days survived earn badges, and you collect XP while playing.',
 ['Nagyjából ötnaponta új jelvény jár.','Az XP-szintek: Grincs, Kevin, John McClane.','XP jár a minijátékokért, a meghívásokért, a csapat létrehozásáért, a hely ajánlásáért és a napi belépésért.'],
 ['A new badge roughly every five days.','XP levels: Grinch, Kevin, John McClane.','XP comes from mini games, invitations, creating a team, suggesting a place and daily visits.']),
('kiesesbejelento','Kiesésbejelentő és képeslap','Elimination report and postcard','Ha elkapott a dal, jelentsd be, és oszd meg a képeslapot.','If the song got you, report it and share the postcard.',
 ['Piros „Sajnos kiestem” gomb a Játék menüben, időbélyeggel (utólag is megadható).','Megadhatod, hol és milyen körülmények között estél ki, a közösségi média előre sorolva.','A letölthető képeslapon előbb a neved, alatta az „elesett a harcban” felirat áll.'],
 ['A red “I’m out” button in the Game menu, with a timestamp (can be entered afterwards).','You can add where and under what circumstances you fell, with social media listed first.','On the downloadable postcard your name comes first, “fell in battle” below it.']),
('terkep','Térkép','Map','Hol estek ki a játékosok, és hol élnek még?','Where players fell and where they still survive.',
 ['A térképet mindenki láthatja, a települések szerint összesítve.','Az adatok óránként frissülő pillanatképből jönnek, ezért gyors és takarékos.','Az admin kapcsolhatja, hogy csak a magyar vagy a világtérkép látszik.'],
 ['Everyone can see the map, summarised by town.','The data comes from an hourly snapshot, so it is fast and light.','The admin can switch between a Hungary-only and a world map.']),
]
def fpage(slug,t,d,bul,en):
    cta='<p><a class="cta" href="index.html?lang=en">Open the app</a> <a class="cta alt" href="features.html">All features</a></p>' if en else '<p><a class="cta" href="index.html">Belépek és játszom</a> <a class="cta alt" href="funkciok.html">Minden funkció</a></p>'
    li=''.join('<li>%s</li>'%html.escape(x) for x in bul)
    return '<h1>%s</h1><p class="lead">%s</p><ul>%s</ul>%s'%(html.escape(t),html.escape(d),li,cta)
for sl,thu,ten,dhu,den,bhu,ben in FEAT:
    page('f-%s.html'%sl,thu+' – Karácsonyi Túlélőközpont',dhu,'l-mini.png',fpage(sl,thu,dhu,bhu,False),alt=('en','feature-%s.html'%sl))
    page('feature-%s.html'%sl,ten+' – Christmas Survival Center',den,'l-en.png',fpage(sl,ten,den,ben,True),lang='en',alt=('hu','f-%s.html'%sl))
page('funkciok.html','Funkciók – Karácsonyi Túlélőközpont','A Karácsonyi Túlélőközpont minden funkciója: mini játékok, térkép, csapatok, települések, adventi naptár, XP.','l-mini.png','<h1>Funkciók</h1><p class="lead">Minden, amit a Karácsonyi Túlélőközpont tud.</p><ul>'+''.join('<li><a href="f-%s.html"><b>%s</b></a>: %s</li>'%(f[0],html.escape(f[1]),html.escape(f[3])) for f in FEAT)+'</ul>'+CTA,alt=('en','features.html'))
page('features.html','Features – Christmas Survival Center','Everything the Christmas Survival Center does: mini games, map, teams, town contest, advent calendar, XP.','l-en.png','<h1>Features</h1><p class="lead">Everything the Christmas Survival Center can do.</p><ul>'+''.join('<li><a href="feature-%s.html"><b>%s</b></a>: %s</li>'%(f[0],html.escape(f[2]),html.escape(f[4])) for f in FEAT)+'</ul><p><a class="cta" href="index.html?lang=en">Open the app</a></p>',lang='en',alt=('hu','funkciok.html'))

import datetime
TODAY=datetime.date.today().isoformat()
LEG=['adatkezeles.html','aszf.html','impresszum.html','privacy.html','terms.html','imprint.html']
pages=['index.html']+[p for p in REG if p!='index.html']
open(f'{OUT}/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{BASE}{"" if p=="index.html" else p}</loc><lastmod>{TODAY}</lastmod></url>\n' for p in pages+LEG)+'</urlset>\n')
open(f'{OUT}/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
print('pages ok')
