import iris
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *

cube = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_GFDL-CM4_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')


add_month_number(cube, 'time', name='month_number')
cube2 = cube[np.where((cube.coord('month_number').points == 12) | (cube.coord('month_number') == 1) | (cube.coord('month_number') == 2))]

#then to average this by each year, so that you have the December-Jan for each year add the 'season year', i.e. a number of each 'season'
add_season_year(cube2, 'time', name='season_year')

#then average by the season year:
cube3 = cube2.aggregated_by(['season_year'], iris.analysis.MEAN)

#average all of the data together along the time axis
cube2 = cube.collapsed('time',iris.analysis.MEAN)

#extracting a geographical region
west = 40
east = 120
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
y = global_average_variable.coord('ocean model level').points
z= global_average_variable.data


fig, ax = plt.subplots()
levels = np.linspace(-2, 16, 16)
cs = ax.contourf(x, y, z, levels=levels,
                 cmap='YlGnBu_r', vmin=-2, vmax=16, extend='both')
plt.ylim(1000,0)
plt.xticks([-70, -65, -60, -55, -50, -45, -40])
cb = fig.colorbar(cs, extend='both')
cb.set_label(label='K', weight='bold')
cb.ax.set_yticklabels(["-2", "0", "2", "4", "6", "8", "10", "12", "14", "16"], weight='bold')
ax.set_xticklabels(["-70$^\circ$S", "-65$^\circ$S", "-60$^\circ$S", "-55$^\circ$S", "-50$^\circ$S", "-45$^\circ$S", "-40$^\circ$S"], fontsize=9, weight='bold')
ax.set_yticklabels(["0", "200", "400", "600", "800", "1000"], fontsize=9, weight='bold')
plt.ylabel('Depth (m)', weight='bold', fontsize=9)
plt.show()
