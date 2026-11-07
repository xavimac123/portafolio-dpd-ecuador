#!/usr/bin/env bash
# Exporta todas las plantillas Markdown de los kits a Word (.docx).
# Uso: bash scripts/exportar_docx.sh
set -euo pipefail
cd "$(dirname "$0")/.."
for dir in 02-kit-plantillas 03-kit-vulneraciones; do
  mkdir -p "$dir/docx"
  for f in "$dir"/*.md; do
    name=$(basename "$f" .md)
    [ "$name" = "README" ] && continue
    pandoc "$f" -o "$dir/docx/$name.docx"
    echo "OK $dir/docx/$name.docx"
  done
done
