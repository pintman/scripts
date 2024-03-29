#!/usr/bin/env python3

import requests

city_ids = { 
    "Bochum":5911, 
    "Dortmund":5913, 
    "Herne":5916, 
    "Essen":5113, 
    "Recklinghausen":5562 
    }

datasource='https://www.lzg.nrw.de/covid19/daten/covid19_{stadt}.csv'

# header:
# kreis,datumstd,datum,anzahlM,anzahlE,anzahlEM,verstorben,verstorbenE,verstorbenM,hospitalisiert,genesen,r,anzahlMKumuliert,anzahlEKumuliert,hospitalisiertKumuliert,verstorbenKumuliert,verstorbenEKumuliert,verstorbenMKumuliert,genesenKumuliert,krankKumuliert,anzahlM7Tage,anzahlE7Tage,verstorben7Tage,verstorbenE7Tage,verstorbenM7Tage,hospitalisiert7Tage,rateMKumuliert,rateEKumuliert,anteilVerstorbenM,rateVerstorbenKumuliert,anteilVerstorbenEKumuliert,anteilVerstorbenMKumuliert,rateM7Tage,rateE7Tage,rateVerstorben7Tage,anteilVerstorbenE7Tage,anteilVerstorbenM7Tage,anzahlMKumuliertVortag,rateM7TageVortag,verstorbenKumuliertVortag,anzahlMA00,anzahlMA10,anzahlMA20,anzahlMA30,anzahlMA40,anzahlMA50,anzahlMA60,anzahlMA70,anzahlMA80,anzahlMA90,anzahlMA00M,anzahlMA10M,anzahlMA20M,anzahlMA30M,anzahlMA40M,anzahlMA50M,anzahlMA60M,anzahlMA70M,anzahlMA80M,anzahlMA90M,anzahlMAGM,anzahlMA00W,anzahlMA10W,anzahlMA20W,anzahlMA30W,anzahlMA40W,anzahlMA50W,anzahlMA60W,anzahlMA70W,anzahlMA80W,anzahlMA90W,anzahlMAGW,anzahlMA00D,anzahlMA10D,anzahlMA20D,anzahlMA30D,anzahlMA40D,anzahlMA50D,anzahlMA60D,anzahlMA70D,anzahlMA80D,anzahlMA90D,anzahlMAGD,hospitalisiertA00,hospitalisiertA10,hospitalisiertA20,hospitalisiertA30,hospitalisiertA40,hospitalisiertA50,hospitalisiertA60,hospitalisiertA70,hospitalisiertA80,hospitalisiertA90,hospitalisiertA00M,hospitalisiertA10M,hospitalisiertA20M,hospitalisiertA30M,hospitalisiertA40M,hospitalisiertA50M,hospitalisiertA60M,hospitalisiertA70M,hospitalisiertA80M,hospitalisiertA90M,hospitalisiertAGM,hospitalisiertA00W,hospitalisiertA10W,hospitalisiertA20W,hospitalisiertA30W,hospitalisiertA40W,hospitalisiertA50W,hospitalisiertA60W,hospitalisiertA70W,hospitalisiertA80W,hospitalisiertA90W,hospitalisiertAGW,verstorbenA00,verstorbenA10,verstorbenA20,verstorbenA30,verstorbenA40,verstorbenA50,verstorbenA60,verstorbenA70,verstorbenA80,verstorbenA90,verstorbenA00M,verstorbenA10M,verstorbenA20M,verstorbenA30M,verstorbenA40M,verstorbenA50M,verstorbenA60M,verstorbenA70M,verstorbenA80M,verstorbenA90M,verstorbenAGM,verstorbenA00W,verstorbenA10W,verstorbenA20W,verstorbenA30W,verstorbenA40W,verstorbenA50W,verstorbenA60W,verstorbenA70W,verstorbenA80W,verstorbenA90W,verstorbenAGW,anzahlMA00Kumuliert,anzahlMA10Kumuliert,anzahlMA20Kumuliert,anzahlMA30Kumuliert,anzahlMA40Kumuliert,anzahlMA50Kumuliert,anzahlMA60Kumuliert,anzahlMA70Kumuliert,anzahlMA80Kumuliert,anzahlMA90Kumuliert,anzahlMA00MKumuliert,anzahlMA10MKumuliert,anzahlMA20MKumuliert,anzahlMA30MKumuliert,anzahlMA40MKumuliert,anzahlMA50MKumuliert,anzahlMA60MKumuliert,anzahlMA70MKumuliert,anzahlMA80MKumuliert,anzahlMA90MKumuliert,anzahlMAGMKumuliert,anzahlMA00WKumuliert,anzahlMA10WKumuliert,anzahlMA20WKumuliert,anzahlMA30WKumuliert,anzahlMA40WKumuliert,anzahlMA50WKumuliert,anzahlMA60WKumuliert,anzahlMA70WKumuliert,anzahlMA80WKumuliert,anzahlMA90WKumuliert,anzahlMAGWKumuliert,anzahlMA00DKumuliert,anzahlMA10DKumuliert,anzahlMA20DKumuliert,anzahlMA30DKumuliert,anzahlMA40DKumuliert,anzahlMA50DKumuliert,anzahlMA60DKumuliert,anzahlMA70DKumuliert,anzahlMA80DKumuliert,anzahlMA90DKumuliert,anzahlMAGDKumuliert,hospitalisiertA00Kumuliert,hospitalisiertA10Kumuliert,hospitalisiertA20Kumuliert,hospitalisiertA30Kumuliert,hospitalisiertA40Kumuliert,hospitalisiertA50Kumuliert,hospitalisiertA60Kumuliert,hospitalisiertA70Kumuliert,hospitalisiertA80Kumuliert,hospitalisiertA90Kumuliert,hospitalisiertA00MKumuliert,hospitalisiertA10MKumuliert,hospitalisiertA20MKumuliert,hospitalisiertA30MKumuliert,hospitalisiertA40MKumuliert,hospitalisiertA50MKumuliert,hospitalisiertA60MKumuliert,hospitalisiertA70MKumuliert,hospitalisiertA80MKumuliert,hospitalisiertA90MKumuliert,hospitalisiertAGMKumuliert,hospitalisiertA00WKumuliert,hospitalisiertA10WKumuliert,hospitalisiertA20WKumuliert,hospitalisiertA30WKumuliert,hospitalisiertA40WKumuliert,hospitalisiertA50WKumuliert,hospitalisiertA60WKumuliert,hospitalisiertA70WKumuliert,hospitalisiertA80WKumuliert,hospitalisiertA90WKumuliert,hospitalisiertAGWKumuliert,verstorbenA00Kumuliert,verstorbenA10Kumuliert,verstorbenA20Kumuliert,verstorbenA30Kumuliert,verstorbenA40Kumuliert,verstorbenA50Kumuliert,verstorbenA60Kumuliert,verstorbenA70Kumuliert,verstorbenA80Kumuliert,verstorbenA90Kumuliert,verstorbenA00MKumuliert,verstorbenA10MKumuliert,verstorbenA20MKumuliert,verstorbenA30MKumuliert,verstorbenA40MKumuliert,verstorbenA50MKumuliert,verstorbenA60MKumuliert,verstorbenA70MKumuliert,verstorbenA80MKumuliert,verstorbenA90MKumuliert,verstorbenAGMKumuliert,verstorbenA00WKumuliert,verstorbenA10WKumuliert,verstorbenA20WKumuliert,verstorbenA30WKumuliert,verstorbenA40WKumuliert,verstorbenA50WKumuliert,verstorbenA60WKumuliert,verstorbenA70WKumuliert,verstorbenA80WKumuliert,verstorbenA90WKumuliert,verstorbenAGWKumuliert,anzahlMA007Tage,anzahlMA107Tage,anzahlMA207Tage,anzahlMA307Tage,anzahlMA407Tage,anzahlMA507Tage,anzahlMA607Tage,anzahlMA707Tage,anzahlMA807Tage,anzahlMA907Tage,anzahlMA00M7Tage,anzahlMA10M7Tage,anzahlMA20M7Tage,anzahlMA30M7Tage,anzahlMA40M7Tage,anzahlMA50M7Tage,anzahlMA60M7Tage,anzahlMA70M7Tage,anzahlMA80M7Tage,anzahlMA90M7Tage,anzahlMA00W7Tage,anzahlMA10W7Tage,anzahlMA20W7Tage,anzahlMA30W7Tage,anzahlMA40W7Tage,anzahlMA50W7Tage,anzahlMA60W7Tage,anzahlMA70W7Tage,anzahlMA80W7Tage,anzahlMA90W7Tage,rateMA00Kumuliert,rateMA10Kumuliert,rateMA20Kumuliert,rateMA30Kumuliert,rateMA40Kumuliert,rateMA50Kumuliert,rateMA60Kumuliert,rateMA70Kumuliert,rateMA80Kumuliert,rateMA90Kumuliert,rateMA00MKumuliert,rateMA10MKumuliert,rateMA20MKumuliert,rateMA30MKumuliert,rateMA40MKumuliert,rateMA50MKumuliert,rateMA60MKumuliert,rateMA70MKumuliert,rateMA80MKumuliert,rateMA90MKumuliert,rateMAGMKumuliert,rateMA00WKumuliert,rateMA10WKumuliert,rateMA20WKumuliert,rateMA30WKumuliert,rateMA40WKumuliert,rateMA50WKumuliert,rateMA60WKumuliert,rateMA70WKumuliert,rateMA80WKumuliert,rateMA90WKumuliert,rateMAGWKumuliert,rateVerstorbenA00Kumuliert,rateVerstorbenA10Kumuliert,rateVerstorbenA20Kumuliert,rateVerstorbenA30Kumuliert,rateVerstorbenA40Kumuliert,rateVerstorbenA50Kumuliert,rateVerstorbenA60Kumuliert,rateVerstorbenA70Kumuliert,rateVerstorbenA80Kumuliert,rateVerstorbenA90Kumuliert,rateVerstorbenA00MKumuliert,rateVerstorbenA10MKumuliert,rateVerstorbenA20MKumuliert,rateVerstorbenA30MKumuliert,rateVerstorbenA40MKumuliert,rateVerstorbenA50MKumuliert,rateVerstorbenA60MKumuliert,rateVerstorbenA70MKumuliert,rateVerstorbenA80MKumuliert,rateVerstorbenA90MKumuliert,rateVerstorbenAGMKumuliert,rateVerstorbenA00WKumuliert,rateVerstorbenA10WKumuliert,rateVerstorbenA20WKumuliert,rateVerstorbenA30WKumuliert,rateVerstorbenA40WKumuliert,rateVerstorbenA50WKumuliert,rateVerstorbenA60WKumuliert,rateVerstorbenA70WKumuliert,rateVerstorbenA80WKumuliert,rateVerstorbenA90WKumuliert,rateVerstorbenAGWKumuliert,anteilVerstorbenA00Kumuliert,anteilVerstorbenA10Kumuliert,anteilVerstorbenA20Kumuliert,anteilVerstorbenA30Kumuliert,anteilVerstorbenA40Kumuliert,anteilVerstorbenA50Kumuliert,anteilVerstorbenA60Kumuliert,anteilVerstorbenA70Kumuliert,anteilVerstorbenA80Kumuliert,anteilVerstorbenA90Kumuliert,anteilVerstorbenA00MKumuliert,anteilVerstorbenA10MKumuliert,anteilVerstorbenA20MKumuliert,anteilVerstorbenA30MKumuliert,anteilVerstorbenA40MKumuliert,anteilVerstorbenA50MKumuliert,anteilVerstorbenA60MKumuliert,anteilVerstorbenA70MKumuliert,anteilVerstorbenA80MKumuliert,anteilVerstorbenA90MKumuliert,anteilVerstorbenA00WKumuliert,anteilVerstorbenA10WKumuliert,anteilVerstorbenA20WKumuliert,anteilVerstorbenA30WKumuliert,anteilVerstorbenA40WKumuliert,anteilVerstorbenA50WKumuliert,anteilVerstorbenA60WKumuliert,anteilVerstorbenA70WKumuliert,anteilVerstorbenA80WKumuliert,anteilVerstorbenA90WKumuliert

delimiter = ','
fieldname_7tage_inzidenz = 'rateM7Tage'  # oder rateE7Tage
steps = '▁▂▃▄▅▆▇█'

def main():
    # mapping places to incidence
    city_incidence = {}
    headers= { 'Referer': 'https://www.lzg.nrw.de/covid19/covid19.html' }
    for city in city_ids:
        cid = city_ids[city]
        lines = requests.get(datasource.format(stadt=cid), headers=headers).text.split('\n')
        headline = str(lines[0]).split(delimiter)
        index_7tage_inzidenz = headline.index(fieldname_7tage_inzidenz)
        city_incidence[city] = float(
            str(lines[-2]).split(delimiter)[index_7tage_inzidenz])

    # output configured places
    max_width = 10
    print('Stadt         \tInfizierte/100kEinw. in 7 Tagen\n')
    for stadt in city_ids:
        inzidenz = city_incidence[stadt]
        inzidenz_r = round(inzidenz, 1)
        symbol = int(inzidenz/100) * '*'
        #symbol = steps[int(inzidenz/10)]
        print(
            f'{stadt[:max_width]}   \t{inzidenz_r} \t{symbol}')

if __name__ == '__main__':
    main()
    