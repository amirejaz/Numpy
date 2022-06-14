import numpy as np

A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3

print(A)
print(B)
print(C)

np.add(A, B, out=B)
np.divide(A, 2, out=A)
np.negative(A, out=A)
np.multiply(A, B, out=A)

print(A)