#!/usr/bin/env python3
"""Simple test server for DOCSight addon."""

import http.server
import socketserver
import sys
import os

PORT = 8765

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>DOCSight Test Server</h1><p>Working!</p>')

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
        print(f"Test server running on port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped")
            sys.exit(0)
