import iris
import numpy as np
import matplotlib.pyplot as plt
import iris.quickplot as qplt
import iris.analysis

#cube_tmp = iris.load_cube('GLODAPv2.2016b.TCO2.nc','variable')
cube = iris.load_cube('/disk2/lr452/Downloads/GLODAPv2.2016b.TCO2.nc', 'moles of dissolved inorganic carbon per unit mass in seawater')

#cube.data = cube_tmp.data

#cube.add_dim_coord('depth_surface', 3)
print(cube)
#print(cube.data)
#print(cube.shape)
#print(cube.coord('latitude').points)
#print(cube.coord('depth').points)


max_depth = 100.0
indexes = np.where(cube.coord('depth').points <= max_depth)[0]
cube = cube[indexes]
average_across_depth = cube.collapsed(['depth'],iris.analysis.MEAN)

#print(average_across_depth.shape)

average_across_depth.coord('latitude').guess_bounds()
average_across_depth.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth)
cube1_average = average_across_depth.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube1_average.data)
#print(cube1_average.shape)
#print(cube1_average.coord('latitude').points)

cube1_n = np.mean(cube1_average.data[49])
cube1_s = np.mean(cube1_average.data[15])
cube1_av = np.mean(cube1_average.data[10:49])
cube1_dic = (cube1_n - cube1_s) / cube1_av
print(cube1_dic)
print(cube1_n)
print(cube1_s)
print(cube1_av)


#Extracting a region (Indian, Atlantic, or Pacific)
#west = 
#east = 20
#south = -75
#north = -40
#temporary_cube = average_across_depth.intersection(longitude = (west, east))
#cube_region = temporary_cube.intersection(latitude = (south,north))

#average_across_depth.coord('latitude').guess_bounds()
#average_across_depth.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth)
#global_average_variable = average_across_depth.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1 = cube1_average.coord('latitude').points
variable2 = cube1_average.data

print(variable1.shape)
print(variable2.shape)

#slope,intercept,r_value,p_value,std_err = linregress(variable1, variable2)
#print(slope)

plt.plot(variable1,variable2)
#plt.plot(variable1,(slope*variable1)+intercept)
plt.xlabel('latitude')
plt.ylabel('DIC concentration')
plt.xlim([-75, -40])
plt.show()
