FROM python:3.12-slim
ARG VERSION=dev
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gosu \
    && rm -rf /var/lib/apt/lists/*

# Create appuser
RUN adduser --disabled-password --gecos "" --uid 1000 appuser

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app/ ./app/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create data directory
RUN mkdir -p /data && chown appuser:appuser /data

# Set up version
RUN echo "${VERSION}" > /app/VERSION

# Health check
HEALTHCHECK --interval=60s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8765/health || exit 1

# Expose port
EXPOSE 8765

# Start the application
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "-m", "app.main"]
