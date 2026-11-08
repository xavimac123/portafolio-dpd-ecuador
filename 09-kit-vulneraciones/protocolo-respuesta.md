# Protocolo de Respuesta a Vulneraciones de la Seguridad de Datos Personales

**[RAZÓN SOCIAL]** · Versión [VERSIÓN] · Aprobado el [FECHA] por [ÓRGANO QUE APRUEBA]

> **Nota para quien redacta (eliminar antes de aprobar):** base normativa: LOPDP art. 43 (reformado por la Ley Orgánica para el Fortalecimiento de la Ciberseguridad, RO 5to Supl. 290, 22-05-2026), RGLOPDP arts. 24 a 28 y Res. SPDP-SPD-2026-0040-R (norma técnica de notificación). El plazo de notificación a titulares y la forma de notificar al CSIRT están pendientes de verificación (ver BASE-LEGAL.md). Revisa este protocolo cada vez que la SPDP emita normativa sobre la materia.

## 1. Objetivo y alcance

Establecer cómo [RAZÓN SOCIAL] detecta, contiene, evalúa, notifica y documenta las vulneraciones de la seguridad de los datos personales que trata como responsable o encargado.

Aplica a todo el personal, a los encargados del tratamiento y a cualquier persona que acceda a datos personales por cuenta de [RAZÓN SOCIAL].

## 2. Qué es una vulneración

Todo incidente que afecte la **confidencialidad**, la **integridad** o la **disponibilidad** de datos personales. Un mismo incidente puede afectar más de una dimensión.

| Tipo | Ejemplos |
|---|---|
| Confidencialidad | Correo con datos enviado al destinatario equivocado; acceso no autorizado a una base de datos; robo de una laptop sin cifrar; publicación accidental |
| Integridad | Alteración no autorizada de registros; datos corrompidos por un error o un ataque |
| Disponibilidad | Ransomware; pérdida de respaldos; borrado accidental sin copia; caída prolongada de un sistema |

**Debe notificarse a la autoridad** cuando la vulneración probablemente represente un riesgo para los derechos y libertades de los titulares, en particular si (RGLOPDP art. 24):

1. los datos se destruyeron, dejaron de existir o no están disponibles de forma útil;
2. los datos se alteraron, corrompieron o quedaron incompletos;
3. se perdió el control o el acceso a los datos;
4. el tratamiento no fue autorizado o es ilícito, incluida la divulgación o el acceso por destinatarios no autorizados.

## 3. Equipo de respuesta

| Rol | Persona | Contacto | Funciones |
|---|---|---|---|
| Coordinador | [NOMBRE] | [CONTACTO] | Dirige la respuesta y decide sobre las notificaciones |
| Delegado de Protección de Datos | [NOMBRE] | [CONTACTO] | Evalúa el riesgo, prepara notificaciones, lleva la bitácora |
| Responsable de TI / seguridad | [NOMBRE] | [CONTACTO] | Contención técnica, análisis de causa, evidencias |
| Asesor legal | [NOMBRE] | [CONTACTO] | Revisión jurídica, relación con autoridades |
| Comunicación | [NOMBRE] | [CONTACTO] | Comunicación a titulares y, si procede, a medios |

## 4. Fases y plazos

| Fase | Qué se hace | Plazo |
|---|---|---|
| 0. Detección y reporte interno | Quien detecte el incidente lo reporta de inmediato a [CANAL INTERNO] | Inmediato |
| 1. Contención | Aislar sistemas, revocar accesos, cambiar credenciales, recuperar información enviada por error | Primeras horas |
| 2. Evaluación | Determinar tipo, datos y titulares afectados, causa presunta y nivel de riesgo. Abrir la bitácora | Día 1 |
| 3a. Encargado → responsable | Si [RAZÓN SOCIAL] actúa como encargado, comunica al responsable | **Máximo 2 días** (Res. SPDP-SPD-2026-0040-R) |
| 3b. Notificación a la SPDP | Mediante el formulario del SISPDP (servicios.spdp.gob.ec) | **Término de 5 días** desde que se tuvo constancia (LOPDP art. 43) |
| 3c. Notificación a ARCOTEL y al CSIRT | Según el art. 43 reformado | [VERIFICAR PLAZO Y CANAL] |
| 3d. Comunicación a titulares | Por los canales habituales de contacto, en lenguaje claro | [VERIFICAR PLAZO VIGENTE — la doctrina cita 3 días, art. 46 LOPDP] |
| 4. Remediación | Corregir la causa, reforzar medidas, actualizar RAT y evaluación de riesgos | Según el plan |
| 5. Cierre y lecciones aprendidas | Informe final, actualización de este protocolo, capacitación | 30 días después del cierre |

> "Término" se computa en días hábiles. Lleva la cuenta desde el momento en que [RAZÓN SOCIAL] tuvo constancia de la vulneración y deja registro de esa fecha.

## 5. Evaluación del riesgo

Valorar, como mínimo:

- **Tipo de datos:** ¿categorías especiales (salud, biométricos), datos financieros, credenciales, datos de niñas, niños y adolescentes?
- **Volumen:** número de titulares y de registros.
- **Facilidad de identificación:** ¿los datos permiten identificar directamente a las personas?
- **Consecuencias:** fraude, suplantación de identidad, discriminación, daño reputacional, pérdida de acceso a servicios.
- **Reversibilidad:** ¿se pueden recuperar o restablecer los datos? Una vulneración de confidencialidad es, en esencia, permanente.
- **Medidas que reducen el riesgo:** cifrado robusto, recuperación inmediata, confirmación de que el receptor eliminó la información.

Resultado: **sin riesgo aparente / riesgo / riesgo alto**. Documentar la justificación aunque se decida no notificar.

## 6. Contenido de las notificaciones

- **A la SPDP** (RGLOPDP art. 26): naturaleza y tipo de vulneración; titulares afectados; sistemas vulnerados; causa presunta; volumen y tipos de datos; medidas adoptadas y previstas; evaluación del riesgo; otros aspectos que determine la autoridad.
- **Del encargado al responsable** (RGLOPDP art. 27): lo mismo, excepto la evaluación del riesgo.
- **A los titulares** (RGLOPDP art. 28; Res. SPDP-SPD-2026-0040-R): naturaleza de la vulneración; fecha o período estimado; medidas adoptadas; recomendaciones para protegerse; lenguaje claro y sencillo.

Modelos: ver `comunicacion-encargado-responsable.md`, `notificacion-spdp.md` y `comunicacion-titulares.md`.

## 7. Registro y evidencias

Toda vulneración, se notifique o no, se registra en la bitácora (`bitacora-vulneracion.md`). Conservar: constancia de recepción del SISPDP, copias de las comunicaciones, evidencias técnicas y decisiones con su justificación.

## 8. Consecuencias del incumplimiento

La falta de notificación a los titulares constituye infracción grave. Notificar fuera de plazo o de forma incompleta también expone a sanción.

## 9. Revisión

Este protocolo se revisa al menos una vez al año, después de cada vulneración relevante y cuando cambie la normativa.
