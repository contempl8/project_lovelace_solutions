#!/usr/bin/env python3

def rna(dna):
    return dna.replace("T","U")[::-1]

print(rna("CCTAGGACCAGGTT"))