# Salient Feature System

## Team members:
- Dheepak S
- Nandhakumar G
- Sriniketh J
- Vignesh M

## Inspiration


## What it does


## Tools & Framework:
- 🐍 Python
- ⚱️ Gradio
- 🤗 HuggingFace
- 🔸 Jupyter Notebook

## Libraries:
- 🐼 Pandas
- ␂ NLTK
- 🩵 Scikit-Learn
- ⚱️ Gradio

## 🎯Project Details ():

### Data Preparation
- *Stop-word removal*: This involves the removal of words that don't add much value to the sentence and helps build a better vectorizer to fit into the classifier.
- *Punc-clean*: This involves the refactoring of punctuation marks and more like those that don't add much value if the model is trained over and reduces the training overhead.

### Model building
1. Detect profanity in the sentences.
2. Perform saliency checking on a sentence-by-sentence basis.

**Profanity Detection**: 
- You'll need a profanity detection mechanism to identify and flag profane words or phrases in the sentences. You can use a pre-trained model, a list of profane words, or a combination of techniques to detect profanity.
- 

**Saliency Checking Sentence-wise:**

- *TF-IDF (Term Frequency-Inverse Document Frequency)*: Convert sentences into TF-IDF vectors to capture word importance within sentences. You can treat sentences as "documents."
- *Word Embeddings*: Consider using pre-trained word embeddings (Word2Vec, GloVe, or fastText) to represent sentences as dense vectors. These embeddings capture semantic relationships between words.

## Challenges we ran into
- We were facing issues at the beginning in converting the `saliency` column to `0` or `1`.
- Then we were stuck in the model-building phase. We were building models using Logistic Regression, but that seemed to produce a 

## What we learned
- 
