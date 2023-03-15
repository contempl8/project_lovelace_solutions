#!/usr/bin/env python3

def area_of_rectangles(rects, dx):
    area = 0
    for height in rects:
        area+=height*dx
    return area

print(area_of_rectangles([0, 1, 2, 3, 4, 5],1.5))
print(area_of_rectangles([-1, 2, -3, 4, -5],2))