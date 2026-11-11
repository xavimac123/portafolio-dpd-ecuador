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
LIB = (ROOT / "scripts" / "exportar.js").read_text(encoding="utf-8").replace("</", "<\\/")
EXPORTA = r"""<style>.msc-exp{display:inline-flex;gap:6px;flex-wrap:wrap}body.msc-expmodo .toast{visibility:hidden}</style>
<script>(function(){var D=window.MSCDoc,P=null;try{if(window.parent!==window&&window.parent.MSCDoc){P=window.parent;if(!D)D=P.MSCDoc}}catch(e){}if(!D)return;
var modo=null,cap=null,OB=window.Blob;
function B(parts,opt){if(opt&&/^text\/html/.test(opt.type||'')&&parts&&typeof parts[0]==='string'){try{var h=D.firma(parts.join(''));cap=h;parts=[h]}catch(e){}}return new OB(parts,opt)}
B.prototype=OB.prototype;window.Blob=B;
if(!window.ClipboardItem)window.ClipboardItem=function(o){this.o=o};
try{var C=navigator.clipboard||{},cw=C.write?C.write.bind(C):null;var nw=function(it){if(modo)return Promise.resolve();return cw?cw(it):Promise.reject(new Error('sin portapapeles'))};
 if(navigator.clipboard)navigator.clipboard.write=nw;else Object.defineProperty(navigator,'clipboard',{configurable:true,value:{write:nw}})}catch(e){}
function aviso(t){try{if(P&&P.PDToast){P.PDToast(t);return}}catch(e){}var e=document.getElementById('msc-av');if(!e){e=document.createElement('div');e.id='msc-av';e.style.cssText='position:fixed;left:50%;bottom:20px;transform:translateX(-50%);background:#14181E;color:#fff;padding:10px 16px;border-radius:8px;font-size:14px;z-index:1000;max-width:92%';document.body.appendChild(e)}e.textContent=t;e.hidden=false;clearTimeout(e._t);e._t=setTimeout(function(){e.hidden=true},3200)}
function titulo(src){var t='';try{var d=document.createElement('div');d.innerHTML=cap||'';var h=d.querySelector('h1,h2');t=h?h.textContent:''}catch(e){}if(!t)t=(src.textContent||'').replace(/^Copiar\s+/i,'').replace(/\s*\(Word\)\s*$/i,'');
 var c='';try{if(P&&P.PDNombre)c=P.PDNombre()||''}catch(e){}var f=new Date(),iso=f.getFullYear()+'-'+String(f.getMonth()+1).padStart(2,'0')+'-'+String(f.getDate()).padStart(2,'0');return [t.trim().slice(0,48),c.slice(0,28),iso].filter(Boolean).join(' ')}
function exporta(src,tipo){modo=tipo;cap=null;document.body.classList.add('msc-expmodo');try{src.click()}catch(e){}
 setTimeout(function(){var h=cap,m=modo;modo=null;setTimeout(function(){document.body.classList.remove('msc-expmodo')},2200);
  if(!h){aviso('Complete el informe antes de exportarlo.');return}var n=titulo(src);
  try{if(m==='docx'){var fn=D.docx(h,n);aviso('Word descargado: '+fn)}else{D.pdf(h,n);aviso('En la impresión elija «Guardar como PDF».')}}catch(e){aviso('No se pudo exportar: '+e.message)}},80)}
function botones(){[].slice.call(document.querySelectorAll('button')).forEach(function(b){if(b.dataset.mscx||b.closest('.msc-exp'))return;var t=(b.textContent||'').trim();if(!/\(Word\)$/i.test(t)&&!/^Copiar documento$/i.test(t))return;b.dataset.mscx=1;
 var s=document.createElement('span');s.className='msc-exp';var cls=(b.className||'btn').replace(/\boro\b/,'').trim()+' sec';
 [['docx','Word (.docx)'],['pdf','PDF']].forEach(function(k){var n=document.createElement('button');n.type='button';n.className=cls;n.textContent=k[1];n.title=t.replace(/^Copiar/i,'Descargar').replace(/\(Word\)$/i,'')+(k[0]==='pdf'?'en PDF':'en Word');n.onclick=function(){exporta(b,k[0])};s.appendChild(n)});
 b.parentNode.insertBefore(s,b.nextSibling)})}
botones();setTimeout(botones,600)})();</script>"""


def _pon(html: str, ini: str, fin: str, bloque: str) -> str:
    if ini in html:
        return re.sub(re.escape(ini) + ".*?" + re.escape(fin), lambda m: bloque, html, flags=re.S)
    i = html.rindex("</body>")
    return html[:i] + bloque + html[i:]


def aplicar(html: str, num: str, en_app: bool = False) -> str:
    """en_app=True omite la biblioteca de exportación: dentro de la app se usa la de la ventana principal."""
    html = _pon(html, INI, FIN, SNIPPET.replace("__NUM__", num))
    lib = "" if en_app else "<script>" + LIB + "</script>"
    return _pon(html, EINI, EFIN, EINI + lib + EXPORTA + EFIN)


if __name__ == "__main__":
    for num, rel in PAGINAS.items():
        p = ROOT / rel
        p.write_text(aplicar(p.read_text(encoding="utf-8"), num), encoding="utf-8")
        print("ok", rel)
