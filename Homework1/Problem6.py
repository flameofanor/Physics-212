import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9

#problem variables

Ra = 0.55 #meters
Rb = 0
Qa = 2.5 * 10**(-6)
Qb = 4.5 * 10**(-6)

Rb = sqrt((Qb * Ra ** 2) / Qa)
print(str(Rb) + " meters")
print(str(Rb * 100) + "cm")

#correct!
