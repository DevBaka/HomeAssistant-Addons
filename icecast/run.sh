#!/usr/bin/env bash

# Use custom port if provided
if [ ! -z "$PORT" ]; then
    sed -i "s/<port>8000<\/port>/<port>$PORT<\/port>/" /etc/icecast2/icecast.xml
fi

# Start Icecast as icecast user
exec su -s /bin/bash icecast -c "icecast -c /etc/icecast2/icecast.xml"
