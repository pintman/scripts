#!/usr/bin/env bash

# Update dns record for given domain. Must be created before in
# ducks dns account.
# needs token to be stored env.

echo "Usage: $0 domain"

set -eu

DOMAIN=$1

curl "https://www.duckdns.org/update?\
domains=$DOMAIN&\
token=$DUCKDNS_TOKEN"

