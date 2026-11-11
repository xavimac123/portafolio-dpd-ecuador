# Metodología de la calculadora de honorarios del DPD

Versión 0.1. Fuente única: `scripts/honorarios_config.py`.

> **Criterio propio.** No existe en Ecuador una tabla oficial ni gremial de honorarios para el Delegado de Protección de Datos. Los tramos, pisos, tarifas y factores de esta herramienta son criterio propio de Macías Sánchez Consultores, contrastados con referencias públicas del mercado (sección «Referencias de mercado»). Solo son normativos: la clasificación de empresas, el Modelo Técnico de Gran Escala, la tarifa del IVA, las retenciones y los rubros laborales del DPD interno.

## Fases del servicio

| Fase | Cobro | Qué incluye |
|---|---|---|
| Evaluación inicial | Única vez | Diagnóstico de madurez, exposición económica, análisis de gran escala y plan de acción |
| Implementación (referencial) | Única vez | RAT, política y avisos, contratos de encargo, protocolo de vulneraciones, derechos. La decide el responsable y la ejecuta su personal, un proveedor o un tercero coordinado por MSC; solo suma a la proforma si la factura MSC (subcontratada o como consultor que no es DPO del cliente). Si no, el valor sirve para comparar la cotización del implementador |
| Revisión y verificación | Por evaluación o por hito | S29 revisión del DPO a evaluaciones elaboradas por el responsable; S30 verificación de lo implementado |
| Control | Mensual | DPD externo o acompañamiento: supervisión, RAT vivo, derechos, incidentes, reporte a la gerencia |

## Tamaño de la empresa

Reglamento a la Estructura e Institucionalidad de Desarrollo Productivo del COPCI, art. 106; COPCI art. 53 (las ventas prevalecen sobre los trabajadores).

| Tamaño | Trabajadores | Ventas anuales (USD) |
|---|---|---|
| Microempresa | 1 a 9 | $0 a $100.000 |
| Pequeña empresa | 10 a 49 | $100.000 a $1.000.000 |
| Mediana empresa | 50 a 199 | $1.000.000 a $5.000.000 |
| Gran empresa | 200 o más | más de $5.000.000 |

Factor sectorial (criterio propio): Logística, transporte o courier ×1,15; Turismo, hotelería o restaurantes ×1,05; Tecnología o comercio electrónico ×1,2; Seguridad privada o vigilancia ×1,2; Educación (niñas, niños y adolescentes) ×1,25; Salud ×1,3; Financiero, seguros o crédito ×1,3; Organización sin fines de lucro ×0,9. Resto ×1.

## Método 1 · Volumen de negocio

Honorario **anual** de control = suma de cada tramo de ventas × su porcentaje marginal. Control mensual = máximo entre el piso del tamaño y el anual / 12.

| Tramo de ventas | % marginal |
|---|---|
| $0 a $100.000 | 0,9 % |
| $100.000 a $1.000.000 | 0,25 % |
| $1.000.000 a $5.000.000 | 0,08 % |
| $5.000.000 a $20.000.000 | 0,03 % |
| $20.000.000 a más | 0,01 % |

| | Micro | Pequeña | Mediana | Grande |
|---|---|---|---|---|
| Piso mensual | $120 | $200 | $350 | $700 |
| Piso evaluación inicial | $350 | $600 | $1.100 | $2.200 |
| Piso adecuación | $900 | $1.800 | $3.500 | $7.000 |

Evaluación inicial = máx(piso, 35 % del control anual). Implementación (referencial) = máx(piso, 90 % del control anual).

## Método 2 · Volumen de tratamiento

El puntaje es el **Modelo Técnico de Gran Escala (MTGE)** de la Res. SPDP-SPD-2026-0005-R (art. 8: variables; art. 9: suma; art. 10: umbral de 6 puntos; art. 12: efectos; art. 14: calificación directa). Se aplica al tratamiento principal del cliente.

| Variable | Opciones y puntos |
|---|---|
| Número de titulares (12 meses, tratamiento) | 0 a 1.000 (1); 1.001 a 10.000 (2); 10.001 a 100.000 (3); Más de 100.000 (4) |
| Volumen: tipos de datos por titular | Hasta 10 (0,5); 11 a 30 (1); 31 a 100 (2); 101 o más (3) |
| Categorías de datos | Solo datos básicos (0,5); Incluye una categoría especial (2); Más de una categoría especial, grupos vulnerables o datos penales (3) |
| Frecuencia | Puntual (0,5); Periódica o recurrente (1); Continua o en tiempo real (2) |
| Permanencia | Ocasional (0,5); Temporal (menos de 3 años) (1); Prolongada (3 años o más) (2) |
| Alcance geográfico | Local (1); Nacional (2); Global o transfronterizo (3) |

Calificación directa (art. 14): Datos de salud (sistemas de salud, seguridad social, historias clínicas) u otras categorías especiales; Evaluación sistemática automatizada de aspectos personales (perfiles, predicción) con efectos jurídicos; Observación sistemática de personas en espacios públicos (videovigilancia u otro monitoreo continuo); Datos biométricos o geolocalización de titulares; Sistemas de información crediticia, financiera o de riesgo económico; Datos de niñas, niños y adolescentes en entornos dirigidos a ellos; Transferencias sistemáticas que constituyen flujos continuos o estructurales; Servicios de mensajería, correo expreso o courier.

Tarifario sobre el puntaje (criterio propio):

