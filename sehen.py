# Seiten "Sehen" (Inspiration) und "Werdegang" + Kachel-Motive aus dem Alltagsblick
# Wird von bauen.py eingebunden. Texte sind Entwürfe nach Daniels eigenen Sätzen: bitte selbst überarbeiten.

ZITAT = ("Kunst gibt nicht das Sichtbare wieder, sondern macht sichtbar.", "Paul Klee", "Schöpferische Konfession, 1920")

# Zwei Blicke: (Kachel, Blick der anderen, mein Blick, Bildunterschrift)
BLICKE = [
    ("wild:3", "Eine Grube. Irgendein Unkraut.", "Schafgarbe, Beifuß, Gräser.",
     "Ein Graben mit Wildwuchs: Andere sehen eine Grube, in der irgendein Unkraut wächst. Ich sehe Schafgarbe, Beifuß und verschiedene Gräser."),
    ("stein:5", "Schotter. Grober Kies.", "Kleine Steine mit Mustern.",
     "Auf dem Boden liegt grober Schotter. Ich sehe kleine Steine mit faszinierenden Mustern, nehme sie mit und fotografiere sie."),
    ("blatt:7", "Ein grünes Blatt.", "Eine Maserung wie eine Karte.",
     "Blätter mit spannender Maserung: Ich sehe die Adern und fotografiere sie.")]

# Sammlung: (Kachel, Titel, Gruppe)
SAMMLUNG = [
    ("stein:11", "Stein mit Bänderung", "Steine"), ("stein:12", "Kies, genau betrachtet", "Steine"), ("stein:13", "Mitgenommen vom Weg", "Steine"),
    ("blatt:21", "Blattmaserung I", "Blätter"), ("blatt:22", "Blattmaserung II", "Blätter"), ("blatt:23", "Blatt im Gegenlicht", "Blätter"),
    ("wild:31", "Graben im Spätsommer", "Schnappschüsse"), ("wild:32", "Wiese am Weinberg", "Schnappschüsse"),
    ("mal:41", "Abstrakt, Erdtöne", "Malerei"), ("mal:42", "Abstrakt, Linien und Fläche", "Malerei"),
    ("arr:51", "Alte Ziegel und Balken", "Arrangements"), ("arr:52", "Holz, Stein, Pflanze", "Arrangements")]

# Farben (vorläufig, später aus den Fotos abnehmen)
FARBEN = [("Holz", "#B98B5E"), ("Nuss", "#6E4B33"), ("Pfirsichkern", "#9A6A4C"), ("Kürbiskern", "#7C8C4E")]

