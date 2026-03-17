import requests

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    # Optional but recommended
    "HTTP-Referer": "http://localhost",  
    "X-OpenRouter-Title": "Image Analyzer App"
}

payload = {
    # ✅ Use a vision-capable model
    "model": "google/gemma-3-4b-it:free",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://live.staticflickr.com/3851/14825276609_098cac593d_b.jpg"
                    }
                }
            ]
        }
    ]
}

try:
    response = requests.post(url, headers=headers, json=payload)

    print("Status Code:", response.status_code)

    # ✅ If successful
    if response.status_code == 200:
        result = response.json()
        print("\n🧠 Model Response:\n")
        print(result["choices"][0]["message"]["content"])
    else:
        print("\n❌ Error Response:\n")
        print(response.text)

except Exception as e:
    print("\n⚠️ Exception occurred:\n", str(e))