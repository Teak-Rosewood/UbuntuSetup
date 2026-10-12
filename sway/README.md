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
| `$mod+Shift+d` | display menu: eye saver, re-apply docked layout, display GUI |
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
- Displays: the monitor icon opens wdisplays; `$mod+Shift+d` has the display menu

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

### Shared monitor (switching its input between two laptops)
The Acer XV272K is shared with a second laptop. Switching its input away often
does not make the kernel see a disconnect, so Sway keeps driving a dead link and
the monitor comes back black or stuck at 60Hz. Three pieces handle it:
- `scripts/dock-watch` (started from `config`) asks the monitor which input is
  active over DDC/CI. On another input it disables the output, so windows move to
  the laptop panel. When the input is back it re-enables the output and sends
  workspaces 9 and 10 home. `HOME_INPUT` at the top is this laptop's input
  (`ddcutil getvcp 60` while the monitor shows this laptop; HDMI-1 is `x11`).
- `scripts/dock-apply` brings the output up at 60Hz and then raises it to 160Hz,
  because enabling straight at 160Hz is rejected (`Atomic commit failed: Invalid
  argument`). It retries and falls back to 60Hz. kanshi's `docked` profile also
  runs it, since 160Hz is no longer in the profile.
- `workspace ... output` rules in `config` give workspaces 9 and 10 the monitor
  as home and the laptop panel as fallback.

Needs `ddcutil` and DDC/CI enabled in the monitor's on-screen menu. Logs:
```bash
journalctl --user -t dock-watch -t dock-apply -b
```
If the monitor ever shows nothing, `$mod+Shift+d` then "Re-apply docked layout".
`swaymsg reload` resets the monitor's scale; run the same menu entry afterwards.

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
