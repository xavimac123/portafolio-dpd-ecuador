"""Fuente única de la Herramienta 06: Evaluación de impacto del tratamiento de datos personales.

Base: LOPDP arts. 40 y 42; RGLOPDP arts. 29 a 32; Res. SPDP-SPD-2025-0003-R (Guía de Gestión de
Riesgos y Evaluación de Impacto, Cap. I obligatorio, Cap. II referencial).

Las escalas de impacto y probabilidad son PROPIAS del portafolio: la guía de la SPDP deja las escalas
en el Cap. II, que es referencial, y permite agregar criterios. Ajustables aquí.
"""

# ---------- 1. ¿Es obligatoria?
NECESIDAD = [
    {"id": "n_perfiles", "grupo": "ley", "oblig": True,
     "texto": "¿Se evalúan de forma sistemática y exhaustiva aspectos personales mediante tratamiento automatizado (incluida la elaboración de perfiles), y con base en ello se toman decisiones con efectos jurídicos para las personas?",
     "concepto": "Ejemplos: scoring crediticio que aprueba o niega un crédito, filtros automáticos que descartan postulantes, sistemas que fijan primas de seguro según el perfil.",
     "norma": "Art. 42 lit. a LOPDP: evaluación sistemática y exhaustiva de aspectos personales basada en tratamiento automatizado, como la elaboración de perfiles, sobre cuya base se tomen decisiones con efectos jurídicos."},
    {"id": "n_especiales", "grupo": "ley", "oblig": True,
     "texto": "¿Se tratan a gran escala categorías especiales de datos o datos relativos a condenas e infracciones penales?",
     "concepto": "Categorías especiales: datos sensibles, de niñas, niños y adolescentes, de salud y de personas con discapacidad (art. 25 LOPDP). Gran escala se valora por número de titulares, volumen, duración y alcance geográfico. Ejemplos: clínica u hospital, colegio, aseguradora de salud, empresa que verifica récords policiales de miles de postulantes.",
     "norma": "Art. 42 lit. b LOPDP: tratamiento a gran escala de las categorías especiales de datos, o de los datos personales relativos a condenas e infracciones penales."},
    {"id": "n_observacion", "grupo": "ley", "oblig": True,
     "texto": "¿Se observa de forma sistemática y a gran escala una zona de acceso público?",
     "concepto": "Ejemplos: cámaras de un centro comercial, de un terminal o de una urbanización que captan áreas abiertas al público; lectura de placas en vías.",
     "norma": "Art. 42 lit. c LOPDP: observación sistemática a gran escala de una zona de acceso público."},
    {"id": "n_autoridad", "grupo": "ley", "oblig": True,
     "texto": "¿La SPDP ha requerido realizar la evaluación de impacto?",
     "concepto": "La Superintendencia puede exigirla aunque no concurra ninguno de los tres supuestos.",
     "norma": "Art. 42 LOPDP: se realiza también cuando la Autoridad de Protección de Datos Personales lo requiera."},
    {"id": "n_biometricos", "grupo": "norma", "oblig": False,
     "texto": "¿Se tratan datos biométricos (huella, rostro, voz) para identificar a las personas?",
     "concepto": "La norma general de datos biométricos remite a la guía de riesgos y evaluación de impacto para fijar las medidas reforzadas. Con datos de niñas, niños y adolescentes, la evaluación de impacto es condición expresa.",
     "norma": "Res. SPDP-SPD-2026-0039-R (norma general de datos biométricos). Ver BASE-LEGAL.md."},
    {"id": "n_ia", "grupo": "norma", "oblig": False,
     "texto": "¿Se usan sistemas de inteligencia artificial que traten datos personales?",
     "concepto": "La SPDP emitió una norma general sobre protección de datos en sistemas de inteligencia artificial, reformada en 2026.",
     "norma": "Res. SPDP-SPD-2026-0009-R, reformada por Res. SPDP-SPD-2026-0037-R. Ver BASE-LEGAL.md."},
    {"id": "n_nna_il", "grupo": "norma", "oblig": False,
     "texto": "¿Se tratan datos de niñas, niños o adolescentes con base en el interés legítimo?",
     "concepto": "Solo se admite con justificación expresa vinculada al interés superior del niño, respaldada en la evaluación de ponderación o de impacto, con medidas reforzadas.",
     "norma": "Res. SPDP-SPD-2025-0041-R (interés legítimo)."},
    {"id": "n_nueva_tec", "grupo": "riesgo", "oblig": False,
     "texto": "¿Se trata de una tecnología nueva o de un uso innovador de datos en la organización?",
     "concepto": "Indicador de alto riesgo por su naturaleza o contexto: los riesgos aún no son conocidos ni controlados.",
     "norma": "Art. 42 LOPDP: alto riesgo por la naturaleza, contexto o fines del tratamiento."},
    {"id": "n_combinacion", "grupo": "riesgo", "oblig": False,
     "texto": "¿Se combinan o cruzan bases de datos de distintos orígenes o finalidades?",
     "concepto": "El cruce de bases revela información que el titular no esperaba que se conociera.",
     "norma": "Art. 42 LOPDP: alto riesgo por la naturaleza, contexto o fines del tratamiento."},
    {"id": "n_vulnerables", "grupo": "riesgo", "oblig": False,
     "texto": "¿Los titulares pertenecen a grupos vulnerables (niñas, niños y adolescentes, personas con discapacidad, adultos mayores, pacientes, trabajadores frente al empleador)?",
     "concepto": "La guía de la SPDP considera la vulnerabilidad de grupos especiales como criterio de evaluación.",
     "norma": "Art. 40 LOPDP (particularidades de las partes involucradas); Guía Res. SPDP-SPD-2025-0003-R, Cap. II, 1.1."},
    {"id": "n_impide", "grupo": "riesgo", "oblig": False,
     "texto": "¿El tratamiento puede impedir a las personas ejercer un derecho o acceder a un servicio o contrato?",
     "concepto": "Ejemplos: listas de morosos, verificación de antecedentes que condiciona una contratación.",
     "norma": "Art. 42 LOPDP: alto riesgo para los derechos y libertades del titular."},
]
GRUPOS_NECESIDAD = {
    "ley": "Supuestos de obligatoriedad (art. 42 LOPDP)",
    "norma": "Normativa especial de la SPDP que exige o remite a la evaluación de impacto",
    "riesgo": "Indicadores de alto riesgo (art. 42 LOPDP: naturaleza, contexto o fines)",
}

