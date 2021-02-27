import numpy as np
import math

a = np.array([3.039,1.879])
b = np.array([0.825,2.036])

adotb = np.dot(a,b)
b_modulus = np.sqrt((b*b).sum() )
projab = (adotb / b_modulus **2) * b
print(projab)

x = np.array([-9.88,-3.264,-8.159])
y = np.array([-2.155,-9.353,-9.473])

xdoty = np.dot(x,y)
y_modulus = np.sqrt((y*y).sum() )
projxy = (xdoty / y_modulus**2) * y
x_perp = x - projxy
print(x_perp)

p = np.array([3.009,-6.172,3.692,-2.51])
q = np.array([6.404,-9.144,2.759,8.718])

pdotq = np.dot(p,q)
q_modulus = np.sqrt((q*q).sum() )
projpq = (pdotq / q_modulus**2) * q
p_perp = p - projpq
print(projpq)
print(p_perp)
