import numpy as np

x = np.allclose([1e10,1e-6], [1.00001e10,1e-7])
print(x)

x = np.allclose([1e12,1e-8], [1.00001e12,1e-9])
print(x)

x = np.allclose([1e10,1e-8], [1.0001e10,1e-9])
print(x)

x = np.allclose([1.0, np.nan], [1.0, np.nan])
print(x)

x = np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)
print(x)

x = np.allclose(1., 1.)
print(x)

x = np.allclose(1., 1. + 0j)
print(x)

x = np.allclose(np.inf, np.inf)
print(x)

x = np.allclose(np.inf + 0j, np.inf)
print(x)

x = np.allclose(np.inf + 0j, np.inf + 0j)
print(x)

x = np.allclose(1 + np.inf * 1j, 1 + np.inf * 1j)
print(x)