# ---------- 2. Necesidad y proporcionalidad (art. 32 num. 2 RGLOPDP)
PROPORCIONALIDAD = [
    {"id": "p_base", "texto": "La base legitimadora está identificada y documentada (art. 7 LOPDP).",
     "ayuda": "Si es interés legítimo, adjunta la evaluación de ponderación (Res. SPDP-SPD-2025-0041-R)."},
    {"id": "p_finalidad", "texto": "La finalidad es determinada, explícita y legítima.",
     "ayuda": "Evita finalidades genéricas como 'gestión comercial'."},
    {"id": "p_necesario", "texto": "El tratamiento es necesario para la finalidad: no existe una alternativa menos invasiva que logre lo mismo.",
     "ayuda": "Describe las alternativas consideradas y por qué se descartaron."},
    {"id": "p_minimizacion", "texto": "Solo se recogen los datos estrictamente necesarios (minimización).",
     "ayuda": "Revisa campo por campo del formulario o sistema."},
    {"id": "p_conservacion", "texto": "El plazo de conservación está definido y justificado.", "ayuda": ""},
    {"id": "p_calidad", "texto": "Existen mecanismos para mantener los datos exactos y actualizados.", "ayuda": ""},
    {"id": "p_info", "texto": "Los titulares son informados conforme al art. 12 LOPDP.", "ayuda": ""},
    {"id": "p_derechos", "texto": "Existe un procedimiento para que los titulares ejerzan sus derechos.", "ayuda": ""},
    {"id": "p_encargados", "texto": "Los encargados tienen contrato con el contenido del art. 41 RGLOPDP.", "ayuda": ""},
    {"id": "p_transf", "texto": "Las transferencias internacionales tienen garantía y están documentadas.", "ayuda": "Marca 'No aplica' si no hay transferencias."},
]
RESP_PROP = ["Cumple", "Parcial", "No cumple", "No aplica"]

