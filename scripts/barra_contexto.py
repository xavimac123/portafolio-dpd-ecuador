"""Complementos comunes de las nueve páginas web: barra de contexto y exportación a Word y PDF.

1. Barra de contexto que aparece al desplazarse.

Muestra «herramienta › pestaña › sección» para que el usuario sepa dónde está en páginas largas.
Dentro de la app MSC Protección de Datos (iframe), no dibuja su propia barra: envía el texto a la
barra superior de la app (window.parent.PDCtx).

2. Exportación: junto a cada botón «Copiar … (Word)» agrega «Word (.docx)» y «PDF», que descargan el mismo
informe con espacio para firma y sello (scripts/exportar.js). El texto copiado también lleva ese espacio.

Es idempotente: reemplaza los bloques marcados si ya existen. Ejecutar después de los generadores:
    python scripts/barra_contexto.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGINAS = {
    "01": "01-catalogo-servicios/catalogo-servicios.html", "02": "02-honorarios/calculadora-honorarios.html",
    "03": "03-madurez/asistente-madurez.html", "04": "04-registro-tratamientos/asistente-rat.html",
    "05": "05-gran-escala/evaluacion-gran-escala.html", "06": "06-interes-legitimo/asistente-interes-legitimo.html",
    "07": "07-evaluacion-impacto/asistente-eipd.html", "08": "08-kit-plantillas/generador-documentos.html",
    "09": "09-kit-vulneraciones/asistente-vulneraciones.html",
}
INI, FIN = "<!--barra-contexto-->", "<!--/barra-contexto-->"

SNIPPET = INI + """<style>#ctxbar{position:fixed;top:0;left:0;right:0;z-index:999;background:#14181E;color:#F7F5EE;font:600 13px/1.3 'Archivo',system-ui,sans-serif;padding:8px 14px;display:flex;gap:6px;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.25);transform:translateY(-110%);transition:transform .18s;white-space:nowrap;overflow:hidden}
#ctxbar.on{transform:none}#ctxbar b{color:#C9BC82;font-weight:800;letter-spacing:.04em}#ctxbar span{overflow:hidden;text-overflow:ellipsis}
#ctxbar button{margin-left:auto;flex:none;background:none;border:1px solid #3A3F47;color:#F7F5EE;border-radius:6px;font:inherit;font-size:12px;padding:3px 8px;cursor:pointer}</style>
<script>(function(){var N='__NUM__',T=(document.title||'').split(' — ')[0];
var inApp=false;try{inApp=!!(window.parent!==window&&window.parent.PDCtx)}catch(e){}
var bar=null;if(!inApp){bar=document.createElement('div');bar.id='ctxbar';bar.setAttribute('aria-hidden','true');bar.innerHTML='<b>'+N+'</b><span></span><button type="button">Arriba</button>';document.body.appendChild(bar);bar.querySelector('button').onclick=function(){window.scrollTo({top:0,behavior:'smooth'})}}
function vis(e){return e&&e.offsetParent!==null}
function txt(e){return e?(e.textContent||'').replace(/\\s+/g,' ').trim():''}
function calc(){var tab=document.querySelector('nav [aria-selected="true"],[role=tablist] [aria-selected="true"],.tabs .on');
 var hs=[].slice.call(document.querySelectorAll('main h2,main h3,section h2,section h3,.card h3')).filter(vis),sec='';
 for(var i=0;i<hs.length;i++){var r=hs[i].getBoundingClientRect();if(r.top<80)sec=txt(hs[i]);else break}
 var p=[];var t=txt(tab);if(t)p.push(t);if(sec&&sec!==t)p.push(sec.slice(0,70));return p.join(' › ')}
var tk=0;function upd(){tk=0;var y=window.scrollY||document.documentElement.scrollTop,s=calc();
 if(inApp){try{window.parent.PDCtx(y>60?s:'')}catch(e){}return}
 bar.querySelector('span').textContent=(T&&window.innerWidth>700?T+' › ':'')+s;bar.classList.toggle('on',y>140)}
window.addEventListener('scroll',function(){if(!tk){tk=1;requestAnimationFrame(upd)}},{passive:true});
document.addEventListener('click',function(){setTimeout(upd,60)});upd()})();</script>""" + FIN


EINI, EFIN = "<!--exportar-->", "<!--/exportar-->"
OINI, OFIN = "<!--oscuro-->", "<!--/oscuro-->"
import tema_oscuro as TO  # noqa: E402
import sys as _s  # noqa: E402
_s.path.insert(0, str(ROOT / "scripts"))

# Modo oscuro (se activa si la app está en oscuro) y datos del cliente o de la empresa de práctica.
OSCURO_JS = r"""<script>(function(){var P=null;try{if(window.parent!==window&&window.parent.PDTema)P=window.parent}catch(e){}if(!P)return;
__MAPA__
function tema(){var dk=false;try{dk=!!P.PDTema()}catch(e){}document.documentElement.classList.toggle('msc-dark',dk);if(dk){mscInline(document);if(!window._mscMo){window._mscMo=new MutationObserver(function(){if(window._mscT)return;window._mscT=setTimeout(function(){window._mscT=0;mscInline(document)},60)});window._mscMo.observe(document.body,{childList:true,subtree:true})}}}
window.MSCTema=tema;tema();
/* Datos de la empresa: rellena solo campos vacíos, por etiqueta, marcador o identificador. */
function etq(i){var t='';if(i.id){var l=document.querySelector('label[for="'+i.id+'"]');if(l)t=l.textContent}if(!t){var b=i.closest('div');var l2=b&&b.querySelector('label');if(l2)t=l2.textContent}return (t+' '+(i.placeholder||'')+' '+(i.getAttribute('data-k')||'')+' '+(i.id||'')).toLowerCase()}
function pon(i,v){if(v==null||v==='')return false;if(i.tagName==='SELECT'){var o=[].slice.call(i.options).filter(function(o){return o.value&&v(o.text)})[0];if(!o||i.value)return false;i.value=o.value}else{if(i.value)return false;i.value=v}i.dispatchEvent(new Event('input',{bubbles:true}));i.dispatchEvent(new Event('change',{bubbles:true}));return true}
function rango(n){return function(t){var m=t.replace(/\./g,'').match(/(\d+)\D+(\d+)/),a=t.replace(/\./g,'').match(/(\d+)\s*o m[aá]s/);if(m)return n>=+m[1]&&n<=+m[2];if(a)return n>=+a[1];return false}}
function datos(){var C=null;try{C=P.PDCliente&&P.PDCliente()}catch(e){}if(!C)return;var n=0;try{P.PDPrefill&&P.PDPrefill(true)}catch(e){}
 [].slice.call(document.querySelectorAll('input:not([type=checkbox]):not([type=radio]):not([type=file]),select')).forEach(function(i){if(i.closest('#ctxbar'))return;var t=etq(i);
  if(/raz[oó]n social|organizaci[oó]n evaluada|nombre de la empresa|responsable del tratamiento|\bcliente\b|i_resp|d_resp|ctx_emp/.test(t)&&!/representante|cargo|contacto|aprobado|elaborado|encargado/.test(t)){if(pon(i,i.tagName==='SELECT'?null:C.rs))n++}
  else if(/\bruc\b/.test(t)&&i.tagName!=='SELECT'){if(pon(i,C.ruc))n++}
  else if(/sector|actividad econ/.test(t)&&C.sec){if(i.tagName==='SELECT'){var k=(C.secK||C.sec).toLowerCase();if(pon(i,function(x){return x.toLowerCase().indexOf(k)>-1}))n++}}
  else if(/trabajadores/.test(t)&&+C.trab){if(pon(i,i.tagName==='SELECT'?rango(+C.trab):String(C.trab)))n++}
  else if(/ventas|ingresos por venta/.test(t)&&i.type==='number'&&+C.ven){if(pon(i,String(C.ven)))n++}
  else if(/ciudad/.test(t)&&i.tagName!=='SELECT'){if(pon(i,C.ciu))n++}});
 window.MSCDatos=n;setTimeout(function(){try{P.PDPrefill&&P.PDPrefill(false)}catch(e){}},400)}
setTimeout(datos,750);document.addEventListener('click',function(e){var t=e.target&&e.target.textContent||'';if(/nueva/i.test(t)&&!/ejemplo/i.test(t))setTimeout(datos,350)})})();</script>""".replace("__MAPA__", TO.JS_MAPA)
LIB = (ROOT / "scripts" / "exportar.js").read_text(encoding="utf-8").replace("</", "<\\/")
# Modo «Elaboración» / «Revisión del DPO» (Res. SPDP-SPD-2025-0028-R art. 15.2): solo en las herramientas que el DPO
# no debe ejecutar por sí mismo (RAT, interés legítimo y evaluación de impacto).
CON_REVISION = {"04", "06", "07"}
REV = (ROOT / "scripts" / "revision_dpo.js").read_text(encoding="utf-8").replace("</", "<\\/")
EXPORTA = r"""<style>.msc-exp{display:inline-flex;gap:6px;flex-wrap:wrap}body.msc-expmodo .toast{visibility:hidden}</style>
<script>(function(){var D=window.MSCDoc,P=null;try{if(window.parent!==window&&window.parent.MSCDoc){P=window.parent;if(!D)D=P.MSCDoc}}catch(e){}if(!D)return;
var modo=null,cap=null,OB=window.Blob;
function B(parts,opt){if(opt&&/^text\/html/.test(opt.type||'')&&parts&&typeof parts[0]==='string'){try{var h=parts.join('');if(window.MSCRevAnexo){try{h=window.MSCRevAnexo(h)}catch(e){}}h=D.firma(h);cap=h;parts=[h]}catch(e){}}return new OB(parts,opt)}
B.prototype=OB.prototype;window.Blob=B;
if(!window.ClipboardItem)window.ClipboardItem=function(o){this.o=o};
var capT=null;try{var C=navigator.clipboard||{},cw=C.write?C.write.bind(C):null,ct=C.writeText?C.writeText.bind(C):null;var nw=function(it){if(modo)return Promise.resolve();return cw?cw(it):Promise.reject(new Error('sin portapapeles'))},nt=function(t){if(modo){capT=String(t);return Promise.resolve()}return ct?ct(t):Promise.reject(new Error('sin portapapeles'))};
 if(navigator.clipboard){navigator.clipboard.write=nw;navigator.clipboard.writeText=nt}else Object.defineProperty(navigator,'clipboard',{configurable:true,value:{write:nw,writeText:nt}})}catch(e){}
var oec=document.execCommand?document.execCommand.bind(document):null;document.execCommand=function(c){if(modo&&c==='copy'){var a=document.activeElement;if(a&&'value' in a)capT=a.value;else{var sl=window.getSelection();capT=sl?String(sl):''}return true}return oec?oec.apply(document,arguments):false};
function aviso(t){try{if(P&&P.PDToast){P.PDToast(t);return}}catch(e){}var e=document.getElementById('msc-av');if(!e){e=document.createElement('div');e.id='msc-av';e.style.cssText='position:fixed;left:50%;bottom:20px;transform:translateX(-50%);background:#14181E;color:#fff;padding:10px 16px;border-radius:8px;font-size:14px;z-index:1000;max-width:92%';document.body.appendChild(e)}e.textContent=t;e.hidden=false;clearTimeout(e._t);e._t=setTimeout(function(){e.hidden=true},3200)}
function titulo(src){var t='';try{var d=document.createElement('div');d.innerHTML=cap||'';var h=d.querySelector('h1,h2');t=h?h.textContent:''}catch(e){}if(!t||modo==='xlsx')t=(src.textContent||'').replace(/^Copiar\s+/i,'').replace(/\s*\((Word|Excel)\)\s*$/i,'').replace(/\s*para Excel\s*$/i,'');t=t.replace(/\s+(de|del|en|para)\s*$/i,'');
 var c='';try{if(P&&P.PDNombre)c=P.PDNombre()||''}catch(e){}var f=new Date(),iso=f.getFullYear()+'-'+String(f.getMonth()+1).padStart(2,'0')+'-'+String(f.getDate()).padStart(2,'0');t=t.trim();if(t.length>44)t=t.slice(0,44).replace(/\s+\S*$/,'');return [t||'documento',c.replace(/\.+$/,'').slice(0,28),iso].filter(Boolean).join(' ')}
function exporta(src,tipo){modo=tipo;cap=null;capT=null;document.body.classList.add('msc-expmodo');try{src.click()}catch(e){}
 setTimeout(function(){var h=cap,m=modo;modo=null;setTimeout(function(){document.body.classList.remove('msc-expmodo')},2200);
  var n=titulo(src);
  if(m==='xlsx'){if(!capT){aviso('Complete los datos antes de exportar.');return}try{D.xlsx(capT,n,'Datos').then(function(f){if(f)aviso('Excel guardado: '+f)})}catch(e){aviso('No se pudo exportar: '+e.message)}return}
  if(!h){aviso('Complete el informe antes de exportarlo.');return}
  try{if(m==='docx'){D.docx(h,n).then(function(f){if(f)aviso('Word guardado: '+f)})}else{D.vista(h,n,null,{aviso:aviso})}}catch(e){aviso('No se pudo exportar: '+e.message)}},80)}
function botones(){[].slice.call(document.querySelectorAll('button')).forEach(function(b){if(b.dataset.mscx||b.closest('.msc-exp'))return;var t=(b.textContent||'').trim(),xl=/\(Excel\)$|para Excel/i.test(t);if(!/\(Word\)$/i.test(t)&&!/^Copiar documento$/i.test(t)&&!xl)return;b.dataset.mscx=1;
 var s=document.createElement('span');s.className='msc-exp';var cls=(b.className||'btn').replace(/\boro\b/,'').trim()+' sec';
 (xl?[['xlsx','Excel (.xlsx)']]:[['pdf','Vista previa y PDF'],['docx','Word (.docx)']]).forEach(function(k){var n=document.createElement('button');n.type='button';n.className=cls;n.textContent=k[1];n.title=k[0]==='pdf'?'Ver el documento y guardarlo en PDF':'Guardar '+(k[0]==='xlsx'?'en Excel':'en Word')+' en su equipo';n.onclick=function(){exporta(b,k[0])};s.appendChild(n)});
 b.parentNode.insertBefore(s,b.nextSibling)})}
function firmaApp(){var F=null;try{if(P&&P.PDFirma)F=P.PDFirma()}catch(e){}if(!F)return;
 [].slice.call(document.querySelectorAll('input')).forEach(function(i){var v=(i.value||'').trim(),nv=null;
  if(/^Consultor en Protecci[oó]n de Datos( Personales)?( · Mat\. ?[\d-]+)?$/.test(v)||/^Delegado de Protecci[oó]n de Datos/.test(v))nv=F.ec;else if(v==='Abg. Mariano X. Macías Sánchez'&&F.nom)nv=F.nom;
  if(nv&&nv!==v){i.value=nv;i.dispatchEvent(new Event('input',{bubbles:true}));i.dispatchEvent(new Event('change',{bubbles:true}))}})}
botones();setTimeout(botones,600);setTimeout(firmaApp,700);document.addEventListener('click',function(e){if(e.target&&/ejemplo|nueva/i.test(e.target.textContent||''))setTimeout(firmaApp,300)})})();</script>"""


# Navegación paso a paso y resultado al pie: al final de cada pestaña, «Anterior / Siguiente» y, si la pestaña
# muestra un resultado arriba (resNec, resFiltro, balance…), una copia de ese resultado abajo, al terminar de responder.
PASOS = r"""<style>.msc-pie{margin:18px 0 6px;border-top:1px solid rgba(128,128,128,.25);padding-top:14px}.msc-pie .pp{font-size:12px;opacity:.75;margin-bottom:8px}
.msc-pie .row2{display:flex;gap:8px;flex-wrap:wrap;justify-content:space-between}.msc-pie button{font:inherit;font-weight:700;font-size:14px;border-radius:8px;padding:11px 16px;cursor:pointer;min-height:44px}
.msc-pie .sig{background:#A09046;border:1px solid #A09046;color:#14181E;flex:1;min-width:180px}.msc-pie .ant{background:transparent;border:1px solid rgba(128,128,128,.5);color:inherit}
.msc-res{margin:14px 0 4px}.msc-res>.t{font-size:11.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;opacity:.75;margin-bottom:6px}</style>
<script>(function(){var B=[].slice.call(document.querySelectorAll('nav button[data-t]'));if(B.length<2)return;
var S=B.map(function(b){return document.getElementById(b.dataset.t)}).filter(Boolean);if(S.length!==B.length)return;
function nom(b){return (b.textContent||'').replace(/^\s*\d+\s*·\s*/,'').trim()}
S.forEach(function(sec,i){if(sec.querySelector('.msc-pie'))return;
 var src=[].slice.call(sec.querySelectorAll('[id]')).filter(function(e){return /^(res[A-Z]\w*|balance|pvR)$/.test(e.id)&&e.closest('section')===sec})[0],box=null;
 if(src){box=document.createElement('div');box.className='msc-res';box.hidden=true;box.innerHTML='<div class="t">Resultado</div><div class="c"></div>';
  var cp=function(){var h=src.innerHTML.trim();box.hidden=!h||/Responde todas|Responde las preguntas/i.test(src.textContent);box.querySelector('.c').innerHTML=h.replace(/\sid="/g,' data-oid="')};
  new MutationObserver(cp).observe(src,{childList:true,subtree:true,characterData:true});cp()}
 var pie=document.createElement('div');pie.className='msc-pie';
 pie.innerHTML='<div class="pp">Paso '+(i+1)+' de '+S.length+'</div><div class="row2">'+(i?'<button type="button" class="ant">‹ '+nom(B[i-1])+'</button>':'<span></span>')+(i<S.length-1?'<button type="button" class="sig">Siguiente: '+nom(B[i+1])+' ›</button>':'')+'</div>';
 var a=pie.querySelector('.ant'),n=pie.querySelector('.sig');if(a)a.onclick=function(){B[i-1].click();window.scrollTo(0,0)};if(n)n.onclick=function(){B[i+1].click();window.scrollTo(0,0)};
 if(box)sec.appendChild(box);sec.appendChild(pie)})})();</script>"""


def _pon(html: str, ini: str, fin: str, bloque: str) -> str:
    if ini in html:
        return re.sub(re.escape(ini) + ".*?" + re.escape(fin), lambda m: bloque, html, flags=re.S)
    i = html.rindex("</body>")
    return html[:i] + bloque + html[i:]


def aplicar(html: str, num: str, en_app: bool = False) -> str:
    """en_app=True omite la biblioteca de exportación: dentro de la app se usa la de la ventana principal."""
    html = _pon(html, INI, FIN, SNIPPET.replace("__NUM__", num))
    lib = "" if en_app else "<script>" + LIB + "</script>"
    rev = ("<script>" + REV + "</script>") if num in CON_REVISION else ""
    html = _pon(html, EINI, EFIN, EINI + lib + rev + EXPORTA + PASOS + EFIN)
    if en_app:
        html = _pon(html, OINI, OFIN, OINI + "<style>" + TO.css_oscuro(html) + "</style>" + OSCURO_JS + OFIN)
    return html


if __name__ == "__main__":
    for num, rel in PAGINAS.items():
        p = ROOT / rel
        p.write_text(aplicar(p.read_text(encoding="utf-8"), num), encoding="utf-8")
        print("ok", rel)
