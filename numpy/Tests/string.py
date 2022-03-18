import numpy as np

tmp = 'c'
x = np.char.isalpha(tmp)
print(x)

tmp = 'razdwa3'
x = np.char.isalpha(tmp)
print(x)

x = np.char.index(tmp, 'r')
print(x)

tmp = np.array(['la'])
x = np.char.multiply(tmp,5)
print(x[0])

x = np.char.upper(x[0])
print(x)

tmp = 'raz dwa 3'
x = np.char.isupper(tmp)
print(x)

tmp = 'RAZDWA3'
x = np.char.isupper(tmp)
print(x)
