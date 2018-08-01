from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import matplotlib
#matplotlib.use('Agg')
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FixedFormatter
import matplotlib.cm as cm

def graphSepDistance(atomNumberA, atomNumberB, sepDistance, atomNamesA, atomNamesB, filterAmount=None):
# print all colormaps
#    print cm.datad.keys()
    A, B, Z = prepareGraph(atomNumberA, atomNumberB, sepDistance,filterAmount)
    fig = plt.figure()
    majorYFormatter = FixedFormatter(atomNamesA)
    majorXFormatter = FixedFormatter(atomNamesB)
    majorXLocator = MaxNLocator(nbins=20,integer=True)
    majorYLocator = MaxNLocator(nbins=20,integer=True)
    plt.xticks( rotation=90 )
    ax = fig.add_subplot(111)
    CS = ax.contourf(B,A,Z,10,rstride=10,cstride=10,cmap=cm.hot_r)
    CB = plt.colorbar(CS, shrink=0.8, extend='both')
    CB.ax.set_ylabel('angstroms apart')
    ax.set_xlabel('Protein B')
    ax.set_ylabel('Protein A')
    ax.xaxis.set_major_locator(majorXLocator)
    ax.yaxis.set_major_locator(majorYLocator)
    ax.xaxis.set_major_formatter(majorXFormatter)
    ax.yaxis.set_major_formatter(majorYFormatter)
#    ax.yaxis.set_major_formatter(majorFormatter)
    ax.grid(True)
    fig.set_size_inches(19.2,12)
    plt.show()

    
def prepareGraph(atomNumberA, atomNumberB, value, filterAmount):
    A = np.array(atomNumberA)
    B = np.array(atomNumberB)
    S = np.array(value)
    #maximum = np.maximum(S)
    if filterAmount != None:
        for i in range(0,len(S)):
            if S[i] > filterAmount:
                S[i] = filterAmount
    A = np.unique(A)
    B = np.unique(B)
    Z = np.zeros((A.size,B.size))
    i = 0
    for x in range(0,A.size):
        for y in range(0,B.size):
            Z[x,y] = S[i]
            i=i+1
    return A,B,Z;
    
