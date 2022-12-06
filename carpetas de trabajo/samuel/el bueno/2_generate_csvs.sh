#! /bin/bash

mongoexport --db=shapi --collection=superheroes --type=csv --out superheroes_monetdb.csv --fields=name,slug,powerstats.intelligence,powerstats.strength,powerstats.speed,powerstats.durability,powerstats.power,powerstats.combat,appearance.height,appearance.weight,appearance.eyeColor,appearance.hairColor,appearance.gender,appearance.race,work.occupation,biography.fullName,biography.alterEgos,biography.firstAppearance,biography.aliases

mongoexport --db=shapi --collection=superheroes --type=csv --out superheroes_n4j.csv --fields=name,slug,appearance.gender,appearance.race,biography.publisher,biography.placeOfBirth,biography.alignment,work.base,connections.groupAffiliation, connections.relatives
