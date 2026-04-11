FROM python:3.12-slim
WORKDIR /app

RUN pip install --no-cache-dir flask

RUN echo "from flask import Flask" > app.py && \
    echo "app = Flask(__name__)" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/')" >> app.py && \
    echo "def hello():" >> app.py && \
    echo "    return 'Speedtest Tracker is running!'" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/health')" >> app.py && \
    echo "def health():" >> app.py && \
    echo "    return 'OK'" >> app.py && \
    echo "" >> app.py && \
    echo "if __name__ == '__main__':" >> app.py && \
    echo "    app.run(host='0.0.0.0', port=8080)" >> app.py

EXPOSE 8080

CMD ["python", "app.py"]
