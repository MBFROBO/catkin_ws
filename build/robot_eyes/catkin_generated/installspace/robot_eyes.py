#!/usr/bin/env python3

import cv2 as cv
import rospy
import numpy as np
from std_msgs.msg import UInt8MultiArray, Int16, String
from skimage.util import img_as_ubyte
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image 


class Hand_detection():

    def __init__(self):

        self.bridge = CvBridge()
        self.pub = rospy.Publisher('Hand_detection',Image, queue_size=10)
        rospy.init_node('Hand_detection', anonymous= True)

        self.cap = cv.VideoCapture(0)

        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
        
    def Video_Capture(self):
        # rate = rospy.Rate(30)  
        while True:
            try:
                ret,frame = self.cap.read()

                if not ret:
                    break

                # res_img = cv.resize(frame, (320,240), cv.IMREAD_GRAYSCALE)
                # img_binary = cv.threshold(res_img, 75, 255, cv.THRESH_BINARY)[1]
                img = cv.rectangle()
                
                hsv = cv.cvtColor(res_img, cv.COLOR_BGR2HSV)
                h,s,v = cv.split(hsv) 

                cv.imshow('h', h)
                cv.imshow('s', s)
                cv.imshow('v',v)

                cv.waitKey(3)

                msg= self.bridge.cv2_to_imgmsg(hsv,"bgr8")
                self.pub.publish(msg)
                # rospy.loginfo(msg)

                # message = bridge.cv2_to_compressed_imgmsg(img, n_channels)
                # eye_data = UInt8MultiArray()
                # eye_data.data = [0]*2

                # eye_data.data[0] = h
                # eye_data.data[1] = w

                # pub.publish(eye_data)
                # print('CAMERA:', message)
                # rate.sleep()
                
                if rospy.is_shutdown(): # Клавиша Esc
                    self.cap.release()
                    rospy.loginfo('Shutdown')
                    break

            except CvBridgeError as e:
                rospy.loginfo('CV_BRIDGE_ERROR')
                
        cv.destroyAllWindows()

if __name__ == "__main__":
    try:

        HD = Hand_detection()
        HD.Video_Capture()

    except rospy.ROSInterruptException:
        pass