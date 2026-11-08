# 02 · Calculadora de honorarios del DPD

## Propósito

Estimar los honorarios del Delegado de Protección de Datos para una empresa en Ecuador en tres fases (evaluación inicial, adecuación y control mensual), comparar tres métodos de cálculo, decidir un precio defendible y emitir una proforma de servicios con IVA, argumentos de valor y firma.

## A quién va dirigida

Al consultor o DPD externo que prepara una oferta. No se entrega al cliente: al cliente se entrega la **proforma**.

## Contenido

| Archivo | Uso |
|---|---|
| `calculadora-honorarios.html` | Página web con seis pestañas: cliente, volumen de negocio, volumen de tratamiento, estimación técnica, comparar y decidir, proforma |
| `metodologia-honorarios.md` | Fórmulas, tablas, parámetros y referencias de mercado (generado desde la configuración) |
| `proforma-servicios.md` | Plantilla de proforma para Word, con firma de elaborado y aceptación del cliente |
| `docx/` | Versiones Word |

Fuente única: `scripts/honorarios_config.py`. Los servicios de la proforma (códigos S01 a S28) vienen del catálogo `scripts/catalogo_config.py` (herramienta 01); la proforma permite importar los códigos seleccionados allí. Regenerar con `python scripts/generar_calculadora_honorarios.py`.

## Base legal y técnica

| Elemento | Fuente | Naturaleza |
|---|---|---|
| Tamaño de la empresa (ventas y trabajadores; prevalecen las ventas) | Reglamento del COPCI art. 106; COPCI art. 53 | Norma |
| Puntaje de volumen de tratamiento y gran escala | Res. SPDP-SPD-2026-0005-R, arts. 8 a 14 (MTGE) | Norma |
| IVA 15 % | LRTI art. 65; Circular SRI NAC-DGECCGC25-00000006 | Norma |
| Retención de renta 10 % (persona natural) | Res. SRI NAC-DGERCGC26-00000009 | Norma |
| Costo de un DPD interno | Código del Trabajo arts. 111, 113 y 196; aporte patronal al IESS | Norma |
| Tramos por volumen de negocio, tarifario por puntaje, tarifas por hora, horas por tarea, pisos, paquetes y precios de servicios | Macías Sánchez Consultores | **Criterio propio** |

Todas las citas constan en `BASE-LEGAL.md`.

## Instrucciones

1. **Cliente**: ventas del ejercicio anterior sin IVA, trabajadores, sector y perfil del tratamiento (actividades y encargados del RAT, si existe).
2. **Volumen de negocio**: revise el honorario por tramos. Es la mirada de la capacidad de pago del cliente.
3. **Volumen de tratamiento**: puntúe el tratamiento principal con el MTGE y marque los supuestos de calificación directa. Indica además si el DPD es obligatorio por gran escala.
4. **Estimación técnica**: elija su perfil y tarifa; ajuste las horas por tarea si conoce mejor el caso. Es su piso.
5. **Comparar y decidir**: lea la mediana, el rango y las advertencias; elija el método base para la proforma. Revise los paquetes, la bolsa de horas, la comparación con un DPD interno y lo que recibirá neto de retenciones.
6. **Proforma**: marque servicios, ajuste valores, agregue la multa estimada de la herramienta 03 para el argumento de inversión, complete condiciones y firma, y copie a Word o Excel.

## Limitaciones

- No existe tabla oficial ni gremial de honorarios del DPD en Ecuador: los valores sugeridos son referenciales y deben ajustarse a la ciudad, la experiencia y el mercado.
- Las referencias de mercado son ofertas comerciales públicas, no estudios de precios.
- El IVA, el SBU y los porcentajes de retención cambian por decreto o resolución: verifíquelos cada año en `ECON`.
- La comparación con un DPD interno contrasta un cargo a tiempo completo con la dedicación estimada; la proforma la presenta así para no inducir a error.
- La multa estimada proviene de la herramienta 03 y es orientativa.
