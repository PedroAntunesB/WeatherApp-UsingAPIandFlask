from flask import Blueprint, render_template, request
import requests

clima = Blueprint('clima' ,__name__)

@clima.route('/')
def index():
    return render_template('index.html', city=0)


@clima.route('/processar', methods=['POST', 'GET'])
def processar():
    local = request.form.get('search-bar')
    url = f"https://wttr.in/{local}?format=j1"
    response = requests.get(url)
    dados = response.json()
    clima_atual = dados['current_condition'][0]

    city = {
        'cidade': local,
        'temperatura': clima_atual['temp_C'],
        'clima': clima_atual['weatherDesc'][0]['value']
    }

    return render_template('index.html', city=city)