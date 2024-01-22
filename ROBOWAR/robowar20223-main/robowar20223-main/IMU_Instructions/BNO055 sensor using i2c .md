How to use BNO055 sensor using i2c 
communication to generate IMU data?

INSTRUCTIONS RETRIEVED FROM:
https://automaticaddison.com/how-to-publish-imu-data-using-ros-and-the-bno055-imu-sensor/

1. You need to set up your Jetson Nano with ROS
• Instruction for installing ROS on Jetson nano found HERE. (Start from Step 2).
2. Connect the pins correctly (instructions in slide 5)
3. Turn on Jetson Nano
4. Open a terminal window
5. Type following command to verify that you can see the BNO055:
• sudo i2cdetect -r -y 1
You should see:<img src="/IMU_Instructions/sudo i2cdetect -r -y 1.png" alt="sudo i2cdetect -r -y 1"/> 
6. Install the libi2c-dev library using following commands:
• sudo apt update
• sudo apt install libi2c-dev
7. Install the BNO055 ROS package:
• cd ~/catkin_ws/src
8. Remove any existing package named ‘ros_imu_bno055’:
• git clone https://github.com/dheera/ros-imu-bno055.git
9. Build the package
• cd ~/catkin_ws/
• catkin_make--only-pkg-with-deps imu_bno055
10. Open a new terminal window, and see if our package depends on other packages, type these commands. 
Ignore any error messages you see in the terminal:
• rosdep update
• rosdep check imu_bno055
11. Reboot your computer:
• sudo reboot<img src="/IMU_Instructions/IMU_Instructions.png"/>
12. Install the ROS IMU plugin so we can visualize the IMU data on rviz:
• sudo apt-get install ros-melodic-rviz-imu-plugin
13. Open a terminal window, and type:
• roslaunch imu_bno055 imu.launch
14. Open a terminal window and see the active topics:
• rostopic list
15. To see the imu data on the topic named /imu/data type:
• rostopic echo /imu/data
You should see something similar:<img src="/IMU_Instructions/imu_data-on_topic_named.png"/>
For the I2C connection, we will
only need to use 4 pins:
1. VDC (power- in this case 3.3v)
2. GND (ground)
3. SCL (clock)
4. SDA (data)<img src="/IMU_Instructions/Nana_BNO055.png"/>
These pins on the jetson nano 
(pins 1, 3, 5, and 6) will be
plugged into the corresponding
pins on the BMA220.<img src="/IMU_Instructions/I2C_Connection.png"/>
