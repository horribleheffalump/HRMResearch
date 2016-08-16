import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rc('text', usetex = True)
import pylab


filename = u"../Data/FR230-HRMV4-5BPM1137.txt"
t1, HR1 = np.loadtxt(filename, delimiter = ',', usecols=(0,4), unpack=True, dtype=float)
filename = u"../Data/FR235-Optical-HR-5BPM1139.txt"
t2, HR2 = np.loadtxt(filename, delimiter = ',', usecols=(0,4), unpack=True, dtype=float)
filename = u"../Data/FR630-HRM-TRI-5BPM1138.txt"
t3, HR3 = np.loadtxt(filename, delimiter = ',', usecols=(0,4), unpack=True, dtype=float)
filename = u"../Data/SuuntoAmbit3Peak-SCoscheMove_2015_11_25_23_11_39_Running.txt"
t4, HR4 = np.loadtxt(filename, delimiter = ',', usecols=(0,4), unpack=True, dtype=float)


from pylab import *

f = plt.figure(num=None, figsize=(10, 10), dpi=150, facecolor='w', edgecolor='k')


plt.subplots_adjust(left=0.06, bottom=0.07, right=0.98, top=0.95, wspace=0.1)
#plt.plot(t, X, 'x', color = 'blue')
plt.plot(t1, HR1, '-', color = 'red')
plt.plot(t2, HR2, '-', color = 'green')
plt.plot(t3, HR3, '-', color = 'blue')
plt.plot(t4, HR4, '-', color = 'black')


plt.show()