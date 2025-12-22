from bs4 import BeautifulSoup
import requests
import os

def test_server():
    HOST = "192.168.0.15"
    PORT ="0"
    PORT_TEXT ="port_text.txt"

    # Reads the port from the text file
    with open(PORT_TEXT, "r") as port_storage:
        PORT = port_storage.read().strip()

    if PORT is None:
        print("Server port not found in environment variables. Start the server first.")


    url = f"http://{HOST}:{PORT}"

    try:
        
        response = requests.get(url)
        response.raise_for_status()
        
        response_text = response.text
        soup = BeautifulSoup(response_text, "html.parser")
        print(url)
        print(soup.prettify())
        
    except requests.HTTPError as http_err:
        
        print(f"HTTP error occurred: {http_err}")
            
    except Exception as err:
        
        print(f"Other error occurred: {err}")
    
if __name__ == "__main__":
    test_server()