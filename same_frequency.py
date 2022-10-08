def same_frequency(num1, num2):
    num3=f'{num1}'
    num4=f'{num2}'
    for num in num3:
        if num3.count(num) != num4.count(num):
            return False
    return True
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))