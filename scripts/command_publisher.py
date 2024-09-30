#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def command_publisher():
    pub = rospy.Publisher('/turtlebot_commands', String, queue_size=10)
    rospy.init_node('command_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        command = input("Enter a command (e.g., 'Forward 5', 'Left 2'): ")
        rospy.loginfo(f"Publishing command: {command}")
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        command_publisher()
    except rospy.ROSInterruptException:
        pass
