#!/bin/bash
# Installs and configures Docker Engine + Compose v2 from the Ubuntu archive.
# Run: sudo ~/projects/UbuntuSetup/docker/install.sh
set -euo pipefail

[ "$(id -u)" -eq 0 ] || { echo "Run with sudo"; exit 1; }
user="${SUDO_USER:?run via sudo, not as a root login}"

apt-get update
apt-get install -y docker.io docker-compose-v2 docker-buildx

# Rotate container logs so they never fill the disk
install -d /etc/docker
cat > /etc/docker/daemon.json <<'EOF'
{
  "log-driver": "json-file",
  "log-opts": { "max-size": "10m", "max-file": "3" }
}
EOF

# Let the user run docker without sudo (takes effect on next login)
usermod -aG docker "$user"

systemctl enable --now docker
systemctl restart docker

docker --version
docker compose version
echo "Done. Log out and back in (or run: newgrp docker) to use docker without sudo."
