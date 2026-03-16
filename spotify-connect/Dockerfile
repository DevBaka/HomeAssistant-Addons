FROM python:3.12-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir flask requests

# Create simple app
RUN echo 'from flask import Flask, jsonify\nimport os\n\napp = Flask(__name__)\n\n@app.route("/")\ndef index():\n    return jsonify({"status": "running", "service": "spotify-connect"})\n\n@app.route("/health")\ndef health():\n    return jsonify({"status": "ok"})\n\nif __name__ == "__main__":\n    port = int(os.environ.get("PORT", 4070))\n    app.run(host="0.0.0.0", port=port)' > app.py

EXPOSE 4070

CMD ["python", "app.py"]
