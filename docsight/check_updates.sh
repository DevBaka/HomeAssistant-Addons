#!/bin/bash
# ==============================================================================
# Quick Update Check for DOCSight
# ==============================================================================

UPSTREAM_REPO="itsDNNS/docsight"
LOCAL_DIR="/app"

echo "🔍 Quick update check..."

# Get latest release info (with timeout)
LATEST_RELEASE=$(timeout 10 curl -s "https://api.github.com/repos/${UPSTREAM_REPO}/releases/latest" | grep '"tag_name"' | cut -d '"' -f 4 || echo "unknown")
CURRENT_VERSION=$(cat ${LOCAL_DIR}/VERSION 2>/dev/null || echo "unknown")

echo "📦 Latest: ${LATEST_RELEASE} | Current: ${CURRENT_VERSION}"

if [ "$LATEST_RELEASE" != "unknown" ] && [ "$CURRENT_VERSION" != "unknown" ] && [ "$LATEST_RELEASE" != "$CURRENT_VERSION" ]; then
    echo "🔄 Update available: ${LATEST_RELEASE}"
    echo "💡 Run '/app/manual_update.sh' to update"
else
    echo "✅ Up to date"
fi
