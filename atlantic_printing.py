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
cube1 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube2 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_CanESM5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube3 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_CESM2_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.depth.nc','thetao')
cube4 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_GFDL-CM4_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube5 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_GISS-E2-1-G_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube6 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_IPSL-CM6A-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube7 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_MIROC-ES2L_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube8 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube9 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_NorESM2-MM_historical_r1i1p1f1_gr_199401-201412.rg.yr.so.fix.mask.nc','thetao')
cube10 = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_UKESM1-0-LL_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')



###CUBE 1
#Time average, depth average and longitude average 
add_month_number(cube1, 'time', name='month_number')
cube_months1 = cube1[np.where((cube1.coord('month_number').points == 12) | (cube1.coord('month_number') == 1) | (cube1.coord('month_number') == 2))]

add_season_year(cube_months1, 'time', name='season_year')

#then average by the season year:
seasons1 = cube_months1.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average1 = seasons1.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average1.coord('depth').points <= max_depth)[0]
seasonal_average1 = seasonal_average1[indexes]
average_across_depth1 = seasonal_average1.collapsed(['depth'],iris.analysis.MEAN)

#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube = average_across_depth1.intersection(longitude = (west, east))
temporary_cubeb = temporary_cube.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cubeb.coord('latitude').guess_bounds()
temporary_cubeb.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cubeb)
cube1_average = temporary_cubeb.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)