JS_MOTIVE = r'''
/* Motive aus dem Alltagsblick (Platzhalter bis zu echten Fotos) */
function wildSVG(seed=1,w=400,h=500){
  const r=rng(seed+3);let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><rect width="${w}" height="${h}" fill="#CFC9A4"/><rect y="${h*.55}" width="${w}" height="${h*.45}" fill="#9C8F6A"/>`;
  for(let i=0;i<26;i++){const x=r()*w,y=h*(.5+r()*.5),hh=60+r()*130,sw=(r()-.5)*50;s+=`<path d="M${x.toFixed(0)} ${y.toFixed(0)} q${(sw/2).toFixed(0)} ${(-hh/2).toFixed(0)} ${sw.toFixed(0)} ${(-hh).toFixed(0)}" fill="none" stroke="${["#5F7A3A","#7C9446","#A3A85A"][Math.floor(r()*3)]}" stroke-width="${(1.5+r()*2).toFixed(1)}" stroke-linecap="round"/>`}
  for(let i=0;i<6;i++){const x=w*(.12+r()*.76),y=h*(.2+r()*.35);s+=`<path d="M${x.toFixed(0)} ${(y+h*.35).toFixed(0)} V${y.toFixed(0)}" stroke="#6B7A3A" stroke-width="2.4"/>`;for(let k=0;k<9;k++){const a=k/9*Math.PI*2;s+=`<circle cx="${(x+Math.cos(a)*14).toFixed(1)}" cy="${(y+Math.sin(a)*8).toFixed(1)}" r="7" fill="#F4EFDD"/>`}s+=`<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="8" fill="#E9D98A"/>`}
  for(let i=0;i<5;i++){const x=w*(.1+r()*.8),y=h*(.45+r()*.4);for(let k=0;k<5;k++)s+=`<path d="M${x.toFixed(0)} ${y.toFixed(0)} q${(-18+k*9)} -28 ${(-30+k*15)} -50" fill="none" stroke="#8FA08A" stroke-width="2.2" stroke-linecap="round"/>`}
  return s+"</svg>";
}
function steinSVG(seed=1,w=400,h=500){
  const r=rng(seed+5),C=["#A89F94","#8E857A","#C9B79C","#B5A58C","#7D766E","#D2C6B0","#9A7B5E"];
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><rect width="${w}" height="${h}" fill="#B9B0A2"/>`;
  for(let i=0;i<20;i++){const x=r()*w,y=r()*h,rx=22+r()*38,ry=rx*(.6+r()*.4),rot=r()*180,c=C[Math.floor(r()*C.length)];
    s+=`<g transform="rotate(${rot.toFixed(0)} ${x.toFixed(0)} ${y.toFixed(0)})"><ellipse cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" rx="${rx.toFixed(0)}" ry="${ry.toFixed(0)}" fill="${c}" stroke="#4E4943" stroke-opacity=".5" stroke-width="1.4"/>`;
    const n=2+Math.floor(r()*3);for(let k=0;k<n;k++){const o=(k-n/2)*ry*.35;s+=`<path d="M${(x-rx*.8).toFixed(0)} ${(y+o).toFixed(0)} q${(rx*.8).toFixed(0)} ${(r()*14-7).toFixed(0)} ${(rx*1.6).toFixed(0)} 0" fill="none" stroke="${r()>.5?"#F4EFE4":"#4E4943"}" stroke-opacity=".6" stroke-width="${(1+r()*2).toFixed(1)}"/>`}
    s+=`</g>`}
  return s+"</svg>";
}
function blattSVG(seed=1,w=400,h=500){
  const r=rng(seed+9),cx=w/2,top=h*.1,bot=h*.9,g=["#4E7A32","#668F3C","#7BA24A"][seed%3];
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><rect width="${w}" height="${h}" fill="#E8E2CB"/>`;
  s+=`<path d="M${cx} ${bot} C ${w*.02} ${h*.65}, ${w*.05} ${h*.2}, ${cx} ${top} C ${w*.95} ${h*.2}, ${w*.98} ${h*.65}, ${cx} ${bot}Z" fill="${g}"/>`;
  s+=`<path d="M${cx} ${bot} V${top}" stroke="#DDE8B8" stroke-width="5" stroke-linecap="round"/>`;
  for(let i=1;i<=9;i++){const y=bot-(bot-top)*i/10,len=w*(.34-Math.abs(i-5)*.03);for(const d of [-1,1])s+=`<path d="M${cx} ${y.toFixed(0)} q${(d*len*.5).toFixed(0)} ${(-30-r()*10).toFixed(0)} ${(d*len).toFixed(0)} ${(-60-r()*12).toFixed(0)}" fill="none" stroke="#DDE8B8" stroke-opacity=".8" stroke-width="2.2" stroke-linecap="round"/>`}
  return s+"</svg>";
}
function malSVG(seed=1,w=400,h=500){
  const r=rng(seed+13),C=["#6E4B33","#B98B5E","#7C8C4E","#E8DCC0","#2E4A34","#9A6A4C"];
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><rect width="${w}" height="${h}" fill="#EFE7D6"/>`;
  for(let i=0;i<6;i++){const c=C[Math.floor(r()*C.length)];s+=`<rect x="${(r()*w*.7).toFixed(0)}" y="${(r()*h*.7).toFixed(0)}" width="${(60+r()*w*.5).toFixed(0)}" height="${(50+r()*h*.35).toFixed(0)}" rx="${(r()*20).toFixed(0)}" fill="${c}" fill-opacity="${(.5+r()*.45).toFixed(2)}" transform="rotate(${(r()*16-8).toFixed(0)} ${w/2} ${h/2})"/>`}
  for(let i=0;i<5;i++){let d=`M${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)}`;for(let k=0;k<3;k++)d+=` C${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)} ${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)} ${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)}`;s+=`<path d="${d}" fill="none" stroke="#2A2118" stroke-width="${(1+r()*3).toFixed(1)}" stroke-linecap="round" opacity=".8"/>`}
  return s+"</svg>";
}
function arrSVG(seed=1,w=400,h=500){
  const r=rng(seed+17);
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><rect width="${w}" height="${h}" fill="#CFC6B2"/>`;
  for(let row=0;row<6;row++){let x=-(r()*40);while(x<w){const bw=70+r()*30;s+=`<rect x="${x.toFixed(0)}" y="${(row*h/9+h*.06).toFixed(0)}" width="${(bw-4).toFixed(0)}" height="${(h/9-5).toFixed(0)}" rx="3" fill="${["#A8503A","#B5603F","#94452F","#C27050"][Math.floor(r()*4)]}"/>`;x+=bw}}
  s+=`<rect x="${w*.06}" y="${h*.66}" width="${w*.88}" height="${h*.1}" rx="3" fill="#8A6A44"/>`;
  for(let k=0;k<14;k++)s+=`<path d="M${(w*.06+r()*w*.8).toFixed(0)} ${(h*.68+r()*h*.06).toFixed(0)} h${(30+r()*60).toFixed(0)}" stroke="#5E4529" stroke-opacity=".6" stroke-width="1.5"/>`;
  s+=`<circle cx="${w*.3}" cy="${h*.62}" r="26" fill="#6BAF88"/><circle cx="${w*.34}" cy="${h*.58}" r="16" fill="#8FC395"/>`;
  return s+"</svg>";
}
const KIND={plan:planSVG,praxis:praxisSVG,mix:mixSVG,wild:wildSVG,stein:steinSVG,blatt:blattSVG,mal:malSVG,arr:arrSVG};
'''

