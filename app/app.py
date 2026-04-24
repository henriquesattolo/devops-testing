from http.server import HTTPServer, BaseHTTPRequestHandler
from calculator import add, subtract, multiply, divide
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy"}).encode())
        else:
            self.send_response(200)
            self.end_headers()
            result = {
                "add": add(10, 5),
                "subtract": subtract(10, 5),
                "multiply": multiply(10, 5),
                "divide": divide(10, 5)
            }
            self.wfile.write(json.dumps(result).encode())

    def log_message(self, format, *args):
        pass

HTTPServer(("", 8080), Handler).serve_forever()
