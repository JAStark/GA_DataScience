# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:25:21 2015

@author: jenniferstark
"""
import pandas as pd

# read ufo.csv into a DataFrame called 'ufo'
ufo = pd.read_csv('ufo.csv')

# check the shape of the DataFrame
ufo.shape  # = (80543, 5)

# calculate the most frequent value for each of the columns (in a single command)
ufo.dropna().describe()
'''
           City Colors Reported Shape Reported  State            Time
count     15510           15510          15510  15510           15510
unique     5436              31             25     50           14080
top     Seattle          ORANGE          LIGHT     CA  7/4/2014 22:00
freq        122            4888           3727   2101              19
'''

# what are the four most frequent colors reported?
ufo['Colors Reported'].value_counts().head(4)
# for reports in VA, what's the most frequent city?
ufo[ufo.State =='VA'].describe()
'''
                  City Colors Reported Shape Reported State              Time
count             1581             327           1406  1582              1582
unique             397              17             21     1              1551
top     Virginia Beach             RED          LIGHT    VA  11/17/2012 18:30
freq               110              88            283  1582                 3
'''

# show only the UFO reports from Arlington, VA
ufo[ufo.City == 'Arlington']
ufo[(ufo.State == "VA") & (ufo.City == 'Arlington')] #because Arlington also in Tx

# count the number of missing values in each column
ufo.isnull().sum()
'''
City                  47
Colors Reported    63509
Shape Reported      8402
State                  0
Time                   0
dtype: int64
'''

# show only the UFO reports in which the City is missing
ufo[ufo.City.isnull()]

# how many rows remain if you drop all rows with any missing values?
ufo.dropna().shape[0]

# replace any spaces in the column names with an underscore
ufo.rename(columns={'Colors Reported':'colors', 'Shape Reported':'shape'}, inplace=True)

# BONUS: redo the task above, writing generic code to replace spaces with underscores
# In other words, your code should not reference the specific column names
ufo.columns = [column.replace(' ', '_') for column in ufo.columns]
# or
ufo.columns = ufo.columns.str.replace(' ', '_')

# BONUS: create a new column called 'Location' that includes both City and State
# For example, the 'Location' for the first row would be 'Ithaca, NY'
ufo['location'] = ufo.City + ', ' + ufo.State


'''
EXERCISE FOUR
'''

# for each occupation in 'users', count the number of occurrences
users = pd.read_csv('u.user', sep='|', index_col='user_id')
users.occupation.value_counts()

# for each occupation, calculate the mean age
users.groupby('occupation').age.mean()

# BONUS: for each occupation, calculate the minimum and maximum ages
users.groupby('occupation').age.agg(['min', 'max'])

# BONUS: for each combination of occupation and gender, calculate the mean age
users.groupby(['occupation', 'gender']).age.mean()
