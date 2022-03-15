import numpy as np

x = np.linspace(0, 10, 10, endpoint = True)
print(x)

x = np.linspace(0, 10, 10, endpoint = False)
print(x)

x = np.linspace(0,10, 10,endpoint = True, retstep = True)
print(x)

x = np.linspace(0,10, 10,endpoint = True, dtype = int)
print(x)

x = np.linspace(0,10, 10, endpoint = True).astype(int)
print(x)

x = np.linspace(-10,0, 10,endpoint = True, dtype = int)
print(x)

x = np.linspace(-10, 0, 10, endpoint = True).astype(int)
print(x)
