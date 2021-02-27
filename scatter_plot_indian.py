import iris 
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
from scipy.stats.mstats import *
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature


#Load in model data
cube1 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube2 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_CanESM5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube3 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_CESM2_historical_r1i1p1f1_gr_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube4 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_GFDL-CM4_historical_r1i1p1f1_gr_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube5 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_GISS-E2-1-G_historical_r101i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube6 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_IPSL-CM6A-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube7 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_MIROC-ES2L_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube8 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube9 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_NorESM2-MM_historical_r1i1p1f1_gr_199401-201412.rg.yr.so.fix.mask.nc','dissic')
cube10 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_UKESM1-0-LL_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')



###CUBE 1
#Time average, depth average and longitude average 
average_across_time1 = cube1.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time1.coord('depth').points <= max_depth)[0]
average_across_time1 = average_across_time1[indexes]
average_across_depth1 = average_across_time1.collapsed(['depth'],iris.analysis.MEAN)

#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube = average_across_depth1.intersection(longitude = (west, east))
temporary_cubeb = temporary_cube.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cubeb.coord('latitude').guess_bounds()
temporary_cubeb.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cubeb)
cube1_average = temporary_cubeb.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)


#print(cube1_average)
#print(cube1_average.coord('latitude').points)

#average_across_time1d = cube1.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time1d.coord('depth').points <= max_depthd)[0]
#average_across_time1d = average_across_time1d[indexesd]
#average_across_depth1d = average_across_time1d.collapsed(['depth'],iris.analysis.MEAN)

#average_across_depth1d.coord('latitude').guess_bounds()
#average_across_depth1d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth1d)
#cube1d_average = average_across_depth1d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube1_n = np.mean(cube1_average.data[28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_s = np.mean(cube1_average.data[17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_av = np.mean(cube1_average.data[17:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_dic = (cube1_n - cube1_s) / cube1_av
print(cube1_dic) 


###CUBE 2
#Time average, depth average and longitude average 
average_across_time2 = cube2.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time2.coord('depth').points <= max_depth)[0]
average_across_time2 = average_across_time2[indexes]
average_across_depth2 = average_across_time2.collapsed(['depth'],iris.analysis.MEAN)

#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube2 = average_across_depth2.intersection(longitude = (west, east))
temporary_cube2b = temporary_cube2.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube2b.coord('latitude').guess_bounds()
temporary_cube2b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube2b)
cube2_average = temporary_cube2b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)


#print(cube1_average)
#print(cube1_average.coord('latitude').points)

#average_across_time1d = cube1.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time1d.coord('depth').points <= max_depthd)[0]
#average_across_time1d = average_across_time1d[indexesd]
#average_across_depth1d = average_across_time1d.collapsed(['depth'],iris.analysis.MEAN)

#average_across_depth1d.coord('latitude').guess_bounds()
#average_across_depth1d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth1d)
#cube1d_average = average_across_depth1d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube2_n = np.mean(cube2_average.data[28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_s = np.mean(cube2_average.data[17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_av = np.mean(cube2_average.data[17:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_dic = (cube2_n - cube2_s) / cube2_av
print(cube2_dic)  

###CUBE 3
#Time average, depth average and longitude average 
average_across_time3 = cube3.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time3.coord('ocean model level').points <= max_depth)[0]
average_across_time3 = average_across_time3[indexes]
average_across_depth3 = average_across_time3.collapsed(['ocean model level'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube3 = average_across_depth3.intersection(longitude = (west, east))
temporary_cube3b = temporary_cube3.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube3b.coord('latitude').guess_bounds()
temporary_cube3b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube3b)
cube3_average = temporary_cube3b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube3_average.coord('latitude').points)

#average_across_time3d = cube3.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time3d.coord('ocean model level').points <= max_depthd)[0]
#average_across_time3d = average_across_time3d[indexesd]
#average_across_depth3d = average_across_time3d.collapsed(['ocean model level'],iris.analysis.MEAN)

#average_across_depth3d.coord('latitude').guess_bounds()
#average_across_depth3d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth3d)
#cube3d_average = average_across_depth3d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube3_n = np.mean(cube3_average.data[26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_s = np.mean(cube3_average.data[16])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_av = np.mean(cube3_average.data[16:26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_dic = (cube3_n - cube3_s) / cube3_av
print(cube3_dic)

