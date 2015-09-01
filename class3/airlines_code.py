# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:13:51 2015

@author: jenniferstark
"""

f = open ('airlines.csv', mode='rU')  #read universal mode 
file_string = f.read()
f.close()  

#better practice to use "with"
with open('airlines.csv', mode='rU') as f:
    file_string = f.read()
    
    
with open('airlines.csv', mode='rU') as f:
    file_list = []
    for row in f:
        file_list.append(row)  #when you iterate through a file you get rows
        
#list comprehension style
with open('airlines.csv', mode='rU') as f:
    file_list = [row for row in f]
    
# Splitting strings
"Hello DAT students".split('e') # splitting before every 'e' and discards the thing it splits on
"Hello DAT students".split() # splitting before every SPACE and discards the SPACE it splits on

#so now we're gonna split the file_list at the commas, and then we'll have a list of lists
with open('airlines.csv', mode='rU') as f:
    file_list = [row.split(',') for row in f]
    
#we want to get rid of the \n end of line bits
import csv
with open('airlines.csv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f)] #plit on commas for us, and take care of new lines
    
#now we also want to separate out the header row
header = file_nested_list[0]
data = file_nested_list[1:]

'''
Create list containing average number of indidents per year for each airline
'''
incidents = []
for row in data:
    incidents.append(round((int(row[2])) + (int(row[5]))/30),2)
print(incidents)

##in list comprehension style with rounding :D
incidents = [round((int(row[2]) + int(row[5])) / float(30), 2) for row in data]
'''
Create a list of airline names without stars
'''
airlines = []
for row in data:
    airlines.append(str(row[0]).replace('*', ''))
print(airlines)


'''
Create a list that contains 1 if there's a stark and 0 ir not.
'''
stars = []
for row in data:
    if str(row[0]).endswith('*'):
        stars.append(int(1))
    else:
        stars.append(int(0))
print(stars)

#Put the 2 things together
airlines = []
starred = []

for row in data:
    if row[0][-1] == '*':
        starred.append(1)
        airlines.append(row[0][:-1])
    else:
        starred.append(0)
        airlines.append(row[0])


'''
BONUS: Create a dictionary in which the key is the airline name (without the star) adn the value 
is the average number of incidents.
'''
air_dict = dict(zip(airlines, incidents))
print(air_dict)


'''
tips
'''
my_list = [1,2,1]
set(my_list) # looks for unique things
len(set(my_list)) # retuns num of unique items

my_string.count('e') #counts elements in strings





