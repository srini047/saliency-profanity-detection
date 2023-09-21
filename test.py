from gradio_client import Client

client = Client("https://1712bd40513e8f2c8a.gradio.live/")
result = client.predict(
				"Howdy!",	# str in 'text' Textbox component
				api_name="/predict"
)
print(result)
