#!/usr/bin/env bash

echo "Usage: $0 domain"

set -eu

DOMAIN=$1

curl "https://www.duckdns.org/update?domains=$DOMAIN&token=$DUCKDNS_TOKEN"

