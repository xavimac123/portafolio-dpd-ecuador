"""Fuente única de la Herramienta 07: Evaluación de impacto del tratamiento de datos personales.

Base: LOPDP arts. 40 y 42; RGLOPDP arts. 29 a 32; Res. SPDP-SPD-2026-0012-R (Guía de Gestión de
Riesgos y Evaluación de Impacto, versión 2: Cap. I obligatorio, Cap. II referencial). La guía v2 ordena
cinco etapas: establecimiento del contexto, identificación, análisis, evaluación y tratamiento.

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
     "concepto": "La Superintendencia puede exigirla aunque no concurra ninguno de los tres supuestos, y puede definir otros casos. Ante la duda sobre si procede, el responsable puede consultar a la SPDP (RGLOPDP art. 31). No hacerla cuando es obligatoria es infracción grave (LOPDP art. 68 num. 5).",
     "norma": "Art. 42 LOPDP: se realiza también cuando la Autoridad de Protección de Datos Personales lo requiera."},
    {"id": "n_biometricos", "grupo": "norma", "oblig": True,
     "texto": "¿Se tratan datos biométricos (huella, rostro, iris, voz) para identificar o verificar a las personas?",
     "concepto": "La norma de biométricos exige análisis de riesgos y evaluación de impacto ANTES de implementar cualquier sistema biométrico, revisada cada 12 meses y cuando cambie el riesgo. Debe justificar que la biometría es estrictamente necesaria y que no hay un medio menos invasivo; si hay asimetría (trabajador, cliente sin alternativa), ofrecer una alternativa no biométrica equivalente o documentar aquí por qué es imposible. Privilegiar plantillas y no guardar el dato bruto. Con niñas, niños y adolescentes, prohibido con fines identificativos salvo que no exista medio menos invasivo y haya evaluación de impacto. Quien ya usaba biometría tiene 12 meses desde el 24-09-2026 para adecuarse.",
     "norma": "Res. SPDP-SPD-2026-0039-R, Norma general para el tratamiento de datos biométricos (RO 376, 24-09-2026), según resúmenes de terceros; LOPDP arts. 4, 25 y 26."},
    {"id": "n_ia", "grupo": "norma", "oblig": False,
     "texto": "¿Se desarrollan, entrenan, implementan, despliegan o proveen sistemas de inteligencia artificial que traten datos personales?",
     "concepto": "La norma de IA obliga a informar al titular el uso de IA y su carácter automatizado, hacer gestión de riesgos antes del desarrollo, evaluación de impacto cuando corresponda según el riesgo, medidas de seguridad, incluir el tratamiento y las decisiones automatizadas con efectos jurídicos en el RAT y auditar el sistema según su riesgo. La reforma de septiembre de 2026 limita las obligaciones del encargado a las fases en que tiene acceso, visibilidad o control efectivo de los datos. Si hay decisiones automatizadas con efectos jurídicos, la evaluación es obligatoria por el art. 42 lit. a de la LOPDP.",
     "norma": "Res. SPDP-SPD-2026-0009-R (RO 240, 10-03-2026) arts. 5 a 7, reformada por la Res. SPDP-SPD-2026-0037-R; LOPDP arts. 20 y 42."},
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
     "norma": "Art. 40 LOPDP (particularidades de las partes involucradas); Guía Res. SPDP-SPD-2026-0012-R (v2), Cap. II, establecimiento del contexto."},
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
    {"id": "p_conservacion", "texto": "El plazo de conservación está definido y justificado.", "ayuda": "Pide la norma o la razón de negocio que sustenta cada plazo y qué ocurre al vencer (supresión, anonimización o bloqueo)."},
    {"id": "p_calidad", "texto": "Existen mecanismos para mantener los datos exactos y actualizados.", "ayuda": "Ejemplos: actualización periódica, validación al ingreso, canal de rectificación."},
    {"id": "p_info", "texto": "Los titulares son informados conforme al art. 12 LOPDP.", "ayuda": "El art. 12 enumera 17 elementos: fines, base legal, tipos de tratamiento, conservación, existencia de la base de datos, origen, otras finalidades, identidad del responsable y del DPD, transferencias, consecuencias de entregar o no los datos, efecto de datos erróneos, revocatoria, ejercicio de derechos, portabilidad, reclamos y decisiones automatizadas. Si los datos no vienen del titular, se le informa en 30 días o en la primera comunicación."},
    {"id": "p_derechos", "texto": "Existe un procedimiento para que los titulares ejerzan sus derechos.", "ayuda": "Verifica canal, responsable interno, registro de solicitudes y plazo de 15 días para acceso, rectificación, eliminación y oposición (LOPDP arts. 13 a 16; RGLOPDP arts. 12 a 15)."},
    {"id": "p_encargados", "texto": "Los encargados tienen contrato con el contenido del art. 41 RGLOPDP.", "ayuda": "Contrato escrito con objeto, duración, naturaleza, finalidad, categorías de datos, titulares y obligaciones del encargado. No tenerlo es infracción grave (LOPDP art. 68 num. 9)."},
    {"id": "p_transf", "texto": "Las transferencias internacionales tienen garantía y están documentadas.", "ayuda": "Marca 'No aplica' si no hay transferencias. Vías: país con nivel adecuado, garantías en instrumento vinculante, normas corporativas vinculantes, autorización de la SPDP o excepciones (LOPDP arts. 56 a 60). Un encargado en el exterior no convierte por sí solo el encargo en transferencia internacional."},
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
    "Separación de bases de datos o de entornos (separar)", "Agregación o generalización de datos (abstraer)",
    "Configuración por defecto más protectora (por defecto)",
]
DECISIONES = ["Modificar (mitigar)", "Aceptar", "Evitar", "Transferir"]  # estrategias de la Guía v2, etapa 5

# ---------- Establecimiento del contexto (Guía v2, Cap. II, etapa 1)
# Los cinco factores (a-e) vienen de la guía. Las opciones y los puntos son CRITERIO PROPIO del portafolio.
FACTORES_IMPACTO = [
    {"id": "fa", "letra": "a", "nombre": "Categorías especiales de datos (art. 25 LOPDP)",
     "ayuda": "Datos sensibles, de salud, de niñas, niños y adolescentes, y de personas con discapacidad.",
     "ops": [["No se tratan", 0], ["Sí, de forma accesoria", 1], ["Sí, son el dato principal", 2]]},
    {"id": "fb", "letra": "b", "nombre": "Vulnerabilidad de los titulares",
     "ayuda": "La guía pide considerar edad, género, nivel educativo y socioeconómico, discapacidad y etnia. La relación de subordinación (trabajador frente al empleador, paciente frente a la clínica) reduce la capacidad de oponerse.",
     "ops": [["Población general", 0], ["Relación de subordinación o dependencia", 1], ["Grupos especialmente vulnerables", 2]]},
    {"id": "fc", "letra": "c", "nombre": "Número de titulares afectados",
     "ayuda": "La guía admite reglas específicas; cita como ejemplo que una vulneración que afecte a más de mil personas sea de riesgo muy alto.",
     "ops": [["Menos de 100", 0], ["De 100 a 1.000", 1], ["Más de 1.000", 2]]},
    {"id": "fd", "letra": "d", "nombre": "Naturaleza de la afectación más grave posible",
     "ayuda": "La pérdida de confidencialidad puede ser irreversible; la de integridad o disponibilidad suele ser temporal si existen respaldos y planes de continuidad. Analiza cada escenario por separado.",
     "ops": [["Disponibilidad o integridad recuperable", 0], ["Integridad que altera decisiones sobre el titular", 1], ["Confidencialidad: exposición irreversible", 2]]},
    {"id": "fe", "letra": "e", "nombre": "Volumen de datos por titular",
     "ayuda": "Cuántos atributos y cuánto historial se guarda de cada persona.",
     "ops": [["Pocos datos de identificación o contacto", 0], ["Perfil moderado", 1], ["Perfil amplio o historial detallado", 2]]},
]
# Piso de impacto sugerido = máx(1, redondeo hacia arriba de la suma / 2). Criterio propio.
DERECHOS = [
    "Protección de datos personales (autodeterminación informativa)", "Intimidad personal y familiar",
    "Honra y buen nombre", "Igualdad y no discriminación", "Trabajo", "Salud", "Integridad personal",
    "Libertad de expresión y de opinión", "Libertad de movimiento", "Acceso a bienes y servicios",
    "Propiedad y patrimonio", "Interés superior de niñas, niños y adolescentes", "Seguridad jurídica",
]
PERIODOS = ["Un año", "Un semestre", "Un trimestre", "Un mes"]
METODOS = [
    "Cualitativo calibrado: juicio experto con justificación (rationale) de cada valor",
    "Cualitativo estructurado: Delphi, Lens o análisis argumental",
    "Cuantitativo: frecuentista, bayesiano, Monte Carlo, FAIR o VaR",
    "Híbrido: cualitativo con datos cuantitativos donde existan",
]
PASOS_IMPACTO = [
    ["Define los criterios antes de valorar", "Completa los cinco factores de esta pestaña. Fijan cuán grave sería, como mínimo, una afectación en este tratamiento."],
    ["Identifica los derechos en juego", "Marca qué derechos del titular podría afectar el tratamiento. No te limites a la privacidad: piensa en trabajo, salud, igualdad, patrimonio."],
    ["Describe el escenario", "En la pestaña de riesgos, combina dato en riesgo, amenaza y vulnerabilidad: «un empleado con privilegios descarga la base de pacientes porque no hay registro de accesos»."],
    ["Separa impactos primarios y secundarios", "Primario: lo que sufre directamente el titular (exposición, fraude). Secundario: lo que provocan terceros (despido, discriminación, burla)."],
    ["Asigna impacto y probabilidad con justificación", "Cada valor necesita su rationale: antecedentes, datos del sector, controles existentes. Sin justificación, el número es ruido."],
    ["Compara con el piso de impacto", "Si asignas un impacto menor al piso sugerido por el contexto, explica por qué."],
    ["Decide y vuelve a medir", "Elige medidas, estima el riesgo residual y compáralo con el umbral de aceptación. Repite cuando cambie el tratamiento."],
]

OPERACIONES = ["Recolección", "Registro", "Almacenamiento", "Consulta y uso", "Análisis o perfilado",
               "Comunicación a terceros", "Transferencia internacional", "Conservación", "Supresión o anonimización"]

DICTAMEN = [
    "Favorable: el tratamiento puede iniciar",
    "Favorable con condiciones: iniciar solo tras implementar las medidas del plan",
    "Desfavorable: el riesgo residual no es aceptable; rediseñar el tratamiento",
]
