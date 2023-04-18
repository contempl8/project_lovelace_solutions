from fractions import Fraction
from math import factorial, comb

def bernoulli(n):
    if n == 0:
        return 1
    if n == 1:
        return -1/2
    return sum([comb(n+1, k) * bernoulli(k) / (n+1-k) for k in range(1, n+1)]) * (-1/n)


print(bernoulli(8))