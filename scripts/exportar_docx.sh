#!/usr/bin/env bash
# Exporta las plantillas Markdown de los kits a Word (.docx), con firma de responsabilidad al final.
# Uso: bash scripts/exportar_docx.sh            (con firma)
#      SIN_FIRMA=1 bash scripts/exportar_docx.sh (sin firma)
set -euo pipefail
cd "$(dirname "$0")/.."
FIRMA=scripts/firma-responsabilidad.md
for dir in 01-catalogo-servicios 02-honorarios 03-madurez 05-gran-escala 06-interes-legitimo 07-evaluacion-impacto 08-kit-plantillas 09-kit-vulneraciones; do
  mkdir -p "$dir/docx"
  for f in "$dir"/*.md; do
    name=$(basename "$f" .md)
    [ "$name" = "README" ] && continue
    # La proforma trae su propia firma; la solicitud de información, la carta de presentación y los correos van firmados por el consultor
    if [ -n "${SIN_FIRMA:-}" ] || [ "$name" = "proforma-servicios" ] || [ "$name" = "solicitud-informacion" ] || [ "$name" = "carta-presentacion" ] || [ "$name" = "correos-campana" ]; then
      pandoc "$f" -o "$dir/docx/$name.docx"
    else
      cat "$f" "$FIRMA" | pandoc -f markdown -o "$dir/docx/$name.docx"
    fi
    echo "OK $dir/docx/$name.docx"
  done
done
