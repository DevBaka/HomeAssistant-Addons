#!/usr/bin/env bash
# Start Icecast direkt, HA Add-on läuft als PID 1
exec icecast -c /etc/icecast2/icecast.xml
