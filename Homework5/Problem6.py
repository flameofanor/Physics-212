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

mass = 1650 # mass in kg of water
deltaT = 30 # degrees celsius
efficency = 0.75

cost = 10.5 # cents / kWh

c = 4184 # joules / kg * degree celsius

joules = (mass * c * deltaT) / 0.75

kwh = joules / (1000 * 3600)
print(kwh)

cents = kwh * cost

dollars = cents / 100
print("cost = $" + f"{dollars:.4f}") # correct! nice!

i = joules / (3.6 * 3600 * 220)
print("current = " + f"{i:.4f}" + " amps")


