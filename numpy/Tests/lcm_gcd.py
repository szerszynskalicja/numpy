import numpy as np

x1 = 12
x2 = 20
y = np.lcm(x1, x2)
print(y)

x = np.array([3, 4, 6, 18])
y = np.lcm.reduce(x)
print(y)

x = np.arange(6)
y = np.lcm(x, 20)
print(y)

x1 = np.arange(6)
x2 = np.arange(3, 9)
y = np.lcm(x1, x2)
print(y)

x1 = 12
x2 = 20
y = np.gcd(x1, x2)
print(y)

x = np.array([4, 20, 12, 8])
y = np.gcd.reduce(x)
print(y)

x = np.arange(6)
y = np.gcd(x, 20)
print(y)

x1 = np.arange(6)
x2 = np.arange(3, 9)
y = np.gcd(x1, x2)
print(y)