#!/usr/bin/env python3

from math import exp

v_e = 2550  # rocket exhaust velocity [m/s]
M = 250000  # rocket dry mass [kg]

def rocket_fuel(v):
    m_fuel = M * (exp(v/v_e)-1)
    return m_fuel

print(rocket_fuel(11186.0))
print(rocket_fuel(500.0))