# Leichtgewichtiges ARM64 Base-Image
FROM arm64v8/debian:bookworm-slim

# Icecast installieren
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# HAOS Add-on Umgebungsvariablen
ENV SOURCE_PASSWORD=hackme
ENV ADMIN_PASSWORD=admin

# Add Startscript
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Start Icecast
CMD ["/run.sh"]
