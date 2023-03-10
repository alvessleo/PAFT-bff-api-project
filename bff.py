from flask import Flask, render_template, jsonify, request
import requests
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

headers = {
    'X-Auth-Token': '5711e4dae4b9455c82d632c0e6955c31'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nba')
def teams():
    if request.method == 'GET':
        try:
            url = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams'
            respEspn = requests.get(url)

            jsonTeams = respEspn.json()

            x = random.randint(1, 29)

            respNBA = {
                'teamName' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('displayName'),
                'abbreviation' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('abbreviation'),
                'location' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('location'),
                'url' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('links')[0].get('href'),
                'foto' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('logos')[0].get('href'),
                'color' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('color')
                }
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return respNBA

@app.route('/matches')
def matches():
    if request.method == 'GET':
        try:
            url = "https://api.football-data.org/v4/matches"
            respMatches = requests.get(url, headers=headers).json()

            api_key = '5f527d552e6cbf05eca944e42dc82ddf'
            
            url_weather = 'https://api.openweathermap.org/data/2.5/weather?q=Guaiaquil&appid=' + api_key
            response = requests.get(url_weather).json()
            # temperatura = response['main']['temp']
            # descricao = response['weather'][0]['description']

            resp = {
                'homeCrest' : respMatches['matches'][0].get('homeTeam')['crest'],
                'nameHomeTeam' : respMatches['matches'][0].get('homeTeam')['name'],
                'scoreHomeTeam' : respMatches['matches'][0].get('score')['fullTime']['home'],
                'scoreAwayTeam' : respMatches['matches'][0].get('score')['fullTime']['away'],
                'awayCrest' : respMatches['matches'][0].get('awayTeam')['crest'],
                'nameAwayTeam' : respMatches['matches'][0].get('awayTeam')['name'],
                'weather' : response['main']['temp'],
                'description' : response['weather'][0]['description']
            }
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return resp

@app.route('/listTemplate')
def list():
    if request.method == 'GET':
        try:
            url = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams'
            respEspn = requests.get(url)

            jsonTeams = respEspn.json()

            x = random.randint(1, 29)
            y = random.randint(1, 29)
            z = random.randint(1, 29)

            team_list = [{'teamName' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('displayName'),
                'abbreviation' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('abbreviation'),
                'location' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('location'),
                'url' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('links')[0].get('href'),
                'foto' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('logos')[0].get('href'),
                'color' : jsonTeams['sports'][0]['leagues'][0]['teams'][x]['team'].get('color')},
                {
                'teamName' : jsonTeams['sports'][0]['leagues'][0]['teams'][y]['team'].get('displayName'),
                'abbreviation' : jsonTeams['sports'][0]['leagues'][0]['teams'][y]['team'].get('abbreviation'),
                'location' : jsonTeams['sports'][0]['leagues'][0]['teams'][y]['team'].get('location'),
                'url' : jsonTeams['sports'][0]['leagues'][0]['teams'][y]['team'].get('links')[0].get('href'),
                'foto' : jsonTeams['sports'][0]['leagues'][0]['teams'][y]['team'].get('logos')[0].get('href'),
                'color' : jsonTeams['sports'][0]['leagues'][0]['teams'][y]['team'].get('color')
                },
                {
                'teamName' : jsonTeams['sports'][0]['leagues'][0]['teams'][z]['team'].get('displayName'),
                'abbreviation' : jsonTeams['sports'][0]['leagues'][0]['teams'][z]['team'].get('abbreviation'),
                'location' : jsonTeams['sports'][0]['leagues'][0]['teams'][z]['team'].get('location'),
                'url' : jsonTeams['sports'][0]['leagues'][0]['teams'][z]['team'].get('links')[0].get('href'),
                'foto' : jsonTeams['sports'][0]['leagues'][0]['teams'][z]['team'].get('logos')[0].get('href'),
                'color' : jsonTeams['sports'][0]['leagues'][0]['teams'][z]['team'].get('color')
                }]
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return render_template('list-template.html',list=team_list)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
