"""Fuente única del catálogo de servicios y del glosario (herramienta 01).

La calculadora de honorarios (herramienta 02) importa SERVICIOS desde aquí: ambas herramientas
usan los mismos códigos, nombres, unidades y precios sugeridos. Los precios son CRITERIO PROPIO.
"""

VERSION = "0.1"

TAMANOS = ["Micro", "Pequeña", "Mediana", "Grande"]

# Orden de las fases (también es el orden de los grupos en la proforma).
FASES = [
    ("Evaluación inicial", "Medir antes de proponer: dónde está la empresa, cuánto arriesga y qué obligaciones tiene."),
    ("Inventario y riesgos", "Saber qué datos se tratan y qué riesgo tienen antes de redactar documentos."),
    ("Adecuación", "Documentos y procedimientos que la empresa aprueba e implementa; el consultor redacta y asesora."),
    ("Control mensual", "Supervisión continua: la función propia del DPD."),
    ("Control anual", "Revisiones e informes periódicos que exige o recomienda la norma."),
    ("Por evento", "Servicios que se cotizan como tarifa y se cobran solo cuando ocurren."),
]

NATURALEZA = {
    "A": "Asesoría y diagnóstico",
    "B": "Borradores para aprobación de la empresa",
    "S": "Supervisión (función del DPD)",
    "F": "Formación",
    "R": "Acompañamiento ante la autoridad",
}

# Cada servicio:
#  cod, id, fase, nombre, naturaleza, que, como (pasos), para (dirigido a), obtiene,
#  herramientas (códigos del kit), responsable (departamento principal), conjunto, levantar (con quién),
#  recomendaciones, base, unidad, precio ([micro, pequeña, mediana, grande] o "auto:clave"), beneficio (texto para el cliente), proforma (bool)
S = []


def srv(cod, id_, fase, nombre, nat, que, como, para, obtiene, herr, resp, conj, levantar, rec, base, unidad, precio, beneficio, proforma=True):
    S.append(dict(cod=cod, id=id_, fase=fase, nombre=nombre, nat=nat, que=que, como=como, para=para, obtiene=obtiene,
                  herr=herr, resp=resp, conj=conj, levantar=levantar, rec=rec, base=base, unidad=unidad, precio=precio,
                  beneficio=beneficio, proforma=proforma))


# ---------------------------------------------------------------- Evaluación inicial
srv("S01", "reunion", "Evaluación inicial", "Reunión de diagnóstico inicial", "A",
    "Primera reunión de 30 a 45 minutos para entender el negocio, detectar señales de incumplimiento y explicar el rol del DPD.",
    ["Revisar el sitio web y la información pública de la empresa", "Aplicar el guion de primera reunión", "Mostrar un hallazgo concreto", "Proponer el diagnóstico con alcance y precio"],
    "Toda empresa interesada, antes de contratar", "Hallazgos preliminares y una propuesta de evaluación con alcance claro",
    ["01", "02"], "Gerencia", "—", "Gerente general o propietario",
    ["Explique en una frase que el DPD asesora y supervisa, no implementa", "No entregue el diagnóstico gratis: muestre un hallazgo, no la solución"],
    "LOPDP art. 10 lit. k", "reunión", [0, 0, 0, 0], "Saber en una reunión si su empresa tiene riesgos visibles.", proforma=False)
srv("S02", "diag", "Evaluación inicial", "Diagnóstico de madurez y exposición económica", "A",
    "Medición del cumplimiento en 12 dominios, estimación de la multa con la metodología de la SPDP, apetito al riesgo y plan de acción priorizado.",
    ["Mapeo inicial de la empresa", "Entrevistas por área con pedido de evidencia", "Aplicación del cuestionario de madurez", "Estimación de la multa con el volumen de negocio del ejercicio anterior", "Informe y plan de acción"],
    "Toda empresa al iniciar; cada año como revisión", "Índice de madurez, radar, multa estimada, plan de acción con responsables de la empresa",
    ["03"], "Gerencia", "Todas las áreas", "Gerencia, talento humano, contabilidad, ventas, sistemas, marketing",
    ["Sin documento no hay puntaje 3: puntúe con evidencia", "La multa es una estimación orientativa, no una liquidación", "Pida los ingresos del ejercicio anterior a contabilidad, no a la gerencia"],
    "LOPDP arts. 10 lit. k, 47, 71 a 73; Res. SPDP-SPD-2025-0022-R", "servicio", "auto:diag",
    "Saber exactamente dónde está su empresa, cuánto arriesga y qué hacer primero.")
