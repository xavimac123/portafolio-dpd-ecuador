"""Genera la plantilla del Registro de Actividades de Tratamiento (RAT) y un ejemplo ficticio.

Uso: python scripts/generar_rat.py
Salida: 01-registro-tratamientos/plantilla-RAT.xlsx y ejemplo-RAT-ficticio.xlsx
"""
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

OUT = Path(__file__).resolve().parent.parent / "01-registro-tratamientos"

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

# (encabezado, ancho, numeral art. 38 RGLOPDP o None, nota)
COLS = [
    ("ID", 7, None, "Código interno, ej. T-01"),
    ("Actividad de tratamiento", 28, None, "Nombre corto: Nómina, Historias clínicas, Videovigilancia..."),
    ("Área responsable", 16, None, "Unidad interna a cargo"),
    ("Finalidades", 34, "num. 2", "Para qué se tratan los datos. Una finalidad concreta, no genérica."),
    ("Categorías de titulares", 22, "num. 4", "Pacientes, trabajadores, proveedores, usuarios web..."),
    ("Categorías de datos personales", 30, "num. 4", "Identificación, contacto, financieros, salud..."),
    ("¿Categorías especiales?", 12, None, "Sí si incluye datos sensibles, de salud, biométricos, etc."),
    ("¿Datos de niñas, niños y adolescentes?", 14, None, ""),
    ("Origen de los datos", 20, None, "Del propio titular, de terceros, de fuentes públicas"),
    ("Base legitimadora", 26, "num. 7", "Elegir de la lista (art. 7 LOPDP)"),
    ("Ref. evaluación de interés legítimo", 20, "num. 7", "Obligatoria si la base es interés legítimo (Res. SPDP-SPD-2025-0041-R)"),
    ("Categorías de destinatarios", 26, "num. 3", "A quién se comunican: IESS, SRI, aseguradoras..."),
    ("Encargados del tratamiento", 24, None, "Proveedores que tratan por cuenta del responsable (nube, nómina, TI)"),
    ("¿Elaboración de perfiles?", 12, "num. 5", ""),
    ("¿Transferencia internacional?", 13, "num. 6", ""),
    ("País y garantía de la transferencia", 24, "num. 6", "País destino y mecanismo que la habilita"),
    ("Plazo de conservación / supresión", 24, "num. 8", "Plazo o criterio y su fundamento"),
    ("Medidas técnicas, jurídicas, administrativas y organizativas", 34, "num. 9", "Descripción general"),
    ("Fecha de última revisión", 13, None, "AAAA-MM-DD"),
    ("Alertas", 46, None, "Automático: no editar"),
]


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
        ("Macías Sánchez Consultores · Herramienta 01 · v0.1", False, 10),
        ("", False, 10),
        ("Para qué sirve", True, 11),
        ("Documentar cada actividad de tratamiento con el contenido mínimo del art. 38 del Reglamento General a la LOPDP y detectar vacíos automáticamente.", False, 10),
        ("", False, 10),
        ("Cómo se usa", True, 11),
        ("1. Hoja 'Obligado': responde las preguntas; cada una tiene su explicación y la norma que la sustenta (arts. 38, 39 y 44 RGLOPDP).", False, 10),
        ("2. Hoja 'Responsable': datos de contacto del responsable, corresponsable y DPD (art. 38 num. 1).", False, 10),
        ("3. Hoja 'RAT': una fila por actividad. Las celdas amarillas tienen listas desplegables; si tu caso no está, escribe tu propio texto en la celda ('Otro').", False, 10),
        ("4. La columna 'Alertas' indica qué falta. Una fila está lista cuando dice 'Completo'.", False, 10),
        ("5. Hoja 'Resumen': estado general del registro.", False, 10),
        ("", False, 10),
        ("Leyenda", True, 11),
        ("Celda amarilla = dato a completar · Verde = fila completa · Naranja = fila con alertas", False, 10),
        ("La primera fila de la hoja RAT es un ejemplo ficticio: reemplázala o elimínala.", False, 10),
        ("", False, 10),
        ("Límites", True, 11),
        ("Las alertas revisan que los campos existan, no que su contenido sea jurídicamente correcto. La calificación de bases legitimadoras, plazos y medidas requiere análisis profesional.", False, 10),
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
        "Razón social / nombre", "RUC", "Dirección", "Correo de atención al titular", "Teléfono",
        "Corresponsable (si existe)", "Contacto del corresponsable",
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
    for j, (nombre, d) in enumerate(C.LISTAS.items(), start=2):
        L = get_column_letter(j)
        ws.cell(row=1, column=j, value=nombre).font = Font(name=FONT, bold=True)
        ops = d["opciones"] + [C.OTRO + " (escribir en la celda)"]
        for i, o in enumerate(ops, start=2):
            ws.cell(row=i, column=j, value=o).font = Font(name=FONT, size=10)
        ws.column_dimensions[L].width = 40
        rangos[nombre] = f"=Listas!${L}$2:${L}${1 + len(ops)}"
    ws.column_dimensions["A"].width = 50
    ws.sheet_state = "hidden"
    return rangos


