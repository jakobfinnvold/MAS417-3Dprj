from PIL import Image
import re

class Temp:
    def __init__(self, length):
        self.length = length

    def get_temp(self):

        g = 'partially_cloudy'
        r = len(g)
        with open("WeatherSymbol.txt") as f:
            symbol = f.readline(r)
            rdline = r + 5
            t = f.readline(rdline)
            f.close()

        print(symbol, t)








