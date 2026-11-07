# 02 · Kit de plantillas

## Propósito

Documentos base para que un responsable del tratamiento cumpla el deber de información, formalice la relación con sus encargados y obtenga consentimientos válidos cuando corresponda.

## Archivos

| Plantilla | Cuándo se usa | Base |
|---|---|---|
| `politica-privacidad.md` | Política completa (segunda capa) para web, contratos y atención de titulares | LOPDP arts. 7 y 12 |
| `aviso-privacidad.md` | Texto breve junto a formularios, letreros de videovigilancia y correos (primera capa) | LOPDP art. 12 |
| `contrato-encargo.md` | Con cada proveedor que trate datos por cuenta del responsable | RGLOPDP art. 41; Res. SPDP-SPD-2025-0006-R, Anexo I; LOPDP art. 68 num. 9 |
| `clausulas-consentimiento.md` | Cláusula para contratos con clientes y autorizaciones específicas (marketing, datos sensibles, NNA, imagen) | LOPDP art. 7; Res. SPDP-SPD-2025-0006-R, Anexo I |
| `generador-documentos.html` | Versión web: completas los datos una vez y se rellenan todas las plantillas | — |
| `docx/` | Versiones Word generadas con `scripts/exportar_docx.sh` | — |

## Orden de trabajo recomendado

1. Completar primero el **RAT** (herramienta 01): la política se alimenta de él.
2. Redactar la **política de privacidad**.
3. Derivar de ella los **avisos** de cada punto de recolección.
4. Identificar en el RAT la columna "Encargados" y firmar un **contrato de encargo** con cada uno.
5. Usar las **cláusulas de consentimiento** solo para las finalidades cuya base sea el consentimiento.

## Convenciones

- `[MAYÚSCULAS ENTRE CORCHETES]`: dato a completar.
- `[texto / alternativa]`: elegir una opción.
- Bloques con `>`: notas para quien redacta; eliminarlas antes de usar el documento.

## Limitaciones

- Son plantillas generales; deben adaptarse al sector (salud, financiero, educación) y a la normativa especial aplicable.
- Pendiente de verificación literal: elementos del art. 12 LOPDP y reglas sobre consentimiento de adolescentes (ver `BASE-LEGAL.md`).
