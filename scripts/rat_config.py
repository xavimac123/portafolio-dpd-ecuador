"""Fuente única de listas, preguntas y ayudas del RAT.

La usan generar_rat.py (Excel) y generar_asistente_rat.py (web).
Para incorporar el texto LITERAL de una norma, reemplaza el valor de "norma"
y cambia "literal" a True: la interfaz dejará de rotularlo como resumen.
"""

OTRO = "Otro"

# tipo: "uno" = una opción + Otro; "varios" = selección múltiple + Otro
LISTAS = {
    "actividad": {"tipo": "uno", "opciones": [
        "Gestión de nómina y personal", "Selección de personal", "Control de asistencia (reloj o biométrico)",
        "Seguridad y salud ocupacional", "Gestión de clientes y facturación", "Atención al cliente y reclamos",
        "Cobranza", "Marketing y publicidad", "Sitio web y formularios de contacto", "Redes sociales",
        "Videovigilancia", "Control de acceso de visitantes", "Gestión de proveedores",
        "Atención de salud / historias clínicas", "Gestión académica de estudiantes",
    ]},
    "area": {"tipo": "uno", "opciones": [
        "Gerencia", "Talento Humano", "Contabilidad y Finanzas", "Comercial / Ventas", "Marketing",
        "Atención al cliente", "Tecnología (TI)", "Seguridad física", "Legal", "Operaciones",
        "Dirección médica", "Dirección académica",
    ]},
    "finalidad": {"tipo": "varios", "opciones": [
        "Cumplir obligaciones laborales y de seguridad social", "Cumplir obligaciones tributarias",
        "Ejecutar el contrato o prestar el servicio", "Gestionar cobros y pagos", "Atender solicitudes y reclamos",
        "Enviar publicidad y promociones", "Seguridad de personas e instalaciones", "Seleccionar personal",
        "Controlar la asistencia", "Atender requerimientos de autoridades", "Elaborar estadísticas internas",
    ]},
    "titulares": {"tipo": "varios", "opciones": [
        "Trabajadores", "Ex trabajadores", "Postulantes", "Cargas familiares de trabajadores", "Clientes",
        "Potenciales clientes", "Usuarios del sitio web", "Proveedores (personas naturales)",
        "Contactos de empresas proveedoras", "Visitantes", "Pacientes", "Estudiantes", "Representantes legales",
    ]},
    "datos": {"tipo": "varios", "opciones": [
        "Identificación (nombre, cédula)", "Contacto (teléfono, correo, dirección)", "Financieros y bancarios",
        "Laborales (cargo, remuneración)", "Académicos", "Imagen o video", "Navegación y cookies",
        "Geolocalización", "Firma",
        "Salud", "Biométricos (huella, rostro)", "Niñas, niños y adolescentes", "Discapacidad",
        "Pasado judicial", "Etnia, religión, ideología u orientación sexual", "Condición migratoria", "Genéticos",
    ],
     # opciones que activan "categorías especiales" (LOPDP arts. 4 y 25)
     "especiales": ["Salud", "Biométricos (huella, rostro)", "Niñas, niños y adolescentes", "Discapacidad",
                    "Pasado judicial", "Etnia, religión, ideología u orientación sexual", "Condición migratoria",
                    "Genéticos"],
     # subconjunto de datos sensibles (art. 4 LOPDP): su tratamiento requiere una excepción del art. 26
     "sensibles": ["Salud", "Biométricos (huella, rostro)", "Pasado judicial",
                   "Etnia, religión, ideología u orientación sexual", "Condición migratoria", "Genéticos"],
     "nna": ["Niñas, niños y adolescentes"]},
    "origen": {"tipo": "uno", "opciones": [
        "Del propio titular", "De terceros (otra empresa o persona)", "De fuentes de acceso público",
        "Generados por la organización", "Captación automática (cámaras, sitio web)",
    ]},
    "dest": {"tipo": "varios", "opciones": [
        "Ninguno", "IESS", "SRI", "Ministerio del Trabajo", "Entidades bancarias", "Aseguradoras",
        "Auditores externos", "Autoridades judiciales o policiales (por requerimiento)",
        "Empresas del mismo grupo", "Superintendencia de Compañías",
    ]},
    "enc": {"tipo": "varios", "opciones": [
        "Ninguno", "Proveedor de nube u hosting", "Software contable o de nómina", "Contador o estudio contable externo",
        "Empresa de seguridad", "Plataforma de correo masivo o mensajería", "Agencia de publicidad",
        "Soporte técnico de TI", "Courier o mensajería física",
    ]},
    "tgar": {"tipo": "uno", "opciones": [
        "Cláusulas contractuales con el receptor", "País con nivel adecuado según la SPDP",
        "Consentimiento del titular para la transferencia",
    ]},
    "plazo": {"tipo": "uno", "opciones": [
        "Durante la relación contractual y luego el plazo legal aplicable (indicar norma)",
        "Plazo fijado por la normativa tributaria (indicar)", "Plazo fijado por la normativa laboral o de seguridad social (indicar)",
        "Hasta que el titular revoque su consentimiento", "Plazo corto fijado internamente (indicar días) salvo incidente",
    ]},
    "medidas": {"tipo": "varios", "opciones": [
        "Usuario y contraseña", "Perfiles de acceso por rol", "Cifrado de información", "Respaldos periódicos",
        "Antivirus y actualizaciones", "Acuerdos de confidencialidad con el personal",
        "Contratos de encargo con proveedores", "Capacitación al personal", "Archivo físico bajo llave",
        "Bitácora de accesos", "Procedimiento de atención de derechos",
    ]},
    "sistemas": {"tipo": "varios", "opciones": [
        "Software contable o ERP", "Software de nómina", "Hojas de cálculo", "Correo electrónico",
        "Almacenamiento en la nube (Drive, OneDrive)", "CRM o sistema de ventas", "Sistema clínico o académico",
        "Sitio web y formularios", "WhatsApp o mensajería", "Grabador de cámaras (DVR/NVR)", "Reloj biométrico",
        "Archivo físico",
    ]},
    "macro": {"tipo": "uno", "opciones": [
        "Gestión de personas", "Clientes y ventas", "Servicio principal (salud, educación, etc.)", "Proveedores y compras",
        "Marketing y comunicación", "Finanzas y cobranza", "Seguridad física", "Tecnología y sistemas", "Legal y cumplimiento",
    ]},
    "evento": {"tipo": "uno", "opciones": [
        "Levantamiento inicial", "Revisión periódica", "Nuevo proveedor o encargado", "Cambio de finalidad",
        "Nuevo sistema o herramienta", "Nueva categoría de datos o de titulares", "Nueva transferencia internacional",
        "Inicio de perfiles o decisiones automatizadas", "Vencimiento del plazo de conservación",
        "Vulneración de la seguridad", "Cambio normativo o requerimiento de la SPDP", "Fusión, adquisición o reorganización",
    ]},
    "volumen": {"tipo": "uno", "opciones": [
        "Menos de 100", "De 100 a 1.000", "De 1.001 a 10.000", "Más de 10.000",
    ]},
    "info": {"tipo": "uno", "opciones": [
        "Aviso de privacidad en el formulario o punto de recogida", "Cláusula en el contrato",
        "Política de privacidad publicada", "Cartel informativo (videovigilancia)",
        "Comunicación interna al personal", "No se informa aún",
    ]},
}

