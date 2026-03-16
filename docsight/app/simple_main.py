#!/usr/bin/env python3
"""Simple DOCSight test app."""

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>DOCSight is running!</h1><p>Port: 8765</p>"

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8765))
    app.run(host='0.0.0.0', port=port)
