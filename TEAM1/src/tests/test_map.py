#Simple test file to ensure that the mapping function works (and we are not missing entries)
#from __future__ import absolute_import
import sys
import os
import pandas as pd

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'data_cleaning')
sys.path.append( mymodule_dir )
import country_match
from country_match import country_code_map

def test_2010():

    #Read CSV
    df = pd.read_csv('../../data/perfil_eleitorado_2010.csv')

    #Replace row names with underscores for easy access
    new_column_names = [x.lower().replace(' ','_') for x in df.columns]
    df.columns = new_column_names

    #missing entries
    missing = set()

    #Iterate through rows and try to update codes/name
    #If there is no entry in our map, add to missing set
    for i in df.index:

        #test code and name mapping
        code = df.at[i, 'municipality_code']
        try:
            new_code, name = country_code_map[code]
            df.at[i, 'municipality_code'] = new_code
            df.at[i, 'municipality_name'] = name
        except:
            missing.add((df.at[i, 'municipality_code'], df.at[i, 'municipality_name']))

    #Print missing elements from set
    print("Total Missing 2010: ", len(missing))
    for i, el in enumerate(missing):
        print("Miss {}: {}".format(i, el))

def test_2014():
    df = pd.read_csv('../../data/perfil_eleitorado_2014.csv', skiprows=[1]) #remove extraneous first row (Portuguese col names)

    #Replace row names with underscores for easy access
    new_column_names = [x.lower().replace(' ','_') for x in df.columns]
    df.columns = new_column_names

   #missing entries
    missing = set()

    #Iterate through rows and try to update codes/name
    #If there is no entry in our map, add to missing set
    for i in df.index:

        #test code and name mapping
        code = df.at[i, 'municipality_code']
        try:
            new_code, name = country_code_map[code]
            df.at[i, 'municipality_code'] = new_code
            df.at[i, 'municipality_name'] = name
        except:
            missing.add((df.at[i, 'municipality_code'], df.at[i, 'municipality_name']))

    #Print missing elements from set
    print("Total Missing 2014: ", len(missing))
    for i, el in enumerate(missing):
        print("Miss {}: {}".format(i, el))

def test_2018():
    df = pd.read_csv('../../data/perfil_eleitorado_2018.csv', skiprows=[1]) #remove extraneous first row (Portuguese col names)

    #Replace row names with underscores for easy access
    new_column_names = [x.lower().replace(' ','_') for x in df.columns]
    df.columns = new_column_names
    
    #missing entries
    missing = set()

    #Iterate through rows and try to update codes/name
    #If there is no entry in our map, add to missing set
    for i in df.index:

        #test code and name mapping
        code = df.at[i, 'municipality_code']
        try:
            new_code, name = country_code_map[code]
            df.at[i, 'municipality_code'] = new_code
            df.at[i, 'municipality_name'] = name
        except:
            missing.add((df.at[i, 'municipality_code'], df.at[i, 'municipality_name']))

    #Print missing elements from set
    print("Total Missing 2018: ", len(missing))
    for i, el in enumerate(missing):
        print("Miss {}: {}".format(i, el))

    # print(df.head())


if __name__ == '__main__':
    test_2010()
    test_2014()
    test_2018()