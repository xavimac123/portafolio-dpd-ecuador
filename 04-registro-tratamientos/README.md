# 04 · Registro de Actividades de Tratamiento (RAT)

## Propósito

Documentar cada actividad de tratamiento de datos personales con el contenido mínimo exigido por el art. 38 del Reglamento General a la LOPDP y detectar automáticamente los vacíos.

## A quién va dirigida

Responsables del tratamiento (empresas, profesionales, instituciones) y DPD que preparan o auditan el registro.

## Archivos

| Archivo | Uso |
|---|---|
| `plantilla-RAT.xlsx` | Plantilla para completar: obligatoriedad, responsable, RAT por secciones con control automático, RAT del encargado, catálogo de actividades y resumen. |
| `ejemplo-RAT-ficticio.xlsx` | Clínica dental ficticia con 6 actividades: 2 completas y 4 con errores intencionales, útil para capacitaciones y demostraciones. |
| `asistente-rat.html` | Versión web interactiva: verifica obligatoriedad, registra actividades con sugerencias del catálogo, importa un RAT existente pegado desde Excel, muestra estado, riesgo y alertas, y copia el registro con firma de responsabilidad. |
| `../scripts/rat_config.py` | **Fuente única** de campos, secciones, listas, catálogo, criterio de riesgo y preguntas de obligatoriedad. Para agregar un campo u opción, edita este archivo y regenera ambos formatos. |
| `../scripts/generar_rat.py` · `../scripts/generar_asistente_rat.py` | Regeneran el Excel y el asistente web desde la configuración. |

## ¿Está obligada la organización?

16 preguntas en cinco grupos (rol, tamaño, habitualidad, categorías especiales y riesgo), cada una con una ayuda de **Qué significa** y **Qué dice la norma**. El resultado indica la causal concreta que obliga (o qué falta responder) y advierte la regla del encargado (art. 44 RGLOPDP). Las ayudas son resúmenes fieles de la norma; al incorporar el texto literal, cambia `literal` a `True` en `rat_config.py`.

## Listas desplegables con "Otro"

Actividad, área, finalidades, titulares, categorías de datos, origen, destinatarios, encargados, garantía de transferencia, plazo y medidas se eligen de listas. Si la opción no existe, se elige **Otro** y se escribe. En el asistente web las categorías especiales aparecen en rojo y marcan automáticamente la actividad. En el Excel, las listas aceptan texto libre; para varios valores se separan con punto y coma.

## Base legal

- RGLOPDP art. 38: obligación (100 o más trabajadores) y contenido mínimo de 9 elementos.
- RGLOPDP art. 39: extensión a organizaciones con menos de 100 trabajadores (riesgo, tratamiento no ocasional, categorías especiales).
- RGLOPDP art. 44: registro del encargado.
- LOPDP art. 7: bases legitimadoras.
- Res. SPDP-SPD-2025-0041-R: interés legítimo y evaluación de ponderación.

Estado de verificación de cada norma: ver [BASE-LEGAL.md](../BASE-LEGAL.md).

## Cómo delimitar una actividad

Una fila = una actividad de tratamiento, definida por su **finalidad**, no por la base de datos ni el programa. Si dos finalidades tienen bases legitimadoras o plazos distintos (por ejemplo, prestar el servicio y enviar publicidad), van en filas separadas. Levanta el registro recorriendo cada área de la organización; la hoja "Catálogo" sugiere actividades frecuentes.

## Estructura del registro

| Sección | Campos | Art. 38 RGLOPDP |
|---|---|---|
| 1 · Identificación | ID, actividad, área, responsable interno, descripción | — (buena práctica) |
| 2 · Finalidad y legitimación | Finalidades · Base legitimadora · Ref. interés legítimo | num. 2 · num. 7 |
| | Excepción del art. 26 (si hay datos sensibles) · Cómo se informa al titular | buena práctica (LOPDP arts. 26 y 12) |
| 3 · Titulares y datos | Categorías de titulares · Categorías de datos | num. 4 |
| | Volumen, categorías especiales, NNA, origen | buena práctica |
| 4 · Comunicaciones | Destinatarios · Transferencia, país y garantía · Perfiles | num. 3 · num. 6 · num. 5 |
| | Encargados y contrato de encargo | buena práctica (RGLOPDP art. 41) |
| 5 · Conservación y seguridad | Plazo · Medidas | num. 8 · num. 9 |
| | Sistemas y soportes | buena práctica |
| 6 · Riesgo | Nivel de riesgo orientativo (automático) · Evaluación de impacto y referencia | buena práctica (LOPDP art. 42) |
| 7 · Control | Fecha de alta, última revisión, próxima revisión (automática) | buena práctica |

