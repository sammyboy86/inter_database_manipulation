import json

def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)

js_r("superheroes.json")

my_data = js_r('num.json')
print(my_data)
