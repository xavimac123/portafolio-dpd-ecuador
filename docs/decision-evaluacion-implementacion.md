# Decisión: separar la evaluación y el diagnóstico de la implementación

Fecha: 2026-11-11. Estado: adoptada.

## Problema

Las herramientas presentaban a MSC como quien redacta los borradores (RAT, política, contratos, protocolos) y conduce el RAT, la ponderación del interés legítimo y la evaluación de impacto, y los paquetes de la proforma combinaban adecuación y DPD externo. Eso choca con la función del DPD:

- No puede implementar directamente la normativa (Res. SPDP-SPD-2025-0028-R art. 15.1).
- No ejecuta la gestión de riesgos ni la evaluación de impacto; solo emite observaciones no vinculantes (art. 15.2).
- No decide fines ni medios (art. 15.3).
- Hay conflicto de intereses si ejecuta o participa en tratamientos, y debe declararse (arts. 17 y 18).
- La organización puede contratar, aparte del DPD, implementación o consultoría con personas jurídicas (art. 12), pero la norma no dice si una misma firma puede prestar ambos servicios al mismo cliente (punto abierto 32 de `BASE-LEGAL.md`).

## Decisión

1. **Dos líneas.** *Evaluación, diagnóstico y supervisión*: la realiza MSC como consultor o como DPO. *Implementación*: la decide el responsable.
2. **Quién implementa** (lo elige el responsable): personal propio; proveedor que elija; implementador aliado presentado por MSC con **contrato y factura directos** (modalidad preferida); MSC mediante un tercero que MSC subcontrata y factura; o MSC como consultor.
3. **Borradores según el rol de MSC** (decisión del usuario: «depende del cliente»). Si MSC no es ni será DPO del cliente, puede redactar y ejecutar. Si es DPO designado o por designar, no redacta ni implementa: lo hace el implementador y MSC revisa y verifica.
4. **Modalidad subcontratada** (decisión del usuario: ofrecer ambas en la proforma). Se permite, pero la herramienta 02 advierte el conflicto potencial y exige declaración del art. 17, personas distintas y, de preferencia, consulta a la SPDP (RGLOPDP art. 53).
5. **Herramientas 04, 06 y 07 con dos modos** (decisión del usuario). *Elaboración*: la completa el responsable o su implementador y responde las observaciones. *Revisión del DPO*: el DPO registra observaciones no vinculantes por pestaña, con prioridad, estado y respuesta, y una conclusión. Las observaciones se anexan al informe de la herramienta y tienen su propio informe con firma.
6. **Supervisión siempre del DPO.** Nuevos servicios S29 (revisión del DPO a una evaluación elaborada por el responsable) y S30 (verificación de la implementación).

## Dónde se aplica

| Componente | Cambio |
|---|---|
| `scripts/catalogo_config.py` | `LINEAS`, `ROLES_MSC`, `IMPLEMENTACION`; fases reagrupadas por línea; S05 a S07, S09 a S15 y S23 pasan a «Implementación»; S29 y S30 nuevos |
| Herramienta 01 | Catálogo dividido en dos líneas, «Quién ejecuta» en cada servicio, tarjeta de modalidades |
| Herramienta 02 | Rol de MSC e implementador en la proforma; la implementación solo suma si la factura MSC; advertencias; paquetes sin implementación |
| Herramientas 04, 06 y 07 | Panel «Elaboración / Revisión del DPO» (`scripts/revision_dpo.js`, insertado por `scripts/barra_contexto.py`) |
| App | Ficha del cliente con rol de MSC, implementación a cargo de y nombre del implementador; el modo de 04, 06 y 07 se preselecciona según el rol; tema «Evaluación frente a implementación» en Responsabilidades DPO |
| Guía | Capítulo 3.2, ruta de trabajo y tabla de servicios |

## Pendiente

- Consultar a la SPDP si una misma firma puede ser DPD de un cliente y, por medio de personas distintas, prestarle la implementación subcontratada (punto abierto 32).
- Texto de declaración de la relación con el implementador aliado para el kit 08.
