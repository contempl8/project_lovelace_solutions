#!/usr/bin/env python3

from math import sqrt

def habitable_exoplanet(L, r):
    inner_chz, outer_chz = sqrt(L/1.1), sqrt(L/0.54)
    if r > outer_chz: return "too cold"
    elif r < inner_chz: return "too hot"
    else: return "just right"

print(habitable_exoplanet(1.11,1.04))
print(habitable_exoplanet(1.5,2.5))