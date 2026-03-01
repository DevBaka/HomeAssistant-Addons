#!/bin/bash
# ==============================================================================
# Manual Update Trigger for DOCSight
# ==============================================================================

echo "🚀 Starting manual DOCSight update..."

# Run the update script
/app/update_docsight.sh

# Check if update was successful
if [ $? -eq 0 ]; then
    echo "✅ Update completed! Please restart the addon."
    echo "📋 You can restart the addon from Home Assistant Supervisor."
else
    echo "❌ Update failed. Please check the logs."
    exit 1
fi
