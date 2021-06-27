import requests as requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/villagers/')
def villagers():

    url = 'http://127.0.0.1:5000/villagers'
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        villagers_list = r.json()
        print(villagers_list)
        return render_template('villagers.html', villagers_list=villagers_list)

    return render_template('error.html')


