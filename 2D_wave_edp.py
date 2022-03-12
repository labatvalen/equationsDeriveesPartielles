""" EQUATION DE LA CHALEUR EN 2D PAR DF """

import numpy as np
import matplotlib.pyplot as plt

if 'qt' in plt.get_backend().lower():
    try:
        from PyQt4 import QtGui
    except ImportError:
        from PySide import QtGui


#### PARAMETRES
##      PHYSIQUES
kappa = 0.5    # kappa : coefficient de diffusion 
Lx = 1.0   # Longueur du domaine (en x)
Ly = 1.0   # Longueur du domaine (en y)
T = 0.3  #Duree en temps
S = 1000000.0         # Terme Source 

##     NUMERIQUES
NT = 250        # Subdivisions de temps
NX = 151               # Subdivisions en espace (en x)
NY = 101               # Subdivisions en espace (en y)
C = 0.05
kappa = C*C
dt = T/NT      # Pas de temps (k)
dx = Lx/(NX-1)   # Pas en espace en x (hx)
dy = Ly/(NY-1)   # Pas en espace en x (hx)

## DISCRETISATION
xx = np.linspace(0,Lx,NX)
yy = np.linspace(0,Ly,NY)

plt.ion()
plt.figure()



### MAIN PROGRAM ###
#INITIALISATION 
uu = np.zeros((NX,NY))

## modification qui n'a pas fonctionne

#for i in range(NX):
#    for j in range(NY):
#        uu[i,j] = np.exp( -40.0 * ( (xx-1.5)*(xx-1.5) + (yy-1.5)*(yy-1.5) ) )



RHS = np.zeros((NX,NY))  #Right Hand Side (second memre)

# Boucle principale, en temps
for n in range(0,NT):
   RHS[1:-1,1:-1] = dt*kappa*( (uu[:-2,1:-1]-2*uu[1:-1,1:-1]+uu[2:,1:-1])/(dx**2)  \
                         + (uu[1:-1,:-2]-2*uu[1:-1,1:-1]+uu[1:-1,2:])/(dy**2) )
   uu[1:-1,1:-1] += (RHS[1:-1,1:-1]+dt*S)


#Plot tous les 100 pas de temps
   if (n%100 == 0):
      plotlabel = "t = %1.2f" %(n * dt)
      plt.pcolormesh(xx,yy,uu,  shading="gouraud")  #flat
      plt.title(plotlabel)
      plt.axis('image')
      plt.draw()
      plt.pause(0.02)     # pause avec duree en secondes
      if 'qt' in plt.get_backend().lower():
          QtGui.qApp.processEvents()

      plt.show()
