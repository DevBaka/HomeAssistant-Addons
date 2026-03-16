FROM python:3.12-slim
ARG VERSION=dev
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app/ ./app/
COPY run.sh /run.sh
COPY update_docsight.sh /update_docsight.sh
COPY ha_panel_install.sh /ha_panel_install.sh
COPY manual_update.sh /manual_update.sh
COPY check_updates.sh /check_updates.sh
COPY web_interface.py /web_interface.py
RUN chmod +x /run.sh /update_docsight.sh /ha_panel_install.sh /manual_update.sh /check_updates.sh

# Set up version
RUN echo "${VERSION}" > /app/VERSION

# Health check
HEALTHCHECK --interval=60s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:8765/health || exit 1

# Expose port
EXPOSE 8765 9999

# Start the application
CMD ["/run.sh"]
