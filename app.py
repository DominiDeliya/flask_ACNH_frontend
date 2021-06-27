import requests as requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('villagers'))


@app.route('/villagers', methods=['GET', 'POST'])
def villagers():
    headers = {'content-type': 'application/json'}
    search_text = request.form.get('search_text')
    if request.method == 'POST':
        url = 'http://localhost:5000/villagers/search'
        r = requests.get(url, headers=headers, params={'name': search_text})
    else:
        url = 'http://localhost:5000/villagers'
        r = requests.get(url, headers=headers)

    if r.status_code == 200:
        villagers_list = r.json()
        if search_text is None:
            search_text = ''
        return render_template('villagers.html', villagers_list=villagers_list, search_text=search_text)

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


