/* MSCRev: modo «Elaboración» y modo «Revisión del DPO» para las herramientas 04 (RAT), 06 (interés legítimo) y 07 (EIPD).
   Fuente única: scripts/revision_dpo.js. La incrusta scripts/barra_contexto.py solo en esas tres herramientas.
   Base: Res. SPDP-SPD-2025-0028-R art. 15.2 (el DPD no ejecuta la gestión de riesgos ni la evaluación de impacto; puede
   emitir observaciones no vinculantes), art. 15.3 (no decide fines ni medios) y art. 13 (asesora o supervisa).
   - Elaboración: la completa el responsable o su implementador; puede responder las observaciones del DPO.
   - Revisión del DPO: el DPO registra observaciones no vinculantes por pestaña, con prioridad, y una conclusión.
   - El informe principal de la herramienta (Copiar … (Word), Word y PDF) recibe un anexo «Revisión del DPO»
     (window.MSCRevAnexo, que llama scripts/barra_contexto.py). Además hay un informe propio de observaciones. */
(function(){
"use strict";
var KEY='msc-rev-v1',P=null;try{if(window.parent!==window)P=window.parent}catch(e){}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function hoy(){var d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}
var PRI=['Alta','Media','Baja'],EST=['Pendiente','Acogida','No acogida'],
 CONC=['Sin observaciones','Con observaciones no vinculantes: el responsable decide si las acoge','Recomienda una nueva versión antes de aprobar o de iniciar el tratamiento'];
var S=null;try{S=JSON.parse(localStorage.getItem(KEY)||'null')}catch(e){}
function cli(){try{return P&&P.PDCliente?P.PDCliente():null}catch(e){return null}}
function firma(){try{return P&&P.PDFirma?P.PDFirma():null}catch(e){return null}}
if(!S){var C=cli()||{},F=firma()||{};S={modo:C.rol==='dpo'?'rev':'elab',el:C.implNom||'',ver:'',rv:F.nom||'',fe:'',obs:[],concl:''}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}}
var TIT=(document.title||'').split(' — ')[0];
function tabs(){return [].slice.call(document.querySelectorAll('nav [data-t]')).map(function(b){return (b.textContent||'').replace(/^\s*\d+\s*·\s*/,'').trim()})}
function actual(){var b=document.querySelector('nav [aria-selected="true"]');return b?(b.textContent||'').replace(/^\s*\d+\s*·\s*/,'').trim():''}

var css='#mscrev{border:1px solid rgba(128,128,128,.35);border-left:4px solid #3FB8C9;border-radius:10px;padding:12px 14px;margin:12px 0}'+
 '#mscrev summary{cursor:pointer;font-weight:800;font-size:14.5px;list-style:none}#mscrev summary::-webkit-details-marker{display:none}'+
 '#mscrev summary small{display:block;font-weight:400;font-size:12.5px;opacity:.8;margin-top:2px}'+
 '#mscrev .mr-seg{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0}#mscrev .mr-seg button{flex:1;min-width:170px;min-height:42px;border:1px solid rgba(128,128,128,.5);background:transparent;color:inherit;border-radius:8px;font:inherit;font-weight:700;font-size:13px;padding:8px;cursor:pointer}'+
 '#mscrev .mr-seg button.on{background:#3FB8C9;color:#0B1E33;border-color:#3FB8C9}'+
 '#mscrev .mr-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 12px;margin:8px 0}#mscrev label{display:block;font-size:12.5px;font-weight:700;margin-bottom:3px}'+
 '#mscrev input,#mscrev select,#mscrev textarea{width:100%;box-sizing:border-box;font:inherit;font-size:14px;padding:8px;border:1px solid rgba(128,128,128,.5);border-radius:6px;background:transparent;color:inherit}#mscrev textarea{min-height:70px}'+
 '#mscrev .mr-n{font-size:12.5px;opacity:.85;margin:6px 0}#mscrev .mr-o{border:1px solid rgba(128,128,128,.3);border-radius:8px;padding:8px 10px;margin:8px 0;font-size:13.5px}'+
 '#mscrev .mr-o .h{display:flex;gap:8px;flex-wrap:wrap;align-items:center;font-size:12px;font-weight:700;opacity:.85;margin-bottom:4px}'+
 '#mscrev .mr-p{border-radius:999px;padding:1px 8px;font-size:11px}#mscrev .mr-p.Alta{background:#F6DADA;color:#8A1C1C}#mscrev .mr-p.Media{background:#F6EBCF;color:#7A5A12}#mscrev .mr-p.Baja{background:#E3EEDF;color:#2F5A23}'+
 '#mscrev .mr-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}#mscrev .mr-x{margin-left:auto;background:none;border:none;color:inherit;opacity:.7;cursor:pointer;font:inherit;font-size:12px;text-decoration:underline}';

function panel(){var nav=document.querySelector('nav[role=tablist],nav');if(!nav||document.getElementById('mscrev'))return;
 var sec0=document.querySelector('main section')||document.querySelector('section');
 var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
 var d=document.createElement('details');d.id='mscrev';
 d.innerHTML='<summary></summary><div class="mr-seg" role="group" aria-label="Modo de trabajo"><button type="button" data-m="elab">Elaboración<br><small style="font-weight:400">responsable o implementador</small></button><button type="button" data-m="rev">Revisión del DPO<br><small style="font-weight:400">observaciones no vinculantes</small></button></div>'+
  '<p class="mr-n" id="mr-nota"></p><div class="mr-g"><div><label for="mr-el">Elaborado por (implementador)</label><input id="mr-el" data-r="el" placeholder="Área interna o razón social del tercero"></div><div><label for="mr-ver">Versión revisada</label><input id="mr-ver" data-r="ver" placeholder="1.0"></div>'+
  '<div><label for="mr-rv">Revisor (DPO)</label><input id="mr-rv" data-r="rv"></div><div><label for="mr-fe">Fecha de revisión</label><input id="mr-fe" data-r="fe" type="date"></div></div>'+
  '<div id="mr-add"><div class="mr-g"><div><label for="mr-sec">Pestaña o sección</label><select id="mr-sec"></select></div><div><label for="mr-pri">Prioridad</label><select id="mr-pri">'+PRI.map(function(p){return '<option>'+p+'</option>'}).join('')+'</select></div></div>'+
  '<label for="mr-txt">Observación del DPO</label><textarea id="mr-txt" placeholder="Qué se observa, por qué (norma o evidencia) y qué se sugiere. No reescriba la evaluación: la decisión es del responsable."></textarea>'+
  '<div class="mr-row"><button type="button" class="btn" id="mr-ok">Agregar observación</button></div></div>'+
  '<div id="mr-lista"></div><div id="mr-cc"><label for="mr-concl">Conclusión de la revisión</label><select id="mr-concl" data-r="concl"><option value="">—</option>'+CONC.map(function(c){return '<option>'+esc(c)+'</option>'}).join('')+'</select></div>'+
  '<div class="mr-row"><button type="button" class="btn oro" id="mr-cop">Copiar observaciones del DPO (Word)</button></div>'+
  '<p class="mr-n">Base: Res. SPDP-SPD-2025-0028-R arts. 13, 15.2 y 15.3. Las observaciones se agregan como anexo al informe de esta herramienta.</p>';
 if(sec0)sec0.parentNode.insertBefore(d,sec0);else nav.parentNode.insertBefore(d,nav.nextSibling);
 [].slice.call(d.querySelectorAll('[data-r]')).forEach(function(i){i.value=S[i.dataset.r]||'';i.onchange=function(){S[i.dataset.r]=i.value;save();pinta()}});
 [].slice.call(d.querySelectorAll('[data-m]')).forEach(function(b){b.onclick=function(){S.modo=b.dataset.m;if(S.modo==='rev'&&!S.fe){S.fe=hoy();document.getElementById('mr-fe').value=S.fe}save();pinta()}});
 document.getElementById('mr-ok').onclick=function(){var t=document.getElementById('mr-txt');if(!t.value.trim()){t.focus();return}
  S.obs.push({sec:document.getElementById('mr-sec').value,pri:document.getElementById('mr-pri').value,txt:t.value.trim(),est:'Pendiente',resp:''});t.value='';save();pinta()};
 document.getElementById('mr-cop').onclick=copiar;
 document.addEventListener('click',function(e){if(e.target&&e.target.closest&&e.target.closest('nav [data-t]'))setTimeout(secActual,30)});
 pinta()}
function secActual(){var s=document.getElementById('mr-sec');if(s){var a=actual();if(a)s.value=a}}
function pinta(){var d=document.getElementById('mscrev');if(!d)return;var rev=S.modo==='rev',pend=S.obs.filter(function(o){return o.est==='Pendiente'}).length;
 d.querySelector('summary').innerHTML=(rev?'Revisión del DPO':'Elaboración por el responsable o su implementador')+' · '+S.obs.length+(S.obs.length===1?' observación':' observaciones')+(pend?' ('+pend+' pendiente'+(pend===1?'':'s')+')':'')+'<small>Toque para '+(d.open?'cerrar':'abrir')+'. Cambie el modo según quién usa la herramienta.</small>';
 [].slice.call(d.querySelectorAll('[data-m]')).forEach(function(b){b.classList.toggle('on',b.dataset.m===S.modo);b.setAttribute('aria-pressed',b.dataset.m===S.modo)});
 document.getElementById('mr-nota').innerHTML=rev?'<b>Modo revisión.</b> El DPO no ejecuta esta evaluación ni la corrige: registra observaciones no vinculantes por pestaña y una conclusión. El responsable decide si las acoge y responde cada una.':'<b>Modo elaboración.</b> La completa el responsable o el implementador que eligió (MSC solo si no es DPO de este cliente). Aquí se responden las observaciones del DPO.';
 document.getElementById('mr-add').hidden=!rev;document.getElementById('mr-cc').hidden=!rev&&!S.concl;document.getElementById('mr-concl').disabled=!rev;
 var sel=document.getElementById('mr-sec'),v=sel.value;sel.innerHTML=tabs().concat(['General']).map(function(t){return '<option>'+esc(t)+'</option>'}).join('');sel.value=v||actual()||'General';
 document.getElementById('mr-lista').innerHTML=S.obs.length?S.obs.map(function(o,i){return '<div class="mr-o"><div class="h"><span>'+(i+1)+'. '+esc(o.sec)+'</span><span class="mr-p '+esc(o.pri)+'">'+esc(o.pri)+'</span>'+(rev?'<button type="button" class="mr-x" data-del="'+i+'">Eliminar</button>':'')+'</div>'+esc(o.txt).replace(/\n/g,'<br>')+
  '<div class="mr-g"><div><label for="mr-e'+i+'">Estado</label><select id="mr-e'+i+'" data-ix="'+i+'" data-k="est">'+EST.map(function(e){return '<option'+(o.est===e?' selected':'')+'>'+e+'</option>'}).join('')+'</select></div><div style="grid-column:span 2"><label for="mr-r'+i+'">Respuesta del responsable</label><input id="mr-r'+i+'" data-ix="'+i+'" data-k="resp" value="'+esc(o.resp)+'" placeholder="Qué hizo o por qué no la acoge"></div></div></div>'}).join(''):'<p class="mr-n">Sin observaciones registradas.</p>';
 [].slice.call(d.querySelectorAll('[data-ix]')).forEach(function(i){i.onchange=function(){S.obs[+i.dataset.ix][i.dataset.k]=i.value;save();pinta()}});
 [].slice.call(d.querySelectorAll('[data-del]')).forEach(function(b){b.onclick=function(){if(!b.dataset.c){b.dataset.c=1;b.textContent='¿Eliminar? Toque otra vez';return}S.obs.splice(+b.dataset.del,1);save();pinta()}})}

function tabla(){var th='style="text-align:left;background:#E6EEF3"';return '<table border="1" cellpadding="5" style="border-collapse:collapse;width:100%;font-size:10pt"><tr><th '+th+'>N.º</th><th '+th+'>Pestaña o sección</th><th '+th+'>Prioridad</th><th '+th+'>Observación del DPO</th><th '+th+'>Estado</th><th '+th+'>Respuesta del responsable</th></tr>'+
 S.obs.map(function(o,i){return '<tr><td>'+(i+1)+'</td><td>'+esc(o.sec)+'</td><td>'+esc(o.pri)+'</td><td>'+esc(o.txt).replace(/\n/g,'<br>')+'</td><td>'+esc(o.est)+'</td><td>'+esc(o.resp)+'</td></tr>'}).join('')+'</table>'}
function datos(){return '<p>Elaborado por: <b>'+esc(S.el||'[IMPLEMENTADOR]')+'</b>'+(S.ver?' · versión '+esc(S.ver):'')+'. Revisado por el DPO: <b>'+esc(S.rv||'[DPO]')+'</b>'+(S.fe?' · '+esc(S.fe):'')+'.</p>'}
var NOTA='<p style="font-size:9pt">Observaciones no vinculantes del Delegado de Protección de Datos. El DPD no ejecuta la gestión de riesgos ni la evaluación de impacto y no decide sobre los fines ni los medios del tratamiento; la decisión final corresponde al responsable (Res. SPDP-SPD-2025-0028-R arts. 13, 15.2 y 15.3).</p>';
function firmas(){var th='style="text-align:left;background:#E6EEF3;width:50%"';return '<table border="1" cellpadding="5" style="border-collapse:collapse;width:100%;font-size:10pt"><tr><th '+th+'>Revisado por (DPO)</th><th '+th+'>Recibido por el responsable</th></tr><tr><td>Firma: ______________________</td><td>Firma: ______________________</td></tr><tr><td>'+esc(S.rv||'')+'</td><td></td></tr></table>'}
function hayAlgo(){return S.obs.length||S.concl||S.modo==='rev'}
window.MSCRevAnexo=function(html){if(!html||/data-mscrev/.test(html)||!hayAlgo())return html;
 var a='<div data-mscrev="1"><h2>Revisión del DPO</h2>'+datos()+(S.obs.length?tabla():'<p>Sin observaciones.</p>')+(S.concl?'<p><b>Conclusión:</b> '+esc(S.concl)+'</p>':'<p><b>Conclusión:</b> revisión en curso.</p>')+NOTA+'<p><b>Firma del DPO</b></p>'+firmas()+'</div>';
 var m=html.search(/<p><b>FIRMA DE RESPONSABILIDAD<\/b><\/p>/);return m>=0?html.slice(0,m)+a+html.slice(m):html+a};
function informe(){var c=cli()||{};return '<div data-mscrev="1"><h1>Observaciones del DPO</h1><p><b>'+esc(TIT)+'</b>'+(c.rs?' · '+esc(c.rs):'')+'</p>'+datos()+
 (S.obs.length?tabla():'<p>Sin observaciones.</p>')+'<p><b>Conclusión:</b> '+esc(S.concl||'revisión en curso')+'</p>'+NOTA+'<p><b>FIRMA DE RESPONSABILIDAD</b></p>'+firmas()+'</div>'}
function copiar(){var h=informe(),t=document.createElement('div');t.innerHTML=h;var pl=t.innerText||t.textContent;
 try{if(window.ClipboardItem&&navigator.clipboard&&navigator.clipboard.write){navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([h],{type:'text/html'}),'text/plain':new Blob([pl],{type:'text/plain'})})]).then(ok,function(){fb(pl)});return}}catch(e){}fb(pl)}
function ok(){if(document.body.classList.contains('msc-expmodo'))return;aviso('Observaciones copiadas: pegue en Word')}
function fb(t){var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(e){}a.remove()}
function aviso(t){try{if(P&&P.PDToast){P.PDToast(t);return}}catch(e){}var e=document.getElementById('toast');if(e){e.textContent=t;e.classList.add('on');setTimeout(function(){e.classList.remove('on')},1900)}}
window.MSCRev={estado:function(){return S},pinta:pinta};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',panel);else panel();
})();
