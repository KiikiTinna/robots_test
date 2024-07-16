#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from humanlike import RobotControllerHuman
from robotlike import RobotControllerRobot



def robot_contoler_callback(data):
    if data.data == "1":
        
        robot_controller = RobotControllerRobot()
        #robot_controller.turn_robot()
        robot_controller.move_robot()

    elif data.data == "2":
        robot_controller = RobotControllerHuman()
        #robot_controller.turn_robot()
        robot_controller.move_robot()
    else:
        rospy.loginfo("Invalid behavior. Please choose '1' or '2'.")

def robot_behavior_listener():
    rospy.init_node('robot_controller', anonymous=True)
    rospy.Subscriber("robot_behavior", String, robot_contoler_callback)

    while not rospy.is_shutdown():
        # Read user input from keyboard
        user_input = input("Enter '1' for robot behavior or '2' for human behavior: ")

        # Publish user input to the robot_behavior topic
        pub = rospy.Publisher('robot_behavior', String, queue_size=10)
        pub.publish(user_input)

    rospy.spin()

if __name__ == '__main__':
    try:
        robot_behavior_listener()
    except rospy.ROSInterruptException:
        pass

