import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


root_dir = './data/'
train_df = pd.read_csv(os.path.join(root_dir,'train.csv'), sep='\t')
x_train, y_train = train_df['Phrase'], train_df['Sentiment']

test_df = pd.read_csv(os.path.join(root_dir, 'test.csv'), sep='\t')
label = pd.read_csv(os.path.join(root_dir,'sent_ana_test.csv'))
x_test, y_test = test_df['Phrase'], label['Sentiment']

vec = CountVectorizer(stop_words='english')
x_train_vec = vec.fit_transform(x_train).toarray()
x_test_vec = vec.transform(x_test).toarray()

gnb = MultinomialNB()
y_pred = gnb.fit(x_train_vec, y_train).predict(x_test_vec)

print("Number of mislabeled points out of a total %d points : %d" % (x_test.shape[0], (y_test != y_pred).sum()))
print('Accuracy: ', gnb.score(x_test_vec, y_test))
