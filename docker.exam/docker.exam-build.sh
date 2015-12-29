#!/bin/sh

# Build the docker image

docker build -t exam $(dirname $0)
