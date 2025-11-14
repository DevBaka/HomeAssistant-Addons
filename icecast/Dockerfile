FROM arm64v8/debian:bookworm-slim

# Install Icecast
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Add icecast user und Gruppe
RUN groupadd -f icecast && \
    id -u icecast || useradd -r -g icecast -d /var/lib/icecast -s /bin/false icecast && \
    mkdir -p /var/lib/icecast && chown -R icecast:icecast /var/lib/icecast

# Copy Icecast config
COPY icecast.xml /etc/icecast2/icecast.xml
RUN chown icecast:icecast /etc/icecast2/icecast.xml

# Copy run script
COPY run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 8000

CMD ["/run.sh"]
