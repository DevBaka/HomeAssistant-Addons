#!/bin/bash
# ==============================================================================
# DOCSight Addon Start Script
# ==============================================================================

echo "Starting DOCSight..."

# Set default log level
export LOG_LEVEL="info"

# Change to app directory
cd /app

# Start DOCSight
exec python3 -m app.main
