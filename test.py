import pandas as pd
from gradio_client import Client

# data = pd.read_csv('./train-cleaned.csv')
data = ''

salient = []
non_salient = []
profane = []
non_profane = []

for i in data['text']:
	client = Client("https://1ffd44ea7559e85f4c.gradio.live")
	result = client.predict(
					i,	# str in 'text' Textbox component
					api_name="/predict"
	)
	
	if(result['text']['salient'] == "Salient"):
		salient.append(i)
	else:
		non_salient.append(i)
	if(result['text']['profanity'] == 'true'):
		profane.append(i)
	else:
		non_profane.append(i)
