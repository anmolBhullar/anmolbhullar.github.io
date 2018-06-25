def MaxIndex(L):
    # Pre: L is a nonempty list of integers
    # Post: Returns the highest index of the smallest
    #       (integer) element in L
    i = 0
    j = len(L)-1
    while i < j:
        if L[i] < L[j]:
            j = j-1
        else:
            i = i+1
    return j
