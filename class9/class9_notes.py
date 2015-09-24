# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:49:07 2015

@author: jenniferstark
"""

#make ASSERT statements when I know or am expecting certain things;
# eg:
assert(data.nontweets > 1) 

'''
if want to make sure splitting of data to make training and testing samples
that represent the whole, use STRATIFIED split

eg

you have
80 centers
10 forwards
10 guards

and you want the split to contain equal proportions of each of those, and not
a ton of centers in your trianing set, and NO forwards, for example
'''