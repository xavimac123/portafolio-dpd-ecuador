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
        "Pasado judicial", "Etnia, religión, ideología u orientación sexual", "Condición migratoria",
    ],
     # opciones que activan "categorías especiales" (LOPDP arts. 4 y 25)
     "especiales": ["Salud", "Biométricos (huella, rostro)", "Niñas, niños y adolescentes", "Discapacidad",
                    "Pasado judicial", "Etnia, religión, ideología u orientación sexual", "Condición migratoria"],
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
}

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
