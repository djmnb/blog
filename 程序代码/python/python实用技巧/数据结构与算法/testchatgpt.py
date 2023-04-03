import requests
import os
import json
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"
api_key = "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"
response = requests.post(
    'https://api.openai.com/v1/completions',
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    },
    json = {
        'model': 'text-davinci-003',
        'prompt': '如何变帅',
        'temperature': 0.4,
        'max_tokens': 300
    }
)
print(response.status_code)
info = json.loads(response.text)
print(info["choices"][0]["text"])