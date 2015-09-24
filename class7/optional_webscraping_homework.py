# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:00:17 2015

@author: jenniferstark
"""

'''
OPTIONAL WEB SCRAPING HOMEWORK
First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)

For example, get_movie_info('tt0111161') should return:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}
 
Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.

Finally, convert that list into a DataFrame.
'''
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    # Create keys for the movie dictionary
    keys = ['Title', 'Star Rating', 'Description', 'Content Rating', 'Duration']
    
    #Create an empty list to put each movie dictionary
    all_movies = []
    
    #create a function to collect specific information for each movie
    def get_movie_info(imdb_id):
        r = requests.get('http://www.imdb.com/title/'+imdb_id)
        b = BeautifulSoup(r.text)
        title = b.find(name='span', attrs={'class':'itemprop', 'itemprop':'name'}).text
        star_rating = float(b.find(name='span', attrs={'itemprop':'ratingValue'}).text)
        description = b.find(name='p', attrs={'itemprop':'description'}).text.strip() #gets rid of \n character
        content_rating = b.find(name='meta', attrs={'itemprop':'contentRating'})['content']
        duration = int(b.find(name='time', attrs={'itemprop':'duration'})['datetime'][2:-1])
        return title, star_rating, description, content_rating, duration
    
    #open the text file containing the movie ids
    with open('imdb_ids.txt') as movie_ids:
        # loop through the movie id list
        for m in movie_ids:
            print(m)
            # put the output of get_movie_info for each movie into "values"
            values = get_movie_info(m)
            # create a dictionary from the "values" for each movie and the "keys" 
            movie_dict = dict(zip(keys, values))
            # append each movie dictionary to a list
            all_movies.append(movie_dict)
            
    # Convert the list of dictionaries to a pandas dataframe
    moviedb = pd.DataFrame(all_movies)


'''
Rachael's cleaner version
'''
# define a function that accepts an IMDb ID and returns a dictionary of movie information
def get_movie_info(imdb_id):
    r = requests.get('http://www.imdb.com/title/' + imdb_id + '/')
    b = BeautifulSoup(r.text)
    info = {}
    info['title'] = b.find(name='span', attrs={'class':'itemprop', 'itemprop':'name'}).text
    info['star_rating'] = float(b.find(name='span', attrs={'itemprop':'ratingValue'}).text)
    info['description'] = b.find(name='p', attrs={'itemprop':'description'}).text.strip()
    info['content_rating'] = b.find(name='meta', attrs={'itemprop':'contentRating'})['content']
    info['duration'] = int(b.find(name='time', attrs={'itemprop':'duration'}).text.strip()[:-4])
    return info
    
 # open the file of IDs (one ID per row), and store the IDs in a list
imdb_ids = []
with open('imdb_ids.txt', 'rU') as f:
    imdb_ids = [row.strip() for row in f]

# get the information for each movie, and store the results in a list, space queries w/ sleep
from time import sleep
movies = []
for imdb_id in imdb_ids:
    movies.append(get_movie_info(imdb_id))
    sleep(1)

import pandas as pd
pd.DataFrame(movies, index=imdb_ids)
