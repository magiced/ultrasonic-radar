# https://matplotlib.org/stable/api/animation_api.html

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,


# https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),init_func=init, blit=True)

ani = FuncAnimation(fig, update, frames=np.linspace(0,10), init_func=init)#, blit=True)

plt.show()