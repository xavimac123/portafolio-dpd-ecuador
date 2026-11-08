"""Construye la herramienta 07 desde granescala_config.py.

Salidas:
  07-gran-escala/evaluacion-gran-escala.html  (asistente web)
  07-gran-escala/informe-gran-escala.md       (plantilla de informe para Word)
  07-gran-escala/solicitud-informacion.md     (lista de información a pedir al cliente)

Uso: python scripts/generar_gran_escala.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import granescala_config as C  # noqa: E402

OUT = ROOT / "07-gran-escala"
OUT.mkdir(exist_ok=True)


def tr(nombre, area, sistema, **k):
    base = {"nombre": nombre, "area": area, "sistema": sistema, "dir": [], "tit": "", "vol": "", "cnt": [], "cntOtros": "",
            "cat": [], "catRev": True, "fre": "", "per": "", "geo": "", "ev": {}}
    base.update(k)
    return base


DIR_144 = [False] * 9 + [True]  # Res. art. 14.4 biométricos
ejemplo = {
    "org": {"emp": "Ferretería Ficticia El Tornillo S.A. (EJEMPLO)", "ruc": "[RUC]", "rol": "Responsable", "sector": "Comercio",
            "fecha": "2026-11-08", "entrev": "Gerente general, contadora, jefa de talento humano, proveedor de sistemas"},
    "tr": [
        tr("Facturación y gestión de clientes", "Ventas y contabilidad", "ERP", tit="8500", vol="12", fre="1", per="2", geo="1",
           ev={"tit": "Reporte del ERP: clientes únicos por cédula o RUC, nov. 2025 a oct. 2026", "vol": "Ficha de cliente del ERP (12 campos)",
               "cat": "Revisión de la ficha: sin categorías especiales", "fre": "Cada venta", "per": "Clientes recurrentes; uso activo de 5 años en cartera y fidelización",
               "geo": "Dos sucursales: Guayaquil y Durán"}),
        tr("Gestión de nómina", "Talento humano", "Sistema de nómina y archivo físico", tit="52", vol="34", cat=[0, 8], fre="1", per="2", geo="0",
           ev={"tit": "Trabajadores activos y cesados en 12 meses", "vol": "Ficha de personal (34 campos)", "cat": "Certificados médicos y cargas familiares menores de edad",
               "fre": "Mensual", "per": "Durante la relación laboral", "geo": "Una ciudad"}),
        tr("Control de asistencia con huella", "Talento humano", "Reloj biométrico", dir=DIR_144, tit="45", vol="4", cat=[1], fre="2", per="1", geo="0",
           ev={"tit": "Trabajadores enrolados", "vol": "Huella, nombre, cédula, marcaciones", "cat": "Huella dactilar (biométrico)", "fre": "Cada marcación",
               "per": "Plantilla activa mientras dura la relación; marcaciones 2 años", "geo": "Matriz"}),
        tr("Registro de asistentes a feria comercial", "Marketing", "Formulario en papel", tit="650", vol="3", fre="0", per="0", geo="0",
           ev={"tit": "Formularios recibidos en la feria", "vol": "Nombre, teléfono, correo", "cat": "Datos básicos", "fre": "Una vez",
               "per": "Uso para una sola invitación", "geo": "Guayaquil"}),
    ],
    "sel": 0,
    "f": {"el": "Abg. Mariano X. Macías Sánchez", "ec": "Consultor en Protección de Datos Personales · Matrícula profesional 09-2022-736",
          "ap": "[REPRESENTANTE LEGAL]", "ac": "Gerente general"},
}

cfg = {"version": C.VERSION, "umbral": C.UMBRAL, "directa": C.DIRECTA, "tipos": C.TIPOS_DATOS, "categorias": C.CATEGORIAS,
       "variables": C.VARIABLES, "obligaciones": C.OBLIGACIONES, "solicitud": C.SOLICITUD, "ejemplo": ejemplo}
shell = (ROOT / "scripts" / "plantilla-gran-escala.html").read_text(encoding="utf-8")
(OUT / "evaluacion-gran-escala.html").write_text(
    shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("OK", OUT / "evaluacion-gran-escala.html")


def n(x):
    return f"{x:g}".replace(".", ",")


def opciones(v):
    if v["tipo"] == "num":
        return "; ".join(f"{t[2]} ({n(t[1])})" for t in v["tramos"])
    if v["tipo"] == "cat":
        return "Solo datos básicos (0,5); una categoría especial (2); más de una, datos penales o de grupos vulnerables (3)"
    return "; ".join(f"{o} ({n(p)})" for o, p in v["ops"])


# ---------------------------------------------------------------- informe (plantilla)
I = ["# Informe de evaluación del tratamiento a gran escala", "",
     "**[RAZÓN SOCIAL]** · RUC [RUC] · [FECHA]", "",
     "> **Nota para quien elabora (eliminar antes de entregar):** el asistente `evaluacion-gran-escala.html` calcula los puntajes y "
     "redacta este informe con los datos ingresados. Use esta plantilla si trabaja sin el asistente. Las ayudas didácticas son material propio; "
     "los puntajes y casos de calificación directa son de la Res. SPDP-SPD-2026-0005-R y del RGLOPDP.", "",
     "## 1. Alcance y metodología", "",
     "Se evaluaron [NÚMERO] tratamientos en los que la organización actúa como [responsable / encargado]. Información proporcionada por [PERSONAS ENTREVISTADAS]. "
     "Se aplicaron los casos de calificación directa del RGLOPDP (art. 4 num. 7) y de la Res. SPDP-SPD-2026-0005-R (art. 14), y el Modelo Técnico de "
     "Gran Escala (arts. 7 a 10): suma de seis variables con umbral de 6 puntos.", "",
     "## 2. Escala aplicada (art. 8)", "", "| Variable | Opciones y puntos |", "|---|---|"]
I += [f"| {v['nombre']} | {opciones(v)} |" for v in C.VARIABLES]
I += ["", "## 3. Resultado", "", "| Tratamiento | " + " | ".join(v["nombre"].split(" (")[0] for v in C.VARIABLES) + " | Total | Resultado |",
      "|---" * (len(C.VARIABLES) + 3) + "|",
      "| [TRATAMIENTO] | " + " | ".join("[ ]" for _ in C.VARIABLES) + " | [TOTAL] | [Gran escala / No es gran escala / Directa] |", "",
      "## 4. Detalle y evidencia por tratamiento", "", "### 4.1 [TRATAMIENTO]", "", "Área: [ÁREA] · Sistema: [SISTEMA]", "",
      "Calificación directa: [Ninguna / supuesto y fuente]", "",
      "| Variable | Valor declarado | Puntos | Fuente o evidencia |", "|---|---|---|---|"]
I += [f"| {v['nombre']} | [VALOR] | [ ] | [EVIDENCIA] |" for v in C.VARIABLES]
I += ["", "## 5. Conclusión", "", "[CONCLUSIÓN]", "", "Obligaciones que se activan si algún tratamiento es de gran escala:", "",
      "| Obligación | Base | Cuándo |", "|---|---|---|"]
I += [f"| {o[0]} | {o[1]} | {o[2]} |" for o in C.OBLIGACIONES]
I += ["", "## 6. Observaciones", "",
      "- El cálculo y su evidencia deben constar en el RAT y actualizarse al menos una vez al año o ante cambios sustanciales (arts. 6, 7 y 13).",
      "- La permanencia se mide como tiempo de operaciones activas, sin contar archivo o bloqueo (art. 3.9).",
      "- El art. 8.1.4 omite el rango de 100.001 a 100.999 titulares; de presentarse, se asigna al tramo superior.",
      "- Si un resultado se considera desproporcionado, el responsable puede consultar a la SPDP; su respuesta es obligatoria para el consultante (RGLOPDP art. 53).", ""]
(OUT / "informe-gran-escala.md").write_text("\n".join(I) + "\n", encoding="utf-8")
print("OK", OUT / "informe-gran-escala.md")

# ---------------------------------------------------------------- solicitud de información
Q = ["# Solicitud de información para la evaluación de tratamientos a gran escala", "",
     "**Para:** [NOMBRE Y CARGO] · **Organización:** [RAZÓN SOCIAL] · **Fecha:** [FECHA]", "",
     "Estimado(a) [NOMBRE]:", "",
     "Para determinar si los tratamientos de datos personales de [RAZÓN SOCIAL] son de gran escala según la Res. SPDP-SPD-2026-0005-R, "
     "le agradeceré remitir la siguiente información hasta el [FECHA LÍMITE]:", "",
     "| Información | Para qué | Área sugerida |", "|---|---|---|"]
Q += [f"| {a} | {b} | {c} |" for a, b, c in C.SOLICITUD]
Q += ["", "No es necesario enviar datos personales de clientes o trabajadores: bastan conteos, listas de campos y descripciones. "
      "La información se tratará con confidencialidad.", "", "Atentamente,", "", "[NOMBRE]", "", "[CARGO]", ""]
(OUT / "solicitud-informacion.md").write_text("\n".join(Q) + "\n", encoding="utf-8")
print("OK", OUT / "solicitud-informacion.md")
