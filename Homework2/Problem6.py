import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import pi, e

#remember that trig functions are all in radians

#constants
g = 9.8 #m/s
elementary_charge = 1.602176634 * 10 ** (-19) # also electron volt eV
mass_electron = 9.109 * 10 ** (-31) #kg

G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9
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

q1 = 9.5 * 10 **(-6)
q2 = -54 * 10 **(-6)
q3 = 35 * 10 **(-6)

a = 39 / 100
b = 74 / 100
c = sqrt (a**2 + b**2)

Ua = k * q1 * q2 / a
Ub = k * q3 * q2 / b
Uc = k * q1 * q3 / c
U = Ua + Ub + Uc
print(U) #nice

# change if q3 is brought into its position from infinitely far away
print(Ub + Uc)



