"""Fuente única de la pestaña «Responsabilidades DPO» de la app.

Regla del repositorio: toda cita consta en BASE-LEGAL.md. Lo que no viene de la norma (formas de ejercer una función,
fases de auditoría, clasificación de hallazgos) se rotula como criterio propio en la interfaz y en la exportación.
DPO es la sigla en inglés; en la LOPDP la figura se llama «delegado de protección de datos» (DPD).
Siglas de cita: «Res. 0028» = Res. SPDP-SPD-2025-0028-R; «Guía v2» = Res. SPDP-SPD-2026-0012-R.
"""
REVISION = "2026-11-11"

INTRO = {
 "definicion": [
  ["Persona natural que informa al responsable o al encargado sobre sus obligaciones legales, vela o supervisa el cumplimiento y coopera con la SPDP como punto de contacto.", "LOPDP art. 4"],
  ["Se encarga principalmente de asesorar, velar y supervisar, de manera independiente, el cumplimiento de las obligaciones legales del responsable y del encargado.", "RGLOPDP art. 48"],
  ["Es uno de los seis integrantes del sistema de protección de datos personales.", "LOPDP art. 5"]],
 "regla": "El DPD asesora y supervisa; el responsable decide e implementa. Sus observaciones sobre riesgos y evaluaciones de impacto no son vinculantes, pero deben constar por escrito: si actuó con diligencia, no responde por las decisiones finales del responsable.",
 "regla_cita": "Res. 0028 arts. 13 (inciso final), 15.1 y 15.2",
 "verbos": [
  ["Asesorar", "Informa y orienta al responsable, a su personal y al encargado.", "LOPDP art. 49 num. 1"],
  ["Supervisar", "Verifica que el cumplimiento sea real y que las medidas funcionen.", "LOPDP art. 49 num. 2"],
  ["Cooperar", "Es el punto de contacto con la SPDP, sin representar a la organización.", "LOPDP art. 49 num. 4; Res. 0028 art. 15.4"]],
}

# Catálogo de funciones. Cada ítem: t (función), d (alcance según la norma), c (cita), como (buena práctica, criterio propio), herr.
FUNCIONES = [
 {"eje": "Asesorar", "items": [
  {"t": "Asesorar sobre la normativa", "d": "Asesorar al responsable, a su personal y al encargado sobre la LOPDP, su reglamento y las directrices, lineamientos y regulaciones de la SPDP.", "c": "LOPDP art. 49 num. 1",
   "como": ["Responder las consultas por escrito y con la norma citada.", "Emitir notas técnicas cuando cambie la normativa (nuevas resoluciones de la SPDP).", "Explicar a cada área sus obligaciones en lenguaje claro."], "herr": ["01"]},
  {"t": "Asesorar en riesgos, evaluación de impacto y medidas de seguridad", "d": "Asesorar en el análisis de riesgo, la evaluación de impacto y la evaluación de medidas de seguridad, incluidas las aplicables a las transferencias de datos.", "c": "LOPDP art. 49 num. 3; Res. 0028 art. 13.1",
   "como": ["Revisar que la metodología justifique cada valor de probabilidad e impacto (rationale).", "Emitir observaciones no vinculantes por escrito; no elaborar la evaluación por el cliente.", "Verificar que la evaluación de impacto se haga antes de iniciar el tratamiento."], "herr": ["07", "05"]},
  {"t": "Intervenir a tiempo en todo asunto de protección de datos", "d": "La organización debe garantizar que su participación en todas las cuestiones de protección de datos sea apropiada y oportuna.", "c": "LOPDP art. 50 num. 1",
   "como": ["Pedir que se le consulte antes de lanzar proyectos, sistemas, proveedores o campañas que traten datos.", "Dejar constancia cuando se le consulte tarde o no se le consulte."], "herr": []}]},
 {"eje": "Supervisar el cumplimiento", "items": [
  {"t": "Supervisar el cumplimiento normativo", "d": "Supervisar el cumplimiento de la LOPDP, el reglamento y las regulaciones de la SPDP en los tratamientos que se realicen.", "c": "LOPDP art. 49 num. 2; Res. 0028 art. 13.6",
   "como": ["Planificar revisiones periódicas por tratamiento del RAT.", "Medir el avance con el diagnóstico de madurez.", "Informar a la alta dirección con hallazgos, riesgos y recomendaciones."], "herr": ["03"]},
  {"t": "Supervisar la aplicación de riesgos, evaluación de impacto y medidas", "d": "Supervisar que el análisis de riesgo, la evaluación de impacto y las medidas de seguridad se apliquen.", "c": "LOPDP art. 49 num. 3",
   "como": ["Verificar que cada medida tenga responsable, plazo y evidencia de implementación.", "Revisar el riesgo residual tras las medidas."], "herr": ["07"]},
  {"t": "Controlar la eficacia y eficiencia de las medidas", "d": "Asesorar o supervisar el control de eficacia y eficiencia de las medidas técnicas, físicas, administrativas, organizativas y jurídicas implementadas.", "c": "Res. 0028 art. 13.4; LOPDP art. 37",
   "como": ["Pedir indicadores de cumplimiento (por ejemplo, tiempos de respuesta a derechos o incidentes).", "Revisar los informes de auditoría técnica hechos por especialistas."], "herr": []},
  {"t": "Supervisar el registro de actividades de tratamiento", "d": "Asesorar o supervisar el cumplimiento del RAT con los requisitos del reglamento y los que fije la SPDP.", "c": "Res. 0028 art. 13.5; RGLOPDP arts. 38 y 39",
   "como": ["Verificar los nueve contenidos mínimos por actividad.", "Comprobar que el RAT esté actualizado tras cada cambio relevante."], "herr": ["04"]},
  {"t": "Supervisar a los encargados", "d": "Sus funciones alcanzan al encargado. El encargado debe permitir que el responsable, o la persona que este determine, revise sus registros y procesos.", "c": "Res. 0028 art. 13; RGLOPDP art. 47",
   "como": ["Pedir al responsable que lo designe para revisar a los encargados críticos.", "Verificar contratos de encargo, medidas y avisos de vulneración en 2 días."], "herr": ["08"]},
  {"t": "Supervisar tratamientos especiales", "d": "Supervisar el cumplimiento de las normas especiales de la SPDP, como las de inteligencia artificial, biometría y gran escala.", "c": "LOPDP art. 49 num. 2; Res. 2026-0009 arts. 5 y 7; Res. 2026-0005 art. 12",
   "como": ["Inventariar herramientas de IA y sistemas biométricos.", "Verificar si hay gran escala y, en ese caso, la auditoría anual."], "herr": ["05", "07"]}]},
 {"eje": "Derechos de los titulares", "items": [
  {"t": "Supervisar la atención de solicitudes", "d": "Asesorar o supervisar la atención de las solicitudes de derechos. Se limita a supervisar que el responsable, su personal o el encargado ejecuten correctamente el procedimiento.", "c": "Res. 0028 arts. 13.2 y 14",
   "como": ["Revisar por muestreo el registro de solicitudes y las respuestas.", "Verificar el plazo de 15 días y la regla de aclaración en 5 días."], "herr": []},
  {"t": "Ser contactable por los titulares", "d": "El titular puede contactar al DPD para ejercer sus derechos; la identidad y los datos de contacto del DPD se informan cuando sea del caso.", "c": "LOPDP arts. 12 num. 9 y 50 num. 6",
   "como": ["Derivar la solicitud al canal del responsable y supervisar su respuesta.", "No resolver la solicitud por sí mismo."], "herr": ["08"]}]},
 {"eje": "Vulneraciones de la seguridad", "items": [
  {"t": "Asesorar o supervisar la gestión de vulneraciones", "d": "Asesorar o supervisar la gestión de vulneraciones y su notificación a los titulares, a la SPDP y al organismo competente.", "c": "Res. 0028 art. 13.3; LOPDP arts. 43 y 46",
   "como": ["Verificar que exista un protocolo con responsables y plazos.", "Acompañar la evaluación del riesgo; la notificación la presenta el responsable por el SISPDP.", "Conservar la línea de tiempo y la constancia de recepción."], "herr": ["09"]}]},
 {"eje": "Cooperación con la SPDP", "items": [
  {"t": "Ser punto de contacto con la SPDP", "d": "Cooperar con la SPDP y actuar como punto de contacto en las cuestiones de tratamiento de datos.", "c": "LOPDP arts. 4 y 49 num. 4",
   "como": ["Mantener un canal de comunicación con la SPDP.", "Informar al responsable de los requerimientos; no comparecer en su nombre."], "herr": []},
  {"t": "Funciones que fije la SPDP", "d": "Las demás que establezca la SPDP con ocasión de las categorías especiales de datos.", "c": "LOPDP art. 49 num. 5",
   "como": ["Revisar la pestaña Referencia tras cada resolución nueva."], "herr": []}]},
 {"eje": "Deberes propios del delegado", "items": [
  {"t": "Aceptar el cargo y verificar su registro", "d": "Firma la aceptación al pie del nombramiento y ejerce desde su otorgamiento. El responsable o encargado lo inscribe en la SPDP en el término de 15 días.", "c": "Res. 0028 arts. 4.7 y 5",
   "como": ["Pedir copia de la constancia de inscripción."], "herr": ["08"]},
  {"t": "Declarar los conflictos de intereses", "d": "Antes de aceptar, declara toda situación de conflicto real, potencial o aparente; lo mismo si surge durante el ejercicio.", "c": "Res. 0028 art. 17",
   "como": ["Usar la lista «Antes de aceptar» de esta pestaña y conservar la declaración firmada."], "herr": []},
  {"t": "Mantener independencia e imparcialidad", "d": "Total independencia e imparcialidad, incluso en relación de dependencia; no recibe instrucciones sobre sus funciones.", "c": "Res. 0028 arts. 12 y 15; RGLOPDP arts. 48 y 49",
   "como": ["Dejar por escrito las recomendaciones que la dirección no acoja."], "herr": []},
  {"t": "Guardar estricta confidencialidad", "d": "Mantiene la más estricta confidencialidad; suscribe un acuerdo que no puede limitar su acceso a la información necesaria y que subsiste al terminar la relación.", "c": "LOPDP art. 50 num. 7; RGLOPDP art. 57", "como": [], "herr": ["08"]},
  {"t": "Cumplir los requisitos y formarse", "d": "Derechos políticos, mayoría de edad, título de tercer nivel en Derecho, Sistemas de Información, Comunicación o Tecnologías y cinco años de experiencia; desde el 1 de enero de 2029, aprobar el programa profesionalizante.", "c": "RGLOPDP art. 55; Res. 0028 art. 11 y transitoria séptima",
   "como": ["Planificar el programa profesionalizante con una institución de educación superior aprobada por la SPDP (mínimo 80 horas)."], "herr": []},
  {"t": "Denunciar el menoscabo de su independencia", "d": "Denuncia ante la SPDP cualquier hecho que menoscabe su independencia o constituya represalia.", "c": "Res. 0028 arts. 19 y 20; RGLOPDP art. 51",
   "como": ["Conservar comunicaciones y evidencia de los hechos."], "herr": []},
  {"t": "Responder por el incumplimiento de sus funciones", "d": "Responde administrativa, civil y penalmente si incumple sus funciones; no responde por las decisiones finales del responsable si demuestra diligencia.", "c": "LOPDP art. 49 (inciso final); Res. 0028 art. 13 (inciso final)",
   "como": ["Trazabilidad: cada recomendación con fecha, destinatario, fundamento y respuesta de la dirección."], "herr": []}]},
]

