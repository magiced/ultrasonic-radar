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

sweep_width = 20

# ping, = ax.scatter(np.pi,0.69, c="white", alpha=1)

#Maybe use this:
# https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection

sweeps = []
decay_coeff = 1/sweep_width
for i in range(1,sweep_width):
    angle_vals = [0,(angle-i)*np.pi/180]
    rad_vals = [0,rad]
    i, = ax.plot(angle_vals, rad_vals, c="white", alpha=1/(i))
    sweeps.append(i)

# add points

# another list of points, 360 for each degree point
# update based on angle and distance reading from servo/ultrasonic info
# decay alpha based on time of last reading

points = []
for i in range(360):
    point = ax.scatter(i*np.pi/180, 0.76,c="white", alpha=0.75)
    points.append(point)

sweeps = sweeps + points

# def init():
#     for line in sweeps:
#         angle_vals = [0,(angle-i)*np.pi/180]
#         rad_vals = [0,rad]
#         line.set_data(angle_vals, rad_vals)
#     return sweeps,

def update(frame):
    global angle
    angle += 1
    if angle > 359:
        angle = 0

    for i in range(sweep_width):
        angle_vals = [0,(angle-i)*np.pi/180]
        rad_vals = [0,rad]
        sweeps[i].set_data(angle_vals, rad_vals)
    return sweeps

# https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation

ani = FuncAnimation(fig, update,  interval = 7)#, blit=True) #init_func=init,

plt.show()