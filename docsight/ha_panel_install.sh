#!/bin/bash
# ==============================================================================
# Install DOCSight Panel in Home Assistant
# ==============================================================================

CONFIG_DIR="/config"
PANEL_FILE="$CONFIG_DIR/configuration.yaml"

echo "🔧 Installing DOCSight panel in Home Assistant..."

# Create backup
if [ -f "$PANEL_FILE" ]; then
    cp "$PANEL_FILE" "$PANEL_FILE.backup"
    echo "💾 Backed up configuration.yaml"
fi

# Add panel configuration
cat >> "$PANEL_FILE" << 'EOF'

# DOCSight Panel Configuration
panel_iframe:
  docsight:
    title: DOCSight
    icon: mdi:network-outline
    url: http://homeassistant.local:8765
    require_admin: false

EOF

echo "✅ DOCSight panel installed successfully!"
echo "🔄 Please restart Home Assistant to see the panel"
echo "📍 You'll find DOCSight in the sidebar with a network icon"
