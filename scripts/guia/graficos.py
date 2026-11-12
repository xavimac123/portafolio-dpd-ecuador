"""Gráficos de la Guía del DPD. Usa los datos de ejemplo de las herramientas (fuente única).

Uso: python scripts/guia/graficos.py  -> docs/guia/img/*.png
"""
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker  # noqa: E402,F401
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import madurez_config as MC  # noqa: E402

OUT = ROOT / "docs" / "guia" / "img"
OUT.mkdir(parents=True, exist_ok=True)
FD = ROOT / "scripts" / "vendor" / "fonts"
for f in FD.glob("*.ttf"):
    font_manager.fontManager.addfont(str(f))
plt.rcParams.update({"font.family": "Archivo", "font.size": 10, "axes.edgecolor": "#B8B19A",
                     "axes.labelcolor": "#14181E", "xtick.color": "#6E6230", "ytick.color": "#6E6230"})

ORO, CAR, MAR, OLI, ORC = "#A09046", "#14181E", "#F7F5EE", "#6E6230", "#C9BC82"
OK, AM, AL, MA = "#4E9A6B", "#D2A93A", "#C8693D", "#9B3434"
DPI = 220


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("OK", name)


def box(ax, x, y, w, h, title, sub="", fc=MAR, ec=ORO, tc=CAR, fs=10.5, fss=8.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h * (0.64 if sub else 0.5), title, ha="center", va="center", fontsize=fs, weight="bold", color=tc)
    if sub:
        ax.text(x + w / 2, y + h * 0.3, sub, ha="center", va="center", fontsize=fss, color=ORC if fc in (CAR, OLI) else OLI, wrap=True)


def arrow(ax, a, b, color=OLI, rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13, color=color, lw=1.4,
                                 connectionstyle=f"arc3,rad={rad}"))


# 1. Flujo de las herramientas
def flujo():
    fig, ax = plt.subplots(figsize=(15, 3.7))
    ax.set_xlim(0, 15); ax.set_ylim(0, 3.7); ax.axis("off")
    pasos = [("01", "Catálogo", "Servicios\ny glosario"), ("02", "Honorarios", "Proforma\nantes de iniciar"), ("03", "Madurez", "Mapeo, diagnóstico\ny plan de acción"),
             ("04", "RAT", "Inventario de\nactividades"), ("05", "Gran escala", "Puntaje MTGE\npor actividad"), ("06", "Interés\nlegítimo", "Ponderación\nprevia"), ("07", "Evaluación\nde impacto", "Actividades de\nalto riesgo"),
             ("08", "Plantillas", "Política, avisos,\ncontratos, DPD"), ("09", "Vulneraciones", "Protocolo y\nrespuesta")]
    w, gap, y = 1.48, 0.18, 1.3
    for i, (n, t, s_) in enumerate(pasos):
        x = 0.08 + i * (w + gap)
        dark = i == 2
        fc = CAR if dark else ("#EFEBDD" if i < 2 else MAR)
        ax.add_patch(FancyBboxPatch((x, y), w, 1.55, boxstyle="round,pad=0.02,rounding_size=0.08", fc=fc, ec=ORO, lw=1.5, ls="--" if i < 2 else "-"))
        ax.text(x + 0.14, y + 1.32, n, fontsize=9, weight="bold", color=ORO)
        ax.text(x + w / 2, y + 0.92, t, ha="center", va="center", fontsize=10.5, weight="bold", color=MAR if dark else CAR)
        ax.text(x + w / 2, y + 0.33, s_, ha="center", va="center", fontsize=7.8, color=ORC if dark else OLI)
        if i < len(pasos) - 1:
            arrow(ax, (x + w + 0.02, y + 0.78), (x + w + gap - 0.02, y + 0.78))
    arrow(ax, (14.2, 1.25), (4.1, 1.25), color=ORO, rad=-0.16)
    ax.text(9.1, 0.12, "Revisión anual: repetir 03 · Madurez y 05 · Gran escala para medir el avance", ha="center", fontsize=9, color=OLI, style="italic")
    save(fig, "flujo_herramientas")


