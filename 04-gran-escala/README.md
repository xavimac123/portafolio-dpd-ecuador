# 04 · Evaluación del tratamiento a gran escala

## Propósito

Determinar, tratamiento por tratamiento, si una organización realiza tratamientos de datos personales a gran escala, aplicando los casos de calificación directa y el Modelo Técnico de Gran Escala (MTGE) de la Res. SPDP-SPD-2026-0005-R, y documentar el cálculo con su evidencia para el RAT.

## A quién va dirigida

Al DPD o consultor, incluso con poca experiencia: la herramienta enseña qué mide cada variable, qué dato pedir, a quién, cómo contarlo y cómo explicar el resultado a la gerencia.

## Contenido

| Archivo | Uso |
|---|---|
| `evaluacion-gran-escala.html` | Asistente web: aprender, organización, evaluación por tratamiento, resultados y obligaciones, informe |
| `solicitud-informacion.md` | Carta con la información que debe pedirse al cliente antes de las entrevistas |
| `informe-gran-escala.md` | Plantilla del informe de evaluación, para trabajar sin el asistente |
| `docx/` | Versiones Word |

Fuente única: `scripts/granescala_config.py`. Regenerar con `python scripts/generar_gran_escala.py`.

## Base legal

| Elemento | Fuente |
|---|---|
| Definición y casos predeterminados de gran escala | RGLOPDP art. 4 num. 7 (lit. a a f) |
| Consulta vinculante a la SPDP ante dudas sobre la designación del DPD | RGLOPDP art. 53 |
| Gran escala de categorías especiales | RGLOPDP art. 54; LOPDP art. 48 |
| Definiciones de alcance, frecuencia, titulares, permanencia y volumen | Res. SPDP-SPD-2026-0005-R art. 3 |
| Registro en el RAT y actualización anual | Res. arts. 4, 6 y 7 |
| Variables, puntos, suma y umbral de 6 | Res. arts. 8 a 10 |
| Efectos: evaluación de impacto, DPD, RAT, medidas reforzadas | Res. art. 12; LOPDP art. 42 |
| Calificación directa | Res. art. 14 |
| Obligaciones reforzadas: RAT, privacidad desde el diseño, auditorías, política e informe anual | Res. arts. 15 a 18 |
| Plazo transitorio de 90 días para designar y registrar al DPD | Res., disposición transitoria |

El contador de tipos de datos, las ayudas didácticas, el guion para el cliente y la advertencia de resultado sensible (a menos de un punto del umbral) son **material de apoyo propio**, no norma.

## Instrucciones

1. **Aprender**: lea las variables y la lectura crítica. Envíe al cliente la solicitud de información.
2. **Organización**: datos de identificación y rol (responsable o encargado).
3. **Evaluar tratamientos**: agregue cada tratamiento del RAT. Paso A, calificación directa; Paso B, seis variables con su evidencia.
4. **Resultados**: tabla, conclusión, obligaciones y guion para la gerencia.
5. **Informe**: firma, copia a Word y columnas para el RAT (Excel).

## Limitaciones

- La gran escala se mide por tratamiento, no por organización.
- El texto del art. 8.1.4 omite de 100.001 a 100.999 titulares; la herramienta los asigna al tramo superior.
- El art. 14.1 incluye «otros datos sensibles»: su alcance es amplio y debe documentarse el criterio aplicado.
- El umbral se alcanza con facilidad (por ejemplo, permanencia prolongada y alcance nacional con valores mínimos suman 6,5); ante resultados desproporcionados, considere la consulta a la SPDP.
- No sustituye el análisis jurídico ni la evaluación de impacto.
