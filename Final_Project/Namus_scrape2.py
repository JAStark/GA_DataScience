# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:25:40 2015

@author: jenniferstark
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from timeit import default_timer as timer
import get_html
import get_namus
import os

'''
TO DO
- maybe use "asserts" to test contents of cell AND/OR keep all data to be assessed as to what to do wiht it later
'''        

#test = get_namus(871)
#testdb = pd.DataFrame(test, index=[0])

case_ranges = range(12000, 16000)
start = timer()

def namus_scrape(cases):
    for case in cases:
        case_html = ('case_' + str(case) + '.html') 
        if os.path.isfile("./html_files/" + case_html) == False:
            try:
                print(case)
                get_html(case)
            except:
                continue
        sleep(2)
    
end = timer()
print(end - start)

namus_scrape(case_ranges)
# Convert the list of dictionaries to a pandas dataframe
namusdb = pd.DataFrame(namus)



# ...
