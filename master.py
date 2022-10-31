import requests as rq
import time
from PIL import Image
from getLocationandWeather import WeatherSymbol

location = input("Enter your desired location!: ")

my_location = WeatherSymbol(location)
print(my_location.get_weather_symbol())

with open("WeatherSymbol.txt") as f:
    symbol = f.readline()

    f.close()


weather_symbol = f'./png/{symbol}.png'

print(weather_symbol)

try:
    img = Image.open(weather_symbol).convert('LA')
except IOError:
        print("Error Importing Image")

r = img.show(img)


























