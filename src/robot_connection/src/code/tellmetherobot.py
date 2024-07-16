#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from spherov2 import scanner

def tell_me_the_robot(pub):
    toy = scanner.find_toy()

    # Check if a Sphero robot was found
    if toy:
        # Get the name of the Sphero robot
        robot_name = toy.name
        # Publish the robot name
        pub.publish(robot_name)
        rospy.loginfo(f"Published robot name: {robot_name}")
    else:
        rospy.loginfo("No Sphero robot found.")

if __name__ == '__main__':
    rospy.init_node('name_robot')
    pub = rospy.Publisher('sphero_name', String, queue_size=10)
    rate = rospy.Rate(1)  # Adjust the frequency as needed (1 Hz here)
    
    while not rospy.is_shutdown():
        try:
            tell_me_the_robot(pub)
            rospy.sleep(30) # Wait for 30 seconds before publishing again
        except rospy.ROSInterruptException:
            pass
        rate.sleep()

