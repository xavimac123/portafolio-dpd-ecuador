"""Genera la plantilla del Registro de Actividades de Tratamiento (RAT) y un ejemplo ficticio.

Uso: python scripts/generar_rat.py
Salida: 04-registro-tratamientos/plantilla-RAT.xlsx y ejemplo-RAT-ficticio.xlsx
"""
import datetime
from pathlib import Path

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import rat_config as C  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "04-registro-tratamientos"

FONT = "Arial"
AZUL = "1F3864"
INPUT = PatternFill("solid", fgColor="FFF2CC")  # celdas a completar
HEAD = PatternFill("solid", fgColor=AZUL)
OKF = PatternFill("solid", fgColor="E2EFDA")
ALERTF = PatternFill("solid", fgColor="FCE4D6")
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

BASES = C.BASES
SINO = ["Sí", "No"]
CAMPOS = C.CAMPOS
SECF = PatternFill("solid", fgColor="D9E1F2")
AUTOF = PatternFill("solid", fgColor="EDEDED")
FIRST = 5  # primera fila de datos de la hoja RAT


def colmap():
    """Letra de columna por clave de campo, más las columnas de estado."""
    m = {c["k"]: get_column_letter(i) for i, c in enumerate(CAMPOS, start=1)}
    n = len(CAMPOS)
    m["_estado"], m["_min"], m["_obs"] = (get_column_letter(n + 1), get_column_letter(n + 2), get_column_letter(n + 3))
    return m


