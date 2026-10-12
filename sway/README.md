# Sway Configuration

Sway port of the i3 setup: same modifier, vim-style keys, workspaces and
layout bindings, with a flat, light look and bundled desktop/lock-screen wallpapers.
Targets Ubuntu 24.04/26.04 on a hybrid Intel + NVIDIA laptop.

## Install
```bash
cd sway
./install.sh
```
Installs the packages, symlinks every config into `~/.config`, and adds a
`Sway (Hybrid GPU)` entry to GDM. Log out and pick it from the gear menu.
GNOME stays available as a fallback.

## What replaces what
| i3 / X11 | Sway |
|---|---|
| i3bar + bumblebee-status | waybar |
| rofi | wofi |
| i3lock / betterlockscreen + xss-lock | swaylock + swayidle |
| feh | built-in `output * bg` |
| picom | none (no transparency, to save GPU) |
| xrandr / arandr | kanshi (automatic) + wdisplays (GUI) |
| gnome-screenshot | grim + slurp (`scripts/screenshot`) |
| xinput | `input` blocks in `config` |
| gnome-terminal | kitty |
| (no notification daemon) | mako |

The desktop and lock-screen images are stored in `wallpapers/` so the config
does not depend on files elsewhere on the machine.

## Keys
Same as i3 unless noted. `$mod` is the Super key.

| Key | Action |
|---|---|
| `$mod+Return` | terminal (kitty) |
| `$mod+d` | launcher |
| `$mod+x` | close window |
| `$mod+h/j/k/l` | focus (add Shift to move) |
| `$mod+n` / `$mod+v` | split horizontal / vertical |
| `$mod+s` / `$mod+w` / `$mod+e` | stacking / tabbed / toggle split |
| `$mod+f` | fullscreen |
| `$mod+r` | resize mode |
| `$mod+1..0` | workspaces (Shift to move window) |
| `$mod+m` | send workspace to the other monitor |
| `$mod+Shift+x` | lock |
| `$mod+Shift+p` | power menu (was an instant shutdown in i3) |
| `$mod+Shift+d` | display settings GUI |
| `$mod+Shift+v` | clipboard history |
| `$mod+Shift+s` / `Print` | screenshot area / full |
| `$mod+Shift+c` | reload config |
| `$mod+Shift+r` | restart waybar |
| `$mod+Shift+e` | exit Sway |

## Controls
Everything is reachable from the bar:
- Wi-Fi: nm-applet in the tray
- Bluetooth: blueman in the tray
- Audio: click the volume module for pavucontrol, scroll to change volume
- Brightness: scroll on the brightness module, or the keyboard keys
- Power profile and battery: shown in the bar
- Displays: the monitor icon opens wdisplays

## Monitors
`kanshi/config` matches monitors by make/model/serial, not by connector name,
since connector names change between boots. Unknown monitors fall into the
`unknown-external` profile and are enabled at their preferred mode
automatically. To add a permanent profile for a new monitor, read its
description with:
```bash
swaymsg -t get_outputs | grep -E 'Output|make|model|serial'
```
Changes made in wdisplays are temporary until written to the kanshi config.

## Hybrid GPU
`session/sway-session` makes Sway render on the Intel iGPU and use the NVIDIA
GPU only to drive the HDMI port. This needs the NVIDIA driver matching the
running kernel (`nvidia-smi` must work) and `nvidia-drm.modeset=1` on the
kernel command line.

## Testing without logging out
```bash
sway -C                       # validate the config
WLR_BACKENDS=wayland sway     # run nested inside the current session
```
