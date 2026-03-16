#!/bin/bash
# ==============================================================================
# DOCSight Addon Start Script
# ==============================================================================

echo "Starting DOCSight..."

# Set default log level
export LOG_LEVEL="info"

# Read configuration from Home Assistant addon options
# These are passed as environment variables by HA Supervisor
HA_PANEL=${HA_PANEL:-false}
CHECK_UPDATES=${CHECK_UPDATES:-false}
AUTO_UPDATE=${AUTO_UPDATE:-false}

# Try to read from JSON config file if environment vars are not set
if [ "$HA_PANEL" = "false" ] && [ -f "/data/options.json" ]; then
    HA_PANEL=$(jq -r '.ha_panel // false' /data/options.json)
    CHECK_UPDATES=$(jq -r '.check_updates // false' /data/options.json)
    AUTO_UPDATE=$(jq -r '.auto_update // false' /data/options.json)
fi

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

# Start management interface
echo "🌐 Starting management interface on port 9999..."
python3 /app/web_interface.py &

# Change to app directory
cd /app

# Start DOCSight
exec python3 -m app.main
