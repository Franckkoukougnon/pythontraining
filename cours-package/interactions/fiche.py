#!/usr/bin/env python
# -*- coding: utf-8 -*-
from func import *
from utils.operations import ajoute_deux

age = input("Quel est votre age? : ")
print("Vous avez %d ans" % age)

age_plus_un = ajoute_un(age)

print ("dans un an vous aurez %d ans " % age_plus_un)

age_plus_deux = ajoute_deux(age)
print("Dans deux ans vous aurez %d ans" % age_plus_deux)