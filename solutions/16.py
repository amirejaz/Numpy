import numpy as np

arr = np.zeros((10,10))
arr[1:-1,1:-1] = 1
print(arr)