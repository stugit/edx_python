def recurPower(base, exp):
    if (exp == 0):
        return 1
    elif (exp == 1):
        return base
    else:
        return base * recurPower(base, exp - 1)


print(recurPower(2, 0))
print(recurPower(2, 1))
print(recurPower(2, 2))
print(recurPower(2, 3))
print(recurPower(2, 4))
print(recurPower(2, 5))
