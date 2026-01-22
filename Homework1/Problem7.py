import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables
ringCharge = 5.7 * 10 ** (-6) #Coulombs
radius = 0.45 #meters

Fe = (k * ringCharge) / radius ** 2
print(Fe)

