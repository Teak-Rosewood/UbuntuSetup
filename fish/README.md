# Fish Shell Configuration
### Cloning Repository

```
git clone https://github.com/Teak-Rosewood/UbuntuSetup.git
cd UbuntuSetup
```
### Installing and setting up the Fish Shell

installing fish

```
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt update
sudo apt install fish 
```

installing oh-my-fish

```
curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
curl -sL https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install.sha256 | shasum -a 256 --check
```
setting up theme
```
omf install edan
```
setting up configuration
```
cp -r fish/ ~.config/fish/
```
if fish shell has to be started whenever oepning terminal add `exec fish` to `.bashrc`