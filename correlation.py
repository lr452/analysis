import iris 
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
from scipy.stats.mstats import *

variable1 = np.array([2.099, 2.504, 1.109, 1.247, 1.576, 2.012, 0.587, 1.248, 2.368, 1.73])
variable2 = np.array([51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 46.11, 49.16, 53.81, 51.78])

slope,intercept,r_value,p_value,std_err = linregress(variable2, variable1)
print(slope)
correlation = spearmanr(variable1, variable2)
print(correlation)

fig, ax = plt.subplots()
ax.scatter(variable2[0], variable1[0], s=125, label='ACCESS-ESM1-5', marker='*', facecolor='orangered', edgecolor='black')
ax.scatter(variable2[1], variable1[1], s=100, label='CanESM5', marker='p', facecolor='gold', edgecolor='black')
ax.scatter(variable2[2], variable1[2], s=100, label='CESM2', marker='<', facecolor='yellowgreen', edgecolor='black')
ax.scatter(variable2[3], variable1[3], s=100, label='GFDL-CM4', marker='8', facecolor='dimgrey', edgecolor='black')
ax.scatter(variable2[4], variable1[4], s=100, label='GISS-E2-1-G', marker='s', facecolor='mediumaquamarine', edgecolor='black')
ax.scatter(variable2[5], variable1[5], s=100, label='IPSL-CM6A-LR', marker='P', facecolor='deepskyblue', edgecolor='black')
ax.scatter(variable2[6], variable1[6], s=100, label='MIROC-ES2L', marker='X', facecolor='darkviolet', edgecolor='black')
ax.scatter(variable2[7], variable1[7], s=100, label='MPI-ESM1-2-LR', marker='H', facecolor='hotpink', edgecolor='black')
ax.scatter(variable2[8], variable1[8], s=75, label='NorESM2-MM', marker='D', facecolor='steelblue', edgecolor='black')
plt.scatter(variable2[9], variable1[9], s=100, label='UKESM1-0-LL', marker='v', facecolor='darkcyan', edgecolor='black')
ax.set_facecolor('whitesmoke')
ax.grid(True)
plt.plot(variable2,(slope*variable2)+intercept, c='black', linewidth=1)
plt.xlabel('Lat of Tmax [$^\circ$S]', fontsize=9, fontweight='bold')
plt.ylabel('$\Delta$T [K]', fontsize=9, fontweight='bold')
#plt.ylim([-0.001, 0])
#plt.xlim([-0.012, 0.00])
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')
plt.legend(bbox_to_anchor=(1.02,0.8), loc='centre left', fontsize=6, frameon=False, prop=dict(weight='bold'))
plt.text(51.3, 0.65, 'r=0.333, p=0.35', fontweight='bold')
plt.tight_layout()
plt.show()


#np.array([-0.0253, -0.0138, -0.0185, -0.0186, 0.0426, -0.0397, -0.0098, -0.0123, -0.0115, -0.0255]) #DIC 

#[0.2004, 0.2049, 0.2041, 0.1787, 0.1923, 0.1785, 0.1997, 0.1919, 0.198  #Wind strength

#0.00334, 0.0001295, 0.0000593, 0.000124, 0.0003266, 0.00008918, 0.0000739, -0.000196, 0.0001899, 0.00009412 #JJA

#-0.000118, -0.0000786, 0.0001699, 0.000055, 0.0001665, 0.0000889, 0.00008542, 0.000404, 0.0002061, 0.000148 # DJF

#-0.0067, -0.0062, -0.0101, -0.0038, -0.0011, -0.0046, -0.0017, -0.0024, -0.006, -0.0082 #salinity dif

#[2.099, 2.504, 1.109, 1.247, 1.576, 2.012, 0.587, 1.248, 2.368, 1.73 #temp diff

#51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 46.11, 49.16, 53.81, 51.78

#0.0258, 0.0136, 0.0197, 0.0162, -0.0557, 0.0394, 0.0103, 0.0112, 0.0123, 0.0252 DJF DIC

#[0.0065, 0.006, 0.0099, 0.0034, 0.0007, 0.0036, 0.0016, 0.0022, 0.0059, 0.0078 DJF salinity


#-2.106, -2.575, -1.151, -1.303, -1.653, -2.177, -0.346, -1.241, -2.381, -1.786 DJF temp

#0.0265, 0.0141, 0.0207, 0.0166, -0.0546, 0.0406, 0.0101, 0.0124, 0.0126, 0.0262 JJA DIC

#[0.0068, 0.0064, 0.0104, 0.004, 0.0013, 0.0051, 0.0017, 0.0026, 0.0062, 0.0084 JJA salinity 

#-2.124, -2.599, -1.109, -1.276, -1.625, -2.163, -0.352, -1.261, -2.457, -1.78 JJA temp


#'$\Delta$T [K]'

#[62.47, 62.2, 63.59, 61.78, 64.63, 61.8, 57.7, 61.56, 63.81, 62.46

#[50.5, 52.5, 52.5, 52.5, 54.5, 50.5, 50.5, 49.5, 53.5, 51.5

# [$^\circ$S]

#[-0.0364, -0.01521, -0.0156, -0.0211, -0.0054, -0.0551, -0.01394, -0.0230, -0.0188, -0.0314 atlantic dic

#[-0.0274, -0.0132, -0.0116, -0.0103, 0.0204, -0.0465, -0.0133, -0.023, -0.0162, -0.025 indian dic

#[-0.0329, -0.0218, -0.0159, -0.0219, -0.0223, -0.0347, -0.0118, -0.0191, -0.0236, -0.0283 pacific dic

#11.97, 9.7, 11.09, 9.28, 8.13, 11.3, 7.2, 12.06, 10.31, 10.96 ud distance

#[2.206, 2.238, 2.171, 2.240, 2.183, 2.236, 2.154, 2.154, 2.189, 2.233 dic upwelled

#[2.135, 2.198, 2.137, 2.201, 2.203, 2.136, 2.125, 2.109, 2.144, 2.168 dic downwelled

#[-0.0253, -0.0138, -0.0185, -0.0186, 0.0426, -0.0397, -0.0123, -0.0115, -0.0255
