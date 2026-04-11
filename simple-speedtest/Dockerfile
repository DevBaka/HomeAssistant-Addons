FROM python:3.12-slim

WORKDIR /app

RUN pip install flask

RUN echo "from flask import Flask, jsonify" > app.py && \
    echo "import time, random" >> app.py && \
    echo "app = Flask(__name__)" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/')" >> app.py && \
    echo "def index():" >> app.py && \
    echo "    return jsonify({'status': 'running'})" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/api/speedtest')" >> app.py && \
    echo "def speedtest():" >> app.py && \
    echo "    return jsonify({'download': 50, 'upload': 20, 'ping': 10})" >> app.py && \
    echo "" >> app.py && \
    echo "if __name__ == '__main__':" >> app.py && \
    echo "    app.run(host='0.0.0.0', port=8080)" >> app.py

EXPOSE 8080

CMD ["python", "app.py"]
