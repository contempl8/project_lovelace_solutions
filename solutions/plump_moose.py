#!/usr/bin/env python3

def moose_body_mass(latitude):
    mass = 2.757 * latitude + 16.793
    return mass

print(moose_body_mass(60.5))