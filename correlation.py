import iris 
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
from scipy.stats.mstats import *

variable1 = [0.2004, 0.2049, 0.2041, 0.1787, 0.1923, 0.1785, 0.128, 0.1997, 0.1919, 0.198]
variable2 = [51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 46.11, 49.16, 53.81, 51.78]

slope,intercept,r_value,p_value,std_err = linregress(variable2, variable1)
correlation = spearmanr(variable2, variable1)
print(correlation)

plt.scatter(variable2[0], variable1[0],label='ACCESS-ESM1-5')
plt.scatter(variable2[1], variable1[1],label='CanESM5')
plt.scatter(variable2[2], variable1[2],label='CESM2')
plt.scatter(variable2[3], variable1[3],label='GFDL-CM4')
plt.scatter(variable2[4], variable1[4],label='GISS-E2-1-G')
plt.scatter(variable2[5], variable1[5],label='IPSL-CM6A-LR')
plt.scatter(variable2[6], variable1[6],label='MIROC-ES2L')
plt.scatter(variable2[7], variable1[7],label='MPI-ESM1-2-LR')
plt.scatter(variable2[8], variable1[8],label='NorESM2-MM')
plt.scatter(variable2[9], variable1[9],label='UKESM1-0-LL')
#plt.plot(variable1,(slope*variable1)+intercept)
plt.xlabel('Latitude to maximum wind stress')
plt.ylabel('Wind speed')
plt.legend()
plt.show()