# Lo que la organización debe garantizar al DPD (y que el DPD debe exigir).
GARANTIAS = [
 ["Participación apropiada y oportuna en todas las cuestiones de protección de datos.", "LOPDP art. 50 num. 1"],
 ["Acceso a los datos de las operaciones de tratamiento y a los recursos necesarios.", "LOPDP art. 50 num. 2; RGLOPDP art. 48"],
 ["Capacitación y actualización del delegado.", "LOPDP art. 50 num. 3"],
 ["No destituirlo ni sancionarlo por el correcto desempeño de sus funciones; si ocurre, puede llevarlo a la SPDP.", "LOPDP art. 50 num. 4; RGLOPDP art. 51; Res. 0028 art. 23"],
 ["Relación directa con el más alto nivel ejecutivo y de decisión.", "LOPDP art. 50 num. 5; Res. 0028 art. 22.1"],
 ["No darle instrucciones sobre sus funciones ni tomar represalias por su actuación técnica.", "Res. 0028 art. 15 (inciso final)"],
 ["Control anual de su independencia: contacto con la alta dirección, recursos técnicos, financieros y humanos, observaciones emitidas e informes de cumplimiento. Es institucional y no jerárquico; no lo ejecuta el DPD ni se usa para presionarlo.", "Res. 0028 art. 22"],
 ["Nombramiento con sus nueve contenidos e inscripción en la SPDP en el término de 15 días; el registro tardío se considera incumplimiento de una medida de seguridad jurídica.", "Res. 0028 arts. 4 y 5"],
 ["La inscripción no valida su idoneidad: la SPDP puede verificar los requisitos en cualquier momento.", "Res. 0028 art. 6"],
 ["Otras funciones solo si no generan conflicto ni exigen una preparación distinta.", "LOPDP art. 50 (inciso final); RGLOPDP art. 48"],
 ["Puede designarse un DPD único para un grupo empresarial, un DPD voluntario y un suplente.", "RGLOPDP arts. 50 y 52"],
]

PROHIBICIONES = [
 ["Implementar directamente en la organización la LOPDP, el reglamento y la normativa: es obligación del responsable, su personal o el encargado.", "Res. 0028 art. 15.1"],
 ["Ejecutar directamente la gestión de riesgos o la evaluación de impacto; solo emite observaciones u orientaciones no vinculantes.", "Res. 0028 art. 15.2"],
 ["Decidir la finalidad del tratamiento o los medios para realizarlo.", "Res. 0028 art. 15.3"],
 ["Representar a la organización ante la SPDP como responsable o encargado.", "Res. 0028 art. 15.4"],
 ["Ejercer a la vez como oficial de seguridad de la información, oficial de cumplimiento, implementador u otro cargo en conflicto.", "Res. 0028 art. 15.5"],
 ["Desempeñar cualquier función que comprometa su independencia, autonomía, imparcialidad u objetividad.", "Res. 0028 art. 15.6"],
 ["Ejecutar actividades de tratamiento o participar en su ejecución, ocasional o permanentemente.", "Res. 0028 art. 18.1"],
 ["Prestar asesorías ajenas a su función que busquen salvaguardar los intereses de la organización.", "Res. 0028 art. 18.2"],
 ["Tomar decisiones sobre la organización, sus actividades o sus gestiones internas.", "Res. 0028 art. 18.3"],
 ["Atender por sí mismo las solicitudes de derechos: solo supervisa el procedimiento.", "Res. 0028 art. 14"],
]

IMPEDIMENTOS = [
 ["Miembros de los órganos de administración y control del responsable o encargado.", "RGLOPDP art. 56 num. 1"],
 ["Socios o accionistas del responsable o encargado.", "RGLOPDP art. 56 num. 2"],
 ["Cónyuges de administradores, directores o comisarios, o sus parientes hasta el cuarto grado de consanguinidad o segundo de afinidad.", "RGLOPDP art. 56 num. 3"],
 ["Quienes tengan conflicto de intereses con el responsable o encargado.", "RGLOPDP art. 56 num. 4; Res. 0028 art. 18"],
 ["El oficial de seguridad de la información y el oficial de cumplimiento de la organización.", "Res. 0028 arts. 16.1 y 16.2"],
 ["Apoderados especiales de responsables o encargados extranjeros.", "Res. 0028 art. 16.3"],
 ["Cargos del nivel jerárquico superior en el sector público.", "Res. 0028 art. 16.4"],
]

