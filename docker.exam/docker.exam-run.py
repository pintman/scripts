#!/usr/bin/python

# Run containers

import sys
import os

basePort = int(os.getenv("BASEPORT", 50000))

# checking command line arguments
if len(sys.argv) != 2:
  print("Give number of containers to be created.")
  print("Change base port for containers:")
  print("BASEPORT=50000 " + sys.argv[0]);
  exit(1)

anzahl = int(sys.argv[1])

# Starting containers exam0, ..., examN
print(" Starting " + str(anzahl) + " containers and mapping ports")

for i in range(1, anzahl + 1):
  ii = basePort + 100 * i
  portmap = (
    " -p " + str(ii+22) + ":22"
    " -p " + str(ii+80) + ":80"
    " -p " + str(ii+43) + ":443 "
  )
  containerName = "exam" + str(i)
  print(" => Starting exam" + containerName)
  os.system("docker run -d -h " + containerName + " --name=" + containerName + portmap + " exam")
  os.system("docker port " + containerName)
