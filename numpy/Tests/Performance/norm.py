import numpy as np
from numpy import emath
from numpy import linalg as LA
import tracemalloc


def generate_matrix(size:np.ulonglong):
    number = np.power(size, 2, dtype=np.ulonglong)
    matrix = np.arange(0, number, dtype=np.ulonglong).reshape(size, size)
    return matrix

def test(size:np.ulonglong):
    matrix = generate_matrix(size)
    tracemalloc.start()
    norm_matrix = LA.norm(matrix, 2)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 10**6}MB; Peak: {peak / 10**6}MB")
    tracemalloc.stop()

test(np.power(10,3))
test(6*np.power(10,4))