srv("S03", "mtge", "Evaluación inicial", "Análisis de gran escala y obligación de designar DPD", "A",
    "Calificación de cada tratamiento con el Modelo Técnico de Gran Escala y revisión de las causales de designación obligatoria del DPD.",
    ["Enviar la solicitud de información", "Revisar los casos de calificación directa", "Puntuar las seis variables con evidencia", "Revisar las causales de la Res. SPDP-SPD-2025-0028-R", "Informe y columnas para el RAT"],
    "Empresas que dudan si deben tener DPD; obligatorio de facto para toda empresa con RAT", "Respuesta documentada a «¿debo tener DPD?» y obligaciones reforzadas, si las hay",
    ["05"], "Gerencia", "Sistemas, dueños de procesos", "Sistemas (conteos de titulares), dueños de procesos (campos, frecuencia), legal (plazos)",
    ["Mida por tratamiento, no por empresa", "La permanencia es tiempo de uso activo, no de archivo", "Si el resultado es desproporcionado, sugiera la consulta a la SPDP"],
    "RGLOPDP arts. 4 num. 7 y 53; Res. SPDP-SPD-2026-0005-R; Res. SPDP-SPD-2025-0028-R", "servicio", [120, 180, 250, 350],
    "Certeza, con base en el modelo oficial, sobre si debe designar DPD y evaluar riesgos.")
srv("S04", "informe", "Evaluación inicial", "Informe ejecutivo y presentación a la gerencia", "A",
    "Informe de evaluación general con matriz de soportes y reunión de 20 minutos centrada en decisiones.",
    ["Consolidar resultados de los servicios contratados", "Armar la matriz de soportes", "Presentar tres gráficos y tres decisiones", "Levantar el acta"],
    "Gerencias y directorios", "Decisiones aprobadas por la gerencia y acta como evidencia",
    ["03", "04", "05"], "Gerencia", "Directorio o socios", "Gerencia general",
    ["Hable en lenguaje de negocio: riesgo, costo, decisión", "Cada cifra del informe debe tener soporte"],
    "LOPDP art. 10 lit. k", "servicio", [150, 250, 400, 600], "Decisiones claras de la dirección, con respaldo documental.")
# ---------------------------------------------------------------- Inventario y riesgos
srv("S05", "rat", "Inventario y riesgos", "Registro de actividades de tratamiento (RAT)", "B",
    "Inventario de cada actividad de tratamiento con el contenido mínimo del art. 38 RGLOPDP, encargados, destinatarios y plazos.",
    ["Entrevistas por proceso", "Catálogo de actividades y validación con el dueño", "Registro de encargados y destinatarios", "Control del mínimo legal", "Aprobación de la gerencia"],
    "Obligatorio con 100 o más trabajadores o en los supuestos del art. 39 RGLOPDP; necesario para cualquier adecuación", "RAT aprobado: la base de la política, los contratos y la evaluación de impacto",
    ["04"], "Dueños de procesos", "Sistemas, legal", "Cada jefe de área, sistemas, contabilidad",
    ["Una actividad por finalidad y base: no agrupe todo en «clientes»", "El RAT es de la empresa: usted lo redacta, ellos lo aprueban y mantienen"],
    "RGLOPDP arts. 38, 39 y 44; LOPDP art. 51", "servicio", [350, 700, 1400, 2800], "El inventario oficial que pedirá la Superintendencia.")
srv("S06", "eipd", "Inventario y riesgos", "Evaluación de impacto (por tratamiento)", "A",
    "Análisis previo de necesidad, proporcionalidad, riesgos y medidas, con informe del contenido del art. 32 RGLOPDP.",
    ["Confirmar si es obligatoria", "Describir el tratamiento", "Evaluar necesidad y proporcionalidad", "Valorar riesgos y medidas", "Dictamen y plan; aprobación de la gerencia"],
    "Tratamientos de gran escala, perfiles automatizados, biométricos, inteligencia artificial, datos de NNA", "Decisión informada antes de lanzar un tratamiento de alto riesgo",
    ["06"], "Dueño del proceso evaluado", "Sistemas, gerencia", "Dueño del proceso, sistemas, proveedor de la tecnología",
    ["Hágala antes del tratamiento, no después", "Las medidas las implementa la empresa; usted verifica el riesgo residual"],
    "LOPDP art. 42; RGLOPDP arts. 29 a 32; Res. SPDP-SPD-2025-0003-R", "tratamiento", [450, 600, 900, 1500],
    "Lanzar tratamientos de alto riesgo con respaldo técnico y legal.")
