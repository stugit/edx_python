def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    count = 0
    bTup = []

    # loop through aTup
    for a in aTup:
        # count item in aTup
        count=count+1
        # if count is odd
        if (count % 2) == 1:
            # append onto the bTub
            bTup.append(a)
    return tuple(bTup)

# Test
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
