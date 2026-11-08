"""Fuente única de la Herramienta 06: Evaluación de ponderación del interés legítimo.

Base: LOPDP art. 7 (bases de legitimación); RGLOPDP art. 38 num. 7 (base en el RAT);
Res. SPDP-SPD-2025-0041-R (normativa general para la aplicación del interés legítimo, solo sector privado,
y su Anexo 1: metodología mínima de la evaluación de ponderación).

Lo que viene de la norma: características del interés (art. 4), evaluación previa, motivada, documentada y
disponible; supuestos admisibles y prohibiciones; registro de evaluaciones con revisión al menos anual;
derechos de acceso y oposición. Lo que es CRITERIO PROPIO: los puntajes de la ponderación y el efecto de las
salvaguardas. La herramienta lo rotula así en la interfaz y en el informe.
"""

VERSION = "v0.1"

# ---------- Paso 1. ¿Puede invocarse?
SUPUESTOS = [
    {"id": "mkt", "nombre": "Mercadotecnia directa",
     "cond": ["No se usan datos sensibles ni datos de niñas, niños o adolescentes",
              "Existe un mecanismo gratuito e inmediato para oponerse (darse de baja)"]},
    {"id": "fraude", "nombre": "Prevención y reporte de fraude, lavado de activos y financiamiento del terrorismo",
     "cond": ["Los datos se conservan solo el tiempo estrictamente necesario"]},
    {"id": "grupo", "nombre": "Comunicación interna dentro de un grupo empresarial",
     "cond": ["Se limita a finalidades legítimas", "Es transparente para los titulares (consta en la política y en los avisos)"]},
    {"id": "redes", "nombre": "Seguridad de redes y sistemas de información",
     "cond": ["Existen medidas técnicas y organizativas adecuadas"]},
    {"id": "cctv", "nombre": "Videovigilancia con fines de seguridad de personas, bienes o instalaciones",
     "cond": ["No se capta ni graba audio", "Hay señalética visible en las zonas vigiladas"]},
]
# La última condición del CCTV (señalética) es deber de información general (LOPDP art. 12), no requisito de la RES-0041.

PROHIBICIONES = [
    {"id": "x_esp", "texto": "¿El tratamiento usa datos sensibles o de categorías especiales?",
     "efecto": "reforzado",
     "nota": "Solo se admite si es estrictamente indispensable, con medidas de seguridad reforzadas y una ponderación que garantice plenamente los derechos."},
    {"id": "x_perf", "texto": "¿Hay elaboración de perfiles automatizada con efectos jurídicos o un impacto significativo en las personas?",
     "efecto": "prohibido_salvo",
     "nota": "Prohibido, salvo en los sectores financiero y de seguros con salvaguardas adicionales."},
    {"id": "x_nna", "texto": "¿Se tratan datos de niñas, niños o adolescentes?",
     "efecto": "reforzado",
     "nota": "Solo con justificación expresa en el interés superior del niño, respaldada en la ponderación, con medidas reforzadas."},
    {"id": "x_masivo", "texto": "¿Se tratan datos de forma masiva o se reutilizan para una finalidad distinta o incompatible con la original?",
     "efecto": "prohibido",
     "nota": "No puede invocarse el interés legítimo. Busca otra base o rediseña el tratamiento."},
]

# ---------- Paso 2. Identificación del interés (RES-0041 art. 4: características)
CARACTERISTICAS = [
    {"id": "c_licito", "nombre": "Lícito", "pregunta": "¿La finalidad está permitida por la ley y no persigue un fin prohibido?"},
    {"id": "c_real", "nombre": "Real y concreto", "pregunta": "¿Responde a una necesidad cierta y demostrable, no hipotética ni futura?"},
    {"id": "c_prop", "nombre": "Proporcional", "pregunta": "¿El tratamiento es adecuado, necesario, oportuno y no excesivo?"},
    {"id": "c_expect", "nombre": "Coherente con las expectativas razonables", "pregunta": "¿Se informó al titular antes del tratamiento y consta en la política de privacidad?"},
]
RESP = ["Cumple", "Parcial", "No cumple"]

# ---------- Paso 3. Necesidad
NECESIDAD = [
    {"id": "n_indisp", "texto": "El tratamiento es indispensable para lograr la finalidad."},
    {"id": "n_alt", "texto": "Se analizaron alternativas menos intrusivas y ninguna logra el mismo fin."},
    {"id": "n_min", "texto": "Solo se usan los datos mínimos necesarios (campo por campo)."},
    {"id": "n_plazo", "texto": "El plazo de conservación está definido y es el mínimo necesario."},
]

# ---------- Paso 4. Ponderación (CRITERIO PROPIO: puntajes 0 a 2)
PESO_INTERES = [
    {"id": "w_imp", "nombre": "Importancia del interés", "ops": [["Conveniencia comercial", 0], ["Interés relevante para la operación", 1], ["Interés vinculado a seguridad, fraude o protección de terceros", 2]]},
    {"id": "w_benef", "nombre": "Beneficio para los titulares o la sociedad", "ops": [["Solo beneficia al responsable", 0], ["Beneficio indirecto para los titulares", 1], ["Protege directamente a los titulares o a terceros", 2]]},
    {"id": "w_conexo", "nombre": "Respaldo normativo o sectorial", "ops": [["Ninguno", 0], ["Recomendación o buena práctica sectorial", 1], ["Deber legal conexo o supuesto admisible expreso", 2]]},
]
IMPACTO_TITULAR = [
    {"id": "i_datos", "nombre": "Naturaleza de los datos", "ops": [["Identificación o contacto", 0], ["Datos financieros, de ubicación o de comportamiento", 1], ["Datos sensibles o de categorías especiales", 2]]},
    {"id": "i_expect", "nombre": "Expectativa del titular", "ops": [["Lo espera: hay relación previa y fue informado", 0], ["Podría esperarlo", 1], ["No lo espera o le sorprendería", 2]]},
    {"id": "i_pos", "nombre": "Posición del titular", "ops": [["Igualdad con el responsable", 0], ["Dependencia o subordinación", 1], ["Grupo especialmente vulnerable", 2]]},
    {"id": "i_efecto", "nombre": "Efectos posibles", "ops": [["Molestias menores", 0], ["Pérdida de control o publicidad no deseada", 1], ["Decisiones, exclusión, discriminación o daño económico", 2]]},
    {"id": "i_escala", "nombre": "Escala y duración", "ops": [["Pocos titulares y por poco tiempo", 0], ["Volumen moderado o tratamiento continuo", 1], ["Gran escala o tratamiento permanente", 2]]},
]
SALVAGUARDAS = [
    "Oposición gratuita e inmediata (darse de baja en un paso)", "Información previa específica y visible",
    "Minimización de datos", "Plazo de conservación corto con borrado automático", "Seudonimización o anonimización",
    "Acceso restringido por perfil y registro de accesos", "Sin decisiones automatizadas", "Sin audio (videovigilancia)",
    "Cifrado en reposo y en tránsito", "Revisión periódica de la ponderación",
]
SALV_REDUCE = 0.5   # cada salvaguarda reduce 0,5 puntos el impacto (criterio propio)
SALV_TOPE = 3       # reducción máxima por salvaguardas (criterio propio)

RESULTADOS = [
    "Prevalece el interés legítimo: puede usarse como base",
    "Prevalece solo con las salvaguardas indicadas: aplicarlas antes de iniciar",
    "No prevalece: el interés legítimo no puede ser la base; usar otra base o rediseñar el tratamiento",
]
REVISION_MESES = 12  # revisión al menos anual, o antes si cambian finalidad, datos o riesgo (RES-0041)
