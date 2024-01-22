#!/usr/bin/env python

import rospy
import threading
from std_msgs.msg import Float64
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Twist
import math
import tensorflow as tf
import tf.transformations
import random


def calculate_velocity_to_target(current_position, target_position, max_speed=2.0):
    dx = target_position.x - current_position.x
    dy = target_position.y - current_position.y
    distance = math.sqrt(dx**2 + dy**2)
    if distance < 0.1:  # If close to the target, stop
        return 0.0, 0.0

    # Normalize vector and scale to max speed
    vx = (dx / distance) * max_speed
    vy = (dy / distance) * max_speed
    return vx, vy

def quaternion_to_euler(orientation):
    quaternion = (
        orientation.x,
        orientation.y,
        orientation.z,
        orientation.w
    )
    euler = tf.transformations.euler_from_quaternion(quaternion)
    return euler  # in radians

def get_heading_to_target(robot_position, target_position):
    return math.atan2(target_position.y - robot_position.y,
                      target_position.x - robot_position.x)

def model_state_callback(data):

    try:
        robot5_index = data.name.index('robotti_5')
        robot5_position = data.pose[robot5_index].position
        robot5_orientation = data.pose[robot5_index].orientation

        # Convert quaternion to Euler angles
        _, _, robot5_yaw = quaternion_to_euler(robot5_orientation)

        # Find the first object that is not 'robotti_5' and has non-zero velocity (indicating it might be a robot)
        target_index = next(i for i, (name, twist) in enumerate(zip(data.name, data.twist))
                            if i != robot5_index and (twist.linear.x != 0 or twist.linear.y != 0 or twist.linear.z != 0))
        target_position = data.pose[target_index].position

        target_heading = get_heading_to_target(robot5_position, target_position)

        # Determine the required angular velocity to turn towards the target
        angle_diff = target_heading - robot5_yaw
        print(angle_diff, " Angle_diff")
        print(target_heading, "target heading")
        print(robot5_yaw, "robo5 yaw")

        # Control logic to turn and move robotti_5 towards the target
        # Here, you need to determine how to use the angle_diff to control your robot's wheels
        # This will depend on your robot's specific kinematics and might require some tuning
        # Example (you will need to adjust the values and logic based on your robot's design):
        # Define the range for random values
        min_random_value = -6
        max_random_value = -2

        if angle_diff > 0.5:
            wheel_bl_value = 1
            wheel_br_value = -1
            wheel_fl_value = 1 
            wheel_fr_value = -1 

            wheel_bl_pub.publish(wheel_bl_value)
            wheel_br_pub.publish(wheel_br_value)
            wheel_fl_pub.publish(wheel_fl_value)
            wheel_fr_pub.publish(wheel_fr_value)

        elif angle_diff < -0.5:
            wheel_bl_value = -1 
            wheel_br_value = 1 
            wheel_fl_value = -1 
            wheel_fr_value = 1 

            wheel_bl_pub.publish(wheel_bl_value)
            wheel_br_pub.publish(wheel_br_value)
            wheel_fl_pub.publish(wheel_fl_value)
            wheel_fr_pub.publish(wheel_fr_value)

        else:
            wheel_bl_value = -4 + random.uniform(min_random_value, max_random_value)
            wheel_br_value = -4 + random.uniform(min_random_value, max_random_value)
            wheel_fl_value = -4 + random.uniform(min_random_value, max_random_value)
            wheel_fr_value = -4 + random.uniform(min_random_value, max_random_value)

            wheel_bl_pub.publish(wheel_bl_value)
            wheel_br_pub.publish(wheel_br_value)
            wheel_fl_pub.publish(wheel_fl_value)
            wheel_fr_pub.publish(wheel_fr_value)
            
    except (ValueError, StopIteration) as e:
        print("Exception in callback: ", e)


def listener():
    rospy.Subscriber("/gazebo/model_states", ModelStates, model_state_callback)

if __name__ == '__main__':
    rospy.init_node('robot5_control_and_monitor', anonymous=True)

    global wheel_bl_pub, wheel_br_pub, wheel_fl_pub, wheel_fr_pub
    wheel_bl_pub = rospy.Publisher('/robot5/wheel_bl_velocity_controller/command', Float64, queue_size=10)
    wheel_br_pub = rospy.Publisher('/robot5/wheel_br_velocity_controller/command', Float64, queue_size=10)
    wheel_fl_pub = rospy.Publisher('/robot5/wheel_fl_velocity_controller/command', Float64, queue_size=10)
    wheel_fr_pub = rospy.Publisher('/robot5/wheel_fr_velocity_controller/command', Float64, queue_size=10)

    listener_thread = threading.Thread(target=listener)
    listener_thread.start()
    rospy.spin()
