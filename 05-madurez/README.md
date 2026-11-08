# 05 · Nivel de madurez en protección de datos personales

## Propósito

Diagnosticar en qué punto está una organización frente a sus obligaciones de protección de datos y obtener un plan de acción priorizado que remite a las herramientas 01 a 04 del portafolio. Sirve como **primera reunión con un cliente** y para medir el avance en revisiones posteriores.

## A quién va dirigida

DPD y consultores que inician un proyecto de adecuación; responsables que quieren autoevaluarse.

## Archivos

| Archivo | Uso |
|---|---|
| `asistente-madurez.html` | Cuestionario web de 39 preguntas en 12 dominios, índice ponderado, gráfico de radar, barras por dominio y plan de acción. Copia el informe para Word y los resultados para Excel. Incluye un ejemplo ficticio (pyme comercial). |
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

## Limitaciones

- Es un diagnóstico orientativo, no una auditoría ni una certificación. El resultado depende de que las respuestas se apoyen en evidencia.
- Las ponderaciones y umbrales son criterio del portafolio; se ajustan en `madurez_config.py`.
- El dominio de transferencias internacionales no cita artículos de la LOPDP hasta verificar su numeración (ver puntos abiertos en `BASE-LEGAL.md`).
