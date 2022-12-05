#API de superheroes de muchos universos 
import pymongo
from pymongo import MongoClient
import requests
import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
  
client=MongoClient('localhost',27017)
db=client.shapi
col=db.superheroes

lista=[] 
for i in range(1,732): 
    url = f'https://akabab.github.io/superhero-api/api/id/{i}.json'
    superhero=requests.get(url).text
    if (validateJSON(superhero)==True): 
        superheroes=json.loads(superhero)
        lista.append(superheroes)
lista

col.insert_many(lista)
