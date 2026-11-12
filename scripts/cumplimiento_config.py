"""Fuente de la organización de la pestaña Herramientas y de dos vistas nativas de la app:

- ART12: informe del deber de información (LOPDP art. 12, texto de la copia LEXIS de la ley reformada al 22-05-2026).
- ACCIONES: plan de implementación (lo que la empresa debe hacer para cumplir; el DPD supervisa y verifica),
  con base legal (LOPDP art. 47 y normas citadas en BASE-LEGAL.md) y el departamento responsable sugerido por tamaño.
- CLASIF: clasificación de las herramientas por tamaño de empresa.

Los departamentos, la clasificación y los tamaños son CRITERIO PROPIO: se rotulan así en la interfaz y en el informe.
Tamaños según trabajadores (referencia del Código Orgánico de la Producción): micro 1-9, pequeña 10-49, mediana 50-199, grande 200+.
"""

TAMANOS = ["Microempresa", "Pequeña", "Mediana", "Grande"]

# [num, elemento, qué verificar y dónde]
ART12 = [
 [1, "Los fines del tratamiento", "Cada finalidad se describe de forma concreta (no «fines comerciales» genéricos), en la política y en los avisos de cada formulario."],
 [2, "La base legal del tratamiento", "Para cada finalidad se indica la base del art. 7 (consentimiento, contrato, obligación legal, interés legítimo…)."],
 [3, "Tipos de tratamiento", "Se explica qué se hace con los datos: recolección, almacenamiento, análisis, perfiles, envío a terceros."],
 [4, "Tiempo de conservación", "Plazo o criterio de conservación por tipo de dato o finalidad, y qué ocurre al vencer."],
 [5, "Existencia de una base de datos con sus datos", "Se informa que los datos constan en una base de datos y quién la administra."],
 [6, "Origen de los datos cuando no se obtuvieron del titular", "Si se compran o reciben bases de terceros o fuentes públicas, se indica el origen y se informa en 30 días o en la primera comunicación."],
 [7, "Otras finalidades y tratamientos ulteriores", "Usos posteriores previstos (estadística, mejora del servicio, publicidad) y su compatibilidad."],
 [8, "Identidad y contacto del responsable", "Razón social, domicilio legal, teléfono y correo electrónico."],
 [9, "Identidad y contacto del delegado (cuando corresponda)", "Nombre o cargo del DPD, dirección, teléfono y correo. Si no hay DPD obligatorio, indicar el canal de contacto en materia de datos."],
 [10, "Transferencias o comunicaciones nacionales o internacionales", "Destinatarios y sus clases, finalidades y garantías; incluye proveedores en la nube fuera del país."],
 [11, "Consecuencias de entregar o negarse a entregar los datos", "Qué datos son obligatorios y qué ocurre si el titular no los entrega."],
 [12, "Efecto de suministrar datos erróneos o inexactos", "Advertencia sobre las consecuencias de datos falsos o desactualizados."],
 [13, "Posibilidad de revocar el consentimiento", "Cómo revocar, sin costo y por un medio sencillo."],
 [14, "Existencia y forma de ejercer los derechos", "Acceso, eliminación, rectificación y actualización, oposición, anulación, limitación y no ser objeto de decisiones automatizadas: canal, requisitos y plazo de respuesta."],
 [15, "Mecanismos para ejercer la portabilidad", "Cómo se solicita y en qué formato se entregan los datos."],
 [16, "Dónde y cómo reclamar ante el responsable y ante la SPDP", "Canal interno de reclamos y mención de la Superintendencia de Protección de Datos Personales."],
 [17, "Existencia de valoraciones y decisiones automatizadas, incluida la elaboración de perfiles", "Si existen (scoring, segmentación, IA), se informa su lógica y consecuencias; si no existen, se declara."],
]
ART12_COND = [
 ["Momento", "Si los datos se recogen del titular, la información se entrega antes o en el momento mismo de la recogida."],
 ["Datos de terceros o fuentes públicas", "Se informa dentro de 30 días o en la primera comunicación, lo que ocurra primero."],
 ["Forma", "Información expresa, inequívoca, transparente, inteligible, concisa, precisa, sin barreras técnicas y en lenguaje claro, por un medio comprobable."],
 ["Niñas, niños y adolescentes", "En productos o servicios dirigidos a ellos, la información se entrega a su representante legal."],
]
# Dónde suele estar la información (para el campo «Dónde consta»)
DOCS12 = ["Política de privacidad publicada", "Aviso en formulario web", "Aviso en formulario físico", "Contrato o anexo",
          "Aviso de videovigilancia", "Contrato de trabajo o reglamento interno", "Correo o mensaje al titular", "No consta"]

