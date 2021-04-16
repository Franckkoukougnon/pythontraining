#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
16/04/2021
Author: ib
"""
nbre = float(input(" saisir un nombre: "))

if nbre < 0:
    print(" vous avez choisi un nombre inferieur a zero")
else:
    print(nbre ** 0.5)
