import requests
import json
import sys
import pprint

BASEURL = 'https://api.darksky.net'


def getforecast(key, lat, lon):
    session = requests.get(BASEURL + '/forecast/' + key +
                           '/' + lat + ',' + lon)
    return session.json()

try:
    with open('darksky_api.json') as f:
        api_key = json.loads(f.read())['api_key']
except():
    print("Unable to open darksky_api.json")
    sys.exit()

forecast = (getforecast(key=api_key, lat='38.5071335', lon='-121.5477066'))
pprint.pprint(forecast)