| Concepto | Valor |
|---|---|
| Base mensual por puntaje | $120 (menos de 4), $220 (4 a 5,9), $420 (gran escala) |
| Por actividad sobre 5 | $12/mes |
| Por encargado | $8/mes |
| Transferencias internacionales | $40/mes |
| Por solicitud de derechos mensual | $20 |
| Por sede adicional | $30/mes |
| Evaluación inicial | $250 + $45 por actividad + $15 por encargado + $300 si es gran escala + $100 por sede adicional |
| Implementación (referencial) | $600 + $120 por actividad + $40 por encargado + $450 por evaluación de impacto |

## Método 3 · Estimación técnica

Horas por tarea × tarifa por hora × (1 + gastos indirectos). Las horas aumentan con el factor sectorial. Es el **piso** de la negociación.

| Perfil | Tarifa sin IVA |
|---|---|
| Consultor en formación (sin registro como DPD) | $25/h |
| Consultor con programa profesionalizante | $35/h |
| Especialista con experiencia acreditada | $50/h |
| Especialista con certificación ISO/IEC 27701 | $70/h |

Gastos indirectos y reserva por defecto: 15 %. Áreas a entrevistar por tamaño: Micro 3, Pequeña 5, Mediana 8, Grande 12.

**Evaluación inicial**

| Tarea | Horas |
|---|---|
| Reunión de inicio y plan de trabajo | 2 fijo |
| Entrevistas por área | 1,25 por área |
| Revisión documental | 2 fijo + 0,5 por actividad |
| Diagnóstico de madurez y exposición económica | 3 fijo |
| Levantamiento preliminar de actividades | 0,75 por actividad |
| Encargados y transferencias | 0,3 por encargado + 1 si hay transferencias |
| Informe y presentación a la gerencia | 4 fijo |

**Implementación (referencial)**

| Tarea | Horas |
|---|---|
| Registro de actividades (RAT) completo | 2 fijo + 2 por actividad |
| Política de privacidad y avisos | 6 fijo + 0,5 por área |
| Contratos de encargo y cláusulas | 1 fijo + 1 por encargado |
| Evaluaciones de impacto | 8 por evaluación de impacto |
| Protocolo de vulneraciones y procedimiento de derechos | 6 fijo |
| Capacitación inicial | 3 fijo |
| Designación del DPD y registro ante la SPDP | 2 fijo |

**Control mensual**

| Tarea | Horas |
|---|---|
| Revisión y actualización del RAT | 1 fijo + 0,15 por actividad |
| Supervisión de encargados | 0,1 por encargado |
| Atención de solicitudes de derechos | 0,75 por solicitud |
| Gestión de incidentes (promedio mensual) | 0,5 fijo |
| Capacitación (prorrateo anual) | 0,083 por hora de capacitación anual |
| Reporte y reunión con la gerencia | 1,5 fijo |
| Vigilancia normativa y asesoría a proyectos | 1 fijo + 2 si es gran escala |
| Comunicación con la SPDP | 0,5 fijo |

## Recomendación

Para cada fase: mediana de los tres métodos, y nunca menos que la estimación técnica. La herramienta advierte cuando el volumen de negocio no cubre el costo técnico (proponer menor alcance o cobro por evento) y cuando el tratamiento es de gran escala (el DPD es obligatorio).

## Otras modalidades

- **Paquetes** Esencial, Cumplimiento e Integral (servicios en `PAQUETES`).
- **Bolsa de horas** prepagada: 5 % de descuento por menos de 20 h, 10 % desde 20 h y 15 % desde 40 h (criterio propio).
- **Comparación con un DPD interno**: sueldo × 12 + aporte patronal 12,15 % + décimo tercero (Código del Trabajo art. 111) + décimo cuarto, un SBU de $482 (art. 113) + fondos de reserva 8,33 % (art. 196).
- **Retenciones** para el consultor (uso interno): retención de renta y de IVA según la tabla vigente del SRI.

## IVA y retenciones

- IVA: tarifa general 15 % (LRTI art. 65; el SRI recordó en la Circular NAC-DGECCGC25-00000006 que se mantiene mientras no la modifique un decreto ejecutivo).
- Retención de renta en honorarios profesionales de persona natural: 10 % (Res. NAC-DGERCGC26-00000009, desde el 1-03-2026). Sociedad: 5 % según resúmenes; verificar.
- Retención de IVA en honorarios profesionales de persona natural: 100 % del IVA cuando el cliente es agente de retención (tabla vigente del SRI; verificar).

## Referencias de mercado consultadas (no vinculantes)

| Fuente | Dato | Fecha de consulta |
|---|---|---|
| Blue Nova (bluenova.com.ec), guía LOPDP 2026 | DPD externo USD 300 a 800 al mes; asesoría legal USD 1.000 a 5.000; cumplimiento básico USD 2.500 a 7.000; precios sin IVA | 2026-11-08 |
| Blue Nova, diagnóstico LOPDP | Diagnóstico básico desde USD 500; con plan de acción desde USD 800; programa completo desde USD 2.500 | 2026-11-08 |
| delegadodatosecuador.com | Precios por proforma; modalidad de DPD externo distinta para pequeña empresa (factura menos de USD 1 millón o menos de 15 empleados) y mediana | 2026-11-08 |
| Aviso de empleo DPD, Quito (cazvid.com) | Sueldo de USD 1.500 a 2.500 al mes, tiempo completo | 2026-11-08 |
| Jorge Badiola, «¿Cómo calcular los honorarios del DPD?» (LinkedIn) | Variables: tamaño, trabajadores, sedes, encargados y trabajo previo; cláusula de recuperación del esfuerzo inicial | 2026-11-08 |

Actualice estas referencias y los parámetros económicos (IVA, SBU, retenciones) al inicio de cada año.
