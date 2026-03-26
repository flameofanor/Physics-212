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

R = 0.39e-3
I = 7.5

A = I / (pi * R ** 2 / 3)
#print("A = " + f"{A:.0f}" + " Amps per Meter squared")


iMax = A * pi * R**2 / 3
#print("iMax = " + f"{iMax:.4f}" + " Amps")

r = R * 0.74
Bin = (m0 * I * r) * ( 3/2 - r/R )/(pi * R ** 2 )
print("r = " + f"{r:.6f}" + " m")
print("Bin = " + f"{Bin:.6f}")

