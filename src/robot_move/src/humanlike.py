#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color


class RobotControllerHuman:

    def __init__(self):
        self.toy = scanner.find_toy()
        self.droid = SpheroEduAPI(self.toy)
    
    def move_robot(self):
        with self.droid:
            # Go straight
            self.droid.set_main_led(Color(r=0, g=0, b=255))  # Set the color to blue
            self.droid.roll(0, 31, 3)  # Roll forward at speed 100 for 3 seconds
            #rospy.sleep(0.5)

            # Turn left
            self.droid.roll(270, 31, 2)  # Turn left at speed 100 for 1 second
            #rospy.sleep(0.5)

            # Go straight at a slower speed for a shorter time
            self.droid.roll(0, 31, 3)  # Roll forward at speed 30 for 1 second
            #rospy.sleep(0.5)


    def turn_robot(self):
        with self.droid:
        # First, turn the robot 360 degrees to the left
            self.droid.spin(360, 2)
            rospy.sleep(3)


    def color_robot(self):
        self.droid.set_main_led(Color(r=0,g=255,b=0))
        rospy.sleep(1)
