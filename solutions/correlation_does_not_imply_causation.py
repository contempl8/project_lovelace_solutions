#!/usr/bin/env python3

import numpy as np

def correlation_coefficient(x, y):
    r = 0
    numerator=np.cov(x,y, bias=True)[0][1]
    denomenator=np.std(x)*np.std(y)
    r=numerator/denomenator

    return r

x = [  5427,   5688,   6198,   6462,   6635,   7336,   7248,   7491,   8161,   8578,   9000]
y = [18.079, 18.594, 19.753, 20.734, 20.831, 23.029, 23.597, 23.584, 22.525, 27.731, 29.449]

print(correlation_coefficient(x,y))