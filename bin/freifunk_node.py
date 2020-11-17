#!/usr/bin/env python3

import json
from urllib.request import urlopen

api ='http://map.freifunk-bochum.de:4000/nodes.json'
my_id = 'a0f3c178087c'

data = urlopen(api)
js = json.load(data)

for node in js['nodes']:
    node_info = node['nodeinfo']
    node_id = node_info['node_id']
    if node_id == my_id:
        fw = node_info['software']['firmware']['release']
        netaddr = node_info['network']['addresses']
        clients = node['statistics']['clients']
        hostname = node_info['hostname']
        print('Hostname:', hostname)
        print('Clients:', clients)
        print('Firmware:', fw)
        print('Adresses:', ', '.join(netaddr))
