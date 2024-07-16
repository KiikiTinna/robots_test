#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

def color_publisher():
    rospy.init_node('color_publisher')
    pub = rospy.Publisher('sphero_color', String, queue_size=10)

    toy = scanner.find_toy()
    with SpheroEduAPI(toy) as droid:
        while not rospy.is_shutdown():
            # You can modify the color based on your requirements
            # For example, let's change the color to blue
            droid.set_main_led(Color(r=0, g=0, b=255))
            
            # Publish the color change information
            pub.publish("Color changed to blue")
            
            rospy.sleep(1)  # Sleep for 1 second (adjust as needed)

if __name__ == '__main__':
    try:
        color_publisher()
    except rospy.ROSInterruptException:
        pass

