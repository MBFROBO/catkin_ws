#!/usr/bin/env python3
import sys
import rospy
import servo_angle_restrictions as servo_rest
from std_msgs.msg import UInt8MultiArray, Int8
import time

class Communication:

    def __init__(self):
        
        rospy.init_node('robot_servo_communication', anonymous=True)

        self.right_arm = rospy.Publisher('/right_arm', UInt8MultiArray, queue_size=10)
        self.left_arm = rospy.Publisher('/left_arm', UInt8MultiArray, queue_size=10)
        self.right_shoulder = rospy.Publisher('/right_shoulder', UInt8MultiArray, queue_size=10)
        self.left_shoulder = rospy.Publisher('/left_shoulder', UInt8MultiArray, queue_size=10)
        rospy.Subscriber('/right_arm_fingers', Int8, self.Right_arm)


        self.data_right_arm = UInt8MultiArray()
        self.data_right_arm.data = [0]*6
        self.data_left_arm = UInt8MultiArray()
        self.data_left_arm.data = [0]*6
        self.data_right_shoulder = UInt8MultiArray()
        self.data_right_shoulder.data = [0]*4
        self.data_left_shoulder = UInt8MultiArray()
        self.data_left_shoulder.data = [0]*4

    def Right_arm(self,data = None):
        if data == Int8(1):
            self.data_right_arm.data[0] = 50
            self.data_right_arm.data[1] = 80
            self.data_right_arm.data[2] = 90
            self.data_right_arm.data[3] = 130
            self.data_right_arm.data[4] = 130
            self.data_right_arm.data[5] = 90
            
        if data == Int8(0):
            
            self.data_right_arm.data[0] = 0
            self.data_right_arm.data[1] = 0
            self.data_right_arm.data[2] = 0
            self.data_right_arm.data[3] = 0
            self.data_right_arm.data[4] = 0
            self.data_right_arm.data[5] = 0
        
        if data == None:
            pass

        self.right_arm.publish(self.data_right_arm)

    def Left_arm(self, data = None):
                
        self.data_left_arm.data[0] = 100
        self.data_left_arm.data[1]= 40
        self.data_left_arm.data[2] = 40
        self.data_left_arm.data[3] = servo_rest.lHAND_FINGER_4_MIN
        self.data_left_arm.data[4] =servo_rest.lHAND_FINGER_5_MIN
        self.data_left_arm.data[5] = 100
        # rospy.loginfo(data_left_arm)
        self.left_arm.publish(self.data_left_arm)

        if data == None:
            pass
    
    def Right_shoulder(self, data = None):

        self.data_right_shoulder.data[0] = 45
        self.data_right_shoulder.data[1] = 160
        self.data_right_shoulder.data[2] = 80
        self.data_right_shoulder.data[3] = 80

        self.right_shoulder.publish(self.data_right_shoulder)

    def Left_shoulder(self, data = None):

        self.data_left_shoulder.data[0] = 45
        self.data_left_shoulder.data[1] = 160
        self.data_left_shoulder.data[2] = 80
        self.data_left_shoulder.data[3] = 80

        self.left_shoulder.publish(self.data_left_shoulder)
    def main(self):
        rate = rospy.Rate(1)
        
        while not rospy.is_shutdown():
            self.Left_arm()
            self.Left_shoulder()
            self.Right_shoulder()
            rospy.spin()
            rate.sleep()

if __name__ == '__main__':
    try:
        COMMUNICATE = Communication()
        COMMUNICATE.main()
    except:
        pass