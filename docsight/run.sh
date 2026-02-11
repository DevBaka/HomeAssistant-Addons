#!/bin/bash
# ==============================================================================
# DOCSight Addon Start Script
# ==============================================================================

# Source bashio functions if available
if [ -f /usr/lib/bashio/bashio ]; then
    source /usr/lib/bashio/bashio
    bashio::log.info "Starting DOCSight..."
else
    echo "Starting DOCSight..."
fi

# Set default log level if not provided
LOG_LEVEL="info"
if [ -f /usr/lib/bashio/bashio ]; then
    LOG_LEVEL=$(bashio::config 'log_level' 'info')
fi
export LOG_LEVEL

# Install Home Assistant integration if enabled
if [ -f /usr/lib/bashio/bashio ] && bashio::config.true 'ha_integration'; then
    if [ -f /usr/lib/bashio/bashio ]; then
        bashio::log.info "Installing Home Assistant integration..."
    else
        echo "Installing Home Assistant integration..."
    fi
    /ha_integration_install.sh
fi

# Change to app directory
cd /app

# Start DOCSight
exec python3 -m app.main
