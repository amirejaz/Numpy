import numpy as np

arr = np.arange(10)
arr[(arr > 3) & (arr < 8)] *= -1
print(arr)