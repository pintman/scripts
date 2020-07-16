#!/usr/bin/env python3

import pymsteams
import datetime
import sys
import os
import json

tokens = {}
homedir = os.environ['HOME']
CONFIG_FILE = homedir + os.sep + '.local' + os.sep + 'etc' + os.sep + 'msteams.conf'

def save_config():
    with open(CONFIG_FILE, 'w') as f:
        json.dump(tokens, f) 
    
def load_config():
    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)

    else:
        save_config()
        return load_config()

def add(args):
    if len(args) != 2: 
        print("need name and url of channel to be added")
        return

    name, url = args
    print('name url', name, url)
    tokens[name] = url
    save_config()

def list():
    print('registered tokens:')
    print('\n'.join(tokens.keys()))

def delete(args):
    if len(args) != 1:
        print('need name of url')
        return

    print('deleting', args[0])
    del tokens[args[0]]
    save_config()

def send(args):
    if len(args) == 0:
        print('need channel name and message')
        return

    chan_url = tokens[args[0]]
    msg = ' '.join(args[1:])

    card = pymsteams.connectorcard(chan_url)
    #card.title(f'Titel {datetime.datetime.now()}')
    card.text(msg)
    #card.printme()
    card.send()

def main():
    global tokens
    tokens = load_config()

    args = sys.argv[1:]
    if len(sys.argv) < 2:
        print('need command: add, del, list, send')
        return

    if args[0] == 'add':
        add(args[1:])
    elif args[0] == 'del':
        delete(args[1:])
    elif args[0] == 'list':
        list()
    elif args[0] == 'send':
        send(args[1:])
    else:
        print('command unknown:', args[0])

if __name__ == '__main__':
    main()
