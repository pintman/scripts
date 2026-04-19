#!/usr/bin/env python3

import requests
import json

BASE = 'https://termine.bochum.de'
SUB = '/m/buergerbuero/extern/calendar/search_result?search_mode=earliest&uid=eab3c2ce-bd9c-4c81-8dab-663aebdc0ce3&wsid=62e76b0e-3946-4152-917e-d0b6d9132901'


def main():
    URL = BASE + SUB
    html = requests.get(URL).text

    # looking for json in HTML
    #
    inJson = False
    js_str = ''
    for l in html.split():
        if 'json_appointment_list' in l:
            inJson = True

        elif inJson and '</div>' in l:
            inJson = False

        elif inJson:
            js_str += l + ' '

    js = json.loads(js_str)

    for app in js['appointments']:
        print(app['date_time'], app['unit'], '\n', BASE + app['link'])

if __name__ == "__main__":
    main()
    
