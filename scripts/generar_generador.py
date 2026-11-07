"""Construye los generadores web a partir de las plantillas Markdown.

Uso: python scripts/generar_generador.py
Una sola fuente: editar los .md (o el panel extra) y volver a ejecutar este script.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHELL = (ROOT / "scripts" / "plantilla-generador.html").read_text(encoding="utf-8")
MARKED = (ROOT / "scripts" / "vendor" / "marked.min.js").read_text(encoding="utf-8")
SHELL = SHELL.replace("/*__MARKED__*/", MARKED.replace("</script", "<\\/script"))
FIRMA = (ROOT / "scripts" / "firma-responsabilidad.md").read_text(encoding="utf-8")


def js(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


KITS = [
    {
        "out": "02-kit-plantillas/generador-documentos.html",
        "key": "msc-gen-v1",
        "herramienta": "Herramienta 02",
        "titulo": "Generador de documentos de protección de datos",
        "subtitulo": "Política de privacidad, avisos, contrato de encargo y cláusulas de consentimiento · LOPDP Ecuador",
        "extra": "",
        "plantillas": [
            ("Política de privacidad", "02-kit-plantillas/politica-privacidad.md"),
            ("Aviso de privacidad", "02-kit-plantillas/aviso-privacidad.md"),
            ("Contrato de encargo", "02-kit-plantillas/contrato-encargo.md"),
            ("Cláusulas de consentimiento", "02-kit-plantillas/clausulas-consentimiento.md"),
            ("Designación del DPD", "02-kit-plantillas/comunicacion-dpd.md"),
        ],
        "campos": [
            ["RAZÓN SOCIAL", "Razón social"], ["RUC", "RUC"], ["DIRECCIÓN", "Dirección"], ["CIUDAD", "Ciudad"],
            ["CORREO DE ATENCIÓN AL TITULAR", "Correo de atención al titular"], ["TELÉFONO", "Teléfono"], ["URL", "URL de la política"],
            ["NOMBRE DEL REPRESENTANTE LEGAL", "Representante legal"], ["CARGO DEL REPRESENTANTE LEGAL", "Cargo del representante legal"],
            ["NOMBRE DEL DPD", "DPD registrado en la SPDP: nombre"], ["CORREO DEL DPD", "DPD: correo directo"],
            ["FECHA DE DESIGNACIÓN", "DPD: fecha de designación"], ["FECHA DE REGISTRO SPDP", "DPD: fecha de registro en la SPDP"],
            ["REGISTRO SPDP", "DPD: referencia del registro SPDP"],
            ["VERSIÓN", "Versión de la política"], ["FECHA DE VIGENCIA", "Fecha de vigencia"], ["FECHA", "Fecha del documento"],
            ["RAZÓN SOCIAL DEL ENCARGADO", "Encargado: razón social"], ["RUC DEL ENCARGADO", "Encargado: RUC"],
            ["DIRECCIÓN DEL ENCARGADO", "Encargado: dirección"], ["CORREO DEL RESPONSABLE", "Correo del responsable para avisos"],
        ],
        "ejemplo": {
            "RAZÓN SOCIAL": "Ferretería Ficticia El Tornillo S.A.", "RUC": "0999999999001", "DIRECCIÓN": "Av. Ejemplo 123",
            "CIUDAD": "Guayaquil", "CORREO DE ATENCIÓN AL TITULAR": "privacidad@ejemplo.ec", "TELÉFONO": "04 000 0000",
            "NOMBRE DEL REPRESENTANTE LEGAL": "Juan Ejemplo Pérez", "CARGO DEL REPRESENTANTE LEGAL": "Gerente General", "NOMBRE DEL DPD": "Ana Ficticia Torres",
            "FECHA DE DESIGNACIÓN": "3 de noviembre de 2026", "FECHA DE REGISTRO SPDP": "5 de noviembre de 2026",
            "REGISTRO SPDP": "[EJEMPLO-0001]", "URL": "https://ejemplo.ec/privacidad", "VERSIÓN": "1.0", "FECHA DE VIGENCIA": "1 de diciembre de 2026",
            "FECHA": "7 de noviembre de 2026", "RAZÓN SOCIAL DEL ENCARGADO": "Nube Ficticia Cía. Ltda.",
            "RUC DEL ENCARGADO": "0988888888001", "DIRECCIÓN DEL ENCARGADO": "Calle Ficticia 456, Quito",
            "CORREO DEL RESPONSABLE": "privacidad@ejemplo.ec",
        },
    },
    {
        "out": "03-kit-vulneraciones/asistente-vulneraciones.html",
        "key": "msc-vul-v1",
        "herramienta": "Herramienta 03",
        "titulo": "Asistente de respuesta a vulneraciones",
        "subtitulo": "Plazos, evaluación de riesgo y modelos de comunicación · LOPDP Ecuador",
        "extra": (ROOT / "scripts" / "panel-vulneraciones.html").read_text(encoding="utf-8"),
        "plantillas": [
            ("Protocolo", "03-kit-vulneraciones/protocolo-respuesta.md"),
            ("Bitácora", "03-kit-vulneraciones/bitacora-vulneracion.md"),
            ("Encargado → responsable", "03-kit-vulneraciones/comunicacion-encargado-responsable.md"),
            ("Notificación SPDP", "03-kit-vulneraciones/notificacion-spdp.md"),
            ("Comunicación a titulares", "03-kit-vulneraciones/comunicacion-titulares.md"),
        ],
        "campos": [
            ["RAZÓN SOCIAL", "Razón social del responsable"], ["RUC", "RUC"],
            ["VUL-AAAA-NN", "Código del incidente"], ["FECHA Y HORA", "Fecha y hora de constancia"],
            ["FECHA LÍMITE", "Fecha límite SPDP"], ["CORREO DE ATENCIÓN AL TITULAR", "Correo de atención al titular"],
            ["TELÉFONO", "Teléfono de atención"], ["HORARIO", "Horario de atención"], ["CORREO DEL DPD", "Correo del DPD"],
            ["RAZÓN SOCIAL DEL ENCARGADO", "Encargado (si aplica)"], ["CORREO DEL RESPONSABLE", "Correo del responsable"],
            ["VERSIÓN", "Versión del protocolo"], ["FECHA", "Fecha de aprobación"],
        ],
        "ejemplo": {
            "RAZÓN SOCIAL": "Ferretería Ficticia El Tornillo S.A.", "RUC": "0999999999001", "VUL-AAAA-NN": "VUL-2026-01",
            "CORREO DE ATENCIÓN AL TITULAR": "privacidad@ejemplo.ec", "TELÉFONO": "04 000 0000",
            "HORARIO": "lunes a viernes, 08:00 a 17:00", "RAZÓN SOCIAL DEL ENCARGADO": "Nube Ficticia Cía. Ltda.",
            "CORREO DEL RESPONSABLE": "privacidad@ejemplo.ec", "VERSIÓN": "1.0", "FECHA": "7 de noviembre de 2026",
        },
    },
]

for k in KITS:
    data = [{"nombre": n, "md": (ROOT / p).read_text(encoding="utf-8")} for n, p in k["plantillas"]]
    html = (
        SHELL.replace("/*__TEMPLATES__*/", js(data))
        .replace("/*__FIRMA__*/", js(FIRMA))
        .replace("/*__CAMPOS__*/", js(k["campos"]))
        .replace("/*__EJ__*/", js(k["ejemplo"]))
        .replace("__KEY__", k["key"])
        .replace("__HERRAMIENTA__", k["herramienta"])
        .replace("__TITULO__", k["titulo"])
        .replace("__SUBTITULO__", k["subtitulo"])
        .replace("<!--__EXTRA__-->", k["extra"])
    )
    out = ROOT / k["out"]
    out.write_text(html, encoding="utf-8")
    print("OK", out)
