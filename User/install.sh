#!/bin/bash
# Recreates the VS Code setup: links settings, keybindings, tasks and snippets from
# this repo into ~/.config/Code/User, then installs the extensions in
# extensions.txt at their recorded versions (falls back to the latest if a version
# is no longer available). Safe to re-run; existing real files are moved to *.bak once.
#
# Not stored here on purpose: chatLanguageModels.json (holds API keys), Settings Sync
# state, globalStorage and workspaceStorage. Re-enter those by hand or via Settings Sync.
#
# Refresh the extension list after installing or removing extensions:
#   code --list-extensions --show-versions > extensions.txt
set -euo pipefail

repo="$(cd "$(dirname "$0")" && pwd)"
dst="$HOME/.config/Code/User"

link() {
    local src="$1" target="$2"
    mkdir -p "$(dirname "$target")"
    if [ -e "$target" ] && [ ! -L "$target" ]; then
        mv "$target" "$target.bak"
    fi
    ln -sfn "$src" "$target"
    echo "    $target -> $src"
}

echo "==> Linking VS Code user config"
link "$repo/settings.json"    "$dst/settings.json"
link "$repo/keybindings.json" "$dst/keybindings.json"
link "$repo/tasks.json"       "$dst/tasks.json"
link "$repo/snippets"         "$dst/snippets"

echo "==> Installing extensions"
installed="$(code --list-extensions --show-versions)"
while read -r ext; do
    [ -n "$ext" ] || continue
    if grep -qix "$ext" <<<"$installed"; then
        echo "    have $ext"
    elif code --install-extension "$ext" --force >/dev/null 2>&1; then
        echo "    installed $ext"
    elif code --install-extension "${ext%@*}" >/dev/null 2>&1; then
        echo "    installed ${ext%@*} (pinned version $ext unavailable)"
    else
        echo "    FAILED $ext" >&2
    fi
done <"$repo/extensions.txt"
