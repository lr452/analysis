
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

average_across_depth1.coord('latitude').guess_bounds()
average_across_depth1.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth1)
cube1_average = average_across_depth1.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)


variable1a = cube1_average.coord('latitude').points
variable2a = cube1_average.data



###CUBE 2
#Time average, depth average and longitude average 
average_across_time2 = cube2.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time2.coord('depth').points <= max_depth)[0]
average_across_time2 = average_across_time2[indexes]
average_across_depth2 = average_across_time2.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth2.coord('latitude').guess_bounds()
average_across_depth2.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth2)
cube2_average = average_across_depth2.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1b = cube2_average.coord('latitude').points
variable2b = cube2_average.data 

###CUBE 3
#Time average, depth average and longitude average 
average_across_time3 = cube3.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time3.coord('ocean model level').points <= max_depth)[0]
average_across_time3 = average_across_time3[indexes]
average_across_depth3 = average_across_time3.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth3.coord('latitude').guess_bounds()
average_across_depth3.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth3)
cube3_average = average_across_depth3.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1c = cube3_average.coord('latitude').points
variable2c = cube3_average.data

###CUBE 4
#Time average, depth average and longitude average 
average_across_time4 = cube4.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time4.coord('ocean model level').points <= max_depth)[0]
average_across_time4 = average_across_time4[indexes]
average_across_depth4 = average_across_time4.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth4.coord('latitude').guess_bounds()
average_across_depth4.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth4)
cube4_average = average_across_depth4.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1d = cube4_average.coord('latitude').points
variable2d = cube4_average.data

###CUBE 5
#Time average, depth average and longitude average 
average_across_time5 = cube5.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time5.coord('depth').points <= max_depth)[0]
average_across_time5 = average_across_time5[indexes]
average_across_depth5 = average_across_time5.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth5.coord('latitude').guess_bounds()
average_across_depth5.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth5)
cube5_average = average_across_depth5.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1e = cube5_average.coord('latitude').points
variable2e = cube5_average.data

###CUBE 6
#Time average, depth average and longitude average 
average_across_time6 = cube6.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time6.coord('Vertical T levels').points <= max_depth)[0]
average_across_time6 = average_across_time6[indexes]
average_across_depth6 = average_across_time6.collapsed(['Vertical T levels'],iris.analysis.MEAN)

average_across_depth6.coord('latitude').guess_bounds()
average_across_depth6.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth6)
cube6_average = average_across_depth6.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1f = cube6_average.coord('latitude').points
variable2f = cube6_average.data


###CUBE 7
#Time average, depth average and longitude average 
average_across_time7 = cube7.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time7.coord('ocean sigma over z coordinate').points <= max_depth)[0]
average_across_time7 = average_across_time7[indexes]
average_across_depth7 = average_across_time7.collapsed(['ocean sigma over z coordinate'],iris.analysis.MEAN)

average_across_depth7.coord('latitude').guess_bounds()
average_across_depth7.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth7)
cube7_average = average_across_depth7.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1g = cube7_average.coord('latitude').points
variable2g = cube7_average.data

###CUBE 8
#Time average, depth average and longitude average 
average_across_time8 = cube8.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time8.coord('depth').points <= max_depth)[0]
average_across_time8 = average_across_time8[indexes]
average_across_depth8 = average_across_time8.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth8.coord('latitude').guess_bounds()
average_across_depth8.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth8)
cube8_average = average_across_depth8.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1h = cube8_average.coord('latitude').points
variable2h = cube8_average.data


###CUBE 9
#Time average, depth average and longitude average 
average_across_time9 = cube9.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time2.coord('depth').points <= max_depth)[0]
average_across_time9 = average_across_time9[indexes]
average_across_depth9 = average_across_time9.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth9.coord('latitude').guess_bounds()
average_across_depth9.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth9)
cube9_average = average_across_depth9.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1i = cube9_average.coord('latitude').points
variable2i = cube9_average.data

###CUBE 10
#Time average, depth average and longitude average 
average_across_time10 = cube10.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time9.coord('depth').points <= max_depth)[0]
average_across_time10 = average_across_time10[indexes]
average_across_depth10 = average_across_time10.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth10.coord('latitude').guess_bounds()
average_across_depth10.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth10)
cube10_average = average_across_depth10.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

variable1j = cube10_average.coord('latitude').points
variable2j = cube10_average.data


plt.plot(variable1a, variable2a,label='ACCESS-ESM1-5')
plt.plot(variable1b, variable2b,label='CanESM5')
plt.plot(variable1c, variable2c,label='CESM2')
plt.plot(variable1d, variable2d,label='GFDL-CM4')
#plt.plot(variable1e, variable2e,label='GISS-E2-1-G')
plt.plot(variable1f, variable2f,label='IPSL-CM6A-LR')
plt.plot(variable1g, variable2g,label='MIROC-ES2L')
plt.plot(variable1h, variable2h,label='MPI-ESM1-2-LR')
plt.plot(variable1i, variable2i,label='NorESM2-MM')
plt.plot(variable1j, variable2j,label='UKESM1-0-LL')
#plt.plot(variable2,(slope*variable2)+intercept)
plt.legend(bbox_to_anchor=(1.02,0.8), loc='centre left')
plt.tight_layout()
plt.show()
