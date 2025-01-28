# ROS POS
A virtual POS for retail, built in ROS.

## Now with an Automatic Cashier

## Quickstart
1. make a ROS workspace with a /src directory
2. clone the contents of this repo the /src of the workspace
3. from the workspace root directory, run `colcon build`
4. source the overlay `. install/setup.bash`
5. `ros2 run pos service` # opens up the POS GUI
6. (optional) new terminal, source the overlay
7. `ros2 run pos card_reader` # opens a mock card reader
8. new terminal, source the overlay
9. `ros2 run pos scanner` # opens a mock UPS/qrcode scanner
10. new terminal, source the overlay
11. `ros2 run pos llmi` # starts the interface for the cashier agent (it will start scanning things)
12. new terminal, source the overlay
13. `ros2 run pos interface` # starts the input field to the LLM

In parallel, the cashier will be
A. scanning out items (a random batch from the items of `price_lookup.yaml`)
B. carry out comfortable dialogue with knowledge of its doing A.

### nota bene
To use a Python package through `pip` with `colcon`, just add the pip package name to the `install_requires` line in `setup.py`. This is used in the case of mySQL. (This N.B. will expire soon.)

