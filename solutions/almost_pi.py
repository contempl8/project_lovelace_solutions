#!/usr/bin/env python3

def almost_pi(N):
    pi=0
    for k in range(0,N):
        numerator=(-1)**k
        denomenator=2*k+1
        pi+=numerator/denomenator
    pi*=4
    return pi

print(almost_pi(25))
print(almost_pi(10000))