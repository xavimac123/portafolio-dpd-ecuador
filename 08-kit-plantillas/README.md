# 08 · Kit de plantillas

## Propósito

Documentos base para que un responsable del tratamiento cumpla el deber de información, formalice la relación con sus encargados y obtenga consentimientos válidos cuando corresponda.

## Archivos

| Plantilla | Cuándo se usa | Base |
|---|---|---|
| `politica-privacidad.md` | Política completa (segunda capa) para web, contratos y atención de titulares | LOPDP arts. 7 y 12 |
| `aviso-privacidad.md` | Texto breve junto a formularios, letreros de videovigilancia y correos (primera capa) | LOPDP art. 12 |
| `contrato-encargo.md` | Con cada proveedor que trate datos por cuenta del responsable | RGLOPDP art. 41; Res. SPDP-SPD-2025-0006-R, Anexo I; LOPDP art. 68 num. 9 |
| `clausulas-consentimiento.md` | Cláusula para contratos con clientes y autorizaciones específicas (marketing, datos sensibles, NNA, imagen) | LOPDP art. 7; Res. SPDP-SPD-2025-0006-R, Anexo I |
| `clausula-laboral.md` | Contratos de trabajo: datos del trabajador, bases, comunicaciones al IESS y SRI, plazos | Res. SPDP-SPD-2025-0006-R, arts. 1 y 4 y Anexo I (modelo responsable–titular) |
| `clausula-cargo-rol.md` | Compromiso de confidencialidad del personal según su nivel de acceso (general, datos sensibles, acceso privilegiado, responsable de área) | Res. SPDP-SPD-2025-0006-R, Anexo I (acuerdos de confidencialidad con el personal) |
| `clausula-encargo.md` | Cláusula breve para insertar en el contrato de servicios con un proveedor encargado; remite al contrato de encargo completo | RGLOPDP arts. 40 y 41; Res. SPDP-SPD-2025-0006-R, Anexo I (modelo responsable–encargado) |
| `clausula-transferencia.md` | Entrega de datos a otra organización que los usará para sus propios fines | LOPDP arts. 33 y 56; Res. SPDP-SPD-2025-0006-R, Anexo I (modelo responsable–destinatario) |
| `clausula-corresponsables.md` | Dos o más responsables que deciden juntos finalidades y medios | Res. SPDP-SPD-2025-0006-R, Anexo I (modelo de corresponsables) |
| `comunicacion-dpd.md` | Ficha del DPD registrado en la SPDP, comunicación interna, comunicación a titulares, texto web y lista de control | LOPDP arts. 12, 47 num. 13, 48 y 68; Res. SPDP-SPD-2025-0028-R |
| `generador-documentos.html` | Versión web: datos generales una vez, campos propios por documento, firma de responsabilidad, edición e importación de plantillas propias | — |
| `docx/` | Versiones Word generadas con `scripts/exportar_docx.sh` | — |

## Qué cláusula usar según el tipo de contrato

La Res. SPDP-SPD-2025-0006-R obliga a incluir cláusulas de protección de datos en los contratos entre los actores del sistema; su Anexo I ofrece modelos referenciales, no obligatorios en su redacción. Elige así:

| Pregunta | Si la respuesta es sí | Plantilla |
|---|---|---|
| ¿Es un contrato de trabajo? | La empresa es responsable y el trabajador es titular | `clausula-laboral.md` |
| ¿La persona tratará datos de otros en su cargo? | Debe asumir deberes de confidencialidad según su nivel de acceso | `clausula-cargo-rol.md` (además de la laboral) |
| ¿El proveedor trata datos solo para prestar un servicio a la empresa? | Es encargado | `clausula-encargo.md` + `contrato-encargo.md` |
| ¿El otro usará los datos para sus propios fines? | Es destinatario de una transferencia o comunicación | `clausula-transferencia.md` |
| ¿Ambas partes deciden juntas para qué y cómo se tratan? | Son corresponsables | `clausula-corresponsables.md` |
| ¿Es un contrato con un cliente? | La empresa es responsable y el cliente es titular | `clausulas-consentimiento.md` (adaptar la base) |

Todas deben evitar los defectos del art. 4 de la resolución: ambigüedad, finalidades no legítimas, falta de base legal, falta de transparencia, omisión de medidas de seguridad, recolección excesiva, limitación de derechos, transferencias sin control, exenciones excesivas y ausencia de plazo de conservación.

## Orden de trabajo recomendado

1. Completar primero el **RAT** (herramienta 04): la política se alimenta de él.
2. Redactar la **política de privacidad**.
3. Derivar de ella los **avisos** de cada punto de recolección.
4. Si corresponde designar DPD, completar la **ficha y comunicaciones del DPD** y actualizar la política y los avisos con el correo de atención al titular.
5. Identificar en el RAT la columna "Encargados" y firmar un **contrato de encargo** con cada uno.
6. Usar las **cláusulas de consentimiento** solo para las finalidades cuya base sea el consentimiento.
7. Incorporar la **cláusula laboral** en los contratos de trabajo y el **compromiso por cargo o rol** para quien trata datos; revisar los contratos con aliados para aplicar la **cláusula de transferencia** o la **de corresponsables**.

## Mejorar las plantillas

- **En el generador web:** "Editar plantilla" permite corregir el texto; "Importar plantilla propia" agrega un documento que ya uses. Cada `[MARCADOR]` nuevo genera su campo automáticamente. Los cambios quedan en el navegador: usa "Copiar Markdown" para llevarlos al repositorio.
- **En el repositorio:** deja documentos anonimizados en `referencias/plantillas/` para que Claude Code proponga mejoras de estructura.

## Firma de responsabilidad

El generador agrega al final de cada documento un bloque "Elaborado por / Revisado y aprobado por" (desactivable). La exportación a Word también lo incluye (`SIN_FIRMA=1` para omitirlo).

## Convenciones

- `[MAYÚSCULAS ENTRE CORCHETES]`: dato a completar.
- `[texto / alternativa]`: elegir una opción.
- Bloques con `>`: notas para quien redacta; eliminarlas antes de usar el documento.

## Limitaciones

- Son plantillas generales; deben adaptarse al sector (salud, financiero, educación) y a la normativa especial aplicable.
- Pendiente de verificación literal: elementos del art. 12 LOPDP y reglas sobre consentimiento de adolescentes (ver `BASE-LEGAL.md`).
