"""Construye 07-evaluacion-impacto/asistente-eipd.html desde eipd_config.py.

Uso: python scripts/generar_asistente_eipd.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import eipd_config as C  # noqa: E402

EJEMPLO = {
    "nec": {"n_perfiles": "No", "n_especiales": "No", "n_observacion": "No", "n_autoridad": "No",
            "n_biometricos": "Sí", "n_ia": "No", "n_nna_il": "No", "n_nueva_tec": "Sí", "n_combinacion": "No",
            "n_vulnerables": "Sí", "n_impide": "No"},
    "d": {"d_resp": "Ferretería Ficticia El Tornillo S.A. (EJEMPLO)", "d_trat": "Control de asistencia con lector de huella",
          "d_rat": "T-07", "d_inicio": "2027-01-15",
          "d_fin": "Registrar la hora de entrada y salida del personal para calcular la jornada, las horas extraordinarias y los atrasos.",
          "ops": ["Recolección", "Registro", "Almacenamiento", "Consulta y uso", "Conservación", "Supresión o anonimización"],
          "d_datos": "Plantilla biométrica de la huella dactilar; nombres, cédula, área y cargo; registros de marcación.",
          "d_tit": "Trabajadores en relación de dependencia (120).",
          "d_sist": "Lector de huella en la entrada; software de asistencia en servidor local; reporte mensual exportado a Excel para nómina.",
          "d_terc": "Proveedor del software (soporte remoto) como encargado. Sin transferencias internacionales.",
          "d_part": "Gerencia de Talento Humano, jefe de TI, asesor externo en protección de datos.", "ops_": []},
    "prop": {
        "p_base": {"r": "Parcial", "j": "Obligación legal de llevar el control de la jornada; falta analizar si exige un medio biométrico."},
        "p_finalidad": {"r": "Cumple", "j": "Control de jornada y horas extraordinarias."},
        "p_necesario": {"r": "Parcial", "j": "Existen alternativas menos invasivas (tarjeta de proximidad, registro en aplicación). Justificar por qué no bastan."},
        "p_minimizacion": {"r": "Cumple", "j": "El lector guarda la plantilla, no la imagen de la huella."},
        "p_conservacion": {"r": "No cumple", "j": "No hay plazo definido para borrar la plantilla al terminar la relación laboral."},
        "p_calidad": {"r": "Cumple", "j": ""},
        "p_info": {"r": "No cumple", "j": "No existe aviso de privacidad para el personal."},
        "p_derechos": {"r": "Parcial", "j": "Las solicitudes se atienden en Talento Humano sin procedimiento escrito."},
        "p_encargados": {"r": "No cumple", "j": "El proveedor del software no tiene contrato de encargo."},
        "p_transf": {"r": "No aplica", "j": ""},
    },
    "riesgos": [
        {"dim": "Confidencialidad", "esc": "Acceso no autorizado a los datos por un tercero externo (ataque informático)",
         "ame": "Ciberdelincuentes", "vul": "Técnica", "vulD": "Servidor local sin cifrado ni actualizaciones",
         "imp": ["Suplantación de identidad o fraude", "Pérdida de control sobre sus datos"], "i0": 5, "p0": 2,
         "ctl": ["Cifrado en reposo y en tránsito", "Control de acceso por perfil y mínimo privilegio", "Pruebas de seguridad (vulnerabilidades, penetración)"],
         "i1": 5, "p1": 1, "dec": "Modificar (mitigar)", "own": "Jefe de TI", "plazo": "2026-12-15"},
        {"dim": "Confidencialidad", "esc": "Divulgación por un encargado o proveedor",
         "ame": "Encargado o proveedor", "vul": "Jurídica", "vulD": "Sin contrato de encargo con el proveedor del software",
         "imp": ["Pérdida de control sobre sus datos"], "i0": 4, "p0": 3,
         "ctl": ["Contrato de encargo y auditoría al proveedor"], "i1": 4, "p1": 1, "dec": "Modificar (mitigar)",
         "own": "Asesor legal", "plazo": "2026-12-01"},
        {"dim": "Derechos y licitud", "esc": "Conservación de los datos más allá del plazo necesario",
         "ame": "El propio responsable (uso indebido)", "vul": "Organizacional", "vulD": "Sin procedimiento de baja",
         "imp": ["Pérdida de control sobre sus datos"], "i0": 3, "p0": 4,
         "ctl": ["Plazo de conservación con borrado automático"], "i1": 3, "p1": 1, "dec": "Modificar (mitigar)",
         "own": "Talento Humano", "plazo": "2026-12-01"},
        {"dim": "Derechos y licitud", "esc": "Vigilancia excesiva o intrusión en la intimidad",
         "ame": "El propio responsable (uso indebido)", "vul": "De grupos especialmente vulnerables",
         "vulD": "Relación de subordinación laboral",
         "imp": ["Angustia o temor"], "i0": 3, "p0": 3,
         "ctl": ["Aviso de privacidad específico y canal de derechos", "Minimización de datos recogidos"],
         "i1": 2, "p1": 2, "dec": "Modificar (mitigar)", "own": "Talento Humano", "plazo": "2026-12-01"},
    ],
    "ctx": {"f": {"fa": 1, "fb": 1, "fc": 1, "fd": 2, "fe": 0},
            "der": ["Protección de datos personales (autodeterminación informativa)", "Intimidad personal y familiar", "Trabajo"],
            "per": "Un año", "met": C.METODOS[0], "cap": "5000",
            "rat": "Valores estimados por el jefe de TI y el asesor externo con base en los incidentes del sector y en los controles actuales del servidor. Sin incidentes propios registrados en los últimos tres años."},
    "c": {"c_umbral": 9, "c_dict": C.DICTAMEN[1],
          "c_obs": "Ejemplo ficticio. Antes de usar el lector, ofrecer una alternativa no biométrica a quien lo solicite y verificar la norma general de datos biométricos de la SPDP.",
          "c_rev": "2027-12-01", "c_ver": "1.0"},
    "f": {"f_el": "Abg. Mariano X. Macías Sánchez", "f_ec": "Consultor en Protección de Datos · Mat. 09-2022-736",
          "f_ap": "[REPRESENTANTE LEGAL]", "f_ac": "Gerente General", "f_fe": ""},
}

_DER = [["Protección de datos personales (autodeterminación informativa)", "Propiedad y patrimonio"],
        ["Protección de datos personales (autodeterminación informativa)"],
        ["Protección de datos personales (autodeterminación informativa)"],
        ["Intimidad personal y familiar", "Trabajo"]]
_RAT = ["Impacto 5: la plantilla biométrica no se puede cambiar como una contraseña (exposición irreversible). Probabilidad 2: servidor sin cifrado, pero sin acceso desde internet.",
        "Sin contrato no hay obligación de confidencialidad ni de devolución; el proveedor tiene acceso remoto permanente.",
        "Hoy se conservan plantillas de personas que ya no trabajan en la empresa.",
        "La subordinación limita la capacidad del trabajador de oponerse; impacto secundario posible en la relación laboral."]
for _i, _r in enumerate(EJEMPLO["riesgos"]):
    _r["der"], _r["rat"] = _DER[_i], _RAT[_i]

for q in C.NECESIDAD:
    q["fuente"] = re.split(r":| \(|\. Ver|;", q["norma"])[0].strip()

cfg = {
    "necesidad": C.NECESIDAD, "grupos": C.GRUPOS_NECESIDAD, "prop": C.PROPORCIONALIDAD, "respProp": C.RESP_PROP,
    "impacto": C.IMPACTO, "probabilidad": C.PROBABILIDAD, "niveles": C.NIVELES, "umbral": C.UMBRAL_ACEPTABLE,
    "dimensiones": C.DIMENSIONES, "escenarios": C.ESCENARIOS, "amenazas": C.AMENAZAS,
    "vulnerabilidades": C.VULNERABILIDADES, "impactosTitular": C.IMPACTOS_TITULAR, "controles": C.CONTROLES,
    "decisiones": C.DECISIONES, "factores": C.FACTORES_IMPACTO, "derechos": C.DERECHOS,
    "periodos": C.PERIODOS, "metodos": C.METODOS, "pasos": C.PASOS_IMPACTO, "operaciones": C.OPERACIONES, "dictamen": C.DICTAMEN, "ejemplo": EJEMPLO,
}
shell = (ROOT / "scripts" / "plantilla-asistente-eipd.html").read_text(encoding="utf-8")
out = ROOT / "07-evaluacion-impacto" / "asistente-eipd.html"
out.parent.mkdir(exist_ok=True)
out.write_text(shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("OK", out)
