from neo4j.v1 import GraphDatabase, basic_auth
import json

article2 = '{"id":"article0002","title":"article title 0002","date":"2017-09-20T1:25:00+00:00","subject":"Twitter","description":"body of text 0002"}'
article3 = '{"id":"article0003","title":"article title 0003","date":"2017-09-20T1:26:00+00:00","subject":"Google","description":"body of text 0003"}'

ajson2 = json.loads(article2)
ajson3 = json.loads(article3)

# print('{0}' .format(ajson['id']))

def createArticle(aj):
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    results = session.run("CREATE (" + aj['id'] + ":Article {title:{title}, subject:{subject}, description:{description}, liked:0, weight:0})"
                          ,{"title": aj['title'],"subject": aj['subject'],"description": aj['description']})
    session.close()
    # print(vars(results))
    print("create node: " + results.parameters["title"])

def readArticle(title):
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} RETURN article.subject as subject",{"title": title})
    session.close()
    result = results.single()
    print(result['subject'])

def updateArticle(title, subject):
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} " +
                          "SET article.subject = {subject} " +
                          "RETURN article.subject as subject", {"title": title, "subject": subject})
    session.close()
    result = results.single()
    print(result['subject'])

# not done
def deleteArticle(title):
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} " +
                          "DELETE article", {"title": title})
    session.close()

# not done
def linkArticles(title1, title2):
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} RETURN article.subject as subject",{"title": title})
    session.close()
    result = results.single()
    print(result['subject'])

def deleteDB():
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    session.run("MATCH (n) DETACH DELETE n")
    session.close()

def readDB():
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    results = session.run("MATCH (n) RETURN n")
    session.close()
    print(vars(results))
    print("---------")
    print(results._buffer)
    print("---------")
    for r in results:
        print(r[0].properties["title"])

deleteDB()
createArticle(ajson2)
createArticle(ajson3)

readArticle("article title 0002")
readArticle("article title 0003")

updateArticle("article title 0003","Microsoft")
readArticle("article title 0003")
readDB()
