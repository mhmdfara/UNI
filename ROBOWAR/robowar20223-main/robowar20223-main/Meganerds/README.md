# Documentation:
Welcome to the world of Jetson Nano Robotics, where cutting-edge technology meets the thrill of autonomous fighting robots. In a landscape where robotics and AI merge to create combat machines, our mission is to empower you with the tools and knowledge needed to build, control, and unleash the power of your battle-ready robots.

The Jetson Nano, developed by NVIDIA, is a powerful, energy-efficient AI platform that opens up a world of possibilities for robotics enthusiasts and professionals. In this project, we harness the Jetson Nano's computational prowess and flexibility to create a control system that brings your fighting robots to life with unprecedented intelligence and autonomy.

By Santeri, Henri, Natalija and Mattis

## First setup:
Here we present the progress we archieved during the project chronologically by presenting the challenges and solutions we found.

### Reading the SD card
*Challenge:* - SD card not showing up in the reader <br />
*Solution:* - In the disc manager we deleted the corrupted portion and created a new volume <br />
https://www.cleverfiles.com/howto/fix-sd-card-not-showing-up.html#assign_letter
![alt text](https://github.com/SAMKroboWars/robowar20223/blob/main/Meganerds/materials/4.png?raw=true "formatting")   


### Flashing the Jetson Nano developer kit SD card image
*Challenge:* - Bring the image to the SD card <br />
*Solution:* - Use BalenaEtcher <br />
(start etcher -> choose the sd card -> choose the nvidia linux image -> Done)

### Configuring USB to TTL connection
*Challenge:* - Finding the correct serial connections for the TTL <br />
*Solution:* 
 - Sexy schematics https://ftdichip.com/wp-content/uploads/2020/08/DS_UMFT234XF.pdf <br />
 ![alt text](https://github.com/SAMKroboWars/robowar20223/blob/main/Meganerds/materials/1.png?raw=true "schematics")
 - and a youtube tutorial: https://www.youtube.com/watch?v=Kwpxhw41W50 <br />

### Accessing Jetson console
*Challenge:* - Getting access to the Jetson console <br />
*Solution:*  - Looking in to the Windows Device Manager/Ports to get the COM number and putting it to Putty (https://www.putty.org/)
https://github.com/SAMKroboWars/robowar20223/blob/MegaNerds/materials/images/2.png?raw=true
![alt text](https://github.com/SAMKroboWars/robowar20223/blob/main/Meganerds/materials/2.png?raw=true "PuTTY")

### Serial port in wrong mode
*Problem:* The serial port was in the wrong mode <br />
*Solution:* <br />
-> Boot linux from usb stick <br />
-> put sd card into the reader <br />
-> open the files on the sd card <br />
-> locate /boot folder <br />
-> inside boot is another folder called ”linux something” <br />
-> open “linuxsomething”.conf with a text editor <br />
-> locate part “console=xxxx0” change to “console=xxxx1” <br />

### WIFI connection
*Problem:* We need a wifi connection <br />
*Solution:* After trying a few different approaches including creating a hotspot with the phone, the actual solution was to connect to the SAMK-LAB4 wifi

### Basic downloads and installations:
*Problem:* Some packages are not installed or up to date <br />
*Solution:* Install and update all needed packages including: 
- ros melodic 
- python 

### Configuring a hostname
*Problem:* The IP adress could be changing <br />
*Solution:* Configurating a hostname
![image](https://github.com/SAMKroboWars/robowar20223/blob/main/Meganerds/materials/3.png?raw=true)

### SSH connection
*Problem:* We need a ssh connection to get rid of the cable. <br />
*Solution:* 
```bash
ssh jetson@meganerds
```

### Old Ubuntu version?
*Problem:* Ubunto 18.04 installed -> ros melodic only supports python 2 <br />
*Solution:* We found a git repository for the ubuntu 20.04 image and how to make it work on the jetbot <br />
https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image/blob/main/README.md <br />
(of course after that we had to do all the previous steps again, <br />
(but OpenCV, Pytorch, TensoFlow, Python, TorchVision, TensorRT, TeamViewer and Jtop were allready pre installed.) <br /><br />

*Additional problem:* The partition was too small for all the packages <br />
*Solution:* Enlarge the partition to 116 GB
```bash  
sudo parted /dev/sdX  # Replace /dev/sdX with your actual disk identifier <br />
(parted) resizepart <partition_number> <new_size>  # Replace <partition_number> with the partition number of the last 
                                                   # partition and <new_size> with +31.3GB to use all the available space
(parted) quit

sudo resize2fs /dev/sdXY  # Replace /dev/sdXY with the last partition identifier (e.g., /dev/sda3)
```

## Working with a raspberry pico microcontroller
### get arduiuno
*Problem:* Get the right version of arduino on the jetson
*Solution:* Searched for the right version (https://www.arduino.cc/en/software)
--> Linux ARM 64 bits --> downloaded + installed

### Adding the Raspberry Pi Pico to the Boards Manager
*Problem:* 
*Solution:* Enter the following URL into the “Additional Boards Manager URLs” field:
--> https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json

- Open the Boards Manager. Go to Tools > Board > Boards Manager…
- Search for “pico” and install the Raspberry Pi Pico/RP2040 boards. (3.6 Version)
- Now, if you go to Tools > Board, there should be a selection of Raspberry Pi Pico boards.

Go to Tools > Board and select the Raspberry Pi Pico model you’re using—Pico or Pico W (wireless support).

As an example, we’ll upload the classic Blink LED sketch. Go to File > Examples > 1. Basic > Blink.

--> Problem: we didn't find the Serial port..
--> Solution --> wrong usb to usb-c cable
https://randomnerdtutorials.com/programming-raspberry-pi-pico-w-arduino-ide/

Now make arduino library
$ cd Arduino/libraries/
$ rosrun rosserial_arduino make_libraries.py .


### Adding the Teensy to the Boards Manager
*Problem:* 
*Solution:* Enter the following URL into the “Additional Boards Manager URLs” field:
--> https://www.pjrc.com/teensy/package_teensy_index.json

- Open the Boards Manager. Go to Tools > Board > Boards Manager…
- Search for “teensy” and install the Teensy Board. (lates version Version)
- Now, if you go to Tools > Board, there should be a selection of Raspberry Pi Pico boards.




## Working with the skript on moodle:
first of all: start roscore <br><br>

stop rosserial if running <br>
Upload the code (choose right serial/ teensy port) <br><br>
   
reconnect the pico (teesy doesn't need to be restarted)<br>
   
rosrun rosserial_python serial_node.py _port:=/dev/serial/by-id/usb-Raspberry_Pi_Pico_E4675468E7380923-if00 <br>
rosrun rosserial_python serial_node.py _port:=/dev/serial/by-id/usb-Teensyduino_USB_Serial_6902610-if00 <br>
(alternative: rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0      -       check first if the COM port in the /dev folder)
       
rostopic pub -r10 /left_wheel_cmd_topic std_msgs/Float64 "data: 120"


## Working on our drill script with the IBT_2 h-bridge
enablespin - splitted -> both have to be 1 to work 


## Tiny Screen
GND - GND <br>
VCC - 3.3V <br>
SCL - 5 <br>
SDA - 3 <br>
RES - 29 <br>
DC - 31 <br>
CS - 32 <br>
BLK - 33 (or 3.3V -> always on) <br>