# Finalidades demasiado genéricas si aparecen solas: conviene describir el servicio concreto.
FINALIDADES_GENERICAS = ["Ejecutar el contrato o prestar el servicio", "Elaborar estadísticas internas"]
# Finalidad que casi siempre tiene una base distinta del resto: si se combina con otra, sugerir separar.
FINALIDAD_SEPARABLE = "Enviar publicidad y promociones"

# Práctica interna (no fijada por la norma): meses entre revisiones del RAT.
REVISION_MESES = 12

# ---------------------------------------------------------------------------
# Campos del registro. Fuente única para el Excel y el asistente web.
# tipo: lista (usa LISTAS[clave]) · base · sino · opc (opciones propias) · texto · fecha · auto
# min: numeral del art. 38 RGLOPDP si forma parte del contenido mínimo; None = buena práctica
# si: condición para mostrar el campo en el asistente web
# ---------------------------------------------------------------------------
SECCIONES = {
    "ident": "1 · Identificación de la actividad",
    "fin": "2 · Finalidad y legitimación",
    "datos": "3 · Titulares y datos",
    "com": "4 · Comunicaciones, encargados y transferencias",
    "cons": "5 · Conservación, seguridad y sistemas",
    "riesgo": "6 · Riesgo y evaluación de impacto",
    "ctrl": "7 · Control del registro",
}

