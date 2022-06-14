import numpy as np

arr = np.random.randint(0, 3, (3, 10))

print((~arr.any(axis=0)).any())