# 2. Ciclo de intervención del DPD
def ciclo():
    fig, ax = plt.subplots(figsize=(6.6, 6.6))
    ax.set_xlim(-1.62, 1.62); ax.set_ylim(-1.62, 1.62); ax.axis("off"); ax.set_aspect("equal")
    fases = [("1", "Diagnóstico", "Madurez"), ("2", "Inventario", "RAT y mapa\nde datos"), ("3", "Riesgos", "Análisis y\nevaluación de impacto"),
             ("4", "Implementación", "Políticas, avisos,\ncontratos"), ("5", "Respuesta", "Vulneraciones\ny derechos"), ("6", "Control", "Indicadores,\nauditoría, mejora")]
    cols = [CAR, OLI, ORO, "#8C7E3E", "#5A4F25", "#3A3F47"]
    for i, (n, t, s) in enumerate(fases):
        a0 = 90 - i * 60
        ax.add_patch(Wedge((0, 0), 1.55, a0 - 58, a0, width=0.62, fc=cols[i], ec="white", lw=3))
        am = math.radians(a0 - 29)
        ax.text(1.24 * math.cos(am), 1.24 * math.sin(am) + 0.06, t, ha="center", va="center", fontsize=9, weight="bold", color="white")
        ax.text(1.24 * math.cos(am), 1.24 * math.sin(am) - 0.12, n, ha="center", va="center", fontsize=8, color=ORC)
        ax.text(0.62 * math.cos(am), 0.62 * math.sin(am), s, ha="center", va="center", fontsize=7.6, color=OLI)
    ax.add_patch(Circle((0, 0), 0.34, fc=MAR, ec=ORO, lw=1.5))
    ax.text(0, 0.05, "Responsabilidad", ha="center", fontsize=8.5, weight="bold", color=CAR)
    ax.text(0, -0.1, "proactiva", ha="center", fontsize=8.5, weight="bold", color=CAR)
    save(fig, "ciclo_dpd")


# 3. Radar del ejemplo de madurez (mismos datos del asistente)
EJ_R = {"gob": [2, 1, 1, 0], "dpd": [3, "na", "na"], "rat": [2, 1, 0], "lic": [2, 2, "na", 1], "tra": [3, 2, 1],
        "der": [2, 1, 1], "enc": [2, 1, 0], "seg": [2, 2, 3, 1], "eipd": [1, "na", 0], "vul": [1, 1, 0, 1],
        "tri": [2, 1], "cul": [1, 3, 0]}


def puntajes():
    res = []
    for d in MC.DOMINIOS:
        v = [x for x in EJ_R[d["id"]] if x != "na"]
        res.append((d, sum(v) / len(v)))
    w = sum(d["peso"] for d, _ in res)
    idx = sum(s * d["peso"] for d, s in res) / w
    return res, idx


def radar():
    res, idx = puntajes()
    N = len(res)
    ang = [2 * math.pi * i / N for i in range(N)] + [0]
    val = [s for _, s in res] + [res[0][1]]
    obj = [3.0] * (N + 1)
    fig = plt.figure(figsize=(6.6, 6.2))
    ax = fig.add_subplot(111, polar=True)
    ax.set_theta_offset(math.pi / 2); ax.set_theta_direction(-1)
    ax.set_ylim(0, 4); ax.set_yticks([1, 2, 3, 4]); ax.set_yticklabels(["1", "2", "3", "4"], fontsize=7, color=OLI)
    ax.set_xticks(ang[:-1]); ax.set_xticklabels([d["corto"] for d, _ in res], fontsize=9, color=CAR)
    ax.plot(ang, obj, color=OK, lw=1.3, ls="--", label="Meta del plan (3,0 · Implementado)")
    ax.plot(ang, val, color=ORO, lw=2.2, label=f"Situación actual (índice {idx:.2f})")
    ax.fill(ang, val, color=ORO, alpha=0.25)
    ax.grid(color="#E4DFCF")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=1, frameon=False, fontsize=8.5)
    save(fig, "radar_madurez")
    return idx


# 4. Mapa de calor de evaluación de impacto (ejemplo del asistente)
def heatmap():
    inh = [(5, 2, "R1"), (4, 3, "R2"), (3, 4, "R3"), (3, 3, "R4")]
    res = [(5, 1, "R1"), (4, 1, "R2"), (3, 1, "R3"), (2, 2, "R4")]
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.4))
    for ax, data, tit in [(axs[0], inh, "Riesgo inherente (antes de medidas)"), (axs[1], res, "Riesgo residual (después de medidas)")]:
        for i in range(1, 6):
            for p in range(1, 6):
                n = i * p
                c = "#E6F2EA" if n <= 4 else "#FFF4D6" if n <= 9 else "#FBEDE5" if n <= 16 else "#F6DADA"
                ax.add_patch(plt.Rectangle((p - 0.5, i - 0.5), 1, 1, fc=c, ec="white", lw=2))
                ax.text(p, i - 0.32, str(n), ha="center", fontsize=6.5, color="#9a9278")
        cell = {}
        for i, p, r in data:
            cell.setdefault((i, p), []).append(r)
        for (i, p), rs in cell.items():
            ax.text(p, i + 0.05, " ".join(rs), ha="center", va="center", fontsize=9.5, weight="bold", color=CAR)
        ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5); ax.set_aspect("equal")
        ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
        ax.set_xlabel("Probabilidad"); ax.set_ylabel("Impacto"); ax.set_title(tit, fontsize=10.5, weight="bold", color=CAR)
        for s in ax.spines.values():
            s.set_visible(False)
    fig.text(0.5, -0.02, "Bajo 1-4 · Medio 5-9 · Alto 10-16 · Muy alto 17-25 (escala propia del portafolio)", ha="center", fontsize=8.5, color=OLI)
    save(fig, "heatmap_eipd")


