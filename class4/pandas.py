# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:42:34 2015

@author: jenniferstark
"""

import pandas as pd


pd.read_table('u.user') #this could be URL instead if needed

users = pd.read_table('u.user', sep='|', index_col='user_id') # need to alter tab-default seperator


'''
Also changed Index column to be User_id to be the index column which does not get
included in number of columns

method() = something you DO, 
attribute = something you are or that you have
users.index = index is sometimes called labels
users.dtype = data type. Strings here are instead Objects here

users['gender'] = select specific columns
pandas makes column names into attributes -> users.gender 

users.describe() = summary of each column like R's summary() 

users.gender.describe = can string things together (df.attribute.method)

# FILTERING AND SORTING

users.age <20   #broadcast the operating across all elements of the series, returning Trues and Falses
'''
young_bool = users.age < 20
users[young_bool] # will select out the True rows from the original df
users[users.age < 20]  #is the same as the 2 lines above
users[users.age < 20].occupation
users[users.age < 20].occupation.value_counts()

# Using multiple conditions

users[(users.age < 20) & (users.gender=='M')]  # Ampersand for AND conditions, not 'and'
users[(users.age < 20) | (users.age > 60)]  # Pipe for OR condition

# SORTING
users.age.order   #to sort Series (Columns). Only returns the series
users.sort('age') # to sort a df, and tell it the column name to sort by, returns the whole DF
