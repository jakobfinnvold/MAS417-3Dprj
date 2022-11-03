# Trying to combine the two classes for getting location and weather together in one class, as there were trouble
# getting the correct information from the weatherAPI/locationforecats.
# Still using the tutorial here: https://frost.met.no/python_example.html for location and
# https://docs.api.met.no/doc/locationforecast/HowTO and
# https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python for locationforecast

import requests as rq


class WeatherSymbol:

    def __init__(self, location):
        self.location = location

    # Initializing
    longitude = 0
    latitude = 0


    def acquire_location(self):

        client_id = 'bcfc74f6-c102-4435-8c22-d65236a14074'

        endpoint = f'https://frost.met.no/locations/v0.jsonld?names={self.location}'

        request = rq.get(endpoint, auth=(client_id, ''))

        json = request.json()

        # Print error message if location is not valid/obtainable, #If ok, write to txt file to verify
        if request.status_code == 200:
            data = json['data'][00]['geometry']['coordinates']
            #print('Data retrieved from frost.met.no!')
            f = open("WeatherLocation.txt", 'w')
            f.write(request.text)
            f.close()
            self.latitude = data[1]
            self.longitude = data[0]



        else:
            print('Error! Returned status code %s' % request.status_code)
            print('Message: %s' % json['error']['message'])
            print('Reason: %s' % json['error']['reason'])



    def get_weather_symbol(self):

        endpoint = f'https://api.met.no/weatherapi/locationforecast/2.0/compact.json?lat={self.latitude}&lon={self.longitude}'

        headers = {
            'User-Agent': "User 1",
            'From': 'jakobuf@uia.no'
        }

        request = rq.get(endpoint, headers=headers)

        json = request.json()

        if request.status_code == 200:
            data = json['properties']['timeseries'][00]['data']['next_6_hours']['summary']['symbol_code']
            #print('Data retrieved from frost.met.no!')
            self.wsymbol = data[0:100]  # Large buffer to get the whole string
            f = open("WeatherSymbol.txt", 'w')  # Writing symbol string to a textfile that can be read when creating.stl
            f.write(self.wsymbol)
            f.close()


        else:
            print('Error! Returned status code %s' % request.status_code)
            print('Message: %s' % json['error']['message'])
            print('Reason: %s' % json['error']['reason'])

        return f'{self.location} will be {self.wsymbol} for the next 6 hours'