srv("S07", "ponderacion", "Inventario y riesgos", "Ponderación del interés legítimo (por tratamiento)", "A",
    "Análisis que respalda el uso del interés legítimo como base: finalidad, necesidad y equilibrio con los derechos del titular.",
    ["Identificar el interés y su legitimidad", "Probar la necesidad", "Ponderar con las expectativas del titular", "Documentar garantías y conclusión"],
    "Empresas que usan videovigilancia, marketing a clientes, prevención de fraude u otros tratamientos sin consentimiento", "Documento de ponderación que se registra en el RAT",
    ["04"], "Dueño del proceso", "Legal, marketing", "Marketing, seguridad, legal",
    ["Solo en el sector privado", "Si la ponderación no favorece a la empresa, la base debe ser otra"],
    "LOPDP art. 7; Res. SPDP-SPD-2025-0041-R; RGLOPDP art. 38 num. 7", "tratamiento", [150, 200, 300, 450],
    "Tratar datos sin consentimiento con un fundamento sólido y documentado.")
srv("S08", "transfer", "Inventario y riesgos", "Análisis de encargos y transferencias", "A",
    "Clasificación de cada flujo de datos como encargo o comunicación, y análisis de las transferencias internacionales y sus garantías.",
    ["Listar proveedores y destinatarios", "Preguntar para quién trabaja cada uno", "Revisar ubicación y contratos", "Definir base y garantías de cada transferencia"],
    "Empresas con nube, proveedores externos, grupo empresarial o envíos de datos al exterior", "Mapa de encargados y destinatarios, con la base o el contrato que necesita cada uno",
    ["04", "07"], "Legal o compras", "Sistemas, contabilidad", "Compras, sistemas, contabilidad, legal",
    ["Un encargado en el exterior no convierte el encargo en transferencia internacional", "Si un proveedor usa los datos para sus fines, es responsable"],
    "LOPDP arts. 33 a 35 y 56; RGLOPDP art. 43; Res. SPDP-SPD-2026-0004-R", "servicio", [200, 300, 450, 700],
    "Saber qué contrato o base necesita cada proveedor y cada envío de datos.")
# ---------------------------------------------------------------- Adecuación
srv("S09", "adec", "Adecuación", "Programa de adecuación integral", "B",
    "Borradores de RAT, política y avisos, contratos de encargo, protocolo de vulneraciones, procedimiento de derechos, capacitación inicial y designación del DPD.",
    ["Plan de trabajo con responsables de la empresa", "Redacción de borradores", "Revisión y aprobación de la gerencia", "Implementación por la empresa", "Verificación"],
    "Empresas sin documentación, que prefieren un solo programa", "Documentos aprobados y plan de implementación a cargo de la empresa",
    ["04", "07", "08"], "Gerencia", "Todas las áreas", "Gerencia y jefes de área",
    ["Escriba en la propuesta qué implementa la empresa", "No combine este programa con servicios sueltos que ya incluye"],
    "LOPDP arts. 10 lit. k y 47", "programa", "auto:adec", "Cumplimiento documentado de las obligaciones de la LOPDP en un solo programa.")
srv("S10", "politica", "Adecuación", "Política de privacidad y avisos", "B",
    "Política construida desde el RAT y avisos para cada punto de recolección: formularios, cámaras, correo, contratación.",
    ["Trasladar finalidades, bases y plazos del RAT", "Redactar un aviso por punto de recolección", "Aprobación y publicación por la empresa"],
    "Toda empresa que recolecta datos", "Deber de información cumplido", ["07"], "Gerencia", "Marketing, talento humano, sistemas (web)",
    "Marketing, talento humano, sistemas",
    ["Sin RAT, la política queda genérica: no la haga primero", "Un aviso por canal, no uno genérico"],
    "LOPDP art. 12", "paquete", [250, 400, 600, 900], "Clientes y trabajadores informados conforme al art. 12 LOPDP.")
