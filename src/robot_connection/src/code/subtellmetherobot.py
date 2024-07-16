#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def robot_name_subscriber():
    rospy.init_node('robot_name_subscriber')
    rospy.Subscriber('sphero_name', String, handle_robot_name)
    rospy.spin()

def handle_robot_name(data):
    robot_name = data.data
    rospy.loginfo(f"Received robot name: {robot_name}")

    # Perform actions based on the robot name
    if robot_name[:2] == 'SB':
        with SpheroEduAPI(scanner.find_toy()) as droid:
            droid.set_main_led(Color(r=0, g=0, b=255))
            rospy.loginfo("Changed color to blue")
    elif robot_name[:2] == 'SM':
        with SpheroEduAPI(scanner.find_toy()) as droid:
            droid.set_main_led(Color(r=255, g=0, b=0))
            rospy.loginfo("Changed color to red")
    else:
        rospy.loginfo("Received unknown robot name")

if __name__ == '__main__':
    try:
        robot_name_subscriber()
    except rospy.ROSInterruptException:
        pass