This guide will help you with the steps to connect the OLED display same things are mentioned in this document:
https://jetsonhacks.com/2019/12/03/adafruit-pioled-on-jetson-nano/

First thing is to clone the repository:
	git clone https://github.com/JetsonHacksNano/installPiOLED
	cd installPiOLED


You need to install dependencies, these installs are handled by the installPIOled script, run:
	./installPiOLED

Go to pioled:
	cd pioled

Next, you need to change the "stats.py" file inside the repository that you cloned.
The service is running stats.py file that fetches the IP address.

You need to change a couple of things:
1. Change "eth0" on rows 114 and 115 to "wlan". Row 114 is just a string to print "wlan" to the screen. Row 115 actually tells the program to look for the IP address of a network interface named "wlan".
2. You may need to change row 69 "i2c_bus" value from 1 to 0 depending on your connection to the Jetson board. If you get errors when running the createService script, you can try to change this bus if you are not sure what bus you are using.

After the changes, you can run the the "stats.py" or create a service to run when the device starts:
	sudo python3 stats.py

Or to create the service:
	./createService

If you want to change some of the contents of the "stats.py" file after you have created the service, you need to remove the wheel generated for it:
	sudo pip3 uninstall pioled-1.0-py3-none-any.whl

After this you can make modifications to the "stats.py", create the service again and have the changes on the OLED display.







