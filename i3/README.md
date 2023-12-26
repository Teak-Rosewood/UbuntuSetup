# i3 Configuration

## Prerequisites
### Applications
1. discord
2. vscode 
3. whatsapp
4. [playerctl](https://github.com/altdesktop/playerctl/releases)
### Initial installations
```
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
```
sudo apt-get install rofi
cd ~/Documents
git clone https://github.com/Murzchnvok/rofi-collection.git
cd rofi-collection
mkdir ~/.config/rofi/themes
cp -r . ~/.config/rofi/themes/
```
### Setting up status bar 
```
pip install --user bumblebee-status
pip install netifaces
```
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

### Adding icons to workspace tabs
figure it out from this link:
[Font Awesome](https://github.com/FortAwesome/Font-Awesome/wiki)
