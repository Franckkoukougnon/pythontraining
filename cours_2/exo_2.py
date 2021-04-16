#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
16/04/2021
Author: ib
"""
pSeuil = 2.3
vSeuil = 7.41

volume_courant = int(input("un nbre pour definir le volume:"))
pression_courant = int(input('un nbre pour definir la pression:'))

if volume_courant > vSeuil and pression_courant > pSeuil:
    print(" arret immediat")
elif pression_courant > pSeuil:
    print("Augmenter le volume l'enceinte")
elif volume_courant > vSeuil:
    print("diminuer le volume de l'enceinte")
else:
    print("tout va bien")
