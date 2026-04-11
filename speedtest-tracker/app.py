from flask import Flask, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'status': 'Speedtest Tracker running', 'endpoints': ['/api/speedtest']})

@app.route('/api/speedtest')
def speedtest():
    try:
        result = subprocess.run(['speedtest-cli', '--json'], capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            return jsonify(json.loads(result.stdout))
        return jsonify({'error': 'speedtest failed'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
