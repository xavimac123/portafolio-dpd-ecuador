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
import os  # noqa: E402
# MSC_PUBLICO=1: compilación para un sitio público; no incluye las copias de bases jurídicas de uso del suscriptor.
PUBLICO = os.environ.get("MSC_PUBLICO") == "1"
pdf = {k: ("normas/%s.pdf" % k if not PUBLICO and (NORMAS / (k + ".pdf")).exists() else "") for k in ("lopdp", "rglopdp")}
import glosario_config as GLC  # noqa: E402
import responsabilidades_config as RESP  # noqa: E402
glo = {"lopdp": CAT.GLOSARIO_LOPDP, "norma": CAT.GLOSARIO_NORMATIVA, "iso": GLC.ISO, "metodos": GLC.METODOS}
ref = {"rev": REFC.REVISION, "normas": REFC.NORMAS, "plazos": REFC.PLAZOS, "contraste": contraste, "abiertos": abiertos, "pdf": pdf, "enlaces": REFC.ENLACES}
dpo = {k: getattr(RESP, k) for k in ("REVISION", "INTRO", "FUNCIONES", "GARANTIAS", "PROHIBICIONES", "IMPEDIMENTOS", "NO_ES", "AUDITORIA", "ANTES", "ABIERTOS", "QUIEN", "TEMAS", "INFRACCIONES")}
import publicidad_config as PUBC  # noqa: E402
pub = {k: getattr(PUBC, k) for k in ("PREGUNTAS", "DATOS", "CTA", "BAJA", "AUTODIAG", "ESTRATEGIA")}
pub["SERV"] = [[x["cod"], x["nombre"], x["beneficio"], x["que"], x["fase"]] for x in CAT.SERVICIOS]
exp_js = (ROOT / "scripts" / "exportar.js").read_text(encoding="utf-8").replace("</", "<\\/")
src = src.replace("__SEP_JSON__", js({"roles": CAT.ROLES_MSC, "impl": CAT.IMPLEMENTACION, "lineas": CAT.LINEAS}))
src = src.replace("__TOOLS_JSON__", js(tools)).replace("__SERV_JSON__", js(serv)).replace("__IMG_JSON__", js(img))
src = src.replace("__REF_JSON__", js(ref)).replace("__GLO_JSON__", js(glo)).replace("__EXPORT_JS__", exp_js).replace("__DPO_JSON__", js(dpo)).replace("__PUB_JSON__", js(pub))
assert "__PUB_JSON__" not in src and "__DPO_JSON__" not in src and "__GLO_JSON__" not in src and "__REF_JSON__" not in src and "__EXPORT_JS__" not in src
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
 if(r.mode==='navigate'){{const np=new URL(r.url).pathname,sp=new URL(self.registration.scope).pathname;if(np!==sp&&np!==sp+'index.html')return;e.respondWith(fetch(r).then(res=>{{const cp=res.clone();caches.open(C).then(c=>c.put('./index.html',cp));return res}}).catch(()=>caches.match('./index.html')));return}}
 const u=new URL(r.url);if(u.origin!==self.location.origin&&!/fonts\\.(googleapis|gstatic)\\.com$/.test(u.hostname))return;
 if(u.origin===self.location.origin&&!u.pathname.startsWith(new URL(self.registration.scope).pathname))return;
 e.respondWith(caches.match(r).then(hit=>hit||fetch(r).then(res=>{{if(res.ok||res.type==='opaque'){{const cp=res.clone();caches.open(C).then(c=>c.put(r,cp))}}return res}}).catch(()=>hit)))}});
"""
(D / "sw.js").write_text(sw.replace("__EXTRA__", extra), encoding="utf-8")

# --- Página puente del autodiagnóstico: vista previa con la marca (og:image) y redirección al formulario ---
def puente():
    from PIL import Image, ImageDraw, ImageFont
    import html as H
    A = PUBC.AUTODIAG
    PD = D / "autodiagnostico"; PD.mkdir(exist_ok=True)
    F = ROOT / "scripts" / "vendor" / "fonts"
    f = lambda n, z: ImageFont.truetype(str(F / n), z)
    W, Hh = 1200, 630
    im = Image.new("RGB", (W, Hh), (20, 24, 30)); d = ImageDraw.Draw(im)
    for i in range(6):
        d.line([(W - 470 + i * 75, -20), (W + 80, 470 - i * 75)], fill=(52, 50, 38), width=3)
    d.rectangle([0, Hh - 14, W, Hh], fill=(160, 144, 70))
    iso = Image.open(R / "assets" / "logo-msc-original.png").convert("RGBA").crop((0, 0, 876, 889)).resize((118, 120), Image.LANCZOS)
    im.paste(iso, (70, 60), iso)
    d.text((212, 74), "MACÍAS SÁNCHEZ", font=f("ArchivoExp-ExtraBold.ttf", 40), fill=(160, 144, 70))
    d.text((214, 128), "CONSULTORES · PROTECCIÓN DE DATOS", font=f("Archivo-SemiBold.ttf", 22), fill=(201, 188, 130))
    d.rounded_rectangle([70, 230, 70 + 330, 278], radius=24, fill=(160, 144, 70))
    d.text((92, 240), "GRATIS · 5 MINUTOS", font=f("ArchivoExp-Bold.ttf", 24), fill=(20, 24, 30))
    d.text((70, 300), "Autodiagnóstico de", font=f("ArchivoExp-ExtraBold.ttf", 58), fill=(247, 245, 238))
    d.text((70, 370), "protección de datos", font=f("ArchivoExp-ExtraBold.ttf", 58), fill=(247, 245, 238))
    d.rectangle([70, 452, 190, 458], fill=(160, 144, 70))
    d.text((70, 480), "15 preguntas · su nivel de riesgo frente a la LOPDP al instante", font=f("Archivo-Regular.ttf", 28), fill=(231, 228, 218))
    d.text((70, 530), "Ecuador · Ley Orgánica de Protección de Datos Personales", font=f("Archivo-Medium.ttf", 22), fill=(154, 161, 170))
    im.save(PD / "og.png", optimize=True)
    url, base = A["url"], A["corto"]
    t, desc = "Autodiagnóstico de protección de datos · Macías Sánchez Consultores", "15 preguntas, 5 minutos y el nivel de riesgo de su empresa frente a la LOPDP al instante. Gratis."
    e = H.escape
    (PD / "index.html").write_text(f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(t)}</title><meta name="description" content="{e(desc)}"><meta name="robots" content="noindex">
<meta property="og:type" content="website"><meta property="og:site_name" content="Macías Sánchez Consultores"><meta property="og:locale" content="es_EC">
<meta property="og:title" content="{e(t)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{e(base)}">
<meta property="og:image" content="{e(base)}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Autodiagnóstico de protección de datos, Macías Sánchez Consultores">
<meta name="twitter:card" content="summary_large_image"><meta http-equiv="refresh" content="1;url={e(url)}">
<style>body{{margin:0;background:#14181E;color:#F7F5EE;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;display:flex;min-height:100vh;align-items:center;justify-content:center;text-align:center;padding:24px}}a{{color:#C9BC82}}img{{max-width:100%;border-radius:12px}}</style>
<script>location.replace({json.dumps(url)})</script></head><body><div><img src="og.png" alt="" width="600"><p>Abriendo el autodiagnóstico…</p><p><a href="{e(url)}">Si no se abre, toque aquí</a></p></div></body></html>""", encoding="utf-8")

puente()
print("Listo:", D, "versión", ver, f"({len(out)//1024} KB)")
