/* Pflanzgenerator: Raster -> Geste, mehrere Arten, Dichte, Zeit. Alles deterministisch pro Würfelwurf. */
(function(){
const svg=document.getElementById('gsvg');if(!svg)return;
const W=600,G=20,CELL=W/G;
const ARTEN=[
 {n:'Schafgarbe',c:'#C9B04A',r:4.5,g:1.2},
 {n:'Federgras',c:'#98A845',r:4.5,g:1.5},
 {n:'Beifuß',c:'#9DB59A',r:4.5,g:1.7},
 {n:'Wildrose',c:'#C4553A',r:5,g:2.1},
 {n:'Feldahorn',c:'#3F6048',r:6,g:3.6},
 {n:'Natternkopf',c:'#A79BC8',r:4.5,g:2.6}];
const PRE={
 'Trockenrasen':{w:[30,40,15,10,0,5],t:30,d:55,s:35,k:30,v:50},
 'Feuchtwiese':{w:[10,45,5,0,10,30],t:45,d:70,s:60,k:55,v:60},
 'Gehölzrand':{w:[5,10,10,25,40,10],t:70,d:60,s:45,k:40,v:55},
 'Waldgarten':{w:[15,10,10,15,30,20],t:100,d:85,s:75,k:65,v:75}};
const S={t:30,d:55,s:35,k:30,v:50,w:[30,40,15,10,0,5]};
let seed=7,P=[],AN=[];
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gauss(r){return (r()+r()+r()-1.5)/1.5}
function wuerfeln(){
 const r=rng(seed);
 AN=ARTEN.map(()=>[0,1].map(()=>({x:60+r()*480,y:60+r()*480})));
 const cells=[];for(let i=0;i<G*G;i++)cells.push(i);
 for(let i=cells.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[cells[i],cells[j]]=[cells[j],cells[i]]}
 P=cells.map(c=>({gx:(c%G+.5)*CELL,gy:(Math.floor(c/G)+.5)*CELL,rx:20+r()*560,ry:20+r()*560,u:r(),sz:r(),a:r()<.5?0:1,gx2:gauss(r),gy2:gauss(r)}));
}
function ease(t){return t*t*(3-2*t)}
function zeichnen(){
 const sum=S.w.reduce((a,b)=>a+b,0);
 const n=Math.round(S.d/100*P.length),sc=S.s/100,kl=S.k/100,t=ease(S.t/100),va=S.v/100;
 let h='',zaehl=ARTEN.map(()=>0),list=[];
 if(sum>0){
  const cum=[];let c=0;S.w.forEach(w=>{c+=w/sum;cum.push(c)});
  for(let i=0;i<n;i++){
   const p=P[i];let s=cum.findIndex(v=>p.u<v);if(s<0)s=ARTEN.length-1;
   const A=ARTEN[s],an=AN[s][p.a];
   let x=p.gx+(p.rx-p.gx)*sc,y=p.gy+(p.ry-p.gy)*sc;
   x+=(an.x+p.gx2*55-x)*kl*sc;y+=(an.y+p.gy2*55-y)*kl*sc;
   x=Math.max(8,Math.min(W-8,x));y=Math.max(8,Math.min(W-8,y));
   const r=A.r*(1-va*.55+va*1.3*p.sz)*(1+t*A.g*1.4);
   zaehl[s]++;list.push({x,y,r,A});
  }
 }
 list.sort((a,b)=>b.r-a.r);
 const o=(1-sc)*.16;
 for(let i=0;i<=G;i++){const v=i*CELL-CELL/2;if(v<0||v>W)continue;h+=`<path d="M${v} 0V${W}M0 ${v}H${W}" stroke="#1B2614" stroke-opacity="${o.toFixed(3)}" stroke-width="1" fill="none"/>`}
 for(const q of list){
  const big=q.r>14;
  h+=`<circle cx="${q.x.toFixed(1)}" cy="${q.y.toFixed(1)}" r="${q.r.toFixed(1)}" fill="${q.A.c}" fill-opacity="${big?.5:.8}"${big?` stroke="${q.A.c}" stroke-opacity=".7"`:''}/>`;
  if(big)h+=`<circle cx="${q.x.toFixed(1)}" cy="${q.y.toFixed(1)}" r="${(q.r*.42).toFixed(1)}" fill="${q.A.c}" fill-opacity=".95"/>`;
 }
 svg.innerHTML=h;
 const ph=S.t<34?'Phase 1 · Experiment':S.t<67?'Phase 2 · Ausbreiten':'Phase 3 · Zeit übernimmt';
 document.getElementById('ginfo').textContent=ph+' · '+list.length+' Pflanzen';
 ARTEN.forEach((a,i)=>{document.getElementById('gz'+i).textContent=zaehl[i]});
 [['t','gt'],['d','gd'],['s','gs'],['k','gk'],['v','gv']].forEach(([k,id])=>{const e=document.getElementById(id);if(e)e.value=S[k]});
 ARTEN.forEach((a,i)=>{document.getElementById('gw'+i).value=S.w[i]});
}
const box=document.getElementById('garten');
box.innerHTML=ARTEN.map((a,i)=>`<label class="art"><i style="background:${a.c}"></i><span>${a.n}</span><output id="gz${i}">0</output><input type="range" id="gw${i}" min="0" max="100" value="${S.w[i]}" aria-label="Anteil ${a.n}"></label>`).join('');
ARTEN.forEach((a,i)=>document.getElementById('gw'+i).addEventListener('input',e=>{S.w[i]=+e.target.value;zeichnen()}));
[['t','gt'],['d','gd'],['s','gs'],['k','gk'],['v','gv']].forEach(([k,id])=>document.getElementById(id).addEventListener('input',e=>{S[k]=+e.target.value;zeichnen()}));
const pre=document.getElementById('gpre');
pre.innerHTML=Object.keys(PRE).map(k=>`<button type="button" class="f" data-p="${k}">${k}</button>`).join('');
pre.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const p=PRE[b.dataset.p];Object.assign(S,{t:p.t,d:p.d,s:p.s,k:p.k,v:p.v,w:p.w.slice()});pre.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));zeichnen()});
document.getElementById('gneu').addEventListener('click',()=>{seed=Math.floor(Math.random()*99999);wuerfeln();zeichnen()});
wuerfeln();zeichnen();
})();
