# Visualize Rplidar data in Rviz

1. Run ROS across multiple machines (Instructions can be found in different file)

2. In your Jetson Nano terminal type command:
   >**roslaunch rplidar_ros rplidar.launch**

3. In your own computers terminal open Rviz:
   >**rosrun rviz rviz**

4. Add new LaserScan. At the bottom left press button "Add" and select LaserScan.
   
5. Make these changes into the settings of LaserScan:
   >(Note: Delete and type, there is no options to select from)
   - Topic: /scan
   - Fixed Frame: laser
   - Check that you receive messages from topic
   - Increase size (m) to 0.05
   
     
   ![Change these in Rviz](/rplidar_data_to_rviz/rviz.png)
