# ROS POS
A virtual POS for retail, built in ROS.

## Guide
1. make a ROS workspace with a /src directory
2. clone the contents of this repo's /src into a /src of the workspace
3. from the workspacer root directory, run `colcon build`
4. source the overlay `. install/setup.bash`
5. `ros2 run pos service`
6. new terminal, source the overlay
7. `ros2 run pos card_reader`
8. new terminal, source the overlay
9. `ros2 run pos scanner`
