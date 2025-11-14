ARG BUILD_FROM=ghcr.io/linuxserver/icecast:latest
FROM ${BUILD_FROM}

# Environment variables für HAOS Add-on
ENV SOURCE_PASSWORD=${SOURCE_PASSWORD}
ENV ADMIN_PASSWORD=${ADMIN_PASSWORD}

# Config wird über linuxserver/icecast automatisch übernommen
# Ports und Volumes via HA Add-on Config
