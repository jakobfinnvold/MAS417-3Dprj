import requests as rq
import time
from getLocationandWeather import WeatherSymbol

location = input("Enter your desired location!: ")

my_location = WeatherSymbol(location)
print(my_location.get_weather_symbol())

with open("WeatherSymbol.txt") as f:
    symbol = f.readlines()
    print(symbol)























