#!/usr/bin/python
#-*- coding: Utf-8 -*-

import math
from matplotlib.pyplot import *


# SCHEMA EULER EXPLICITE/PROGRESSIVE
def euler_explicite(phi,tt):
        uu = [y0]
        for i in range(len(tt)-1): 
                uu.append(uu[i]+h*phi(tt[i],uu[i])) 
        return uu

# INITIALISATION
Nh = 5
t0=0.
y0=1.
tfinal = 3.

def phi(t,y):
        return y

def sol_exacte(t):
        return math.exp(t)


#CALCUL
h = (tfinal-t0)/Nh
tt=[t0+i*h for i in range(Nh+1)]
yy=[sol_exacte(t) for t in tt]
uu = euler_explicite(phi,tt)

# GRAPH
axis([t0, tfinal, min(uu), max(uu)])
plot(tt,yy,"-o",tt,uu,"go")
show()

