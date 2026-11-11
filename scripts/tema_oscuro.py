"""Genera el modo oscuro de las herramientas a partir de su propio CSS.

Lee las reglas de cada página, resuelve las variables de :root y, para cada color de fondo, de texto o de borde,
escribe una regla «html.msc-dark selector{...!important}» con el color equivalente oscuro (mismo tono, otra luminosidad).
Así se respetan los estados (.on, [aria-selected]) porque se transforma regla por regla. La app activa la clase
msc-dark en la herramienta cuando ella misma está en modo oscuro. Los colores de estilos en línea se ajustan en
tiempo de ejecución con la misma función (JS_MAPA).
"""
import colorsys
import re

FONDO_OSCURO = (0x0F, 0x12, 0x16)


def _hex(c):
    c = c.lstrip("#")
    if len(c) == 3:
        c = "".join(x * 2 for x in c)
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _a_hex(rgb):
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(v))) for v in rgb)


def mapear(color, tipo):
    """tipo: 'bg' (fondo), 'tx' (texto) o 'bd' (borde)."""
    r, g, b = [v / 255 for v in _hex(color)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if tipo == "tx":
        if l > 0.55:
            return None  # texto claro: ya se lee sobre fondo oscuro
        l2 = 0.86 - l * 0.35
        s2 = min(s, 0.45)
    elif tipo == "bd":
        if l < 0.6:
            return None
        l2, s2 = 0.21, min(s, 0.15)
    else:
        if l < 0.2:
            l2, s2 = 0.2, min(s, 0.12)  # fondos muy oscuros (botones, seleccionados): un poco más claros que la tarjeta
        elif l > 0.55:
            l2, s2 = 0.08 + (1 - l) * 0.55, min(s, 0.35)
        else:
            return None
    r2, g2, b2 = colorsys.hls_to_rgb(h, max(0, min(1, l2)), s2)
    return _a_hex((r2 * 255, g2 * 255, b2 * 255))


def _reglas(css):
    """Devuelve (prefijo_media, selector, declaraciones) para reglas simples y dentro de @media."""
    out, i, n = [], 0, len(css)
    while i < n:
        a = css.find("{", i)
        if a < 0:
            break
        sel = css[i:a].strip()
        if sel.startswith("@media"):
            prof, j = 1, a + 1
            while j < n and prof:
                prof += {"{": 1, "}": -1}.get(css[j], 0)
                j += 1
            for _, s2, d2 in _reglas(css[a + 1:j - 1]):
                out.append((sel, s2, d2))
            i = j
            continue
        z = css.find("}", a)
        out.append(("", sel, css[a + 1:z]))
        i = z + 1
    return out


PROPS = {"background": "bg", "background-color": "bg", "color": "tx", "-webkit-text-fill-color": "tx", "caret-color": "tx",
         "border-color": "bd", "border": "bd", "border-top": "bd", "border-bottom": "bd", "border-left": "bd", "border-right": "bd", "outline": "bd"}
RE_COLOR = re.compile(r"#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b|\bwhite\b|\bvar\(--[\w-]+\)")


def css_oscuro(html):
    estilos = "".join(re.findall(r"<style[^>]*>(.*?)</style>", html, flags=re.S))
    estilos = re.sub(r"/\*.*?\*/", "", estilos, flags=re.S)
    root = {}
    for _, sel, d in _reglas(estilos):
        if sel.strip() == ":root":
            for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;]+)", d):
                root[k] = v.strip()
    salida = ["html.msc-dark{color-scheme:dark}html.msc-dark,html.msc-dark body{background:#0F1216!important;color:#E7E4DA!important}",
              "html.msc-dark input::placeholder,html.msc-dark textarea::placeholder{color:#8C8F96!important;-webkit-text-fill-color:#8C8F96!important}",
              "html.msc-dark select option{background:#1C2128;color:#E7E4DA}",
              "html.msc-dark button:disabled{opacity:.45}"]
    for media, sel, d in _reglas(estilos):
        if not sel or sel.startswith("@") or sel.strip() in (":root", "html,body", "body", "html"):
            continue
        nuevas = []
        decl = re.findall(r"([\w-]+)\s*:\s*([^;]+)", d)
        # Si la regla pone un fondo de color de marca (tono medio), el texto se deja tal cual: ya contrasta.
        fondo_medio = False
        for prop, val in decl:
            if PROPS.get(prop.strip()) == "bg":
                for c in RE_COLOR.findall(val):
                    c = root.get(c[4:-1], "") if c.startswith("var(") else ("#FFFFFF" if c == "white" else c)
                    if c.startswith("#"):
                        r, g, b = [v / 255 for v in _hex(c)]
                        if 0.2 <= colorsys.rgb_to_hls(r, g, b)[1] <= 0.55:
                            fondo_medio = True
        # Botones y elementos seleccionados: si el fondo es oscuro (carbón), pasan a dorado con texto oscuro,
        # como en la app; si es claro, a gris elevado con borde visible.
        es_boton = bool(re.search(r"btn|button|\.on\b|aria-selected|\.sel\b|\.act\b", sel))
        if es_boton:
            oscuro = claro = False
            for prop, val in decl:
                if PROPS.get(prop.strip()) == "bg":
                    for c in RE_COLOR.findall(val):
                        c = root.get(c[4:-1], "") if c.startswith("var(") else ("#FFFFFF" if c == "white" else c)
                        if c.startswith("#"):
                            r, g, b = [v / 255 for v in _hex(c)]
                            L = colorsys.rgb_to_hls(r, g, b)[1]
                            oscuro = oscuro or L < 0.2
                            claro = claro or L > 0.55
            if oscuro:
                nuevas = ["background:#A09046!important", "color:#14181E!important", "border-color:#A09046!important", "-webkit-text-fill-color:#14181E!important"]
            elif claro:
                nuevas = ["background:#1F252D!important", "color:#E7E4DA!important", "border-color:#4A525E!important", "-webkit-text-fill-color:#E7E4DA!important"]
            if oscuro or claro:
                sels = ",".join("html.msc-dark " + x.strip() for x in sel.split(",") if x.strip())
                regla = sels + "{" + ";".join(nuevas) + "}"
                salida.append(media + "{" + regla + "}" if media else regla)
                continue
        for prop, val in decl:
            if fondo_medio and PROPS.get(prop.strip()) == "tx":
                continue
            tipo = PROPS.get(prop.strip())
            if not tipo:
                continue
            def sub(m):
                c = m.group(0)
                if c.startswith("var("):
                    c = root.get(c[4:-1], "")
                if c == "white":
                    c = "#FFFFFF"
                if not c.startswith("#"):
                    return m.group(0)
                nv = mapear(c, tipo)
                return nv or m.group(0)
            v2 = RE_COLOR.sub(sub, val)
            if v2 != val:
                nuevas.append("%s:%s!important" % (prop.strip(), v2.strip()))
        if nuevas:
            sels = ",".join("html.msc-dark " + s.strip() for s in sel.split(",") if s.strip())
            regla = sels + "{" + ";".join(nuevas) + "}"
            salida.append(media + "{" + regla + "}" if media else regla)
    return "".join(salida)


