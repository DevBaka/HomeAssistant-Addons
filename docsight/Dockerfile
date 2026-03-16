FROM python:3.12-slim
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY tools/icmp_probe_helper.c /build/
RUN mkdir -p /build/out && \
    gcc -O2 -Wall -o /build/out/docsight-icmp-helper /build/icmp_probe_helper.c && \
    cp /build/out/docsight-icmp-helper /usr/local/bin/

RUN echo "dev" > /app/VERSION

HEALTHCHECK --interval=60s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8765/health || exit 1

EXPOSE 8765

CMD ["python", "-m", "app.main"]
