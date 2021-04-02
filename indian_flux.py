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
cube1 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube2 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_CanESM5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube3 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_CESM2_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube4 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_GFDL-CM4_historical_r1i1p1f1_gr_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube5 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_GISS-E2-1-G_historical_r101i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube6 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_IPSL-CM6A-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube7 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_MIROC-ES2L_historical_r1i1p1f2_gn_199401-201412.rg.so.fix.mask.nc','fgco2')
cube8 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube9 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_NorESM2-MM_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')
cube10 = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_UKESM1-0-LL_historical_r10i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')



###CUBE 1
#Time average, depth average and longitude average 
add_month_number(cube1, 'time', name='month_number')
cube_months1 = cube1[np.where((cube1.coord('month_number').points == 6) | (cube1.coord('month_number') == 7) | (cube1.coord('month_number') == 8))]

add_season_year(cube_months1, 'time', name='season_year')

#then average by the season year:
seasons1 = cube_months1.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average1 = seasons1.collapsed('time',iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube = seasonal_average1.intersection(longitude = (west, east))
temporary_cubeb = temporary_cube.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cubeb.coord('latitude').guess_bounds()
temporary_cubeb.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cubeb)
cube1_average = temporary_cubeb.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)


cube1_av = np.mean(cube1_average.data[17:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube1_dic = (cube1_n - cube1_s) / cube1_av
print(cube1_av) 


###CUBE 2
#Time average, depth average and longitude average 
add_month_number(cube2, 'time', name='month_number')
cube_months2 = cube2[np.where((cube2.coord('month_number').points == 6) | (cube2.coord('month_number') == 7) | (cube2.coord('month_number') == 8))]

add_season_year(cube_months2, 'time', name='season_year')

#then average by the season year:
seasons2 = cube_months2.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average2 = seasons2.collapsed('time',iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube2 = seasonal_average2.intersection(longitude = (west, east))
temporary_cube2b = temporary_cube2.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube2b.coord('latitude').guess_bounds()
temporary_cube2b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube2b)
cube2_average = temporary_cube2b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube2_av = np.mean(cube2_average.data[17:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube2_dic = (cube2_n - cube2_s) / cube2_av
print(cube2_av)  


###CUBE 3
#Time average, depth average and longitude average 
add_month_number(cube3, 'time', name='month_number')
cube_months3 = cube3[np.where((cube3.coord('month_number').points == 6) | (cube3.coord('month_number') == 7) | (cube3.coord('month_number') == 8))]

add_season_year(cube_months3, 'time', name='season_year')

#then average by the season year:
seasons3 = cube_months3.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average3 = seasons3.collapsed('time',iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube3 = seasonal_average3.intersection(longitude = (west, east))
temporary_cube3b = temporary_cube3.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube3b.coord('latitude').guess_bounds()
temporary_cube3b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube3b)
cube3_average = temporary_cube3b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube3_av = np.mean(cube3_average.data[16:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube3_dic = (cube3_n - cube3_s) / cube3_av
print(cube3_av)

###CUBE 4
#Time average, depth average and longitude average 
add_month_number(cube4, 'time', name='month_number')
cube_months4 = cube4[np.where((cube4.coord('month_number').points == 6) | (cube4.coord('month_number') == 7) | (cube4.coord('month_number') == 8))]

add_season_year(cube_months4, 'time', name='season_year')

#then average by the season year:
seasons4 = cube_months4.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average4 = seasons4.collapsed('time',iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube4 = seasonal_average4.intersection(longitude = (west, east))
temporary_cube4b = temporary_cube4.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube4b.coord('latitude').guess_bounds()
temporary_cube4b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube4b)
cube4_average = temporary_cube4b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube4_av = np.mean(cube4_average.data[18:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube4_dic = (cube4_n - cube4_s) / cube4_av
print(cube4_av)


###CUBE 5
#Time average, depth average and longitude average 
add_month_number(cube5, 'time', name='month_number')
cube_months5 = cube5[np.where((cube5.coord('month_number').points == 6) | (cube5.coord('month_number') == 7) | (cube5.coord('month_number') == 8))]

add_season_year(cube_months5, 'time', name='season_year')

#then average by the season year:
seasons5 = cube_months5.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average5 = seasons5.collapsed('time',iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube5 = seasonal_average5.intersection(longitude = (west, east))
temporary_cube5b = temporary_cube5.intersection(latitude = (south,north))
#averaging across longitudes
temporary_cube5b.coord('latitude').guess_bounds()
temporary_cube5b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube5b)
cube5_average = temporary_cube5b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube5_av = np.mean(cube5_average.data[15:23])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube5_dic = (cube5_n - cube5_s) / cube5_av
print(cube5_av)

###CUBE 6
#Time average, depth average and longitude average 
add_month_number(cube6, 'time', name='month_number')
cube_months6 = cube6[np.where((cube6.coord('month_number').points == 6) | (cube6.coord('month_number') == 7) | (cube6.coord('month_number') == 8))]

add_season_year(cube_months6, 'time', name='season_year')

#then average by the season year:
seasons6 = cube_months6.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average6 = seasons6.collapsed('time',iris.analysis.MEAN)

#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube6 = seasonal_average6.intersection(longitude = (west, east))
temporary_cube6b = temporary_cube6.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube6b.coord('latitude').guess_bounds()
temporary_cube6b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube6b)
cube6_average = temporary_cube6b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube6_av = np.mean(cube6_average.data[18:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube6_dic = (cube6_n - cube6_s) / cube6_av
print(cube6_av)


###CUBE 7
#Time average, depth average and longitude average 
add_month_number(cube7, 'time', name='month_number')
cube_months7 = cube7[np.where((cube7.coord('month_number').points == 6) | (cube7.coord('month_number') == 7) | (cube7.coord('month_number') == 8))]

add_season_year(cube_months7, 'time', name='season_year')

#then average by the season year:
seasons7 = cube_months7.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average7 = seasons7.collapsed('time',iris.analysis.MEAN)

#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube7 = seasonal_average7.intersection(longitude = (west, east))
temporary_cube7b = temporary_cube7.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube7b.coord('latitude').guess_bounds()
temporary_cube7b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube7b)
cube7_average = temporary_cube7b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube7_av = np.mean(cube7_average.data[22:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube7_dic = (cube7_n - cube7_s) / cube7_av
print(cube7_av)


###CUBE 8
#Time average, depth average and longitude average 
add_month_number(cube8, 'time', name='month_number')
cube_months8 = cube8[np.where((cube8.coord('month_number').points == 6) | (cube8.coord('month_number') == 7) | (cube8.coord('month_number') == 8))]

add_season_year(cube_months8, 'time', name='season_year')

#then average by the season year:
seasons8 = cube_months8.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average8 = seasons8.collapsed('time',iris.analysis.MEAN)

#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube8 = seasonal_average8.intersection(longitude = (west, east))
temporary_cube8b = temporary_cube8.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube8b.coord('latitude').guess_bounds()
temporary_cube8b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube8b)
cube8_average = temporary_cube8b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube8_av = np.mean(cube8_average.data[18:30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube8_dic = (cube8_n - cube8_s) / cube8_av
print(cube8_av)


###CUBE 9
#Time average, depth average and longitude average 
add_month_number(cube9, 'time', name='month_number')
cube_months9 = cube9[np.where((cube9.coord('month_number').points == 6) | (cube9.coord('month_number') == 7) | (cube9.coord('month_number') == 8))]

add_season_year(cube_months9, 'time', name='season_year')

#then average by the season year:
seasons9 = cube_months9.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average9 = seasons9.collapsed('time',iris.analysis.MEAN)


#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube9 = seasonal_average9.intersection(longitude = (west, east))
temporary_cube9b = temporary_cube9.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube9b.coord('latitude').guess_bounds()
temporary_cube9b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube9b)
cube9_average = temporary_cube9b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube9_av = np.mean(cube9_average.data[16:26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube9_dic = (cube9_n - cube9_s) / cube9_av
print(cube9_av)

###CUBE 10
#Time average, depth average and longitude average 
add_month_number(cube10, 'time', name='month_number')
cube_months10 = cube10[np.where((cube10.coord('month_number').points == 6) | (cube10.coord('month_number') == 7) | (cube10.coord('month_number') == 8))]

add_season_year(cube_months10, 'time', name='season_year')

#then average by the season year:
seasons10 = cube_months10.aggregated_by(['season_year'], iris.analysis.MEAN)


seasonal_average10 = seasons10.collapsed('time',iris.analysis.MEAN)

#extracting a geographical region
west = 40
east = 120
south = -80
north = -40
temporary_cube10 = seasonal_average10.intersection(longitude = (west, east))
temporary_cube10b = temporary_cube10.intersection(latitude = (south,north))

#averaging across longitudes
temporary_cube10b.coord('latitude').guess_bounds()
temporary_cube10b.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(temporary_cube10b)
cube10_average = temporary_cube10b.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube10_av = np.mean(cube10_average.data[17:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube10_dic = (cube10_n - cube10_s) / cube10_av
print(cube10_av)


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
