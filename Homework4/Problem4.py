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
c1 = 55e-6
c2 = 15e-6
v = 1.5

q1 = c1 * v
q2 = c2 * v

print("q1 = " + f"{q1 * 1e6:.4f}" + " uC")
print("q2 = " + f"{q2 * 1e6:.4f}" + " uC")

cEq = c1 + c2
print("cEq = " + f"{cEq * 1e6:.4f}" + " uF")

