#!/usr/bin/env python3
'''
Fetch corona incidence for a city in NRW and create an svg file that shows the
incidence in text form.
'''

from urllib.request import urlopen

template = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg">
  <text x="0" y="0" dy="20">{incidence}</text>
</svg>
"""

city_id = 5911 # Bochum
datasource=f'https://www.lzg.nrw.de/covid19/daten/covid19_{city_id}.csv'
fieldname_7day_incidence = 'rateM7Tage'  # oder rateE7Tage
filename = str(city_id)+'.svg'

def main():
  with urlopen(datasource) as response:
      lines = response.readlines()
      header = str(lines[0]).split(',')
      index_7day_incidence = header.index(fieldname_7day_incidence)
      incidence = float(
              str(lines[-1]).split(',')[index_7day_incidence])
      incdence_rounded = round(incidence, ndigits=1)

      print(f'Writing incidence for city id {city_id} to {filename}')
      with open(filename, 'wt') as f:
          f.write(template.format(incidence=incdence_rounded))
 
if __name__ == '__main__':
  main()
