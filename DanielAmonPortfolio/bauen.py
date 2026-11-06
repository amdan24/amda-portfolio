# Daniel Amon · Portfolio-Prototyp (Lupen-Stil)
# Aufruf:  py bauen.py   ->  schreibt style.css, main.js, daten.js, index.html, portfolio.html, ueber-mich.html, kontakt.html
# Alles Nötige liegt in diesem Ordner: vorlage/ (Struktur, CSS), lebenslauf.json (Daten), lupe_svg.py (Gartenplan).
import json, os, re, sys, html as _h

HIER = os.path.dirname(os.path.abspath(__file__))
VORLAGE = os.path.join(HIER, "vorlage")
sys.path.insert(0, HIER)
from lupe_svg import plan_svg, praxis_svg
from sehen import JS_MOTIVE, seiten as sehen_seiten, ZITAT, streifen_html  # derselbe Gartenplan zweimal

e = _h.escape
def lies(p, base=VORLAGE):
    return open(os.path.join(base, p), encoding="utf-8").read()
def schreibe(p, s):
    open(os.path.join(HIER, p), "w", encoding="utf-8").write(s)

# ---------- Lebenslauf-Daten laden ----------
ns = {k: v for k, v in json.load(open(os.path.join(HIER, "lebenslauf.json"), encoding="utf-8")).items()}
PROJ = {p["titel"]: p for p in ns["PROJEKTE"]}

# ---------- Projekte (echt aus dem Lebenslauf + Platzhalter) ----------
def P(t, c, y, a, lage="", tat="", ergebnis="", tools=(), ph=False, kurz=""):
    return dict(t=t, c=c, y=y, a=a, lage=lage, tat=tat, ergebnis=ergebnis, tools=list(tools), ph=ph, kurz=kurz)

g = PROJ["Gartengestaltung und Bau im eigenen Garten"]
bb = {b[0]: b[2] for b in g["bausteine"]}
ob = PROJ["Obst-, Gemüse- und Kräuteranbau"]
bo = PROJ["Eigenes Betriebssystem für Geldflüsse und Buchhaltung"]
st = PROJ["Selbstständigkeit mit mehreren Standbeinen"]
gis = PROJ["GIS-Portfolio mit QGIS"]
web = {b[0]: b for b in st["bausteine"]}

PROJEKTE = [
    P("Mein Garten: Gestaltung und Bau", "Praxis", "laufend", "mix:3", g["lage"], g["tat"], g["ergebnis"], g["werkzeuge"], kurz=g["kurz"]),
    P("Hochbeete aus Lehmziegeln und Holzbalken", "Praxis", "Foto folgt", "praxis:12", "", bb["Hochbeete"], "", ["Hochbeet", "Holzbau", "Recycling"], True),
    P("Ziegelpflaster im Sandbett", "Praxis", "Foto folgt", "praxis:21", "", bb["Pflasterarbeiten"], "", ["Pflaster", "Wegebau"], True),
    P("Gartenbeleuchtung mit Tontopf-Lampen", "Praxis", "Foto folgt", "praxis:33", "", bb["Gartenbeleuchtung"], "", ["12-V-LED", "Elektrik"], True),
    P("Obst, Gemüse und Kräuter", "Praxis", "laufend", "praxis:41", ob.get("lage", ""), ob["tat"], ob["ergebnis"], ob["werkzeuge"], kurz=ob["kurz"]),
    P("GIS-Portfolio mit QGIS", "Planung", "im Aufbau", "plan:51", "", gis["tat"], "", gis["werkzeuge"], True, kurz=gis["kurz"]),
    P("Freiraumentwurf: Darstellung und Zeichnung", "Planung", "Platzhalter", "plan:61",
      "Platzhalter für eine Entwurfsarbeit aus dem Studium (Darstellungsmethoden und freies Zeichnen).",
      "Hier kommen Lageplan, Schnitt und Pflanzplan hinein.", "Hier kommt das Ergebnis hinein.", ["Zeichnen", "Lageplan", "Pflanzplan"], True),
    P("Weinberg vor der Haustür: Beobachtung", "Planung", "Platzhalter", "mix:71",
      "Platzhalter: Standorte und Vegetation im Jahresverlauf beobachten.",
      "Hier kommen Fotos, Karten und Artenlisten hinein.", "Hier kommt die Auswertung hinein.", ["Vegetation", "Standort", "Kartierung"], True),
    P("Eigenes Betriebssystem für Geldflüsse", "Digital", "laufend", "mix:81", bo["lage"], bo["tat"], bo["ergebnis"], bo["werkzeuge"], kurz=bo["kurz"]),
    P("Websites für Kleinbetriebe", "Digital", "im Aufbau", "plan:91", "", web["Websites für Kleinbetriebe"][2], "", ["HTML & CSS", "Cloudflare", "Vorlagen"], kurz="Aus Texten und Fotos entstehen fertige Webseiten."),
    P("Print-on-Demand-Shops", "Digital", "laufend", "praxis:101", "", web["Print-on-Demand-Shops"][2], "", ["Canva", "GIMP", "Inkscape"], kurz="Eigene Designs, ohne Lagerhaltung."),
    P("Abstrakte Linienarbeiten", "Prozess", "Platzhalter", "plan:111",
      "Platzhalter: freie Arbeiten auf Papier, dichte schwarze Linien in Blockform.",
      "Hier kommen die Scans hinein.", "Hier kommt der Gedanke dazu hinein.", ["Papier", "Tusche", "Linie"], True),
]

