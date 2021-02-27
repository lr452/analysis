import iris 
import numpy as np
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.coord_categorisation import *
from matplotlib.pyplot import *
import matplotlib as mpl
from scipy.stats.mstats import *

variable_1 = [51.37, 50.68, 53.2, 50.63, 52.2, 50.47, 46.11, 49.16, 53.81, 51.78]
variable_2 = [51, 53, 52.5, 52, 60, 50, 50, 49, 53, 51.5]

slope,intercept,r_value,p_value,std_err = linregress(variable_1, variable_2)
#plt.plot(variable_1,(slope*variable_1)+intercept)
plt.scatter(variable_1, variable_2)
plt.show()
