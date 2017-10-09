A collection of python functions to perform CRUD operations on a Neo4j database

Platform:
  Ubuntu 17.04

Install neo4j:
  https://neo4j.com/docs/operations-manual/current/installation/linux/debian/

Start neo4j server (http://localhost:7474/browser/):
  sudo /usr/bin/neo4j start

Install python neo4j-driver:
  sudo pip install neo4j-driver

Create config.json file with text:
{"username":"neo4j","password":"mypassword"}

!!!!!WARNING THE FUNCTION deleteDB() WILL DELETE ALL OF THE NEO4J DATABASE!!!!!
!!!!!USE ONLY WHEN CONNECTED TO YOUR LOCAL NEO4J DATABASE!!!!!
!!!!!NEVER RUN THIS SCRIPT ON THE GCP SERVER, IT WILL DELETE ALL DATA IN NEO4J!!!!!
#deleteDB() # ONLY uncomment when running script from localhost
