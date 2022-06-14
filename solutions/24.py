import numpy as np

# solution 1
arr = np.dot(np.ones((5,3)), np.ones((3,5)))
print(arr)

#solution 2 from range method
array1 = np.arange(15).reshape(5,3)
array2 = np.arange(15).reshape(3,5)

mul_result = np.dot(array1, array2)
print(mul_result)

#solution 3 from random method
array3 = np.random.random(15).reshape(5,3)
array4 = np.random.random(15).reshape(3,5)

multiply_result = np.dot(array3, array4)
print(multiply_result)

