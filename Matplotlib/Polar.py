"""
================
Annotation Polar
================

"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

line, = ax.plot([np.pi/2, np.pi/2], [0, 1])

plt.show()
