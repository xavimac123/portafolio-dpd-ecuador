# Contraste de las herramientas con las guías de la SPDP

Revisión del 2026-11-08, actualizada el 2026-11-09 con los resúmenes estructurados (JSON) aportados por el usuario. Compara cada exigencia de las dos guías técnicas de la Superintendencia de Protección de Datos Personales (SPDP) con las herramientas del portafolio, para que ningún paso quede sin cubrir.

- **Guía v2 de gestión de riesgos y evaluación de impacto** (RES-2026-0012). Capítulo I obligatorio; capítulo II referencial. Lectura parcial: capítulo I y etapas 1 a 3.
- **Guía de protección de datos desde el diseño y por defecto** (RES-2025-0040). Lectura de la versión de julio de 2025.

Estado: ✅ cubierto · 🟡 parcial · ⬜ pendiente.

## 1. Guía v2: principios (capítulo I, obligatorio)

| Exigencia | Herramienta | Estado | Qué se hizo o qué falta |
|---|---|---|---|
| Rechazo del cumplimiento «en el papel»: no basta con listas de chequeo | 03, 07 | 🟡 | La 07 ahora pide la justificación de cada valor de impacto y probabilidad. La 03 sigue siendo un cuestionario: se presenta como diagnóstico inicial, no como gestión de riesgos |
| Justificación (rationale) de todo valor de entrada | 07 | ✅ | Campo obligatorio por riesgo, aviso si falta y columna en el informe y la matriz |
| Integración con la seguridad de la información | 07 | ✅ | Dimensiones de confidencialidad, integridad, disponibilidad y derechos |
| Estándares como referencia, no como garantía | Guía, cap. 13 | ✅ | La guía del DPD presenta ISO como apoyo |
| Auditorías jurídicas, organizacionales y técnicas | 01 (S20 y S21), guía cap. 12 | 🟡 | Las auditorías técnicas (pruebas de penetración) exceden el rol del DPD: se recomiendan a especialistas |
| Vulneraciones: notificación a la SPDP en cinco días | 09 | ✅ | Panel de plazos |

## 2. Guía v2: procedimiento (capítulo II, referencial)

| Etapa | Exigencia | Herramienta | Estado | Qué se hizo o qué falta |
|---|---|---|---|---|
| 1. Contexto | Criterios de impacto: categorías especiales, grupos vulnerables, número de titulares, naturaleza de la afectación, volumen por titular | 07, pestaña 4 | ✅ | **Nuevo.** Cinco factores con piso de impacto sugerido (regla de cálculo de criterio propio) |
| 1. Contexto | Probabilidad en un lapso definido | 07 | ✅ | **Nuevo.** Periodo de referencia |
| 1. Contexto | Aceptación del riesgo: capacidad y tolerancia | 07, 03 | ✅ | Capacidad en USD (nuevo) y umbral de riesgo residual |
| 1. Contexto | Coordinación del DPD con las demás áreas | Guía, cap. 3 y 10 | ✅ | Roadmap del DPD (nuevo) |
| 2. Identificación | Datos: RAT con dónde, quién, qué datos y cadena de activos | 04 | ✅ | Campo de sistemas y soportes |
| 2. Identificación | Comunidades de amenaza y capacidad | 07 | ✅ | Catálogo de amenazas |
| 2. Identificación | Vulnerabilidades jurídicas, de grupos vulnerables, organizacionales y técnicas | 07 | ✅ | Las cuatro categorías |
| 2. Identificación | Escenarios de riesgo con impactos primarios y secundarios | 07 | ✅ | **Nuevo.** Rótulo de impactos primarios y secundarios y derechos afectados por escenario |
| 3. Análisis | Modelo cualitativo calibrado con justificación; Delphi, Lens o análisis argumental | 07 | ✅ | Método declarado en el contexto, con las opciones de la guía |
| 3. Análisis | Modelos cuantitativos (frecuentista, bayesiano, Monte Carlo, FAIR) | 03 (multas) | 🟡 | Solo la estimación de multas usa simulación. Una evaluación cuantitativa completa requiere datos que las pymes rara vez tienen; queda como mejora futura |
| 3. Análisis | Advertencia sobre matrices que subestiman riesgos de baja probabilidad y alto impacto | 07 | ✅ | Aviso automático |
| 3. Análisis | Modelos paralelos para grupos vulnerables | 07 | 🟡 | Se reflejan en el piso de impacto; no hay un modelo separado |
| 4. Evaluación | Comparar con la aceptación y decidir | 07, pestaña 6 | ✅ | Umbral y dictamen sugerido |
| 5. Tratamiento | Medidas, responsables y plazos; estrategias aceptar, modificar, transferir o evitar | 07 | ✅ | Decisión con las cuatro estrategias de la guía («Modificar» reemplaza a «Mitigar»), responsable y plazo |
| 5. Tratamiento | Retorno de la inversión en seguridad (ROSI) y FAIR-CAM | — | ⬜ | Requiere datos de pérdidas y costos de controles; mejora futura |
| 5. Tratamiento | Declaración de aplicabilidad | — | ⬜ | Texto no leído. Pendiente al obtener la guía completa |
| Anexo | Formato oficial de evaluación de impacto | 07 | ⬜ | Anexo no leído. El informe sigue el art. 32 RGLOPDP; contrastar con el anexo |

