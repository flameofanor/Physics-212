import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt
from math import pi, e

#remember that trig functions are all in radians

#constants
g = 9.8 #m/s
G = 6.6743 * 10 ** (-11) #m^3 / kg * s^2
k = 8.988 * 10 ** 9
protonCharge = 1.60217733 * 10 **(-19) #C
protonMass = 1.672621 * 10 ** (-27) #kg

#horizontal
E = 3.8 * 10 ** 5 # newtons per coulomb
V = 1.7 * 10 ** 7 # meters per second
L = 0.12 # meters
t = L / V

#vertical
F = E * protonCharge

x0 = 0
x1 = None	
v0 = 0
v1 = None
a = F / protonMass

x1 = 0.5 * a * t ** 2
print(str(x1 * 1000) + "mm")
#YOOOO first attempt correct! hell yeah dude

v1 = a * t
theta = atan(v1 / V) #radians
thetaDeg = (theta / pi) * 180
print(thetaDeg)