# 5. Escenarios de multa (ejemplo del asistente de madurez)
def multa():
    sa, cp, mn, mx, lim = 17773.88, 15484.50, 12950.0, 18500.0, 8000.0
    ea, ec = 4443.47, 1238.76
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.9), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axs[0]
    ax.barh([1, 0], [sa, cp], color=[AL, OK], height=0.5)
    ax.axvspan(mn, mx, color="#EFEBDD", zorder=0)
    ax.axvline(lim, color=CAR, ls="--", lw=1.3)
    ax.text(lim, 1.5, f" Apetito al riesgo\n USD {lim:,.0f}".replace(",", "."), fontsize=8, color=CAR, va="top")
    ax.text((mn + mx) / 2, -0.55, "Rango legal de infracción grave (0,7 %-1 % del volumen de negocio)", ha="center", fontsize=7.8, color=OLI)
    for y, v in [(1, sa), (0, cp)]:
        ax.text(v + 150, y, f"USD {v:,.0f}".replace(",", "."), va="center", fontsize=9, weight="bold", color=CAR)
    ax.set_yticks([1, 0]); ax.set_yticklabels(["Si no actúa\n(índice 1,47)", "Con plan\n(índice 3,0)"])
    ax.set_xlim(0, 21500); ax.set_ylim(-0.8, 1.6)
    ax.set_title("Multa estimada", fontsize=10.5, weight="bold", color=CAR)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x/1000:.0f} mil"))
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax = axs[1]
    ax.bar([0, 1], [ea, ec], color=[AL, OK], width=0.55)
    for x, v, p in [(0, ea, "25 %"), (1, ec, "8 %")]:
        ax.text(x, v + 120, f"USD {v:,.0f}".replace(",", "."), ha="center", fontsize=9, weight="bold")
        ax.text(x, v / 2, f"prob.\n{p}", ha="center", va="center", fontsize=8, color="white")
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Si no actúa", "Con plan"]); ax.set_ylim(0, 5600)
    ax.set_title("Riesgo anual esperado (probabilidad × multa)", fontsize=10.5, weight="bold", color=CAR)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x/1000:.0f} mil"))
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    fig.text(0.5, -0.03, "Ejemplo ficticio: volumen de negocio USD 1,85 millones · Res. SPDP-SPD-2025-0022-R (modelo MPRIV-1) · estimación orientativa",
             ha="center", fontsize=8, color=OLI)
    fig.tight_layout()
    save(fig, "multa_escenarios")


# 6. Mapa de flujo de datos (ejemplo)
def flujo_datos():
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis("off")
    cols = [("ORIGEN", 0.2), ("RECOLECCIÓN", 2.2), ("SISTEMAS", 4.25), ("ENCARGADOS", 6.3), ("DESTINATARIOS", 8.3)]
    for t, x in cols:
        ax.text(x + 0.75, 4.35, t, ha="center", fontsize=8.5, weight="bold", color=ORO)
    B = {}
    def b(k, x, y, t, s="", fc=MAR):
        box(ax, x, y, 1.5, 0.78, t, s, fc=fc, fs=8.6, fss=7); B[k] = (x, y)
    b("cli", 0.2, 3.1, "Clientes", "identificación y contacto")
    b("tra", 0.2, 1.7, "Trabajadores", "laborales, bancarios")
    b("pos", 0.2, 0.3, "Postulantes", "hoja de vida")
    b("web", 2.2, 3.1, "Formulario web", "aviso de privacidad")
    b("fis", 2.2, 1.7, "Ficha física", "firma y consentimiento")
    b("mail", 2.2, 0.3, "Correo", "")
    b("erp", 4.25, 3.1, "ERP / facturación", "servidor local")
    b("nom", 4.25, 1.7, "Software nómina", "nube")
    b("arc", 4.25, 0.3, "Archivo físico", "bajo llave")
    b("nube", 6.3, 2.45, "Proveedor nube", "EE. UU. · encargo (no transferencia)", fc="#FBEDE5")
    b("cont", 6.3, 0.85, "Contadora externa", "contrato de encargo")
    b("sri", 8.3, 3.1, "SRI", "obligación legal")
    b("iess", 8.3, 1.7, "IESS · MDT", "obligación legal")
    b("sup", 8.3, 0.3, "Supresión", "plazo vencido", fc="#E6F2EA")
    def a(k1, k2):
        x1, y1 = B[k1]; x2, y2 = B[k2]
        arrow(ax, (x1 + 1.5, y1 + 0.39), (x2, y2 + 0.39))
    for p in [("cli", "web"), ("tra", "fis"), ("pos", "mail"), ("web", "erp"), ("fis", "nom"), ("mail", "arc"),
              ("erp", "sri"), ("nom", "nube"), ("nom", "cont"), ("cont", "iess"), ("arc", "sup")]:
        a(*p)
    save(fig, "flujo_datos")


