#!/usr/bin/python
#-*- coding: Utf-8 -*-

import math
from matplotlib.pyplot import *


# SCHEMA EULER EXPLICITE
def euler_explicite(phi,tt):
	uu = [y0]
	for i in range(len(tt)-1): 
		uu.append(uu[i]+h*phi(tt[i],uu[i])) 
	return uu

# INITIALISATION
def phi(t,y): 
	return y

def sol_exacte(t): 
	return math.exp(t)

t0 = 0.
y0 = 1.
tfinal = 1.


err = []    # Vecteur erreur
K = 12     # Nb totale de valeur de h

# CALCUL
yy_tfinal = sol_exacte(tfinal)
H = [ 2**(-k-1) for k in range(K) ]   # Vecteur contenant toutes les valeurs de h=1/N
for h in H:
	N = int((tfinal-t0)/h)
	tt = [ t0+i*h for i in range(N+1) ]  # Vecteur des noeuds
	uu = euler_explicite(phi,tt) 
	uu_tfinal = uu[N-1]               # Récupération de la denière valeur de u (temps final)
	err.append(abs(yy_tfinal-uu_tfinal))  # Erreur

# ESTIMATION ORDRE DE CONVERGENCE
pente = [ math.log(err[k]/err[k-1])/math.log(H[k]/H[k-1]) for k in range(2,K)] 
print (pente)   # Affichage des valeurs de la pente "p"


# ECHELLE LOG-LOG
axis([H[-1], H[0], min(err), max(err)])
loglog(H,err, linewidth=2, color='red',label='$\ln(e(h))\sim\ln(h)$') 
xlabel('$\ln(h)$')
ylabel('$\ln(e)$')
legend(loc='best')
grid(True)
show()
