#!/bin/bash

echo "frei/reserviert/belegt"
ebike_status.py | grep "Ostring 25"
