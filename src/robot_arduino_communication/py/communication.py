#!/usr/bin/env python3
import sys
import rospy
import servo_angle_restrictions as servo_rest
from std_msgs.msg import UInt8MultiArray, Int8, Int32MultiArray, Float32MultiArray
import numpy as np
import time

       
rospy.init_node('robot_servo_communication', anonymous=True)
rate = rospy.Rate(1)
log_timer_head = 0
log_timer_neck = 0
log_timer_right_arm = 0
log_timer_right_shoulder = 0
log_timer_left_shoulder = 0
log_timer_left_arm = 0

right_arm = rospy.Publisher('/right_arm', UInt8MultiArray, queue_size=10)
left_arm = rospy.Publisher('/left_arm', UInt8MultiArray, queue_size=10)
right_shoulder = rospy.Publisher('/right_shoulder', UInt8MultiArray, queue_size=10)
left_shoulder = rospy.Publisher('/left_shoulder', UInt8MultiArray, queue_size=10)
head = rospy.Publisher('/head', UInt8MultiArray, queue_size= 10)
neck = rospy.Publisher('/neck', UInt8MultiArray, queue_size= 10)
Head_wrist = []
DEBUG = False
BASE_STATEMENT_HEAD=70
head_wrist_flag = 0

def Right_arm_callback(data, right_arm = right_arm):
    global right_arm_handshake_flag
    global log_timer_right_arm
    data_right_arm = UInt8MultiArray()
    data_right_arm.data = [0]*6
    
    if data == Int8(1):

        data_right_arm.data[0] = 10    # указательный
        data_right_arm.data[1] = 10    # средний
        data_right_arm.data[2] = 10    # безымянный
        data_right_arm.data[3] = 10   # мезинец
        data_right_arm.data[4] = 10   # большой
        data_right_arm.data[5] = 180    # запястьем
        
    elif data == Int8(0):
        
        data_right_arm.data[0] = 170
        data_right_arm.data[1] = 170
        data_right_arm.data[2] = 170
        data_right_arm.data[3] = 170
        data_right_arm.data[4] = 170
        data_right_arm.data[5] = 0

    else:

        data_right_arm.data[0] = 180
        data_right_arm.data[1] = 180
        data_right_arm.data[2] = 180
        data_right_arm.data[3] = 180
        data_right_arm.data[4] = 180
        data_right_arm.data[5] = 180

    if (rospy.get_time() - log_timer_right_arm) > 0.1:
        log_timer_right_arm = rospy.get_time()
        right_arm.publish(data_right_arm)

def right_arm_handshake_flag(data = None):
    right_arm_handshake_flag = 1
    return right_arm_handshake_flag

def Left_arm(data,left_arm = left_arm):
    global log_timer_left_arm
    data_left_arm = UInt8MultiArray()
    data_left_arm.data = [0]*6

    if data == Int8(1):
        data_left_arm.data[0] = 0
        data_left_arm.data[1]= 0
        data_left_arm.data[2] = 0
        data_left_arm.data[3] = 0
        data_left_arm.data[4] = 0      # Большой палец
        data_left_arm.data[5] = 140
    elif data == Int8(0):
        data_left_arm.data[0] = 180
        data_left_arm.data[1]= 180
        data_left_arm.data[2] = 180
        data_left_arm.data[3] = 180
        data_left_arm.data[4] = 180    # Большой палец
        data_left_arm.data[5] = 70
    else:
        data_left_arm.data[0] = 180
        data_left_arm.data[1]= 180
        data_left_arm.data[2] = 180
        data_left_arm.data[3] = 180
        data_left_arm.data[4] = 180    # Большой палец
        data_left_arm.data[5] = 70

    if (rospy.get_time() - log_timer_left_arm) > 0.1:
        log_timer_left_arm = rospy.get_time()
        rospy.logwarn(data)
        left_arm.publish(data_left_arm)

def Right_shoulder(data = None, right_shoulder = right_shoulder):
    global log_timer_right_shoulder
    data_right_shoulder = UInt8MultiArray()

    if data.data is not None:
        if data.data[3] == 0:
            data_right_shoulder.data = [0]*4

            data_right_shoulder.data[0] = 75
            data_right_shoulder.data[1] = 90
            data_right_shoulder.data[2] = 90
            data_right_shoulder.data[3] = 75

        else:
            data_right_shoulder.data = [0]*4

            data_right_shoulder.data[0] = 75
            data_right_shoulder.data[1] = 90
            data_right_shoulder.data[2] = 90
            data_right_shoulder.data[3] = 93

        #     data_right_shoulder.data = [0]*4

        #     data_right_shoulder.data[0] = 60
        #     data_right_shoulder.data[1] = 40
        #     data_right_shoulder.data[2] = 50
        #     data_right_shoulder.data[3] = 75
    else:
        data_right_shoulder.data = [0]*4

        data_right_shoulder.data[0] = 75
        data_right_shoulder.data[1] = 90
        data_right_shoulder.data[2] = 90
        data_right_shoulder.data[3] = 75

    if (rospy.get_time() - log_timer_right_shoulder) > 1:
        log_timer_right_shoulder = rospy.get_time()
        right_shoulder.publish(data_right_shoulder)

