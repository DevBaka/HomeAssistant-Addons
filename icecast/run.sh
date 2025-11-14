#!/usr/bin/env bash
set -e

# Erzeuge Icecast Config aus HAOS Options
cat <<EOF > /etc/icecast2/icecast.xml
<icecast>
  <authentication>
    <source-password>${SOURCE_PASSWORD}</source-password>
    <admin-user>admin</admin-user>
    <admin-password>${ADMIN_PASSWORD}</admin-password>
  </authentication>
  <hostname>raspberrypi</hostname>
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

exec icecast2 -c /etc/icecast2/icecast.xml
