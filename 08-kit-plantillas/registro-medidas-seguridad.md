# Registro y Verificación de Medidas de Seguridad

**[RAZÓN SOCIAL]** · RUC [RUC] · Versión [VERSIÓN] · Corte al [FECHA]

> **Nota para quien redacta (eliminar antes de usar):**
> - Base: LOPDP arts. 10 lit. j (principio de seguridad), 37 (medidas y verificación continua de su eficacia, con evidencia de que mitigan los riesgos), 41 (factores para determinar las medidas), 47 nums. 2, 3, 6 y 7 (implementar medidas, verificarlas periódicamente, evaluar la adecuación de la seguridad **antes** del tratamiento, y prevenir y mitigar riesgos) y 68 nums. 1 y 6 (no implementarlas es infracción grave). RGLOPDP art. 38 num. 9: el RAT describe las medidas técnicas, jurídicas, administrativas y organizativas.
> - **Quién hace qué:** la empresa elige, implementa y documenta las medidas. El DPD asesora en la evaluación de medidas y supervisa su aplicación (LOPDP art. 49 num. 3; Res. SPDP-SPD-2025-0028-R art. 13.4); no las implementa ni ejerce como oficial de seguridad de la información (art. 15.5).
> - Las medidas se eligen a partir del análisis de riesgos (herramienta 07 y calculadora de riesgos): cada medida debe responder a un riesgo identificado. Este registro no reemplaza una auditoría técnica hecha por especialistas.
> - La escala de eficacia de la parte C es de **criterio propio**.

## A. Contexto (art. 41 LOPDP)

| Factor | Descripción | Fuente |
|---|---|---|
| Resultado del análisis de riesgos | [RIESGOS PRINCIPALES Y NIVEL] | Herramienta 07 / informe de riesgos del [FECHA] |
| Naturaleza de los datos | [Datos comunes / sensibles / de NNA / biométricos / crediticios] | RAT |
| Partes involucradas | [Áreas, encargados, destinatarios] | RAT |
| Antecedentes de vulneraciones o accesos indebidos | [INCIDENTES DE LOS ÚLTIMOS 24 MESES O «NINGUNO REGISTRADO»] | Bitácora de vulneraciones |
| Volumen y alcance | [N.º APROXIMADO DE TITULARES Y REGISTROS] | RAT / herramienta 05 |

## B. Inventario de medidas

> Una fila por medida. «Tipo» sigue la clasificación del art. 47 num. 2 LOPDP. «Actividad del RAT» enlaza la medida con el tratamiento que protege.

| Código | Medida | Tipo (técnica, física, organizativa, administrativa, jurídica) | Actividad del RAT que protege | Riesgo que mitiga | Propietario | Estado (implementada, en curso, planificada) | Fecha de implementación | Evidencia (documento, captura, registro) |
|---|---|---|---|---|---|---|---|---|
| MS-01 | [Ej.: cifrado de los equipos portátiles] | Técnica | [ACTIVIDAD] | [Pérdida o robo del equipo] | [CARGO] | | | |
| MS-02 | [Ej.: copias de respaldo diarias con prueba de restauración trimestral] | Técnica | [ACTIVIDAD] | [Pérdida de disponibilidad] | [CARGO] | | | |
| MS-03 | [Ej.: control de accesos por perfil y revisión semestral] | Técnica / organizativa | [ACTIVIDAD] | [Acceso no autorizado] | [CARGO] | | | |
| MS-04 | [Ej.: archivadores con llave para expedientes en papel] | Física | [ACTIVIDAD] | [Acceso indebido a papel] | [CARGO] | | | |
| MS-05 | [Ej.: compromisos de confidencialidad del personal] | Jurídica | Todas | [Divulgación por personal] | [CARGO] | | | |
| MS-06 | [Ej.: contratos de encargo con cada proveedor] | Jurídica | [ACTIVIDAD] | [Tratamiento indebido por el encargado] | [CARGO] | | | |
| MS-07 | [Ej.: procedimiento de altas y bajas de usuarios] | Administrativa | Todas | [Accesos de personal que ya salió] | [CARGO] | | | |
| MS-08 | [Ej.: protocolo de respuesta a vulneraciones aprobado] | Organizativa | Todas | [Respuesta tardía a incidentes] | [CARGO] | | | |

### Medidas que la LOPDP menciona expresamente (art. 37)

Marque si la empresa las aplica y, si no, anote la razón (no son obligatorias en todos los casos, pero su ausencia debe estar justificada por el análisis de riesgos).

| Medida del art. 37 | ¿Se aplica? | Código en el inventario o razón de su ausencia |
|---|---|---|
| 1. Anonimización, seudonimización o cifrado | | |
| 2. Confidencialidad, integridad y disponibilidad permanentes; acceso rápido a los datos en caso de incidente | | |
| 3. Resiliencia técnica, física, administrativa y jurídica | | |
| 4. Adopción de estándares internacionales de gestión de riesgos o de seguridad de la información, o de códigos de conducta autorizados por la SPDP | | |

## C. Verificación de la eficacia (art. 37 incisos 2 y 3; art. 47 num. 3)

> Escala de **criterio propio:** 0 = no existe; 1 = existe pero no funciona o no hay evidencia; 2 = funciona con fallas; 3 = funciona y hay evidencia de que mitiga el riesgo.

| Código | Cómo se verificó (prueba, muestreo, revisión documental, entrevista) | Fecha | Resultado (0 a 3) | Hallazgo | Acción correctiva | Responsable | Fecha compromiso |
|---|---|---|---|---|---|---|---|
| MS-01 | | | | | | | |
| MS-02 | | | | | | | |
| MS-03 | | | | | | | |

## D. Evaluación de adecuación antes de un nuevo tratamiento (art. 47 num. 6)

Complete esta parte antes de poner en marcha un tratamiento nuevo o un cambio importante.

| Pregunta | Respuesta |
|---|---|
| Tratamiento o proyecto | [NOMBRE] |
| ¿Está en el RAT con finalidad, base y plazo? | [Sí / No] |
| ¿Se analizaron sus riesgos? ¿Requiere evaluación de impacto (art. 42)? | [Sí / No · referencia] |
| Medidas existentes que lo cubren | [CÓDIGOS] |
| Medidas nuevas necesarias antes de empezar | [DETALLE] |
| ¿Interviene un encargado? ¿Firmó contrato de encargo? | [Sí / No] |
| ¿Hay transferencia internacional o servicio en la nube en el exterior? | [Sí / No · mecanismo] |
| Conclusión de la empresa | [Puede iniciar / Puede iniciar con condiciones / No puede iniciar] |
| Observación del DPD (no vinculante) | [OBSERVACIÓN] |

## E. Revisión

| Fecha de revisión | Motivo (periódica, cambio de tratamiento, vulneración, cambio normativo) | Revisado por | Cambios principales |
|---|---|---|---|
| [FECHA] | | | |
