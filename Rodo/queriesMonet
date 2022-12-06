--top 10 promedios de inteligencia por raza
select "race", avg(intelligence) as intel
from supers
group by "race"
order by intel desc
limit 10;

--nombres de los 15 personajes más rapidos con género
select "name",gender, speed as vel
from supers
order by vel desc
limit 15;

--promedio de poder en personajes agrupados por color de ojos
select eyecolor,avg(power) as poder
from supers
group by eyecolor
order by poder desc
limit 10;
