import requests as requests
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/villagers/')
def villagers():

    url = 'http://localhost:5000/villagers'
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        villagers_list = r.json()
        return render_template('villagers.html', villagers_list=villagers_list)

    return render_template('error.html')


@app.route('/villager/<int:villager_id>')
def villager(villager_id):

    url = 'http://localhost:5000/villager/' + str(villager_id)
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        villager_data = r.json()
        return render_template('villager.html', villager=villager_data)

    return render_template('error.html')