STATIONEN = [dict(zeit=s["zeit"], titel=s["titel"], ort=s.get("ort", "")) for s in ns["STATIONEN"] if s.get("art") != "zukunft"]
DATEN = dict(projekte=PROJEKTE, stationen=STATIONEN, blick=ns["BLICK"],
             staerken=[t for _, t in ns["STAERKEN"]], profil=ns["PROFIL"], status=ns["STATUS"], ort=ns["ORT"], mail=ns["MAIL"],
             leidenschaft=ns["LEIDENSCHAFT"], digital=[t for _, t in ns["DIGITAL"]], zert_technik=ns["ZERT_TECHNIK"], zert_orga=ns["ZERT_ORGA"], sprachen=ns["SPRACHEN"])
for _i, _p in enumerate(PROJEKTE, 1):
    _p["bild"] = f"bilder/projekt-{_i:02d}.jpg"
schreibe("daten.js", "window.DATEN=" + json.dumps(DATEN, ensure_ascii=False) + ";\n")

# ---------- style.css ----------
css = lies("style.css")
css = css.replace("--acc1:#e4572e; --acc2:#2e6fe4; --acc3:#f0b429;",
                  "--acc1:#1D6B37; --acc2:#6BAF88; --acc3:#F6D44A; --tinte:#161816; --rand:var(--gut); --gruen-text:#2E6B39; --kapsel:#8FC395; --mint:#EEF6ED;\n  --hand:'Patrick Hand','Comic Neue','Segoe Print',cursive; --kopf:'Aileron','Helvetica Neue',Arial,sans-serif;")
css = css.replace('--sans:"Helvetica Neue",Helvetica,Arial,sans-serif;', "--sans:'Montserrat','Helvetica Neue',Arial,sans-serif;")
css = re.sub(r"@media \(prefers-color-scheme:dark\)\{:root\{[^}]*\}\}\n", "", css)
css = css.replace("h1,h2,h3{font-weight:500;", "h1,h2,h3{font-family:var(--kopf);font-weight:800;")
css = css.replace("opacity:.5}", "opacity:.3}", 1)
css += """
/* Prototyp-Ergänzungen */
@media(max-width:760px){header.nav{flex-wrap:wrap;gap:6px 16px;padding:12px var(--gut)}header.nav nav{flex-wrap:wrap;gap:4px 14px}}
header.nav{mix-blend-mode:normal;color:var(--tinte);background:rgba(246,245,242,.92);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.tag{display:inline-block;font-family:var(--mono);font-size:.64rem;letter-spacing:.08em;text-transform:uppercase;padding:3px 9px;border-radius:99px;background:var(--mint);color:var(--gruen-text)}
.status{display:flex;width:fit-content;max-width:100%;align-items:center;gap:.6rem;padding:.45rem 1rem;border-radius:999px;background:var(--mint);font-size:.9rem;font-weight:600;color:var(--gruen-text)}
.status::before{content:"";flex:none;width:.6rem;height:.6rem;border-radius:50%;background:var(--acc1)}
.marken{display:flex;flex-wrap:wrap;gap:8px;list-style:none;margin-top:14px}
.marken li{padding:7px 14px;border-radius:99px;border:1px solid var(--line);font-size:.9rem;background:#fff}
"""
schreibe("style.css", css)

# ---------- main.js ----------
js = lies("main.js")
js = js.replace('const NAME = "Vorname Nachname"; // <- hier den echten Namen eintragen', 'const NAME = "Daniel Amon";')
js = js.replace('[["portfolio.html","Portfolio"],["ueber-mich.html","Über mich"],["studio.html","Studio"],["kontakt.html","Kontakt"]]',
                '[["sehen.html","Sehen"],["portfolio.html","Arbeiten"],["werdegang.html","Werdegang"],["ueber-mich.html","Über mich"],["kontakt.html","Kontakt"]]')
js = js.replace("Architektur · Kunst · Prozess", "Landschaft · Planung · Praxis").replace("hallo@deinname.com", "amondaniel@live.at")
js = js.replace('<a href="kontakt.html">amondaniel@live.at</a></footer>', '<a href="kontakt.html">amondaniel@live.at</a><span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span></footer>')
js = js.replace('const PAL=["#e4572e","#2e6fe4","#f0b429","#1c1c1c","#2fa37a","#d94f9b"];',
                'const PAL=["#1D6B37","#3E8A4F","#6BAF88","#8FC395","#F6D44A","#B5573C"];')
