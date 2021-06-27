import requests

base_url = 'http://localhost:5000'
headers = {'content-type': 'application/json'}


# Request list of all villagers from the REST service, if not 200 return None
def get_villagers():
    url = base_url + '/villagers'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        villagers_list = response.json()
        return villagers_list


def get_villager(villager_id):
    url = base_url + '/villager/' + str(villager_id)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        villager_data = response.json()
        return villager_data


def search_villagers(search_text):
    url = base_url + '/villagers/search'
    response = requests.get(url, headers=headers, params={'name': search_text})
    if response.status_code == 200:
        search_result = response.json()
        return search_result
