import numpy as np
from numpy import *

arr = np.random.uniform(-10, +10, 10)
print(np.copysign(np.ceil(np.abs(arr)), arr))