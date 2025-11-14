# ARM64-kompatibles Base-Image
ARG BUILD_FROM=ghcr.io/linuxserver/icecast:latest
FROM ${BUILD_FROM}

# Umgebungsvariablen für HAOS Add-on
ENV PUID=1000
ENV PGID=1000
ENV TZ=Europe/Berlin
ENV SOURCE_PASSWORD=hackme
ENV ADMIN_PASSWORD=admin

# Kein run.sh nötig – linuxserver/icecast startet automatisch
