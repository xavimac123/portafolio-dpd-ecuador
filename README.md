# Portafolio DPD Ecuador

Herramientas para la gestión del cumplimiento de la **Ley Orgánica de Protección de Datos Personales (LOPDP)** y su Reglamento, desarrolladas por **Mariano Xavier Macías Sánchez — Macías Sánchez Consultores**.

> Estado: **privado / en desarrollo**. Todas las herramientas usan datos ficticios. No contienen información de clientes.

## Herramientas

| # | Herramienta | Cuándo se usa | Contenido | Estado |
|---|---|---|---|---|
| 01 | [Calculadora de honorarios](01-honorarios/) | Antes de empezar: cotizar | Honorarios por volumen de negocio, volumen de tratamiento (MTGE) y estimación técnica; IVA; paquetes; proforma con firma | v0.1 |
| 02 | [Nivel de madurez](02-madurez/) | Diagnóstico inicial y revisión anual | 12 dominios, índice ponderado, radar, plan de acción, multa estimada (Res. SPDP-SPD-2025-0022-R) y apetito al riesgo | v0.2 |
| 03 | [Registro de actividades de tratamiento](03-registro-tratamientos/) | Inventario de lo que la empresa hace con datos | Plantilla Excel con control del mínimo legal, catálogo de actividades, RAT del encargado, asistente web | v0.5 |
| 04 | [Evaluación de gran escala](04-gran-escala/) | Sobre cada actividad del RAT | Calificación directa y Modelo Técnico de Gran Escala (Res. SPDP-SPD-2026-0005-R), evidencia, obligaciones e informe | v0.1 |
| 05 | [Evaluación de impacto](05-evaluacion-impacto/) | Actividades de alto riesgo o gran escala | Necesidad (art. 42), descripción, proporcionalidad, matriz de riesgos y medidas, informe del art. 32 RGLOPDP | v0.1 |
| 06 | [Kit de plantillas](06-kit-plantillas/) | Adecuación documental, después del RAT | Política y avisos, contrato de encargo, cláusulas de consentimiento, designación del DPD; generador web | v0.2 |
| 07 | [Kit de vulneraciones](07-kit-vulneraciones/) | Preparación y respuesta a incidentes | Protocolo, bitácora, modelos de comunicación, calculadora de plazos y evaluación de riesgo | v0.2 |

La numeración sigue el orden de uso explicado en la guía.

Páginas web publicadas (privadas hasta que se compartan), por slug: 01 `0906a15b-6c3b-40bb-b242-ce13bf481bb8` · 02 `50aeccd0-a29a-4069-9bf2-efd6d90bb5b1` · 03 `1a5b1944-cd6b-491e-aead-e3b03f1376fe` · 04 `c625607f-3157-4e5f-beb8-dd529eaca8c6` · 05 `2a24339d-59be-4d4a-b964-61ff5a421213` · 06 `545a36a1-052f-4320-ad68-dcb946f26481` · 07 `cdc001fc-2413-4c30-b4d5-bd65292c3e07`.

## Flujo recomendado con un cliente

1. **01 · Honorarios**: estimar y presentar la proforma.
2. **02 · Madurez**: mapeo inicial, diagnóstico y plan de acción.
3. **03 · RAT**: inventario de actividades de tratamiento.
4. **04 · Gran escala**: puntuar cada actividad; define si el DPD y la evaluación de impacto son obligatorios.
5. **05 · Evaluación de impacto**: para las actividades de alto riesgo o gran escala.
6. **06 · Kit de plantillas**: política, avisos, contratos de encargo, DPD.
7. **07 · Kit de vulneraciones**: protocolo y respuesta.
8. Repetir **02** y **04** cada año para medir el avance.

## Guía de uso para el DPD

[docs/guia/Guia-DPD-Kit-LOPDP.pdf](docs/guia/Guia-DPD-Kit-LOPDP.pdf): rol y límites del DPD, metodología, mapeo inicial de la empresa, recorrido de los datos (encargo y transferencia), herramientas paso a paso según el caso, abordaje al cliente, propuestas de evaluación y control, identificación de datos (RAT y NIST Privacy Framework ID.IM-P), áreas de tratamiento, informe a la gerencia con matriz de soportes, control, normas ISO y anexos. Los gráficos, cronogramas, metas e ISO por prioridad son criterio propio.

## Cómo se usa

1. Cada carpeta tiene un `README.md` con instrucciones.
2. Las plantillas están en Markdown (`.md`) y se exportan a Word con `make docx` o `pandoc archivo.md -o archivo.docx`.
3. Los campos a completar van entre corchetes: `[RAZÓN SOCIAL]`.
4. La base normativa de todo el repositorio está en [BASE-LEGAL.md](BASE-LEGAL.md).

## Advertencia

Estas herramientas son material de apoyo y no sustituyen el análisis jurídico del caso concreto. La normativa ecuatoriana de protección de datos está en desarrollo activo por la Superintendencia de Protección de Datos Personales (SPDP); verifica la vigencia de cada norma antes de usarla.

## Licencia

Pendiente de definir antes de hacer público el repositorio (ver `docs/decision-licencia.md`).

## Regenerar los archivos derivados

```bash
python scripts/generar_calculadora_honorarios.py   # 01 calculadora, metodología y proforma
python scripts/generar_asistente_madurez.py        # 02 asistente y cuestionario de madurez
python scripts/generar_rat.py                      # 03 Excel del RAT
python scripts/generar_asistente_rat.py            # 03 asistente web del RAT
python scripts/generar_gran_escala.py              # 04 evaluación de gran escala
python scripts/generar_asistente_eipd.py           # 05 asistente de evaluación de impacto
python scripts/generar_generador.py                # 06 y 07 páginas web de los kits
bash scripts/exportar_docx.sh                      # versiones Word
python scripts/guia/graficos.py && python scripts/guia/generar_guia.py  # guía PDF
```

`scripts/vendor/marked.min.js` (licencia MIT, ver `marked-LICENSE.md`) se incrusta en las páginas web para que funcionen sin conexión. La tipografía Archivo (`scripts/vendor/fonts/`, licencia OFL) se usa en la guía PDF.
