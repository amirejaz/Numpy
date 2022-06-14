import numpy as np

#  Subtract the mean of each row of a matrix

x = np.random.rand(5, 10)

y = x - x.mean(axis=1, keepdims = True)

print(y)