# Qué NO es ser un DPO: [mito, realidad, cita]
NO_ES = [
 ["El responsable del cumplimiento", "La obligación de cumplir y demostrar el cumplimiento es del responsable. El DPD asesora y supervisa y, si fue diligente, no responde por las decisiones finales del responsable.", "LOPDP arts. 10 lit. k y 47; Res. 0028 arts. 13 (inciso final) y 15.1"],
 ["Quien implementa: hace el RAT, las políticas y la evaluación de impacto", "Tiene prohibido implementar directamente y ejecutar la gestión de riesgos o la evaluación de impacto; puede orientar con observaciones no vinculantes. La implementación se contrata como un servicio distinto.", "Res. 0028 arts. 12, 15.1 y 15.2"],
 ["El oficial de seguridad (CISO) o el oficial de cumplimiento con otro título", "Son cargos incompatibles: no pueden ser designados como DPD ni ejercer ambas funciones a la vez.", "Res. 0028 arts. 15.5, 16.1 y 16.2"],
 ["El representante o apoderado de la empresa ante la SPDP", "Es punto de contacto y coopera con la SPDP, pero no representa a la organización: ese rol es indelegable.", "LOPDP art. 49 num. 4; Res. 0028 arts. 15.4 y 16.3"],
 ["El abogado que defiende los intereses de la empresa", "Asesorar fuera de su función para salvaguardar los intereses de la organización es conflicto de intereses (por ejemplo, defenderla frente a un titular: ejemplo de criterio propio).", "Res. 0028 art. 18.2"],
 ["Quien responde las solicitudes de los titulares", "El titular puede contactarlo, pero quien atiende y responde es el responsable; el DPD supervisa el procedimiento.", "LOPDP art. 50 num. 6; RGLOPDP art. 42; Res. 0028 art. 14"],
 ["Quien decide qué datos se recogen y para qué", "Decidir fines y medios es lo que define al responsable; al DPD le está prohibido.", "LOPDP art. 4; Res. 0028 art. 15.3"],
 ["Un cargo para un directivo, socio o familiar de confianza", "Administradores, socios, parientes de directivos y cargos de nivel jerárquico superior en el sector público no pueden ser DPD.", "RGLOPDP art. 56; Res. 0028 art. 16.4"],
 ["Un empleado que obedece instrucciones", "Ejerce con total independencia, aun en relación de dependencia; no recibe instrucciones sobre sus funciones ni puede ser sancionado por ejercerlas.", "RGLOPDP arts. 48 y 51; Res. 0028 arts. 12 y 15"],
 ["Quien firma papeles para cumplir", "La SPDP exige cumplimiento real («el SER y no el DEBER SER») y la justificación de cada estimación de riesgo; las listas de chequeo no bastan.", "Guía v2, Cap. I, §§ 4 y 5; Cap. II, § 2.3"],
 ["Un auditor acreditado o un certificador", "La auditoría por auditor acreditado por la SPDP y la certificación o los sellos de entidades de certificación son figuras distintas. El informe del DPD es de supervisión, no una certificación.", "LOPDP arts. 47 num. 14 y 54"],
 ["Un trámite que termina con el nombramiento", "El nombramiento se inscribe en 15 días y la SPDP puede verificar en cualquier momento la idoneidad del delegado.", "Res. 0028 arts. 5 y 6"],
]

AUDITORIA = {
 "base": [
  ["Responsables y encargados deben auditar periódicamente el tratamiento. Auditar es verificar el cumplimiento en normas y riesgos de las obligaciones de la LOPDP. Se requieren auditorías jurídicas, organizacionales y técnicas.", "Guía v2, Cap. I, § 6.1 (obligatorio)"],
  ["Auditoría jurídica: constatar en la práctica los principios, los derechos y los registros. No basta que exista una política: los titulares deben tener mecanismos reales para ejercer sus derechos. Los auditores jurídicos deben ser expertos en protección de datos.", "Guía v2, Cap. I, § 6.2"],
  ["Auditoría organizacional: lo esencial es el cumplimiento en la práctica de las políticas y sistemas de gestión; auditores expertos en seguridad organizacional.", "Guía v2, Cap. I, § 6.3"],
  ["Auditoría técnica: vulnerabilidades de software y hardware; requiere especialistas (hacking ético, pruebas de penetración, respuesta a incidentes, informática forense).", "Guía v2, Cap. I, § 6.4"],
  ["El DPD revisa la veracidad de las auditorías de seguridad, audita los resultados de las auditorías jurídicas y de las evaluaciones de impacto, y pide ajustes en políticas, convenios con encargados y mecanismos de derechos.", "Guía v2, Cap. II, §§ 1.7 y 1.8 (referencial)"],
  ["Debe asesorar o supervisar el control de eficacia y eficiencia de las medidas; sus observaciones e informes de cumplimiento forman parte del control anual de su independencia.", "Res. 0028 arts. 13.4, 22.3 y 22.4"],
  ["El responsable implementa la verificación continua de las medidas y puede fijar indicadores de cumplimiento; el encargado debe permitir la revisión de sus registros y procesos.", "LOPDP arts. 37 y 47 num. 3; RGLOPDP arts. 36 y 47"],
  ["Gran escala: auditoría cada 12 meses e informes conservados 5 años. Inteligencia artificial: auditar el sistema según su nivel de riesgo.", "Res. 2026-0005 arts. 17 y 18; Res. 2026-0009 arts. 5.5 y 7.3"],
  ["Los resultados de auditorías pueden ser prueba en procesos sancionatorios: el informe debe ser riguroso y verificable.", "LOPDP art. 54"]],
 "principios": [
  ["Independencia", "No auditar lo que uno mismo implementó ni recibir instrucciones sobre el resultado.", "Res. 0028 arts. 15 y 18.1"],
  ["Evidencia antes que declaración", "Cada conclusión se apoya en documentos, registros o pruebas fechadas y verificables.", "Guía v2, Cap. I, § 6.2"],
  ["Enfoque en los titulares", "Priorizar lo que puede afectar sus derechos y libertades; ante conflicto prevalece su protección.", "Guía v2, Cap. I, § 1.2"],
  ["Justificación", "Todo nivel de riesgo asignado lleva su rationale.", "Guía v2, Cap. I, § 4"],
  ["Proporcionalidad", "Escalar la profundidad según tamaño, volumen y criticidad de los tratamientos.", "Guía v2, Cap. I, § 3.4"],
  ["Competencia", "Si el DPD no es especialista técnico, se apoya en informes de especialistas y los revisa.", "Guía v2, Cap. I, § 6.4"],
  ["Confidencialidad", "Los hallazgos y la evidencia se manejan con estricta reserva.", "LOPDP art. 50 num. 7"]],
 # Fases: criterio propio sobre la base normativa anterior.
 "fases": [
  {"n": "Planificar", "pasos": ["Definir el alcance por tratamientos del RAT, áreas y encargados.", "Fijar los criterios: normas aplicables (pestaña Referencia).", "Declarar conflictos y verificar que no se audita trabajo propio.", "Acordar el plan y el cronograma con la alta dirección.", "Enviar con anticipación la solicitud de evidencias."], "herr": ["04", "05"]},
  {"n": "Recolectar evidencia", "pasos": ["Revisión documental: políticas, contratos, registros, actas.", "Entrevistas que ayuden al entrevistado a calibrar sus estimaciones (Guía v2, Cap. II, § 3.7).", "Observación de los procesos en funcionamiento.", "Pruebas de recorrido: usar el canal de derechos o el formulario web como lo haría un titular.", "Muestreo de solicitudes, incidentes y contratos.", "Revisión de los informes técnicos de especialistas."], "herr": ["03"]},
  {"n": "Evaluar", "pasos": ["Contrastar cada hallazgo con el criterio aplicable.", "Clasificarlo (escala de criterio propio): no conformidad crítica, mayor o menor, observación u oportunidad de mejora.", "Vincularlo al artículo y, si corresponde, a la infracción (LOPDP arts. 67 y 68).", "Valorar el riesgo para los titulares con su justificación."], "herr": ["07"]},
  {"n": "Informar", "pasos": ["Informe escrito a la alta dirección (LOPDP art. 50 num. 5).", "Contenido: alcance, criterios, método, hallazgos con evidencia, riesgo, recomendación y prioridad.", "Las recomendaciones no son vinculantes: la dirección decide, fija responsables y plazos.", "Registrar la respuesta de la dirección a cada recomendación.", "Firma de responsabilidad con espacio para firma y sello."], "herr": []},
  {"n": "Dar seguimiento", "pasos": ["Verificar el cierre con evidencia, no con declaraciones.", "Actualizar el diagnóstico de madurez y la agenda.", "Repetir al menos una vez al año (obligatorio en gran escala) y ante cambios: sistemas nuevos, IA, biometría, encargados nuevos o un incidente."], "herr": ["03"]}],
 # [área, qué pedir o probar, cita, herramientas]
 "mapa": [
  ["Bases de legitimación y RAT", "RAT actualizado; base por actividad; excepción del art. 26 si hay datos sensibles.", "LOPDP arts. 7 y 26; RGLOPDP art. 38", ["04"]],
  ["Información y transparencia", "Política y avisos frente a los 17 elementos; prueba en el formulario real.", "LOPDP art. 12", ["08"]],
  ["Consentimiento", "Evidencia demostrable y procedimiento sencillo de revocatoria.", "LOPDP art. 8; RGLOPDP arts. 5 y 6", []],
  ["Derechos de los titulares", "Registro de solicitudes; muestra de respuestas en plazo; prueba del canal.", "LOPDP arts. 13 a 16; RGLOPDP arts. 12 a 15", []],
  ["Encargados y contratos", "Inventario de encargados; contrato con los siete contenidos; revisión de sus registros.", "RGLOPDP arts. 41 y 47; Res. 2025-0006", ["08"]],
  ["Riesgos y evaluación de impacto", "Metodología, justificación de valores y evaluación previa al tratamiento.", "LOPDP arts. 40 y 42; Guía v2", ["07", "05"]],
  ["Seguridad", "Informes técnicos, controles implementados e indicadores de eficacia.", "LOPDP art. 37; RGLOPDP art. 36", []],
  ["Vulneraciones", "Protocolo, registro de incidentes, constancias del SISPDP y plazos cumplidos.", "LOPDP arts. 43 y 46; Res. 2026-0040", ["09"]],
  ["Conservación y eliminación", "Plazos por categoría y evidencia de eliminación, incluso en respaldos.", "LOPDP art. 10 lit. i; RGLOPDP arts. 9 a 11", []],
  ["Transferencias internacionales", "Proveedores fuera del país y garantías o mecanismo aplicable.", "LOPDP arts. 56 a 60", ["04"]],
  ["Registro Nacional y DPD", "Inscripción de bases o tratamientos; nombramiento del DPD inscrito.", "LOPDP art. 47 nums. 12 y 13; Res. 0028 art. 5", []],
  ["Personal", "Contratos de confidencialidad con quienes tratan datos.", "LOPDP art. 47 num. 10", ["08"]],
  ["Tratamientos especiales", "IA, biometría y gran escala con sus obligaciones reforzadas.", "Res. 2026-0009; Res. 2026-0039; Res. 2026-0005", ["05", "07"]]],
 "errores": [
  ["Auditar solo documentos: la política existe, pero el canal no funciona.", "Guía v2, Cap. I, § 6.2"],
  ["Asignar niveles de riesgo sin justificación o con una lista de chequeo.", "Guía v2, Cap. I, § 4"],
  ["Autoauditarse: revisar lo que uno mismo implementó.", "Res. 0028 arts. 15.1 y 18.1"],
  ["Declarar «cumple» sin evidencia fechada y verificable.", "criterio propio"],
  ["Opinar sobre seguridad técnica sin informe de un especialista.", "Guía v2, Cap. I, § 6.4"],
  ["Entregar el informe a un mando medio y no a la alta dirección.", "LOPDP art. 50 num. 5"],
  ["Suavizar hallazgos por presión; ante represalias, denunciar.", "Res. 0028 art. 19"],
  ["Fijar por la empresa responsables y plazos: el DPD recomienda y la dirección decide.", "Res. 0028 art. 15.3"],
  ["No verificar el cierre de las recomendaciones.", "criterio propio"]],
}

