This document contains comprehensive guide on how to train robots in gazebo simulation.
When code is referred check the codes in this folder.

These are steps from 'Position from ultra sonic sensors' document and they should be done prior to running any gazebo commands
    1. sudo apt update
    2. sudo apt install python3-pip
    3. sudo apt install python3-testresources
    4. pip3 install --user tensorflow
    5. pip3 install --user pandas
    6. cd ~/<your workspace>/src
    7. catkin_create_pkg robot_position rospy nav_msgs sensor_msgs
    8. cd ~/<your workspace>
    9. catkin_make
    10. source devel/setup.bash
    11. cd robot_position/src
    12. touch robot_write_to_csv.py
        Now there are typos in the Documentation so it is recommended to use the one in here
    13. chmod +x robot1_write_to_csv.py
    14. git clone https://github.com/tonaalt/ros_ai_robowars_ws.git
        Do this in your src folder
    15. roslaunch samk_robowar_world samk_robowar_arena_no_pit.launch 
        If the blade of the robot1 is not moving you need to update controllers. The error messages can be seen when gazebo is starting.

Here is where the documentations instructions get derailed so this is the updated guide on what to do next:
    1. Run both_robots_move.py 
        This makes both of the simulation robots move randomly
    2. Run restart_simulation.sh
        This resets the simulation every minute. This is important since the robots clip off from the arena or get stuck from time to time.
    3. Run robot1_write_to_csv.py
        This creates a csv file in the directory you are in. It coordinates from the lidars. You should collect at least 50000 lines of data.
    4. (Optional) Run row_printing.py 
        This prints how many rows you csv file currectly has. Run it during data collecting.
    5. After collecting data run train_robot1_position.py
        You need to change the paths in the code to match your own.
    6. After training you will have saved_model and then you can run test_robot1_position.py to see how accurate your model is.

Done. Now you have a trained model where the robot knows its position.
