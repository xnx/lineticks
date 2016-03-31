import numpy as np
import matplotlib.pyplot as plt
from lineticks import LineTicks

x = np.arange(0, 2*np.pi, np.pi/40)
y = np.sin(x)

fig, ax = plt.subplots()
circle_line, = ax.plot(x, y)
minor_ticks = LineTicks(circle_line, range(0, len(x), 2), 5, lw=2, color='k')
major_ticks = LineTicks(circle_line, range(0, len(x), 10), 20,lw=2,color='r', direction=-1)
plt.show()