# Lista de verificación antes de aceptar una designación. [texto, cita, clase] clase "i" = impedimento o conflicto; "g" = garantía.
ANTES = [
 ["No formo parte de los órganos de administración o control del cliente.", "RGLOPDP art. 56 num. 1", "i"],
 ["No soy socio ni accionista del cliente.", "RGLOPDP art. 56 num. 2", "i"],
 ["No soy cónyuge ni pariente (4.º de consanguinidad o 2.º de afinidad) de sus administradores, directores o comisarios.", "RGLOPDP art. 56 num. 3", "i"],
 ["No soy su oficial de seguridad de la información ni su oficial de cumplimiento.", "Res. 0028 arts. 16.1 y 16.2", "i"],
 ["No soy apoderado especial de un responsable o encargado extranjero.", "Res. 0028 art. 16.3", "i"],
 ["No ocupo un cargo del nivel jerárquico superior en el sector público.", "Res. 0028 art. 16.4", "i"],
 ["No ejecuto ni participo en tratamientos de datos del cliente.", "Res. 0028 art. 18.1", "i"],
 ["No le presto asesorías ajenas a la función para salvaguardar sus intereses.", "Res. 0028 art. 18.2", "i"],
 ["No tomo decisiones sobre la organización ni sus gestiones internas.", "Res. 0028 art. 18.3", "i"],
 ["No implemento la normativa ni ejecuto su gestión de riesgos o evaluación de impacto (si lo hice antes, lo declaro como conflicto potencial o aparente).", "Res. 0028 arts. 15.1, 15.2 y 17", "i"],
 ["Cumplo los requisitos: derechos políticos, mayoría de edad, título de tercer nivel afín y cinco años de experiencia.", "RGLOPDP art. 55", "g"],
 ["Tendré relación directa con la alta dirección, acceso a los datos y recursos.", "LOPDP art. 50 nums. 2 y 5", "g"],
 ["El acuerdo de confidencialidad no limita mi acceso a la información necesaria.", "RGLOPDP art. 57", "g"],
 ["El nombramiento tendrá sus nueve contenidos y se inscribirá en 15 días.", "Res. 0028 arts. 4 y 5", "g"],
]

ABIERTOS = [
 ["Riesgos: la guía v2 (Cap. II, referencial) pone al DPD a fijar criterios de riesgo y «auditar» informes, mientras la Res. 0028 art. 15.2 le prohíbe ejecutar la gestión de riesgos. Criterio de la app: el DPD propone, revisa y observa; el responsable aprueba y ejecuta.", "BASE-LEGAL, punto 30"],
 ["Vulneraciones: la Res. 0028 art. 13.3 aún nombra a la ARCOTEL; rige el art. 43 LOPDP reformado (organismo competente y CSIRT).", "BASE-LEGAL, punto 31"],
 ["Una misma firma como DPD e implementadora del mismo cliente: la norma no lo resuelve. Criterio adoptado en la app (2026-11-11): la evaluación y la supervisión se separan de la implementación; si MSC es DPO no implementa; la implementación la ejecuta el responsable, un proveedor o un tercero coordinado por MSC, de preferencia con contrato directo; si MSC subcontrata, personas distintas, declaración del art. 17 y consulta a la SPDP.", "BASE-LEGAL, punto 32"],
 ["Infracciones muy graves: el art. 66 num. 3 LOPDP las menciona, pero la ley no las tipifica ni les fija multa. Tampoco hay un catálogo de infracciones propio del DPD; su responsabilidad se rige por el art. 49 LOPDP y la Res. 0028 art. 13. La multa exacta depende del Anexo I de la Res. 0022, aún no cotejado.", "BASE-LEGAL, puntos 11 y 38"],
]

