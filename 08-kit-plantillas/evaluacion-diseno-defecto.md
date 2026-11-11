# Evaluación de Protección de Datos desde el Diseño y por Defecto

**[RAZÓN SOCIAL]** · RUC [RUC] · Proyecto: [NOMBRE DEL PROYECTO] · Fecha: [FECHA]

> **Nota para quien redacta (eliminar antes de usar):**
> - Base: LOPDP arts. 39 (definición), 47 num. 9 (obligación del responsable) y 67 num. 2 (no implementarla es infracción leve); RGLOPDP arts. 59 (medidas desde el diseño, antes del tratamiento) y 60 (medidas por defecto); Res. SPDP-SPD-2025-0040-R, Guía de Protección de Datos Personales desde el Diseño y por Defecto (RO 163, 13-11-2025).
> - **Qué es obligatorio** (Res. 0040 art. 2): los principios de los capítulos 1 y 2 de la guía, cuando sean aplicables según la naturaleza, el alcance y las características del tratamiento. El resto es orientativo. Las tácticas del capítulo 2 se escogen en proporción al riesgo. El eje DevSecOps solo es obligatorio si hay desarrollo o personalización de software. El capítulo 3 (madurez) es optativo, pero recomendado.
> - **Cuándo se usa:** en la concepción de todo proyecto, sistema, aplicación, formulario, campaña, herramienta de IA o cambio relevante que trate datos personales, **antes** de empezar. Repítala al pasar de diseño a producción.
> - **Quién hace qué:** la empresa (dueño del proyecto, TI y legal) completa la evaluación y decide. El DPD revisa y emite observaciones no vinculantes (Res. SPDP-SPD-2025-0028-R arts. 13.1 y 15.2).
> - La escala de la columna «Nivel» reproduce los niveles de la guía (§ 3.1). Sus porcentajes se aplican por proceso con su justificación (rationale).

## A. Identificación del proyecto

| Campo | Detalle |
|---|---|
| Proyecto o cambio | [NOMBRE DEL PROYECTO] |
| Dueño del proyecto | [NOMBRE Y CARGO] |
| Fase actual | [Concepción / Diseño / Desarrollo / Pruebas / Puesta en marcha] |
| Actividad del RAT relacionada | [ACTIVIDAD O «NUEVA»] |
| Finalidad y base de legitimación | [FINALIDAD] · [BASE] |
| Titulares y categorías de datos | [TITULARES] · [DATOS] |
| ¿Incluye datos sensibles, de NNA, biométricos o IA? | [Sí / No · cuáles] |
| ¿Hay desarrollo o personalización de software? (activa DevSecOps) | [Sí / No] |
| Encargados o proveedores | [PROVEEDORES] |
| ¿Requiere evaluación de impacto (LOPDP art. 42)? | [Sí / No · referencia a la herramienta 07] |

## B. Factores para fijar las medidas (RGLOPDP art. 59)

| Factor | Descripción |
|---|---|
| 1. Naturaleza, ámbito y finalidad del tratamiento | [DESCRIPCIÓN] |
| 2. Riesgos, con su probabilidad y gravedad | [RIESGOS PRINCIPALES · referencia al análisis de riesgos] |
| 3. Estado de la técnica | [SOLUCIONES DISPONIBLES Y ACEPTADAS] |
| 4. Coste de aplicación | [ESTIMACIÓN Y JUSTIFICACIÓN] |

## C. Protección por defecto (RGLOPDP art. 60; guía § 1.2)

«Por defecto» son los valores que el sistema trae preconfigurados. Por defecto deben quedar activados la minimización y los mecanismos para ejercer los derechos.

| Aspecto | Pregunta | Configuración por defecto propuesta | ¿Cumple? |
|---|---|---|---|
| Cantidad de datos | ¿El formulario o sistema solo pide los datos necesarios? ¿Los campos opcionales están marcados como tales? | | |
| Extensión del tratamiento | ¿Los usos adicionales (marketing, perfiles, compartir con terceros) vienen desactivados hasta que el titular los acepte? | | |
| Período de almacenamiento | ¿El sistema elimina o anonimiza solo al vencer el plazo del RAT? | | |
| Accesibilidad | ¿Los perfiles y registros son privados por defecto y el acceso interno es por rol? | | |
| No accesibles a un número indefinido de personas | ¿Ningún dato queda publicado o indexable de forma automática sin una acción del titular? | | |
| Derechos preconfigurados | ¿Existen opciones para acceder, corregir, eliminar, oponerse, portar y revocar el consentimiento? | | |

