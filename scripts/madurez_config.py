"""Fuente única de la Herramienta 03: Nivel de madurez en protección de datos personales.

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
     "base": "LOPDP arts. 10 lit. k y 47", "herramienta": "Esta evaluación (plan de acción), 08 · Política interna y 08 · Plan e informe de supervisión",
     "preguntas": [
         ("La alta dirección aprobó formalmente una política interna de protección de datos.", "Política firmada o acta de aprobación"),
         ("Hay roles y responsables definidos para la protección de datos en cada área.", "Organigrama o matriz de responsabilidades"),
         ("Existe presupuesto o recursos asignados al cumplimiento.", "Presupuesto o plan anual"),
         ("La dirección recibe reportes periódicos del estado de cumplimiento.", "Informes o actas"),
     ]},
    {"id": "dpd", "corto": "DPD", "nombre": "Delegado de Protección de Datos", "peso": 2,
     "base": "LOPDP arts. 47 num. 13, 48 y 68; Res. SPDP-SPD-2025-0028-R", "herramienta": "08 · Designación del DPD",
     "preguntas": [
         ("Se analizó si la organización está obligada a designar DPD (causales del art. 10 de la Res. 0028).", "Informe de análisis"),
         ("Si corresponde, el DPD está designado y registrado ante la SPDP.", "Nombramiento y constancia de registro"),
         ("El DPD actúa con independencia y tiene acceso a la información y a la dirección.", "Funciones documentadas"),
     ]},
    {"id": "rat", "corto": "RAT", "nombre": "Registro de actividades de tratamiento", "peso": 2,
     "base": "RGLOPDP arts. 38, 39 y 44; LOPDP art. 51", "herramienta": "04 · Registro de actividades de tratamiento",
     "preguntas": [
         ("Existe un RAT con el contenido mínimo del art. 38 RGLOPDP para todas las actividades.", "RAT vigente"),
         ("El RAT se actualiza ante cambios (proveedores, sistemas, finalidades) y se revisa periódicamente.", "Fechas de revisión y motivo de actualización"),
         ("Las bases de datos se inscribieron en el Registro Nacional de Protección de Datos Personales.", "Constancia de inscripción"),
     ]},
    {"id": "lic", "corto": "Licitud", "nombre": "Licitud y bases legitimadoras", "peso": 2,
     "base": "LOPDP arts. 7 y 26; Res. SPDP-SPD-2025-0041-R", "herramienta": "04 · RAT (base legitimadora), 06 · Interés legítimo y 08 · Cláusulas",
     "preguntas": [
         ("Cada actividad tiene identificada su base legitimadora.", "Columna de base en el RAT"),
         ("Los consentimientos son específicos, informados, verificables y revocables.", "Formularios y registro de consentimientos"),
         ("Si se usa interés legítimo, existe la evaluación de ponderación documentada.", "Evaluación de ponderación"),
         ("Los datos sensibles se tratan solo bajo una excepción del art. 26 LOPDP.", "Análisis por actividad"),
     ]},
    {"id": "tra", "corto": "Transparencia", "nombre": "Transparencia e información al titular", "peso": 1,
     "base": "LOPDP art. 12", "herramienta": "08 · Política y avisos de privacidad",
     "preguntas": [
         ("Existe una política de privacidad publicada con los contenidos del art. 12 LOPDP.", "Política publicada"),
         ("Cada punto de recolección (formularios, cámaras, web) tiene su aviso de privacidad.", "Avisos y letreros"),
         ("Los trabajadores reciben información sobre el tratamiento de sus datos.", "Aviso interno o cláusula contractual"),
     ]},
    {"id": "der", "corto": "Derechos", "nombre": "Derechos de los titulares", "peso": 1,
     "base": "LOPDP arts. 12 a 20 y 67 num. 1; RGLOPDP arts. 12 a 15", "herramienta": "08 · Formulario y procedimiento de derechos",
     "preguntas": [
         ("Existe un canal y un procedimiento escrito para atender solicitudes de derechos.", "Procedimiento y correo de atención"),
         ("Las solicitudes se registran y se responden dentro del plazo legal (15 días para acceso, rectificación, eliminación y oposición).", "Registro de solicitudes con fechas de recepción y respuesta"),
         ("El personal que recibe solicitudes sabe a quién derivarlas.", "Capacitación o instructivo"),
     ]},
    {"id": "enc", "corto": "Encargados", "nombre": "Encargados y terceros", "peso": 2,
     "base": "RGLOPDP art. 41; LOPDP art. 68 num. 9; Res. SPDP-SPD-2025-0006-R", "herramienta": "08 · Contrato de encargo",
     "preguntas": [
         ("Existe un inventario de proveedores que tratan datos por cuenta de la organización.", "Lista de encargados"),
         ("Todos los encargados tienen contrato con el contenido del art. 41 RGLOPDP.", "Contratos firmados"),
         ("Se verifica periódicamente que los encargados cumplan sus obligaciones.", "Auditorías o certificaciones"),
     ]},
    {"id": "seg", "corto": "Seguridad", "nombre": "Seguridad y gestión de riesgos", "peso": 2,
     "base": "LOPDP art. 40; Res. SPDP-SPD-2026-0012-R", "herramienta": "07 · Evaluación de impacto (matriz de riesgos) y 08 · Registro de medidas de seguridad",
     "preguntas": [
         ("Existe un análisis de riesgos de los tratamientos con una metodología documentada.", "Matriz de riesgos"),
         ("Hay controles de acceso por perfil y mínimo privilegio.", "Política de accesos"),
         ("Hay respaldos periódicos y probados.", "Registro de pruebas de restauración"),
         ("Los datos sensibles o críticos están cifrados.", "Configuración documentada"),
     ]},
    {"id": "eipd", "corto": "Evaluación de impacto", "nombre": "Evaluación de impacto y privacidad desde el diseño", "peso": 1,
     "base": "LOPDP art. 42; RGLOPDP arts. 29 a 32", "herramienta": "07 · Evaluación de impacto y 08 · Evaluación de diseño y por defecto",
     "preguntas": [
         ("Se identifica qué tratamientos requieren evaluación de impacto.", "Columna en el RAT o análisis"),
         ("Las evaluaciones obligatorias se hacen antes de iniciar el tratamiento.", "Informes de evaluación"),
         ("Los proyectos nuevos consideran la protección de datos desde su diseño.", "Lista de verificación de proyectos"),
     ]},
    {"id": "vul", "corto": "Vulneraciones", "nombre": "Gestión de vulneraciones", "peso": 2,
     "base": "LOPDP art. 43; RGLOPDP arts. 24 a 28; Res. SPDP-SPD-2026-0040-R", "herramienta": "09 · Kit de vulneraciones",
     "preguntas": [
         ("Existe un protocolo aprobado de respuesta a vulneraciones.", "Protocolo"),
         ("El personal sabe cómo reportar internamente un incidente.", "Canal interno y capacitación"),
         ("Existe una bitácora de incidentes, se notifiquen o no.", "Bitácora"),
         ("La organización conoce los términos (5 días a la SPDP, al regulador y al CSIRT; 3 días a los titulares; 2 días del encargado) y el canal (SISPDP).", "Protocolo con plazos y responsables"),
     ]},
    {"id": "tri", "corto": "Transferencias", "nombre": "Transferencias internacionales", "peso": 1,
     "base": "LOPDP art. 56; Res. SPDP-SPD-2026-0004-R; RGLOPDP art. 38 num. 6", "herramienta": "04 · RAT (transferencias)",
     "preguntas": [
         ("Se identificaron los servicios que alojan o envían datos fuera del Ecuador (nube, correo, CRM).", "Inventario de servicios"),
         ("Cada transferencia tiene una garantía documentada.", "Cláusulas o evaluación de la transferencia"),
     ]},
    {"id": "cul", "corto": "Cultura", "nombre": "Capacitación y cultura", "peso": 1,
     "base": "RGLOPDP art. 30 num. 4 (cultura preventiva)", "herramienta": "08 · Plan de capacitación",
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


# ---------------------------------------------------------------------------
# Impacto económico: estimación de la multa (modelo MPRIV-1, Res. SPDP-SPD-2025-0022-R)
# ---------------------------------------------------------------------------
# Fórmulas publicadas (resumen de Corral Rosales, 23-07-2025; el Anexo I oficial no se pudo leer):
#   CDI = VDN x RDMmin + (PDI/100) x VDN x (RDMmax - RDMmin)
#   SDI = 2 (IED + INT + RER), cada factor por PERT = (mín + 4 x más probable + máx) / 6
#   Multa = CDI x SDI, acotada al mínimo y máximo de la LOPDP
# INTERPRETACIÓN DEL PORTAFOLIO (rotular siempre así):
#   - PDI: el reglamento lo describe como el grado de madurez en el cumplimiento y de las medidas
#     correctivas, en escala 0-100 %. Como un PDI mayor acerca la multa al máximo, se toma
#     PDI = (1 - índice de madurez / 4) x 100: a menor madurez, mayor multa.
#   - Pesos publicados (IED 60 %, INT 40 %, RER 20 % opcional) aplicados como
#     SDI = 2 (0,6 IED + 0,4 INT + 0,2 RER), con factores en escala 0 a 1. Con IED = INT = 0,5
#     y sin reincidencia, SDI = 1 (no altera la categoría).
MULTAS = {
    "rdm": {"Leve": (0.001, 0.007), "Grave": (0.007, 0.010)},  # LOPDP arts. 71 y 72
    "pesos": {"IED": 0.6, "INT": 0.4, "RER": 0.2},
    # Opciones con su terna PERT (mínimo, más probable, máximo) en escala 0-1: criterio propio
    "IED": [
        ("Baja", "Datos comunes, pocos titulares, sin grupos vulnerables, vulneración reversible", (0.1, 0.2, 0.4)),
        ("Media", "Algún dato sensible o financiero, cientos de titulares, efectos superables", (0.3, 0.5, 0.7)),
        ("Alta", "Categorías especiales o NNA, miles de titulares, efectos graves o irreversibles", (0.6, 0.8, 1.0)),
    ],
    "INT": [
        ("Negligencia leve", "Descuido puntual; la organización desconocía la obligación pero actuó de buena fe", (0.1, 0.3, 0.5)),
        ("Negligencia grave", "La obligación era conocida o fácilmente cognoscible y no se adoptaron medidas", (0.4, 0.6, 0.8)),
        ("Intencional", "Se conocía el incumplimiento y se mantuvo deliberadamente", (0.7, 0.9, 1.0)),
    ],
    "RER": [
        ("Ninguna", "Sin sanciones previas", (0.0, 0.0, 0.0)),
        ("Reiteración", "Sancionada antes por dos o más leves, o por una de igual o mayor gravedad de otra naturaleza", (0.3, 0.5, 0.7)),
        ("Reincidencia", "Sancionada antes por una infracción de la misma naturaleza", (0.6, 0.8, 1.0)),
    ],
    # Probabilidad anual orientativa de una sanción según el nivel de madurez: criterio propio, editable
    "prob_por_nivel": [0.40, 0.25, 0.15, 0.08, 0.04],
    "indice_objetivo": 3.0,  # escenario "con plan de acción": nivel Implementado
}

# Dominios cuyo incumplimiento está calificado como infracción GRAVE en las fuentes del portafolio.
# Solo se listan los verificados (ver BASE-LEGAL.md); el resto queda a criterio del evaluador.
INFRACCION_GRAVE = {
    "dpd": "No designar al DPD cuando corresponde (LOPDP art. 68 num. 12)",
    "enc": "No suscribir contratos con cláusulas de confidencialidad y tratamiento adecuado con el encargado y el personal (LOPDP art. 68 num. 9)",
    "seg": "No implementar medidas de seguridad ni usar una metodología de análisis y gestión de riesgos (LOPDP art. 68 nums. 1, 4 y 6)",
    "eipd": "No realizar la evaluación de impacto cuando es obligatoria (LOPDP art. 68 num. 5)",
    "vul": "No notificar una vulneración a la SPDP o a los titulares (LOPDP art. 68 nums. 7 y 8)",
}
# Infracciones leves del responsable (LOPDP art. 67), para orientar al evaluador en los demás dominios:
# num. 1 no tramitar o negar solicitudes de titulares; num. 2 no aplicar diseño y por defecto; num. 3 no mantener
# disponibles las políticas; num. 4 elegir un encargado sin garantías; num. 5 incumplir medidas correctivas.