def hoja_rat(wb, filas, rangos, n_filas=100):
    ws = wb.create_sheet("RAT")
    ncols = len(COLS)
    ws.cell(row=1, column=1, value="Registro de Actividades de Tratamiento").font = Font(name=FONT, bold=True, size=13, color=AZUL)
    # fila 2: numeral del art. 38
    for c, (_, width, numeral, nota) in enumerate(COLS, start=1):
        cell = ws.cell(row=2, column=c, value=f"Art. 38 {numeral}" if numeral else "")
        cell.font = Font(name=FONT, size=8, italic=True, color="7F7F7F")
        cell.alignment = Alignment(horizontal="center")
        ws.column_dimensions[get_column_letter(c)].width = width
    for c, (head, _, _, nota) in enumerate(COLS, start=1):
        cell = ws.cell(row=3, column=c, value=head)
        if nota:
            cell.comment = Comment(nota, "MSC")
    style_header(ws, 3, ncols)
    ws.row_dimensions[3].height = 48

    # columna auxiliar oculta para alertas
    aux = ncols + 1
    ws.cell(row=3, column=aux, value="aux")
    ws.column_dimensions[get_column_letter(aux)].hidden = True

    first, last = 4, 3 + n_filas
    for r in range(first, last + 1):
        for c in range(1, ncols):
            cell = ws.cell(row=r, column=c)
            cell.fill = INPUT
            cell.border = BORDER
            cell.font = Font(name=FONT, size=9)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        L = {name: get_column_letter(i) for i, (name, *_ ) in enumerate(COLS, start=1)}
        B, D, E, F, G, J, K, Lc, O, P, Q, R, S = (
            L["Actividad de tratamiento"], L["Finalidades"], L["Categorías de titulares"],
            L["Categorías de datos personales"], L["¿Categorías especiales?"], L["Base legitimadora"],
            L["Ref. evaluación de interés legítimo"], L["Categorías de destinatarios"],
            L["¿Transferencia internacional?"], L["País y garantía de la transferencia"],
            L["Plazo de conservación / supresión"],
            L["Medidas técnicas, jurídicas, administrativas y organizativas"], L["Fecha de última revisión"],
        )
        raw = (
            f'=IF({D}{r}="","Falta finalidad. ","")'
            f'&IF({E}{r}="","Faltan titulares. ","")'
            f'&IF({F}{r}="","Faltan categorías de datos. ","")'
            f'&IF({J}{r}="","Falta base legitimadora. ","")'
            f'&IF(AND({J}{r}="Interés legítimo",{K}{r}=""),"Interés legítimo sin evaluación de ponderación. ","")'
            f'&IF({Lc}{r}="","Faltan destinatarios. ","")'
            f'&IF(AND({O}{r}="Sí",{P}{r}=""),"Transferencia internacional sin país o garantía. ","")'
            f'&IF({Q}{r}="","Falta plazo de conservación. ","")'
            f'&IF({R}{r}="","Faltan medidas de seguridad. ","")'
            f'&IF({S}{r}="","Sin fecha de revisión. ","")'
            f'&IF({G}{r}="Sí","Revisar si requiere evaluación de impacto. ","")'
        )
        ws.cell(row=r, column=aux, value=raw)
        al = ws.cell(row=r, column=ncols)
        auxL = get_column_letter(aux)
        al.value = f'=IF({B}{r}="","",IF({auxL}{r}="","Completo",TRIM({auxL}{r})))'
        al.font = Font(name=FONT, size=9, bold=True)
        al.alignment = Alignment(wrap_text=True, vertical="top")
        al.border = BORDER

    # datos
    for i, fila in enumerate(filas):
        for c, val in enumerate(fila, start=1):
            ws.cell(row=first + i, column=c, value=val)

    # validaciones
    Lmap = {name: get_column_letter(i) for i, (name, *_ ) in enumerate(COLS, start=1)}
    dv_base = DataValidation(type="list", formula1=f"=Listas!$A$2:$A${1 + len(BASES)}", allow_blank=True)
    dv_sino = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True)
    ws.add_data_validation(dv_base)
    ws.add_data_validation(dv_sino)
    col = Lmap["Base legitimadora"]
    dv_base.add(f"{col}{first}:{col}{last}")
    # listas con "Otro": aceptan texto libre (sin mensaje de error)
    abiertas = {
        "Actividad de tratamiento": "actividad", "Área responsable": "area", "Finalidades": "finalidad",
        "Categorías de titulares": "titulares", "Categorías de datos personales": "datos", "Origen de los datos": "origen",
        "Categorías de destinatarios": "dest", "Encargados del tratamiento": "enc",
        "Plazo de conservación / supresión": "plazo",
        "Medidas técnicas, jurídicas, administrativas y organizativas": "medidas",
    }
    for head, key in abiertas.items():
        multi = C.LISTAS[key]["tipo"] == "varios"
        dv = DataValidation(type="list", formula1=rangos[key], allow_blank=True, showErrorMessage=False,
                            showInputMessage=True, promptTitle="Lista u Otro",
                            prompt=("Elige de la lista o escribe tu propio texto. Varios valores: sepáralos con punto y coma."
                                    if multi else "Elige de la lista o escribe tu propio texto si es otro."))
        ws.add_data_validation(dv)
        col = Lmap[head]
        dv.add(f"{col}{first}:{col}{last}")
    for name in ["¿Categorías especiales?", "¿Datos de niñas, niños y adolescentes?", "¿Elaboración de perfiles?", "¿Transferencia internacional?"]:
        col = Lmap[name]
        dv_sino.add(f"{col}{first}:{col}{last}")

    alert_col = get_column_letter(ncols)
    rng = f"A{first}:{alert_col}{last}"
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'${alert_col}{first}="Completo"'], fill=OKF))
    ws.conditional_formatting.add(rng, FormulaRule(formula=[f'AND(${alert_col}{first}<>"",${alert_col}{first}<>"Completo")'], fill=ALERTF))
    ws.freeze_panes = "C4"
    return first, last, alert_col


