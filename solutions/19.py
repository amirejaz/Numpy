import numpy as np

#checkerboard pattern
arr = np.zeros((8,8), dtype=int)
arr[1::2, ::2] = 1
arr[::2, 1::2] = 1
print(arr)
