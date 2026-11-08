# 02 · Nivel de madurez en protección de datos personales

## Propósito

Diagnosticar en qué punto está una organización frente a sus obligaciones de protección de datos y obtener un plan de acción priorizado que remite a las herramientas 03 a 04 del portafolio. Sirve como **primera reunión con un cliente** y para medir el avance en revisiones posteriores.

## A quién va dirigida

DPD y consultores que inician un proyecto de adecuación; responsables que quieren autoevaluarse.

## Archivos

| Archivo | Uso |
|---|---|
| `asistente-madurez.html` | Cuestionario web de 39 preguntas en 12 dominios, índice ponderado, gráfico de radar, barras por dominio, plan de acción e **impacto económico** (multa estimada, riesgo anual esperado y apetito al riesgo). Copia el informe para Word y los resultados para Excel. Incluye un ejemplo ficticio (pyme comercial). |
| `cuestionario-madurez.md` | Versión para aplicar en entrevista o imprimir (generada desde la configuración). |
| `docx/` | Versión Word con firma de responsabilidad. |
| `../scripts/madurez_config.py` | **Fuente única**: dominios, preguntas, evidencias sugeridas, pesos, escala y niveles. |

## El modelo

**Es un modelo propio de Macías Sánchez Consultores.** La SPDP no ha emitido un modelo oficial de madurez. Los 12 dominios siguen las obligaciones de la LOPDP, su Reglamento y la normativa de la SPDP registrada en `BASE-LEGAL.md`:

Gobierno y responsabilidad proactiva · DPD (crítico) · RAT (crítico) · Licitud y bases (crítico) · Transparencia · Derechos de los titulares · Encargados (crítico) · Seguridad y riesgos (crítico) · Evaluación de impacto y diseño · Vulneraciones (crítico) · Transferencias internacionales · Capacitación y cultura.

- **Escala por pregunta:** 0 No existe · 1 Inicial · 2 En desarrollo · 3 Implementado · 4 Gestionado · N/A (no cuenta).
- **Índice:** promedio ponderado de los dominios; los **críticos pesan el doble** porque su incumplimiento tiene mayor exposición sancionatoria o es la base del resto (no tener RAT impide saber qué proteger).
- **Niveles:** Inexistente (0-0,99) · Inicial (1-1,99) · En desarrollo (2-2,79) · Implementado (2,8-3,49) · Gestionado (3,5-4).
- **Plan de acción:** prioridad Alta si un dominio crítico está bajo 2; Media si cualquier dominio está bajo 2,8; cada fila indica la herramienta del portafolio que cierra la brecha.

## Impacto económico y apetito al riesgo

La pestaña 4 estima la multa que podría imponerse si la organización no actúa, con el modelo **MPRIV-1** de la Res. SPDP-SPD-2025-0022-R:

1. **Volumen de negocio (VDN)** del ejercicio económico anterior: ingresos por ventas y servicios menos impuestos directamente relacionados (LOPDP arts. 71 a 73). El año se propone automáticamente (año de la evaluación − 1).
2. **Categoría**: leve (0,1 % a 0,7 % del VDN) o grave (0,7 % a 1 %). Se sugiere "Grave" cuando tiene puntaje bajo un dominio cuyo incumplimiento está verificado como grave (DPD, contrato de encargo, notificación a titulares).
3. **PDI** (peso de la infracción): según el reglamento mide el grado de madurez en el cumplimiento; se toma como **PDI = (1 − índice / 4) × 100**.
4. **Seriedad (SDI)**: afectación a derechos (IED 60 %), intencionalidad (INT 40 %) y reincidencia (RER 20 %), cada una con estimación PERT; **SDI = 2 (0,6 IED + 0,4 INT + 0,2 RER)**.
5. **Multa = CDI × SDI**, acotada al mínimo y máximo legal de la categoría.
6. **Dos escenarios**: si no actúa (índice actual) y con el plan de acción (índice 3,0, nivel Implementado).
7. **Riesgo anual esperado** = multa × probabilidad anual de sanción (sugerida por nivel de madurez, editable), como en el ejemplo de la Guía SPDP.
8. **Apetito al riesgo** = capacidad (USD) × tolerancia (Baja 50 %, Media 100 %, Alta 150 %): indica si la multa estimada está dentro o fuera.

La pantalla muestra el cálculo paso a paso para que el cliente pueda auditarlo.

**Interpretaciones del portafolio (rotuladas en la interfaz y el informe):** el sentido del PDI, la forma de aplicar los pesos 60/40/20, las escalas de IED, INT y RER, las probabilidades por nivel y los factores de tolerancia. Las fórmulas provienen de un resumen profesional de la resolución: el Anexo I oficial no se pudo leer (ver puntos abiertos 11 a 13 en `BASE-LEGAL.md`). Todo es editable en `madurez_config.py`.

## Limitaciones

- Es un diagnóstico orientativo, no una auditoría ni una certificación. La multa es una estimación para gestionar el riesgo, no una liquidación: la SPDP fija los valores con sus propios rationales y puede usar un cálculo estocástico.
- No calcula multas del sector público (servidores públicos en SBU) hasta verificar los múltiplos para infracciones graves.
- El resultado depende de que las respuestas se apoyen en evidencia.
- Las ponderaciones y umbrales son criterio del portafolio; se ajustan en `madurez_config.py`.
- El dominio de transferencias internacionales no cita artículos de la LOPDP hasta verificar su numeración (ver puntos abiertos en `BASE-LEGAL.md`).
