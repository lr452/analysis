import iris
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature


cube = iris.load_cube('/disk2/lr452/Downloads/fgco2_data/fgco2_Omon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_199401-201412.rg.yr.so.fix.mask.nc','fgco2')

print(cube)
print(cube.shape)

add_month_number(cube, 'time', name='month_number')
cube2 = cube[np.where((cube.coord('month_number').points == 12) | (cube.coord('month_number') == 1) | (cube.coord('month_number') == 2))]

#then to average this by each year, so that you have the December-Jan for each year add the 'season year', i.e. a number of each 'season'
add_season_year(cube2, 'time', name='season_year')

#then average by the season year:
cube3 = cube2.aggregated_by(['season_year'], iris.analysis.MEAN)


cube4 = cube3.collapsed('time',iris.analysis.MEAN)

#print(cube4.coord('latitude').points)

#west = 40
#east = 120
#south = -80
#north = -40
#temporary_cube5 = cube4.intersection(longitude = (west, east))
#temporary_cube5b = temporary_cube5.intersection(latitude = (south,north))

cube4.coord('latitude').guess_bounds()
cube4.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(cube4)
cube6_average = cube4.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube_cut = np.mean(cube6_average.data[17:29])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
#cube1_flux = (cube1_n - cube1_s) / cube1_av
print(cube_cut) 




#fig = plt.figure(figsize=[10, 10])
#ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.SouthPolarStereo())

    # Limit the map to -60 degrees latitude and below.
#ax1.set_extent([-180, 180, -90, -40], ccrs.PlateCarree())


#lons = cube4.coord('longitude').points
#lats = cube4.coord('latitude').points
#data = cube4.data

#l = ax1.pcolormesh(lons, lats, data,
               # transform=ccrs.PlateCarree(),
               # cmap='bwr', vmin=-2e-9, vmax=2e-9)

#m = ax1.contourf(lons, lats, data,
#                transform=ccrs.PlateCarree(),
#                cmap='bwr')

#ax1.add_feature(cfeature.LAND)
#ax1.gridlines()
#ax1.legend()
#ax1.set_title('fgco2')
#fig.colorbar(l)

    # Compute a circle in axes coordinates, which we can use as a boundary
    # for the map. We can pan/zoom as much as we like - the boundary will be
    # permanently circular.

#plt.show()
