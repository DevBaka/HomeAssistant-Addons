ARG BUILD_FROM=ghcr.io/linuxserver/icecast:latest
FROM ${BUILD_FROM}

# Environment variables für HAOS Add-on
ENV PUID=1000
ENV PGID=1000
ENV TZ=Europe/Berlin

# Optionale Config: SOURCE_PASSWORD, ADMIN_PASSWORD
ENV SOURCE_PASSWORD=hackme
ENV ADMIN_PASSWORD=admin

# linuxserver/icecast startet automatisch, kein run.sh nötig
