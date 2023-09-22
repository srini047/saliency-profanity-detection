import gradio as gr
from salient import vectr, clf
from profanity import pf
pf.set_censor("@")

def predict(text):
    senti = clf.predict(vectr.transform([text]))
    if(pf.is_profane(text)):
        prof = True
        censored_text = pf.censor(text)
    else:
        prof = False
        censored_text = pf.censor(text)
    
    if (int(senti)):
        text_sent = "Salient"
    else:
        text_sent = "Not salient"

    return {
        "salient": text_sent,
        "profanity": prof,
        "censored_text": censored_text
    }

demo = gr.Interface(fn=predict, inputs="text", outputs="json")
demo.launch(share=True)