# ---------- 3. Escalas (propias, compatibles con la guía)
IMPACTO = [
    (1, "Muy bajo", "Molestias menores que el titular supera sin dificultad."),
    (2, "Bajo", "Inconvenientes superables con poco esfuerzo (repetir un trámite, cambiar una contraseña)."),
    (3, "Medio", "Consecuencias significativas pero superables: pérdidas económicas menores, estrés, publicidad no deseada."),
    (4, "Alto", "Consecuencias graves y difíciles de revertir: fraude, discriminación, pérdida de empleo, daño a la reputación."),
    (5, "Muy alto", "Consecuencias irreversibles o que afectan la integridad física, la libertad o a grupos vulnerables. La guía de la SPDP pone como ejemplo de criterio que una vulneración que afecte a más de mil personas sea siempre de riesgo muy alto."),
]
PROBABILIDAD = [
    (1, "Muy baja", "Menos de 5 % en un año. No hay antecedentes y existen controles sólidos."),
    (2, "Baja", "5 % a 20 % en un año."),
    (3, "Media", "20 % a 50 % en un año. Ha ocurrido en el sector."),
    (4, "Alta", "50 % a 80 % en un año. Ha ocurrido en la organización."),
    (5, "Muy alta", "Más de 80 % en un año. Ocurre de forma recurrente o los controles no existen."),
]
# nivel = impacto x probabilidad
NIVELES = [(1, 4, "Bajo"), (5, 9, "Medio"), (10, 16, "Alto"), (17, 25, "Muy alto")]
UMBRAL_ACEPTABLE = 9  # riesgo residual aceptable hasta este valor (apetito de riesgo por defecto, editable)

# ---------- 4. Catálogos para identificar riesgos (Guía SPDP, Cap. II, 2)
DIMENSIONES = ["Confidencialidad", "Integridad", "Disponibilidad", "Derechos y licitud"]
ESCENARIOS = [
    ("Confidencialidad", "Acceso no autorizado a los datos por un tercero externo (ataque informático)"),
    ("Confidencialidad", "Acceso o uso indebido por personal interno"),
    ("Confidencialidad", "Envío de datos a un destinatario equivocado"),
    ("Confidencialidad", "Pérdida o robo de dispositivos o documentos físicos"),
    ("Confidencialidad", "Divulgación por un encargado o proveedor"),
    ("Integridad", "Alteración o corrupción de los datos por error o ataque"),
    ("Integridad", "Datos inexactos que llevan a decisiones erróneas sobre el titular"),
    ("Disponibilidad", "Secuestro de datos (ransomware) o pérdida sin respaldo"),
    ("Disponibilidad", "Indisponibilidad prolongada del sistema que impide atender al titular"),
    ("Derechos y licitud", "Uso de los datos para una finalidad distinta a la informada"),
    ("Derechos y licitud", "Conservación de los datos más allá del plazo necesario"),
    ("Derechos y licitud", "Decisión automatizada injusta o discriminatoria"),
    ("Derechos y licitud", "Imposibilidad del titular de ejercer sus derechos"),
    ("Derechos y licitud", "Vigilancia excesiva o intrusión en la intimidad"),
    ("Derechos y licitud", "Transferencia internacional sin garantías adecuadas"),
]
AMENAZAS = [
    "Ciberdelincuentes", "Personal interno sin privilegios", "Personal interno con privilegios",
    "Encargado o proveedor", "Error humano", "El propio responsable (uso indebido)", "Hacktivistas",
    "Amenaza natural (incendio, inundación, terremoto)", "Falla técnica o eléctrica",
]
VULNERABILIDADES = ["Jurídica", "De grupos especialmente vulnerables", "Organizacional", "Técnica"]
IMPACTOS_TITULAR = [
    "Suplantación de identidad o fraude", "Pérdida económica", "Discriminación", "Daño a la reputación",
    "Pérdida de empleo u oportunidades", "Afectación a la salud o integridad", "Pérdida de control sobre sus datos",
    "Angustia o temor", "Exclusión de un servicio",
]
CONTROLES = [
    "Control de acceso por perfil y mínimo privilegio", "Autenticación de dos factores", "Cifrado en reposo y en tránsito",
    "Respaldos periódicos probados", "Registro y revisión de accesos (bitácora)", "Seudonimización o anonimización",
    "Minimización de datos recogidos", "Plazo de conservación con borrado automático", "Contrato de encargo y auditoría al proveedor",
    "Acuerdos de confidencialidad y capacitación al personal", "Intervención humana en decisiones automatizadas",
    "Aviso de privacidad específico y canal de derechos", "Pruebas de seguridad (vulnerabilidades, penetración)",
    "Plan de respuesta a vulneraciones", "Señalética y limitación del ángulo de cámaras",
]
DECISIONES = ["Mitigar", "Aceptar", "Evitar", "Transferir"]

OPERACIONES = ["Recolección", "Registro", "Almacenamiento", "Consulta y uso", "Análisis o perfilado",
               "Comunicación a terceros", "Transferencia internacional", "Conservación", "Supresión o anonimización"]

DICTAMEN = [
    "Favorable: el tratamiento puede iniciar",
    "Favorable con condiciones: iniciar solo tras implementar las medidas del plan",
    "Desfavorable: el riesgo residual no es aceptable; rediseñar el tratamiento",
]
