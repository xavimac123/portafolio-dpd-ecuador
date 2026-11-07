# Portafolio DPD Ecuador

Herramientas para la gestión del cumplimiento de la **Ley Orgánica de Protección de Datos Personales (LOPDP)** y su Reglamento, desarrolladas por **Mariano Xavier Macías Sánchez — Macías Sánchez Consultores**.

> Estado: **privado / en desarrollo**. Todas las herramientas usan datos ficticios. No contienen información de clientes.

## Herramientas

| # | Herramienta | Contenido | Estado |
|---|---|---|---|
| 01 | [Registro de actividades de tratamiento](01-registro-tratamientos/) | Guía, plantilla Excel con validación de vacíos, ejemplo ficticio, asistente web | v0.1 |
| 02 | [Kit de plantillas](02-kit-plantillas/) | Política de privacidad, aviso de privacidad, contrato de encargo, cláusulas de consentimiento | v0.1 |
| 03 | [Kit de vulneraciones](03-kit-vulneraciones/) | Protocolo, bitácora, modelos de comunicación encargado→responsable, SPDP y titulares | v0.1 |

## Cómo se usa

1. Cada carpeta tiene un `README.md` con instrucciones.
2. Las plantillas están en Markdown (`.md`) y se exportan a Word con `make docx` o `pandoc archivo.md -o archivo.docx`.
3. Los campos a completar van entre corchetes: `[RAZÓN SOCIAL]`.
4. La base normativa de todo el repositorio está en [BASE-LEGAL.md](BASE-LEGAL.md).

## Advertencia

Estas herramientas son material de apoyo y no sustituyen el análisis jurídico del caso concreto. La normativa ecuatoriana de protección de datos está en desarrollo activo por la Superintendencia de Protección de Datos Personales (SPDP); verifica la vigencia de cada norma antes de usarla.

## Licencia

Pendiente de definir antes de hacer público el repositorio (ver `docs/decision-licencia.md`).
