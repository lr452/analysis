import iris 
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
from scipy.stats.mstats import *


#Load in model data
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


### CUBE 1
##Time average 
average_across_time1 = cube1.collapsed(['time'],iris.analysis.MEAN)

##Depth average
max_depth = 100.0
indexes = np.where(average_across_time1.coord('depth').points <= max_depth)[0]
average_across_time1 = average_across_time1[indexes]
average_across_depth1 = average_across_time1.collapsed(['depth'],iris.analysis.MEAN)

##Longitude average
average_across_depth1.coord('latitude').guess_bounds()
average_across_depth1.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth1)
cube1_average = average_across_depth1.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

##Index data
cube1_n = np.mean(cube1_average.data[28:30])
cube1_s = np.mean(cube1_average.data[16:18])
cube1_av = np.mean(cube1_average.data[16:30])

##Cube maths
cube1_dic = (cube1_n - cube1_s) / cube1_av
print(cube1_dic) 


### CUBE 2
##Time average 
average_across_time2 = cube2.collapsed(['time'],iris.analysis.MEAN)

##Depth average
max_depth = 100.0
indexes = np.where(average_across_time2.coord('depth').points <= max_depth)[0]
average_across_time2 = average_across_time2[indexes]
average_across_depth2 = average_across_time2.collapsed(['depth'],iris.analysis.MEAN)

##Longitude average
average_across_depth2.coord('latitude').guess_bounds()
average_across_depth2.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth2)
cube2_average = average_across_depth2.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

##Index data
cube2_n = np.mean(cube2_average.data[26:28]))
cube2_s = np.mean(cube2_average.data[16:18])
cube2_av = np.mean(cube2_average.data[16:28])

##Cube maths
cube2_dic = (cube2_n - cube2_s) / cube2_av
print(cube2_dic) 



###CUBE 3
#Time average, depth average and longitude average 
average_across_time3 = cube3.collapsed(['time'],iris.analysis.MEAN)

max_depth = 100.0
indexes = np.where(average_across_time3.coord('ocean model level').points <= max_depth)[0]
average_across_time3 = average_across_time3[indexes]
average_across_depth3 = average_across_time3.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth3.coord('latitude').guess_bounds()
average_across_depth3.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth3)
cube3_average = average_across_depth3.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

#print(cube3_average.coord('latitude').points)

