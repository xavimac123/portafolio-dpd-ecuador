#!/usr/bin/env bash
# Exporta las plantillas Markdown de los kits a Word (.docx), con firma de responsabilidad al final.
# Uso: bash scripts/exportar_docx.sh            (con firma)
#      SIN_FIRMA=1 bash scripts/exportar_docx.sh (sin firma)
set -euo pipefail
cd "$(dirname "$0")/.."
FIRMA=scripts/firma-responsabilidad.md
for dir in 02-kit-plantillas 03-kit-vulneraciones; do
  mkdir -p "$dir/docx"
  for f in "$dir"/*.md; do
    name=$(basename "$f" .md)
    [ "$name" = "README" ] && continue
    if [ -n "${SIN_FIRMA:-}" ]; then
      pandoc "$f" -o "$dir/docx/$name.docx"
    else
      cat "$f" "$FIRMA" | pandoc -f markdown -o "$dir/docx/$name.docx"
    fi
    echo "OK $dir/docx/$name.docx"
  done
done
