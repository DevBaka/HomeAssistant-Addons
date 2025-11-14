FROM arm64v8/debian:bookworm-slim

# Install Icecast
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Add user only if it doesn't exist
RUN id -u icecast &>/dev/null || useradd -r -m -s /bin/false icecast

# Copy start script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Copy default Icecast config
COPY icecast.xml /etc/icecast2/icecast.xml

# Expose Icecast port
EXPOSE 8000

CMD ["/run.sh"]
