"""Fuente única de la herramienta 05: evaluación del tratamiento a gran escala.

Base: RGLOPDP art. 4 num. 7 (definición y casos predeterminados), arts. 53 y 54; LOPDP arts. 42 y 48;
Res. SPDP-SPD-2026-0005-R (MTGE). Las ayudas didácticas, el contador de tipos de datos y la lectura de
sensibilidad son material de apoyo de Macías Sánchez Consultores (criterio propio), no norma.
"""

VERSION = "0.1"
UMBRAL = 6

# Calificación directa: si se cumple alguno, el tratamiento es de gran escala sin aplicar el MTGE.
DIRECTA = [
    # fuente, texto, ejemplo práctico
    ["RGLOPDP art. 4 num. 7 lit. a", "Datos de pacientes en la actividad normal de un hospital o de instituciones del Sistema Nacional de Salud", "Clínica privada que lleva historias clínicas."],
    ["RGLOPDP art. 4 num. 7 lit. b", "Datos de desplazamiento de usuarios del transporte público de una ciudad", "Tarjeta de pasajes de un sistema de metro o buses."],
    ["RGLOPDP art. 4 num. 7 lit. c", "Geolocalización en tiempo real de clientes por un responsable especializado en ese servicio", "Aplicación de rastreo vehicular o de taxis."],
    ["RGLOPDP art. 4 num. 7 lit. d", "Datos de clientes en la actividad normal de aseguradoras, intermediarios de seguros o instituciones financieras", "Cooperativa de ahorro y crédito; bróker de seguros."],
    ["RGLOPDP art. 4 num. 7 lit. e", "Datos para publicidad comportamental por un motor de búsqueda", "Buscador que perfila a sus usuarios para anuncios."],
    ["RGLOPDP art. 4 num. 7 lit. f", "Datos de contenido, tráfico y ubicación por proveedores de telefonía o internet", "Operadora de telefonía o proveedor de internet."],
    ["Res. 2026-0005 art. 14.1", "Tratamientos de salud (sistemas sanitarios, asistenciales, de seguridad social o historias clínicas) y otros datos sensibles o categorías especiales. Criterio de la SPDP (Oficio SPDP-IRD-2026-0221-O, según resumen): tratar datos sensibles no basta por sí solo; fuera de los sistemas de salud e historias clínicas, valora magnitud, alcance y sistematicidad con el MTGE", "Laboratorio clínico, consultorio, aseguradora de salud. No califica por sí solo: certificados médicos en la nómina de una pyme."],
    ["Res. 2026-0005 art. 14.2", "Evaluación sistemática y exhaustiva automatizada de aspectos personales (perfiles, predicción, monitoreo de conductas) con efectos jurídicos o que afecte derechos", "Puntaje automático para aprobar créditos o contratar personal."],
    ["Res. 2026-0005 art. 14.3", "Observación sistemática de personas en espacios públicos mediante videovigilancia u otro monitoreo continuo", "Cámaras que captan la vía pública o áreas abiertas al público."],
    ["Res. 2026-0005 art. 14.4", "Todo tratamiento de datos biométricos o de geolocalización. Son supuestos autónomos: cualquiera basta por sí solo (Oficio SPDP-IRD-2026-0221-O, según resumen)", "Reloj biométrico de asistencia; aplicación con GPS de vendedores."],
    ["Res. 2026-0005 art. 14.5", "Tratamiento estructural en sistemas de información crediticia o de riesgo económico", "Burós de crédito; cartera que reporta o consulta riesgo."],
    ["Res. 2026-0005 art. 14.5 (segundo)", "Tratamiento sistemático de datos de niñas, niños y adolescentes en entornos institucionales, educativos o digitales dirigidos a ellos", "Unidad educativa; plataforma de juegos infantiles."],
    ["Res. 2026-0005 art. 14.6", "Transferencias sistemáticas que forman flujos continuos o estructurales, dentro o fuera del Ecuador (recurrentes, organizadas e integradas en la operación; las ocasionales no cuentan)", "Envío diario de datos a la casa matriz o a un proveedor en el exterior."],
    ["Res. 2026-0005 art. 14.7", "Tratamiento de datos en servicios de mensajería acelerada, expresa o courier", "Empresa de courier o entregas a domicilio."],
]

# Contador de tipos de datos (ayuda didáctica): cada casilla es un tipo de dato por titular.
TIPOS_DATOS = {
    "Identificación": ["Nombres y apellidos", "Cédula o pasaporte", "RUC", "Fecha de nacimiento", "Edad", "Sexo", "Nacionalidad", "Estado civil", "Fotografía", "Firma", "Número de cliente o código interno"],
    "Contacto": ["Dirección domiciliaria", "Teléfono fijo", "Teléfono celular", "Correo electrónico", "Usuario de redes sociales", "Contacto de emergencia"],
    "Laborales y académicos": ["Cargo", "Área", "Fecha de ingreso", "Sueldo o remuneración", "Historial laboral", "Formación académica", "Evaluaciones de desempeño", "Número de afiliación al IESS"],
    "Económicos y financieros": ["Cuenta bancaria", "Tarjeta (últimos dígitos)", "Historial de compras o facturas", "Deudas o cartera", "Ingresos declarados", "Calificación de riesgo"],
    "Técnicos y de uso": ["Dirección IP", "Identificador de dispositivo", "Cookies o identificadores en línea", "Registros de acceso", "Geolocalización", "Imagen de videovigilancia", "Grabaciones de voz"],
    "Familiares": ["Cónyuge o conviviente", "Hijos o cargas familiares", "Datos de beneficiarios"],
    "Categorías especiales (también se marcan abajo)": ["Datos de salud", "Datos biométricos", "Datos genéticos", "Pasado judicial", "Condición migratoria", "Etnia o identidad cultural", "Religión o ideología", "Filiación política", "Orientación sexual o identidad de género", "Discapacidad"],
}

