#!/usr/bin/with-contenv bashio
# ==============================================================================
# Icecast Addon Start Script
# ==============================================================================

# Start Icecast as non-root user
exec su -s /bin/bash icecast -c "icecast -c /etc/icecast2/icecast.xml"
