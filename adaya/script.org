# Cómo correr nuestro proyecto
## Empecemos con lo de las apis

Usamos una api de superheroes que tienen sus características, por quiénes fueron publicados, sus ciudades, etc. Lo padre es que no son de los mismos universos y eso nos da más posiblidades de análisis.
Aquí es necesario que ejecutemos el siguiente código de python.

#+begin_src py
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
#+end_src
