#!/usr/bin/env bash

# Setze Passwörter aus Home Assistant config.json
ICECAST_XML="/etc/icecast2/icecast.xml"

sed -i "s|<SOURCE-PASSWORD>|${SOURCE_PASSWORD}|g" $ICECAST_XML
sed -i "s|<ADMIN-PASSWORD>|${ADMIN_PASSWORD}|g" $ICECAST_XML
sed -i "s|<HOSTNAME>|${HOSTNAME}|g" $ICECAST_XML
sed -i "s|<PORT>|${PORT}|g" $ICECAST_XML

# Starte Icecast im Vordergrund
exec icecast2 -n -c $ICECAST_XML
