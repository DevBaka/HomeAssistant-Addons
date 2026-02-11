#!/usr/bin/with-contenv bashio
# ==============================================================================
# Install DOCSight Home Assistant Integration
# ==============================================================================

bashio::log.info "Installing DOCSight Home Assistant integration..."

# Get Home Assistant config path
HA_CONFIG=$(bashio::config 'config_path')

if [ -z "$HA_CONFIG" ]; then
    HA_CONFIG="/config"
fi

# Create custom_components directory if it doesn't exist
mkdir -p "$HA_CONFIG/custom_components/docsight"

# Copy integration files
cp -r /app/ha_integration/* "$HA_CONFIG/custom_components/docsight/"

# Set proper permissions
chown -R root:root "$HA_CONFIG/custom_components/docsight"
chmod -R 755 "$HA_CONFIG/custom_components/docsight"

bashio::log.info "DOCSight integration installed successfully!"
bashio::log.info "Please restart Home Assistant to complete the installation."
