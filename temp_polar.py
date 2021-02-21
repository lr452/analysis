import iris
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature

cube = iris.load_cube('/disk2/lr452/Downloads/temp_data/thetao_Omon_UKESM1-0-LL_historical_r1i1p1f2_gn_199401-201412.rg.yr.so.fix.mask.nc','thetao')

#print(cube) 
#print(cube.shape)


#Taking the mean value across the 20 years
average_across_time = cube.collapsed(['time'],iris.analysis.MEAN)

#Averaging across depth
max_depth = 100.0
indexes = np.where(average_across_time.coord('depth').points <= max_depth)[0]
average_across_time = average_across_time[indexes]
average_across_depth = average_across_time.collapsed(['depth'],iris.analysis.MEAN)

print(average_across_depth.shape)

fig = plt.figure(figsize=[10, 10])
ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.SouthPolarStereo())

    # Limit the map to -60 degrees latitude and below.
ax1.set_extent([-180, 180, -90, -40], ccrs.PlateCarree())


lons = average_across_depth.coord('longitude').points
lats = average_across_depth.coord('latitude').points
data = average_across_depth.data

l = ax1.pcolormesh(lons, lats, data,
                transform=ccrs.PlateCarree(),
                cmap='bwr')

#m = ax1.contourf(lons, lats, data,
#                transform=ccrs.PlateCarree(),
#                cmap='bwr')

ax1.add_feature(cfeature.LAND)
ax1.gridlines()
ax1.legend()
ax1.set_title('temperature')
fig.colorbar(l)

plt.show()
