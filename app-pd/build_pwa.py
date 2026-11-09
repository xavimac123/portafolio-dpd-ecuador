"""Construye MSC Protección de Datos (PWA instalable y offline).

Toma las nueve herramientas ya generadas del portafolio, el catálogo de servicios y las imágenes,
y escribe docs/ (lo que publica GitHub Pages) y dist/preview.html (vista previa sin PWA).

Uso: python app-pd/build_pwa.py   (antes, regenerar las herramientas del portafolio)
"""
import hashlib, json, pathlib, sys
R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
sys.path.insert(0, str(ROOT / "scripts"))
import catalogo_config as CAT  # noqa: E402

TOOLS = {"01": "01-catalogo-servicios/catalogo-servicios.html", "02": "02-honorarios/calculadora-honorarios.html",
         "03": "03-madurez/asistente-madurez.html", "04": "04-registro-tratamientos/asistente-rat.html",
         "05": "05-gran-escala/evaluacion-gran-escala.html", "06": "06-interes-legitimo/asistente-interes-legitimo.html",
         "07": "07-evaluacion-impacto/asistente-eipd.html", "08": "08-kit-plantillas/generador-documentos.html",
         "09": "09-kit-vulneraciones/asistente-vulneraciones.html"}

def js(o):
    return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

tools = {k: (ROOT / v).read_text(encoding="utf-8") for k, v in TOOLS.items()}
serv = [[s["cod"], s["nombre"], s["fase"]] for s in CAT.SERVICIOS]
emb = (R / "assets" / "embebidos.txt").read_text(encoding="utf-8").split("\n")
img = {"iso": emb[0], "lineas": emb[1], "icono": emb[2]}
src = (R / "fuente" / "index.html").read_text(encoding="utf-8")
src = src.replace("__TOOLS_JSON__", js(tools)).replace("__SERV_JSON__", js(serv)).replace("__IMG_JSON__", js(img))
assert "__TOOLS_JSON__" not in src
(R / "dist").mkdir(exist_ok=True)
(R / "dist" / "preview.html").write_text(src, encoding="utf-8")

ver = hashlib.sha1(src.encode()).hexdigest()[:8]
NAME = "MSC Protección de Datos"
head = ('<script>window.MSC_PWA=true</script><link rel="manifest" href="manifest.webmanifest">'
        '<meta name="theme-color" content="#14181E"><meta name="apple-mobile-web-app-capable" content="yes">'
        '<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">'
        f'<meta name="apple-mobile-web-app-title" content="MSC PD"><link rel="apple-touch-icon" href="icons/icon-180.png"><link rel="icon" href="icons/icon-192.png">')
reg = '<script>if("serviceWorker" in navigator){window.addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){})})}</script>'
out = src.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + head, 1)
i = out.rindex("</body></html>"); out = out[:i] + reg + out[i:]
D = R / "docs"; D.mkdir(exist_ok=True)
(D / "index.html").write_text(out, encoding="utf-8")
(D / ".nojekyll").write_text("", encoding="utf-8")
man = {"name": NAME, "short_name": "MSC PD", "lang": "es-EC", "start_url": "./", "scope": "./", "display": "standalone",
       "background_color": "#F7F5EE", "theme_color": "#14181E", "id": "msc-proteccion-datos",
       "description": "Gestión de clientes, herramientas LOPDP y agenda de cumplimiento del DPD. Uso profesional de Macías Sánchez Consultores.",
       "icons": [{"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
                 {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
                 {"src": "icons/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
(D / "manifest.webmanifest").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
sw = f"""const C='mscpd-{ver}';const CORE=['./','./index.html','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png','./icons/maskable-512.png','./icons/icon-180.png'];
self.addEventListener('install',e=>{{e.waitUntil(caches.open(C).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))}});
self.addEventListener('activate',e=>{{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x.startsWith('mscpd-')&&x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))}});
self.addEventListener('fetch',e=>{{const r=e.request;if(r.method!=='GET')return;
 if(r.mode==='navigate'){{e.respondWith(fetch(r).then(res=>{{const cp=res.clone();caches.open(C).then(c=>c.put('./index.html',cp));return res}}).catch(()=>caches.match('./index.html')));return}}
 const u=new URL(r.url);if(u.origin!==self.location.origin&&!/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname))return;
 if(u.origin===self.location.origin&&!u.pathname.includes('/msc-protecciondatos/'))return;
 e.respondWith(caches.match(r).then(hit=>hit||fetch(r).then(res=>{{if(res.ok||res.type==='opaque'){{const cp=res.clone();caches.open(C).then(c=>c.put(r,cp))}}return res}}).catch(()=>hit)))}});
"""
(D / "sw.js").write_text(sw, encoding="utf-8")
print("Listo:", D, "versión", ver, f"({len(out)//1024} KB)")
