#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np


# In[36]:


def read_data_post2006(filename):
    """
    :function: 
    reads in csv file and returns dataframe 
    :params:
    filename - filepath for dataset that is 2010 or after.
    :returns:
    dataframe
    """
    data = pd.read_csv(filename)
    data = pd.DataFrame(data)
    
    #Dropping the row of portuguese names for the columns
    data.drop(index = data.index[0], axis = 0, inplace = True)
    
    return data
    
    


# In[41]:


def read_data_pre2010(filename):
    """
    :function: 
    reads in csv file and returns dataframe 
    :params:
    filename - filepath for dataset that is before 2010
    :returns:
    dataframe
    """
    data = pd.read_csv(filename)
    data = pd.DataFrame(data)
    
    #Dropping the row of portuguese names for the columns
    data.drop(index = data.index[0], axis = 0, inplace = True)
    
    #Convert Attaiment codes to ints not strings
    data["Educational Attainment Code"] = data["Educational Attainment Code"].astype(int)
    
    return data
    


# In[61]:

def clean2018(df):
    """the 2018 data treats the characters with accents incorrectly, and thus doesn't match
    the data of the rest. this function will fix it so the accents are treated correctly."""
    unique_descriptions = df["educational_attainment_description"].unique()
    for row in range(len(df)):
        if df["educational_attainment_description"][row] == 'ENSINO M<c9>DIO COMPLETO':
            df.loc[row, "educational_attainment_description"] = 'ENSINO MEDIO COMPLETO'
            
        
        if df["educational_attainment_description"][row] == 'ENSINO M<c9>DIO INCOMPLETO':
            df.loc[row, "educational_attainment_description"] = 'ENSINO MEDIO INCOMPLETO'
        
        if df["educational_attainment_description"][row] == 'L<ca> E ESCREVE':
            df.loc[row, "educational_attainment_description"] = 'LE E ESCREVE'
        
        if df["educational_attainment_description"][row] == 'N<c3>O INFORMADO':
            df.loc[row, "educational_attainment_description"] = 'NAO INFORMADO'
    
    


def add_education_codes(data_2002, data):
    """
    :function: 
    Adds a column to the dataframe for "data" called educational attainment codes, using the
    codes from 2002.
    :params:
    data_2002 - data from electorate in 2002, dataframe
    data - data that needs to have educational attainment codes added, dataframe
    :returns:
    df 
    """
    
    #Get a unique list of the educational attainment codes.
    unique_codes = data_2002["educational_attainment_code"].unique()
    
    #Get a unique list of the educational attainment description.
    unique_descriptions = data_2002["educational_attainment_description"].unique()

    #Creat list of educationl attainment codes, where each entry is a code for a row of the data
    column_codes = []
    for row in range(len(data)):
        index = np.where(unique_descriptions == data["educational_attainment_description"][row])[0][0]
        column_codes += [unique_codes[index]]
    data.insert(6, "educational_attainment_code", column_codes, True)
    
    return data
    

