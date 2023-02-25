#!/usr/bin/env python

import sys
import rospy
import servo_angle_restrictions as servo_rest
from std_msgs.msg import UInt8MultiArray

rospy.init_node('robot_servo_communication', anonymous=True)
right_arm = rospy.Publisher('/right_arm', UInt8MultiArray, queue_size=10)
left_arm = rospy.Publisher('/left_arm', UInt8MultiArray, queue_size=10)
right_shoulder = rospy.Publisher('/right_shoulder', UInt8MultiArray, queue_size=10)

data_right_arm = UInt8MultiArray()
data_right_arm.data = [0]*6
data_left_arm = UInt8MultiArray()
data_left_arm.data = [0]*6
data_right_shoulder = UInt8MultiArray()
data_right_shoulder.data = [0]*4

data_right_shoulder.data[0] = 45
data_right_shoulder.data[1] = 160
data_right_shoulder.data[2] = 80
data_right_shoulder.data[3] = 80

# change = 0

# time_t = rospy.get_time()
# while (rospy.get_time() - time_t) < 0.5:
#     pass

# rospy.loginfo(data_right_shoulder)
# right_shoulder.publish(data_right_shoulder)

time_t = rospy.get_time()
while (rospy.get_time() - time_t) < 1:
    pass

data_right_arm.data[0] = 100
data_right_arm.data[1] = 40
data_right_arm.data[2] = 40
data_right_arm.data[3] = servo_rest.rHAND_FINGER_4_MAX
data_right_arm.data[4] = servo_rest.rHAND_FINGER_5_MAX
data_right_arm.data[5] = 100
rospy.loginfo(data_right_arm)
right_arm.publish(data_right_arm)

rospy.loginfo("FINISH")
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    # if change == 0:
    #     change = 1
    #     data_right_arm.data[0] = servo_rest.rHAND_FINGER_1_MAX
    #     data_right_arm.data[1] = servo_rest.rHAND_FINGER_2_MAX
    #     data_right_arm.data[2] = servo_rest.rHAND_FINGER_3_MAX
    #     data_right_arm.data[3] = servo_rest.rHAND_FINGER_4_MAX
    #     data_right_arm.data[4] = servo_rest.rHAND_FINGER_5_MAX
    #     data_right_arm.data[5] = 100
    # elif change == 1:
    #     change = 2
    #     data_right_arm.data[0] = servo_rest.rHAND_FINGER_1_MIN
    #     data_right_arm.data[1] = servo_rest.rHAND_FINGER_2_MIN
    #     data_right_arm.data[2] = servo_rest.rHAND_FINGER_3_MIN
    #     data_right_arm.data[3] = servo_rest.rHAND_FINGER_4_MIN
    #     data_right_arm.data[4] = servo_rest.rHAND_FINGER_5_MIN
    #     data_right_arm.data[5] = 80
    # elif change == 2:
    #     change = 3
    #     data_left_arm.data[0] = servo_rest.lHAND_FINGER_1_MAX
    #     data_left_arm.data[1] = servo_rest.lHAND_FINGER_2_MAX
    #     data_left_arm.data[2] = servo_rest.lHAND_FINGER_3_MAX
    #     data_left_arm.data[3] = servo_rest.lHAND_FINGER_4_MAX
    #     data_left_arm.data[4] = servo_rest.lHAND_FINGER_5_MAX
    #     data_left_arm.data[5] = 100
    # elif change == 3:
    #     change = 0
    #     data_left_arm.data[0] = servo_rest.lHAND_FINGER_1_MIN
    #     data_left_arm.data[1] = servo_rest.lHAND_FINGER_2_MIN
    #     data_left_arm.data[2] = servo_rest.lHAND_FINGER_3_MIN
    #     data_left_arm.data[3] = servo_rest.lHAND_FINGER_4_MIN
    #     data_left_arm.data[4] = servo_rest.lHAND_FINGER_5_MIN
    #     data_left_arm.data[5] = 80
    
    # rospy.loginfo(data_right_arm)
    # right_arm.publish(data_right_arm)
    # rospy.loginfo(data_left_arm)
    # left_arm.publish(data_left_arm)
    # rospy.loginfo(data_right_shoulder)
    # right_shoulder.publish(data_right_shoulder)

    

    rate.sleep()
    
