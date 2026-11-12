# MSC Protección de Datos (app PD)

App web instalable (PWA) que reúne las nueve herramientas del portafolio en un registro por cliente, con agenda de cumplimiento, cifrado y sincronización con Google. Funciona sin internet después de abrirla una vez. Ícono: isotipo MSC con las siglas **PD**, para distinguirla de MSC Gestor Legal.

**Dirección:** `https://xavimac123.github.io/portafolio-dpd-ecuador/` (rama `gh-pages` de este repositorio, que solo contiene la app compilada).

## Qué incluye

- **Inicio:** vencidos, próximos 7 días, clientes activos, solicitudes abiertas y accesos rápidos (cliente nuevo, vulneración, solicitud de derechos, diagnóstico).
- **Clientes:** ficha de la empresa (razón social, RUC, tamaño, sector, contacto, modalidad, rol de MSC e implementador, servicios del catálogo S01 a S30), expediente con las nueve herramientas, plazos, solicitudes de derechos y resumen para Word. Solo datos de la empresa: **nunca datos de los titulares**.
- **Herramientas:** cada herramienta se abre dentro de la app y guarda su avance en el expediente del cliente elegido, o en «modo libre».
- **Agenda:** plazos de todos los clientes (control mensual, revisiones anuales, vulneraciones, entregas, reuniones), «Agendar ciclo anual» y solicitudes de derechos con código.
- **Semáforo de cumplimiento** por cliente (lista, ficha e inicio). Rojo: plazos vencidos o vulneración abierta. Amarillo: plazos en 7 días, herramientas 03, 04 y 05 sin aplicar o con más de 12 meses (06 y 07 si tienen más de 12 meses) o sin control mensual agendado. Reglas de **criterio propio**.
- **Reloj de vulneraciones:** registra la fecha y hora de constancia, el rol del cliente (responsable o encargado) y agenda solos los plazos: encargado al responsable en 2 días y SPDP en 5 días hábiles (excluye fines de semana y feriados nacionales 2026-2027). Titulares: término de 3 días (LOPDP art. 46), configurable en Ajustes. Cuenta regresiva en inicio y en la ficha.
- **Evidencias por cliente:** archivos de hasta 8 MB cifrados en el equipo y en Google Drive (`mscpd-doc-…`), con la herramienta y la fecha a la que corresponden.
- **Bitácora de horas y actividades:** horas del mes, valor efectivo por hora frente al honorario mensual y aviso si se superan las horas que cubre el valor hora objetivo.
- **Informe mensual:** borrador para Word con estado (semáforo), actividades, herramientas actualizadas, plazos, solicitudes, vulneraciones, evidencias, próximos pasos, observaciones y firma.
- **Revisión automática:** al actualizar las herramientas 03 a 07 de un cliente, propone agendar su revisión a 12 meses.
- **Proforma en Gestor Legal:** envía los servicios S01 a S30 de la ficha a la proforma de MSC Gestor Legal (misma dirección web; clave `msc:pd-handoff`, vigente 7 días).
- **Barra de contexto:** al desplazarse, la app y cada herramienta muestran dónde está el usuario (pestaña › sección); dentro de la app, en la barra superior de la herramienta.
- **Inicio:** búsqueda de clientes, accesos rápidos («¿Qué necesita hacer?»), «Continuar donde lo dejó» y lista de primeros pasos.
- **Calculadora de plazos de notificación:** por caso (rol, sector, constancia, comunicación del encargado, riesgo para titulares, excepciones del art. 46, feriados locales); exporta a Word o PDF y agenda la vulneración en el cliente.
- **Glosario:** términos de la LOPDP y de la normativa, normas ISO de protección de datos y ciberseguridad, y métodos de medición de riesgos con ejemplo y gráfico (`scripts/glosario_config.py`).
- **Herramientas organizadas en bloques** separados por una línea: (1) diagnóstico y evaluación, que realiza el DPD: 03, informe del art. 12, 05, 06 y 07; (2) implementación y cumplimiento, que ejecuta la empresa y verifica el DPD: plan de implementación, 04, 08 y 09; (3) gestión del consultor: 01 y 02; y consulta y cálculo. Cada herramienta se clasifica por tamaño de empresa (esencial, recomendada o según el caso) y las de implementación indican el departamento responsable sugerido. Clasificación y departamentos: criterio propio (`scripts/cumplimiento_config.py`).
- **Informe del deber de información (art. 12):** evalúa los 17 elementos y las condiciones del art. 12 (cumple, parcial, no cumple, no aplica; dónde consta; observación) y genera el informe detallado de lo que la empresa tiene y de lo que debe corregir.
- **Plan de implementación y verificación:** 14 acciones con base legal (LOPDP art. 47 y normas relacionadas), entregable, departamento responsable según el tamaño, fecha compromiso, estado y casilla «Verificado por el DPD» con la evidencia revisada. Exporta el plan con la constancia de verificación (no certifica el cumplimiento integral).
- **Calculadora de riesgos:** frecuentista (bitácora), Delphi (panel por rondas), bayesiano (referencia del sector actualizada) y Monte Carlo (pérdida esperada y ROSI). Sugiere la probabilidad en la escala de la herramienta 07 y redacta la justificación. Umbrales de consenso y pesos: criterio propio. Las herramientas 07 y 09 sugieren qué método usar según el caso.
- **Datos para las herramientas:** al abrir una herramienta se elige cliente registrado (toma los datos de su ficha y guarda en su expediente), cliente nuevo (consulta, sin expediente) o modo práctica (empresa ficticia generada por tipo: microempresa de comercio, salud, cooperativa, retail, unidad educativa, tecnología, seguridad privada, courier). Solo se rellenan campos vacíos; rellenar no cuenta como «herramienta actualizada».
- **Modo oscuro en las herramientas:** sigue el tema de la app; los colores oscuros se generan al compilar desde el CSS de cada herramienta (`scripts/tema_oscuro.py`).
- **Exportar:** «Vista previa y PDF» muestra el documento en A4 y desde ahí se guarda en PDF (impresión › Guardar como PDF) o en Word. En la PC (Chrome o Edge), Word y Excel abren «Guardar como» para elegir la carpeta; en el celular se descargan. Los botones «Excel» de las herramientas generan un .xlsx real.
- **Herramientas paso a paso:** cada pestaña termina con «Anterior / Siguiente» y, si tiene un resultado arriba, lo repite al pie al terminar de responder. En la 03, el resultado del diagnóstico aparece al pie del cuestionario y la evidencia de respaldo se habilita según el nivel (0: no existe; 1: registro informal; 2: propuesta o informe aprobado; 3 y 4: documento aprobado y aplicación), criterio propio.
- **Firma:** cargo «Consultor» o «Delegado de Protección de Datos Personales» y número de registro ante la SPDP; se propone también dentro de las herramientas.
- **Referencia:** plazos y cifras clave, ley, reglamento y resoluciones de la SPDP con puntos de consulta, estado de verificación de cada fuente, contraste con las guías, puntos abiertos y descarga en PDF de la LOPDP y el RGLOPDP (si están en `app-pd/normas/`). Fuente: `scripts/referencia_config.py`.
- **Exportación:** informes en Word (.docx) y PDF con 6 cm para firma y sello, en la app y dentro de cada herramienta (`scripts/exportar.js`).
- **Evidencias:** lista de documentos sugeridos por herramienta, casilla «verificado» y anexo en el informe mensual.
- **Ajustes:** tema claro u oscuro, Google Drive, Google Calendar, firma del consultor, plazo de respuesta a solicitudes, contraseña, respaldo cifrado e instalación.

