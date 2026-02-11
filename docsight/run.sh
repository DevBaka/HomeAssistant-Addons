#!/usr/bin/with-contenv bashio
# ==============================================================================
# DOCSight Addon Start Script
# ==============================================================================
bashio::log.info "Starting DOCSight..."

# Set default log level if not provided
LOG_LEVEL=$(bashio::config 'log_level' 'info')
export LOG_LEVEL

# Change to app directory
cd /app

# Start DOCSight
exec python3 -m app.main