srv("S11", "contratos", "Adecuación", "Contratos de encargo y cláusulas", "B",
    "Contratos con encargados y cláusulas de consentimiento cuando esa es la base; paquete de hasta cinco.",
    ["Identificar encargados desde el RAT", "Redactar contratos con el contenido del art. 41", "Firma de la empresa y el proveedor"],
    "Empresas con contador, nómina, nube, seguridad u otros proveedores con acceso a datos", "Encargados obligados por contrato",
    ["07"], "Legal o compras", "Gerencia", "Compras, legal, contabilidad",
    ["La falta de contrato de encargo es infracción grave", "Pida consentimiento solo cuando es la base correcta"],
    "RGLOPDP arts. 40 y 41; LOPDP arts. 34, 35 y 68 num. 9; Res. SPDP-SPD-2025-0006-R", "paquete", [200, 350, 500, 800],
    "Proveedores obligados por contrato: evita una infracción grave.")
srv("S12", "gobierno", "Adecuación", "Política interna y roles de protección de datos", "B",
    "Política interna aprobada por la dirección, roles y responsables por área, y reporte periódico a la gerencia.",
    ["Definir responsables por área", "Redactar la política interna", "Aprobación de la gerencia y comunicación al personal"],
    "Empresas medianas y grandes, o con varios procesos con datos", "Gobierno de la protección de datos con responsables claros",
    ["03"], "Gerencia", "Talento humano", "Gerencia, talento humano",
    ["Los responsables por área son de la empresa, no el DPD", "Incluya el canal de reporte al DPD"],
    "LOPDP arts. 10 lit. k y 47", "paquete", [200, 300, 450, 700], "Cada área sabe qué le toca y a quién reportar.")
srv("S13", "conservacion", "Adecuación", "Tabla de conservación y procedimiento de supresión", "B",
    "Plazos de conservación por actividad y procedimiento de bloqueo, anonimización o eliminación al vencer el plazo.",
    ["Tomar los plazos del RAT", "Contrastar con plazos legales", "Definir método de supresión y constancia"],
    "Empresas con archivos acumulados o datos sin plazo definido", "Datos conservados solo el tiempo necesario y supresión documentada",
    ["04"], "Legal", "Contabilidad, talento humano, sistemas", "Legal, contabilidad, talento humano, sistemas",
    ["Distinga uso activo de archivo", "La eliminación la ejecuta la empresa; usted verifica la constancia"],
    "LOPDP art. 10; Res. SPDP-SPD-2025-0030-R", "paquete", [150, 250, 400, 650], "Menos datos guardados sin razón: menos riesgo.")
srv("S14", "derechos", "Adecuación", "Procedimiento de atención de derechos", "B",
    "Canal, formularios, plazos y registro de solicitudes de acceso, rectificación, eliminación, oposición y otros derechos.",
    ["Definir canal y responsable interno", "Redactar formularios y respuestas tipo", "Registro de solicitudes"],
    "Toda empresa con clientes o trabajadores", "Respuesta en plazo a cada titular", ["07"], "Servicio al cliente", "Talento humano, legal",
    "Servicio al cliente, talento humano",
    ["Use un correo institucional, no el personal del DPD", "Registre cada solicitud, se atienda o no"],
    "LOPDP arts. 12 y siguientes", "paquete", [150, 250, 400, 600], "Atender reclamos a tiempo y reducir denuncias ante la SPDP.")
srv("S15", "vulner", "Adecuación", "Protocolo de vulneraciones y bitácora", "B",
    "Protocolo aprobado, roles, bitácora y modelos de notificación a la SPDP, ARCOTEL, CSIRT y titulares.",
    ["Definir el equipo de respuesta", "Redactar el protocolo con plazos", "Aprobación y difusión interna"],
    "Toda empresa; prioritario si ya tuvo incidentes", "Respuesta en plazo, sin improvisar", ["08"], "Sistemas", "Gerencia, legal",
    "Sistemas, gerencia",
    ["El protocolo debe existir antes del incidente", "El responsable notifica; el DPD asesora y coordina"],
    "LOPDP art. 43; RGLOPDP arts. 24 a 28; Res. SPDP-SPD-2026-0040-R", "paquete", [200, 350, 550, 850],
    "Responder a un incidente en los plazos legales.")
srv("S16", "web", "Adecuación", "Revisión de sitio web y canales digitales", "A",
    "Revisión de formularios, avisos, cookies, chat y redes sociales donde la empresa recolecta datos.",
    ["Recorrer cada canal digital", "Listar hallazgos", "Recomendar ajustes; la empresa los implementa"],
    "Empresas con comercio electrónico, formularios web o campañas digitales", "Lista priorizada de ajustes en canales digitales",
    ["03", "07"], "Marketing", "Sistemas", "Marketing, sistemas, proveedor web",
    ["Es la evidencia más visible para un cliente o la SPDP", "No modifique el sitio usted mismo"],
    "LOPDP arts. 8 y 12", "servicio", [150, 200, 300, 450], "Canales digitales que informan y piden datos correctamente.")
