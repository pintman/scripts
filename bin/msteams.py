#!/usr/bin/env python3

import pymsteams
import os
import stat
import json
import click

tokens = {}
homedir = os.environ['HOME']
CONFIG_FILE = homedir + '/.local/etc/msteams.conf'

def save_config():
    with open(CONFIG_FILE, 'w') as f:
        json.dump(tokens, f) 
    
def load_config():
    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)

    else:
        # no config file found - creating new (empty) one.
        save_config()
        # read/write by owner only
        os.chmod(CONFIG_FILE, stat.S_IREAD | stat.S_IWRITE)
        return load_config()

@click.group()
def cli():
    '''
    CLI for sending messages to channels in MS-Teams. Each channel must
    be configured as incoming webhook and must be added to the database.

    By default all configuration is stored in ~/.local/etc/msteams.conf.
    '''

@cli.command()
@click.argument('name')
@click.argument('url')
def add(name, url):
    'Add a token to the database.'
    tokens[name] = url
    save_config()

@cli.command()
def list():
    'List registered tokens.'
    print('Registered token names:', ','.join(tokens.keys()))

@cli.command()
@click.argument('name')
def delete(name):
    'Delete a given token.'
    print('deleting', name)
    del tokens[name]
    save_config()

@cli.command()
@click.argument('name')
@click.argument('message', nargs=-1)
def send(name, message):
    'Send a message to a named channel.'
    chan_url = tokens[name]

    card = pymsteams.connectorcard(chan_url)
    #card.title(f'Titel {datetime.datetime.now()}')
    card.text(' '.join(message))
    #card.printme()
    card.send()

def main():
    global tokens
    tokens = load_config()

    cli()

if __name__ == '__main__':
    main()
