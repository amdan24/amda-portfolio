/* Gemeinsame Bausteine: Navigation, Footer, generierte Platzhalter-Kunst, Reveal */
const NAME = "Daniel Amon";
const PAGES = [["portfolio.html","Portfolio"],["ueber-mich.html","Über mich"],["kontakt.html","Kontakt"]];
(function(){
  const here = location.pathname.split("/").pop() || "index.html";
  document.body.insertAdjacentHTML("afterbegin",
    `<header class="nav"><a class="logo" href="index.html">${NAME}</a><nav>${
      PAGES.map(([h,t])=>`<a href="${h}" class="${h===here?"on":""}">${t}</a>`).join("")}</nav></header>`);
  document.body.insertAdjacentHTML("beforeend",
    `<footer class="foot mono"><span>© ${new Date().getFullYear()} ${NAME}</span><span>Landschaft · Planung · Praxis</span><a href="kontakt.html">amondaniel@live.at</a><span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span></footer>`);
  const io = new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}}),{threshold:.12});
  document.querySelectorAll(".rv,.rule").forEach(el=>io.observe(el));
})();

/* deterministischer Zufall */
function rng(seed){let s=seed*9301+49297;return()=>((s=(s*9301+49297)%233280)/233280)}
const PAL=["#1D6B37","#3E8A4F","#6BAF88","#8FC395","#F6D44A","#B5573C"];

/* Plan: Zeichnung eines Freiraums (Tinte auf Weiß) */
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