###CUBE 4
#Time average, depth average and longitude average 
average_across_time4 = cube4.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time4.coord('ocean model level').points <= max_depth)[0]
average_across_time4 = average_across_time4[indexes]
average_across_depth4 = average_across_time4.collapsed(['ocean model level'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube4 = average_across_depth4.intersection(longitude = (west, east))
temporary_cube4b = temporary_cube4.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube4b.coord('latitude').guess_bounds()
temporary_cube4b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube4b)
cube4_average = temporary_cube4b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube4_average.coord('latitude').points)

#average_across_time4d = cube4.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time4d.coord('ocean model level').points <= max_depthd)[0]
#average_across_time4d = average_across_time4d[indexesd]
#average_across_depth4d = average_across_time4d.collapsed(['ocean model level'],iris.analysis.MEAN)

#average_across_depth4d.coord('latitude').guess_bounds()
#average_across_depth4d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth4d)
#cube4d_average = average_across_depth4d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube4_n = np.mean(cube4_average.data[27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_s = np.mean(cube4_average.data[18])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_av = np.mean(cube4_average.data[18:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_dic = (cube4_n - cube4_s) / cube4_av
print(cube4_dic)

###CUBE 5
#Time average, depth average and longitude average 
average_across_time5 = cube5.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time5.coord('depth').points <= max_depth)[0]
average_across_time5 = average_across_time5[indexes]
average_across_depth5 = average_across_time5.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube5 = average_across_depth5.intersection(longitude = (west, east))
temporary_cube5b = temporary_cube5.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube5b.coord('latitude').guess_bounds()
temporary_cube5b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube5b)
cube5_average = temporary_cube5b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5_average.coord('latitude').points)

#average_across_time5d = cube5.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time5d.coord('depth').points <= max_depthd)[0]
#average_across_time5d = average_across_time5d[indexesd]
#average_across_depth5d = average_across_time5d.collapsed(['depth'],iris.analysis.MEAN)

#average_across_depth5d.coord('latitude').guess_bounds()
#average_across_depth5d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth5d)
#cube5d_average = average_across_depth5d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube5_n = np.mean(cube5_average.data[19])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_s = np.mean(cube5_average.data[15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_av = np.mean(cube5_average.data[15:19])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_dic = (cube5_n - cube5_s) / cube5_av
print(cube5_dic)

###CUBE 6
#Time average, depth average and longitude average 
average_across_time6 = cube6.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time6.coord('Vertical T levels').points <= max_depth)[0]
average_across_time6 = average_across_time6[indexes]
average_across_depth6 = average_across_time6.collapsed(['Vertical T levels'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube6 = average_across_depth6.intersection(longitude = (west, east))
temporary_cube6b = temporary_cube6.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube6b.coord('latitude').guess_bounds()
temporary_cube6b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube6b)
cube6_average = temporary_cube6b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube6_average.coord('latitude').points)

#average_across_time6d = cube6.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time6d.coord('Vertical T levels').points <= max_depthd)[0]
#average_across_time6d = average_across_time6d[indexesd]
#average_across_depth6d = average_across_time6d.collapsed(['Vertical T levels'],iris.analysis.MEAN)

#average_across_depth6d.coord('latitude').guess_bounds()
#average_across_depth6d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth6d)
#cube6d_average = average_across_depth6d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube6_n = np.mean(cube6_average.data[29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_s = np.mean(cube6_average.data[18])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_av = np.mean(cube6_average.data[18:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_dic = (cube6_n - cube6_s) / cube6_av
print(cube6_dic)


###CUBE 7
#Time average, depth average and longitude average 
average_across_time7 = cube7.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time7.coord('ocean sigma over z coordinate').points <= max_depth)[0]
average_across_time7 = average_across_time7[indexes]
average_across_depth7 = average_across_time7.collapsed(['ocean sigma over z coordinate'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube7 = average_across_depth7.intersection(longitude = (west, east))
temporary_cube7b = temporary_cube7.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube7b.coord('latitude').guess_bounds()
temporary_cube7b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube7b)
cube7_average = temporary_cube7b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube7_average.coord('latitude').points)

#average_across_time7d = cube7.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time7d.coord('ocean sigma over z coordinate').points <= max_depthd)[0]
#average_across_time7d = average_across_time7d[indexesd]
#average_across_depth7d = average_across_time7d.collapsed(['ocean sigma over z coordinate'],iris.analysis.MEAN)

