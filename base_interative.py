def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 0
    loop = exp
    for i in range(0, exp + 1):
        if (i == 0):
            result = 1
        elif (i == 1):
            result = base
        elif (i > 1):
            result = result * base
        #print("loop ", i, " result ", result)
     
    result = round(result, 4)
    #print("base ", base, " exp ", exp, " result ", result )
    return result


iterPower(2, 0)
iterPower(2, 1)
iterPower(2, 2)
iterPower(2, 3)
iterPower(4.51, 0)
iterPower(-0.6, 8)
iterPower(8.28, 1)
iterPower(-8.16, 9)
