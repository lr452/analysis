import iris
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *

cube = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_GISS-E2-1-G_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')


#add_month_number(cube, 'time', name='month_number')
#cube2 = cube[np.where((cube.coord('month_number').points == 6) | (cube.coord('month_number') == 7) | (cube.coord('month_number') == 8))]

#then to average this by each year, so that you have the December-Jan for each year add the 'season year', i.e. a number of each 'season'
#add_season_year(cube2, 'time', name='season_year')

#then average by the season year:
#cube3 = cube2.aggregated_by(['season_year'], iris.analysis.MEAN)

#average all of the data together along the time axis
cube2 = cube.collapsed('time',iris.analysis.MEAN)

#extracting a geographical region
#west = 40
#east = 120
#south = -65
#north = -40
#temporary_cube = cube4.intersection(longitude = (west, east))
#cube4_region = temporary_cube.intersection(latitude = (south,north))

#averaging across longitudes
cube2.coord('latitude').guess_bounds()
cube2.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(cube2)
global_average_variable = cube2.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

qplt.pcolormesh(global_average_variable)
#plt.xlim(1000,0)
plt.ylim(1000,0)
plt.show()
