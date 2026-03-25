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

''' unit conversions:
F to pF x * 1e12
F to nF x * 1e9
F to uF x * 1e6
F to mF x * 1e3
mF to F x * 1e-3
uF to F x * 1e-6
nF to F x * 1e-9
pF to F x * 1e-12
'''


#problem variables

R = 412.3
C = 93.54e-6
L = 16.28e-3
f = 100


xL = 2 * pi * f * L
xC = 1 / (2 * pi * f * C)

print("xL = " + f"{xL:.5f}" + " \u03A9")
print("xC = " + f"{xC:.5f}" + " \u03A9")

Z = sqrt(R**2 + (xL - xC)**2)
print("Z = " + f"{Z:.5f}" + " \u03A9")
