import scipy.io as sio
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D

data = sio.loadmat('data_map1.mat')

ALL = data["data_map"]
X = [i[0] for i in ALL]
Y = [i[1] for i in ALL]
Z = [i[2] for i in ALL]
z1 = Z


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot3D(X, Y, Z)
ax.legend()

plt.show()



