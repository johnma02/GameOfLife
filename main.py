# Standard imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Set up empty Figure, Axes and Line objects
fig, ax = plt.subplots()
# Set axes limits so that the whole image is included
ax.set(xlim=(-0.1, 2*np.pi+0.1), ylim=(-1.1, 1.1))
# Draw a blank line
line, = ax.plot([], [])
# Define data - one sine wave
x = np.linspace(0, 2*np.pi, num=50)
y = np.sin(x)
# Define animate function
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,
# Pass to FuncAnimation
anim = FuncAnimation(fig, animate, frames=len(x)+1, interval=30, blit=True)
# Save in the current working directory
anim.save("Sin.gif")