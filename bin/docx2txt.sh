#!/usr/bin/env bash
# Extrahiert den Text aus einer .docx-Datei via unzip.
# Nutzung: docx2txt.sh <datei.docx>
set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Nutzung: $(basename "$0") <datei.docx>" >&2
    exit 1
fi

unzip -p "$1" word/document.xml | sed 's/<[^>]*>/ /g'