CSS_SEHEN = r'''
.top{padding-top:140px;padding-bottom:30px}
.zitat{padding:clamp(60px,10vw,140px) 0;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);margin-top:50px}
.zitat blockquote{font-family:var(--kopf);font-weight:800;font-size:clamp(1.8rem,5vw,4.2rem);line-height:1.04;letter-spacing:-.035em;max-width:20em}
.zitat figcaption{margin-top:24px}
.blicke{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(14px,2vw,30px)}
@media(max-width:900px){.blicke{grid-template-columns:1fr}}
.blick{position:relative;aspect-ratio:4/3;overflow:hidden;cursor:none;background:#fff;--mx:50%;--my:50%;--r:0px;user-select:none;-webkit-user-select:none;touch-action:pan-y}
.blick .ebene{position:absolute;inset:0}
.blick .art>svg{display:block;width:100%;height:100%}
.blick .a .art{filter:grayscale(1) contrast(.8) brightness(1.18)}
.blick .b{clip-path:circle(var(--r) at var(--mx) var(--my))}
.blick .t{position:absolute;left:14px;right:14px;bottom:12px;font:400 clamp(1.25rem,2.2vw,1.6rem)/1.15 var(--hand)}
.blick .t span{display:inline-block;padding:.2rem .8rem;border-radius:1rem;background:rgba(255,255,255,.93);color:var(--tinte)}
.blick .b .t span{background:var(--tinte);color:#fff}
.blick .ring{position:absolute;left:var(--mx);top:var(--my);width:calc(var(--r)*2);height:calc(var(--r)*2);transform:translate(-50%,-50%);border-radius:50%;border:3px solid #fff;box-shadow:0 0 0 1.5px var(--tinte),0 10px 26px rgba(22,24,22,.25);pointer-events:none}
@media(hover:none){.blick{cursor:auto}}
.blick-text{margin-top:12px;font-size:.95rem;max-width:30em;opacity:.85}
.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:clamp(12px,2vw,28px);margin-top:30px}
.card{grid-column:span 3;position:relative}
.card .tile{aspect-ratio:4/5}
.card .meta{display:flex;justify-content:space-between;gap:10px;padding-top:10px}
.card .meta b{font-weight:500;letter-spacing:-.01em}
.card.hide{display:none}
@media(max-width:900px){.card{grid-column:span 6}}
@media(max-width:500px){.card{grid-column:1/-1}}
.filters{display:flex;gap:10px;flex-wrap:wrap;margin:26px 0 10px}
.f{font-family:var(--mono);font-size:.74rem;letter-spacing:.08em;text-transform:uppercase;padding:10px 18px;border:1px solid var(--line);background:none;color:var(--ink);cursor:pointer;transition:all .3s}
.f:hover{border-color:var(--ink)}
.f.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.farben{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(10px,1.6vw,22px);margin-top:20px}
.farben div{min-width:0;overflow:hidden;aspect-ratio:3/5;border-radius:3px;display:flex;flex-direction:column;justify-content:flex-end;padding:14px;color:#fff;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.farben div:nth-child(2){margin-top:30px}.farben div:nth-child(4){margin-top:56px}
.farben div:hover{transform:translateY(-10px)}
.farben b{font-family:var(--kopf);font-size:1.2rem;letter-spacing:-.02em}
.farben span{font-family:var(--mono);font-size:.68rem;opacity:.8}
@media(max-width:600px){.farben{grid-template-columns:repeat(2,minmax(0,1fr))}.farben div:nth-child(n){margin-top:0;aspect-ratio:1}}
.zwei{display:grid;grid-template-columns:repeat(12,1fr);gap:clamp(12px,2vw,28px);align-items:center}
.zwei .txt{grid-column:1/6}.zwei .bild{grid-column:7/13}.zwei .bild-l{grid-column:1/7}.zwei .txt-r{grid-column:8/13}
.zwei .tile{aspect-ratio:4/3}
@media(max-width:800px){.zwei .txt,.zwei .bild,.zwei .bild-l,.zwei .txt-r{grid-column:1/-1}}
'''