## 3. Guía de diseño y por defecto

| Exigencia | Herramienta | Estado | Qué se hizo o qué falta |
|---|---|---|---|
| Considerar los riesgos desde la planificación del proyecto | 01 (S24), 07 | ✅ | Servicio de privacidad desde el diseño y pregunta de tecnología nueva en la 07 |
| Por defecto, solo los datos necesarios para cada finalidad | 06, 07 | ✅ | Criterios de minimización en ambas |
| Principio «minimizar» | 07 | ✅ | Control de minimización y plazo con borrado |
| Principio «ocultar» | 07 | ✅ | Cifrado, seudonimización, control de acceso |
| Principio «separar» | 07 | ✅ | **Nuevo** control: separación de bases o entornos |
| Principio «abstraer» | 07 | ✅ | **Nuevo** control: agregación o generalización |
| Principio «informar» | 08 | ✅ | Política, avisos y comunicación de vulneraciones |
| Principio «controlar» | 08, 06 | ✅ | Consentimiento y oposición; canal de derechos |
| Principio «cumplir» | 07, 03 | 🟡 | Responsables y plazos por medida; falta la declaración de aplicabilidad |
| Principio «demostrar» | 04, 09 | ✅ | RAT, bitácora e informes |
| Configuración por defecto más protectora | 07 | ✅ | **Nuevo** control |
| Madurez por principio (niveles 0 a 3: 0 %, menos de 25 %, 25 % a 75 %, más de 75 %) sobre las actividades del RAT, calibrada por eje (DevPrivOps, DevSecOps, DevRiskOps) | 03 | 🟡 | La 03 mide por dominio, no por principio y actividad. Las tácticas de cada principio ya constan en BASE-LEGAL. Candidata a una herramienta propia de madurez desde el diseño |
| DevSecOps y DevRiskOps | Guía, cap. 13 | 🟡 | Se mencionan; su ejecución corresponde al área de tecnología, no al DPD |

## 4. Decisiones

1. Las escalas siguen siendo de criterio propio y se rotulan así; la guía v2 lo permite en su capítulo II.
2. La herramienta 07 no implementa modelos cuantitativos: el DPD de una pyme rara vez cuenta con datos de frecuencias y pérdidas. Si el cliente los tiene, el método «cuantitativo» del contexto documenta que se usaron fuera de la herramienta.
3. Los puntos ⬜ están en `docs/recursos-pendientes.md` y en «Puntos abiertos» de `BASE-LEGAL.md`.
