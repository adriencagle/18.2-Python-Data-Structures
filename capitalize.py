def capitalize(phrase):
    phrase = phrase.replace (phrase[0], phrase[0].swapcase())
    return phrase
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
print(capitalize('hello'))