"""Construye MSC Protección de Datos (PWA instalable y offline).

Toma las nueve herramientas ya generadas del portafolio, el catálogo de servicios y las imágenes,
y escribe docs/ (lo que publica GitHub Pages) y dist/preview.html (vista previa sin PWA).

Uso: python app-pd/build_pwa.py   (antes, regenerar las herramientas del portafolio)
"""
import hashlib, json, pathlib, re, sys
R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
sys.path.insert(0, str(ROOT / "scripts"))
import catalogo_config as CAT  # noqa: E402
import barra_contexto as BC  # noqa: E402

TOOLS = {"01": "01-catalogo-servicios/catalogo-servicios.html", "02": "02-honorarios/calculadora-honorarios.html",
         "03": "03-madurez/asistente-madurez.html", "04": "04-registro-tratamientos/asistente-rat.html",
         "05": "05-gran-escala/evaluacion-gran-escala.html", "06": "06-interes-legitimo/asistente-interes-legitimo.html",
         "07": "07-evaluacion-impacto/asistente-eipd.html", "08": "08-kit-plantillas/generador-documentos.html",
         "09": "09-kit-vulneraciones/asistente-vulneraciones.html"}

def js(o):
    return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

tools = {k: BC.aplicar((ROOT / v).read_text(encoding="utf-8"), k, en_app=True) for k, v in TOOLS.items()}
serv = [[s["cod"], s["nombre"], s["fase"]] for s in CAT.SERVICIOS]
emb = (R / "assets" / "embebidos.txt").read_text(encoding="utf-8").split("\n")
img = {"iso": emb[0], "lineas": emb[1], "icono": emb[2]}
src = (R / "fuente" / "index.html").read_text(encoding="utf-8")
import referencia_config as REFC  # noqa: E402
import shutil  # noqa: E402


def _tablas(md):
    """Secciones «## título» con sus filas de tabla (sin encabezado ni separador)."""
    out, sec = [], None
    for ln in md.splitlines():
        if ln.startswith("## "):
            sec = {"sec": ln[3:].strip(), "filas": []}
            out.append(sec)
        elif sec is not None and ln.startswith("|") and not set(ln) <= set("|-: "):
            c = [x.strip().replace("**", "") for x in ln.strip().strip("|").split("|")]
            sec["filas"].append(c)
    for s_ in out:
        s_["filas"] = s_["filas"][1:]
    return [s_ for s_ in out if s_["filas"]]


contraste = []
for s_ in _tablas((ROOT / "docs" / "contraste-guias-spdp.md").read_text(encoding="utf-8")):
    filas = [(f[-4:] if len(f) >= 4 else None) for f in s_["filas"]]
    filas = [[(f[0] if len(o) == 4 else o[0] + ": " + o[1]), f[1], f[2], f[3]] for f, o in zip(filas, s_["filas"]) if f]
    contraste.append({"sec": s_["sec"], "filas": filas})
bl = (ROOT / "BASE-LEGAL.md").read_text(encoding="utf-8")
ab = bl.split("## Puntos abiertos", 1)[1].split("\n## ", 1)[0]
abiertos = [re.sub(r"\*\*|`", "", m.group(1)).strip() for m in re.finditer(r"^\d+\.\s+(.+)$", ab, flags=re.M)]
NORMAS = R / "normas"
pdf = {k: ("normas/%s.pdf" % k if (NORMAS / (k + ".pdf")).exists() else "") for k in ("lopdp", "rglopdp")}
ref = {"rev": REFC.REVISION, "normas": REFC.NORMAS, "plazos": REFC.PLAZOS, "contraste": contraste, "abiertos": abiertos, "pdf": pdf}
exp_js = (ROOT / "scripts" / "exportar.js").read_text(encoding="utf-8").replace("</", "<\\/")
src = src.replace("__TOOLS_JSON__", js(tools)).replace("__SERV_JSON__", js(serv)).replace("__IMG_JSON__", js(img))
src = src.replace("__REF_JSON__", js(ref)).replace("__EXPORT_JS__", exp_js)
assert "__REF_JSON__" not in src and "__EXPORT_JS__" not in src
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
extra = ""
for k, v in pdf.items():
    if v:
        (D / "normas").mkdir(exist_ok=True)
        shutil.copyfile(NORMAS / (k + ".pdf"), D / v)
        extra += ",'./" + v + "'"
man = {"name": NAME, "short_name": "MSC PD", "lang": "es-EC", "start_url": "./", "scope": "./", "display": "standalone",
       "background_color": "#F7F5EE", "theme_color": "#14181E", "id": "msc-proteccion-datos",
       "description": "Gestión de clientes, herramientas LOPDP y agenda de cumplimiento del DPD. Uso profesional de Macías Sánchez Consultores.",
       "icons": [{"src": "icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
                 {"src": "icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
                 {"src": "icons/maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}
(D / "manifest.webmanifest").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
sw = f"""const C='mscpd-{ver}';const CORE=['./','./index.html','./manifest.webmanifest','./icons/icon-192.png','./icons/icon-512.png','./icons/maskable-512.png','./icons/icon-180.png'__EXTRA__];
self.addEventListener('install',e=>{{e.waitUntil(caches.open(C).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))}});
self.addEventListener('activate',e=>{{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x.startsWith('mscpd-')&&x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))}});
self.addEventListener('fetch',e=>{{const r=e.request;if(r.method!=='GET')return;
 if(r.mode==='navigate'){{e.respondWith(fetch(r).then(res=>{{const cp=res.clone();caches.open(C).then(c=>c.put('./index.html',cp));return res}}).catch(()=>caches.match('./index.html')));return}}
 const u=new URL(r.url);if(u.origin!==self.location.origin&&!/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname))return;
 if(u.origin===self.location.origin&&!u.pathname.startsWith(new URL(self.registration.scope).pathname))return;
 e.respondWith(caches.match(r).then(hit=>hit||fetch(r).then(res=>{{if(res.ok||res.type==='opaque'){{const cp=res.clone();caches.open(C).then(c=>c.put(r,cp))}}return res}}).catch(()=>hit)))}});
"""
(D / "sw.js").write_text(sw.replace("__EXTRA__", extra), encoding="utf-8")
print("Listo:", D, "versión", ver, f"({len(out)//1024} KB)")
