import math
from math import sin, cos, tan, asin, acos, atan
from math import pow, sqrt, log
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
e0 = 1 / (4 * pi * k)
m0 = 1.25663706e-6 # permeability of free space

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

sol_turns = 550
sol_length = 0.655
n = sol_turns / sol_length

R = 0.0481
r = 0.0173
turns = 31
resistance = 3.06

i_rise = 23.9
t_run = 0.00198
di_dt = i_rise / t_run

db_dt = m0 * n * di_dt
emf = -1 * turns * db_dt * pi * r ** 2
print(emf)

I = emf / resistance
print(I) #YAAAAH BUDDY CORRECT! FIRST TRY!!!!


