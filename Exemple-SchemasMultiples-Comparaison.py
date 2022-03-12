#!/usr/bin/python
#-*- coding: Utf-8 -*-

import math
from matplotlib.pyplot import *


#### SCHEMAS
# EULER EXPLICITE/PROGRESSIVE
def euler_explicite(y0,phi,tt):
        uu = [y0]
        N=len(tt)
        h=tt[2]-tt[1]
        for i in range(N-1): 
                uu.append(uu[i]+h*phi(tt[i],uu[i])) 
        return uu

# EULER MODIFIE
def euler_modifie(y0,phi,tt):
        uu = [y0]
        N=len(tt)
        h=tt[1]-tt[0]
        for i in range(N-1):
                k1 = h * phi( tt[i], uu[i] )
                uu.append( uu[i]+h * phi( tt[i]+h/2. , uu[i]+k1/2.)  )
        return uu

# HEUN
def heun(y0,phi,tt):
        uu = [y0]
        N=len(tt)
        h=tt[2]-tt[1]
        for i in range(N-1):
                k1 = h * phi( tt[i], uu[i] )
                k2 = h * phi( tt[i+1], uu[i] +k1)
                uu.append( uu[i] + (k1+k2) /2.0 )
        return uu

# ADAMS D'ORDRE 2
def AB2(y0,phi,tt):
        uu = [y0]
        N=len(tt)
        h=tt[2]-tt[1]
        uu.append(uu[0]+h*phi(tt[0],uu[0]))
        for i in range(1,N-1):
                k1 = h * phi( tt[i], uu[i] )
                k2 = h * phi( tt[i-1], uu[i-1] )
                uu.append( uu[i] + (3.*k1-k2) /2.0 )
        return uu

# ADAMS D'ORDRE 3
def AB3(y0,phi,tt):
        uu = [y0]
        N=len(tt)
        h=tt[2]-tt[1]
        uu.append(uu[0]+h*phi(tt[0],uu[0]))
        uu.append(uu[1]+h*(3.*phi(tt[1],uu[1])-phi(tt[0],uu[0]))/2.)
        for i in range(2,N-1):
                k1 = h * phi( tt[i], uu[i] )
                k2 = h * phi( tt[i-1], uu[i-1] )
                k3 = h * phi( tt[i-2], uu[i-2] )
                uu.append( uu[i] + (23.*k1-16.*k2+5.*k3) /12.0 )
        return uu

# RUNGE-KUTTA D'ORDRE 4
def RK4(y0,phi,tt):
        uu = [y0]
        N=len(tt)
        h=tt[2]-tt[1]
        for i in range(N-1):
                k1 = h * phi( tt[i], uu[i] )
                k2 = h * phi( tt[i]+h/2. , uu[i]+k1/2. )
                k3 = h * phi( tt[i]+h/2. , uu[i]+k2/2. )
                k4 = h * phi( tt[i+1] , uu[i]+k3 )
                uu.append( uu[i] + (k1+2.0*k2+2.0*k3+k4) /6.0 )
        return uu

### PROBLEME DE CAUCHY
#INITIALISATION
t0=0.
y0=1.
tfinal = 1.

def phi(t,y):
        return -2.*y*t

def sol_exacte(t):
        return math.exp(-t**2)

# DISCRETISATION
N = 8
h=(tfinal-t0)/N
tt= [ t0+i*h for i in range(N+1) ]


#CALCULS
yy=[sol_exacte(t) for t in tt]
uu_ep = euler_explicite(y0,phi,tt)
uu_em = euler_modifie(y0,phi,tt)
uu_heun = heun(y0,phi,tt)
uu_AB2 = AB2(y0,phi,tt)
uu_AB3 = AB3(y0,phi,tt)
uu_RK4 = RK4(y0,phi,tt)


###ERREURS
##err_ep = [abs(uu_ep[i]-yy[i]) for i in range(N+1)]
##err_em = [abs(uu_em[i]-yy[i]) for i in range(N+1)]
##err_heun = [abs(uu_heun[i]-yy[i]) for i in range(N+1)]
##err_AB2 = [abs(uu_AB2[i]-yy[i]) for i in range(N+1)]
##err_AB3 = [abs(uu_AB3[i]-yy[i]) for i in range(N+1)]
##err_RK4 = [abs(uu_RK4[i]-yy[i]) for i in range(N+1)]

# GRAPH
figure()
axis([t0, tfinal, min(yy), max(yy)])
plot(tt,yy,'b-',lw=3)
plot(tt,uu_ep,'r-D',tt,uu_em,'m-o',tt,uu_heun,'k-v',tt,uu_AB2,'g->',tt,uu_AB3,'c-+',tt,uu_RK4,'y-D')
legend(['Exacte','Euler explicite', 'Euler modifie', 'Heun','AB2','AB3','RK4'])
show()


#### PLOT DE L'ERREUR
##figure()
##axis([t0, tfinal, min(err_ep), max(err_ep)])
##plot(tt,err_ep,'r-D',tt,err_em,'m-o',tt,err_heun,'k-v',tt,err_AB2,'g->',tt,err_AB3,'c-+',tt,err_RK4,'y-D')
##legend(['Euler explicite', 'Euler modifie', 'Heun','AB2','AB3','RK4'])
##show()

