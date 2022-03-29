import numpy as np
from numpy import emath 
import time
from copy import deepcopy
import random as rm


def numpy_implementation(arr1, arr2):
    return np.array(arr1).dot(arr2)


def python_implementation(arr1, arr2):
    result = [[0 for _ in range(len(arr1))] for _ in range(len(arr2[0]))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result


def generate(size):
    arr = [[i for i in range(1, size)] for _ in range(1,size)]
    return arr


def tests(power):
    size = np.power(10, power)
    tmp = generate(size)
    tmp2 = deepcopy(tmp)
    
    start_time = time.perf_counter()
    numpy_implementation(tmp, tmp2)
    timer = time.perf_counter() - start_time
    print("Test numpy dla wielkości 10^"+str(power)+" czas:"+str(timer))
    
    start_time = time.perf_counter()
    python_implementation(tmp, tmp2)
    timer = time.perf_counter() - start_time
    print("Test python dla wielkości 10^"+str(power)+" czas:"+str(timer))

tests(2)
tests(3)