# Departamento responsable sugerido por tamaño: [micro, pequeña, mediana, grande]
ACCIONES = [
 {"id": "A01", "n": "Política interna de protección de datos aprobada", "base": "LOPDP art. 47 num. 4", "herr": "08",
  "ent": "Política aprobada por la gerencia o el directorio, difundida al personal",
  "dep": ["Gerente propietario", "Gerencia con asesor legal externo", "Legal o Cumplimiento", "Oficina de Cumplimiento (aprueba el Directorio)"]},
 {"id": "A02", "n": "Política de privacidad y avisos con los 17 elementos del art. 12", "base": "LOPDP art. 12", "herr": "A12",
  "ent": "Política publicada y avisos en cada punto de recolección (web, formularios, cámaras, contratos)",
  "dep": ["Gerente propietario", "Administración", "Marketing con Legal", "Marketing y Experiencia del cliente con Legal"]},
 {"id": "A03", "n": "Registro de actividades de tratamiento (RAT)", "base": "RGLOPDP arts. 38 y 39; LOPDP art. 47 num. 2", "herr": "04", "regla": "rat",
  "ent": "RAT con los nueve contenidos mínimos, firmado y actualizado",
  "dep": ["Gerente propietario con el DPD", "Administración", "Cumplimiento con TI", "Oficina de Cumplimiento con los dueños de cada proceso"]},
 {"id": "A04", "n": "Contratos con encargados (proveedores que tratan datos)", "base": "LOPDP art. 47 nums. 10 y 11; RGLOPDP art. 41; Res. SPDP-SPD-2025-0006-R", "herr": "08",
  "ent": "Contratos o adendas firmados con nómina, contabilidad, nube, mensajería, marketing",
  "dep": ["Gerente propietario", "Administración", "Compras con Legal", "Abastecimiento con Legal"]},
 {"id": "A05", "n": "Acuerdos de confidencialidad del personal", "base": "LOPDP art. 47 num. 10", "herr": "08",
  "ent": "Cláusula o acuerdo firmado por cada persona que conoce datos personales",
  "dep": ["Gerente propietario", "Talento humano o Administración", "Talento humano", "Talento humano"]},
 {"id": "A06", "n": "Formularios de consentimiento cuando esa es la base", "base": "LOPDP arts. 7 y 8; RGLOPDP arts. 5 y 6", "herr": "08",
  "ent": "Consentimiento libre, específico, informado e inequívoco, demostrable y revocable",
  "dep": ["Gerente propietario", "Área comercial", "Marketing", "Marketing y Canales digitales"]},
 {"id": "A07", "n": "Canal y registro de solicitudes de derechos", "base": "LOPDP arts. 13 a 16; RGLOPDP arts. 12 a 15", "herr": "SOL",
  "ent": "Canal publicado, responsable interno, registro y respuesta en 15 días",
  "dep": ["Gerente propietario", "Atención al cliente", "Servicio al cliente con Legal", "Servicio al cliente con la Oficina de privacidad"]},
 {"id": "A08", "n": "Análisis de riesgos y medidas de seguridad", "base": "LOPDP art. 47 nums. 5, 6 y 7", "herr": "07",
  "ent": "Matriz de riesgos justificada y plan de medidas con responsables y plazos",
  "dep": ["Proveedor de TI externo", "Encargado o proveedor de TI", "Tecnología de la información", "Seguridad de la información (CISO)"]},
 {"id": "A09", "n": "Protocolo de respuesta a vulneraciones", "base": "LOPDP arts. 43, 46 y 47 num. 8; Res. SPDP-SPD-2026-0040-R", "herr": "09",
  "ent": "Protocolo aprobado, bitácora de incidentes y acceso al SISPDP",
  "dep": ["Gerente propietario con proveedor de TI", "Administración con TI", "TI con Legal", "Comité de incidentes (Seguridad, Legal y Comunicación)"]},
 {"id": "A10", "n": "Protección de datos desde el diseño y por defecto", "base": "LOPDP art. 47 num. 9; Res. SPDP-SPD-2025-0040-R", "herr": "07",
  "ent": "Revisión de privacidad en proyectos y sistemas nuevos; configuración mínima por defecto",
  "dep": ["Gerente propietario", "Encargado de TI", "TI y Proyectos", "Desarrollo y Proyectos con Seguridad"]},
 {"id": "A11", "n": "Evaluación periódica de la eficacia de las medidas", "base": "LOPDP art. 47 num. 3", "herr": "03",
  "ent": "Diagnóstico anual y seguimiento del plan de acción",
  "dep": ["Gerente propietario", "Gerencia", "Cumplimiento", "Auditoría interna y Cumplimiento"]},
 {"id": "A12", "n": "Designación del delegado de protección de datos", "base": "LOPDP arts. 47 num. 13 y 48; Res. SPDP-SPD-2025-0028-R", "herr": "05", "regla": "dpd",
  "ent": "Nombramiento y su registro ante la SPDP, o análisis documentado de por qué no es obligatorio",
  "dep": ["Gerente propietario", "Gerencia general", "Gerencia general", "Directorio o Gerencia general"]},
 {"id": "A13", "n": "Inscripción en el Registro Nacional de Protección de Datos", "base": "LOPDP art. 47 num. 12", "herr": "", "regla": "reg",
  "ent": "Inscripción y actualización cuando la SPDP habilite el registro",
  "dep": ["Gerente propietario", "Administración", "Legal", "Oficina de Cumplimiento"]},
 {"id": "A14", "n": "Capacitación del personal", "base": "Buena práctica (criterio propio); apoya LOPDP art. 47 num. 2", "herr": "",
  "ent": "Capacitación inicial y anual con registro de asistencia",
  "dep": ["Gerente propietario", "Talento humano o Administración", "Talento humano", "Talento humano con Cumplimiento"]},
]

