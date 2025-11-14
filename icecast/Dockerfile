# Basis Image für ARM64
FROM arm64v8/debian:bookworm-slim

# Installiere Icecast2
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Addon Dateien
COPY icecast.xml /etc/icecast2/icecast.xml
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Starte Icecast
CMD ["/run.sh"]