# ---------------- Quién puede ser DPD ----------------
# Los criterios de oficios de absolución de consultas se conocen por resúmenes de terceros (nmslaw.com.ec) y son
# opiniones referenciales, no vinculantes (Res. SPDP-SPDP-2024-0012-R arts. 1 y 2).
QUIEN = {
 "requisitos": [
  ["Ser persona natural: la función es personalísima. Una persona jurídica no puede ser DPD, pero puede prestar el servicio por medio de una persona natural, que responde personalmente.", "LOPDP art. 4; Oficio SPDP-IRD-2025-0277-O (resumen)"],
  ["Estar en goce de los derechos políticos.", "RGLOPDP art. 55 num. 1"],
  ["Ser mayor de edad.", "RGLOPDP art. 55 num. 2"],
  ["Título de tercer nivel en Derecho, Sistemas de Información, Comunicación o Tecnologías. No lo reemplazan cursos, diplomados, certificaciones ni el programa profesionalizante.", "RGLOPDP art. 55 num. 3; criterio SPDP de noviembre de 2025 (resumen)"],
  ["Experiencia profesional de al menos cinco años.", "RGLOPDP art. 55 num. 4"],
  ["Desde el 1 de enero de 2029, aprobar el programa profesionalizante oficializado por la SPDP; maestrías y certificaciones no son equivalentes.", "Res. 0028 art. 11 y transitoria séptima; Oficio SPDP-IRD-2025-0262-O (resumen)"],
  ["No estar incurso en impedimentos ni conflicto de intereses.", "RGLOPDP art. 56; Res. 0028 arts. 16 a 18"]],
 "computo": [
  ["Según la SPDP, los cinco años se cuentan desde la obtención del título de tercer nivel.", "Oficio SPDP-IRD-2025-0262-O (resumen)"],
  ["La experiencia no tiene que ser en protección de datos: basta que sea profesional en un área habilitada (Derecho, Sistemas de Información, Comunicación o Tecnologías).", "Oficio SPDP-IRD-2025-0262-O (resumen)"],
  ["La norma no dice cómo se prueba. Buena práctica (criterio propio): título registrado en la SENESCYT, certificados laborales o contratos, historial de aportes del IESS, matrícula profesional y facturas por servicios profesionales.", "criterio propio"],
  ["La calculadora suma solo los periodos posteriores al título y en área habilitada, sin contar dos veces los periodos que se superponen.", "criterio propio sobre el Oficio SPDP-IRD-2025-0262-O"]],
 "pueden": [
  ["Abogados (título de tercer nivel en Derecho).", "RGLOPDP art. 55 num. 3"],
  ["Profesionales de Sistemas de Información (por ejemplo, ingeniería o licenciatura en sistemas).", "RGLOPDP art. 55 num. 3"],
  ["Profesionales de Comunicación.", "RGLOPDP art. 55 num. 3"],
  ["Profesionales de Tecnologías (por ejemplo, tecnologías de la información, computación o software).", "RGLOPDP art. 55 num. 3"],
  ["Pueden ser internos (relación de dependencia) o externos (prestación de servicios); en el sector público lo designa la máxima autoridad.", "RGLOPDP art. 49; Res. 0028 art. 12"]],
 "no_pueden": [
  ["Profesionales de otras áreas (contabilidad, administración, psicología, medicina, entre otras) si no tienen además un título habilitante.", "RGLOPDP art. 55 num. 3"],
  ["Quien solo tiene cuarto nivel, diplomados o certificaciones en protección de datos sin título de tercer nivel habilitante.", "criterio SPDP de noviembre de 2025 (resumen)"],
  ["Una persona jurídica como tal.", "Oficio SPDP-IRD-2025-0277-O (resumen)"],
  ["Quienes tengan impedimentos: administradores, socios, parientes de directivos, oficial de seguridad o de cumplimiento, apoderados especiales y cargos de nivel jerárquico superior del sector público.", "RGLOPDP art. 56; Res. 0028 art. 16"]],
 "otros": [
  ["El DPD no puede registrar su propio nombramiento: lo hace el responsable o el encargado.", "Oficio SPDP-IRD-2025-0262-O (resumen)"],
  ["El DPD no debe custodiar contraseñas de bases de datos o sistemas: es control operativo y compromete su independencia.", "Oficio SPDP-IRD-2025-0279-O (resumen)"],
  ["Un DPD que no reside en el Ecuador no tiene régimen especial: cumple los mismos requisitos.", "Oficio SPDP-IRD-2025-0262-O (resumen)"]],
 "areas": [["der", "Derecho"], ["sis", "Sistemas de Información"], ["com", "Comunicación"], ["tec", "Tecnologías"], ["otra", "Otra área (no habilitada)"]],
}

