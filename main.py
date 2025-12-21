from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "192.168.0.15"
PORT = 8080
class NeuralNetHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1> WELCOME TO EVIL INC! </h1></body></html>", "utf-8"))
        
server = HTTPServer((HOST, PORT), NeuralNetHTTPRequestHandler)

print(f"Starting server at http://{HOST}:{PORT}")
server.serve_forever()
server.server_close()
print("Stopping server.")