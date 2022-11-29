import pandas as pd
import requests
import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["pokemon"]
collection = my_db["pokemon"]
response = []

for i in range(1, 152):
	response.append(requests.get("https://pokeapi.co/api/v2/pokemon/" + str(i)).json())

collection.insert_many(response)

