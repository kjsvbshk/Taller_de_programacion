import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir los vértices del cubo en coordenadas (x, y, z)
vertices = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]

# Definir las aristas del cubo conectando los vértices
aristas = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

# Dibujar 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar los vértices del cubo
for vertice in vertices:
    ax.scatter(vertice[0], vertice[1], vertice[2], color='r')

# Dibujar las aristas del cubo
for arista in aristas:
    ax.plot([vertices[arista[0]][0], vertices[arista[1]][0]],
            [vertices[arista[0]][1], vertices[arista[1]][1]],
            [vertices[arista[0]][2], vertices[arista[1]][2]], color='b')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()
