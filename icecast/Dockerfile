FROM arm64v8/debian:bookworm-slim

# Install Icecast
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    rm -rf /var/lib/apt/lists/*

# Add user
RUN useradd -r -m icecast

# Copy start script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Expose Icecast ports
EXPOSE 8000

CMD ["/run.sh"]