def hoja_resumen(wb, first, last, alert_col, ref_oblig):
    ws = wb.create_sheet("Resumen", 1)
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 44
    ws.column_dimensions["C"].width = 14
    ws["B2"] = "Estado del registro"
    ws["B2"].font = Font(name=FONT, bold=True, size=13, color=AZUL)
    rat = f"RAT!${alert_col}${first}:${alert_col}${last}"
    rat_b = f"RAT!$B${first}:$B${last}"
    items = [
        ("Actividades registradas", f'=COUNTA({rat_b})'),
        ("Actividades completas", f'=COUNTIF({rat},"Completo")'),
        ("Actividades con alertas", "=C4-C5"),
        ("Porcentaje completo", '=IF(C4=0,0,C5/C4)'),
        ("Con categorías especiales", f'=COUNTIF(RAT!$G${first}:$G${last},"Sí")'),
        ("Con transferencia internacional", f'=COUNTIF(RAT!$O${first}:$O${last},"Sí")'),
        ("Basadas en interés legítimo", f'=COUNTIF(RAT!$J${first}:$J${last},"Interés legítimo")'),
        ("¿Obligado a llevar el RAT?", "=" + ref_oblig),
    ]
    for i, (label, f) in enumerate(items, start=4):
        ws.cell(row=i, column=2, value=label).font = Font(name=FONT, size=10)
        c = ws.cell(row=i, column=3, value=f)
        c.font = Font(name=FONT, size=10, bold=True, color="008000" if "!" in f and "Obligado" in f else "000000")
        c.alignment = Alignment(horizontal="center")
        c.border = BORDER
    ws["C7"].number_format = "0%"
    firma(ws, 14)
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


