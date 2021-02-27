import numpy as np

import math

x = np.array([7.887,4.138])
y = np.array([-8.802,6.776])

x_dot_y = x[0]*y[0] +x[1]*y[1] 
print(x_dot_y)

a = np.array([-5.955,-4.904,-1.874])
b = np.array([-4.496,-8.755,7.103])

adotb = np.dot(a,b)
print(adotb)

p = np.array([3.183,-7.627])
q = np.array([-2.668,5.319])

pdotq = np.dot(p,q)
p_modulus = np.sqrt((p*p).sum() )
q_modulus = np.sqrt((q*q).sum() )

cos_angle_pq = pdotq / p_modulus / q_modulus
radians_pq = np.arccos(cos_angle_pq)
print(radians_pq)

v = np.array([7.35,0.221,5.188])
w = np.array([2.751,8.259,3.985])

vdotw = np.dot(v,w)
v_modulus = np.sqrt((v*v).sum() )
w_modulus = np.sqrt((w*w).sum() )

cos_angle_vw = vdotw / ((v_modulus)*(w_modulus))
radians_vw = np.arccos(cos_angle_vw)
angle_vw = radians_vw * 360.0 /2.0 /np.pi
print(angle_vw)
