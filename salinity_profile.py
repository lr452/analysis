import iris
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from scipy.stats.mstats import *

cube = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_GISS-E2-1-G_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')

print(cube) 
#print(cube.shape)


#Taking the mean value across the 20 years
average_across_time = cube.collapsed(['time'],iris.analysis.MEAN)

#Averaging across depth
max_depth = 100.0
indexes = np.where(average_across_time.coord('depth').points <= max_depth)[0]
average_across_time = average_across_time[indexes]
average_across_depth = average_across_time.collapsed(['depth'],iris.analysis.MEAN)

#Extracting a region (Indian, Atlantic, or Pacific)
#west = 40
#east = 120
#south = -65
#north = -40
#temporary_cube = average_across_depth.intersection(longitude = (west, east))
#cube_region = temporary_cube.intersection(latitude = (south,north))

#Averaging across lo
average_across_depth.coord('latitude').guess_bounds()
average_across_depth.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth)
global_average_variable = average_across_depth.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1 = global_average_variable.coord('latitude').points
variable2 = global_average_variable.data

my_result = global_average_variable.collapsed(['longitude', 'latitude'], iris.analysis.MIN)
print(my_result)
#print(variable1.shape)
#print(variable2.shape)

#slope,intercept,r_value,p_value,std_err = linregress(variable1, variable2)

#print(slope)

plt.scatter(variable1,variable2)
#plt.plot(variable1,(slope*variable1)+intercept)
plt.xlabel('latitude')
plt.ylabel('Salinity')
plt.show()
