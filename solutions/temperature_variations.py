#!/usr/bin/env python3
from math import sqrt
def temperature_statistics(T):
    mean = 0
    std  = 0
    n = len(T)
    mean = sum(T) / n
    t_numer=0
    for temp in T:
        t_numer+=(temp - mean)**2
    std=sqrt(t_numer / n)
    return mean, std

temps=[4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3]
print(temperature_statistics(temps))