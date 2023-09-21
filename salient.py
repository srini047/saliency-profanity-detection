"""# MODEL BUILDING"""

import numpy as np # For linear algebra
import pandas as pd # Data processing, CSV file I/O (e.g. pd.read_csv)
# from ydata_profiling import ProfileReport  # For generating data report

data = pd.read_csv('train-cleaned.csv')
data

import nltk  #Natural Language Processing Toolkit
def punc_clean(text):
    import string as st
    a=[w for w in text if w not in st.punctuation]
    return ''.join(a)
data[''] = data['Extracted text'].apply(punc_clean)
#data.head(2)

def remove_stopword(text):
    stopword=nltk.corpus.stopwords.words('english')
    stopword.remove('not')
    a=[w for w in nltk.word_tokenize(text) if w not in stopword]
    return ' '.join(a)
data['Extracted text'] = data['Extracted text'].apply(remove_stopword)

from sklearn.feature_extraction.text import TfidfVectorizer

vectr = TfidfVectorizer(ngram_range=(1,2), min_df=1)
vectr.fit(data['Extracted text'])

vect_X = vectr.transform(data['Extracted text'])

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

clf=model.fit(vect_X,data['saliency'])
# clf.score(vect_X, data['saliency'])*100

# """# PREDICTION"""

# clf.predict(vectr.transform(['''UThat has to be canceled by the 23rd. It had a reminder on my my television uh so I wanted to make sure. Yeah, I wanted to go ahead and cancel that today promo all the free promo channels are. However, you say that.''']))

# clf.predict(vectr.transform(['''uhhh....''']))

# clf.predict(vectr.transform(['''mhm . Let check happening .''']))