EJEMPLO_UNICO = [[
    "T-01", "Gestión de nómina", "Talento Humano",
    "Pago de remuneraciones y cumplimiento de obligaciones laborales y de seguridad social",
    "Trabajadores", "Identificación, contacto, cuenta bancaria, remuneración",
    "No", "No", "Del propio titular", "Obligación legal", "",
    "IESS, SRI, Ministerio del Trabajo, banco pagador", "[Proveedor de software de nómina]",
    "No", "No", "", "[Plazo legal aplicable y su fundamento]",
    "Acceso restringido por roles, respaldo cifrado, acuerdos de confidencialidad", "2026-11-07",
]]

EJEMPLO_CLINICA = [
    ["T-01", "Historias clínicas", "Dirección médica",
     "Prestación de servicios odontológicos y seguimiento del tratamiento",
     "Pacientes", "Identificación, contacto, datos de salud, imágenes diagnósticas",
     "Sí", "Sí", "Del propio titular", "Ejecución de contrato o medidas precontractuales", "",
     "Laboratorios dentales, aseguradoras (con autorización)", "Proveedor de software clínico en la nube",
     "No", "Sí", "Estados Unidos — cláusulas contractuales con el proveedor",
     "[Plazo según normativa sanitaria aplicable]",
     "Control de acceso por perfil, cifrado en reposo, bitácora de accesos, confidencialidad del personal", "2026-11-01"],
    ["T-02", "Agenda de citas", "Recepción",
     "Programar y recordar citas", "Pacientes", "Nombre, teléfono, correo",
     "No", "No", "Del propio titular", "Ejecución de contrato o medidas precontractuales", "",
     "Ninguno", "Plataforma de mensajería para recordatorios",
     "No", "No", "", "Mientras sea paciente activo + 1 año",
     "Acceso con usuario y contraseña", "2026-11-01"],
    ["T-03", "Videovigilancia", "Administración",
     "Seguridad de personas e instalaciones", "Pacientes, visitantes, trabajadores", "Imagen",
     "No", "Sí", "Captación directa", "Interés legítimo", "",
     "Policía Nacional o Fiscalía ante requerimiento", "Empresa de seguridad",
     "No", "No", "", "30 días salvo incidente",
     "", "2026-11-01"],
    ["T-04", "Marketing por correo", "Comercial",
     "Envío de promociones y campañas de prevención", "Pacientes que aceptan", "Nombre, correo",
     "No", "No", "Del propio titular", "Consentimiento del titular", "",
     "", "Plataforma de email marketing",
     "Sí", "Sí", "",
     "Hasta revocatoria del consentimiento", "Doble confirmación de suscripción, enlace de baja", ""],
    ["T-05", "Nómina", "Talento Humano",
     "Pago de remuneraciones y obligaciones laborales", "Trabajadores",
     "Identificación, cuenta bancaria, remuneración, cargas familiares",
     "No", "Sí", "Del propio titular", "Obligación legal", "",
     "IESS, SRI, Ministerio del Trabajo, banco", "Contadora externa",
     "No", "No", "", "[Plazo legal aplicable]",
     "Carpeta cifrada, acceso solo de Talento Humano y contadora", "2026-11-01"],
    ["T-06", "Selección de personal", "Talento Humano",
     "Evaluar candidatos a vacantes", "Postulantes", "Identificación, contacto, experiencia, formación",
     "No", "No", "Del propio titular", "Ejecución de contrato o medidas precontractuales", "",
     "Ninguno", "",
     "No", "No", "", "",
     "Acceso restringido", "2026-11-01"],
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
    "Delegado de Protección de Datos (DPD)": "[NOMBRE DEL DPD]",
    "Correo del DPD": "dpd@ejemplo.ec",
}


def build(path, filas, datos, oblig=None):
    wb = Workbook()
    hoja_instrucciones(wb)
    ref_oblig = hoja_obligado(wb, oblig)
    hoja_responsable(wb, datos)
    rangos = hoja_listas(wb)
    first, last, alert_col = hoja_rat(wb, filas, rangos)
    hoja_resumen(wb, first, last, alert_col, ref_oblig)
    wb.save(path)
    print("OK", path)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    build(OUT / "plantilla-RAT.xlsx", EJEMPLO_UNICO, {})
    build(OUT / "ejemplo-RAT-ficticio.xlsx", EJEMPLO_CLINICA, DATOS_CLINICA, OBLIG_CLINICA)
