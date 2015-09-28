#! /usr/bin/env bash

docker run -d --name neo4j -p 7474:7474 neo4j/neo4j

docker run -it --link neo4j:neo4j -v $(pwd):/usr/src/app -p 5000:5000 ipedrazas/landscape-api
