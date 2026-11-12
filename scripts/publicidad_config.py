"""Fuente única de la pestaña «Publicidad» de la app (piezas para WhatsApp).

Regla: toda afirmación normativa lleva su cita y consta en BASE-LEGAL.md. Lenguaje claro para gerentes y titulares,
sin prometer resultados ni exagerar multas. Los datos de contacto NO se guardan aquí: se toman de Ajustes (cifrados).
"""
# Cada pieza combina lo técnico con el enfoque comercial (criterio propio):
#  g = gancho: primera línea del mensaje, nombra un problema del gerente, no un artículo.
#  p = pregunta o título de la pieza.   r = respuesta técnica breve.   c = cita (consta en BASE-LEGAL.md).
#  n = «Para su negocio»: por qué le importa (riesgo, costo, confianza, ventas). Sin cifras de mercado ni promesas.
PREGUNTAS = [
 {"g": "¿Su empresa está en una de las 14 actividades que deben tener Delegado?", "p": "¿Mi empresa necesita un Delegado de Protección de Datos?", "r": "Depende de su actividad y del volumen de datos. Es obligatorio en el sector público, con control permanente y sistematizado, en gran escala de datos sensibles y en 14 actividades privadas como educación, salud, seguros, seguridad privada o telecomunicaciones.", "c": "LOPDP art. 48; Res. SPDP-SPD-2025-0028-R art. 10", "n": "Si su actividad está en la lista, designarlo no es opcional. Saberlo hoy le permite presupuestarlo con calma y no resolverlo bajo presión."},
 {"g": "Un correo sin responder puede convertirse en una infracción.", "p": "¿En cuánto tiempo debo responder si un cliente pide ver o borrar sus datos?", "r": "En 15 días. No responder o negar sin causa es infracción leve.", "c": "LOPDP arts. 13 a 16 y 67", "n": "Un canal claro de atención evita reclamos ante la SPDP y transmite seriedad: responder a tiempo también es servicio al cliente."},
 {"g": "Si mañana le hackean el correo, ¿sabe a quién avisar y en qué plazo?", "p": "¿Qué hago si sufro un hackeo o una filtración de datos?", "r": "Notificar a la Superintendencia, al organismo de control de su sector y al CSIRT en máximo 5 días hábiles, y a las personas afectadas en 3 días si hay riesgo para sus derechos.", "c": "LOPDP arts. 43 y 46", "n": "Los primeros días definen el daño. Tener el procedimiento escrito y los contactos listos reduce el impacto legal y el golpe a su reputación."},
 {"g": "Tener una política publicada no es lo mismo que cumplir.", "p": "¿Basta con tener una política de privacidad publicada?", "r": "No. La SPDP exige cumplimiento real: que los canales funcionen, que los datos se protejan y que todo esté documentado.", "c": "Guía SPDP de riesgos v2, Cap. I, § 6.2", "n": "Lo que no está documentado no se puede demostrar. Ordenar la evidencia ahora le ahorra tiempo y costos si llega un requerimiento."},
 {"g": "¿Marca asistencia con huella o reconocimiento facial? Revise esto.", "p": "¿Puedo usar huella o reconocimiento facial para marcar asistencia?", "r": "Solo si es estrictamente necesario, con consentimiento explícito, evaluación de impacto previa y una alternativa no biométrica para el trabajador.", "c": "Res. SPDP-SPD-2026-0039-R", "n": "Es uno de los tratamientos más sensibles de la empresa. Ofrecer la alternativa y documentar la evaluación evita tener que detener el sistema más adelante."},
 {"g": "La multa no es una cifra fija: se calcula sobre su volumen de negocio.", "p": "¿Cuánto puede costar una multa?", "r": "En el sector privado, de 0,1 % a 0,7 % del volumen de negocio por infracción leve y de 0,7 % a 1 % por infracción grave.", "c": "LOPDP arts. 71 y 72", "n": "Prevenir le permite decidir cuánto invertir y cuándo; una sanción no. Un diagnóstico le muestra dónde está el riesgo antes de que lo vea la autoridad."},
 {"g": "Su contador, su nómina o su nube también manejan los datos de su empresa.", "p": "¿Mis proveedores de nómina, contabilidad o nube tienen que firmar algo?", "r": "Sí. Todo encargado que trata datos por cuenta de su empresa necesita un contrato escrito con contenidos mínimos.", "c": "RGLOPDP art. 41; LOPDP art. 68 num. 9", "n": "Si el proveedor falla, usted sigue respondiendo ante sus clientes. Un contrato bien hecho reparte responsabilidades y le da herramientas para exigir."},
 {"g": "¿Sabe exactamente qué datos personales maneja su empresa?", "p": "¿Qué es el Registro de actividades de tratamiento (RAT)?", "r": "Es el inventario de qué datos trata su empresa, para qué, con qué base legal y cómo los protege. Es obligatorio con 100 o más trabajadores y, con menos, si hay riesgo o datos sensibles.", "c": "RGLOPDP arts. 38 y 39", "n": "El RAT es el mapa de su información: sin él no se puede proteger ni demostrar nada, y es la base de políticas, contratos y seguridad."},
 {"g": "¿Vende por WhatsApp? Esto le interesa.", "p": "¿Puedo enviar publicidad por WhatsApp a mis clientes?", "r": "Sí, con una base legal válida y ofreciendo en cada mensaje una forma fácil y gratuita de dejar de recibirla.", "c": "LOPDP art. 16 num. 2; Res. SPDP-SPD-2025-0041-R art. 11", "n": "Respetar a quien pide no recibir mensajes cuida su reputación: una lista de contactos interesados vale más que una lista grande."},
 {"g": "Las cámaras de su local también tratan datos personales.", "p": "¿Las cámaras de seguridad tratan datos personales?", "r": "Sí. Deben informarse con carteles y no pueden grabar audio ni ubicarse en baños, vestidores o lactarios.", "c": "LOPDP art. 12; Res. SPDP-SPD-2025-0041-R art. 15", "n": "Un cartel bien hecho y reglas claras sobre las grabaciones le dan respaldo cuando necesite usar un video ante un incidente."},
 {"g": "Antes de lanzar ese nuevo sistema, evalúe el riesgo.", "p": "¿Qué es una evaluación de impacto?", "r": "Un análisis previo de los riesgos para las personas antes de iniciar un tratamiento de alto riesgo, como perfiles automáticos o datos sensibles a gran escala.", "c": "LOPDP art. 42; RGLOPDP arts. 29 a 32", "n": "Corregir un problema en la etapa de diseño es mucho más sencillo que hacerlo con el sistema en marcha y los datos ya recogidos."},
 {"g": "No cualquiera puede ser Delegado de Protección de Datos.", "p": "¿Quién puede ser Delegado de Protección de Datos?", "r": "Una persona natural con título de tercer nivel en Derecho, Sistemas de Información, Comunicación o Tecnologías y cinco años de experiencia profesional, sin conflicto de intereses.", "c": "RGLOPDP arts. 55 y 56", "n": "Designar a alguien que no cumple los requisitos o tiene conflicto de intereses le obliga a repetir el proceso. Verifique antes de firmar."},
 {"g": "¿Usa inteligencia artificial con datos de clientes?", "p": "¿Uso inteligencia artificial con datos de clientes: qué debo hacer?", "r": "Informarlo, gestionar los riesgos antes de implementarla, incluir el tratamiento en el RAT y auditar el sistema según su riesgo.", "c": "Res. SPDP-SPD-2026-0009-R art. 5", "n": "La IA con reglas claras es una ventaja competitiva; sin ellas, un riesgo. Documentar su uso desde el inicio le permite crecer sin frenar el proyecto."},
 {"g": "¿Su formulario pide más datos de los que necesita?", "p": "¿Puedo pedir la cédula o datos de los hijos en un formulario?", "r": "Solo si son necesarios para la finalidad. Pedir datos de más incumple el principio de minimización.", "c": "LOPDP art. 10 lit. e", "n": "Cada dato extra es un riesgo extra que debe proteger. Un formulario más corto también es más fácil de llenar para su cliente."},
]

