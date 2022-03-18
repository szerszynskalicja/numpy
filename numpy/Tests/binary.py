import numpy as np

x = np.binary_repr(4, 8)
print(x)

x = np.binary_repr(100,8)
print(x)

x = np.invert(True)
print(x)

x = np.invert(False)
print(x)

x = np.bitwise_and(1,1)
print(x)

x = np.bitwise_and(1,0)
print(x)

x = np.bitwise_or(1,1)
print(x)

x = np.bitwise_or(0,0)
print(x)

x = np.bitwise_or([0,0],[1,1])
print(x)