# ---------------- Temas clave ----------------
TEMAS = [
 {"id": "separacion", "t": "Evaluación frente a implementación",
  "que": "El DPD evalúa, revisa, observa y verifica; no implementa. La implementación (elaborar el RAT, las ponderaciones, las evaluaciones de impacto, políticas, contratos y procedimientos, y ponerlos en marcha) la decide el responsable y la ejecuta su personal, un proveedor o un tercero.",
  "que_c": "Res. 0028 arts. 12, 13, 15.1 y 15.2",
  "ejemplos": ["El implementador elabora la evaluación de impacto; el DPD la revisa y emite observaciones no vinculantes.", "El área legal redacta los contratos de encargo; el DPD verifica que tengan el contenido del art. 41 del RGLOPDP.", "Un tercero coordinado por la firma implementa el protocolo de vulneraciones; el DPD verifica que funciona con un simulacro."],
  "implica": [
   ["El DPD no puede implementar directamente la normativa.", "Res. 0028 art. 15.1"],
   ["El DPD no ejecuta la gestión de riesgos ni la evaluación de impacto; puede emitir observaciones no vinculantes.", "Res. 0028 art. 15.2"],
   ["La organización puede contratar, aparte del DPD, implementación o consultoría con personas jurídicas.", "Res. 0028 art. 12"],
   ["Hay conflicto de intereses si el DPD ejecuta o participa en tratamientos; se declara antes de aceptar.", "Res. 0028 arts. 17 y 18"]],
  "dpd": ["Registrar en la ficha del cliente su rol (consultor o DPO) y quién implementa.", "Usar las herramientas 04, 06 y 07 en modo «Revisión del DPO» cuando sea DPO del cliente.", "Verificar lo implementado con evidencia (S30) y dejar constancia de cada observación y su respuesta.", "Si la firma coordina la implementación, preferir que el tercero contrate y facture directo y declarar la relación."],
  "exigir": ["Nombre del implementador y alcance de su contrato.", "Versiones fechadas de lo elaborado y respuesta escrita a cada observación.", "Evidencias de la puesta en marcha (documentos firmados, formularios publicados, registros)."],
  "herr": ["01", "02", "04", "06", "07"]},
 {"id": "perfiles", "t": "Elaboración de perfiles",
  "que": "Todo tratamiento de datos que permite evaluar, analizar o predecir aspectos de una persona para determinar comportamientos o estándares sobre su rendimiento profesional, situación económica, salud, preferencias, intereses, habilidad, ubicación o movimiento.",
  "que_c": "LOPDP art. 4",
  "ejemplos": ["Puntaje de crédito o de riesgo de cliente.", "Segmentación publicitaria por comportamiento de compra o navegación.", "Filtros automáticos de hojas de vida en selección de personal.", "Evaluación de desempeño con métricas automáticas o geolocalización de vendedores.", "Chatbots o sistemas de IA que clasifican a los usuarios."],
  "implica": [
   ["Informar al titular que existen valoraciones y decisiones automatizadas, incluida la elaboración de perfiles.", "LOPDP art. 12 num. 17"],
   ["El titular puede oponerse en todo momento a perfiles con fines de mercadotecnia directa.", "LOPDP art. 16 num. 2"],
   ["El titular puede no ser sometido a decisiones basadas única o parcialmente en valoraciones automatizadas con efectos jurídicos o que afecten sus derechos: pedir explicación motivada, presentar observaciones, conocer criterios, tipos de datos y fuente, e impugnar. Excepciones: contrato, autorización normativa, consentimiento explícito o falta de impacto grave.", "LOPDP art. 20"],
   ["Con datos sensibles o de niñas, niños y adolescentes se requiere autorización expresa o un interés público esencial con salvaguardas.", "LOPDP art. 21; RGLOPDP art. 19"],
   ["Evaluación de impacto obligatoria si hay evaluación sistemática y exhaustiva con decisiones de efectos jurídicos.", "LOPDP art. 42 lit. a"],
   ["Registrar en el RAT el uso de perfiles y, con IA, las decisiones automatizadas con efectos jurídicos.", "RGLOPDP art. 38 num. 5; Res. 2026-0009 art. 7.1"],
   ["Los perfiles automatizados con efectos jurídicos califican directamente como gran escala.", "Res. 2026-0005 art. 14"],
   ["No pueden basarse en el interés legítimo (salvo finanzas y seguros con salvaguardas).", "Res. 2025-0041 art. 16.3"],
   ["Las empresas de publicidad o investigación de mercados que perfilan deben designar DPD.", "Res. 0028 art. 10.6"],
   ["La información inferida por perfiles no entra en la portabilidad.", "LOPDP art. 17"]],
  "dpd": ["Identificar en el RAT cada tratamiento que perfila y si deriva en decisiones automatizadas.", "Asesorar sobre la base legal (consentimiento explícito, contrato o norma), nunca interés legítimo para perfiles con efectos.", "Exigir la evaluación de impacto antes de iniciar y revisar su justificación.", "Verificar que la política y los avisos informen los perfiles y cómo oponerse.", "Supervisar que exista intervención humana y un canal para explicar e impugnar decisiones.", "Revisar si el perfilamiento activa la gran escala o la obligación de designar DPD."],
  "exigir": ["Inventario de modelos, reglas o proveedores que perfilan (incluida la IA).", "Criterios de valoración, variables usadas y su fuente.", "Pruebas de sesgo o discriminación y responsable de revisión humana.", "Evidencia del consentimiento o del contrato que respalda la decisión.", "Procedimiento de oposición y de impugnación con plazos."],
  "herr": ["04", "07", "05"]},
 {"id": "rationales", "t": "Rationales (justificación de los valores de riesgo)",
  "que": "El rationale es el razonamiento de respaldo que sustenta cualquier valor de entrada de una gestión de riesgos (probabilidad, frecuencia, impacto, etiquetas de una matriz). Evita ingresar valores sin sustento que distorsionen el análisis.",
  "que_c": "Guía v2, Cap. I, §§ 0 y 4.1",
  "donde": [
   ["Es obligatorio justificar toda estimación cuantitativa o cualitativa del impacto en los derechos de los titulares.", "Guía v2, Cap. I, § 4.1 (obligatorio)"],
   ["Rige para el análisis de riesgos y la evaluación de impacto que exige la ley.", "LOPDP arts. 40 y 42; Guía v2, art. 2 de la resolución"],
   ["Toda evaluación de impacto debe adjuntar como anexos los documentos de respaldo de las métricas y modelos usados.", "Guía v2, anexo"],
   ["Se aplica también a los sistemas de IA y a la biometría, que remiten a la guía de riesgos vigente.", "Res. 2026-0009 arts. 5 y 6; Res. 2026-0039 (resumen)"],
   ["Forma parte del contenido mínimo del programa profesionalizante del DPD.", "Res. 0004, Anexo I, bloque 3"]],
  "tipos": [
   ["Cuantitativo", "Se apoya en datos: frecuencias históricas, estadística, Bayes, Monte Carlo, predicción conformal. Se expresa en rangos o distribuciones.", "Guía v2, Cap. I, § 4.2"],
   ["Cualitativo", "Se apoya en la opinión de expertos, idealmente calibrada (Delphi, Lens o análisis argumental). En pymes basta un experto que calibre sus opiniones.", "Guía v2, Cap. I, § 4.3"]],
  "pasos": ["Definir el escenario de riesgo y el lapso (por ejemplo, un año).", "Reunir la evidencia: registros de incidentes, reportes del SOC, auditorías, estadísticas del sector, sanciones de la SPDP.", "Elegir el método (cuantitativo o cualitativo) y aplicarlo.", "Expresar el valor en un rango, no en una cifra exacta.", "Escribir el rationale: qué dato, de qué fuente, con qué método y por qué ese valor.", "Adjuntar el respaldo como anexo y revisarlo cuando cambien las circunstancias."],
  "ejemplo": ["Escenario (ficticio): phishing con acceso a datos de clientes en el próximo año.", "Valor: entre 3 y 8 eventos al año.", "Rationale: promedio de los registros de incidentes de los últimos tres años [ADJUNTAR ANEXO], sin cambios relevantes en amenazas ni controles.", "Si no hay datos: cinco expertos consultados de forma anónima (método Delphi), promedio de sus estimaciones [ADJUNTAR ANEXO]."],
  "errores": [["Usar escalas de 1 a 3 y llamarlo análisis cuantitativo: los números son solo etiquetas.", "Guía v2, Cap. II, § 3.2"], ["Usar la matriz de riesgo para calibrar: la matriz solo representa.", "Guía v2, Cap. II, § 3.5"], ["Multiplicar probabilidad por impacto por defecto y ocultar riesgos de baja probabilidad y alto impacto.", "Guía v2, Cap. II, § 3.9"], ["Copiar valores de otra empresa o de una plantilla sin respaldo.", "Guía v2, Cap. I, § 4.1"]],
  "dpd": ["Revisar que cada valor tenga su rationale y su anexo; si falta, emitir observación escrita.", "Ayudar a los expertos internos a calibrar sus estimaciones mediante entrevistas.", "Proponer métodos de calibración (no fijar los valores por el responsable).", "Verificar que los rationales se actualicen tras un incidente o un cambio de sistema."],
  "exigir": ["Registros de incidentes y reportes de seguridad.", "Identidad y perfil de los expertos consultados y sus respuestas.", "Fuentes externas usadas (informes, sanciones, estadísticas).", "Memoria de cálculo o archivo del modelo."],
  "herr": ["07"]},
]

