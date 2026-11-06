/* Gemeinsame Bausteine: Navigation, Footer, generierte Platzhalter-Kunst, Reveal */
const NAME = "Daniel Amon";
const PAGES = [["sehen.html","Sehen"],["portfolio.html","Arbeiten"],["werdegang.html","Werdegang"],["ueber-mich.html","Über mich"],["kontakt.html","Kontakt"]];
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
  return (KIND[kind]||mixSVG)(sd);
}
function fillTiles(root=document){
  root.querySelectorAll("[data-art]").forEach(el=>{
    el.innerHTML=artHTML(el.dataset.art);
    if(el.dataset.bild){const im=new Image();im.alt="";im.style.cssText="position:absolute;inset:0;width:100%;height:100%;object-fit:cover";
      im.onload=()=>{if(!el.querySelector("img"))el.appendChild(im)};im.src=el.dataset.bild}
  });
}
document.addEventListener("DOMContentLoaded",()=>fillTiles());

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
