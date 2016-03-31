import numpy as np
import matplotlib.pyplot as plt
from lineticks import LineTicks

# Acceleration due to gravity, m.s-2
g = 9.81
# Initial speed (m.s-1) and launch angle (deg)
v0, alpha_deg = 40, 45
alpha = np.radians(alpha_deg)

# Time of flight
tmax = 2 * v0 * np.sin(alpha) / g

# Grid of time points, and (x,y) coordinates of trajectory
n = 100
t = np.linspace(0, tmax, n)
x = v0 * t * np.cos(alpha)
y = - g * t**2 / 2 + v0 * t * np.sin(alpha)

fig, ax = plt.subplots(facecolor='w')
fig.suptitle('Trajectory of a projectile launched at {} m/s at an angle'
             ' of {}°'.format(v0, alpha_deg))
traj, = ax.plot(x, y, c='purple', lw=4)
ax.set_xlabel('Range /m')
ax.set_ylabel('Height /m')
ax.set_xlim(-20,x[-1]+10)

# Add major ticks every 10th time point and minor ticks every 4th;
# label the major ticks with the corresponding time in secs.
major_ticks = LineTicks(traj, range(0, n, 10), 10, lw=2,
                        label=['{:.2f} s'.format(tt) for tt in t[::10]])
minor_ticks = LineTicks(traj, range(0,n), 4, lw=1)

plt.show()