# ---------------- Infracciones, sanciones y actuación del DPD ----------------
# Fuente: LOPDP arts. 49, 65 a 73 y disposición general sexta; RGLOPDP art. 51; Res. 0028 arts. 13, 15 y 19 a 23.
# «Qué se exige para corregir» resume la obligación que la conducta incumple (norma citada).
# «Qué hace el DPD» y las prácticas de protección son criterio propio, salvo cita expresa.
INFRACCIONES = {
 "reglas": [
  ["Leve, sector privado o empresa pública: multa de 0,1 % a 0,7 % del volumen de negocio del ejercicio económico inmediatamente anterior.", "LOPDP art. 71 num. 2"],
  ["Grave, sector privado o empresa pública: multa de 0,7 % a 1 % del volumen de negocio del ejercicio anterior.", "LOPDP art. 72 num. 1"],
  ["Servidores públicos: leve de 1 a 10 SBU; grave de 10 a 20 SBU, sin perjuicio de la responsabilidad extracontractual del Estado.", "LOPDP arts. 71 num. 1 y 72"],
  ["Volumen de negocio: ventas de productos y servicios del último ejercicio, sin IVA ni otros impuestos ligados a la operación.", "LOPDP art. 73"],
  ["La SPDP fija la multa dentro del rango por proporcionalidad: intencionalidad, reiteración, naturaleza del perjuicio y reincidencia. La metodología de cálculo es el modelo MPRIV-1 (sector privado).", "LOPDP arts. 71 y 72; Res. SPDP-SPD-2025-0022-R"],
  ["Además de la multa, la SPDP dicta medidas correctivas: cese del tratamiento, eliminación de los datos o imposición de medidas técnicas, jurídicas, organizativas o administrativas.", "LOPDP art. 65"],
  ["Leve: si el infractor ya consta en el Registro Único de Responsables y Encargados Incumplidos, la SPDP inicia directamente el procedimiento sancionatorio, con medidas correctivas y sanción.", "LOPDP art. 66 num. 1; disposición general sexta"],
  ["Grave: primero medidas correctivas; si se cumplen tarde, en parte o de forma defectuosa, se sanciona.", "LOPDP art. 66 num. 2"],
  ["Reiterar faltas leves, o incumplir las medidas correctivas después de una sanción leve, se convierte en infracción grave.", "LOPDP art. 68 num. 14"],
  ["Notificar a tiempo una vulneración y ejecutar oportunamente medidas de respuesta son atenuantes.", "LOPDP art. 46"],
  ["El art. 66 num. 3 menciona infracciones «muy graves», pero la LOPDP no las tipifica ni fija su multa. Ver puntos abiertos.", "LOPDP art. 66 num. 3"]],
 "sectores": {
  "priv": {"t": "Sector privado y empresas públicas", "quien": "Se sanciona a la entidad (responsable o encargado) con multa sobre su volumen de negocio. Las empresas públicas siguen esta misma regla.", "c": "LOPDP arts. 71 num. 2, 72 num. 1 y 73",
   "notas": [["Base de la multa: volumen de negocio del ejercicio anterior, sin IVA.", "LOPDP art. 73"], ["Metodología de cálculo: modelo MPRIV-1.", "Res. SPDP-SPD-2025-0022-R"], ["El DPD es obligatorio en las causales de la Res. 0028 art. 10 y del RGLOPDP.", "LOPDP art. 48 nums. 2 y 3; Res. 0028 art. 10"]]},
  "pub": {"t": "Sector público", "quien": "Se sanciona a los servidores o funcionarios por cuya acción u omisión se cometió la infracción, con multa en salarios básicos unificados (SBU), sin perjuicio de la responsabilidad extracontractual del Estado.", "c": "LOPDP arts. 71 num. 1 y 72",
   "notas": [["Las conductas infractoras son las mismas de los arts. 67 a 70; cambia quién responde y la cuantía.", "LOPDP arts. 67 a 72"], ["Designar DPD es siempre obligatorio para las entidades del art. 225 de la Constitución.", "LOPDP art. 48 num. 1; Res. 0028 art. 9"], ["Las medidas de seguridad se rigen además por el mecanismo gubernamental de seguridad de la información.", "LOPDP art. 38"], ["No puede ser DPD quien ejerce un cargo del nivel jerárquico superior; la SPDP define otras incompatibilidades.", "Res. 0028 art. 16.4; RGLOPDP art. 56"], ["Metodología de cálculo para el sector público: modelo MPUB-1.", "Res. SPDP-SPD-2025-0022-R"]]}},
 "grupos": [
  {"id": "rl", "nivel": "Leve", "sujeto": "Responsable", "art": "LOPDP art. 67", "multa": {"priv": "0,1 % a 0,7 % del volumen de negocio del ejercicio anterior (art. 71 num. 2)", "pub": "1 a 10 SBU a los servidores o funcionarios por cuya acción u omisión se incurrió en la infracción (art. 71 num. 1)"}, "items": [
   {"t": "No tramitar, tramitar fuera del término o negar sin justificación las peticiones o quejas del titular.", "c": "art. 67 num. 1",
    "exige": "Canal operativo, registro de solicitudes y respuestas motivadas en término (LOPDP arts. 13 a 20 y 62; RGLOPDP arts. 12 a 15).",
    "dpd": "Revisar el registro, alertar por escrito las solicitudes vencidas y recomendar respuesta inmediata; no responder en nombre de la empresa.", "herr": ["08"]},
   {"t": "No implementar la protección de datos desde el diseño y por defecto.", "c": "art. 67 num. 2",
    "exige": "Medidas previas al tratamiento y ajustes por defecto (LOPDP art. 39; RGLOPDP arts. 59 y 60; Res. SPDP-SPD-2025-0040-R).",
    "dpd": "Pedir la evaluación de diseño y por defecto de cada proyecto nuevo y dejar observaciones no vinculantes antes de su lanzamiento.", "herr": ["08", "03"]},
   {"t": "No mantener disponibles políticas de protección de datos afines al tratamiento.", "c": "art. 67 num. 3",
    "exige": "Política de privacidad publicada y política interna aprobada y difundida (LOPDP arts. 12 y 47 num. 4).",
    "dpd": "Verificar que existan, que coincidan con el RAT y que el personal las conozca; recomendar su aprobación por escrito.", "herr": ["08"]},
   {"t": "Elegir un encargado que no ofrezca garantías suficientes.", "c": "art. 67 num. 4",
    "exige": "Evaluación previa del proveedor y contrato de encargo (LOPDP art. 47 num. 11; RGLOPDP arts. 41 y 47).",
    "dpd": "Revisar la evaluación de proveedores y el contrato; recomendar no entregar datos hasta que se firme.", "herr": ["08"]},
   {"t": "Incumplir las medidas correctivas dispuestas por la SPDP.", "c": "art. 67 num. 5",
    "exige": "Cumplir la medida en el plazo y la forma dispuestos (LOPDP arts. 65 y 66).",
    "dpd": "Hacer seguimiento documentado del cumplimiento e informar al más alto nivel si hay atraso.", "herr": []}]},
  {"id": "rg", "nivel": "Grave", "sujeto": "Responsable", "art": "LOPDP art. 68", "multa": {"priv": "0,7 % a 1 % del volumen de negocio del ejercicio anterior (art. 72 num. 1)", "pub": "10 a 20 SBU a los servidores o funcionarios por cuya acción u omisión se incurrió en la infracción (art. 72)"}, "items": [
   {"t": "No implementar medidas administrativas, técnicas, físicas, organizativas y jurídicas que garanticen un tratamiento conforme a la ley.", "c": "art. 68 num. 1",
    "exige": "Medidas documentadas y verificadas (LOPDP arts. 37 y 47 nums. 2 y 3).", "dpd": "Supervisar el registro de medidas y su verificación; dejar constancia de las brechas detectadas.", "herr": ["08", "03"],
    "pub": "En el sector público, las medidas se integran al mecanismo gubernamental de seguridad de la información, que también alcanza a concesionarios de servicios públicos (LOPDP art. 38)."},
   {"t": "Usar los datos para fines distintos a los declarados.", "c": "art. 68 num. 2",
    "exige": "Respetar la finalidad del RAT y de la política (LOPDP art. 10 lit. d).", "dpd": "Advertir por escrito el desvío y recomendar suspender ese uso o buscar una base legítima.", "herr": ["04"]},
   {"t": "Ceder o comunicar datos sin cumplir los requisitos legales.", "c": "art. 68 num. 3",
    "exige": "Base de legitimación y documento de transferencia (LOPDP arts. 33 a 36).", "dpd": "Revisar las comunicaciones del RAT y recomendar la cláusula de transferencia o detener la entrega.", "herr": ["04", "08"]},
   {"t": "No usar metodologías de análisis y gestión de riesgos adaptadas al tratamiento.", "c": "art. 68 num. 4",
    "exige": "Gestión de riesgos según la guía v2 (LOPDP arts. 40 y 47 num. 5; Res. SPDP-SPD-2026-0012-R).", "dpd": "Proponer la metodología y revisar los rationales; no ejecutar el análisis (Res. 0028 art. 15.2).", "herr": ["07"]},
   {"t": "No realizar evaluaciones de impacto cuando eran necesarias.", "c": "art. 68 num. 5",
    "exige": "Evaluación de impacto previa en los casos del art. 42 LOPDP.", "dpd": "Advertir por escrito que es obligatoria antes de iniciar y emitir observaciones no vinculantes.", "herr": ["07", "05"]},
   {"t": "No implementar medidas para prevenir, mitigar y controlar riesgos y vulneraciones identificados.", "c": "art. 68 num. 6",
    "exige": "Plan de tratamiento de riesgos ejecutado (LOPDP arts. 41 y 47 num. 7).", "dpd": "Hacer seguimiento a los riesgos residuales y recordar por escrito las medidas pendientes.", "herr": ["07", "08"]},
   {"t": "No notificar a la SPDP y al titular las vulneraciones que afecten derechos.", "c": "art. 68 nums. 7 y 8",
    "exige": "Notificación en 5 días a la SPDP, regulador y CSIRT, y en 3 días a los titulares (LOPDP arts. 43 y 46; Res. SPDP-SPD-2026-0040-R).", "dpd": "Asesorar desde la primera hora, calcular los términos y recomendar notificar; la firma es del responsable.", "herr": ["09"]},
   {"t": "No suscribir contratos de confidencialidad y tratamiento con el encargado y con el personal.", "c": "art. 68 num. 9",
    "exige": "Contrato de encargo y cláusulas de confidencialidad firmadas (LOPDP art. 47 num. 10).", "dpd": "Revisar por muestreo los expedientes y contratos y reportar los faltantes.", "herr": ["08"]},
   {"t": "No mantener actualizado o no consignar lo exigido en el Registro Nacional de Protección de Datos Personales.", "c": "art. 68 nums. 10 y 11",
    "exige": "Información del art. 51 LOPDP reportada y actualizada.", "dpd": "Comparar el RAT con lo reportado y recomendar la actualización.", "herr": ["04"]},
   {"t": "No designar al DPD cuando corresponde.", "c": "art. 68 num. 12",
    "exige": "Designación y registro ante la SPDP (LOPDP arts. 47 num. 13 y 48; Res. SPDP-SPD-2025-0028-R).", "dpd": "Si es candidato, verificar que el nombramiento se registre; el registro tardío es incumplimiento de una medida jurídica (Res. 0028 art. 5).", "herr": ["08"],
    "priv": "En el sector privado, la obligación depende de las causales de la Res. 0028 art. 10 y del RGLOPDP (control permanente y sistematizado, gran escala de categorías especiales).",
    "pub": "En el sector público, designar DPD es siempre obligatorio (LOPDP art. 48 num. 1; Res. 0028 art. 9). No pueden ser DPD quienes ejercen cargos del nivel jerárquico superior (Res. 0028 art. 16.4)."},
   {"t": "No permitir ni contribuir a auditorías o inspecciones del auditor acreditado por la SPDP.", "c": "art. 68 num. 13",
    "exige": "Facilitar el acceso y la información (LOPDP art. 47 num. 14).", "dpd": "Actuar como punto de contacto y recomendar cooperación plena con la SPDP (LOPDP art. 49 num. 4).", "herr": []},
   {"t": "Incumplir medidas correctivas después de una sanción leve, o reiterar faltas leves.", "c": "art. 68 num. 14",
    "exige": "Cumplimiento completo y oportuno de las medidas correctivas.", "dpd": "Escalar al más alto nivel con un informe de riesgo de sanción grave.", "herr": []}]},
  {"id": "el", "nivel": "Leve", "sujeto": "Encargado", "art": "LOPDP art. 69", "multa": {"priv": "0,1 % a 0,7 % del volumen de negocio del ejercicio anterior (art. 71 num. 2)", "pub": "1 a 10 SBU a los servidores o funcionarios por cuya acción u omisión se incurrió en la infracción (art. 71 num. 1)"}, "items": [
   {"t": "No colaborar con el responsable para atender las solicitudes de derechos.", "c": "art. 69 num. 1", "exige": "Cláusula de colaboración en el contrato de encargo y respuesta oportuna.", "dpd": "Revisar que el contrato la incluya y que el encargado conteste a tiempo.", "herr": ["08"]},
   {"t": "No facilitar al responsable la información sobre el cumplimiento de sus obligaciones.", "c": "art. 69 num. 2", "exige": "Entregar la información pedida (RGLOPDP art. 47).", "dpd": "Recomendar requerimientos por escrito y registrar las respuestas.", "herr": ["08"]},
   {"t": "No permitir auditorías o inspecciones del responsable o de un auditor autorizado.", "c": "art. 69 num. 3", "exige": "Permitir la revisión de registros y procesos (RGLOPDP art. 47).", "dpd": "Incluir al encargado en el plan de supervisión y documentar la negativa.", "herr": ["08"]},
   {"t": "Incumplir las medidas correctivas de la SPDP.", "c": "art. 69 num. 4", "exige": "Cumplir la medida dispuesta.", "dpd": "Hacer seguimiento y advertir al responsable.", "herr": []}]},
  {"id": "eg", "nivel": "Grave", "sujeto": "Encargado", "art": "LOPDP art. 70", "multa": {"priv": "0,7 % a 1 % del volumen de negocio del ejercicio anterior (art. 72 num. 1)", "pub": "10 a 20 SBU a los servidores o funcionarios por cuya acción u omisión se incurrió en la infracción (art. 72)"}, "items": [
   {"t": "Tratar datos sin observar los principios y derechos de la ley.", "c": "art. 70 num. 1", "exige": "Tratamiento conforme a la LOPDP.", "dpd": "Recomendar al responsable revisar al encargado y, si es necesario, suspender el encargo.", "herr": ["08"]},
   {"t": "No tratar los datos según el contrato con el responsable, incluidas las transferencias internacionales.", "c": "art. 70 num. 2", "exige": "Cumplir las instrucciones del contrato (LOPDP art. 34).", "dpd": "Verificar el cumplimiento del contrato en la supervisión.", "herr": ["08"]},
   {"t": "No suscribir contratos de confidencialidad con su personal.", "c": "art. 70 num. 3", "exige": "Cláusulas firmadas por el personal del encargado.", "dpd": "Pedir evidencia por muestreo.", "herr": ["08"]},
   {"t": "No implementar mecanismos de confidencialidad, integridad, disponibilidad y resiliencia.", "c": "art. 70 num. 4", "exige": "Medidas de seguridad del encargado (LOPDP art. 37).", "dpd": "Pedir el informe de seguridad del encargado.", "herr": ["08"]},
   {"t": "No implementar medidas preventivas y correctivas de seguridad.", "c": "art. 70 num. 5", "exige": "Plan de seguridad del encargado.", "dpd": "Revisar incidentes y acciones correctivas del encargado.", "herr": ["08"]},
   {"t": "No suprimir los datos al terminar el encargo.", "c": "art. 70 num. 6", "exige": "Devolución o eliminación con constancia (LOPDP art. 34; RGLOPDP art. 46).", "dpd": "Pedir el acta de eliminación al cierre del contrato.", "herr": ["08"]},
   {"t": "Comunicar datos sin cumplir los requisitos legales.", "c": "art. 70 num. 7", "exige": "Prohibición de comunicar sin instrucción (LOPDP art. 34).", "dpd": "Recomendar acciones contractuales y evaluar si hubo vulneración.", "herr": ["09"]},
   {"t": "Incumplir medidas correctivas después de una sanción leve.", "c": "art. 70 num. 8", "exige": "Cumplimiento completo y oportuno.", "dpd": "Informar al responsable el riesgo de mantener el encargo.", "herr": []},
   {"t": "No notificar al responsable una vulneración, o hacerlo con retraso injustificado.", "c": "art. 70 num. 9", "exige": "Notificar en el término de 2 días (LOPDP art. 43).", "dpd": "Verificar que el contrato fije el canal y el término y probarlo en un simulacro.", "herr": ["09"]}]}],
 "actuar": [
  ["Detectar y documentar: qué conducta, desde cuándo, qué tratamiento y qué evidencia existe.", "Criterio propio"],
  ["Informar por escrito y sin demora al más alto nivel ejecutivo, con la norma incumplida, el riesgo para los titulares y el rango de multa.", "LOPDP art. 50 num. 5; Res. 0028 art. 22.3"],
  ["Recomendar las medidas para corregir y un plazo; la empresa decide y ejecuta.", "LOPDP art. 49 nums. 1 y 2; Res. 0028 art. 15.1"],
  ["Si hay vulneración de seguridad, activar el protocolo y los términos de notificación desde la primera hora.", "LOPDP arts. 43 y 46"],
  ["Hacer seguimiento hasta el cierre y registrarlo en el informe de supervisión.", "Res. 0028 art. 22.4"],
  ["Si la SPDP inicia un procedimiento, actuar como punto de contacto y cooperar; no representar a la empresa como responsable.", "LOPDP art. 49 num. 4; Res. 0028 art. 15.4"]],
 "protege": [
  ["El DPD responde administrativa, civil y penalmente si incumple sus funciones.", "LOPDP art. 49, último párrafo"],
  ["No responde por las decisiones finales del responsable o del encargado si demuestra que actuó con diligencia: la prueba es su archivo de recomendaciones.", "Res. 0028 art. 13, último párrafo"],
  ["No puede ser destituido ni sancionado por cumplir sus funciones; si lo es, puede ponerlo en conocimiento de la SPDP.", "LOPDP art. 50 num. 4; RGLOPDP art. 51"],
  ["Debe denunciar ante la SPDP todo hecho que menoscabe su independencia o sea represalia; la SPDP investiga y puede sancionar al responsable.", "Res. 0028 arts. 19 a 21 y 23"],
  ["La organización evalúa cada año, sin que la evaluación la haga el DPD, su independencia: contacto con la alta dirección, recursos, observaciones emitidas e informes.", "Res. 0028 art. 22"],
  ["No ejecutar, no decidir y no firmar como responsable: hacerlo genera conflicto y traslada responsabilidad.", "Res. 0028 arts. 15 y 18"],
  ["Toda observación por escrito, fechada y con constancia de recepción; nunca solo verbal.", "Criterio propio"],
  ["Contrato o nombramiento que delimite el alcance (asesorar y supervisar) y el deber de la empresa de entregar información.", "Criterio propio; LOPDP art. 50 num. 2"],
  ["Conservar el expediente de supervisión al menos mientras puedan iniciarse acciones en su contra.", "Criterio propio"],
  ["Valorar un seguro de responsabilidad civil profesional.", "Criterio propio"]]}
