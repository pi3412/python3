'''
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


x = np.array([-0.5,0.5,-0.5,0.5])
y = np.array([-1,-1,1,1])
z = np.array([0,0,0,0])

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlim(-1.01, 1.01)
ax.set_ylim(-1.01, 1.01)
ax.set_zlim(-1.01, 1.01)

ax.plot_trisurf(x, y, z, antialiased=True)

plt.show()
