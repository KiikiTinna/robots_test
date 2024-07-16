#!/usr/bin/env python3


import rospy
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color


class RobotControllerRobot:
    def __init__(self):
        self.toy = scanner.find_toy()
        self.droid = SpheroEduAPI(self.toy)

    def move_robot(self):
        with self.droid:
            # Go straight
            self.droid.set_main_led(Color(r=0, g=0, b=255))  # Set the color to blue
            self.droid.roll(0, 31, 3) # Roll forward at speed 100 for 3 seconds
            rospy.sleep(1)

            # Slow down and go straight for a shorter time
            self.droid.roll(270, 31, 2) # Roll forward at speed 50 for 2 seconds
            rospy.sleep(1)

            # Turn left
            self.droid.roll(0, 31, 3) # Turn left at speed 100 for 1 second
            rospy.sleep(1)


    def turn_robot(self):
        with self.droid:
        # First, turn the robot 360 degrees to the left
            self.droid.spin(100, 1)
            rospy.sleep(0.5)
            self.droid.spin(100, 1)
            rospy.sleep(0.5)
            self.droid.spin(100, 1)
            rospy.sleep(0.5)
            self.droid.spin(60, 1)
            rospy.sleep(1)
