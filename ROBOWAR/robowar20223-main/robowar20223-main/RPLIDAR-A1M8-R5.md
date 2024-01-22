# RPLIDAR On Jetson Nano

This file will attempt to guide yout through installing an RPLIDAR module on your Jetson Nano and setting it up for use in the Robot Operating System (ROS).

The exact models used in our test case were:

 - RPLIDAR: A1M8-R5
 - Jetson Nano: P3450
 - Robot Operating System: Ros-Melodic

Instructions closely follow those originally on this page: https://collabnix.com/getting-started-with-the-low-cost-rplidar-using-jetson/#:~:text=Connect%20the%20RPlidar%20to%20the%20Jetson%20Nano%3A%20Plug%20one%20end,Nano%20and%20power%20it%20up

This guide assumes you already have a working operating system and ROS installment on your device and that you have shell access to it.


## Connecting your RPLIDAR sensor

The connection method used here was a simple micro-USB interface. Simply connect the cables.


## Step 1. Clone the github repository for RPLIDAR
`git clone  https://github.com/robopeak/rplidar_ros.git

cd ..`

## Step 2. Run catkin_make to compile your workspace
`catkin_make`

## Step 3. Source your environment

`source devel/setup.bash`

## Step 4. Run roscore

In another terminal, run roscore:

`roscore`

## Step 5. Attempt to launch the Node

`roslaunch rplidar_ros view_rplidar.launch`

### USB Privilege errors

We ran in to an issue with the USB device not having the correct privileges for ROS to be able to utilize it. The exact error message was as follows:

>[ERROR] [1696415889.435554015]: Error, cannot bind to the specified serial port /dev/ttyUSB0.
>[rplidarNode-1] process has died [pid 16295, exit code 255, cmd /home/v2k2/catkin_ws/devel/lib/rplidar_ros/rplidarNode __name:=rplidarNode __log:=/home/v2k2/.ros/log/a3bee638-629f-11ee-be4c-a0d768102991/rplidarNode-1.log].

In case you run in to this, or a similar issue, you will have to make sure the USB port has the correct privileges:

`sudo chmod 777 /dev/ttyUSB0`

It's plausible, but unlikely, that your device is another USB,

### Step 7. Verify Topic & Data are Running Correctly

Once the node is running, you should be able to see a new ROS topic. In our case it was called 'scan'. To see active topics, use the following command:

`rostopic list`

Then to listen to the data in that topic you can simply type:

`rostopic echo scan`

You should now see the data in your terminal.





