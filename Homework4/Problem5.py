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
c1 = 4.9e-6
c2 = 3.1e-6
c3 = 7.4e-6
c4 = 2.9e-6
c5 = 1.5e-6
c6 = 13e-6

ca = c1 * c2 / (c1 + c2)
cb = c5 + c6
cc = cb * c4 / (cb + c4)

cEq = ca + c3 + cc
print("Ceq = " + f"{cEq * 1e6:.4f}" + " uF") #correct