def style_header(ws, row, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(name=FONT, bold=True, color="FFFFFF", size=10)
        cell.fill = HEAD
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = BORDER


def base_font(ws):
    for row in ws.iter_rows():
        for cell in row:
            if cell.font is None or cell.font.name != FONT:
                f = cell.font
                cell.font = Font(name=FONT, size=f.size or 10, bold=f.bold, italic=f.italic, color=f.color)


def hoja_instrucciones(wb):
    ws = wb.active
    ws.title = "Instrucciones"
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 100
    lines = [
        ("Registro de Actividades de Tratamiento (RAT) — LOPDP Ecuador", True, 14),
        ("Macías Sánchez Consultores · Herramienta 08 · v0.4", False, 10),
        ("", False, 10),
        ("Para qué sirve", True, 11),
        ("Documentar cada actividad de tratamiento con el contenido mínimo del art. 38 del Reglamento General a la LOPDP, separar lo exigido por la norma de lo recomendable y detectar vacíos automáticamente.", False, 10),
        ("", False, 10),
        ("Cómo se levanta el registro", True, 11),
        ("1. Hoja 'Obligado': confirma si la organización debe llevar el RAT (arts. 38, 39 y 44 RGLOPDP).", False, 10),
        ("2. Hoja 'Responsable': datos de contacto del responsable, corresponsable y DPD (art. 38 num. 1).", False, 10),
        ("3. Recorre la organización por áreas (Talento Humano, Contabilidad, Comercial, TI, Seguridad...) y pregunta a cada una qué datos personales usa y para qué. La hoja 'Catálogo' sugiere actividades frecuentes.", False, 10),
        ("4. Hoja 'RAT': una fila por actividad de tratamiento. Una actividad se define por su finalidad, no por la base de datos ni el programa que se usa. Si dos finalidades tienen bases legitimadoras o plazos distintos, regístralas en filas separadas.", False, 10),
        ("5. Celdas amarillas = listas desplegables que aceptan texto propio ('Otro'); varios valores se separan con punto y coma. Celdas grises = cálculo automático.", False, 10),
        ("6. Columnas de control: 'Faltantes del mínimo legal' (art. 38) y 'Observaciones' (buenas prácticas y riesgos de cumplimiento). Estado: Incompleto · Mínimo cumplido · Completo.", False, 10),
        ("7. Hoja 'RAT encargado': solo si la organización trata datos por cuenta de clientes obligados (art. 44 RGLOPDP).", False, 10),
        ("8. Hoja 'Resumen': estado general y firma de responsabilidad. Revisa el registro al menos cada %d meses y siempre que cambie un tratamiento." % C.REVISION_MESES, False, 10),
        ("", False, 10),
        ("Fila 3 de la hoja RAT", True, 11),
        ("'Art. 38 num. X' marca el contenido mínimo exigido; 'Buena práctica' marca campos recomendados que no exige la norma pero facilitan demostrar cumplimiento, atender derechos y gestionar vulneraciones.", False, 10),
        ("", False, 10),
        ("Límites", True, 11),
        ("Las alertas revisan que los campos existan, no que su contenido sea jurídicamente correcto. La calificación de bases legitimadoras, plazos y medidas requiere análisis profesional.", False, 10),
        ("El nivel de riesgo es un criterio interno orientativo; no sustituye la evaluación de impacto del art. 42 LOPDP.", False, 10),
        ("El RAT es distinto de la inscripción en el Registro Nacional de Protección de Datos Personales (art. 51 LOPDP).", False, 10),
        ("Verifica la vigencia de la normativa citada antes de usar esta herramienta con un cliente (ver BASE-LEGAL.md).", False, 10),
    ]
    for i, (text, bold, size) in enumerate(lines, start=2):
        c = ws.cell(row=i, column=2, value=text)
        c.font = Font(name=FONT, bold=bold, size=size, color=AZUL if bold else "000000")
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.sheet_view.showGridLines = False


def hoja_obligado(wb, respuestas=None):
    ws = wb.create_sheet("Obligado")
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 52
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 55
    ws.column_dimensions["E"].width = 62
    ws["B2"] = "¿Debe la organización llevar el RAT? (arts. 38, 39 y 44 RGLOPDP)"
    ws["B2"].font = Font(name=FONT, bold=True, size=13, color=AZUL)
    ws["B3"] = "Responde en las celdas amarillas. Las columnas D y E explican cada pregunta. La columna E es un resumen fiel de la norma salvo que diga 'Texto literal'."
    ws["B3"].font = Font(name=FONT, size=9, italic=True, color="7F7F7F")
    r = 5
    for col, h in zip("BCDE", ["Pregunta", "Respuesta", "Qué significa", "Qué dice la norma"]):
        ws[f"{col}{r}"] = h
    style_header(ws, r, 5)
    ws.cell(row=r, column=1).fill = PatternFill(None)
    dv_sn = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True)
    dv_rol = DataValidation(type="list", formula1='"Responsable,Encargado,Ambos"', allow_blank=True)
    ws.add_data_validation(dv_sn)
    ws.add_data_validation(dv_rol)
    filas = {}
    grupo = None
    r += 1
    for q in C.PREGUNTAS:
        if q["grupo"] != grupo:
            grupo = q["grupo"]
            c = ws.cell(row=r, column=2, value=C.GRUPOS[grupo])
            c.font = Font(name=FONT, bold=True, size=10, color=AZUL)
            r += 1
        ws.cell(row=r, column=2, value=q["texto"])
        resp_c = ws.cell(row=r, column=3, value=(respuestas or {}).get(q["id"]))
        resp = resp_c
        resp.fill = INPUT
        resp.font = Font(name=FONT, size=10, color="0000FF")
        resp.alignment = Alignment(horizontal="center", vertical="top")
        ws.cell(row=r, column=4, value=q["concepto"])
        norma = q["norma"] + ("" if not q["norma"] else ("  [Texto literal]" if q["literal"] else "  [Resumen fiel]"))
        ws.cell(row=r, column=5, value=norma)
        for cc in (2, 4, 5):
            cell = ws.cell(row=r, column=cc)
            cell.font = Font(name=FONT, size=9 if cc > 2 else 10)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        for cc in range(2, 6):
            ws.cell(row=r, column=cc).border = BORDER
        if q["tipo"] == "sino":
            dv_sn.add(f"C{r}")
        elif q["tipo"] == "rol":
            dv_rol.add(f"C{r}")
        filas.setdefault(q["grupo"], []).append(r)
        filas[q["id"]] = r
        ws.row_dimensions[r].height = 62
        r += 1

    def rng(g):
        rows = filas[g]
        return f"C{rows[0]}:C{rows[-1]}"

    trab = f"C{filas['trab']}"
    rol = f"C{filas['rol']}"
    total = len(C.PREGUNTAS)
    r += 1
    ws.cell(row=r, column=2, value="Resultado").font = Font(name=FONT, bold=True, size=12)
    res = ws.cell(row=r, column=3)
    res.value = (f'=IF(AND({trab}="",{rol}=""),"",IF(OR(N({trab})>=100,COUNTIF({rng("habitual")},"Sí")>0,'
                 f'COUNTIF({rng("especial")},"Sí")>0,COUNTIF({rng("riesgo")},"Sí")>0),"OBLIGADO",'
                 f'IF(COUNTA(C{filas["rol"]}:C{filas[C.PREGUNTAS[-1]["id"]]})<{total},"PENDIENTE","NO OBLIGADO")))')
    res.font = Font(name=FONT, bold=True, size=12)
    res.alignment = Alignment(horizontal="center")
    res.border = BORDER
    fund = ws.cell(row=r, column=4)
    fund.value = (f'=IF(C{r}="","",IF(N({trab})>=100,"100 o más trabajadores (art. 38). ","")'
                  f'&IF(COUNTIF({rng("habitual")},"Sí")>0,"Tratamiento habitual, no ocasional (art. 39). ","")'
                  f'&IF(COUNTIF({rng("especial")},"Sí")>0,"Incluye categorías especiales (art. 39; art. 25 LOPDP). ","")'
                  f'&IF(COUNTIF({rng("riesgo")},"Sí")>0,"Indicadores de riesgo para los titulares (art. 39). ","")'
                  f'&IF(C{r}="PENDIENTE","Faltan respuestas. ","")'
                  f'&IF(C{r}="NO OBLIGADO","Situación poco frecuente: revisar respuestas. ","")'
                  f'&IF(OR({rol}="Encargado",{rol}="Ambos"),"Como encargado, lleva el RAT de cada cliente solo si ese responsable está obligado (art. 44).",""))')
    fund.font = Font(name=FONT, size=10, italic=True)
    fund.alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
    ws.row_dimensions[r].height = 60
    ws.cell(row=r + 2, column=2, value=C.NORMA_39 + "  [Resumen fiel]").font = Font(name=FONT, size=9, italic=True, color="7F7F7F")
    ws.cell(row=r + 2, column=2).alignment = Alignment(wrap_text=True)
    ws.merge_cells(start_row=r + 2, start_column=2, end_row=r + 2, end_column=5)
    ws.row_dimensions[r + 2].height = 30
    ws.freeze_panes = "B6"
    ws.sheet_view.showGridLines = False
    return f"Obligado!$C${r}"


