import numpy as np

arr1 = np.random.randint(0, 10, 10)
arr2 = np.random.randint(0, 10, 10)

print(np.intersect1d(arr1, arr2))