#average_across_depth7d.coord('latitude').guess_bounds()
#average_across_depth7d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth7d)
#cube7d_average = average_across_depth7d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube7_n = np.mean(cube7_average.data[29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_s = np.mean(cube7_average.data[22])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_av = np.mean(cube7_average.data[22:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_dic = (cube7_n - cube7_s) / cube7_av
print(cube7_dic)

###CUBE 8
#Time average, depth average and longitude average 
average_across_time8 = cube8.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time8.coord('depth').points <= max_depth)[0]
average_across_time8 = average_across_time8[indexes]
average_across_depth8 = average_across_time8.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube8 = average_across_depth8.intersection(longitude = (west, east))
temporary_cube8b = temporary_cube8.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube8b.coord('latitude').guess_bounds()
temporary_cube8b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube8b)
cube8_average = temporary_cube8b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube8_average.coord('latitude').points)

#average_across_time8d = cube8.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time8d.coord('depth').points <= max_depthd)[0]
#average_across_time8d = average_across_time8d[indexesd]
#average_across_depth8d = average_across_time8d.collapsed(['depth'],iris.analysis.MEAN)

#average_across_depth8d.coord('latitude').guess_bounds()
#average_across_depth8d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth8d)
#cube8d_average = average_across_depth8d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube8_n = np.mean(cube8_average.data[30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_s = np.mean(cube8_average.data[18])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_av = np.mean(cube8_average.data[18:30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_dic = (cube8_n - cube8_s) / cube8_av
print(cube8_dic)


###CUBE 9
#Time average, depth average and longitude average 
average_across_time9 = cube9.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time2.coord('depth').points <= max_depth)[0]
average_across_time9 = average_across_time9[indexes]
average_across_depth9 = average_across_time9.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube9 = average_across_depth9.intersection(longitude = (west, east))
temporary_cube9b = temporary_cube9.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube9b.coord('latitude').guess_bounds()
temporary_cube9b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube9b)
cube9_average = temporary_cube9b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube9_average.coord('latitude').points)

#average_across_time9d = cube1.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time9.coord('depth').points <= max_depthd)[0]
#average_across_time9d = average_across_time9[indexesd]
#average_across_depth9d = average_across_time9d.collapsed(['depth'],iris.analysis.MEAN)

#average_across_depth9d.coord('latitude').guess_bounds()
#average_across_depth9d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth9d)
#cube9d_average = average_across_depth9d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube9_n = np.mean(cube9_average.data[26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_s = np.mean(cube9_average.data[16])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_av = np.mean(cube9_average.data[16:25])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_dic = (cube9_n - cube9_s) / cube9_av
print(cube9_dic)

###CUBE 10
#Time average, depth average and longitude average 
average_across_time10 = cube10.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time9.coord('depth').points <= max_depth)[0]
average_across_time10 = average_across_time10[indexes]
average_across_depth10 = average_across_time10.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube10 = average_across_depth10.intersection(longitude = (west, east))
temporary_cube10b = temporary_cube10.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube10b.coord('latitude').guess_bounds()
temporary_cube10b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube10b)
cube10_average = temporary_cube10b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube10_average.coord('latitude').points)

#average_across_time10d = cube10.collapsed(['time'],iris.analysis.MEAN)
#max_depthd = 250.0
#indexesd = np.where(average_across_time10d.coord('depth').points <= max_depthd)[0]
#average_across_time10d = average_across_time10d[indexesd]
#average_across_depth10d = average_across_time10d.collapsed(['depth'],iris.analysis.MEAN)

#average_across_depth10d.coord('latitude').guess_bounds()
#average_across_depth10d.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth10d)
#cube10d_average = average_across_depth10d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube10_n = np.mean(cube10_average.data[28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_s = np.mean(cube10_average.data[17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_av = np.mean(cube10_average.data[17:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_dic = (cube10_n - cube10_s) / cube10_av
print(cube10_dic)


#Load wind data
wind_variable = [51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 46.11, 49.16, 53.81, 51.78]


variable1 = [cube1_dic, cube2_dic, cube3_dic, cube4_dic, cube5_dic, cube6_dic, cube7_dic, cube8_dic, cube9_dic, cube10_dic]
variable2 = wind_variable 

slope,intercept,r_value,p_value,std_err = linregress(variable2, variable1)
print(slope)

plt.scatter(variable2, variable1)
#plt.plot(variable2,(slope*variable2)+intercept)
#plt.legend()
plt.show()
