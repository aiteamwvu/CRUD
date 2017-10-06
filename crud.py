from neo4j.v1 import GraphDatabase, basic_auth
import json, datetime

config = json.loads(open('config.json').read())
username = config["username"]
password = config["password"]
url = "bolt://localhost:7687"
date = datetime.datetime.today()

article1 = '{"id":"article0001","title":"article title 0001","date":"'+str(date)+'","subject":"Neo4j","description":"body of text 0001"}'
article2 = '{"id":"article0002","title":"article title 0002","date":"'+str(date)+'","subject":"Twitter","description":"body of text 0002"}'
article3 = '{"id":"article0003","title":"article title 0003","date":"'+str(date)+'","subject":"Google","description":"body of text 0003"}'
article4 = '{"id":"article0004","title":"article title 0004","date":"'+str(date)+'","subject":"Oracle","description":"body of text 0004"}'

ajson1 = json.loads(article1)
ajson2 = json.loads(article2)
ajson3 = json.loads(article3)
ajson4 = json.loads(article4)

dr = GraphDatabase.driver(url, auth=basic_auth(username,password))

def createArticle(aj):
    session = dr.session()
    results = session.run("CREATE (" + aj['id'] + ":Article {title:{title}, subject:{subject}, description:{description}, liked:0, weight:0})"
                          ,{"title": aj['title'],"subject": aj['subject'],"description": aj['description']})
    session.close()

def readArticle(title):
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} RETURN article.subject as subject",{"title": title})
    session.close()
    result = results.single()
    print(result['subject'])

def updateArticle(title, subject):
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} " +
                          "SET article.subject = {subject} " +
                          "RETURN article.subject as subject", {"title": title, "subject": subject})
    session.close()
    result = results.single()
    print(result['subject'])

def deleteArticle(title):
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} " +
                          "DELETE article", {"title": title})
    session.close()

def linkArticles(title1, title2, keys):
    session = dr.session()
    results = session.run("MATCH (article1:Article), (article2:Article) " +
                          "WHERE article1.title = {title1} AND article2.title = {title2} " +
                          "CREATE (article1)-[r:SHARED_KU {keys:['" + keys + "']}]->(article2) " +
                          "RETURN r", {"title1": title1, "title2": title2})
    session.close()
    return results

def deleteDB():
    session = dr.session()
    session.run("MATCH (n) DETACH DELETE n")
    session.close()

def readDB():
    session = dr.session()
    results = session.run("MATCH (n) RETURN n")
    session.close()
    print("---------")
    for r in results:
        print(r[0].properties["title"])

deleteDB()
createArticle(ajson1)
createArticle(ajson2)
createArticle(ajson3)
createArticle(ajson4)

readArticle("article title 0002")
readArticle("article title 0003")

updateArticle("article title 0003","Microsoft")
readArticle("article title 0003")
deleteArticle("article title 0003")

linkArticles("article title 0001","article title 0002", "k1,k2,k3,k4")
readDB()
