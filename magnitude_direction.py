import numpy as np

import math

x = np.array([-0.221,7.437])
xprime = np.sqrt(x[0]**2 + x[1]**2)
x_unit = x/xprime
print(xprime)

y = np.array([8.813, -1.331,-6.247])
yprime = np.sqrt(y[0]**2 + y[1]**2 +y[2]**2)
y_unit = y/yprime
print(yprime)


a = np.array([5.581, -2.136])
aprime = np.sqrt(a[0]**2 + a[1]**2)
a_unit = a/aprime
print(a_unit)

b = np.array([1.996, 3.108,-4.554])
bprime = np.sqrt(b[0]**2 + b[1]**2 +b[2]**2)
b_unit = b/bprime
print(b_unit)
