
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
cube1 = iris.load_cube('/disk2/lr452/Downloads/dissic_data/dissic_Omon_GISS-E2-1-G_historical_r101i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','dissic')

#print(cube1)

###CUBE 1

add_month_number(cube1, 'time', name='month_number')
cube2 = cube1[np.where((cube1.coord('month_number').points == 6) | (cube1.coord('month_number') == 7) | (cube1.coord('month_number') == 8))]

#then to average this by each year, so that you have the December-Jan for each year add the 'season year', i.e. a number of each 'season'
add_season_year(cube2, 'time', name='season_year')

#then average by the season year:
cube3 = cube2.aggregated_by(['season_year'], iris.analysis.MEAN)

cube4 = cube3.collapsed('time',iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(cube4.coord('depth').points <= max_depth)[0]
average_across_time1 = cube4[indexes]
average_across_depth1 = cube4.collapsed(['depth'],iris.analysis.MEAN)

#extracting a geographical region
#west = -180
#east = -70
#south = -80
#north = -40
#temporary_cube2 = average_across_depth1.intersection(longitude = (west, east))
#temporary_cube2b = temporary_cube2.intersection(latitude = (south,north))

#averaging across longitudes
average_across_depth1.coord('latitude').guess_bounds()
average_across_depth1.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth1)
cube1_average = average_across_depth1.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)


#print(cube1_average)
#print(cube1_average.coord('latitude').points)


cube1_n = np.mean(cube1_average.data[15])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
print(cube1_n)
cube1_s = np.mean(cube1_average.data[26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
print(cube1_s)
cube1_av = np.mean(cube1_average.data[15:26])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
print(cube1_av)
cube1_so = (cube1_s - cube1_n) / cube1_av
print(cube1_so) 


