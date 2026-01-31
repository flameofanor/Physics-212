import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import pi, e

#remember that trig functions are all in radians

#constants
g = 9.8 #m/s
elementary_charge = 1.602176634 * 10 ** (-19) # also electron volt eV
mass_electron = 9.109 * 10 ** (-31) #kg

G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9
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
v1 = 21
v2 = 169
Vdif = v2 - v1
#U = Vdif * elementary_charge
print(Vdif) #yay!

#part two, velocity of the electron
velocity = sqrt((2 * elementary_charge * Vdif) / mass_electron)
print(str(velocity) + " m/s") #hell yes



