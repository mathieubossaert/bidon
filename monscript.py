#!/usr/bin/python
# -*- coding: utf-8 -*-


def moy_coeff(list_coeff, list_note):
    "calcule la moyenne de note à coefficients différents"
    numerateur=0
    denominateur=0
    for i in range (len(list_coeff)):
        numerateur+=list_coeff[i]*list_note[i]
        denominateur+=list_coeff[i]
    return numerateur/denominateur
    
        
# lancement des fonctions
print moy_coeff([2,2,5],[13.,9.,8.])

