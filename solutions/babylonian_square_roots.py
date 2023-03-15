#!/usr/bin/env python3
   
def babylonian_sqrt(S):
    guess=1
    error=1
    if S == 0: return 0
    while error > 1e-11:
        guess=(guess + (S / guess)) / 2
        error=abs(guess**2 - S) / S
    return guess

print(babylonian_sqrt(420))
print(babylonian_sqrt(0))