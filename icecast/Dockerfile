FROM arm64v8/debian:bookworm-slim

# Icecast installieren
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# HAOS Add-on Config
ENV SOURCE_PASSWORD=hackme
ENV ADMIN_PASSWORD=admin

# Icecast config über Template
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
