# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:17:15 2015

@author: jenniferstark
"""

import requests
from bs4 import BeautifulSoup


r = requests.get('https://identifyus.org/en/cases/14215')
b = BeautifulSoup(r.text)
