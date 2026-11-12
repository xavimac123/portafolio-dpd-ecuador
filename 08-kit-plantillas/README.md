# 08 · Kit de plantillas

## Propósito

Documentos base para que un responsable del tratamiento cumpla el deber de información, formalice la relación con sus encargados, obtenga consentimientos válidos cuando corresponda, fije sus reglas internas, atienda los derechos de los titulares, documente sus medidas de seguridad y deje evidencia de la supervisión (responsabilidad proactiva y demostrada, LOPDP art. 10 lit. k).

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
| `politica-interna.md` | Reglas internas para el personal: roles, principios, nuevos tratamientos, accesos, terceros, derechos, incidentes, conservación y revisión. Distinta de la política de privacidad | LOPDP arts. 10, 37, 47 nums. 4 y 10, 67 num. 3 |
| `formulario-derechos.md` | Formulario para que el titular ejerza sus derechos (lenguaje claro). Es un canal, no un requisito | LOPDP arts. 13 a 20, 24 y 62; RGLOPDP arts. 12 y 13 |
| `procedimiento-derechos.md` | Procedimiento interno, reglas por derecho, excepciones, modelos de aclaración y respuesta, registro de solicitudes y lista de supervisión del DPD | LOPDP arts. 13 a 20, 62, 64 y 67 num. 1; RGLOPDP arts. 12 a 17; Res. SPDP-SPD-2025-0028-R art. 13.2 |
| `registro-medidas-seguridad.md` | Inventario de medidas por tipo y tratamiento, verificación de su eficacia y evaluación de adecuación antes de un tratamiento nuevo | LOPDP arts. 37, 41, 47 nums. 2, 3, 6 y 7; Res. SPDP-SPD-2025-0028-R art. 13.4 |
| `plan-informe-supervision.md` | Plan e informe de supervisión del DPD con programa de verificación, hallazgos y seguimiento. No es auditoría acreditada ni certificación | LOPDP arts. 47 nums. 3 y 14, 49 y 54; Res. SPDP-SPD-2026-0012-R, Cap. I, § 6; Res. SPDP-SPD-2025-0028-R art. 13.6 |
| `evaluacion-diseno-defecto.md` | Evaluación previa de cada proyecto: factores del art. 59 RGLOPDP, ajustes por defecto, ejes DevPrivOps, DevSecOps y DevRiskOps, declaración de aplicabilidad y madurez | LOPDP arts. 39, 47 num. 9 y 67 num. 2; RGLOPDP arts. 59 y 60; Res. SPDP-SPD-2025-0040-R |
| `plan-capacitacion.md` | Guía para que el DPD organice la capacitación, diez módulos sugeridos, matriz de públicos, plan anual, registro de asistencia, evaluación e indicadores | LOPDP arts. 10 lit. k, 24, 47 nums. 2 y 10, 49 num. 1; RGLOPDP art. 30 num. 4 (ver BASE-LEGAL, punto 36) |
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
8. Aprobar la **política interna** y entregarla al personal con constancia de recepción.
9. Publicar el **formulario de derechos** junto a la política de privacidad y aprobar el **procedimiento de derechos** con su registro.
10. Levantar el **registro de medidas de seguridad** a partir del análisis de riesgos (herramienta 07) y verificar su eficacia.
11. Antes de cada proyecto nuevo, la empresa completa la **evaluación de diseño y por defecto** y el DPD la observa.
12. Aprobar el **plan de capacitación** anual y aplicar la inducción a cada trabajador nuevo.
13. Al cierre de cada periodo, el DPD aplica el **plan e informe de supervisión**; la empresa aprueba su plan de acción.

## Correspondencia con la lista de herramientas de cumplimiento de la responsabilidad proactiva

| Herramienta | Dónde está en MSC PD |
|---|---|
| Políticas de protección de datos | 08 · `politica-privacidad.md` (externa) y `politica-interna.md` |
| RAT | 04 |
| Privacidad desde el diseño y por defecto | 08 · `evaluacion-diseno-defecto.md`; 03 (eje 9) y servicio S24 |
| Análisis de riesgos | Calculadora de riesgos y 07 |
| Evaluación de impacto | 07 |
| Medidas de seguridad | 08 · `registro-medidas-seguridad.md` |
| Capacitación | 08 · `plan-capacitacion.md`; 03 (eje 12) y servicio del catálogo |
| DPD | Pestaña «Responsabilidades DPO» y 08 · `comunicacion-dpd.md` |
| Gestión de incidentes de seguridad | 09 |
| Supervisión y auditoría | 08 · `plan-informe-supervision.md` y pestaña «Responsabilidades DPO» |
| Gestión de derechos | 08 · `formulario-derechos.md` y `procedimiento-derechos.md` |
| Contratos con encargados | 08 · `contrato-encargo.md` y `clausula-encargo.md` |

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
- Derechos: la relación entre el término de 10 días del art. 62 y el plazo de 15 días de los arts. 13 a 16 está abierta (punto 27); el procedimiento aplica el criterio prudente de responder dentro de los 10 días.
- La estructura de la política interna, las columnas del registro de solicitudes, la escala de eficacia de las medidas, la clasificación de hallazgos y los módulos, duraciones e indicadores de capacitación son **criterio propio**: la SPDP aún no ha fijado su contenido.
- El DPD supervisa y recomienda en todos estos documentos; la empresa aprueba, implementa y firma (Res. SPDP-SPD-2025-0028-R art. 15).
