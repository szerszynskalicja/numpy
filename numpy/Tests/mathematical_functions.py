import numpy as np

tmp = 90
x = np.radians(tmp)
print(x)

x = np.degrees(x)
print(x)

tmp = -90
x = np.radians(tmp)
print(x)

x = np.degrees(x)
print(x)


tmp = 400
x = np.radians(tmp)
print(x)

x = np.degrees(x)
print(x)


tmp = [2.93, -1.99, 4.69, 9.01, -5.91, -3.99]
x = np.sum(tmp)
print(x)

x = np.sum(np.ones(10000))
print(x)

x = np.sum(np.random.rand(6))
print(x)

x = np.gradient(tmp)
print(x)

x = np.gradient(np.zeros(5))
print(x)

x = np.gradient(np.ones(5))
print(x)

x = np.gradient(np.random.rand(6))
print(x)