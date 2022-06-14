import numpy as np

arr = np.zeros(10)
arr.flags.writeable = False
arr[0] = 1
print(arr)