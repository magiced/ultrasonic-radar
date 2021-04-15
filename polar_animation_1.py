# https://matplotlib.org/stable/api/animation_api.html

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(dpi=100)
ax = fig.add_subplot(111, projection='polar')
ax.set_facecolor("blue")

ax.set_rmax(1)
ax.set_rticks([0.25, 0.5, 0.75, 1])  # Less radial ticks
# ax.set_rorigin(90)
ax.set_theta_direction(-1)
ax.set_theta_zero_location(loc="N")

angle = 0
rad = 1
#radians = degrees x π/180°
angle_vals = [0,angle*np.pi/180]
rad_vals = [0,rad]

sweep, = ax.plot(angle_vals, rad_vals, c="white", alpha=1)
# ping, = ax.scatter(np.pi,0.69, c="white", alpha=1)


def init():
    sweep.set_data(angle_vals, rad_vals)
    return sweep,

def update(frame):
    global angle
    angle += 1
    if angle > 359:
        angle = 0

    angle_vals = [0,angle*np.pi/180]
    rad_vals = [0,rad]
    sweep.set_data(angle_vals, rad_vals)
    return sweep,

# https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation

ani = FuncAnimation(fig, update, init_func=init, interval = 25, blit=True)

plt.show()