"""Genera los íconos (isotipo MSC + siglas PD) y las imágenes embebidas de la app."""
import base64, io, pathlib
from PIL import Image, ImageDraw, ImageFont
R = pathlib.Path(__file__).parent
FONT = R.parent / "scripts" / "vendor" / "fonts" / "ArchivoExp-ExtraBold.ttf"
CARBON, ORO, ORO_C = (20, 24, 30, 255), (160, 144, 70, 255), (201, 188, 130, 255)

def isotipo():
    return Image.open(R / "assets" / "logo-msc-original.png").convert("RGBA").crop((0, 0, 876, 889))

def icon(size, maskable=False):
    im = Image.new("RGBA", (size, size), CARBON)
    s = int(size * (0.40 if maskable else 0.50))
    fs = int(size * (0.19 if maskable else 0.235))
    gap = int(size * 0.045)
    e = isotipo().resize((s, round(s * 889 / 876)), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(str(FONT), fs)
    bb = d.textbbox((0, 0), "PD", font=f); tw, th = bb[2] - bb[0], bb[3] - bb[1]
    total = e.height + gap + th
    y0 = (size - total) // 2
    im.alpha_composite(e, ((size - e.width) // 2, y0))
    d.text(((size - tw) // 2 - bb[0], y0 + e.height + gap - bb[1]), "PD", font=f, fill=ORO_C)
    return im

def b64png(img):
    buf = io.BytesIO(); img.save(buf, "PNG", optimize=True); return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

if __name__ == "__main__":
    D = R / "docs" / "icons"; D.mkdir(parents=True, exist_ok=True)
    for n in (180, 192, 512): icon(n).save(D / f"icon-{n}.png")
    icon(512, True).save(D / "maskable-512.png")
    icon(1024).save(R / "assets" / "icono-pd-1024.png")
    iso = isotipo().resize((96, 97), Image.LANCZOS)
    line = Image.open(R / "assets" / "diseno-isotipo-lineas.png").convert("RGBA").resize((520, 520), Image.LANCZOS)
    # líneas en dorado claro, para fondos oscuros
    px = line.load()
    for yy in range(line.height):
        for xx in range(line.width):
            a = px[xx, yy][3]
            if a: px[xx, yy] = (201, 188, 130, a)
    (R / "assets" / "embebidos.txt").write_text(b64png(iso) + "\n" + b64png(line) + "\n" + b64png(icon(192)), encoding="utf-8")
    print("ok")
