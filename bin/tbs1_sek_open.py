#!/usr/bin/env python3

import datetime

now = datetime.datetime.now()
# 0=Mon, 6=Sun
wday = now.weekday()
hour = now.hour
minu = now.minute

sek_open = False
# Mo-Fr 7:15-13:00
if 0 <= wday <= 4:
    if hour == 7 and minu >= 15:
        sek_open = True
    if 8 <= hour < 13:
        sek_open = True

# Mo-Do 14:15-15:45
if 0 <= wday <= 3:
    if hour == 14 and minu >= 15:
        sek_open = True
    if hour == 15 and minu <= 45:
        sek_open = True

# Fr 14-15
if wday == 4:
    if 14 <= hour < 15:
        sek_open = True

print(sek_open)

