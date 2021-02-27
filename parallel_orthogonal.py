import numpy as np
import math

x = np.array([-7.579,-7.88])
y = np.array([22.737,23.64])

x_modulus = np.sqrt((x*x).sum() )
y_modulus = np.sqrt((y*y).sum() )

xdoty = np.dot(x,y)
x_modulus = np.sqrt((x*x).sum() )
y_modulus = np.sqrt((y*y).sum() )

cos_angle_xy = xdoty / ((x_modulus)*(y_modulus))
radians_xy = np.arccos(cos_angle_xy)
angle_xy = radians_xy * 360.0 /2.0 /np.pi
print(angle_xy)

a = np.array([-2.029,9.97,4.172])
b = np.array([-9.231,-6.639,-7.245])
adotb = np.dot(a,b)
a_modulus = np.sqrt((a*a).sum() )
b_modulus = np.sqrt((b*b).sum() )

cos_angle_ab = adotb / ((a_modulus)*(b_modulus))
radians_ab = np.arccos(cos_angle_ab)
angle_ab = radians_ab * 360.0 /2.0 /np.pi
print(angle_ab)

p = np.array([-2.328,-7.284,-1.214])
q = np.array([-1.821,1.072,-2.94])
pdotq = np.dot(p,q)
p_modulus = np.sqrt((p*p).sum() )
q_modulus = np.sqrt((q*q).sum() )

cos_angle_pq = pdotq / ((p_modulus)*(q_modulus))
radians_pq = np.arccos(cos_angle_pq)
angle_pq = radians_pq * 360.0 /2.0 /np.pi
print(angle_pq)

v = np.array([2.118,4.827])
w = np.array([0,0])
vdotw = np.dot(v,w)
print(vdotw)