JS_MAPA = r"""function mscMap(hex,t){var c=hex.replace('#','');if(c.length===3)c=c.replace(/./g,'$&$&');var r=parseInt(c.substr(0,2),16)/255,g=parseInt(c.substr(2,2),16)/255,b=parseInt(c.substr(4,2),16)/255,mx=Math.max(r,g,b),mn=Math.min(r,g,b),l=(mx+mn)/2,s=0,h=0,d=mx-mn;
 if(d){s=l>.5?d/(2-mx-mn):d/(mx+mn);h=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;h/=6}var l2,s2;
 if(t==='tx'){if(l>.55)return null;l2=.86-l*.35;s2=Math.min(s,.45)}else{if(l<.2){l2=.2;s2=Math.min(s,.12)}else if(l>.55){l2=.08+(1-l)*.55;s2=Math.min(s,.35)}else return null}
 var q=l2<.5?l2*(1+s2):l2+s2-l2*s2,p=2*l2-q,f=function(t){t<0&&(t+=1);t>1&&(t-=1);return t<1/6?p+(q-p)*6*t:t<.5?q:t<2/3?p+(q-p)*(2/3-t)*6:p},x=function(v){return('0'+Math.round(v*255).toString(16)).slice(-2)};
 return '#'+x(f(h+1/3))+x(f(h))+x(f(h-1/3))}
function mscInline(root){[].slice.call((root||document).querySelectorAll('[style*="#"]')).forEach(function(e){if(e.dataset.mscd)return;e.dataset.mscd=1;var st=e.getAttribute('style'),n=st.replace(/(background(?:-color)?|color)\s*:\s*(#[0-9A-Fa-f]{3,6})/g,function(m,pr,hx){var v=mscMap(hx,pr==='color'?'tx':'bg');return v?pr+':'+v:m});if(n!==st)e.setAttribute('style',n)})}"""
