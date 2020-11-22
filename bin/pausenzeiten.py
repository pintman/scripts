#!/usr/bin/env python

import csv
import sys

COL_WIDTH = 20


def main():
if len(sys.argv) == 1:
    print('CSV-File mit Pausenzeiten angeben.')
    exit(1)

file = sys.argv[1]
pausen = list(csv.reader(open(file)))
print(len(pausen), 'Einträge eingelesen')

anwesenheit = {}
for id_,startzeit,_endzeit,mail,name,pause in pausen[1:]:
    anwesenheit[name] = (startzeit, pause)

print('NAME'.ljust(COL_WIDTH), 'STATUS'.ljust(COL_WIDTH), 'DATUM'.ljust(COL_WIDTH))
for name in anwesenheit:
    ende, status = anwesenheit[name]
    print(name.ljust(COL_WIDTH), status.ljust(COL_WIDTH), ende.ljust(COL_WIDTH))

if __name__ == "__main__":
    main()