CAMPOS = [
    {"k": "id", "h": "ID", "sec": "ident", "tipo": "texto", "w": 7, "min": None, "nota": "Código interno, ej. T-01"},
    {"k": "actividad", "h": "Actividad de tratamiento", "sec": "ident", "tipo": "lista", "w": 28, "min": None,
     "nota": "Nombre de la actividad, no de la base de datos ni del programa. Ej.: Nómina, Videovigilancia."},
    {"k": "area", "h": "Área responsable", "sec": "ident", "tipo": "lista", "w": 16, "min": None, "nota": "Unidad interna a cargo"},
    {"k": "macro", "h": "Macroproceso", "sec": "ident", "tipo": "lista", "w": 18, "min": None,
     "nota": "Agrupa actividades afines (personas, clientes, proveedores...). Facilita el levantamiento por áreas y las vistas por proceso."},
    {"k": "entidad", "h": "Entidad o ámbito", "sec": "ident", "tipo": "texto", "w": 16, "min": None,
     "nota": "Sociedad, sucursal o unidad de negocio, si el registro abarca varias. Déjalo vacío si hay una sola."},
    {"k": "propietario", "h": "Responsable interno (cargo)", "sec": "ident", "tipo": "texto", "w": 18, "min": None,
     "nota": "Cargo que responde por la actividad y mantiene la fila al día. Ej.: Jefe de Talento Humano."},
    {"k": "descripcion", "h": "Descripción breve", "sec": "ident", "tipo": "texto", "w": 30, "min": None,
     "nota": "Qué se hace con los datos, en una o dos frases."},
    {"k": "finalidad", "h": "Finalidades", "sec": "fin", "tipo": "lista", "w": 34, "min": "2",
     "nota": "Para qué se tratan los datos. Concreta, no genérica. Si dos finalidades tienen bases distintas, sepáralas en dos actividades."},
    {"k": "base", "h": "Base legitimadora", "sec": "fin", "tipo": "base", "w": 26, "min": "7", "nota": "Art. 7 LOPDP"},
    {"k": "il", "h": "Ref. evaluación de interés legítimo", "sec": "fin", "tipo": "texto", "w": 20, "min": "7",
     "si": "base=Interés legítimo", "nota": "Obligatoria si la base es interés legítimo (Res. SPDP-SPD-2025-0041-R)"},
    {"k": "exc26", "h": "Excepción del art. 26 LOPDP (datos sensibles)", "sec": "fin", "tipo": "texto", "w": 24, "min": None,
     "si": "sensibles", "nota": "Si hay datos sensibles, indica cuál de las siete excepciones del art. 26 LOPDP permite tratarlos: a) consentimiento explícito con fines específicos; b) obligaciones y derechos laborales o de seguridad y protección social; c) interés vital cuando el titular no puede consentir; d) datos hechos manifiestamente públicos por el titular; e) orden de autoridad judicial; f) archivo de interés público, investigación científica o histórica, o estadística; g) datos de salud tratados conforme a la ley. El interés legítimo no sirve para datos sensibles (Res. SPDP-SPD-2025-0041-R art. 16.1)."},
    {"k": "info", "h": "Cómo se informa al titular", "sec": "fin", "tipo": "lista", "w": 24, "min": None,
     "nota": "Medio por el que se cumple el derecho a la información (art. 12 LOPDP)."},
    {"k": "titulares", "h": "Categorías de titulares", "sec": "datos", "tipo": "lista", "w": 22, "min": "4"},
    {"k": "volumen", "h": "Volumen aproximado de titulares", "sec": "datos", "tipo": "lista", "w": 14, "min": None,
     "nota": "Orienta la valoración de gran escala y de riesgo."},
    {"k": "datos", "h": "Categorías de datos personales", "sec": "datos", "tipo": "lista", "w": 30, "min": "4"},
    {"k": "especial", "h": "¿Categorías especiales?", "sec": "datos", "tipo": "sino", "w": 12, "min": None,
     "nota": "Sí si incluye datos sensibles, de salud, biométricos, de NNA o de discapacidad (art. 25 LOPDP)."},
    {"k": "nna", "h": "¿Datos de niñas, niños y adolescentes?", "sec": "datos", "tipo": "sino", "w": 14, "min": None},
    {"k": "origen", "h": "Origen de los datos", "sec": "datos", "tipo": "lista", "w": 20, "min": None},
    {"k": "dest", "h": "Categorías de destinatarios", "sec": "com", "tipo": "lista", "w": 26, "min": "3",
     "nota": "A quién se comunican. Si no hay, escribe Ninguno."},
    {"k": "enc", "h": "Encargados del tratamiento", "sec": "com", "tipo": "lista", "w": 24, "min": None,
     "nota": "Proveedores que tratan datos por cuenta del responsable."},
    {"k": "contrato", "h": "¿Contrato de encargo firmado?", "sec": "com", "tipo": "opc", "w": 14, "min": None,
     "ops": ["Sí, con todos", "Con algunos", "No"], "si": "encargados",
     "nota": "Contenido mínimo: art. 41 RGLOPDP. Su falta es infracción grave (art. 68 num. 9 LOPDP)."},
    {"k": "transf", "h": "¿Transferencia internacional?", "sec": "com", "tipo": "sino", "w": 13, "min": "6"},
    {"k": "pais", "h": "País de destino", "sec": "com", "tipo": "texto", "w": 16, "min": "6", "si": "transf=Sí"},
    {"k": "tgar", "h": "Garantía de la transferencia", "sec": "com", "tipo": "lista", "w": 22, "min": "6", "si": "transf=Sí"},
    {"k": "tia", "h": "Ref. evaluación de la transferencia", "sec": "com", "tipo": "texto", "w": 18, "min": None, "si": "transf=Sí",
     "nota": "Buena práctica: documento que analiza el país de destino y la garantía elegida."},
    {"k": "perfiles", "h": "¿Elaboración de perfiles o decisiones automatizadas?", "sec": "com", "tipo": "sino", "w": 14, "min": "5"},
    {"k": "plazo", "h": "Plazo de conservación / supresión", "sec": "cons", "tipo": "lista", "w": 24, "min": "8",
     "nota": "Plazo o criterio y su fundamento. Evita 'indefinido'."},
    {"k": "medidas", "h": "Medidas técnicas, jurídicas, administrativas y organizativas", "sec": "cons", "tipo": "lista",
     "w": 34, "min": "9", "nota": "Descripción general. No anotes contraseñas ni detalles que debiliten la seguridad."},
    {"k": "sistemas", "h": "Sistemas y soportes", "sec": "cons", "tipo": "lista", "w": 24, "min": None,
     "nota": "Dónde residen los datos. Indispensable para gestionar una vulneración (Herramienta 09)."},
    {"k": "riesgo", "h": "Nivel de riesgo (orientativo)", "sec": "riesgo", "tipo": "auto", "w": 12, "min": None,
     "nota": "Automático. Criterio interno, no normativo: ver README."},
    {"k": "eipd", "h": "¿Requiere evaluación de impacto?", "sec": "riesgo", "tipo": "opc", "w": 14, "min": None,
     "ops": ["Sí", "No", "Por analizar"], "nota": "Art. 42 LOPDP"},
    {"k": "eipdref", "h": "Ref. evaluación de impacto", "sec": "riesgo", "tipo": "texto", "w": 16, "min": None, "si": "eipd=Sí"},
    {"k": "alta", "h": "Fecha de alta", "sec": "ctrl", "tipo": "fecha", "w": 12, "min": None},
    {"k": "rev", "h": "Fecha de última revisión", "sec": "ctrl", "tipo": "fecha", "w": 12, "min": None},
    {"k": "evento", "h": "Motivo de la última actualización", "sec": "ctrl", "tipo": "lista", "w": 22, "min": None,
     "nota": "El RAT se actualiza ante cambios, no solo por calendario: deja constancia de qué la motivó."},
    {"k": "prox", "h": "Próxima revisión", "sec": "ctrl", "tipo": "auto", "w": 12, "min": None,
     "nota": "Automático: última revisión + %d meses (práctica interna)." % REVISION_MESES},
]

