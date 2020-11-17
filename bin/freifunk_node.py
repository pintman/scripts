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
        netaddr = node_info['network']['addresses']
        stat = node['statistics']
        print('Hostname:', node_info['hostname'])
        print('Clients:', stat['clients'])
        print('Firmware:', node_info['software']['firmware']['release'])
        print('Adresses:', ', '.join(netaddr))
        print('Average Load:', stat['loadavg'])
        print('Uptime:', stat['uptime'])
        print('Memory Usage:', stat['memory_usage'])
        print('Online:', node['flags']['online'])
