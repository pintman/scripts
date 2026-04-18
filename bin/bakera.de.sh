#!/bin/bash

echo "$0 PAGENAME"

set -xeu

curl "https://www.bakera.de/doku.php/$1?do=export_raw"
