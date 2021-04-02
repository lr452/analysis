import iris
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *

cube = iris.load_cube('/disk2/lr452/Downloads/salinity_data/so_Omon_GISS-E2-1-G_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','so')


add_month_number(cube, 'time', name='month_number')
cube2 = cube[np.where((cube.coord('month_number').points == 6) | (cube.coord('month_number') == 7) | (cube.coord('month_number') == 8))]

#then to average this by each year, so that you have the December-Jan for each year add the 'season year', i.e. a number of each 'season'
add_season_year(cube2, 'time', name='season_year')

#then average by the season year:
cube3 = cube2.aggregated_by(['season_year'], iris.analysis.MEAN)

#average all of the data together along the time axis
cube2 = cube.collapsed('time',iris.analysis.MEAN)

#extracting a geographical region
west = -60
east = 30
south = -70
north = -40
temporary_cube = cube2.intersection(longitude = (west, east))
cube2_region = temporary_cube.intersection(latitude = (south,north))

#averaging across longitudes
cube2_region.coord('latitude').guess_bounds()
cube2_region.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(cube2_region)
global_average_variable = cube2_region.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

x = global_average_variable.coord('latitude').points
y = global_average_variable.coord('depth').points
z= global_average_variable.data


fig, ax = plt.subplots()
levels = np.linspace(33, 35, 22)
cs = ax.contourf(x, y, z, levels=levels, cmap='RdPu', extend='both', vmin=33, vmax=35)
plt.ylim(1000,0)
plt.xticks([-70, -65, -60, -55, -50, -45, -40])
cb = fig.colorbar(cs, extend='both')
cb.set_label(label='Salinity [psu]', weight='bold')
cb.ax.set_yticklabels(["33.0", "33.25", "33.5", "33.75", "34.0", "34.25", "34.5", "34.75", "35"], weight='bold')
ax.set_xticklabels(["-70$^\circ$S", "-65$^\circ$S", "-60$^\circ$S", "-55$^\circ$S", "-50$^\circ$S", "-45$^\circ$S", "-40$^\circ$S"], fontsize=9, weight='bold')
ax.set_yticklabels(["0", "200", "400", "600", "800", "1000"], fontsize=9, weight='bold')
plt.ylabel('Depth (m)', weight='bold', fontsize=9)
plt.show()
