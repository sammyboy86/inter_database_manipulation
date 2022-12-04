# QueriesMongo 
**1. ¿Quienes son más inteligentes los superhéroes o villanos?**
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
**2. ¿Cuál es la distribución de los personajes por publisher?**

```
db.superheroes.aggregate({$group: {_id: "$biography.publisher", Numberofcharacters: {$sum:1}}})
```

**Respuesta:**
```
[
  { _id: 'Black Racer', Numberofcharacters: 1 },
  { _id: 'Power Man', Numberofcharacters: 1 },
  { _id: 'Impulse', Numberofcharacters: 1 },
  { _id: 'Phoenix', Numberofcharacters: 1 },
  { _id: 'Superman Prime One-Million', Numberofcharacters: 1 },
  { _id: 'George Lucas', Numberofcharacters: 12 },
  { _id: 'Dark Horse Comics', Numberofcharacters: 15 },
  { _id: null, Numberofcharacters: 6 },
  { _id: 'Rebellion', Numberofcharacters: 1 },
  { _id: 'Ms Marvel II', Numberofcharacters: 1 },
  { _id: 'Scorpion', Numberofcharacters: 1 },
  { _id: 'Gemini V', Numberofcharacters: 1 },
  { _id: 'Batman II', Numberofcharacters: 2 },
  { _id: 'Universal Studios', Numberofcharacters: 1 },
  { _id: 'Image Comics', Numberofcharacters: 3 },
  { _id: 'Anti-Venom', Numberofcharacters: 2 },
  { _id: 'South Park', Numberofcharacters: 1 },
  { _id: 'DC Comics', Numberofcharacters: 155 },
  { _id: 'Batgirl V', Numberofcharacters: 1 },
  { _id: 'Marvel Comics', Numberofcharacters: 269 }
]
```

**3. ¿Cuál es la distribución de villanos, superheroes o neutrales por género?**
```
db.superheroes.aggregate({$group:{_id:{CharacterType:"$CharacterType", Gender:"$appearance.gender"}, Count:{$sum:1}}})
```

**Respuesta:** 

```
[
  { _id: { CharacterType: 'superhero', Gender: '-' }, Count: 8 },
  { _id: { CharacterType: 'Villain', Gender: 'Male' }, Count: 134 },
  { _id: { CharacterType: 'Villain', Gender: 'Female' }, Count: 28 },
  { _id: { CharacterType: 'Villain', Gender: '-' }, Count: 4 },
  { _id: { CharacterType: 'Neutral', Gender: 'Male' }, Count: 23 },
  { _id: { CharacterType: 'Neutral', Gender: '-' }, Count: 3 },
  { _id: { CharacterType: 'superhero', Gender: 'Male' }, Count: 239 },
  { _id: { CharacterType: 'Neutral', Gender: 'Female' }, Count: 4 },
  { _id: { CharacterType: 'superhero', Gender: 'Female' }, Count: 120 }
]
```


