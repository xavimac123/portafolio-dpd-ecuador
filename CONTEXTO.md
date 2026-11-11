# ARCHIVO MAESTRO DE CONTEXTO · MSC Protección de Datos (MSC PD)

Actualizado: 2026-11-11 (segunda entrega). Leer junto con `CLAUDE.md` (reglas) y `BASE-LEGAL.md` (normas).

## 1. Identidad y propósito
- **Qué es:** app instalable (PWA) para gestionar clientes y cumplimiento LOPDP (Ecuador) con las nueve herramientas del portafolio de Macías Sánchez Consultores.
- **Usuario:** Abg. Mariano X. Macías Sánchez, consultor en protección de datos personales (Guayaquil).
- **Stack:** HTML, CSS y JavaScript sin frameworks, en un solo archivo; compilación con Python. Sin dependencias externas por CDN.
- **Publicación actual:** GitHub Pages, rama `gh-pages` › `https://xavimac123.github.io/portafolio-dpd-ecuador/`. Destino previsto: Cloudflare Pages con Cloudflare Access.
- **Reglas clave:** nunca datos reales de clientes ni de titulares; toda cita legal consta en `BASE-LEGAL.md`; escalas propias rotuladas «criterio propio»; firma «Consultor en Protección de Datos Personales» (no «DPD» hasta el registro ante la SPDP); el DPD asesora y supervisa, no implementa; terminología LOPDP; dinero como «USD $ 1.234,56»; exportaciones con 6 cm para firma y sello.

## 2. Estado arquitectónico
- `app-pd/fuente/index.html`: toda la app. Pestañas: Inicio, Clientes, Herramientas, Agenda, Referencia, Ajustes.
- `app-pd/build_pwa.py`: incrusta las nueve herramientas, `scripts/exportar.js`, la Referencia (`scripts/referencia_config.py`, tablas de `docs/contraste-guias-spdp.md` y puntos abiertos de `BASE-LEGAL.md`) y copia los PDF de `app-pd/normas/`. Genera `app-pd/docs/` y `app-pd/dist/preview.html`.
- `scripts/exportar.js` (MSCDoc): Word .docx real y PDF por impresión, con espacio para firma y sello. `scripts/barra_contexto.py` lo agrega a las nueve herramientas (botones «Word (.docx)» y «PDF» junto a cada «Copiar … (Word)»).
- `scripts/*_config.py`: fuente única de cada herramienta; `scripts/generar_*.py` generan las páginas.
- Datos: registro cifrado (AES-GCM 256, PBKDF2-SHA256) en el dispositivo; copia cifrada en Google Drive (`mscpd-…`); plazos en Google Calendar. **No renombrar** el prefijo `mscpd-`, las claves `mscpd:` ni el cliente OAuth.
- Plazos que calcula la app: vulneración 5 días hábiles (SPDP, regulador y CSIRT), 2 del encargado y 3 a titulares (LOPDP arts. 43 y 46); derechos 15 días calendario (arts. 13 a 16).

## 3. Hecho el 2026-11-10/11 (rama `claude/correcciones-referencia-exportacion`)
- «Volver» de las herramientas: cierre directo e iframe nuevo por apertura; desde Inicio se elige el cliente en un selector y se regresa a Inicio.
- Exportación a Word y PDF en la app y en las herramientas; firma con 6 cm; formato «USD $».
- Evidencias: lista por herramienta, casilla «verificado» y anexo en el informe mensual.
- Pestaña Referencia: plazos clave, 14 normas con puntos de consulta, contraste con guías, puntos abiertos, PDF de LOPDP y RGLOPDP.
- Normas: herramienta 06 alineada con la Res. 0041 (arts. 10 a 18 y Anexo 1); 09 y reloj con el art. 43 reformado y el art. 46; 03 con los numerales del art. 68; ayudas ampliadas en 04, 05 y 07.
- Aviso «Todos los derechos reservados» y `LICENSE`.
- Auditoría automatizada de funciones y botones: sin errores.

## 3b. Segunda entrega (2026-11-11)
- Calculadora de plazos de notificación por caso (Herramientas › Consulta rápida y en Inicio).
- Glosario: términos legales, 15 normas ISO y 5 métodos de medición de riesgos con gráfico (Delphi, frecuentista, bayesiano, Monte Carlo y matriz).
- Inicio: búsqueda de clientes, accesos rápidos, «Continuar donde lo dejó», primeros pasos.
- Herramienta 03: evidencia de respaldo por pregunta (presentada, solicitada, no existe; descripción y verificación), en el informe y en una solicitud de evidencias.
- Firma: Consultor o Delegado con registro SPDP; se propaga a las herramientas.
- Normas: biométricos (Res. 2026-0039, por resúmenes) e IA (Res. 2026-0009, texto leído; reforma 0037 por resumen) en la 07, la 05, Referencia, contraste y BASE-LEGAL. Tensión abierta: biometría y gran escala (punto 28).
- Publicado en `main` y `gh-pages` compilado con `MSC_PUBLICO=1` (sin los PDF de LEXIS).

## 4. Pendiente (orden de prioridad)
2. PDF de la ley y el reglamento: son copias LEXIS; no se versionan mientras el repositorio sea público. Publicarlos al pasar a Cloudflare con Access.
3. Contrastar los textos aportados al proyecto y aún no leídos: Res. 0028 (DPD), programa profesionalizante, guía v2 de riesgos; y los textos oficiales de las Res. 2026-0039 y 0037 (puntos 8, 20, 25, 28 y 29 de `BASE-LEGAL.md`).
3b. Evidencia de respaldo también en 06 y 07; cláusula de IA en el contrato de encargo; campo de alternativa no biométrica en la 07.
4. Traslado a Cloudflare Pages con Access; volver privado el repositorio. Los datos no migran solos: restaurar desde Drive.
5. Cambio de nombre y marca (propuesta «Sentinel Data Protection»): solo tras la búsqueda fonética en SENADI; cambiar lo visible, no los identificadores internos. Hacerlo junto con el punto 4.
6. Plataforma con usuarios para vender accesos (especificación pendiente).
7. RAT: lista desplegable de excepciones del art. 26 y columna de puntaje MTGE por actividad.

## 5. Flujo de trabajo
Editar fuente › `python scripts/generar_*.py` › `python scripts/barra_contexto.py` › `python app-pd/build_pwa.py` › probar en 390 px y 1200 px (claro y oscuro) › commit en español › copiar `app-pd/docs/` a `gh-pages`.
