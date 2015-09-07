# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:46:26 2015

@author: jenniferstark
"""


'''Pandas continued'''

import pandas

drinks_cols = ['country', 'beer', 'spirit', 'wine', 'liters', 'continent']
drinks = pd.read_csv('drinks.csv', header=0, names=drinks_cols) #header=0 means header on row 0

#adding column values
drinks['servings'] = drinks.beer + drinks.spirit + drinks.wine #adds things along each row together
drinks['hello'] = 3 #will give a header called 'Hello' and put 3 in that column in each row
drinks.hello #will return the list from that column
drinks['mL'] =  drinks.liters * 1000 # does vectorised math, and broadcasts it

# Removing columns
drinks.drop('mL', axis=1) #axis 0 is rows, axis 1 is the columns
drinks.drop('mL', axis=1, inplace=True) #axis 0 is rows, axis 1 is the columns
drinks.drop(2, inplace=True) #to drop Algeria, axis=0 is the default so dont need it
# now you'll see index number 2 is now gone when you do drinks.head()
#if removing more than one column, need to use a list:
drinks.drop(['column 1', 'column 2'])

#Finding missing numbers
drinks.continent.isnull()  #True if missing
drinks.continent.notnull() # True if NOT missing
drinks[drinks.continent.isnull()]
drinks[drinks.continent.notnull()]

drinks.sum()  # did sums of each column
drinks.sum(axis=1) #will sum along the rows

drinks.isnull().sum() #do EVERY time have a new DF to understand the data

drinks.dropna() # will auto drop rows if they have missing values in ONE column only
drinks.dropna(how='all') # drop if ALL cells in row NA
drinks.continent.fillna(value='NA', inplace=True) # fill missing values with STRING NA

#turn off missing value filter:
drinks = pd.read_csv('drinks.csv', header=0, names=drink_cols, na_filter=False)
# this is to tell it to ignore NAs cos you're gonna deal with them yourself
