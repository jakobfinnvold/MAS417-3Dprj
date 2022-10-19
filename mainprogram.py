# Libraries for API
import requests
import pandas as pd

client_id = 'bcfc74f6-c102-4435-8c22-d65236a14074'

# ID for grimstad -> SN38140
endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources' : 'SN38140',
    'elements' : 'mean(air_temperature P1D)',
    'referencetime' : '2010-10-09',
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

df = pd.DataFrame()
for i in range(len(data)):
    row = pd.DataFrame(data[i]['observations'])
    row['referenceTime'] = data[i]['referenceTime']
    row['sourceId'] = data[i]['sourceId']
    df = df.append(row)

df = df.reset_index()
df.head()