El numeral 1 (contacto del responsable, corresponsable y DPD) está en la hoja "Responsable".

## Control automático

Cada fila tiene un **Estado**:

- **Incompleto:** falta algún contenido del art. 38 (columna "Faltantes del mínimo legal").
- **Mínimo cumplido:** el art. 38 está cubierto, pero hay observaciones (columna "Observaciones y recomendaciones").
- **Completo:** sin faltantes ni observaciones.

Observaciones que se generan: finalidad genérica; publicidad mezclada con otras finalidades; datos especiales no marcados; datos sensibles sin excepción del art. 26; NNA con consentimiento; titular no informado; encargados sin contrato completo; plazo genérico; sin sistemas, volumen o responsable interno; evaluación de impacto sin definir o sin referencia; revisión ausente o vencida.

## Nivel de riesgo orientativo

Suma: categorías especiales 2, perfiles 2, NNA 1, transferencia internacional 1, datos financieros 1, geolocalización 1, volumen de 1.001 a 10.000 titulares 1, más de 10.000 titulares 2. **Alto** desde 4, **Medio** desde 2, **Bajo** el resto. Es un criterio interno para priorizar, no fijado por la norma, y no sustituye la evaluación de impacto. Se ajusta en `RIESGO` de `rat_config.py`.

## RAT del encargado

Hoja "RAT encargado": una fila por cliente por cuenta de quien se tratan datos. Solo es exigible si ese cliente está obligado a llevar el RAT (art. 44 RGLOPDP). Su contenido es de buena práctica hasta confirmar el texto del art. 44 (ver Puntos abiertos en BASE-LEGAL.md).

## Importar un RAT que ya uses

En el asistente web, pestaña "Estado del registro" → "Importar RAT existente": copia la tabla desde Excel (con encabezados) y pégala. El asistente reconoce las columnas por su nombre aunque estén en otro orden, informa las que no reconoce y aplica las alertas a cada actividad. Para mejorar la estructura de la plantilla con registros reales, deja versiones anonimizadas en `referencias/rat/`.

## Firma de responsabilidad

La hoja "Resumen" del Excel y la copia del asistente web incluyen el bloque "Elaborado por / Revisado y aprobado por".

## Limitaciones

- Las alertas comprueban que el campo exista, no que su contenido sea jurídicamente correcto.
- El catálogo y el nivel de riesgo son puntos de partida; las bases legitimadoras sugeridas deben validarse en cada caso.
- La comparación con la AEPD se hizo sin acceso a las páginas citadas por el usuario; ver `docs/metodologia-rat.md`.
- El RAT no reemplaza la inscripción de bases de datos en el Registro Nacional de Protección de Datos Personales (art. 51 LOPDP).
- El asistente web guarda los datos solo en el navegador de quien lo usa. No ingresar datos de personas reales.

## Elaboración y revisión del DPO

La herramienta tiene dos modos (panel bajo las pestañas). **Elaboración:** la completa el responsable o el implementador que eligió (MSC solo si no es DPO de ese cliente) y responde las observaciones. **Revisión del DPO:** el DPO registra observaciones no vinculantes por pestaña, con prioridad, y una conclusión; no corrige ni ejecuta la evaluación (Res. SPDP-SPD-2025-0028-R arts. 13, 15.2 y 15.3). Las observaciones se anexan al informe y tienen su propio informe con firma («Copiar observaciones del DPO»). En la app, el modo se preselecciona según el rol de MSC registrado en la ficha del cliente. Ver `docs/decision-evaluacion-implementacion.md`.

