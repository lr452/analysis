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
cube1s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube2s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_CanESM5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube3s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_CESM2_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.depth.nc','so')
cube4s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_GFDL-CM4_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube5s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_GISS-E2-1-G_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube6s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_IPSL-CM6A-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube7s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_MIROC-ES2L_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube8s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube9s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_NorESM2-MM_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')
cube10s = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_UKESM1-0-LL_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','so')


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


###CUBE 1 salinity
#Time average, depth average and longitude average 
average_across_time1s = cube1s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time1s.coord('depth').points <= max_depth)[0]
average_across_time1s = average_across_time1s[indexes]
average_across_depth1s = average_across_time1s.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth1s.coord('latitude').guess_bounds()
average_across_depth1s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth1s)
cube1s_average = average_across_depth1s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube1s_average)
#print(cube1s_average.coord('latitude').points)

cube1s_n = np.mean(cube1s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1s_s = np.mean(cube1s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1s_av = np.mean(cube1s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1s_so = (cube1s_n - cube1s_s) / cube1s_av
print(cube1s_so) 


###CUBE 2 salinity
#Time average, depth average and longitude average 
average_across_time2s = cube2s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time2s.coord('depth').points <= max_depth)[0]
average_across_time2s = average_across_time2s[indexes]
average_across_depth2s = average_across_time2s.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth2s.coord('latitude').guess_bounds()
average_across_depth2s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth2s)
cube2s_average = average_across_depth2s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube2s_average)
#print(cube2s_average.coord('latitude').points)

cube2s_n = np.mean(cube2s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2s_s = np.mean(cube2s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2s_av = np.mean(cube2s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2s_so = (cube2s_n - cube2s_s) / cube2s_av
print(cube2s_so) 

###CUBE 3 salinity
#Time average, depth average and longitude average 
average_across_time3s = cube3s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time3s.coord('lev').points <= max_depth)[0]
average_across_time3s = average_across_time3s[indexes]
average_across_depth3s = average_across_time3s.collapsed(['lev'],iris.analysis.MEAN)

average_across_depth3s.coord('latitude').guess_bounds()
average_across_depth3s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth3s)
cube3s_average = average_across_depth3s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube3s_average)
#print(cube3s_average.coord('latitude').points)

cube3s_n = np.mean(cube3s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3s_s = np.mean(cube3s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3s_av = np.mean(cube3s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3s_so = (cube3s_n - cube3s_s) / cube3s_av
print(cube3s_so) 

###CUBE 4 salinity
#Time average, depth average and longitude average 
average_across_time4s = cube4s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time4s.coord('ocean model level').points <= max_depth)[0]
average_across_time4s = average_across_time4s[indexes]
average_across_depth4s = average_across_time4s.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth4s.coord('latitude').guess_bounds()
average_across_depth4s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth4s)
cube4s_average = average_across_depth4s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube4s_average)
#print(cube4s_average.coord('latitude').points)

