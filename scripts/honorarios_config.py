"""Fuente única de la calculadora de honorarios (herramienta 02).

Todo valor monetario, porcentaje, tarifa y ponderación de este archivo es CRITERIO PROPIO de
Macías Sánchez Consultores, salvo los marcados con su norma (IVA, MTGE, clasificación de empresas,
retenciones, costo laboral). Las referencias de mercado consultadas constan en
02-honorarios/metodologia-honorarios.md.
"""

VERSION = "0.1"

# ---------------------------------------------------------------- Parámetros económicos (verificar cada año)
ECON = {
    "iva": 15,            # % tarifa general (LRTI art. 65; Circular SRI NAC-DGECCGC25-00000006)
    "sbu": 482,           # USD 2026 (Consejo Nacional de Trabajo y Salarios, 15-12-2025)
    "ret_ir_natural": 10,  # % retención IR honorarios profesionales persona natural (Res. NAC-DGERCGC26-00000009)
    "ret_ir_sociedad": 5,  # % según resúmenes de la misma resolución: verificar (punto abierto)
    "ret_iva": 100,       # % retención de IVA en honorarios profesionales de persona natural (tabla SRI vigente)
    "aporte_patronal": 12.15,  # % IESS patronal 11,15 + IECE 0,5 + SECAP 0,5
}

# ---------------------------------------------------------------- Tamaño de empresa (Reglamento COPCI art. 106; COPCI art. 53)
# Las ventas prevalecen sobre el número de trabajadores cuando no coinciden (COPCI art. 53).
TAMANOS = [
    {"id": "micro", "nombre": "Microempresa", "trab": [1, 9], "ventas": [0, 100000]},
    {"id": "peq", "nombre": "Pequeña empresa", "trab": [10, 49], "ventas": [100000.01, 1000000]},
    {"id": "med", "nombre": "Mediana empresa", "trab": [50, 199], "ventas": [1000000.01, 5000000]},
    {"id": "gra", "nombre": "Gran empresa", "trab": [200, None], "ventas": [5000000.01, None]},
]

# Factor de complejidad sectorial (criterio propio): sectores con categorías especiales o regulación sectorial.
SECTORES = [
    ("Comercio", 1.0), ("Servicios profesionales", 1.0), ("Manufactura o industria", 1.0), ("Construcción e inmobiliario", 1.0),
    ("Logística, transporte o courier", 1.15), ("Turismo, hotelería o restaurantes", 1.05), ("Tecnología o comercio electrónico", 1.2),
    ("Seguridad privada o vigilancia", 1.2), ("Educación (niñas, niños y adolescentes)", 1.25), ("Salud", 1.3),
    ("Financiero, seguros o crédito", 1.3), ("Organización sin fines de lucro", 0.9), ("Otro", 1.0),
]

# ---------------------------------------------------------------- Método 1: volumen de negocio
# Tramos marginales sobre el volumen de negocio anual (como una tabla progresiva): honorario ANUAL de control.
VOLNEG = {
    "tramos": [[0, 100000, 0.90], [100000, 1000000, 0.25], [1000000, 5000000, 0.08], [5000000, 20000000, 0.03], [20000000, None, 0.01]],
    "piso_mensual": {"micro": 120, "peq": 200, "med": 350, "gra": 700},
    "diag_factor": 0.35,   # diagnóstico = 35 % del honorario anual de control
    "diag_piso": {"micro": 350, "peq": 600, "med": 1100, "gra": 2200},
    "adec_factor": 0.90,   # adecuación = 90 % del honorario anual de control
    "adec_piso": {"micro": 900, "peq": 1800, "med": 3500, "gra": 7000},
}

