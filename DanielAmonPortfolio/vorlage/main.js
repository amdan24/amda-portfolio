/* Gemeinsame Bausteine: Navigation, Footer, generierte Platzhalter-Kunst, Reveal */
const NAME = "Vorname Nachname"; // <- hier den echten Namen eintragen
const PAGES = [["portfolio.html","Portfolio"],["ueber-mich.html","Über mich"],["studio.html","Studio"],["kontakt.html","Kontakt"]];
(function(){
  const here = location.pathname.split("/").pop() || "index.html";
  document.body.insertAdjacentHTML("afterbegin",
    `<header class="nav"><a class="logo" href="index.html">${NAME}</a><nav>${
      PAGES.map(([h,t])=>`<a href="${h}" class="${h===here?"on":""}">${t}</a>`).join("")}</nav></header>`);
  document.body.insertAdjacentHTML("beforeend",
    `<footer class="foot mono"><span>© ${new Date().getFullYear()} ${NAME}</span><span>Architektur · Kunst · Prozess</span><a href="kontakt.html">hallo@deinname.com</a></footer>`);
  const io = new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}}),{threshold:.12});
  document.querySelectorAll(".rv,.rule").forEach(el=>io.observe(el));
})();

/* deterministischer Zufall */
function rng(seed){let s=seed*9301+49297;return()=>((s=(s*9301+49297)%233280)/233280)}
const PAL=["#e4572e","#2e6fe4","#f0b429","#1c1c1c","#2fa37a","#d94f9b"];

/* Architektur: Raster, Grundrisse, Schraffur (schwarz/weiß, ein Farbakzent) */
function archSVG(seed=1,w=400,h=500,transparent=false){
  const r=rng(seed),ink="#111",acc=PAL[Math.floor(r()*3)];
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">`;
  if(!transparent)s+=`<rect width="${w}" height="${h}" fill="#efede7"/>`;
  s+=`<defs><pattern id="hat${seed}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#111" stroke-width="1"/></pattern></defs>`;
  for(let x=0;x<=w;x+=w/10)s+=`<line x1="${x}" y1="0" x2="${x}" y2="${h}" stroke="#0002"/>`;
  for(let y=0;y<=h;y+=h/12)s+=`<line x1="0" y1="${y}" x2="${w}" y2="${y}" stroke="#0002"/>`;
  const n=3+Math.floor(r()*3);
  for(let i=0;i<n;i++){
    const x=(Math.floor(r()*6)+1)*w/10,y=(Math.floor(r()*7)+1)*h/12,ww=(1+Math.floor(r()*4))*w/10,hh=(1+Math.floor(r()*4))*h/12;
    const fill=i===0?acc:(r()>.6?`url(#hat${seed})`:"none");
    s+=`<rect x="${x}" y="${y}" width="${ww}" height="${hh}" fill="${fill}" stroke="${ink}" stroke-width="1.4"/>`;
    s+=`<line x1="${x}" y1="${y}" x2="${x+ww}" y2="${y+hh}" stroke="${ink}" stroke-width=".6"/>`;
  }
  s+=`<path d="M0 ${h*.8} H${w}" stroke="${ink}" stroke-width="1.6"/><text x="12" y="${h-12}" font-family="monospace" font-size="9" fill="#111">M 1:${50+Math.floor(r()*150)}</text></svg>`;
  return s;
}
/* Kunst: freie Formen, Pinsel, Farbe */
function artSVG(seed=1,w=400,h=500){
  const r=rng(seed+40);
  let s=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><rect width="${w}" height="${h}" fill="#f2efe8"/>`;
  for(let i=0;i<4;i++){
    const c=PAL[Math.floor(r()*PAL.length)],cx=r()*w,cy=r()*h,rad=60+r()*150;
    let d="";const pts=7;
    for(let k=0;k<pts;k++){const a=k/pts*Math.PI*2,rr=rad*(.6+r()*.7);d+=(k?"L":"M")+(cx+Math.cos(a)*rr).toFixed(1)+" "+(cy+Math.sin(a)*rr).toFixed(1)}
    s+=`<path d="${d}Z" fill="${c}" fill-opacity="${(.55+r()*.4).toFixed(2)}" stroke="${c}" stroke-width="6" stroke-linejoin="round"/>`;
  }
  for(let i=0;i<5;i++){
    let d=`M${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)}`;
    for(let k=0;k<3;k++)d+=` C${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)} ${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)} ${(r()*w).toFixed(0)} ${(r()*h).toFixed(0)}`;
    s+=`<path d="${d}" fill="none" stroke="#111" stroke-width="${(.8+r()*3).toFixed(1)}" stroke-linecap="round" opacity=".85"/>`;
  }
  return s+"</svg>";
}
/* Mix: Raster trifft Geste – das Signaturmotiv */
function mixSVG(seed=1){
  return `<div style="position:absolute;inset:0">${artSVG(seed)}</div><div style="position:absolute;inset:0;mix-blend-mode:multiply">${archSVG(seed+7,400,500,true)}</div>`;
}
function artHTML(spec){
  const [kind,seed]=spec.split(":");const sd=+seed||1;
  return kind==="arch"?archSVG(sd):kind==="art"?artSVG(sd):mixSVG(sd);
}
function fillTiles(root=document){
  root.querySelectorAll("[data-art]").forEach(el=>{el.innerHTML=artHTML(el.dataset.art)});
}
document.addEventListener("DOMContentLoaded",()=>fillTiles());
