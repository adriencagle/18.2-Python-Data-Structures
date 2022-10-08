def single_letter_count(word, letter):
    x =0
    for letters in word:
        if letters.lower() == letter:
                x=x+1
    return x
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
print(single_letter_count('Hello World', 'd'))