## Seguridad

- Registro cifrado con AES-GCM de 256 bits; clave derivada con PBKDF2-SHA256 (310.000 iteraciones). Código de recuperación al crear el registro.
- Google Drive: copia cifrada en la carpeta oculta de la app (`drive.appdata`), una versión diaria (10 días) y una mensual (12 meses). Google no recibe datos sin cifrar.
- Google Calendar (`calendar.events`): plazos con avisos 3 días y 1 día antes.
- Usa el mismo ID de cliente OAuth que MSC Gestor Legal (origen `https://xavimac123.github.io`). Ambas apps comparten la carpeta oculta de Drive, pero sus archivos tienen nombres distintos (`mscpd-…` y `msc-…`) y ninguna borra los de la otra.

## Compilar

```bash
python scripts/generar_*.py              # regenerar las herramientas del portafolio
python scripts/barra_contexto.py         # barra de contexto en las nueve páginas
python app-pd/make_assets.py             # íconos y gráficos embebidos (solo si cambian)
python app-pd/build_pwa.py               # escribe app-pd/docs/ y app-pd/dist/preview.html
```

Para publicar, copiar el contenido de `app-pd/docs/` a la rama `gh-pages` (GitHub Pages: Settings › Pages › rama `gh-pages`, carpeta raíz).

## Limitaciones

- Los datos viven en cada dispositivo y se igualan mediante Google Drive; no hay usuarios múltiples. Es la base de la futura plataforma con usuario y contraseña, no esa plataforma.
- La vista previa (`dist/preview.html`) no conecta con Google: el origen no está autorizado.
- El repositorio público expone el contenido de las herramientas (no datos). Definir la licencia (`docs/decision-licencia.md`) antes de difundir el enlace.

## Inicio, clima y autodiagnóstico

- **Saludo:** «Buenos días / tardes / noches» según la hora, nombre abreviado con título (o el «Nombre para el saludo» de Ajustes) y el cargo con el que firma.
- **Clima:** pronóstico de MET Norway (Locationforecast 2.0, datos CC BY 4.0; uso comercial permitido para sitios de bajo volumen que se identifican por su origen). Se consulta como máximo cada 30 minutos; ubicación predeterminada Guayaquil, o la del dispositivo redondeada a 2 decimales (Ajustes › Apariencia).
- **Autodiagnóstico:** `build_pwa.py` genera `docs/autodiagnostico/` (página puente con `og:image` de la marca que redirige al formulario de Tally). Así el enlace enviado por WhatsApp muestra la vista previa de Macías Sánchez Consultores en lugar de la de Tally. El *service worker* no intercepta esa ruta.
- **Contacto:** el WhatsApp y el correo de atención se guardan una sola vez en Ajustes › Datos del consultor (cifrados) y se usan en publicidad, invitaciones y mensajes. No se escriben en el código porque el repositorio es público.
