from bs4 import BeautifulSoup
from dotenv import load_dotenv, dotenv_values
import requests
import os
import re
import base64

load_dotenv()

# Define regex pattern for plain API keys
API_SYNTAX = r"API\|\d{8}"
# Define regex pattern for Base64 encoded API keys
API_SYNTAX_BASE64 = r"[A-Za-z0-9+/=]{20}"

def test_server():
    
    FILE_FOLDER = os.getenv("FOLDER")
    HOST = os.getenv("HOST") # store host from .env file
    PORT = "0" # default port value
    PORT_TEXT ="port_text.txt" # text file to store the port number. Used for communication between server and response.py

    # Reads the port from the text file and stores it in PORT variable
    with open(PORT_TEXT, "r") as port_storage:
        PORT = port_storage.read().strip()

    if PORT is None:
        print("Server port not found in environment variables. Start the server first.")
        return

    url = f"http://{HOST}:{PORT}/help.html" # constructs the URL using the host and port. Points to help.html page
    print(f"Testing server at: {url}")

    try:
        # Sends a GET request to the server
        response = requests.get(url)
        response.raise_for_status()

    except requests.HTTPError as http_err: 
        print(f"HTTP error occurred: {http_err}")
            
    except Exception as err:
        print(f"Other error occurred: {err}")

    response_text = response.text
    text = str(BeautifulSoup(response_text, "html.parser"))
        
    # Initialize list to store found API keywords
    found_keys = []
        
    # Search for API syntax (defined above) in the text content and extend found_keywords list with matches
    matches = re.findall(API_SYNTAX, text)
    for match in matches:
        found_keys.append(match)

    # Search for Base64 encoded API keys, decode them, and check if they match the API syntax. If they do, add to found_keys list
    base64_matches = re.findall(API_SYNTAX_BASE64, text)
    for base64_match in base64_matches:
        try:
            # Decode the Base64 string using UTF-8 encoding (ASCII failed)
            string_bytes = base64.b64decode(base64_match.encode("utf-8"))
            string_string = string_bytes.decode("utf-8")
                
            if re.match(API_SYNTAX, string_string):
                found_keys.append(string_string.strip())
                    
        except Exception as e:
            print(f"Decoding {base64_match} failed: {e}")
            
    print("Found API keys:", found_keys)
    
    # Store found API keys in api.py
    with open("api.txt", "w") as api_storage:
        api_storage.write("API keys: \n")
        for key in found_keys:
            api_storage.write(f"{key}\n")
    
    print("Keys securely stored in api.py.")
    
    # Creats a clean copy of help.html
    original_help = os.path.join(FILE_FOLDER, "help.html")
    copied_help = os.path.join(FILE_FOLDER, "help_key_removed.html")

    
    with open(original_help, "r") as original_file:
        html = original_file.read()
        
        for key in found_keys:
            html = html.replace(key, "")
        
        # IMPROVE THIS PART!!!
        for key64 in base64_matches:
            try:
                # Decode the Base64 string using UTF-8 encoding (ASCII failed)
                string_bytes = base64.b64decode(key64.encode("utf-8"))
                string_string = string_bytes.decode("utf-8").strip()

                if string_string in found_keys:
                    html = html.replace(f"'key64'", "")
                    html = html.replace(f'"key64"', "")
                    html = html.replace(key64, "")
            except Exception:
                continue
        
        with open(copied_help, "w") as copied_file:
            copied_file.write(html)
    
if __name__ == "__main__":
    test_server()