# 09 · Kit de respuesta a vulneraciones

## Propósito

Que una organización sepa qué hacer en las primeras horas de una vulneración de la seguridad de datos personales: contener, evaluar, cumplir los plazos de notificación y dejar evidencia.

## Archivos

| Archivo | Uso |
|---|---|
| `protocolo-respuesta.md` | Protocolo interno para aprobar: equipo, fases, plazos, evaluación de riesgo |
| `bitacora-vulneracion.md` | Registro de cada incidente, se notifique o no |
| `comunicacion-encargado-responsable.md` | Aviso del proveedor al responsable (máximo 2 días) |
| `notificacion-spdp.md` | Lista para reunir la información antes de llenar el formulario del SISPDP |
| `comunicacion-titulares.md` | Modelo de comunicación en lenguaje claro |
| `asistente-vulneraciones.html` | Versión web: calcula plazos, orienta la evaluación de riesgo y rellena los modelos |
| `docx/` | Versiones Word generadas con `scripts/exportar_docx.sh` |

## Base legal

- LOPDP art. 43, reformado por la Ley Orgánica para el Fortalecimiento de la Ciberseguridad (RO 5to Supl. 290, 22-05-2026): notificación a SPDP, ARCOTEL y CSIRT.
- RGLOPDP arts. 24 a 28: causales de riesgo, contenido de la notificación, notificación del encargado y del titular.
- Res. SPDP-SPD-2026-0040-R: norma técnica (tipos de vulneración, 2 días encargado, 5 días responsable, SISPDP, contenido para titulares).
- LOPDP art. 46: notificación a titulares (plazo pendiente de verificación).

## Puntos abiertos

Antes de usar con un cliente, cerrar en `BASE-LEGAL.md`:

1. Plazo exacto de comunicación a titulares.
2. Canal y plazo de notificación a ARCOTEL y al CSIRT tras la reforma.
3. Campos actuales del formulario del SISPDP.

## Limitaciones

- El cálculo de días hábiles excluye fines de semana y solo los feriados que ingrese el usuario.
- La evaluación de riesgo del asistente es orientativa; la decisión final y su justificación corresponden al responsable y su DPD.
