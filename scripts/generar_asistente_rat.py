"""Construye 01-registro-tratamientos/asistente-rat.html desde rat_config.py.

Uso: python scripts/generar_asistente_rat.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import rat_config as C  # noqa: E402

EJEMPLO = [
    {"actividad": "Atención de salud / historias clínicas", "area": "Dirección médica",
     "finalidad": "Ejecutar el contrato o prestar el servicio", "titulares": "Pacientes",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Salud; Niñas, niños y adolescentes",
     "especial": "Sí", "nna": "Sí", "origen": "Del propio titular", "base": "Ejecución de contrato o medidas precontractuales",
     "il": "", "dest": "Laboratorios dentales", "enc": "Proveedor de nube u hosting", "perfiles": "No", "transf": "Sí",
     "tgar": "Estados Unidos — Cláusulas contractuales con el receptor", "plazo": "Según normativa sanitaria (indicar norma)",
     "medidas": "Perfiles de acceso por rol; Cifrado de información; Bitácora de accesos", "rev": "2026-11-01"},
    {"actividad": "Videovigilancia", "area": "Seguridad física", "finalidad": "Seguridad de personas e instalaciones",
     "titulares": "Visitantes; Trabajadores", "datos": "Imagen o video", "especial": "No", "nna": "No",
     "origen": "Captación automática (cámaras, sitio web)", "base": "Interés legítimo", "il": "",
     "dest": "Autoridades judiciales o policiales (por requerimiento)", "enc": "Empresa de seguridad", "perfiles": "No",
     "transf": "No", "tgar": "", "plazo": "30 días salvo incidente", "medidas": "", "rev": "2026-11-01"},
    {"actividad": "Gestión de nómina y personal", "area": "Talento Humano",
     "finalidad": "Cumplir obligaciones laborales y de seguridad social; Cumplir obligaciones tributarias",
     "titulares": "Trabajadores; Cargas familiares de trabajadores",
     "datos": "Identificación (nombre, cédula); Financieros y bancarios; Laborales (cargo, remuneración); Niñas, niños y adolescentes",
     "especial": "Sí", "nna": "Sí", "origen": "Del propio titular", "base": "Obligación legal", "il": "",
     "dest": "IESS; SRI; Ministerio del Trabajo; Entidades bancarias", "enc": "Contador o estudio contable externo",
     "perfiles": "No", "transf": "No", "tgar": "", "plazo": "Plazo del Código del Trabajo y normativa IESS: [indicar]",
     "medidas": "Perfiles de acceso por rol; Respaldos periódicos; Acuerdos de confidencialidad con el personal",
     "rev": "2026-11-01"},
]

cfg = {
    "listas": C.LISTAS, "bases": C.BASES, "preguntas": C.PREGUNTAS, "grupos": C.GRUPOS, "ejemplo": EJEMPLO,
}
shell = (ROOT / "scripts" / "plantilla-asistente-rat.html").read_text(encoding="utf-8")
out = ROOT / "01-registro-tratamientos" / "asistente-rat.html"
out.write_text(shell.replace("/*__CONFIG__*/", json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("OK", out)
