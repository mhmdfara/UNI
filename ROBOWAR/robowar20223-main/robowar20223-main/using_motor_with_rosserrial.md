# how to use rosserial to use a motor connected on a raspberry pi pico

## softwares

firstly you need to have an IDE like arduino IDE or teensy to code for the raspberry Pi pico (we use arduino IDE)
You code it on another computer, your laptop or anything, not on the Jetson Nano

## installations

You need to have rosserial and rosserial-arduino
We use ros melodic so we used those commands :

``` bash
sudo apt-get install ros-melodic-rosserial-arduino

sudo apt-get install ros-melodic-rosserial
```

## access to the raspberry as a node

Firstly you need to run `roscore` in another terminal

To start the ros node you can use this command (when the raspberry is plugged) :

``` bash
rosrun rosserial_python serial_node.py _port:=/dev/serial/by-id/<usb-id>
```

you replace `<usb-id>` by the one you can find in `/dev/serial/by-id`

If you get an *error* which says that you can't acces or that the permission is denied you need to get you user in the group of **dialout** to do so juste enter this command

```bash
sudo adduser $USER dialout
```

> [!NOTE]
> Replace $USER by your user

## commands to see the nodes and topic running

You can run those after the previous steps to be sure everything is running

``` bash
rosnode list
```

## raspberry's code

We did modify the code that you can find on the moodle in *[ROS serial]*
The code use the topic *'motor_publisher'*

To use it use the command `rostopic pub /motor_publisher std_msgs/Float64 "data: <value>"` in the terminal, you just need to replace \<value>

- value = 0 ==> motor stops
- value < 0 ==> motor goes backward
- value > 0 ==> motor goes frontward

the value itself is the velocity (from 0 to 255)
If the value is to low, the motor struggles to work

> [!NOTE]
> (for us) to start the motor, the min value is 130 but if it is started yet you can go lower ==> the treshold

> [!NOTE]
> The code make the motor running at the setup to be sure it works
> The led blinks at the setup and each time the raspberry recieve a message from the *'motor_publisher'*

```c++
/* Maintainer: Toni Aaltonen @ toni.aaltonen@samk.fi
 * rosserial Subscriber motor driver
 * 
 * CLAV : modified version of the first code
 * we use a raspberry Pi pico
 * we publish on the ros topic 'motor_publisher"
 *
 * here is an exemple of the command to use were the 0.0 can be change by another value
 * rostopic pub /motor_publisher std_msgs/Float64 "data: 0.0"
 * 
 * if the value is to low, the motor struggles to work so we chosed this treshold
 * to start the motor, the min value is 130 but if it is started yet you can go lower ==> the treshold
 */

#include <ros.h>
#include <std_msgs/Float64.h>

int forwardPin = 11;
int backwardPin = 12;
int motorPWMPin = 13;
int ledPin = 25;

ros::NodeHandle nh;

void velocityCb( const std_msgs::Float64 &msg){
  // the values for analogWrite go from 0 to 255
  int value = int(msg.data);
  if(value > 255) {
    value = 255;
  } else if (value < -255) {
    value = -255;
  }

  // if the value is to low, the motor struggles to work so we chosed this treshold
  // to start the motor, the min value is 130 but if it is started yet you can go lower ==> the treshold
  int treshold = 55;

  // we recieve a number between -255 and 255 and 0 makes the motor stop
  if ( value > 0 ) {    
    if(value < treshold) {
      value = treshold;
    }
    analogWrite(motorPWMPin, value);
    digitalWrite(backwardPin, LOW);
    digitalWrite(forwardPin, HIGH);
  } else if (value == 0) {
    analogWrite(motorPWMPin, 0);
    digitalWrite(backwardPin, LOW);
    digitalWrite(forwardPin, LOW);
  } else {
    if(value > -treshold) {
      value = -treshold;
    }
    analogWrite(motorPWMPin, value * -1);
    digitalWrite(forwardPin, LOW);
    digitalWrite(backwardPin, HIGH);
  }
  digitalWrite(ledPin, HIGH);
  delay(5);
  digitalWrite(ledPin, LOW);  
}

ros::Subscriber<std_msgs::Float64> velSub("motor_publisher", &velocityCb);

void setup()
{
 
  nh.initNode();
  nh.subscribe(velSub);

  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);
  pinMode(motorPWMPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  
  digitalWrite(ledPin, HIGH);
  analogWrite(motorPWMPin, 140);
  digitalWrite(backwardPin, LOW);
  digitalWrite(forwardPin, HIGH);
  delay(1000);

  digitalWrite(ledPin, LOW);
  analogWrite(motorPWMPin, 0);
  digitalWrite(backwardPin, LOW);
  digitalWrite(forwardPin, LOW);
  delay(500);

  digitalWrite(ledPin, HIGH);
  analogWrite(motorPWMPin, 140);
  digitalWrite(backwardPin, HIGH);
  digitalWrite(forwardPin, LOW);
  delay(1000);

  analogWrite(motorPWMPin, 0);
  digitalWrite(backwardPin, LOW);
  digitalWrite(forwardPin, LOW);
  digitalWrite(ledPin, LOW);
}
void loop()
{
  nh.spinOnce();
  delay(1);
}
```
