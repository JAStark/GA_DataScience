# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:28:01 2015

@author: jenniferstark
"""

import pandas as pd
from bs4 import BeautifulSoup
from timeit import default_timer as timer
import get_namus_fromFile
import os



namus = []
start = timer()

def namus_fromFile(cases):
    for case in cases:
        try:
            with open(("../../Namus_data/html_files2/" + 'case_' + str(case) + '.html'), 'rU') as f:
                lines = len(f.readlines())
                if lines > 500:
                    with open(("../../Namus_data/html_files2/" + 'case_' + str(case) + '.html'), 'rU') as f:
                        html = f.read()
                        print(case)
                        namus.append(get_namus_fromFile(html))
        except:
            continue
        
end = timer()
print(end - start)

namus_fromFile(range(0,16000))

# Convert the list of dictionaries to a pandas dataframe
namusdb = pd.DataFrame(namus)

namusdb.to_csv('namus_html2.csv')
namusdb.to_pickle('namus_html2.pkl')