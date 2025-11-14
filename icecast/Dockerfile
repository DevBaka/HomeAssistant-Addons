# Base image
FROM arm64v8/debian:bookworm-slim

# Install Icecast and s6-overlay
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 curl && \
    rm -rf /var/lib/apt/lists/*

# s6-overlay
ADD https://github.com/just-containers/s6-overlay/releases/download/v3.1.2.2/s6-overlay-arm64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-arm64.tar.gz -C /

# Add Icecast user if missing
RUN getent group icecast || groupadd -r icecast && \
    id -u icecast || useradd -r -g icecast -d /var/lib/icecast -s /usr/sbin/nologin icecast && \
    mkdir -p /var/lib/icecast && chown -R icecast:icecast /var/lib/icecast

# Copy configuration
COPY icecast.xml /etc/icecast2/icecast.xml
RUN chown icecast:icecast /etc/icecast2/icecast.xml

# Copy run script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Expose Icecast port
EXPOSE 8000

# Start s6-overlay
ENTRYPOINT ["/init"]
