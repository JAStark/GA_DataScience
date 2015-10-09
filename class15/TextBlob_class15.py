# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:10:51 2015

@author: jenniferstark
"""

from textblob import TextBlob, Word
from nltk.stem.snowball import SnowballStemmer
%matplotlib inline

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/yelp.csv'
yelp = pd.read_csv(url)

yelp_best_worst = yelp[(yelp.stars==5) | (yelp.stars==1)]


review = TextBlob(yelp_best_worst.text[0])
review.words
review.lower()
stemmer = SnowballStemmer('english')
print ([stemmer.stem(word) for word in review.words])
print ([word.lemmatize() for word in review.words])
print ([word.lemmatize(pos='v') for word in review.words])

# define a function that accepts text and returns a list of lemmas
def split_into_lemmas(text):
    text = unicode(text, 'utf-8').lower()
    words = TextBlob(text).words
    return [word.lemmatize() for word in words]
    
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def tokenize_test(vect):
    X_train_dtm = vect.fit_transform(X_train)
    print ('Features: ', X_train_dtm.shape[1])
    X_test_dtm = vect.transform(X_test)
    nb = MultinomialNB()
    nb.fit(X_train_dtm, y_train)
    y_pred_class = nb.predict(X_test_dtm)
    print ('Accuracy: ', metrics.accuracy_score(y_test, y_pred_class))
# use split_into_lemmas as the feature extraction function
vect = CountVectorizer(analyzer=split_into_lemmas)
tokenize_test(vect)



'''
TO DO
Make Kaggle account
visit kaggle.com/join/dat8ga
download sample submission
submit it (requires sms verification)
'''
