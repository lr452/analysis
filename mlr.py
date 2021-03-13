import numpy as np
import matplotlib.pyplot as plt

y = np.array([-0.03275, -0.018157, -0.01605, -0.01773, 0.00922, -0.045778, -0.01356, -0.02102, -0.02088, -0.02947]) #DIC 

x1 = np.array([51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 46.11, 49.16, 53.81, 51.78]) #lat of Tmax
x2 = np.array([0.2004, 0.2049, 0.2041, 0.1787, 0.1923, 0.1785, 0.128, 0.1997, 0.1919, 0.198]) #wind strength
x3 = np.array([62.47, 62.2, 63.59, 61.78, 64.63, 61.8, 57.7, 61.56, 63.81, 62.46]) #lat of maximum upwelling
x4 = np.array([50.5, 52.5, 52.5, 52.5, 56.5, 50.5, 50.5, 49.5, 53.5, 51.5]) #lat of downwelling
x5 = np.array([11.97, 9.7, 11.09, 9.28, 8.13, 11.3, 7.2, 12.06, 10.31, 10.96]) #distance between upwelling and downwelling
x6 = np.array([2.206, 2.238, 2.171, 2.24, 2.183, 2.236, 2.154, 2.154, 2.189, 2.233]) #DIC conc in upwelled water
x7 = np.array([2.135, 2.198, 2.137, 2.201, 2.203, 2.136, 2.125, 2.109, 2.144, 2.168]) #DIC conc in downwelled water

x = [x1,x2,x3,x4,x5,x6,x7]

X = np.column_stack(x+[[1]*len(x[0])])
m7,m6,m5,m4,m3,m2,m1,c = np.linalg.lstsq(X,y)[0]

plt.plot(y,'r')
plt.plot(m7*x7 + m6*x6 + m5*x5 + m4*x4 + m3*x3 + m2*x2 + m1*x1 + c, 'g--')
plt.show()
