import numpy as np
import math

p = np.array([-4.046,2.836,1.21])
q = np.array([10.115,7.09,3.025])

intsec_x = (q[1]*p[2] - p[1]*q[2])/ (p[0]*q[1] - p[1]*q[0])
intsec_y = (-q[0]*p[2] + p[0]*q[2])/ (p[0]*q[1] - p[1]*q[0])
print(intsec_x,intsec_y)

p = np.array([7.204,3.182,8.68])
q = np.array([8.172,4.114,9.883])

intsec_x = (q[1]*p[2] - p[1]*q[2])/ (p[0]*q[1] - p[1]*q[0])
intsec_y = (-q[0]*p[2] + p[0]*q[2])/ (p[0]*q[1] - p[1]*q[0])
print(intsec_x,intsec_y)

p = np.array([1.182,5.562,6.744])
q = np.array([1.773,8.343,9.525])

#intsec_x = (q[1]*p[2] - p[1]*q[2])/ (p[0]*q[1] - p[1]*q[0])
#intsec_y = (-q[0]*p[2] + p[0]*q[2])/ (p[0]*q[1] - p[1]*q[0])
#print(intsec_x,intsec_y)