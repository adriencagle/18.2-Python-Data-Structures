def reverse_string(phrase):
    tempStr = ''
    x= len(phrase)
    for letter in phrase:
        tempStr = tempStr + phrase[x-1]
        x=x-1
    return tempStr

    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
print (reverse_string('hello'))