# Puntaje orientativo de riesgo (criterio interno del portafolio, no fijado por la norma).
# Alto >= 4 · Medio 2-3 · Bajo 0-1
RIESGO = {
    "especial": 2, "nna": 1, "perfiles": 2, "transf": 1,
    "volumen": {"De 1.001 a 10.000": 1, "Más de 10.000": 2},
    "datos": {"Financieros y bancarios": 1, "Geolocalización": 1},
    "umbral_alto": 4, "umbral_medio": 2,
}

# Catálogo de actividades típicas: punto de partida para el levantamiento.
# Son sugerencias que el usuario debe revisar; nunca se cargan sin su acción.
CATALOGO = [
    {"actividad": "Gestión de nómina y personal", "area": "Talento Humano",
     "finalidad": "Cumplir obligaciones laborales y de seguridad social; Cumplir obligaciones tributarias",
     "titulares": "Trabajadores; Cargas familiares de trabajadores",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Financieros y bancarios; Laborales (cargo, remuneración); Niñas, niños y adolescentes",
     "origen": "Del propio titular", "base": "Obligación legal",
     "dest": "IESS; SRI; Ministerio del Trabajo; Entidades bancarias", "enc": "Software contable o de nómina",
     "plazo": "Plazo fijado por la normativa laboral o de seguridad social (indicar)",
     "sistemas": "Software de nómina; Archivo físico", "info": "Comunicación interna al personal",
     "nota": "Las cargas familiares suelen ser menores de edad: son categoría especial."},
    {"actividad": "Selección de personal", "area": "Talento Humano", "finalidad": "Seleccionar personal",
     "titulares": "Postulantes", "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Académicos",
     "origen": "Del propio titular", "base": "Ejecución de contrato o medidas precontractuales", "dest": "Ninguno",
     "plazo": "Plazo corto fijado internamente (indicar días) salvo incidente",
     "info": "Aviso de privacidad en el formulario o punto de recogida",
     "nota": "Si se pide récord policial, es dato sensible (pasado judicial): justifica la necesidad y la excepción del art. 26. Conservar hojas de vida para futuras vacantes requiere otra base."},
    {"actividad": "Control de asistencia (reloj o biométrico)", "area": "Talento Humano", "finalidad": "Controlar la asistencia",
     "titulares": "Trabajadores", "datos": "Identificación (nombre, cédula); Biométricos (huella, rostro)",
     "origen": "Del propio titular", "sistemas": "Reloj biométrico", "info": "Comunicación interna al personal",
     "nota": "La huella o el rostro son datos sensibles. Analiza si un medio no biométrico (tarjeta, código) cumple la misma finalidad y documenta la excepción del art. 26."},
    {"actividad": "Gestión de clientes y facturación", "area": "Contabilidad y Finanzas",
     "finalidad": "Cumplir obligaciones tributarias; Gestionar cobros y pagos", "titulares": "Clientes",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Financieros y bancarios",
     "origen": "Del propio titular", "base": "Obligación legal", "dest": "SRI; Entidades bancarias",
     "enc": "Software contable o de nómina", "plazo": "Plazo fijado por la normativa tributaria (indicar)",
     "sistemas": "Software contable o ERP", "info": "Cláusula en el contrato",
     "nota": "La prestación del servicio (base contractual) y la facturación (obligación legal) pueden registrarse como actividades separadas."},
    {"actividad": "Marketing y publicidad", "area": "Marketing", "finalidad": "Enviar publicidad y promociones",
     "titulares": "Clientes; Potenciales clientes", "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección)",
     "origen": "Del propio titular", "base": "Consentimiento del titular",
     "enc": "Plataforma de correo masivo o mensajería", "plazo": "Hasta que el titular revoque su consentimiento",
     "sistemas": "CRM o sistema de ventas; WhatsApp o mensajería",
     "info": "Aviso de privacidad en el formulario o punto de recogida",
     "nota": "Registra aparte de la gestión de clientes: tiene base y plazo distintos. Si segmentas por preferencias, marca elaboración de perfiles."},
    {"actividad": "Sitio web y formularios de contacto", "area": "Marketing", "finalidad": "Atender solicitudes y reclamos",
     "titulares": "Usuarios del sitio web", "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Navegación y cookies",
     "origen": "Captación automática (cámaras, sitio web)", "enc": "Proveedor de nube u hosting",
     "sistemas": "Sitio web y formularios", "info": "Política de privacidad publicada",
     "nota": "Si el hosting o las herramientas de analítica están fuera del Ecuador, hay transferencia internacional."},
    {"actividad": "Videovigilancia", "area": "Seguridad física", "finalidad": "Seguridad de personas e instalaciones",
     "titulares": "Trabajadores; Visitantes; Clientes", "datos": "Imagen o video",
     "origen": "Captación automática (cámaras, sitio web)", "base": "Interés legítimo",
     "dest": "Autoridades judiciales o policiales (por requerimiento)", "enc": "Empresa de seguridad",
     "plazo": "Plazo corto fijado internamente (indicar días) salvo incidente",
     "sistemas": "Grabador de cámaras (DVR/NVR)", "info": "Cartel informativo (videovigilancia)",
     "nota": "Con interés legítimo, documenta la evaluación de ponderación (Res. SPDP-SPD-2025-0041-R). Si las cámaras captan la vía pública, revisa la evaluación de impacto (art. 42)."},
    {"actividad": "Gestión de proveedores", "area": "Contabilidad y Finanzas", "finalidad": "Gestionar cobros y pagos",
     "titulares": "Proveedores (personas naturales); Contactos de empresas proveedoras",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Financieros y bancarios",
     "origen": "Del propio titular", "base": "Ejecución de contrato o medidas precontractuales",
     "dest": "SRI; Entidades bancarias", "sistemas": "Software contable o ERP", "info": "Cláusula en el contrato"},
    {"actividad": "Atención de salud / historias clínicas", "area": "Dirección médica",
     "finalidad": "Ejecutar el contrato o prestar el servicio", "titulares": "Pacientes",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Salud",
     "origen": "Del propio titular", "sistemas": "Sistema clínico o académico; Archivo físico",
     "info": "Aviso de privacidad en el formulario o punto de recogida",
     "nota": "Datos de salud a gran escala exigen evaluación de impacto (art. 42). Describe la finalidad concreta (atención, seguimiento) y la excepción del art. 26."},
]

