# Path Planning Optimization using Bezier Curves
A new approach to path planning for heavy robots in warehouses
## Prerequisites
- Gazebo Fortress LTS
- ROS 2 Humble LTS

## Building the workspace

```sh
# Pulling the repository 
git clone git@github.com:Teak-Rosewood/bezier-curve-path-planning.git
cd bezier-curve-path-planning

# building the workspace 
colcon build
```
## Launching the simulation 
go into the workspace directory
```sh
source install/setup.bash
ros2 launch roverrobotics_gazebo 4wd_rover_gazebo.launch.py
```