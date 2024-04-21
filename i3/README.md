# i3 Configuration

## Prerequisites
### Initial installations
```bash
sudo apt -y install feh
sudo apt-get -y install arandr 
sudo apt-get -y install lxappearance 
sudo apt -y install picom 
sudo apt-get -y install blueman
```
installing basic neovim
```bash
sudo snap install nvim --classic
git clone https://github.com/LunarVim/Launch.nvim.git ~/.config/nvim
sudo apt install xsel # for X11
sudo apt install wl-clipboard # for wayland
pip install pynvim
npm i -g neovim
```

## Setup 

### Setting up i3 Menu 
```bash
sudo apt-get install rofi
cd ~/Documents
git clone https://github.com/Murzchnvok/rofi-collection.git
cd rofi-collection
mkdir ~/.config/rofi/themes
cp -r . ~/.config/rofi/themes/
```
### Setting up status bar 
```bash
pip install --user bumblebee-status
pip install netifaces
```
installing dependencies
```bash
# Spotify module 
pip install dbus-python
# Audio modules
pip install pulsectl
# Bluetooth
sudo apt install -y dbus
sudo apt install blueman-manager
# System Module 
sudo apt install python3-tk
# Fonts and icons
sudo apt install fonts-font-awesome
sudo apt-get install fonts-powerline
```
### Setting up i3 Lock 
```bash
sudo apt install autoconf gcc make pkg-config libpam0g-dev libcairo2-dev libfontconfig1-dev libxcb-composite0-dev libev-dev libx11-xcb-dev libxcb-xkb-dev libxcb-xinerama0-dev libxcb-randr0-dev libxcb-image0-dev libxcb-util0-dev libxcb-xrm-dev libxkbcommon-dev libxkbcommon-x11-dev libjpeg-dev

git clone https://github.com/Raymo111/i3lock-color.git
cd i3lock-color
./install-i3lock-color.sh

sudo apt -y install imagemagick

wget https://raw.githubusercontent.com/betterlockscreen/betterlockscreen/main/install.sh -O - -q | sudo bash -s system
```

### Setting up Touch Pad and other devices
we will be using xinput to configure the devices 

```
# List Devices
xinput list 

# List Props
xinput list-props <device-id>

# Set Props
xinput set-prop <device-id> <prop-id> <prop-value>
```
Once you have figured the props out add it to your i3 config file

## Common Editions 

### Executing on startup
```bash
exec $application_name # starting everytime laptop is restarted
exec_always $application_name # start everytime when logged in
```

### Making application start at specific workspace
Open a terminal and type the following:
```bash
xprop
```
Click on the desired application and note the class.
Add the following line to the i3 config file
```bash
assign [class = $second_string] $workspace_variable
```


