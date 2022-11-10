import time
from getLocationandWeather import WeatherSymbol
from Conv import STL
import re


# Function for converting return statement from location class, and printing terminal messages
def convert(a, b):
    symbol_str = re.sub('[^a-zA-Z_]+', '', a)  # Extracting characters and symbols only from the return statement get_weather_symbol
    speed = re.findall(r'[-+]?(?:\d*\.\d+|\d+)', a) # Extracting the float number representing wind speed
    speed_str = ""

    for x in speed: # Converting from list to string
        speed_str += x

    print(f'You chose {b}!')
    time.sleep(2)
    print(f'{b} will be {symbol_str} for the next 6 hours.')  # Printing the forecast
    time.sleep(2)
    print(f'The wind speed is {speed_str}')
    return symbol_str, speed_str


def main():
    location = input("Enter your desired location!: ")

    my_location = WeatherSymbol(location) # Send location to weather symbol class
    init_weather = my_location.acquire_location() # Initiate the first function to get weather data

    init_symbol = my_location.get_weather_symbol()
    symbol, wind = convert(init_symbol, location)

    my_stl = STL(symbol, wind) # Initializing the STL class
    my_cube = my_stl.bottom_mesh() # Running the function to create bottom plate stl file
    my_symbol = my_stl.symbol_mesh() # Running the function to create symbol stl file
    my_speed = my_stl.wind_speed() # Running the function to create windspeed
    my_final_file = my_stl.mergeSTL() # Run the function to merge the bottom plate and symbol stl files


if __name__ == "__main__":
    main()



























