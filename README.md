# Portafolio DPD Ecuador

Herramientas para la gestión del cumplimiento de la **Ley Orgánica de Protección de Datos Personales (LOPDP)** y su Reglamento, desarrolladas por **Mariano Xavier Macías Sánchez — Macías Sánchez Consultores**.

> Estado: **privado / en desarrollo**. Todas las herramientas usan datos ficticios. No contienen información de clientes.

## Herramientas

| # | Herramienta | Cuándo se usa | Contenido | Estado |
|---|---|---|---|---|
| 01 | [Catálogo de servicios y glosario](01-catalogo-servicios/) | Antes de proponer: qué ofrecer | 28 servicios con aplicación, responsables, recomendaciones y precios; glosario LOPDP; kit comercial (carta de presentación y campaña de correos) | v0.2 |
| 02 | [Calculadora de honorarios](02-honorarios/) | Cotizar | Tres métodos, IVA, paquetes y proforma con los servicios del catálogo | v0.2 |
| 03 | [Nivel de madurez](03-madurez/) | Diagnóstico inicial y revisión anual | 12 dominios, índice, radar, plan de acción, multa estimada y apetito al riesgo | v0.2 |
| 04 | [Registro de actividades de tratamiento](04-registro-tratamientos/) | Inventario | Excel con control del mínimo legal, catálogo de actividades, asistente web | v0.5 |
| 05 | [Evaluación de gran escala](05-gran-escala/) | Sobre cada actividad del RAT | Calificación directa y MTGE, evidencia, obligaciones e informe | v0.1 |
| 06 | [Interés legítimo](06-interes-legitimo/) | Cuando la base es el interés legítimo | Supuestos admisibles, prohibiciones, características, necesidad, ponderación, salvaguardas, informe y registro (Res. SPDP-SPD-2025-0041-R) | v0.1 |
| 07 | [Evaluación de impacto](07-evaluacion-impacto/) | Alto riesgo o gran escala | Necesidad, proporcionalidad, establecimiento del contexto (Guía v2), matriz de riesgos con justificación e informe del art. 32 RGLOPDP | v0.2 |
| 08 | [Kit de plantillas](08-kit-plantillas/) | Adecuación documental | Política, avisos, contrato de encargo, cláusulas por tipo de contrato (laboral, cargo o rol, encargo, transferencia, corresponsables), designación del DPD | v0.3 |
| 09 | [Kit de vulneraciones](09-kit-vulneraciones/) | Preparación y respuesta | Protocolo, bitácora, notificaciones, plazos y riesgo | v0.2 |

La numeración sigue el orden de uso explicado en la guía.

Páginas web publicadas (privadas hasta que se compartan), por slug: 01 `6c74365b-6821-4c88-9b39-cc11e6b5be1e` · 02 `0906a15b-6c3b-40bb-b242-ce13bf481bb8` · 03 `50aeccd0-a29a-4069-9bf2-efd6d90bb5b1` · 04 `1a5b1944-cd6b-491e-aead-e3b03f1376fe` · 05 `c625607f-3157-4e5f-beb8-dd529eaca8c6` · 06 `ba68d9ba-6c54-4a61-8fdf-ee03f1b5998c` · 07 `2a24339d-59be-4d4a-b964-61ff5a421213` · 08 `545a36a1-052f-4320-ad68-dcb946f26481` · 09 `cdc001fc-2413-4c30-b4d5-bd65292c3e07`.

## Flujo recomendado con un cliente

1. **01 · Catálogo**: elegir los servicios que corresponden al caso.
2. **02 · Honorarios**: cotizar con los mismos códigos y emitir la proforma.
3. **03 · Madurez**: mapeo inicial, diagnóstico y plan de acción.
4. **04 · RAT**: inventario de actividades de tratamiento.
5. **05 · Gran escala**: puntuar cada actividad; define si el DPD y la evaluación de impacto son obligatorios.
6. **06 · Interés legítimo**: ponderación previa de cada tratamiento basado en el interés legítimo.
7. **07 · Evaluación de impacto**: actividades de alto riesgo o gran escala.
8. **08 · Kit de plantillas**: política, avisos, contratos de encargo, cláusulas por tipo de contrato, DPD.
9. **09 · Kit de vulneraciones**: protocolo y respuesta.
10. Repetir **03** y **05** cada año.

## Guía de uso para el DPD

[docs/guia/Guia-DPD-Kit-LOPDP.pdf](docs/guia/Guia-DPD-Kit-LOPDP.pdf): rol y límites del DPD, metodología, mapeo inicial de la empresa, recorrido de los datos (encargo y transferencia), herramientas paso a paso según el caso, abordaje al cliente, propuestas de evaluación y control, identificación de datos (RAT y NIST Privacy Framework ID.IM-P), áreas de tratamiento, informe a la gerencia con matriz de soportes, control, normas ISO, roadmap de la gestión del DPD, kit comercial, contraste con las guías de la SPDP y anexos.

Otros documentos de decisión: [docs/contraste-guias-spdp.md](docs/contraste-guias-spdp.md) (cobertura de la Guía v2 y de la guía de diseño y por defecto) y [docs/recursos-pendientes.md](docs/recursos-pendientes.md) (textos oficiales por obtener). Los gráficos, cronogramas, metas e ISO por prioridad son criterio propio.

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
python scripts/generar_catalogo.py                 # 01 catálogo y glosario
python scripts/generar_calculadora_honorarios.py   # 02 calculadora y proforma (usa el catálogo)
python scripts/generar_asistente_madurez.py        # 03
python scripts/generar_rat.py                      # 04 Excel del RAT
python scripts/generar_asistente_rat.py            # 04 asistente web
python scripts/generar_gran_escala.py              # 05
python scripts/generar_interes_legitimo.py         # 06
python scripts/generar_asistente_eipd.py           # 07
python scripts/generar_generador.py                # 08 y 09
bash scripts/exportar_docx.sh                      # versiones Word
python scripts/guia/graficos.py && python scripts/guia/generar_guia.py  # guía PDF
```

`scripts/vendor/marked.min.js` (licencia MIT, ver `marked-LICENSE.md`) se incrusta en las páginas web para que funcionen sin conexión. La tipografía Archivo (`scripts/vendor/fonts/`, licencia OFL) se usa en la guía PDF.