## D. Eje DevPrivOps: principios de privacidad (guía § 2.1)

> Niveles de la guía (§ 3.1): 0 caótico (no considerado, 0 %); 1 implícito (menos del 25 %); 2 temprano explícito (25 % a 75 %); 3 maduro explícito (más del 75 %).

| Principio | Tácticas de la guía | Medida en este proyecto | Evidencia | Nivel (0 a 3) |
|---|---|---|---|---|
| 2.1.1 Minimizar | Seleccionar, excluir, remover, eliminar (incluso en respaldos, si es técnicamente posible) | | | |
| 2.1.2 Ocultar | Restringir, ofuscar, disociar, mezclar | | | |
| 2.1.3 Separar | Aislar, distribuir | | | |
| 2.1.4 Abstraer | Sumarizar, agrupar, perturbar | | | |
| 2.1.5 Informar | Suministrar, explicar, notificar | | | |
| 2.1.6 Controlar | Consentir, escoger, actualizar, retraer | | | |
| 2.1.7 Cumplir | Responsabilizar (personal especializado), declaración de aplicabilidad, monitorear | | | |
| 2.1.8 Demostrar | Registrar, auditar, reportar a la SPDP cuando se requiera | | | |

## E. Eje DevSecOps: seguridad en el desarrollo (guía § 2.2; solo si hay desarrollo o personalización de software)

| Principio | Qué se espera | Medida en este proyecto | Evidencia | Nivel (0 a 3) |
|---|---|---|---|---|
| 2.2.1 Integración temprana | Cifrado, autenticación robusta y minimización desde el inicio | | | |
| 2.2.2 Automatización | Análisis de código (SAST, DAST, SCA), escaneo de infraestructura como código, detección de fuga de datos, validaciones en el flujo de integración y despliegue | | | |
| 2.2.3 Colaboración interdisciplinaria | Desarrollo, operaciones, seguridad y protección de datos trabajan juntos; minimización validada en el diseño; sin datos reales en pruebas; accesos según sensibilidad | | | |
| 2.2.4 Monitoreo y retroalimentación continua | Detección de intrusos, monitoreo de registros en tiempo real, alertas | | | |

## F. Eje DevRiskOps: gestión de riesgos (guía § 2.3)

| Principio | Medida o evidencia en este proyecto | Nivel (0 a 3) |
|---|---|---|
| 2.3.1 Gestión de riesgos para derechos y libertades desde la concepción | | |
| 2.3.2 Integración con la gestión de riesgos de seguridad de la información | | |
| 2.3.3 Estándares de mejores prácticas, con métricas y modelos de riesgo | | |
| 2.3.4 Justificación (rationale) de los valores y criterios de los modelos | | |
| 2.3.5 Conformidad efectiva en la práctica, no solo en el papel | | |
| 2.3.6 Auditoría de eficacia y eficiencia, considerando el ROSI | | |
| 2.3.7 Prevención de vulneraciones de confidencialidad, integridad y disponibilidad | | |

## G. Declaración de aplicabilidad (guía § 2.1.7)

Indique qué controles se aplican y por qué se excluye alguno. Las exclusiones deben responder al riesgo y a la naturaleza del tratamiento, no solo al costo.

| Control o táctica | ¿Se aplica? | Justificación | Responsable | Fecha de implementación |
|---|---|---|---|---|
| | | | | |
| | | | | |

## H. Madurez del proyecto (guía cap. 3; optativo)

| Eje | Promedio de niveles | Rationale (dato, fuente o criterio experto) |
|---|---|---|
| DevPrivOps | | |
| DevSecOps (si aplica) | | |
| DevRiskOps | | |

> Para la empresa en conjunto, la guía calibra cada principio sobre todos los procesos del RAT (espacio de muestreo) y promedia por eje (§§ 3.2 y 3.3). La herramienta 03, eje 9, ofrece una aproximación general.

## I. Conclusión y observaciones

| Campo | Detalle |
|---|---|
| Decisión de la empresa | [Puede iniciar / Puede iniciar con las medidas pendientes de la parte G / No puede iniciar] |
| Medidas pendientes antes de iniciar | [DETALLE] |
| Fecha de revisión | [FECHA] |
| Observaciones del DPD (no vinculantes) | [OBSERVACIONES] |

Aprobado por: [NOMBRE DEL REPRESENTANTE LEGAL] · [CARGO DEL REPRESENTANTE LEGAL]
