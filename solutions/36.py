import numpy as np

array = np.random.uniform(1,10,10)
#Method 1
print(array - array%1)

# Method 2
print(np.floor(array))

# Method 3
print(np.ceil(array) - 1)

# Method 4
print(array.astype(int))

# Method 5
print(np.trunc(array))

