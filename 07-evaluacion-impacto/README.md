# 07 · Evaluación de impacto del tratamiento de datos personales (EIPD)

## Propósito

Determinar si un tratamiento exige evaluación de impacto y, en su caso, realizarla con el contenido mínimo del art. 32 del Reglamento: descripción, necesidad y proporcionalidad, riesgos y medidas.

## A quién va dirigida

Responsables del tratamiento que van a iniciar o modificar un tratamiento de riesgo, y DPD o consultores que la elaboran.

## Archivos

| Archivo | Uso |
|---|---|
| `asistente-eipd.html` | Asistente web en 6 pasos: necesidad (art. 42), descripción, proporcionalidad, establecimiento del contexto (Guía v2), matriz de riesgos con derechos afectados, justificación de cada valor y mapa de calor, conclusión. Copia el informe completo para Word y la matriz para Excel. Incluye un ejemplo ficticio (control de asistencia con huella). |
| `informe-eipd.md` | Plantilla del informe para completar a mano. |
| `docx/` | Versión Word con firma de responsabilidad (`scripts/exportar_docx.sh`). |
| `../scripts/eipd_config.py` | **Fuente única**: preguntas, escalas, catálogos de escenarios, amenazas, vulnerabilidades y controles, umbral de aceptación. |

## Base legal

- LOPDP art. 42: supuestos de obligatoriedad (perfiles con efectos jurídicos; gran escala de categorías especiales o datos penales; observación sistemática a gran escala de zonas públicas) y requerimiento de la SPDP.
- LOPDP art. 40: metodología de análisis de riesgos.
- RGLOPDP art. 29 (concepto), art. 30 (objeto), art. 31 (obligatoria y previa al tratamiento), art. 32 (presentación ante la SPDP y contenido mínimo).
- Res. SPDP-SPD-2026-0012-R: Guía de Gestión de Riesgos y Evaluación de Impacto, versión 2. Cap. I obligatorio (justificación de cada valor; rechazo de las listas de chequeo); Cap. II referencial (cinco etapas: contexto, identificación, análisis, evaluación y tratamiento).
- LOPDP art. 39 y Res. SPDP-SPD-2025-0040-R: protección desde el diseño y por defecto (controles DevPrivOps en el catálogo de medidas).
- Normativa especial que remite a la evaluación de impacto: Res. SPDP-SPD-2026-0039-R (biométricos), Res. SPDP-SPD-2026-0009-R y 2026-0037-R (inteligencia artificial), Res. SPDP-SPD-2025-0041-R (interés legítimo).

Estado de verificación: `BASE-LEGAL.md`.

## Decisiones de diseño

- **Escalas propias.** La guía de la SPDP deja las escalas y matrices en su Cap. II, que es referencial, y permite agregar criterios. La herramienta usa impacto × probabilidad de 1 a 5, con niveles Bajo (1-4), Medio (5-9), Alto (10-16) y Muy alto (17-25). Se ajustan en `eipd_config.py`.
- **Establecimiento del contexto (nuevo en v0.2).** Pestaña 4 con los cinco factores de impacto de la guía v2 (categorías especiales, vulnerabilidad, número de titulares, naturaleza de la afectación, volumen por titular). Las opciones y su puntaje son **criterio propio**; la suma da un *piso de impacto sugerido* (máx(1, suma ÷ 2) redondeado hacia arriba) y el asistente avisa si un riesgo se valora por debajo. Incluye los derechos en juego, el periodo de la probabilidad, el método y la capacidad de riesgo, y una guía paso a paso para determinar el impacto sobre los derechos.
- **Justificación por riesgo (nuevo en v0.2).** Cada riesgo registra los derechos afectados y la justificación (rationale) de impacto y probabilidad; el informe y la matriz la incluyen.
- **Criterios de la guía incorporados:** categorías especiales, vulnerabilidad de grupos, cantidad de titulares, naturaleza de la vulneración y volumen; el ejemplo de la guía (más de mil afectados equivale a riesgo muy alto) aparece en la ayuda del impacto 5.
- **Advertencia de matrices.** La guía advierte que las matrices pueden distorsionar los riesgos de alto impacto y baja probabilidad: el asistente lo señala cuando el impacto es 5 y la probabilidad es 1 o 2.
- **Umbral de aceptación** por defecto 9 (nivel Medio), editable en el paso 6 como tolerancia de la organización (Guía v2, establecimiento del contexto).
- **Vínculo con el RAT:** cada evaluación anota el código de la actividad; el RAT tiene los campos "¿Requiere evaluación de impacto?" y "Ref. evaluación de impacto".

## Limitaciones

- La herramienta no reemplaza el análisis técnico de seguridad ni la metodología cuantitativa que la guía de la SPDP describe como opción.
- No implementa modelos cuantitativos (Monte Carlo, FAIR, bayesiano); el método «cuantitativo» del contexto documenta que se usaron fuera de la herramienta.
- No se pudo leer el anexo de la guía v2 con el formato oficial ni sus etapas 4 y 5 (declaración de aplicabilidad); el informe sigue el art. 32 del Reglamento. Pendiente de contraste (ver puntos abiertos en `BASE-LEGAL.md`).
- Los datos del asistente web se guardan solo en el navegador. No ingresar datos reales de personas.
