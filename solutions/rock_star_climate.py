def rock_temperature(S, a, e):
    SB_CONST=5.670374419*10**-8
    numerator = (1 - a) * S
    denominator = 4 * e * SB_CONST
    res = numerator / denominator
    kelvin = res ** (1. / 4)
    return kelvin - 273.15

print(rock_temperature(1361,0.306,0.612))