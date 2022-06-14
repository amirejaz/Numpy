import numpy as np
from numpy import*

Yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
Today = np.datetime64('today', 'D')
Tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')

print("Yesterday date: ", Yesterday)
print("Today date: ", Today)
print("Tomorrow date: ", Tomorrow)