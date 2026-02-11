#!/usr/bin/with-contenv bashio
# ==============================================================================
# DOCSight Addon Start Script
# ==============================================================================
bashio::log.info "Starting DOCSight..."

# Set default log level if not provided
LOG_LEVEL=$(bashio::config 'log_level' 'info')
export LOG_LEVEL

# Install Home Assistant integration if enabled
if bashio::config.true 'ha_integration'; then
    bashio::log.info "Installing Home Assistant integration..."
    /app/ha_integration_install.sh
fi

# Change to app directory
cd /app

# Start DOCSight
exec python3 -m app.main
