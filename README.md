# MAS417-3Dprj

This repo contains all files used in the making of the 3D-Project

Python is the main language used

APIs -> [frost](https://frost.met.no/index.html) and https://api.met.no/weatherapi/weathericon/2.0/documentation

# Requirements
## Packages & libraries
* Numpy
* Numpystl
* requests
* Pillow
* Time

## Versions
The project is made using python 3.8 interpreter, so it is confirmed that the program runs using this enterpreter. No other interpreters are tried.

The stl files can be printed using a software of choice which accepts such files. In this case we use Ultimaker Cura. 

# How to run the program

The program can be ran either from terminal or using a suitable IDE. Both PyCharm and the Ubuntu terminal is tested, and works with the program. To run the program from terminal, use this command inside the project folder: 
  ```
   python3 master.py
  ```

From here the user is prompted to choose a location. This location is restricted to any place in Norway. Examples are Oslo, Grimstad or Kristiansand. The program will then retrieve information about the desired location of the user, and print a forecast for the chosen area for the next 6 hours. 

The final stl file will then be saved in the project folder, under the name "merged.stl". There will in addition be two more .stl files, which are the bottom plate and the weather icon itself. These are merged into the "merged.stl" file. This merged stl file is the weather symbol representing the forecast for the user selected area.  
