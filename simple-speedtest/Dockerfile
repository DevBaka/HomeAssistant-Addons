FROM arm64v8/debian:bookworm-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip curl speedtest-cli && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install flask

RUN echo "from flask import Flask, jsonify" > app.py && \
    echo "import subprocess, json" >> app.py && \
    echo "app = Flask(__name__)" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/')" >> app.py && \
    echo "def index():" >> app.py && \
    echo "    return jsonify({'status': 'running', 'test': '/api/speedtest'})" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/api/speedtest')" >> app.py && \
    echo "def speedtest():" >> app.py && \
    echo "    try:" >> app.py && \
    echo "        result = subprocess.run(['speedtest-cli', '--json'], capture_output=True, text=True, timeout=120)" >> app.py && \
    echo "        return jsonify(json.loads(result.stdout)) if result.returncode == 0 else jsonify({'error': 'test failed'})" >> app.py && \
    echo "    except Exception as e:" >> app.py && \
    echo "        return jsonify({'error': str(e)})" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/health')" >> app.py && \
    echo "def health():" >> app.py && \
    echo "    return 'OK'" >> app.py && \
    echo "" >> app.py && \
    echo "if __name__ == '__main__':" >> app.py && \
    echo "    app.run(host='0.0.0.0', port=8080)" >> app.py

EXPOSE 8080

CMD ["python3", "app.py"]
