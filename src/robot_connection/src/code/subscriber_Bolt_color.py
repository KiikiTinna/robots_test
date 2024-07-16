#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def color_subscriber():
    rospy.init_node('color_subscriber')
    rospy.Subscriber('sphero_color', String, color_callback)
    rospy.spin()

def color_callback(data):
    # Parse the color information from the received message
    rospy.loginfo("Received color information: %s", data.data)

if __name__ == '__main__':
    color_subscriber()
