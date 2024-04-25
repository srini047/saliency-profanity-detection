import pickle
import pandas as pd
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

clf = pickle.load(open("saliency_model", 'rb'))