srv("S17", "capac", "Adecuación", "Capacitación al personal (taller de 2 horas)", "F",
    "Taller práctico con casos del propio negocio, evaluación y registro de asistencia como evidencia.",
    ["Diseñar casos del negocio", "Impartir el taller", "Evaluar y registrar asistencia"],
    "Todo el personal; directivos por separado", "Personal que reconoce riesgos y sabe a quién reportar", ["03"], "Talento humano", "Gerencia",
    "Talento humano",
    ["Capacitar es compatible con la función del DPD", "Separe el taller de directivos del operativo"],
    "RGLOPDP art. 30 num. 4", "taller", [200, 300, 450, 700], "La primera barrera contra incidentes: personas preparadas.")
# ---------------------------------------------------------------- Control
srv("S18", "dpd", "Control mensual", "Delegado de Protección de Datos externo", "S",
    "Funciones del art. 49 LOPDP: asesorar, supervisar el cumplimiento, asesorar en riesgos y evaluaciones de impacto, y ser punto de contacto con la SPDP.",
    ["Designación y registro ante la SPDP", "Revisión periódica del RAT y de evidencias", "Asesoría en consultas y proyectos", "Reporte mensual a la gerencia"],
    "Empresas obligadas a designar DPD (gran escala o Res. SPDP-SPD-2025-0028-R) o que deciden hacerlo", "Supervisión independiente e interlocución con la SPDP",
    ["03", "04", "05"], "Gerencia", "Todas las áreas", "Gerencia y responsables por área",
    ["Contrato de servicios, de encargo y de confidencialidad antes de iniciar", "No decida por la empresa ni implemente lo que supervisa", "No acumule cargos de oficial de cumplimiento, de seguridad de la información o apoderado especial"],
    "LOPDP arts. 48 y 49; RGLOPDP arts. 48 y 55; Res. SPDP-SPD-2025-0028-R", "mes", "auto:mens",
    "Un especialista independiente que supervisa el cumplimiento cada mes.")
srv("S19", "acomp", "Control mensual", "Acompañamiento de cumplimiento (sin designación)", "A",
    "Soporte al responsable interno: revisión del RAT, asesoría en proyectos nuevos y consultas.",
    ["Reunión mensual", "Revisión de cambios en procesos", "Asesoría por consulta"],
    "Empresas no obligadas a designar DPD o con un responsable interno", "Soporte experto continuo a menor costo",
    ["04"], "Responsable interno", "Gerencia", "Responsable interno",
    ["No es designación: no registre su nombre como DPD", "Fije un número de horas o consultas incluidas"],
    "LOPDP art. 47", "mes", "auto:acomp", "Soporte experto continuo a un costo menor.")
srv("S20", "informeanual", "Control anual", "Informe anual de cumplimiento", "S",
    "Informe que consolida control interno, revisiones del MTGE, evaluaciones de impacto e incidentes del año.",
    ["Recalcular la madurez y la gran escala", "Revisar indicadores y evidencias", "Redactar y presentar el informe"],
    "Obligatorio con tratamientos de gran escala; recomendado para todos", "Evidencia anual de responsabilidad proactiva",
    ["03", "05"], "Gerencia", "Todas las áreas", "Gerencia, responsables por área",
    ["Consérvelo cinco años si hay gran escala", "Incluya lo que no se cumplió y por qué"],
    "Res. SPDP-SPD-2026-0005-R art. 18; LOPDP art. 10 lit. k", "informe", [200, 300, 500, 800], "Un año de cumplimiento demostrado en un solo documento.")
srv("S21", "auditoria", "Control anual", "Auditoría de cumplimiento independiente", "A",
    "Revisión independiente del programa de protección de datos frente a la LOPDP, con hallazgos y plan de mejora.",
    ["Plan de auditoría", "Revisión de evidencias y entrevistas", "Informe de hallazgos"],
    "Empresas con tratamientos de gran escala o que necesitan una revisión externa", "Hallazgos independientes y plan de mejora",
    ["03", "05"], "Gerencia", "Todas las áreas", "Gerencia, responsables por área",
    ["No audite a un cliente del que es DPD o al que adecuó: perdería independencia", "La auditoría por gran escala es al menos cada 12 meses"],
    "Res. SPDP-SPD-2026-0005-R art. 17", "auditoría", [500, 900, 1600, 3000], "Una mirada independiente sobre su cumplimiento.")
