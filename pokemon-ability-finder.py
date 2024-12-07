
import json
import requests


def search(pokemon_name):
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if pokemon.status_code==200:
        o = pokemon.json()
        return o
    else:
        return None

pokemon_input=input("Name a pokemon: ")
ability=search(pokemon_input)

abilities = ability['abilities']
for name in abilities:
        print(name['ability']['name'])
