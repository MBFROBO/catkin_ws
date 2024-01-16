#!/usr/bin/env python3
import sys
import rospy
import cv2 as cv
import numpy as np
from skimage.util import img_as_ubyte
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# import servo_angle_restrictions as servo_rest
from std_msgs.msg import Int32MultiArray, Int8, String
import random

bridge = CvBridge()
people = 0
time_t = 0
time_t2 = 0
time_t3 = 0
point_x = 0
point_y = 0
start_play = 0
start_play_1 = 0
speach_flag = 0

CONDITION_AREA = 35000

def count(c_1, c_2, c_3):

    if len(c_1) != 0:
        return (c_1, 0)
    
    if len(c_1) == 0 and len(c_2) != 0:
        return (c_2, 1)
    
    if len(c_2) == 0 and len(c_1) == 0 and len(c_3) != 0:
        return (c_3, 2)
    
    else:
        return c_1, 0

def video_procesing(contours, hierarchy, drawing, level):

    global time_t2
    global people
    global point_x
    global point_y
    
    for i in range(len(contours)):
            
        if level == 0:
            color = (0, 0, 255)
        elif level == 1:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)

        track_point_color = (0, 0, 255)
        track_point_size  = 2
        thickness = 4

        if cv.contourArea(contours[i]) > CONDITION_AREA:
            time_t2 = rospy.get_time()
            x,y,w,h = cv.boundingRect(contours[i])

            if level == 0:
                people = 0
            if level == 1:
                people = 1
            if level == 2:
                people = 0


            cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
            point_x = int(x+0.5*w)
            point_y = int(y+0.1*h)
            cv.circle(drawing, (point_x,point_y), track_point_size, track_point_color, thickness)

    if (rospy.get_time() - time_t2) > 1:
        time_t2 = rospy.get_time()
        people = 0

    if level == 0 or level == 1:
        return people, point_x, point_y
    else:
        return people, 250, 0
    
def tracking(data):

    global bridge
    global time_t
    global start_play
    global pub_audio
    global time_t3
    global speach_flag
    global start_play_1

    eye_publisher = rospy.Publisher('/astra_eyes', Int32MultiArray, queue_size=10)
    count_pub = rospy.Publisher('/COUNT_PUBLISHER', Image, queue_size=10)

    try:
        cv_image = bridge.imgmsg_to_cv2(data, "32FC1")
    except CvBridgeError as e:
        print('CV_BRIDGE_ERROR: ',e)

    img2 = np.float32(cv_image) 
    img2 = img2 * 0.5   

    cv_image_convert_uint8_t = img_as_ubyte(img2)
    cv_image_convert_uint8_t = cv.blur(cv_image_convert_uint8_t,(1,1))

    frame_threshold_1 = cv.inRange(cv_image_convert_uint8_t, 10, 110)
    frame_threshold_2 = cv.inRange(cv_image_convert_uint8_t, 110, 175)
    frame_threshold_3 = cv.inRange(cv_image_convert_uint8_t, 175, 230)

    contours_1, hierarchy_1 = cv.findContours(frame_threshold_1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_2, hierarchy_2 = cv.findContours(frame_threshold_2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_3, hierarchy_3 = cv.findContours(frame_threshold_3, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    drawing = np.zeros((cv_image_convert_uint8_t.shape[0], cv_image_convert_uint8_t.shape[1], 3), dtype=np.uint8)

    contours, condition = count(contours_1, contours_2, contours_3)

    if condition == 0:
        people, point_x, point_y = video_procesing(contours, hierarchy_1, drawing, condition)
    elif condition == 1:
        people, point_x, point_y = video_procesing(contours, hierarchy_2, drawing, condition)
    else:
        people, point_x, point_y = video_procesing(contours, hierarchy_3, drawing, condition)

    try:
        max_countur_area = max([cv.contourArea(countur) for countur in contours])
    except ValueError:
        max_countur_area = 0

    if condition == 1 and max_countur_area > CONDITION_AREA:

        if speach_flag == 0:
            time_t3 = rospy.get_time()
            speach_flag = 1
        if start_play == 0 and (rospy.get_time() - time_t3) > 2:
            songs = ["~/_6.mp3","~/hello.mp3","~/hello_2.mp3"]
            song_num = random.randint(0,len(songs)-1)
            start_play = 1
            str_play = songs[song_num]
            pub_audio.publish(str_play)
            speach_flag = 0

    elif condition == 0 and max_countur_area > CONDITION_AREA:

        if speach_flag == 0:
            time_t3 = rospy.get_time()
            speach_flag = 1
        if start_play_1 == 0 and (rospy.get_time() - time_t3) > 2:
            songs = "~/hand_shake.mp3"
            start_play_1 = 1
            str_play = songs
            pub_audio.publish(str_play)
            speach_flag = 0

    elif condition != 0 and condition != 1 and max_countur_area > CONDITION_AREA:
        if start_play == 1:
            start_play = 0
            str_stop = "~/__.mp3"
            pub_audio.publish(str_stop)

        if start_play_1 == 1:
            start_play_1 = 0
            str_stop = "~/__.mp3"
            pub_audio.publish(str_stop)

    if (rospy.get_time() - time_t) >= 0.2:
        time_t = rospy.get_time()
        p = Int32MultiArray()
        p.data = [0]*4

        p.data[0] = people # флаг на обнаружение
        p.data[1] = point_x
        p.data[2] = point_y
        p.data[3] = condition # уровень взаимодействия
        
        eye_publisher.publish(p)

    count_pub.publish(bridge.cv2_to_imgmsg(drawing, 'bgr8'))
    cv.waitKey(3)



if __name__ == "__main__":

    rospy.init_node('image_converter', anonymous=True)
    image_sub = rospy.Subscriber("/camera/depth/image", Image, tracking)
    pub_audio = rospy.Publisher('/audio_file_player/play', String, queue_size=10)
    rospy.spin()