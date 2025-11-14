#!/usr/bin/env bash
set -e

ICECAST_USER=icecast

# Icecast Config erstellen
cat <<EOF > /etc/icecast2/icecast.xml
<icecast>
  <authentication>
    <source-password>${SOURCE_PASSWORD}</source-password>
    <admin-user>admin</admin-user>
    <admin-password>${ADMIN_PASSWORD}</admin-password>
  </authentication>
  <hostname>${BIND_IP}</hostname>
  <listen-socket>
    <port>8000</port>
    <bind-address>${BIND_IP}</bind-address>
  </listen-socket>
  <fileserve>1</fileserve>
  <paths>
    <logdir>/var/log/icecast2</logdir>
    <webroot>/usr/share/icecast2/web</webroot>
  </paths>
  <mount>
    <mount-name>${MOUNTPOINT}</mount-name>
  </mount>
</icecast>
EOF

# Icecast als icecast User starten
exec su -s /bin/bash -c "icecast2 -c /etc/icecast2/icecast.xml" $ICECAST_USER
