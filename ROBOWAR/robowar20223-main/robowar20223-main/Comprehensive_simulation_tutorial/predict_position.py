#! /usr/bin/python3
import rospy, message_filters
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range
from geometry_msgs.msg import Pose
import angles
from tf.transformations import euler_from_quaternion
import numpy as np
from tensorflow import keras
from pathlib import Path
from sklearn.metrics import mean_squared_error


model = keras.models.load_model('/home/saku/sms_ws/src/robot_position/src/saved_model')

predict_data = np.zeros((1,10))
print(predict_data.shape)
test_predictions = model.predict(predict_data)
print(test_predictions)

class Robot_position:
    def __init__(self):
        self.node = rospy.init_node("robot1_position_node")
        self.predicted_pose_publisher = rospy.Publisher('robot1/predicted_pose',Pose, queue_size=1)
        self.us1_sub = message_filters.Subscriber('/ultrasonic1',Range)
        self.us2_sub = message_filters.Subscriber('/ultrasonic2',Range)
        self.us3_sub = message_filters.Subscriber('/ultrasonic3',Range)
        self.us4_sub = message_filters.Subscriber('/ultrasonic4',Range)
        self.us5_sub = message_filters.Subscriber('/ultrasonic5',Range)
        self.us6_sub = message_filters.Subscriber('/ultrasonic6',Range)
        self.odom_sub = message_filters.Subscriber('/robot1/odom',Odometry)

        
        self.subs = message_filters.ApproximateTimeSynchronizer([self.us1_sub,self.us2_sub,self.us3_sub,self.us4_sub,self.us5_sub,self.us6_sub,self.odom_sub],queue_size=1, slop=0.9, allow_headerless=True)
        #self.path_model = Path("/home/saku/sms_ws/src/robot_position/src/saved_model")
        #self.model = keras.models.load_model(self.path_model)
        self.model = keras.models.load_model('/home/saku/sms_ws/src/robot_position/src/saved_model')
        self.predict_data = np.zeros((1,10))
        self.subs.registerCallback(self.sensor_cb)

    def sensor_cb(self, us1_sub,us2_sub,us3_sub,us4_sub,us5_sub,us6_sub,odom_sub):
        
        orientation_in_quaternions = (
            odom_sub.pose.pose.orientation.x,
            odom_sub.pose.pose.orientation.y,
            odom_sub.pose.pose.orientation.z,
            odom_sub.pose.pose.orientation.w)

        orientation_in_euler = euler_from_quaternion(orientation_in_quaternions)
        yaw = orientation_in_euler[2]
        yaw_radians = angles.normalize_angle_positive(yaw)

        ground_truth_x = odom_sub.pose.pose.position.x
        ground_truth_y = odom_sub.pose.pose.position.y

        # Quaternion orientation
        self.predict_data[0][0] = odom_sub.pose.pose.orientation.x
        self.predict_data[0][1] = odom_sub.pose.pose.orientation.y
        self.predict_data[0][2] = odom_sub.pose.pose.orientation.z
        self.predict_data[0][3] = odom_sub.pose.pose.orientation.w

        # Ultrasonic sensor readings
        self.predict_data[0][4] = us1_sub.range
        self.predict_data[0][5] = us2_sub.range
        self.predict_data[0][6] = us3_sub.range
        self.predict_data[0][7] = us4_sub.range
        self.predict_data[0][8] = us5_sub.range
        self.predict_data[0][9] = us6_sub.range

        test_predictions = self.model.predict(self.predict_data)
        print("predictions " + str(test_predictions[0][0]) +"  " +  str(test_predictions[0][1]))
        print("ground truth" + str(ground_truth_x) + "  "+str(ground_truth_y))
        # Calculate and print MSE
        mse = mean_squared_error(
            [ground_truth_x, ground_truth_y], 
            [test_predictions[0][0], test_predictions[0][1]]
        )
        print("MSE: " + str(mse))
        # Or use rospy.loginfo for logging
        rospy.loginfo("MSE: {}".format(mse))
        p_msg = Pose()
        p_msg.position.x = test_predictions[0][0]
        p_msg.position.y = test_predictions[0][1]
        p_msg.position.z = 0
        p_msg.orientation.x = 0
        p_msg.orientation.y = 0
        p_msg.orientation.z = 0
        p_msg.orientation.w = 0
        self.predicted_pose_publisher.publish(p_msg)

if __name__ == '__main__':
    print("start")
    positions = Robot_position()
    rospy.spin()
