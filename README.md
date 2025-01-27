# ROS POS
A virtual POS for retail, built in ROS.

## Guide
1. make a ROS workspace with a /src directory
2. clone the contents of this repo the /src of the workspace
3. from the workspacer root directory, run `colcon build`
4. source the overlay `. install/setup.bash`
5. `ros2 run pos service` # opens up the POS GUI
6. new terminal, source the overlay
7. `ros2 run pos card_reader` # opens a mock card reader
8. new terminal, source the overlay
9. `ros2 run pos scanner` # opens a mock UPS/qrcode scanner

### nota bene
To use a Python package through `pip` with `colcon`, just add the pip package name to the `install_requires` line in `setup.py`. This is used in the case of mySQL. (Maybe there's a better option.)

