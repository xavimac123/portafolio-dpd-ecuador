# MSC Protección de Datos (app PD)

App web instalable (PWA) que reúne las nueve herramientas del portafolio en un registro por cliente, con agenda de cumplimiento, cifrado y sincronización con Google. Funciona sin internet después de abrirla una vez. Ícono: isotipo MSC con las siglas **PD**, para distinguirla de MSC Gestor Legal.

**Dirección prevista:** `https://xavimac123.github.io/msc-protecciondatos/` (repositorio público que solo contiene la carpeta `docs/` compilada).

## Qué incluye

- **Inicio:** vencidos, próximos 7 días, clientes activos, solicitudes abiertas y accesos rápidos (cliente nuevo, vulneración, solicitud de derechos, diagnóstico).
- **Clientes:** ficha de la empresa (razón social, RUC, tamaño, sector, contacto, modalidad, servicios del catálogo S01 a S28), expediente con las nueve herramientas, plazos, solicitudes de derechos y resumen para Word. Solo datos de la empresa: **nunca datos de los titulares**.
- **Herramientas:** cada herramienta se abre dentro de la app y guarda su avance en el expediente del cliente elegido, o en «modo libre».
- **Agenda:** plazos de todos los clientes (control mensual, revisiones anuales, vulneraciones, entregas, reuniones), «Agendar ciclo anual» y solicitudes de derechos con código.
- **Ajustes:** tema claro u oscuro, Google Drive, Google Calendar, firma del consultor, plazo de respuesta a solicitudes, contraseña, respaldo cifrado e instalación.

## Seguridad

- Registro cifrado con AES-GCM de 256 bits; clave derivada con PBKDF2-SHA256 (310.000 iteraciones). Código de recuperación al crear el registro.
- Google Drive: copia cifrada en la carpeta oculta de la app (`drive.appdata`), una versión diaria (10 días) y una mensual (12 meses). Google no recibe datos sin cifrar.
- Google Calendar (`calendar.events`): plazos con avisos 3 días y 1 día antes.
- Usa el mismo ID de cliente OAuth que MSC Gestor Legal (origen `https://xavimac123.github.io`). Ambas apps comparten la carpeta oculta de Drive, pero sus archivos tienen nombres distintos (`mscpd-…` y `msc-…`) y ninguna borra los de la otra.

## Compilar

```bash
python scripts/generar_*.py              # regenerar las herramientas del portafolio
python app-pd/make_assets.py             # íconos y gráficos embebidos (solo si cambian)
python app-pd/build_pwa.py               # escribe app-pd/docs/ y app-pd/dist/preview.html
```

Para publicar, copiar el contenido de `app-pd/docs/` al repositorio `msc-protecciondatos` (rama `main`, carpeta `/docs`) y activar GitHub Pages.

## Limitaciones

- Los datos viven en cada dispositivo y se igualan mediante Google Drive; no hay usuarios múltiples. Es la base de la futura plataforma con usuario y contraseña, no esa plataforma.
- La vista previa (`dist/preview.html`) no conecta con Google: el origen no está autorizado.
- El repositorio público expone el contenido de las herramientas (no datos). Definir la licencia (`docs/decision-licencia.md`) antes de difundir el enlace.
