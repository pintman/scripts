#!/usr/bin/env python3

import csv
import os
import tempfile


class Kontakt:
    def __init__(self, klasse, name, vorname, betrieb, ausbilder, mail):
        self.klasse = klasse
        self.name = name
        self.vorname = vorname
        self.betrieb = betrieb
        self.ausbilder = ausbilder
        self.ausbildermail = mail


def main():
    # read config file with fields:
    # klasse, name, vorname, betrieb, ausbilder, ausbildermail
    configfile = os.environ["HOME"] + "/.ausbilder-mail.csv"

    # read template with variables: schuelername, daten, ausbilder
    template_file = os.environ["HOME"] + "/.ausbilder-mail.tmpl"
    template = "".join(open(template_file).readlines())

    betreff = "Versäumter Unterricht {schuelername}"
    # read config into list Kontakte
    with open(configfile, "rt") as config:
        # read and remove the first line (header)
        rows = list(csv.reader(config, delimiter=";"))[1:]

    kontakte = []
    klassen = []
    for row in rows:
        kontakte.append(Kontakt(*row))

        # output name of a class the first time we see them
        if row[0] not in klassen:
            print(len(klassen), row[0])
            klassen.append(row[0])

    # Ask for class to be used.
    klasse = klassen[int(input("Klasse? "))]

    # Output of students of the chosen class
    for (i, kont) in enumerate(kontakte):
        if kont.klasse == klasse:
            print(i, kont.name, kont.vorname, "(" + kont.ausbilder + ")")

    # Ask for student and dates of absence
    schueler = kontakte[int(input("Schüler? "))]
    schueler_txt = schueler.vorname + " " + schueler.name
    daten = input("Fehltage? ")

    # create mail, temporary file of content, send mail and remove temp file.
    to = schueler.ausbildermail
    betreff = betreff.format(schuelername=schueler_txt)

    content = template.format(
        schuelername=schueler_txt, daten=daten, ausbilder=schueler.ausbilder)
    tmp_file = tempfile.NamedTemporaryFile(mode="wt", delete=False)
    tmp_file.write(content)
    tmp_file.close()

    mail_cmd = "mutt -b bakera@tbs1.de -s \"{betreff}\" -i {msg_file} {to}".format(
        betreff=betreff,
        to=to,
        msg_file=tmp_file.name)
    os.system(mail_cmd)
    os.remove(tmp_file.name)


if __name__ == "__main__":
    main()
