#!/usr/bin/env bash

# Set Icecast config file permissions
chown icecast:icecast /etc/icecast2/icecast.xml

# Start Icecast as the icecast user using changeowner
exec icecast -c /etc/icecast2/icecast.xml
