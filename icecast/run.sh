#!/usr/bin/env bash
set -e

# Set passwords from addon options or default
SOURCE_PASS="${SOURCE_PASSWORD:-hackme}"
ADMIN_PASS="${ADMIN_PASSWORD:-hackme}"

# Replace placeholders in Icecast config
ICECAST_CONF="/etc/icecast2/icecast.xml"
sed -i "s/<source-password>.*<\/source-password>/<source-password>${SOURCE_PASS}<\/source-password>/" $ICECAST_CONF
sed -i "s/<admin-password>.*<\/admin-password>/<admin-password>${ADMIN_PASS}<\/admin-password>/" $ICECAST_CONF

# Start Icecast
exec icecast2 -n -c $ICECAST_CONF
