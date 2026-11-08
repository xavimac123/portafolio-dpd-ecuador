# Metodología del RAT: qué se adoptó de la práctica comparada

Fecha: 2026-11-08 · Herramienta 01, v0.4

## Contexto

Se revisó la metodología de la Agencia Española de Protección de Datos (AEPD) para elaborar el registro de actividades de tratamiento, que desarrolla el art. 30 del RGPD europeo, y se pidió considerar también las guías de DPO Partners (Chile, Ley 21.719) y Wiibiq (Ecuador, LOPDP).

**Limitación de fuentes:** las tres páginas indicadas por el usuario no fueron accesibles desde el entorno de trabajo. La comparación con la AEPD se hizo con base en el art. 30 RGPD y en los criterios conocidos de sus guías públicas. **No se incorporó contenido de DPO Partners ni de Wiibiq.** Antes de citarlas en un documento para clientes, deben leerse directamente (ver "Referencias comparadas" en `BASE-LEGAL.md`).

Las referencias europeas son comparativas y no vinculantes en Ecuador. La herramienta solo exige lo que dicen la LOPDP y el RGLOPDP; lo demás se rotula como **buena práctica**.

## Qué se adoptó y cómo se adaptó

| Criterio de la práctica comparada (AEPD / RGPD) | Adaptación al Ecuador | Dónde está |
|---|---|---|
| El registro se organiza por **actividad o finalidad**, no por base de datos ni por programa | Guía en la hoja Instrucciones y en el asistente; alerta de finalidad genérica; sugerencia de separar la publicidad de otras finalidades | `rat_config.py`: `FINALIDADES_GENERICAS`, `FINALIDAD_SEPARABLE` |
| Levantamiento por áreas, con entrevistas a cada unidad | Paso 3 de las instrucciones y hoja Catálogo con actividades frecuentes | Hoja "Catálogo"; sugerencias en el asistente |
| Distinguir el contenido obligatorio del recomendable | Fila "Art. 38 num. X / Buena práctica" y dos columnas de control: faltantes del mínimo legal y observaciones | Hoja RAT, columnas finales |
| Contenido mínimo del responsable (art. 30.1 RGPD) | Se reemplaza por los 9 numerales del **art. 38 RGLOPDP**, que además exige indicar el uso de perfiles y las bases legitimadoras (el RGPD no las exige en el registro) | Campos con `min` |
| Registro propio del encargado (art. 30.2 RGPD) | Hoja separada, exigible solo cuando el responsable está obligado (**art. 44 RGLOPDP**). Su contenido es de buena práctica hasta confirmar el texto del art. 44 | Hoja "RAT encargado" |
| Descripción **general** de las medidas, sin detalles que debiliten la seguridad | Nota en el campo de medidas | Comentario del encabezado |
| Vincular el registro con el análisis de riesgos y la evaluación de impacto | Nivel de riesgo orientativo y campo de evaluación de impacto con referencia (**art. 42 LOPDP**) | Sección 6 |
| Identificar sistemas y soportes donde residen los datos | Campo "Sistemas y soportes", útil para la Herramienta 03 (vulneraciones) | Sección 5 |
| Registro vivo: responsable interno, fecha de alta, revisiones | Responsable interno, fecha de alta, última y próxima revisión, alerta de revisión vencida | Secciones 1 y 7 |
| Relación con encargados y contratos | Campo de contrato de encargo y alerta (**art. 41 RGLOPDP; art. 68 num. 9 LOPDP**) | Sección 4 |

## Revisión de DPO Partners y Wiibiq (2026-11-07, v0.5)

Ambas páginas se leyeron directamente. Son contenido comercial sin plantillas descargables.

| Fuente | Qué se adoptó | Dónde |
|---|---|---|
| DPO Partners (Chile) | Ámbito o entidad para registros de grupos; disparadores de actualización por eventos; vínculo del RAT con la evaluación de transferencias | Campos `entidad`, `evento`, `tia` |
| Wiibiq (Ecuador) | Organización por macroprocesos; lista de eventos que obligan a actualizar | Campos `macro`, `evento` |

**No se adoptó de Wiibiq:** (1) atribuye el contenido mínimo del RAT al art. 13 LOPDP; en el portafolio rige el **art. 38 RGLOPDP**; (2) cita la Res. SPDP-SPD-2025-0028-R para transferencias internacionales, pero esa resolución regula al DPD; (3) recomienda revisión trimestral sin base normativa. Sus citas no deben usarse sin contraste con el Registro Oficial.

## Qué no se adoptó

- **Umbral de 250 trabajadores y sus excepciones (art. 30.5 RGPD):** en Ecuador rigen los 100 trabajadores del art. 38 y las causales del art. 39 RGLOPDP.
- **Publicación del inventario de actividades por el sector público:** no consta en la base legal del portafolio.
- **Terminología europea** ("interesado", "licitud", "EIPD"): se usa la de la LOPDP.

## Decisiones propias que no vienen de la norma

1. **Nivel de riesgo orientativo.** Suma puntos por categorías especiales (2), perfiles (2), NNA (1), transferencia internacional (1), datos financieros o de geolocalización (1 cada uno) y volumen (1 o 2). Alto desde 4, Medio desde 2. Es un filtro para priorizar, no una evaluación de riesgos ni de impacto. Ajustable en `RIESGO`.
2. **Revisión cada 12 meses.** La norma no fija periodicidad; es práctica interna, ajustable en `REVISION_MESES`.
3. **Catálogo de actividades.** Las bases y notas son sugerencias de partida. Nunca se cargan sin acción del usuario y solo llenan campos vacíos. Los plazos se dejan con "(indicar)" para no afirmar plazos legales no verificados.
