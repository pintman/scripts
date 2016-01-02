#!/usr/bin/python

# Run containers

import sys
import os

def usage():
    print("Give number of containers to be created.")
    print(sys.argv[0] + " NUM")
    print("Change base port for containers:")
    print("BASEPORT=50000 " + sys.argv[0]);
    print("Change name of container")
    print("CONTAINERNAME=exam " + sys.argv[0])

def main():
  basePort = int(os.getenv("BASEPORT", 50000))
  containerName = os.getenv("CONTAINERNAME", "exam")

  # checking command line arguments
  if len(sys.argv) != 2:
    usage()
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
    cName = containerName + str(i)
    print(" => Starting " + cName)
    os.system("docker run -d -h " + cName + " --name=" + cName + portmap + " exam")
    os.system("docker port " + cName)


if __name__ == "__main__":
  main()