def Left_shoulder(data = None, left_shoulder = left_shoulder):

    global log_timer_left_shoulder

    data_left_shoulder = UInt8MultiArray()


    if data is not None:
        if data.data == Int8(1):
            data_left_shoulder.data = [0]*4
            data_left_shoulder.data[0] = 90
            data_left_shoulder.data[1] = 80
            data_left_shoulder.data[2] = 90
            data_left_shoulder.data[3] = 93
        if data.data == Int8(0):
            data_left_shoulder.data = [0]*4
            data_left_shoulder.data[0] = 90
            data_left_shoulder.data[1] = 80
            data_left_shoulder.data[2] = 90
            data_left_shoulder.data[3] = 93
        else:
            data_left_shoulder.data = [0]*4
            data_left_shoulder.data[0] = 90
            data_left_shoulder.data[1] = 80
            data_left_shoulder.data[2] = 90
            data_left_shoulder.data[3] = 93

    if (rospy.get_time() - log_timer_left_shoulder) > 3:
        log_timer_left_shoulder = rospy.get_time()
        left_shoulder.publish(data_left_shoulder)

def Neck(data = None, neck = neck):
    data_Neck = UInt8MultiArray()
    global log_timer_neck

    if data is not None:
        if data.data[3] == 0: 
            data_Neck.data = [0]*3
            data_Neck.data[0] =180# правая
            data_Neck.data[1] = 0 # левая
            data_Neck.data[2] = 120 # центральная
        if data.data[3] == 2:
            data_Neck.data = [0]*3
            data_Neck.data[0] = 180 # правая
            data_Neck.data[1] = 0 # левая
            data_Neck.data[2] = 0 # центральная
    else:
        data_Neck.data[0] =180# правая
        data_Neck.data[1] = 0 # левая
        data_Neck.data[2] = 0

    if (rospy.get_time() - log_timer_neck) > 1:
        log_timer_neck = rospy.get_time()
        neck.publish(data_Neck)

def map_(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

data_data_1_old = 0
error_old = 0

def Head(data = None, head = head):

    global right_arm_handshake_flag
    global head_wrist_flag
    data_Head = UInt8MultiArray()
    global log_timer_head
    global data_data_1_old
    global error_old
    mean_wrist = 70

    if data is not None:

        if (rospy.get_time() - log_timer_head) > 0.05:
            if (data.data[0] == 0.0) and data.data[1] == 0.0:
                data_data_1_old = 80
                data_Head.data = [0]*4
                data_Head.data[0] = 0 # рот
                data_Head.data[1] = 70 # поворот глаз
                data_Head.data[2] = 180 # наклон глаз
                data_Head.data[3] = 110 # поворот головы

            elif data.data[0] == 1.0 and data.data[1] == 0.0:
                data_data_1_old = 80
                data_Head.data = [0]*4
                data_Head.data[0] = 0 # рот
                data_Head.data[1] = 70 # поворот глаз
                data_Head.data[2] = 180 # наклон глаз
                data_Head.data[3] = 80 # поворот головы

            elif data.data[0] == 1.0:
                
                data_Head.data = [0]*4
                global Head_wrist                
                Kp = 11
                error = (0.5 - (1 - data.data[1]))
                P = error * Kp

                data_data_1_old = data_data_1_old + int(P)
                mean_wrist = int(data_data_1_old)
                
                if mean_wrist > 255:
                    mean_wrist = 255
                if mean_wrist < 0:
                    mean_wrist = 0

                data_Head.data[0] = 0 # рот
                data_Head.data[1] = 100 # поворот глаз
                data_Head.data[2] = 180 #наклон глаз
                data_Head.data[3] = abs(int(mean_wrist))

            log_timer_head = rospy.get_time()
            # rospy.logwarn('Head turn %s', data_Head)
            head.publish(data_Head)


while not rospy.is_shutdown():

    rospy.Subscriber('/data_eyes_confirm', Int8, Right_arm_callback)
    rospy.Subscriber('/data_eyes_confirm', Int8, Left_shoulder)
    rospy.Subscriber('/face_xmin', Float32MultiArray, Head)
    rospy.Subscriber('/astra_eyes', Int32MultiArray, Neck)
    rospy.Subscriber('/astra_eyes', Int32MultiArray, Right_shoulder)
    rospy.Subscriber('/data_eyes_confirm', Int8, Right_arm_callback)
    rate.sleep()

rospy.spin()
        
