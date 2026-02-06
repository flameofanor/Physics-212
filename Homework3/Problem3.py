import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import pi, e

# f"{some_float:.2f}"
# print("R1 = " + f"{r1:.2f}" + " \u03A9")

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

q1 = 5.11e-9
q2 = -5.11e-9
q3 = 17.2e-9
q4 = -16.3e-9

Flux_1 = q1 / E0
print("Flux 1 = " + f"{Flux_1:.4f}")

Flux_2 = (q1 + q2) / E0
print("Flux 2 = " + f"{Flux_2:.4f}")

Flux_3 = (q2 + q3) / E0
print("Flux 3 = " + f"{Flux_3:.4f}")

Flux_4 = (q1 + q2 + q3 + q4) / E0
print("Flux 4 = " + f"{Flux_4:.4f}")

#nice!