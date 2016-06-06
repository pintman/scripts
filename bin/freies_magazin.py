#!/usr/bin/python3
#
# Ein einfaches Skript, das die Ausgaben des Linux-Magazins "freies Magazin"
# nach einem Stichwort durchsucht. Es werden Titel und Zusammenfassungen der
# Artikel berücksichtigt.
# 
# Der folgende Beispielaufruf liefert alle Artikel, in den Python thematisiert wird.
#
# ./freies_magazin.py Python
#
# 
#

import xml.etree.ElementTree as ET
import urllib.request
import sys

base_url = "http://www.freiesmagazin.de/freiesmagazin.xml"
NS = "{urn:freiesmagazin}"

def suche(suchwort):
    """
    Durchsuche den Suchbaum ab root nach dem suchwort. Suche in summary und
    title von Artikeln.
    """
    xml = urllib.request.urlopen(base_url)
    tree = ET.parse(xml)
    root = tree.getroot()

    for issue in root.iter(NS+"issue"):
        number = issue.find(NS+"number").text

        for article in issue.iter(NS+"article"):
            summary = article.find(NS+"summary").text
            if summary is None:
                summary = ""
            title   = article.find(NS+"title").text
            if title is None:
                title = ""

            if  suchwort in summary or suchwort in title:
                url = issue.find(NS+"url").text
                print("%s (Ausgabe %s)\n%s" % (title, number, url))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ich brauche ein Suchwort.")
        exit(1)

    suchwort = ""
    for wort in sys.argv[1:]:
        suchwort += wort + " "

    suche(suchwort.strip())

