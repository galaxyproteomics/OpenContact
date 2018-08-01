from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import numpy as np
import matplotlib
#matplotlib.use('Agg')
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

x = np.random.randn(8873)
y = np.random.randn(8873)

heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap, extent=extent)
plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#X = np.arange(-5, 5, 0.25)
#Y = np.arange(-5, 5, 0.25)
#X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
#print Z
#surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
#        linewidth=0, antialiased=False)
#ax.set_zlim3d(-1.01, 1.01)

#ax.w_zaxis.set_major_locator(LinearLocator(10))
#ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))

#fig.colorbar(surf, shrink=0.5, aspect=5)
#X, Y, Z = axes3d.get_test_data(0.05)
#ax.plot_surface(X,Y,Z,rstride=10, cstride=10)
#ax.contourf(X,Y,Z)
#ax.set_title("Title")
#ax.grid(True)
#fig.set_figheight(196)
#fig.set_figwidth(24)
#plt.show()
#plt.savefig("testgraph")
