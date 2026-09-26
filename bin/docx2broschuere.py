#!/usr/bin/env python3
"""
Erzeugt aus einer DOCX- (oder PDF-)Datei mit 4 A4-Seiten ein PDF für eine
A3-Broschüre (ein Blatt A3, einmal gefaltet).

Ergebnis: 2 Seiten A3 quer
  Seite 1 (innen):  A4-Seiten 2 | 3
  Seite 2 (außen):  A4-Seiten 4 | 1

Drucken: A3, beidseitig, Wenden an der KURZEN Kante.

Voraussetzungen unter WSL (Ubuntu):
  sudo apt install libreoffice-writer python3-pypdf python3-click

Aufruf:
  docx2broschuere.py /mnt/c/Users/.../flyer.docx [ausgabe.pdf]
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import click
from pypdf import PdfReader, PdfWriter, Transformation

A3_QUER = (1190.55, 841.89)
LAYOUT = [(2, 3), (4, 1)]


def einpassen(breite, hoehe, ziel_breite, ziel_hoehe):
    """Skalierung und Versatz, um eine Seite zentriert in ein Feld einzupassen.

    >>> einpassen(595.28, 841.89, 595.275, 841.89)
    (0.99999, 0.0, 0.0)
    >>> einpassen(612, 792, 595.275, 841.89)
    (0.97267, 0.0, 35.77)
    """
    faktor = min(ziel_breite / breite, ziel_hoehe / hoehe)
    dx = (ziel_breite - breite * faktor) / 2
    dy = (ziel_hoehe - hoehe * faktor) / 2
    return round(faktor, 5), round(dx, 2), round(dy, 2)


def docx_zu_pdf(docx, zielordner):
    soffice = shutil.which('soffice') or shutil.which('libreoffice')
    if not soffice:
        sys.exit('LibreOffice fehlt: sudo apt install libreoffice-writer')
    subprocess.run([soffice, '--headless', '--convert-to', 'pdf',
                    '--outdir', str(zielordner), str(docx)],
                   check=True, stdout=subprocess.DEVNULL)
    return Path(zielordner) / (docx.stem + '.pdf')


def broschuere(pdf, ausgabe):
    seiten = PdfReader(pdf).pages
    if len(seiten) != 4:
        sys.exit(f'Erwartet 4 Seiten, gefunden: {len(seiten)}')

    feld_breite = A3_QUER[0] / 2
    writer = PdfWriter()
    for links, rechts in LAYOUT:
        blatt = writer.add_blank_page(*A3_QUER)
        for spalte, nr in enumerate((links, rechts)):
            seite = seiten[nr - 1]
            faktor, dx, dy = einpassen(float(seite.mediabox.width),
                                       float(seite.mediabox.height),
                                       feld_breite, A3_QUER[1])
            t = (Transformation()
                 .translate(-float(seite.mediabox.left),
                            -float(seite.mediabox.bottom))
                 .scale(faktor)
                 .translate(spalte * feld_breite + dx, dy))
            blatt.merge_transformed_page(seite, t)
    with open(ausgabe, 'wb') as f:
        writer.write(f)


@click.command()
@click.argument('eingabe', type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument('ausgabe', required=False, type=click.Path(dir_okay=False, path_type=Path))
def main(eingabe, ausgabe):
    ausgabe = ausgabe or eingabe.with_name(eingabe.stem + '_broschuere.pdf')
    with tempfile.TemporaryDirectory() as tmp:
        pdf = eingabe if eingabe.suffix.lower() == '.pdf' else docx_zu_pdf(eingabe, tmp)
        broschuere(pdf, ausgabe)
    print(f'{ausgabe} erstellt. Drucken: A3, beidseitig, Wenden an kurzer Kante.')


if __name__ == '__main__':
    main()