def seiten(seite, schreibe, e, DATEN_STATIONEN_ALLE):
    # ---------- Sehen ----------
    blicke_html = "".join(
        f'''<div class="rv"><div class="blick" data-spec="{k}"><div class="ebene a"><div class="art" data-art="{k}" style="position:absolute;inset:0"></div><div class="t"><span>{e(a)}</span></div></div><div class="ebene b" aria-hidden="true"><div class="art" data-art="{k}" style="position:absolute;inset:0"></div><div class="t"><span>{e(m)}</span></div></div><div class="ring" aria-hidden="true"></div></div><p class="blick-text">{e(t)}</p></div>'''
        for (k, a, m, t) in BLICKE)
    gruppen = []
    for _, _, gname in SAMMLUNG:
        if gname not in gruppen:
            gruppen.append(gname)
    filt = '<button class="f on" data-f="all">Alle</button>' + "".join(f'<button class="f" data-f="{e(g)}">{e(g)}</button>' for g in gruppen)
    karten = "".join(
        f'<div class="card rv in" data-c="{e(g)}"><div class="tile" data-art="{k}" data-bild="bilder/sehen-{i:02d}.jpg"></div><div class="meta"><b>{e(t)}</b><span class="mono">{e(g)}</span></div></div>'
        for i, (k, t, g) in enumerate(SAMMLUNG, 1))
    farben = "".join(f'<div style="background:{h}"><b>{e(n)}</b><span>{h}</span></div>' for n, h in FARBEN)
    body = f'''<main>
<div class="wrap top">
  <p class="mono">Sehen · Inspiration</p>
  <h1 class="display" style="margin:16px 0 20px">Ich sehe,<br>was da wächst.</h1>
  <p class="lead">Meine Inspiration kommt aus dem Alltag, aus dem genauen Hinschauen. Hier sammle ich, was mir dabei auffällt.</p>
  <figure class="zitat rv"><blockquote>„{e(ZITAT[0])}“</blockquote><figcaption class="mono">{e(ZITAT[1])} · {e(ZITAT[2])}</figcaption></figure>
</div>
<section>
  <div class="wrap">
    <div class="sec-head mono"><span>01 / Zwei Blicke</span><span>Fahre mit der Lupe über die Bilder</span></div>
    <div class="rule"></div><br><br>
    <div class="blicke">{blicke_html}</div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head mono"><span>02 / Sammlung</span><span>Platzhalter · Fotos folgen</span></div>
    <div class="rule"></div>
    <div class="filters" id="filters">{filt}</div>
    <div class="grid" id="grid">{karten}</div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head mono"><span>03 / Farben</span><span>Vorläufige Werte</span></div>
    <div class="rule"></div><br>
    <div class="zwei"><div class="txt rv"><h2 class="h2">Farben, die<br>zusammenpassen.</h2><p class="lead" style="margin-top:18px">Holz, Nuss, Pfirsichkern, Kürbiskern: Diese Töne harmonieren, und ich kann sie in einem Bild festhalten.</p></div>
    <div class="bild rv"><div class="farben">{farben}</div></div></div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-head mono"><span>04 / Im Garten</span><span>Naturmaterial</span></div>
    <div class="rule"></div><br>
    <div class="zwei"><div class="bild-l rv"><div class="tile" data-art="arr:61" data-bild="bilder/sehen-13.jpg"></div></div>
    <div class="txt-r rv"><h2 class="h2">Alt wird<br>Arrangement.</h2><p class="lead" style="margin-top:18px">Im Garten kombiniere ich gern Naturmaterial: alte Holzbalken, alte Ziegel. Oft ergibt sich dabei ein nettes Arrangement.</p><br><a class="btn" href="portfolio.html">Zu den Arbeiten <span class="arr">→</span></a></div></div>
  </div>
</section>
</main>'''
    js = '''<script src="blick.js"></script>
<script>
const g=document.getElementById('grid');
fillTiles(document.querySelector('main'));
document.getElementById('filters').addEventListener('click',ev=>{
  const b=ev.target.closest('.f');if(!b)return;
  document.querySelectorAll('.f').forEach(x=>x.classList.toggle('on',x===b));
  g.querySelectorAll('.card').forEach(c=>c.classList.toggle('hide',!(b.dataset.f==='all'||c.dataset.c===b.dataset.f)));
});
</script>'''
    schreibe("sehen.html", seite("Sehen · Daniel Amon", "Wie Daniel Amon sieht: Wildwuchs, Steine, Blattmaserung, Farben und Naturmaterial als Inspiration.", CSS_SEHEN, body, js, "sehen.html"))

    # ---------- Werdegang ----------
    return CSS_SEHEN