# Datos clave: [cifra, texto, cita, gancho, para su negocio]
DATOS = [
 ["5 días", "para notificar una vulneración de la seguridad a la SPDP, al regulador y al CSIRT.", "LOPDP art. 43", "¿Cuánto tiempo tiene para avisar un incidente de seguridad?", "Con un plan listo, esos días alcanzan; sin él, se van en averiguar qué pasó."],
 ["15 días", "para responder solicitudes de acceso, rectificación, eliminación u oposición.", "LOPDP arts. 13 a 16", "Cuando un cliente pide sus datos, el reloj empieza a correr.", "Un procedimiento sencillo de atención evita reclamos y demuestra profesionalismo."],
 ["Hasta 1 %", "del volumen de negocio por infracción grave en el sector privado.", "LOPDP art. 72", "Las multas se calculan sobre las ventas, no sobre la utilidad.", "Para una empresa en crecimiento es una cifra que conviene prevenir, no pagar."],
 ["14 actividades", "privadas deben designar un Delegado de Protección de Datos.", "Res. SPDP-SPD-2025-0028-R art. 10", "¿Su sector está en la lista?", "Educación, salud, seguros, seguridad privada, telecomunicaciones y más: revise si la suya está incluida."],
 ["15 días hábiles", "para inscribir el nombramiento del Delegado ante la SPDP.", "Res. SPDP-SPD-2025-0028-R art. 5", "Designar al Delegado no termina con la firma.", "El nombramiento debe inscribirse a tiempo; planifíquelo desde la designación."],
 ["17 elementos", "debe informar a las personas antes de recoger sus datos.", "LOPDP art. 12", "Su aviso de privacidad, ¿tiene todo lo que exige la ley?", "Un aviso completo genera confianza justo cuando su cliente le entrega sus datos."],
 ["100 trabajadores", "o más obligan a llevar el Registro de actividades de tratamiento.", "RGLOPDP art. 38", "¿Su empresa ya llegó a 100 trabajadores?", "Si ya los tiene, el RAT es obligatorio; si no, es la mejor forma de ordenar su información antes de crecer."],
 ["2 días", "tiene su proveedor para avisarle de una vulneración.", "LOPDP art. 43", "Si su proveedor sufre un incidente, ¿le avisaría a tiempo?", "Revise que sus contratos lo digan por escrito: lo que no está pactado es difícil de exigir."],
]

