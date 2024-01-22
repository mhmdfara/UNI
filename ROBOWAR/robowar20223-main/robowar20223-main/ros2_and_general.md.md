# General about ROS1 and ROS2
The last distribution release of ROS1 is Noetic Ninjemys, release date 23. May 2020, and the support duration is 5 years ending in May 2025.

ROS2 currently (October 2023) has 2 supported releases:
- Humble Hawksbill (5 years), Release date: 23.  May 2022,  EOL date: May 2027
- Iron Irwini (1.5 years), Release date: 23.  May 2023,  EOL date: November 2024
- more ROS2 releases to come after these two

source: https://en.wikipedia.org/wiki/Robot_Operating_System

# ROS1 Noetic/Ubuntu installation on Apple silicon
First you need a virtualization platform like VMware.

It seems e.g. https://cdimage.ubuntu.com/releases/focal/release/ provides only a server image. If you don't find a desktop image for arm Ubuntu 20.04, you can always download the server image and upgrade Gnome desktop to it

Ubuntu 20.04, the end of standard support is April 2025, and end of life is April 2030. [https://wiki.ubuntu.com/Releases]

After that follow instructions on http://wiki.ros.org/noetic/Installation/Ubuntu.
# ROS2 installation (Humble)
Similarly you need a virtualization platform like VMware for installing Ubuntu, especially if you are using Apple silicon (or try installing ROS2 natively on MacOs).

Ubuntu 22.04 long term support (LTS), the end of standard support is April 2027, and end of life is April 2032. [https://wiki.ubuntu.com/Releases]

Ubuntu 22.04 can be downloaded from https://cdimage.ubuntu.com/jammy/daily-live/pending/ be sure to choose your architecture correctly (arm64 or amd64).

The installation instructions for ROS2 are in https://docs.ros.org/en/humble/index.html.
Supported platforms for ROS2 humble:
- Ubuntu 22.04 (Jammy Jellyfish)
- Windows 10
- RHEL9 (Red Hat, Linux)

# Useful terminal commands to check versions, distributions etc:
these will probably also work on 20.04, 22.04 and MacOs terminal as well.
- arch
	- tells your architecture of your computer/virtual machine
- lsb_release -a 
	- tells your ubuntu version
- printenv | grep -i ROS
	- prints info of ROS version, Python version and Path informaion
- echo $ROS_DISTRO
	- prints your ROS distribution name

# ROS1  / ROS 2 bridge
links:
- https://roscon.ros.org/2019/talks/roscon2019_bridging_ros1_to_ros2.pdf
- https://www.youtube.com/watch?v=sJLvv1xtjSM
- https://github.com/ros2/ros1_bridge
