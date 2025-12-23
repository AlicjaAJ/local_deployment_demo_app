from bs4 import BeautifulSoup
import requests
import os

def test_server():
    
    HOST = os.getenv("HOST") # store host from .env file
    PORT = "0" # default port value
    PORT_TEXT ="port_text.txt" # text file to store the port number. Used for communication between server and response.py

    # Reads the port from the text file and stores it in PORT variable
    with open(PORT_TEXT, "r") as port_storage:
        PORT = port_storage.read().strip()

    if PORT is None:
        print("Server port not found in environment variables. Start the server first.")


    url = f"http://{HOST}:{PORT}" # constructs the URL using the host and port

    try:
        # Sends a GET request to the server
        response = requests.get(url)
        response.raise_for_status()
        
        response_text = response.text
        soup = BeautifulSoup(response_text, "html.parser")
        # Prints the prettified HTML content received from the server
        print(soup.prettify())
        
    except requests.HTTPError as http_err: 
        print(f"HTTP error occurred: {http_err}")
            
    except Exception as err:
        print(f"Other error occurred: {err}")
    
if __name__ == "__main__":
    test_server()