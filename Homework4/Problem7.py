import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import pi, e

# f"{some_float:.4f}"
# print("x = " + f"{x:.4f}" + " \u03A9")

#remember that trig functions are all in radians

#constants
g = 9.8 #m/s
elementary_charge = 1.602176634e-19 # also electron volt eV
mass_electron = 9.109e-31 #kg

G = 6.6743e-11 #m^3 / kg * s^2
k = 8.988e9
E0 = 1 / (4 * pi * k)

''' kinematics
x0 = 
x1 = 
v0 = 
v1 = 
a = 
deltaT =
'''

#problem variables 
v1 = 525
c1 = 837.8e-15
c2 = 237.7e-15

v2 = c1 * v1 / c2
print("v2 = " + f"{v2:.2f}" + " volts") #correct

e1 = 0.5 * c1 * v1
e2 = .5 * c2 * v2
print(e1 == e2)

q1 = c1 * v1
d1 = k * c1


q2 = c2 * v2
d2 = k * c2

print(q1 == q2)