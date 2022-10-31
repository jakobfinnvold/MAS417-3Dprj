import numpy as np
from stl import mesh
from PIL import Image

with open("WeatherSymbol.txt") as f:
    symbol = f.readline()
    f.close()

weather_symbol = f'./png/{symbol}.png'

# Open image and convert to grey scale
try:
    img = Image.open(weather_symbol).convert('L')
except IOError:
    print("Error Importing Image")

# Creating 2D shape of the image
max_size = (100, 100)
max_height = 10
min_height = 0

img.thumbnail(max_size)
numImg = np.array(img)
maxPixels = numImg.max()
minPixels = numImg.min()

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
        one = verticies[-1][-1]
        two = verticies[+1][+1]
        three = verticies[+1][-1]
        face1 = np.array([one, two, three])

        one = verticies[y][x]
        two = verticies[y+1][x]
        three = verticies[y+1][x+1]
        face2 = np.array([one, two, three])

        # Face 2
        one = verticies[y][x]
        two = verticies[y][x+1]
        three = verticies[y+1][x+1]

        face3 = np.array([one, two, three])

        faces.append(face1)
        faces.append(face2)
        faces.append(face3)

print(f"Number of faces:  {len(faces)}")
facesNum = np.array(faces)

# Creating mesh
surface = mesh.Mesh(np.zeros(facesNum.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        surface.vectors[i][j] = facesNum[i][j]

# Write mesh to file
surface.save('symbol.stl')
print(surface)
























