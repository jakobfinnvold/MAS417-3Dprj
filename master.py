import requests as rq
import time
from getLocationandWeather import WeatherSymbol

location = input("Enter your desired location!: ")

my_location = WeatherSymbol(location)

print(my_location.get_weather_symbol(), type(my_location))

























