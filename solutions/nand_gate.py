#!/usr/bin/env python3

def NAND(A, B):
    nand = not (A and B)
    return int(nand)

print(NAND(1,1))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(0,0))