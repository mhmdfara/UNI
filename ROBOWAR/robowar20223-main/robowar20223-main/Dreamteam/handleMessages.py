#!/usr/bin/env python

import rospy
from my_ros_package.msg import MyCustomMessage  # Import your custom message
from std_msgs.msg import Bool, Float32  # Import Bool message for health status
from dataclasses import dataclass

@dataclass
class Sensor:
    sensor_data: Float32
    sensor_healthy: Bool = None

class SensorMonitor:
    def __init__(self):
        rospy.init_node('sensor_monitor', anonymous=True)
        self.sensor_data:MyCustomMessage = None
        rospy.Subscriber("/chatter", MyCustomMessage, self.callback)
        self.threshold = 1e-7
        self.sensors = []
    '''
    def callback(self, data):
        for sensor_reading in data:
            self.sensors.append(Sensor(sensor_data=sensor_reading))
            
        for sensor in self.sensors:
            self.check_sensor_health(sensor)
    '''
    def check_sensor_health(self, sensor:Sensor):
        
        if sensor.sensor_data < self.threshold:
            # Sensor data is not changing
            rospy.logwarn("Sensor data is not changing. Sensor may not be working.")
            sensor.sensor_healthy = False
        else:
            # Sensor data is changing
            rospy.loginfo("Received new sensor data.")
            sensor.sensor_healthy = True
            

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    sensor_monitor = SensorMonitor()
    sensor_monitor.run()
