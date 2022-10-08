from re import X


def truncate(phrase, n):
    x=0
    ans = ''
    if n>3:
        if n<len(phrase):
            while x<n-3:
                 ans = ans + phrase[x]
                 x +=1
            return f'{ans}...'
        else:
            return phrase
    else:
        return 'n must be greater than 3'
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
print(truncate("Problem solving is the best!", 10))
print(truncate("Yo", 100))