average_across_time3d = cube3.collapsed(['time'],iris.analysis.MEAN)
max_depthd = 250.0
indexesd = np.where(average_across_time3d.coord('ocean model level').points <= max_depthd)[0]
average_across_time3d = average_across_time3d[indexesd]
average_across_depth3d = average_across_time3d.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth3d.coord('latitude').guess_bounds()
average_across_depth3d.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth3d)
cube3d_average = average_across_depth3d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube3_n = np.mean(cube3_average.data[26:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_s = np.mean(cube3_average.data[15:17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube3_av = np.mean(cube3_average.data[15:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
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

average_across_time4d = cube4.collapsed(['time'],iris.analysis.MEAN)
max_depthd = 250.0
indexesd = np.where(average_across_time4d.coord('ocean model level').points <= max_depthd)[0]
average_across_time4d = average_across_time4d[indexesd]
average_across_depth4d = average_across_time4d.collapsed(['ocean model level'],iris.analysis.MEAN)

average_across_depth4d.coord('latitude').guess_bounds()
average_across_depth4d.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth4d)
cube4d_average = average_across_depth4d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube4_n = np.mean(cube4_average.data[26:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_s = np.mean(cube4_average.data[17:19])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube4_av = np.mean(cube4_average.data[17:28])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
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

average_across_time5d = cube5.collapsed(['time'],iris.analysis.MEAN)
max_depthd = 250.0
indexesd = np.where(average_across_time5d.coord('depth').points <= max_depthd)[0]
average_across_time5d = average_across_time5d[indexesd]
average_across_depth5d = average_across_time5d.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth5d.coord('latitude').guess_bounds()
average_across_depth5d.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth5d)
cube5d_average = average_across_depth5d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube5_n = np.mean(cube5_average.data[22:24])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_s = np.mean(cube5_average.data[14:16])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube5_av = np.mean(cube5_average.data[14:24])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
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

average_across_time6d = cube6.collapsed(['time'],iris.analysis.MEAN)
max_depthd = 250.0
indexesd = np.where(average_across_time6d.coord('Vertical T levels').points <= max_depthd)[0]
average_across_time6d = average_across_time6d[indexesd]
average_across_depth6d = average_across_time6d.collapsed(['Vertical T levels'],iris.analysis.MEAN)

average_across_depth6d.coord('latitude').guess_bounds()
average_across_depth6d.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth6d)
cube6d_average = average_across_depth6d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube6_n = np.mean(cube6_average.data[28:30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_s = np.mean(cube6_average.data[17:19])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube6_av = np.mean(cube6_average.data[17:30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
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

average_across_time7d = cube7.collapsed(['time'],iris.analysis.MEAN)
max_depthd = 250.0
indexesd = np.where(average_across_time7d.coord('ocean sigma over z coordinate').points <= max_depthd)[0]
average_across_time7d = average_across_time7d[indexesd]
average_across_depth7d = average_across_time7d.collapsed(['ocean sigma over z coordinate'],iris.analysis.MEAN)

average_across_depth7d.coord('latitude').guess_bounds()
average_across_depth7d.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth7d)
cube7d_average = average_across_depth7d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube7_n = np.mean(cube7_average.data[28:30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_s = np.mean(cube7_average.data[21:23])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube7_av = np.mean(cube7_average.data[21:30])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
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

average_across_time8d = cube8.collapsed(['time'],iris.analysis.MEAN)
max_depthd = 250.0
indexesd = np.where(average_across_time8d.coord('depth').points <= max_depthd)[0]
average_across_time8d = average_across_time8d[indexesd]
average_across_depth8d = average_across_time8d.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth8d.coord('latitude').guess_bounds()
average_across_depth8d.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth8d)
cube8d_average = average_across_depth8d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube8_n = np.mean(cube8_average.data[29:31])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_s = np.mean(cube8_average.data[17:19])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube8_av = np.mean(cube8_average.data[17:31])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
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

average_across_time9d = cube1.collapsed(['time'],iris.analysis.MEAN)
max_depthd = 250.0
indexesd = np.where(average_across_time9.coord('depth').points <= max_depthd)[0]
average_across_time9d = average_across_time9[indexesd]
average_across_depth9d = average_across_time9d.collapsed(['depth'],iris.analysis.MEAN)

average_across_depth9d.coord('latitude').guess_bounds()
average_across_depth9d.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth9d)
cube9d_average = average_across_depth9d.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

cube9_n = np.mean(cube9_average.data[25:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_s = np.mean(cube9_average.data[15:17])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_av = np.mean(cube9_average.data[15:27])#.collapsed(['latitude'],iris.analysis.MEAN,weights=grid_areas)
cube9_dic = (cube9_n - cube9_s) / cube9_av
print(cube9_dic)

### CUBE 10
##Time average
average_across_time10 = cube10.collapsed(['time'],iris.analysis.MEAN)

##Depth average
max_depth = 100.0
indexes = np.where(average_across_time9.coord('depth').points <= max_depth)[0]
average_across_time10 = average_across_time10[indexes]
average_across_depth10 = average_across_time10.collapsed(['depth'],iris.analysis.MEAN)

##Longitude average
average_across_depth10.coord('latitude').guess_bounds()
average_across_depth10.coord('longitude').guess_bounds()
grid_areas = iris.analysis.cartography.area_weights(average_across_depth10)
cube10_average = average_across_depth10.collapsed(['longitude'],iris.analysis.MEAN,weights=grid_areas)

##Index data
cube10_n = np.mean(cube10_average.data[27:29])
cube10_s = np.mean(cube10_average.data[16:18])
cube10_av = np.mean(cube10_average.data[16:29])

##Cube maths
cube10_dic = (cube10_n - cube10_s) / cube10_av
print(cube10_dic)


### LOAD WIND DATA
wind_variable = np.array([51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 49.16, 53.81, 51.78])


### ASSIGN VARIABLES
variable1 = np.array([cube1_dic, cube2_dic, cube3_dic, cube4_dic, cube5_dic, cube6_dic, cube8_dic, cube9_dic, cube10_dic])
variable2 = wind_variable 


### TAKE THE CORRELATION BETWEEN THE VARIABLES
slope,intercept,r_value,p_value,std_err = linregress(variable2, variable1)
print(slope)
correlation = spearmanr(variable1, variable2)
print(correlation)


### PLOT THE DATA
fig, ax = plt.subplots()

ax.scatter(variable2[0], variable1[0], s=125, label='ACCESS-ESM1-5', marker='*',facecolor='orangered', edgecolor='black')
ax.scatter(variable2[1], variable1[1], s=100, label='CanESM5', marker='p', facecolor='gold', edgecolor='black')
ax.scatter(variable2[2], variable1[2], s=100, label='CESM2', marker='<', facecolor='yellowgreen', edgecolor='black')
ax.scatter(variable2[3], variable1[3], s=100, label='GFDL-CM4', marker='8', facecolor='dimgrey', edgecolor='black')
ax.scatter(variable2[4], variable1[4], s=100, label='GISS-E2-1-G', marker='s', facecolor='mediumaquamarine', edgecolor='black')
ax.scatter(variable2[5], variable1[5], s=100, label='IPSL-CM6A-LR', marker='P', facecolor='deepskyblue', edgecolor='black')
ax.scatter(variable2[6], variable1[6], s=100, label='MIROC-ES2L', marker='X', facecolor='darkviolet', edgecolor='black')
ax.scatter(variable2[7], variable1[7], s=100, label='MPI-ESM1-2-LR', marker='H', facecolor='hotpink', edgecolor='black')
ax.scatter(variable2[8], variable1[8], s=75, label='NorESM2-MM', marker='D', facecolor='steelblue', edgecolor='black')
plt.scatter(variable2[9], variable1[9], s=100, label='UKESM1-0-LL', marker='v', facecolor='darkcyan', edgecolor='black')

ax.plot(variable2,(slope*variable2)+intercept, c='black', linewidth=1)

ax.set_facecolor('whitesmoke')
ax.grid(True)


plt.xlabel('Lat of Tmax [$^\circ$S]', fontsize=10, fontweight='bold')
plt.ylabel('$\Delta$DIC [mol $m^{-3}$]', fontsize=10, fontweight='bold')
plt.xticks(fontsize=9, fontweight='bold')
plt.yticks(fontsize=9, fontweight='bold')

plt.legend(bbox_to_anchor=(1.02,0.8), loc='centre left', fontsize=6, frameon=False, prop=dict(weight='bold'))

plt.text(50.2, -5.35, 'r=-0.789, p=0.007', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.show()
