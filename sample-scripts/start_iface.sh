#!/bin/bash

PHY=${1:-phy0}

sudo iw phy $PHY set channel 1
sudo iw phy $PHY interface add mon0 type monitor

docker run \
    -p7474:7474 -p7687:7687 \
    --rm  -ti\
    --env NEO4J_AUTH=neo4j/demo \
    neo4j:latest