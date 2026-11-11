# Instrucciones para Claude en este repositorio

Repositorio de herramientas de cumplimiento LOPDP (Ecuador) de Macías Sánchez Consultores.

## Reglas

- **Nunca** incluir datos reales de clientes ni de personas. Solo datos ficticios y marcadores `[ENTRE CORCHETES]`.
- Toda cita normativa debe existir en `BASE-LEGAL.md`. Si una herramienta necesita un artículo nuevo, primero se agrega a esa matriz con su fuente y estado de verificación.
- Si una regla tiene dudas (plazos, alcance), se registra en "Puntos abiertos" de `BASE-LEGAL.md`; no se rellena con supuestos.
- Terminología de la LOPDP: "titular", "responsable", "encargado", "vulneración de la seguridad", "Superintendencia de Protección de Datos Personales (SPDP)", "Registro de actividades de tratamiento (RAT)". No usar términos del RGPD europeo ("interesado", "brecha", "AEPD") salvo en comparaciones explícitas.
- Español de Ecuador, registro formal. Lenguaje claro en los documentos dirigidos a titulares.
- Cada herramienta tiene su `README.md` con: propósito, a quién va dirigida, base legal, instrucciones y limitaciones.
- Versionar con commits descriptivos en español.
- `referencias/` contiene documentos anonimizados que el usuario ya utilizó. Úsalos para mejorar la **estructura** de las plantillas (secciones, orden, campos), nunca para copiar redacción de terceros. Si una referencia contiene datos personales reales, detente y avisa antes de procesarla.
- Ediciones hechas en los generadores web ("Copiar Markdown") se incorporan reemplazando el `.md` correspondiente y regenerando con `scripts/generar_generador.py`.
- Toda exportación lleva firma de responsabilidad (`scripts/firma-responsabilidad.md`) con 6 cm libres para firma y sello (`ALTO_FIRMA_CM` en `scripts/exportar.js`).
- Los valores en dinero se muestran como «USD $ 1.234,56».
- Escalas, umbrales y ponderaciones que no vienen de la norma se rotulan como criterio propio en la interfaz, el informe y el README.

## Estructura

La numeración de las herramientas sigue el orden de uso de la guía (`docs/guia/`). Si se agrega una herramienta, ubicarla en ese orden y actualizar la guía.


- `01-catalogo-servicios/` — catálogo de servicios y glosario, fuente `scripts/catalogo_config.py`; la proforma de 02 importa de allí sus servicios (mismos códigos S01 a S28)
- `02-honorarios/` — calculadora de honorarios y proforma, fuente `scripts/honorarios_config.py` (tarifas y tramos son criterio propio)
- `03-madurez/` — diagnóstico de madurez, fuente `scripts/madurez_config.py` (modelo propio, rotularlo siempre así)
- `04-registro-tratamientos/` — RAT
- `05-gran-escala/` — evaluación de gran escala (MTGE), fuente `scripts/granescala_config.py`
- `06-interes-legitimo/` — evaluación de ponderación del interés legítimo, fuente `scripts/interes_config.py` (puntajes de ponderación de criterio propio)
- `07-evaluacion-impacto/` — evaluación de impacto (EIPD), fuente `scripts/eipd_config.py`
- `08-kit-plantillas/` — documentos contractuales e informativos
- `09-kit-vulneraciones/` — gestión y notificación de vulneraciones
- `app-pd/` — app instalable MSC Protección de Datos (PWA): `fuente/index.html`, `build_pwa.py`; publica `app-pd/docs/` en la rama `gh-pages` (GitHub Pages)
- `scripts/referencia_config.py` — fuente única de la pestaña «Referencia» de la app (normas, puntos de consulta y plazos); todo lo que cite debe constar en `BASE-LEGAL.md`
- `scripts/glosario_config.py` — normas ISO y métodos de medición de riesgos del Glosario (las definiciones legales se toman de `catalogo_config.py`)
- `scripts/exportar.js` — exportación a Word (.docx) y PDF con espacio para firma y sello; la usan la app y las nueve herramientas
- `app-pd/normas/` — PDF de la LOPDP y del RGLOPDP (`lopdp.pdf`, `rglopdp.pdf`); no se versionan. Para publicar en un sitio público compilar con `MSC_PUBLICO=1` (omite esos PDF y enlaza a la fuente oficial)
- `docs/` — decisiones del proyecto, contraste con las guías de la SPDP y recursos pendientes
- `referencias/` — plantillas ya utilizadas, anonimizadas
- `scripts/` — generadores (Excel, exportación a Word)
