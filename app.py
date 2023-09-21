import gradio as gr
from salient import vectr, clf

def predict(text):
    senti = clf.predict(vectr.transform([text]))
    if (int(senti)):
        text_sent = "Salient"
    else:
        text_sent = "Not salient"

    return text_sent

demo = gr.Interface(fn=predict, inputs="text", outputs="text")
demo.launch(share=True)
