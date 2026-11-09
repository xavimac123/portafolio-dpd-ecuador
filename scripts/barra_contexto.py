"""Agrega a las nueve páginas web una barra de contexto que aparece al desplazarse.

Muestra «herramienta › pestaña › sección» para que el usuario sepa dónde está en páginas largas.
Dentro de la app MSC Protección de Datos (iframe), no dibuja su propia barra: envía el texto a la
barra superior de la app (window.parent.PDCtx).

Es idempotente: reemplaza el bloque marcado si ya existe. Ejecutar después de los generadores:
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


def aplicar(html: str, num: str) -> str:
    bloque = SNIPPET.replace("__NUM__", num)
    if INI in html:
        return re.sub(re.escape(INI) + ".*?" + re.escape(FIN), lambda m: bloque, html, flags=re.S)
    i = html.rindex("</body>")
    return html[:i] + bloque + html[i:]


if __name__ == "__main__":
    for num, rel in PAGINAS.items():
        p = ROOT / rel
        p.write_text(aplicar(p.read_text(encoding="utf-8"), num), encoding="utf-8")
        print("ok", rel)
