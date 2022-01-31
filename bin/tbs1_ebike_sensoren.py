#!/usr/bin/env python3

from urllib.request import urlopen
import json

ids = [3659,  #: ['P1', 'P10'], 
       3660]  #: ['temperature', 'humidity']

api = 'https://data.sensor.community/airrohr/v1/sensor/{id}/'

'''
Beispiel payload

[
  {
    "sensordatavalues": [
      {
        "value": "21.30",
        "value_type": "temperature",
        "id": 5480598392
      },
      {
        "value": "99.90",
        "value_type": "humidity",
        "id": 5480598394
      }
    ],
    "timestamp": "2020-11-08 11:47:21",
    "sampling_rate": null,
    "sensor": {
      "sensor_type": {
        "manufacturer": "various",
        "name": "DHT22",
        "id": 9
      },
      "pin": "7",
      "id": 3660
    },
    "location": {
      "indoor": 0,
      "longitude": "7.224",
      "latitude": "51.482",
      "id": 1846,
      "country": "DE",
      "exact_location": 0,
      "altitude": "96.7"
    },
    "id": 2534442076
  }, ...
]
'''

for sid in ids:
    js = json.load(urlopen(api.format(id=sid)))
    most_recent = 0
    print(f'Sensor #{sid}, last update: {js[most_recent]["timestamp"]}')
    results = {}
    for entry in js[most_recent]['sensordatavalues']:
        print(f"{entry['value_type']}: {entry['value']}")
