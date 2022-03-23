from cmath import pi
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

tmp =  np.arange(13.) * 30.
print(tmp)
x = np.radians(tmp)
print(x)

out = np.zeros((tmp.shape))
np.radians(tmp, out)
print(out)