# 7. Calendario anual del DPD
def calendario():
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    act = [("Reporte de indicadores a la gerencia", [3, 6, 9, 12], ORO),
           ("Revisión del RAT por eventos y periódica", [1, 7], OLI),
           ("Revisión de solicitudes de derechos", list(range(1, 13)), "#8C7E3E"),
           ("Seguimiento a encargados (contratos, auditoría)", [2, 8], "#5A4F25"),
           ("Capacitación al personal", [4, 10], OK),
           ("Simulacro de vulneración", [5], AL),
           ("Revisión de evaluaciones de impacto", [6], "#3A3F47"),
           ("Diagnóstico de madurez y plan anual", [11], CAR),
           ("Monitoreo normativo SPDP", list(range(1, 13)), "#B8B19A")]
    fig, ax = plt.subplots(figsize=(10, 3.9))
    for i, (t, ms, c) in enumerate(act):
        y = len(act) - i
        for m in ms:
            ax.add_patch(FancyBboxPatch((m - 0.42, y - 0.32), 0.84, 0.64, boxstyle="round,pad=0,rounding_size=0.12", fc=c, ec="none"))
        ax.text(0.3, y, t, ha="right", va="center", fontsize=8.6, color=CAR)
    ax.set_xlim(0.4, 12.6); ax.set_ylim(0.3, len(act) + 0.8)
    ax.set_xticks(range(1, 13)); ax.set_xticklabels(meses, fontsize=8.5); ax.set_yticks([])
    ax.xaxis.tick_top()
    for s in ax.spines.values():
        s.set_visible(False)
    ax.grid(axis="x", color="#EFEBDD")
    save(fig, "calendario_dpd")


# 8. ISO por niveles
def iso():
    fig, ax = plt.subplots(figsize=(10, 4.3))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.3); ax.axis("off")
    capas = [
        ("INDISPENSABLES", CAR, MAR, ["ISO/IEC 27701:2025\nGestión de la privacidad", "ISO/IEC 27001:2022\nSeguridad de información", "ISO/IEC 29100\nMarco de privacidad", "ISO/IEC 29134\nEvaluación de impacto"]),
        ("RECOMENDADAS", ORO, CAR, ["ISO/IEC 27002:2022\nControles", "ISO/IEC 27005 · ISO 31000\nGestión de riesgos", "ISO/IEC 27035\nIncidentes", "ISO/IEC 29151\nControles para datos personales"]),
        ("SEGÚN EL CASO", MAR, CAR, ["ISO/IEC 27018\nDatos en la nube", "ISO/IEC 29184\nAvisos y consentimiento", "ISO/IEC 27560\nRegistro de consentimientos", "ISO/IEC 42001\nInteligencia artificial"]),
    ]
    for r, (t, fc, tc, items) in enumerate(capas):
        y = 2.95 - r * 1.42
        ax.text(0.05, y + 0.5, t, fontsize=9, weight="bold", color=ORO if r else CAR, va="center")
        for j, it in enumerate(items):
            x = 1.75 + j * 2.07
            ax.add_patch(FancyBboxPatch((x, y), 1.92, 1.0, boxstyle="round,pad=0.02,rounding_size=0.07", fc=fc, ec=ORO, lw=1.2))
            a, b_ = it.split("\n")
            ax.text(x + 0.96, y + 0.64, a, ha="center", va="center", fontsize=8, weight="bold", color=tc)
            ax.text(x + 0.96, y + 0.3, b_, ha="center", va="center", fontsize=7, color=tc if r == 1 else (ORC if r == 0 else OLI))
    save(fig, "iso_niveles")


