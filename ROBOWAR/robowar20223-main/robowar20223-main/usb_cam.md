# Using a USB Camera With The Jetson Nano

We will be using the following package: https://github.com/ros-drivers/usb_cam

### 1.  Connect Your Camera

### 2. Make Sure The System Sees It
`ls /dev/video*`

You should see an output of the available video devices. Usually the default for the connected device will be video0, if no other video source exists.

### 3. Install Dependancy
`sudo apt update`

`sudo apt install libv4l-dev`

### 4. System Link for OpenCV
The package we're using was written on a debian base but in Jetpack, the installation path for OpenCV is slightly different so we need to tell the system where to find it instead:

`sudo ln -s /usr/include/opencv4/opencv2/ /usr/include/opencv`


### 5. Clone the repository and build
`cd *path to ros workspace / src*`

`git clone https://github.com/ros-drivers/usb_cam.git`

`cd ..`

`catkin_make`

### 6. Source your environment and run usb_cam
`source devel/setup.bash`

`roslaunch usb_cam usb_cam-test.launch`

you should now be able to see the topic name by running:
`rostopic list`


## Troubleshooting:

### User does not have the right group assigned:

It's possible that your user can not access video devices if they are not added to the video group. To add them, simply run:
`sudo usermod -a -G video *yourUsername* `

### Video device has wrong privileges:
Another possible reason why no program can access the data from your device. Attempt to fix by running:
`sudo chmod 660 /dev/video0`
Remember to change video0 to correspond with your actual device.
