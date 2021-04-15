# https://matplotlib.org/stable/api/animation_api.html

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata = 0
ydata = 0
ln, = plt.plot(xdata, ydata, 'ro')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def update(frame):
    xdata = random.randint(0,10)
    ydata = random.randint(0,10)
    ln.set_data(xdata, ydata)
    return ln,


# https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),init_func=init, blit=True)

ani = FuncAnimation(fig, update, frames=np.linspace(0,10), init_func=init, interval = 100)#, blit=True)

plt.show()