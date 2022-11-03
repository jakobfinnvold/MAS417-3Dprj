import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
import mpl_toolkits

verticies1 = np.array([\
    [0, 0, 10],
    [0, 100, 10],
    [100, 100, 10],
    [100, 0, 10],
    [0, 0, 0],
    [0, 100, 0],
    [100, 100, 0],
    [100, 0, 0]])

faces1 = np.array([\
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

    [2, 3, 2],
    [2, 3, 3]])


shape = mesh.Mesh(np.zeros(faces1.shape[0], dtype=mesh.Mesh.dtype))
shape1 = mesh.Mesh(np.zeros)
for i, f in enumerate(faces1):
    for j in range(3):
        shape.vectors[i][j] = verticies1[f[j], :]

shape.save("cube.stl")