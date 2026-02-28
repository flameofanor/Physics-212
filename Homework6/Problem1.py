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
R2 = 2.5
r1 = 0.5
R3 = 1.5
r2 = 0.5
E1 = 18
E2 = 45
I2 = 0.27

I3 = (-R2*I2 + E1 - r1*I2 - E2) / (-1 * (R3 + r2))
print("I3 = " + f"{I3:.4f}" + " amps")