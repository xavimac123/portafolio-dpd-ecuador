# 01 · Catálogo de servicios y glosario

## Propósito

Mostrar al DPD qué servicios puede ofrecer, cómo se aplica cada uno, a quién va dirigido, qué se obtiene, qué departamento de la empresa responde y con quién levantar información, con un precio sugerido por tamaño de empresa. Incluye el glosario de la LOPDP, su Reglamento y la normativa de la SPDP.

## A quién va dirigida

Al DPD o consultor, en especial al que empieza. La versión para el cliente (botón «Copiar catálogo para el cliente») omite las recomendaciones internas.

## Contenido

| Archivo | Uso |
|---|---|
| `catalogo-servicios.html` | Página web: catálogo filtrable, responsables por servicio, glosario y selección de códigos |
| `catalogo-servicios.md` | Ficha interna completa para Word |
| `glosario.md` | Glosario para Word |
| `carta-presentacion.md` | Carta genérica de presentación del servicio para cualquier empresa |
| `correos-campana.md` | Secuencia de cinco correos empresariales y dos respuestas tipo, con pie de baja obligatorio |
| `docx/` | Versiones Word |

Fuente única: `scripts/catalogo_config.py`. La calculadora de honorarios (herramienta 02) importa de allí sus servicios: **mismos códigos (S01 a S28), nombres, unidades y precios sugeridos**. Regenerar con `python scripts/generar_catalogo.py` y `python scripts/generar_calculadora_honorarios.py`.

## Sincronización con la proforma

1. Marque servicios en el catálogo y copie los códigos (pestaña «Mi selección»).
2. En la proforma de la herramienta 02, pegue los códigos y pulse «Importar del catálogo».
3. Para agregar o cambiar un servicio, edite solo `catalogo_config.py` y regenere ambas herramientas.

## Base legal

El glosario resume las 24 definiciones del art. 4 de la LOPDP (no es texto literal) y conceptos del RGLOPDP (arts. 4, 38) y de las resoluciones de la SPDP. La base de cada servicio consta en su ficha; todas las citas están en `BASE-LEGAL.md`.

## Instrucciones

1. Filtre por fase o busque por palabra; elija el tamaño de empresa para ver precios.
2. Abra cada servicio para revisar aplicación, responsables y recomendaciones.
3. Revise la pestaña «Responsables por servicio» para planificar entrevistas.
4. Seleccione servicios, copie los códigos y cotice en la herramienta 02.

## Kit comercial

- **Carta de presentación:** personalice solo el párrafo marcado y los datos de contacto. Va firmada por el consultor; no lleva el bloque de firma de responsabilidad.
- **Campaña de correos:** cinco correos (días 1, 4, 9, 15 y 22) y dos respuestas tipo. Cada correo debe llevar el pie de baja. El correo de un contacto empresarial es un dato personal: envíe solo con base de legitimación y, si usa el interés legítimo para mercadotecnia directa, haga antes la ponderación con la herramienta 06. Las cifras de multas provienen de la LOPDP arts. 71 y 72.

## Limitaciones

- Los precios son **criterio propio** y referenciales; los servicios «desde» dependen del cálculo de la herramienta 02.
- La naturaleza de cada servicio delimita el rol: solo los de supervisión son función propia del DPD; la implementación siempre es de la empresa.
- El glosario no sustituye el texto oficial para escritos formales.
