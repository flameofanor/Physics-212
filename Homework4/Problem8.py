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

''' kinematics:

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
l = 8.85 / 100
d = 3.22 / 1000
A = l ** 2 

pyrex = 5.6
polystyrene = 2.56

c1 = (E0 * A * pyrex) / (d / 2)
c2 = (E0 * A * polystyrene) / (d / 2)

Ceq = (c1 * c2) / (c1 + c2)

print("C = " + f"{Ceq * 1e12:.4f}" + " pF")

v = 67.3

U = 0.5 * Ceq * v ** 2
print("U = " + f"{U * 1e6:.4f}" + " uJ")
