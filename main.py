#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
from argparse import Namespace
import os
import argparse
import socket
import test

HOST = "192.168.0.15"
PORT ="0"
PORT_TEXT ="port_text.txt"

def main():
    global PORT
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", type = int, help = "Port to run the server on (if port not provided, a random port will be assigned).")

    try:
        args: Namespace = parser.parse_args()
    except: 
        print("Invalid port or server error.")
        return
    
    if args.port is not None:
        
        PORT = args.port
    
    else:
        
        environ_port = os.getenv("PORT")
        
        if environ_port is not None:
            
                PORT = int(environ_port) # add try?????
            
        else:
            PORT = 0
            
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    PORT = sock.getsockname()[1]
    
    # Saves port to a text file
    with open(PORT_TEXT, "w") as port_storage:
        port_storage.write(str(PORT))
    
    sock.close()   

    print(f"Port set to: {PORT}")

    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

    try:
        print(f"Starting server at http://{HOST}:{PORT}")
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