# ---------------------------------------------------------------- Por evento
srv("S22", "incidente", "Por evento", "Gestión de una vulneración de la seguridad", "R",
    "Acompañamiento en la evaluación, documentación y notificaciones en plazo de un incidente.",
    ["Registrar la hora de constancia", "Evaluar gravedad", "Preparar notificaciones", "Bitácora y lecciones aprendidas"],
    "Empresas que sufren un incidente", "Notificaciones en plazo y documentación completa", ["08"], "Sistemas", "Gerencia, legal",
    "Sistemas, gerencia, encargado involucrado",
    ["Los plazos corren desde la constancia del incidente", "La contención técnica la hace sistemas"],
    "LOPDP art. 43; Res. SPDP-SPD-2026-0040-R", "incidente", [250, 400, 600, 900], "Acompañamiento inmediato cuando más se necesita.")
srv("S23", "solicitud", "Por evento", "Atención de solicitud de derechos adicional", "A",
    "Revisión y respuesta tipo para una solicitud fuera del volumen incluido en el plan mensual.",
    ["Verificar identidad y alcance", "Preparar respuesta", "Registrar"], "Clientes con plan mensual que superan el volumen incluido",
    "Respuesta en plazo", ["07"], "Servicio al cliente", "Legal", "Servicio al cliente",
    ["La respuesta la firma la empresa"], "LOPDP arts. 12 y siguientes", "solicitud", [25, 35, 50, 70], "Respuesta en plazo a cada titular.")
srv("S24", "proyecto", "Por evento", "Privacidad desde el diseño en un proyecto nuevo", "A",
    "Asesoría en un sistema, aplicación, campaña o proceso nuevo antes de su lanzamiento.",
    ["Revisar el proyecto", "Identificar datos y riesgos", "Recomendar ajustes y, si corresponde, evaluación de impacto"],
    "Empresas que contratan software, lanzan aplicaciones o campañas", "Proyecto ajustado antes de tratar datos", ["05", "06"], "Dueño del proyecto",
    "Sistemas, proveedor", "Dueño del proyecto, sistemas, proveedor",
    ["Intervenga antes de firmar con el proveedor", "Recomiende; la decisión es del dueño del proyecto"],
    "Res. SPDP-SPD-2026-0005-R art. 16; LOPDP art. 42", "proyecto", [250, 350, 500, 800], "Pensar en los datos antes de comprar o desarrollar.")
srv("S25", "proveedor", "Por evento", "Evaluación de un proveedor encargado", "A",
    "Revisión de las garantías de un proveedor antes de contratarlo: contrato, medidas de seguridad, ubicación y subencargados.",
    ["Cuestionario al proveedor", "Revisión de contrato y garantías", "Recomendación"], "Empresas que contratan proveedores con acceso a datos",
    "Proveedor evaluado y contrato con garantías", ["04", "07"], "Compras", "Sistemas, legal", "Compras, sistemas, el proveedor",
    ["Pregunte por subencargados y servidores", "Guarde la evaluación como evidencia"],
    "RGLOPDP arts. 40 y 41", "proveedor", [60, 80, 100, 150], "Contratar proveedores que protegen sus datos.")
srv("S26", "simulacro", "Por evento", "Simulacro de vulneración", "F",
    "Ejercicio de mesa con un incidente ficticio para probar el protocolo, los roles y los plazos.",
    ["Diseñar el escenario", "Conducir el ejercicio", "Informe de mejoras"], "Empresas con protocolo aprobado", "Protocolo probado y mejoras identificadas",
    ["08"], "Sistemas", "Gerencia, legal, comunicación", "Equipo de respuesta",
    ["Hágalo una vez al año", "Mida tiempos reales frente a los plazos legales"],
    "LOPDP art. 43; Res. SPDP-SPD-2026-0040-R", "ejercicio", [200, 300, 450, 700], "Saber que el protocolo funciona antes de necesitarlo.")
