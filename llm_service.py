# llm_service.py
import os
import requests

API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")
API_VERSION = "2023-03-15-preview"
print()
print("Using endpoint:", ENDPOINT)
print("Using deployment:", DEPLOYMENT_NAME)
def query_llm(prompt, temperature, top_p, top_k):
    url = f"{ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version={API_VERSION}"
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "top_p": top_p,
        # "top_k": top_k,
        "max_tokens": 1000
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]