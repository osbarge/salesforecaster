import requests
import json


def load_config():
    with open('.//apicaller//config') as json_file:  
        params = json.load(json_file)
        return params


config = load_config()
base_url = 'https://api.darksky.net/forecast/' 
url = base_url + config['apikey'] + '/' \
    + config['lat'] + ',' + config['long'] + ',' + config['time-unix'] + config['optional-params']
print('URL=', url)

response = requests.get(url)

# The response should be written into a json file
print(response.json())