# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:33:48 2015

@author: jenniferstark
"""
'''
1. df -> pandas df object (5, 6)
2. df.continent -> series, (5,)
3. df['continent'] -> series (5,)
4. df[['country', 'continent']] -> df of just those series, (5, 2)
if you pass it a list of strings, it will return a dataframe 
5. df[[Fasle, True, False, True, False]] -> df type selects rows from original dataframe
of shape (2, 6) so 2 rows where there were "True's" and all the columns associated.
It keeps all columns and just filters rows

'''