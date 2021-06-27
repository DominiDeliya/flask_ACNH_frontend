from flask import Flask, render_template, request, redirect, url_for
from rest_client import get_villager, search_villagers, get_villagers

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('villagers'))


@app.route('/villagers', methods=['GET', 'POST'])
def villagers():
    search_text = request.form.get('search_text')
    if request.method == 'POST' and search_text:
        response = search_villagers(search_text)
    else:
        response = get_villagers()

    if response:
        if search_text is None:
            search_text = ''
        return render_template('villagers.html', villagers_list=response, search_text=search_text)

    return render_template('error.html')


@app.route('/villager/<int:villager_id>')
def villager(villager_id):
    response = get_villager(villager_id)
    if response:
        return render_template('villager.html', villager=response)

    return render_template('error.html')


