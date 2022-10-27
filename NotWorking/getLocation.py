import numpy as np
import requests as rq
# This class is based on the tutorial from met.no located here: https://frost.met.no/python_example.html The correct
# locations in the API will be used to provide latitude and longitude to the weatherAPI to retrieve a forecast


class WeatherLocation:

    def __init__(self, location, latitude, longitude):
        self.location = location
        self.latitude = latitude
        self.longitude = longitude


    # Printing the chosen location to confirm that we have a valid one
    def __str__(self):
        return f'Location: {self.location}, Latitude: {self.latitude}, Longitude: {self.longitude}'


    def acquire_location(self):

        client_id = 'bcfc74f6-c102-4435-8c22-d65236a14074'

        endpoint = f'https://frost.met.no/locations/v0.jsonld?names={self.location}'

        request = rq.get(endpoint, auth=(client_id, ''))

        json = request.json()

        # Print error message if location is not valid/obtainable, #If ok, write to txt file to verify
        if request.status_code == 200:
            data = json['data']
            print('Data retrieved from frost.met.no!')
            f = open("WeatherLocation.txt", 'w')
            f.write(request.text)
            f.close()

        else:
            print('Error! Returned status code %s' % request.status_code)
            print('Message: %s' % json['error']['message'])
            print('Reason: %s' % json['error']['reason'])


        self.latitude = [data[0]["geometry"]["coordinates"][1]]
        self.longitude = [data[0]["geometry"]["coordinates"][0]]

        print(self.latitude, self.longitude)




pass


