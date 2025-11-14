ARG BUILD_FROM=ghcr.io/linuxserver/icecast:latest
FROM ${BUILD_FROM}

# linuxserver/icecast startet Icecast automatisch
# Optionale Umgebungsvariablen:
ENV PUID=1000
ENV PGID=1000
ENV TZ=Europe/Berlin
ENV SOURCE_PASSWORD=hackme
ENV ADMIN_PASSWORD=admin

# Kein run.sh nötig
