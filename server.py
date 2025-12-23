#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
from argparse import Namespace
from dotenv import load_dotenv, dotenv_values
import os
import argparse
import socket

load_dotenv()

host = os.getenv("HOST")
PORT_TEXT = "port_text.txt"
silent_logging = os.getenv("SILENT_LOGGING", "False")

class SilentHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        if silent_logging != "1":
            super().log_message(format, *args)

def main():
    
    try:
        FRONTEND_FOLDER = os.getenv("FOLDER", "/Users/alicjajaskolka/Desktop/Programming/frontend")
        os.chdir(FRONTEND_FOLDER)
    except:
        print("Could not change directory to frontend folder.")
        return
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", type = int, help = "Port to run the server on (if port not provided, a random port will be assigned).")

    try:
        args: Namespace = parser.parse_args()
    except: 
        print("Invalid port or server error.")
        return
    
    port = 0
    
    if args.port is not None:
        
        port = args.port
    
    else:
        
        environ_port = os.getenv("PORT")
        
        if environ_port is not None:
            
                port = int(environ_port) # add try?????
            
        else:
            ()
            
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    port = sock.getsockname()[1]
    
    # Saves port to a text file
    with open(PORT_TEXT, "w") as port_storage:
        port_storage.write(str(port))
    
    sock.close()   

    print(f"Port set to: {port}")

    server = HTTPServer((host, port), SilentHTTPRequestHandler)

    try:
        print(f"Serving files from folder: {os.getcwd()}")
        print("Silent logging:", silent_logging)
        print(type(silent_logging))
        print(f"Starting server at http://{host}:{port}")
        server.serve_forever()
    except KeyboardInterrupt:
        ()
        
    except:
        print("Invalid port or server error.")
    finally:
        
        with open(PORT_TEXT, "w") as port_storage:
            port_storage.write("0")
            
        server.server_close()
        print(" Stopping server.")
    

if __name__ == "__main__":
    main()