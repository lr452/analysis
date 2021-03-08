import iris
import matplotlib.pyplot as plt
import iris.quickplot as qplt
import iris.analysis

cube_tmp = iris.load_cube('GLODAPv2.2016b.Cant.nc','variable')
cube = iris.load_cube('/disk2/lr452/Downloads/GLODAPv2.2016b.Cant.nc')

cube.data = cube_tmp.data

print(cube.data)
