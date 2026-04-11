FROM python:3.12-slim

WORKDIR /app

# Install speedtest-cli and flask
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y speedtest-cli && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask

# Copy app
COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]
