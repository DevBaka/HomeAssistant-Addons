#!/bin/bash
# ==============================================================================
# DOCSight Update Script
# ==============================================================================
# This script updates the local DOCSight files from the upstream repository

set -e

UPSTREAM_REPO="itsDNNS/docsight"
LOCAL_DIR="docsight"

echo "🔍 Checking for DOCSight updates..."

# Get latest release info
LATEST_RELEASE=$(curl -s "https://api.github.com/repos/${UPSTREAM_REPO}/releases/latest" | grep '"tag_name"' | cut -d '"' -f 4)
CURRENT_VERSION=$(cat ${LOCAL_DIR}/VERSION 2>/dev/null || echo "unknown")

echo "📦 Latest upstream version: ${LATEST_RELEASE}"
echo "📦 Current local version: ${CURRENT_VERSION}"

if [ "$LATEST_RELEASE" = "$CURRENT_VERSION" ]; then
    echo "✅ Already up to date!"
    exit 0
fi

echo "🔄 Updating to version ${LATEST_RELEASE}..."

# Create temporary directory
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

# Download latest release
echo "📥 Downloading latest release..."
curl -L "https://github.com/${UPSTREAM_REPO}/archive/${LATEST_RELEASE}.tar.gz" | tar xz -C "$TEMP_DIR"

# Backup important HA addon files
echo "💾 Backing up Home Assistant addon files..."
cp "${LOCAL_DIR}/config.json" "${TEMP_DIR}/config.json.backup" 2>/dev/null || true
cp "${LOCAL_DIR}/run.sh" "${TEMP_DIR}/run.sh.backup" 2>/dev/null || true
cp "${LOCAL_DIR}/Dockerfile" "${TEMP_DIR}/Dockerfile.backup" 2>/dev/null || true
cp "${LOCAL_DIR}/Dockerfile."* "${TEMP_DIR}/" 2>/dev/null || true

# Update files
echo "📂 Updating application files..."
rm -rf "${LOCAL_DIR}/app"
cp -r "${TEMP_DIR}/docsight-"*/app/* "${LOCAL_DIR}/app/"
cp "${TEMP_DIR}/docsight-"*/requirements.txt "${LOCAL_DIR}/"
cp "${TEMP_DIR}/docsight-"*/VERSION "${LOCAL_DIR}/"

# Restore HA addon files
echo "🔄 Restoring Home Assistant addon files..."
mv "${TEMP_DIR}/config.json.backup" "${LOCAL_DIR}/config.json" 2>/dev/null || true
mv "${TEMP_DIR}/run.sh.backup" "${LOCAL_DIR}/run.sh" 2>/dev/null || true
mv "${TEMP_DIR}/Dockerfile.backup" "${LOCAL_DIR}/Dockerfile" 2>/dev/null || true
mv "${TEMP_DIR}/Dockerfile."* "${LOCAL_DIR}/" 2>/dev/null || true

# Update version in config.json
echo "🔧 Updating version in config.json..."
sed -i "s/\"version\": \".*\"/\"version\": \"${LATEST_RELEASE}\"/" "${LOCAL_DIR}/config.json"

# Create changelog entry
CHANGELOG_FILE="CHANGELOG.md"
echo "📝 Updating changelog..."
cat > "${CHANGELOG_FILE}.tmp" << EOF
# Changelog

## [${LATEST_RELEASE}] - $(date +%Y-%m-%d)

### Updated
- DOCSight updated to upstream version ${LATEST_VERSION}

### Upstream Changes
See the [DOCSight changelog](https://github.com/${UPSTREAM_REPO}/releases/tag/${LATEST_RELEASE}) for details.

EOF

if [ -f "$CHANGELOG_FILE" ]; then
    tail -n +2 "$CHANGELOG_FILE" >> "${CHANGELOG_FILE}.tmp"
    mv "${CHANGELOG_FILE}.tmp" "$CHANGELOG_FILE"
else
    mv "${CHANGELOG_FILE}.tmp" "$CHANGELOG_FILE"
fi

echo "✅ Update completed successfully!"
echo "📋 Summary:"
echo "   - Updated DOCSight from ${CURRENT_VERSION} to ${LATEST_RELEASE}"
echo "   - Home Assistant addon configuration preserved"
echo "   - Changelog updated"
echo ""
echo "🚀 Commit and push these changes to trigger a new build:"