def hoja_responsable(wb, datos):
    ws = wb.create_sheet("Responsable")
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 36
    ws.column_dimensions["C"].width = 50
    ws["B2"] = "Identificación del responsable (art. 38 num. 1 RGLOPDP)"
    ws["B2"].font = Font(name=FONT, bold=True, size=12, color=AZUL)
    campos = [
        "Razón social / nombre", "RUC", "Representante legal", "Dirección", "Correo de atención al titular", "Teléfono",
        "Sector o actividad económica", "Corresponsable (si existe)", "Contacto del corresponsable",
        "Delegado de Protección de Datos (DPD)", "Correo del DPD", "Fecha de registro del DPD ante la SPDP",
        "Referencia del registro del DPD en la SPDP",
    ]
    for i, campo in enumerate(campos, start=4):
        ws.cell(row=i, column=2, value=campo).font = Font(name=FONT, size=10, bold=True)
        c = ws.cell(row=i, column=3, value=datos.get(campo, ""))
        c.fill = INPUT
        c.border = BORDER
        c.font = Font(name=FONT, size=10, color="0000FF")
    ws.sheet_view.showGridLines = False


def hoja_listas(wb):
    ws = wb.create_sheet("Listas")
    ws.cell(row=1, column=1, value="Bases legitimadoras (art. 7 LOPDP)").font = Font(name=FONT, bold=True)
    for i, b in enumerate(BASES, start=2):
        ws.cell(row=i, column=1, value=b).font = Font(name=FONT, size=10)
    rangos = {}
    j = 2
    for nombre, d in C.LISTAS.items():
        L = get_column_letter(j)
        ws.cell(row=1, column=j, value=nombre).font = Font(name=FONT, bold=True)
        ops = d["opciones"] + [C.OTRO + " (escribir en la celda)"]
        for i, o in enumerate(ops, start=2):
            ws.cell(row=i, column=j, value=o).font = Font(name=FONT, size=10)
        ws.column_dimensions[L].width = 40
        rangos[nombre] = f"=Listas!${L}$2:${L}${1 + len(ops)}"
        j += 1
    # listas auxiliares para detección automática
    for nombre, vals in (("especiales", C.LISTAS["datos"]["especiales"]), ("sensibles", C.LISTAS["datos"]["sensibles"])):
        L = get_column_letter(j)
        ws.cell(row=1, column=j, value=nombre).font = Font(name=FONT, bold=True)
        for i, o in enumerate(vals, start=2):
            ws.cell(row=i, column=j, value=o)
        rangos[nombre] = f"Listas!${L}$2:${L}${1 + len(vals)}"
        j += 1
    ws.column_dimensions["A"].width = 50
    ws.sheet_state = "hidden"
    return rangos


