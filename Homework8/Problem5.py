import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt, log
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
e0 = 1 / (4 * pi * k)
m0 = 1.25663706e-6 # permeability of free space

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

I = 0.55
c = 0.041
a = 0.022
b = 0.083

phi = (m0 * b * I / (2 * pi)) * log((a + c) / c)

print("phi = " + f"{phi * 1e9 * 10 ** (-9) :.12f}" + " T * m**2")
