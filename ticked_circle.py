import numpy as np
import matplotlib.pyplot as plt
from lineticks import LineTicks

theta = np.arange(0, 2*np.pi, np.pi/40)
x, y = np.cos(theta), np.sin(theta)

fig, ax = plt.subplots()
ax.set_aspect('equal')
circle_line, = ax.plot(x, y)
minor_ticks = LineTicks(circle_line, range(0, len(x), 2), 5, lw=2, color='k')
major_ticks = LineTicks(circle_line, range(0, len(x), 10), 20,lw=2,color='r')
plt.show()

