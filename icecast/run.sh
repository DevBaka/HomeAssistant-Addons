#!/usr/bin/env bash
set -e

# default values if HA didn't pass them
: "${BIND_IP:=0.0.0.0}"
: "${PORT:=8000}"
: "${MOUNTPOINT:=/stream}"
: "${SOURCE_PASSWORD:=hackme}"
: "${ADMIN_PASSWORD:=admin}"

ICECAST_CONF="/etc/icecast2/icecast.xml"

# replace placeholders
sed -i "s|<BIND_IP>|${BIND_IP}|g" "$ICECAST_CONF"
sed -i "s|<PORT>|${PORT}|g" "$ICECAST_CONF"
sed -i "s|<MOUNTPOINT>|${MOUNTPOINT}|g" "$ICECAST_CONF"
sed -i "s|<SOURCE_PASSWORD>|${SOURCE_PASSWORD}|g" "$ICECAST_CONF"
sed -i "s|<ADMIN_PASSWORD>|${ADMIN_PASSWORD}|g" "$ICECAST_CONF"

# ensure permissions
chown icecast:icecast "$ICECAST_CONF"
chown -R icecast:icecast /var/lib/icecast /var/log/icecast2

# run icecast2 in foreground. icecast2 will drop privileges using <changeowner>.
exec /usr/bin/icecast2 -n -c "$ICECAST_CONF"
