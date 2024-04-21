# Ubuntu General Configurations

## Initial Setup
### Updating and Upgrading Ubuntu 
```bash
sudo apt update
sudo apt upgrade
sudp apt install snap
sudo apt install python3
sudo apt install curl
```
### Installing Battery Manager
we will be using TLP for battery management
```bash
sudo apt install tlp tlp-rdw
systemctl enable tlp.service
sudo tlp start
```
### Install Lunar Vim
Install Neo Vim from Source
```
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
sudo rm -rf /opt/nvim
sudo tar -C /opt -xzf nvim-linux64.tar.gz
```
Add `set PATH "$PATH:/opt/nvim-linux64/bin"` to you `.bashrc` or `config.fish`
```bash
LV_BRANCH='release-1.3/neovim-0.9' bash <(curl -s https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.sh)
```

### Git Setup and Repository Cloning
```bash
sudo apt install git
git clone https://github.com/Teak-Rosewood/UbuntuSetup.git
cd UbuntuSetup
```

## Installing specific packages

### Miniconda
To install a different version or architecture of Miniconda for Linux, change the name of the .sh installer in the wget command.
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```
After installing, initialize your newly-installed Miniconda. The following commands initialize for bash and zsh shells:
```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
To use conda with fish shell, run the following in your terminal:
Add conda binary to $PATH, if not yet added:
```bash
fish_add_path <conda-install-location>/condabin
```
Configure fish-shell:
```bash
conda init fish
```

### Node Version Manager (NVM)
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```
### Docker

First uninstall any dependencies
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```
set up repository 
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

install the latest version
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

set docker to run without sudo
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# Test 
docker run hello-world
```
### Discord
```bash
sudo snap install discord
```
### Spotify
```bash
sudo snap install spotify
```
### Visual Studio Code
```bash
sudo snap install code --classic
```