def formulas(r, M, rg):
    """Fórmulas de riesgo, próxima revisión, faltantes y observaciones para la fila r."""
    c = {k: f"{v}{r}" for k, v in M.items()}
    R = C.RIESGO
    vol = "+".join(f'IF({c["volumen"]}="{k}",{v},0)' for k, v in R["volumen"].items())
    dat = "+".join(f'IF(ISNUMBER(SEARCH("{k}",{c["datos"]})),{v},0)' for k, v in R["datos"].items())
    pts = (f'IF({c["especial"]}="Sí",{R["especial"]},0)+IF({c["nna"]}="Sí",{R["nna"]},0)'
           f'+IF({c["perfiles"]}="Sí",{R["perfiles"]},0)+IF({c["transf"]}="Sí",{R["transf"]},0)+{vol}+{dat}')
    riesgo = (f'=IF({c["actividad"]}="","",IF({pts}>={R["umbral_alto"]},"Alto",'
              f'IF({pts}>={R["umbral_medio"]},"Medio","Bajo")))')
    prox = f'=IF({c["rev"]}="","",EDATE({c["rev"]},{C.REVISION_MESES}))'
    hay = lambda lista, celda: f'SUMPRODUCT(--ISNUMBER(SEARCH({rg[lista]},{celda})))>0'
    falt = (
        f'=IF({c["actividad"]}="","",TRIM('
        f'IF({c["finalidad"]}="","Finalidad (num. 2). ","")'
        f'&IF({c["dest"]}="","Destinatarios (num. 3); escribe Ninguno si no hay. ","")'
        f'&IF({c["titulares"]}="","Categorías de titulares (num. 4). ","")'
        f'&IF({c["datos"]}="","Categorías de datos (num. 4). ","")'
        f'&IF({c["perfiles"]}="","Indicar si hay perfiles (num. 5). ","")'
        f'&IF({c["transf"]}="","Indicar si hay transferencia internacional (num. 6). ","")'
        f'&IF(AND({c["transf"]}="Sí",OR({c["pais"]}="",{c["tgar"]}="")),"País o garantía de la transferencia (num. 6). ","")'
        f'&IF({c["base"]}="","Base legitimadora (num. 7). ","")'
        f'&IF(AND({c["base"]}="Interés legítimo",{c["il"]}=""),"Evaluación de ponderación del interés legítimo (num. 7; Res. 0041). ","")'
        f'&IF({c["plazo"]}="","Plazo de conservación (num. 8). ","")'
        f'&IF({c["medidas"]}="","Medidas (num. 9). ","")))'
    )
    gen = " ,".join(f'{c["finalidad"]}="{g}"' for g in C.FINALIDADES_GENERICAS).replace(" ,", ",")
    obs = (
        f'=IF({c["actividad"]}="","",TRIM('
        f'IF(OR({gen}),"Finalidad genérica: describe el servicio concreto. ","")'
        f'&IF(AND(ISNUMBER(SEARCH("{C.FINALIDAD_SEPARABLE}",{c["finalidad"]})),ISNUMBER(SEARCH(";",{c["finalidad"]}))),"La publicidad suele tener otra base: considera una actividad separada. ","")'
        f'&IF(AND({hay("especiales", c["datos"])},{c["especial"]}<>"Sí"),"Los datos incluyen categorías especiales: marca Sí. ","")'
        f'&IF(AND({hay("sensibles", c["datos"])},{c["exc26"]}=""),"Datos sensibles sin excepción del art. 26 LOPDP. ","")'
        f'&IF(AND({c["nna"]}="Sí",{c["base"]}="Consentimiento del titular"),"NNA con consentimiento: verificar quién lo otorga. ","")'
        f'&IF(OR({c["info"]}="",{c["info"]}="No se informa aún"),"Definir cómo se informa al titular (art. 12 LOPDP). ","")'
        f'&IF(AND({c["enc"]}<>"",{c["enc"]}<>"Ninguno",{c["contrato"]}<>"Sí, con todos"),"Encargados sin contrato de encargo completo (art. 41 RGLOPDP; art. 68 num. 9 LOPDP). ","")'
        f'&IF(ISNUMBER(SEARCH("(indicar",{c["plazo"]})),"Plazo genérico: indica la norma o el número de días. ","")'
        f'&IF(AND({c["transf"]}="Sí",{c["tia"]}=""),"Documenta la evaluación de la transferencia (buena práctica). ","")'
        f'&IF({c["sistemas"]}="","Indica sistemas y soportes. ","")'
        f'&IF({c["volumen"]}="","Indica el volumen aproximado de titulares. ","")'
        f'&IF(AND(OR({c["riesgo"]}="Alto",{c["especial"]}="Sí",{c["perfiles"]}="Sí"),{c["eipd"]}=""),"Define si requiere evaluación de impacto (art. 42 LOPDP). ","")'
        f'&IF(AND({c["eipd"]}="Sí",{c["eipdref"]}=""),"Falta referencia de la evaluación de impacto. ","")'
        f'&IF({c["rev"]}="","Sin fecha de revisión. ","")'
        f'&IF(AND({c["prox"]}<>"",{c["prox"]}<TODAY()),"Revisión vencida. ","")'
        f'&IF({c["propietario"]}="","Asigna un responsable interno. ","")))'
    )
    estado = (f'=IF({c["actividad"]}="","",IF({c["_min"]}<>"","Incompleto",'
              f'IF({c["_obs"]}<>"","Mínimo cumplido","Completo")))')
    return {"riesgo": riesgo, "prox": prox, "_min": falt, "_obs": obs, "_estado": estado}


