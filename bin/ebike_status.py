#!/usr/bin/env python3

from urllib.request import urlopen
import json

API = 'https://api.e-bike-garage.de/api/v1'
STATUS_FREE = 'free'
STATUS_TAKEN = 'taken'
STATUS_RESERVED = 'reserved'

def get_containers():
    ''' Fetch list of containers:
    [
        {
            "id": 0,
            "uid": "string",
            "name": "string",
            "description": "string",
            "location": "string",
            "lat": 0,
            "lon": 0,
            "modified": "2020-11-03T16:33:56.231Z"
        }
    ]
    '''
    url = f'{API}/containers'
    return json.load(urlopen(url))

def get_boxes(container_id):
    '''
    Fetch status of boxes.
    [{'containerId': 6,
    'id': 28,
    'modified': '2020-11-03T17:13:31+01:00',
    'name': 'Box1',
    'status': 'taken',
    'uid': 'c9816a81-af27-4479-b2ba-62d169590f1c'},
    ...
    ]
    '''
    url = f'{API}/container/{container_id}/boxes'
    return json.load(urlopen(url))

def main():
    print('Status der Boxen in E-Bike-Garagen in Bochum (frei/reserviert/belegt)')
    for container in get_containers():
        boxes = get_boxes(container['id'])
        free, reserved, taken = 0,0,0
        for box in boxes:
            status = box['status']
            if status == STATUS_FREE: free += 1
            elif status == STATUS_RESERVED: reserved += 1
            elif status == STATUS_TAKEN: taken += 1

        print(f'{free}/{reserved}/{taken}: {container["location"]}')

if __name__ == '__main__':
    main()
