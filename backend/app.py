from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "project": "Project Sanjeevani",
        "status": "Running"
    }

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    description = data.get("description", "")

    prompt = f"""
You are an emergency response assistant.

Analyze the accident and provide:

1. Severity Level
2. Immediate Actions
3. Emergency Services Required
4. Risk To Life

Accident:
{description}
"""

    payload = {
        "model": "qwen2.5-3b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3
    }

    response = requests.post(
        "http://127.0.0.1:1234/v1/chat/completions",
        json=payload
    )

    result = response.json()

    return jsonify({
        "analysis": result["choices"][0]["message"]["content"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
