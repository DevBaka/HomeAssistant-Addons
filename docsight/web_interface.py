#!/usr/bin/env python3
"""
Simple web interface for DOCSight addon management
"""
import json
import subprocess
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class DOCSightHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        
        if parsed_url.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Read current config
            config = self.read_config()
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>DOCSight Management</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    .container {{ max-width: 800px; margin: 0 auto; }}
                    .card {{ background: #f5f5f5; padding: 20px; margin: 10px 0; border-radius: 8px; }}
                    .btn {{ background: #03a9f4; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; margin: 5px; }}
                    .btn:hover {{ background: #0288d1; }}
                    .status {{ padding: 10px; margin: 10px 0; border-radius: 4px; }}
                    .success {{ background: #4caf50; color: white; }}
                    .info {{ background: #2196f3; color: white; }}
                    .config {{ background: #ff9800; color: white; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🌐 DOCSight Management</h1>
                    
                    <div class="card">
                        <h2>🔗 Quick Access</h2>
                        <a href="http://homeassistant.local:8765" target="_blank">
                            <button class="btn">📊 Open DOCSight Dashboard</button>
                        </a>
                    </div>
                    
                    <div class="card">
                        <h2>⚙️ Current Configuration</h2>
                        <div class="status config">
                            <strong>HA Panel:</strong> {config.get('ha_panel', 'false')}<br>
                            <strong>Check Updates:</strong> {config.get('check_updates', 'false')}<br>
                            <strong>Auto Update:</strong> {config.get('auto_update', 'false')}
                        </div>
                    </div>
                    
                    <div class="card">
                        <h2>🔄 Update Management</h2>
                        <button class="btn" onclick="checkUpdates()">🔍 Check for Updates</button>
                        <button class="btn" onclick="runUpdate()">🚀 Run Update</button>
                        <div id="update-status"></div>
                    </div>
                    
                    <div class="card">
                        <h2>🖥️ Home Assistant Panel</h2>
                        <button class="btn" onclick="installPanel()">📋 Install HA Panel</button>
                        <div id="panel-status"></div>
                    </div>
                    
                    <div class="card">
                        <h2>📊 Version Info</h2>
                        <div id="version-info">Loading...</div>
                    </div>
                </div>
                
                <script>
                    function checkUpdates() {{
                        document.getElementById('update-status').innerHTML = '<div class="status info">Checking for updates...</div>';
                        fetch('/check-updates')
                            .then(response => response.text())
                            .then(data => {{
                                document.getElementById('update-status').innerHTML = '<div class="status info">' + data + '</div>';
                            }});
                    }}
                    
                    function runUpdate() {{
                        if (confirm('This will update DOCSight to the latest version. Continue?')) {{
                            document.getElementById('update-status').innerHTML = '<div class="status info">Updating...</div>';
                            fetch('/run-update')
                                .then(response => response.text())
                                .then(data => {{
                                    document.getElementById('update-status').innerHTML = '<div class="status success">' + data + '</div>';
                                }});
                        }}
                    }}
                    
                    function installPanel() {{
                        document.getElementById('panel-status').innerHTML = '<div class="status info">Installing panel...</div>';
                        fetch('/install-panel')
                            .then(response => response.text())
                            .then(data => {{
                                document.getElementById('panel-status').innerHTML = '<div class="status success">' + data + '</div>';
                            }});
                    }}
                    
                    // Load version info on page load
                    window.onload = function() {{
                        fetch('/version-info')
                            .then(response => response.text())
                            .then(data => {{
                                document.getElementById('version-info').innerHTML = data;
                            }});
                    }}
                </script>
            </body>
            </html>
            """
            
            self.wfile.write(html.encode())
            
        elif parsed_url.path == '/check-updates':
            self.handle_command('/app/check_updates.sh', 'Checking for updates...')
            
        elif parsed_url.path == '/run-update':
            self.handle_command('/app/manual_update.sh', 'Running update...')
            
        elif parsed_url.path == '/install-panel':
            self.handle_command('/app/ha_panel_install.sh', 'Installing panel...')
            
        elif parsed_url.path == '/version-info':
            self.handle_version_info()
            
        else:
            self.send_response(404)
            self.end_headers()
    
    def handle_command(self, command, description):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            output = result.stdout + result.stderr
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(output.encode())
            
        except subprocess.TimeoutExpired:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Command timed out')
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())
    
    def handle_version_info(self):
        try:
            # Get current version
            with open('/app/VERSION', 'r') as f:
                current_version = f.read().strip()
            
            # Get latest version
            import urllib.request
            import json
            
            response = urllib.request.urlopen('https://api.github.com/repos/itsDNNS/docsight/releases/latest')
            data = json.loads(response.read().decode())
            latest_version = data.get('tag_name', 'unknown')
            
            version_info = f"""
            <strong>Current Version:</strong> {current_version}<br>
            <strong>Latest Version:</strong> {latest_version}<br>
            <strong>Status:</strong> {'✅ Up to date' if current_version == latest_version else '🔄 Update available'}
            """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(version_info.encode())
            
        except Exception as e:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error getting version info: {str(e)}'.encode())
    
    def read_config(self):
        try:
            if os.path.exists('/data/options.json'):
                with open('/data/options.json', 'r') as f:
                    return json.load(f)
        except:
            pass
        return {}
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

def run_server():
    server = HTTPServer(('0.0.0.0', 9999), DOCSightHandler)
    print("DOCSight Management Interface running on port 9999")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
