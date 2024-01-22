# How to use the raspberry Pi Pico
The Raspberry Pi Pico is a microcontroller
It can be used as an arduino micro controller

You can use code in Python or in C++ but here we will use C++ (only in the last step)

## IDE
There is different IDE like the Arduino IDE or Thonny
There is a lot more documentation and informations on internet for arduino IDE so we will use this one so if we have an issue it's easier to find how to solve the problem

You can download the Arduino IDE on you laptop here : https://www.arduino.cc/en/software
When installed you can run it

How to plug the Raspberry, install the board manager, upload anduse the serial are explain here if you prefere a video we found instead of reading those instructions : https://youtu.be/IZKpCz6LEdg?si=q64kaoJZtHePYGRq

### Plug the Raspberry to the laptop
You can plug the Raspberry Pi Pico while keeping the button *"BOOTSEL"* pressed if you want to import code in it

### board manager
> [!Note]
> (You can go in the "Select Board" on the top left of the screen but if you select the port and the Raspberry Pi Pico Board, it will ask you to install the board manager but it never worked for us but if it work for you, you may don't need the next steps)

You will need to download the Board manager, to do so you go in File>Preferences
In the *Settings* part there is ***"Additional boards manager URL"*** you past this URL in it : https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
Then press OK

Now go in ***Tools>Board>Board Manager*** (or the button on the left between the "skethbook" and "library manager")
Here Type "Raspberry" in the searchbar and install the "Rapberry Pi Pico/RP2040"

### Upload code in the Raspberry Pi Pico
When you plug it you can go in the the box aside the buttons "verify", "Upload" and "Debug" Here you can select "other Board and Port"

Here you can select the *port* where the Raspberry is plugged and also the *Board* type (search "Raspberry" and take the one taht tell "Raspberry Pi Pico - Raspberry Pi Pico/RP2040" when you have the mouse hover it) then click *OK*

Now you can code and verify it with the button on the top left and if everything is right you can Upload it, that will upload the code in the Raspberry

When the code is Uploaded it should start on the Raspberry
> [!NOTE]
> If you want a code that run automatically when the raspberry start, you should name it *main*

### Use serial Monitor on the laptop
If the Raspberry Pi Pico run a code that should send data/message or recieve input you can see or enter those in the Serial Monitor and Serial Plotter

You can find them in ***Tools>Serial Monitor*** and ***Tools>Serial Plotter***

## Using the ROS libraries
You need to download the "rosserial" library in the IDE, to do so, go in ***Sketch>Include libray>Manage library...***
Here you search "rosserial" and install the "Rosserial Arduino Library"

Now you can use the ROS library by importing it (`#include <ros.h>` in C++)

more informations here : https://maker.pro/arduino/tutorial/how-to-use-arduino-with-robot-operating-system-ros
