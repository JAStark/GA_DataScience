# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:12:29 2015

@author: jenniferstark
"""

import pandas as pd
train = pd.read_csv('../../kaggle/train.csv', index_col=0)

# EXPLORATION
train.head()

train.OpenStatus.value_counts()

train.OwnerUserId.value_counts()
train[train.OwnerUserId == 466534].describe()
train[train.OwnerUserId == 466534].head(10)

train.groupby('OwnerUserId').OpenStatus.agg(['mean', 'count']).sort('count')

train[train.OwnerUserId == 185593].head(10)

train.groupby('OpenStatus').ReputationAtPostCreation.describe().unstack()

train[train.ReputationAtPostCreation < 1000].ReputationAtPostCreation.plot(kind='hist')
train[train.ReputationAtPostCreation < 1000].hist(column='ReputationAtPostCreation', by='OpenStatus')
train[train.ReputationAtPostCreation < 1000].boxplot(column='ReputationAtPostCreation', by='OpenStatus')

train.rename(columns={'OwnerUndeletedAnswerCountAtPostTime': 'Answers'}, inplace=True)

train.groupby('OpenStatus').Answers.describe().unstack()

train['TitleLength'] = train.Title.apply(len)
train.groupby('OpenStatus').TitleLength.describe().unstack()

def make_features(filename):
    df = pd.read_csv(filename, index_col=0)
    df.rename(columns={'OwnerUndeletedAnswerCountAtPostTime': 'Answers'}, inplace=True)
    df['TitleLength'] = df.Title.apply(len)
    return df
    
train = make_features('../../kaggle/train.csv')
test = make_features('../../kaggle/test.csv')

feature_cols = ['ReputationAtPostCreation', 'Answers', 'TitleLength']
X = train[feature_cols]
y = train.OpenStatus

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)

logreg.coef_

y_pred_class = logreg.predict(X_test)
y_pred_prob = logreg.predict_proba(X_test)[:,1]

from sklearn import metrics
metrics.accuracy_score(y_test, y_pred_class)
metrics.confusion_matrix(y_test, y_pred_class)
metrics.roc_auc_score(y_test, y_pred_prob)
metrics.log_loss(y_test, y_pred_prob)

logreg.fit(X,y)
X_oos = test[feature_cols]   #oos is OUT OF SAMPLE
oos_pred_prob = logreg.predict_proba(X_oos)[:,1]

test.index
oos_pred_prob

sub = pd.DataFrame({'id': test.index, 'OpenStatus': oos_pred_prob}).set_index('id')
sub.to_csv('sub1.csv')

train.isnull().sum()
train['NumTags'] = train.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)
train.groupby('OpenStatus').NumTags.mean()
train.groupby('NumTags').OpenStatus.mean()

train['OwnerCreationDate'] = pd.to_datetime(train.OwnerCreationDate)
train['PostCreationDate'] = pd.to_datetime(train.PostCreationDate)
train['OwnerAge'] = (train.PostCreationDate - train.OwnerCreationDate).dt.days

train.boxplot(column = "OwnerAge", by="OpenStatus")

import numpy as np
train['OwnerAge'] = np.where(train.OwnerAge < 0, 0, train.OwnerAge)
train.boxplot(column = "OwnerAge", by="OpenStatus")

# update the function
def make_features(filename):
    df = pd.read_csv(filename, index_col=0, parse_dates=['OwnerCreationDate', 'PostCreationDate'])
    df.rename(columns={'OwnerUndeletedAnswerCountAtPostTime':'Answers'}, inplace=True)
    df['TitleLength'] = df.Title.apply(len)
    df['NumTags'] = df.loc[:, 'Tag1':'Tag5'].notnull().sum(axis=1)
    df['OwnerAge'] = (df.PostCreationDate - df.OwnerCreationDate).dt.days
    df['OwnerAge'] = np.where(df.OwnerAge < 0, 0, df.OwnerAge)
    return df

# apply function to both training and testing files
train = make_features('../../kaggle/train.csv')
test = make_features('../../kaggle/test.csv')

# train the model on ALL data
feature_cols = ['ReputationAtPostCreation', 'Answers', 'TitleLength', 'NumTags', 'OwnerAge']
X = train[feature_cols]
logreg.fit(X, y)

# predict class probabilities for the actual testing data
X_oos = test[feature_cols]
oos_pred_prob = logreg.predict_proba(X_oos)[:, 1]

# create submission file
sub = pd.DataFrame({'id':test.index, 'OpenStatus':oos_pred_prob}).set_index('id')
sub.to_csv('sub2.csv')



'''
Build a document-term matrix from Title using CountVectorizer
'''

# build document-term matrix for the training data
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(stop_words='english')
dtm = vect.fit_transform(train.Title)

# define X and y
X = dtm
y = train.OpenStatus

# build document-term matrix for the actual testing data and make predictions
oos_dtm = vect.transform(test.Title)
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X, y)
oos_pred_prob = nb.predict_proba(oos_dtm)[:, 1]
sub = pd.DataFrame({'id':test.index, 'OpenStatus':oos_pred_prob}).set_index('id')
sub.to_csv('sub3.csv')  # 0.544
'''
We used the length of the Title as a feature. How about the length of BodyMarkdown?
We created a document term matrix for Title. How about doing the same for BodyMarkdown?
Can you think of any custom features for Title? Like, we theorized that all 
lowercase titles might be indicative of bad questions. Can you create that as a feature?
What about using sentiment of the Title or BodyMarkdown as a feature?





