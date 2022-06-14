import numpy as np


rand_matrix = np.random.random((5,5))

#to normalize, first we have to find the max or min.

rand_matrix_max = rand_matrix.max() 
rand_matrix_min = rand_matrix.min() 

#normalization formula
 
rand_matrix = (rand_matrix - rand_matrix_min) / (rand_matrix_max - rand_matrix_min)

print(rand_matrix)