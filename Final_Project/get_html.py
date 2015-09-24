# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:14:35 2015

@author: jenniferstark
"""
def get_html(case_id):
    case_html = ('case_' + str(case_id) + '.html') 
    with open((case_html), 'wb') as f:
        r = requests.get('https://identifyus.org/en/cases/' + str(case_id) + '/')
        b = BeautifulSoup(r.text)
        for b in r.iter_content(1024):
            f.write(b)
    return case_html