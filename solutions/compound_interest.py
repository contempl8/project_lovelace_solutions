#!/usr/bin/env python3

def compound_interest(amount, rate, years):
    new_amount = amount*(1 + rate)**years
    return new_amount

print(compound_interest(1000,0.07,25))