"""Fuente única de la Herramienta 05: Nivel de madurez en protección de datos personales.

MODELO PROPIO de Macías Sánchez Consultores. La SPDP no ha emitido un modelo de madurez:
los dominios se ordenan por las obligaciones de la LOPDP, su Reglamento y la normativa SPDP
citada en BASE-LEGAL.md. Las escalas y ponderaciones son criterio del portafolio.
"""

ESCALA = [
    (0, "No existe", "No hay nada al respecto."),
    (1, "Inicial", "Se hace de manera informal o aislada, sin documento."),
    (2, "En desarrollo", "Existe un documento o práctica, pero incompleto o sin aplicar en toda la organización."),
    (3, "Implementado", "Documentado, aprobado y aplicado; hay evidencia."),
    (4, "Gestionado", "Implementado, con responsables, indicadores y revisión periódica."),
]

NIVELES = [  # rango del promedio (0-4)
    (0.0, 0.99, "Inexistente", "La organización no ha iniciado su adecuación. Exposición alta a sanciones."),
    (1.0, 1.99, "Inicial", "Hay acciones aisladas. Faltan los documentos básicos exigidos por la LOPDP."),
    (2.0, 2.79, "En desarrollo", "Existen documentos clave, pero incompletos o sin aplicación sistemática."),
    (2.8, 3.49, "Implementado", "El cumplimiento está documentado y aplicado; falta medir y mejorar."),
    (3.5, 4.0, "Gestionado", "Cumplimiento sostenido, medido y revisado: responsabilidad proactiva demostrable."),
]

