# SET UP TWO MACHINES
## jetson nano (JN)
#### -connect to JN:
    ssh v2k2@v2k2 (ssh <username>@<ipaddress>)
#### - open the '.bashrc' file:
    nano .bashrc
#### - At the end of the file, type the command below. (Replace 10.103.4.99 with your JN IpAddress then save the file.)
    export ROS_MASTER_URI=http://10.103.4.99:11311    
#### - apply the change we made in '.bashrc' file:
    source .bashrc

## laptop
#### - open your terminal
#### - open the '.bashrc' file:
    nano .bashrc
#### - At the end of the file, type the command below. (Replace 10.103.4.99 with your JN IpAddress then save the file.)
    export ROS_MASTER_URI=http://10.103.4.99:11311    
#### - apply the change we made in '.bashrc' file:
    source .bashrc

## TALKER/ LISTENER ACROSS TWO MACHINES
### jetson nano (JN)
#### - run the master (in JN):
    roscore
#### - Start the talker:
    rosrun rospy_tutorials talker.py

### laptop
#### - Start the listener:
    rosrun rospy_tutorials listener.py

## TESTING TALKER AND LISTENER
    rostopic list






