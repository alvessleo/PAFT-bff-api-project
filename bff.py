from flask import Flask, render_template, jsonify, request
import requests
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

headers = {
    'X-Auth-Token': '5711e4dae4b9455c82d632c0e6955c31'
}

@app.route('/nba')
def teams():
    url = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams'
    respEspn = requests.get(url)

    jsonTeams = respEspn.json()

    x = random.randint(1, 20)

    respNBA = {
        'teamName' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('displayName'),
        'abbreviation' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('abbreviation'),
        'location' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('location'),
        'url' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('links')[0].get('href'),
        'foto' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('logos')[0].get('href')
        }

    return respNBA

@app.route('/matches')
def get_matches():
    url = "https://api.football-data.org/v4/matches"
    respMatches = requests.get(url, headers=headers).json()

    resp = {
        'homeCrest' : respMatches['matches'][0].get('homeTeam')['crest'],
        'nameHomeTeam' : respMatches['matches'][0].get('homeTeam')['name'],
        'scoreHomeTeam' : respMatches['matches'][0].get('score')['fullTime']['home'],
        'scoreAwayTeam' : respMatches['matches'][0].get('score')['fullTime']['away'],
        'awayCrest' : respMatches['matches'][0].get('awayTeam')['crest'],
        'nameAwayTeam' : respMatches['matches'][0].get('awayTeam')['name']
    }
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=5002)
