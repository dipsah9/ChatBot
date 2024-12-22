from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Fetch the Hugging Face API key
api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key:
    raise ValueError("HF_API_KEY is not set or invalid. Please check your .env file.")

# Debugging: Print the API key (optional, remove in production)
print(f"HF_API_KEY: {api_key}")

# Define the Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

# Function to query the Hugging Face API
def query_huggingface_api(prompt):
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.text}")
        return None

# Test the API with a prompt
prompt = "Translate English to French: Hello, how are you?"
response = query_huggingface_api(prompt)
print(response)
