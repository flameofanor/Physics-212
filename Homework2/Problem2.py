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
a = 18.74 
b = 5.07 
n = 4

def E(x):
	return (a * (x ** n)) - b

def aX(A, X, N):
	return (A / N) * X ** N


x1 = 0.55
x2 = 2.03
#xDif = x2 - x1


Vdif = (aX(a, x2, 5) - aX(a, x1, 5)) - (aX(b, x2, 1) - aX(b, x1, 1))
print(Vdif)
#bruh sign error. damn



'''
v1 = E(x1)
v2 = E(x2)
vDif = v2 - v1

x1_volts = v1 * x1
x2_volts = v2 * x2

print(x1_volts)
print(x2_volts)
print(x2_volts - x1_volts)

print("v1 = " + str(v1))
print("v2 = " + str(v2))
print(str(vDif) + " volts")



#V_meter = v2 - v1  #volts per meter
#volts = V_meter * (x2 - x1)
#print(str(volts) + " volts")
'''

