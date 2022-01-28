#!/usr/bin/env python3

import datetime

n = datetime.datetime.now()
_, weeknumber, _ = n.isocalendar()

if weeknumber % 2 != 0:
    print('A')
else:
    print('B')