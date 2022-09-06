from flask import render_template, redirect, request
from flask_app import app 
import requests

@app.route("/pokedex")
def pokedex():
    return render_template("pokedex.html")

@app.route("/pokedex/find", methods=['POST'])
def findPokemon():
    pokemon = {
        "name": request.form["name"]
    }
    data = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon)).json()
    print(data)
    return redirect('/pokedex', pokemon = data)

@app.route("/pokemon", methods = ['POST'])
def get_pokemon():
    results = []
    if request.form['name']:
        results.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{request.form["name"]}').json())
    else: 
        results.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/rayquaza').json())
    print(results)
    return render_template('poke.html', pokemon = results)