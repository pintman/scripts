#!/usr/bin/env sh

set -e

TMPFILE=/tmp/test.bin

curl -o $TMPFILE https://ash-speed.hetzner.com/1GB.bin && rm $TMPFILE