# Dominios: id, nombre, base (debe constar en BASE-LEGAL.md), herramienta del portafolio que ayuda a cerrar la brecha,
# peso (1 = normal, 2 = crítico por exposición sancionatoria), preguntas (texto, evidencia sugerida)
DOMINIOS = [
    {"id": "gob", "corto": "Gobierno", "nombre": "Gobierno y responsabilidad proactiva", "peso": 1,
     "base": "LOPDP art. 47 (obligaciones del responsable)", "herramienta": "Esta evaluación (plan de acción)",
     "preguntas": [
         ("La alta dirección aprobó formalmente una política interna de protección de datos.", "Política firmada o acta de aprobación"),
         ("Hay roles y responsables definidos para la protección de datos en cada área.", "Organigrama o matriz de responsabilidades"),
         ("Existe presupuesto o recursos asignados al cumplimiento.", "Presupuesto o plan anual"),
         ("La dirección recibe reportes periódicos del estado de cumplimiento.", "Informes o actas"),
     ]},
    {"id": "dpd", "corto": "DPD", "nombre": "Delegado de Protección de Datos", "peso": 2,
     "base": "LOPDP arts. 47 num. 13, 48 y 68; Res. SPDP-SPD-2025-0028-R", "herramienta": "02 · Designación del DPD",
     "preguntas": [
         ("Se analizó si la organización está obligada a designar DPD (causales del art. 10 de la Res. 0028).", "Informe de análisis"),
         ("Si corresponde, el DPD está designado y registrado ante la SPDP.", "Nombramiento y constancia de registro"),
         ("El DPD actúa con independencia y tiene acceso a la información y a la dirección.", "Funciones documentadas"),
     ]},
    {"id": "rat", "corto": "RAT", "nombre": "Registro de actividades de tratamiento", "peso": 2,
     "base": "RGLOPDP arts. 38, 39 y 44; LOPDP art. 51", "herramienta": "01 · Registro de actividades de tratamiento",
     "preguntas": [
         ("Existe un RAT con el contenido mínimo del art. 38 RGLOPDP para todas las actividades.", "RAT vigente"),
         ("El RAT se actualiza ante cambios (proveedores, sistemas, finalidades) y se revisa periódicamente.", "Fechas de revisión y motivo de actualización"),
         ("Las bases de datos se inscribieron en el Registro Nacional de Protección de Datos Personales.", "Constancia de inscripción"),
     ]},
    {"id": "lic", "corto": "Licitud", "nombre": "Licitud y bases legitimadoras", "peso": 2,
     "base": "LOPDP arts. 7 y 26; Res. SPDP-SPD-2025-0041-R", "herramienta": "01 · RAT (base legitimadora) y 02 · Cláusulas de consentimiento",
     "preguntas": [
         ("Cada actividad tiene identificada su base legitimadora.", "Columna de base en el RAT"),
         ("Los consentimientos son específicos, informados, verificables y revocables.", "Formularios y registro de consentimientos"),
         ("Si se usa interés legítimo, existe la evaluación de ponderación documentada.", "Evaluación de ponderación"),
         ("Los datos sensibles se tratan solo bajo una excepción del art. 26 LOPDP.", "Análisis por actividad"),
     ]},
    {"id": "tra", "corto": "Transparencia", "nombre": "Transparencia e información al titular", "peso": 1,
     "base": "LOPDP art. 12", "herramienta": "02 · Política y avisos de privacidad",
     "preguntas": [
         ("Existe una política de privacidad publicada con los contenidos del art. 12 LOPDP.", "Política publicada"),
         ("Cada punto de recolección (formularios, cámaras, web) tiene su aviso de privacidad.", "Avisos y letreros"),
         ("Los trabajadores reciben información sobre el tratamiento de sus datos.", "Aviso interno o cláusula contractual"),
     ]},
    {"id": "der", "corto": "Derechos", "nombre": "Derechos de los titulares", "peso": 1,
     "base": "LOPDP art. 12 y derechos del titular", "herramienta": "02 · Política de privacidad (canal de derechos)",
     "preguntas": [
         ("Existe un canal y un procedimiento escrito para atender solicitudes de derechos.", "Procedimiento y correo de atención"),
         ("Las solicitudes se registran y se responden dentro del plazo legal.", "Registro de solicitudes"),
         ("El personal que recibe solicitudes sabe a quién derivarlas.", "Capacitación o instructivo"),
     ]},
    {"id": "enc", "corto": "Encargados", "nombre": "Encargados y terceros", "peso": 2,
     "base": "RGLOPDP art. 41; LOPDP art. 68 num. 9; Res. SPDP-SPD-2025-0006-R", "herramienta": "02 · Contrato de encargo",
     "preguntas": [
         ("Existe un inventario de proveedores que tratan datos por cuenta de la organización.", "Lista de encargados"),
         ("Todos los encargados tienen contrato con el contenido del art. 41 RGLOPDP.", "Contratos firmados"),
         ("Se verifica periódicamente que los encargados cumplan sus obligaciones.", "Auditorías o certificaciones"),
     ]},
    {"id": "seg", "corto": "Seguridad", "nombre": "Seguridad y gestión de riesgos", "peso": 2,
     "base": "LOPDP art. 40; Res. SPDP-SPD-2025-0003-R", "herramienta": "04 · Evaluación de impacto (matriz de riesgos)",
     "preguntas": [
         ("Existe un análisis de riesgos de los tratamientos con una metodología documentada.", "Matriz de riesgos"),
         ("Hay controles de acceso por perfil y mínimo privilegio.", "Política de accesos"),
         ("Hay respaldos periódicos y probados.", "Registro de pruebas de restauración"),
         ("Los datos sensibles o críticos están cifrados.", "Configuración documentada"),
     ]},
    {"id": "eipd", "corto": "Evaluación de impacto", "nombre": "Evaluación de impacto y privacidad desde el diseño", "peso": 1,
     "base": "LOPDP art. 42; RGLOPDP arts. 29 a 32", "herramienta": "04 · Evaluación de impacto",
     "preguntas": [
         ("Se identifica qué tratamientos requieren evaluación de impacto.", "Columna en el RAT o análisis"),
         ("Las evaluaciones obligatorias se hacen antes de iniciar el tratamiento.", "Informes de evaluación"),
         ("Los proyectos nuevos consideran la protección de datos desde su diseño.", "Lista de verificación de proyectos"),
     ]},
    {"id": "vul", "corto": "Vulneraciones", "nombre": "Gestión de vulneraciones", "peso": 2,
     "base": "LOPDP art. 43; RGLOPDP arts. 24 a 28; Res. SPDP-SPD-2026-0040-R", "herramienta": "03 · Kit de vulneraciones",
     "preguntas": [
         ("Existe un protocolo aprobado de respuesta a vulneraciones.", "Protocolo"),
         ("El personal sabe cómo reportar internamente un incidente.", "Canal interno y capacitación"),
         ("Existe una bitácora de incidentes, se notifiquen o no.", "Bitácora"),
         ("La organización conoce los plazos y el canal (SISPDP) para notificar a la SPDP.", "Protocolo con plazos"),
     ]},
    {"id": "tri", "corto": "Transferencias", "nombre": "Transferencias internacionales", "peso": 1,
     "base": "LOPDP (régimen de transferencias internacionales); RGLOPDP art. 38 num. 6", "herramienta": "01 · RAT (transferencias)",
     "preguntas": [
         ("Se identificaron los servicios que alojan o envían datos fuera del Ecuador (nube, correo, CRM).", "Inventario de servicios"),
         ("Cada transferencia tiene una garantía documentada.", "Cláusulas o evaluación de la transferencia"),
     ]},
    {"id": "cul", "corto": "Cultura", "nombre": "Capacitación y cultura", "peso": 1,
     "base": "RGLOPDP art. 30 num. 4 (cultura preventiva)", "herramienta": "Plan de capacitación",
     "preguntas": [
         ("El personal recibe capacitación en protección de datos al ingresar y periódicamente.", "Registro de asistencia"),
         ("El personal firma compromisos de confidencialidad.", "Acuerdos firmados"),
         ("Se miden los resultados de la capacitación.", "Evaluaciones o indicadores"),
     ]},
]

CONTEXTO = [
    ("ctx_emp", "Organización evaluada", "texto"),
    ("ctx_sector", "Sector", "lista", ["Comercio", "Servicios profesionales", "Salud", "Educación", "Financiero o seguros",
                                       "Tecnología", "Industria", "Construcción", "Seguridad privada", "Sector público", "Otro"]),
    ("ctx_trab", "Número de trabajadores", "lista", ["1 a 9", "10 a 49", "50 a 99", "100 a 199", "200 o más"]),
    ("ctx_fecha", "Fecha de la evaluación", "fecha"),
    ("ctx_entrev", "Personas entrevistadas", "texto"),
]
