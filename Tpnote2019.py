#!/usr/bin/python
#-*- coding: Utf-8 -*-

## Permet que la division se fasse correctement (division réelle et pas division entière)
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

## But : Pas spatial
## Entrées : (a,b) bornes, N subdivisions
## Sortie : h réel
def deltax(a,b,N):
    h=(b-a)/N
    return h


## But : Pas temporel
## Entrées : (a,b) bornes, M subdivisions
## Sortie : k réel
def deltat(a,b,M):
    k=(b-a)/M
    return k


## But : Discretisation spatiale
## Necessite : deltax(a,b,N)
## Entrées : (a,b) bornes, N subdivisions
## Sortie : xx vecteur
def vectspace(a,b,N):
    H = deltax(a,b,N)
    x = a
    xx = []
    for i in range(0,N+1) :
        xx.append(x)
        x = x + H
    return xx


## But : Discretisation temporelle
## Necessite : deltat(a,b,M)
## Entrées : (a,b) bornes, M subdivisions
## Sortie : tt vecteur
def vecttime(a,b,M):
    H = deltat(a,b,M)
    t = a
    tt = []
    for i in range(0,M+1) :
        tt.append(t)
        t = t + H
    return tt


## But : Condition initiale
## Entrées : xx vecteur
## Sortie : uu vecteur
def initcond(xx):
    n = np.size(xx)
    uu = np.zeros(n)
    return uu


## But : Condition de dirichlet
## Entrées : t reel
## Sortie : u reel
def initcond(t):
    u = 20
    return u


xx = vecttime(1,5,5)
print(xx)
print(initcond(xx))
