


import math
from matplotlib.pyplot import *


def phi(alpha,y):
    return alpha*y


# euler explicite
def euler_explicite(phi,tt,h):
        uu = [1.0] ## car y_0 = 1
        N=len(tt)
        for i in range(N-1): 
                uu.append(uu[i]+h*phi(tt[i],uu[i])) 
        return uu

# solution exacte
def sol_exacte (t) :
    return math.exp(t)

# donnees initiales
t0 = 0.0
tfinal = 2.0
N = 5
y0 = 1
alpha = 1


#donnees graphe
h = (tfinal - t0)/N
tt = [ t0+i*h for i in range(N+1) ]
yy=[sol_exacte(t) for t in tt]
uu = euler_explicite(phi,tt,h)

# graphique 1
figure()
axis([t0,tfinal,min(uu),max(uu)])
plot(tt,uu,'go')
show()


#donnees graphe
N10 = 10
h10 = (tfinal - t0)/N10
tt10 = [ t0+i*h for i in range(N+1) ]
yy10=[sol_exacte(t) for t in tt]
uu10 = euler_explicite(phi,tt,h10)

# graphique 2
axis([t0,tfinal,min(uu),max(uu)])
plot(tt,uu,'go')
show()


#question 2, a

#donnees graphe
N50 = 50
h50 = (tfinal - t0)/N50
tt50 = [ t0+i*h for i in range(N+1) ]
yy50=[sol_exacte(t) for t in tt]
uu50 = euler_explicite(phi,tt,h50)

#graphique 3
axis([t0,tfinal,min(yy),max(yy)])
plot(tt,yy,'-o')
show()



# question 2, b
imax=12
N = [ 2**i for i in range(imax+1) ]
H = [ 1./(2**i)for i in range(imax+1) ]
print N
print H

## Les graphiques 4 et 5 n'ont pas été effectués par manque de temps