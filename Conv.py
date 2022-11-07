import numpy as np
from stl import mesh
from PIL import Image
import stl


class STL:

    def __init__(self, location):
        self.location = location

    def bottom_mesh(self): # Creating a basic cube, with same length and width as png file. Height is smaller (3mm).
        verticies = np.array([ \
            [0, 0, 3],
            [0, 100, 3],
            [100, 100, 3],
            [100, 0, 3],
            [0, 0, 0],
            [0, 100, 0],
            [100, 100, 0],
            [100, 0, 0]])

        faces = np.array([ \
            [0, 2, 1],
            [0, 3, 2],

            [0, 1, 5],
            [0, 5, 4],

            [5, 1, 2],
            [5, 2, 6],

            [3, 6, 2],
            [3, 7, 6],

            [0, 4, 7],
            [0, 7, 3],

            [4, 7, 6],
            [4, 6, 5]]) # Creating the 12 triangles for the cube, so that we can mesh it

        shape = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

        for i, f in enumerate(faces):
            for j in range(3):
                shape.vectors[i][j] = verticies[f[j], :]

        self.bottomstl = shape.save("bottom.stl")


    def symbol_mesh(self):

        with open("WeatherSymbol.txt") as f:
            symbol = f.readline()
            f.close()

        weather_symbol = f'./png/{symbol}.png' # Using the line that was read from the txt file to load correct png

        # Open image and convert to grey scale
        try:
            img = Image.open(weather_symbol).convert('L') # L is the conversion from RGB to grey
        except IOError:
            print("Error Importing Image")

        # Creating 2D shape of the image. LengthxWidth = 100 x 100 mm, max height is 1 cm
        max_size = (100, 100)
        max_height = 10
        min_height = 0

        img.thumbnail(max_size)
        numImg = np.array(img)
        maxPixels = numImg.max()

        (columns, rows) = img.size

        verticies = np.zeros((rows, columns, 3))

        for x in range(0, columns):
            for y in range(0, rows):
                intensity = numImg[y][x]
                z = (intensity * max_height) / maxPixels
                verticies[y][x] = (x, y, z)

        faces = []

        # Face 1
        for x in range(0, columns - 1):
            for y in range(0, rows - 1):

                one = verticies[y][x]
                two = verticies[y+1][x]
                three = verticies[y+1][x+1]
                face1 = np.array([one, two, three])

                # Face 2
                one = verticies[y][x]
                two = verticies[y][x+1]
                three = verticies[y+1][x+1]

                face2 = np.array([one, two, three])

                faces.append(face1)
                faces.append(face2)

        facesNum = np.array(faces)

        # Creating mesh
        surface = mesh.Mesh(np.zeros(facesNum.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(faces):
            for j in range(3):
                surface.vectors[i][j] = facesNum[i][j]

        # Write mesh to file
        self.surfacestl = surface.save('symbol.stl')


    def mergeSTL(self):
        file_one = mesh.Mesh.from_file('./bottom.stl')
        file_two = mesh.Mesh.from_file('./symbol.stl')

        combined = mesh.Mesh(np.concatenate([file_one.data, file_two.data]))
        combined.save('merged.stl', mode=stl.Mode.ASCII)

        print('STL file complete! "merged.stl is the final product ready for 3D printing!')
        print('Check the project folder to find your file!')



























