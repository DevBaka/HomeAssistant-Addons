FROM arm64v8/debian:bookworm-slim

# Install Icecast
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Add icecast user if it doesn't exist
RUN id -u icecast &>/dev/null || useradd -r -d /var/lib/icecast -s /usr/sbin/nologin icecast && \
    mkdir -p /var/lib/icecast && chown icecast:icecast /var/lib/icecast

# Copy default Icecast config
COPY icecast.xml /etc/icecast2/icecast.xml
RUN chown icecast:icecast /etc/icecast2/icecast.xml

# Copy start script
COPY run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 8000

CMD ["/run.sh"]