# 9. Estados del RAT de ejemplo
def estados_rat():
    fig, ax = plt.subplots(figsize=(4.6, 3.4))
    vals, labs, cols = [4, 3, 1], ["Incompleto (4)", "Mínimo cumplido (3)", "Completo (1)"], [AL, AM, OK]
    ax.pie(vals, colors=cols, startangle=90, counterclock=False, wedgeprops={"width": 0.38, "edgecolor": "white", "linewidth": 2})
    ax.text(0, 0.06, "50 %", ha="center", fontsize=17, weight="bold", color=CAR)
    ax.text(0, -0.2, "con mínimo legal", ha="center", fontsize=8, color=OLI)
    ax.legend(labs, loc="center left", bbox_to_anchor=(1, 0.5), frameon=False, fontsize=8.5)
    save(fig, "estados_rat")


# 10. Puntaje MTGE del ejemplo de la herramienta 04
def mtge():
    import granescala_config as G
    trat = [("Facturación y clientes", [2, 1, 0.5, 1, 2, 2], False), ("Nómina", [1, 2, 3, 1, 2, 1], False),
            ("Asistencia con huella", [1, 0.5, 2, 2, 1, 1], True), ("Asistentes a feria", [1, 0.5, 0.5, 0.5, 0.5, 1], False)]
    nombres = ["Titulares", "Volumen", "Categorías", "Frecuencia", "Permanencia", "Alcance"]
    cols = [CAR, OLI, AL, ORO, "#8C7E3E", ORC]
    fig, ax = plt.subplots(figsize=(9, 3.6))
    for i, (t, v, d) in enumerate(trat):
        left = 0
        for j, x in enumerate(v):
            ax.barh(i, x, left=left, color=cols[j], edgecolor="white", height=0.6, label=nombres[j] if i == 0 else None)
            left += x
        ax.text(left + 0.15, i, f"{str(left).replace('.0', '').replace('.', ',')} pts" + ("  · directa (biométrico)" if d else ""), va="center", fontsize=9, weight="bold", color=AL if left >= G.UMBRAL else OK)
    ax.axvline(G.UMBRAL, color=CAR, lw=1.6, ls="--"); ax.text(G.UMBRAL + 0.08, 3.55, "Umbral 6", fontsize=8.5, weight="bold")
    ax.set_yticks(range(len(trat))); ax.set_yticklabels([t for t, _, _ in trat]); ax.invert_yaxis(); ax.set_xlim(0, 15)
    ax.set_xlabel("Puntaje MTGE (Res. SPDP-SPD-2026-0005-R, art. 8)")
    for s_ in ("top", "right"): ax.spines[s_].set_visible(False)
    ax.legend(ncol=6, fontsize=7.5, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.22))
    save(fig, "mtge_ejemplo")


# 11. Honorarios por método (ejemplo de la herramienta 01)
def honorarios():
    fases = ["Evaluación inicial", "Implementación", "Control mensual × 12"]
    datos = {"Volumen de negocio": [1470, 3780, 350 * 12], "Volumen de tratamiento": [1090, 2210, 590 * 12], "Técnica (piso)": [1350, 2130, 370 * 12]}
    rec = [1350, 2210, 370 * 12]
    fig, ax = plt.subplots(figsize=(9, 3.6))
    cols = [ORC, OLI, CAR]; wb = 0.24
    for k, (m, v) in enumerate(datos.items()):
        xs = [i + (k - 1) * wb for i in range(3)]
        ax.bar(xs, v, width=wb, color=cols[k], label=m)
    for i, r in enumerate(rec):
        ax.plot([i - 0.4, i + 0.4], [r, r], color=AL, lw=2)
        ax.text(i + 0.42, r, f"${r:,.0f}".replace(",", "."), va="center", fontsize=8.5, weight="bold", color=AL)
    ax.plot([], [], color=AL, lw=2, label="Recomendado (mediana con piso técnico)")
    ax.set_xticks(range(3)); ax.set_xticklabels(fases); ax.set_ylabel("USD sin IVA")
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x:,.0f}".replace(",", ".")))
    for s_ in ("top", "right"): ax.spines[s_].set_visible(False)
    ax.legend(fontsize=8, frameon=False, ncol=2, loc="upper left")
    save(fig, "honorarios_metodos")


