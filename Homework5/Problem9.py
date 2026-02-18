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
v = 12
r1 = 0.75
r2 = 4.75
r3 = 11

ra = (r2 * r3) / (r2 + r3)
req = ra + r1
#print(req)

i = v / req
#print(i)

v1 = i * r1
#print(v1)
v2 = 12 - v1
print(v2)

p = v2 ** 2 / r3
print(p)

p_total = i * v
print(p_total)