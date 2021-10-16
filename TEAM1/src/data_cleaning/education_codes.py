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


def add_education_codes(data_2002, data):
    """
    :function: 
    Adds a column to the dataframe for "data" called educational attainment codes, using the
    codes from 2002.
    :params:
    data_2002 - data from electorate in 2002, dataframe
    data - data that needs to have educational attainment codes added
    :returns:
    list 
    """
    
    #Get a unique list of the educational attainment codes.
    unique_codes = data_2002["Educational Attainment Code"].unique()
    
    #Get a unique list of the educational attainment description.
    unique_descriptions = data_2002["Educational Attainment Description"].unique()

    #Creat list of educationl attainment codes, where each entry is a code for a row of the data
    column_codes = []
    for row in range(1, len(data) + 1):
        index = np.where(unique_descriptions == data["Educational Attainment Description"][row])[0][0]
        column_codes += [unique_codes[index]]
    data.insert(7, "Educational Attainment Code", column_codes, True)
    
    return data
    

