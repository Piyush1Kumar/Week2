def recurPower(base,exp):
    if exp==1:
        return base
    else:
        return base*recurPower(exp-1)
