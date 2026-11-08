# Portafolio DPD Ecuador

Herramientas para la gestión del cumplimiento de la **Ley Orgánica de Protección de Datos Personales (LOPDP)** y su Reglamento, desarrolladas por **Mariano Xavier Macías Sánchez — Macías Sánchez Consultores**.

> Estado: **privado / en desarrollo**. Todas las herramientas usan datos ficticios. No contienen información de clientes.

## Herramientas

| # | Herramienta | Contenido | Estado |
|---|---|---|---|
| 01 | [Registro de actividades de tratamiento](01-registro-tratamientos/) | Plantilla Excel por secciones con control del mínimo legal, catálogo de actividades, RAT del encargado, asistente web | v0.5 |
| 02 | [Kit de plantillas](02-kit-plantillas/) | Política y avisos de privacidad, contrato de encargo, cláusulas de consentimiento, designación del DPD; generador web | v0.2 |
| 03 | [Kit de vulneraciones](03-kit-vulneraciones/) | Protocolo, bitácora, modelos de comunicación, calculadora de plazos y evaluación de riesgo | v0.2 |
| 04 | [Evaluación de impacto](04-evaluacion-impacto/) | Necesidad (art. 42), descripción, proporcionalidad, matriz de riesgos y medidas, informe del art. 32 RGLOPDP | v0.1 |
| 05 | [Nivel de madurez](05-madurez/) | Diagnóstico en 12 dominios, índice ponderado, radar, plan de acción, multa estimada (Res. SPDP-SPD-2025-0022-R) y apetito al riesgo | v0.2 |

## Flujo recomendado con un cliente

1. **05 · Madurez**: diagnóstico inicial y plan de acción.
2. **01 · RAT**: inventario de actividades; identifica cuáles requieren evaluación de impacto.
3. **04 · Evaluación de impacto**: para las actividades de alto riesgo.
4. **02 · Kit de plantillas**: política, avisos, contratos de encargo, DPD.
5. **03 · Kit de vulneraciones**: protocolo y respuesta.
6. Repetir **05** para medir el avance.

## Guía de uso para el DPD

[docs/guia/Guia-DPD-Kit-LOPDP.pdf](docs/guia/Guia-DPD-Kit-LOPDP.pdf): metodología, herramientas paso a paso, abordaje al cliente, propuestas de evaluación y control, identificación de datos (RAT y NIST Privacy Framework ID.IM-P), áreas de tratamiento, informe a la gerencia con matriz de soportes, control, normas ISO y anexos. Los gráficos, cronogramas, metas e ISO por prioridad son criterio propio.

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
python scripts/generar_rat.py          # Excel del RAT
python scripts/generar_asistente_rat.py  # asistente web del RAT
python scripts/generar_generador.py    # páginas web de los kits 02 y 03
python scripts/generar_asistente_eipd.py     # asistente de evaluación de impacto
python scripts/generar_asistente_madurez.py  # asistente y cuestionario de madurez
bash scripts/exportar_docx.sh          # versiones Word
python scripts/guia/graficos.py && python scripts/guia/generar_guia.py  # guía PDF
```

`scripts/vendor/marked.min.js` (licencia MIT, ver `marked-LICENSE.md`) se incrusta en las páginas web para que funcionen sin conexión. La tipografía Archivo (`scripts/vendor/fonts/`, licencia OFL) se usa en la guía PDF.
