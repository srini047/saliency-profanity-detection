# Salient Feature System

## Demo video
https://youtu.be/Ttry3E8UA2s

## Deployed App
https://huggingface.co/spaces/srini047/saliency-profanity-detection

## Team members:
- Dheepak S
- Nandhakumar G
- Sriniketh J
- Vignesh M

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

## 🎯Project Details:

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
- Then we were stuck in the model-building phase. We were building models using Logistic Regression, but that seemed to produce a biased output which led us to go over a voting classifier (thanks for the input from the team)
- In the voting classifier, we use logistic regression in combination with SVC (support vector classifier) which seemed to produce a promising output, and decided to finalize the model.
- As always, the deployment proved to be the most time-consuming and tiresome of all. We tried to deploy the Gradio interface with the Huggigface space to reduce the overhead of server requirements. However, there were deployment errors though we used the proper virtual environment and couldn't figure out the turnaround. Hence we decided to move with the localhost server but that can be accessed by anyone.

