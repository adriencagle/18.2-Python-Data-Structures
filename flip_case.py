def flip_case(phrase, to_swap):
    ans = ''
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            ans += letter.swapcase()
        else:
            ans += letter
    return ans

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
print(flip_case('Aaahh', 'a'))