# 12. Recorrido de los datos (roadmap)
def roadmap():
    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.set_xlim(0, 11); ax.set_ylim(0, 4.2); ax.axis("off")
    et = [("1", "Captación", "Formulario, contrato,\ncámara, correo", "Aviso de privacidad\ny base legal"),
          ("2", "Registro", "ERP, nómina, Excel,\narchivo físico", "RAT y medidas\nde seguridad"),
          ("3", "Uso", "Facturar, pagar,\natender, vender", "Solo para la\nfinalidad informada"),
          ("4", "Comunicación", "Encargados y\ndestinatarios", "Contrato de encargo\no base del art. 33"),
          ("5", "Conservación", "Mientras se necesita\no lo exige la ley", "Plazo definido\nen el RAT"),
          ("6", "Supresión", "Borrado, destrucción\no anonimización", "Constancia de\nsupresión")]
    w, gap = 1.62, 0.2
    for i, (n, t, q, c) in enumerate(et):
        x = 0.1 + i * (w + gap)
        ax.add_patch(FancyBboxPatch((x, 2.0), w, 1.45, boxstyle="round,pad=0.02,rounding_size=0.08", fc=CAR if i in (0, 3) else MAR, ec=ORO, lw=1.5))
        dark = i in (0, 3)
        ax.text(x + 0.14, 3.22, n, fontsize=9, weight="bold", color=ORO)
        ax.text(x + w / 2, 2.98, t, ha="center", va="center", fontsize=10.5, weight="bold", color=MAR if dark else CAR)
        ax.text(x + w / 2, 2.42, q, ha="center", va="center", fontsize=7.6, color=ORC if dark else OLI)
        ax.add_patch(FancyBboxPatch((x + 0.08, 0.55), w - 0.16, 0.95, boxstyle="round,pad=0.02,rounding_size=0.06", fc="#E6F2EA", ec=OK, lw=1))
        ax.text(x + w / 2, 1.02, c, ha="center", va="center", fontsize=7.6, color="#2E5E40")
        arrow(ax, (x + w / 2, 1.98), (x + w / 2, 1.52), color=OK)
        if i < len(et) - 1:
            arrow(ax, (x + w + 0.02, 2.72), (x + w + gap - 0.02, 2.72))
    ax.text(0.1, 3.85, "QUÉ PASA CON EL DATO", fontsize=8.5, weight="bold", color=ORO)
    ax.text(0.1, 0.15, "QUÉ EXIGE LA LEY EN CADA ETAPA (lo documenta la empresa; el DPD asesora y supervisa)", fontsize=8.5, weight="bold", color=OK)
    save(fig, "roadmap_datos")


# 13. Encargo frente a comunicación o transferencia
def roles():
    fig, ax = plt.subplots(figsize=(10.5, 4.8))
    ax.set_xlim(0, 10.5); ax.set_ylim(0, 4.8); ax.axis("off")
    ax.add_patch(FancyBboxPatch((4.0, 1.75), 2.5, 1.3, boxstyle="round,pad=0.02,rounding_size=0.1", fc=CAR, ec=ORO, lw=2))
    ax.text(5.25, 2.6, "RESPONSABLE", ha="center", fontsize=11, weight="bold", color=MAR)
    ax.text(5.25, 2.15, "La empresa: decide\npara qué y cómo", ha="center", va="center", fontsize=8, color=ORC)
    ax.text(1.6, 4.5, "ENCARGADOS · tratan por cuenta del responsable", ha="center", fontsize=8.5, weight="bold", color=OLI)
    ax.text(1.6, 4.2, "No es transferencia (LOPDP arts. 34 y 35) · contrato art. 41 RGLOPDP", ha="center", fontsize=7.2, color=OLI)
    ax.text(8.9, 4.5, "DESTINATARIOS · usan los datos para fines propios", ha="center", fontsize=8.5, weight="bold", color=AL)
    ax.text(8.9, 4.2, "Comunicación o transferencia (LOPDP art. 33) · base legal", ha="center", fontsize=7.2, color=AL)
    izq = [("Contadora externa", "lleva la contabilidad"), ("Proveedor de nómina", "calcula roles de pago"), ("Nube o ERP en el exterior", "aloja la información")]
    der = [("SRI · IESS · Ministerio", "obligación legal"), ("Aseguradora médica", "a pedido del titular"), ("Fiscalía o juez", "orden o requerimiento")]
    for i, (t, s_) in enumerate(izq):
        y = 3.2 - i * 1.15
        box(ax, 0.3, y, 2.6, 0.82, t, s_, fc=MAR, ec=OLI, fs=8.8, fss=7.4)
        arrow(ax, (4.0, 2.4), (2.92, y + 0.41), color=OLI)
    for i, (t, s_) in enumerate(der):
        y = 3.2 - i * 1.15
        box(ax, 7.6, y, 2.6, 0.82, t, s_, fc="#FBEDE5", ec=AL, fs=8.8, fss=7.4)
        arrow(ax, (6.5, 2.4), (7.58, y + 0.41), color=AL)
    ax.text(5.25, 0.35, "Si un encargado usa los datos para sus propios fines, pasa a ser responsable (RGLOPDP art. 43).", ha="center", fontsize=8, style="italic", color=CAR)
    save(fig, "roles_datos")


