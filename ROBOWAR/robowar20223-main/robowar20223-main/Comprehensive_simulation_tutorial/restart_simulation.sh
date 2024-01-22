#!/bin/bash

# Infinite loop
while true; do
    # Execute your command
    rosservice call /gazebo/reset_world

    # Wait for 60 seconds (1 minute)
    sleep 60
done
