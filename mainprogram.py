# Libraries for API Moretest from other laptop
import requests
import pandas as pd

client_id = 'bcfc74f6-c102-4435-8c22-d65236a14074'

# ID for Grimstad -> SN38140 | Krs SN39210
endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources' : 'SN18700',
    'elements' : 'over_time(weather_cloud_symbol PT6H)',
    'referencetime' : '1966-06-06T12',
}

r = requests.get(endpoint, parameters, auth=(client_id, ''))
json = r.json()

# Check if the request worked, print out any errors
if r.status_code == 200:
    data = json['data']
    print('Data retrieved from frost.met.no!')
else:
    print('Error! Returned status code %s' % r.status_code)
    print('Message: %s' % json['error']['message'])
    print('Reason: %s' % json['error']['reason'])


f = open('Weatherdata.txt', 'w')
f.write(r.text)
f.close()

