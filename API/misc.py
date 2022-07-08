import requests
import urllib.parse

def summarize_passage(text):
    api_key = "97fd8472-2d93-407a-8412-8687b7d5ab83"
    url = "https://api.oneai.com/api/v0/pipeline"
    
    headers = {
    "api-key": api_key, 
    "content-type": "application/json"
    }
    payload = {
    "input": text,
    "input_type": "article",
    "steps": [
            {
            "skill": "summarize",
            "params": {
                "max_length": 100,
                        "min_length": 5,
                        "auto_length": True,
                        "find_origins": True
            }
            }
        ]
    }
    r = requests.post(url, json=payload, headers=headers)
    data = r.json()
    return data

def detect_truth(text):
    # text = urllib.parse.quote_plus(text)
    text = f'text={urllib.parse.quote_plus(text)}'
    url = "https://dawg-fake-news-detector.p.rapidapi.com/predict"

    payload = text
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "eb1ce18d20msh3920e481175ed8ap104483jsn263e1650f87f",
        "X-RapidAPI-Host": "dawg-fake-news-detector.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    return response.text