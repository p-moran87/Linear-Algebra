import numpy as np
import math

a = np.array([8.462,7.893,-8.187])
b = np.array([6.984,-5.975,4.778])

acrossb = np.cross(a,b)
print(acrossb)

x = np.array([-8.987,-9.838,5.031])
y = np.array([-4.268,-1.861,-8.866])

xcrossy = np.cross(x,y)
area_parallelogram_xy = np.sqrt((xcrossy*xcrossy).sum() ) 
print(area_parallelogram_xy)

p = np.array([1.5,9.547,3.691])
q = np.array([-6.007,0.124,5.772])

pcrossq = np.cross(p,q)
area_triangle_pq = np.sqrt((pcrossq*pcrossq).sum() ) *0.5
print(area_triangle_pq)