# Kachel-Motive neu: Plan (Tinte) und Praxis (Garten) statt Architektur und Kunst
i = js.index("/* Architektur: Raster")
neu = r'''/* Plan: Zeichnung eines Freiraums (Tinte auf Weiß) */
function planSVG(seed=1,w=400,h=500,transparent=false){
  const r=rng(seed),ink="#161816";
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">`;
  if(!transparent)s+=`<rect width="${w}" height="${h}" fill="#fff"/>`;
  for(let i=0;i<3;i++){const y=h*(.3+i*.17);s+=`<path d="M0 ${y} C ${w*.25} ${y-40}, ${w*.5} ${y+40}, ${w} ${y-20}" fill="none" stroke="${ink}" stroke-opacity=".16" stroke-width="1.2"/>`}
  s+=`<path d="M${w*.08} ${h*.07} L${w*.93} ${h*.05} L${w*.95} ${h*.92} L${w*.06} ${h*.94}Z" fill="none" stroke="${ink}" stroke-width="1.3" stroke-dasharray="10 4 2 4"/>`;
  const n=2+Math.floor(r()*2);
  for(let i=0;i<n;i++){const x=w*(.18+r()*.64),y=h*(.15+r()*.3),ww=w*(.14+r()*.14),hh=h*(.06+r()*.08);s+=`<rect x="${x.toFixed(0)}" y="${y.toFixed(0)}" width="${ww.toFixed(0)}" height="${hh.toFixed(0)}" fill="none" stroke="${ink}" stroke-width="1.8"/>`}
  const t=4+Math.floor(r()*4);
  for(let i=0;i<t;i++){const x=w*(.14+r()*.72),y=h*(.4+r()*.5),rad=16+r()*26;
    s+=`<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${rad.toFixed(0)}" fill="${transparent?"none":"#fff"}" stroke="${ink}" stroke-width="1.6"/><circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${(rad*.6).toFixed(0)}" fill="none" stroke="${ink}" stroke-dasharray="3 4"/><path d="M${(x-5).toFixed(0)} ${y.toFixed(0)}h10M${x.toFixed(0)} ${(y-5).toFixed(0)}v10" stroke="${ink}" stroke-width="1.5"/>`}
  return s+`<text x="12" y="${h-12}" font-family="Patrick Hand,cursive" font-size="15" fill="${ink}">M 1:${50+Math.floor(r()*150)}</text></svg>`;
}
/* Praxis: derselbe Raum gelebt, in Grün und Erde */
function praxisSVG(seed=1,w=400,h=500){
  const r=rng(seed+40),G=["#2E6B39","#3E8A4F","#6BAF88","#8FC395"];
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><rect width="${w}" height="${h}" fill="${G[Math.floor(r()*2)]}"/>`;
  s+=`<path d="M${w*.5} ${h} C ${w*.4} ${h*.7}, ${w*.7} ${h*.55}, ${w*.55} ${h*.3}" fill="none" stroke="#B5573C" stroke-width="26" stroke-linecap="round"/><path d="M${w*.5} ${h} C ${w*.4} ${h*.7}, ${w*.7} ${h*.55}, ${w*.55} ${h*.3}" fill="none" stroke="#D98A5F" stroke-width="22" stroke-linecap="round" stroke-dasharray="12 4"/>`;
  for(let i=0;i<2;i++){const x=w*(.1+r()*.6),y=h*(.12+r()*.4);s+=`<rect x="${x.toFixed(0)}" y="${y.toFixed(0)}" width="${w*.22}" height="${h*.08}" rx="3" fill="#6B4A32" stroke="#B5573C" stroke-width="6"/>`}
  const t=5+Math.floor(r()*3);
  for(let i=0;i<t;i++){const x=w*(.1+r()*.8),y=h*(.35+r()*.6),rad=18+r()*32,c=G[Math.floor(r()*4)];
    s+=`<ellipse cx="${(x+rad*.2).toFixed(0)}" cy="${(y+rad*.3).toFixed(0)}" rx="${rad.toFixed(0)}" ry="${(rad*.9).toFixed(0)}" fill="#0F3A1E" fill-opacity=".35"/><circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${rad.toFixed(0)}" fill="${c}"/><circle cx="${(x-rad*.2).toFixed(0)}" cy="${(y-rad*.2).toFixed(0)}" r="${(rad*.55).toFixed(0)}" fill="#fff" fill-opacity=".16"/>`}
  for(let i=0;i<7;i++){const x=r()*w,y=h*(.1+r()*.85);s+=`<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="5" fill="#F6D44A"/><circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="2" fill="#fff"/>`}
  return s+"</svg>";
}
/* Mix: Plan über Praxis, das Signaturmotiv */
function mixSVG(seed=1){
  return `<div style="position:absolute;inset:0">${praxisSVG(seed)}</div><div style="position:absolute;inset:0;mix-blend-mode:screen;opacity:.9">${planSVG(seed+7,400,500,true).replace(/#161816/g,"#ffffff")}</div>`;
}
function artHTML(spec){
  const [kind,seed]=spec.split(":");const sd=+seed||1;
  return kind==="plan"?planSVG(sd):kind==="praxis"?praxisSVG(sd):mixSVG(sd);
}
function fillTiles(root=document){
  root.querySelectorAll("[data-art]").forEach(el=>{
    el.innerHTML=artHTML(el.dataset.art);
    if(el.dataset.bild){const im=new Image();im.alt="";im.style.cssText="position:absolute;inset:0;width:100%;height:100%;object-fit:cover";
      im.onload=()=>{if(!el.querySelector("img"))el.appendChild(im)};im.src=el.dataset.bild}
  });
}
document.addEventListener("DOMContentLoaded",()=>fillTiles());
'''
js = js[:i] + neu
js = js.replace("return kind===\"plan\"?planSVG(sd):kind===\"praxis\"?praxisSVG(sd):mixSVG(sd);", "return (KIND[kind]||mixSVG)(sd);")
js += JS_MOTIVE
schreibe("main.js", js)

