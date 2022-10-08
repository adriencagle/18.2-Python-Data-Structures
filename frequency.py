def frequency(lst, search_term):
    x=0
    for num in lst:
        if num == search_term:
            x=x+1
    return x
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
print (frequency([1,1,2,3],2))