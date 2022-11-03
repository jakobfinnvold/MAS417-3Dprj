import requests as rq
import time
from PIL import Image
from getLocationandWeather import WeatherSymbol
from Conv import STL

location = input("Enter your desired location!: ")

my_location = WeatherSymbol(location) # Send location to weather symbol class
init_weather = my_location.acquire_location() # Initiate the first function to get weather data
time.sleep(1)
print(my_location.get_weather_symbol()) # Printing the forecast

my_stl = STL(location)
my_file = my_stl.symbol_mesh()
my_cube = my_stl.bottom_mesh()



























