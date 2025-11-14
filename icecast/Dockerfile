FROM arm64v8/debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install Icecast and small support package for mime types
RUN apt-get update && \
    apt-get install -y --no-install-recommends icecast2 mime-support && \
    rm -rf /var/lib/apt/lists/*

# Create group and user in a robust way
RUN groupadd -f icecast && \
    if ! id -u icecast >/dev/null 2>&1; then useradd -r -g icecast -d /var/lib/icecast -s /bin/false icecast; fi && \
    mkdir -p /var/lib/icecast /var/log/icecast2 && chown -R icecast:icecast /var/lib/icecast /var/log/icecast2

# Copy config and start script
COPY icecast.xml /etc/icecast2/icecast.xml
RUN chown icecast:icecast /etc/icecast2/icecast.xml

COPY run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 8000

CMD ["/run.sh"]
