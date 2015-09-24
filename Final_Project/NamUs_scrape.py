# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:17:15 2015

@author: jenniferstark
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from timeit import default_timer as timer
import get_html
import get_namus

'''
TO DO
- maybe use "asserts" to test contents of cell AND/OR keep all data to be assessed as to what to do wiht it later
'''        

#test = get_namus(871)
#testdb = pd.DataFrame(test, index=[0])

namus = []
start = timer()

for case in range(12001, 13001):
    try:
        print(case)
        namus.append(get_namus(case))
        get_html(case)
    except:
        continue
    sleep(2)
    
end = timer()
print(end - start)

# Convert the list of dictionaries to a pandas dataframe
namusdb = pd.DataFrame(namus)



# ...