# ---------- gemeinsamer Seitenkopf ----------
DOMAIN = "https://amda.work"
def seite(titel, beschr, style, body, scripts, datei="index.html", robots=""):
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(titel)}</title>
<meta name="description" content="{e(beschr)}">{robots}
<meta name="theme-color" content="#EFEAE0">
<link rel="canonical" href="{DOMAIN}/{"" if datei == "index.html" else datei}">
<meta property="og:title" content="{e(titel)}">
<meta property="og:description" content="{e(beschr)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{DOMAIN}/{"" if datei == "index.html" else datei}">
<meta property="og:locale" content="de_AT">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="schriften.css">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="collage.css">
<style>
{style}
</style>
</head>
<body>
{body}
<script src="daten.js"></script>
<script src="main.js"></script>
{scripts}
</body>
</html>
'''

def stil(datei):
    m = re.search(r"<style>(.*?)</style>", lies(datei), re.S)
    return m.group(1).strip()

# ---------- index ----------
hero_css = r'''
.lupe{position:relative;height:100svh;min-height:34rem;max-height:62rem;overflow:hidden;cursor:none;background:var(--bg);--mx:62%;--my:48%;--r:0px;touch-action:pan-y;user-select:none;-webkit-user-select:none;outline-offset:-4px}
.lupe-ebene{position:absolute;inset:0}
.lupe-b{z-index:2;clip-path:circle(var(--r) at var(--mx) var(--my))}
.lupe-b::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(135deg,rgba(14,22,8,.66) 0,rgba(14,22,8,.34) 48%,rgba(14,22,8,.05) 80%)}
.lupe .plan{position:absolute;right:var(--gut);top:clamp(72px,10vh,96px);bottom:31%;width:auto;aspect-ratio:770/700;max-width:62%;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 7%);mask-image:linear-gradient(90deg,transparent 0,#000 7%)}
.lupe .plan svg{display:block;width:100%;height:100%}
.lupe .hill{position:absolute;left:0;bottom:0;width:100%;height:clamp(170px,34%,420px);object-fit:cover;object-position:50% 0;display:block}
.lupe .praxis{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 40%;display:block}
.lupe-ring{position:absolute;left:var(--mx);top:var(--my);width:calc(var(--r)*2);height:calc(var(--r)*2);transform:translate(-50%,-50%);border-radius:50%;border:3px solid var(--bg);box-shadow:0 0 0 1.5px var(--wald),inset 0 0 0 1.5px var(--wald),0 14px 36px rgba(22,24,22,.28);pointer-events:none;z-index:4}
.lupe-text{position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:flex-start;padding:clamp(88px,13vh,120px) var(--rand) 0;pointer-events:none}
.lupe-text.b{z-index:3;color:#fff;clip-path:circle(var(--r) at var(--mx) var(--my))}
.lupe-text .mono{margin-bottom:1.1rem;color:var(--gruen-text)}
.lupe-titel{margin:0;font-size:clamp(2.5rem,6.6vw,6.4rem);line-height:.94;color:var(--wald)}
.lupe-text.b .lupe-titel,.lupe-text.b .g{color:#F6F2E6}
.lupe-text.b .s{color:#DCE5B8}
.lupe-hinweis{position:absolute;left:var(--gut);bottom:1.6rem;z-index:5;margin:0;padding:.55rem 1.1rem;border-radius:999px;background:var(--bg);font:400 .95rem/1.25 var(--serif);font-style:italic;color:var(--wald);pointer-events:none;max-width:min(30rem,60vw)}
.lupe-weiter{position:absolute;right:var(--gut);bottom:1.6rem;z-index:6;cursor:pointer;background:var(--bg)}
@media (hover:none){.lupe{cursor:auto}}
@media (max-width:42rem){.lupe-titel{font-size:11.5vw}.lupe .plan{left:var(--gut);right:var(--gut);max-width:none;aspect-ratio:auto;top:47%;bottom:27%;-webkit-mask-image:none;mask-image:none}.lupe .hill{height:26%}.lupe-hinweis{display:none}.lupe-weiter{left:var(--gut);right:auto}}
.zitat-s{margin:clamp(30px,5vw,60px) 0}.zitat-s blockquote{font-family:var(--kopf);font-weight:800;font-size:clamp(1.7rem,4.6vw,3.6rem);line-height:1.05;letter-spacing:-.035em;max-width:20em}.zitat-s figcaption{margin-top:16px}
.intro-s{padding-bottom:0}
.intro-grid{display:grid;grid-template-columns:repeat(12,1fr);gap:var(--gut)}
.intro-h{grid-column:1/8}
.intro-t{grid-column:8/13}
@media(max-width:800px){.intro-h,.intro-t{grid-column:1/-1}}
.zahlen{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(12px,2vw,28px);margin-top:clamp(40px,6vw,80px)}
.zahlen div{border-top:1px solid var(--ink);padding-top:14px}
.zahlen h3{font-size:1.25rem;margin:8px 0 6px;line-height:1.15}
.zahlen p{font-size:.92rem;opacity:.78}
@media(max-width:900px){.zahlen{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.zahlen{grid-template-columns:1fr}}
.feat{display:grid;grid-template-columns:repeat(12,1fr);gap:clamp(12px,2vw,28px)}
.feat a{grid-column:span 4;display:block}
.feat a:nth-child(2){margin-top:4vw}
.feat .tile{aspect-ratio:4/5}
.feat .tile>*{transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.feat a:hover .tile>*{transform:scale(1.07) rotate(.6deg)}
.feat .meta{padding-top:10px;display:flex;justify-content:space-between;gap:10px}
.feat .meta b{letter-spacing:-.01em}
@media(max-width:800px){.feat a,.feat a:nth-child(2){grid-column:1/-1;margin-top:0}}
'''

def plan_hero():
    p = plan_svg()
    p = p.replace('<rect width="1200" height="800" fill="#fff"/>', "")
    p = re.sub(r'<path d="M0 \d+ C[^>]*stroke-opacity="\.16"[^>]*/>', "", p)
    p = p.replace('fill="#fff"', 'fill="#F5F1E8"').replace('stroke="#fff"', 'stroke="#EFEAE0"')
    p = p.replace('viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice"', 'viewBox="440 40 770 700" preserveAspectRatio="xMidYMax meet"')
    return p

hero = f'''<section class="lupe" id="lupe" tabindex="0" aria-label="Kopfbild: derselbe Ort als Plan und als Foto. Eine Lupe lässt sich mit Maus, Finger oder Pfeiltasten bewegen.">
  <div class="lupe-ebene lupe-a">
    <div class="plan">{plan_hero()}</div>
    <img class="hill" src="bilder/hero-huegel.webp" alt="" width="2000" height="662">
  </div>
  <div class="lupe-ebene lupe-b" aria-hidden="true"><img class="praxis" src="bilder/praxis-lupe.jpg" alt=""></div>
  <div class="lupe-ring" aria-hidden="true"></div>
  <p class="lupe-hinweis" aria-hidden="true">Fahre mit der Lupe über den Plan. Außen der Plan, innen die Praxis.</p>
  <div class="lupe-text">
    <p class="mono">Daniel Amon · Landschaftsplanung · BOKU Wien</p>
    <h1 class="lupe-titel"><span class="g">Landschaft<br>planen.</span><em class="s">Freiräume<br>gestalten.</em></h1>
  </div>
  <div class="lupe-text b" aria-hidden="true">
    <p class="mono" style="visibility:hidden">Daniel Amon · Landschaftsplanung · BOKU Wien</p>
    <p class="lupe-titel"><span class="g">Zwanzig Jahre<br>Praxis.</span><em class="s">Hände in<br>der Erde.</em></p>
  </div>
  <a class="btn lupe-weiter" href="#start">Weiter <span class="arr">↓</span></a>
</section>'''
index_body = f'''<main>
{hero}
<section class="intro-s" id="start">
  <div class="wrap intro-grid">
    <div class="rv intro-h"><h2 class="h2">Zwischen Plan<br>und Praxis.</h2><img class="fels" src="bilder/fels-moos.webp" alt="" loading="lazy" width="1700" height="1076"></div>
    <div class="rv intro-t"><p class="lead" style="margin-bottom:24px">Ich studiere Landschaftsplanung und Landschaftsarchitektur an der BOKU Wien. Dazu kommen über zwanzig Jahre Berufspraxis in Technik, Handwerk, Handel, Büro und Betreuung.</p><p style="margin-bottom:24px"><span class="status">Suche Teilzeitstelle · 8 bis 12 Wochenstunden</span></p><a class="btn" href="portfolio.html">Portfolio <span class="arr">→</span></a></div>
  </div>
  <div class="wrap"><div class="zahlen" id="zahlen"></div></div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head mono"><span>Wie ich sehe</span><span>Inspiration</span></div>
    <div class="rule"></div>
    <div class="sehen-grid">
      <div class="sehen-txt">
        <figure class="zitat-s rv"><blockquote>„{ZITAT[0]}“</blockquote><figcaption class="mono">{ZITAT[1]}</figcaption></figure>
        <p class="lead rv" style="max-width:30em">Ich sehe in einem Graben Schafgarbe und Beifuß, wo andere nur Unkraut sehen. Auf dieser Seite sammle ich, was mir auffällt.</p><br>
        <a class="btn" href="sehen.html">Zur Sammlung <span class="arr">→</span></a>
      </div>
      <figure class="sehen-bild rv"><img src="bilder/pflanzen.jpg" alt="Schafgarbe, Beifuß, Eichenlaub und Flechten am Wegrand" loading="lazy" width="1400" height="2087"><figcaption class="mono">Schafgarbe · Beifuß · Flechten</figcaption></figure>
    </div>
    {streifen_html()}
  </div>
</section>
<section>
  <div class="wrap">
    <div class="sec-head mono"><span>Ausgewählte Arbeiten</span><span>Prototyp · Inhalte teils Platzhalter</span></div>
    <div class="rule"></div><br><br>
    <div class="feat" id="feat"></div>
    <br><br><a class="btn" href="portfolio.html">Alle Arbeiten <span class="arr">→</span></a>
  </div>
</section>
</main>'''
index_js = '''<script src="lupe.js"></script>
<script>
const D=window.DATEN;
document.getElementById('zahlen').innerHTML=D.blick.map((b,i)=>`<div class="rv"><p class="mono">${String(i+1).padStart(2,"0")}</p><h3>${b[0]}</h3><p>${b[1]}</p></div>`).join("");
const F=[0,5,8].map(i=>D.projekte[i]);
document.getElementById('feat').innerHTML=F.map(p=>`<a class="rv" href="portfolio.html"><div class="tile" data-art="${p.a}" data-bild="${p.bild}"></div><div class="meta"><b>${p.t}</b><span class="mono">${p.c}</span></div></a>`).join("");
fillTiles(document.getElementById('feat'));
</script>'''
schreibe("index.html", seite("Daniel Amon · Landschaftsplanung und Praxis", "Portfolio von Daniel Amon: Landschaftsplanung und Landschaftsarchitektur an der BOKU Wien, mit über zwanzig Jahren Praxis.", hero_css, index_body, index_js, datei="index.html"))

# ---------- portfolio ----------
pf_body = '''<main>
<header class="band" style="--bild:url(bilder/hohlweg.jpg)"><div class="wrap">
  <p class="mono">Portfolio · <span id="count"></span> Arbeiten · Prototyp</p>
  <h1 class="display" style="margin-top:18px">Arbeiten</h1>
  <em class="s" style="margin-left:0">Planung, Praxis, Digitales.</em>
</div></header>
<div class="wrap" style="padding-top:36px">
  <div class="filters" id="filters">
    <button class="f on" data-f="all">Alle</button>
    <button class="f" data-f="Planung">Planung</button>
    <button class="f" data-f="Praxis">Praxis</button>
    <button class="f" data-f="Digital">Digital</button>
    <button class="f" data-f="Prozess">Prozess</button>
  </div>
  <div class="rule"></div>
  <div class="grid" id="grid"></div>
</div>
<div style="height:100px"></div>
</main>
<div class="case" id="case" aria-hidden="true">
  <div class="bar mono"><span id="caseTitle"></span><button id="closeCase">Schließen ✕</button></div>
  <div class="steps" id="steps"></div>
  <div class="making"><div class="play"></div><div><p class="mono">Fotos und Making-of</p><p style="max-width:34em">Platzhalter: hier kommen Fotos vom Bau, Pläne und ein kurzes Video hinein.</p></div></div>
</div>'''
pf_js = '''<script>
const P=window.DATEN.projekte;
const g=document.getElementById('grid');
g.innerHTML=P.map((p,i)=>`<div class="card rv" data-c="${p.c}" data-i="${i}"><div class="tile" data-art="${p.a}" data-bild="${p.bild}"></div><div class="meta"><b>${p.t}</b><span class="mono">${p.c} · ${p.y}</span></div></div>`).join("");
fillTiles(g);
document.getElementById('count').textContent=P.length;
document.querySelectorAll('.rv').forEach(el=>el.classList.add('in'));
document.getElementById('filters').addEventListener('click',e=>{
  const b=e.target.closest('.f');if(!b)return;
  document.querySelectorAll('.f').forEach(x=>x.classList.toggle('on',x===b));
  const f=b.dataset.f;
  g.querySelectorAll('.card').forEach(c=>c.classList.toggle('hide',!(f==='all'||c.dataset.c===f)));
});
const cs=document.getElementById('case');
const PH="Platzhalter: Text folgt.";
g.addEventListener('click',e=>{
  const c=e.target.closest('.card');if(!c)return;
  const p=P[+c.dataset.i];
  document.getElementById('caseTitle').textContent=p.t+" · "+p.c+" · "+p.y;
  const lab=[["01","Ausgangslage",p.lage||PH],["02","Vorgehen",p.tat||PH],["03","Ergebnis",p.ergebnis||PH]];
  const [k,s]=p.a.split(":");const sd=+s;
  const tiles=["plan:"+sd,"mix:"+sd,"praxis:"+sd];
  document.getElementById('steps').innerHTML=
   `<div><p class="mono">${p.c}${p.ph?' · <span class="tag">Platzhalter</span>':''}</p><h2 class="display" style="margin:12px 0;font-size:clamp(2.4rem,7vw,6rem)">${p.t}</h2>${p.kurz?`<p class="lead">${p.kurz}</p>`:''}${p.tools.length?`<ul class="marken">${p.tools.map(t=>`<li>${t}</li>`).join("")}</ul>`:''}</div>`+
   lab.map((l,i)=>`<div class="step"><div class="n"><b>${l[0]}</b><p class="mono">${l[1]}</p></div><div class="m"><div class="tile" data-art="${tiles[i]}"${i===2?` data-bild="${p.bild}"`:""}></div><p class="body">${l[2]}</p></div></div>`).join("");
  fillTiles(document.getElementById('steps'));
  cs.classList.add('open');cs.scrollTop=0;cs.setAttribute('aria-hidden','false');
});
function closeCase(){cs.classList.remove('open');cs.setAttribute('aria-hidden','true')}
document.getElementById('closeCase').onclick=closeCase;
addEventListener('keydown',e=>{if(e.key==='Escape')closeCase()});
</script>'''
schreibe("portfolio.html", seite("Arbeiten · Daniel Amon", "Arbeiten von Daniel Amon: Planung, Praxis, Digitales und Prozess.", stil("portfolio.html"), pf_body, pf_js, datei="portfolio.html"))

# ---------- über mich ----------
um_css = stil("ueber-mich.html").replace("filter:grayscale(1) contrast(1.05)", "").replace("#e4572e", "#F6D44A")
um_body = '''<main>
<div class="wrap">
  <div class="hero2">
    <div class="portrait rv"><img src="foto.jpg" alt="Porträt von Daniel Amon"></div>
    <div class="intro rv">
      <p class="mono">Daniel Amon</p>
      <h1 class="display" style="font-size:clamp(2.6rem,6.4vw,6.4rem);margin:14px 0 24px">Ich plane<br>mit Erde<br>an den Händen.</h1>
      <p class="lead" id="profil"></p>
    </div>
  </div>
</div>
<section>
  <div class="wrap">
    <div class="sec-head mono"><span>01 / Haltung</span><span>Wie Praxis und Planung einander prüfen</span></div>
    <div class="rule"></div><br><br>
    <div class="haltung"><figure class="blatt-panel rv"><img src="bilder/blatt.jpg" alt="Getrocknete Königskerzenblätter vor hellem Grund" loading="lazy" width="1300" height="1741"></figure>
    <div class="pillars">
      <div class="rv"><p class="mono">I</p><h3>Beobachten</h3><p class="body">Ob eine Pflanze am richtigen Standort gedeiht, zeigt sich oft erst nach einer Saison. Genau diese Beobachtung macht für mich den Reiz aus.</p></div>
      <div class="rv"><p class="mono">II</p><h3>Selber machen</h3><p class="body">Hochbeete, Pflaster, Beleuchtung: Ich arbeite mit vorhandenen Materialien und lerne am fertigen Ding, was der Plan nicht verrät.</p></div>
      <div class="rv"><p class="mono">III</p><h3>Systematisch denken</h3><p class="body">Organisation, Dokumentation und Prozessdenken aus zwanzig Jahren Berufspraxis, jetzt mit QGIS und Planungsmethodik verbunden.</p></div>
    </div></div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head mono"><span>02 / Pflanzgenerator</span><span>Interaktiv</span></div>
    <div class="rule"></div><br><br>
    <div class="gen">
      <div class="gen-feld rv"><svg id="gsvg" viewBox="0 0 600 600" role="img" aria-label="Zufällig erzeugte Pflanzung"></svg><p class="gen-info mono" id="ginfo"></p></div>
      <div class="gen-reg rv">
        <h2 class="gen-tit"><span class="g">Pflanz</span><em class="s">dir was.</em></h2>
        <p class="body">Vom strengen Raster zur gewachsenen Gesellschaft: Arten mischen, Dichte und Streuung ändern, die Zeit laufen lassen. Jeder Wurf ist neu.</p>
        <div class="gen-pre" id="gpre"></div>
        <div class="gen-gr">
          <label>Zeit<span class="mono">Experiment → Zeit übernimmt</span><input type="range" id="gt" min="0" max="100" value="30"></label>
          <label>Dichte<span class="mono">leer → dicht</span><input type="range" id="gd" min="5" max="100" value="55"></label>
          <label>Raster ↔ Geste<span class="mono">Plan → gewachsen</span><input type="range" id="gs" min="0" max="100" value="35"></label>
          <label>Gruppenbildung<span class="mono">verstreut → Flecken</span><input type="range" id="gk" min="0" max="100" value="30"></label>
          <label>Größenvielfalt<span class="mono">einheitlich → wild</span><input type="range" id="gv" min="0" max="100" value="50"></label>
        </div>
        <p class="mono gen-kopf">Artenanteil</p>
        <div class="gen-arten" id="garten"></div>
        <button type="button" class="btn" id="gneu">Neu würfeln <span class="arr">↻</span></button>
      </div>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head mono"><span>03 / Weiter</span><span>Mehr von mir</span></div>
    <div class="rule"></div><br>
    <a class="btn" href="werdegang.html">Werdegang <span class="arr">→</span></a>&nbsp;
    <a class="btn" href="sehen.html">Wie ich sehe <span class="arr">→</span></a>&nbsp;
    <a class="btn" href="kontakt.html">Kontakt <span class="arr">→</span></a>
  </div>
</section>
</main>'''
morph_js = re.search(r"<script>(.*?)</script>", lies("ueber-mich.html").split("main.js")[1], re.S).group(1)
morph_js = morph_js.replace("#e4572e", "#F6D44A").replace("#2e6fe4", "#3E8A4F")
um_js = f'''<script>
const D=window.DATEN;
document.getElementById('profil').textContent=D.profil.split(". ")[0]+".";
</script>
<script src="generator.js"></script>'''
schreibe("ueber-mich.html", seite("Über mich · Daniel Amon", "Daniel Amon: Student der Landschaftsplanung, Praxis in Garten, Technik und Organisation.", um_css, um_body, um_js, datei="ueber-mich.html"))

# ---------- kontakt ----------
k_body = '''<div class="kbg" aria-hidden="true"></div>
<main>
<div class="wrap k">
  <div class="glas">
    <p class="mono">Kontakt</p>
    <h1 class="kin" id="kin" aria-label="Schreib mir.">Schreib<br>mir.</h1>
    <a class="mail" href="mailto:amondaniel@live.at">amondaniel@live.at</a>
    <div class="rows">
      <a href="mailto:amondaniel@live.at?subject=Teilzeitstelle"><span>Suche Teilzeitstelle</span><span class="mono">8 bis 12 Wochenstunden</span></a>
      <a href="ueber-mich.html"><span>Werdegang</span><span class="mono">Gobelsburg, Niederösterreich</span></a>
    </div>
    <div class="cta">
      <a class="btn" href="mailto:amondaniel@live.at?subject=Gespr%C3%A4chsanfrage">Gespräch anfragen <span class="arr">→</span></a>
      <span class="mono">Antwort innerhalb eines Tages</span>
    </div>
  </div>
</div>
</main>'''
k_js = re.search(r"<script>(.*?)</script>", lies("kontakt.html").split("main.js")[1], re.S).group(0)
k_js = k_js.replace("['#e4572e','#2e6fe4','#f0b429']", "['#E4EBC8','#C9D68A','#F6D44A']")
schreibe("kontakt.html", seite("Kontakt · Daniel Amon", "Kontakt zu Daniel Amon.", stil("kontakt.html"), k_body, k_js, datei="kontakt.html"))

wd_body = """<main>
<div class="wrap top wd-kopf">
  <img class="wd-deko" src="bilder/trockenrasen.webp" alt="" width="1500" height="1784">
  <p class="mono">Werdegang</p>
  <h1 class="display" style="margin:16px 0 20px">Vom Handwerk<br>zur Landschaft.</h1>
  <p class="lead" id="profil"></p>
</div>
<section style="padding-top:20px">
  <div class="wrap">
    <div class="sec-head mono"><span>01 / Stationen</span><span>Aus dem Lebenslauf</span></div>
    <div class="tl" id="tl"></div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head mono"><span>02 / Können</span><span>Fähigkeiten und Zertifikate</span></div>
    <div class="rule"></div>
    <div class="spalten">
      <div class="rv"><h3>Stärken aus der Praxis</h3><ul class="marken" id="staerken"></ul></div>
      <div class="rv"><h3>Digitales und Kreatives</h3><ul class="marken" id="digital"></ul></div>
      <div class="rv"><h3>Zertifikate</h3><ul class="marken" id="zert"></ul><h3 style="margin-top:26px">Sprachen</h3><p id="sprachen" style="margin-top:8px"></p></div>
    </div>
    <br><br><a class="btn" href="kontakt.html">Kontakt aufnehmen <span class="arr">→</span></a>
  </div>
</section>
</main>"""
wd_css = stil("ueber-mich.html").split(".pillars")[0] + ".top{padding-top:140px;padding-bottom:10px}.spalten{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(14px,2.4vw,40px);margin-top:30px}.spalten h3{font-size:1.3rem}@media(max-width:900px){.spalten{grid-template-columns:1fr}}"
wd_js = """<script>
const D=window.DATEN;
document.getElementById('profil').textContent=D.profil.split(". ")[0]+".";
document.getElementById('tl').innerHTML=D.stationen.map(s=>`<div class="row rv"><span class="mono">${s.zeit}</span><b>${s.titel}</b><span class="mono">${s.ort}</span></div>`).join("");
const li=a=>a.map(t=>`<li>${t}</li>`).join("");
document.getElementById('staerken').innerHTML=li(D.staerken);
document.getElementById('digital').innerHTML=li(D.digital);
document.getElementById('zert').innerHTML=li(D.zert_technik.concat(D.zert_orga));
document.getElementById('sprachen').textContent=D.sprachen;
</script>"""
schreibe("werdegang.html", seite("Werdegang · Daniel Amon", "Werdegang von Daniel Amon: Stationen, Fähigkeiten und Zertifikate.", wd_css, wd_body, wd_js, "werdegang.html"))
sehen_seiten(seite, schreibe, e, None)

# ---------- Rechtliches, 404, robots, sitemap ----------
recht_css = ".recht{max-width:46rem;padding:150px var(--gut) 90px;margin:0 auto}.recht h1{font-size:clamp(2.4rem,6vw,4rem);margin-bottom:30px}.recht h2{font-size:1.3rem;margin:34px 0 8px;letter-spacing:-.02em}.recht p{max-width:40em;opacity:.88}.recht a{text-decoration:underline}"
impressum = """<div class="recht"><h1>Impressum</h1>
<h2>Offenlegung nach § 25 Mediengesetz</h2>
<p>Medieninhaber: Daniel Amon<br>Wohnort: Gobelsburg, Niederösterreich<br>E-Mail: <a href="mailto:amondaniel@live.at">amondaniel@live.at</a></p>
<h2>Grundlegende Richtung</h2>
<p>Persönliches Portfolio. Die Seite stellt Arbeiten, Werdegang und Fähigkeiten von Daniel Amon vor.</p>
<h2>Haftung für Links</h2>
<p>Für die Inhalte verlinkter fremder Seiten ist allein deren Betreiber verantwortlich.</p></div>"""
datenschutz = """<div class="recht"><h1>Datenschutz</h1>
<p>Diese Seite setzt keine Cookies, verwendet keine Analyse- oder Werbedienste und lädt nichts von fremden Servern. Schriften und Bilder liegen auf dieser Domain.</p>
<h2>Verantwortlicher</h2>
<p>Daniel Amon, Gobelsburg, Niederösterreich, <a href="mailto:amondaniel@live.at">amondaniel@live.at</a></p>
<h2>Hosting</h2>
<p>Die Seite wird über GitHub Pages ausgeliefert (GitHub, Inc., USA, ein Unternehmen von Microsoft). Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie die IP-Adresse, um die Seite auszuliefern und vor Missbrauch zu schützen. Rechtsgrundlage ist das berechtigte Interesse an einem sicheren Betrieb (Art. 6 Abs. 1 lit. f DSGVO). GitHub ist nach dem EU-US Data Privacy Framework zertifiziert.</p>
<h2>Kontakt per E-Mail</h2>
<p>Schreiben Sie mir, verwende ich Ihre Angaben nur, um Ihre Nachricht zu beantworten (Art. 6 Abs. 1 lit. b und f DSGVO), und lösche sie, wenn sie dafür nicht mehr gebraucht werden.</p>
<h2>Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch. Eine Beschwerde können Sie bei der Österreichischen Datenschutzbehörde einbringen (dsb.gv.at).</p></div>"""
NL = chr(10)
nein = NL + '<meta name="robots" content="noindex">'
schreibe("impressum.html", seite("Impressum · Daniel Amon", "Impressum von Daniel Amon.", recht_css, "<main>" + impressum + "</main>", "", "impressum.html", nein))
schreibe("datenschutz.html", seite("Datenschutz · Daniel Amon", "Datenschutzerklärung.", recht_css, "<main>" + datenschutz + "</main>", "", "datenschutz.html", nein))
schreibe("404.html", seite("Seite nicht gefunden · Daniel Amon", "Diese Seite gibt es nicht.", recht_css + ".recht .btn{margin-top:30px}", '<main><div class="recht"><h1>Diese Seite gibt es nicht.</h1><p>Vielleicht hilft die Startseite weiter.</p><a class="btn" href="/">Zur Startseite <span class="arr">→</span></a></div></main>', "", "404.html", nein))
schreibe("robots.txt", NL.join(["User-agent: *", "Allow: /", f"Sitemap: {DOMAIN}/sitemap.xml", ""]))
urls = "".join(f"<url><loc>{DOMAIN}/{p}</loc></url>" + NL for p in ("", "sehen.html", "portfolio.html", "werdegang.html", "ueber-mich.html", "kontakt.html"))
schreibe("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>' + NL + '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + NL + urls + "</urlset>" + NL)
print("fertig:", ", ".join(sorted(f for f in os.listdir(HIER) if f.endswith((".html", ".css", ".js")))))
