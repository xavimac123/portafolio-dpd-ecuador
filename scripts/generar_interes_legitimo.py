"""Construye 06-interes-legitimo/ (página web e informe Markdown) desde interes_config.py.

Uso: python scripts/generar_interes_legitimo.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import interes_config as C  # noqa: E402

OUT = ROOT / "06-interes-legitimo"
OUT.mkdir(exist_ok=True)

EJEMPLO = {
    "y": {"priv": "Sí"}, "sup": "mkt", "cond": {"0": "Se cumple", "1": "Se cumple", "2": "Se cumple", "3": "Se cumple"},
    "x": {"x_sens": "No", "x_esp": "No", "x_perf": "No", "x_nna": "No", "x_masivo": "No"},
    "i": {"i_resp": "Ferretería Ficticia El Tornillo S.A. (EJEMPLO)", "i_trat": "Correos de ofertas a clientes actuales",
          "i_rat": "T-12", "i_benef": "El responsable",
          "i_int": "Informar a quienes ya compraron en la tienda sobre ofertas de productos similares a los adquiridos.",
          "i_datos": "Nombre, correo electrónico y categoría de los productos comprados.",
          "i_tit": "4.500 clientes con compras en los últimos 24 meses.",
          "i_otra": "El consentimiento sería una base posible, pero los clientes ya mantienen una relación comercial y esperan recibir información de la tienda; se ofrece oposición inmediata."},
    "car": {"c_licito": {"r": "Cumple", "j": "La publicidad de productos propios es una actividad lícita."},
            "c_real": {"r": "Cumple", "j": "Campañas mensuales ya planificadas."},
            "c_prop": {"r": "Cumple", "j": "Máximo dos correos al mes; sin perfiles detallados."},
            "c_expect": {"r": "Parcial", "j": "La política vigente no menciona el envío de ofertas: incorporarlo antes de iniciar."}},
    "n": {"n_indisp": {"r": "Cumple", "j": ""}, "n_alt": {"r": "Cumple", "j": ""},
          "n_min": {"r": "Cumple", "j": "No se usa teléfono ni dirección."}, "n_cons": {"r": "Cumple", "j": "Sin el envío, los clientes no conocen las ofertas y caen las ventas recurrentes."}, "n_plazo": {"r": "Parcial", "j": "Definir la baja automática a los 24 meses sin compras."}},
    "altd": "Publicidad en redes sin datos personales: no llega a los clientes recurrentes. Pedir consentimiento en caja: se mantiene como alternativa si la ponderación cambia.",
    "w": {"w_imp": 1, "w_benef": 1, "w_conexo": 2},
    "im": {"i_datos": 0, "i_expect": 1, "i_pos": 0, "i_efecto": 1, "i_escala": 1},
    "salv": ["Oposición gratuita e inmediata (darse de baja en un paso)", "Información previa específica y visible", "Minimización de datos", "Plazo de conservación corto con borrado automático"],
    "salvO": "", "mot": "El interés comercial es legítimo y esperado por clientes con relación previa. El impacto es bajo: datos de contacto, sin perfiles y con baja inmediata. Prevalece si se actualiza la política antes de iniciar.",
    "r": {"r_res": C.RESULTADOS[1], "r_pol": "Se incorporará antes de iniciar", "r_opo": "Enlace de baja en cada correo y privacidad@ejemplo.ec",
          "r_cod": "IL-2026-01", "r_fec": "2026-11-10", "r_rev": "2027-11-10", "r_obs": "Ejemplo ficticio."},
    "f": {"f_el": "Abg. Mariano X. Macías Sánchez", "f_ec": "Consultor en Protección de Datos · Mat. 09-2022-736",
          "f_ap": "[REPRESENTANTE LEGAL]", "f_ac": "Gerente General"},
}

cfg = {"supuestos": C.SUPUESTOS, "prohibiciones": C.PROHIBICIONES, "caracteristicas": C.CARACTERISTICAS,
       "resp": C.RESP, "necesidad": C.NECESIDAD, "peso": C.PESO_INTERES, "impacto": C.IMPACTO_TITULAR,
       "salvaguardas": C.SALVAGUARDAS, "salvReduce": C.SALV_REDUCE, "salvTope": C.SALV_TOPE,
       "resultados": C.RESULTADOS, "revision": C.REVISION_MESES, "ejemplo": EJEMPLO}
shell = (ROOT / "scripts" / "plantilla-interes-legitimo.html").read_text(encoding="utf-8")
(OUT / "asistente-interes-legitimo.html").write_text(
    shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")

# ---- informe en Markdown (para Word)
L = ["# Evaluación de ponderación del interés legítimo", "",
     "| Campo | Contenido |", "|---|---|", "| Responsable | [RAZÓN SOCIAL] |", "| Tratamiento | [TRATAMIENTO] |",
     "| Código en el RAT | [CÓDIGO] |", "| Código de la evaluación | [IL-AAAA-NN] |", "| Fecha | [FECHA] |", "",
     "Evaluación previa exigida por la Resolución SPDP-SPD-2025-0041-R para usar el interés legítimo como base de legitimación "
     "(art. 7 LOPDP), con los criterios mínimos de su Anexo 1. Se conserva y está disponible para la Superintendencia de "
     "Protección de Datos Personales y para los titulares.", "",
     "## 1. Ámbito, supuesto admisible y prohibiciones", "", "Responsable del sector privado: [SÍ / NO]", "",
     "Supuesto admisible (marcar uno):", ""]
L += [f"- [ ] {s['nombre']}. Condiciones: {'; '.join(s['cond'])}." for s in C.SUPUESTOS]
L += ["", "| Prohibición | Respuesta | Consecuencia |", "|---|---|---|"]
L += [f"| {p['texto']} | [SÍ / NO] | {p['nota']} |" for p in C.PROHIBICIONES]
L += ["", "## 2. Identificación y justificación del interés", "", "| Campo | Contenido |", "|---|---|",
      "| Titular del interés | [RESPONSABLE / TERCERO] |", "| Interés invocado | [DESCRIPCIÓN] |", "| Datos | [DATOS] |",
      "| Titulares y volumen | [TITULARES] |", "| Por qué no otra base | [JUSTIFICACIÓN] |", "",
      "| Característica (Res. SPDP-SPD-2025-0041-R, art. 4) | Valoración | Justificación |", "|---|---|---|"]
L += [f"| {c['nombre']}: {c['pregunta']} | [CUMPLE / PARCIAL / NO CUMPLE] | [ ] |" for c in C.CARACTERISTICAS]
L += ["", "## 3. Necesidad", "", "| Criterio | Valoración | Justificación |", "|---|---|---|"]
L += [f"| {c['texto']} | [ ] | [ ] |" for c in C.NECESIDAD]
L += ["", "Alternativas consideradas y por qué se descartaron: [ ]", "",
      "## 4. Ponderación con los derechos del titular", "",
      "Puntajes de **criterio propio** de Macías Sánchez Consultores (0 a 2 por factor). No provienen de la resolución.", "",
      "| Factor | Opciones (0 / 1 / 2) | Valor |", "|---|---|---|"]
L += [f"| Interés: {f['nombre']} | {' / '.join(o[0] for o in f['ops'])} | [ ] |" for f in C.PESO_INTERES]
L += [f"| Titular: {f['nombre']} | {' / '.join(o[0] for o in f['ops'])} | [ ] |" for f in C.IMPACTO_TITULAR]
L += ["", f"Cada salvaguarda implementada reduce {str(C.SALV_REDUCE).replace('.', ',')} puntos el impacto, hasta {C.SALV_TOPE} (criterio propio).", "",
      "Motivación de la ponderación: [ ]", "", "## 5. Salvaguardas", ""]
L += [f"- [ ] {s}" for s in C.SALVAGUARDAS]
L += ["", "## 6. Resultado, transparencia y registro", ""]
L += [f"- [ ] {r}" for r in C.RESULTADOS]
L += ["", "| Campo | Contenido |", "|---|---|", "| Consta en la política de privacidad | [ ] |", "| Canal de oposición | [ ] |",
      "| Próxima revisión (plazo de un año, art. 18) | [FECHA] |", "| Conservación de evidencias (Anexo 1) | Cinco años, o la duración del tratamiento más dos años |", "",
      "La evaluación se revisa al menos una vez al año o cuando cambien la finalidad, el tipo de datos o el nivel de riesgo. "
      "El titular puede ejercer en cualquier momento sus derechos, en especial el de oposición.", ""]
(OUT / "informe-ponderacion.md").write_text("\n".join(L), encoding="utf-8")
print("OK", OUT)
