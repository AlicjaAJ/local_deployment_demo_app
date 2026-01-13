#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
from argparse import Namespace
from dotenv import load_dotenv, dotenv_values
import os
import argparse
import socket

load_dotenv()

#---- Configuration ----#

host = os.getenv("HOST") # store host from .env file
PORT_TEXT = "port_text.txt" # text file to store the port number. Used for communication between server and response.py
silent_logging = os.getenv("SILENT_LOGGING", "False") # if set to "1", logging is silent

#---- SilentHTTPRequestHandler Class ----#

# SimpleHTTPRequestHandler subclass with overridden log_message method to enable silent logging
class SilentHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        if silent_logging != "1":
            super().log_message(format, *args)

def main():
    
    # Changes directory to frontend folder
    try:
        FRONTEND_FOLDER = os.getenv("FOLDER", "/Users/alicjajaskolka/Desktop/Programming/frontend")
        os.chdir(FRONTEND_FOLDER)
    except:
        print("Could not change directory to frontend folder.")
        return
    
    # Argument parser for port
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", type = int, help = "Port to run the server on (if port not provided, a random port will be assigned).")

    try:
        args: Namespace = parser.parse_args()
    except: 
        print("Invalid port or server error.")
        return
    
    port = 0
    
    # Parse argument for port set as first priority,
    # then check .env file, else assign random port
    if args.port is not None:
        
        port = args.port
    
    else:
        
        environ_port = int(os.getenv("PORT"))
        
        if environ_port is not None:
            
                port = int(environ_port) # add try?????
            
        else:
            ()
    
    # If port is 0 (no port provided by parser or .env), assign random available port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    port = sock.getsockname()[1]
    
    # Saves port to a text file for communication with response.py
    with open(PORT_TEXT, "w") as port_storage:
        port_storage.write(str(port))
    
    sock.close()   

    print(f"Port set to: {port}")

    server = HTTPServer((host, port), SilentHTTPRequestHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        print(f"Serving files from folder: {os.getcwd()}") # print current working directory
        print("Silent logging:", silent_logging) # print silent logging status
        print(f"Starting server at http://{host}:{port}/help.html") # print server address
        server.serve_forever()
        
    except KeyboardInterrupt:
        ()
        
    except:
        print("Invalid port or server error.")
        
    finally:
        # On server stop, reset port in text file to "0"
        with open(PORT_TEXT, "w") as port_storage:
            port_storage.write("0")
            
        server.server_close()
        print(" Stopping server.")
    

if __name__ == "__main__":
    main()