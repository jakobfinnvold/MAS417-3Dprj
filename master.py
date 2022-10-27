import re
import time
from getLocation import WeatherLocation
from getWeather import WeatherSymbol

# Initializing the variables to go to WeatherLocation
longitude = 0
latitude = 0

def main():

    location = input("Enter your desired location!: ")

    my_location = WeatherLocation(location, latitude, longitude)
    my_weather = WeatherSymbol(location, latitude, longitude)

    print(my_location.acquire_location())
    print(my_weather.get_weather_data())



if __name__=="__main__":
    main()














