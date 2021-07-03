#!/usr/bin/env python3

import urllib.request

datasource = 'https://pavelmayer.de/covid/risks/data.csv'
delimiter = ','
fieldname_7tage_inzidenz = 'InzidenzFallNeu_7TageSumme'
fieldname_landkreis = 'Landkreis'
fieldname_meldung = 'MeldeDay'
staedte = ['SK Bochum', 'SK Dortmund', 'SK Herne', 'SK Essen', 'LK Recklinghausen']
steps = '▁▂▃▄▅▆▇█'

lines = urllib.request.urlopen(datasource).readlines()

headline = str(lines[0]).split(delimiter)
index_7tage_inzidenz = headline.index(fieldname_7tage_inzidenz)
index_landkreis = headline.index(fieldname_landkreis)

# mapping places to incidence
city_incidence = {}
# iterating and ignoring first line (headline)
for line in lines[1:]:
    line_splitted = str(line).split(delimiter)
    landkreis = line_splitted[index_landkreis]
    siebenT_inzidenz = line_splitted[index_7tage_inzidenz]
    city_incidence[landkreis] = float(siebenT_inzidenz)

# output configured places
max_width = 14
print('Stadt         \tInfizierte/100kEinw. in 7 Tagen\n')
for stadt in staedte:
    inzidenz = city_incidence[stadt]
    inzidenz_r = round(inzidenz, 1)
    symbol = int(inzidenz/10) * '*'
    #symbol = steps[int(inzidenz/10)]
    print(
        f'{stadt[:max_width]}\t{inzidenz_r} \t{symbol}')
