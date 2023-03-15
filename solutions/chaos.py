#!/usr/bin/env python3

def logistic_map(r):
    x = [0.5]
    for n in range(0,50):
        x.append(r*x[n]*(1-x[n]))
    return x

# print(logistic_map(2.81))
print(logistic_map(2))
# print(logistic_map(3.88))