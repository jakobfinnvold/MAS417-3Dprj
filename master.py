import time
from getLocationandWeather import WeatherSymbol
from Conv import STL

location = input("Enter your desired location!: ")

# Get the location
my_location = WeatherSymbol(location) # Send location to weather symbol class
init_weather = my_location.acquire_location() # Initiate the first function to get weather data
time.sleep(1)
r = my_location.get_weather_symbol() # Getting the forecast symbol
print(r) # Printing the forecast


# Input symbol char length and merge the stl files
my_stl = STL(location) # Initializing the STL class
my_cube = my_stl.bottom_mesh() # Running the function to create bottom plate stl file
my_symbol = my_stl.symbol_mesh() # Running the function to create symbol stl file
my_final_file = my_stl.mergeSTL() # Run the function to merge the bottom plate and symbol stl files




























