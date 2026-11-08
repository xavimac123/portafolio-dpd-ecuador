"""Construye 05-madurez/asistente-madurez.html y 05-madurez/cuestionario-madurez.md desde madurez_config.py.

Uso: python scripts/generar_asistente_madurez.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import madurez_config as C  # noqa: E402

OUT = ROOT / "05-madurez"
OUT.mkdir(exist_ok=True)

# Ejemplo ficticio: pyme comercial de 45 trabajadores con adecuación inicial
EJ_R = {
    "gob": [2, 1, 1, 0], "dpd": [3, "na", "na"], "rat": [2, 1, 0], "lic": [2, 2, "na", 1], "tra": [3, 2, 1],
    "der": [2, 1, 1], "enc": [2, 1, 0], "seg": [2, 2, 3, 1], "eipd": [1, "na", 0], "vul": [1, 1, 0, 1],
    "tri": [2, 1], "cul": [1, 3, 0],
}
ejemplo = {
    "ctx": {"ctx_emp": "Ferretería Ficticia El Tornillo S.A. (EJEMPLO)", "ctx_sector": "Comercio", "ctx_trab": "10 a 49",
            "ctx_fecha": "2026-11-07", "ctx_entrev": "Gerente general, contadora, jefe de ventas"},
    "r": {f"{d}_{i}": (str(v) if v != "na" else "na") for d, vals in EJ_R.items() for i, v in enumerate(vals)},
    "c": {"dpd_1": "No obligada: ninguna causal del art. 10 de la Res. 0028 (análisis de 2026-10).",
          "dpd_2": "No aplica al no existir DPD.", "lic_2": "No se usa interés legítimo.", "eipd_1": "Ningún tratamiento obligado a evaluación."},
    "f": {"f_el": "Abg. Mariano X. Macías Sánchez", "f_ec": "Consultor en Protección de Datos · Mat. 09-2022-736",
          "f_ap": "[REPRESENTANTE LEGAL]", "f_ac": "Gerente General"},
}

cfg = {"escala": C.ESCALA, "niveles": C.NIVELES, "dominios": C.DOMINIOS, "contexto": C.CONTEXTO, "ejemplo": ejemplo}
shell = (ROOT / "scripts" / "plantilla-asistente-madurez.html").read_text(encoding="utf-8")
(OUT / "asistente-madurez.html").write_text(
    shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("OK", OUT / "asistente-madurez.html")

# Cuestionario imprimible (Markdown -> Word)
L = ["# Cuestionario de Madurez en Protección de Datos Personales", "",
     "**[ORGANIZACIÓN]** · Sector [SECTOR] · Trabajadores [NÚMERO] · Fecha [FECHA] · Entrevistados [PERSONAS]", "",
     "> **Nota para quien aplica el cuestionario (eliminar antes de entregar):** modelo propio de Macías Sánchez "
     "Consultores; la SPDP no ha emitido un modelo oficial de madurez. Puntúa con base en evidencia. N/A no cuenta en el "
     "promedio. Índice = promedio ponderado de los dominios (los críticos pesan el doble). El asistente web "
     "`asistente-madurez.html` hace el cálculo, el gráfico y el plan de acción.", "",
     "## Escala de respuesta", "", "| Puntaje | Nivel | Significado |", "|---|---|---|"]
L += [f"| {v} | {n} | {d} |" for v, n, d in C.ESCALA] + ["| N/A | No aplica | Justificar en la columna de evidencia |", ""]
L += ["## Niveles de madurez", "", "| Índice | Nivel | Lectura |", "|---|---|---|"]
L += [f"| {a:.1f} a {b:.1f} | {n} | {d} |" for a, b, n, d in C.NIVELES] + [""]
for i, d in enumerate(C.DOMINIOS, start=1):
    L += [f"## {i}. {d['nombre']}{' (crítico)' if d['peso'] > 1 else ''}", "", f"Base: {d['base']}. Herramienta: {d['herramienta']}.", "",
          "| Pregunta | Evidencia sugerida | Puntaje (0-4 / N/A) | Evidencia revisada |", "|---|---|---|---|"]
    L += [f"| {q} | {e} | [ ] | [EVIDENCIA] |" for q, e in d["preguntas"]]
    L += ["", f"**Puntaje del dominio:** [PROMEDIO]", ""]
L += ["## Resultado", "", "| Índice de madurez | Nivel |", "|---|---|", "| [ÍNDICE] | [NIVEL] |", ""]
(OUT / "cuestionario-madurez.md").write_text("\n".join(L), encoding="utf-8")
print("OK", OUT / "cuestionario-madurez.md")
