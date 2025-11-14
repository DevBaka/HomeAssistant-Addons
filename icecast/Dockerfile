FROM arm64v8/debian:bookworm-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y icecast2 && \
    useradd -r -m icecast && \
    rm -rf /var/lib/apt/lists/*

COPY run.sh /run.sh
RUN chmod +x /run.sh

ENV SOURCE_PASSWORD=hackme
ENV ADMIN_PASSWORD=admin
ENV BIND_IP=0.0.0.0
ENV MOUNTPOINT=/stream

CMD ["/run.sh"]
