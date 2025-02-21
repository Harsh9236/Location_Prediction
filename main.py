import requests
import base64
import json
from io import BytesIO
from PIL import Image

OPENROUTER_API_KEY = "API key here"
API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "google/gemini-2.0-flash-thinking-exp:free"

IMAGE_FILE_PATH = "./test_image.jpg"
TEXT_PROMPT = "Can you guess the country of the image? Please enclose your guess within less than and greater than signs. For example: <Your Guess>."
OUTPUT_FILE_PATH = "model_response.txt"

def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            base64_encoded_image = base64.b64encode(image_data).decode('utf-8')
            return base64_encoded_image
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

# --- Prepare the image ---
base64_image = encode_image_to_base64(IMAGE_FILE_PATH)
if base64_image is None:
    exit()

# --- Construct the request body ---
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

data = {
    "model": MODEL_NAME,
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": TEXT_PROMPT},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "auto"  # Or "low" or "high" depending on model and needs
                    }
                }
            ]
        }
    ]
}

try:
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    response_json = response.json()

    if 'choices' in response_json and response_json['choices']:
        generated_text = response_json['choices'][0]['message']['content']

        try:
            with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as outfile:
                outfile.write(generated_text)

        except Exception as e:
            print(f"Error saving output to file: {e}")

    else:
        print("No response content received.")

except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
    if response is not None:
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
except json.JSONDecodeError:
    print("Failed to decode JSON response from API.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
