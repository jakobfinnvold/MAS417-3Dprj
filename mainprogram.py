# Libraries for API Moretest from other laptop


import requests
import re


#Icon Values
rain_icon = 9
cloud_icon = 4
sun_icon = 1


# Classes


class Weather:
    def __init__(self, icon, img):
        self.icon = icon
        self.img = img

    def image(self, img):
        return f"{self.img}"

    pass


class Cloudy(Weather):
    imgC = "04.svg"

    def image(self, img=imgC):
        return super().image(img)

    pass


class Rain(Weather):
    imgR = "09.svg"

    def image(self, img=imgR):
        return super().image(img)

    pass


class Sun(Weather):
    imgS = "01d.svg"

    def image(self, img=imgS):
        return super().image(img)

    pass

# Functions


def w_function():
    f = open('Weatherdata.txt', 'w')
    wrt = r.text
    f.write(wrt)
    f.close()


def r_function():
    f = open('Weatherdata.txt', 'r')
    value_line = f.readlines()
    value_str = value_line[17]
    value_nbr = re.findall(r'\d', value_str)
    int_nbr = [int(x) for x in value_nbr]
    print("Weather icon value is", int_nbr)
    f.close()
    return int_nbr


client_id = 'bcfc74f6-c102-4435-8c22-d65236a14074'

# ID for Grimstad -> SN38140 | Krs SN39210
endpoint = 'https://frost.met.no/observations/v0.jsonld'
parameters = {
    'sources' : 'SN18700',
    'elements' : 'over_time(weather_cloud_symbol PT6H)',
    'referencetime' : '2022-10-25T12',
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

w_function()
icon_value = r_function()


if icon_value == [rain_icon]:
    rain_img = Rain(icon_value, "09.svg")
elif icon_value == [cloud_icon]:
    cloud_image = Cloudy(icon_value, "04.svg")
    print("Cloud")
elif icon_value == [sun_icon]:
    sun_image = Sun(icon_value, "01.svg")
else:
    print("This image is not available")