cube4s_n = np.mean(cube4s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4s_s = np.mean(cube4s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4s_av = np.mean(cube4s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4s_so = (cube4s_n - cube4s_s) / cube4s_av
print(cube4s_so) 


###CUBE 5 salinity
#Time average, depth average and longitude average 
average_across_time5s = cube5s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time5s.coord('depth').points <= max_depth)[0]
average_across_time5s = average_across_time5s[indexes]
average_across_depth5s = average_across_time5s.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth5s.coord('latitude').guess_bounds()
average_across_depth5s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth5s)
cube5s_average = average_across_depth5s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube5s_n = np.mean(cube5s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5s_s = np.mean(cube5s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5s_av = np.mean(cube5s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5s_so = (cube5s_n - cube5s_s) / cube5s_av
print(cube5s_so) 


###CUBE 6 salinity
#Time average, depth average and longitude average 
average_across_time6s = cube6s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time6s.coord('Vertical T levels').points <= max_depth)[0]
average_across_time6s = average_across_time6s[indexes]
average_across_depth6s = average_across_time6s.collapsed(['Vertical T levels'],iris.analysis.MEAN)

average_across_depth6s.coord('latitude').guess_bounds()
average_across_depth6s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth6s)
cube6s_average = average_across_depth6s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube6s_n = np.mean(cube6s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6s_s = np.mean(cube6s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6s_av = np.mean(cube6s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6s_so = (cube6s_n - cube6s_s) / cube6s_av
print(cube6s_so) 



###CUBE 7 salinity
#Time average, depth average and longitude average 
average_across_time7s = cube7s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time7s.coord('ocean sigma over z coordinate').points <= max_depth)[0]
average_across_time7s = average_across_time7s[indexes]
average_across_depth7s = average_across_time7s.collapsed(['ocean sigma over z coordinate'],iris.analysis.MEAN)

average_across_depth7s.coord('latitude').guess_bounds()
average_across_depth7s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth7s)
cube7s_average = average_across_depth7s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube7s_n = np.mean(cube7s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7s_s = np.mean(cube7s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7s_av = np.mean(cube7s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7s_so = (cube7s_n - cube7s_s) / cube7s_av
print(cube7s_so) 



###CUBE 8 salinity
#Time average, depth average and longitude average 
average_across_time8s = cube8s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time8s.coord('depth').points <= max_depth)[0]
average_across_time8s = average_across_time8s[indexes]
average_across_depth8s = average_across_time8s.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth8s.coord('latitude').guess_bounds()
average_across_depth8s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth8s)
cube8s_average = average_across_depth8s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube8s_n = np.mean(cube8s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8s_s = np.mean(cube8s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8s_av = np.mean(cube8s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8s_so = (cube8s_n - cube8s_s) / cube8s_av
print(cube8s_so) 


###CUBE 9 salinity
#Time average, depth average and longitude average 
#average_across_time9s = cube9s.collapsed(['time'],iris.analysis.MEAN)

##print(cube9s## no depth dimension**

#max_depth = 100.0
#indexes = np.where(average_across_time9s.coord('potential density referenced to 2000 dbar').points <= max_depth)[0]
#average_across_time9s = average_across_time9s[indexes]
#average_across_depth9s = average_across_time9s.collapsed(['potential density referenced to 2000 dbar'],iris.analysis.MEAN)

#average_across_depth9s.coord('latitude').guess_bounds()
#average_across_depth9s.coord('longitude').guess_bounds()
#grid_areas = iris.analysis.cartography.area_weights(average_across_depth9s)
#cube9s_average = average_across_depth9s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

#cube9s_n = np.mean(cube9s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube9s_s = np.mean(cube9s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube9s_av = np.mean(cube9s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube9s_so = (cube9s_n - cube9s_s) / cube9s_av
#print(cube9s_so) 


###CUBE 10 salinity
#Time average, depth average and longitude average 
average_across_time10s = cube10s.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time10s.coord('depth').points <= max_depth)[0]
average_across_time10s = average_across_time10s[indexes]
average_across_depth10s = average_across_time10s.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth10s.coord('latitude').guess_bounds()
average_across_depth10s.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth10s)
cube10s_average = average_across_depth10s.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube5s_average)
#print(cube5s_average.coord('latitude').points)

cube10s_n = np.mean(cube10s_average.data[37:39])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10s_s = np.mean(cube10s_average.data[13:15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10s_av = np.mean(cube10s_average.data[:])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10s_so = (cube10s_n - cube10s_s) / cube10s_av
print(cube10s_so) 


variable1 = [cube1_dic, cube2_dic, cube3_dic, cube4_dic, cube5_dic, cube6_dic, cube7_dic, cube8_dic, cube10_dic]
variable2 = [cube1s_so, cube2s_so, cube3s_so, cube4s_so, cube5s_so, cube6s_so, cube7s_so, cube8s_so, cube10s_so]

plt.scatter(variable2, variable1)
#plt.legend()
plt.show()
