# MSC Protección de Datos (app PD)

App web instalable (PWA) que reúne las nueve herramientas del portafolio en un registro por cliente, con agenda de cumplimiento, cifrado y sincronización con Google. Funciona sin internet después de abrirla una vez. Ícono: isotipo MSC con las siglas **PD**, para distinguirla de MSC Gestor Legal.

**Dirección prevista:** `https://xavimac123.github.io/msc-protecciondatos/` (repositorio público que solo contiene la carpeta `docs/` compilada).

## Qué incluye

- **Inicio:** vencidos, próximos 7 días, clientes activos, solicitudes abiertas y accesos rápidos (cliente nuevo, vulneración, solicitud de derechos, diagnóstico).
- **Clientes:** ficha de la empresa (razón social, RUC, tamaño, sector, contacto, modalidad, servicios del catálogo S01 a S28), expediente con las nueve herramientas, plazos, solicitudes de derechos y resumen para Word. Solo datos de la empresa: **nunca datos de los titulares**.
- **Herramientas:** cada herramienta se abre dentro de la app y guarda su avance en el expediente del cliente elegido, o en «modo libre».
- **Agenda:** plazos de todos los clientes (control mensual, revisiones anuales, vulneraciones, entregas, reuniones), «Agendar ciclo anual» y solicitudes de derechos con código.
- **Semáforo de cumplimiento** por cliente (lista, ficha e inicio). Rojo: plazos vencidos o vulneración abierta. Amarillo: plazos en 7 días, herramientas 03, 04 y 05 sin aplicar o con más de 12 meses (06 y 07 si tienen más de 12 meses) o sin control mensual agendado. Reglas de **criterio propio**.
- **Reloj de vulneraciones:** registra la fecha y hora de constancia, el rol del cliente (responsable o encargado) y agenda solos los plazos: encargado al responsable en 2 días y SPDP en 5 días hábiles (excluye fines de semana y feriados nacionales 2026-2027). El plazo a titulares solo se agenda si el consultor lo configura (punto abierto). Cuenta regresiva en inicio y en la ficha.
- **Evidencias por cliente:** archivos de hasta 8 MB cifrados en el equipo y en Google Drive (`mscpd-doc-…`), con la herramienta y la fecha a la que corresponden.
- **Bitácora de horas y actividades:** horas del mes, valor efectivo por hora frente al honorario mensual y aviso si se superan las horas que cubre el valor hora objetivo.
- **Informe mensual:** borrador para Word con estado (semáforo), actividades, herramientas actualizadas, plazos, solicitudes, vulneraciones, evidencias, próximos pasos, observaciones y firma.
- **Revisión automática:** al actualizar las herramientas 03 a 07 de un cliente, propone agendar su revisión a 12 meses.
- **Proforma en Gestor Legal:** envía los servicios S01 a S28 de la ficha a la proforma de MSC Gestor Legal (misma dirección web; clave `msc:pd-handoff`, vigente 7 días).
- **Barra de contexto:** al desplazarse, la app y cada herramienta muestran dónde está el usuario (pestaña › sección); dentro de la app, en la barra superior de la herramienta.
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

Para publicar, copiar el contenido de `app-pd/docs/` al repositorio `msc-protecciondatos` (rama `main`, carpeta `/docs`) y activar GitHub Pages.

## Limitaciones

- Los datos viven en cada dispositivo y se igualan mediante Google Drive; no hay usuarios múltiples. Es la base de la futura plataforma con usuario y contraseña, no esa plataforma.
- La vista previa (`dist/preview.html`) no conecta con Google: el origen no está autorizado.
- El repositorio público expone el contenido de las herramientas (no datos). Definir la licencia (`docs/decision-licencia.md`) antes de difundir el enlace.
