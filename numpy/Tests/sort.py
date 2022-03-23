import numpy as np

x = np.array([2, 1, 3, 0])
y = np.sort(x)
print(y)

x = np.array([True, False, True])
y = np.sort(x)
print(y)

x = np.array(['venus', 'earth', 'mars', 'mercury'])
y = np.sort(x)
print(y)

x = np.array([[4, 3, 2], [1, 2, 0]])
y = np.sort(x)
print(y)

x = np.array([[4, 3, 2], [1, 2, 0]])
y = np.sort(x, axis=0)
print(y)

x = np.array([[4, 3, 2], [1, 2, 0]])
y = np.sort(x, axis=None)
print(y)

dtype = [('name', 'S10'), ('distance_from_sun', int), ('type', 'S10')]
values = [('Saturn', 1429400000, 'outer'), ('Venus', 108200000, 'inner'),
          ('Mars', 227940000, 'inner')]
x = np.array(values, dtype=dtype)

y = np.sort(x, order='distance_from_sun')
print(y)

y = np.sort(x, order=['type', 'name'])
print(y)
