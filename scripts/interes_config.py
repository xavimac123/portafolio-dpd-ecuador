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
    {"id": "mkt", "nombre": "Mercadotecnia directa (art. 11)",
     "cond": ["No se usan datos sensibles ni datos de niñas, niños o adolescentes",
              "Los titulares tienen una relación contractual previa o una expectativa razonable de ser contactados, y fueron informados antes",
              "Cada comunicación ofrece un mecanismo de oposición visible, gratuito y eficaz, que se atiende sin dilación",
              "Si hay perfilado, no produce efectos jurídicos significativos ni afecta gravemente los derechos"]},
    {"id": "fraude", "nombre": "Prevención y reporte de fraude, lavado de activos y financiamiento del terrorismo (art. 12)",
     "cond": ["Solo se tratan los datos estrictamente necesarios para detectar, analizar o reportar operaciones sospechosas",
              "Las listas de bloqueo se conservan solo el tiempo estrictamente necesario"]},
    {"id": "grupo", "nombre": "Comunicación interna dentro de un grupo empresarial (art. 13)",
     "cond": ["El grupo empresarial puede acreditarse (actos societarios, certificados o registros)",
              "Los datos se limitan a gestiones internas legítimas; si salen del país, hay nivel adecuado o garantías",
              "El titular fue informado de finalidades, responsables, medidas y canales de derechos"]},
    {"id": "redes", "nombre": "Seguridad de redes y sistemas de información (art. 14)",
     "cond": ["Existen controles técnicos y organizativos acordes a los riesgos, sustentados en protocolos de ciberseguridad",
              "Se aplica protección de datos desde el diseño y por defecto"]},
    {"id": "cctv", "nombre": "Videovigilancia con fines de seguridad de personas, bienes o instalaciones (art. 15)",
     "cond": ["La finalidad es de seguridad y existe una justificación concreta de necesidad y proporcionalidad",
              "No se capta ni graba audio (prohibido, también para supervisión laboral)",
              "No hay cámaras en zonas íntimas: baños, vestidores, lactarios o comedores",
              "Hay señalética visible en las zonas vigiladas (deber de información, LOPDP art. 12)"]},
]

# Prohibiciones del art. 16. efecto: "prohibido", "prohibido_salvo" o "reforzado".
PROHIBICIONES = [
    {"id": "x_sens", "texto": "¿El tratamiento usa datos sensibles (art. 4 LOPDP: etnia, identidad de género o cultural, religión, ideología, filiación política, pasado judicial, condición migratoria, orientación sexual, salud, biométricos, genéticos)?",
     "efecto": "prohibido",
     "nota": "Art. 16.1: no puede invocarse el interés legítimo para datos sensibles. Busca otra base (por ejemplo, una excepción del art. 26 LOPDP) o retira esos datos del tratamiento."},
    {"id": "x_esp", "texto": "¿Usa otras categorías especiales (art. 25 LOPDP), como datos de personas con discapacidad?",
     "efecto": "reforzado",
     "nota": "Art. 16.2: solo si es estrictamente indispensable, la ponderación garantiza en todo momento los derechos y se aplican medidas reforzadas. El Anexo 1 exige una justificación reforzada por cada categoría."},
    {"id": "x_perf", "texto": "¿Hay elaboración de perfiles automatizada con efectos jurídicos significativos o que afecte gravemente los derechos?",
     "efecto": "prohibido_salvo",
     "nota": "Art. 16.3: prohibido, salvo en los sectores financiero, bancario y de seguros, con medidas reforzadas, transparencia, oposición, revisión humana y supervisión."},
    {"id": "x_nna", "texto": "¿Se tratan datos de niñas, niños o adolescentes?",
     "efecto": "reforzado",
     "nota": "Art. 16.4: solo con justificación expresa en el interés superior del niño, documentada en la evaluación, con medidas reforzadas. En mercadotecnia directa no se admite."},
    {"id": "x_masivo", "texto": "¿Los datos se reutilizan para una finalidad nueva, incompatible con la original?",
     "efecto": "prohibido",
     "nota": "Art. 16.5: no puede invocarse el interés legítimo para una reutilización incompatible con la finalidad original. Busca otra base o rediseña el tratamiento."},
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
    {"id": "n_cons", "texto": "Se describieron las consecuencias previsibles de no realizar el tratamiento (seguridad, cumplimiento u operación)."},
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
    "Revisión humana de las decisiones", "Capacitación del personal que accede a los datos", "Cláusulas de confidencialidad y contrato de encargo con proveedores",
]
SALV_REDUCE = 0.5   # cada salvaguarda reduce 0,5 puntos el impacto (criterio propio)
SALV_TOPE = 3       # reducción máxima por salvaguardas (criterio propio)

RESULTADOS = [
    "Prevalece el interés legítimo: puede usarse como base",
    "Prevalece solo con las salvaguardas indicadas: aplicarlas antes de iniciar",
    "No prevalece: el interés legítimo no puede ser la base; usar otra base o rediseñar el tratamiento",
]
REVISION_MESES = 12  # art. 18: revisión en el plazo de un año; pierde vigencia si cambian finalidad, datos, titulares o riesgos