# 14. Matriz de mapeo: áreas × dominios de madurez
def mapeo():
    areas = ["Gerencia", "Talento humano", "Ventas y\natención", "Contabilidad\ny finanzas", "Sistemas (TI)", "Marketing", "Seguridad\nfísica", "Legal o\ncompras"]
    doms = [d["corto"] for d in MC.DOMINIOS]
    P, S_ = 2, 1  # principal, apoyo
    M = {
        "Gerencia":            [P, P, S_, S_, 0, 0, 0, 0, 0, S_, 0, P],
        "Talento humano":      [0, 0, P, P, P, S_, S_, S_, 0, S_, 0, P],
        "Ventas y\natención":  [0, 0, P, P, P, P, 0, 0, 0, 0, 0, S_],
        "Contabilidad\ny finanzas": [0, 0, P, P, S_, 0, P, S_, 0, 0, S_, 0],
        "Sistemas (TI)":       [0, 0, S_, 0, 0, 0, P, P, P, P, P, S_],
        "Marketing":           [0, 0, P, P, P, P, S_, 0, S_, 0, S_, 0],
        "Seguridad\nfísica":   [0, 0, P, P, P, 0, S_, P, S_, S_, 0, 0],
        "Legal o\ncompras":    [S_, S_, S_, P, 0, S_, P, 0, 0, 0, P, 0],
    }
    import numpy as np
    Z = np.array([M[a] for a in areas])
    from matplotlib.colors import ListedColormap
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.imshow(Z, cmap=ListedColormap(["#FFFFFF", ORC, ORO]), vmin=0, vmax=2, aspect="auto")
    ax.set_xticks(range(len(doms))); ax.set_xticklabels(doms, rotation=35, ha="right", fontsize=8.5)
    ax.set_yticks(range(len(areas))); ax.set_yticklabels(areas, fontsize=8.5)
    for i in range(len(areas)):
        for j in range(len(doms)):
            if Z[i, j] == 2: ax.plot(j, i, "o", ms=6, color=CAR)
            elif Z[i, j] == 1: ax.plot(j, i, "o", ms=6, mfc="white", mec=OLI)
    ax.set_xticks(np.arange(-.5, len(doms)), minor=True); ax.set_yticks(np.arange(-.5, len(areas)), minor=True)
    ax.grid(which="minor", color="#DDD8C8", lw=0.8); ax.tick_params(which="minor", length=0)
    for s_ in ax.spines.values(): s_.set_visible(False)
    ax.plot([], [], "o", ms=6, color=CAR, label="Fuente principal de evidencia"); ax.plot([], [], "o", ms=6, mfc="white", mec=OLI, label="Aporta información")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, frameon=False, fontsize=8.5)
    save(fig, "mapeo_areas")


