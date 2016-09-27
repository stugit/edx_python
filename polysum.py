from math import pi, tan

def polysum(n, s):
    a = 0.25 * n * s**2 / tan(pi/n)
    r = (s * n) ** 2
    return round(a + r, 4)


print( polysum(80, 13))
