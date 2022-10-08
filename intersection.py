def intersection(l1, l2):
    ans = []
    for item in l1:
        if l2.count(item) >= 1:
            ans.append(item)
    return ans
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
print (intersection([1, 2, 3], [2, 3, 4]))