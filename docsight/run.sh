#!/bin/bash
# ==============================================================================
# DOCSight Addon Start Script
# ==============================================================================

echo "Starting DOCSight..."

# Set default log level
export LOG_LEVEL="info"

# Get configuration values (Home Assistant addon environment)
HA_PANEL=${HA_PANEL:-false}
CHECK_UPDATES=${CHECK_UPDATES:-false}
AUTO_UPDATE=${AUTO_UPDATE:-false}

echo "Configuration:"
echo "  - HA Panel: $HA_PANEL"
echo "  - Check Updates: $CHECK_UPDATES"
echo "  - Auto Update: $AUTO_UPDATE"

# Install HA Panel if enabled
if [ "$HA_PANEL" = "true" ]; then
    echo "🔧 Installing Home Assistant panel..."
    /app/ha_panel_install.sh
fi

# Quick check for updates if enabled (non-blocking)
if [ "$CHECK_UPDATES" = "true" ]; then
    echo "🔍 Checking for updates..."
    /app/check_updates.sh &
fi

# Change to app directory
cd /app

# Start DOCSight
exec python3 -m app.main
