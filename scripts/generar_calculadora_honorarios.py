"""Construye la herramienta 02 desde honorarios_config.py.

Salidas:
  02-honorarios/calculadora-honorarios.html  (página web)
  02-honorarios/metodologia-honorarios.md    (método, tablas y fuentes)
  02-honorarios/proforma-servicios.md        (plantilla de proforma para Word)

Uso: python scripts/generar_calculadora_honorarios.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import honorarios_config as C  # noqa: E402

OUT = ROOT / "02-honorarios"
OUT.mkdir(exist_ok=True)

ejemplo = {
    "c": {"emp": "Ferretería Ficticia El Tornillo S.A. (EJEMPLO)", "ruc": "[RUC]", "contacto": "[NOMBRE DEL GERENTE]", "cargo": "Gerente general",
          "sector": "Comercio", "ventas": "1850000", "trab": "45", "sedes": "2", "act": "8", "enc": "5", "sol": "1", "tr": "Sí",
          "eipd": "1", "cap": "4", "areas": ""},
    "v": {"tit": 1, "vol": 1, "cat": 0, "fre": 1, "per": 2, "geo": 1, "dir": []},
    "t": {"perfil": "1", "tarifa": C.PERFILES[1][1], "gastos": C.GASTOS_PCT, "ov": {}},
    "k": {"met": "rec", "salario": C.DPD_INTERNO["salario"], "regimen": "Persona natural", "agente": "Sí",
          "retir": C.ECON["ret_ir_natural"], "retiva": C.ECON["ret_iva"], "horas": 20},
    "p": {"num": "MSC-2026-001", "fecha": "2026-11-08", "validez": 30, "meses": 12, "desc": 0, "iva": C.ECON["iva"],
          "cond": C.CONDICIONES, "multa": "17773.88", "aten": "",
          "rol": "dpo", "impl": "msc_directo", "implNom": "[IMPLEMENTADOR ALIADO]", "implVal": "",
          "items": {"diag": {"on": True, "q": 1, "v": ""}, "adec": {"on": True, "q": 1, "v": ""}, "dpd": {"on": True, "q": 1, "v": ""},
                    "verificacion": {"on": True, "q": 3, "v": ""},
                    "capac": {"on": True, "q": 1, "v": ""}, "incidente": {"on": True, "q": 1, "v": ""}, "hora": {"on": True, "q": 1, "v": ""}},
          "f": {"el": "Abg. Mariano X. Macías Sánchez", "ec": "Consultor en Protección de Datos Personales · Matrícula profesional 09-2022-736",
                "cl": "[REPRESENTANTE LEGAL]", "cc": "Gerente general"}},
}

cfg = {"version": C.VERSION, "econ": C.ECON, "tamanos": C.TAMANOS, "sectores": C.SECTORES, "volneg": C.VOLNEG, "mtge": C.MTGE,
       "voltrat": C.VOLTRAT, "perfiles": C.PERFILES, "gastos": C.GASTOS_PCT, "tareas": C.TAREAS, "areas": C.AREAS_POR_TAMANO,
       "dpdInterno": C.DPD_INTERNO, "rolesMsc": C.ROLES_MSC, "impl": C.IMPLEMENTACION, "lineas": C.LINEAS, "paquetes": C.PAQUETES, "servicios": C.SERVICIOS, "grupos": C.GRUPOS, "condiciones": C.CONDICIONES,
       "beneficios": C.BENEFICIOS, "ejemplo": ejemplo}
shell = (ROOT / "scripts" / "plantilla-calculadora-honorarios.html").read_text(encoding="utf-8")
(OUT / "calculadora-honorarios.html").write_text(
    shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("OK", OUT / "calculadora-honorarios.html")


def usd(x):
    return "$" + f"{x:,.0f}".replace(",", ".")


def n(x):
    return f"{x:g}".replace(".", ",")


TAM = ["micro", "peq", "med", "gra"]
TAMN = ["Micro", "Pequeña", "Mediana", "Grande"]

# ------------------------------------------------------------------ metodología
M = ["# Metodología de la calculadora de honorarios del DPD", "",
     f"Versión {C.VERSION}. Fuente única: `scripts/honorarios_config.py`.", "",
     "> **Criterio propio.** No existe en Ecuador una tabla oficial ni gremial de honorarios para el Delegado de Protección de Datos. "
     "Los tramos, pisos, tarifas y factores de esta herramienta son criterio propio de Macías Sánchez Consultores, contrastados con "
     "referencias públicas del mercado (sección «Referencias de mercado»). Solo son normativos: la clasificación de empresas, el "
     "Modelo Técnico de Gran Escala, la tarifa del IVA, las retenciones y los rubros laborales del DPD interno.", "",
     "## Fases del servicio", "",
     "| Fase | Cobro | Qué incluye |", "|---|---|---|",
     "| Evaluación inicial | Única vez | Diagnóstico de madurez, exposición económica, análisis de gran escala y plan de acción |",
     "| Implementación (referencial) | Única vez | RAT, política y avisos, contratos de encargo, protocolo de vulneraciones, derechos. La decide el responsable y la ejecuta su personal, un proveedor o un tercero coordinado por MSC; solo suma a la proforma si la factura MSC (subcontratada o como consultor que no es DPO del cliente). Si no, el valor sirve para comparar la cotización del implementador |",
     "| Revisión y verificación | Por evaluación o por hito | S29 revisión del DPO a evaluaciones elaboradas por el responsable; S30 verificación de lo implementado |",
     "| Control | Mensual | DPD externo o acompañamiento: supervisión, RAT vivo, derechos, incidentes, reporte a la gerencia |", "",
     "## Tamaño de la empresa", "",
     "Reglamento a la Estructura e Institucionalidad de Desarrollo Productivo del COPCI, art. 106; COPCI art. 53 (las ventas prevalecen sobre los trabajadores).", "",
     "| Tamaño | Trabajadores | Ventas anuales (USD) |", "|---|---|---|"]
for t in C.TAMANOS:
    tr = f"{t['trab'][0]} a {t['trab'][1]}" if t["trab"][1] else f"{t['trab'][0]} o más"
    ve = f"{usd(t['ventas'][0])} a {usd(t['ventas'][1])}" if t["ventas"][1] else f"más de {usd(t['ventas'][0] - 0.01)}"
    M.append(f"| {t['nombre']} | {tr} | {ve} |")
M += ["", "Factor sectorial (criterio propio): " + "; ".join(f"{s} ×{n(f)}" for s, f in C.SECTORES if f != 1) + ". Resto ×1.", "",
      "## Método 1 · Volumen de negocio", "",
      "Honorario **anual** de control = suma de cada tramo de ventas × su porcentaje marginal. Control mensual = máximo entre el piso del tamaño y el anual / 12.", "",
      "| Tramo de ventas | % marginal |", "|---|---|"]
for a, b, p in C.VOLNEG["tramos"]:
    M.append(f"| {usd(a)} a {usd(b) if b else 'más'} | {n(p)} % |")
M += ["", "| | " + " | ".join(TAMN) + " |", "|---|---|---|---|---|",
      "| Piso mensual | " + " | ".join(usd(C.VOLNEG["piso_mensual"][k]) for k in TAM) + " |",
      "| Piso evaluación inicial | " + " | ".join(usd(C.VOLNEG["diag_piso"][k]) for k in TAM) + " |",
      "| Piso adecuación | " + " | ".join(usd(C.VOLNEG["adec_piso"][k]) for k in TAM) + " |", "",
      f"Evaluación inicial = máx(piso, {n(C.VOLNEG['diag_factor'] * 100)} % del control anual). Implementación (referencial) = máx(piso, {n(C.VOLNEG['adec_factor'] * 100)} % del control anual).", "",
      "## Método 2 · Volumen de tratamiento", "",
      "El puntaje es el **Modelo Técnico de Gran Escala (MTGE)** de la Res. SPDP-SPD-2026-0005-R (art. 8: variables; art. 9: suma; art. 10: umbral de 6 puntos; "
      "art. 12: efectos; art. 14: calificación directa). Se aplica al tratamiento principal del cliente.", "",
      "| Variable | Opciones y puntos |", "|---|---|"]
for v in C.MTGE["variables"]:
    M.append(f"| {v['nombre']} | " + "; ".join(f"{o} ({n(p)})" for o, p in v["ops"]) + " |")
M += ["", "Calificación directa (art. 14): " + "; ".join(C.MTGE["directa"]) + ".", "",
      "Tarifario sobre el puntaje (criterio propio):", "",
      "| Concepto | Valor |", "|---|---|"]
V = C.VOLTRAT
M += [f"| Base mensual por puntaje | {usd(V['base_mensual'][0][2])} (menos de 4), {usd(V['base_mensual'][1][2])} (4 a 5,9), {usd(V['base_mensual'][2][2])} (gran escala) |",
      f"| Por actividad sobre {V['act_incluidas']} | {usd(V['por_actividad'])}/mes |", f"| Por encargado | {usd(V['por_encargado'])}/mes |",
      f"| Transferencias internacionales | {usd(V['transferencias'])}/mes |", f"| Por solicitud de derechos mensual | {usd(V['por_solicitud'])} |",
      f"| Por sede adicional | {usd(V['por_sede'])}/mes |",
      f"| Evaluación inicial | {usd(V['diag']['base'])} + {usd(V['diag']['por_actividad'])} por actividad + {usd(V['diag']['por_encargado'])} por encargado + {usd(V['diag']['gran_escala'])} si es gran escala + {usd(V['diag']['por_sede'])} por sede adicional |",
      f"| Implementación (referencial) | {usd(V['adec']['base'])} + {usd(V['adec']['por_actividad'])} por actividad + {usd(V['adec']['por_encargado'])} por encargado + {usd(V['adec']['por_eipd'])} por evaluación de impacto |", "",
      "## Método 3 · Estimación técnica", "",
      "Horas por tarea × tarifa por hora × (1 + gastos indirectos). Las horas aumentan con el factor sectorial. Es el **piso** de la negociación.", "",
      "| Perfil | Tarifa sin IVA |", "|---|---|"]
M += [f"| {p} | {usd(t)}/h |" for p, t in C.PERFILES]
M += ["", f"Gastos indirectos y reserva por defecto: {C.GASTOS_PCT} %. Áreas a entrevistar por tamaño: " + ", ".join(f"{TAMN[i]} {C.AREAS_POR_TAMANO[k]}" for i, k in enumerate(TAM)) + ".", ""]
lab = {"diag": "Evaluación inicial", "adec": "Implementación (referencial)", "mens": "Control mensual"}
var = {"base": "fijo", "a": "por área", "act": "por actividad", "enc": "por encargado", "sol": "por solicitud", "tr": "si hay transferencias",
       "ge": "si es gran escala", "eipd": "por evaluación de impacto", "cap": "por hora de capacitación anual"}
for k in ("diag", "adec", "mens"):
    M += [f"**{lab[k]}**", "", "| Tarea | Horas |", "|---|---|"]
    M += [f"| {t} | " + " + ".join(f"{n(round(v, 3))} {var[x]}" for x, v in f.items()) + " |" for t, f in C.TAREAS[k]]
    M.append("")
M += ["## Recomendación", "",
      "Para cada fase: mediana de los tres métodos, y nunca menos que la estimación técnica. La herramienta advierte cuando el volumen de negocio "
      "no cubre el costo técnico (proponer menor alcance o cobro por evento) y cuando el tratamiento es de gran escala (el DPD es obligatorio).", "",
      "## Otras modalidades", "",
      "- **Paquetes** Esencial, Cumplimiento e Integral (servicios en `PAQUETES`).",
      "- **Bolsa de horas** prepagada: 5 % de descuento por menos de 20 h, 10 % desde 20 h y 15 % desde 40 h (criterio propio).",
      "- **Comparación con un DPD interno**: sueldo × 12 + aporte patronal "
      f"{n(C.ECON['aporte_patronal'])} % + décimo tercero (Código del Trabajo art. 111) + décimo cuarto, un SBU de {usd(C.ECON['sbu'])} (art. 113) + fondos de reserva 8,33 % (art. 196).",
      "- **Retenciones** para el consultor (uso interno): retención de renta y de IVA según la tabla vigente del SRI.", "",
      "## IVA y retenciones", "",
      f"- IVA: tarifa general {C.ECON['iva']} % (LRTI art. 65; el SRI recordó en la Circular NAC-DGECCGC25-00000006 que se mantiene mientras no la modifique un decreto ejecutivo).",
      f"- Retención de renta en honorarios profesionales de persona natural: {C.ECON['ret_ir_natural']} % (Res. NAC-DGERCGC26-00000009, desde el 1-03-2026). Sociedad: {C.ECON['ret_ir_sociedad']} % según resúmenes; verificar.",
      f"- Retención de IVA en honorarios profesionales de persona natural: {C.ECON['ret_iva']} % del IVA cuando el cliente es agente de retención (tabla vigente del SRI; verificar).", "",
      "## Referencias de mercado consultadas (no vinculantes)", "",
      "| Fuente | Dato | Fecha de consulta |", "|---|---|---|",
      "| Blue Nova (bluenova.com.ec), guía LOPDP 2026 | DPD externo USD 300 a 800 al mes; asesoría legal USD 1.000 a 5.000; cumplimiento básico USD 2.500 a 7.000; precios sin IVA | 2026-11-08 |",
      "| Blue Nova, diagnóstico LOPDP | Diagnóstico básico desde USD 500; con plan de acción desde USD 800; programa completo desde USD 2.500 | 2026-11-08 |",
      "| delegadodatosecuador.com | Precios por proforma; modalidad de DPD externo distinta para pequeña empresa (factura menos de USD 1 millón o menos de 15 empleados) y mediana | 2026-11-08 |",
      "| Aviso de empleo DPD, Quito (cazvid.com) | Sueldo de USD 1.500 a 2.500 al mes, tiempo completo | 2026-11-08 |",
      "| Jorge Badiola, «¿Cómo calcular los honorarios del DPD?» (LinkedIn) | Variables: tamaño, trabajadores, sedes, encargados y trabajo previo; cláusula de recuperación del esfuerzo inicial | 2026-11-08 |", "",
      "Actualice estas referencias y los parámetros económicos (IVA, SBU, retenciones) al inicio de cada año."]
(OUT / "metodologia-honorarios.md").write_text("\n".join(M) + "\n", encoding="utf-8")
print("OK", OUT / "metodologia-honorarios.md")

# ------------------------------------------------------------------ proforma (documento)
P = ["# Proforma de servicios de protección de datos personales", "",
     "**N.º [NÚMERO]** · [FECHA] · Validez: [DÍAS] días", "",
     "| | |", "|---|---|", "| Cliente | [RAZÓN SOCIAL] |", "| RUC | [RUC] |", "| Dirigida a | [NOMBRE Y CARGO] |",
     "| Perfil | [TAMAÑO] · sector [SECTOR] |", "",
     "> **Nota para el consultor (eliminar antes de entregar):** los valores sugeridos dependen del tamaño y el sector; "
     "calcúlelos en `calculadora-honorarios.html`. Elimine las filas de servicios que no ofrezca. Valores de referencia sin IVA "
     "por tamaño (micro / pequeña / mediana / grande), criterio propio: "
     + "; ".join(f"{s[7]} {s[2]}: " + " / ".join(usd(x) for x in s[5]) for s in C.SERVICIOS if isinstance(s[5], list)) + ".", "",
     "Agradecemos su interés. Presentamos la propuesta para que su organización cumpla la Ley Orgánica de Protección de Datos "
     "Personales (LOPDP), su Reglamento General y la normativa de la Superintendencia de Protección de Datos Personales (SPDP), y pueda demostrarlo.", ""]
grupos = []
for s in C.SERVICIOS:
    if s[0] not in grupos:
        grupos.append(s[0])
for i, g in enumerate(grupos, start=1):
    P += [f"## {i}. {g}" + (" (tarifas, no incluidas en el total)" if g == "Por evento" else ""), "",
          "| Servicio | Cantidad | Valor unitario | Subtotal |", "|---|---|---|---|"]
    P += [f"| **{s[7]} · {s[2]}**. {s[3]} | [CANT.] ({s[4]}) | [VALOR] | [SUBTOTAL] |" for s in C.SERVICIOS if s[0] == g]
    P.append("")
P += ["## Resumen económico", "", "| Concepto | Valor |", "|---|---|",
      "| Evaluación y adecuación, subtotal sin IVA | [VALOR] |", "| Descuento | [VALOR] |", "| IVA [15] % | [VALOR] |", "| **Total única vez** | **[VALOR]** |",
      "| Control mensual, subtotal sin IVA | [VALOR] |", "| IVA [15] % | [VALOR] |", "| **Total mensual** | **[VALOR]** |",
      "| **Inversión del primer año, con IVA** | **[VALOR]** |", "",
      "## Lo que su organización obtiene", ""]
P += [f"- **{s[2]}:** {s[6]}" for s in C.SERVICIOS if s[0] != "Por evento"]
P += ["", "## Por qué es una buena inversión", "",
      "- **Su inversión frente a su exposición.** La multa estimada si no actúa es de [MULTA ESTIMADA] (metodología de la Res. SPDP-SPD-2025-0022-R sobre su volumen de negocio). La inversión del primer año equivale al [PORCENTAJE] de esa exposición.",
      "- **La dedicación que necesita, sin carga laboral.** Un DPD a tiempo completo costaría alrededor de [COSTO ANUAL] al año con aportes y beneficios de ley; su organización requiere una dedicación estimada de [HORAS] horas al mes, que este servicio cubre por [VALOR ANUAL].",
      "- **Cumplimiento de una obligación expresa** (si aplica): su tratamiento principal alcanza [PUNTAJE] puntos en el Modelo Técnico de Gran Escala (Res. SPDP-SPD-2026-0005-R).", "",
      "## Nuestro compromiso", ""]
P += [f"- {b}" for b in C.BENEFICIOS]
P += ["", "## Condiciones", "", C.CONDICIONES, "",
      "Las estimaciones de exposición y ahorro son orientativas y no constituyen una liquidación de multa ni una garantía de resultado.", "",
      "---", "", "**FIRMA DE RESPONSABILIDAD**", "",
      "| Elaborado por | Aceptado por el cliente |", "|---|---|",
      "| Firma: ______________________ | Firma: ______________________ |",
      "| [ELABORADO POR] | [REPRESENTANTE LEGAL] |", "| [CARGO / MATRÍCULA] | [CARGO] |", "| | [RAZÓN SOCIAL] |", "",
      "Fecha de aceptación: [FECHA]", ""]
(OUT / "proforma-servicios.md").write_text("\n".join(P) + "\n", encoding="utf-8")
print("OK", OUT / "proforma-servicios.md")
