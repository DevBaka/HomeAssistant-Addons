FROM python:3.12-slim

WORKDIR /app

# Install Python packages
RUN pip install --no-cache-dir flask

# Create the application
RUN echo "from flask import Flask, jsonify" > app.py && \
    echo "import os" >> app.py && \
    echo "" >> app.py && \
    echo "app = Flask(__name__)" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/')" >> app.py && \
    echo "def index():" >> app.py && \
    echo "    return jsonify({" >> app.py && \
    echo "        \"status\": \"running\"," >> app.py && \
    echo "        \"service\": \"spotify-simple\"" >> app.py && \
    echo "    })" >> app.py && \
    echo "" >> app.py && \
    echo "@app.route('/health')" >> app.py && \
    echo "def health():" >> app.py && \
    echo "    return jsonify({\"status\": \"ok\"})" >> app.py && \
    echo "" >> app.py && \
    echo "if __name__ == '__main__':" >> app.py && \
    echo "    port = int(os.environ.get('PORT', 4070))" >> app.py && \
    echo "    app.run(host='0.0.0.0', port=port)" >> app.py

EXPOSE 4070

CMD ["python", "app.py"]
