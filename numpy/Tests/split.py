import numpy as np

x = np.arange(4.)
y = np.array_split(x, 2)
print(y)

x = np.arange(10)
y = np.array_split(x, 4)
print(y)

x = np.arange(3.)
y = np.array_split(x, 4)
print(y)

x = np.array([[0, 1],
              [2, 3],
              [4, 5],
              [6, 7],
              [8, 9]])
y = np.array_split(x, 3)
print(y)

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])
y = np.array_split(x, 3)
print(y)

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
y = np.array_split(x, 3, axis=1)
print(y)