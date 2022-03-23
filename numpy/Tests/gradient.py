import numpy as np
tmp = [2, -1, 4, 9, -5, -3]
tmp2 = [1, -1, 10, -21, 0, 93]


x = np.gradient(tmp)
print(x)


x = np.gradient(tmp, 2)
print(x)

x = np.gradient(tmp, tmp2)
print(x)


x = np.gradient([tmp, tmp2], axis = 1)
print(x)

x = np.gradient(np.zeros(5))
print(x)

x = np.gradient(np.ones(5))
print(x)

tmp = np.random.rand(15)
x = np.gradient(tmp, edge_order=2)
print(x)