srv("S27", "spdp", "Por evento", "Acompañamiento ante requerimientos o consultas a la SPDP", "R",
    "Preparación de respuestas a requerimientos, acompañamiento en inspecciones y elaboración de consultas formales.",
    ["Analizar el requerimiento", "Reunir evidencias", "Preparar la respuesta o la consulta", "Acompañar la diligencia"],
    "Empresas que reciben requerimientos o necesitan un criterio vinculante", "Respuesta en plazo y respaldada; consultas con respuesta obligatoria para el consultante",
    [], "Gerencia", "Legal", "Gerencia, legal",
    ["Si además será patrocinio en un procedimiento sancionador, evalúe el conflicto con su rol de DPD"],
    "LOPDP art. 76; RGLOPDP art. 53", "trámite", [200, 350, 500, 800], "Responder a la autoridad con orden y evidencia.")
srv("S28", "hora", "Por evento", "Hora adicional de asesoría", "A",
    "Asesoría puntual fuera del alcance contratado.", ["Registrar la consulta", "Responder por escrito"], "Cualquier cliente",
    "Respuesta puntual documentada", ["02"], "Quien consulta", "—", "Quien consulta",
    ["Registre el tiempo para justificar la factura"], "—", "hora", "auto:hora", "Flexibilidad para consultas puntuales.")

SERVICIOS = S

RECOMENDACIONES = [
    ["Alcance escrito", "Cada servicio contratado debe indicar qué entrega el consultor y qué ejecuta la empresa."],
    ["Orden", "No ofrezca documentos antes del inventario: S05 antes de S10 a S15."],
    ["Independencia", "Separe por contrato la adecuación (asesoría) del servicio de DPD (supervisión). No audite lo que adecuó o supervisa."],
    ["Evidencia", "Todo servicio termina en un documento fechado y firmado: es la prueba de responsabilidad proactiva del cliente y su respaldo profesional."],
    ["Confidencialidad y encargo", "Si accederá a datos personales del cliente, firme contrato de encargo y acuerdo de confidencialidad antes de iniciar."],
    ["Precios", "Use los valores sugeridos como referencia; ajústelos con la calculadora (herramienta 02) al tamaño, sector y volumen real del cliente."],
    ["Códigos", "Use los códigos S01 a S28 en la proforma, el contrato y la factura para que todos hablen del mismo servicio."],
    ["Actualización", "Revise el catálogo cuando la SPDP emita normativa nueva: un servicio puede volverse obligatorio para el cliente."],
]