def hoja_rat(wb, filas, rangos, n_filas=100):
    ws = wb.create_sheet("RAT")
    M = colmap()
    n = len(CAMPOS)
    extra = [("_estado", "Estado", 14), ("_min", "Faltantes del mínimo legal (art. 38)", 40), ("_obs", "Observaciones y recomendaciones", 48)]
    ncols = n + len(extra)
    ws.cell(row=1, column=1, value="Registro de Actividades de Tratamiento").font = Font(name=FONT, bold=True, size=13, color=AZUL)
    # fila 2: secciones
    secs = {}
    for i, cpo in enumerate(CAMPOS, start=1):
        secs.setdefault(cpo["sec"], [i, i])[1] = i
    secs["_ctl"] = [n + 1, ncols]
    for sec, (a, b) in secs.items():
        cell = ws.cell(row=2, column=a, value=C.SECCIONES.get(sec, "8 · Control automático"))
        cell.font = Font(name=FONT, bold=True, size=9, color=AZUL)
        cell.fill = SECF
        cell.alignment = Alignment(horizontal="left", vertical="center")
        if b > a:
            ws.merge_cells(start_row=2, start_column=a, end_row=2, end_column=b)
        for cc in range(a, b + 1):
            ws.cell(row=2, column=cc).border = BORDER
    # fila 3: numeral o buena práctica; fila 4: encabezados
    for i, cpo in enumerate(CAMPOS, start=1):
        txt = f"Art. 38 num. {cpo['min']}" if cpo["min"] else ("Automático" if cpo["tipo"] == "auto" else "Buena práctica")
        cell = ws.cell(row=3, column=i, value=txt)
        cell.font = Font(name=FONT, size=8, italic=True, bold=bool(cpo["min"]), color="1F3864" if cpo["min"] else "7F7F7F")
        cell.alignment = Alignment(horizontal="center")
        ws.column_dimensions[get_column_letter(i)].width = cpo["w"]
        h = ws.cell(row=4, column=i, value=cpo["h"])
        if cpo.get("nota"):
            h.comment = Comment(cpo["nota"], "MSC")
    for j, (k, head, w) in enumerate(extra, start=n + 1):
        ws.cell(row=3, column=j, value="Automático").font = Font(name=FONT, size=8, italic=True, color="7F7F7F")
        ws.cell(row=3, column=j).alignment = Alignment(horizontal="center")
        ws.cell(row=4, column=j, value=head)
        ws.column_dimensions[get_column_letter(j)].width = w
    style_header(ws, 4, ncols)
    ws.row_dimensions[4].height = 58

    first, last = FIRST, FIRST - 1 + n_filas
    autos = {c["k"] for c in CAMPOS if c["tipo"] == "auto"} | {k for k, *_ in extra}
    for r in range(first, last + 1):
        f = formulas(r, M, rangos)
        for i, cpo in enumerate(CAMPOS, start=1):
            cell = ws.cell(row=r, column=i)
            cell.fill = AUTOF if cpo["k"] in autos else INPUT
            if cpo["tipo"] == "fecha":
                cell.number_format = "yyyy-mm-dd"
        for k in autos:
            cell = ws[f"{M[k]}{r}"]
            cell.value = f[k]
            cell.fill = AUTOF
        ws[f"{M['prox']}{r}"].number_format = "yyyy-mm-dd"
        for cc in range(1, ncols + 1):
            cell = ws.cell(row=r, column=cc)
            cell.border = BORDER
            cell.font = Font(name=FONT, size=9, bold=cc == n + 1)
            cell.alignment = Alignment(wrap_text=True, vertical="top")

    # datos de ejemplo (diccionarios por clave)
    for i, fila in enumerate(filas):
        for k, val in fila.items():
            if k in M and k not in autos:
                ws[f"{M[k]}{first + i}"] = val

    # validaciones
    def rng_col(k):
        return f"{M[k]}{first}:{M[k]}{last}"
    dv_base = DataValidation(type="list", formula1=f"=Listas!$A$2:$A${1 + len(BASES)}", allow_blank=True)
    dv_sino = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True)
    ws.add_data_validation(dv_base)
    ws.add_data_validation(dv_sino)
    for cpo in CAMPOS:
        t, k = cpo["tipo"], cpo["k"]
        if t == "base":
            dv_base.add(rng_col(k))
        elif t == "sino":
            dv_sino.add(rng_col(k))
        elif t == "opc":
            dv = DataValidation(type="list", formula1='"' + ",".join(cpo["ops"]) + '"', allow_blank=True)
            ws.add_data_validation(dv)
            dv.add(rng_col(k))
        elif t == "lista":
            multi = C.LISTAS[k]["tipo"] == "varios"
            dv = DataValidation(type="list", formula1=rangos[k], allow_blank=True, showErrorMessage=False,
                                showInputMessage=True, promptTitle="Lista u Otro",
                                prompt=("Elige de la lista o escribe tu propio texto. Varios valores: sepáralos con punto y coma."
                                        if multi else "Elige de la lista o escribe tu propio texto si es otro."))
            ws.add_data_validation(dv)
            dv.add(rng_col(k))

    est = M["_estado"]
    rng = f"A{first}:{get_column_letter(ncols)}{last}"
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'${est}{first}="Completo"'], fill=OKF))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'${est}{first}="Mínimo cumplido"'], fill=PatternFill("solid", fgColor="FFF2CC")))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'${est}{first}="Incompleto"'], fill=ALERTF))
    ws.conditional_formatting.add(f"{M['riesgo']}{first}:{M['riesgo']}{last}",
                                  FormulaRule(formula=[f'{M["riesgo"]}{first}="Alto"'], font=Font(color="C00000", bold=True)))
    ws.freeze_panes = f"C{first}"
    ws.auto_filter.ref = f"A4:{get_column_letter(ncols)}{last}"
    return first, last, M


def hoja_encargado(wb, n_filas=30):
    ws = wb.create_sheet("RAT encargado")
    ws["A1"] = "Registro del encargado del tratamiento (art. 44 RGLOPDP)"
    ws["A1"].font = Font(name=FONT, bold=True, size=13, color=AZUL)
    ws["A2"] = ("Úsala solo si la organización trata datos por cuenta de clientes. El encargado lleva el registro cuando "
                "el responsable está obligado. Contenido de buena práctica: confirmar con el texto del art. 44.")
    ws["A2"].font = Font(name=FONT, size=9, italic=True, color="7F7F7F")
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(C.CAMPOS_ENCARGADO) + 1)
    for i, (h, w, nota) in enumerate(C.CAMPOS_ENCARGADO, start=1):
        cell = ws.cell(row=4, column=i, value=h)
        if nota:
            cell.comment = Comment(nota, "MSC")
        ws.column_dimensions[get_column_letter(i)].width = w
    al = len(C.CAMPOS_ENCARGADO) + 1
    ws.cell(row=4, column=al, value="Alertas")
    ws.column_dimensions[get_column_letter(al)].width = 40
    style_header(ws, 4, al)
    ws.row_dimensions[4].height = 48
    dv = DataValidation(type="list", formula1='"Sí,No,Por confirmar"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"C5:C{4 + n_filas}")
    for r in range(5, 5 + n_filas):
        for c in range(1, al + 1):
            cell = ws.cell(row=r, column=c)
            cell.fill = AUTOF if c == al else INPUT
            cell.border = BORDER
            cell.font = Font(name=FONT, size=9)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=r, column=al, value=(
            f'=IF(A{r}="","",TRIM(IF(C{r}="","Confirma si el responsable está obligado. ","")'
            f'&IF(C{r}="No","No exigible por art. 44; puede llevarse como buena práctica. ","")'
            f'&IF(D{r}="","Faltan los tratamientos. ","")&IF(F{r}="","Sin contrato de encargo (art. 41 RGLOPDP). ","")'
            f'&IF(I{r}="","Faltan medidas. ","")&IF(J{r}="","Sin fecha de revisión. ","")))'))
    ws.freeze_panes = "B5"


