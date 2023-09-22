import requests
import time
import json
from profanityfilter import ProfanityFilter

model_name = "Dabid/abusive-tagalog-profanity-detection"
endpoint = f"https://api-inference.huggingface.co/models/Dabid/abusive-tagalog-profanity-detection"

input_text = "like"
payload = {
    "inputs": input_text,
    "options": {
        "max_length": 50,
        "temperature": 1,
    },
}

pf = ProfanityFilter()
# print(pf.is_profane(input_text))


headers = {"Authorization": "Bearer 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"}
response = requests.post(endpoint, json=payload, headers=headers)
if response.status_code == 200:
    result = json.loads(response.text)
    filtered_text = result[0]
    # print(filtered_text)
    # print("Filtered Text:")
    p = filtered_text[0]["label"]
    val = filtered_text[0]["score"]
    if p == "Non-Abusive" and val > 0.75:
        print("Non Profane")
    else:
        print("Profane")
elif "Model is currently loading" in response.text:
    print("Model is still loading. Retrying in a few seconds...")
    time.sleep(20)
else:
    print("API call failed with status code:", response.status_code)
    print(response.text)
