import numpy as np

arr = np.random.randint(0,10,(3,3))
print(arr)
print(arr[arr[:,1].argsort()])
