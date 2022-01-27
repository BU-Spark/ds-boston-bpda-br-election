def remove_accents(word):
    '''
    Removes accents from text data
    :param word - A string from which accents should be removed
    :return The name with the accent removed
    '''
    #Source - https://pypi.org/project/Unidecode/
    from unidecode import unidecode
    remove_accent =unidecode(word)
    return remove_accent