# ---------------------------------------------------------------- Glosario
# LOPDP art. 4: resumen fiel de cada definición (no es texto literal; consultar el Registro Oficial).
GLOSARIO_LOPDP = [
    ["Autoridad de Protección de Datos Personales", "Autoridad pública independiente que supervisa la aplicación de la ley, su reglamento y sus resoluciones para proteger los derechos de las personas sobre sus datos. En Ecuador es la SPDP."],
    ["Anonimización", "Medidas que impiden identificar o reidentificar a una persona sin esfuerzos desproporcionados."],
    ["Base de datos o fichero", "Conjunto estructurado de datos, cualquiera sea su forma, soporte o ubicación, centralizado o distribuido."],
    ["Consentimiento", "Manifestación de voluntad libre, específica, informada e inequívoca por la que el titular autoriza el tratamiento."],
    ["Dato biométrico", "Dato único relativo a características físicas, fisiológicas o conductuales que permite o confirma la identificación de una persona, como la imagen facial o la huella."],
    ["Dato genético", "Dato único sobre características genéticas heredadas o adquiridas que informa sobre la fisiología o la salud de una persona."],
    ["Dato personal", "Dato que identifica o hace identificable a una persona natural, de forma directa o indirecta."],
    ["Datos personales crediticios", "Datos que reflejan el comportamiento económico de una persona para evaluar su capacidad financiera."],
    ["Datos relativos a la salud", "Datos sobre la salud física o mental de una persona, incluida la atención sanitaria que revele su estado de salud."],
    ["Datos sensibles", "Datos sobre etnia, identidad de género, identidad cultural, religión, ideología, filiación política, pasado judicial, condición migratoria, orientación sexual, salud, biométricos, genéticos y otros cuyo tratamiento indebido pueda causar discriminación o atentar contra derechos."],
    ["Delegado de protección de datos", "Persona natural que informa y asesora al responsable o encargado sobre sus obligaciones, supervisa el cumplimiento y coopera con la Autoridad como punto de contacto."],
    ["Destinatario", "Persona natural o jurídica a la que se comunican datos personales."],
    ["Elaboración de perfiles", "Tratamiento que evalúa o predice aspectos de una persona: desempeño laboral, situación económica, salud, preferencias, intereses, fiabilidad, comportamiento o ubicación."],
    ["Encargado del tratamiento", "Persona o entidad, pública o privada, que trata datos personales por cuenta del responsable."],
    ["Entidad certificadora", "Entidad reconocida por la Autoridad que puede emitir certificaciones en protección de datos."],
    ["Fuente accesible al público", "Base de datos que cualquier persona puede consultar libremente, sin condiciones."],
    ["Responsable del tratamiento", "Persona o entidad, pública o privada, que sola o con otros decide las finalidades y los medios del tratamiento."],
    ["Sellos de protección de datos", "Acreditación que otorga una entidad certificadora a quien implementó mejores prácticas, para generar confianza del titular, según la normativa técnica de la Autoridad."],
    ["Seudonimización", "Tratamiento que impide atribuir los datos a una persona sin información adicional guardada por separado y protegida."],
    ["Titular", "Persona natural cuyos datos son objeto de tratamiento."],
    ["Transferencia o comunicación", "Revelación de datos a una persona distinta del titular, el responsable o el encargado, por cualquier medio: entrega, consulta, interconexión, transmisión o difusión."],
    ["Tratamiento", "Cualquier operación sobre datos personales, automatizada o no: recolección, registro, conservación, uso, modificación, comunicación, supresión y otras."],
    ["Vulneración de la seguridad de los datos personales", "Incidente de seguridad que afecta la confidencialidad, disponibilidad o integridad de los datos."],
]
GLOSARIO_NORMATIVA = [
    ["Tercero", "Persona o entidad distinta del titular, el responsable, el encargado y quienes están autorizados a tratar los datos bajo su autoridad.", "RGLOPDP art. 4 num. 6"],
    ["Tratamiento a gran escala", "El que afecta a muchos datos de un elevado número de titulares de amplia diversidad geográfica y puede implicar riesgo; se mide con el MTGE (6 puntos o más) o por calificación directa.", "RGLOPDP art. 4 num. 7; Res. SPDP-SPD-2026-0005-R"],
    ["Registro de actividades de tratamiento (RAT)", "Inventario de las actividades de tratamiento con su contenido mínimo legal.", "RGLOPDP art. 38"],
    ["Evaluación de impacto", "Análisis previo de los riesgos de un tratamiento para los derechos de los titulares y de las medidas para mitigarlos.", "LOPDP art. 42; RGLOPDP arts. 29 a 32"],
    ["Responsabilidad proactiva", "Obligación del responsable de acreditar que implementó mecanismos de protección de datos.", "LOPDP art. 10 lit. k"],
    ["Base legitimadora", "Fundamento que hace lícito el tratamiento: consentimiento, obligación legal, orden judicial, interés público, contrato, interés vital, fuentes públicas o interés legítimo.", "LOPDP art. 7"],
    ["Interés legítimo", "Base de legitimación del sector privado que requiere una ponderación documentada frente a los derechos del titular.", "Res. SPDP-SPD-2025-0041-R"],
    ["Encargo", "Acceso de un encargado a los datos para prestar un servicio al responsable; no es transferencia ni comunicación.", "LOPDP arts. 34 y 35"],
    ["Modelo Técnico de Gran Escala (MTGE)", "Suma de seis variables por tratamiento: titulares, volumen, categorías, frecuencia, permanencia y alcance geográfico.", "Res. SPDP-SPD-2026-0005-R arts. 7 a 10"],
    ["SISPDP", "Sistema de la SPDP por el que se notifican obligatoriamente las vulneraciones de seguridad.", "Res. SPDP-SPD-2026-0040-R"],
]
GLOSARIO_KIT = [
    ["Adecuación", "Diagnosticar y documentar lo que la empresa debe cambiar para cumplir. La empresa la aprueba; el consultor puede redactar los borradores."],
    ["Implementación", "Poner en operación las medidas: formularios, sistemas, contratos firmados, capacitación. La ejecuta la empresa."],
    ["Supervisión", "Verificar, medir e informar que lo documentado e implementado se cumple. Es la función propia del DPD."],
    ["Riesgo inherente y residual", "Riesgo antes de las medidas y riesgo que queda después de aplicarlas."],
    ["Apetito al riesgo", "Pérdida que la gerencia está dispuesta a asumir, expresada como capacidad y tolerancia (criterio referencial de la guía de riesgos de la SPDP)."],
    ["Volumen de negocio", "Ingresos por ventas y servicios del ejercicio anterior, sin IVA ni impuestos relacionados; base de las multas (LOPDP art. 73)."],
]
