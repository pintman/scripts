#!/usr/bin/python

# Run containers

import sys
import os

portprefix = "5"

# checking command line arguments
if len(sys.argv) != 2:
  print("Give number of containers to be created.")
  exit(1)

anzahl = int(sys.argv[1])
if anzahl >= 10:
  print("Maximum of 9 containers allowed")
  exit(1)

# Starting containers exam0, ..., examN
print(" Starting " + str(anzahl) + " containers and mapping ports")

for i in range(1, anzahl + 1):
  # ii = format("%02.0f" % i) # format i to exactly two places
  ii = str(i)
  portmap = (
    " -p " + portprefix + ii + "022:22"
    " -p " + portprefix + ii + "080:80"
    " -p " + portprefix + ii + "443:443 "
  )
  print(" Starting exam" + ii)
  os.system("docker run -d -h exam" + ii + " --name=exam" + ii + portmap + " exam")
  os.system("docker port exam" + str(i))

