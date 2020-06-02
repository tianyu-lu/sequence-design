import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def ackley(x):
	x = np.array(x)
	return -20*np.exp(-0.2 * np.sqrt(np.sum(x**2, axis=0)/x.shape[0])) - np.exp(np.sum(np.cos(2*math.pi*x), axis=0)/x.shape[0]) + 20 + np.exp(1)

def ackley_grid(X, Y):
	grid = np.stack((X, Y))
	return ackley(grid)

np.random.seed(1234)
data = np.zeros((60000, 291))
for i in range(60000):
	x1 = np.random.default_rng().uniform(-32.768, 32.768, 290)
	y = ackley(x1)
	data[i,:-1] = x1
	data[i,-1] = y
np.save("ackley_data.npy", data)

# x2 = np.random.default_rng().uniform(-32.768, 32.768, 20)
# x1, x2 = np.meshgrid(x1, x2)
# z = ackley_grid(x1, x2)

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.scatter(x1, x2, z)
# surf = ax.plot_surface(x1, x2, z, cmap=cm.Spectral,
#                        linewidth=0, antialiased=False)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()