# ---------------------------------------------------------------- Método 2: volumen de tratamiento (MTGE, Res. SPDP-SPD-2026-0005-R art. 8)
MTGE = {
    "variables": [
        {"id": "tit", "nombre": "Número de titulares (12 meses, tratamiento)", "ops": [["0 a 1.000", 1], ["1.001 a 10.000", 2], ["10.001 a 100.000", 3], ["Más de 100.000", 4]]},
        {"id": "vol", "nombre": "Volumen: tipos de datos por titular", "ops": [["Hasta 10", 0.5], ["11 a 30", 1], ["31 a 100", 2], ["101 o más", 3]]},
        {"id": "cat", "nombre": "Categorías de datos", "ops": [["Solo datos básicos", 0.5], ["Incluye una categoría especial", 2], ["Más de una categoría especial, grupos vulnerables o datos penales", 3]]},
        {"id": "fre", "nombre": "Frecuencia", "ops": [["Puntual", 0.5], ["Periódica o recurrente", 1], ["Continua o en tiempo real", 2]]},
        {"id": "per", "nombre": "Permanencia", "ops": [["Ocasional", 0.5], ["Temporal (menos de 3 años)", 1], ["Prolongada (3 años o más)", 2]]},
        {"id": "geo", "nombre": "Alcance geográfico", "ops": [["Local", 1], ["Nacional", 2], ["Global o transfronterizo", 3]]},
    ],
    "umbral": 6,
    "directa": [
        "Datos de salud (sistemas de salud, seguridad social, historias clínicas) u otras categorías especiales",
        "Evaluación sistemática automatizada de aspectos personales (perfiles, predicción) con efectos jurídicos",
        "Observación sistemática de personas en espacios públicos (videovigilancia u otro monitoreo continuo)",
        "Datos biométricos o geolocalización de titulares",
        "Sistemas de información crediticia, financiera o de riesgo económico",
        "Datos de niñas, niños y adolescentes en entornos dirigidos a ellos",
        "Transferencias sistemáticas que constituyen flujos continuos o estructurales",
        "Servicios de mensajería, correo expreso o courier",
    ],
}
# Tarifario por volumen (criterio propio)
VOLTRAT = {
    "base_mensual": [[0, 4, 120], [4, 6, 220], [6, 99, 420]],  # por puntaje MTGE del tratamiento principal
    "act_incluidas": 5, "por_actividad": 12, "por_encargado": 8, "transferencias": 40, "por_solicitud": 20, "por_sede": 30,
    "diag": {"base": 250, "por_actividad": 45, "por_encargado": 15, "gran_escala": 300, "por_sede": 100},
    "adec": {"base": 600, "por_actividad": 120, "por_encargado": 40, "por_eipd": 450},
}

# ---------------------------------------------------------------- Método 3: estimación técnica (horas × tarifa)
PERFILES = [
    ["Consultor en formación (sin registro como DPD)", 25],
    ["Consultor con programa profesionalizante", 35],
    ["Especialista con experiencia acreditada", 50],
    ["Especialista con certificación ISO/IEC 27701", 70],
]
GASTOS_PCT = 15  # gastos indirectos y reserva (criterio propio)
# Fórmulas de horas: base + coeficientes sobre las variables del cliente (a=áreas, act, enc, sol, tr=transferencias 0/1, ge=gran escala 0/1, eipd, cap=horas de capacitación anuales)
TAREAS = {
    "diag": [
        ["Reunión de inicio y plan de trabajo", {"base": 2}],
        ["Entrevistas por área", {"a": 1.25}],
        ["Revisión documental", {"base": 2, "act": 0.5}],
        ["Diagnóstico de madurez y exposición económica", {"base": 3}],
        ["Levantamiento preliminar de actividades", {"act": 0.75}],
        ["Encargados y transferencias", {"enc": 0.3, "tr": 1}],
        ["Informe y presentación a la gerencia", {"base": 4}],
    ],
    "adec": [
        ["Registro de actividades (RAT) completo", {"base": 2, "act": 2}],
        ["Política de privacidad y avisos", {"base": 6, "a": 0.5}],
        ["Contratos de encargo y cláusulas", {"base": 1, "enc": 1}],
        ["Evaluaciones de impacto", {"eipd": 8}],
        ["Protocolo de vulneraciones y procedimiento de derechos", {"base": 6}],
        ["Capacitación inicial", {"base": 3}],
        ["Designación del DPD y registro ante la SPDP", {"base": 2}],
    ],
    "mens": [
        ["Revisión y actualización del RAT", {"base": 1, "act": 0.15}],
        ["Supervisión de encargados", {"enc": 0.1}],
        ["Atención de solicitudes de derechos", {"sol": 0.75}],
        ["Gestión de incidentes (promedio mensual)", {"base": 0.5}],
        ["Capacitación (prorrateo anual)", {"cap": 1 / 12}],
        ["Reporte y reunión con la gerencia", {"base": 1.5}],
        ["Vigilancia normativa y asesoría a proyectos", {"base": 1, "ge": 2}],
        ["Comunicación con la SPDP", {"base": 0.5}],
    ],
}
AREAS_POR_TAMANO = {"micro": 3, "peq": 5, "med": 8, "gra": 12}

