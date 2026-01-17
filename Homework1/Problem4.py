import math
from math import sin
from math import cos


#t = 0
l = 1.14 # m 
m = 0.00348 # kg
theta = 8.07 # degrees


#Fe = 0
g = 9.8 # m/s
k = 8.988 * 10 ** 9

Ty = m * g
print(Ty)
Tx = (Ty / cos(theta) ) * sin(theta)
print(Tx)


#Fx = t * sin(theta) + Fe
#Fy = t * cos(theta) - m*g

#(k2q) / l * sin(theta)

rsquared = (l * sin(theta) * 2) ** 2

qsquared = (Tx * rsquared) / (k)
print(qsquared)

q = math.sqrt(-1 * qsquared)
print(q)

#hmmm one more attempt. try solving on paper?
