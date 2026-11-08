"""Construye la herramienta 01: catálogo de servicios y glosario.

Salidas:
  01-catalogo-servicios/catalogo-servicios.html  (página web)
  01-catalogo-servicios/catalogo-servicios.md    (ficha interna completa, para Word)
  01-catalogo-servicios/glosario.md              (glosario, para Word)

Uso: python scripts/generar_catalogo.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import catalogo_config as C  # noqa: E402
import honorarios_config as H  # noqa: E402

OUT = ROOT / "01-catalogo-servicios"
OUT.mkdir(exist_ok=True)
TAM = ["micro", "peq", "med", "gra"]


def r10(x):
    return int(round(x / 10.0) * 10)


hora = r10(H.PERFILES[1][1] * (1 + H.GASTOS_PCT / 100))
DESDE = {"diag": [H.VOLNEG["diag_piso"][t] for t in TAM], "adec": [H.VOLNEG["adec_piso"][t] for t in TAM],
         "mens": [H.VOLNEG["piso_mensual"][t] for t in TAM], "acomp": [r10(H.VOLNEG["piso_mensual"][t] * 0.7) for t in TAM],
         "hora": [hora] * 4}
HERR = {"01": "Catálogo", "02": "Honorarios", "03": "Madurez", "04": "RAT", "05": "Gran escala", "06": "Interés legítimo", "07": "Evaluación de impacto",
        "08": "Plantillas", "09": "Vulneraciones"}
cfg = {"version": C.VERSION, "tamanos": C.TAMANOS, "fases": C.FASES, "naturaleza": C.NATURALEZA, "servicios": C.SERVICIOS,
       "recomendaciones": C.RECOMENDACIONES, "gloLopdp": C.GLOSARIO_LOPDP, "gloNorma": C.GLOSARIO_NORMATIVA, "gloKit": C.GLOSARIO_KIT,
       "desde": DESDE, "herramientas": HERR}
shell = (ROOT / "scripts" / "plantilla-catalogo.html").read_text(encoding="utf-8")
(OUT / "catalogo-servicios.html").write_text(shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("OK", OUT / "catalogo-servicios.html")


def usd(x):
    return "$" + f"{x:,.0f}".replace(",", ".")


def precios(s):
    if isinstance(s["precio"], str):
        k = s["precio"].split(":")[1]
        return " / ".join("desde " + usd(v) for v in DESDE[k])
    if not any(s["precio"]):
        return "Sin costo"
    return " / ".join(usd(v) for v in s["precio"])


M = ["# Catálogo de servicios de protección de datos personales", "",
     f"Versión {C.VERSION}. Ficha interna para el consultor. Fuente única: `scripts/catalogo_config.py` (también alimenta la proforma de la herramienta 02).", "",
     "> **Rol del consultor:** asesora, redacta borradores para aprobación y supervisa. Las decisiones y la implementación son de la empresa.", "",
     "Precios sugeridos sin IVA por tamaño (micro / pequeña / mediana / grande), **criterio propio**. «Desde» indica el piso de la calculadora de honorarios.", "",
     "## Índice", "", "| Código | Servicio | Fase | Naturaleza | Precio sugerido |", "|---|---|---|---|---|"]
M += [f"| {s['cod']} | {s['nombre']} | {s['fase']} | {C.NATURALEZA[s['nat']]} | {precios(s)} por {s['unidad']} |" for s in C.SERVICIOS]
for fase, desc in C.FASES:
    M += ["", f"## {fase}", "", desc]
    for s in [x for x in C.SERVICIOS if x["fase"] == fase]:
        M += ["", f"### {s['cod']} · {s['nombre']}", "", "| | |", "|---|---|",
              f"| Qué es | {s['que']} |", f"| Naturaleza | {C.NATURALEZA[s['nat']]} |",
              f"| Cómo se aplica | {'; '.join(s['como'])} |", f"| Para quién | {s['para']} |", f"| Qué se obtiene | {s['obtiene']} |",
              f"| Responsable principal | {s['resp']} |", f"| Participan | {s['conj']} |", f"| Levantar información con | {s['levantar']} |",
              f"| Herramientas del kit | {', '.join(h + ' ' + HERR[h] for h in s['herr']) or '—'} |", f"| Base | {s['base']} |",
              f"| Precio sugerido | {precios(s)} por {s['unidad']} |", f"| Recomendaciones | {' · '.join(s['rec'])} |"]
M += ["", "## Recomendaciones generales", ""] + [f"- **{a}.** {b}" for a, b in C.RECOMENDACIONES] + [""]
(OUT / "catalogo-servicios.md").write_text("\n".join(M) + "\n", encoding="utf-8")
print("OK", OUT / "catalogo-servicios.md")

G = ["# Glosario de protección de datos personales", "",
     "> Resumen fiel de las definiciones; no es texto literal. Para escritos formales cite el texto del Registro Oficial.", "",
     "## LOPDP, art. 4", "", "| Término | Definición |", "|---|---|"]
G += [f"| {a} | {b} |" for a, b in C.GLOSARIO_LOPDP]
G += ["", "## Reglamento y normativa de la SPDP", "", "| Término | Definición | Fuente |", "|---|---|---|"]
G += [f"| {a} | {b} | {c} |" for a, b, c in C.GLOSARIO_NORMATIVA]
G += ["", "## Conceptos del kit", "", "| Término | Definición |", "|---|---|"]
G += [f"| {a} | {b} |" for a, b in C.GLOSARIO_KIT] + [""]
(OUT / "glosario.md").write_text("\n".join(G) + "\n", encoding="utf-8")
print("OK", OUT / "glosario.md")
