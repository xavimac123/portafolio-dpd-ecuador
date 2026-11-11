# 06 · Evaluación de ponderación del interés legítimo

## Propósito

Determinar si un tratamiento puede basarse en el interés legítimo y documentar la **evaluación de ponderación previa, motivada y documentada** que exige la Res. SPDP-SPD-2025-0041-R, con los criterios mínimos de su Anexo 1.

## A quién va dirigida

Al DPD o consultor que asesora a un responsable del **sector privado** que usa, o quiere usar, el interés legítimo como base: mercadotecnia directa a clientes, prevención de fraude o lavado de activos, comunicación dentro de un grupo empresarial, seguridad de redes y videovigilancia de seguridad.

## Archivos

| Archivo | Uso |
|---|---|
| `asistente-interes-legitimo.html` | Asistente web en 5 pasos: ¿puede invocarse? (ámbito, supuesto admisible, prohibiciones), el interés y sus características, necesidad, ponderación con salvaguardas, resultado y registro. Copia el informe para Word y la fila del registro para Excel. Ejemplo ficticio: correos de ofertas a clientes actuales. |
| `informe-ponderacion.md` | Plantilla del informe para completar a mano (se genera desde la configuración). |
| `docx/` | Versión Word con firma de responsabilidad. |
| `../scripts/interes_config.py` | **Fuente única**: supuestos, condiciones, prohibiciones, características, criterios de necesidad, factores de ponderación, salvaguardas y resultados. |

Regenerar: `python scripts/generar_interes_legitimo.py`.

## Base legal

- LOPDP art. 7: el interés legítimo como base de legitimación.
- RGLOPDP art. 38 num. 7: la base debe constar en el RAT.
- Res. SPDP-SPD-2025-0041-R: solo sector privado; características del interés (art. 4: lícito, real y concreto, proporcional, coherente con las expectativas razonables); evaluación de ponderación previa, motivada, documentada y disponible para la SPDP y los titulares (su omisión es infracción grave); registro actualizado con revisión al menos anual; supuestos admisibles y prohibiciones; derechos de acceso y oposición; Anexo 1 (criterios mínimos).

Estado de verificación: `BASE-LEGAL.md` (puntos abiertos 19 y 22).

## Elaboración y revisión del DPO

La herramienta tiene dos modos (panel bajo las pestañas). **Elaboración:** la completa el responsable o el implementador que eligió (MSC solo si no es DPO de ese cliente) y responde las observaciones. **Revisión del DPO:** el DPO registra observaciones no vinculantes por pestaña, con prioridad, y una conclusión; no corrige ni ejecuta la evaluación (Res. SPDP-SPD-2025-0028-R arts. 13, 15.2 y 15.3). Las observaciones se anexan al informe y tienen su propio informe con firma («Copiar observaciones del DPO»). En la app, el modo se preselecciona según el rol de MSC registrado en la ficha del cliente. Ver `docs/decision-evaluacion-implementacion.md`.

## Instrucciones

1. Confirme en el RAT que la actividad usa el interés legítimo como base.
2. **Paso 1.** Si la herramienta dice «no puede invocarse», deténgase: busque otra base o rediseñe el tratamiento.
3. **Pasos 2 y 3.** Escriba el interés en términos concretos y justifique cada característica y criterio de necesidad con evidencia.
4. **Paso 4.** Valore los factores y marque solo las salvaguardas que se implementarán antes de iniciar. Escriba la motivación con sus palabras.
5. **Paso 5.** Elija el resultado (la herramienta sugiere uno), verifique la política de privacidad y el canal de oposición, y fije la revisión anual.
6. Copie el informe a Word, fírmelo y archívelo; copie la fila al registro de evaluaciones y anote el código en el RAT.

## Decisiones de diseño

- **Lo que viene de la norma:** supuestos, condiciones, prohibiciones, características, necesidad, registro y revisión anual.
- **Criterio propio** (rotulado así en la interfaz y el informe): los puntajes de 0 a 2 de los factores de ponderación, la normalización a 10, la reducción de 0,5 puntos por salvaguarda (máximo 3) y la regla del resultado sugerido (diferencia de 2 puntos o más: prevalece; entre −1 y 2, o con criterios «Parcial»: prevalece con salvaguardas; menos de −1: no prevalece). Cualquier característica o criterio de necesidad «No cumple» impide que prevalezca.
- El consultor recomienda; la decisión y la implementación de las salvaguardas son del responsable.

## Limitaciones

- No se pudo leer el texto oficial completo: los supuestos y prohibiciones se tomaron de resúmenes profesionales y de extractos del texto. Confirmar los números de artículo y si existe una evaluación simplificada para riesgo medio.
- La señalética en videovigilancia proviene del deber de información general, no de la resolución.
- Los datos del asistente se guardan solo en el navegador. No ingresar datos reales de personas.
