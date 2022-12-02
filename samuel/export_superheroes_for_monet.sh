#! /bin/bash

mongoexport --host localhost --db shapi --collection superheroes --type=csv --out superheroes.csv --fields id,name,powerstats.intelligence

