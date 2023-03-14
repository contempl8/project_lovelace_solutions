#!/usr/bin/env python3

c = 299792458  # Speed of light [m/s]

def light_time(distance):
    t=distance/c
    return t

print(light_time(376291600))
print(light_time(299792458))