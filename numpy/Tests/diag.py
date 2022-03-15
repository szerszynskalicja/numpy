import numpy as np

y = [0, 2, 4, 8]
x = np.diag(y)
print(x)

x = np.diag(x)
print(x)

y = np.diag(np.diag(np.arange(100)))
print (y)

x = np.arange(16).reshape((4,4))
print(x)
y = np.diag(x)
print(y)

y = np.diag(x, 1)
print(y)

y = np.diag(x,-1)
print(y)

y = np.diag(x,2)
print(y)

y = np.diag(x,3)
print(y)

y = np.diag(x,4)
print(y)

x = np.arange(6).reshape((3,2))
print(x)

y = np.diag(x)
print(y)

x = []
y = np.diag(x)
print(y)

#gives error
x = np.arange(8).reshape(2,2,2)
y = np.diag(x)
print(x)