# Hoja del encargado (art. 44 RGLOPDP). El art. 44 fija cuándo se lleva; el contenido es de buena práctica
# hasta confirmar el texto (ver Puntos abiertos en BASE-LEGAL.md).
CAMPOS_ENCARGADO = [
    ("Responsable por cuenta de quien se trata", 26, "Cliente que encarga el tratamiento"),
    ("Contacto del responsable", 22, ""),
    ("¿El responsable está obligado a llevar el RAT?", 16, "Art. 44 RGLOPDP: solo entonces el encargado lleva este registro"),
    ("Servicio o tratamientos que se realizan por cuenta del responsable", 32, ""),
    ("Categorías de datos tratados", 26, ""),
    ("Ref. del contrato de encargo", 18, "Art. 41 RGLOPDP"),
    ("Subencargados", 22, "Otros proveedores que intervienen, con autorización del responsable"),
    ("¿Transferencia internacional? País y garantía", 24, ""),
    ("Medidas de seguridad", 30, "Descripción general"),
    ("Fecha de última revisión", 13, "AAAA-MM-DD"),
]

BASES = [
    "Consentimiento del titular", "Obligación legal", "Orden judicial", "Interés público / potestades públicas",
    "Ejecución de contrato o medidas precontractuales", "Interés vital", "Datos de bases de acceso público",
    "Interés legítimo",
]