cube1_n = np.mean(cube1_average.data[29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_s = np.mean(cube1_average.data[17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_av = np.mean(cube1_average.data[17:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube1_dic = (cube1_n - cube1_s) / cube1_av
print(cube1_dic) 


###CUBE 2
#Time average, depth average and longitude average 
add_month_number(cube2, 'time', name='month_number')
cube_months2 = cube2[np.where((cube2.coord('month_number').points == 12) | (cube2.coord('month_number') == 1) | (cube2.coord('month_number') == 2))]

add_season_year(cube_months2, 'time', name='season_year')

#then average by the season year:
seasons2 = cube_months2.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average2 = seasons2.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average2.coord('depth').points <= max_depth)[0]
seasonal_average2 = seasonal_average2[indexes]
average_across_depth2 = seasonal_average2.collapsed(['depth'],iris.analysis.MEAN)

#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube2 = average_across_depth2.intersection(longitude = (west, east))
temporary_cube2b = temporary_cube2.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube2b.coord('latitude').guess_bounds()
temporary_cube2b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube2b)
cube2_average = temporary_cube2b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube2_n = np.mean(cube2_average.data[27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_s = np.mean(cube2_average.data[17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_av = np.mean(cube2_average.data[17:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube2_dic = (cube2_n - cube2_s) / cube2_av
print(cube2_dic)  


###CUBE 3
#Time average, depth average and longitude average 
add_month_number(cube3, 'time', name='month_number')
cube_months3 = cube3[np.where((cube3.coord('month_number').points == 12) | (cube3.coord('month_number') == 1) | (cube3.coord('month_number') == 2))]

add_season_year(cube_months3, 'time', name='season_year')

#then average by the season year:
seasons3 = cube_months3.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average3 = seasons3.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average3.coord('lev').points <= max_depth)[0]
seasonal_average3 = seasonal_average3[indexes]
average_across_depth3 = seasonal_average3.collapsed(['lev'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube3 = average_across_depth3.intersection(longitude = (west, east))
temporary_cube3b = temporary_cube3.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube3b.coord('latitude').guess_bounds()
temporary_cube3b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube3b)
cube3_average = temporary_cube3b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)


cube3_n = np.mean(cube3_average.data[27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_s = np.mean(cube3_average.data[16])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_av = np.mean(cube3_average.data[16:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_dic = (cube3_n - cube3_s) / cube3_av
print(cube3_dic)

###CUBE 4
#Time average, depth average and longitude average 
add_month_number(cube4, 'time', name='month_number')
cube_months4 = cube4[np.where((cube4.coord('month_number').points == 12) | (cube4.coord('month_number') == 1) | (cube4.coord('month_number') == 2))]

add_season_year(cube_months4, 'time', name='season_year')

#then average by the season year:
seasons4 = cube_months4.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average4 = seasons4.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average4.coord('ocean model level').points <= max_depth)[0]
seasonal_average4 = seasonal_average4[indexes]
average_across_depth4 = seasonal_average4.collapsed(['ocean model level'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube4 = average_across_depth4.intersection(longitude = (west, east))
temporary_cube4b = temporary_cube4.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube4b.coord('latitude').guess_bounds()
temporary_cube4b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube4b)
cube4_average = temporary_cube4b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube4_n = np.mean(cube4_average.data[27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_s = np.mean(cube4_average.data[18])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_av = np.mean(cube4_average.data[18:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_dic = (cube4_n - cube4_s) / cube4_av
print(cube4_dic)


###CUBE 5
#Time average, depth average and longitude average 
add_month_number(cube5, 'time', name='month_number')
cube_months5 = cube5[np.where((cube5.coord('month_number').points == 12) | (cube5.coord('month_number') == 1) | (cube5.coord('month_number') == 2))]

add_season_year(cube_months5, 'time', name='season_year')

#then average by the season year:
seasons5 = cube_months5.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average5 = seasons5.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average5.coord('depth').points <= max_depth)[0]
seasonal_average5 = seasonal_average5[indexes]
average_across_depth5 = seasonal_average5.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube5 = average_across_depth5.intersection(longitude = (west, east))
temporary_cube5b = temporary_cube5.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube5b.coord('latitude').guess_bounds()
temporary_cube5b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube5b)
cube5_average = temporary_cube5b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube5_n = np.mean(cube5_average.data[23])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_s = np.mean(cube5_average.data[15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_av = np.mean(cube5_average.data[15:23])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_dic = (cube5_n - cube5_s) / cube5_av
print(cube5_dic)

###CUBE 6
#Time average, depth average and longitude average 
add_month_number(cube6, 'time', name='month_number')
cube_months6 = cube6[np.where((cube2.coord('month_number').points == 12) | (cube6.coord('month_number') == 1) | (cube6.coord('month_number') == 2))]

add_season_year(cube_months6, 'time', name='season_year')

#then average by the season year:
seasons6 = cube_months6.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average6 = seasons6.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average6.coord('Vertical T levels').points <= max_depth)[0]
seasonal_average6 = seasonal_average6[indexes]
average_across_depth6 = seasonal_average6.collapsed(['Vertical T levels'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube6 = average_across_depth6.intersection(longitude = (west, east))
temporary_cube6b = temporary_cube6.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube6b.coord('latitude').guess_bounds()
temporary_cube6b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube6b)
cube6_average = temporary_cube6b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube6_n = np.mean(cube6_average.data[29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_s = np.mean(cube6_average.data[18])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_av = np.mean(cube6_average.data[18:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_dic = (cube6_n - cube6_s) / cube6_av
print(cube6_dic)


###CUBE 7
#Time average, depth average and longitude average 
add_month_number(cube7, 'time', name='month_number')
cube_months7 = cube7[np.where((cube7.coord('month_number').points == 12) | (cube7.coord('month_number') == 1) | (cube7.coord('month_number') == 2))]

add_season_year(cube_months7, 'time', name='season_year')

#then average by the season year:
seasons7 = cube_months7.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average7 = seasons7.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average7.coord('ocean sigma over z coordinate').points <= max_depth)[0]
seasonal_average7 = seasonal_average7[indexes]
average_across_depth7 = seasonal_average7.collapsed(['ocean sigma over z coordinate'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube7 = average_across_depth7.intersection(longitude = (west, east))
temporary_cube7b = temporary_cube7.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube7b.coord('latitude').guess_bounds()
temporary_cube7b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube7b)
cube7_average = temporary_cube7b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube7_n = np.mean(cube7_average.data[29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_s = np.mean(cube7_average.data[22])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_av = np.mean(cube7_average.data[22:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_dic = (cube7_n - cube7_s) / cube7_av
print(cube7_dic)


###CUBE 8
#Time average, depth average and longitude average 
add_month_number(cube8, 'time', name='month_number')
cube_months8 = cube8[np.where((cube8.coord('month_number').points == 12) | (cube8.coord('month_number') == 1) | (cube8.coord('month_number') == 2))]

add_season_year(cube_months8, 'time', name='season_year')

#then average by the season year:
seasons8 = cube_months8.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average8 = seasons8.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average8.coord('depth').points <= max_depth)[0]
seasonal_average8 = seasonal_average8[indexes]
average_across_depth8 = seasonal_average8.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube8 = average_across_depth8.intersection(longitude = (west, east))
temporary_cube8b = temporary_cube8.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube8b.coord('latitude').guess_bounds()
temporary_cube8b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube8b)
cube8_average = temporary_cube8b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube8_n = np.mean(cube8_average.data[30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_s = np.mean(cube8_average.data[18])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_av = np.mean(cube8_average.data[18:30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_dic = (cube8_n - cube8_s) / cube8_av
print(cube8_dic)


###CUBE 9
#Time average, depth average and longitude average 
add_month_number(cube9, 'time', name='month_number')
cube_months9 = cube9[np.where((cube9.coord('month_number').points == 12) | (cube9.coord('month_number') == 1) | (cube9.coord('month_number') == 2))]

add_season_year(cube_months9, 'time', name='season_year')

#then average by the season year:
seasons9 = cube_months9.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average9 = seasons9.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average9.coord('depth').points <= max_depth)[0]
seasonal_average9 = seasonal_average9[indexes]
average_across_depth9 = seasonal_average9.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube9 = average_across_depth9.intersection(longitude = (west, east))
temporary_cube9b = temporary_cube9.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube9b.coord('latitude').guess_bounds()
temporary_cube9b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube9b)
cube9_average = temporary_cube9b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube9_n = np.mean(cube9_average.data[26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_s = np.mean(cube9_average.data[16])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_av = np.mean(cube9_average.data[16:26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_dic = (cube9_n - cube9_s) / cube9_av
print(cube9_dic)

###CUBE 10
#Time average, depth average and longitude average 
add_month_number(cube10, 'time', name='month_number')
cube_months10 = cube10[np.where((cube10.coord('month_number').points == 12) | (cube10.coord('month_number') == 1) | (cube10.coord('month_number') == 2))]

add_season_year(cube_months10, 'time', name='season_year')

#then average by the season year:
seasons10 = cube_months10.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average10 = seasons10.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(seasonal_average10.coord('depth').points <= max_depth)[0]
seasonal_average10 = seasonal_average10[indexes]
average_across_depth10 = seasonal_average10.collapsed(['depth'],iris.analysis.MEAN)


#extracting a geographical region
west = -60
east = 30
south = -80
north = -40
temporary_cube10 = average_across_depth10.intersection(longitude = (west, east))
temporary_cube10b = temporary_cube10.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube10b.coord('latitude').guess_bounds()
temporary_cube10b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube10b)
cube10_average = temporary_cube10b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)


cube10_n = np.mean(cube10_average.data[28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_s = np.mean(cube10_average.data[17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_av = np.mean(cube10_average.data[17:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube10_dic = (cube10_n - cube10_s) / cube10_av
print(cube10_dic)


#Load wind data
wind_variable = np.array([51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 49.16, 53.81, 51.78])


variable1 = np.array([cube1_dic, cube2_dic, cube3_dic, cube4_dic, cube5_dic, cube6_dic, cube8_dic, cube9_dic, cube10_dic])
variable2 = wind_variable 

slope,intercept,r_value,p_value,std_err = linregress(variable2, variable1)
print(slope)
correlation = spearmanr(variable1, variable2)
print(correlation)

plt.scatter(variable2, variable1)

plt.scatter(variable2[0], variable1[0],label='ACCESS-ESM1-5')
plt.scatter(variable2[1], variable1[1],label='CanESM5')
plt.scatter(variable2[2], variable1[2],label='CESM2')
plt.scatter(variable2[3], variable1[3],label='GFDL-CM4')
plt.scatter(variable2[4], variable1[4],label='GISS-E2-1-G')
plt.scatter(variable2[5], variable1[5],label='IPSL-CM6A-LR')
#plt.scatter(variable2[6], variable1[6],label='MIROC-ES2L')
plt.scatter(variable2[6], variable1[6],label='MPI-ESM1-2-LR')
plt.scatter(variable2[7], variable1[7],label='NorESM2-MM')
plt.scatter(variable2[8], variable1[8],label='UKESM1-0-LL')
plt.plot(variable2,(slope*variable2)+intercept)
plt.xlabel('Latitude of maximum wind stress (degrees south)')
plt.ylabel('Relative DIC concentration (kg/metre sqr)')
plt.title('Atlantic Ocean')
plt.legend(bbox_to_anchor=(1.02,0.8), loc='centre left')
plt.show()
