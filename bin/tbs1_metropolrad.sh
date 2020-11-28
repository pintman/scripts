#!/bin/bash

API="https://maps.nextbike.net/maps/nextbike-live.json?city=130"

jq_tbs1='.countries[0].cities[0].places[]|select(.name=="Technische Berufliche Schule 1")'
jq_bikes="$jq_tbs1|.bike_list|length"

echo "Frei Räder an der TBS1-Station Metropolradruhr"
curl -s "$API" | jq "$jq_bikes"
