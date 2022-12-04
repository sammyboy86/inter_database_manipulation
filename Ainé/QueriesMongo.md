# QueriesMongo 

Primero convertimos todos los campos con strings separados por comas en arrays: 
```
db.superheroes.updateMany({},[{$addFields:{"connections.groupAffiliation": { "$split": [ "$connections.groupAffiliation", "," ]}}}])
db.superheroes.updateMany({},[{$addFields:{"connections.relatives": { "$split": [ "$connections.relatives", "," ]}}}])
db.superheroes.updateMany({},[{$addFields:{"work.occupation": { "$split": [ "$work.occupation", "," ]}}}])
db.superheroes.updateMany({},[{$addFields:{"work.base": { "$split": [ "$work.base", "," ]}}}])
```


1. ¿Quienes son más inteligentes los superhéroes o villanos?

Agregamos un campo a la base de datos CharacterType dependiendo de su alignment: 
```
db.superheroes.updateMany({},[{$addFields:{CharacterType:{$cond: {if:{$in:["$biography.alignment",["good"]]},then: "superhero", else: {$cond: {if:{$in:["$biography.alignment", ["bad"]]},then:"Villain",else:"Neutral"}}}}}}])
```
Luego agrupamos y sacamos el promedio de cada uno de los grupos: 
```
db.superheroes.aggregate({$group: {_id: "$CharacterType", Avgintelligence: {$avg: "$powerstats.intelligence"}}})
```
Respuesta: Villanos 
```
[
  { _id: 'Villain', Avgintelligence: 68.04819277108433 },
  { _id: 'Neutral', Avgintelligence: 65.93333333333334 },
  { _id: 'superhero', Avgintelligence: 62.776566757493185 }
]
```

