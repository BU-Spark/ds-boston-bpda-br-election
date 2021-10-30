
def remove_accents(row):
    '''
    Removes accents from the municipallity name text data
    :param row - A dataframe row
    :return The name with the accent removed
    '''
    #Source - https://pypi.org/project/Unidecode/
    from unidecode import unidecode
    remove_accent =unidecode(row.municipality_name)
    return remove_accent

def remove_accents_education(row):
    from unidecode import unidecode
    remove_accent =unidecode(row.educational_attainment_description)
    return remove_accent
    