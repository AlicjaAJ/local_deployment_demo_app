#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
from argparse import Namespace
from dotenv import load_dotenv, dotenv_values
import os
import argparse
import socket

load_dotenv()

#---- Configuration ----#

HOST = os.getenv("HOST") # store host from .env file
PORT_TEXT = "port_text.txt" # text file to store the port number. Used for communication between server and response.py
silent_logging = os.getenv("SILENT_LOGGING", "False") # if set to "1", logging is silent
FRONTEND_FOLDER = os.getenv("FOLDER") # folder to be served

#---- SilentHTTPRequestHandler Class ----#

# SimpleHTTPRequestHandler subclass with overridden log_message method to enable silent logging.
class SilentHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        if silent_logging != "1":
            super().log_message(format, *args)

def main():
    
    # Changes directory to frontend folder, if it is not set yet
    try:
        os.chdir(FRONTEND_FOLDER)
    except Exception as err:
        print(f"Could not change directory to frontend folder: {err}.")
        return
    
    # Creates a socket for the server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Modifying socket options. Allows the socket to reuse the local address.
        # Allows deploy_cron.sh to quickly restart the server without causing as error.
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except:
        print("Failed to open a socket.")
    
    # Argument parser for port. Allows user to enter a port in the format -port XXXX.
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", type = int, help = "Port to run the server on.")
    
    #---- Assigning a port ----#
    
    # Parse argument for port set as first priority,
    # then check .env file, else assign random port
    try:
        args: Namespace = parser.parse_args()
        PORT = 0
        
        if args.port is not None:
            PORT = args.port
        
        else:
            environ_port = int(os.getenv("PORT"))
            if environ_port is not None:
                    PORT = int(environ_port)
                
            else:
                ()
                
    except Exception as err:
        print(f"Fail to set the valid port: {err}.")
    
    # If port is 0 (no port provided by parser or .env), bind a socket to privided host and port
    try: 
        sock.bind((HOST, PORT))
        port = sock.getsockname()[1]
    except Exception as err:
        print(f"Failed to bind a socket to port: {PORT} and host: {HOST}: {err}")
    
    # Saves port to a text file for communication with response.py
    with open(PORT_TEXT, "w") as port_storage:
        port_storage.write(str(PORT))
    
    sock.close()   
    
    print(f"Port set to: {PORT}")

    # Creats a running server on the provided port and host.
    server = HTTPServer((HOST, PORT), SilentHTTPRequestHandler)
    server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    print(f"Serving files from folder: {os.getcwd()}") # print current working directory
    print("Silent logging:", silent_logging) # print silent logging status
    print(f"Starting server at http://{HOST}:{PORT}/help.html") # print server address

    try:
        server.serve_forever()
        
    except KeyboardInterrupt:
        ()
        
    except Exception as err:
        print(f"Error in server run: {err}")
        
    finally:
        # On server stop, reset port in text file to "0"
        with open(PORT_TEXT, "w") as port_storage:
            port_storage.write("0")
            
        server.server_close()
        print(" Stopping server.")
    

if __name__ == "__main__":
    main()