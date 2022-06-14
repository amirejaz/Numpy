import numpy as np

arr = np.arange(100)

v = np.random.uniform(0,100)

index = (np.abs(arr - v).argmin())
print(arr[index])