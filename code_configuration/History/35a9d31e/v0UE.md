# Mars Rover Manipal, IRC 2023, Navigation Stack
Mars Rover Manipal's Autonomous Expedition stack for International Rover Challenge 2023, It deals with the automation of the rover to detect and follow arrows and cons while recording their GPS coordinates

The current version targets [ROS Noetic Ninjemys](http://wiki.ros.org/noetic/Installation/) distribution and was mainly developed and tested on [Ubuntu 20.04 Focal Fossa](https://releases.ubuntu.com/20.04/).
 
## Prerequisites 

1. [Ubuntu 20.04 Focal Fossa](https://releases.ubuntu.com/20.04/)
2. [ROS Noetic Ninjemys](http://wiki.ros.org/noetic/Installation/)
3. [Ultralytics](https://ultralytics.com)
4. [OpenCV](https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html) 
5. [CUDA](https://developer.nvidia.com/) 
6. [ZED SDK](https://www.stereolabs.com/developers/release/)

The tools necessary to build this project can be installed with apt:
```
sudo apt-get install libgeographic-dev ros-noetic-geographic-msgs
sudo apt install python3-rosdep python3-catkin-tools
```

#### Installing JetsonGPIO
```
git clone git@github.com:pjueon/JetsonGPIO.git

cd JetsonGPIO
mkdir build && cd build
cmake ..
sudo make install

sudo mkdir /usr/local/include/JetsonGPIO
sudo mkdir /usr/local/lib/JetsonGPIO
```
add the .so and .h files to the specified folders 

#### Installing pigpio
```
wget https://github.com/joan2937/pigpio/archive/master.zip

unzip master.zip
cd pigpio-master
make
sudo make install

sudo mkdir /usr/local/include/pigpio
sudo mkdir /usr/local/lib/pigpio
```
add the .so and .h files to the specified folders 

#### Installing OpenCV from source 

```
sudo apt update && sudo apt install -y cmake g++ wget unzip

wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip

unzip opencv.zip
unzip opencv_contrib.zip

mkdir -p build && cd build

cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x

cmake --build .
``` 

#### Installing Ultralytics 

```sh
sudo apt install pip
pip3 install ultralytics
``` 
 
## Building 
 
To clone the repository:
```sh
git clone git@github.com:Teak-Rosewood/MRM-IRC2023-NavStack.git
```
Use the `rosdep` tool to install any missing dependencies. If you are running `rosdep` for the first time, you might have to run:
```sh
sudo rosdep init
```
first. Then, to install the dependencies, type:
```sh
rosdep update
sudo apt update
rosdep install --rosdistro noetic --from-paths src -iy
```
Now, use the `catkin` tool to build the workspace:
```sh
catkin config --extend /opt/ros/noetic
catkin build
source devel/setup.bash
```

## Running the Navigation Stack 

#### Setting up ROS Master URI
add these lines to the .bashrc of the processors 
```
export ROS_MASTER_URI=http://IP_OF_MASTER:11311
export ROS_HOSTNAME=IP_OF_PROCESSOR
```

#### Nodes running on the Jetson Xavier NX

#### Nodes running on the Raspberry Pi  

## Setting up docker 

Seting up nvidia to docker connection

```
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd
```
Running the docker
```
docker run -it --rm -v $(pwd):/workspace --runtime=nvidia -w /workspace -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY jetson
```


