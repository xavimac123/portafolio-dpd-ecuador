"""Fuente única de la calculadora de honorarios (herramienta 01).

Todo valor monetario, porcentaje, tarifa y ponderación de este archivo es CRITERIO PROPIO de
Macías Sánchez Consultores, salvo los marcados con su norma (IVA, MTGE, clasificación de empresas,
retenciones, costo laboral). Las referencias de mercado consultadas constan en
01-honorarios/metodologia-honorarios.md.
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
PAQUETES = [
    {"id": "esencial", "nombre": "Esencial", "para": "Microempresa o riesgo bajo",
     "items": ["diag", "politica", "contratos", "acomp"]},
    {"id": "cumplimiento", "nombre": "Cumplimiento", "para": "Pequeña y mediana empresa",
     "items": ["diag", "adec", "dpd", "capac"]},
    {"id": "integral", "nombre": "Integral", "para": "Gran escala, sectores regulados o gran empresa",
     "items": ["diag", "adec", "eipd", "dpd", "capac", "informe"]},
]

# ---------------------------------------------------------------- Catálogo de servicios de la proforma (USD por tamaño: micro, pequeña, mediana, grande)
# "auto" toma el valor del método elegido en la pestaña Comparar.
SERVICIOS = [
    # grupo, id, nombre, descripción, unidad, precios | "auto:clave", beneficio para el cliente
    ["Evaluación inicial", "diag", "Diagnóstico de madurez y exposición económica",
     "Entrevistas, revisión documental, índice de madurez en 12 dominios, estimación de multa (Res. SPDP-SPD-2025-0022-R), apetito al riesgo y plan de acción priorizado.",
     "servicio", "auto:diag", "Saber exactamente dónde está su empresa, cuánto arriesga y qué hacer primero."],
    ["Evaluación inicial", "mtge", "Análisis de gran escala y obligación de designar DPD",
     "Aplicación del Modelo Técnico de Gran Escala (Res. SPDP-SPD-2026-0005-R) y de las causales de la Res. SPDP-SPD-2025-0028-R.",
     "servicio", [120, 180, 250, 350], "Certeza sobre si su empresa debe designar DPD y realizar evaluaciones de impacto."],
    ["Evaluación inicial", "informe", "Informe ejecutivo y presentación a la gerencia",
     "Informe de evaluación general con matriz de soportes y reunión de decisiones con la gerencia.",
     "servicio", [150, 250, 400, 600], "Decisiones claras de la dirección, con respaldo documental."],
    ["Adecuación", "adec", "Programa de adecuación integral",
     "RAT completo, política y avisos, contratos de encargo, protocolo de vulneraciones, procedimiento de derechos, capacitación inicial y designación del DPD.",
     "programa", "auto:adec", "Cumplimiento documentado de las obligaciones de la LOPDP en un solo programa."],
    ["Adecuación", "rat", "Registro de actividades de tratamiento (RAT)",
     "Inventario de actividades con el contenido mínimo del art. 38 RGLOPDP, estados y fechas de revisión.",
     "servicio", [350, 700, 1400, 2800], "El inventario oficial que pedirá la Superintendencia."],
    ["Adecuación", "eipd", "Evaluación de impacto (por tratamiento)",
     "Necesidad y proporcionalidad, matriz de riesgos, medidas e informe con el contenido del art. 32 RGLOPDP.",
     "tratamiento", [450, 600, 900, 1500], "Lanzar tratamientos de alto riesgo con respaldo técnico y legal."],
    ["Adecuación", "politica", "Política de privacidad y avisos",
     "Política construida desde el RAT y avisos para cada punto de recolección (formularios, cámaras, correo).",
     "paquete", [250, 400, 600, 900], "Clientes y trabajadores informados conforme al art. 12 LOPDP."],
    ["Adecuación", "contratos", "Contratos de encargo y cláusulas",
     "Contratos con encargados (art. 41 RGLOPDP) y cláusulas de consentimiento; paquete de hasta cinco.",
     "paquete", [200, 350, 500, 800], "Proveedores obligados por contrato: evita una infracción grave."],
    ["Adecuación", "vulner", "Protocolo de vulneraciones y bitácora",
     "Protocolo aprobado, roles, bitácora y modelos de notificación a la SPDP, ARCOTEL, CSIRT y titulares.",
     "paquete", [200, 350, 550, 850], "Responder a un incidente en los plazos legales, sin improvisar."],
    ["Adecuación", "derechos", "Procedimiento de atención de derechos",
     "Canal, formularios, plazos y registro de solicitudes de los titulares.",
     "paquete", [150, 250, 400, 600], "Atender reclamos a tiempo y reducir denuncias ante la SPDP."],
    ["Adecuación", "capac", "Capacitación al personal (taller de 2 horas)",
     "Taller práctico con evaluación y registro de asistencia como evidencia.",
     "taller", [200, 300, 450, 700], "Personal que sabe proteger datos: la primera barrera contra incidentes."],
    ["Control mensual", "dpd", "Delegado de Protección de Datos externo",
     "Funciones del DPD, registro ante la SPDP, supervisión del cumplimiento, atención de derechos y vulneraciones, reporte mensual.",
     "mes", "auto:mens", "Un especialista independiente que responde por el cumplimiento cada mes."],
    ["Control mensual", "acomp", "Acompañamiento de cumplimiento (sin designación)",
     "Revisión del RAT, asesoría en proyectos nuevos y soporte al responsable interno.",
     "mes", "auto:acomp", "Soporte experto continuo a un costo menor."],
    ["Por evento", "incidente", "Gestión de una vulneración de la seguridad",
     "Evaluación, contención documental y notificaciones en plazo (por incidente).",
     "incidente", [250, 400, 600, 900], "Acompañamiento inmediato cuando más se necesita."],
    ["Por evento", "solicitud", "Atención de solicitud de derechos adicional",
     "Respuesta a una solicitud fuera del volumen incluido en el plan mensual.",
     "solicitud", [25, 35, 50, 70], "Respuesta en plazo a cada titular."],
    ["Por evento", "hora", "Hora adicional de asesoría",
     "Asesoría puntual fuera del alcance contratado, a la tarifa por hora.",
     "hora", "auto:hora", "Flexibilidad para consultas puntuales."],
]

CONDICIONES = (
    "Los valores están expresados en dólares de los Estados Unidos de América. "
    "Forma de pago: servicios de evaluación y adecuación, 50 % de anticipo y 50 % contra entrega; servicio mensual, por mes adelantado dentro de los cinco primeros días. "
    "Plazo mínimo del servicio mensual: seis meses. "
    "Antes del inicio se suscribirán el contrato de prestación de servicios, el acuerdo de confidencialidad y el contrato de encargo del tratamiento (art. 41 RGLOPDP). "
    "No incluye pruebas técnicas de seguridad informática, tasas ni gastos de movilización fuera de la ciudad, salvo que se indique."
)

BENEFICIOS = [
    "Metodología propia basada en la LOPDP, su Reglamento y las resoluciones de la SPDP, con herramientas de diagnóstico, registro y evaluación.",
    "Cada entregable deja evidencia documental para demostrar el cumplimiento ante la Superintendencia (responsabilidad proactiva, art. 10 lit. k LOPDP).",
    "Independencia profesional: el consultor asesora y supervisa; no decide sobre las finalidades ni administra los sistemas que supervisa.",
    "Confidencialidad y contrato de encargo firmados antes de acceder a cualquier dato personal.",
    "Acompañamiento en los plazos legales ante una vulneración de la seguridad.",
]
