FROM arm64v8/debian:bookworm-slim

# Install Icecast
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Add icecast user if not exists
RUN getent group icecast || groupadd -r icecast && \
    id -u icecast || useradd -r -g icecast -d /var/lib/icecast -s /usr/sbin/nologin icecast && \
    mkdir -p /var/lib/icecast && chown -R icecast:icecast /var/lib/icecast

# Copy config
COPY icecast.xml /etc/icecast2/icecast.xml
RUN chown icecast:icecast /etc/icecast2/icecast.xml

# Copy run script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Expose ports
EXPOSE 8000

# Use s6-overlay entrypoint
ENTRYPOINT ["/run.sh"]
