#!/usr/bin/env python3

import sys
import rospy
import cv2 as cv
import numpy as np
from skimage.util import img_as_ubyte
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

people = 0

start_play = 0

def callback(data):

    global people
    global time_t
    global start_play

    try:
        cv_image = bridge.imgmsg_to_cv2(data, "32FC1")
    except CvBridgeError as e:
        print(e)

    img2 = np.float32(cv_image) 
    img2 = img2 * 0.5
    # img2 = np.clip(img2, -255.0, 255.0) 

    cv_image_convert_uint8_t = img_as_ubyte(img2)

    cv_image_convert_uint8_t = cv.blur(cv_image_convert_uint8_t,(1,1))

    frame_threshold = cv.inRange(cv_image_convert_uint8_t, 100, 150)
    contours, hierarchy = cv.findContours(frame_threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    drawing = np.zeros((cv_image_convert_uint8_t.shape[0], cv_image_convert_uint8_t.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (0, 255, 255)
        if cv.contourArea(contours[i]) > 50000:
            people = 1
            time_t = rospy.get_time()
            cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)

    if people == 1:
        if start_play == 0:
            start_play = 1
            str_play = "~/_1.mp3"
            pub.publish(str_play)
    else:
        if start_play == 1:
            start_play = 0
            print("stop")
            time_t = rospy.get_time()
            str_stop = "~/__.mp3"
            pub.publish(str_stop)  

    if people == 1:
        if rospy.get_time() - time_t > 2:
            people = 0
    

    
            

    cv.imshow("Image window", cv_image_convert_uint8_t)
    cv.imshow("frame_threshold", frame_threshold)
    cv.imshow('Contours', drawing)
    cv.waitKey(3)



rospy.init_node('image_converter', anonymous=True)
image_sub = rospy.Subscriber("/camera/depth/image", Image, callback)
pub = rospy.Publisher('/audio_file_player/play', String, queue_size=10)

time_t = rospy.get_time()

try:
    rospy.spin()
except KeyboardInterrupt:
    print("Shutting down")
cv.destroyAllWindows()

