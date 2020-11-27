#!/usr/bin/env python3

import json
from urllib.request import urlopen

API = 'https://maps.nextbike.net/maps/nextbike-live.json?city=130'
PLACE_NAMES = ['Technische Berufliche Schule 1', 'Hauptbahnhof', 
               'Bochumer Fenster / Massenbergstr.']

def fetch_bochum():
    js = json.load(urlopen(API))

    assert len(js['countries']) == 1, 'More than one country found'
    ger = js['countries'][0]

    assert len(ger['cities']) == 1, 'More than one City found'
    bochum = ger['cities'][0]
    assert bochum['alias'] == 'bochum'

    return bochum

def main():
    print('LEIH-FARHRRÄDER AN STANDORTEN DER BOCHUMER INNENSTADT')
    for place in fetch_bochum()['places']:
        if place['name'] in PLACE_NAMES:
            print(f'{place["name"]}: {len(place["bike_list"])}')

if __name__ == "__main__":
    main()


'''
sample output:

{
  "countries": [
    {
      "lat": 51.4818,
      "lng": 7.21966,
      "zoom": 9,
      "name": "metropolradruhr Bochum",
      "hotline": "00493069205046",
      "domain": "ms",
      "language": "de",
      "email": "kundenservice@nextbike.de",
      "timezone": "Europe/Berlin",
      "currency": "EUR",
      "country_calling_code": "+49",
      "system_operator_address": "nextbike GmbH, Erich-Zeigner Allee 69-73, 04229 Leipzig",
      "country": "DE",
      "country_name": "Germany",
      "terms": "https://www.nextbike.de/de/agb/#202006",
      "policy": "https://www.nextbike.de/datenschutz/",
      "website": "https://www.metropolradruhr.de/de/",
      "show_bike_types": false,
      "show_bike_type_groups": false,
      "show_free_racks": false,
      "booked_bikes": 2,
      "set_point_bikes": 697,
      "available_bikes": 674,
      "capped_available_bikes": false,
      "no_registration": false,
      "pricing": "https://www.metropolradruhr.de/de/preise/",
      "cities": [
        {
          "uid": 130,
          "lat": 51.4813,
          "lng": 7.2133,
          "zoom": 14,
          "maps_icon": "metroradruhr",
          "alias": "bochum",
          "break": false,
          "name": "Bochum",
          "num_places": 143,
          "refresh_rate": "10120",
          "bounds": {
            "south_west": {
              "lat": 51.1871,
              "lng": 6.7737
            },
            "north_east": {
              "lat": 51.5317,
              "lng": 7.4811
            }
          },
          "booked_bikes": 2,
          "set_point_bikes": 697,
          "available_bikes": 674,
          "return_to_official_only": true,
          "bike_types": {
            "4": 4,
            "14": 2,
            "29": 8,
            "71": 43,
            "150": 629
          },
          "website": "https://www.metropolradruhr.de/de/",
          "places": [
            {
              "uid": 338081,
              "lat": 51.48105636,
              "lng": 7.22485781,
              "bike": false,
              "name": "Technische Berufliche Schule 1",
              "address": null,
              "spot": true,
              "number": 7167,
              "booked_bikes": 0,
              "bikes": 10,
              "bikes_available_to_rent": 10,
              "bike_racks": 10,
              "free_racks": 0,
              "special_racks": 0,
              "free_special_racks": 0,
              "maintenance": false,
              "terminal_type": "stele",
              "bike_list": [
                {
                  "number": "500977",
                  "bike_type": 71,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551026768,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "500022",
                  "bike_type": 71,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551026229,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "502183",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551036012,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "502132",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551035805,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "502056",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551035591,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "501991",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551039030,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "501948",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551034357,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "501827",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551034723,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "501782",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551058495,
                  "pedelec_battery": null,
                  "battery_pack": null
                },
                {
                  "number": "501645",
                  "bike_type": 150,
                  "lock_types": [
                    "frame_lock"
                  ],
                  "active": true,
                  "state": "ok",
                  "electric_lock": true,
                  "boardcomputer": 7551057013,
                  "pedelec_battery": null,
                  "battery_pack": null
                }
              ],
              "bike_numbers": [
                "500977",
                "500022",
                "502183",
                "502132",
                "502056",
                "501991",
                "501948",
                "501827",
                "501782",
                "501645"
              ],
              "bike_types": {
                "71": 2,
                "150": 8
              },
              "place_type": "0",
              "rack_locks": false
            },
          ]
        }
      ]
    }
  ]
}
'''
