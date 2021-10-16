
def remove_accents(row):
    '''
    Removes accents from the municipallity name text data
    param: row - A dataframe row
    '''
    #Source - https://pypi.org/project/Unidecode/
    from unidecode import unidecode
    remove_accent =unidecode(row.municipality_name)
    return remove_accent