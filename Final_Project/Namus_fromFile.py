# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:28:01 2015

@author: jenniferstark
"""

import pandas as pd
from bs4 import BeautifulSoup
from timeit import default_timer as timer
import get_namus


namus = []
start = timer()

for case in range(0, 4396):
    try:
        with open(('case_' + str(case) + '.html'), 'rU') as f:
            html = f.read()
            print(case)
            namus.append(get_namus_fromFile(html))
    except:
        continue    
        
end = timer()
print(end - start)


# Convert the list of dictionaries to a pandas dataframe
namusdb = pd.DataFrame(namus)