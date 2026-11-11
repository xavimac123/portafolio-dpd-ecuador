# ARCHIVO MAESTRO DE CONTEXTO · MSC Protección de Datos (MSC PD)

Actualizado: 2026-11-10. Leer junto con `CLAUDE.md` (reglas) y `BASE-LEGAL.md` (normas).

## 1. Identidad y propósito
- **Qué es:** app instalable (PWA) para gestionar clientes y cumplimiento LOPDP (Ecuador) con las nueve herramientas del portafolio de Macías Sánchez Consultores.
- **Usuario:** Abg. Mariano X. Macías Sánchez, consultor en protección de datos personales (Guayaquil).
- **Stack:** HTML, CSS y JavaScript sin frameworks, en un solo archivo; compilación con Python. Sin dependencias externas por CDN.
- **Publicación actual:** GitHub Pages, rama `gh-pages` › `https://xavimac123.github.io/portafolio-dpd-ecuador/`. Destino previsto: Cloudflare Pages con Cloudflare Access.
- **Reglas clave:** nunca datos reales de clientes ni de titulares; toda cita legal consta en `BASE-LEGAL.md`; escalas propias rotuladas «criterio propio»; firma «Consultor en Protección de Datos Personales» (no «DPD» hasta el registro ante la SPDP); el DPD asesora y supervisa, no implementa; terminología LOPDP (titular, responsable, encargado, vulneración).

## 2. Estado arquitectónico
- `app-pd/fuente/index.html`: toda la app (interfaz, cifrado, clientes, agenda, sincronización).
- `app-pd/build_pwa.py`: incrusta las nueve herramientas y genera `app-pd/docs/` (lo que se publica) y `app-pd/dist/preview.html`.
- `scripts/*_config.py`: fuente única del contenido de cada herramienta; `scripts/generar_*.py` generan las páginas de las carpetas 01 a 09; `scripts/barra_contexto.py` agrega la barra de contexto.
- Herramientas: 01 catálogo, 02 honorarios, 03 madurez, 04 RAT, 05 gran escala, 06 interés legítimo, 07 evaluación de impacto, 08 plantillas, 09 vulneraciones. Se abren dentro de la app y guardan por cliente.
- Datos: registro cifrado (AES-GCM 256, PBKDF2-SHA256) en el dispositivo; copia cifrada en la carpeta oculta de Google Drive (`mscpd-…`); plazos en Google Calendar. Mismo cliente OAuth que MSC Gestor Legal.
- Funciones probadas: clientes y expediente, agenda, solicitudes de derechos, semáforo de cumplimiento, reloj de vulneraciones, evidencias cifradas, bitácora de horas, informe mensual, revisiones a 12 meses, envío de servicios S01 a S28 a la proforma de Gestor Legal (`#prf&pd=…`), barra de contexto.

## 3. Bugs y bloqueos activos
- Al abrir una herramienta desde Inicio no se puede volver (sin reproducir aún).
- Los informes solo se copian al portapapeles; no exportan a Word ni PDF; la firma no deja espacio para firma y sello.
- Falta revisar todos los botones.
- Repositorio público y sin licencia: contenido y tarifas a la vista.
- Los datos no migran solos al cambiar de dirección web (restaurar desde Drive).
- Normativa: puntos abiertos en `BASE-LEGAL.md` y `docs/recursos-pendientes.md` (plazo a titulares, texto íntegro de la Res. 0041, anexo de la Guía v2, número de la resolución de la Guía v2).

## 4. Backlog (orden de prioridad)
1. Corregir el botón de volver desde Inicio.
2. Exportar informes a Word y PDF, con espacio de 3 a 4 dedos para firma y sello.
3. Formato «USD $» con centavos en todos los valores.
4. Evidencias: lista de documentos por herramienta, casilla «verificado» y anexos del informe.
5. Sección «Normativa»: resoluciones de la SPDP por prioridad, ley y sitio de la SPDP.
6. Mostrar en la app el contraste con los resúmenes JSON de normas.
7. Aviso «Todos los derechos reservados» y archivo LICENSE.
8. Traslado a Cloudflare Pages con Access; volver privado el repositorio.
9. Plataforma con usuarios para vender accesos (especificación pendiente).

## 5. Flujo de trabajo
Editar fuente › `python scripts/generar_*.py` › `python scripts/barra_contexto.py` › `python app-pd/build_pwa.py` › probar en 390 px y 1200 px (claro y oscuro) › commit en español en `main` › copiar `app-pd/docs/` a `gh-pages`.
