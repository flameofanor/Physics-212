import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import pi, e

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables
Q = 5.7 * 10 ** (-6) #Coulombs
R = 0.45 #meters
Rho = Q / pi


E = (2 * k * Rho) / R ** 2
print(E)
#yurrrr correct!

