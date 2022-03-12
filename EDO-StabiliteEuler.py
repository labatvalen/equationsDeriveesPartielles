#!/usr/bin/python
#-*- coding: Utf-8 -*-

import math
from matplotlib.pyplot import *

# SCHEMAS
def euler_explicite(phi,tt):
        uu = [y0]
        for i in range(len(tt)-1): 
                uu.append(uu[i]+h*phi(tt[i],uu[i])) 
        return uu
	
def phi(t,y): 
        return -y
	
def sol_exacte(t): 
        return math.exp(-t)
	
# INITIALISATION
t0 = 0.
y0 = 1.
tfinal = 12.

# CALCUL H ET SOLUTION APPROCHEE
H = [ 2**(k-2) for k in range(5) ]
tt = []
uu = []

for h in H:
        N = int((tfinal-t0)/h)
        tt.append( [ t0+i*h for i in range(N+1) ] ) 
        uu.append(euler_explicite(phi,tt[-1]))
	
# CALCUL SOLUTION EXACTE
yy = [sol_exacte(t) for t in tt[0]]

# GRAPH SOL EXACTE
axis([t0, tfinal, -10, 10])
subplot(231)
plot(tt[0],yy,'-', label='$y(t)=e^{-t}$')
xlabel('$ t $')
ylabel('$ y $')
legend(loc='best')
#title('$y(t)=e^{-t}$')
grid(True)

# GESTION FENETRE AFFICHAGE
miny=[-0.05, -0.05, -0.05, -1, -27]
maxy=[1.05, 1.05, 1.05, 1, 10]

# GRAPH EULER SELON H
for k in range(5):
        stringa = str('2'+'3'+str(k+2)) 
        subplot(stringa)
        axis([t0, tfinal, miny[k], maxy[k]])
        xlabel('$ t $')
        ylabel('$ u $')
        plot(tt[k],uu[k],'-o', label='h='+str(H[k]))
        legend(loc='best')
        #title('h='+str(H[k])) 
        grid(True)

show()