# Categorías: definen la variable 3 del MTGE.
CATEGORIAS = [
    # texto, tipo: "esp" (categoría especial) o "tres" (lleva directamente a 3 puntos)
    ["Datos de salud", "esp"], ["Datos biométricos", "esp"], ["Datos genéticos", "esp"],
    ["Etnia o identidad cultural", "esp"], ["Religión o ideología", "esp"], ["Filiación política", "esp"],
    ["Orientación sexual o identidad de género", "esp"], ["Condición migratoria", "esp"],
    ["Niñas, niños y adolescentes", "esp"], ["Personas con discapacidad y sus sustitutos", "esp"],
    ["Pasado judicial, condenas o infracciones penales", "tres"],
    ["Grupos vulnerables o de atención prioritaria (adultos mayores, víctimas, personas en movilidad, etc.)", "tres"],
]

# Variables del MTGE con su material didáctico.
VARIABLES = [
    {"id": "tit", "nombre": "Número de titulares", "base": "Res. 2026-0005 arts. 3.8 y 8.1",
     "pregunta": "¿A cuántas personas distintas se refiere este tratamiento en los últimos 12 meses?",
     "pedir": "Un conteo de registros únicos (por cédula, RUC o correo) del sistema donde vive el tratamiento: ERP, nómina, CRM, base de clientes, registro de visitantes.",
     "aquien": "Sistemas o el dueño del proceso (contabilidad, talento humano, ventas).",
     "contar": "Cuente a cada persona una sola vez aunque aparezca varias veces (titular único). Solo las de este tratamiento, no las de toda la empresa: el MTGE se aplica a cada tratamiento por separado y no se suman bases distintas (trabajadores, clientes, proveedores) para llegar al umbral (Oficio SPDP-IRD-2026-0221-O, según resumen). Periodo: 12 meses.",
     "explicar": "No importa cuántas veces compró un cliente: importa cuántas personas distintas hay detrás de los datos.",
     "tipo": "num", "tramos": [[1000, 1, "Hasta 1.000"], [10000, 2, "1.001 a 10.000"], [100000, 3, "10.001 a 100.000"], [None, 4, "Más de 100.000"]]},
    {"id": "vol", "nombre": "Volumen de datos (tipos de datos por titular)", "base": "Res. 2026-0005 arts. 3.13 y 8.2",
     "pregunta": "¿Cuántos tipos de datos distintos se guardan de cada persona?",
     "pedir": "Los formularios, fichas o la estructura de la base de datos (campos o columnas) del tratamiento.",
     "aquien": "Dueño del proceso; sistemas para la estructura de la base.",
     "contar": "Cada campo con información de la persona es un tipo de dato: nombre, cédula, correo, dirección, sueldo… Use el contador de abajo si no tiene la lista.",
     "explicar": "Cuanto más se sabe de cada persona, mayor es el daño si los datos se filtran. Minimizar campos reduce el riesgo y el puntaje.",
     "tipo": "num", "tramos": [[10, 0.5, "Hasta 10"], [30, 1, "11 a 30"], [100, 2, "31 a 100"], [None, 3, "101 o más"]]},
    {"id": "cat", "nombre": "Categorías de datos", "base": "Res. 2026-0005 arts. 3.6 y 8.3; LOPDP arts. 4 y 25",
     "pregunta": "¿El tratamiento incluye datos sensibles, de niñas, niños y adolescentes, de salud, de personas con discapacidad, penales o de grupos vulnerables?",
     "pedir": "La lista de campos del paso anterior y los documentos que se recogen (certificados médicos, récord policial, partidas de nacimiento de cargas).",
     "aquien": "Dueño del proceso.",
     "contar": "Solo datos básicos: 0,5 puntos. Una categoría especial: 2. Más de una, o datos penales o de grupos vulnerables: 3.",
     "explicar": "Son datos que, mal usados, pueden discriminar o causar un daño grave: la ley les exige más cuidado.",
     "tipo": "cat"},
    {"id": "fre", "nombre": "Frecuencia", "base": "Res. 2026-0005 arts. 3.7 y 8.4",
     "pregunta": "¿Con qué frecuencia se tratan los datos?",
     "pedir": "Descripción del proceso: cuándo se recogen, consultan o actualizan los datos.",
     "aquien": "Dueño del proceso.",
     "contar": "Puntual: una vez o de forma excepcional. Periódica: se repite en intervalos (mensual, por cada venta). Continua: permanente o en tiempo real (cámaras, GPS, sistemas en línea).",
     "explicar": "Un tratamiento que nunca se detiene expone a las personas de forma permanente.",
     "tipo": "sel", "ops": [["Puntual o única", 0.5], ["Periódica o recurrente", 1], ["Continua o en tiempo real", 2]]},
    {"id": "per", "nombre": "Permanencia", "base": "Res. 2026-0005 arts. 3.9 a 3.12 y 8.5",
     "pregunta": "¿Durante cuánto tiempo se realizan operaciones activas sobre los datos?",
     "pedir": "Política o práctica de conservación y el plazo real en que los datos se usan (no solo el plazo legal de archivo).",
     "aquien": "Dueño del proceso; contabilidad o legal para los plazos de conservación.",
     "contar": "Ocasional: excepcional o esporádico. Temporal: menos de tres años. Prolongada: tres años o más. La norma mide operaciones activas: el periodo de archivo o bloqueo no cuenta.",
     "explicar": "Mientras más tiempo se usan los datos, más tiempo están expuestos.",
     "tipo": "sel", "ops": [["Ocasional", 0.5], ["Temporal (menos de 3 años)", 1], ["Prolongada (3 años o más)", 2]]},
    {"id": "geo", "nombre": "Alcance geográfico", "base": "Res. 2026-0005 arts. 3.1 a 3.5 y 8.6",
     "pregunta": "¿Dónde están los titulares y dónde se tratan sus datos?",
     "pedir": "Sedes, sucursales, cobertura de ventas o servicio, y ubicación de los servidores o servicios en la nube.",
     "aquien": "Gerencia (cobertura) y sistemas (servidores).",
     "contar": "Local: una provincia, cantón o ciudad. Nacional: más de una. Global o transfronterizo: involucra otro país, una organización internacional o un territorio económico internacional.",
     "explicar": "A mayor alcance, más personas y más jurisdicciones involucradas.",
     "tipo": "sel", "ops": [["Local", 1], ["Nacional", 2], ["Global o transfronterizo", 3]]},
]

