#!/usr/bin/env bash
set -e

# Icecast als nicht-root user ausführen
ICECAST_USER=icecast
ICECAST_GROUP=icecast

# Hostname aus HAOS Add-on Options
HOSTNAME=${HOSTNAME:-raspberrypi}

# Config generieren
cat <<EOF > /etc/icecast2/icecast.xml
<icecast>
  <authentication>
    <source-password>${SOURCE_PASSWORD}</source-password>
    <admin-user>admin</admin-user>
    <admin-password>${ADMIN_PASSWORD}</admin-password>
  </authentication>
  <hostname>${HOSTNAME}</hostname>
  <listen-socket>
    <port>8000</port>
  </listen-socket>
  <fileserve>1</fileserve>
  <paths>
    <logdir>/var/log/icecast2</logdir>
    <webroot>/usr/share/icecast2/web</webroot>
  </paths>
</icecast>
EOF

# Icecast2 starten
exec su -s /bin/bash -c "icecast2 -c /etc/icecast2/icecast.xml" $ICECAST_USER
