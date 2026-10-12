#!/bin/bash
# Links the user-level dotfiles in this repo into $HOME. No sudo.
# Safe to re-run. Existing real files are moved to *.bak once.
#
# Other pieces have their own installers (see README "Restore a machine"):
#   sway/install.sh   Sway, waybar, kanshi, ... (uses sudo)
#   User/install.sh   VS Code settings + extensions
#   docker/install.sh Docker Engine (sudo)
#   system/install.sh NVIDIA/wifi module options, extra GDM sessions (sudo)
set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"

link() {
    local src="$1" dst="$2"
    mkdir -p "$(dirname "$dst")"
    if [ -e "$dst" ] && [ ! -L "$dst" ]; then
        mv "$dst" "$dst.bak"
    fi
    ln -sfn "$src" "$dst"
    echo "    $dst -> $src"
}

echo "==> Linking dotfiles"
link "$repo/bash/bashrc"                          "$HOME/.bashrc"
link "$repo/bash/profile"                         "$HOME/.profile"
link "$repo/git/gitconfig"                        "$HOME/.gitconfig"
link "$repo/desktop/gtk-3.0/settings.ini"         "$HOME/.config/gtk-3.0/settings.ini"
link "$repo/desktop/gtk-4.0/settings.ini"         "$HOME/.config/gtk-4.0/settings.ini"
link "$repo/desktop/nwg-displays/config"          "$HOME/.config/nwg-displays/config"
link "$repo/desktop/nwg-look/config"              "$HOME/.config/nwg-look/config"
link "$repo/desktop/mimeapps.list"                "$HOME/.config/mimeapps.list"
link "$repo/hypr"                                 "$HOME/.config/hypr"
