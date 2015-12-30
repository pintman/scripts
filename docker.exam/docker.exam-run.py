#!/usr/bin/python

# Run containers

import sys
import os

basePort = 50000

# checking command line arguments
if len(sys.argv) != 2:
  print("Give number of containers to be created.")
  exit(1)

anzahl = int(sys.argv[1])

# Starting containers exam0, ..., examN
print(" Starting " + str(anzahl) + " containers and mapping ports")

for i in range(1, anzahl + 1):
  # ii = format("%02.0f" % i) # format i to exactly two places
  ii = basePort + 100 * i
  portmap = (
    " -p " + str(ii+22) + ":22"
    " -p " + str(ii+80) + ":80"
    " -p " + str(ii+43) + ":443 "
  )
  print(" Starting exam" + str(i))
  containerName = "exam" + str(i)
  os.system("docker run -d -h " + containerName + " --name=" + containerName + portmap + " exam")
  os.system("docker port " + containerName)

