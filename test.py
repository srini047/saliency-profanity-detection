import pandas as pd
from gradio_client import Client

# data = pd.read_csv('./train-cleaned.csv')
data = ''

salient = []
non_salient = []
profane = []
non_profane = []

for i in data['text']:

	client = Client("https://d59be99b02bf0eb45e.gradio.live/")
	result = client.predict(
					i,	# str in 'text' Textbox component
					api_name="/predict"
	)

