#!/usr/bin/env python3
import sys
import rospy
import time
from std_msgs.msg import Int8



flag = 0
pub = rospy.Publisher('/data_eyes_confirm',Int8,queue_size=10)
time_t = 0
def main(data = None):
    global pub
    global time_t
     
    if (rospy.get_time() - time_t) > 0.5:
        time_t = rospy.get_time()
        pub.publish(data)

rospy.init_node('data_eyes_confirm', anonymous= True)
rospy.Subscriber('right_arm_fingers', Int8, callback=main, tcp_nodelay=True)

try:
    rospy.spin()

except:
    print('shutting down')
