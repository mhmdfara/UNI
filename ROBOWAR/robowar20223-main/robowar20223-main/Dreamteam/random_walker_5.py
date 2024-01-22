#! /usr/bin/python3
import rospy, random, math
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import tf_conversions

def callback(data):
    vel_l_msg = Float64()
    vel_r_msg = Float64()
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y

    qx = data.pose.pose.orientation.x
    qy = data.pose.pose.orientation.y
    qz = data.pose.pose.orientation.z
    qw = data.pose.pose.orientation.w
    quaternio = (qx,qy,qz,qw)
    euler = tf_conversions.transformations.euler_from_quaternion(quaternio)
    theta = euler[2] # 0,1,2 & roll,pitch,yaw

    velocity_forward = 5
    turning_speed = 10

    marginal = 0.5 # 0.7
    side = 3

    vel_msg = Twist()

    if x > (side-marginal):
        if theta >= 0:
            vel_msg.angular.z = turning_speed
            vel_msg.linear.x = velocity_forward
        else:
            vel_msg.angular.z = -turning_speed
            vel_msg.linear.x = velocity_forward

    elif x < marginal:
        if theta >= 0:
            vel_msg.angular.z = -turning_speed
            vel_msg.linear.x = velocity_forward
        else:
            vel_msg.angular.z = turning_speed
            vel_msg.linear.x = velocity_forward

    elif y > (side-marginal):
        if theta >= math.pi/2 or theta < -math.pi/2:
            vel_msg.angular.z = turning_speed
            vel_msg.linear.x = velocity_forward
        else:
            vel_msg.angular.z = -turning_speed
            vel_msg.linear.x = velocity_forward

    elif y < marginal:
        if theta >= -math.pi/2 and theta < math.pi/2:
            vel_msg.angular.z = turning_speed
            vel_msg.linear.x = velocity_forward
        else:
            vel_msg.angular.z = -turning_speed
            vel_msg.linear.x = velocity_forward

    else:
        vel_msg.angular.z = random.uniform(-turning_speed,turning_speed)
        vel_msg.linear.x = random.uniform(0,velocity_forward)


    if vel_msg.angular.z <= 0:
        vel_r_msg.data = abs(vel_msg.angular.z) * -1
        vel_l_msg.data = abs(vel_msg.angular.z)
    else:
        vel_r_msg.data = abs(vel_msg.angular.z)  
        vel_l_msg.data = abs(vel_msg.angular.z) * -1

    vel_l_msg.data = vel_l_msg.data + vel_msg.linear.x
    vel_r_msg.data = vel_r_msg.data + vel_msg.linear.x

    # for some reason REVERSED, so multiply by -1
    vel_l_msg.data = vel_l_msg.data * -1
    vel_r_msg.data = vel_r_msg.data * -1

    velocity_bl_publisher.publish(vel_l_msg)
    velocity_fl_publisher.publish(vel_l_msg)
    velocity_br_publisher.publish(vel_r_msg)
    velocity_fr_publisher.publish(vel_r_msg)

if __name__ == '__main__':
    while not rospy.is_shutdown():
        rospy.init_node("random_walk_robot5")
        print("start")

        velocity_bl_publisher = rospy.Publisher('/robot5/wheel_bl_velocity_controller/command', Float64, queue_size=1)
        velocity_fl_publisher = rospy.Publisher('/robot5/wheel_fl_velocity_controller/command', Float64, queue_size=1)
        velocity_br_publisher = rospy.Publisher('/robot5/wheel_br_velocity_controller/command', Float64, queue_size=1)
        velocity_fr_publisher = rospy.Publisher('/robot5/wheel_fr_velocity_controller/command', Float64, queue_size=1)
        rospy.Subscriber("/robot5/odom", Odometry, callback)
        rospy.spin()