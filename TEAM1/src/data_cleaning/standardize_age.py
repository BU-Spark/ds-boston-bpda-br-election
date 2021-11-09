

def standardize_age_desc(age:str):
    import numpy as np
    '''
    Standardizes post 2010 (2014 and 2018) age descriptions to match 
    age descriptions in the 2010 dataset (prior to 2010, age codes were
    not provided)
    :param age - A String Description of the age 
    :return A string Age description in 2010 format
    '''
    try:
        age_array = age.strip().split()
        begin_age = int(age_array[0])
    except:
        return np.nan


    #Ages < 18 are just listed as X ANOS
    if begin_age < 18:
        age.upper()
        return age
    #Bucket ages between 18 and 20
    elif begin_age < 21:
        return "18 A 20 ANOS"
    #Bucket ages between 21 and 25
    elif begin_age < 25:
        return "21 A 24 ANOS"
    #Bucket ages between 25 and 34
    elif begin_age < 35:
        return "25 A 34 ANOS"
    #Bucket ages between 35 and 44
    elif begin_age < 45:
        return "35 A 44 ANOS"
    #Bucket ages between 45 and 60
    elif begin_age < 60:
        return "45 A 59 ANOS"
    #Bucket ages between 60 and 69
    elif begin_age < 70:
        return "60 A 69 ANOS"
    #Bucket ages between 70 and 79
    elif begin_age < 79:
        return "70 A 79 ANOS"
    #Otherwise bucket as over 79
    else:
        return "SUPERIOR A 79 ANOS"



    