"""Construye 03-registro-tratamientos/asistente-rat.html desde rat_config.py.

Uso: python scripts/generar_asistente_rat.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import rat_config as C  # noqa: E402

from generar_rat import EJEMPLO_CLINICA  # noqa: E402

# Mismo ejemplo ficticio que el Excel, con fechas en texto ISO.
EJEMPLO = [{k: (v.isoformat() if hasattr(v, "isoformat") else v) for k, v in fila.items()} for fila in EJEMPLO_CLINICA]

cfg = {
    "listas": C.LISTAS, "bases": C.BASES, "preguntas": C.PREGUNTAS, "grupos": C.GRUPOS, "ejemplo": EJEMPLO,
    "campos": C.CAMPOS, "secciones": C.SECCIONES, "catalogo": C.CATALOGO, "riesgo": C.RIESGO,
    "revision_meses": C.REVISION_MESES, "genericas": C.FINALIDADES_GENERICAS, "separable": C.FINALIDAD_SEPARABLE,
}
shell = (ROOT / "scripts" / "plantilla-asistente-rat.html").read_text(encoding="utf-8")
out = ROOT / "03-registro-tratamientos" / "asistente-rat.html"
out.write_text(shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("OK", out)
