#!/bin/bash
# ==============================================================================
# Install DOCSight Home Assistant Integration
# ==============================================================================

# Source bashio functions if available
if [ -f /usr/lib/bashio/bashio ]; then
    source /usr/lib/bashio/bashio
    bashio::log.info "Installing DOCSight Home Assistant integration..."
else
    echo "Installing DOCSight Home Assistant integration..."
fi

# Get Home Assistant config path
HA_CONFIG="/config"
if [ -f /usr/lib/bashio/bashio ]; then
    HA_CONFIG=$(bashio::config 'config_path' '/config')
fi

# Create custom_components directory if it doesn't exist
mkdir -p "$HA_CONFIG/custom_components/docsight"

# Copy integration files
if [ -d "/app/ha_integration" ]; then
    cp -r /app/ha_integration/* "$HA_CONFIG/custom_components/docsight/"
else
    echo "Warning: ha_integration directory not found"
fi

# Set proper permissions
chown -R root:root "$HA_CONFIG/custom_components/docsight" 2>/dev/null || true
chmod -R 755 "$HA_CONFIG/custom_components/docsight" 2>/dev/null || true

if [ -f /usr/lib/bashio/bashio ]; then
    bashio::log.info "DOCSight integration installed successfully!"
    bashio::log.info "Please restart Home Assistant to complete the installation."
else
    echo "DOCSight integration installed successfully!"
    echo "Please restart Home Assistant to complete the installation."
fi
