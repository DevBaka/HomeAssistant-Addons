FROM lscr.io/linuxserver/speedtest-tracker:latest

# Create data directory
RUN mkdir -p /config

# Set permissions
RUN chown -R abc:abc /config

EXPOSE 80

CMD ["/init"]
