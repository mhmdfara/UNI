#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float64

def generate_biased_random(min_backward, max_backward, min_forward, max_forward):
    # This function will generate a random number with a higher chance of it being positive.
    if random.random() < 0.3:  # 30% chance to move backward
        return random.uniform(min_forward, max_forward)
    else:  # 30% chance to move backward
        return random.uniform(min_backward, max_backward)

def random_movement():
    rospy.init_node('random_robot_mover', anonymous=True)

    # Publishers for robot1
    weapon_pub_r1 = rospy.Publisher('/robot1/weapon_velocity_controller/command', Float64, queue_size=10)
    wheel_l_pub_r1 = rospy.Publisher('/robot1/wheel_l_velocity_controller/command', Float64, queue_size=10)
    wheel_r_pub_r1 = rospy.Publisher('/robot1/wheel_r_velocity_controller/command', Float64, queue_size=10)

    # Publishers for robot5
    wheel_bl_pub_r5 = rospy.Publisher('/robot5/wheel_bl_velocity_controller/command', Float64, queue_size=10)
    wheel_br_pub_r5 = rospy.Publisher('/robot5/wheel_br_velocity_controller/command', Float64, queue_size=10)
    wheel_fl_pub_r5 = rospy.Publisher('/robot5/wheel_fl_velocity_controller/command', Float64, queue_size=10)
    wheel_fr_pub_r5 = rospy.Publisher('/robot5/wheel_fr_velocity_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(1) # 1 Hz

    while not rospy.is_shutdown():
        # Biased random values for robot1's wheels with increased forward speed
        random_wheel_l_vel_r1 = generate_biased_random(-1.5, 0.0, 0.0, 5.0)  # Increased max speed to 3.0
        random_wheel_r_vel_r1 = generate_biased_random(-1.5, 0.0, 0.0, 5.0)

        # Biased random values for robot5's wheels with increased forward speed
        random_wheel_bl_vel_r5 = generate_biased_random(-1.5, 0.0, 0.0, 5.0)
        random_wheel_br_vel_r5 = generate_biased_random(-1.5, 0.0, 0.0, 5.0)
        random_wheel_fl_vel_r5 = generate_biased_random(-1.5, 0.0, 0.0, 5.0)
        random_wheel_fr_vel_r5 = generate_biased_random(-1.5, 0.0, 0.0, 5.0)

        # Publish the random values for robot1
        weapon_pub_r1.publish(random.uniform(-1.0, 1.0))  # Random weapon velocity for robot1
        wheel_l_pub_r1.publish(random_wheel_l_vel_r1)
        wheel_r_pub_r1.publish(random_wheel_r_vel_r1)

        # Publish the biased random values for robot5 with increased speed
        wheel_bl_pub_r5.publish(random_wheel_bl_vel_r5)
        wheel_br_pub_r5.publish(random_wheel_br_vel_r5)
        wheel_fl_pub_r5.publish(random_wheel_fl_vel_r5)
        wheel_fr_pub_r5.publish(random_wheel_fr_vel_r5)

        rate.sleep()

if __name__ == '__main__':
    try:
        random_movement()
    except rospy.ROSInterruptException:
        pass
