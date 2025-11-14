FROM arm64v8/debian:bookworm-slim

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Icecast user & directories
RUN groupadd -r icecast && \
    useradd -r -g icecast -d /var/lib/icecast -s /usr/sbin/nologin icecast && \
    mkdir -p /var/lib/icecast && \
    chown -R icecast:icecast /var/lib/icecast

# Copy default config
COPY icecast.xml /etc/icecast2/icecast.xml
RUN chown icecast:icecast /etc/icecast2/icecast.xml

# Switch to icecast user
USER icecast

# Expose port
EXPOSE 8000

# Run icecast
CMD ["icecast", "-c", "/etc/icecast2/icecast.xml"]
