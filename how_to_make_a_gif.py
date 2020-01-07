import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def generate_plot(t):
    '''animation function. This is called sequentially for every time t'''

    # remove the previous frame, if any
    fig.gca().remove()

    # now plot
    x = np.linspace(0., 1., 100)
    y = np.sin(2. * np.pi * (x - t))
    return plt.plot(x, y)

# create an empty figure
fig = plt.figure ()

# prepare a list of times
times = np.linspace(0., 5., 200.)

# render the animation
anim = animation.FuncAnimation(fig, generate_plot, frames=times, blit=True)

# save, install ffmpeg with  conda install -c conda-forge ffmpeg
writer = animation.writers['ffmpeg'](fps=20)
anim.save('animation.mp4', writer=writer)
