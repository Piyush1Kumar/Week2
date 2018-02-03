def isIn(char,aStr):
    if aStr=='':
        return False
    if len(aStr)==1:
        return aStr==char
    mid=int(len(aStr/2))
    midChar=aStr[mid]
    if char==midChar:
        return True
    elif char<midChar:
        return isIn(char,aStr[:mid])
    else:
        return isIn(char,aStr[mid+1:])
