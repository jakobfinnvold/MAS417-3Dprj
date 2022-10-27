import re

from getLocation import WeatherLocation
from getWeather import WeatherSymbol


def read_location():
    f = open("WeatherLocation.txt", 'r')
    value_line1 = f.readlines()
    value_str1 = value_line1[17]
    value_nmb1 = re.findall(r'\d+\.\d+\d+\d+\d+', value_str1)
    f.close()
    latitude = value_nmb1[0]
    longitude = value_nmb1[1]

    print(latitude, longitude)
    my_weather = WeatherSymbol(latitude, longitude)
    return my_weather


location = input("Enter your desired location!: ")

my_location = WeatherLocation(location)

# Reading the location to get floating numbers to put in to WeatherSymbol
read_location()
















