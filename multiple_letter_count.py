def multiple_letter_count(phrase):
    letters ={}
    for letter in phrase:
        if letter not in letters:
            letters[f'{letter}'] = 1
        else:
            letters[f'{letter}'] = 1 + letters[f'{letter}']
    return letters

    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
print(multiple_letter_count('howdyd'))