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

turns = 18

x = 0.05
y = 0.02
A = x * y

R = 5.9

B0 = 0.25 # tesla
alpha = 225 # seconds ** -1

t1 = 0.001
t2 = 0.02

E1 = -turns * A * B0 * (-alpha) * (e ** (-alpha * t1))
i1 = E1 / R
print("i1 = " + f"{i1:.6f}" + " amps")


E2 = -turns * A * B0 * (-alpha) * (e ** (-alpha * t2))
i2 = E2 / R
print("i2 = " + f"{i2:.6f}" + " amps")

# B1 = B0 * (e ** (-alpha * t1))
# flux1 = (B1-B0) * A
# E1 = -1 * turns * flux1 / t1
# print(E1)
# i1 = E1 / R
# print("i1 = " + f"{i1:.6f}" + " amps")

# B = B0 * e ** (-alpha * t2)
# print(B)
# flux = B * A
# print(flux)
# E2 = turns * flux / t2
# print(E2)
# i2 = E2 / R
# print("i2 = " + f"{i2:.6f}" + " amps")

