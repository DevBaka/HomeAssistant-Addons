FROM arm64v8/debian:bookworm-slim

# Install Python, Flask and speedtest-cli
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip curl speedtest-cli && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install flask

# Create simple speedtest app
RUN echo "from flask import Flask, jsonify" > app.py && \
    echo "import subprocess, json" >> app.py && \
    echo "app = Flask(__name__)" >> app.py && \
    echo "" >> app.py && \
    echo "def get_speedtest():" >> app.py && \
    echo "    try:" >> app.py && \
    echo "        result = subprocess.run(['speedtest-cli', '--json'], capture_output=True, text=True, timeout=120)" >> app.py && \
    echo "        return json.loads(result.stdout) if result.returncode == 0 else None" >> app.py && \
    echo "    except:" >> app.py && \
    echo "        return None" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/api/speedtest')" >> app.py && \
    echo "def speedtest():" >> app.py && \
    echo "    data = get_speedtest()" >> app.py && \
    echo "    return jsonify(data) if data else jsonify({'error': 'speedtest failed'})" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/')" >> app.py && \
    echo "def index():" >> app.py && \
    echo "    return 'Speedtest Tracker Running'" >> app.py && \
    echo "" >> app.py && \
    echo "if __name__ == '__main__':" >> app.py && \
    echo "    app.run(host='0.0.0.0', port=8080)" >> app.py

EXPOSE 8080

CMD ["python3", "app.py"]
