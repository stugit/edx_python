def isIn(char, aStr):
    if len(aStr) == 0:
        return False
    
    if len(aStr) == 1:
        return char == aStr;

    i = int(len(aStr)/2)

    print("i: " + str(i))
    print("aStr: " + aStr)

    if char == aStr[i]:
        return True
    elif char < aStr[i]:
        if i > 0:
            print("splice aStrl: " + aStr[0:i])
            return isIn(char, aStr[0:i])
    else:
        if i < len(aStr) - 1:
            print("splice aStrr: " + aStr[i:len(aStr)])
            return isIn(char, aStr[i:len(aStr)])
    return False
        
#print(isIn('c', 'abcd'))
print(isIn('k', 'bdfffjjknvx'))