# Preguntas de obligatoriedad. grupo: rol | tamano | habitual | especial | riesgo
PREGUNTAS = [
    {"id": "rol", "grupo": "rol", "tipo": "rol",
     "texto": "¿La organización decide para qué y cómo se tratan los datos, o los trata por encargo de otra?",
     "concepto": "Responsable es quien decide la finalidad y el modo del tratamiento (por ejemplo, una empresa con sus propios trabajadores y clientes). Encargado es quien trata datos por cuenta de otro (por ejemplo, el contador externo o el proveedor de nube). Una misma organización puede ser responsable de unos tratamientos y encargada de otros.",
     "norma": "Art. 4 LOPDP: el responsable es la persona natural o jurídica, pública o privada, autoridad u otro organismo que, solo o junto con otros, decide la finalidad y el tratamiento de los datos; el encargado trata datos personales en nombre y por cuenta del responsable. Art. 44 RGLOPDP: el encargado lleva el registro solo cuando el responsable esté obligado.",
     "literal": False},
    {"id": "trab", "grupo": "tamano", "tipo": "numero",
     "texto": "¿Cuántos trabajadores tiene la organización?",
     "concepto": "Cuenta a todas las personas en relación de dependencia. Si son 100 o más, la obligación es directa, sin necesidad de analizar las demás preguntas.",
     "norma": "Art. 38 RGLOPDP: el responsable que cuente con cien o más trabajadores llevará un registro de todas las actividades de tratamiento de datos personales que sean de su competencia.",
     "literal": False},
    {"id": "h_nomina", "grupo": "habitual", "tipo": "sino",
     "texto": "¿Tiene trabajadores en nómina, aunque sea uno?",
     "concepto": "Pagar sueldos, afiliar al IESS y llevar expedientes del personal es un tratamiento de datos continuo, no ocasional.",
     "norma": "", "literal": False},
    {"id": "h_clientes", "grupo": "habitual", "tipo": "sino",
     "texto": "¿Mantiene un listado o base de datos de clientes, pacientes, estudiantes o usuarios?",
     "concepto": "Registrar clientes para facturar, dar seguimiento o volver a contactarlos es un tratamiento habitual.",
     "norma": "", "literal": False},
    {"id": "h_visitas", "grupo": "habitual", "tipo": "sino",
     "texto": "¿Registra visitantes o tiene cámaras de seguridad?",
     "concepto": "El registro de ingresos y la videovigilancia son tratamientos permanentes de datos de las personas que entran a las instalaciones.",
     "norma": "", "literal": False},
    {"id": "h_publicidad", "grupo": "habitual", "tipo": "sino",
     "texto": "¿Envía publicidad o mensajes a una lista de contactos (correo, WhatsApp, SMS)?",
     "concepto": "Mantener una lista de difusión implica conservar y usar datos de contacto de forma recurrente.",
     "norma": "", "literal": False},
    {"id": "e_salud", "grupo": "especial", "tipo": "sino",
     "texto": "¿Trata datos de salud? (certificados médicos, exámenes ocupacionales, historias clínicas)",
     "concepto": "Datos de salud son los relativos a la salud física o mental de una persona, incluida la atención sanitaria, que revelen su estado de salud. Son categoría especial.",
     "norma": "Art. 4 LOPDP (datos de salud) y art. 25 LOPDP: son categorías especiales los datos sensibles, los de niñas, niños y adolescentes, los de salud y los de personas con discapacidad y sus sustitutos, relativos a la discapacidad.",
     "literal": False},
    {"id": "e_bio", "grupo": "especial", "tipo": "sino",
     "texto": "¿Usa datos biométricos? (reloj de huella, reconocimiento facial)",
     "concepto": "Biométricos son datos únicos sobre características físicas, fisiológicas o de conducta que permiten identificar a una persona, como la huella dactilar o la imagen facial. Un reloj de marcación por huella trata datos biométricos.",
     "norma": "Art. 4 LOPDP: los datos biométricos forman parte de los datos sensibles; el art. 25 los incluye dentro de las categorías especiales.",
     "literal": False},
    {"id": "e_nna", "grupo": "especial", "tipo": "sino",
     "texto": "¿Trata datos de niñas, niños o adolescentes? (estudiantes, pacientes menores, cargas familiares de trabajadores)",
     "concepto": "Cualquier dato de una persona menor de 18 años es categoría especial. Ojo: registrar las cargas familiares de los trabajadores también implica datos de menores.",
     "norma": "Art. 25 LOPDP, literal b: datos de niñas, niños y adolescentes.",
     "literal": False},
    {"id": "e_disc", "grupo": "especial", "tipo": "sino",
     "texto": "¿Trata datos de personas con discapacidad o de sus sustitutos?",
     "concepto": "Por ejemplo, el registro de trabajadores con carné de discapacidad o de sustitutos para cumplir la cuota laboral.",
     "norma": "Art. 25 LOPDP, literal d: datos de personas con discapacidad y de sus sustitutos, relativos a la discapacidad.",
     "literal": False},
    {"id": "e_sens", "grupo": "especial", "tipo": "sino",
     "texto": "¿Trata otros datos sensibles? (récord policial o pasado judicial, religión, etnia, afiliación política, orientación sexual, condición migratoria)",
     "concepto": "Pedir el récord policial a postulantes o registrar la condición migratoria de trabajadores extranjeros son ejemplos frecuentes.",
     "norma": "Art. 4 LOPDP: datos sensibles son los relativos a etnia, identidad de género o cultural, religión, ideología, filiación política, pasado judicial, condición migratoria, orientación sexual, salud, datos biométricos y genéticos, y aquellos cuyo tratamiento indebido pueda generar discriminación o afectar derechos fundamentales. Art. 26: su tratamiento está prohibido salvo las excepciones que enumera.",
     "literal": False},
    {"id": "r_perfiles", "grupo": "riesgo", "tipo": "sino",
     "texto": "¿Elabora perfiles o toma decisiones automáticas sobre las personas? (scoring de crédito, segmentación publicitaria, evaluación automatizada de postulantes)",
     "concepto": "Elaborar perfiles es evaluar, analizar o predecir aspectos de una persona (desempeño laboral, situación económica, salud, preferencias, ubicación) para determinar su comportamiento.",
     "norma": "Art. 4 LOPDP (elaboración de perfiles). Art. 42 LOPDP: la evaluación de impacto procede, entre otros casos, ante evaluaciones sistemáticas de aspectos personales basadas en tratamiento automatizado.",
     "literal": False},
    {"id": "r_observacion", "grupo": "riesgo", "tipo": "sino",
     "texto": "¿Vigila de forma sistemática zonas de acceso público? (cámaras que captan la vía pública o áreas abiertas al público)",
     "concepto": "La observación sistemática de espacios públicos afecta a personas que no tienen relación con la organización y que no pueden evitar ser grabadas.",
     "norma": "Art. 42 LOPDP: la observación sistemática a gran escala de una zona de acceso público es uno de los supuestos que exigen evaluación de impacto.",
     "literal": False},
    {"id": "r_escala", "grupo": "riesgo", "tipo": "sino",
     "texto": "¿Trata datos a gran escala? (miles de titulares, o una porción significativa de la población de una ciudad o sector)",
     "concepto": "La gran escala se valora por el número de titulares, el volumen de datos, la duración y el alcance geográfico del tratamiento.",
     "norma": "Art. 42 LOPDP: el tratamiento a gran escala de categorías especiales de datos exige evaluación de impacto. Los criterios de gran escala los desarrolla el RGLOPDP y la SPDP.",
     "literal": False},
    {"id": "r_financieros", "grupo": "riesgo", "tipo": "sino",
     "texto": "¿Trata datos financieros, crediticios o de medios de pago de los titulares?",
     "concepto": "Una filtración de estos datos puede causar fraude o pérdidas económicas directas a las personas.",
     "norma": "", "literal": False},
    {"id": "r_geo", "grupo": "riesgo", "tipo": "sino",
     "texto": "¿Rastrea la ubicación de las personas? (GPS de vehículos o celulares, aplicaciones con geolocalización)",
     "concepto": "La geolocalización continua revela hábitos, rutinas y lugares frecuentados.",
     "norma": "", "literal": False},
]

GRUPOS = {
    "rol": "Rol en el tratamiento",
    "tamano": "Tamaño de la organización",
    "habitual": "¿El tratamiento es habitual? (si alguna respuesta es Sí, no es ocasional)",
    "especial": "¿Incluye categorías especiales de datos?",
    "riesgo": "¿El tratamiento implica riesgo para los titulares?",
}

NORMA_39 = ("Art. 39 RGLOPDP: aun con menos de cien trabajadores, el registro es obligatorio cuando el tratamiento "
            "implica riesgo para los derechos y libertades de los titulares, no es ocasional o incluye categorías "
            "especiales de datos.")