# ---------------------------------------------------------------- Comparación y otras modalidades
DPD_INTERNO = {"salario": 1800}  # referencia: avisos de empleo en Quito, USD 1.500 a 2.500 mensuales
# Los paquetes solo contienen la línea de evaluación y supervisión. La implementación se agrega aparte, según quién la
# ejecute (pestaña 6): así un paquete nunca mezcla el servicio del DPO con la implementación que supervisa.
PAQUETES = [
    {"id": "esencial", "nombre": "Esencial", "para": "Microempresa o riesgo bajo",
     "items": ["diag", "acomp", "verificacion"]},
    {"id": "cumplimiento", "nombre": "Cumplimiento", "para": "Pequeña y mediana empresa",
     "items": ["diag", "dpd", "verificacion", "capac"]},
    {"id": "integral", "nombre": "Integral", "para": "Gran escala, sectores regulados o gran empresa",
     "items": ["diag", "mtge", "dpd", "revision", "verificacion", "capac", "informeanual"]},
]

# ---------------------------------------------------------------- Servicios de la proforma
# Fuente única: scripts/catalogo_config.py (herramienta 01). Formato que usa la proforma:
import catalogo_config as _CAT  # noqa: E402
# [grupo, id, nombre, descripción, unidad, precio, beneficio, código, línea ("eval" o "impl")]
SERVICIOS = [[x["fase"], x["id"], x["nombre"], x["que"], x["unidad"], x["precio"], x["beneficio"], x["cod"], x["linea"]]
             for x in _CAT.SERVICIOS if x["proforma"]]
GRUPOS = [f[0] for f in _CAT.FASES]
LINEAS = _CAT.LINEAS
ROLES_MSC = _CAT.ROLES_MSC
IMPLEMENTACION = _CAT.IMPLEMENTACION

CONDICIONES = (
    "Los valores están expresados en dólares de los Estados Unidos de América. "
    "Forma de pago: servicios de evaluación e implementación facturados por MSC, 50 % de anticipo y 50 % contra entrega; servicio mensual, por mes adelantado dentro de los cinco primeros días. "
    "La implementación que ejecute el personal del responsable, un proveedor de su elección o un implementador con contrato directo no forma parte de esta proforma. "
    "Plazo mínimo del servicio mensual: seis meses. "
    "Antes del inicio se suscribirán el contrato de prestación de servicios, el acuerdo de confidencialidad y el contrato de encargo del tratamiento (art. 41 RGLOPDP). "
    "No incluye pruebas técnicas de seguridad informática, tasas ni gastos de movilización fuera de la ciudad, salvo que se indique."
)

BENEFICIOS = [
    "Metodología propia basada en la LOPDP, su Reglamento y las resoluciones de la SPDP, con herramientas de diagnóstico, registro y evaluación.",
    "Cada entregable deja evidencia documental para demostrar el cumplimiento ante la Superintendencia (responsabilidad proactiva, art. 10 lit. k LOPDP).",
    "Independencia profesional: la evaluación y la supervisión están separadas de la implementación. Quien implementa lo decide su organización; el DPO revisa, emite observaciones no vinculantes y verifica, sin ejecutar lo que supervisa.",
    "Confidencialidad y contrato de encargo firmados antes de acceder a cualquier dato personal.",
    "Acompañamiento en los plazos legales ante una vulneración de la seguridad.",
]
