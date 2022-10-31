import numpy as np

from getLocationandWeather import WeatherSymbol
import requests
import numpy
import matplotlib as mpl
from PIL import Image

with open("WeatherSymbol.txt") as f:
    symbol = f.readline()
    f.close()

weather_symbol = f'./png/{symbol}.png'

# Open image and convert to grey scale
img = Image.open(weather_symbol).convert('LA')

if IOError == 0:
    print("Error Importing Image")

# Defining verticies



















