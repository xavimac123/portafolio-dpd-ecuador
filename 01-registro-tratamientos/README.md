# 01 · Registro de Actividades de Tratamiento (RAT)

## Propósito

Documentar cada actividad de tratamiento de datos personales con el contenido mínimo exigido por el art. 38 del Reglamento General a la LOPDP y detectar automáticamente los vacíos.

## A quién va dirigida

Responsables del tratamiento (empresas, profesionales, instituciones) y DPD que preparan o auditan el registro.

## Archivos

| Archivo | Uso |
|---|---|
| `plantilla-RAT.xlsx` | Plantilla para completar. Incluye hoja de obligatoriedad, datos del responsable, registro con alertas automáticas y resumen. |
| `ejemplo-RAT-ficticio.xlsx` | Clínica dental ficticia con 6 actividades: 2 completas y 4 con errores intencionales, útil para capacitaciones y demostraciones. |
| `asistente-rat.html` | Versión web interactiva: verifica obligatoriedad, registra actividades, importa un RAT existente pegado desde Excel, muestra alertas y copia el registro con firma de responsabilidad. |
| `../scripts/generar_rat.py` | Regenera ambos Excel (`python scripts/generar_rat.py`). |

## Base legal

- RGLOPDP art. 38: obligación (100 o más trabajadores) y contenido mínimo de 9 elementos.
- RGLOPDP art. 39: extensión a organizaciones con menos de 100 trabajadores (riesgo, tratamiento no ocasional, categorías especiales).
- RGLOPDP art. 44: registro del encargado.
- LOPDP art. 7: bases legitimadoras.
- Res. SPDP-SPD-2025-0041-R: interés legítimo y evaluación de ponderación.

Estado de verificación de cada norma: ver [BASE-LEGAL.md](../BASE-LEGAL.md).

## Correspondencia con el art. 38 RGLOPDP

| Numeral | Contenido | Columna en la plantilla |
|---|---|---|
| 1 | Contacto del responsable, corresponsable y DPD | Hoja "Responsable" |
| 2 | Finalidades | Finalidades |
| 3 | Categorías de destinatarios | Categorías de destinatarios |
| 4 | Titulares y categorías de datos | Categorías de titulares · Categorías de datos personales |
| 5 | Uso de perfiles | ¿Elaboración de perfiles? |
| 6 | Transferencias internacionales | ¿Transferencia internacional? · País y garantía |
| 7 | Bases legitimadoras | Base legitimadora · Ref. evaluación de interés legítimo |
| 8 | Plazos de supresión o revisión | Plazo de conservación / supresión |
| 9 | Medidas técnicas, jurídicas, administrativas y organizativas | Medidas |

Columnas adicionales (buena práctica, no exigidas por el art. 38): área responsable, categorías especiales, datos de niñas, niños y adolescentes, origen, encargados y fecha de revisión.

## Alertas automáticas

Una fila se marca "Completo" cuando tiene todos los campos mínimos. Se generan alertas cuando:

- falta cualquier elemento mínimo del art. 38;
- la base es interés legítimo y no hay referencia a la evaluación de ponderación;
- hay transferencia internacional sin país o garantía;
- incluye categorías especiales (recordatorio de revisar la evaluación de impacto);
- no hay fecha de revisión.

## Importar un RAT que ya uses

En el asistente web, pestaña "Estado del registro" → "Importar RAT existente": copia la tabla desde Excel (con encabezados) y pégala. El asistente reconoce las columnas por su nombre aunque estén en otro orden, informa las que no reconoce y aplica las alertas a cada actividad. Para mejorar la estructura de la plantilla con registros reales, deja versiones anonimizadas en `referencias/rat/`.

## Firma de responsabilidad

La hoja "Resumen" del Excel y la copia del asistente web incluyen el bloque "Elaborado por / Revisado y aprobado por".

## Limitaciones

- Las alertas comprueban que el campo exista, no que su contenido sea jurídicamente correcto.
- El RAT no reemplaza la inscripción de bases de datos en el Registro Nacional de Protección de Datos Personales (art. 51 LOPDP).
- El asistente web guarda los datos solo en el navegador de quien lo usa. No ingresar datos de personas reales.
