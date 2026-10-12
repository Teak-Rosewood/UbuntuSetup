#!/bin/bash
# System-level settings that are not owned by any package: kernel module options
# for the hybrid NVIDIA laptop and the extra GDM session entries.
# Run: sudo ~/projects/UbuntuSetup/system/install.sh
set -euo pipefail

[ "$(id -u)" -eq 0 ] || { echo "Run with sudo"; exit 1; }
repo="$(cd "$(dirname "$0")" && pwd)"

install -m 644 "$repo"/modprobe/*.conf /etc/modprobe.d/
install -m 644 "$repo"/wayland-sessions/*.desktop /usr/share/wayland-sessions/
update-initramfs -u

cat <<MSG
Module options and session entries installed; initramfs rebuilt.
Not automated (a typo in GRUB can stop the machine booting): set the kernel
command line from system/grub-cmdline.txt in /etc/default/grub, then run
  sudo update-grub
MSG
