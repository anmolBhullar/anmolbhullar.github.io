def RecPowerTwo(n):
    # Pre:  n is a natural number
    # Post: Returns 2^n.
    if n == 0:
        result = 1
    else:
        result =  2 * RecPowerTwo(n-1)
    return result