# Obligaciones cuando el tratamiento es de gran escala
OBLIGACIONES = [
    ["Designar un delegado de protección de datos y registrarlo ante la SPDP", "Res. 2026-0005 art. 12 num. 2; LOPDP art. 48", "Inmediato; el plazo transitorio de 90 días corrió desde el 25-02-2026"],
    ["Realizar la evaluación de impacto antes del tratamiento", "Res. 2026-0005 art. 12 num. 1; LOPDP art. 42", "Antes de iniciar o modificar el tratamiento"],
    ["Incluir el tratamiento y el cálculo del MTGE en el RAT, con descripción, categorías y tipos de datos, titulares, frecuencia, permanencia y medidas de seguridad", "Res. 2026-0005 arts. 4, 7, 12 num. 3 y 15", "Al calificar el tratamiento"],
    ["Actualizar el RAT y el cálculo al menos una vez al año, y conservar la evidencia del cálculo", "Res. 2026-0005 arts. 6 y 13", "Cada 12 meses o ante cambios sustanciales"],
    ["Aplicar privacidad desde el diseño y por defecto", "Res. 2026-0005 art. 16", "Antes y durante el tratamiento"],
    ["Realizar auditorías y conservar los informes al menos cinco años", "Res. 2026-0005 art. 17", "Cada 12 meses y tras cambios significativos"],
    ["Identificar los tratamientos de gran escala en la política de privacidad y elaborar un informe anual de cumplimiento", "Res. 2026-0005 art. 18", "Anual; conservar cinco años"],
]

# Lo que debe pedirse al cliente (base del documento de solicitud de información)
SOLICITUD = [
    ["Listado de procesos o del RAT vigente", "Identificar los tratamientos a evaluar", "Gerencia o responsable de cumplimiento"],
    ["Número de personas únicas por base de datos en los últimos 12 meses (clientes, trabajadores, proveedores personas naturales, visitantes, pacientes, alumnos)", "Variable 1: titulares", "Sistemas y dueños de procesos"],
    ["Formularios, fichas y estructura de campos de cada base de datos", "Variables 2 y 3: volumen y categorías", "Dueños de procesos y sistemas"],
    ["Documentos que se piden a las personas (certificados médicos, récord policial, partidas de nacimiento)", "Variable 3: categorías especiales", "Talento humano, servicio al cliente"],
    ["Descripción de cuándo se recogen y usan los datos (por venta, mensual, en tiempo real)", "Variable 4: frecuencia", "Dueños de procesos"],
    ["Política o práctica de conservación y tiempo real de uso activo", "Variable 5: permanencia", "Legal, contabilidad"],
    ["Sedes, cobertura geográfica y ubicación de servidores o servicios en la nube", "Variable 6: alcance geográfico", "Gerencia y sistemas"],
    ["Uso de cámaras, relojes biométricos, GPS, perfiles automáticos, buró de crédito, datos de menores y envíos de datos al exterior", "Calificación directa", "Gerencia, seguridad, sistemas"],
]
