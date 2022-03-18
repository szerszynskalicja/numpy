import numpy as np
from numpy import emath 
import time
from copy import deepcopy

start_time = time.perf_counter()
number = np.power(10, 8)
tmp = np.array(np.arange(0,number, dtype=float), dtype=object)
tmp2 = deepcopy(tmp)
end = tmp.dot(tmp2)
end_time = time.perf_counter()
timer = end_time - start_time
print(timer)