import requests as rq
from getLocation import WeatherLocation
# Class for getting the weather symbol from the weatherapi https://api.met.no/weatherapi/locationforecast/2.0/documentation#!/data/get_compact_format
# Using the compact formate gives a more compact response and is easier to navigate. The complete formate uses XML, and the compact uses json
# This tutorial is used as reference to create the request: https://docs.api.met.no/doc/locationforecast/HowTO
# along with this guide https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python


class WeatherSymbol:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_weather_data(self):

        endpoint = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={self.latitude}&lon={self.longitude}'

        headers = {
            'User-Agent': "User 1",
            'From': 'jakobuf@uia.no'
        }

        request = rq.get(endpoint, headers=headers)

        json = request.json()

        if request.status_code == 200:
            data = json['data']
            print('Data retrieved from frost.met.no!')
            f = open("WeatherForecast.txt", 'w')
            f.write(request.text)
            f.close()

        else:
            print('Error! Returned status code %s' % request.status_code)
            print('Message: %s' % json['error']['message'])
            print('Reason: %s' % json['error']['reason'])




