import requests
import os

PORT = os.getenv("PORT")

HOST = os.getenv("HOST")

if PORT is None:
    print("PORT environment variable not set.")

if HOST is None:
    print("HOST environment variable not set.")

try:
    
    response = requests.get(f"http://{HOST}:{PORT}")
    response.raise_for_status()
    
except requests.HTTPError as http_err:
    
    print(f"HTTP error occurred: {http_err}")
        
except Exception as err:
    
    print(f"Other error occurred: {err}")
    
else:
    print("Success!")
    
response_text = response.text
print(response_text)