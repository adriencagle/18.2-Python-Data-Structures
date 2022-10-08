def remove_every_other(lst):
    x=0
    ans =[]
    for item in lst:
        if x == 1:
            x =x-1
        else:
            ans.append(item)
            x=x+1
    return ans
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
print(remove_every_other([1, 2, 3, 4, 5]))