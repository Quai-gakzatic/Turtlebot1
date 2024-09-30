#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def command_callback(data):
    command = data.data.lower().split()
    direction = command[0]
    speed = float(command[1]) if len(command) > 1 else 1.0

    twist_msg = Twist()

    if direction in ['forward', 'move']:
        twist_msg.linear.x = speed
    elif direction == 'backward':
        twist_msg.linear.x = -speed
    elif direction == 'left':
        twist_msg.angular.z = speed
    elif direction == 'right':
        twist_msg.angular.z = -speed

    pub.publish(twist_msg)
    rospy.loginfo(f"Processed command: {data.data}, Twist: {twist_msg}")

def command_processor():
    rospy.init_node('command_processor', anonymous=True)
    rospy.Subscriber('/turtlebot_commands', String, command_callback)
    global pub
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        command_processor()
    except rospy.ROSInterruptException:
        pass
