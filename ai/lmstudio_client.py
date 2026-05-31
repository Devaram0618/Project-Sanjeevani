import requests

class LMStudioClient:

    def generate(self, prompt):

        url = "http://localhost:1234/v1/chat/completions"

        payload = {
            "model": "local-model",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(url, json=payload)

        return response.json()