def hoja_catalogo(wb):
    ws = wb.create_sheet("Catálogo")
    ws["A1"] = "Catálogo de actividades frecuentes (punto de partida, revisar en cada caso)"
    ws["A1"].font = Font(name=FONT, bold=True, size=13, color=AZUL)
    cols = [("actividad", "Actividad", 26), ("area", "Área", 16), ("finalidad", "Finalidad sugerida", 30),
            ("titulares", "Titulares", 22), ("datos", "Datos frecuentes", 34), ("base", "Base habitual", 22),
            ("plazo", "Plazo", 26), ("nota", "Advertencia", 50)]
    for i, (_, h, w) in enumerate(cols, start=1):
        ws.cell(row=3, column=i, value=h)
        ws.column_dimensions[get_column_letter(i)].width = w
    style_header(ws, 3, len(cols))
    for r, item in enumerate(C.CATALOGO, start=4):
        for i, (k, *_ ) in enumerate(cols, start=1):
            cell = ws.cell(row=r, column=i, value=item.get(k, "") or ("A definir según el caso" if k == "base" else ""))
            cell.font = Font(name=FONT, size=9, bold=i == 1)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = BORDER
    ws.freeze_panes = "B4"
    ws.sheet_view.showGridLines = False


def hoja_resumen(wb, first, last, M, ref_oblig):
    ws = wb.create_sheet("Resumen", 1)
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 44
    ws.column_dimensions["C"].width = 14
    ws["B2"] = "Estado del registro"
    ws["B2"].font = Font(name=FONT, bold=True, size=13, color=AZUL)
    col = lambda k: f"RAT!${M[k]}${first}:${M[k]}${last}"
    items = [
        ("Actividades registradas", f'=COUNTA({col("actividad")})'),
        ("Completas", f'=COUNTIF({col("_estado")},"Completo")'),
        ("Mínimo legal cumplido, con observaciones", f'=COUNTIF({col("_estado")},"Mínimo cumplido")'),
        ("Incompletas (falta contenido del art. 38)", f'=COUNTIF({col("_estado")},"Incompleto")'),
        ("Porcentaje con mínimo legal cumplido", '=IF(C4=0,0,(C5+C6)/C4)'),
        ("Riesgo orientativo alto", f'=COUNTIF({col("riesgo")},"Alto")'),
        ("Con categorías especiales", f'=COUNTIF({col("especial")},"Sí")'),
        ("Con transferencia internacional", f'=COUNTIF({col("transf")},"Sí")'),
        ("Basadas en interés legítimo", f'=COUNTIF({col("base")},"Interés legítimo")'),
        ("Encargados sin contrato completo", f'=COUNTIFS({col("enc")},"<>",{col("enc")},"<>Ninguno",{col("contrato")},"<>Sí, con todos")'),
        ("Revisiones vencidas", f'=COUNTIFS({col("prox")},"<"&TODAY(),{col("prox")},"<>")'),
        ("Hoja Responsable (art. 38 num. 1)", '=IF(OR(Responsable!C4="",Responsable!C8=""),"Incompleta","Completa")'),
        ("¿Obligado a llevar el RAT?", "=" + ref_oblig),
    ]
    for i, (label, f) in enumerate(items, start=4):
        ws.cell(row=i, column=2, value=label).font = Font(name=FONT, size=10)
        c = ws.cell(row=i, column=3, value=f)
        c.font = Font(name=FONT, size=10, bold=True)
        c.alignment = Alignment(horizontal="center")
        c.border = BORDER
    ws["C8"].number_format = "0%"
    firma(ws, 4 + len(items) + 2)
    ws.sheet_view.showGridLines = False


def firma(ws, r0):
    ws.column_dimensions["D"].width = 4
    ws.column_dimensions["E"].width = 30
    ws.column_dimensions["F"].width = 40
    ws.cell(row=r0, column=2, value="FIRMA DE RESPONSABILIDAD").font = Font(name=FONT, bold=True, size=11, color=AZUL)
    filas = [
        ("Elaborado por", "Abg. Mariano X. Macías Sánchez", "Revisado y aprobado por", ""),
        ("Cargo", "Consultor en Protección de Datos Personales", "Cargo", ""),
        ("Matrícula / registro", "Matrícula profesional 09-2022-736", "Responsable", "=IF(Responsable!C4=\"\",\"\",Responsable!C4)"),
        ("Firma", "", "Firma", ""),
        ("Fecha", "", "Fecha", ""),
    ]
    for i, (l1, v1, l2, v2) in enumerate(filas, start=r0 + 1):
        ws.cell(row=i, column=2, value=l1).font = Font(name=FONT, size=10, bold=True)
        c = ws.cell(row=i, column=3, value=v1)
        ws.cell(row=i, column=5, value=l2).font = Font(name=FONT, size=10, bold=True)
        d = ws.cell(row=i, column=6, value=v2)
        for cell in (c, d):
            cell.font = Font(name=FONT, size=10, color="008000" if str(cell.value).startswith("=") else "0000FF")
            cell.border = BORDER
            if not str(cell.value).startswith("="):
                cell.fill = INPUT
        if l1 == "Firma":
            ws.row_dimensions[i].height = 42
    ws.column_dimensions["C"].width = 40


