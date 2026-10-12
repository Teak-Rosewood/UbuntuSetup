#!/bin/bash
# Installs Sway and links this repo's configs into ~/.config.
# Safe to re-run. Existing files are moved to *.bak once.
set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"
cfg="$HOME/.config"

packages=(
    sway swaybg swayidle swaylock kanshi mako-notifier wdisplays
    waybar wofi kitty
    xdg-desktop-portal-wlr xdg-desktop-portal-gtk policykit-1-gnome
    network-manager-gnome blueman pavucontrol brightnessctl playerctl
    grim slurp wl-clipboard cliphist libnotify-bin wlsunset
    power-profiles-daemon
    ddcutil jq
)

echo "==> Installing packages"
sudo apt-get update
sudo apt-get install -y "${packages[@]}"

link() {
    local src="$1" dst="$2"
    mkdir -p "$(dirname "$dst")"
    if [ -e "$dst" ] && [ ! -L "$dst" ]; then
        mv "$dst" "$dst.bak"
    fi
    ln -sfn "$src" "$dst"
    echo "    $dst -> $src"
}

echo "==> Linking configs"
link "$repo/config"                 "$cfg/sway/config"
link "$repo/scripts"                "$cfg/sway/scripts"
link "$repo/kanshi/config"          "$cfg/kanshi/config"
link "$repo/waybar/config"          "$cfg/waybar/config"
link "$repo/waybar/style.css"       "$cfg/waybar/style.css"
link "$repo/kitty/kitty.conf"       "$cfg/kitty/kitty.conf"
link "$repo/mako/config"            "$cfg/mako/config"
link "$repo/wofi/config"            "$cfg/wofi/config"
link "$repo/wofi/style.css"         "$cfg/wofi/style.css"
link "$repo/swaylock/config"        "$cfg/swaylock/config"
link "$repo/xdg-desktop-portal/sway-portals.conf" "$cfg/xdg-desktop-portal/sway-portals.conf"

chmod +x "$repo"/scripts/* "$repo/session/sway-session"

echo "==> Installing GDM session entry"
sudo install -m 755 "$repo/session/sway-session" /usr/local/bin/sway-session
sudo install -m 644 "$repo/session/sway-hybrid.desktop" /usr/share/wayland-sessions/sway-hybrid.desktop

echo "Done. Log out and choose 'Sway (Hybrid GPU)' from the gear menu in GDM."
