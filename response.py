from bs4 import BeautifulSoup
from dotenv import load_dotenv, dotenv_values
import requests
import os
import re
import base64

load_dotenv()

# Define regex pattern for API syntax validation
API_SYNTAX = r"API\|\d{8}"

def test_server():
    
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
        
        response_text = response.text
        soup = BeautifulSoup(response_text, "html.parser")
        
        # Prints the prettified HTML content received from the server (test reasons. remove later)
        print(soup.prettify())
        
        # Initialize list to store found API keywords
        found_keys = []
        
        text = soup.get_text()
        
        # Search for API syntax (defined above) in the text content and extend found_keywords list with matches
        matches = re.findall(API_SYNTAX, text)
        for match in matches:
            found_keys.append(match)

        print("Found API keys:", found_keys)

    except requests.HTTPError as http_err: 
        print(f"HTTP error occurred: {http_err}")
            
    except Exception as err:
        print(f"Other error occurred: {err}")
    
if __name__ == "__main__":
    test_server()