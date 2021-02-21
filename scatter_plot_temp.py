import iris 
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature


#Load in model data for DIC
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

#Load in model data for salinity 
cube1t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube2t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_CanESM5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube3t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_CESM2_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.depth.nc','thetao')
cube4t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_GFDL-CM4_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube5t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_GISS-E2-1-G_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube6t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_IPSL-CM6A-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube7t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_MIROC-ES2L_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube8t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube9t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_NorESM2-MM_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube10t = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_UKESM1-0-LL_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')


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

#print(cube1_average)
#print(cube1_average.coord('latitude').points)

cube1_n = np.mean(cube1_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_s = np.mean(cube1_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_av = np.mean(cube1_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_dic = (cube1_n - cube1_s) / cube1_av
print(cube1_dic) 


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

#print(cube2_average.coord('latitude').points)

cube2_n = np.mean(cube2_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_s = np.mean(cube2_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_av = np.mean(cube2_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_dic = (cube2_n - cube2_s) / cube2_av
print(cube2_dic) 

###CUBE 3
#Time average, depth average and longitude average 
average_across_time3 = cube3.collapsed(['time'],iris.analysis.MEAN)

#print(average_across_time3) 

max_depth = 100.0
indexes = np.where(average_across_time3.coord('ocean model level').points <= max_depth)[0]
average_across_time3 = average_across_time3[indexes]
average_across_depth3 = average_across_time3.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth3.coord('latitude').guess_bounds()
average_across_depth3.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth3)
cube3_average = average_across_depth3.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube3_average.coord('latitude').points)

cube3_n = np.mean(cube3_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_s = np.mean(cube3_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_av = np.mean(cube3_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_dic = (cube3_n - cube3_s) / cube3_av
print(cube3_dic)

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

#print(cube4_average.coord('latitude').points)

cube4_n = np.mean(cube4_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_s = np.mean(cube4_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_av = np.mean(cube4_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_dic = (cube4_n - cube4_s) / cube4_av
print(cube4_dic)

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

#print(cube5_average.coord('latitude').points)

cube5_n = np.mean(cube5_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_s = np.mean(cube5_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_av = np.mean(cube5_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_dic = (cube5_n - cube5_s) / cube5_av
print(cube5_dic)

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

#print(cube6_average.coord('latitude').points)

cube6_n = np.mean(cube6_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_s = np.mean(cube6_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_av = np.mean(cube6_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_dic = (cube6_n - cube6_s) / cube6_av
print(cube6_dic)


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

#print(cube7_average.coord('latitude').points)

cube7_n = np.mean(cube7_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_s = np.mean(cube7_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_av = np.mean(cube7_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_dic = (cube7_n - cube7_s) / cube7_av
print(cube7_dic)

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

#print(cube8_average.coord('latitude').points)

cube8_n = np.mean(cube8_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_s = np.mean(cube8_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_av = np.mean(cube8_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_dic = (cube8_n - cube8_s) / cube8_av
print(cube8_dic)


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

#print(cube9_average.coord('latitude').points)

cube9_n = np.mean(cube9_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_s = np.mean(cube9_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_av = np.mean(cube9_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_dic = (cube9_n - cube9_s) / cube9_av
print(cube9_dic)

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

#print(cube10_average.coord('latitude').points)

cube10_n = np.mean(cube10_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_s = np.mean(cube10_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_av = np.mean(cube10_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_dic = (cube10_n - cube10_s) / cube10_av
print(cube10_dic)


###CUBE 1 temperature
#Time average, depth average and longitude average 
average_across_time1t = cube1t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time1t.coord('depth').points <= max_depth)[0]
average_across_time1t = average_across_time1t[indexes]
average_across_depth1t = average_across_time1t.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth1t.coord('latitude').guess_bounds()
average_across_depth1t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth1t)
cube1t_average = average_across_depth1t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube1s_average)
#print(cube1s_average.coord('latitude').points)

cube1t_n = np.mean(cube1t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1t_s = np.mean(cube1t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1t_av = np.mean(cube1t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1t_temp = (cube1t_n - cube1t_s) / cube1t_av
print(cube1t_temp) 


###CUBE 2 temp
#Time average, depth average and longitude average 
average_across_time2t = cube2t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time2t.coord('depth').points <= max_depth)[0]
average_across_time2t = average_across_time2t[indexes]
average_across_depth2t = average_across_time2t.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth2t.coord('latitude').guess_bounds()
average_across_depth2t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth2t)
cube2t_average = average_across_depth2t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube2s_average)
#print(cube2s_average.coord('latitude').points)

cube2t_n = np.mean(cube2t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2t_s = np.mean(cube2t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2t_av = np.mean(cube2t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2t_temp = (cube2t_n - cube2t_s) / cube2t_av
print(cube2t_temp) 

###CUBE 3 temp
#Time average, depth average and longitude average 
average_across_time3t = cube3t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time3t.coord('lev').points <= max_depth)[0]
average_across_time3t = average_across_time3t[indexes]
average_across_depth3t = average_across_time3t.collapsed(['lev'],iris.analysis.MEAN)

average_across_depth3t.coord('latitude').guess_bounds()
average_across_depth3t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth3t)
cube3t_average = average_across_depth3t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube3s_average)
#print(cube3s_average.coord('latitude').points)

cube3t_n = np.mean(cube3t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3t_s = np.mean(cube3t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3t_av = np.mean(cube3t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3t_temp = (cube3t_n - cube3t_s) / cube3t_av
print(cube3t_temp) 

###CUBE 4 temp
#Time average, depth average and longitude average 
average_across_time4t = cube4t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time4t.coord('ocean model level').points <= max_depth)[0]
average_across_time4t = average_across_time4t[indexes]
average_across_depth4t = average_across_time4t.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth4t.coord('latitude').guess_bounds()
average_across_depth4t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth4t)
cube4t_average = average_across_depth4t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube4s_average)
#print(cube4s_average.coord('latitude').points)

cube4t_n = np.mean(cube4t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4t_s = np.mean(cube4t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4t_av = np.mean(cube4t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4t_temp = (cube4t_n - cube4t_s) / cube4t_av
print(cube4t_temp) 


###CUBE 5 temp
#Time average, depth average and longitude average 
average_across_time5t = cube5t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time5t.coord('depth').points <= max_depth)[0]
average_across_time5t = average_across_time5t[indexes]
average_across_depth5t = average_across_time5t.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth5t.coord('latitude').guess_bounds()
average_across_depth5t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth5t)
cube5t_average = average_across_depth5t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube5t_n = np.mean(cube5t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5t_s = np.mean(cube5t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5t_av = np.mean(cube5t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5t_temp = (cube5t_n - cube5t_s) / cube5t_av
print(cube5t_temp) 


###CUBE 6 salinity
#Time average, depth average and longitude average 
average_across_time6t = cube6t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time6t.coord('Vertical T levels').points <= max_depth)[0]
average_across_time6t = average_across_time6t[indexes]
average_across_depth6t = average_across_time6t.collapsed(['Vertical T levels'],iris.analysis.MEAN)

average_across_depth6t.coord('latitude').guess_bounds()
average_across_depth6t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth6t)
cube6t_average = average_across_depth6t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube6t_n = np.mean(cube6t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6t_s = np.mean(cube6t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6t_av = np.mean(cube6t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6t_temp = (cube6t_n - cube6t_s) / cube6t_av
print(cube6t_temp) 



###CUBE 7 salinity
#Time average, depth average and longitude average 
average_across_time7t = cube7t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time7t.coord('ocean sigma over z coordinate').points <= max_depth)[0]
average_across_time7t = average_across_time7t[indexes]
average_across_depth7t = average_across_time7t.collapsed(['ocean sigma over z coordinate'],iris.analysis.MEAN)

average_across_depth7t.coord('latitude').guess_bounds()
average_across_depth7t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth7t)
cube7t_average = average_across_depth7t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube7t_n = np.mean(cube7t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7t_s = np.mean(cube7t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7t_av = np.mean(cube7t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7t_temp = (cube7t_n - cube7t_s) / cube7t_av
print(cube7t_temp) 



###CUBE 8 salinity
#Time average, depth average and longitude average 
average_across_time8t = cube8t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time8t.coord('depth').points <= max_depth)[0]
average_across_time8t = average_across_time8t[indexes]
average_across_depth8t = average_across_time8t.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth8t.coord('latitude').guess_bounds()
average_across_depth8t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth8t)
cube8t_average = average_across_depth8t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube8t_n = np.mean(cube8t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8t_s = np.mean(cube8t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8t_av = np.mean(cube8t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8t_temp = (cube8t_n - cube8t_s) / cube8t_av
print(cube8t_temp) 


###CUBE 9 temp
#Time average, depth average and longitude average 
#average_across_time9t = cube9t.collapsed(['time'],iris.analysis.MEAN)

##print(cube9t## no depth dimension**

#max_depth = 100.0
#indexes = np.where(average_across_time9t.coord('potential density referenced to 2000 dbar').points <= max_depth)[0]
#average_across_time9t = average_across_time9t[indexes]
#average_across_depth9t = average_across_time9t.collapsed(['potential density referenced to 2000 dbar'],iris.analysis.MEAN)

#average_across_depth9t.coord('latitude').guess_bounds()
#average_across_depth9t.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth9t)
#cube9t_average = average_across_depth9t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

#cube9t_n = np.mean(cube9t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube9t_s = np.mean(cube9t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube9t_av = np.mean(cube9t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube9t_temp = (cube9t_n - cube9t_s) / cube9t_av
#print(cube9t_temp) 


###CUBE 10 salinity
#Time average, depth average and longitude average 
average_across_time10t = cube10t.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time10t.coord('depth').points <= max_depth)[0]
average_across_time10t = average_across_time10t[indexes]
average_across_depth10t = average_across_time10t.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth10t.coord('latitude').guess_bounds()
average_across_depth10t.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth10t)
cube10t_average = average_across_depth10t.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube10t_n = np.mean(cube10t_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10t_s = np.mean(cube10t_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10t_av = np.mean(cube10t_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10t_temp = (cube10t_n - cube10t_s) / cube10t_av
print(cube10t_temp) 


variable1 = [cube1_dic, cube2_dic, cube3_dic, cube4_dic, cube5_dic, cube6_dic, cube7_dic, cube8_dic, cube10_dic]
variable2 = [cube1t_temp, cube2t_temp, cube3t_temp, cube4t_temp, cube5t_temp, cube6t_temp, cube7t_temp, cube8t_temp, cube10t_temp]

plt.scatter(variable2, variable1)
#plt.legend()
plt.show()
