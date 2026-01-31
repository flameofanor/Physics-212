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
a = 18.74 # N / (C * m ** 4)
b = 5.07 # 
n = 4

def E(x):
	return (a * (x ** n)) - b

x1 = 0.55
x2 = 2.03

v1 = E(x1)
v2 = E(x2)

V_meter = v2 - v1  #volts per meter
volts = V_meter * (x2 - x1)
print(str(volts) + " volts")


