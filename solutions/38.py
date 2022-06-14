import numpy as np

def generate():
    for x in range(10):
        yield x

array = np.fromiter(generate(), dtype=float, count=-1)

print(array)