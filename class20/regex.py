# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:49:39 2015

@author: jenniferstark
"""

import re
s = 'my 1st string!!'

match = re.search(r'..t', s)  # r because to keep it raw string, so you dont escape your expressions hahah

if match:
    print(match.group())  #produces no error if fails
    
re.search(r'..t', s).group() #produces an error if fails

with open('homicides.txt', mode='rU') as f:
    data = [row for row in f]

ages = []
for row in data:
    match = re.search(r'(\d+)( years? old)', row)
    if match:
        ages.append(int(match.group(1)))
    else:
        ages.append(0)
 
   
ages_new = []
for a in ages:
    ages_new.append(a.rstrip())  #try splitting in a list comprehension based on spaces