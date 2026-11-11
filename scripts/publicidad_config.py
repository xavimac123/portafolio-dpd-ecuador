"""Fuente única de la pestaña «Publicidad» de la app (piezas para WhatsApp).

Regla: toda afirmación normativa lleva su cita y consta en BASE-LEGAL.md. Lenguaje claro para gerentes y titulares,
sin prometer resultados ni exagerar multas. Los datos de contacto NO se guardan aquí: se toman de Ajustes (cifrados).
"""
# [pregunta, respuesta breve, cita]
PREGUNTAS = [
 ["¿Mi empresa necesita un Delegado de Protección de Datos?", "Depende de su actividad y del volumen de datos. Es obligatorio en el sector público, con control permanente y sistematizado, en gran escala de datos sensibles y en 14 actividades privadas como educación, salud, seguros, seguridad privada o telecomunicaciones.", "LOPDP art. 48; Res. SPDP-SPD-2025-0028-R art. 10"],
 ["¿En cuánto tiempo debo responder si un cliente pide ver o borrar sus datos?", "En 15 días. No responder o negar sin causa es infracción leve.", "LOPDP arts. 13 a 16 y 67"],
 ["¿Qué hago si sufro un hackeo o una filtración de datos?", "Notificar a la Superintendencia, al organismo de control de su sector y al CSIRT en máximo 5 días hábiles, y a las personas afectadas en 3 días si hay riesgo para sus derechos.", "LOPDP arts. 43 y 46"],
 ["¿Basta con tener una política de privacidad publicada?", "No. La SPDP exige cumplimiento real: que los canales funcionen, que los datos se protejan y que todo esté documentado.", "Guía SPDP de riesgos v2, Cap. I, § 6.2"],
 ["¿Puedo usar huella o reconocimiento facial para marcar asistencia?", "Solo si es estrictamente necesario, con consentimiento explícito, evaluación de impacto previa y una alternativa no biométrica para el trabajador.", "Res. SPDP-SPD-2026-0039-R"],
 ["¿Cuánto puede costar una multa?", "En el sector privado, de 0,1 % a 0,7 % del volumen de negocio por infracción leve y de 0,7 % a 1 % por infracción grave.", "LOPDP arts. 71 y 72"],
 ["¿Mis proveedores de nómina, contabilidad o nube tienen que firmar algo?", "Sí. Todo encargado que trata datos por cuenta de su empresa necesita un contrato escrito con contenidos mínimos.", "RGLOPDP art. 41; LOPDP art. 68 num. 9"],
 ["¿Qué es el Registro de actividades de tratamiento (RAT)?", "Es el inventario de qué datos trata su empresa, para qué, con qué base legal y cómo los protege. Es obligatorio con 100 o más trabajadores y, con menos, si hay riesgo o datos sensibles.", "RGLOPDP arts. 38 y 39"],
 ["¿Puedo enviar publicidad por WhatsApp a mis clientes?", "Sí, con una base legal válida y ofreciendo en cada mensaje una forma fácil y gratuita de dejar de recibirla.", "LOPDP art. 16 num. 2; Res. SPDP-SPD-2025-0041-R art. 11"],
 ["¿Las cámaras de seguridad tratan datos personales?", "Sí. Deben informarse con carteles y no pueden grabar audio ni ubicarse en baños, vestidores o lactarios.", "LOPDP art. 12; Res. SPDP-SPD-2025-0041-R art. 15"],
 ["¿Qué es una evaluación de impacto?", "Un análisis previo de los riesgos para las personas antes de iniciar un tratamiento de alto riesgo, como perfiles automáticos o datos sensibles a gran escala.", "LOPDP art. 42; RGLOPDP arts. 29 a 32"],
 ["¿Quién puede ser Delegado de Protección de Datos?", "Una persona natural con título de tercer nivel en Derecho, Sistemas de Información, Comunicación o Tecnologías y cinco años de experiencia profesional, sin conflicto de intereses.", "RGLOPDP arts. 55 y 56"],
 ["¿Uso inteligencia artificial con datos de clientes: qué debo hacer?", "Informarlo, gestionar los riesgos antes de implementarla, incluir el tratamiento en el RAT y auditar el sistema según su riesgo.", "Res. SPDP-SPD-2026-0009-R art. 5"],
 ["¿Puedo pedir la cédula o datos de los hijos en un formulario?", "Solo si son necesarios para la finalidad. Pedir datos de más incumple el principio de minimización.", "LOPDP art. 10 lit. e"],
]

# [título corto, texto, cita]
DATOS = [
 ["5 días", "para notificar una vulneración de la seguridad a la SPDP, al regulador y al CSIRT.", "LOPDP art. 43"],
 ["15 días", "para responder solicitudes de acceso, rectificación, eliminación u oposición.", "LOPDP arts. 13 a 16"],
 ["Hasta 1 %", "del volumen de negocio por infracción grave en el sector privado.", "LOPDP art. 72"],
 ["14 actividades", "privadas deben designar un Delegado de Protección de Datos.", "Res. SPDP-SPD-2025-0028-R art. 10"],
 ["15 días hábiles", "para inscribir el nombramiento del Delegado ante la SPDP.", "Res. SPDP-SPD-2025-0028-R art. 5"],
 ["17 elementos", "debe informar a las personas antes de recoger sus datos.", "LOPDP art. 12"],
 ["100 trabajadores", "o más obligan a llevar el Registro de actividades de tratamiento.", "RGLOPDP art. 38"],
 ["2 días", "tiene su proveedor para avisarle de una vulneración.", "LOPDP art. 43"],
]

CTA = [
 "Agende una reunión de diagnóstico",
 "Escríbanos y revisamos su caso",
 "Solicite su autodiagnóstico gratuito",
 "Consulte hoy, antes de una inspección",
]

# Aviso de oposición que se añade a los mensajes (mercadotecnia directa).
BAJA = "Si no desea recibir más mensajes, responda BAJA."

AUTODIAG = {
 "url": "https://tally.so/r/X5LNKV",
 "titulo": "Autodiagnóstico de protección de datos",
 "texto": "15 preguntas, 5 minutos y su nivel de riesgo al instante. Sus datos se tratan solo para enviarle el resultado y contactarle.",
}