# 15. Roadmap de la gestión del DPD en la empresa
def roadmap_dpd():
    fig, ax = plt.subplots(figsize=(15, 7.6))
    ax.set_xlim(0, 15); ax.set_ylim(0, 7.6); ax.axis("off")
    F = [("0", "Propuesta", "Semana 0", "Reunión inicial, catálogo\ny proforma (01 · 02)", "Decide contratar;\ndesigna un enlace"),
         ("1", "Diagnóstico", "Semanas 1-3", "Mapea áreas y mide\nla madurez (03)", "Entrega evidencias;\nla gerencia valida"),
         ("2", "Inventario", "Semanas 3-6", "Mide la gran escala (05);\nrevisa el RAT (04, S29)", "El implementador\nelabora el RAT"),
         ("3", "Riesgos", "Semanas 6-9", "Observaciones no\nvinculantes (06 · 07)", "Implementador elabora;\ndueños deciden"),
         ("4", "Implementación", "Semanas 9-14", "Verifica lo\nimplementado (S30);\nredacta solo si no es DPD", "Elige implementador;\naprueba e IMPLEMENTA"),
         ("5", "Designación", "Semana 14", "Verifica requisitos;\nregistro ante la SPDP", "Designa al DPD (si\ncorresponde) y\ncomunica el canal"),
         ("6", "Control mensual", "Cada mes", "Supervisa, informa,\natiende consultas", "Ejecuta mejoras;\nresponde solicitudes"),
         ("7", "Revisión anual", "Cada año", "Repite 03 y 05; revisa\nponderaciones y EIPD", "Actualiza el RAT y\nel plan de acción")]
    w, gap, x0 = 1.68, 0.12, 0.55
    ax.text(0.1, 5.05, "DPD O\nCONSULTOR", fontsize=8.5, weight="bold", color=ORO, rotation=90, va="center", ha="center")
    ax.text(0.1, 2.75, "EMPRESA\n(RESPONSABLE)", fontsize=8.5, weight="bold", color=OK, rotation=90, va="center", ha="center")
    ax.text(x0, 7.42, "ROADMAP DE LA GESTIÓN DEL DPD", fontsize=12, weight="bold", color=CAR)
    ax.text(x0, 7.08, "El DPD asesora y supervisa; la empresa decide, aprueba e implementa", fontsize=9, color=OLI, style="italic")
    for i, (n, t_, sem, dpd, emp) in enumerate(F):
        x = x0 + i * (w + gap)
        dark = i in (0, 4, 7)
        ax.add_patch(FancyBboxPatch((x, 6.15), w, 0.75, boxstyle="round,pad=0.02,rounding_size=0.08", fc=CAR if dark else ORO, ec=ORO, lw=1.2))
        ax.text(x + 0.12, 6.7, n, fontsize=8, weight="bold", color=ORC if dark else CAR)
        ax.text(x + w / 2, 6.55, t_, ha="center", va="center", fontsize=9.6, weight="bold", color=MAR if dark else CAR)
        ax.text(x + w / 2, 6.27, sem, ha="center", va="center", fontsize=7.2, color=ORC if dark else CAR)
        ax.add_patch(FancyBboxPatch((x, 4.35), w, 1.45, boxstyle="round,pad=0.02,rounding_size=0.06", fc=MAR, ec=ORO, lw=1.2))
        ax.text(x + w / 2, 5.07, dpd, ha="center", va="center", fontsize=7.6, color=CAR)
        ax.add_patch(FancyBboxPatch((x, 2.05), w, 1.45, boxstyle="round,pad=0.02,rounding_size=0.06", fc="#E6F2EA", ec=OK, lw=1.2))
        ax.text(x + w / 2, 2.77, emp, ha="center", va="center", fontsize=7.6, color="#2E5E40", weight="bold" if i == 4 else "normal")
        arrow(ax, (x + w / 2, 4.33), (x + w / 2, 3.52), color=OLI)
        if i < len(F) - 1:
            arrow(ax, (x + w + 0.01, 6.52), (x + w + gap - 0.01, 6.52), color=OLI)
    xa = x0 + 7 * (w + gap) + w / 2
    xb = x0 + 3 * (w + gap) + w / 2
    arrow(ax, (xa, 6.95), (xb, 6.95), color=ORO, rad=0.12)
    ax.text((xa + xb) / 2, 7.5, "La revisión anual vuelve a medir los riesgos", ha="center", fontsize=8, color=OLI, style="italic")
    ax.add_patch(FancyBboxPatch((x0, 0.25), 14.25, 1.25, boxstyle="round,pad=0.02,rounding_size=0.08", fc="#FBEDE5", ec=AL, lw=1.2))
    ax.text(x0 + 0.2, 1.22, "POR EVENTO (en cualquier momento)", fontsize=8.5, weight="bold", color=AL)
    ev = ["Vulneración: protocolo y\nnotificación en plazo (09)", "Proyecto nuevo: protección\ndesde el diseño y por defecto", "Solicitud de un titular:\nrespuesta en plazo", "Requerimiento de la SPDP:\nrespuesta con evidencia"]
    for j, e in enumerate(ev):
        ax.text(x0 + 1.9 + j * 3.55, 0.68, e, ha="center", va="center", fontsize=7.8, color=CAR)
    save(fig, "roadmap_dpd")


if __name__ == "__main__":
    flujo(); ciclo(); idx = radar(); heatmap(); multa(); flujo_datos(); calendario(); iso(); estados_rat(); mtge(); honorarios(); roadmap(); roles(); mapeo(); roadmap_dpd()
    print("índice ejemplo", round(idx, 2))