# Clasificación por tamaño: E = esencial, R = recomendada, C = según el caso. [micro, pequeña, mediana, grande, motivo]
CLASIF = {
 "03": ["E", "E", "E", "E", "Toda empresa: mide el punto de partida y fundamenta el plan."],
 "A12": ["E", "E", "E", "E", "Toda empresa que recoge datos debe informar al titular (LOPDP art. 12)."],
 "05": ["C", "C", "R", "E", "Calificación directa sin importar el tamaño en salud, biometría, geolocalización, crédito, videovigilancia de espacios públicos, menores o courier (Res. 2026-0005 art. 14)."],
 "06": ["C", "C", "C", "C", "Solo si un tratamiento se basa en el interés legítimo (mercadotecnia, videovigilancia, fraude); solo sector privado."],
 "07": ["C", "C", "C", "R", "Obligatoria ante los supuestos del art. 42 LOPDP, biometría o gran escala; más frecuente en empresas grandes."],
 "IMP": ["E", "E", "E", "E", "Toda empresa: hoja de ruta de lo que debe implementar y su verificación."],
 "04": ["C", "C", "E", "E", "Obligatorio con 100 o más trabajadores, o con menos si hay riesgo, tratamiento no ocasional o categorías especiales (RGLOPDP art. 38)."],
 "08": ["E", "E", "E", "E", "Toda empresa necesita política, avisos, contratos de encargo y confidencialidad."],
 "09": ["E", "E", "E", "E", "Toda empresa debe poder notificar una vulneración en 5 días (LOPDP art. 43)."],
}
# Sectores que elevan la gran escala y el DPD a esencial (Res. 2026-0005 art. 14; Res. 2025-0028 art. 10)
SECTORES_ALTO = r"salud|cl[ií]nic|laborator|financ|banc|cooperativ|seguro|educa|escuela|colegio|unidad educativa|seguridad privada|vigilancia|courier|mensajer|telecom|internet|farmac"
