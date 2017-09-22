from neo4j.v1 import GraphDatabase, basic_auth
import json

article2 = '{"id":"article0002","title":"article title 0002","date":"2017-09-20T1:25:00+00:00","subject":"Twitter","description":"body of text 0002"}'
article3 = '{"id":"article0003","title":"article title 0003","date":"2017-09-20T1:26:00+00:00","subject":"Google","description":"body of text 0003"}'

ajson2 = json.loads(article2)
ajson3 = json.loads(article3)

# print('{0}' .format(ajson['id']))

def createArticle(aj):
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("<user>", "<pwd>"))
    session = dr.session()
    results = session.run("CREATE (" + aj['id'] + ":Article {title:{title}, subject:{subject}, description:{description}, liked:0, weight:0})"
                          ,{"title": aj['title'],"subject": aj['subject'],"description": aj['description']})
    session.close()
    print(results)

def readArticle(title):
    dr = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j","west0ver"))
    session = dr.session()
    results = session.run("MATCH (article:Article) WHERE article.title = {title} RETURN article.subject as subject",{"title": title})
    session.close()
    result = results.single()
    print(result['subject'])

createArticle(ajson2)
createArticle(ajson3)

readArticle("article title 0002")
readArticle("article title 0003")
