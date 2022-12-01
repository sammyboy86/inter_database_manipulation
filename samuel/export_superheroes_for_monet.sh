#! /bin/bash

mongoexport --host localhost --db shapi --collection superheroes --type=csv --out text.csv --fields id,name,powerstats.intelligence

