#!/usr/bin/env python3

# write a program that can manipulate xlsx files.

# from https://claude.ai/chat/4799aaf8-88ae-4fcb-a05a-03250fa9ec13

"""
Quiz Grader - Bewertet einen Microsoft-Forms-Quiz-Export neu.

Bewertungsregeln:
  - Keine Antwort  →  0 Punkte
  - Richtig        → +1 Punkt
  - Falsch         → -1 Punkt

Die Datei enthält bereits eine Bepunktung durch Forms (1 = richtig, 0 = falsch/leer).
Dieses Script ersetzt falsche Antworten (0 + Antwort vorhanden) durch -1
und berechnet die Gesamtpunktzahl neu.

Verwendung:
    wahr_falsch_auswertung.py <eingabe.xlsx> [ausgabe.xlsx]
"""

import sys
import pandas as pd


def grade(input_path: str, output_path: str):
    df = pd.read_excel(input_path)

    # Alle "Punkte –" Spalten ermitteln
    punkte_cols = [c for c in df.columns if str(c).startswith("Punkte")]

    if not punkte_cols:
        print("⚠  Keine Punkte-Spalten gefunden. Vorhandene Spalten:")
        for c in df.columns:
            print(f"  {c}")
        sys.exit(1)

    print(f"{len(punkte_cols)} Punkte-Spalte(n) gefunden.")

    # Neubewertung: 0 + Antwort vorhanden → -1
    for pc in punkte_cols:
        answer_col = df.columns[df.columns.get_loc(pc) - 1]
        has_answer = df[answer_col].notna() & (df[answer_col].astype(str).str.strip() != "")
        df.loc[(df[pc] == 0) & has_answer, pc] = -1

    # Gesamtpunktzahl neu berechnen
    df["Gesamtpunktzahl"] = df[punkte_cols].sum(axis=1).clip(lower=0)

    df.to_excel(output_path, index=False)
    print(f"✅  Gespeichert: {output_path}")
    print()
    print(df[["Name", "Gesamtpunktzahl"]].to_string(index=False))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else inp.replace(".xlsx", "_bewertet.xlsx")
    grade(inp, out)

    
