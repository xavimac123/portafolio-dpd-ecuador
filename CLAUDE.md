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

## Estructura

- `01-registro-tratamientos/` — RAT
- `02-kit-plantillas/` — documentos contractuales e informativos
- `03-kit-vulneraciones/` — gestión y notificación de vulneraciones
- `docs/` — decisiones del proyecto
- `scripts/` — generadores (Excel, exportación a Word)
