import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()
grid = gridspec.GridSpec(ncols=3, nrows=3)

fig.add_subplot(grid[0, 0])
fig.add_subplot(grid[0, 1:])
fig.add_subplot(grid[1:, 0])
fig.add_subplot(grid[1:, 1:])

plt.show()