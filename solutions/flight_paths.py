#!/usr/bin/env python3

from math import radians, sqrt, asin, sin, cos

R  = 6372.1  # Radius of the Earth [km]

def haversine_distance(lat1, lon1, lat2, lon2):
    rlat1,rlon1,rlat2,rlon2 = radians(lat1), radians(lon1), radians(lat2), radians(lon2)
    scomp = sin((rlat2 - rlat1) / 2) ** 2
    ccomp = cos(rlat1) * cos(rlat2) * sin((rlon2 - rlon1) / 2) ** 2
    d = 2 * R * asin(sqrt(scomp+ccomp))
    return d

print(haversine_distance(46.283,86.667,-48.877,-123.393))