D = datetime.date
# Fila de muestra de la plantilla vacía: un caso completo que el usuario reemplaza.
EJEMPLO_UNICO = [{
    "id": "T-01", "actividad": "Gestión de nómina y personal", "area": "Talento Humano",
    "propietario": "[Cargo del jefe de Talento Humano]", "descripcion": "Pago de remuneraciones, afiliación y expedientes del personal",
    "finalidad": "Cumplir obligaciones laborales y de seguridad social; Cumplir obligaciones tributarias",
    "base": "Obligación legal", "info": "Comunicación interna al personal",
    "titulares": "Trabajadores", "volumen": "Menos de 100",
    "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Financieros y bancarios; Laborales (cargo, remuneración)",
    "especial": "No", "nna": "No", "origen": "Del propio titular",
    "dest": "IESS; SRI; Ministerio del Trabajo; Entidades bancarias", "enc": "Software contable o de nómina",
    "contrato": "Sí, con todos", "transf": "No", "perfiles": "No",
    "plazo": "[Plazo legal aplicable y su fundamento]",
    "medidas": "Perfiles de acceso por rol; Respaldos periódicos; Acuerdos de confidencialidad con el personal",
    "sistemas": "Software de nómina; Archivo físico", "eipd": "No",
    "alta": D(2026, 11, 7), "rev": D(2026, 11, 7),
}]

# Clínica dental ficticia: T-01 y T-02 completas; T-03 a T-07 con errores intencionales para capacitación.
EJEMPLO_CLINICA = [
    {"id": "T-01", "actividad": "Atención de salud / historias clínicas", "area": "Dirección médica",
     "propietario": "Director médico", "descripcion": "Registro de la atención odontológica y seguimiento del tratamiento",
     "finalidad": "Prestación de servicios odontológicos y seguimiento del tratamiento",
     "base": "Ejecución de contrato o medidas precontractuales",
     "exc26": "[Excepción del art. 26 LOPDP aplicable a datos de salud]",
     "info": "Aviso de privacidad en el formulario o punto de recogida",
     "titulares": "Pacientes", "volumen": "De 1.001 a 10.000",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Salud; Niñas, niños y adolescentes",
     "especial": "Sí", "nna": "Sí", "origen": "Del propio titular",
     "dest": "Laboratorios dentales; Aseguradoras", "enc": "Proveedor de nube u hosting", "contrato": "Sí, con todos",
     "transf": "Sí", "pais": "Estados Unidos", "tgar": "Cláusulas contractuales con el receptor", "perfiles": "No",
     "plazo": "[Plazo según normativa sanitaria aplicable]",
     "medidas": "Perfiles de acceso por rol; Cifrado de información; Bitácora de accesos; Acuerdos de confidencialidad con el personal",
     "sistemas": "Sistema clínico o académico; Archivo físico", "eipd": "Sí", "eipdref": "EI-2026-01",
     "alta": D(2026, 3, 1), "rev": D(2026, 11, 1)},
    {"id": "T-02", "actividad": "Agenda de citas", "area": "Atención al cliente", "propietario": "Coordinador de recepción",
     "finalidad": "Programar y recordar citas", "base": "Ejecución de contrato o medidas precontractuales",
     "info": "Aviso de privacidad en el formulario o punto de recogida",
     "titulares": "Pacientes", "volumen": "De 1.001 a 10.000", "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección)",
     "especial": "No", "nna": "No", "origen": "Del propio titular", "dest": "Ninguno",
     "enc": "Plataforma de correo masivo o mensajería", "contrato": "Sí, con todos", "transf": "No", "perfiles": "No",
     "plazo": "Mientras sea paciente activo y un año después", "medidas": "Usuario y contraseña; Perfiles de acceso por rol",
     "sistemas": "Sistema clínico o académico; WhatsApp o mensajería", "eipd": "No",
     "alta": D(2026, 3, 1), "rev": D(2026, 11, 1)},
    # Error: interés legítimo sin ponderación, sin medidas, sin contrato con la empresa de seguridad
    {"id": "T-03", "actividad": "Videovigilancia", "area": "Seguridad física", "propietario": "Administrador",
     "finalidad": "Seguridad de personas e instalaciones", "base": "Interés legítimo",
     "info": "Cartel informativo (videovigilancia)", "titulares": "Pacientes; Visitantes; Trabajadores",
     "volumen": "De 1.001 a 10.000", "datos": "Imagen o video", "especial": "No", "nna": "Sí",
     "origen": "Captación automática (cámaras, sitio web)",
     "dest": "Autoridades judiciales o policiales (por requerimiento)", "enc": "Empresa de seguridad", "contrato": "No",
     "transf": "No", "perfiles": "No", "plazo": "30 días salvo incidente", "sistemas": "Grabador de cámaras (DVR/NVR)",
     "alta": D(2026, 3, 1), "rev": D(2026, 11, 1)},
    # Error: mezcla publicidad con atención, sin destinatarios, transferencia sin país ni garantía, revisión vencida
    {"id": "T-04", "actividad": "Marketing y publicidad", "area": "Comercial / Ventas",
     "finalidad": "Enviar publicidad y promociones; Atender solicitudes y reclamos",
     "base": "Consentimiento del titular", "titulares": "Pacientes; Potenciales clientes",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección)", "especial": "No", "nna": "No",
     "origen": "Del propio titular", "enc": "Plataforma de correo masivo o mensajería", "contrato": "Con algunos",
     "transf": "Sí", "perfiles": "Sí", "plazo": "Hasta que el titular revoque su consentimiento",
     "medidas": "Doble confirmación de suscripción; enlace de baja", "alta": D(2024, 6, 1), "rev": D(2025, 1, 15)},
    # Error: cargas familiares (NNA) sin marcar, plazo genérico, sin responsable interno
    {"id": "T-05", "actividad": "Gestión de nómina y personal", "area": "Talento Humano",
     "finalidad": "Cumplir obligaciones laborales y de seguridad social", "base": "Obligación legal",
     "info": "Comunicación interna al personal", "titulares": "Trabajadores; Cargas familiares de trabajadores",
     "volumen": "Menos de 100",
     "datos": "Identificación (nombre, cédula); Financieros y bancarios; Laborales (cargo, remuneración); Niñas, niños y adolescentes",
     "especial": "No", "nna": "No", "origen": "Del propio titular", "dest": "IESS; SRI; Ministerio del Trabajo; Entidades bancarias",
     "enc": "Contador o estudio contable externo", "contrato": "Sí, con todos", "transf": "No", "perfiles": "No",
     "plazo": "Plazo fijado por la normativa laboral o de seguridad social (indicar)",
     "medidas": "Cifrado de información; Perfiles de acceso por rol", "sistemas": "Software de nómina",
     "alta": D(2026, 3, 1), "rev": D(2026, 11, 1)},
    # Error: falta plazo, no se informa al titular, finalidad genérica
    {"id": "T-06", "actividad": "Selección de personal", "area": "Talento Humano", "propietario": "Jefe de Talento Humano",
     "finalidad": "Ejecutar el contrato o prestar el servicio", "base": "Ejecución de contrato o medidas precontractuales",
     "info": "No se informa aún", "titulares": "Postulantes", "volumen": "Menos de 100",
     "datos": "Identificación (nombre, cédula); Contacto (teléfono, correo, dirección); Académicos",
     "especial": "No", "nna": "No", "origen": "Del propio titular", "dest": "Ninguno", "enc": "Ninguno",
     "transf": "No", "perfiles": "No", "medidas": "Perfiles de acceso por rol", "sistemas": "Correo electrónico",
     "alta": D(2026, 3, 1), "rev": D(2026, 11, 1)},
    # Error: dato biométrico sin excepción del art. 26 ni análisis de evaluación de impacto
    {"id": "T-07", "actividad": "Control de asistencia (reloj o biométrico)", "area": "Talento Humano",
     "propietario": "Jefe de Talento Humano", "finalidad": "Controlar la asistencia", "base": "Obligación legal",
     "info": "Comunicación interna al personal", "titulares": "Trabajadores", "volumen": "Menos de 100",
     "datos": "Identificación (nombre, cédula); Biométricos (huella, rostro)", "especial": "Sí", "nna": "No",
     "origen": "Del propio titular", "dest": "Ninguno", "enc": "Ninguno", "transf": "No", "perfiles": "No",
     "plazo": "Durante la relación laboral", "medidas": "Usuario y contraseña", "sistemas": "Reloj biométrico",
     "alta": D(2026, 3, 1), "rev": D(2026, 11, 1)},
]

