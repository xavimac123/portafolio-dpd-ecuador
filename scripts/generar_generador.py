"""Construye un generador web a partir de las plantillas Markdown.

Uso: python scripts/generar_generador.py
Mantiene una sola fuente: editar los .md y volver a ejecutar este script.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHELL = (ROOT / "scripts" / "plantilla-generador.html").read_text(encoding="utf-8")
MARKED = (ROOT / "scripts" / "vendor" / "marked.min.js").read_text(encoding="utf-8")
SHELL = SHELL.replace("/*__MARKED__*/", MARKED.replace("</script", "<\\/script"))

KITS = {
    ROOT / "02-kit-plantillas" / "generador-documentos.html": [
        ("Política de privacidad", "02-kit-plantillas/politica-privacidad.md"),
        ("Aviso de privacidad", "02-kit-plantillas/aviso-privacidad.md"),
        ("Contrato de encargo", "02-kit-plantillas/contrato-encargo.md"),
        ("Cláusulas de consentimiento", "02-kit-plantillas/clausulas-consentimiento.md"),
    ],
}

for out, items in KITS.items():
    data = [{"nombre": n, "md": (ROOT / p).read_text(encoding="utf-8")} for n, p in items]
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out.write_text(SHELL.replace("/*__TEMPLATES__*/", payload), encoding="utf-8")
    print("OK", out)
