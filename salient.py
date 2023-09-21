"""# MODEL BUILDING"""
# Commented out IPython magic to ensure Python compatibility.
import numpy as np # For linear algebra
import pandas as pd # Data processing, CSV file I/O (e.g. pd.read_csv)
# import matplotlib.pyplot as plt  # For Visualisation
# %matplotlib inline
# import seaborn as sns  # For Visualisation
# from bs4 import BeautifulSoup  # For Text Parsing
# from ydata_profiling import ProfileReport  # For generating data report

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

def remove_stopword(text):
    stopword=nltk.corpus.stopwords.words('english')
    stopword.remove('not')
    a=[w for w in nltk.word_tokenize(text) if w not in stopword]
    return ' '.join(a)
#data['Extracted text'] = data['Extracted text'].apply(remove_stopword)

data = pd.read_csv('train-cleaned.csv')
data

import nltk  #Natural Language Processing Toolkit
def punc_clean(text):
    import string as st
    a=[w for w in text if w not in st.punctuation]
    return ''.join(a)
data[''] = data['Extracted text'].apply(punc_clean)
#data.head(2)

from sklearn.feature_extraction.text import TfidfVectorizer

vectr = TfidfVectorizer(ngram_range=(1,2),min_df=1)
vectr.fit(data['Extracted text'])

vect_X = vectr.transform(data['Extracted text'])

#from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier

svm_classifier = SVC(kernel='linear', probability=True)
logistic_classifier = LogisticRegression()


model = VotingClassifier(estimators=[
    ('svm', svm_classifier),
    ('logistic', logistic_classifier)
], voting='hard')


clf=model.fit(vect_X,data['saliency'])
# clf.score(vect_X, data['saliency'])*100

# """# PREDICTION"""

# clf.predict(vectr.transform(['''thank you ''']))

# clf.predict(vectr.transform(['''Theres no trailers or nothing on the other side of me and its been facing away from my trailer straight''']))

# clf.predict(vectr.transform([''' I dont think that should really matter Um''']))