# Uso recomendado de las piezas (criterio propio, no normativo)
ESTRATEGIA = [
 "Eduque antes de vender: por cada pieza de servicio, publique unas tres informativas (dato, pregunta o «¿Sabía que…?»).",
 "Una idea por pieza y un gancho que nombre un problema del gerente (un hackeo, una multa, un cliente que reclama), no un artículo de la ley.",
 "Cierre siempre con una sola acción: escribir, agendar o hacer el autodiagnóstico.",
 "Constancia antes que volumen: 3 o 4 estados por semana rinden más que muchos en un solo día.",
 "Secuencia de captación: dato o pregunta → autodiagnóstico → seguimiento personal en menos de 24 horas citando sus brechas concretas.",
 "Segmente por sector: envíe a colegios, clínicas o empresas de seguridad la pieza que más les toca.",
 "Mida: anote qué pieza generó respuestas y repita el tema que funciona.",
]

CTA = [
 "Agende una reunión de diagnóstico",
 "Escríbanos y revisamos su caso",
 "Solicite su autodiagnóstico gratuito",
 "Consulte hoy, antes de una inspección",
 "Conozca su nivel de riesgo en 5 minutos",
 "Hablemos 15 minutos sobre su empresa",
]

# Aviso de oposición que se añade a los mensajes (mercadotecnia directa).
BAJA = "Si no desea recibir más mensajes, responda BAJA."

AUTODIAG = {
 "url": "https://tally.so/r/X5LNKV",
 # Página puente con vista previa de la marca (la genera build_pwa.py y redirige al formulario)
 "corto": "https://xavimac123.github.io/portafolio-dpd-ecuador/autodiagnostico/",
 "titulo": "Autodiagnóstico de protección de datos",
 "texto": "15 preguntas, 5 minutos y su nivel de riesgo al instante. Sus datos se tratan solo para enviarle el resultado y contactarle.",
}
