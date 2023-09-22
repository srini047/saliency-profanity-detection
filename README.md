# Salient Feature System

## Tools & Framework:
- 🐍Python
- ⚱️Gradio
- 🤗HuggingFace

🎯Project Goals (achieved through ML Models):

1. Detect profanity in the sentences.
2. Perform saliency checking on a sentence-by-sentence basis.

**Profanity Detection**: You'll need a profanity detection mechanism to identify and flag profane words or phrases in the sentences. You can use a pre-trained model, a list of profane words, or a combination of techniques to detect profanity.

**Saliency Checking Sentence-wise:**
- *TF-IDF (Term Frequency-Inverse Document Frequency)*: Convert sentences into TF-IDF vectors to capture word importance within sentences. You can treat sentences as "documents."
- *Word Embeddings*: Consider using pre-trained word embeddings (Word2Vec, GloVe, or fastText) to represent sentences as dense vectors. These embeddings capture semantic relationships between words.
- 
