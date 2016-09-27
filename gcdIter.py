def gcdIter(a, b):

    d = a;
    if d > b:
        d = b

    while (not (a % d == 0 and b % d == 0)):
        d-=1
        if (d == 1):
            break

    return d


print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))
