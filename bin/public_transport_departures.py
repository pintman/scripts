#!/usr/bin/env python3

"""
Fetch public transport departures from a given station. Station name, city name
and duration of the search can be configured.
"""

import datetime
import json

# https://pyhafas.readthedocs.io/en/stable/usage/client.html
from pyhafas import HafasClient
from pyhafas.profile import DBProfile

CITY = "Bochum"
STATION_NAME = "Bochum Hbf"
DUATION_MINUTES = 30

# Creating client with the default DB profile
db_profile = DBProfile()
client = HafasClient(db_profile)

# fetching locations, entries are of the form
# <class 'pyhafas.types.fptf.Station'>({'id': '8000041', 'lid': 'A=1@O=Bochum Hbf@X=7223273@Y=51478607@U=80@L=8000041@B=1@p=1726687511@i=U×008010179@', 'name': 'Bochum Hbf', 'latitude': 51.47849, 'longitude': 7.223264})
locations = client.locations(CITY)

# find desired station
station = [l for l in locations if l.name == STATION_NAME][0]

# dont search for IC/ICE
products_filter = {
    'long_distance': False,
    'long_distance_express': False
}

# querying deaprtures. Entries are of the form
# <class 'pyhafas.types.fptf.StationBoardLeg'>({'id': '2|#VN#1#ST#1726687511#PI#0#ZI#272035#TA#0#DA#220924#1S#8000105#1T#650#LS#8002553#LT#1230#PU#80#RT#1#CA#ICE#ZE#1916#ZB#ICE 1916#PC#0#FR#8000105#FT#650#TO#8002553#TT#1230#', 'name': 'ICE 1916', 'direction': 'Hamburg-Altona', 'station': <class 'pyhafas.types.fptf.Station'>({'id': '8000041', 'lid': 'A=1@O=Bochum Hbf@X=7223273@Y=51478607@U=80@L=8000041@i=U×008010179@', 'name': 'Bochum Hbf', 'latitude': 51.478607, 'longitude': 7.223273}), 'dateTime': datetime.datetime(2024, 9, 22, 9, 10, tzinfo=<DstTzInfo 'Europe/Berlin' CEST+2:00:00 DST>), 'cancelled': False, 'delay': datetime.timedelta(seconds=2580), 'platform': '5'})
dep = client.departures(
    station= station.id,
    date=datetime.datetime.now(),
    products=products_filter,
    duration=DUATION_MINUTES,
)

# put entries into a list of dicts
entries = []
for d in dep:
    entry = {
        "name": d.name, "direction": d.direction, 
        "time": str(d.dateTime), "delay": str(d.delay)}
    entries.append(entry)

# preparing and printing result
ret = {
    "query_time": str(datetime.datetime.now()),
    "city": CITY,
    "station": STATION_NAME,
    "duration_minutes": DUATION_MINUTES,
    "departures": entries
}
print(json.dumps(ret, indent=2))