OBLIG_CLINICA = {
    "rol": "Responsable", "trab": 25, "h_nomina": "Sí", "h_clientes": "Sí", "h_visitas": "Sí", "h_publicidad": "Sí",
    "e_salud": "Sí", "e_bio": "No", "e_nna": "Sí", "e_disc": "No", "e_sens": "No",
    "r_perfiles": "No", "r_observacion": "No", "r_escala": "No", "r_financieros": "No", "r_geo": "No",
}

DATOS_CLINICA = {
    "Razón social / nombre": "Clínica Dental Ficticia Sonrisas S.A. (EJEMPLO)",
    "RUC": "[RUC]",
    "Dirección": "Av. Ejemplo 123, Guayaquil",
    "Correo de atención al titular": "privacidad@ejemplo.ec",
    "Teléfono": "[TELÉFONO]",
    "Representante legal": "[NOMBRE DEL REPRESENTANTE LEGAL]",
    "Sector o actividad económica": "Servicios odontológicos",
    "Delegado de Protección de Datos (DPD)": "[NOMBRE DEL DPD]",
    "Correo del DPD": "dpd@ejemplo.ec",
}


def build(path, filas, datos, oblig=None):
    wb = Workbook()
    hoja_instrucciones(wb)
    ref_oblig = hoja_obligado(wb, oblig)
    hoja_responsable(wb, datos)
    rangos = hoja_listas(wb)
    first, last, M = hoja_rat(wb, filas, rangos)
    hoja_encargado(wb)
    hoja_catalogo(wb)
    hoja_resumen(wb, first, last, M, ref_oblig)
    wb.save(path)
    print("OK", path)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    build(OUT / "plantilla-RAT.xlsx", EJEMPLO_UNICO, {})
    build(OUT / "ejemplo-RAT-ficticio.xlsx", EJEMPLO_CLINICA, DATOS_CLINICA, OBLIG_CLINICA)
