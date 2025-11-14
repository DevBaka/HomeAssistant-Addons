#!/usr/bin/env bash

# Generate config
cat <<EOF > /etc/icecast2/icecast.xml
<icecast>
  <authentication>
    <source-password>${SOURCE_PASSWORD}</source-password>
    <admin-user>admin</admin-user>
    <admin-password>${ADMIN_PASSWORD}</admin-password>
  </authentication>

  <hostname>homeassistant</hostname>

  <listen-socket>
    <port>8000</port>
  </listen-socket>

  <fileserve>1</fileserve>

  <paths>
    <logdir>/var/log/icecast</logdir>
    <webroot>/usr/share/icecast2/web</webroot>
  </paths>
</icecast>
EOF

exec icecast2 -c /etc/icecast2/icecast.xml
