FROM python:3.12-slim

WORKDIR /app

# Install speedtest-cli and flask
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y curl gnupg && \
    curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash && \
    apt-get update && \
    apt-get install -y speedtest && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask

# Create app with HTML GUI
RUN echo "from flask import Flask, render_template_string, jsonify, request" > app.py && \
    echo "import os, subprocess, json" >> app.py && \
    echo "app = Flask(__name__)" >> app.py && \
    echo "" >> app.py && \
    echo "HTML = '''" >> app.py && \
    echo "<!DOCTYPE html>" >> app.py && \
    echo "<html><head><title>Speedtest Tracker</title></head><body>" >> app.py && \
    echo "<h1>Speedtest Tracker</h1>" >> app.py && \
    echo "<button onclick=runTest()>Start Speedtest</button>" >> app.py && \
    echo "<div id=result></div>" >> app.py && \
    echo "<script>" >> app.py && \
    echo "function runTest() {" >> app.py && \
    echo "  fetch(").then(r=>r.json()).then(d=>{" >> app.py && \
    echo "    document.getElementById(").innerHTML = JSON.stringify(d, null, 2);" >> app.py && \
    echo "  });" >> app.py && \
    echo "}" >> app.py && \
    echo "</script></body></html>" >> app.py && \
    echo "'''" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/')" >> app.py && \
    echo "def index():" >> app.py && \
    echo "    return render_template_string(HTML)" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/api/speedtest')" >> app.py && \
    echo "def run_speedtest():" >> app.py && \
    echo "    try:" >> app.py && \
    echo "        result = subprocess.run(['speedtest', '-f', 'json'], capture_output=True, text=True, timeout=120)" >> app.py && \
    echo "        return jsonify(json.loads(result.stdout))" >> app.py && \
    echo "    except Exception as e:" >> app.py && \
    echo "        return jsonify({'error': str(e)})" >> app.py && \
    echo "" >> app.py && \
    echo "if __name__ == '__main__':" >> app.py && \
    echo "    port = int(os.environ.get('PORT', 8080))" >> app.py && \
    echo "    app.run(host='0.0.0.0', port=port)" >> app.py

EXPOSE 8080

CMD ["python", "app.py"]
