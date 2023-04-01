#!/usr/bin/env python3

import cv2 as cv
import rospy
import threading
import numpy as np
from std_msgs.msg import UInt8MultiArray, Int16, String, Int8
from skimage.util import img_as_ubyte
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image 
from random import randint
import time



class Hand_detection:

    def __init__(self, debug = False):
        super().__init__()
        self.debug = debug
        self.bridge = CvBridge()
        self.conturs = 0
        self.data_hand = Int8()
        self.data_hand.data = 0

        rospy.init_node('Hand_detection', anonymous= True)
        self.worker = rospy.Subscriber('/right_shoulder',UInt8MultiArray, queue_size=10)
        self.hand = rospy.Publisher('/right_arm_fingers',Int8, queue_size=10)

        self.r = rospy.Rate(0.5)
        self.karnel = np.ones((5, 5), np.float32)/255

        self.cap = cv.VideoCapture(0)

        self.cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

        # self.timer = rospy.Timer(rospy.Duration(2), callback= self.publish_to_hand, reset=True)
        """
            Если DEBUG = 0ff
        """

        self.h = 93
        self.s = 40
        self.v = 255
        self.arg = 0
        self._hand = 0

        if self.debug == True:
            
            cv.namedWindow('track', cv.WINDOW_NORMAL)
            cv.createTrackbar('H','track',0,180,self.nothing)
            cv.createTrackbar('S','track',0,255,self.nothing)
            cv.createTrackbar('V','track',0,255,self.nothing)

            cv.createTrackbar('HL','track',0,180,self.nothing)
            cv.createTrackbar('SL','track',0,180,self.nothing)
            cv.createTrackbar('VL','track',0,180,self.nothing)

            cv.createTrackbar('alpha_brigtness','track', 0, 3, self.nothing)
            cv.createTrackbar('beta_brightness','track', 0, 50, self.nothing)

        self.flag = 0

    def Video_Capture(self):
        # rate = rospy.Rate(30)  
        while True:

            try:
                ret,frame = self.cap.read()

                if not ret:
                    break
                
                # frame = cv.GaussianBlur(frame, (15, 15), 0)
                # frame = cv.medianBlur(frame, 7)
                frame = cv.bilateralFilter(frame, 20 ,50, 50)
                # frame = cv.filter2D(frame, -1, self.karnel)
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
                hsv = hsv[100:240, 100:200]
                if self.debug == True:

                    h = cv.getTrackbarPos('H','track')
                    s = cv.getTrackbarPos('S','track')
                    v = cv.getTrackbarPos('V','track')

                    hl = cv.getTrackbarPos('HL','track')
                    sl = cv.getTrackbarPos('SL','track')
                    vl = cv.getTrackbarPos('VL','track')

                    self.alpha = cv.getTrackbarPos('alpha_brigtness','track')
                    self.beta = cv.getTrackbarPos('beta_brigtness','track')

                    lower = np.array([hl,sl,vl])
                    self.upper = np.array([h,s,v])
                elif self.debug == False and self.flag == 0:

                    lower = np.array([0,0,180])
                    self.upper = np.array([self.h,self.s,self.v])

                mask = cv.inRange(hsv,lower,self.upper)
                opening = cv.morphologyEx(mask, cv.MORPH_OPEN, self.karnel)
                self.closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, self.karnel)

                conturs, h = cv.findContours(self.closing,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
                conturs = sorted(conturs, key = cv.contourArea, reverse=True)
                count_wh = len(self.closing[self.closing == 255])
                areas = []

                for i in range(len(conturs)):
                    area =cv.contourArea(conturs[i])
                    areas.append(area)
                    x,y,w,h = cv.boundingRect(conturs[i])
                    if area > 1000:
                    # Позиция Hand : w = +-56, h = +- 86
                            frame = cv.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)
                            frame = cv.rectangle(frame, (x,y), (x+60, y-25),(0,0,0),-1)
                            cv.putText(frame,f"Is Hand! {w/h}", (x,y),cv.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255),2)
                            self.flag = 1
                            self._hand = 0

                    if sum(map(lambda item: item > 1000, areas)) == 0 and self.flag == 1:
                       self._hand = 1
 
                self.publish_to_hand()
                # cv.imshow('mask', mask)
                cv.imshow('close', self.closing)
                cv.imshow('frame',frame)
                # cv.imshow('res', res)
                # cv.imshow('dilation', dilation)
                cv.waitKey(3)
                
                if rospy.is_shutdown(): # Клавиша Esc
                    self.cap.release()
                    rospy.loginfo('Shutdown')
                    break
                
                
            except CvBridgeError as e:
                rospy.loginfo('CV_BRIDGE_ERROR')
                
        cv.destroyAllWindows()

    
    def change_brigtness(self, img):
        """
            Изменяем яркость
        """
        new_img = np.zeros(img.shape, img.dtype)
        alpha = 2
        beta = 100

        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                for c in range(img.shape[2]):
                    new_img[y,x,c] = np.clip(alpha*img[y,x,c] + beta,0,255)
                    return new_img
        
    def nothing(self, x):
        pass

    def publish_to_hand(self, *arg):
        self.data_hand.data = self._hand
        if self.hand == 1:
            self.hand.publish(self.data_hand)
            rospy.sleep(rospy.Duration(3))
        else:
            self.hand.publish(self.data_hand)

class Move(Hand_detection):
    def __init__(self):
        super().__init__(debug = False)
        self.data_fingers = UInt8MultiArray()
        self.data_shoulder = UInt8MultiArray()

        self.right_shoulder = rospy.Publisher('/right_shoulder', UInt8MultiArray, queue_size=10)
        self.right_arm = rospy.Publisher('/right_arm', UInt8MultiArray, queue_size=10)

    def right_hand_fingers_move(self):
        
        self.data_fingers.data = [0]*6

        self.data_fingers.data[0] = 50
        self.data_fingers.data[1] = 80
        self.data_fingers.data[2] = 90
        self.data_fingers.data[3] = 130
        self.data_fingers.data[4] = 130
        self.data_fingers.data[5] = 90

        self.right_arm.publish(self.data_fingers)

    def right_hand_shoulder_move(self):

        self.data_shoulder.data = [0]*4

        self.data_shoulder.data[0] = 90
        self.data_shoulder.data[1] = 90
        self.data_shoulder.data[2] = 93
        self.data_shoulder.data[3] = 80

        self.right_shoulder.publish(self.data_shoulder)

if __name__ == "__main__":
    try:
        # global _hand
        # _hand = 0
        HD = Move()
        HD.Video_Capture()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        print('Shud down')