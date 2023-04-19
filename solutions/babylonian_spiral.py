# https://www.youtube.com/watch?v=faFOJ6hF0UY
import math
import numpy as np

def compute_step(prev_step):
    '''
    Computing the longest vector in series with integral endpoints on a Cartesian grid
    '''
    max_step = int(math.sqrt(prev_step)) + 2
    min_step = 0

    next_d = prev_step**4 # Big value to minimize
    placeholder_steps=[]
    for i in range(min_step,max_step+1):
        for j in range(min_step,max_step+1):
            idx_distance = i**2 + j**2
            if prev_step < idx_distance <= next_d:
                next_d = idx_distance
                placeholder_steps.append(np.array([i,j]))
    computed_steps=[]
    for ph in placeholder_steps:
        if ph[0]**2 + ph[1]**2 == next_d:
            computed_steps.append(ph)
    return computed_steps, next_d


def babylonian_spiral(n_steps):
    x = [0, 0]
    y = [0, 1]

    return x, y